#!/usr/bin/env python3
"""Analyze the resolver-iteration runs -> results-aggregate.json + console tables.

Net DV = panel-confirmed flaws still REMAIN + new >=2-consensus flaws introduced.
R0 is the definitional anchor: net = full denominator (all flaws remain, 0 new).
"""
import json, pathlib, statistics as stats

PILOT = pathlib.Path(__file__).resolve().parents[1]
V63 = PILOT.parent / "catch-rate-v3-2026-06-28"
RUNS = PILOT / "runs"

PROBLEMS = [p["id"] for p in json.load(open(V63 / "problems.json"))]
_CONS = json.load(open(V63 / "consensus-flaws.json"))
DENOM = {pid: [f["flaw"] for f in fl if f.get("auditors", 0) >= 2] for pid, fl in _CONS.items()}


def load(uid):
    p = RUNS / f"{uid}.json"
    return json.loads(p.read_text()) if p.exists() else None


def score_for(output_id):
    return load(f"score__{output_id}")


_KEYS = ("R0", "R1prime", "R1.same", "R1.cross", "R2.same", "R2.cross",
         "R3.same", "R3.cross", "R3v2.same", "R3v2.cross")


def net_by_condition():
    """Return {condition_key: {pid: net}} over _KEYS (R3 / R3v2 are EXPLORATORY additions)."""
    out = {k: {} for k in _KEYS}
    for pid in PROBLEMS:
        out["R0"][pid] = len(DENOM[pid])           # definitional anchor
        s = score_for(f"R1prime__{pid}")
        if s:
            out["R1prime"][pid] = s["net_flaws_remaining"]
        for arm in ("same", "cross"):
            for cond in ("R1", "R2", "R3", "R3v2"):
                s = score_for(f"{cond}__{arm}__{pid}")
                if s:
                    out[f"{cond}.{arm}"][pid] = s["net_flaws_remaining"]
    return out


def terminal_states(cond="R2"):
    rows = []
    for pid in PROBLEMS:
        for arm in ("same", "cross"):
            u = load(f"{cond}__{arm}__{pid}")
            if u:
                sc = score_for(u["unit"])
                rows.append({"pid": pid, "arm": arm, "terminal": u["terminal_state"],
                             "rounds": u["rounds"],
                             "net": sc["net_flaws_remaining"] if sc else None})
    return rows


def r3_governance_trail(cond="R3"):
    """Extract the verifier-attested accept/reject log + a legibility audit (question 2).
    For R3v2, a 'committed' patch must pass BOTH the local gate AND the global new-flaw budget."""
    rows, n_admit, n_reject, n_blocked_recorded, n_budget_block = [], 0, 0, 0, 0
    for pid in PROBLEMS:
        for arm in ("same", "cross"):
            u = load(f"{cond}__{arm}__{pid}")
            if not u:
                continue
            for entry in u["round_log"]:
                for att in entry.get("patch_attempts", []):
                    g = att["gate"]
                    over_budget = g.get("over_budget", False)
                    committed = g["admit"] and not over_budget
                    n_admit += 1 if committed else 0
                    n_reject += 0 if committed else 1
                    if over_budget:
                        n_budget_block += 1
                    if not committed and (g.get("blockers") or over_budget):
                        n_blocked_recorded += 1
                    rows.append({"pid": pid, "arm": arm, "round": entry["round"],
                                 "attempt": att["attempt"], "admit": committed,
                                 "over_budget": over_budget, "admit_votes": g["admit_votes"],
                                 "new_flaw_cost": g.get("new_flaw_cost"),
                                 "blockers": g.get("blockers", [])})
    legible = (n_reject == 0) or (n_blocked_recorded == n_reject)
    return {"condition": cond, "events": rows, "n_admit": n_admit, "n_reject": n_reject,
            "n_budget_blocked": n_budget_block,
            "rejects_with_recorded_blocker": n_blocked_recorded,
            "every_reject_has_blocker": legible}


def mean(d):
    vals = list(d.values())
    return round(stats.mean(vals), 3) if vals else None


def paired_diff(a, b):
    """mean(a-b) over shared pids, plus sign counts (a<b favors a)."""
    pids = [p for p in PROBLEMS if p in a and p in b]
    diffs = [a[p] - b[p] for p in pids]
    if not diffs:
        return None
    a_better = sum(1 for d in diffs if d < 0)
    b_better = sum(1 for d in diffs if d > 0)
    ties = sum(1 for d in diffs if d == 0)
    return {"n": len(diffs), "mean_diff": round(stats.mean(diffs), 3),
            "per_problem": {p: a[p] - b[p] for p in pids},
            "first_fewer": a_better, "second_fewer": b_better, "ties": ties}


def _state_means(ts):
    by_state = {}
    for r in ts:
        by_state.setdefault(r["terminal"], []).append(r["net"])
    return {st: {"n": len(v), "mean_net": round(stats.mean(v), 3)} for st, v in by_state.items() if v and None not in v}


def main():
    nbc = net_by_condition()
    means = {k: mean(v) for k, v in nbc.items()}
    ts3 = terminal_states("R3")
    ts3v2 = terminal_states("R3v2")

    # The headline recalibration question: did v2's budget+dynamic-cap beat v1, and the locked floors?
    contrasts = {}
    for arm in ("same", "cross"):
        contrasts[f"R3v2_vs_R3.{arm}"] = paired_diff(nbc[f"R3v2.{arm}"], nbc[f"R3.{arm}"])
        contrasts[f"R3v2_vs_R1.{arm}"] = paired_diff(nbc[f"R3v2.{arm}"], nbc[f"R1.{arm}"])
        contrasts[f"R3v2_vs_R1prime.{arm}"] = paired_diff(nbc[f"R3v2.{arm}"], nbc["R1prime"])
        contrasts[f"R3v2_vs_R0.{arm}"] = paired_diff(nbc[f"R3v2.{arm}"], nbc["R0"])

    gaming_v1 = _state_means(ts3)
    gaming_v2 = _state_means(ts3v2)
    gov_v1 = r3_governance_trail("R3")
    gov_v2 = r3_governance_trail("R3v2")

    # warehouse-siting regression watch: did v2 fix the v1 4->5 case?
    ws = {arm: {"R0": nbc["R0"].get("P-warehouse-siting"),
                "R3": nbc[f"R3.{arm}"].get("P-warehouse-siting"),
                "R3v2": nbc[f"R3v2.{arm}"].get("P-warehouse-siting")} for arm in ("same", "cross")}

    agg = {"EXPLORATORY": True, "note": "R3 / R3v2 exploratory; firewalled from Paper 1. v2 = severity-relative bar + global new-flaw budget(<=3) + dynamic round cap.",
           "means_net_flaws_remaining": means, "per_problem": nbc,
           "r3v2_contrasts": contrasts,
           "r3_terminal_states": ts3, "r3v2_terminal_states": ts3v2,
           "r3_net_by_terminal_state": gaming_v1, "r3v2_net_by_terminal_state": gaming_v2,
           "r3_governance": gov_v1, "r3v2_governance": gov_v2,
           "warehouse_siting_regression_watch": ws,
           "denominator_total": sum(len(v) for v in DENOM.values())}
    (PILOT / "analysis").mkdir(exist_ok=True)
    (PILOT / "analysis" / "results-aggregate-r3v2.json").write_text(json.dumps(agg, indent=2))
    (PILOT / "analysis" / "r3v2-governance-trail.json").write_text(json.dumps(gov_v2, indent=2))

    # console
    print("\n=== MEAN NET FLAWS REMAINING (lower better) — v1 vs v2 in context ===")
    for k in _KEYS:
        print(f"  {k:12s}: {means[k]}   (n={len(nbc[k])})")
    print("\n=== R3v2 CONTRASTS (mean paired diff; negative favors R3v2) ===")
    for k, v in contrasts.items():
        if v:
            print(f"  {k:22s}: mean_diff={v['mean_diff']:+.3f}  v2_fewer={v['first_fewer']} other_fewer={v['second_fewer']} ties={v['ties']} (n={v['n']})")
    print("\n=== WAREHOUSE-SITING REGRESSION WATCH (v1 4->5; did v2 fix it?) ===")
    for arm, d in ws.items():
        print(f"  {arm:5s}: R0(denom)={d['R0']}  R3v1={d['R3']}  R3v2={d['R3v2']}")
    print("\n=== TERMINAL STATES: v1 vs v2 ===")
    print(f"  v1: " + ", ".join(f"{st}={v['n']}(net {v['mean_net']})" for st, v in gaming_v1.items()))
    print(f"  v2: " + ", ".join(f"{st}={v['n']}(net {v['mean_net']})" for st, v in gaming_v2.items()))
    print("\n=== R3v2 TERMINAL DETAIL (rounds show if dynamic cap let it run longer) ===")
    for r in ts3v2:
        print(f"  {r['pid']:24s} {r['arm']:5s} {r['terminal']:9s} rounds={r['rounds']} net={r['net']}")
    print("\n=== GOVERNANCE: v1 vs v2 ===")
    print(f"  v1: admitted {gov_v1['n_admit']}  rejected {gov_v1['n_reject']}  legible={gov_v1['every_reject_has_blocker']}")
    print(f"  v2: admitted {gov_v2['n_admit']}  rejected {gov_v2['n_reject']}  budget-blocked {gov_v2['n_budget_blocked']}  legible={gov_v2['every_reject_has_blocker']}")
    print("\nwrote analysis/results-aggregate-r3v2.json + analysis/r3v2-governance-trail.json")


if __name__ == "__main__":
    main()
