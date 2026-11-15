#!/usr/bin/env python3
"""Run generators blind on the situation. They never learn anything was missed.

The prompt is deliberately the PARENT STUDY'S prompt, adapted only where the stimulus
changed (a live matter before a court rather than an exam fact pattern). Keeping it
otherwise identical is what lets the parent's matcher, blind judge and scoring transfer
unchanged -- if the prompt drifted, a difference in results could not be attributed.

"include considerations that are easy to overlook" is retained verbatim from the parent
prompt. It is not seed priming: both rungs in the parent study carried it, and it says
nothing about THIS case's seed.

Rungs, per design-note.md §3 -- fine-grained only:
  g1  gpt-5.2,          natural verbosity   (the baseline system)
  g3  claude-opus-4-8,  natural verbosity   (cross-vendor)

The structured walk is excluded: off-key recovery is UNDEFINED for generators whose items
cover multiple key points (deviation D14). Volume-normalised rungs are excluded: matched
volume pushes both vendors into the padding regime, which the parent study measured.

Resumable by construction -- one file per (case, rung, replicate), existing files skipped.
The workspace spend cap has silently truncated batch runs on this project before; this
harness resumes instead of restarting.

Usage:
  ./generate_miss.py --rungs g1,g3 -n 2
"""
import argparse, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))
RUNS = os.path.abspath(os.path.join(HERE, "..", "runs"))
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

MODELS = {"g1": "gpt-5.2", "g3": "claude-opus-4-8"}

SYS = ("You are reviewing a matter pending before a court, from the case file. List EVERY "
       "distinct legal issue or consideration the court must address to decide it "
       "correctly. Be exhaustive; include considerations that are easy to overlook. "
       'Return JSON: {"issues":[{"label":"<8 words max>","why":"<1 sentence>"}]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rungs", default="g1,g3")
    ap.add_argument("-n", type=int, default=2, help="replicates per case per rung")
    ap.add_argument("--limit", type=int, default=0, help="0 = all cases")
    ap.add_argument("--cases", default=os.path.join(CORPUS, "cases.json"))
    a = ap.parse_args()

    cases = json.load(open(a.cases))["cases"]
    ids = sorted(cases)
    if a.limit:
        ids = ids[:a.limit]
    os.makedirs(RUNS, exist_ok=True)

    rungs = a.rungs.split(",")
    total = len(ids) * len(rungs) * a.n
    print(f"cases {len(ids)}   rungs {rungs}   replicates {a.n}   = {total} generations")
    print("the generator sees the SITUATION only -- never the seed, key, or holding\n")

    done = skipped = 0
    for cid in ids:
        c = cases[cid]
        for rung in rungs:
            model = MODELS[rung]
            for r in range(1, a.n + 1):
                path = os.path.join(RUNS, f"{cid}.{rung}.r{r}.json")
                if os.path.exists(path):
                    skipped += 1
                    continue
                t0 = time.time()
                try:
                    out = (gpt_json(model, SYS, c["situation"]) if model.startswith("gpt")
                           else claude_json(model, SYS, c["situation"], max_tokens=8000))
                except Exception as e:  # noqa: BLE001 - keep going; resume covers the gap
                    print(f"  {cid} {rung} r{r}  ERROR {str(e)[:80]}")
                    continue
                items = out.get("issues", [])
                json.dump({"cluster_id": cid, "case_name": c.get("case_name"),
                           "court": c.get("court"), "date_filed": c.get("date_filed"),
                           "rung": rung, "generator": model, "replicate": r,
                           "raw": out},
                          open(path, "w"), indent=2)
                done += 1
                print(f"  {cid} {rung} r{r}  {len(items):>3} items  "
                      f"({time.time()-t0:>4.0f}s)  {done+skipped}/{total}", flush=True)

    print(f"\ngenerated {done}, reused {skipped}, of {total}")
    print("next: ./score_seed.py")


if __name__ == "__main__":
    main()
