#!/usr/bin/env python3
"""Live rewrite loop — option (a): the load-bearing test of Bart's architecture (EXPLORATORY).

Architecture under test:
  pairwise_raw (ruler) decides if the revision B beats the original A.
    * not B_BETTER  -> revision REJECTED by the ruler (gate never consulted).
    * B_BETTER      -> provisional ACCEPT -> consult the textual coherence gate on B.
        * gate passes -> ACCEPT B (final).
        * gate flags  -> Resolver rewrites B given the quoted contradiction -> B';
                         RE-RUN pairwise(A, B')  [the amendment: the gate can trigger a re-decision]
                         loop until the gate passes or the cap.

Why this is the real test: everything before validated the *detector* and the *veto logic* on static
text. This runs the closed loop and answers the two unknowns:
  1. CONVERGENCE — handed the contradiction quote, does the Resolver remove it in bounded iterations,
     and does the loop accept good revisions in ZERO rewrites (no needless churn)?
  2. DECISION-FLIP — capex is the one case pairwise is FOOLED (B_BETTER) because the contradiction
     reads cleaner. After decontradiction, does pairwise flip to NOT-B_BETTER (correct REJECT), or does
     the rewrite merely launder clean prose onto a wrong decision (ACCEPT, a failure)?

Ground truth (positive-control set): planted_regression -> should end REJECT; planted_improvement ->
should end ACCEPT; no-ops -> pairwise EQUIVALENT (not "better"), never reach the gate.

k-vote on every pairwise/gate verdict (noise discipline). Resumable + parallel-free (the loop is
sequential per pair; pairs run concurrently). Claude-only.

Usage: python3 resolver_loop.py [--k 3] [--cap 3]
Env: ANTHROPIC_API_KEY.
"""
import json, hashlib, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import pairwise_dv_probe as P
from coherence_gate import COHERENCE_SYS, COHERENCE_USER

K_DEFAULT = 3
CAP_DEFAULT = 3
MANIFEST = R.PILOT / "analysis" / "positive-control-set.json"
OUT_JSON = R.PILOT / "analysis" / "resolver-loop.json"

RESOLVER_SYS = (
    "You are revising your own prior recommendation. An independent auditor flagged an INTERNAL "
    "CONTRADICTION in it (quoted below). Produce a corrected recommendation that removes the "
    "contradiction. Make the MINIMAL change needed to be internally consistent — keep your structure, "
    "format, and every claim that is not part of the contradiction; do not pad, re-explain, or add "
    "length. Resolve the contradiction by making the text consistent with the problem's facts, not by "
    "deleting the inconvenient half. Return ONLY the full corrected recommendation text, nothing else."
)
RESOLVER_USER = "PROBLEM:\n{problem}\n\nYOUR RECOMMENDATION:\n{rec}\n\nAUDITOR-FLAGGED CONTRADICTION:\n{contradiction}"


def _flip(tag, j):
    return int(hashlib.sha1(f"{tag}|{j}".encode()).hexdigest(), 16) % 2 == 0


def _map(raw, a_in_slotA):
    if raw not in ("A_BETTER", "B_BETTER"):
        return "EQUIVALENT"
    winner_A = (raw == "A_BETTER")
    return "A_BETTER" if (winner_A == a_in_slotA) else "B_BETTER"


def pairwise_verdict(problem, A, B, tag, k):
    """k-vote pairwise on (A=original, B=candidate); order-randomized. Returns A_BETTER/B_BETTER/EQUIVALENT."""
    votes = []
    for j in range(1, k + 1):
        uid = f"loop_pw__{tag}__rep{j}"
        rec = R.load(uid)
        if not rec:
            a_in_A = _flip(tag, j)
            slotA, slotB = (A, B) if a_in_A else (B, A)
            out = L.claude_json(R.CLAUDE, P.PAIR_JUDGE_SYS,
                                P.PAIR_JUDGE_USER.format(problem=problem, a=slotA, b=slotB), max_tokens=1200)
            raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
            rec = {"mapped": _map(raw, a_in_A)}
            R.save(uid, rec)
        votes.append(rec["mapped"])
    return collections.Counter(votes).most_common(1)[0][0]


def gate_verdict(text, tag, k):
    """k-vote textual coherence gate on one text. Returns (flagged, contradiction)."""
    votes, contras = [], []
    for j in range(1, k + 1):
        uid = f"loop_gate__{tag}__rep{j}"
        rec = R.load(uid)
        if not rec:
            out = L.claude_json(R.CLAUDE, COHERENCE_SYS, COHERENCE_USER.format(rec=text), max_tokens=1200)
            coherent = bool(out.get("coherent", True)) if isinstance(out, dict) else True
            contra = (out.get("contradiction", "") or "") if isinstance(out, dict) else ""
            rec = {"coherent": coherent, "contradiction": contra[:400]}
            R.save(uid, rec)
        votes.append(rec["coherent"])
        if not rec["coherent"] and rec["contradiction"]:
            contras.append(rec["contradiction"])
    flagged = sum(1 for v in votes if not v) >= (k // 2 + 1)
    return flagged, (contras[0] if contras else "")


def rewrite(problem, rec_text, contradiction, tag):
    uid = f"loop_rw__{tag}"
    cached = R.load(uid)
    if cached:
        return cached["text"]
    out = L.call_claude(R.CLAUDE, RESOLVER_SYS,
                        RESOLVER_USER.format(problem=problem, rec=rec_text, contradiction=contradiction),
                        max_tokens=3000)
    R.save(uid, {"text": out})
    return out


def run_pair(pair, k, cap):
    pid = pair["pid"]
    problem = R.PROBLEMS[pid]["problem"]
    A = pair["text_a"]
    B = pair["text_b"]
    base = pair["pair_id"]
    traj = []

    v0 = pairwise_verdict(problem, A, B, f"{base}__it0", k)
    traj.append({"stage": "pairwise", "iter": 0, "verdict": v0})
    if v0 != "B_BETTER":
        return {"pair_id": base, "type": pair["type"], "gt": pair["ground_truth"],
                "outcome": "REJECT", "rewrites": 0, "gate_consulted": False, "trajectory": traj}

    cur = B
    rewrites = 0
    for it in range(cap + 1):
        flagged, contra = gate_verdict(cur, f"{base}__it{it}", k)
        traj.append({"stage": "gate", "iter": it, "flagged": flagged, "contradiction": contra[:160]})
        if not flagged:
            return {"pair_id": base, "type": pair["type"], "gt": pair["ground_truth"],
                    "outcome": "ACCEPT", "rewrites": rewrites, "gate_consulted": True, "trajectory": traj}
        if it == cap:
            return {"pair_id": base, "type": pair["type"], "gt": pair["ground_truth"],
                    "outcome": "ACCEPT_STILL_FLAGGED", "rewrites": rewrites, "gate_consulted": True,
                    "trajectory": traj}
        cur = rewrite(problem, cur, contra, f"{base}__it{it}")
        rewrites += 1
        vr = pairwise_verdict(problem, A, cur, f"{base}__it{it+1}", k)
        traj.append({"stage": "pairwise", "iter": it + 1, "verdict": vr})
        if vr != "B_BETTER":
            return {"pair_id": base, "type": pair["type"], "gt": pair["ground_truth"],
                    "outcome": "REJECT", "rewrites": rewrites, "gate_consulted": True,
                    "decision_flipped": True, "trajectory": traj}
    return {"pair_id": base, "type": pair["type"], "gt": pair["ground_truth"],
            "outcome": "ACCEPT", "rewrites": rewrites, "gate_consulted": True, "trajectory": traj}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--cap", type=int, default=CAP_DEFAULT)
    args = ap.parse_args()
    k, cap = args.k, args.cap

    pairs = json.loads(MANIFEST.read_text())["pairs"]
    print(f"[loop] {len(pairs)} pairs; k={k}; rewrite cap={cap}", flush=True)
    results, errs = [], 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_pair, pair, k, cap): pair["pair_id"] for pair in pairs}
        for f in cf.as_completed(futs):
            try:
                results.append(f.result())
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[loop] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)
    if errs:
        print(f"[loop] {errs} errors -- re-run to retry (resumable).", flush=True)

    # correctness vs ground truth: regression->REJECT, improvement->ACCEPT, no-op->REJECT(not "better")
    def correct(r):
        if r["type"] == "planted_regression":
            return r["outcome"] in ("REJECT",)
        if r["type"] == "planted_improvement":
            return r["outcome"] in ("ACCEPT",)
        return r["outcome"] in ("REJECT",)   # no-ops: pairwise EQUIVALENT -> not accepted as better
    by = collections.defaultdict(lambda: {"n": 0, "correct": 0})
    for r in results:
        r["correct"] = correct(r)
        b = by[r["type"]]; b["n"] += 1; b["correct"] += int(r["correct"])

    summary = {"EXPLORATORY": True, "k": k, "cap": cap, "n_pairs": len(pairs),
               "by_type": {t: dict(v) for t, v in by.items()},
               "results": sorted(results, key=lambda r: (r["type"], r["pair_id"]))}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== RESOLVER LOOP (pairwise ruler + coherence-gate veto + rewrite) ===")
    for t in ["planted_regression", "planted_improvement", "identical", "cosmetic"]:
        v = by.get(t)
        if v:
            print(f"  {t:22s}: {v['correct']}/{v['n']} correct")
    # the hero case + any rewrite-triggered pairs
    print("\n  rewrite-triggered pairs (gate flagged a provisionally-accepted revision):")
    any_rw = False
    for r in summary["results"]:
        if r.get("gate_consulted") and r["rewrites"] > 0:
            any_rw = True
            flip = "  DECISION FLIPPED->REJECT" if r.get("decision_flipped") else ""
            print(f"    {r['pair_id']:42s} outcome={r['outcome']:18s} rewrites={r['rewrites']}{flip}")
    if not any_rw:
        print("    (none)")
    print("\n  no-churn check (improvements accepted with 0 rewrites):")
    imp = [r for r in summary["results"] if r["type"] == "planted_improvement"]
    print(f"    {sum(1 for r in imp if r['outcome']=='ACCEPT' and r['rewrites']==0)}/{len(imp)} improvements accepted in 0 rewrites")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
