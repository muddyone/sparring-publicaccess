#!/usr/bin/env python3
"""Per-round net-flaw trajectory for the v1 (R3) ceremonies — EXPLORATORY analysis, no new run.

Answers "were we hitting the cap before maximizing benefit?" using data we already have: every
committed per-round output is in each ceremony's round_log. We score each with the SAME DV scorer
(score_output) used for the final outputs, uniformly across rounds, and read the trajectory shape.

A ceremony "plateaued before the cap" if its net reached its final value at a round < its last
round (more rounds bought nothing). It was "truncated by the cap" if net was still falling at the
last round (the cap stopped productive improvement — the claim under test).

Usage: python3 trajectory.py        # scores (resumable) + prints + writes analysis/r3-trajectory.json
"""
import json, pathlib, concurrent.futures as cf
import run_study as R

PILOT = R.PILOT
PIDS = R.PIDS


def committed_per_round(u):
    """[(round_index, committed_text)]; round 0 = R0 baseline, then each round's admitted candidate."""
    out = [(0, R.R0[u["pid"]])]
    cur = R.R0[u["pid"]]
    for e in u["round_log"]:
        admitted = None
        for a in e.get("patch_attempts", []):
            if a["gate"]["admit"]:
                admitted = a["candidate"]
        if admitted is not None:
            cur = admitted
            out.append((e["round"], cur))
    return out


def main():
    # 1) score every intermediate committed output (resumable; round 0 is definitional = denom)
    jobs = []
    for pid in PIDS:
        for arm in ("same", "cross"):
            u = R.load(f"R3__{arm}__{pid}")
            if not u:
                continue
            for (ri, text) in committed_per_round(u):
                if ri == 0:
                    continue
                jobs.append((f"traj__R3__{arm}__{pid}__r{ri}", pid, text))
    print(f"[traj] scoring {len(jobs)} intermediate outputs (resumable)...", flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(R.score_output, oid, pid, text): oid for (oid, pid, text) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:  # noqa: BLE001
                print(f"[traj] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)
            done += 1
            if done % 10 == 0:
                print(f"[traj] {done}/{len(jobs)}", flush=True)

    # 2) build trajectories + classify
    traj, summary = {}, []
    for pid in PIDS:
        for arm in ("same", "cross"):
            u = R.load(f"R3__{arm}__{pid}")
            if not u:
                continue
            series = []
            for (ri, _t) in committed_per_round(u):
                if ri == 0:
                    net = len(R.DENOM[pid])
                else:
                    s = R.load(f"score__traj__R3__{arm}__{pid}__r{ri}")
                    net = s["net_flaws_remaining"] if s else None
                series.append({"round": ri, "net": net})
            key = f"{pid}.{arm}"
            traj[key] = {"terminal": u["terminal_state"], "rounds": u["rounds"], "series": series}
            nets = [p["net"] for p in series if p["net"] is not None]
            final_net = nets[-1] if nets else None
            last_round = series[-1]["round"]
            # plateau round = first round whose net equals the final net (and stays there)
            plateau_round = last_round
            for p in series:
                if p["net"] == final_net:
                    plateau_round = p["round"]
                    break
            still_falling = len(nets) >= 2 and nets[-1] < nets[-2]   # net dropped on the very last step
            rounds_wasted = last_round - plateau_round               # rounds after benefit maxed
            summary.append({"key": key, "terminal": u["terminal_state"], "last_round": last_round,
                            "final_net": final_net, "plateau_round": plateau_round,
                            "rounds_wasted_after_plateau": rounds_wasted,
                            "still_falling_at_end": still_falling})

    (PILOT / "analysis").mkdir(exist_ok=True)
    (PILOT / "analysis" / "r3-trajectory.json").write_text(json.dumps({"trajectories": traj, "summary": summary}, indent=2))

    # 3) print
    print("\n=== v1 NET-FLAW TRAJECTORY (per committed round; lower better) ===")
    for key in sorted(traj):
        t = traj[key]
        path = "  ".join(f"r{p['round']}:{p['net']}" for p in t["series"])
        print(f"  {key:30s} [{t['terminal']:9s}]  {path}")
    print("\n=== CAP-TRUNCATION VERDICT (did more rounds keep paying off?) ===")
    capped = [s for s in summary if s["terminal"] == "CAPPED"]
    still = [s for s in summary if s["still_falling_at_end"]]
    print(f"  CAPPED ceremonies: {len(capped)}")
    for s in capped:
        verdict = "STILL FALLING at cap" if s["still_falling_at_end"] else f"plateaued at r{s['plateau_round']} ({s['rounds_wasted_after_plateau']} rounds wasted)"
        print(f"    {s['key']:30s} final_net={s['final_net']}  {verdict}")
    print(f"\n  Across ALL ceremonies, still-falling-on-the-last-step: {len(still)}/{len(summary)}")
    for s in still:
        print(f"    {s['key']:30s} [{s['terminal']}] last_round={s['last_round']} final_net={s['final_net']}")
    print("\nwrote analysis/r3-trajectory.json")


if __name__ == "__main__":
    main()
