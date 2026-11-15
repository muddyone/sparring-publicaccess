#!/usr/bin/env python3
"""Score a generator run in both directions: recall against the key, yield over what it emitted.

Implements scoring-design.md. Two passes with DELIBERATELY DIFFERENT information sets:

  Pass A (matching)      sees items + the answer key   -> weighted recall
  Pass B (adjudication)  sees items + the fact pattern -> yield / noise / off-key discovery
                         and NEVER the answer key

Pass B's blindness is the whole point. Show it the key and it will mark everything off-key
as unsound, the key becomes the definition of soundness, and the study loses its ability to
find a real issue the examiners chose not to grade.

The key then doubles as a positive control: every key point is a known-material item, so a
blind judge that fails to rate key-covered items as signal is a broken judge, and we find
that out from inside the run (scoring-design.md §5).

Usage:
  ./score_pair.py --run <generator_output.json> [-k 3] [--out scored.json]
"""
import argparse, json, os, statistics, sys

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

GPT = "gpt-5.2"
CLAUDE = "claude-opus-4-8"   # pinned: the model this project's harness has run against

# --------------------------------------------------------------------------- Pass A

PASS_A_SYS = """You are matching a candidate issue list against an examiner's answer key.

For EACH key point, decide whether the candidate list contains an item that addresses it.
Wording will differ; judge substance, not phrasing. A candidate item stated more narrowly
or more broadly still counts if it puts the key point's question in play.

Return JSON:
{"matches":[{"key_id":"<id>","covered":true|false,"by":[<candidate indices>],"note":"<8 words>"}]}
Every key point must appear exactly once."""


def pass_a(items, gold, k, model):
    cand = "\n".join(f"[{i}] {it}" for i, it in enumerate(items))
    key = "\n".join(f"{g['point_id']} ({g['weight_pct']}%): {g['issue'] or g['point']}"
                    for g in gold)
    user = f"CANDIDATE ISSUE LIST\n{cand}\n\nEXAMINER KEY POINTS\n{key}"
    reps = []
    for r in range(k):
        out = (gpt_json(model, PASS_A_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_A_SYS, user))
        reps.append({norm_id(m["key_id"]): {"covered": bool(m.get("covered")),
                                   "by": [int(x) for x in (m.get("by") or [])
                                          if isinstance(x, (int, str)) and str(x).isdigit()]}
                     for m in out.get("matches", [])})
    return reps


# --------------------------------------------------------------------------- Pass B

PASS_B_SYS = """You are auditing a candidate issue list against a law-school fact pattern.
You are NOT given an answer key. Judge each item against the facts alone.

For EACH item return four judgments:
  sound     - is this a real, correctly stated legal issue?
  raised    - do THESE facts actually put it in play (not merely adjacent doctrine)?
  material  - could resolving it either way change the analysis or outcome?
  duplicate_of - index of an EARLIER item this restates at a different granularity, else null

Anchors:
  sound=false     : misstates the law, or is not a legal issue at all
  raised=false    : real doctrine, but nothing in these facts triggers it
  material=false  : real and raised, but resolving it cannot move the analysis
  duplicate_of=i  : same underlying question as item i, differently sliced

Return JSON:
{"audit":[{"i":<index>,"sound":bool,"raised":bool,"material":bool,"duplicate_of":<int|null>}]}
Every item must appear exactly once."""


def pass_b(items, fact_pattern, k, model):
    cand = "\n".join(f"[{i}] {it}" for i, it in enumerate(items))
    user = f"FACT PATTERN\n{fact_pattern}\n\nCANDIDATE ISSUE LIST\n{cand}"
    reps = []
    for r in range(k):
        out = (gpt_json(model, PASS_B_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_B_SYS, user))
        reps.append({int(a["i"]): a for a in out.get("audit", []) if "i" in a})
    return reps


# --------------------------------------------------------------------------- aggregate

def norm_id(x):
    """Key ids round-trip through the model with punctuation stripped or added:
    we send "(1)(a)", it answers "1(a)". Compare on alphanumerics only. Without
    this every key point reads as MISS and recall silently reports 0.00."""
    return "".join(c for c in str(x) if c.isalnum()).lower()


def majority(reps, key, field=None):
    """Majority vote across replicates; returns (verdict, unanimity 0..1)."""
    vals = []
    for r in reps:
        v = r.get(key)
        if v is None:
            continue
        vals.append(bool(v if field is None else v.get(field)))
    if not vals:
        return None, 0.0
    t = sum(vals)
    return (t * 2 >= len(vals)), max(t, len(vals) - t) / len(vals)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="generator output json")
    ap.add_argument("-k", type=int, default=3, help="replicates per pass")
    ap.add_argument("--match-model", default=GPT)
    ap.add_argument("--audit-model", default=CLAUDE,
                    help="cross-vendor from the generator by default")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    run = json.load(open(a.run))
    items = [i["label"] for i in run["raw"]["issues"]]
    gold = run["gold"]["gold"]

    # Committed run artifacts have the NCBE fact pattern stripped (copyrighted).
    # Re-read it from the local, gitignored corpus so a committed run stays
    # reproducible without redistributing the source text.
    fact = run["question"].get("text", "")
    if fact.startswith("<NCBE fact pattern withheld"):
        qpath = os.path.join(HERE, "..", "corpus", "questions.json")
        if not os.path.exists(qpath):
            sys.exit("fact pattern withheld and no local corpus -- run "
                     "scripts/fetch_corpus.sh then scripts/extract_questions.py")
        qs = json.load(open(qpath))["questions"]
        hit = [q for q in qs
               if q["administration"] == run["question"]["administration"]
               and q["subject"] == run["question"]["subject"]]
        if not hit:
            sys.exit(f"fact pattern not found in local corpus: "
                     f"{run['question']['administration']} / {run['question']['subject']}")
        fact = hit[0]["text"]

    print(f"fact pattern : {run['question']['administration']} / {run['question']['subject']}")
    print(f"generator    : {run['generator']}  -> {len(items)} items")
    print(f"key          : {len(gold)} weighted points")
    print(f"match model  : {a.match_model}   audit model: {a.audit_model}   k={a.k}\n")

    A = pass_a(items, gold, a.k, a.match_model)
    B = pass_b(items, fact, a.k, a.audit_model)

    # ---- direction 1: weighted recall
    covered, rec_unan = {}, []
    for g in gold:
        v, u = majority(A, norm_id(g["point_id"]), "covered")
        covered[g["point_id"]] = bool(v)
        rec_unan.append(u)

    # Which emitted items did the matcher actually cite for a covered key point?
    # Majority across replicates: an item counts as key-matched if it was cited for
    # some covered key point in at least half the passes.
    cite_counts, per_key = {}, {}
    for rep in A:
        cited = set()
        for kid, m in rep.items():
            if m["covered"]:
                cited.update(m["by"])
                per_key.setdefault(kid, {})
                for i in m["by"]:
                    per_key[kid][i] = per_key[kid].get(i, 0) + 1
        for i in cited:
            cite_counts[i] = cite_counts.get(i, 0) + 1
    matched_idx = {i for i, c in cite_counts.items() if c * 2 >= len(A)}
    wr = sum(g["weight_pct"] for g in gold if covered[g["point_id"]]) / 100.0

    # ---- direction 2: yield over what was emitted
    verdicts = {}
    for i in range(len(items)):
        s, us = majority(B, i, "sound")
        r, ur = majority(B, i, "raised")
        m, um = majority(B, i, "material")
        dupes = [rep[i].get("duplicate_of") for rep in B
                 if i in rep and rep[i].get("duplicate_of") is not None]
        is_dup = len(dupes) * 2 >= a.k
        verdicts[i] = {"item": items[i], "sound": s, "raised": r, "material": m,
                       "duplicate": is_dup,
                       "signal": bool(s and r and m and not is_dup),
                       "unanimity": round(statistics.mean([us, ur, um]), 3)}

    E = len(items)
    S = [i for i, v in verdicts.items() if v["signal"]]
    noise = [i for i, v in verdicts.items() if not (v["sound"] and v["raised"])]
    dups = [i for i, v in verdicts.items() if v["duplicate"]]
    # Off-key discovery: signal items the matcher never cited for any key point --
    # sound, raised, material, non-duplicate issues the examiners did not grade. This
    # is the quantity the original design could not take, and it is why the second
    # direction exists.
    offkey = [i for i in S if i not in matched_idx]

    print("--- direction 1: recall against the key ---")
    for g in gold:
        mark = "HIT " if covered[g["point_id"]] else "MISS"
        print(f"  {mark} {g['point_id']:<7} {g['weight_pct']:>3}%  {(g['issue'] or '')[:70]}")
    print(f"  weighted recall : {wr:.2f}   mean unanimity {statistics.mean(rec_unan):.2f}")

    print("\n--- direction 2: yield over what it emitted ---")
    print(f"  emitted         : {E}")
    print(f"  signal          : {len(S):>3}   yield        {len(S)/E:.2f}")
    print(f"  noise (unsound/unraised) : {len(noise):>3}   noise rate   {len(noise)/E:.2f}")
    print(f"  duplicates      : {len(dups):>3}   redundancy   {len(dups)/E:.2f}")
    print(f"  off-key signal  : {len(offkey):>3}   discovery    {len(offkey)/E:.2f}"
          "   <- sound+material, ungraded by the examiners")
    print(f"  mean unanimity  : {statistics.mean(v['unanimity'] for v in verdicts.values()):.2f}")

    # ---- positive control: does the blind judge rate KEY-COVERED items as signal?
    # Approximated on the items pass A cited most often; reported with its own caveat.
    # Positive control: every key point is a KNOWN-material item, so the blind judge
    # (which never saw the key) must rate the items that cover them as signal. If it
    # does not, its judgment is broken and the yield numbers above are worthless --
    # detected from inside the run, before anything is concluded.
    # Positive control, respecified after the first run (scoring-design.md §5).
    #
    # The first version asked whether EVERY key-matched item was signal, and it
    # failed at 0.50 -- correctly, for the wrong reason. When 17 emitted items all
    # cover one key point, 16 of them ARE duplicates, and the blind judge saying so
    # is right. Deduplication is orthogonal to whether the judge can recognise a
    # known-material issue.
    #
    # The question that actually tests the judge: for each key point, does AT LEAST
    # ONE item covering it get rated sound + raised + material? The duplicate flag is
    # ignored here by design.
    print("\n--- positive control: is the blind judge trustworthy? ---")
    print("  for each key point, >=1 covering item must be rated sound+raised+material")
    ctrl_rows, ctrl_ok = [], 0
    for g in gold:
        kid = norm_id(g["point_id"])
        cites = [i for i, c in per_key.get(kid, {}).items() if c * 2 >= len(A)]
        good = [i for i in cites
                if verdicts.get(i, {}).get("sound")
                and verdicts.get(i, {}).get("raised")
                and verdicts.get(i, {}).get("material")]
        ok = bool(good)
        ctrl_ok += ok
        ctrl_rows.append({"key": g["point_id"], "cited": len(cites),
                          "recognised": len(good), "ok": ok})
        print(f"    {'ok  ' if ok else 'FAIL'} {g['point_id']:<7} "
              f"cited by {len(cites):>2} item(s), {len(good):>2} recognised as material")
    ctrl = ctrl_ok / len(gold) if gold else None
    print(f"  control: {ctrl_ok}/{len(gold)} = {ctrl:.2f}   floor 0.90  -> "
          f"{'PASS' if ctrl >= 0.90 else 'FAIL'}")
    if ctrl < 0.90:
        print("  the audit pass is not reliable enough to interpret; rebuild before use.")

    # Cross-pass disagreement is itself a result: Pass A (sees the key) says an item
    # covers a key point while Pass B (blind) says the facts do not even raise it.
    # That pattern means the matcher is being generous, which inflates recall.
    conflict = [i for i in matched_idx if not verdicts.get(i, {}).get("raised")]
    print(f"\n  cross-pass conflict: {len(conflict)}/{len(matched_idx)} items the matcher "
          f"credited\n  are rated 'not raised by these facts' by the blind judge"
          f" -- matcher generosity,\n  which inflates recall. Reported, not corrected.")

    out = a.out or a.run.replace(".json", ".scored.json")
    json.dump({"weighted_recall": wr, "covered": covered,
               "emitted": E, "signal": len(S), "yield": len(S) / E,
               "noise": len(noise), "duplicates": len(dups),
               "offkey_signal": len(offkey), "offkey_discovery": len(offkey) / E,
               "positive_control": ctrl, "control_rows": ctrl_rows,
               "key_matched": sorted(matched_idx), "cross_pass_conflict": len(conflict),
               "verdicts": verdicts, "k": a.k,
               "match_model": a.match_model, "audit_model": a.audit_model},
              open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
