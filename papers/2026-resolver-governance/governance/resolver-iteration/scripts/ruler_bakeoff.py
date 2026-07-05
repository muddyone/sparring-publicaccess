#!/usr/bin/env python3
"""Ruler bake-off against the positive-control set (EXPLORATORY).

Four candidate correctness rulers, scored on whether they recover CONSTRUCTED ground truth
(analysis/positive-control-set.json: 8 planted_regression=A_BETTER, 8 planted_improvement=B_BETTER,
8 identical + 8 cosmetic = EQUIVALENT). Pass bar: CATCH the planted regressions AND call the no-ops
EQUIVALENT (the bias test is built into the instrument).

Rulers (A=text_a=base R0, B=text_b=variant):
  1. flaw_count          — score_output both sides vs the fixed denominator; compare mean net (tie band).
                           The noisy incumbent; replicated + averaged to give it a fair shot.
  2. pairwise_raw        — the quiet-but-pro-revision-biased pairwise judge (expected to fail no-ops).
  3. pairwise_cf         — counter-framed: anti-bias + length-normalization instruction.
  4. challenge_enum      — Bart's idea, reshaped: enumerate material flaws + severity in EACH side
                           INDEPENDENTLY (blind, symmetric — no "which is the revision" gestalt), then a
                           transparent severity-weighted rule with an EQUIVALENT band decides (design (c)).

Pairwise rulers are order-randomized per (pair, replicate). challenge_enum needs no order randomization
(each side audited alone — that symmetry is the anti-bias property). Resumable + parallel.

Usage:
  python3 ruler_bakeoff.py                     # all rulers, k=5
  python3 ruler_bakeoff.py --k 5 --rulers flaw_count,pairwise_raw,pairwise_cf,challenge_enum
  python3 ruler_bakeoff.py --score-only
Env: ANTHROPIC_API_KEY.
"""
import json, hashlib, statistics, argparse, collections
import concurrent.futures as cf
import run_study as R
import pairwise_dv_probe as P
import lib_llm as L

K_DEFAULT = 5
FLAWCOUNT_TIE = 0.5     # |mean_net_a - mean_net_b| below this -> EQUIVALENT
ENUM_BAND = 1.5         # |mean_sev_a - mean_sev_b| below this -> EQUIVALENT  (design (c))
ALL_RULERS = ["flaw_count", "pairwise_raw", "pairwise_cf", "challenge_enum"]
MANIFEST = R.PILOT / "analysis" / "positive-control-set.json"
OUT_JSON = R.PILOT / "analysis" / "ruler-bakeoff.json"

# counter-framed pairwise system prompt (ruler 3) = base + explicit anti-bias
CF_SYS = P.PAIR_JUDGE_SYS + (
    " CRITICAL anti-bias instruction: do NOT assume the longer, more detailed, more polished, or more "
    "recently-revised version is better — length and polish are NOT quality, and a more thorough-looking "
    "version may have INTRODUCED a material flaw. If two versions differ only in wording with no "
    "substantive change, they are EQUIVALENT. Judge strictly on material would-ship flaws, nothing else."
)

# challenge-enumerator (ruler 4): audit ONE rec alone, list material flaws with severity
ENUM_SYS = (
    "You are an independent auditor. List the MATERIAL would-ship flaws in the recommendation below — "
    "errors that would change the decision or ship a real defect, not style, not length, not polish. For "
    "each flaw give a severity: 1=low, 2=medium, 3=high (decision-changing). If there are no material "
    "flaws, return an empty list — do not manufacture flaws. You are blind to how the recommendation was produced."
)
ENUM_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"flaws\": [{{\"text\": str, \"severity\": 1|2|3}}]}}"
)


def _flip(pair_id, tag, j):
    return int(hashlib.sha1(f"{pair_id}|{tag}|{j}".encode()).hexdigest(), 16) % 2 == 0


def map_pairwise(raw, ctrlA_in_slotA):
    if raw not in ("A_BETTER", "B_BETTER"):
        return "EQUIVALENT"
    winner_slot_A = (raw == "A_BETTER")
    ctrl_winner_A = (winner_slot_A == ctrlA_in_slotA)
    return "A_BETTER" if ctrl_winner_A else "B_BETTER"


# ---- leaf jobs (idempotent, cached) ----
def leaf_flawscore(pair, side, j):
    text = pair["text_a"] if side == "A" else pair["text_b"]
    R.score_output(f"ctrlsc__{pair['pair_id']}__{side}__rep{j}", pair["pid"], text)


def leaf_pairwise(pair, j, mode):
    uid = f"bake__{mode}__{pair['pair_id']}__rep{j}"
    if R.load(uid):
        return
    sysp = P.PAIR_JUDGE_SYS if mode == "raw" else CF_SYS
    a_in_A = _flip(pair["pair_id"], mode, j)
    slotA = pair["text_a"] if a_in_A else pair["text_b"]
    slotB = pair["text_b"] if a_in_A else pair["text_a"]
    out = L.claude_json(R.CLAUDE, sysp, P.PAIR_JUDGE_USER.format(
        problem=R.PROBLEMS[pair["pid"]]["problem"], a=slotA, b=slotB), max_tokens=1200)
    raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
    R.save(uid, {"pair_id": pair["pair_id"], "mode": mode, "rep": j, "ctrlA_in_slotA": a_in_A,
                 "raw_verdict": raw, "mapped": map_pairwise(raw, a_in_A)})


def leaf_enum(pair, side, j):
    uid = f"bake__enum{side}__{pair['pair_id']}__rep{j}"
    if R.load(uid):
        return
    text = pair["text_a"] if side == "A" else pair["text_b"]
    out = L.claude_json(R.CLAUDE, ENUM_SYS, ENUM_USER.format(
        problem=R.PROBLEMS[pair["pid"]]["problem"], rec=text), max_tokens=2500)
    flaws = out.get("flaws", []) if isinstance(out, dict) else []
    sev = sum(int(f.get("severity", 2)) for f in flaws if isinstance(f, dict))
    R.save(uid, {"pair_id": pair["pair_id"], "side": side, "rep": j,
                 "n_flaws": len(flaws), "severity_sum": sev})


def build_jobs(pairs, k, rulers):
    jobs = []
    for pair in pairs:
        for j in range(1, k + 1):
            if "flaw_count" in rulers:
                jobs.append((leaf_flawscore, (pair, "A", j)))
                jobs.append((leaf_flawscore, (pair, "B", j)))
            if "pairwise_raw" in rulers:
                jobs.append((leaf_pairwise, (pair, j, "raw")))
            if "pairwise_cf" in rulers:
                jobs.append((leaf_pairwise, (pair, j, "cf")))
            if "challenge_enum" in rulers:
                jobs.append((leaf_enum, (pair, "A", j)))
                jobs.append((leaf_enum, (pair, "B", j)))
    return jobs


# ---- per-ruler verdict assembly ----
def verdict_flawcount(pair, k):
    na, nb = [], []
    for j in range(1, k + 1):
        sa = R.load(f"score__ctrlsc__{pair['pair_id']}__A__rep{j}")
        sb = R.load(f"score__ctrlsc__{pair['pair_id']}__B__rep{j}")
        if not sa or not sb:
            return None
        na.append(sa["net_flaws_remaining"]); nb.append(sb["net_flaws_remaining"])
    diff = statistics.mean(nb) - statistics.mean(na)   # >0 => B has more flaws => A better
    if diff > FLAWCOUNT_TIE:
        return "A_BETTER"
    if diff < -FLAWCOUNT_TIE:
        return "B_BETTER"
    return "EQUIVALENT"


def verdict_pairwise(pair, k, mode):
    vs = []
    for j in range(1, k + 1):
        rec = R.load(f"bake__{mode}__{pair['pair_id']}__rep{j}")
        if not rec:
            return None
        vs.append(rec["mapped"])
    return collections.Counter(vs).most_common(1)[0][0]


def verdict_enum(pair, k):
    sa, sb = [], []
    for j in range(1, k + 1):
        ea = R.load(f"bake__enumA__{pair['pair_id']}__rep{j}")
        eb = R.load(f"bake__enumB__{pair['pair_id']}__rep{j}")
        if not ea or not eb:
            return None
        sa.append(ea["severity_sum"]); sb.append(eb["severity_sum"])
    diff = statistics.mean(sb) - statistics.mean(sa)   # >0 => B more flaw-weight => A better
    if diff > ENUM_BAND:
        return "A_BETTER"
    if diff < -ENUM_BAND:
        return "B_BETTER"
    return "EQUIVALENT"


VERDICT_FNS = {
    "flaw_count": lambda pair, k: verdict_flawcount(pair, k),
    "pairwise_raw": lambda pair, k: verdict_pairwise(pair, k, "raw"),
    "pairwise_cf": lambda pair, k: verdict_pairwise(pair, k, "cf"),
    "challenge_enum": lambda pair, k: verdict_enum(pair, k),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--rulers", default=",".join(ALL_RULERS))
    ap.add_argument("--score-only", action="store_true")
    args = ap.parse_args()
    k = args.k
    rulers = [r.strip() for r in args.rulers.split(",") if r.strip()]

    manifest = json.loads(MANIFEST.read_text())
    pairs = manifest["pairs"]
    print(f"[bake] {len(pairs)} control pairs; rulers={rulers}; k={k}", flush=True)

    jobs = build_jobs(pairs, k, rulers)
    print(f"[bake] {len(jobs)} leaf calls (resumable; cached skipped)", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(fn, *a): (fn.__name__, a[0]["pair_id"]) for (fn, a) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[bake] ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
            done += 1
            if done % 50 == 0:
                print(f"[bake] {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[bake] {errs} errors -- re-run to retry (resumable).", flush=True)
    if args.score_only:
        print("[bake] --score-only done.")
        return

    # assemble verdicts + score vs ground truth
    TYPES = ["planted_regression", "planted_improvement", "identical", "cosmetic"]
    results = {r: {"per_pair": [], "by_type": collections.defaultdict(lambda: {"n": 0, "correct": 0}),
                   "noop_leans": collections.Counter()} for r in rulers}
    incomplete = collections.Counter()
    for pair in pairs:
        gt = pair["ground_truth"]
        for r in rulers:
            v = VERDICT_FNS[r](pair, k)
            if v is None:
                incomplete[r] += 1
                continue
            correct = (v == gt)
            results[r]["per_pair"].append({"pair_id": pair["pair_id"], "type": pair["type"],
                                           "gt": gt, "verdict": v, "correct": correct})
            bt = results[r]["by_type"][pair["type"]]
            bt["n"] += 1; bt["correct"] += int(correct)
            if pair["type"] in ("identical", "cosmetic"):
                results[r]["noop_leans"][v] += 1

    summary = {"EXPLORATORY": True, "k": k, "rulers": rulers, "n_pairs": len(pairs),
               "flawcount_tie": FLAWCOUNT_TIE, "enum_band": ENUM_BAND, "rulers_detail": {}}
    print("\n=== RULER BAKE-OFF vs POSITIVE CONTROL ===")
    hdr = f"  {'ruler':16s} {'overall':>8s} {'reg-recall':>11s} {'noop-spec':>10s} {'impr-recall':>12s}"
    print(hdr); print("  " + "-" * (len(hdr) - 2))
    for r in rulers:
        pp = results[r]["per_pair"]
        n = len(pp)
        overall = sum(p["correct"] for p in pp) / n if n else None
        bt = results[r]["by_type"]
        def rate(t):
            d = bt.get(t); return (d["correct"] / d["n"]) if d and d["n"] else None
        reg = rate("planted_regression")
        impr = rate("planted_improvement")
        noops = (bt.get("identical", {}).get("n", 0) and 1)  # presence
        noop_correct = (bt.get("identical", {"correct": 0})["correct"] + bt.get("cosmetic", {"correct": 0})["correct"])
        noop_n = (bt.get("identical", {"n": 0})["n"] + bt.get("cosmetic", {"n": 0})["n"])
        noop_spec = noop_correct / noop_n if noop_n else None
        leans = dict(results[r]["noop_leans"])
        summary["rulers_detail"][r] = {
            "overall_accuracy": round(overall, 3) if overall is not None else None,
            "regression_recall": round(reg, 3) if reg is not None else None,
            "noop_specificity": round(noop_spec, 3) if noop_spec is not None else None,
            "improvement_recall": round(impr, 3) if impr is not None else None,
            "noop_verdict_leans": leans,
            "incomplete": incomplete[r],
            "per_type": {t: dict(bt.get(t, {"n": 0, "correct": 0})) for t in TYPES},
            "per_pair": pp,
        }
        def fmt(x): return f"{x:.2f}" if isinstance(x, float) else "  - "
        print(f"  {r:16s} {fmt(overall):>8s} {fmt(reg):>11s} {fmt(noop_spec):>10s} {fmt(impr):>12s}"
              + (f"   incomplete={incomplete[r]}" if incomplete[r] else ""))
    print("\n  PASS BAR: high regression-recall AND high no-op-specificity.")
    print("  no-op verdict leans (a B-lean on no-ops = verbosity/revision bias, since B is the variant):")
    for r in rulers:
        print(f"    {r:16s}: {dict(results[r]['noop_leans'])}")
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    OUT_JSON.write_text(json.dumps(summary, indent=2))
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
