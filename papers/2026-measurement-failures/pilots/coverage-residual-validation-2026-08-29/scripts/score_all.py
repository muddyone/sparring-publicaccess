#!/usr/bin/env python3
"""Score every generator against the examiners' answer key.

This replaces generator-to-generator comparison, which was found to be ill-posed
(comparison-layer-negative.md): three mechanisms resolved the same ambiguity three
different ways and each reported its own resolution as a result.

Key-relative measurement is well-posed for a specific reason. The key is small, fixed,
externally authored, and each of its points is a QUESTION rather than a label -- so "does
this list address this question?" has an answer. That pass scores unanimity 1.00 and its
positive control passes at 1.00, and it has been the only reliable comparison in the study.

Both directions, per scoring-design.md:
  weighted recall  -- of the examiners' weighted points, how many did this run surface?
  yield            -- of everything it emitted, how much was sound, raised, material,
                      non-duplicate? (blind to the key)

Generators are then compared THROUGH their scores rather than against each other, which
never requires deciding whether B's phrasing is the same issue as A's.

What this cannot see, stated up front: anything the examiners did not grade. It measures
how much of a KNOWN answer a generator finds, not what nobody thought of.

Usage:
  ./score_all.py --admin "February 2018" --subject "Family Law" [-k 2] [--rungs g1,g3,g4]
"""
import argparse, glob, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))

from score_pair import pass_a, pass_b, majority, norm_id, GPT, CLAUDE  # noqa: E402

RUNGS = {
    "g1":  "gpt-5.2, natural verbosity        (the baseline system)",
    "g1n": "gpt-5.2, ~55-item budget          (volume-matched)",
    "g3":  "claude-opus-4-8, natural          (cross-vendor)",
    "g3n": "claude-opus-4-8, ~55-item budget  (cross-vendor, volume-matched)",
    "g4":  "structured walk, REAL map        (350 nodes, 341 distinct labels)",
    "g4collapse": "structured walk, COLLAPSED map   (86 nodes -- count AND words cut)",
    "g4relabel":  "structured walk, RELABELLED map  (350 nodes, 85 distinct -- words only)",
}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def score_run(run, fact, k, match_model, audit_model):
    items = [i["label"] for i in run["raw"]["issues"]]
    gold = run["gold"]["gold"]
    if not items:
        return None
    A = pass_a(items, gold, k, match_model)
    B = pass_b(items, fact, k, audit_model)

    covered, cites = {}, {}
    for g in gold:
        v, _ = majority(A, norm_id(g["point_id"]), "covered")
        covered[g["point_id"]] = bool(v)
    for rep in A:
        for kid, m in rep.items():
            if m["covered"]:
                for i in m["by"]:
                    cites[i] = cites.get(i, 0) + 1
    matched = {i for i, c in cites.items() if c * 2 >= len(A)}
    wr = sum(g["weight_pct"] for g in gold if covered[g["point_id"]]) / 100.0

    verdicts = {}
    for i in range(len(items)):
        s, _ = majority(B, i, "sound")
        r, _ = majority(B, i, "raised")
        m, _ = majority(B, i, "material")
        dup = sum(1 for rep in B
                  if i in rep and rep[i].get("duplicate_of") is not None) * 2 >= len(B)
        verdicts[i] = {"sound": s, "raised": r, "material": m, "duplicate": dup,
                       "signal": bool(s and r and m and not dup)}
    E = len(items)
    sig = [i for i, v in verdicts.items() if v["signal"]]
    noise = [i for i, v in verdicts.items() if not (v["sound"] and v["raised"])]
    dups = [i for i, v in verdicts.items() if v["duplicate"]]
    offkey = [i for i in sig if i not in matched]

    # Positive control -- CONDITIONED ON COVERAGE.
    #
    # The first version asked, for every key point, whether >=1 item cited as covering it
    # was rated sound+raised+material. That is confounded with recall: a point the
    # generator never covered has no citing items, so it can never pass, and the control
    # is dragged down by low recall rather than by a bad judge. Measured on the July 2019
    # pattern the two were near-identical (recall/ctrl: 0.98/0.97, 1.00/1.00, 0.35/0.43),
    # so the control was carrying almost no independent information.
    #
    # It now scores only over the points the run ACTUALLY COVERED, which is the question
    # it was meant to ask: where this generator claims to have found something, does a
    # judge that never saw the key agree the item is real and material?
    ctrl_ok, ctrl_n = 0, 0
    for g in gold:
        if not covered[g["point_id"]]:
            continue
        ctrl_n += 1
        kid = norm_id(g["point_id"])
        c = [i for rep in A for k2, m in rep.items() if k2 == kid and m["covered"]
             for i in m["by"]]
        good = [i for i in set(c) if verdicts.get(i, {}).get("sound")
                and verdicts.get(i, {}).get("raised")
                and verdicts.get(i, {}).get("material")]
        ctrl_ok += bool(good)

    return {"control_n": ctrl_n, "emitted": E, "weighted_recall": wr,
            "signal": len(sig), "yield": len(sig) / E,
            "noise": len(noise), "noise_rate": len(noise) / E,
            "duplicates": len(dups), "redundancy": len(dups) / E,
            "offkey": len(offkey), "offkey_rate": len(offkey) / E,
            "control": (ctrl_ok / ctrl_n) if ctrl_n else None,
            "missed_points": [g["point_id"] for g in gold if not covered[g["point_id"]]]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admin", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("-k", type=int, default=2)
    ap.add_argument("--rungs", default="g1,g1n,g3,g3n,g4")
    ap.add_argument("--match-model", default=GPT)
    ap.add_argument("--audit-model", default=CLAUDE)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    q = next(x for x in qs if x["administration"] == a.admin and x["subject"] == a.subject)
    fact = q["text"]
    base = f"{slug(a.admin)}-{slug(a.subject)}"

    print(f"fact pattern : {a.admin} / {a.subject}")
    print(f"key          : {len(json.load(open(os.path.join(HERE, '..', 'gold', 'gold.json')))['fact_patterns'][0]['gold'])}-ish weighted points")
    print(f"matcher {a.match_model}   blind judge {a.audit_model}   k={a.k}\n")

    results = {}
    for rung in a.rungs.split(","):
        paths = sorted(glob.glob(os.path.join(HERE, "..", "runs",
                                              f"{base}.{rung}.r*.json")))
        paths = [p for p in paths if "raw" in json.load(open(p))]
        if not paths:
            print(f"  {rung}: no runs found -- skipped")
            continue
        rows = []
        for p in paths:
            r = score_run(json.load(open(p)), fact, a.k, a.match_model, a.audit_model)
            if r:
                rows.append(r)
        if not rows:
            continue
        agg = {k2: statistics.mean(r[k2] for r in rows)
               for k2 in ("emitted", "weighted_recall", "yield", "noise_rate",
                          "redundancy", "offkey_rate")}
        cvals = [r["control"] for r in rows if r["control"] is not None]
        agg["control"] = statistics.mean(cvals) if cvals else float("nan")
        agg["control_points"] = statistics.mean(r["control_n"] for r in rows)
        agg["n_runs"] = len(rows)
        agg["recall_min"] = min(r["weighted_recall"] for r in rows)
        agg["recall_max"] = max(r["weighted_recall"] for r in rows)
        agg["missed"] = sorted({m for r in rows for m in r["missed_points"]})
        results[rung] = {"agg": agg, "rows": rows}
        print(f"  {rung:<4} {agg['n_runs']} runs  recall {agg['weighted_recall']:.2f}  "
              f"yield {agg['yield']:.2f}  ctrl {agg['control']:.2f}")

    print("\n" + "=" * 78)
    print(f"{'rung':<5} {'items':>6} {'recall':>7} {'yield':>6} {'noise':>6} "
          f"{'redun':>6} {'offkey':>7} {'ctrl':>5}   description")
    print("-" * 78)
    for rung, d in results.items():
        g = d["agg"]
        print(f"{rung:<5} {g['emitted']:>6.0f} {g['weighted_recall']:>7.2f} "
              f"{g['yield']:>6.2f} {g['noise_rate']:>6.2f} {g['redundancy']:>6.2f} "
              f"{g['offkey_rate']:>7.2f} {g['control']:>5.2f}   {RUNGS.get(rung,'')}")
    print("=" * 78)
    print("recall = share of the examiners' WEIGHTED points found (1.00 = all of them)")
    print("yield  = share of what it emitted that was sound + raised + material + unique")
    print("ctrl   = positive control, scored ONLY over points the run covered (so it is not")
    print("         just recall again); below 0.90 the yield figure is not interpretable")
    print("noise  = share unsound or not raised by these facts -- independent of the control")

    for rung, d in results.items():
        miss = d["agg"]["missed"]
        if miss:
            print(f"\n  {rung}: key points missed in at least one run -> {', '.join(miss)}")

    out = a.out or os.path.join(HERE, "..", "runs", f"{base}.key-relative-scores.json")
    json.dump({"fact_pattern": f"{a.admin} / {a.subject}", "k": a.k,
               "match_model": a.match_model, "audit_model": a.audit_model,
               "method": "key-relative (supersedes generator-to-generator residual)",
               "results": {r: d["agg"] for r, d in results.items()},
               "per_run": {r: d["rows"] for r, d in results.items()}},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
