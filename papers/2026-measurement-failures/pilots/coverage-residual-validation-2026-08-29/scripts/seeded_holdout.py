#!/usr/bin/env python3
"""Validate the off-key measure by hiding key points from it.

THE PROBLEM THIS SOLVES.

  Off-key discovery -- items a blind judge calls sound, raised and material that match no
  key point -- is the only measure in this study that looks at ungraded material, which is
  the coverage question. It reached 0.49 for the structured walk on Secured Transactions.

  It is also the one number nothing can check. The positive control validates the judge
  against a human answer, and off-key is BY DEFINITION outside the region where that answer
  exists. The control vouches for the judge exactly where it is not needed and goes silent
  exactly where it is (implications-for-the-proposer-paper.md §3).

THE DESIGN.

  Seeds cannot be authored here. Writing them myself makes them model-generated and
  circular; no domain expert is available (standing constraint). So the seeds are the
  examiners' OWN key points, held out of the scoring key one at a time.

  A held-out point is an ideal seed for three reasons:
    - it is known-material -- the examiners assigned it a percentage weight;
    - it is outside the scoring key BY CONSTRUCTION, so it must surface as off-key or not
      at all;
    - it is human-authored and predates this system, so nothing about it is circular.

  Leave-ONE-out across every point, so nothing is cherry-picked: with a 6-point key that is
  6 conditions per run, using every point exactly once as the seed.

WHAT IS MEASURED.

  recovery = of the (held-out point, run) cases, in how many does the off-key set contain
             an item that addresses the held-out point?

  high -> off-key reliably surfaces known-material content absent from the scoring key.
          The measure is validated for material-recovery, and the 0.49 becomes readable.
  low  -> off-key misses content the examiners themselves called material. Its rate is
          then not evidence of coverage, and the coverage line has no working instrument.

  Honest bound, stated up front: held-out key points are MAINSTREAM -- an examiner graded
  them. This validates that off-key can recover *material* items. It does NOT establish
  sensitivity to genuinely obscure ones, which would need seeds from outside the model
  ecosystem and outside the key.

No extra model calls beyond one matching pass and one audit pass per run -- the leave-one-out
arithmetic is done on their output.

Usage:
  ./seeded_holdout.py --admin "July 2020" --subject "Secured Transactions" --rungs g1,g3,g4
"""
import argparse, glob, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))

from score_pair import pass_a, pass_b, majority, norm_id, GPT, CLAUDE  # noqa: E402


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def analyse(run, fact, k, match_model, audit_model):
    items = [i["label"] for i in run["raw"]["issues"]]
    gold = run["gold"]["gold"]
    if not items:
        return None
    A = pass_a(items, gold, k, match_model)
    B = pass_b(items, fact, k, audit_model)

    # Which items did the matcher cite for each key point? (majority across replicates)
    cite = {}
    for g in gold:
        kid = norm_id(g["point_id"])
        counts = {}
        for rep in A:
            m = rep.get(kid)
            if m and m["covered"]:
                for i in m["by"]:
                    counts[i] = counts.get(i, 0) + 1
        cite[g["point_id"]] = {i for i, c in counts.items() if c * 2 >= len(A)}

    signal = set()
    for i in range(len(items)):
        s, _ = majority(B, i, "sound")
        r, _ = majority(B, i, "raised")
        m, _ = majority(B, i, "material")
        dup = sum(1 for rep in B
                  if i in rep and rep[i].get("duplicate_of") is not None) * 2 >= len(B)
        if s and r and m and not dup:
            signal.add(i)

    # Leave-one-out: hide point p, rebuild the off-key set against the remaining points,
    # and ask whether anything in it addresses p.
    rows = []
    for g in gold:
        p = g["point_id"]
        matched_reduced = set().union(*[cite[q["point_id"]] for q in gold
                                        if q["point_id"] != p]) if len(gold) > 1 else set()
        offkey = signal - matched_reduced
        recovered = bool(offkey & cite[p])
        rows.append({"point": p, "weight": g["weight_pct"],
                     "n_offkey": len(offkey), "recovered": recovered,
                     "cited_by_any": bool(cite[p])})
    return {"items": len(items), "signal": len(signal), "rows": rows}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admin", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--rungs", default="g1,g3,g4")
    ap.add_argument("-k", type=int, default=2)
    ap.add_argument("--match-model", default=GPT)
    ap.add_argument("--audit-model", default=CLAUDE)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    q = next(x for x in qs if x["administration"] == a.admin and x["subject"] == a.subject)
    base = f"{slug(a.admin)}-{slug(a.subject)}"

    print(f"fact pattern : {a.admin} / {a.subject}")
    print(f"design       : leave-one-out over every key point; the held-out point is the seed")
    print(f"judge        : {a.audit_model} (blind to the key)   matcher {a.match_model}   k={a.k}\n")

    results, all_rows = {}, []
    for rung in a.rungs.split(","):
        paths = [p for p in sorted(glob.glob(os.path.join(HERE, "..", "runs",
                                                          f"{base}.{rung}.r*.json")))
                 if "raw" in json.load(open(p))]
        if not paths:
            print(f"  {rung}: no runs -- skipped")
            continue
        rung_rows = []
        for p in paths:
            r = analyse(json.load(open(p)), q["text"], a.k, a.match_model, a.audit_model)
            if r:
                for row in r["rows"]:
                    row["rung"] = rung
                rung_rows.extend(r["rows"])
        if not rung_rows:
            continue
        rec = [r["recovered"] for r in rung_rows if r["cited_by_any"]]
        never = [r for r in rung_rows if not r["cited_by_any"]]
        results[rung] = {
            "cases": len(rung_rows),
            "cases_the_run_could_recover": len(rec),
            "recovery": statistics.mean(rec) if rec else float("nan"),
            "never_found_at_all": len(never),
            "mean_offkey_pool": statistics.mean(r["n_offkey"] for r in rung_rows)}
        all_rows.extend(rung_rows)
        z = results[rung]
        print(f"  {rung:<4} {z['cases']:>3} cases   recovery {z['recovery']:>5.2f}"
              f"   (of {z['cases_the_run_could_recover']} the run actually raised;"
              f" {z['never_found_at_all']} it never raised at all)")

    print("\n" + "=" * 72)
    over = [r["recovered"] for r in all_rows if r["cited_by_any"]]
    print(f"OVERALL RECOVERY: {statistics.mean(over):.2f}"
          f"  ({sum(over)}/{len(over)} held-out points recovered as off-key)")
    print("=" * 72)
    print("Reads: when a run DID raise a point, and that point was hidden from the scoring")
    print("key, how often did it show up in the off-key set instead of vanishing?")
    print("  high -> off-key reliably surfaces known-material ungraded content")
    print("  low  -> off-key loses content the examiners themselves weighted")

    byw = {}
    for r in all_rows:
        if r["cited_by_any"]:
            byw.setdefault(r["weight"], []).append(r["recovered"])
    print("\nrecovery by the examiners' weight on the held-out point:")
    for w in sorted(byw):
        v = byw[w]
        print(f"   {w:>3}%  {statistics.mean(v):>5.2f}   (n={len(v)})")

    out = a.out or os.path.join(HERE, "..", "runs", f"{base}.seeded-holdout.json")
    json.dump({"fact_pattern": f"{a.admin} / {a.subject}", "design": "leave-one-out holdout",
               "k": a.k, "judge": a.audit_model, "matcher": a.match_model,
               "per_rung": results,
               "overall_recovery": statistics.mean(over) if over else None,
               "rows": all_rows}, open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
