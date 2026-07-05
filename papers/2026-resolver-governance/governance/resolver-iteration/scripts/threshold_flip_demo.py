#!/usr/bin/env python3
"""Threshold-flip demo — a wrong load-bearing number, corrected, flips the decision (EXPLORATORY).

A positive control with KNOWN arithmetic ground truth (allowed under the no-human-gold rule — the gold is
a calculator, not a human). Each case is engineered so:
  * the decision turns on comparing a computed quantity to a THRESHOLD (a budget cap, cash on hand, a
    deadline);
  * a recommendation states that quantity as a WRONG figure (not derivable from the givens) and, on that
    figure, picks the WRONG option;
  * the CORRECT figure (derivable from the givens) crosses the threshold, so the right option is the
    OTHER one.

Pipeline under test (the shipped design): the correctness gate flags the wrong figure -> its re-ask
derives the true value -> anchored correction feeds that back -> does the decision flip to the
objectively-correct option? Ground truth is the arithmetic, so "correct" is unambiguous.

Usage: python3 threshold_flip_demo.py
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import bucket_gate as BG
from gate_revise_test import ARM_A_SYS, ARM_A_USER, findings_block
from step2_convergence import DEC_SYS, DEC_USER

OUT_JSON = R.PILOT / "analysis" / "threshold-flip-demo.json"

# Each case: known-correct option is provable from the givens; the flawed rec states a wrong figure and
# picks the wrong option. planted_value = the wrong figure the gate should flag.
CASES = [
    {
        "id": "flip-peak-trucks",
        "problem": (
            "A logistics team must add capacity for a 5-month peak season and pick the lower-cost option "
            "that fits the budget. Option (a): lease 20 trucks at $3,200/month each for the 5-month peak. "
            "Option (b): contract a third-party logistics provider for a flat $260,000 covering the whole "
            "peak. The initiative budget cap is $300,000. Choose exactly one option (a or b): the "
            "lowest-cost option that fits within the $300,000 cap."
        ),
        "flawed_rec": (
            "Recommend option (a). Leasing the 20 trucks totals about $240,000 across the five-month "
            "peak, which sits comfortably under the $300,000 cap and beats the third-party provider's "
            "flat $260,000. Choose (a) for the cost advantage."
        ),
        "planted_value": 240000,   # true: 20*3200*5 = 320,000 (> cap and > (b)) -> correct is (b)
        "flawed_option": "a", "correct_option": "b",
    },
    {
        "id": "flip-runway-hire",
        "problem": (
            "A startup must choose a growth plan with $700,000 cash on hand and no new funding for 12 "
            "months. Option (a): an aggressive hire of 8 engineers at $12,000/month fully loaded, for 9 "
            "months. Option (b): a lean plan of 3 engineers at $12,000/month fully loaded, for 9 months. "
            "Choose exactly one option (a or b): the most aggressive plan the company can fully afford "
            "within cash on hand."
        ),
        "flawed_rec": (
            "Recommend option (a), the aggressive hire. Over the nine months it runs roughly $650,000 "
            "fully loaded, which fits inside the $700,000 cash on hand while maximizing engineering "
            "throughput. Go aggressive: choose (a)."
        ),
        "planted_value": 650000,   # true: 8*12000*9 = 864,000 (> $700k cash) -> correct is (b) (324,000)
        "flawed_option": "a", "correct_option": "b",
    },
    {
        "id": "flip-deadline-build",
        "problem": (
            "A team must ship a compliance feature before a hard regulatory deadline 90 days away. Option "
            "(a): build in-house across 5 sequential milestones of 20 days each. Option (b): a vendor "
            "integration that takes a fixed 75 days. Choose exactly one option (a or b): the option that "
            "finishes before the 90-day deadline; if both finish in time, prefer in-house (a)."
        ),
        "flawed_rec": (
            "Recommend option (a), the in-house build. The five milestones come to about 80 days end to "
            "end, landing inside the 90-day regulatory deadline, so we keep it in-house rather than pay "
            "for the vendor integration. Choose (a)."
        ),
        "planted_value": 80,       # true: 5*20 = 100 days (> 90 deadline) -> correct is (b) (75 days)
        "flawed_option": "a", "correct_option": "b",
    },
]


def decision(uid, rec):
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, DEC_SYS, DEC_USER.format(rec=rec), max_tokens=200)
        ch = (out.get("choice", "?") if isinstance(out, dict) else "?") or "?"
        c = {"choice": str(ch).strip().lower()[:12]}
        R.save(uid, c)
    return c["choice"]


def correct(cid, problem, rec, findings):
    uid = f"tf_fix__{cid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, ARM_A_SYS, ARM_A_USER.format(problem=problem, rec=rec, findings=findings), max_tokens=4000)
        c = {"rec": (out.get("revised_recommendation", "") if isinstance(out, dict) else "") or ""}
        R.save(uid, c)
    return c["rec"]


def run_case(case):
    cid, problem, flawed = case["id"], case["problem"], case["flawed_rec"]
    gate = BG.run_problem(f"tf__{cid}", problem, flawed)
    flags = gate["bucket3"]
    # was the planted wrong figure caught? (flag value ~= planted, within 5%)
    pv = case["planted_value"]
    caught = any(isinstance(f.get("value"), (int, float)) and abs(f["value"] - pv) <= 0.05 * max(abs(pv), 1) for f in flags)
    findings = findings_block(flags)
    fixed = correct(cid, problem, flawed, findings) if flags else flawed
    dec_flawed = decision(f"tf_dec__{cid}__flawed", flawed)
    dec_fixed = decision(f"tf_dec__{cid}__fixed", fixed) if flags else dec_flawed
    flipped_to_correct = (dec_flawed == case["flawed_option"]) and (dec_fixed == case["correct_option"])
    return {
        "id": cid, "flawed_option": case["flawed_option"], "correct_option": case["correct_option"],
        "planted_value": pv, "gate_caught_planted": caught, "n_flags": len(flags),
        "flags": [{"text": f["text"], "value": f["value"], "reason": f.get("reason")} for f in flags],
        "decision_flawed": dec_flawed, "decision_fixed": dec_fixed,
        "flipped_to_correct": flipped_to_correct, "fixed_rec": fixed,
    }


def main():
    print(f"[tf] threshold-flip demo — {len(CASES)} constructed cases (arithmetic ground truth)", flush=True)
    rows = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_case, c): c["id"] for c in CASES}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); rows[r["id"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[tf] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)

    caught = sum(1 for r in rows.values() if r["gate_caught_planted"])
    flipped = sum(1 for r in rows.values() if r["flipped_to_correct"])
    summary = {"EXPLORATORY": True, "positive_control": True, "n_cases": len(rows),
               "gate_caught_planted": f"{caught}/{len(rows)}", "flipped_to_correct": f"{flipped}/{len(rows)}",
               "cases": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== THRESHOLD-FLIP DEMO (wrong load-bearing number -> corrected -> decision flips) ===")
    print(f"  gate caught the planted wrong figure: {caught}/{len(rows)}")
    print(f"  correction flipped the decision to the objectively-correct option: {flipped}/{len(rows)}")
    print(f"\n  {'case':22s} {'planted':>9s} {'caught':>6s}  {'flawed->fixed':16s} {'correct':>7s}  result")
    for c in CASES:
        r = rows.get(c["id"])
        if not r:
            continue
        arrow = f"{r['decision_flawed']} -> {r['decision_fixed']}"
        res = "FLIP ✓" if r["flipped_to_correct"] else ("caught, no flip" if r["gate_caught_planted"] else "missed")
        print(f"  {c['id']:22s} {r['planted_value']:>9} {str(r['gate_caught_planted']):>6}  {arrow:16s} {r['correct_option']:>7s}  {res}")
    print("\n  per-case gate findings:")
    for c in CASES:
        r = rows.get(c["id"])
        if not r:
            continue
        print(f"    {c['id']}:")
        for fl in r["flags"]:
            print(f"      • \"{fl['text']}\" (value {fl['value']}) — {(fl['reason'] or '')[:110]}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
