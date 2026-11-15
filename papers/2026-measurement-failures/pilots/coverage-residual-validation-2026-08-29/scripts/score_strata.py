#!/usr/bin/env python3
"""Is run-to-run variance LOST COVERAGE or CHURN?

The same-system floor (self-residual-floor.md) found that one run delivers ~70% of what
the system surfaces across five, and that a fifth of the pooled issues appeared in exactly
ONE run. Those singletons are either genuine rare insight or sampling garbage, and the
answer changes what the floor means:

  singletons mostly SIGNAL -> the variance is lost coverage. Re-running the same model is
                              a real coverage intervention, and possibly a cheaper one
                              than reaching for a second vendor.
  singletons mostly NOISE  -> the variance is churn. The 0.70 figure overstates the loss,
                              the stable core is close to the system's real reach, and the
                              floor must be read down before any cross-vendor comparison
                              uses it.

METHOD -- the comparison is the measurement, and the blinding is what makes it honest.

A singleton signal rate on its own means nothing: without a reference we cannot tell
"40% is bad" from "40% is what this generator's output looks like everywhere." So the
STABLE CORE (issues every run found) is scored as a control in the same pass.

Both strata go to the judge as ONE shuffled list. The judge never learns which stratum an
item came from, or that strata exist. Scoring them separately -- or in order -- would let
the judge infer the hypothesis from the batch, which is the cheapest possible way to get
the answer we went looking for.

Judgments are the ones already defined in scoring-design.md §3: sound / raised / material,
against the fact pattern alone, never the answer key.

Usage:
  ./score_strata.py --residual runs/<...>.self-residual.json [-k 3]
"""
import argparse, json, os, random, statistics, sys

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

JUDGE = "claude-opus-4-8"     # cross-vendor from the gpt-5.2 generator

# Identical to score_pair.py's Pass B, minus duplicate detection: these items are already
# deduplicated (they ARE consensus clusters), so a duplicate judgment would be meaningless.
SYS = """You are auditing a list of candidate legal issues against a law-school fact
pattern. You are NOT given an answer key. Judge each item against the facts alone.

For EACH item return three judgments:
  sound    - is this a real, correctly stated legal issue?
  raised   - do THESE facts actually put it in play (not merely adjacent doctrine)?
  material - could resolving it either way change the analysis or outcome?

Anchors:
  sound=false    : misstates the law, or is not a legal issue at all
  raised=false   : real doctrine, but nothing in these facts triggers it
  material=false : real and raised, but resolving it cannot move the analysis

Return JSON:
{"audit":[{"i":<index>,"sound":bool,"raised":bool,"material":bool}]}
Every item must appear exactly once."""


def majority(reps, i, field):
    vals = [bool(r[i][field]) for r in reps if i in r and field in r[i]]
    if not vals:
        return None, 0.0
    t = sum(vals)
    return (t * 2 >= len(vals)), max(t, len(vals) - t) / len(vals)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--residual", required=True)
    ap.add_argument("-k", type=int, default=3)
    ap.add_argument("--judge", default=JUDGE)
    ap.add_argument("--seed", type=int, default=20260829)
    ap.add_argument("--out", default=None)
    ap.add_argument("--reread", action="store_true",
                    help="recompute the verdict from a saved .strata.json without "
                         "new model calls -- same data, corrected interpretation")
    a = ap.parse_args()

    if a.reread:
        d = json.load(open(a.residual))
        stats, gap, rows = d["stats"], d["gap"], d["rows"]
        print(f"REREAD (no model calls) : {d['fact_pattern']}   judge {d['judge']}  k={d['k']}")
        print(f"{'stratum':<11} {'n':>3} {'signal':>7} {'rate':>6}  "
              f"{'unsound':>8} {'unraised':>9} {'immaterial':>11}")
        for st in ("core", "singleton"):
            z = stats[st]
            print(f"{st:<11} {z['n']:>3} {z['signal']:>7} {z['rate']:>6.2f}  "
                  f"{z['unsound']:>8} {z['unraised']:>9} {z['immaterial']:>11}")
        print(f"\n  gap : {gap:+.2f}")
        print("\n--- reading ---")
        print("  judge validation is the key-based control (score_pair.py), not the core rate.")
        print(f"  core rate {stats['core']['rate']:.2f} is the reference distribution.")
        if gap <= 0.15:
            print("  LOST COVERAGE: singletons score close to the core. Re-running the same")
            print("  model surfaces real issues; the floor stands as measured.")
        elif gap >= 0.35:
            print("  CHURN: singletons score far below the core. The single-run coverage")
            print("  figure overstates the loss; read the floor down.")
        else:
            print("  MIXED: singletons are meaningfully worse than the core but not noise.")
            print("  The floor is part real coverage, part churn -- report both rates,")
            print("  never a single corrected number.")
        sig = sum(1 for r in rows if r["stratum"] == "singleton" and r["signal"])
        n = stats["singleton"]["n"]
        print(f"\n  concretely: {sig} of {n} issues that only ONE run found were sound,")
        print(f"  raised, and material. A single run missed {sig} real material issues")
        print("  that a rerun of the same model caught.")
        return

    res = json.load(open(a.residual))
    clusters = res["clusters"]
    if "representative" not in clusters[0]:
        sys.exit("this artifact predates cluster-content persistence; re-run self_residual.py")

    strata = {"singleton": [c for c in clusters if c["stratum"] == "singleton"],
              "core": [c for c in clusters if c["stratum"] == "core"]}
    if not strata["singleton"] or not strata["core"]:
        sys.exit(f"need both strata; got "
                 f"{ {k: len(v) for k, v in strata.items()} }")

    # Rehydrate the fact pattern from the gitignored corpus (never committed).
    run0 = json.load(open(os.path.join(os.path.dirname(a.residual),
                                       res["runs"][0]["path"])))
    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    q = next(x for x in qs
             if x["administration"] == run0["question"]["administration"]
             and x["subject"] == run0["question"]["subject"])

    # ---- one shuffled list; the judge cannot tell the strata apart ----
    pool = ([{"stratum": "singleton", "label": c["representative"]}
             for c in strata["singleton"]] +
            [{"stratum": "core", "label": c["representative"]}
             for c in strata["core"]])
    random.Random(a.seed).shuffle(pool)

    print(f"fact pattern : {q['administration']} / {q['subject']}")
    print(f"judge        : {a.judge}  (cross-vendor from the generator)   k={a.k}")
    print(f"scoring      : {len(strata['singleton'])} singleton + "
          f"{len(strata['core'])} core = {len(pool)} items, shuffled together\n")

    listing = "\n".join(f"[{i}] {p['label']}" for i, p in enumerate(pool))
    user = f"FACT PATTERN\n{q['text']}\n\nCANDIDATE ISSUES\n{listing}"
    reps = []
    for r in range(a.k):
        out = (gpt_json(a.judge, SYS, user) if a.judge.startswith("gpt")
               else claude_json(a.judge, SYS, user, max_tokens=8000))
        reps.append({int(x["i"]): x for x in out.get("audit", []) if "i" in x})

    rows = []
    for i, p in enumerate(pool):
        s, us = majority(reps, i, "sound")
        rr, ur = majority(reps, i, "raised")
        m, um = majority(reps, i, "material")
        rows.append({**p, "sound": s, "raised": rr, "material": m,
                     "signal": bool(s and rr and m),
                     "unanimity": round(statistics.mean([us, ur, um]), 3)})

    print(f"{'stratum':<11} {'n':>3} {'signal':>7} {'rate':>6}  "
          f"{'unsound':>8} {'unraised':>9} {'immaterial':>11}")
    stats = {}
    for st in ("core", "singleton"):
        g = [r for r in rows if r["stratum"] == st]
        sig = [r for r in g if r["signal"]]
        stats[st] = {
            "n": len(g), "signal": len(sig), "rate": len(sig) / len(g),
            "unsound": sum(1 for r in g if not r["sound"]),
            "unraised": sum(1 for r in g if not r["raised"]),
            "immaterial": sum(1 for r in g if not r["material"]),
            "unanimity": statistics.mean(r["unanimity"] for r in g)}
        z = stats[st]
        print(f"{st:<11} {z['n']:>3} {z['signal']:>7} {z['rate']:>6.2f}  "
              f"{z['unsound']:>8} {z['unraised']:>9} {z['immaterial']:>11}")

    gap = stats["core"]["rate"] - stats["singleton"]["rate"]
    print(f"\n  core signal rate      : {stats['core']['rate']:.2f}   (the control)")
    print(f"  singleton signal rate : {stats['singleton']['rate']:.2f}")
    print(f"  gap                   : {gap:+.2f}")
    print(f"  mean unanimity        : "
          f"{statistics.mean(r['unanimity'] for r in rows):.2f}")

    print("\n--- reading ---")
    # The stable core is a REFERENCE DISTRIBUTION, not a gold standard. "All five runs
    # said it" does not mean "it is material" -- and on the first run the four core
    # items rated non-signal were all sound-but-inapplicable ("waiver of disclosure"
    # where the party did disclose; "writing and signature" where nothing is disputed).
    # Those are correct judgments, not judge failures.
    #
    # The judge's validation is the KEY-based control in score_pair.py, where the items
    # ARE known-material by construction because the examiners weighted them. On this
    # fact pattern, with this judge, that control passed at 1.00.
    #
    # The first version of this block demanded core >= 0.90, a threshold transplanted
    # from that key-based control, and it fired at 0.87. Corrected AFTER seeing the
    # number, which is only legitimate because the mis-specification is visible
    # independently of the result. The GAP BANDS BELOW ARE UNCHANGED -- they are what
    # decides the actual question, and they stay where they were pre-committed.
    print(f"  judge validation is the key-based control (score_pair.py), not this rate.")
    print(f"  core rate {stats['core']['rate']:.2f} is the reference distribution: what this")
    print(f"  generator's reliably-repeated output looks like when audited.")
    if gap <= 0.15:
        print("  Singletons score close to the stable core: run-to-run variance is")
        print("  LOST COVERAGE, not churn. Re-running the same model surfaces real")
        print("  issues, and the floor stands as measured.")
    elif gap >= 0.35:
        print("  Singletons score far below the stable core: the variance is largely")
        print("  CHURN. The single-run coverage figure overstates the loss and the floor")
        print("  should be read down before any cross-vendor comparison uses it.")
    else:
        print("  Mixed: singletons are meaningfully worse than the core but not noise.")
        print("  The floor is part real coverage, part churn; report both rates rather")
        print("  than a single corrected number.")

    out = a.out or a.residual.replace(".json", "") + ".strata.json"
    json.dump({"stats": stats, "gap": gap, "rows": rows, "k": a.k,
               "judge": a.judge, "seed": a.seed,
               "fact_pattern": f"{q['administration']} / {q['subject']}"},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
