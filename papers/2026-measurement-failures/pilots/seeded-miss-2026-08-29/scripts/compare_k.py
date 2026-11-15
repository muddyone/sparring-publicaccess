#!/usr/bin/env python3
"""Compare two scoring passes of the SAME generator runs at different replicate counts.

The point is not which k gives a nicer number. It is HOW MUCH THE NUMBER MOVES when only
the judging replication changes -- the noise floor every other figure in the study has to
be read against (result.md sec.5).

Reports three things:
  1. aggregate drift per stratum -- what a reader of the headline would see
  2. run-level agreement -- what fraction of individual verdicts flip
  3. per-case drift -- whether the movement is diffuse or concentrated in a few cases

Usage:
  ./compare_k.py --a attic/scored.k2.json --b runs/scored.json --label-a k=2 --label-b k=4
"""
import argparse, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))

FIELDS = [("raw_recovery", "raw"), ("offkey_recovery", "off-key"),
          ("partial_recovery", "partial"), ("absorbed_only", "absorbed")]


def load(p):
    return json.load(open(p))["rows"]


def f(v):
    return statistics.mean(v) if v else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--label-a", default="A")
    ap.add_argument("--label-b", default="B")
    a = ap.parse_args()

    A, B = load(a.a), load(a.b)
    leak = json.load(open(os.path.join(CORPUS, "leakage.json")))["leakage"]
    cases = json.load(open(os.path.join(CORPUS, "cases.json")))["cases"]
    gated = {c for c, v in leak.items() if not v.get("raisable", True)}

    # Compare only runs BOTH passes scored, and apply the same gate to both, so the
    # difference is the replicate count and nothing else.
    shared = [r for r in sorted(set(A) & set(B))
              if A[r]["cluster_id"] not in gated]
    print(f"{a.label_a}: {len(A)} rows   {a.label_b}: {len(B)} rows   "
          f"compared (shared, ungated): {len(shared)}\n")
    if not shared:
        sys.exit("no shared rows")

    def stratum(rid):
        return leak.get(A[rid]["cluster_id"], {}).get("stratum", "unknown")

    print("AGGREGATE DRIFT — what a reader of the headline sees")
    print(f"  {'stratum':<10}{'n':>5}  " +
          "  ".join(f"{lbl:>22}" for _, lbl in FIELDS))
    for st in ("neutral", "hinted", "explicit", "ALL"):
        sub = [r for r in shared if st == "ALL" or stratum(r) == st]
        if not sub:
            continue
        cells = []
        for key, _ in FIELDS:
            va = f([A[r].get(key) for r in sub if A[r].get(key) is not None])
            vb = f([B[r].get(key) for r in sub if B[r].get(key) is not None])
            cells.append(f"{va:.2f} -> {vb:.2f} ({vb-va:+.2f})".rjust(22))
        print(f"  {st:<10}{len(sub):>5}  " + "  ".join(cells))

    print("\nRUN-LEVEL AGREEMENT — how often an individual verdict flips")
    for key, lbl in FIELDS:
        both = [r for r in shared
                if A[r].get(key) is not None and B[r].get(key) is not None]
        if not both:
            continue
        agree = [bool(A[r][key]) == bool(B[r][key]) for r in both]
        print(f"  {lbl:<10} {f(agree):.2f}  ({sum(agree)}/{len(agree)} runs unchanged)")

    print("\nPER-CASE DRIFT in off-key — is the movement diffuse or concentrated?")
    by = {}
    for r in shared:
        by.setdefault(A[r]["cluster_id"], []).append(r)
    rows = []
    for cid, rs in by.items():
        va = f([A[r]["offkey_recovery"] for r in rs])
        vb = f([B[r]["offkey_recovery"] for r in rs])
        rows.append((abs(vb - va), cid, va, vb, stratum(rs[0])))
    rows.sort(reverse=True)
    moved = [r for r in rows if r[0] > 0.01]
    print(f"  {len(moved)} of {len(rows)} cases moved at all; "
          f"{sum(1 for r in rows if r[0] >= 0.5)} moved by >=0.50")
    for d, cid, va, vb, st in rows[:8]:
        if d <= 0.01:
            break
        print(f"    {cases[cid]['case_name'][:34]:<34} [{st:<8}] "
              f"{va:.2f} -> {vb:.2f} ({vb-va:+.2f})")

    print("\nREADING: aggregate drift is the noise floor for every headline figure here.")
    print("Run-level agreement below ~0.90 means individual verdicts are not reproducible,")
    print("even where the aggregate looks stable — the two can differ sharply.")


if __name__ == "__main__":
    main()
