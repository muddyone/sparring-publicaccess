#!/usr/bin/env python3
"""Positive-control set generator (EXPLORATORY) — manufacture ground truth for ruler calibration.

The de-noise probe showed the absolute flaw-count DV is too NOISY; the pairwise probe showed the naive
pairwise judge is QUIET but pro-revision BIASED (candidate "better" 96%). Neither is trustworthy, and we
have no oracle to say which is right. This builds one: controlled (champion, candidate) pairs whose
correct verdict we KNOW by construction, so any candidate ruler can be scored on whether it recovers
ground truth — especially: does it catch a planted regression, and does it call a no-op EQUIVALENT
(the direct bias test).

Four control types per base problem (the 8 §6.3 originals, R0):
  - identical          : (R0, R0)                          -> EQUIVALENT   (pure position/verbosity-bias test)
  - cosmetic           : (R0, reworded R0, no substance)   -> EQUIVALENT   (verbosity/effort-bias test)
  - planted_regression : (R0, R0 + one injected material flaw) -> A_BETTER  (champion better; candidate worse)
  - planted_improvement: (R0, R0 with one KNOWN flaw fixed)     -> B_BETTER  (candidate better)

Records the exact change (injected/fixed flaw text) so the ground truth is auditable. Resumable: each
generated variant caches to runs/ctrl__<pid>__<type>.json. Writes analysis/positive-control-set.json.

This script only GENERATES the set. Scoring rulers against it (flaw-count DV, raw pairwise, counter-framed
pairwise, challenge-enumerated pairwise) is the follow-on bake-off.

Usage: python3 control_set.py            # ~24 generation calls, resumable
Env: ANTHROPIC_API_KEY in the environment.
"""
import json, argparse
import concurrent.futures as cf
import run_study as R
import lib_llm as L

GEN_MAXTOK = 9000   # full recs can be long (run_study used 9000 for R3 producer)

INJECT_SYS = (
    "You are stress-testing an evaluation harness. Take the recommendation below and introduce EXACTLY ONE "
    "clear, material, would-ship flaw — an error that would change the decision or ship a real defect "
    "(e.g., violate a constraint the problem explicitly states, reverse a correct tradeoff, or insert a "
    "wrong number/mechanism). Change NOTHING ELSE — keep length, structure, and all other content as close "
    "to identical as possible; the ONLY substantive difference must be the one flaw you introduce. Do not "
    "fix or improve anything. Report the flaw you introduced in one concrete sentence."
)
INJECT_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION (introduce exactly one material flaw, change nothing else):\n{rec}\n\n"
    "Return JSON: {{\"flawed_recommendation\": str, \"injected_flaw\": str}}"
)

FIX_SYS = (
    "You are stress-testing an evaluation harness. The recommendation below has a known material flaw. "
    "Revise it to fix ONLY that one flaw — change nothing else, keep length/structure/all other content as "
    "close to identical as possible, and do NOT introduce any new flaw or improve anything unrelated. The "
    "only substantive difference must be that the named flaw is resolved. Report what you changed in one sentence."
)
FIX_USER = (
    "PROBLEM:\n{problem}\n\nKNOWN FLAW TO FIX (fix only this):\n{flaw}\n\nRECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"fixed_recommendation\": str, \"fix_note\": str}}"
)

COSMETIC_SYS = (
    "You are stress-testing an evaluation harness. Reword the recommendation below for style ONLY — rephrase "
    "sentences, vary wording, you may make it somewhat longer — but make ZERO substantive change: every "
    "decision, number, tradeoff, caveat, and material claim must be preserved exactly. No flaw added, none "
    "fixed. The two versions must be materially equivalent; only the prose differs."
)
COSMETIC_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION (reword for style only, no substantive change):\n{rec}\n\n"
    "Return JSON: {{\"reworded_recommendation\": str}}"
)

TYPES = ["identical", "cosmetic", "planted_regression", "planted_improvement"]
GT = {"identical": "EQUIVALENT", "cosmetic": "EQUIVALENT",
      "planted_regression": "A_BETTER", "planted_improvement": "B_BETTER"}


def gen_variant(pid, typ):
    """Return (text_b, change_note) for the variant; A is always R0[pid]. Cached/resumable."""
    uid = f"ctrl__{pid}__{typ}"
    cached = R.load(uid)
    if cached:
        return cached
    problem = R.PROBLEMS[pid]["problem"]
    base = R.R0[pid]
    if typ == "identical":
        rec = {"unit": uid, "pid": pid, "type": typ, "text_b": base, "change_note": "identical to A"}
    elif typ == "cosmetic":
        out = L.claude_json(R.CLAUDE, COSMETIC_SYS, COSMETIC_USER.format(problem=problem, rec=base), max_tokens=GEN_MAXTOK)
        rec = {"unit": uid, "pid": pid, "type": typ, "text_b": out["reworded_recommendation"],
               "change_note": "style reword, no substantive change"}
    elif typ == "planted_regression":
        out = L.claude_json(R.CLAUDE, INJECT_SYS, INJECT_USER.format(problem=problem, rec=base), max_tokens=GEN_MAXTOK)
        rec = {"unit": uid, "pid": pid, "type": typ, "text_b": out["flawed_recommendation"],
               "change_note": out.get("injected_flaw", "")}
    elif typ == "planted_improvement":
        denom = R.DENOM[pid]
        flaw = denom[0] if denom else None
        if not flaw:
            rec = {"unit": uid, "pid": pid, "type": typ, "text_b": None, "change_note": "SKIP: no known flaw"}
        else:
            out = L.claude_json(R.CLAUDE, FIX_SYS, FIX_USER.format(problem=problem, flaw=flaw, rec=base), max_tokens=GEN_MAXTOK)
            rec = {"unit": uid, "pid": pid, "type": typ, "text_b": out["fixed_recommendation"],
                   "change_note": out.get("fix_note", ""), "fixed_flaw": flaw}
    else:
        raise ValueError(typ)
    R.save(uid, rec)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    jobs = [(pid, typ) for pid in R.PIDS for typ in TYPES]
    print(f"[ctrl] {len(R.PIDS)} problems x {len(TYPES)} types = {len(jobs)} control pairs", flush=True)
    if args.dry:
        for pid, typ in jobs:
            print(f"  {pid:28s} {typ:20s} -> {GT[typ]}")
        return
    # generate (resumable, parallel)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(gen_variant, pid, typ): (pid, typ) for (pid, typ) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[ctrl] ERROR {futs[f]}: {repr(e)[:150]}", flush=True)
            done += 1
            print(f"[ctrl] generated {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[ctrl] {errs} errors -- re-run to retry (resumable).", flush=True)

    # assemble manifest
    pairs, missing = [], 0
    for pid in R.PIDS:
        for typ in TYPES:
            rec = R.load(f"ctrl__{pid}__{typ}")
            if not rec or rec.get("text_b") is None:
                missing += 1
                continue
            pairs.append({
                "pair_id": f"{pid}__{typ}", "pid": pid, "type": typ,
                "ground_truth": GT[typ],
                "text_a": R.R0[pid], "text_b": rec["text_b"],
                "change_note": rec.get("change_note", ""),
                "fixed_flaw": rec.get("fixed_flaw"),
            })
    manifest = {
        "EXPLORATORY": True,
        "purpose": "constructed ground truth to calibrate correctness rulers (flaw-count, pairwise, "
                   "counter-framed pairwise, challenge-enumerated pairwise)",
        "n_pairs": len(pairs), "n_missing": missing,
        "type_counts": {t: sum(1 for p in pairs if p["type"] == t) for t in TYPES},
        "ground_truth_legend": "A=text_a (always R0/base); B=text_b (variant). A_BETTER=champion better; "
                               "B_BETTER=candidate better; EQUIVALENT=no material difference.",
        "pairs": pairs,
    }
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    out = R.PILOT / "analysis" / "positive-control-set.json"
    out.write_text(json.dumps(manifest, indent=2))

    print("\n=== POSITIVE-CONTROL SET (EXPLORATORY) ===")
    print(f"  built {len(pairs)} control pairs (missing: {missing})")
    for t in TYPES:
        print(f"    {t:20s} -> {GT[t]:11s}  x {sum(1 for p in pairs if p['type']==t)}")
    print(f"\n  Next: run candidate rulers on these pairs (order-randomized, replicated), score vs ground_truth.")
    print(f"        The ruler that catches planted regressions AND calls no-ops EQUIVALENT wins.")
    print(f"\nwrote {out.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
