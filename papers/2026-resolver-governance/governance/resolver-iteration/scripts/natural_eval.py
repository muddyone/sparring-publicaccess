#!/usr/bin/env python3
"""Natural-corpus evaluation — the generalization test past the hothouse (EXPLORATORY).

Applies the validated Phase-4 architecture (pairwise_raw ruler -> coherence gate -> repair loop) to the
12 NATURAL (R0, R1) pairs in natural-corpus.json (no planted flaws), and scores it against an
INDEPENDENT proxy-gold panel (Bart's chosen ground-truth path).

Two questions:
  1. BEHAVIOR — on natural revisions, what does the ruler say (R1 better / worse / equivalent), how often
     does the coherence gate FIRE (the key hypothesis: it may be RARE, because producers usually IMPROVE
     on challenge -> the gate is tail insurance, not a frequent save), and does the loop repair/flip?
  2. AGREEMENT — does the ruler's verdict match an independent panel that uses a DIFFERENT method
     (blind flaw ENUMERATION + count, not holistic pairwise) across TWO vendors (Claude + GPT-5.2)?
     Circularity caveat (Bart flagged it): the Claude auditor shares substrate with the ruler, so the
     GPT auditor's agreement is the least-circular signal — weight it accordingly.

Reuses the loop's own primitives (pairwise_verdict / gate_verdict / rewrite) so this is the SAME
mechanism, not a re-implementation. Panel reuses run_study's independent-auditor prompt. Resumable.

Usage: python3 natural_eval.py [--k 3] [--cap 2]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, statistics, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
from resolver_loop import pairwise_verdict, gate_verdict, rewrite

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "natural-eval.json"
PANEL_BAND = 0.5   # |mean flaw count diff| below this -> EQUIVALENT


# ---------- architecture behavior on a natural pair ----------
def run_arch(pair, k, cap):
    pid, problem, A, B = pair["id"], pair["problem"], pair["R0"], pair["R1"]
    tag = f"nat__{pid}"
    traj = []
    v0 = pairwise_verdict(problem, A, B, f"{tag}__it0", k)
    traj.append({"stage": "pairwise", "iter": 0, "verdict": v0})
    base = {"id": pid, "domain": pair["domain"], "source": pair["source"], "ruler_initial": v0}
    if v0 != "B_BETTER":
        # ruler does not accept the revision as better: A_BETTER = natural regression; EQUIVALENT = no-op
        return {**base, "gate_fired": False, "rewrites": 0,
                "outcome": ("KEEP_R0_regression" if v0 == "A_BETTER" else "KEEP_R0_equivalent"),
                "trajectory": traj}
    cur, rewrites = B, 0
    for it in range(cap + 1):
        flagged, contra = gate_verdict(cur, f"{tag}__it{it}", k)
        traj.append({"stage": "gate", "iter": it, "flagged": flagged, "contradiction": contra[:180]})
        if not flagged:
            return {**base, "gate_fired": (rewrites > 0), "rewrites": rewrites,
                    "outcome": "ACCEPT_R1", "trajectory": traj}
        if it == cap:
            return {**base, "gate_fired": True, "rewrites": rewrites,
                    "outcome": "ACCEPT_STILL_FLAGGED", "trajectory": traj}
        cur = rewrite(problem, cur, contra, f"{tag}__it{it}")
        rewrites += 1
        vr = pairwise_verdict(problem, A, cur, f"{tag}__it{it+1}", k)
        traj.append({"stage": "pairwise", "iter": it + 1, "verdict": vr})
        if vr != "B_BETTER":
            return {**base, "gate_fired": True, "rewrites": rewrites,
                    "outcome": "REJECT_after_repair", "decision_flipped": True, "trajectory": traj}
    return {**base, "gate_fired": True, "rewrites": rewrites, "outcome": "ACCEPT_R1", "trajectory": traj}


# ---------- independent panel: blind flaw enumeration + count, per side, per vendor ----------
def audit_leaf(pair, side, vendor, j):
    uid = f"natpanel__{vendor}__{side}__{pair['id']}__rep{j}"
    if R.load(uid):
        return
    text = pair["R0"] if side == "A" else pair["R1"]
    u = R.AUDIT_USER.format(problem=pair["problem"], rec=text)
    if vendor == "claude":
        out = L.claude_json(R.CLAUDE, R.AUDIT_SYS, u, max_tokens=2000)
    else:
        out = L.gpt_json(R.GPT, R.AUDIT_SYS, u, max_completion_tokens=8000)
    flaws = out.get("flaws", []) if isinstance(out, dict) else []
    R.save(uid, {"n": len(flaws), "flaws": [str(f)[:160] for f in flaws[:8]]})


def panel_verdict(pair, vendor, k):
    na, nb = [], []
    for j in range(1, k + 1):
        a = R.load(f"natpanel__{vendor}__A__{pair['id']}__rep{j}")
        b = R.load(f"natpanel__{vendor}__B__{pair['id']}__rep{j}")
        if not a or not b:
            return None
        na.append(a["n"]); nb.append(b["n"])
    diff = statistics.mean(nb) - statistics.mean(na)   # >0 => B more flaws => A better
    if diff > PANEL_BAND:
        return "A_BETTER"
    if diff < -PANEL_BAND:
        return "B_BETTER"
    return "EQUIVALENT"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--cap", type=int, default=2)
    args = ap.parse_args()
    k, cap = args.k, args.cap

    pairs = json.loads(CORPUS.read_text())["problems"]
    print(f"[nat] {len(pairs)} natural pairs; k={k} cap={cap}", flush=True)

    # 1. panel audits (independent leaves, both vendors, both sides)
    pjobs = [(audit_leaf, (p, side, v, j)) for p in pairs for side in ("A", "B")
             for v in ("claude", "gpt") for j in range(1, k + 1)]
    print(f"[nat] panel: {len(pjobs)} audit leaves", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(fn, *a): a[0]["id"] for (fn, a) in pjobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[nat] panel ERROR {futs[f]}: {repr(e)[:120]}", flush=True)
            done += 1
            if done % 20 == 0:
                print(f"[nat] panel {done}/{len(pjobs)}", flush=True)
    if errs:
        print(f"[nat] {errs} panel errors -- re-run to retry.", flush=True)

    # 2. architecture loop (per-pair sequential; pairs concurrent)
    arch = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_arch, p, k, cap): p["id"] for p in pairs}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); arch[r["id"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[nat] arch ERROR {futs[f]}: {repr(e)[:140]}", flush=True)

    # 3. assemble: ruler vs panel per pair
    rows = []
    for p in pairs:
        a = arch.get(p["id"], {})
        pc = panel_verdict(p, "claude", k)
        pg = panel_verdict(p, "gpt", k)
        rows.append({"id": p["id"], "domain": p["domain"], "source": p["source"],
                     "ruler": a.get("ruler_initial"), "panel_claude": pc, "panel_gpt": pg,
                     "gate_fired": a.get("gate_fired"), "rewrites": a.get("rewrites"),
                     "outcome": a.get("outcome"),
                     "agree_claude": (a.get("ruler_initial") == pc),
                     "agree_gpt": (a.get("ruler_initial") == pg)})

    ruler_dist = collections.Counter(r["ruler"] for r in rows)
    n = len(rows)
    gate_fires = sum(1 for r in rows if r["gate_fired"])
    agree_c = sum(1 for r in rows if r["agree_claude"])
    agree_g = sum(1 for r in rows if r["agree_gpt"])
    summary = {"EXPLORATORY": True, "n": n, "k": k, "cap": cap,
               "ruler_verdict_distribution": dict(ruler_dist),
               "gate_fire_rate": f"{gate_fires}/{n}",
               "ruler_vs_panel_agreement": {"claude(circular)": f"{agree_c}/{n}", "gpt(independent)": f"{agree_g}/{n}"},
               "rows": rows, "arch_detail": arch}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== NATURAL-CORPUS EVALUATION ===")
    print(f"  ruler (R1 vs R0) distribution: {dict(ruler_dist)}")
    print(f"  GATE FIRE RATE (the hypothesis): {gate_fires}/{n}"
          + ("   <- fires rarely => tail-insurance, as predicted" if gate_fires <= 2 else "   <- fires often, unexpected"))
    print(f"  ruler vs panel agreement: claude(circular) {agree_c}/{n}   GPT(independent) {agree_g}/{n}")
    print(f"\n  {'id':22s} {'ruler':10s} {'pan-cl':10s} {'pan-gpt':10s} {'gate':5s} {'outcome':22s}")
    for r in rows:
        g = "FIRE" if r["gate_fired"] else "-"
        print(f"  {r['id']:22s} {str(r['ruler']):10s} {str(r['panel_claude']):10s} "
              f"{str(r['panel_gpt']):10s} {g:5s} {str(r['outcome']):22s}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
