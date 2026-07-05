#!/usr/bin/env python3
"""R6 — recrafted purpose-built GATE vs static/challenge gates, A/B on the same 61 candidates.

EXPLORATORY. Implements the R6-prompt-design-spec gate: default-to-admit, judge-the-delta,
evidence-lock-before-verdict, minimal reasoning, NO fix-proposals, XML-tagged inputs, binary
verdict + severity. Reuses r5's candidate set and DV-truth (no new DV scoring). Outputs the
precision/recall curve over a severity threshold, plus Cohen's kappa + the kappa-phi gap (the
over-flag drift metric, per Rao & Callison-Burch arXiv:2606.00093), with a train/test split.

Usage: python3 r6_gate.py        # resumable; writes analysis/r6-gate.json
"""
import json, math, concurrent.futures as cf
import run_study as R
import r5_challenge_gate as R5

# 3-member panel, same vendor mix as r5 (2 Claude + 1 GPT) for a fair A/B; the prompt is the
# lean purpose-built gate (no angle diversification — the gate is decision-only, not detection).
GATE_VENDORS = ("claude", "claude", "gpt")

RECRAFTED_GATE_SYS = (
    "You are a release GATE. Your only output is a binary ADMIT or REJECT on one proposed revision. "
    "You are NOT a critic and NOT an author; you do NOT suggest improvements or fixes and you do NOT "
    "write long analysis. DEFAULT TO ADMIT. Reject ONLY if the revision introduces a NEW would-ship "
    "defect -- one that on its own would change the decision or ship a real failure -- that was ABSENT "
    "from the previous version and is at least as severe as the flaw it was meant to fix. A nitpick, a "
    "style choice, a flaw that already existed in the previous version, or a 'could be stronger' is NOT "
    "grounds to reject. Quote your evidence first, then decide; keep all reasoning to those quotes."
)
RECRAFTED_GATE_USER = (
    "<previous_version>\n{prev}\n</previous_version>\n\n"
    "<candidate>\n{cand}\n</candidate>\n\n"
    "<target_flaws>\n{flaws}\n</target_flaws>\n\n"
    "<task>\nJudge ONLY the difference between previous_version and candidate.\n"
    "Step 1 (evidence): quote the sentence(s) in <candidate> that address the target_flaws, and any "
    "sentence that introduces a NEW would-ship defect not present in <previous_version>.\n"
    "Step 2 (severity): if there is a new would-ship defect, rate its severity 1-5 (5 = decision-changing "
    "/ ships a real failure); if none, severity is 0.\n"
    "Step 3 (verdict): ADMIT unless a NEW would-ship defect exists with severity at least as high as the "
    "target flaw. Default to ADMIT when uncertain.\n</task>\n\n"
    "Return JSON: {{\"evidence_resolves\": str, \"evidence_new_defect\": str|null, "
    "\"new_defect_severity\": 0, \"verdict\": \"ADMIT\"|\"REJECT\", \"reason\": str}}"
)


def gate_member(vendor, problem, prev, cand, flaws_text):
    user = RECRAFTED_GATE_USER.format(prev=prev, cand=cand, flaws=flaws_text)
    if vendor == "claude":
        out = R.L.claude_json(R.CLAUDE, RECRAFTED_GATE_SYS, user, max_tokens=2000)
    else:
        out = R.L.gpt_json(R.GPT, RECRAFTED_GATE_SYS, user)
    if isinstance(out, list):
        out = out[0] if out and isinstance(out[0], dict) else {}
    verdict = str(out.get("verdict", "ADMIT")).upper()
    sev = out.get("new_defect_severity", 0)
    try:
        sev = int(sev)
    except (TypeError, ValueError):
        sev = 0
    return {"vendor": vendor, "verdict": "REJECT" if verdict == "REJECT" else "ADMIT", "severity": max(0, min(5, sev))}


def run_gate(aid, pid, prev, cand, flaws_text):
    cache = R.load(f"r6gate__{aid}")
    if cache:
        return cache
    problem = R.PROBLEMS[pid]["problem"]
    members = []
    for v in GATE_VENDORS:
        try:
            members.append(gate_member(v, problem, prev, cand, flaws_text))
        except Exception as e:  # noqa: BLE001
            members.append({"vendor": v, "verdict": "ADMIT", "severity": 0, "error": repr(e)[:120]})
    reject_votes = sum(1 for m in members if m["verdict"] == "REJECT")
    sevs = sorted(m["severity"] for m in members)
    rec = {"aid": aid, "members": members, "panel_reject": reject_votes >= 2,
           "median_severity": sevs[1], "max_severity": sevs[-1]}
    R.save(f"r6gate__{aid}", rec)
    return rec


# ---- metrics ----
def confusion(rows, block_key):
    tp = sum(1 for r in rows if r[block_key] and r["reg"])
    fp = sum(1 for r in rows if r[block_key] and not r["reg"])
    fn = sum(1 for r in rows if not r[block_key] and r["reg"])
    tn = sum(1 for r in rows if not r[block_key] and not r["reg"])
    return tp, fp, fn, tn


def metrics(rows, block_key):
    tp, fp, fn, tn = confusion(rows, block_key)
    n = tp + fp + fn + tn
    recall = tp / (tp + fn) if (tp + fn) else None
    prec = tp / (tp + fp) if (tp + fp) else None
    bal = 0.5 * ((tp / (tp + fn) if (tp + fn) else 0) + (tn / (tn + fp) if (tn + fp) else 0))
    den = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    phi = (tp * tn - fp * fn) / den if den else 0.0
    po = (tp + tn) / n if n else 0
    pe = (((tp + fp) / n) * ((tp + fn) / n) + ((fn + tn) / n) * ((fp + tn) / n)) if n else 0
    kappa = (po - pe) / (1 - pe) if (1 - pe) else 0.0
    return {"recall": recall, "precision": round(prec, 3) if prec is not None else None,
            "balanced_acc": round(bal, 3), "phi": round(phi, 3), "kappa": round(kappa, 3),
            "kappa_phi_gap": round(phi - kappa, 3), "block_rate": round((tp + fp) / n, 3) if n else None,
            "confusion": {"tp": tp, "fp": fp, "fn": fn, "tn": tn}}


def main():
    cands, _ = R5.gather()
    # DV-truth per candidate (reuse r5's scores: trajectory for admitted, r5rej for rejected)
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
    print(f"[r6] {len(rows)} candidates with DV-truth; running recrafted gate (resumable)...", flush=True)

    # run the recrafted gate on each
    done = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {}
        for r in rows:
            c = r["c"]
            flaws_text = R.fmt_objections(c["objections"])
            futs[ex.submit(run_gate, c["aid"], c["pid"], R.R0[c["pid"]] if c["round"] == 1 else _prev_text(c), c["candidate"], flaws_text)] = r
        for f in cf.as_completed(futs):
            g = f.result()
            r = futs[f]
            r["panel_reject"] = g["panel_reject"]
            r["median_severity"] = g["median_severity"]
            done += 1
            if done % 10 == 0:
                print(f"[r6] gate {done}/{len(rows)}", flush=True)

    # severity-threshold sweep: block iff median member severity >= theta
    sweep = {}
    for theta in (1, 2, 3, 4, 5):
        for r in rows:
            r[f"block_t{theta}"] = r["median_severity"] >= theta
        sweep[f"theta>={theta}"] = metrics(rows, f"block_t{theta}")
    # the prompt's own binary panel verdict
    prompt_verdict = metrics(rows, "panel_reject")

    # train/test split (deterministic: sort by aid, even=train odd=test) -> pick best theta on train by balanced_acc
    rows_sorted = sorted(rows, key=lambda r: r["c"]["aid"])
    train = [r for i, r in enumerate(rows_sorted) if i % 2 == 0]
    test = [r for i, r in enumerate(rows_sorted) if i % 2 == 1]
    best_theta, best_bal = None, -1
    for theta in (1, 2, 3, 4, 5):
        m = metrics(train, f"block_t{theta}")
        if m["balanced_acc"] > best_bal:
            best_bal, best_theta = m["balanced_acc"], theta
    test_at_best = metrics(test, f"block_t{best_theta}")
    train_at_best = metrics(train, f"block_t{best_theta}")

    # r5 reference points (static + challenge gate) recomputed on the same rows for apples-to-apples
    for r in rows:
        st = R.load(f"R3__{r['c']['arm']}__{r['c']['pid']}")  # static gate verdict is in the R3 attempt
        r["static_block"] = not r["c"]["static_admit"]
        cg = R.load(f"chalgate__{r['c']['aid']}")
        r["challenge_block"] = (not cg["admit"]) if cg else None
    static_ref = metrics(rows, "static_block")
    chal_rows = [r for r in rows if r["challenge_block"] is not None]
    challenge_ref = metrics(chal_rows, "challenge_block")

    n_reg = sum(1 for r in rows if r["reg"])
    out = {"EXPLORATORY": True, "n": len(rows), "n_regressions": n_reg, "n_clean": len(rows) - n_reg,
           "recrafted_gate_severity_sweep": sweep,
           "recrafted_gate_prompt_verdict": prompt_verdict,
           "train_test": {"best_theta_by_train_balacc": best_theta,
                           "train_at_best": train_at_best, "test_at_best": test_at_best,
                           "n_train": len(train), "n_test": len(test)},
           "reference_static_gate": static_ref, "reference_challenge_gate": challenge_ref}
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    (R.PILOT / "analysis" / "r6-gate.json").write_text(json.dumps(out, indent=2))

    def line(name, m):
        return (f"  {name:34s} recall={m['recall']} prec={m['precision']} balAcc={m['balanced_acc']} "
                f"kappa={m['kappa']} (phi={m['phi']}, gap={m['kappa_phi_gap']}) blockRate={m['block_rate']}")
    print(f"\n=== R6 RECRAFTED GATE vs references (n={len(rows)}: {n_reg} regressions / {len(rows)-n_reg} clean) ===")
    print("  (a good gate: high recall on regressions AND high precision; kappa-phi gap -> 0 means flag-rate matches truth)\n")
    print(line("REF static gate (verifier)", static_ref))
    print(line("REF challenge gate (R5)", challenge_ref))
    print(line("recrafted gate (prompt verdict)", prompt_verdict))
    for k, m in sweep.items():
        print(line(f"recrafted gate {k}", m))
    print(f"\n  TRAIN/TEST (best theta>={best_theta} chosen on train balAcc):")
    print(line("   train@best", train_at_best))
    print(line("   test@best ", test_at_best))
    print("\nwrote analysis/r6-gate.json")


def _prev_text(c):
    """Reconstruct the champion-before text for round r (committed output of round r-1)."""
    u = R.load(f"R3__{c['arm']}__{c['pid']}")
    cur = R.R0[c["pid"]]
    for e in u["round_log"]:
        if e["round"] >= c["round"]:
            break
        adm = [a for a in e.get("patch_attempts", []) if a["gate"]["admit"]]
        if adm:
            cur = adm[-1]["candidate"]
    return cur


if __name__ == "__main__":
    main()
