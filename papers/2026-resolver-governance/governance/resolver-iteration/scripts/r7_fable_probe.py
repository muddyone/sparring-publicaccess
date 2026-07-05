#!/usr/bin/env python3
"""R7 — Fable-5 capability-ceiling probe on the gate discrimination wall.

EXPLORATORY. Answers the one question R3->R6 left open: is the gate discrimination wall
(balanced acc ~= 0.50-0.59, kappa ~= 0.00-0.19 across every variant) a MODEL-CAPABILITY ceiling
or a TASK ceiling? Every prior gate ran on claude-opus-4-8. This re-runs the R6 recrafted gate --
same 61 candidates, same prompt, same DV-truth, same metrics -- with the two Claude panel members
upgraded opus-4-8 -> claude-fable-5 (the most capable available model). GPT-5.2 member unchanged so
panel composition is held constant for a clean A/B against analysis/r6-gate.json.

Read the decision rule in R7-fable-capability-probe-spec.md before interpreting: discrimination is
read from balanced_acc / kappa, NOT recall or block_rate (framing controls those).

Arms:
  R7-A (default): 2 fable + 1 gpt-5.2   (matches R6 composition; only the Claude tier changes)
  R7-B (--solo):  3 fable               (removes GPT as a discrimination drag; run only if R7-A flat)

Fable specifics handled here (see spec section "Implementation notes"):
  * thinking is always on + billed -> max_tokens raised to 8000, output_config effort=low
  * never send thinking:disabled (400) or temperature (400) -- omitted
  * refusals are HTTP 200 w/ stop_reason=="refusal" -> server-side fallback to opus-4-8, and the
    served model is TAGGED per member so we can report the fallback rate and run a sensitivity
    metric excluding fable->opus-contaminated candidates.

Usage:
  python3 r7_fable_probe.py            # R7-A, resumable, writes analysis/r7-fable-probe.json
  python3 r7_fable_probe.py --solo     # R7-B (3x fable)
"""
import os, sys, json, requests, concurrent.futures as cf
import run_study as R
import r5_challenge_gate as R5
import r6_gate as R6

FABLE = "claude-fable-5"
FALLBACK = "claude-opus-4-8"
CLAUDE_URL = "https://api.anthropic.com/v1/messages"

SOLO = "--solo" in sys.argv
GATE_VENDORS = ("fable", "fable", "fable") if SOLO else ("fable", "fable", "gpt")
TAG = "r7solo" if SOLO else "r7fable"


def call_fable(system, user, max_tokens=8000):
    """Fable gate call with always-on-thinking headroom, low effort, and server-side
    refusal fallback to opus-4-8. Returns (parsed_json, served_model, refused_bool)."""
    R.L._throttle("claude")
    body = {
        "model": FABLE,
        "max_tokens": max_tokens,
        "system": system + "\n\nRespond with STRICT JSON only -- no prose, no markdown fences.",
        "messages": [{"role": "user", "content": user}],
        "output_config": {"effort": "low"},
        "fallbacks": [{"model": FALLBACK}],
    }
    r = requests.post(
        CLAUDE_URL,
        headers={
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
            "anthropic-beta": "server-side-fallback-2026-06-01",
            "content-type": "application/json",
        },
        json=body,
        timeout=300,
    )
    if r.status_code != 200:
        raise R.L.LLMError(f"fable status {r.status_code}: {r.text[:300]}")
    d = r.json()
    served = d.get("model", FABLE)
    stop = d.get("stop_reason")
    # A refusal that the fallback chain did NOT rescue -> whole chain refused.
    refused = stop == "refusal"
    parts = [b.get("text", "") for b in d.get("content", []) if b.get("type") == "text"]
    text = "".join(parts)
    if refused or not text.strip():
        return {}, served, True
    try:
        return R.L.extract_json(text), served, False
    except R.L.LLMError:
        return {}, served, True


def gate_member(vendor, prev, cand, flaws_text):
    user = R6.RECRAFTED_GATE_USER.format(prev=prev, cand=cand, flaws=flaws_text)
    served, refused = vendor, False
    if vendor == "fable":
        out, served, refused = R.L._retry(
            lambda: call_fable(R6.RECRAFTED_GATE_SYS, user), "fable-gate")
    else:
        out = R.L.gpt_json(R.GPT, R6.RECRAFTED_GATE_SYS, user)
    if isinstance(out, list):
        out = out[0] if out and isinstance(out[0], dict) else {}
    verdict = str(out.get("verdict", "ADMIT")).upper()
    sev = out.get("new_defect_severity", 0)
    try:
        sev = int(sev)
    except (TypeError, ValueError):
        sev = 0
    return {"vendor": vendor, "served": served, "refused": refused,
            "verdict": "REJECT" if verdict == "REJECT" else "ADMIT",
            "severity": max(0, min(5, sev))}


def run_gate(aid, prev, cand, flaws_text):
    cache = R.load(f"{TAG}__{aid}")
    if cache:
        return cache
    members = []
    for v in GATE_VENDORS:
        try:
            members.append(gate_member(v, prev, cand, flaws_text))
        except Exception as e:  # noqa: BLE001
            members.append({"vendor": v, "served": v, "refused": True,
                            "verdict": "ADMIT", "severity": 0, "error": repr(e)[:120]})
    reject_votes = sum(1 for m in members if m["verdict"] == "REJECT")
    sevs = sorted(m["severity"] for m in members)
    rec = {"aid": aid, "members": members, "panel_reject": reject_votes >= 2,
           "median_severity": sevs[1], "max_severity": sevs[-1],
           "any_fallback": any(m.get("served") == FALLBACK for m in members),
           "any_refused": any(m.get("refused") for m in members)}
    R.save(f"{TAG}__{aid}", rec)
    return rec


def main():
    cands, _ = R5.gather()
    # DV-truth per candidate -- IDENTICAL construction to r6_gate.main (reuse r5 scores).
    rows = []
    for c in cands:
        cb = c["champ_before_net"]
        if c["cand_net_uid"] is None:
            cn = R5.traj_net(c["pid"], c["arm"], c["round"])
        else:
            s = R.load(f"score__{c['cand_net_uid']}")
            cn = s["net_flaws_remaining"] if s else None
        if cb is None or cn is None:
            continue
        rows.append({"c": c, "champ_net": cb, "cand_net": cn, "reg": cn > cb})
    print(f"[r7:{TAG}] {len(rows)} candidates with DV-truth; panel={GATE_VENDORS}; running (resumable)...",
          flush=True)

    done = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {}
        for r in rows:
            c = r["c"]
            flaws_text = R.fmt_objections(c["objections"])
            prev = R.R0[c["pid"]] if c["round"] == 1 else R6._prev_text(c)
            futs[ex.submit(run_gate, c["aid"], prev, c["candidate"], flaws_text)] = r
        for f in cf.as_completed(futs):
            g = f.result()
            r = futs[f]
            r["panel_reject"] = g["panel_reject"]
            r["median_severity"] = g["median_severity"]
            r["any_fallback"] = g["any_fallback"]
            r["any_refused"] = g["any_refused"]
            done += 1
            if done % 10 == 0:
                print(f"[r7:{TAG}] gate {done}/{len(rows)}", flush=True)

    # metrics: severity sweep + prompt verdict + train/test -- reuse R6.metrics verbatim.
    sweep = {}
    for theta in (1, 2, 3, 4, 5):
        for r in rows:
            r[f"block_t{theta}"] = r["median_severity"] >= theta
        sweep[f"theta>={theta}"] = R6.metrics(rows, f"block_t{theta}")
    prompt_verdict = R6.metrics(rows, "panel_reject")

    rows_sorted = sorted(rows, key=lambda r: r["c"]["aid"])
    train = [r for i, r in enumerate(rows_sorted) if i % 2 == 0]
    test = [r for i, r in enumerate(rows_sorted) if i % 2 == 1]
    best_theta, best_bal = 1, -1
    for theta in (1, 2, 3, 4, 5):
        m = R6.metrics(train, f"block_t{theta}")
        if m["balanced_acc"] > best_bal:
            best_bal, best_theta = m["balanced_acc"], theta
    train_at_best = R6.metrics(train, f"block_t{best_theta}")
    test_at_best = R6.metrics(test, f"block_t{best_theta}")

    # refusal / fallback contamination + sensitivity metric (clean = no member fell back or refused)
    n_fallback = sum(1 for r in rows if r["any_fallback"])
    n_refused = sum(1 for r in rows if r["any_refused"])
    clean = [r for r in rows if not r["any_fallback"] and not r["any_refused"]]
    sens_verdict = R6.metrics(clean, "panel_reject") if clean else None

    n_reg = sum(1 for r in rows if r["reg"])
    out = {"EXPLORATORY": True, "arm": "R7-B (3x fable)" if SOLO else "R7-A (2 fable + 1 gpt)",
           "n": len(rows), "n_regressions": n_reg, "n_clean_labels": len(rows) - n_reg,
           "fable_severity_sweep": sweep, "fable_prompt_verdict": prompt_verdict,
           "train_test": {"best_theta_by_train_balacc": best_theta,
                          "train_at_best": train_at_best, "test_at_best": test_at_best,
                          "n_train": len(train), "n_test": len(test)},
           "contamination": {"n_candidates_with_fallback": n_fallback,
                             "n_candidates_with_refusal": n_refused,
                             "n_clean_of_contamination": len(clean)},
           "sensitivity_prompt_verdict_no_fallback": sens_verdict}
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    fname = "r7-fable-solo.json" if SOLO else "r7-fable-probe.json"
    (R.PILOT / "analysis" / fname).write_text(json.dumps(out, indent=2))

    # side-by-side vs R6 opus baseline
    r6 = json.loads((R.PILOT / "analysis" / "r6-gate.json").read_text())
    r6_pv = r6["recrafted_gate_prompt_verdict"]

    def line(name, m):
        if not m:
            return f"  {name:38s} (no rows)"
        return (f"  {name:38s} recall={m['recall']} prec={m['precision']} balAcc={m['balanced_acc']} "
                f"kappa={m['kappa']} (phi={m['phi']}, gap={m['kappa_phi_gap']}) blockRate={m['block_rate']}")

    print(f"\n=== R7 FABLE PROBE ({out['arm']}) vs R6 opus baseline "
          f"(n={len(rows)}: {n_reg} reg / {len(rows)-n_reg} clean) ===")
    print("  DECISION: discrimination = balAcc & kappa. Rise (kappa>~0.35, balAcc>~0.65) => capability")
    print("            was the ceiling. Flat (kappa~0, balAcc~0.50-0.55) => NOT capability-bound.\n")
    print(line("R6 opus-4-8 gate (prompt verdict)", r6_pv))
    print(line("R7 fable gate (prompt verdict)", prompt_verdict))
    for k, m in sweep.items():
        print(line(f"R7 fable {k}", m))
    print(f"\n  TRAIN/TEST (best theta>={best_theta} on train balAcc):")
    print(line("   train@best", train_at_best))
    print(line("   test@best ", test_at_best))
    print(f"\n  CONTAMINATION: {n_fallback}/{len(rows)} candidates had a fable->opus fallback, "
          f"{n_refused} had an unrescued refusal.")
    print(line("  sensitivity (drop contaminated)", sens_verdict))
    print(f"\nwrote analysis/{fname}")


if __name__ == "__main__":
    main()
