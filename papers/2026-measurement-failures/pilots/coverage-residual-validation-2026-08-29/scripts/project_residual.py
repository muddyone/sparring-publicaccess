#!/usr/bin/env python3
"""Compare generators by projecting BOTH onto the taxonomy, then doing set arithmetic.

THE THIRD ATTEMPT AT THE COMPARISON LAYER, AND WHY THE FIRST TWO FAILED.

  1. Pooled clustering. Partition every item from every run into clusters, read run
     membership off the partition. Failed: under-merged across vocabularies, marking the
     30%- and 35%-weighted gold points as things free generation never found. Also caused
     the 27% floor swing and the unparseable replicates.

  2. Directed membership against each run's own list. "Is candidate X present in this
     list?" Failed the other way: a 10-item walk of broad taxonomy headings was judged to
     cover 261 of 281 specific candidates. Tightening the prompt barely moved it.

  Both failures have ONE cause. When the two sides speak at different granularities, "is
  this specific question the same as that broad heading?" has no determinate answer. It is
  not a hard measurement; it is an ill-posed one. Clustering resolved the ambiguity toward
  'different', membership toward 'same', and neither is wrong because there is no fact
  being approximated.

THE FIX: give both sides the same coordinate system, fixed externally in advance.

  Project every run onto the NCBE MEE Subject Matter Outline -- 350 nodes, all 14
  subjects, authored by examiners before this study existed. For each run, ask which nodes
  its output covers. Then the residual is EXACT SET ARITHMETIC on node ids. No semantic
  matching happens at comparison time at all; it happens once per run, against a fixed
  external reference, which is the shape that scores unanimity 1.00 in this study.

  Three properties follow, and they are the point:
    - Granularity is fixed by the taxonomy for BOTH sides, so the verbosity confound is
      removed structurally rather than controlled for.
    - The comparison is deterministic given the projections.
    - The structured enumerator (rung G4) already speaks natively in node ids, so it needs
      no projection and cannot be advantaged or disadvantaged by one.

  The cost is real and must be stated: the taxonomy becomes the resolution limit. Two
  issues inside one node are indistinguishable, and an issue outside the outline is
  invisible. This measures coverage OF A DEFINED DOMAIN MAP, not of the world.

Usage:
  ./project_residual.py --a 'runs/*.g1n.r*.json' --b 'runs/*.g4.r*.json' [-k 2]
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

SYS = """You are mapping a list of legal issues onto a fixed topic checklist.

For each checklist topic, decide: does the list contain an entry that actually analyses
this topic?

  covered=yes - an entry addresses this topic, whatever words it uses
  covered=no  - no entry addresses it

Be strict about scope. An entry belongs to a topic only if it analyses THAT topic. An
entry about one topic does not cover its neighbours merely by being in the same area of
law. Most checklist topics will NOT be covered by any given list -- the checklist spans an
entire bar exam and the list addresses one problem.

Return ONLY the numbers of topics that ARE covered:
{"covered":[<topic numbers>]}"""


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield i, seq[i:i + n]


def load_runs(pattern, tag):
    paths = [p for p in sorted(glob.glob(pattern)) if "raw" in json.load(open(p))]
    if len(paths) < 2:
        sys.exit(f"need >=2 runs for {tag}, found {len(paths)} matching {pattern}")
    out = []
    for p in paths:
        d = json.load(open(p))
        items = d["raw"]["issues"]
        out.append({"path": os.path.basename(p), "group": tag, "model": d["generator"],
                    "rung": d.get("rung"), "items": items,
                    # A run already expressed in node ids needs no projection.
                    "native": [i["node_id"] for i in items if i.get("node_id")]})
    return out


def project(run, tax, k, model, chunk):
    if run["native"]:
        return set(run["native"]), k, True
    listing = "\n".join(f"- {i['label']}" + (f" ({i['why']})" if i.get("why") else "")
                        for i in run["items"])
    votes, used = {}, 0
    for _ in range(k):
        got, ok = set(), True
        for off, part in chunks(tax, chunk):
            topics = "\n".join(f"[{off+j}] {n['path']}" for j, n in enumerate(part))
            user = f"THE LIST\n{listing}\n\nCHECKLIST TOPICS\n{topics}"
            try:
                out = (gpt_json(model, SYS, user) if model.startswith("gpt")
                       else claude_json(model, SYS, user, max_tokens=6000))
            except Exception as e:
                print(f"      projection chunk failed: {str(e)[:70]}")
                ok = False
                continue
            for x in out.get("covered", []):
                try:
                    i = int(x)
                except (TypeError, ValueError):
                    continue
                if 0 <= i < len(tax):
                    got.add(tax[i]["node_id"])
        if ok:
            used += 1
            for nid in got:
                votes[nid] = votes.get(nid, 0) + 1
    if not used:
        sys.exit(f"projection failed for {run['path']}")
    return {n for n, v in votes.items() if v * 2 >= used}, used, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("-k", type=int, default=2)
    ap.add_argument("--judge", default=JUDGE)
    ap.add_argument("--chunk", type=int, default=120)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    tax = json.load(open(os.path.join(HERE, "..", "corpus", "taxonomy.json")))["nodes"]
    by_id = {n["node_id"]: n for n in tax}
    A, B = load_runs(a.a, "A"), load_runs(a.b, "B")
    runs = A + B
    ia, ib = list(range(len(A))), list(range(len(A), len(runs)))

    print(f"group A : {A[0]['model']} ({A[0]['rung']})  {len(A)} runs  "
          f"{[len(r['items']) for r in A]}")
    print(f"group B : {B[0]['model']} ({B[0]['rung']})  {len(B)} runs  "
          f"{[len(r['items']) for r in B]}")
    print(f"taxonomy: {len(tax)} nodes -- the shared coordinate system")
    print(f"judge   : {a.judge}  k={a.k}\n")

    sets = []
    for r in runs:
        s, used, native = project(r, tax, a.k, a.judge, a.chunk)
        sets.append(s)
        tag = "native (already node ids)" if native else f"projected ({used}/{a.k} reps)"
        print(f"  {r['path'][:46]:<46} items {len(r['items']):>3} -> "
              f"{len(s):>3} nodes   {tag}")

    def resid(i, j):
        u = sets[i] | sets[j]
        return len(sets[j] - sets[i]) / len(u) if u else 0.0

    wa = statistics.mean([resid(i, j) for i, j in itertools.permutations(ia, 2)])
    wb = statistics.mean([resid(i, j) for i, j in itertools.permutations(ib, 2)])
    amb = statistics.mean([resid(i, j) for i, j in itertools.product(ia, ib)])
    nov = statistics.mean([len(sets[j] - sets[i]) / len(sets[j])
                           for i, j in itertools.product(ia, ib) if sets[j]])
    snov = statistics.mean([len(sets[j] - sets[i]) / len(sets[j])
                            for i, j in itertools.permutations(ia, 2) if sets[j]])
    pa = set().union(*[sets[i] for i in ia])
    pb = set().union(*[sets[i] for i in ib])

    print(f"\npool A {len(pa)} nodes   pool B {len(pb)}   shared {len(pa & pb)}   "
          f"A-only {len(pa - pb)}   B-only {len(pb - pa)}")
    print("\n--- one run vs one run, in taxonomy coordinates ---")
    print(f"  within-A (the floor)        : {wa:.3f}")
    print(f"  within-B                    : {wb:.3f}")
    print(f"  an A run misses, vs a B run : {amb:.3f}")
    print(f"  LIFT = {amb:.3f} - {wa:.3f} = {amb - wa:+.3f}")
    print(f"\n  novelty rate : {nov:.3f}   A's own novelty : {snov:.3f}   "
          f"NOVELTY LIFT {nov - snov:+.3f}")

    print(f"\n--- nodes group B reached that group A never did ({len(pb - pa)}) ---")
    for nid in sorted(pb - pa):
        print(f"    {by_id[nid]['path'][:96]}")
    print(f"\n--- and A-only ({len(pa - pb)}), first 10 ---")
    for nid in sorted(pa - pb)[:10]:
        print(f"    {by_id[nid]['path'][:96]}")

    out = a.out or os.path.join(HERE, "..", "runs", "residual-projected.json")
    json.dump({"method": "projection onto the NCBE taxonomy, then exact set arithmetic",
               "group_a": {"model": A[0]["model"], "rung": A[0]["rung"]},
               "group_b": {"model": B[0]["model"], "rung": B[0]["rung"]},
               "taxonomy_nodes": len(tax), "k": a.k, "judge": a.judge,
               "per_run_nodes": [len(s) for s in sets],
               "pool_a": len(pa), "pool_b": len(pb), "shared": len(pa & pb),
               "a_only": sorted(by_id[n]["path"] for n in pa - pb),
               "b_only": sorted(by_id[n]["path"] for n in pb - pa),
               "within_a": wa, "within_b": wb, "a_misses_vs_b": amb,
               "lift": amb - wa, "novelty_rate": nov, "self_novelty_rate": snov,
               "novelty_lift": nov - snov}, open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
