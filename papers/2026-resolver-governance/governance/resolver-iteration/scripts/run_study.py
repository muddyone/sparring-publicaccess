#!/usr/bin/env python3
"""Resolver-iteration study harness (pre-reg: resolver-iteration-prereg-2026-06-29).

Reuses §6.3 (catch-rate-v3): the 8 problems, the Claude-produced originals (R0),
and the >=2-of-3 panel flaw set as the fixed denominator. Produces final outputs
for R1 / R2 / R1', re-audits each for net-flaw accounting, and blind-codes which
denominator flaws remain. Two vendor arms: same-vendor (Claude challenger),
cross-vendor (GPT-5.2 challenger). R1' and R0 are vendor-independent.

Resumable: every unit writes runs/<id>.json; existing files are skipped.

Usage:
  python3 run_study.py produce        # stage A: generate R1/R2/R1' final outputs
  python3 run_study.py score          # stage B: audit + code every final output
  python3 run_study.py all            # both, in order
"""
import os, sys, json, hashlib, random, pathlib, concurrent.futures as cf
import lib_llm as L

PILOT = pathlib.Path(__file__).resolve().parents[1]
V63 = PILOT.parent / "catch-rate-v3-2026-06-28"
RUNS = PILOT / "runs"
RUNS.mkdir(exist_ok=True)

CLAUDE = "claude-opus-4-8"
GPT = "gpt-5.2"
CAP = 5                  # hard round cap (pre-reg §6)
# claude-opus-4-8 rejects `temperature`, so the 3-auditor panel is diversified by
# ANGLE instead of temperature -- three independent auditors with distinct lenses.
AUDIT_ANGLES = [
    "Focus especially on correctness and the core decision: is the central recommendation actually sound, do the numbers/mechanisms hold, and would following it cause a real failure?",
    "Focus especially on the constraints and edge cases the problem names: are any of the stated requirements unmet, mishandled under failure/partition/scale, or quietly traded away?",
    "Focus especially on feasibility and second-order effects: operational/team/timeline realism, cost, and downstream consequences the recommendation does not account for.",
]
WORKERS = 8

# ----------------------------------------------------------------------------- data
PROBLEMS = {p["id"]: p for p in json.load(open(V63 / "problems.json"))}
R0 = json.load(open(V63 / "recommendations.json"))            # id -> recommendation str
_CONS = json.load(open(V63 / "consensus-flaws.json"))         # id -> [{flaw, auditors}]
# Denominator = >=2-of-3 panel-confirmed flaws (the fixed denominator).
DENOM = {pid: [f["flaw"] for f in flaws if f.get("auditors", 0) >= 2] for pid, flaws in _CONS.items()}
PIDS = list(PROBLEMS.keys())
assert sum(len(v) for v in DENOM.values()) == 31, sum(len(v) for v in DENOM.values())


def save(unit_id, obj):
    (RUNS / f"{unit_id}.json").write_text(json.dumps(obj, indent=2))


def load(unit_id):
    p = RUNS / f"{unit_id}.json"
    return json.loads(p.read_text()) if p.exists() else None


def challenger_call(vendor, system, user):
    if vendor == "claude":
        return L.claude_json(CLAUDE, system, user, max_tokens=6000, temperature=0.8)
    return L.gpt_json(GPT, system, user, max_completion_tokens=16000)


# ----------------------------------------------------------------------------- prompts
CHAL_SYS = (
    "You are an adversarial Challenger reviewing a recommendation another expert produced for a "
    "hard decision problem. Work from a DIFFERENT angle and evidence base than the author. Your job "
    "is to find MATERIAL would-ship flaws: errors that would change the decision or ship a real defect "
    "-- not nitpicks, not style, not 'consider also' additions. Be polite, not pleasing: do not smooth "
    "the road, and do not soften a real objection. But be honest in BOTH directions -- if the "
    "recommendation has no remaining material flaw, say so plainly; do NOT invent objections to prolong "
    "the exchange, and do NOT concede prematurely just to be agreeable. Assign each objection a short "
    "stable handle (snake_case) so it can be tracked across rounds."
)
CHAL_R1_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION UNDER REVIEW:\n{rec}\n\n"
    "Return JSON: {{\"objections\": [{{\"handle\": str, \"text\": str}}], "
    "\"material_objections_remaining\": bool}}"
)
CHAL_RN_USER = (
    "PROBLEM:\n{problem}\n\nREVISED RECOMMENDATION (the author just revised it):\n{rec}\n\n"
    "YOUR OBJECTIONS FROM THE PREVIOUS ROUND (handles + text):\n{prev}\n\n"
    "Re-evaluate the revised recommendation. For each previous objection, decide if the revision "
    "ADEQUATELY addressed it. Raise any genuinely NEW material flaw the revision introduced or that "
    "you now see. Return JSON: {{\"objections\": [{{\"handle\": str, \"text\": str, "
    "\"status\": \"persists\"|\"new\"}}], \"resolved_last_round\": [handle, ...], "
    "\"material_objections_remaining\": bool}}"
)

PROD_SYS = (
    "You are the senior expert who produced a recommendation for a hard decision problem. A Challenger "
    "has raised objections. Revise your recommendation to fix every objection you judge MATERIAL and "
    "valid -- change the core decision if the objection warrants it. Keep it a crisp, shippable "
    "recommendation of similar length, not an essay. If an objection is wrong or immaterial you may hold "
    "your position, but say briefly why. Do not introduce new unforced flaws."
)
PROD_USER = (
    "PROBLEM:\n{problem}\n\nYOUR CURRENT RECOMMENDATION:\n{rec}\n\nCHALLENGER OBJECTIONS:\n{obj}\n\n"
    "Return JSON: {{\"revised_recommendation\": str, "
    "\"dispositions\": [{{\"handle\": str, \"action\": \"addressed\"|\"rejected\", \"note\": str}}], "
    "\"accept_as_final\": bool}}  -- accept_as_final is true only if you believe the revised "
    "recommendation now carries no material would-ship flaw and you would ship it."
)

SELF_SYS = (
    "You produced this recommendation for a hard decision problem. Critically review your OWN work for "
    "MATERIAL would-ship flaws -- decision-changing errors or real defects, not nitpicks -- and revise "
    "to fix any you find. Be your own harshest critic; this is a self-review with no outside challenger. "
    "Keep it a crisp, shippable recommendation of similar length."
)
SELF_USER = (
    "PROBLEM:\n{problem}\n\nYOUR CURRENT RECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"revised_recommendation\": str, \"self_found_flaws\": [str]}}"
)

AUDIT_SYS = (
    "You are an independent auditor. Enumerate the MATERIAL would-ship flaws in the recommendation below "
    "-- ones that would change the decision or ship a real defect, not nitpicks, not style. You are blind "
    "to how the recommendation was produced. State each flaw as one concrete, self-contained sentence. "
    "If you find no material flaw, return an empty list -- do not manufacture flaws."
)
AUDIT_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION:\n{rec}\n\nReturn JSON: {{\"flaws\": [str, ...]}}"
)

MERGE_SYS = (
    "Three independent auditors each listed the material flaws they found in one recommendation. Cluster "
    "their flaws into distinct underlying issues. For each distinct issue, report how many of the three "
    "auditors raised it (1-3). Two phrasings of the same underlying issue count as the same issue."
)
MERGE_USER = (
    "AUDITOR 1 FLAWS:\n{a1}\n\nAUDITOR 2 FLAWS:\n{a2}\n\nAUDITOR 3 FLAWS:\n{a3}\n\n"
    "Return JSON: {{\"issues\": [{{\"flaw\": str, \"auditors\": int}}]}}"
)

CODE_SYS = (
    "You are coding which KNOWN flaws remain in a recommendation. You are given the problem, a fixed "
    "numbered list of known material flaws, and a candidate recommendation. For EACH known flaw, decide "
    "whether that specific flaw still REMAINS in this recommendation or has been RESOLVED by it. Judge "
    "only the presence of that specific flaw. You are blind to how the recommendation was produced."
)
CODE_USER = (
    "PROBLEM:\n{problem}\n\nKNOWN MATERIAL FLAWS (the denominator):\n{flaws}\n\n"
    "CANDIDATE RECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"codes\": [{{\"index\": int, \"status\": \"REMAIN\"|\"RESOLVED\", \"note\": str}}]}}"
)

# --- R3 (admissions-controlled iterate) — EXPLORATORY, not pre-registered. See R3-design-spec-EXPLORATORY.md.
# Producer is told to patch MINIMALLY (the gate punishes churny full rewrites).
PROD_R3_SYS = (
    "You are the senior expert who produced a recommendation for a hard decision problem. A Challenger "
    "has raised objections. Produce the SMALLEST, most surgical revision that fixes the MATERIAL, valid "
    "objections -- change only what a specific objection forces you to change, and preserve everything "
    "else verbatim. Do NOT rewrite for style or re-argue settled points: a release gate will REJECT your "
    "revision if it introduces any new flaw as severe as the one it fixes, and the prior version will be "
    "kept instead. If an objection is wrong or immaterial, hold your position and say briefly why. Keep it "
    "a crisp, shippable recommendation of similar length."
)
PROD_R3_RETRY_NOTE = (
    "\n\nYOUR PREVIOUS REVISION WAS REJECTED BY THE RELEASE GATE for introducing new material flaw(s) as "
    "severe as what it fixed:\n{blockers}\nProduce a TIGHTER, more minimal patch that fixes the objection "
    "without that regression. Touch less, not more."
)

# Each gate verifier returns JUDGMENTS ONLY (resolved set + severities, new flaws + severities);
# the admit rule is applied deterministically in code. 3-member >=2-of-3 cross-vendor panel.
GATE_SYS = (
    "You are a release-gate verifier. You are given a PROBLEM, the CURRENT recommendation, the Challenger's "
    "STANDING objections against CURRENT, and a CANDIDATE revision the author proposes to replace CURRENT. "
    "Judge the candidate against the current version. For EACH standing objection, decide whether the "
    "CANDIDATE resolves it, and rate that objection's severity. Separately, list any genuinely NEW material "
    "would-ship flaw the CANDIDATE introduces that was NOT present in CURRENT, each with its severity. Rate "
    "severity on a 3-point scale: 1=low (minor would-ship issue), 2=medium, 3=high (decision-changing). Be "
    "honest in both directions -- do not rubber-stamp a churny rewrite, and do not invent regressions to "
    "block a clean minimal fix."
)
GATE_USER = (
    "PROBLEM:\n{problem}\n\nCURRENT RECOMMENDATION:\n{current}\n\nSTANDING OBJECTIONS:\n{obj}\n\n"
    "CANDIDATE REVISION:\n{candidate}\n\n"
    "Return JSON: {{\"objection_judgments\": [{{\"handle\": str, \"resolved\": bool, \"severity\": 1|2|3}}], "
    "\"new_flaws\": [{{\"text\": str, \"severity\": 1|2|3}}]}}"
)

NEW_SYS = (
    "An audit panel found material flaws in a REVISED recommendation. Decide which panel flaws are "
    "genuinely NEW versus which are just rewordings of an ORIGINAL known flaw. Mark each panel flaw "
    "MATCHES_ORIGINAL (it is one of the original known flaws, possibly reworded) or NEW (a different "
    "material flaw not in the original list)."
)
NEW_USER = (
    "ORIGINAL KNOWN FLAWS:\n{orig}\n\nPANEL FLAWS FOUND IN THE REVISED RECOMMENDATION:\n{panel}\n\n"
    "Return JSON: {{\"matches\": [{{\"panel_index\": int, \"verdict\": "
    "\"MATCHES_ORIGINAL\"|\"NEW\", \"orig_index\": int|null, \"note\": str}}]}}"
)


def fmt_objections(objs):
    return "\n".join(f"- [{o.get('handle','?')}] {o.get('text','')}" for o in objs) or "(none)"


# ----------------------------------------------------------------------------- stage A: produce
def run_r1prime(pid):
    """Effort-matched control: producer self-revises twice, no challenger. Vendor-independent."""
    uid = f"R1prime__{pid}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    rec = R0[pid]
    steps = []
    for _ in range(2):
        out = L.claude_json(CLAUDE, SELF_SYS, SELF_USER.format(problem=problem, rec=rec), max_tokens=6000, temperature=0.7)
        rec = out["revised_recommendation"]
        steps.append(out.get("self_found_flaws", []))
    save(uid, {"unit": uid, "condition": "R1prime", "pid": pid, "final_output": rec, "self_found": steps})
    return uid


def run_r1(pid, arm):
    """Single challenge + one revision."""
    vendor = "claude" if arm == "same" else "gpt"
    uid = f"R1__{arm}__{pid}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    chal = challenger_call(vendor, CHAL_SYS, CHAL_R1_USER.format(problem=problem, rec=R0[pid]))
    rev = L.claude_json(CLAUDE, PROD_SYS, PROD_USER.format(problem=problem, rec=R0[pid], obj=fmt_objections(chal["objections"])), max_tokens=6000, temperature=0.7)
    save(uid, {"unit": uid, "condition": "R1", "arm": arm, "pid": pid,
               "final_output": rev["revised_recommendation"],
               "challenge": chal, "revision": rev})
    return uid


def run_r2(pid, arm):
    """Iterate to agreement (the gate): challenger <-> producer until CONVERGED / STALLED / CAPPED."""
    vendor = "claude" if arm == "same" else "gpt"
    uid = f"R2__{arm}__{pid}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    current = R0[pid]
    last_accept = True          # producer shipped R0 -> implicitly accepts it
    prev_objs = None
    no_move = 0
    terminal = None
    log = []
    for r in range(1, CAP + 1):
        if prev_objs is None:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_R1_USER.format(problem=problem, rec=current))
        else:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_RN_USER.format(problem=problem, rec=current, prev=fmt_objections(prev_objs)))
        remaining = bool(chal.get("material_objections_remaining"))
        moved = bool(chal.get("resolved_last_round")) or any(o.get("status") == "new" for o in chal.get("objections", []))
        entry = {"round": r, "challenger_remaining": remaining, "moved": moved,
                 "objections": chal.get("objections", []), "resolved_last_round": chal.get("resolved_last_round", [])}
        # Convergence check on the standing output (both agree).
        if not remaining and last_accept:
            terminal = "CONVERGED"
            log.append(entry)
            break
        # Stall check (>=2 rounds; 2 consecutive no-move rounds).
        if r >= 2:
            no_move = 0 if moved else no_move + 1
            if no_move >= 2:
                terminal = "STALLED"
                log.append(entry)
                break
        # Producer revises against current objections.
        rev = L.claude_json(CLAUDE, PROD_SYS, PROD_USER.format(problem=problem, rec=current, obj=fmt_objections(chal["objections"])), max_tokens=6000, temperature=0.7)
        current = rev["revised_recommendation"]
        last_accept = bool(rev.get("accept_as_final"))
        entry["revised"] = current
        entry["producer_accept"] = last_accept
        log.append(entry)
        prev_objs = chal["objections"]
    else:
        terminal = "CAPPED"
    save(uid, {"unit": uid, "condition": "R2", "arm": arm, "pid": pid,
               "final_output": current, "terminal_state": terminal,
               "rounds": len(log), "round_log": log})
    return uid


MAX_PATCH_ATTEMPTS = 2          # tries per round to land an admissible patch (R3)
PROD_R3_MAXTOK = 9000           # complex problems truncated full-rec JSON at 6000; budget generously
# --- R3 v2 dials (EXPLORATORY recalibration, Bart 2026-06-29; see R3-design-spec-EXPLORATORY.md changelog) ---
NEW_FLAW_BUDGET = 3             # v2: cap on CUMULATIVE admitted new-flaw severity per ceremony (the
                               # running-total guard the v1 warehouse-siting 4->5 regression proved missing)
HARD_CAP_V2 = 10               # v2: round cap goes dynamic (stop on CONVERGED/EXHAUSTED); this is only a
                               # runaway backstop, not the intended stop (v1's CAP=5 truncated productive gains)
GATE_LENSES = AUDIT_ANGLES      # reuse the 3 audit lenses as the 3 gate-verifier lenses
GATE_VENDORS = ("claude", "claude", "gpt")   # cross-vendor panel: 2 Claude (lenses) + 1 GPT


def _coerce_obj(x, list_key):
    """Tolerant-JSON sometimes yields a bare list when an object was asked for; wrap it so
    downstream .get() calls don't crash. (One GPT-challenger arm hit this.)"""
    if isinstance(x, dict):
        return x
    if isinstance(x, list):
        return {list_key: x}
    return {}


def gate_member(vendor, lens, problem, current, objs, candidate):
    """One verifier's judgments; returns (resolved_handles_with_sev, new_flaws_with_sev, raw)."""
    sys = GATE_SYS + " " + lens
    user = GATE_USER.format(problem=problem, current=current, obj=fmt_objections(objs), candidate=candidate)
    if vendor == "claude":
        out = L.claude_json(CLAUDE, sys, user, max_tokens=2500)
    else:
        out = L.gpt_json(GPT, sys, user)
    out = _coerce_obj(out, "objection_judgments")
    resolved = {j["handle"]: int(j.get("severity", 2))
                for j in out.get("objection_judgments", []) if j.get("resolved")}
    new = [(nf.get("text", ""), int(nf.get("severity", 2))) for nf in out.get("new_flaws", [])]
    return resolved, new, out


def gate_verdict(problem, current, objs, candidate):
    """>=2-of-3 cross-vendor panel. Admit rule applied deterministically per member.

    member_admit = (>=1 objection resolved) AND (every new flaw severity < max resolved severity)
    gate_admit   = members voting admit >= 2
    Returns (admit:bool, record:dict) — record is the governance-trail entry for this decision.
    """
    members = []
    admit_votes = 0
    blockers = []   # new flaws that blocked an otherwise-resolving member
    for vendor, lens in zip(GATE_VENDORS, GATE_LENSES):
        resolved, new, raw = gate_member(vendor, lens, problem, current, objs, candidate)
        max_res_sev = max(resolved.values()) if resolved else 0
        equal_or_worse = [t for (t, s) in new if s >= max_res_sev] if resolved else [t for (t, _) in new]
        member_admit = bool(resolved) and not equal_or_worse
        if member_admit:
            admit_votes += 1
        else:
            blockers.extend(equal_or_worse)
        members.append({"vendor": vendor, "resolved": resolved, "new_flaws": new,
                        "max_resolved_severity": max_res_sev, "member_admit": member_admit})
    admit = admit_votes >= 2
    # v2 budget accounting: a patch's "new-flaw cost" = median across members of each member's
    # summed new-flaw severity (robust to one noisy verifier). v1 ignores this field.
    costs = sorted(sum(s for (_t, s) in m["new_flaws"]) for m in members)
    new_flaw_cost = costs[1]   # median of 3
    record = {"admit": admit, "admit_votes": admit_votes, "members": members,
              "blockers": blockers[:6], "new_flaw_cost": new_flaw_cost}
    return admit, record


def run_r3(pid, arm):
    """Admissions-controlled iterate: like R2, but every revision must pass a >=2-of-3 cross-vendor
    gate (Pareto-improving under a severity-relative bar) to be committed. EXPLORATORY."""
    vendor = "claude" if arm == "same" else "gpt"
    uid = f"R3__{arm}__{pid}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    current = R0[pid]
    last_accept = True          # producer shipped R0 -> implicitly accepts it
    prev_objs = None
    terminal = None
    trail = []                  # governance trail: one entry per round
    for r in range(1, CAP + 1):
        if prev_objs is None:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_R1_USER.format(problem=problem, rec=current))
        else:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_RN_USER.format(problem=problem, rec=current, prev=fmt_objections(prev_objs)))
        if isinstance(chal, list):      # bare-list response -> remaining keyed off whether objs exist
            chal = {"objections": chal, "material_objections_remaining": bool(chal)}
        remaining = bool(chal.get("material_objections_remaining"))
        objs = chal.get("objections", [])
        entry = {"round": r, "challenger_remaining": remaining, "objections": objs,
                 "resolved_last_round": chal.get("resolved_last_round", []),
                 "patch_attempts": []}
        if not remaining and last_accept:
            terminal = "CONVERGED"
            trail.append(entry)
            break
        # Producer attempts an admissible minimal patch (up to MAX_PATCH_ATTEMPTS).
        admitted = False
        blockers_note = ""
        for attempt in range(1, MAX_PATCH_ATTEMPTS + 1):
            sys = PROD_R3_SYS + (PROD_R3_RETRY_NOTE.format(blockers="; ".join(blockers_note) if isinstance(blockers_note, list) else blockers_note) if blockers_note else "")
            rev = L.claude_json(CLAUDE, sys, PROD_USER.format(problem=problem, rec=current, obj=fmt_objections(objs)), max_tokens=PROD_R3_MAXTOK)
            candidate = rev["revised_recommendation"]
            admit, gate_rec = gate_verdict(problem, current, objs, candidate)
            entry["patch_attempts"].append({"attempt": attempt, "candidate": candidate,
                                            "producer_accept": bool(rev.get("accept_as_final")),
                                            "gate": gate_rec})
            if admit:
                current = candidate
                last_accept = bool(rev.get("accept_as_final"))
                admitted = True
                break
            blockers_note = gate_rec["blockers"] or "the revision did not resolve any standing objection"
        prev_objs = objs
        trail.append(entry)
        if not admitted:
            terminal = "EXHAUSTED"      # no admissible improving move this round
            break
    else:
        terminal = "CAPPED"
    save(uid, {"unit": uid, "condition": "R3", "arm": arm, "pid": pid,
               "final_output": current, "terminal_state": terminal,
               "rounds": len(trail), "round_log": trail})
    return uid


def run_r3v2(pid, arm):
    """R3 v2 (EXPLORATORY recalibration): admissions-controlled iterate with (a) a GLOBAL new-flaw
    budget on top of the per-patch severity-relative bar, and (b) a dynamic round cap (stop on
    CONVERGED/EXHAUSTED, hard backstop only). The budget is the running-total guard v1 lacked."""
    vendor = "claude" if arm == "same" else "gpt"
    uid = f"R3v2__{arm}__{pid}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    current = R0[pid]
    last_accept = True
    prev_objs = None
    terminal = None
    nf_budget_used = 0           # cumulative admitted new-flaw severity (the global guard)
    trail = []
    for r in range(1, HARD_CAP_V2 + 1):
        if prev_objs is None:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_R1_USER.format(problem=problem, rec=current))
        else:
            chal = challenger_call(vendor, CHAL_SYS, CHAL_RN_USER.format(problem=problem, rec=current, prev=fmt_objections(prev_objs)))
        if isinstance(chal, list):
            chal = {"objections": chal, "material_objections_remaining": bool(chal)}
        remaining = bool(chal.get("material_objections_remaining"))
        objs = chal.get("objections", [])
        entry = {"round": r, "challenger_remaining": remaining, "objections": objs,
                 "resolved_last_round": chal.get("resolved_last_round", []),
                 "nf_budget_used_before": nf_budget_used, "patch_attempts": []}
        if not remaining and last_accept:
            terminal = "CONVERGED"
            trail.append(entry)
            break
        admitted = False
        blockers_note = ""
        for attempt in range(1, MAX_PATCH_ATTEMPTS + 1):
            note = blockers_note
            sys = PROD_R3_SYS + (PROD_R3_RETRY_NOTE.format(blockers="; ".join(note) if isinstance(note, list) else note) if note else "")
            rev = L.claude_json(CLAUDE, sys, PROD_USER.format(problem=problem, rec=current, obj=fmt_objections(objs)), max_tokens=PROD_R3_MAXTOK)
            candidate = rev["revised_recommendation"]
            admit, gate_rec = gate_verdict(problem, current, objs, candidate)
            cost = gate_rec["new_flaw_cost"]
            over_budget = admit and (nf_budget_used + cost > NEW_FLAW_BUDGET)
            committed = admit and not over_budget
            gate_rec["over_budget"] = over_budget
            gate_rec["budget_after_if_committed"] = nf_budget_used + cost
            entry["patch_attempts"].append({"attempt": attempt, "candidate": candidate,
                                            "producer_accept": bool(rev.get("accept_as_final")),
                                            "gate": gate_rec})
            if committed:
                current = candidate
                last_accept = bool(rev.get("accept_as_final"))
                nf_budget_used += cost
                admitted = True
                break
            if over_budget:
                blockers_note = [f"adding new flaws would exceed the ceremony's new-flaw budget "
                                 f"(used {nf_budget_used}/{NEW_FLAW_BUDGET}); resolve the objection WITHOUT introducing anything new"]
            else:
                blockers_note = gate_rec["blockers"] or "the revision did not resolve any standing objection"
        prev_objs = objs
        trail.append(entry)
        if not admitted:
            terminal = "EXHAUSTED"
            break
    else:
        terminal = "CAPPED"
    save(uid, {"unit": uid, "condition": "R3v2", "arm": arm, "pid": pid,
               "final_output": current, "terminal_state": terminal,
               "rounds": len(trail), "new_flaw_budget_used": nf_budget_used,
               "new_flaw_budget": NEW_FLAW_BUDGET, "round_log": trail})
    return uid


def stage_produce():
    jobs = []
    for pid in PIDS:
        jobs.append(("r1prime", pid, None))
        for arm in ("same", "cross"):
            jobs.append(("r1", pid, arm))
            jobs.append(("r2", pid, arm))
            jobs.append(("r3", pid, arm))
            jobs.append(("r3v2", pid, arm))
    fns = {"r1prime": lambda pid, arm: run_r1prime(pid),
           "r1": lambda pid, arm: run_r1(pid, arm),
           "r2": lambda pid, arm: run_r2(pid, arm),
           "r3": lambda pid, arm: run_r3(pid, arm),
           "r3v2": lambda pid, arm: run_r3v2(pid, arm)}
    _parallel(jobs, fns, "PRODUCE")


# ----------------------------------------------------------------------------- stage B: score
def final_outputs():
    """Yield (output_id, pid, condition, arm, text). R0 is definitional, not scored here."""
    outs = []
    for pid in PIDS:
        r1p = load(f"R1prime__{pid}")
        if r1p:
            outs.append((f"R1prime__{pid}", pid, "R1prime", None, r1p["final_output"]))
        for arm in ("same", "cross"):
            for cond in ("R1", "R2", "R3", "R3v2"):
                u = load(f"{cond}__{arm}__{pid}")
                if u:
                    outs.append((u["unit"], pid, cond, arm, u["final_output"]))
    return outs


def score_output(output_id, pid, text):
    uid = f"score__{output_id}"
    if load(uid):
        return uid
    problem = PROBLEMS[pid]["problem"]
    denom = DENOM[pid]
    flaws_numbered = "\n".join(f"{i}. {f}" for i, f in enumerate(denom))
    # 1) audit panel (3 independent auditors, diversified by angle)
    audits = []
    for angle in AUDIT_ANGLES:
        a = L.claude_json(CLAUDE, AUDIT_SYS + " " + angle, AUDIT_USER.format(problem=problem, rec=text), max_tokens=2500)
        audits.append(a.get("flaws", []))
    merged = L.claude_json(CLAUDE, MERGE_SYS, MERGE_USER.format(
        a1=json.dumps(audits[0]), a2=json.dumps(audits[1]), a3=json.dumps(audits[2])), max_tokens=3000, temperature=0.3)
    panel = [iss["flaw"] for iss in merged.get("issues", []) if iss.get("auditors", 0) >= 2]
    # 2) remaining-coding against the fixed denominator (blind to condition)
    coded = L.claude_json(CLAUDE, CODE_SYS, CODE_USER.format(problem=problem, flaws=flaws_numbered, rec=text), max_tokens=4500, temperature=0.2)
    codes = coded.get("codes", [])
    remain = sum(1 for c in codes if c.get("status") == "REMAIN")
    # 3) new-flaw matching (which panel flaws are NEW vs original)
    if panel:
        panel_numbered = "\n".join(f"{i}. {f}" for i, f in enumerate(panel))
        nf = L.claude_json(CLAUDE, NEW_SYS, NEW_USER.format(orig=flaws_numbered, panel=panel_numbered), max_tokens=2500, temperature=0.2)
        new_flaws = [m for m in nf.get("matches", []) if m.get("verdict") == "NEW"]
    else:
        new_flaws = []
    new_count = len(new_flaws)
    net = remain + new_count
    save(uid, {"unit": uid, "output_id": output_id, "pid": pid,
               "denom_count": len(denom), "remain": remain, "new_count": new_count,
               "net_flaws_remaining": net,
               "audits": audits, "panel_consensus": panel, "codes": codes, "new_flaws": new_flaws})
    return uid


def stage_score():
    outs = final_outputs()
    # Order-rotate so processing order carries no condition signal (blind-coding control).
    rng = random.Random(20260629)
    rng.shuffle(outs)
    blind_map = [{"slot": i, "output_id": o[0], "condition": o[2], "arm": o[3]} for i, o in enumerate(outs)]
    # Preserve prior blind maps; each exploratory addition writes its own file.
    has_v2 = any(o[2] == "R3v2" for o in outs)
    if has_v2:
        map_name = "coding-blind-map-r3v2.json"
    elif (PILOT / "coding-blind-map.json").exists():
        map_name = "coding-blind-map-r3.json"
    else:
        map_name = "coding-blind-map.json"
    (PILOT / map_name).write_text(json.dumps(blind_map, indent=2))
    jobs = [("score", o, None) for o in outs]
    fns = {"score": lambda o, _a: score_output(o[0], o[1], o[4])}
    _parallel(jobs, fns, "SCORE")


# ----------------------------------------------------------------------------- runner
def _parallel(jobs, fns, label):
    done = 0
    total = len(jobs)
    errors = []
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(fns[kind], a, b): (kind, a, b) for (kind, a, b) in jobs}
        for fut in cf.as_completed(futs):
            kind, a, b = futs[fut]
            try:
                fut.result()
            except Exception as e:  # noqa: BLE001
                errors.append((kind, a, b, repr(e)))
                print(f"[{label}] ERROR {kind} {a} {b}: {repr(e)[:200]}", flush=True)
            done += 1
            print(f"[{label}] {done}/{total} done", flush=True)
    if errors:
        print(f"[{label}] {len(errors)} ERRORS -- re-run to retry (resumable).", flush=True)
    else:
        print(f"[{label}] complete, no errors.", flush=True)
    return errors


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("produce", "all"):
        stage_produce()
    if cmd in ("score", "all"):
        stage_score()
    print("DONE", cmd)
