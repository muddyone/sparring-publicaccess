#!/usr/bin/env python3
"""R5 — challenge-gate vs static-gate, head-to-head RE-ANALYSIS (EXPLORATORY, no new ceremonies).

Tests Bart's hypothesis: the single challenge is the one validated flaw-detection move (~87% in
§6.3), so a gate that USES the challenge move should predict the DV better than the current static
verifier-panel gate.

Design (the point is the isolation): take R3's existing candidate corrections — each with its
champion-before, candidate text, the round's objections, and the static gate's verdict — and:
  1. judge each candidate with a CHALLENGE-based gate (reuses the challenger's round-N move,
     CHAL_RN: given the prior objections, which are resolved and what new flaws appear);
  2. establish DV-truth per candidate (did net flaws actually rise = regression, vs stay/drop);
  3. compare which gate's signals better predict DV-truth.

Unit of analysis is the CANDIDATE DECISION (~61), not the problem (8) — so this escapes the n=8
power wall: the gate-quality question has ~61 data points. Reuses run_study's challenger + DV scorer.

Usage: python3 r5_challenge_gate.py        # resumable; writes analysis/r5-challenge-gate.json
"""
import json, concurrent.futures as cf
import run_study as R

# challenge-gate panel: mirror the static gate's vendor mix (2 Claude angles + 1 GPT), but the MOVE
# is a challenge (CHAL_RN) instead of a verifier audit. Angle-diversify the Claude members.
GATE_CHAL = [("claude", R.AUDIT_ANGLES[0]), ("claude", R.AUDIT_ANGLES[1]), ("gpt", "")]


def committed_per_round(u):
    out = [(0, R.R0[u["pid"]])]
    cur = R.R0[u["pid"]]
    for e in u["round_log"]:
        adm = None
        for a in e.get("patch_attempts", []):
            if a["gate"]["admit"]:
                adm = a["candidate"]
        if adm is not None:
            cur = adm
            out.append((e["round"], cur))
    return out


def traj_net(pid, arm, rnd):
    if rnd == 0:
        return len(R.DENOM[pid])
    s = R.load(f"score__traj__R3__{arm}__{pid}__r{rnd}")
    return s["net_flaws_remaining"] if s else None


def challenge_gate_member(vendor, angle, problem, candidate, objections):
    """One challenge-move verdict on a candidate: which prior objections resolved, any NEW flaw."""
    sysp = R.CHAL_SYS + ((" " + angle) if angle else "")
    user = R.CHAL_RN_USER.format(problem=problem, rec=candidate, prev=R.fmt_objections(objections))
    out = R.challenger_call(vendor, sysp, user)
    if isinstance(out, list):
        out = {"objections": out, "resolved_last_round": [], "material_objections_remaining": bool(out)}
    objs = out.get("objections", [])
    resolved = out.get("resolved_last_round", []) or [o.get("handle") for o in objs if o.get("status") == "resolved"]
    new = [o for o in objs if o.get("status") == "new"]
    member_admit = bool(resolved) and not new          # strict: resolved >=1 AND introduced nothing new
    return {"vendor": vendor, "resolved": list(resolved), "new_count": len(new), "member_admit": member_admit}


def challenge_gate(pid, arm, attempt_id, problem, candidate, objections):
    cache = R.load(f"chalgate__{attempt_id}")
    if cache:
        return cache
    members = []
    for vendor, angle in GATE_CHAL:
        try:
            members.append(challenge_gate_member(vendor, angle, problem, candidate, objections))
        except Exception as e:  # noqa: BLE001
            members.append({"vendor": vendor, "error": repr(e)[:140], "member_admit": False, "new_count": None})
    admit_votes = sum(1 for m in members if m.get("member_admit"))
    flagged_new = sum(1 for m in members if (m.get("new_count") or 0) > 0)
    rec = {"attempt_id": attempt_id, "admit": admit_votes >= 2, "admit_votes": admit_votes,
           "members_flagging_new": flagged_new, "members": members}
    R.save(f"chalgate__{attempt_id}", rec)
    return rec


def gather():
    """All R3 candidate attempts with champion-before net, candidate net (DV-truth), static verdict."""
    cands = []
    score_jobs = []   # rejected candidates need a fresh DV score
    for pid in R.PIDS:
        for arm in ("same", "cross"):
            u = R.load(f"R3__{arm}__{pid}")
            if not u:
                continue
            for e in u["round_log"]:
                r = e["round"]
                champ_before = traj_net(pid, arm, r - 1)
                for i, a in enumerate(e.get("patch_attempts", [])):
                    admitted = a["gate"]["admit"]
                    aid = f"R3__{arm}__{pid}__r{r}__a{i}"
                    if admitted:
                        cand_net_uid = None  # use traj(r)
                    else:
                        cand_net_uid = f"r5rej__{aid}"
                        score_jobs.append((cand_net_uid, pid, a["candidate"]))
                    static_new = sum(1 for m in a["gate"]["members"] if m["new_flaws"])
                    cands.append({"aid": aid, "pid": pid, "arm": arm, "round": r, "admitted_static": admitted,
                                  "champ_before_net": champ_before, "cand_net_uid": cand_net_uid,
                                  "candidate": a["candidate"], "objections": e.get("objections", []),
                                  "static_admit": admitted, "static_members_flagging_new": static_new,
                                  "static_votes": a["gate"]["admit_votes"]})
    return cands, score_jobs


def main():
    cands, score_jobs = gather()
    print(f"[r5] {len(cands)} R3 candidate decisions; scoring {len(score_jobs)} rejected candidates (resumable)", flush=True)
    # 1) DV-score the rejected candidates (admitted ones reuse the trajectory score)
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        list(ex.map(lambda j: R.score_output(*j), score_jobs))
    # 2) challenge-gate every candidate (resumable, cached per attempt)
    print(f"[r5] running challenge-gate on {len(cands)} candidates...", flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(challenge_gate, c["pid"], c["arm"], c["aid"],
                          R.PROBLEMS[c["pid"]]["problem"], c["candidate"], c["objections"]): c["aid"] for c in cands}
        for f in cf.as_completed(futs):
            f.result(); done += 1
            if done % 10 == 0:
                print(f"[r5] challenge-gate {done}/{len(cands)}", flush=True)
    # 3) assemble DV-truth + both gates' decisions
    rows = []
    for c in cands:
        if c["cand_net_uid"] is None:
            cand_net = traj_net(c["pid"], c["arm"], c["round"])
        else:
            s = R.load(f"score__{c['cand_net_uid']}")
            cand_net = s["net_flaws_remaining"] if s else None
        cb = c["champ_before_net"]
        if cand_net is None or cb is None:
            continue
        dv_regression = cand_net > cb            # the candidate made it WORSE by the held-out DV
        dv_clean = cand_net <= cb
        cg = R.load(f"chalgate__{c['aid']}")
        rows.append({"aid": c["aid"], "champ_before_net": cb, "cand_net": cand_net,
                     "dv_regression": dv_regression, "dv_clean": dv_clean,
                     "static_admit": c["static_admit"], "static_flagging_new": c["static_members_flagging_new"],
                     "challenge_admit": cg["admit"], "challenge_flagging_new": cg["members_flagging_new"]})

    def detector_stats(rows, block_key):
        """block_key True == gate would BLOCK. Score against dv_regression as ground truth."""
        tp = sum(1 for r in rows if r[block_key] and r["dv_regression"])   # blocked a real regression
        fn = sum(1 for r in rows if not r[block_key] and r["dv_regression"])  # missed a regression
        fp = sum(1 for r in rows if r[block_key] and not r["dv_regression"])  # blocked a clean one
        tn = sum(1 for r in rows if not r[block_key] and not r["dv_regression"])
        reg = tp + fn
        recall = round(tp / reg, 2) if reg else None      # of real regressions, fraction caught
        prec = round(tp / (tp + fp), 2) if (tp + fp) else None  # of blocks, fraction that were real
        return {"caught_regressions": f"{tp}/{reg}", "recall_on_regressions": recall,
                "block_precision": prec, "false_blocks": fp, "missed_regressions": fn}

    # "block" signals: a gate blocks when it does NOT admit; "flag" = it detected a new flaw
    for r in rows:
        r["static_block"] = not r["static_admit"]
        r["challenge_block"] = not r["challenge_admit"]
        r["static_detect_new"] = r["static_flagging_new"] >= 2     # majority of static panel saw a new flaw
        r["challenge_detect_new"] = r["challenge_flagging_new"] >= 2

    n = len(rows)
    n_reg = sum(1 for r in rows if r["dv_regression"])
    summary = {
        "EXPLORATORY": True, "unit": "candidate decision (escapes n=8: this is n=%d)" % n,
        "n_candidates": n, "n_dv_regressions": n_reg, "n_dv_clean": n - n_reg,
        "static_gate_block":     detector_stats(rows, "static_block"),
        "challenge_gate_block":  detector_stats(rows, "challenge_block"),
        "static_detect_new":     detector_stats(rows, "static_detect_new"),
        "challenge_detect_new":  detector_stats(rows, "challenge_detect_new"),
        "agreement_between_gates": round(sum(1 for r in rows if r["static_admit"] == r["challenge_admit"]) / n, 2) if n else None,
        "rows": rows,
    }
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    (R.PILOT / "analysis" / "r5-challenge-gate.json").write_text(json.dumps(summary, indent=2))

    print(f"\n=== CHALLENGE-GATE vs STATIC-GATE — head-to-head on {n} candidate decisions ===")
    print(f"  DV ground truth: {n_reg} regressions, {n - n_reg} clean")
    print(f"  (a gate should BLOCK regressions and ADMIT clean ones)\n")
    for label, key in [("STATIC gate (verifier-audit move)", "static_gate_block"),
                       ("CHALLENGE gate (validated challenge move)", "challenge_gate_block")]:
        s = summary[key]
        print(f"  {label}:")
        print(f"     caught {s['caught_regressions']} regressions (recall {s['recall_on_regressions']}); "
              f"block precision {s['block_precision']}; false blocks {s['false_blocks']}; missed {s['missed_regressions']}")
    print(f"\n  pure new-flaw DETECTION (majority of panel flags a new flaw):")
    for label, key in [("static audit", "static_detect_new"), ("challenge", "challenge_detect_new")]:
        s = summary[key]
        print(f"     {label:10s}: caught {s['caught_regressions']} regressions (recall {s['recall_on_regressions']}), block precision {s['block_precision']}")
    print(f"\n  the two gates agree on {summary['agreement_between_gates']} of decisions")
    print("\nwrote analysis/r5-challenge-gate.json")


if __name__ == "__main__":
    main()
