#!/usr/bin/env python3
"""Measure the run-to-run coverage floor: what does the SAME system miss against itself?

This is rung G1 of the independence ladder (design-note.md §4), and it is the number
everything else gets read against. A cross-vendor residual only means something above the
residual a system already has against its own reruns.

Per Bart's 2026-08-29 decision the floor is REPORTED, not subtracted. If a single run
misses what the same system surfaces on a rerun, that is a genuine coverage failure of
single-run use -- weaker than a systematic blind spot, but real, and it is the direct
evidence on whether one run can be trusted.

METHOD -- one clustering pass, membership for free.
  Naively this needs two model steps: deduplicate the pooled items, then ask which run
  contains which pooled item. It needs only one. Every pooled item already carries the run
  it came from, so clustering the pool into distinct issues yields run-membership as a
  by-product: run i "has" cluster c iff any of run i's items landed in c.

  That matters beyond cost. The membership question is the semantic-matching weak joint
  (design-note.md §0), and asking it directly -- "does run 2 contain run 1's item X?" --
  is an open-set judgment. Clustering a fixed pool is a closed-set assignment, which is
  the same reliability gain multiple-choice has over free response.

Usage:
  ./self_residual.py --glob 'runs/february-2018-family-law.g1.r*.json' [-k 3]
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

# Cross-vendor from the generator by default: the clusterer must not share the
# generator's sense of what counts as "the same issue".
CLUSTER_MODEL = "claude-opus-4-8"

CLUSTER_SYS = """You are clustering issue labels produced by several independent attempts
at the same legal problem. Group labels that name THE SAME underlying legal issue, even
when they slice it at different granularities or use different words.

Rules:
- One cluster per distinct issue. A label belongs to exactly one cluster.
- Different aspects of one doctrine that a lawyer would analyse together = ONE cluster.
- Genuinely separate questions = SEPARATE clusters, even in the same doctrine.
- Give each cluster a short canonical name.
- Every input index must appear in exactly one cluster.

Return JSON:
{"clusters":[{"name":"<6 words max>","members":[<indices>]}]}"""


# A 280-item clustering emits a lot of JSON. At max_tokens=8000 the response was
# truncated mid-object and JSON extraction failed -- intermittently, because output
# length itself varies between samples. Sized well above the observed need, and a
# short/truncated reply is now reported rather than silently costing a replicate.
CLUSTER_MAX_TOKENS = 16000


def cluster(labels, k, model):
    listing = "\n".join(f"[{i}] {l}" for i, l in enumerate(labels))
    reps = []
    for r in range(k):
        # lib_llm retries HTTP failures, but claude_json/gpt_json parse OUTSIDE that
        # retry -- so one malformed or truncated sample killed a whole replicate, and
        # two of three died that way on the first attempt. Parse failures are transient
        # (the same input parsed fine on other samples), so they get their own retry.
        out = None
        for attempt in range(3):
            try:
                out = (gpt_json(model, CLUSTER_SYS, listing) if model.startswith("gpt")
                       else claude_json(model, CLUSTER_SYS, listing,
                                        max_tokens=CLUSTER_MAX_TOKENS))
                break
            except Exception as e:
                print(f"  clustering replicate {r+1}/{k} attempt {attempt+1}/3 "
                      f"unparseable: {str(e)[:90]}")
        if out is None:
            print(f"  clustering replicate {r+1}/{k} FAILED after 3 attempts")
            continue
        assign = {}
        for ci, c in enumerate(out.get("clusters", [])):
            for m in c.get("members", []):
                try:
                    assign[int(m)] = ci
                except (TypeError, ValueError):
                    continue
        names = [c.get("name", f"cluster{ci}")
                 for ci, c in enumerate(out.get("clusters", []))]
        missing = len(labels) - len(assign)
        if missing:
            print(f"  clustering replicate {r+1}/{k}: {missing} of {len(labels)} items "
                  f"unassigned (truncated or dropped) -- replicate kept, coverage noted")
        reps.append({"assign": assign, "names": names,
                     "assigned": len(assign), "clusters": len(names)})
    if len(reps) < 2:
        sys.exit(f"only {len(reps)} usable clustering replicate(s). Consensus needs >=2 -- "
                 "with one, consensus_clusters() just returns that clustering, which is "
                 "exactly the single-pass judgment this design refuses to trust. "
                 "Re-run, or raise -k.")
    print(f"  clustering: {len(reps)}/{k} replicates usable, "
          f"clusters per replicate {[r['clusters'] for r in reps]}\n")
    return reps


def _modal(strings):
    """Most common label in a cluster, ties broken by shortest -- a stable, neutral
    representative for downstream scoring."""
    from collections import Counter
    c = Counter(strings)
    top = max(c.values())
    return sorted([s for s, n in c.items() if n == top], key=len)[0]


def consensus_clusters(reps, n_items):
    """Co-assignment consensus: two items share a cluster if a majority of replicate
    clusterings put them together. Avoids trusting any single clustering, which is the
    least stable judgment in this study (see first-scored-run.md)."""
    together = {}
    for rep in reps:
        a = rep["assign"]
        for i, j in itertools.combinations(range(n_items), 2):
            if i in a and j in a and a[i] == a[j]:
                together[(i, j)] = together.get((i, j), 0) + 1
    thresh = len(reps) / 2.0
    parent = list(range(n_items))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (i, j), c in together.items():
        if c > thresh:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[max(ri, rj)] = min(ri, rj)
    groups = {}
    for i in range(n_items):
        groups.setdefault(find(i), []).append(i)
    return list(groups.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", required=True, help="glob for replicate run files")
    ap.add_argument("-k", type=int, default=3, help="replicate clusterings")
    ap.add_argument("--model", default=CLUSTER_MODEL)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    # Skip this script's OWN artifacts: the natural glob for the replicate runs also
    # matches the .self-residual.json it writes beside them, which has no "raw" key.
    paths = [p for p in sorted(glob.glob(a.glob))
             if not p.endswith(".self-residual.json")
             and "raw" in json.load(open(p))]
    if len(paths) < 2:
        sys.exit(f"need >=2 replicate runs, found {len(paths)} for {a.glob}")

    runs, labels, owner = [], [], []
    for p in paths:
        d = json.load(open(p))
        its = [i["label"] for i in d["raw"]["issues"]]
        runs.append({"path": os.path.basename(p), "n": len(its),
                     "replicate": d.get("replicate"), "rung": d.get("rung")})
        for l in its:
            labels.append(l)
            owner.append(len(runs) - 1)

    R = len(runs)
    # Exact-duplicate labels are common across runs of the same system (66 of 280 here).
    # Clustering only the distinct strings cuts the model's input and output by a
    # quarter -- cheaper, and less exposed to the truncation that killed replicates.
    distinct = sorted(set(labels))
    didx = {l: i for i, l in enumerate(distinct)}

    print(f"runs          : {R}  ({runs[0]['rung']}, "
          f"{json.load(open(paths[0]))['generator']})")
    print(f"items per run : {[r['n'] for r in runs]}")
    print(f"pooled items  : {len(labels)}   distinct labels: {len(distinct)}")
    print(f"clusterer     : {a.model}   k={a.k}\n")

    reps = cluster(distinct, a.k, a.model)
    dgroups = consensus_clusters(reps, len(distinct))

    # Map distinct-label clusters back onto the original items, then read run
    # membership off ownership -- the by-product that makes this one pass, not two.
    dgroup_of = {}
    for gi, g in enumerate(dgroups):
        for d in g:
            dgroup_of[d] = gi
    groups = [[] for _ in dgroups]
    for i, l in enumerate(labels):
        groups[dgroup_of[didx[l]]].append(i)
    groups = [g for g in groups if g]
    members = [sorted({owner[i] for i in g}) for g in groups]
    P = len(groups)
    per_run = [sum(1 for m in members if r in m) for r in range(R)]

    print("--- the system's own ceiling ---")
    print(f"  distinct issues across all {R} runs (the pool) : {P}")
    print(f"  distinct issues per single run                 : {per_run}")
    print(f"  mean single-run coverage of the pool           : "
          f"{statistics.mean(per_run)/P:.2f}")
    print(f"  issues found by ALL {R} runs (the stable core) : "
          f"{sum(1 for m in members if len(m) == R)}")
    print(f"  issues found by exactly ONE run                : "
          f"{sum(1 for m in members if len(m) == 1)}")

    # Pairwise self-residual: of the union of two runs, what fraction did one miss?
    pair = []
    for i, j in itertools.combinations(range(R), 2):
        si = {c for c, m in enumerate(members) if i in m}
        sj = {c for c, m in enumerate(members) if j in m}
        union = si | sj
        if union:
            pair.append(len(sj - si) / len(union))
            pair.append(len(si - sj) / len(union))
    floor = statistics.mean(pair) if pair else 0.0

    print("\n--- the floor (design-note.md §4, rung G1) ---")
    print(f"  mean pairwise self-residual : {floor:.3f}")
    print(f"    of everything two runs of the SAME system surface between them,")
    print(f"    one run misses {floor*100:.0f}% on average.")
    print(f"  spread across pairs         : "
          f"{min(pair):.3f} - {max(pair):.3f}" if pair else "")
    print("\n  REPORTED, NOT SUBTRACTED. A single run delivering "
          f"{statistics.mean(per_run)/P:.0%} of what the same")
    print("  system finds across reruns is a coverage failure of single-run use.")
    print(f"  Any cross-vendor residual must clear {floor:.3f} to mean anything.")

    out = a.out or os.path.join(HERE, "..", "runs",
                                os.path.basename(a.glob).replace("*", "ALL")
                                .replace(".json", "") + ".self-residual.json")
    json.dump({"runs": runs, "pooled_items": len(labels), "distinct_issues": P,
               "per_run_distinct": per_run,
               "mean_single_run_coverage": statistics.mean(per_run) / P,
               "found_by_all": sum(1 for m in members if len(m) == R),
               "found_by_one": sum(1 for m in members if len(m) == 1),
               "mean_pairwise_self_residual": floor,
               "pairwise": pair, "k": a.k, "cluster_model": a.model,
               # Persist cluster CONTENTS, not just shape. The first version stored
               # only {members_runs, size}, which made the artifact unusable for the
               # obvious follow-up -- scoring the singleton issues to find out whether
               # run-to-run variance is lost coverage or churn -- and forced a re-run.
               "clusters": [{"members_runs": m, "size": len(g),
                             "n_runs": len(m),
                             "stratum": ("core" if len(m) == R
                                         else "singleton" if len(m) == 1 else "mid"),
                             "representative": _modal([labels[i] for i in g]),
                             "labels": [labels[i] for i in g],
                             "item_indices": g}
                            for m, g in zip(members, groups)]},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
