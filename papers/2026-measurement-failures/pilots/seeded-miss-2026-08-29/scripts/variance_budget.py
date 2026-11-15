#!/usr/bin/env python3
"""Where does the wobble in the headline actually come from?

The study documents a ~5-point noise floor but has never said WHICH knob it is on. Two
candidates, and they imply opposite next steps:

  CASE SAMPLING  the clean stratum holds ~9 cases. Which cases happen to land in it is a
                 draw, and a draw of 9 is a small one. Fix by adding cases.
  JUDGE SAMPLING the per-run verdicts come from k stochastic replicates. Fix by raising k.

Estimates both from data already on disk, with no model calls:

  case variance   nonparametric bootstrap over CASES (resample cases with replacement,
                  keep each case's runs together -- runs within a case are not independent)
  judge variance  observed flip rate between two independent scorings of the SAME runs,
                  propagated to the stratum mean

Every input path is printed before anything is loaded -- see catalogue entry 19, where this
tool reported a superseded corpus in the correct format and named no file.

Usage:
  ./variance_budget.py [--stratum neutral] [--boot 20000] [--scored PATH] [--scored-b PATH]
"""
import argparse, json, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))
RUNS = os.path.abspath(os.path.join(HERE, "..", "runs"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stratum", default="neutral")
    ap.add_argument("--boot", type=int, default=20000)
    ap.add_argument("--scored", default=os.path.join(RUNS, "scored.json"))
    # No default: the judge term needs a SECOND INDEPENDENT scoring of the same runs, and
    # there is no live one. Defaulting it to an archived scoring silently pairs the current
    # corpus against superseded, differently-configured rows -- entry 19's failure with an
    # extra step. Pass it explicitly when a real second scoring exists.
    ap.add_argument("--scored-b", default=None)
    ap.add_argument("--field", default="offkey_recovery")
    ap.add_argument("--seed", type=int, default=20260829)
    a = ap.parse_args()

    leak_path = os.path.realpath(os.path.join(CORPUS, "leakage.json"))
    scored_path = os.path.realpath(a.scored)
    scored_b_path = os.path.realpath(a.scored_b) if a.scored_b else None

    # Catalogue entry 19: this tool once analysed an archived snapshot without complaint,
    # in the correct format, because it never named the file it read. Inputs are echoed
    # BEFORE anything is loaded, so a crash still shows what was reached for.
    print("inputs read:")
    print(f"  leakage   {leak_path}")
    print(f"  scored    {scored_path}")
    print(f"  scored-b  {scored_b_path or '(none -- judge term skipped)'}")
    print()

    leak = json.load(open(leak_path))["leakage"]
    gated = {c for c, v in leak.items() if not v.get("raisable", True)}
    A = json.load(open(scored_path))["rows"]

    by_case = {}
    for rid, r in A.items():
        cid = r["cluster_id"]
        if cid in gated:
            continue
        if leak.get(cid, {}).get("stratum") != a.stratum:
            continue
        by_case.setdefault(cid, []).append(r[a.field])
    cases = sorted(by_case)
    if len(cases) < 3:
        sys.exit(f"only {len(cases)} cases in stratum {a.stratum}")

    per_case = {c: statistics.mean(v) for c, v in by_case.items()}
    point = statistics.mean([x for c in cases for x in by_case[c]])
    n_runs = sum(len(by_case[c]) for c in cases)
    print(f"stratum {a.stratum!r}   {len(cases)} cases, {n_runs} runs   "
          f"{a.field} = {point:.3f}\n")
    print("per-case values: " + ", ".join(f"{per_case[c]:.2f}" for c in cases))

    # ---- case-sampling variance: bootstrap over cases, runs kept with their case
    rng = random.Random(a.seed)
    boots = []
    for _ in range(a.boot):
        pick = [rng.choice(cases) for _ in cases]
        vals = [x for c in pick for x in by_case[c]]
        boots.append(statistics.mean(vals))
    boots.sort()
    lo, hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]
    case_sd = statistics.pstdev(boots)
    print(f"\nCASE SAMPLING (bootstrap over {len(cases)} cases, {a.boot} draws)")
    print(f"  sd {case_sd:.3f}   95% interval [{lo:.2f}, {hi:.2f}]   width {hi-lo:.2f}")

    # ---- judge-sampling variance: observed flip rate between two independent scorings
    if not scored_b_path:
        print("\n(no second scoring given -- pass --scored-b to estimate the judge term)")
        return
    try:
        B = json.load(open(scored_b_path))["rows"]
    except OSError:
        print("\n(no second scoring available for the judge estimate)")
        return
    shared = [rid for rid in A
              if rid in B and A[rid]["cluster_id"] in by_case]
    if not shared:
        print("\n(no shared rows in this stratum for the judge estimate)")
        return
    flips = [bool(A[r][a.field]) != bool(B[r][a.field]) for r in shared]
    p = statistics.mean(flips)
    # A flip moves one run by 1.0, so the mean moves by 1/n per flip. Treating flips as
    # independent Bernoulli(p) across n runs gives the sd of the stratum mean.
    judge_sd = (p * (1 - p) / len(shared)) ** 0.5 if 0 < p < 1 else 0.0
    print(f"\nJUDGE SAMPLING (two independent scorings of {len(shared)} shared runs)")
    print(f"  per-run flip rate {p:.3f}   implied sd of the stratum mean {judge_sd:.3f}")

    print("\n" + "=" * 66)
    if case_sd > 2 * judge_sd:
        verdict = ("CASE SAMPLING DOMINATES — adding cases buys more than adding "
                   "replicates")
    elif judge_sd > 2 * case_sd:
        verdict = ("JUDGE SAMPLING DOMINATES — raising k buys more than adding cases")
    else:
        verdict = "COMPARABLE — neither knob alone fixes the wobble"
    print(f"case sd {case_sd:.3f}  vs  judge sd {judge_sd:.3f}   ->  {verdict}")
    print("=" * 66)
    print("Caveat: the judge term is estimated from ONE pair of scorings, so it is itself")
    print("a noisy estimate. The case term assumes cases are exchangeable draws from the")
    print("corpus, which selection effects (design-note 4.2) make only approximately true.")


if __name__ == "__main__":
    main()
