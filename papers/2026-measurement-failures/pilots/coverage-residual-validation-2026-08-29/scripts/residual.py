#!/usr/bin/env python3
"""The comparison layer, rebuilt on directed membership instead of pooled clustering.

WHY THIS REPLACES CLUSTERING.

  Every instability in this study traces to one mechanism: partitioning a 300-400 item
  pool into clusters. It produced a 27% swing in the floor on granularity alone,
  intermittently unparseable replicates, a single clustering that reported itself as a
  consensus, and finally (structured-enumerator.md §4) marked the two highest-weighted
  gold points as things free generation never found.

  The most reliable measurement in the study is the opposite shape: the matching pass in
  scoring-design.md asks "does this list contain key point K?" -- closed-set membership
  against a fixed reference -- and scored unanimity 1.00.

  So the residual is measured that way instead. For each run, ONE directed question:
  "which of these candidate issues appear in this list?" That yields a membership matrix
  (item x run), and every quantity is arithmetic on it -- no further model calls.

THE KEY PROPERTY, AND WHY IT DISSOLVES THE BUG.

  Membership never has to merge synonyms into canonical clusters. It only has to decide
  whether a CONCEPT appears in a LIST. "Division of property" is judged present in a run
  that said "Equitable distribution factors" and "Classification: separate vs marital
  property" -- no cluster has to be built to make that true. The cross-vocabulary problem
  simply does not arise, because vocabularies are never being reconciled with each other,
  only checked against a list.

COST: one call per run per replicate (10 runs, k=2 -> 20 calls), against clustering's
whole-pool partition. Cheaper AND the reliable shape.

Usage:
  ./residual.py --a 'runs/*.g1n.r*.json' --b 'runs/*.g4.r*.json' [-k 2]
"""
import argparse, glob, itertools, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))


def load_env(path=os.environ.get("SPARRING_ENV_FILE")):
    # DEPOSIT COPY: the working-repository original read a hard-coded, machine-specific
    # .env path here. Keys now come from the environment (ANTHROPIC_API_KEY,
    # OPENAI_API_KEY); set SPARRING_ENV_FILE to a KEY=VALUE file to load them from one.
    if not path:
        return
    for line in open(path):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v.strip().strip('"'))


load_env()
from lib_llm import gpt_json, claude_json  # noqa: E402

JUDGE = "claude-opus-4-8"

SYS = """You are checking which candidate legal issues are PRESENT in a given list.

The list and the candidates were written by different people using different vocabularies.
One may say "Division of property" where the other says "Equitable distribution factors"
or "Classification: separate vs marital property". Those are THE SAME ISSUE. Judge the
underlying legal question, never the wording.

PRESENT means an entry in the list addresses THE SAME SPECIFIC QUESTION, differently
worded. Same question, different words = present.

ABSENT means no entry addresses that specific question. In particular:

  A BROAD HEADING DOES NOT MAKE EVERY QUESTION UNDER IT PRESENT.
  "Division of property" does NOT make "goodwill valuation of a closely held business"
  present. "Premarital contracts" does NOT make "waiver of the right to counsel" present.
  A list that names an area of law has not thereby raised every issue in that area.

Most lists are short and most candidates will be ABSENT. A list of 12 entries cannot
address 200 distinct questions. If you are marking nearly everything present, you are
matching topics rather than questions -- re-read and be strict.

Return ONLY the numbers of candidates that are PRESENT:
{"present":[<candidate numbers>]}"""


def load_runs(pattern, tag):
    paths = [p for p in sorted(glob.glob(pattern))
             if "raw" in json.load(open(p))]
    if len(paths) < 2:
        sys.exit(f"need >=2 runs for {tag}, found {len(paths)} matching {pattern}")
    out = []
    for p in paths:
        d = json.load(open(p))
        items = d["raw"]["issues"]
        out.append({"path": os.path.basename(p), "group": tag, "model": d["generator"],
                    "rung": d.get("rung"),
                    "labels": [i["label"] for i in items],
                    "whys": [i.get("why", "") for i in items]})
    return out


def membership(candidates, run, k, model):
    """Which candidates appear in this run's list? k replicates, majority vote."""
    ref = "\n".join(f"- {l}" + (f" ({w})" if w else "")
                    for l, w in zip(run["labels"], run["whys"]))
    cand = "\n".join(f"[{i}] {c}" for i, c in enumerate(candidates))
    user = f"THE LIST\n{ref}\n\nCANDIDATE ISSUES\n{cand}"
    votes = [0] * len(candidates)
    used = 0
    for _ in range(k):
        try:
            out = (gpt_json(model, SYS, user) if model.startswith("gpt")
                   else claude_json(model, SYS, user, max_tokens=8000))
        except Exception as e:
            print(f"      membership replicate failed: {str(e)[:80]}")
            continue
        used += 1
        for x in out.get("present", []):
            try:
                i = int(x)
            except (TypeError, ValueError):
                continue
            if 0 <= i < len(candidates):
                votes[i] += 1
    if not used:
        sys.exit("all membership replicates failed")
    return [v * 2 >= used for v in votes], used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="glob for group A runs (the baseline)")
    ap.add_argument("--b", required=True, help="glob for group B runs (the challenger)")
    ap.add_argument("-k", type=int, default=2, help="membership replicates per run")
    ap.add_argument("--judge", default=JUDGE)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    A, B = load_runs(a.a, "A"), load_runs(a.b, "B")
    runs = A + B
    ia, ib = list(range(len(A))), list(range(len(A), len(runs)))

    # Candidate universe: every distinct label anyone produced. These are NOT clusters and
    # are deliberately not merged -- membership handles synonymy per query.
    cands, seen = [], set()
    for r in runs:
        for l in r["labels"]:
            if l not in seen:
                seen.add(l)
                cands.append(l)

    print(f"group A : {A[0]['model']} ({A[0]['rung']})  {len(A)} runs  "
          f"{[len(r['labels']) for r in A]}")
    print(f"group B : {B[0]['model']} ({B[0]['rung']})  {len(B)} runs  "
          f"{[len(r['labels']) for r in B]}")
    print(f"candidates: {len(cands)} distinct labels")
    print(f"judge     : {a.judge}  k={a.k}   ({len(runs)}x{a.k} = {len(runs)*a.k} calls)\n")

    sets, suspect = [], []
    for n, r in enumerate(runs):
        present, used = membership(cands, r, a.k, a.judge)
        s = {i for i, p in enumerate(present) if p}
        sets.append(s)
        # Plausibility guard. The first build of this judge marked a 10-item walk as
        # covering 275 of 281 candidates -- membership over-merging, the mirror image of
        # the clustering bug it replaced. A short list cannot address most of a large
        # candidate set, so a high covers/own ratio is reported as suspect rather than
        # left to be noticed in the metrics downstream.
        ratio = len(s) / max(len(r["labels"]), 1)
        flag = "  <-- IMPLAUSIBLE" if ratio > 3.0 else ""
        print(f"  {r['path'][:48]:<48} own {len(r['labels']):>3}  covers {len(s):>3}"
              f"  x{ratio:>4.1f}  ({used}/{a.k}){flag}")
        if ratio > 3.0:
            suspect.append(r["path"])

    if suspect:
        print(f"\n  !! {len(suspect)} run(s) show implausible coverage (>3x their own item")
        print("     count). The membership judge is matching topics rather than specific")
        print("     questions; every number below is inflated toward 'shared'. Fix the")
        print("     judge before reading the metrics.")

    def resid(i, j):
        """Fraction of the pair's union that run i lacked and run j had."""
        u = sets[i] | sets[j]
        return len(sets[j] - sets[i]) / len(u) if u else 0.0

    within_a = [resid(i, j) for i, j in itertools.permutations(ia, 2)]
    within_b = [resid(i, j) for i, j in itertools.permutations(ib, 2)]
    a_miss_b = [resid(i, j) for i, j in itertools.product(ia, ib)]
    nov = [len(sets[j] - sets[i]) / len(sets[j])
           for i, j in itertools.product(ia, ib) if sets[j]]
    snov = [len(sets[j] - sets[i]) / len(sets[j])
            for i, j in itertools.permutations(ia, 2) if sets[j]]
    wa, wb, amb = (statistics.mean(x) for x in (within_a, within_b, a_miss_b))
    nv, sn = statistics.mean(nov), statistics.mean(snov)

    pa = set().union(*[sets[i] for i in ia])
    pb = set().union(*[sets[i] for i in ib])
    print(f"\npool A {len(pa)}   pool B {len(pb)}   shared {len(pa & pb)}   "
          f"A-only {len(pa - pb)}   B-only {len(pb - pa)}")

    print("\n--- one run vs one run (directed) ---")
    print(f"  within-A (the floor)        : {wa:.3f}")
    print(f"  within-B                    : {wb:.3f}")
    print(f"  an A run misses, vs a B run : {amb:.3f}")
    print(f"  LIFT = {amb:.3f} - {wa:.3f} = {amb - wa:+.3f}")
    print(f"\n  novelty rate (of what B raises, share A lacked) : {nv:.3f}")
    print(f"  A's own novelty vs another A run                : {sn:.3f}")
    print(f"  NOVELTY LIFT = {nv - sn:+.3f}")

    # Sanity check the fix on the case that exposed the clustering bug: the two
    # highest-weighted gold points must NOT read as things group A missed.
    print("\n--- sanity: items B-only that A demonstrably covered ---")
    bad = []
    for i in sorted(pb - pa):
        lab = cands[i]
        if any(w in lab.lower() for w in
               ("division of property", "premarital contract", "marital property")):
            bad.append(lab)
    if bad:
        print("  STILL WRONG -- these read as B-only:")
        for l in bad:
            print(f"    - {l}")
    else:
        print("  clean: no high-weight gold point reads as something A never found")
    print(f"  B-only labels ({len(pb - pa)}):")
    for i in sorted(pb - pa)[:12]:
        print(f"    - {cands[i][:96]}")

    out = a.out or os.path.join(HERE, "..", "runs", "residual-membership.json")
    json.dump({"group_a": {"model": A[0]["model"], "rung": A[0]["rung"],
                           "runs": [r["path"] for r in A]},
               "group_b": {"model": B[0]["model"], "rung": B[0]["rung"],
                           "runs": [r["path"] for r in B]},
               "method": "directed membership (no pooled clustering)",
               "n_candidates": len(cands), "k": a.k, "judge": a.judge,
               "pool_a": len(pa), "pool_b": len(pb), "shared": len(pa & pb),
               "a_only": len(pa - pb), "b_only": len(pb - pa),
               "b_only_labels": [cands[i] for i in sorted(pb - pa)],
               "within_a": wa, "within_b": wb, "a_misses_vs_b": amb,
               "lift": amb - wa, "novelty_rate": nv, "self_novelty_rate": sn,
               "novelty_lift": nv - sn,
               "per_run_covers": [len(s) for s in sets]},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
