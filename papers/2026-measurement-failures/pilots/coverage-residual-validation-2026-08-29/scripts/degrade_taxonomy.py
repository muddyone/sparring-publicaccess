#!/usr/bin/env python3
"""Build degraded taxonomies to test whether GRANULARITY is causal.

The observational finding across three fact patterns is that the structured walk performs
in proportion to how finely its taxonomy is drawn for that subject
(taxonomy-granularity-finding.md). That comparison is confounded: subjects differ in more
than granularity, and the best-performing case also had the most mechanical answer key.

This makes it an intervention instead. Same fact pattern, same key, same model, same walk
mechanism -- only the map changes.

  control   350 nodes, real leaf labels        "Enforceability (§ 9-203)"
  collapse  ~topic-level nodes only            "Enforceability of security interests"
  relabel   350 nodes, each leaf REPLACED by its parent topic's label

Why two manipulations. Collapsing a hierarchy necessarily reduces node count, so a drop in
the collapse arm could be "fewer things to hit" rather than "vaguer things to hit". The
relabel arm holds the count at 350 and degrades only the WORDS, which is the only way to
isolate specificity from count.

  both arms degrade  -> specificity is causal
  only collapse      -> the finding is a count effect and needs restating

Output is written into the gitignored corpus dir; NCBE text is not redistributed.

Usage:  ./degrade_taxonomy.py
"""
import json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "corpus")

VAGUE = {"basic concepts", "meaning and legal consequences",
         "application in specific areas", "special problems", "general principles",
         "in general", "scope", "introduction", "types", "definitions"}


def profile(nodes, name):
    leaves = [(n["subtopic"] or n["topic"]).strip() for n in nodes]
    med = statistics.median(len(l.split()) for l in leaves)
    vague = sum(1 for l in leaves if l.lower() in VAGUE) / len(leaves)
    uniq = len(set(leaves))
    print(f"  {name:<10} nodes {len(nodes):>4}  distinct labels {uniq:>4}  "
          f"median words {med:>3.0f}  vague {vague:>4.0%}")


def main():
    src = json.load(open(os.path.join(CORPUS, "taxonomy.json")))
    tax = src["nodes"]

    # --- collapse: one node per (subject, topic); the leaf detail disappears ---
    seen, collapse = set(), []
    for n in tax:
        key = (n["subject"], n["topic"])
        if key in seen:
            continue
        seen.add(key)
        collapse.append({"subject": n["subject"], "topic": n["topic"], "subtopic": None,
                         "node_id": f"c{len(collapse):03d}",
                         "path": f"{n['subject']} > {n['topic']}"})

    # --- relabel: keep every node, but show the parent topic's words in place of the
    #     leaf's. Same count, same structure, strictly less specific text. ---
    relabel = []
    for i, n in enumerate(tax):
        relabel.append({"subject": n["subject"], "topic": n["topic"],
                        "subtopic": n["topic"],          # the degradation
                        "node_id": f"r{i:03d}",
                        "path": f"{n['subject']} > {n['topic']}"})

    print("granularity profile of the three arms:")
    profile(tax, "control")
    profile(collapse, "collapse")
    profile(relabel, "relabel")
    print("\n  note: relabel holds node COUNT at the control's level while cutting")
    print("  distinct labels, which is exactly the specificity-vs-count separation.")

    for name, nodes in (("collapse", collapse), ("relabel", relabel)):
        out = os.path.join(CORPUS, f"taxonomy.{name}.json")
        json.dump({"n_nodes": len(nodes), "arm": name, "source": src["source"],
                   "nodes": nodes}, open(out, "w"), indent=2)
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
