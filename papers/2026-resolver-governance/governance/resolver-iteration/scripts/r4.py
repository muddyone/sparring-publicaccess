#!/usr/bin/env python3
"""R4 — per-flaw surgical admissions control with a champion (EXPLORATORY pilot, not pre-registered).

Architecture change from R3: instead of one monolithic producer rewrite per round (judged as a
bundle), R4 keeps a CHAMPION recommendation and advances it ONE gate-passed surgical correction at
a time. Each round: challenge the champion -> generate a minimal one-flaw correction per flaw
(parallel) -> gate each independently -> the champion adopts the single best-gated correction. The
champion never adopts an ungated change, so it is monotonic-by-the-gate (keep-best as an invariant,
no DV leakage).

This pilot is MECHANISM-SCOPED, not a power test. It measures three things vs R3 (all from the
champion-state DV scores, which need no statistical power):
  1. churn        — char-diff size per accepted change (R4 surgical vs R3 whole-rewrite)
  2. monotonicity — DV-net walk-backs across champion states (should be ~0 by construction)
  3. gate<->DV    — fraction of gate-admitted corrections that actually lowered the DV net

Reuses run_study's models, challenger, gate panel, and DV scorer.

Usage:
  python3 r4.py produce       # run R4 ceremonies (same-arm, 8 problems by default)
  python3 r4.py score         # DV-score every champion state (per round)
  python3 r4.py analyze       # compute churn / monotonicity / gate<->DV vs R3
  python3 r4.py all
"""
import sys, json, difflib, concurrent.futures as cf
import run_study as R

CAP_R4 = 8                 # one flaw fixed per round -> allow more rounds than R3's 5
MAX_FLAWS_PER_ROUND = 4    # bound the per-round corrector fan-out (cost)
ARMS = ("same",)           # pilot: same-vendor arm only (captures all 3 R3 pathologies)
CORR_MAXTOK = 9000

CORR_SYS = (
    "You are the senior author of a recommendation for a hard decision problem. A challenger raised "
    "ONE specific objection. Produce the SMALLEST surgical revision that fixes ONLY this one objection "
    "and preserves everything else VERBATIM. Do not address other issues, do not rewrite for style, do "
    "not re-argue settled points. Change as few words as possible. A release gate will REJECT your edit "
    "if it introduces any new flaw as severe as the one it fixes, and the champion will be kept instead. "
    "If this objection cannot be fixed without a larger change, make the smallest change that genuinely "
    "resolves it and say so."
)
CORR_USER = (
    "PROBLEM:\n{problem}\n\nCURRENT RECOMMENDATION (the champion):\n{rec}\n\n"
    "THE ONE OBJECTION TO FIX:\n[{handle}] {text}\n\n"
    "Return JSON: {{\"revised_recommendation\": str, \"what_changed\": str}}"
)


def _corr_and_gate(pid, arm, C, flaw):
    """Generate a surgical correction for one flaw and gate it vs the champion. Returns dict or None."""
    problem = R.PROBLEMS[pid]["problem"]
    try:
        rev = R.L.claude_json(R.CLAUDE, CORR_SYS,
                              CORR_USER.format(problem=problem, rec=C, handle=flaw.get("handle", "?"), text=flaw.get("text", "")),
                              max_tokens=CORR_MAXTOK)
    except Exception as e:  # noqa: BLE001
        return {"flaw": flaw, "error": repr(e)[:160]}
    candidate = rev.get("revised_recommendation", "")
    if not candidate:
        return {"flaw": flaw, "error": "empty candidate"}
    admit, gate_rec = R.gate_verdict(problem, C, [flaw], candidate)
    return {"flaw": flaw, "candidate": candidate, "what_changed": rev.get("what_changed", ""),
            "admit": admit, "gate": gate_rec}


def run_r4(pid, arm):
    vendor = "claude" if arm == "same" else "gpt"
    uid = f"R4__{arm}__{pid}"
    if R.load(uid):
        return uid
    problem = R.PROBLEMS[pid]["problem"]
    C = R.R0[pid]
    champion_states = [{"round": 0, "text": C}]   # for per-round DV scoring
    trail = []
    terminal = None
    for r in range(1, CAP_R4 + 1):
        chal = R.challenger_call(vendor, R.CHAL_SYS, R.CHAL_R1_USER.format(problem=problem, rec=C))
        if isinstance(chal, list):
            chal = {"objections": chal, "material_objections_remaining": bool(chal)}
        flaws = chal.get("objections", [])[:MAX_FLAWS_PER_ROUND]
        remaining = bool(chal.get("material_objections_remaining"))
        entry = {"round": r, "challenger_remaining": remaining, "flaw_count": len(flaws), "candidates": []}
        if not remaining or not flaws:
            terminal = "CONVERGED"
            trail.append(entry)
            break
        # one surgical correction per flaw, gated, in parallel
        results = []
        with cf.ThreadPoolExecutor(max_workers=min(MAX_FLAWS_PER_ROUND, R.WORKERS)) as ex:
            futs = [ex.submit(_corr_and_gate, pid, arm, C, f) for f in flaws]
            for fu in cf.as_completed(futs):
                results.append(fu.result())
        # record compact candidate summaries
        for res in results:
            entry["candidates"].append({
                "flaw_handle": res["flaw"].get("handle", "?"),
                "admit": res.get("admit", False),
                "admit_votes": res.get("gate", {}).get("admit_votes") if res.get("gate") else None,
                "new_flaw_cost": res.get("gate", {}).get("new_flaw_cost") if res.get("gate") else None,
                "error": res.get("error"),
            })
        admitted = [res for res in results if res.get("admit")]
        if not admitted:
            terminal = "EXHAUSTED"
            trail.append(entry)
            break
        # advance champion by the single best-gated correction: most admit votes, then least new-flaw cost
        best = max(admitted, key=lambda x: (x["gate"]["admit_votes"], -x["gate"]["new_flaw_cost"]))
        prev_C = C
        C = best["candidate"]
        entry["chosen_flaw"] = best["flaw"].get("handle", "?")
        entry["chosen_votes"] = best["gate"]["admit_votes"]
        entry["chosen_new_flaw_cost"] = best["gate"]["new_flaw_cost"]
        entry["char_diff_size"] = _diff_size(prev_C, C)
        entry["champion_text"] = C
        champion_states.append({"round": r, "text": C})
        trail.append(entry)
    else:
        terminal = "CAPPED"
    R.save(uid, {"unit": uid, "condition": "R4", "arm": arm, "pid": pid,
                 "final_output": C, "terminal_state": terminal, "rounds": len(trail),
                 "round_log": trail, "champion_states": champion_states})
    return uid


def _diff_size(a, b):
    """Chars changed between two recommendations (added+removed), a churn proxy."""
    sm = difflib.SequenceMatcher(None, a, b)
    changed = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            changed += (i2 - i1) + (j2 - j1)
    return changed


# ---------------------------------------------------------------- stages
def stage_produce():
    jobs = [(pid, arm) for pid in R.PIDS for arm in ARMS]
    done = 0
    for (pid, arm) in jobs:
        try:
            run_r4(pid, arm)
        except Exception as e:  # noqa: BLE001
            print(f"[R4 produce] ERROR {pid} {arm}: {repr(e)[:200]}", flush=True)
        done += 1
        print(f"[R4 produce] {done}/{len(jobs)} ceremonies done", flush=True)


def champion_state_outputs():
    outs = []
    for pid in R.PIDS:
        for arm in ARMS:
            u = R.load(f"R4__{arm}__{pid}")
            if not u:
                continue
            for st in u["champion_states"]:
                outs.append((f"r4state__{arm}__{pid}__r{st['round']}", pid, st["text"]))
    return outs


def stage_score():
    outs = champion_state_outputs()
    print(f"[R4 score] DV-scoring {len(outs)} champion states (resumable)...", flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(R.score_output, oid, pid, text): oid for (oid, pid, text) in outs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:  # noqa: BLE001
                print(f"[R4 score] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)
            done += 1
            if done % 10 == 0:
                print(f"[R4 score] {done}/{len(outs)}", flush=True)


def _champion_net(pid, arm, rnd):
    if rnd == 0:
        return len(R.DENOM[pid])     # R0 baseline = full denominator
    s = R.load(f"score__r4state__{arm}__{pid}__r{rnd}")
    return s["net_flaws_remaining"] if s else None


def stage_analyze():
    rows, walkbacks, gate_calls, gate_agree = [], 0, 0, 0
    churn_r4 = []
    for pid in R.PIDS:
        for arm in ARMS:
            u = R.load(f"R4__{arm}__{pid}")
            if not u:
                continue
            states = u["champion_states"]
            series = [{"round": st["round"], "net": _champion_net(pid, arm, st["round"])} for st in states]
            nets = [p["net"] for p in series]
            # monotonicity: count champion advances that raised DV net (gate said improve, DV disagreed)
            for i in range(1, len(nets)):
                if nets[i] is None or nets[i - 1] is None:
                    continue
                gate_calls += 1
                if nets[i] <= nets[i - 1]:
                    gate_agree += 1          # DV agrees the gated correction did not worsen
                if nets[i] > nets[i - 1]:
                    walkbacks += 1           # champion walked backward by the DV
            for e in u["round_log"]:
                if "char_diff_size" in e:
                    churn_r4.append(e["char_diff_size"])
            rows.append({"pid": pid, "arm": arm, "terminal": u["terminal_state"],
                         "rounds": u["rounds"], "series": series, "final_net": nets[-1]})
    # R3 comparison: churn (whole-rewrite diff) + gate<->DV agreement from existing trajectory scores
    churn_r3, r3_calls, r3_agree, r3_walk = [], 0, 0, 0
    import difflib as _d
    for pid in R.PIDS:
        for arm in ARMS:
            u = R.load(f"R3__{arm}__{pid}")
            if not u:
                continue
            cur = R.R0[pid]
            prev_net = len(R.DENOM[pid])
            for e in u["round_log"]:
                adm = [a for a in e.get("patch_attempts", []) if a["gate"]["admit"]]
                if not adm:
                    continue
                cand = adm[-1]["candidate"]
                churn_r3.append(_diff_size(cur, cand))
                s = R.load(f"score__traj__R3__{arm}__{pid}__r{e['round']}")
                net = s["net_flaws_remaining"] if s else None
                if net is not None:
                    r3_calls += 1
                    if net <= prev_net:
                        r3_agree += 1
                    else:
                        r3_walk += 1
                    prev_net = net
                cur = cand

    def _mean(xs):
        return round(sum(xs) / len(xs), 1) if xs else None
    summary = {
        "EXPLORATORY": True, "scope": f"R4 {ARMS} arm, {len(rows)} ceremonies (mechanism pilot, not powered)",
        "churn_mean_chars": {"R4_surgical": _mean(churn_r4), "R3_whole_rewrite": _mean(churn_r3)},
        "monotonicity": {"R4_champion_advances": gate_calls, "R4_DV_walkbacks": walkbacks,
                          "R3_admitted_patches": r3_calls, "R3_DV_walkbacks": r3_walk},
        "gate_vs_DV_agreement": {
            "R4": f"{gate_agree}/{gate_calls}" + (f" ({round(100*gate_agree/gate_calls)}%)" if gate_calls else ""),
            "R3": f"{r3_agree}/{r3_calls}" + (f" ({round(100*r3_agree/r3_calls)}%)" if r3_calls else "")},
        "terminal_states": {},
        "ceremonies": rows,
    }
    for row in rows:
        summary["terminal_states"][row["terminal"]] = summary["terminal_states"].get(row["terminal"], 0) + 1
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    (R.PILOT / "analysis" / "r4-results.json").write_text(json.dumps(summary, indent=2))

    print("\n=== R4 CHAMPION TRAJECTORIES (DV net per champion state; lower better) ===")
    for row in rows:
        path = " → ".join(str(p["net"]) for p in row["series"])
        print(f"  {row['pid']:24s} {row['arm']:5s} [{row['terminal']:9s}]  {path}")
    print("\n=== MECHANISM: R4 vs R3 ===")
    print(f"  churn (mean chars changed per accepted edit):  R4={summary['churn_mean_chars']['R4_surgical']}  R3={summary['churn_mean_chars']['R3_whole_rewrite']}")
    print(f"  DV walk-backs (champion got worse by the DV):   R4={walkbacks}/{gate_calls}  R3={r3_walk}/{r3_calls}")
    print(f"  gate↔DV agreement (admitted edit truly helped): R4={summary['gate_vs_DV_agreement']['R4']}  R3={summary['gate_vs_DV_agreement']['R3']}")
    print(f"  R4 terminal states: {summary['terminal_states']}")
    print("\nwrote analysis/r4-results.json")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("produce", "all"):
        stage_produce()
    if cmd in ("score", "all"):
        stage_score()
    if cmd in ("analyze", "all"):
        stage_analyze()
    print("DONE", cmd)
