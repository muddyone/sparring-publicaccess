#!/usr/bin/env python3
"""Run a generator against a fact pattern, N times, blind to the answer key.

Generators are the rungs of the independence ladder (design-note.md §4). This script
runs the model-based ones; the structured (G4) and retrieval (G5) rungs are not model
calls and get their own scripts.

  g1  same system, new seed        -- the run-to-run FLOOR. Same model, same prompt,
                                      nothing varied but sampling.
  g3  different vendor, blind      -- the conventional cross-vendor pass.

G1 is the point of this script. Everything downstream is read against it: a
cross-vendor residual only means something above the residual the system already has
against itself. Per Bart's 2026-08-29 decision the floor is REPORTED, not subtracted --
if a single run misses what the same system finds on a rerun, that is a real coverage
failure of single-run use, milder than a systematic blind spot but not noise.

Output is sanitised on write: the NCBE fact pattern is never stored (copyrighted); it is
rehydrated from the gitignored local corpus by whatever consumes the run.

Usage:
  ./generate.py --admin "February 2018" --subject "Family Law" --gen g1 -n 5
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

# The g1 model is the SYSTEM UNDER TEST. g3 must be a different vendor from it, or the
# ladder collapses to one rung and the cross-vendor number means nothing.
MODELS = {"g1": "gpt-5.2", "g3": "claude-opus-4-8",
          # Volume-normalised variants. The uncontrolled cross-vendor run
          # (cross-vendor-null.md) found gpt-5.2 emitting 2.5x more items per run than
          # claude-opus-4-8 on an identical prompt, which leaves "the second vendor added
          # nothing" and "the second vendor said less" indistinguishable. These rungs give
          # BOTH vendors the same explicit item budget so the comparison isolates what a
          # vendor can SEE from how much it happens to SAY.
          "g1n": "gpt-5.2", "g3n": "claude-opus-4-8"}

SYS = ("You are issue-spotting a law-school essay fact pattern. List EVERY distinct legal "
       "issue a complete answer must address. Be exhaustive; include issues that are easy "
       "to overlook. Return JSON: "
       '{"issues":[{"label":"<8 words max>","why":"<1 sentence>"}]}')

# Appended for the volume-normalised rungs. "Do not pad" is deliberate and is not in
# tension with the target: the point is to find out whether a vendor CAN reach the budget
# with real issues. If it pads to hit the number, the blinded stratum scorer will show it
# as fill, and that is a result rather than a contaminated run.
TARGET_SUFFIX = (" Aim for approximately {n} distinct issues, sliced at whatever "
                 "granularity that requires. Do not pad: if you genuinely cannot find "
                 "{n} distinct issues, list fewer.")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admin", required=True, help='e.g. "February 2018"')
    ap.add_argument("--subject", required=True, help='e.g. "Family Law"')
    ap.add_argument("--gen", default="g1", choices=sorted(MODELS))
    ap.add_argument("-n", type=int, default=5, help="replicate runs")
    ap.add_argument("--model", default=None, help="override the generator model")
    ap.add_argument("--target", type=int, default=None,
                    help="explicit item budget, appended to the prompt (volume control)")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "runs"))
    a = ap.parse_args()
    model = a.model or MODELS[a.gen]
    sys_prompt = SYS + (TARGET_SUFFIX.format(n=a.target) if a.target else "")
    if a.gen.endswith("n") and not a.target:
        sys.exit(f"rung {a.gen} is a volume-normalised rung; pass --target N")

    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    gs = json.load(open(os.path.join(HERE, "..", "gold", "gold.json")))["fact_patterns"]
    q = next((x for x in qs if x["administration"] == a.admin
              and x["subject"] == a.subject), None)
    g = next((x for x in gs if x["administration"] == a.admin
              and x["subject"] == a.subject), None)
    if not q or not g:
        sys.exit(f"no such fact pattern: {a.admin} / {a.subject}")

    os.makedirs(a.outdir, exist_ok=True)
    base = f"{slug(a.admin)}-{slug(a.subject)}.{a.gen}"
    print(f"fact pattern : {a.admin} / {a.subject}  ({q['chars']} chars)")
    print(f"generator    : {a.gen} = {model}   replicates: {a.n}"
          + (f"   target: ~{a.target} items" if a.target else ""))
    print(f"key          : {g['n_gold']} weighted points (NOT shown to the generator)\n")

    written = []
    for r in range(1, a.n + 1):
        t0 = time.time()
        out = (gpt_json(model, sys_prompt, q["text"]) if model.startswith("gpt")
               else claude_json(model, sys_prompt, q["text"], max_tokens=8000))
        items = out.get("issues", [])
        # Sanitised question stub -- the fact pattern text is deliberately absent.
        stub = {k: v for k, v in q.items() if k != "text"}
        stub["text"] = ("<NCBE fact pattern withheld -- copyrighted. Rebuild with "
                        "scripts/fetch_corpus.sh + scripts/extract_questions.py>")
        path = os.path.join(a.outdir, f"{base}.r{r}.json")
        json.dump({"question": stub, "gold": g, "generator": model,
                   "rung": a.gen, "replicate": r, "target": a.target, "raw": out},
                  open(path, "w"), indent=2)
        written.append(path)
        print(f"  r{r}: {len(items):>3} items  ({time.time()-t0:.0f}s)  -> {os.path.basename(path)}")

    counts = []
    for p in written:
        counts.append(len(json.load(open(p))["raw"].get("issues", [])))
    print(f"\nitem counts across {a.n} runs of the SAME system: {counts}")
    print(f"  min {min(counts)}  max {max(counts)}  spread {max(counts)-min(counts)}")
    print("\nnext: ./self_residual.py --glob "
          f"'runs/{base}.r*.json'")


if __name__ == "__main__":
    main()
