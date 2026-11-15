#!/usr/bin/env python3
"""What separates cases the off-key measure recovers from cases it does not?

Motivation: per-case off-key recovery is near-bimodal (cases sit at ~0 or ~1, rarely in
between), and variance_budget.py shows case sampling dominating the study's noise. If some
observable feature predicted which cases recover, corpus expansion could be TARGETED --
and the bimodality would mean "some cases are harder", which is a finding about generators.

On the 33-case corpus it did not: every measured feature was near-identical between the
high- and low-recovery groups, INCLUDING raw recovery (1.00 vs 0.97). On the 47-case corpus
that no longer holds -- raw recovery is 0.99 vs 0.86 (25 high vs 11 low), and the off-key pool
and situation length differ by about a fifth. Both comparisons are underpowered. So the
split is a property of each case's key-versus-seed geometry, not of case difficulty, and
it is not forecastable from anything visible before scoring.

Two consequences: expansion must be brute-force rather than targeted, and the variance
genuinely lives at case level (runs within a case agree ~0.90), so more cases -- not more
replicates -- is the lever.

Weak comparison by construction (33-case corpus: 8 low vs 20 high; 47-case: 11 vs 25). Read the columns as "nothing stands
out", never as effects.

Usage:  ./case_profile.py [--scored runs/scored.json]
"""
import argparse, collections, json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))

FEATURES = [("emitted", "items emitted"), ("offkey_pool", "off-key pool size"),
            ("keysize", "key points"), ("recall", "recall"),
            ("sit", "situation chars"), ("seedlen", "seed length"),
            ("raw", "raw recovery")]


def main():
    ap = argparse.ArgumentParser()
    # Default is the LIVE scoring. This defaulted to ../attic/scored.k2.json -- an archived
    # snapshot -- which is catalogue entry 19's exact defect: run bare after the corpus grew, it
    # profiled a superseded corpus in the correct format and never named the file. variance_budget.py
    # got this fix on 2026-08-30; this sibling did not, and the Measurement paper carried a stale
    # "matched on raw recovery (1.00 vs 0.97)" for two weeks because of it (panel finding V1).
    ap.add_argument("--scored", default=os.path.join(HERE, "..", "runs", "scored.json"))
    ap.add_argument("--hi", type=float, default=0.75)
    ap.add_argument("--lo", type=float, default=0.25)
    a = ap.parse_args()

    # Name every input BEFORE loading anything, so a stale or wrong path is visible in the first
    # line of output -- entry 19's transferable fix.
    print("inputs read:")
    print(f"  scored    {os.path.abspath(a.scored)}")
    print(f"  cases     {os.path.join(CORPUS, 'cases.json')}")
    print(f"  leakage   {os.path.join(CORPUS, 'leakage.json')}\n")

    rows = json.load(open(a.scored))["rows"]
    cases = json.load(open(os.path.join(CORPUS, "cases.json")))["cases"]
    leak = json.load(open(os.path.join(CORPUS, "leakage.json")))["leakage"]
    gated = {c for c, v in leak.items() if not v.get("raisable", True)}

    by = collections.defaultdict(list)
    for r in rows.values():
        if r["cluster_id"] not in gated:
            by[r["cluster_id"]].append(r)

    recs = []
    for cid, rs in by.items():
        c = cases[cid]
        recs.append(dict(
            cid=cid, name=c["case_name"][:30],
            st=leak.get(cid, {}).get("stratum", "?"),
            offkey=statistics.mean(r["offkey_recovery"] for r in rs),
            raw=statistics.mean(r["raw_recovery"] for r in rs),
            emitted=statistics.mean(r["emitted"] for r in rs),
            offkey_pool=statistics.mean(r["offkey"] for r in rs),
            keysize=len(c["key"]),
            recall=statistics.mean(r["recall"] for r in rs),
            sit=len(c["situation"]), seedlen=len(c["seed"]["consideration"])))

    hi = [r for r in recs if r["offkey"] >= a.hi]
    lo = [r for r in recs if r["offkey"] <= a.lo]
    print(f"{len(recs)} ungated cases   high (>={a.hi}): {len(hi)}   low (<={a.lo}): {len(lo)}\n")
    print(f"  {'feature':<22}{'high':>10}{'low':>10}{'ratio':>9}")
    for k, lab in FEATURES:
        x = statistics.mean(r[k] for r in hi)
        y = statistics.mean(r[k] for r in lo)
        print(f"  {lab:<22}{x:>10.2f}{y:>10.2f}{(x/y if y else float('nan')):>9.2f}")

    print("\n  stratum mix   high:", dict(collections.Counter(r["st"] for r in hi)),
          "  low:", dict(collections.Counter(r["st"] for r in lo)))
    print("\n  low-recovery cases (note the raw column -- they DID raise the seed):")
    for r in sorted(lo, key=lambda x: x["offkey"]):
        print(f"    {r['name']:<30} [{r['st']:<8}] offkey {r['offkey']:.2f} "
              f"raw {r['raw']:.2f}  key {r['keysize']}  recall {r['recall']:.2f}")


if __name__ == "__main__":
    main()
