#!/usr/bin/env python3
"""Step 1 — cross-vendor confirmation of the step-2 convergence (EXPLORATORY).

Step 2 showed convergence-pressured prompts fixed the decision churn: decision-stable-by-R1 went
4/12 -> 10/12, oscillation gone, R0->R1 correction preserved. But BOTH headline measurements were
Claude-authored:
  * decision extraction (which option each round SELECTS)  -> L.claude_json(DEC_SYS)
  * the anti-bias pairwise step verdict (improved/plateau/DEGRADED) -> L.claude_json(CF_SYS)
(The challenger in step 2 was already GPT; the producer is Claude. So what needs cross-vendor
confirmation is the SCORING, not the trajectory.)

This holds the step-2 trajectories FIXED (R0 from corpus; R1/R2/R3 from the cached s2_rev__* leaves)
and re-derives both measurements with GPT-5.2, to confirm the churn-fix is not a Claude-scoring artifact:
  1. GPT decision extraction per round -> GPT decision-stable-by-R1, and per-round Claude-vs-GPT
     AGREEMENT on the selected option (the vendor-robustness number).
  2. GPT pairwise (same anti-bias CF prompt, k reps, position-flip-debiased) per step -> GPT
     improved/plateau/DEGRADED distribution, compared to Claude's.

Confirmation criteria (pre-stated): GPT decision-stability within ~1 of Claude's 10/12; high per-round
decision agreement; GPT R0->R1 still overwhelmingly 'improved' (the real correction) with later steps
plateauing (no systematic degradation). Resumable; every unit cached under a distinct s1g* prefix.

Usage: python3 step1_xvendor.py [--k 3]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import pairwise_dv_probe as P
from resolver_loop import _flip, _map
from ruler_bakeoff import CF_SYS
from step2_convergence import DEC_SYS, DEC_USER

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
STEP2 = R.PILOT / "analysis" / "step2-convergence.json"
OUT_JSON = R.PILOT / "analysis" / "step1-xvendor.json"
STEPS = [("R0", "R1"), ("R1", "R2"), ("R2", "R3"), ("R1", "R3")]
ROUNDS = ("R0", "R1", "R2", "R3")


def trajectory(pid, R0):
    """Reconstruct the FIXED step-2 trajectory from cache (no regeneration)."""
    outs = {"R0": R0}
    for rnd in (1, 2, 3):
        v = R.load(f"s2_rev__{pid}__r{rnd}")
        outs[f"R{rnd}"] = (v.get("revised_recommendation", "") if v else "") or outs[f"R{rnd-1}"]
    return outs


def gpt_decision(pid, rnd, text):
    uid = f"s1gdec__{pid}__{rnd}"
    rec = R.load(uid)
    if not rec:
        out = L.gpt_json(R.GPT, DEC_SYS, DEC_USER.format(rec=text))
        ch = (out.get("choice", "?") if isinstance(out, dict) else "?") or "?"
        rec = {"choice": str(ch).strip().lower()[:12]}
        R.save(uid, rec)
    return rec["choice"]


def gpt_cf_verdict(problem, A, B, tag, k):
    """GPT pairwise anti-bias verdict, position-flip-debiased, majority of k reps."""
    votes = []
    for j in range(1, k + 1):
        uid = f"s1gpwcf__{tag}__rep{j}"
        rec = R.load(uid)
        if not rec:
            a_in_A = _flip(tag, j)
            slotA, slotB = (A, B) if a_in_A else (B, A)
            out = L.gpt_json(R.GPT, CF_SYS, P.PAIR_JUDGE_USER.format(problem=problem, a=slotA, b=slotB))
            raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
            rec = {"mapped": _map(raw, a_in_A)}
            R.save(uid, rec)
        votes.append(rec["mapped"])
    return collections.Counter(votes).most_common(1)[0][0]


def _stable_by_r1(seq):
    """round at which the decision reaches its final value and never changes again; stable-by-R1 = <=1."""
    if not seq:
        return None
    final = seq[-1]
    return next((i for i in range(len(seq)) if all(x == final for x in seq[i:])), None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()
    k = args.k

    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}
    s2 = json.loads(STEP2.read_text())
    claude_rows = {r["id"]: r for r in s2["rows"]}         # Claude decisions/steps to compare against

    traj = {pid: trajectory(pid, corpus[pid]["R0"]) for pid in corpus}
    print(f"[s1] cross-vendor re-score of {len(traj)} FIXED step-2 trajectories (GPT); k={k}", flush=True)

    def decs(pid):
        return {rnd: gpt_decision(pid, rnd, traj[pid][rnd]) for rnd in ROUNDS if rnd in traj[pid]}

    def score(pid):
        o = traj[pid]; prob = corpus[pid]["problem"]
        return {f"{a}->{b}": gpt_cf_verdict(prob, o[a], o[b], f"s1_{pid}__{a}{b}", k)
                for a, b in STEPS if a in o and b in o}

    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        gdec = dict(zip(traj.keys(), ex.map(decs, traj.keys())))
        gcf = dict(zip(traj.keys(), ex.map(score, traj.keys())))

    label = {"B_BETTER": "improved", "EQUIVALENT": "plateau", "A_BETTER": "DEGRADED"}
    gpt_dist = {f"{a}->{b}": collections.Counter() for a, b in STEPS}
    claude_dist = {f"{a}->{b}": collections.Counter() for a, b in STEPS}

    rows = []
    agree_hits = agree_tot = 0
    for pid in traj:
        gseq = [gdec[pid].get(r) for r in ROUNDS if r in gdec[pid]]
        cseq = claude_rows[pid]["decision_seq"]
        # per-round agreement (same selected option label), position-aligned
        per_round = []
        for i, r in enumerate(ROUNDS):
            if i < len(gseq) and i < len(cseq):
                a = (gseq[i] == cseq[i]); per_round.append(a)
                agree_hits += int(a); agree_tot += 1
        g_flips = sum(1 for i in range(1, len(gseq)) if gseq[i] != gseq[i - 1])
        g_stab = _stable_by_r1(gseq)
        for stp, v in gcf[pid].items():
            gpt_dist[stp][label[v]] += 1
        for stp, v in claude_rows[pid]["cf_steps"].items():
            claude_dist[stp][v] += 1
        rows.append({"id": pid,
                     "gpt_decision_seq": gseq, "claude_decision_seq": cseq,
                     "per_round_agree": per_round, "gpt_flips": g_flips, "gpt_stabilized_round": g_stab,
                     "claude_stabilized_round": claude_rows[pid]["stabilized_round"],
                     "gpt_cf_steps": {stp: label[v] for stp, v in gcf[pid].items()},
                     "claude_cf_steps": claude_rows[pid]["cf_steps"]})

    gpt_stable = sum(1 for r in rows if r["gpt_stabilized_round"] is not None and r["gpt_stabilized_round"] <= 1)
    claude_stable = sum(1 for r in rows if r["claude_stabilized_round"] is not None and r["claude_stabilized_round"] <= 1)
    agree_pct = round(100 * agree_hits / agree_tot, 1) if agree_tot else None
    # decision-stability itself as a per-problem cross-vendor concordance (both agree stable/not)
    concord = sum(1 for r in rows
                  if (r["gpt_stabilized_round"] is not None and r["gpt_stabilized_round"] <= 1)
                  == (r["claude_stabilized_round"] is not None and r["claude_stabilized_round"] <= 1))

    summary = {
        "EXPLORATORY": True, "k": k, "n": len(rows),
        "decision_stable_by_R1": {"claude": f"{claude_stable}/{len(rows)}", "gpt": f"{gpt_stable}/{len(rows)}"},
        "per_round_decision_agreement": {"hits": agree_hits, "total": agree_tot, "pct": agree_pct},
        "decision_stability_concordance": f"{concord}/{len(rows)}",
        "cf_step_distribution": {
            "claude": {stp: dict(c) for stp, c in claude_dist.items()},
            "gpt": {stp: dict(c) for stp, c in gpt_dist.items()},
        },
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== STEP 1 — CROSS-VENDOR CONFIRMATION (GPT re-score of fixed step-2 trajectories) ===")
    print(f"  DECISION STABLE BY R1:   Claude {claude_stable}/{len(rows)}   ->   GPT {gpt_stable}/{len(rows)}")
    print(f"  per-round decision agreement (same option picked): {agree_hits}/{agree_tot}  ({agree_pct}%)")
    print(f"  per-problem stability concordance (both call it stable/unstable): {concord}/{len(rows)}")
    print("\n  CF STEP DISTRIBUTION (improved/plateau/DEGRADED) — Claude vs GPT:")
    print(f"  {'step':9s} | {'Claude':16s} | {'GPT':16s}")
    for a, b in STEPS:
        stp = f"{a}->{b}"
        cc = claude_dist[stp]; gc = gpt_dist[stp]
        cs = f"{cc.get('improved',0):2d}/{cc.get('plateau',0):2d}/{cc.get('DEGRADED',0):2d}"
        gs = f"{gc.get('improved',0):2d}/{gc.get('plateau',0):2d}/{gc.get('DEGRADED',0):2d}"
        print(f"  {stp:9s} | {cs:16s} | {gs:16s}")
    print(f"\n  {'id':22s} {'GPT decisions':22s} {'Claude decisions':22s} agree")
    for r in rows:
        g = " -> ".join(map(str, r["gpt_decision_seq"]))
        c = " -> ".join(map(str, r["claude_decision_seq"]))
        a = "".join("Y" if x else "." for x in r["per_round_agree"])
        print(f"  {r['id']:22s} {g:22s} {c:22s} {a}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
