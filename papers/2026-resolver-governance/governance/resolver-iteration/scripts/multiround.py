#!/usr/bin/env python3
"""Multi-round test — the actual "iterate vs single challenge" question (EXPLORATORY).

The paper covers ONE challenge (R0->R1). The open Phase-4 question: does iterating PAST it help,
plateau, or over-correct? Continues each of the 12 natural problems R0->R1->R2->R3 (cross-vendor GPT
challenger tracking handles across rounds, Claude reviser), then measures each STEP with pairwise:
  B_BETTER = the newer round is better (improvement)
  EQUIVALENT = plateau (no material change)
  A_BETTER = the newer round is WORSE (over-correction / degradation)

Key reads:
  * step distribution R0->R1 vs R1->R2 vs R2->R3: if improvement concentrates in round 1 and later
    steps go EQUIVALENT, the single challenge does most of the work (diminishing returns).
  * any A_BETTER in later steps = over-correction (iteration actively hurts).
  * R1->R3: does 3 rounds beat single-challenge R1 at all?
  * challenger convergence: rounds until material_objections_remaining=False.

No human gold exists (ruled out); trust rests on cross-vendor-robust pairwise (Claude here; the
verdict was shown vendor-robust at 10/12 on R0->R1). Reuses run_study's round-N prompts + the cached
natural R0/R1. Resumable.

Usage: python3 multiround.py [--k 3]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
from resolver_loop import pairwise_verdict

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "multiround.json"


def iterate(pair):
    """Continue R1 -> R2 -> R3 with cross-vendor round-N challenge + Claude revise."""
    pid, problem = pair["id"], pair["problem"]
    outs = {"R0": pair["R0"], "R1": pair["R1"]}
    r1chal = R.load(f"nat_chal__{pid}") or {}
    conv = [{"round": 1, "n_obj": pair.get("n_objections"),
             "material_remaining": pair.get("material_remaining"), "accept": pair.get("accept_as_final")}]
    prev_obj = r1chal.get("objections", [])
    current = pair["R1"]
    for n in (2, 3):
        cu = f"mr_chal__{pid}__r{n}"
        chal = R.load(cu)
        if not chal:
            chal = R.challenger_call("gpt", R.CHAL_SYS,
                                     R.CHAL_RN_USER.format(problem=problem, rec=current,
                                                           prev=R.fmt_objections(prev_obj)))
            R.save(cu, chal)
        objs = chal.get("objections", []) if isinstance(chal, dict) else []
        ru = f"mr_rev__{pid}__r{n}"
        rev = R.load(ru)
        if not rev:
            rev = L.claude_json(R.CLAUDE, R.PROD_SYS,
                                R.PROD_USER.format(problem=problem, rec=current, obj=R.fmt_objections(objs)),
                                max_tokens=6000, temperature=0.7)
            R.save(ru, rev)
        current = (rev.get("revised_recommendation", "") if isinstance(rev, dict) else "") or current
        outs[f"R{n}"] = current
        conv.append({"round": n, "n_obj": len(objs),
                     "material_remaining": chal.get("material_objections_remaining"),
                     "accept": rev.get("accept_as_final")})
        prev_obj = objs
    return {"id": pid, "domain": pair["domain"], "problem": problem, "outs": outs, "convergence": conv}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()
    k = args.k
    pairs = json.loads(CORPUS.read_text())["problems"]
    print(f"[mr] {len(pairs)} problems; rounds R0..R3; k={k}", flush=True)

    # 1. produce R2, R3 (per-problem sequential; problems concurrent)
    built = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(iterate, p): p["id"] for p in pairs}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); built[r["id"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[mr] iterate ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
    print(f"[mr] built {len(built)} trajectories; scoring steps...", flush=True)

    # 2. pairwise each step (older=A, newer=B => B_BETTER = improvement)
    STEPS = [("R0", "R1"), ("R1", "R2"), ("R2", "R3"), ("R1", "R3")]

    def score(rec):
        o = rec["outs"]
        res = {}
        for a, b in STEPS:
            if a in o and b in o:
                res[f"{a}->{b}"] = pairwise_verdict(rec["problem"], o[a], o[b], f"mrpw__{rec['id']}__{a}{b}", k)
        return res
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        scored = dict(zip(built.keys(), ex.map(lambda pid: score(built[pid]), built.keys())))

    # 3. assemble
    label = {"B_BETTER": "improved", "EQUIVALENT": "plateau", "A_BETTER": "DEGRADED"}
    step_dist = {f"{a}->{b}": collections.Counter() for a, b in STEPS}
    rows = []
    for pid, rec in built.items():
        s = scored[pid]
        for stp, v in s.items():
            step_dist[stp][label[v]] += 1
        conv = rec["convergence"]
        # first round where challenger reports no material objections remaining
        conv_round = next((c["round"] for c in conv if c["material_remaining"] is False), None)
        rows.append({"id": pid, "domain": rec["domain"],
                     "steps": {stp: label[v] for stp, v in s.items()},
                     "n_obj_by_round": [c["n_obj"] for c in conv],
                     "material_remaining_by_round": [c["material_remaining"] for c in conv],
                     "converged_round": conv_round})

    summary = {"EXPLORATORY": True, "k": k, "n": len(rows),
               "step_distribution": {stp: dict(c) for stp, c in step_dist.items()},
               "rows": rows, "trajectories": {pid: built[pid]["outs"] for pid in built}}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== MULTI-ROUND: does iterating past the single challenge help? ===")
    print("  step distribution (improved / plateau / DEGRADED):")
    for stp in ["R0->R1", "R1->R2", "R2->R3", "R1->R3"]:
        c = step_dist[stp]
        print(f"    {stp:9s}: improved={c['improved']:2d}  plateau={c['plateau']:2d}  DEGRADED={c['DEGRADED']:2d}")
    # convergence
    convs = [r["converged_round"] for r in rows if r["converged_round"]]
    print(f"\n  challenger 'no material objections remaining' reached: {len(convs)}/{len(rows)} problems"
          + (f" (rounds: {collections.Counter(convs)})" if convs else ""))
    print(f"\n  {'id':22s} {'R0->R1':9s} {'R1->R2':9s} {'R2->R3':9s} {'R1->R3':9s} obj/round")
    for r in rows:
        s = r["steps"]
        print(f"  {r['id']:22s} {s.get('R0->R1',''):9s} {s.get('R1->R2',''):9s} "
              f"{s.get('R2->R3',''):9s} {s.get('R1->R3',''):9s} {r['n_obj_by_round']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
