#!/usr/bin/env python3
"""Re-score the multi-round trajectories with the ANTI-BIAS judge + decision-stability (EXPLORATORY).

The instrument-first step: hold the ALREADY-GENERATED R0->R1->R2->R3 trajectories FIXED and change only
the measurement. Isolates how much of the multi-round "always improved" treadmill is JUDGE change-bias
vs real process churn.

  * Re-score every step (R0->R1, R1->R2, R2->R3, R1->R3) with pairwise_cf (the counter-framed anti-bias
    + length-normalization judge, validated on the constructed set) instead of the plain pro-change judge.
      - If "always improved" collapses to improved-then-EQUIVALENT -> much of the treadmill was JUDGE bias;
        convergence is measurable once debiased ("unmeasurable" takes a hit).
      - If it STILL shows always-improved -> the trajectories really keep changing substantively -> the
        never-converging CHALLENGER is the culprit -> prompt-craft is the next lever.
  * DECISION-STABILITY (bias-free governance metric): extract the option each round SELECTS and track
    whether the core decision flips or holds across rounds. A decision that stabilizes and survives further
    challenge is a defensible trust signal that does NOT depend on the pairwise correctness delta.

No new trajectory generation. Reuses cached R0..R3 from multiround.json. Resumable.

Usage: python3 rescore_debiased.py [--k 3]
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import pairwise_dv_probe as P
from resolver_loop import _flip, _map
from ruler_bakeoff import CF_SYS   # counter-framed anti-bias pairwise system prompt

MR = R.PILOT / "analysis" / "multiround.json"
OUT_JSON = R.PILOT / "analysis" / "rescore-debiased.json"
STEPS = [("R0", "R1"), ("R1", "R2"), ("R2", "R3"), ("R1", "R3")]

DECISION_SYS = (
    "You identify the single option a recommendation SELECTS as its final choice. Recommendations discuss "
    "several options but commit to one. Return only that one option's label, exactly as the text labels it "
    "(e.g. a, b, c). If it truly commits to none, return 'none'."
)
DECISION_USER = ("RECOMMENDATION:\n{rec}\n\nReturn JSON: {{\"choice\": str}} — the single option it SELECTS.")


def cf_verdict(problem, A, B, tag, k):
    votes = []
    for j in range(1, k + 1):
        uid = f"loop_pwcf__{tag}__rep{j}"
        rec = R.load(uid)
        if not rec:
            a_in_A = _flip(tag, j)
            slotA, slotB = (A, B) if a_in_A else (B, A)
            out = L.claude_json(R.CLAUDE, CF_SYS, P.PAIR_JUDGE_USER.format(problem=problem, a=slotA, b=slotB),
                                max_tokens=1200)
            raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
            rec = {"mapped": _map(raw, a_in_A)}
            R.save(uid, rec)
        votes.append(rec["mapped"])
    return collections.Counter(votes).most_common(1)[0][0]


def decision(pid, rnd, text):
    uid = f"decext__{pid}__{rnd}"
    rec = R.load(uid)
    if not rec:
        out = L.claude_json(R.CLAUDE, DECISION_SYS, DECISION_USER.format(rec=text), max_tokens=200)
        ch = (out.get("choice", "?") if isinstance(out, dict) else "?") or "?"
        rec = {"choice": str(ch).strip().lower()[:12]}
        R.save(uid, rec)
    return rec["choice"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()
    k = args.k

    mr = json.loads(MR.read_text())
    traj = mr["trajectories"]                 # {pid: {R0,R1,R2,R3}}
    probmap = {r["id"]: None for r in mr["rows"]}
    # recover problem text from natural-corpus (pairwise needs it)
    corpus = {p["id"]: p["problem"] for p in json.loads((R.PILOT / "analysis" / "natural-corpus.json").read_text())["problems"]}

    print(f"[rescore] {len(traj)} trajectories; anti-bias judge + decision-stability; k={k}", flush=True)

    # 1. CF re-score every step
    def score(pid):
        o = traj[pid]; prob = corpus[pid]
        return {f"{a}->{b}": cf_verdict(prob, o[a], o[b], f"pwcf__{pid}__{a}{b}", k)
                for a, b in STEPS if a in o and b in o}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        cf_scored = dict(zip(traj.keys(), ex.map(score, traj.keys())))

    # 2. decision extraction per round
    def decs(pid):
        return {rnd: decision(pid, rnd, traj[pid][rnd]) for rnd in ("R0", "R1", "R2", "R3") if rnd in traj[pid]}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        dec = dict(zip(traj.keys(), ex.map(decs, traj.keys())))

    label = {"B_BETTER": "improved", "EQUIVALENT": "plateau", "A_BETTER": "DEGRADED"}
    cf_dist = {f"{a}->{b}": collections.Counter() for a, b in STEPS}
    rows = []
    for pid in traj:
        s = cf_scored[pid]
        for stp, v in s.items():
            cf_dist[stp][label[v]] += 1
        seq = [dec[pid].get(r) for r in ("R0", "R1", "R2", "R3") if r in dec[pid]]
        flips = sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1])
        stabilized = None
        # round at which the decision reaches its final value and never changes again
        if seq:
            final = seq[-1]
            stabilized = next((i for i in range(len(seq)) if all(x == final for x in seq[i:])), None)
        rows.append({"id": pid, "cf_steps": {stp: label[v] for stp, v in s.items()},
                     "decision_seq": seq, "flips": flips, "stabilized_round": stabilized})

    plain = mr["step_distribution"]
    summary = {"EXPLORATORY": True, "k": k, "n": len(rows),
               "plain_step_distribution": plain,
               "cf_step_distribution": {stp: dict(c) for stp, c in cf_dist.items()},
               "rows": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== DEBIASED RE-SCORE (anti-bias judge) vs PLAIN — same trajectories ===")
    print(f"  {'step':9s} | {'PLAIN (impr/plat/DEGR)':24s} | {'CF anti-bias (impr/plat/DEGR)':28s}")
    for a, b in STEPS:
        stp = f"{a}->{b}"
        pc = plain[stp]; cc = cf_dist[stp]
        pstr = f"{pc.get('improved',0):2d}/{pc.get('plateau',0):2d}/{pc.get('DEGRADED',0):2d}"
        cstr = f"{cc.get('improved',0):2d}/{cc.get('plateau',0):2d}/{cc.get('DEGRADED',0):2d}"
        flag = "  <- collapses" if (cc.get('improved',0) < pc.get('improved',0) - 1) else ""
        print(f"  {stp:9s} | {pstr:24s} | {cstr:28s}{flag}")

    print("\n=== DECISION STABILITY (bias-free governance signal) ===")
    stab = [r for r in rows if r["stabilized_round"] is not None and r["stabilized_round"] <= 1]
    print(f"  decision stable by R1 (survives further rounds): {len(stab)}/{len(rows)}")
    print(f"  {'id':22s} {'R0->R1->R2->R3 decision':26s} flips")
    for r in rows:
        print(f"  {r['id']:22s} {(' -> '.join(map(str,r['decision_seq']))):26s} {r['flips']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
