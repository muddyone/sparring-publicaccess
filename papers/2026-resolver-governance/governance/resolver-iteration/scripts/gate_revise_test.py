#!/usr/bin/env python3
"""Two-arm revise-loop test — does feeding the gate's findings back improve the answer? (EXPLORATORY)

The correctness gate flags figures a recommendation states as fact but can't ground in the problem's
givens (e.g. the "~$650k/month" trigger whose real value derives to ~$1.5M). This tests whether acting on
those flags improves the answer, and compares two ways of acting — the distinction Bart drew:

  ARM A — DEMAND CORRECTION: give the producer its recommendation + the gate findings and ask it to
          revise (derive the figure, mark it as an assumption, or drop it and any dependent conclusion).
          This is self-correction prompted by an external flag.
  ARM B — INJECT AS NEW GIVEN: hand the producer the gate findings as ESTABLISHED FACTS about the
          numbers and have it decide FRESH from the problem + those facts. This is the "new external
          information as input" mechanism the WHY-TWO-PART literature says actually lifts quality
          (Reflexion / CRITIC / Self-Debug), as opposed to self-correction (which doesn't).

Measured, gold-free:
  1. DECISION CHANGE — does the selected option change vs the original? (per arm)
  2. QUALITY — anti-bias pairwise judge, NEW vs ORIGINAL, cross-vendor (Claude + GPT). This is the
     quality-preservation check the show-your-work-first drafting constraint FAILED (it lowered quality).
  3. RESIDUAL UNSUPPORTED — re-run the gate on each new answer: did the bucket-three count drop?

Prediction: Arm B changes the decision more cleanly and preserves/improves quality more than Arm A,
because it re-grounds and decides rather than re-litigating a prior answer. Runs on the step-2 finals
that carry >=1 bucket-three flag. Resumable; gr_* cache prefixes.

Usage: python3 gate_revise_test.py
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import bucket_gate as BG
from rescore_debiased import cf_verdict
from step1_xvendor import gpt_cf_verdict
from step2_convergence import DEC_SYS, DEC_USER

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
GATE = R.PILOT / "analysis" / "bucket-gate.json"
OUT_JSON = R.PILOT / "analysis" / "gate-revise-test.json"

ARM_A_SYS = (
    "You are the senior expert who produced the recommendation below. A correctness check flagged figures "
    "you stated as fact but that are NOT supported by the problem's given facts. Revise your "
    "recommendation so every flagged figure is handled honestly: for each, either (a) DERIVE it from the "
    "given facts and state the inputs, (b) MARK it explicitly as an assumption the reader must verify, or "
    "(c) REMOVE it and any conclusion that depends on it. Do not introduce new unsupported figures. Keep "
    "it a crisp, shippable recommendation of similar length, and still commit to one option."
)
ARM_A_USER = (
    "PROBLEM:\n{problem}\n\nYOUR RECOMMENDATION:\n{rec}\n\n"
    "CORRECTNESS-CHECK FINDINGS (stated as fact, not supported by the givens):\n{findings}\n\n"
    "Return JSON: {{\"revised_recommendation\": str}}"
)

ARM_B_SYS = (
    "You are a senior expert making a recommendation for a hard decision problem. In addition to the "
    "problem, you are given ESTABLISHED FINDINGS about the numbers — corrections and flags from a prior "
    "analysis of the figures involved; treat them as given facts. Weigh the options and commit to ONE, "
    "with a crisp, shippable rationale. Use the established findings as part of your given information; do "
    "not restate a figure they flag as unsupported."
)
ARM_B_USER = (
    "PROBLEM:\n{problem}\n\nESTABLISHED FINDINGS ABOUT THE NUMBERS (treat as given):\n{findings}\n\n"
    "Return JSON: {{\"recommendation\": str}}"
)

DECLABEL = {"A_BETTER": "original_better", "EQUIVALENT": "equivalent", "B_BETTER": "new_better"}


def findings_block(flags):
    lines = []
    for f in flags:
        reason = f.get("reason") or "stated as fact but not derivable from the problem's given facts"
        lines.append(f"- \"{f['text']}\" (stated value {f['value']}): {reason}")
    return "\n".join(lines)


def decision(uid, rec):
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, DEC_SYS, DEC_USER.format(rec=rec), max_tokens=200)
        ch = (out.get("choice", "?") if isinstance(out, dict) else "?") or "?"
        c = {"choice": str(ch).strip().lower()[:12]}
        R.save(uid, c)
    return c["choice"]


def produce_arm_a(pid, problem, rec, findings):
    uid = f"gr_armA__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, ARM_A_SYS, ARM_A_USER.format(problem=problem, rec=rec, findings=findings), max_tokens=5000)
        c = {"rec": (out.get("revised_recommendation", "") if isinstance(out, dict) else "") or ""}
        R.save(uid, c)
    return c["rec"]


def produce_arm_b(pid, problem, findings):
    uid = f"gr_armB__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, ARM_B_SYS, ARM_B_USER.format(problem=problem, findings=findings), max_tokens=5000)
        c = {"rec": (out.get("recommendation", "") if isinstance(out, dict) else "") or ""}
        R.save(uid, c)
    return c["rec"]


def quality(problem, original, new, tag):
    """NEW vs ORIGINAL, anti-bias pairwise, cross-vendor. original=A slot, new=B slot -> B_BETTER=new better."""
    cl = DECLABEL[cf_verdict(problem, original, new, f"gr_q_cl__{tag}", 3)]
    gp = DECLABEL[gpt_cf_verdict(problem, original, new, f"gr_q_gp__{tag}", 1)]
    return {"claude": cl, "gpt": gp}


def regate(pid, arm, problem, rec):
    """Re-run the gate on a revised answer (synthetic pid so its cache doesn't collide with the original)."""
    r = BG.run_problem(f"{pid}__{arm}", problem, rec)
    return {"n_bucket3": r["n_bucket3"], "n_review_split": r.get("n_review_split", 0),
            "bucket3": [{"text": b["text"], "value": b["value"], "reason": b.get("reason")} for b in r["bucket3"]]}


def run_problem(pid, problem, original, flags):
    findings = findings_block(flags)
    a_rec = produce_arm_a(pid, problem, original, findings)
    b_rec = produce_arm_b(pid, problem, findings)
    dec_o = decision(f"gr_dec__{pid}__orig", original)
    dec_a = decision(f"gr_dec__{pid}__armA", a_rec)
    dec_b = decision(f"gr_dec__{pid}__armB", b_rec)
    return {
        "pid": pid, "n_flags": len(flags),
        "decisions": {"original": dec_o, "armA": dec_a, "armB": dec_b,
                      "armA_changed": dec_a != dec_o, "armB_changed": dec_b != dec_o},
        "quality_vs_original": {"armA": quality(problem, original, a_rec, f"{pid}__A"),
                                "armB": quality(problem, original, b_rec, f"{pid}__B")},
        "residual_gate": {"armA": regate(pid, "armA", problem, a_rec),
                          "armB": regate(pid, "armB", problem, b_rec)},
        "recs": {"armA": a_rec, "armB": b_rec},
    }


def main():
    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}
    gate = json.loads(GATE.read_text())["detail"]
    finals = {}
    for pid in corpus:
        rev = R.load(f"s2_rev__{pid}__r3")
        finals[pid] = (rev.get("revised_recommendation", "") if rev else "") or corpus[pid]["R0"]

    # only recs that carry >=1 bucket-three flag
    targets = {pid: gate[pid]["bucket3"] for pid in corpus if gate.get(pid, {}).get("bucket3")}
    print(f"[gr] two-arm revise-loop on {len(targets)} flagged recommendations "
          f"({sum(len(v) for v in targets.values())} flags)", flush=True)

    rows = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_problem, pid, corpus[pid]["problem"], finals[pid], targets[pid]): pid for pid in targets}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); rows[r["pid"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[gr] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)

    # aggregate
    n = len(rows)
    flags_before = sum(r["n_flags"] for r in rows.values())
    def arm_stats(arm):
        changed = sum(1 for r in rows.values() if r["decisions"][f"{arm}_changed"])
        resid = sum(r["residual_gate"][arm]["n_bucket3"] for r in rows.values())
        qc = collections.Counter(r["quality_vs_original"][arm]["claude"] for r in rows.values())
        qg = collections.Counter(r["quality_vs_original"][arm]["gpt"] for r in rows.values())
        return {"decisions_changed": f"{changed}/{n}", "residual_bucket3": resid,
                "quality_claude": dict(qc), "quality_gpt": dict(qg)}
    summary = {"EXPLORATORY": True, "n_flagged_recs": n, "flags_before": flags_before,
               "armA_demand_correction": arm_stats("armA"), "armB_new_given": arm_stats("armB"),
               "detail": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== TWO-ARM REVISE-LOOP (act on the gate's flags) ===")
    print(f"  flagged recommendations: {n}   bucket-three flags before: {flags_before}")
    for arm, name in (("armA", "A: demand correction"), ("armB", "B: inject as new given")):
        s = arm_stats(arm)
        print(f"\n  ARM {name}")
        print(f"    decision changed vs original: {s['decisions_changed']}")
        print(f"    residual bucket-three flags after: {s['residual_bucket3']}  (was {flags_before})")
        print(f"    quality vs original — Claude: {s['quality_claude']}")
        print(f"    quality vs original — GPT:    {s['quality_gpt']}")
    print(f"\n  {'id':22s} {'orig':>6s} {'armA':>6s} {'armB':>6s}   {'A qual(cl/gp)':22s} {'B qual(cl/gp)':22s}  {'A/B resid':9s}")
    for pid, r in rows.items():
        d = r["decisions"]; q = r["quality_vs_original"]; rg = r["residual_gate"]
        qa = f"{q['armA']['claude']}/{q['armA']['gpt']}"
        qb = f"{q['armB']['claude']}/{q['armB']['gpt']}"
        print(f"  {pid:22s} {str(d['original']):>6s} {str(d['armA']):>6s} {str(d['armB']):>6s}   "
              f"{qa:22s} {qb:22s}  {rg['armA']['n_bucket3']}/{rg['armB']['n_bucket3']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
