#!/usr/bin/env python3
"""Does a second VENDOR see anything the first cannot -- above the first's own noise?

This is the measurement the whole study was built for, and the one that is easy to fake.
"Model B raised 9 issues model A missed" sounds like a blind-spot finding and usually is
not: model A misses things against *itself* on a rerun. Unless the cross-vendor residual
clears that floor, it is indistinguishable from asking the same model twice.

THE COMPARISON MUST LIVE INSIDE ONE CLUSTERING.
  The floor is clustering-dependent -- three clusterings of the same five runs gave
  0.138 / 0.165 / 0.175, a 27% swing on granularity alone (self-residual-floor.md). So a
  cross-vendor residual computed under clustering X and compared against a floor computed
  under clustering Y measures the clusterer, not the vendors.

  This script therefore pools BOTH vendors' runs and clusters them TOGETHER, once, then
  computes all three quantities off that single clustering:

      within-A   mean pairwise residual between two runs of vendor A   <- the floor
      within-B   same, for vendor B
      between    mean pairwise residual between a run of A and a run of B

  LIFT = between - within-A. That is the only number entitled to be called a cross-vendor
  blind-spot effect, and it is what gets reported.

Unit matters: every quantity is ONE RUN vs ONE RUN, so between and within are directly
comparable. Pool-level totals (all 5 of A vs all 5 of B) are also reported, but they are
not comparable to the floor and are labelled accordingly.

Usage:
  ./cross_residual.py --a 'runs/*.g1.r*.json' --b 'runs/*.g3.r*.json' [-k 3]
"""
import argparse, glob, itertools, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))

from self_residual import (cluster, consensus_clusters, _modal,  # noqa: E402
                           CLUSTER_MODEL)


def load_runs(pattern, tag):
    paths = [p for p in sorted(glob.glob(pattern))
             if not p.endswith(".self-residual.json") and ".strata" not in p
             and "raw" in json.load(open(p))]
    if len(paths) < 2:
        sys.exit(f"need >=2 runs for {tag}, found {len(paths)} matching {pattern}")
    out = []
    for p in paths:
        d = json.load(open(p))
        # Cluster on label PLUS its one-line rationale, not the label alone.
        #
        # The structured enumerator (rung G4) emits terse formal taxonomy headings
        # ("Division of property") while free generators emit descriptive, fact-tied
        # phrases ("Equitable distribution factors", "Classification: separate vs marital
        # property"). Clustering bare labels across those two vocabularies UNDER-MERGES:
        # the first structured run scored a novelty lift of +0.274, and inspection showed
        # "Division of property" -- the 35%-weighted gold point, which gpt-5.2 covered with
        # 45 distinct labels -- counted as something free generation never found.
        #
        # The rationale sentence is the bridge: it ties both vocabularies to the same
        # facts. Applied uniformly to every rung so no generator gets a different deal.
        out.append({"path": os.path.basename(p), "vendor": tag,
                    "model": d["generator"], "rung": d.get("rung"),
                    "labels": [i["label"] for i in d["raw"]["issues"]],
                    "texts": [(i["label"] + (" -- " + i["why"] if i.get("why") else ""))
                              for i in d["raw"]["issues"]]})
    return out


def mean_pairwise(sets, idx_a, idx_b, same):
    """Symmetric within-group residual: of the union of two runs, what fraction did one
    miss? Only meaningful WITHIN a vendor, where the two sides are interchangeable."""
    vals = []
    for i, j in itertools.combinations(idx_a, 2) if same else itertools.product(idx_a, idx_b):
        si, sj = sets[i], sets[j]
        u = si | sj
        if u:
            vals.append(len(sj - si) / len(u))
            vals.append(len(si - sj) / len(u))
    return vals


def directional(sets, idx_from, idx_to):
    """What a run from `idx_from` MISSES that a run from `idx_to` had, as a fraction of
    their union. Directional on purpose.

    Averaging the two directions -- which the first version of this script did -- is
    wrong whenever the two generators differ in verbosity, and they do: gpt-5.2 emits
    50-60 items per run against claude-opus-4-8's 20-24. The symmetric mean then fuses
    two unrelated quantities:

        what B ADDS over A   (the cross-vendor question)          -- small here
        what B LACKS from A  (a granularity difference)           -- large here

    and reports their average as a blind-spot effect. On this data that produced
    'between 0.304, lift +0.130, SUBSTANTIAL' off a pool where B contributed 4 clusters
    and A contributed 40. The number was real; the label on it was not."""
    vals = []
    for i, j in itertools.product(idx_from, idx_to):
        si, sj = sets[i], sets[j]
        u = si | sj
        if u:
            vals.append(len(sj - si) / len(u))
    return vals


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="glob for vendor A runs (the baseline)")
    ap.add_argument("--b", required=True, help="glob for vendor B runs (the challenger)")
    ap.add_argument("-k", type=int, default=3)
    ap.add_argument("--model", default=CLUSTER_MODEL)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    A = load_runs(a.a, "A")
    B = load_runs(a.b, "B")
    runs = A + B
    labels, texts, owner = [], [], []
    for ri, r in enumerate(runs):
        for l, t in zip(r["labels"], r["texts"]):
            labels.append(l)      # short form, for display
            texts.append(t)       # label + rationale, for clustering
            owner.append(ri)

    ia = list(range(len(A)))
    ib = list(range(len(A), len(runs)))
    distinct = sorted(set(texts))
    didx = {t: i for i, t in enumerate(distinct)}

    print(f"vendor A : {A[0]['model']}  ({A[0]['rung']})  {len(A)} runs  "
          f"{[len(r['labels']) for r in A]}")
    print(f"vendor B : {B[0]['model']}  ({B[0]['rung']})  {len(B)} runs  "
          f"{[len(r['labels']) for r in B]}")
    print(f"pooled   : {len(labels)} items, {len(distinct)} distinct")
    print(f"clusterer: {a.model}  k={a.k}   (BOTH vendors clustered together, once)\n")

    reps = cluster(distinct, a.k, a.model)
    if len(reps) < 2:
        sys.exit(f"only {len(reps)} usable clustering replicate(s); consensus needs >=2")
    dgroups = consensus_clusters(reps, len(distinct))
    dgroup_of = {d: gi for gi, g in enumerate(dgroups) for d in g}

    groups = [[] for _ in dgroups]
    for i, t in enumerate(texts):
        groups[dgroup_of[didx[t]]].append(i)
    keep = [gi for gi, g in enumerate(groups) if g]
    groups = [groups[gi] for gi in keep]

    # Per-run cluster sets -- the coordinate system all three quantities share.
    sets = [set() for _ in runs]
    for ci, g in enumerate(groups):
        for i in g:
            sets[owner[i]].add(ci)

    within_a = mean_pairwise(sets, ia, ia, True)
    within_b = mean_pairwise(sets, ib, ib, True)
    a_misses_b = directional(sets, ia, ib)   # what an A run misses that a B run had
    b_misses_a = directional(sets, ib, ia)   # the reverse
    wa, wb = statistics.mean(within_a), statistics.mean(within_b)
    amb, bma = statistics.mean(a_misses_b), statistics.mean(b_misses_a)
    # The cross-vendor question is directional: does swapping in a run of B instead of
    # another run of A surface MORE that A lacked? Compare like with like.
    lift = amb - wa

    pool_a = set().union(*[sets[i] for i in ia])
    pool_b = set().union(*[sets[i] for i in ib])

    print(f"distinct issues in the joint pool : {len(groups)}")
    print(f"  vendor A pool (all {len(A)} runs)      : {len(pool_a)}")
    print(f"  vendor B pool (all {len(B)} runs)      : {len(pool_b)}")
    print(f"  shared                              : {len(pool_a & pool_b)}")
    print(f"  A only                              : {len(pool_a - pool_b)}")
    print(f"  B only                              : {len(pool_b - pool_a)}")

    ipr_a = statistics.mean(len(r["labels"]) for r in A)
    ipr_b = statistics.mean(len(r["labels"]) for r in B)
    ratio = max(ipr_a, ipr_b) / max(min(ipr_a, ipr_b), 1)
    if ratio >= 1.5:
        print(f"\n  !! VERBOSITY ASYMMETRY {ratio:.1f}x  (A {ipr_a:.0f} items/run, "
              f"B {ipr_b:.0f})")
        print("     Directional residuals below are NOT interchangeable. A symmetric")
        print("     average would report a granularity difference as a blind spot.")

    print("\n--- one run vs one run, all inside this single clustering ---")
    print(f"  within-A (the floor)      : {wa:.3f}  [{min(within_a):.3f}-{max(within_a):.3f}]")
    print(f"  within-B                  : {wb:.3f}  [{min(within_b):.3f}-{max(within_b):.3f}]")
    print(f"  an A run misses, vs a B run : {amb:.3f}  <- what B ADDS  (the question)")
    print(f"  a B run misses, vs an A run : {bma:.3f}  <- what B LACKS (verbosity)")
    print(f"\n  LIFT = (A misses vs B) - (A misses vs A) = {amb:.3f} - {wa:.3f} = {lift:+.3f}")

    # Fraction-of-union systematically understates a generator that emits FEWER items:
    # the union is dominated by the larger side, so a small generator cannot post a big
    # number however novel it is. The structured enumerator (rung G4) is bounded by its
    # taxonomy -- 350 nodes total, ~39 in the question's own subject -- so it is small by
    # construction, not by choice, and volume-matching is not available as a remedy.
    #
    # NOVELTY RATE asks the question that survives the asymmetry: when B raises something,
    # how often is it something A never had? Denominator is B, not the union.
    novelty = [len(sets[j] - sets[i]) / len(sets[j])
               for i, j in itertools.product(ia, ib) if sets[j]]
    self_novelty = [len(sets[j] - sets[i]) / len(sets[j])
                    for i, j in itertools.combinations(ia, 2) if sets[j]]
    nov, snov = statistics.mean(novelty), statistics.mean(self_novelty)
    print(f"\n  novelty rate  (of what B raises, the share A lacked)   : {nov:.3f}")
    print(f"  A's own novelty vs another A run  (the comparison)   : {snov:.3f}")
    print(f"  NOVELTY LIFT = {nov:.3f} - {snov:.3f} = {nov - snov:+.3f}")
    print("    Use this when the generators differ in size by construction; use LIFT")
    print("    when they are volume-matched. They answer different questions.")

    print("\n--- reading ---")
    if lift <= 0.02:
        pass
    if lift <= 0.02:
        print("  NO CROSS-VENDOR EFFECT. A second vendor surfaces no more than a rerun of")
        print("  the first. On this problem the 'independent generator' is independent in")
        print("  name only -- which is the false-clean the design warned about, arriving")
        print("  as a real result rather than a caveat.")
    elif lift <= 0.10:
        print("  WEAK. A second vendor adds a little over a rerun, but the margin is small")
        print("  relative to the floor's own clustering sensitivity (+/-0.02 to 0.04).")
        print("  Not safe to call a blind-spot finding from one fact pattern.")
    else:
        print("  SUBSTANTIAL. The second vendor surfaces materially more than a rerun of")
        print("  the first -- the shape a genuine shared-blind-spot result would take.")
        print("  Still one fact pattern; needs replication before it means anything.")
    print("\n  Note: none of this says the extra issues are GOOD. Run score_strata.py")
    print("  on the B-only stratum before treating lift as coverage rather than noise.")

    out = a.out or os.path.join(HERE, "..", "runs", "cross-residual.json")
    json.dump({"vendor_a": {"model": A[0]["model"], "runs": [r["path"] for r in A]},
               "vendor_b": {"model": B[0]["model"], "runs": [r["path"] for r in B]},
               "joint_pool": len(groups), "pool_a": len(pool_a), "pool_b": len(pool_b),
               "shared": len(pool_a & pool_b), "a_only": len(pool_a - pool_b),
               "b_only": len(pool_b - pool_a),
               "novelty_rate": nov, "self_novelty_rate": snov,
               "novelty_lift": nov - snov,
               "within_a": wa, "within_b": wb,
               "a_misses_vs_b": amb, "b_misses_vs_a": bma, "lift": lift,
               "items_per_run_a": ipr_a, "items_per_run_b": ipr_b,
               "verbosity_ratio": ratio,
               "per_run_sets": [sorted(s_) for s_ in sets],
               "run_order": [r["path"] for r in runs],
               "k": a.k, "cluster_model": a.model,
               "clusters": [{"stratum": ("shared" if ci in pool_a and ci in pool_b
                                         else "a_only" if ci in pool_a else "b_only"),
                             "representative": _modal([labels[i] for i in g]),
                             "n_runs": len({owner[i] for i in g})}
                            for ci, g in enumerate(groups)]},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
