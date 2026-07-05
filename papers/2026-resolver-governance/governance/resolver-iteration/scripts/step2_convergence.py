#!/usr/bin/env python3
"""Step 2: convergence-pressured prompt-craft — does it stop the decision churn? (EXPLORATORY)

The debiased re-score showed the multi-round treadmill is NOT judge bias (anti-bias judge behaved the
same) but DECISION CHURN: only 4/12 reached a stable decision by R1; 8/12 kept flipping the core choice
(some oscillating a->c->a). Root cause looked like prompt-craft: the producer was told to "change the core
decision if the objection warrants it" every round, and the challenger never declared convergence.

This is the OFAT test of Bart's prompt-craft theory: change ONLY the challenger + producer prompts
(same problems, same R0, same 3 forced rounds, same anti-bias CF judge + decision-stability metric),
and see if the decision stabilizes.

New prompts:
  * Challenger: RISING materiality bar. Round 1 = any material flaw. Round 2+ = ONLY decision-changing
    flaws; refinements are treated as resolved; declares convergence (material_objections_remaining=false)
    when only refinements remain — converging is success, not failure. Tags each objection decision_changing.
  * Producer: DEFEND the settled decision. Prefer refining the SAME option; only switch the core decision
    for a genuinely decision-changing flaw, stated explicitly. No oscillation. Hold + accept_as_final when sound.

Target (bias-free): decision-stability jumps well above baseline 4/12, WITHOUT suppressing the real
R0->R1 correction. If it still churns with convergence-pressured prompts -> stronger case for step 3
(external grounding). Resumable.

Usage: python3 step2_convergence.py [--k 3]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
from rescore_debiased import cf_verdict          # anti-bias pairwise judge (parameterized by tag)

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
BASELINE = R.PILOT / "analysis" / "rescore-debiased.json"
OUT_JSON = R.PILOT / "analysis" / "step2-convergence.json"
STEPS = [("R0", "R1"), ("R1", "R2"), ("R2", "R3"), ("R1", "R3")]

CHAL2_SYS = (
    "You are an adversarial Challenger reviewing a recommendation for a hard decision, working from a "
    "different angle than the author. Find MATERIAL would-ship flaws, but be DISCIPLINED about materiality, "
    "and raise your bar with each round:\n"
    "- A DECISION-CHANGING flaw means: if true, a DIFFERENT option should be chosen, or the recommendation "
    "ships a real defect. These always matter.\n"
    "- A REFINEMENT is a caveat, hedge, nice-to-have, or wording/completeness improvement that does NOT "
    "change which option is right.\n"
    "On round 1, raise any material flaw. On round 2 and later, raise ONLY decision-changing flaws — treat "
    "refinements as already resolved. Be honest in BOTH directions: if the core decision is sound and only "
    "refinements remain, say so plainly and set material_objections_remaining=false. CONVERGING IS SUCCESS, "
    "not failure — do NOT manufacture marginal objections to prolong the exchange, and do NOT concede a real "
    "decision-changing flaw just to converge. Give each objection a stable snake_case handle."
)
CHAL2_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION (this is round {round}):\n{rec}\n\n"
    "PREVIOUS-ROUND OBJECTIONS (handles + text; empty on round 1):\n{prev}\n\n"
    "Return JSON: {{\"objections\": [{{\"handle\": str, \"text\": str, \"decision_changing\": bool}}], "
    "\"material_objections_remaining\": bool}}"
)

PROD2_SYS = (
    "You are the senior expert who produced a recommendation with a core decision (a chosen option). A "
    "Challenger raised objections. Address the genuinely MATERIAL ones while DEFENDING your core decision. "
    "Strong preference: refine the SAME decision — sharpen its justification, add safeguards, correct "
    "details — rather than switch options. Only CHANGE the core decision if an objection genuinely PROVES "
    "the current choice wrong; if you switch, state explicitly why that objection is decision-changing. Do "
    "NOT oscillate or re-litigate settled points. If no objection is materially decision-changing and the "
    "recommendation is sound, HOLD your decision and set accept_as_final=true. Keep it crisp and shippable, "
    "similar length."
)

DEC_SYS = (
    "You identify the single option a recommendation SELECTS as its final choice. Recommendations discuss "
    "several options but commit to one. Return only that one option's label, exactly as the text labels it "
    "(e.g. a, b, c). If it truly commits to none, return 'none'."
)
DEC_USER = "RECOMMENDATION:\n{rec}\n\nReturn JSON: {{\"choice\": str}} — the single option it SELECTS."


def challenge(pid, problem, rec, rnd, prev):
    uid = f"s2_chal__{pid}__r{rnd}"
    c = R.load(uid)
    if not c:
        c = R.challenger_call("gpt", CHAL2_SYS,
                              CHAL2_USER.format(problem=problem, rec=rec, round=rnd, prev=R.fmt_objections(prev)))
        R.save(uid, c)
    return c


def revise(pid, problem, rec, objs, rnd):
    uid = f"s2_rev__{pid}__r{rnd}"
    v = R.load(uid)
    if not v:
        v = L.claude_json(R.CLAUDE, PROD2_SYS,
                          R.PROD_USER.format(problem=problem, rec=rec, obj=R.fmt_objections(objs)),
                          max_tokens=6000, temperature=0.7)
        R.save(uid, v)
    return v


def s2dec(pid, rnd, text):
    uid = f"s2dec__{pid}__{rnd}"
    rec = R.load(uid)
    if not rec:
        out = L.claude_json(R.CLAUDE, DEC_SYS, DEC_USER.format(rec=text), max_tokens=200)
        ch = (out.get("choice", "?") if isinstance(out, dict) else "?") or "?"
        rec = {"choice": str(ch).strip().lower()[:12]}
        R.save(uid, rec)
    return rec["choice"]


def build(pair):
    pid, problem, R0 = pair["id"], pair["problem"], pair["R0"]
    outs = {"R0": R0}
    conv, prev, current = [], [], R0
    for rnd in (1, 2, 3):
        c = challenge(pid, problem, current, rnd, prev)
        objs = c.get("objections", []) if isinstance(c, dict) else []
        v = revise(pid, problem, current, objs, rnd)
        current = (v.get("revised_recommendation", "") if isinstance(v, dict) else "") or current
        outs[f"R{rnd}"] = current
        conv.append({"round": rnd, "n_obj": len(objs),
                     "n_decision_changing": sum(1 for o in objs if isinstance(o, dict) and o.get("decision_changing")),
                     "material_remaining": c.get("material_objections_remaining") if isinstance(c, dict) else None,
                     "accept": v.get("accept_as_final") if isinstance(v, dict) else None})
        prev = objs
    return {"id": pid, "problem": problem, "domain": pair["domain"], "outs": outs, "conv": conv}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()
    k = args.k
    pairs = json.loads(CORPUS.read_text())["problems"]
    print(f"[s2] {len(pairs)} problems; convergence-pressured prompts; 3 forced rounds; k={k}", flush=True)

    # 1. build convergence-pressured trajectories
    built = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(build, p): p["id"] for p in pairs}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); built[r["id"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[s2] build ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
    print(f"[s2] built {len(built)} trajectories; scoring...", flush=True)

    # 2. decisions + CF step verdicts
    def decs(pid):
        o = built[pid]["outs"]
        return {rnd: s2dec(pid, rnd, o[rnd]) for rnd in ("R0", "R1", "R2", "R3") if rnd in o}

    def score(pid):
        o = built[pid]["outs"]; prob = built[pid]["problem"]
        return {f"{a}->{b}": cf_verdict(prob, o[a], o[b], f"s2pwcf__{pid}__{a}{b}", k)
                for a, b in STEPS if a in o and b in o}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        dec = dict(zip(built.keys(), ex.map(decs, built.keys())))
        cfsc = dict(zip(built.keys(), ex.map(score, built.keys())))

    label = {"B_BETTER": "improved", "EQUIVALENT": "plateau", "A_BETTER": "DEGRADED"}
    cf_dist = {f"{a}->{b}": collections.Counter() for a, b in STEPS}
    rows = []
    for pid in built:
        s = cfsc[pid]
        for stp, v in s.items():
            cf_dist[stp][label[v]] += 1
        seq = [dec[pid].get(r) for r in ("R0", "R1", "R2", "R3") if r in dec[pid]]
        flips = sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1])
        final = seq[-1] if seq else None
        stab = next((i for i in range(len(seq)) if all(x == final for x in seq[i:])), None) if seq else None
        conv = built[pid]["conv"]
        conv_round = next((c["round"] for c in conv if c["material_remaining"] is False), None)
        rows.append({"id": pid, "cf_steps": {stp: label[v] for stp, v in s.items()},
                     "decision_seq": seq, "flips": flips, "stabilized_round": stab,
                     "converged_round": conv_round,
                     "decision_changing_by_round": [c["n_decision_changing"] for c in conv],
                     "n_obj_by_round": [c["n_obj"] for c in conv],
                     "accept_by_round": [c["accept"] for c in conv]})

    base = json.loads(BASELINE.read_text())
    base_stable = sum(1 for r in base["rows"] if r["stabilized_round"] is not None and r["stabilized_round"] <= 1)
    new_stable = sum(1 for r in rows if r["stabilized_round"] is not None and r["stabilized_round"] <= 1)
    summary = {"EXPLORATORY": True, "k": k, "n": len(rows),
               "cf_step_distribution": {stp: dict(c) for stp, c in cf_dist.items()},
               "decision_stable_by_R1": {"baseline_lazy": f"{base_stable}/{base['n']}", "step2_convergence": f"{new_stable}/{len(rows)}"},
               "rows": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== STEP 2: convergence-pressured prompts ===")
    print(f"  DECISION STABLE BY R1:  baseline(lazy) {base_stable}/{base['n']}   ->   step2 {new_stable}/{len(rows)}")
    convs = [r["converged_round"] for r in rows if r["converged_round"]]
    print(f"  challenger DECLARED convergence: {len(convs)}/{len(rows)}"
          + (f" (rounds {dict(collections.Counter(convs))})" if convs else "  (baseline was 0/12)"))
    print(f"  CF step distribution (improved/plateau/DEGRADED):")
    for a, b in STEPS:
        c = cf_dist[f"{a}->{b}"]
        print(f"    {a}->{b:3s}: {c.get('improved',0):2d}/{c.get('plateau',0):2d}/{c.get('DEGRADED',0):2d}")
    print(f"\n  {'id':22s} {'decisions':24s} flips conv decision-changing/round")
    for r in rows:
        print(f"  {r['id']:22s} {(' -> '.join(map(str,r['decision_seq']))):24s} {r['flips']:5d} "
              f"{str(r['converged_round']):4s} {r['decision_changing_by_round']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
