#!/usr/bin/env python3
"""Rung G4: the structured non-model enumerator.

The load-bearing rung. With live human evaluation unavailable by standing constraint, and
the cross-vendor pass measured as worth no more than re-running the first model
(cross-vendor-null.md), this is the first generator in the ladder whose failure mode is not
drawn from the same distribution as the others.

WHAT MAKES IT DIFFERENT, STATED PRECISELY.

  A free generator does two things at once: it *thinks of* candidate issues, and it
  *decides* which apply. Both draw on the model's distribution, so two vendors can fail
  identically at the first step and nothing downstream can tell.

  This rung removes the first step. The candidate set is the NCBE MEE Subject Matter
  Outline -- 350 nodes across all 14 subjects, written by examiners as an exhaustive
  statement of the domain, years before this study existed. The model never invents a
  candidate. It only answers, for each node it is handed: do THESE facts raise this?

  So the enumerator CANNOT fail by not thinking of something. That is the whole point, and
  it is a real structural difference rather than a prompt trick.

AND ITS LIMIT, WHICH MUST TRAVEL WITH IT.

  Recognition is still a model judgment. The enumerator can fail to see that a node
  applies, and that failure could still be shared across vendors. This rung removes ONE of
  the two shared-failure channels, not both. Claiming more would be exactly the
  overstatement this study exists to catch.

  It is also bounded by the taxonomy: an issue outside the outline cannot be surfaced. The
  outline is broad (all 14 subjects are walked, not just the question's own) but it is not
  the world.

Blind to the answer key, like every other rung. All 14 subjects are walked -- restricting
to the question's subject would leak which subject matters, information no other generator
was given, and would forfeit the cross-subject issues this rung is best placed to find.

Usage:
  ./enumerate_structured.py --admin "February 2018" --subject "Family Law" -n 5
"""
import argparse, json, os, re, sys, time

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

MODEL = "gpt-5.2"   # same vendor as the g1 baseline ON PURPOSE -- see below

SYS = """You are checking a law-school fact pattern against a fixed checklist of legal
topics. You did not write the checklist and you may not add to it.

For each numbered topic, decide ONE thing: do THESE FACTS raise it?

  raised=true  - something in the fact pattern actually puts this topic in play
  raised=false - the topic is not triggered by these facts

Be strict. A topic is not raised merely because it belongs to the same area of law. It is
raised when a specific fact would make a careful lawyer analyse it.

Return ONLY the topics you judge raised, as JSON:
{"raised":[{"i":<topic number>,"why":"<one short sentence tying it to a specific fact>"}]}"""


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield i, seq[i:i + n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admin", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("-n", type=int, default=5, help="replicate walks")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--chunk", type=int, default=120,
                    help="taxonomy nodes per call (all subjects are always walked)")
    ap.add_argument("--taxonomy", default="taxonomy.json",
                    help="taxonomy file in corpus/ (degraded arms: taxonomy.collapse.json, "
                         "taxonomy.relabel.json)")
    ap.add_argument("--tag", default="g4",
                    help="rung tag for output filenames (g4, g4collapse, g4relabel)")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "runs"))
    a = ap.parse_args()

    tax = json.load(open(os.path.join(HERE, "..", "corpus", a.taxonomy)))["nodes"]
    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    gs = json.load(open(os.path.join(HERE, "..", "gold", "gold.json")))["fact_patterns"]
    q = next((x for x in qs if x["administration"] == a.admin
              and x["subject"] == a.subject), None)
    g = next((x for x in gs if x["administration"] == a.admin
              and x["subject"] == a.subject), None)
    if not q or not g:
        sys.exit(f"no such fact pattern: {a.admin} / {a.subject}")

    subs = sorted({n["subject"] for n in tax})
    print(f"fact pattern : {a.admin} / {a.subject}")
    print(f"taxonomy     : {len(tax)} nodes across {len(subs)} subjects (ALL walked)")
    print(f"model        : {a.model}   replicates: {a.n}   chunk: {a.chunk}")
    print(f"key          : {g['n_gold']} weighted points (NOT shown)\n")

    slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    base = f"{slug(a.admin)}-{slug(a.subject)}.{a.tag}"
    os.makedirs(a.outdir, exist_ok=True)

    for r in range(1, a.n + 1):
        t0, hits = time.time(), []
        for off, part in chunks(tax, a.chunk):
            listing = "\n".join(f"[{off+j}] {n['path']}" for j, n in enumerate(part))
            user = f"FACT PATTERN\n{q['text']}\n\nTOPIC CHECKLIST\n{listing}"
            out = (gpt_json(a.model, SYS, user) if a.model.startswith("gpt")
                   else claude_json(a.model, SYS, user, max_tokens=8000))
            for h in out.get("raised", []):
                try:
                    i = int(h["i"])
                except (KeyError, TypeError, ValueError):
                    continue
                if 0 <= i < len(tax):
                    hits.append({"node_id": tax[i]["node_id"], "path": tax[i]["path"],
                                 "why": h.get("why", "")})
        # De-duplicate on LABEL, not node_id. The relabel arm deliberately gives many
        # nodes the same words, and counting one label twice would inflate that arm's
        # item count for a reason that has nothing to do with what it found. Applied to
        # every arm so the mechanism is identical across them (the control loses 9 of
        # 350 to this, the relabel arm a great many more -- which is the manipulation).
        seen, items = set(), []
        for h in hits:
            if h["path"] not in seen:
                seen.add(h["path"])
                # `label` keeps the same field name every other rung uses, so the residual
                # and scoring scripts consume this without a special case.
                items.append({"label": h["path"].split(" > ")[-1],
                              "why": h["why"], "node_id": h["node_id"],
                              "taxonomy_path": h["path"]})

        stub = {k: v for k, v in q.items() if k != "text"}
        stub["text"] = ("<NCBE fact pattern withheld -- copyrighted. Rebuild with "
                        "scripts/fetch_corpus.sh + scripts/extract_questions.py>")
        path = os.path.join(a.outdir, f"{base}.r{r}.json")
        json.dump({"question": stub, "gold": g, "generator": a.model, "rung": a.tag,
                   "replicate": r, "taxonomy_nodes": len(tax),
                   "taxonomy_file": a.taxonomy,
                   "raw": {"issues": items}}, open(path, "w"), indent=2)
        by_subj = {}
        for it in items:
            s0 = it["taxonomy_path"].split(" > ")[0]
            by_subj[s0] = by_subj.get(s0, 0) + 1
        extra = ", ".join(f"{k} {v}" for k, v in sorted(by_subj.items(), key=lambda x: -x[1])[:4])
        print(f"  r{r}: {len(items):>3}/{len(tax)} nodes raised  ({time.time()-t0:.0f}s)  {extra}")

    print(f"\nnext: python3 scripts/cross_residual.py --a 'runs/{base.replace('.g4','.g1n')}.r*.json' "
          f"--b 'runs/{base}.r*.json'")


if __name__ == "__main__":
    main()
