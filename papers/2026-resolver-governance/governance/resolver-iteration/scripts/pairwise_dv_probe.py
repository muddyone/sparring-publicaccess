#!/usr/bin/env python3
"""Pairwise-preference DV probe (EXPLORATORY).

The de-noise probe showed the absolute net-flaw-count DV is noise-dominated at the +/-1 grain
because the regression label SUBTRACTS two noisy absolute scores (cand_net > champ_net). The fix the
finding points to: don't subtract — judge directly. This probe tests whether a BLIND PAIRWISE judgment
("which recommendation has fewer / less-severe material would-ship flaws — A or B, or equivalent?") is a
quieter, truer correctness ruler than the absolute DV.

Validation uses the stage0 de-noise run as the ANSWER KEY (analysis/stage0-denoise.json):
  - does pairwise reliably call the 2 STABLE regressions "champion better"?
  - does it call the 7 GHOSTS "equivalent"/split (NOT consistently champion-better)?
  - is its replicate flip behavior QUIETER than the absolute DV's on the same 61 pairs?
    (apples-to-apples: both binarized to the same question "is the candidate worse = champion better?",
     k=5, modal agreement = max(votes, k-votes)/k; higher = less noisy.)

Reuses stage0_denoise.gather_items() for the 61 (champion, candidate) pairs + run_study's LLM client.
Single judge, replicated k=5, order randomized per replicate (resumable). ~305 judge calls.
Note: asks ONLY for a verdict + short reason (no flaw list), so it avoids the truncation failure mode
that cost one stage0 replicate.

Usage:
  python3 pairwise_dv_probe.py            # k=5
  python3 pairwise_dv_probe.py --k 5
  python3 pairwise_dv_probe.py --score-only
Env: ANTHROPIC_API_KEY in the environment (Claude-only).
"""
import sys, json, hashlib, statistics, argparse
import concurrent.futures as cf
import run_study as R
import stage0_denoise as S0
import lib_llm as L

K_DEFAULT = 5
STABLE_VOTES = 4   # >=4/5 champion-better => pairwise "stable regression" (mirrors stage0's S_c>=4 lens)

PAIR_JUDGE_SYS = (
    "You are an impartial evaluator comparing TWO candidate recommendations produced for the SAME hard "
    "decision problem. Judge ONLY material would-ship flaws — errors that would change the decision or "
    "ship a real defect — not style, not length, not polish. Decide which recommendation carries FEWER / "
    "LESS-SEVERE material would-ship flaws, or whether they are materially EQUIVALENT. Be willing to say "
    "EQUIVALENT when neither is materially better — do NOT manufacture a difference to pick a winner. You "
    "are blind to how either recommendation was produced."
)
PAIR_JUDGE_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION A:\n{a}\n\nRECOMMENDATION B:\n{b}\n\n"
    "Which carries fewer / less-severe material would-ship flaws? Return JSON: "
    "{{\"verdict\": \"A_BETTER\"|\"B_BETTER\"|\"EQUIVALENT\", \"reason\": str}}"
)


def judge_uid(aid, j):
    return f"pwdv__{aid}__rep{j}"


def order_for(aid, j):
    """Deterministic per (pair, replicate): is the champion in slot A or B? (blind order-randomization)."""
    h = int(hashlib.sha1(f"{aid}|{j}".encode("utf-8")).hexdigest(), 16)
    return "champ_A" if (h % 2 == 0) else "champ_B"


def judge_pair(item, j):
    aid = item["aid"]
    uid = judge_uid(aid, j)
    cached = R.load(uid)
    if cached:
        return cached
    problem = R.PROBLEMS[item["pid"]]["problem"]
    champ, cand = item["champ_text"], item["cand_text"]
    order = order_for(aid, j)
    a, b = (champ, cand) if order == "champ_A" else (cand, champ)
    out = L.claude_json(R.CLAUDE, PAIR_JUDGE_SYS,
                        PAIR_JUDGE_USER.format(problem=problem, a=a, b=b), max_tokens=1200)
    raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
    if raw == "EQUIVALENT":
        mapped = "equivalent"
    elif (raw == "A_BETTER" and order == "champ_A") or (raw == "B_BETTER" and order == "champ_B"):
        mapped = "champ_better"     # candidate is WORSE => the analog of a "regression"
    elif raw in ("A_BETTER", "B_BETTER"):
        mapped = "cand_better"
    else:
        mapped = "equivalent"       # unparseable -> treat as no-material-difference
    rec = {"aid": aid, "rep": j, "order": order, "raw_verdict": raw, "mapped": mapped}
    R.save(uid, rec)
    return rec


def run_judging(items, k):
    jobs = [(it, j) for it in items for j in range(1, k + 1)]
    print(f"[pwdv] {len(items)} pairs x k={k} = {len(jobs)} pairwise judgments "
          f"(resumable; cached skipped)", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(judge_pair, it, j): (it["aid"], j) for (it, j) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[pwdv] ERROR {futs[f]}: {repr(e)[:150]}", flush=True)
            done += 1
            if done % 25 == 0:
                print(f"[pwdv] judged {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[pwdv] {errs} errors -- re-run to retry (resumable).", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--score-only", action="store_true")
    args = ap.parse_args()
    k = args.k

    items = S0.gather_items()
    print(f"[pwdv] {len(items)} candidate pairs; {sum(1 for it in items if it['raw_regression'])} "
          f"raw regressions (expect 61 / 11)", flush=True)
    run_judging(items, k)
    if args.score_only:
        print("[pwdv] --score-only: judging complete; skipping assembly.")
        return

    # stage0 answer key
    s0 = json.loads((R.PILOT / "analysis" / "stage0-denoise.json").read_text())
    s0_rows = {r["aid"]: r for r in s0["rows"] if not r.get("incomplete")}

    rows, incomplete = [], 0
    for it in items:
        aid = it["aid"]
        verdicts = []
        for j in range(1, k + 1):
            rec = R.load(judge_uid(aid, j))
            if not rec:
                verdicts = None
                break
            verdicts.append(rec["mapped"])
        if verdicts is None:
            incomplete += 1
            rows.append({"aid": aid, "incomplete": True})
            continue
        CB = sum(1 for v in verdicts if v == "champ_better")
        CandB = sum(1 for v in verdicts if v == "cand_better")
        Eq = sum(1 for v in verdicts if v == "equivalent")
        s0r = s0_rows.get(aid, {})
        S_c = s0r.get("S_c")
        rows.append({
            "aid": aid, "raw_regression": it["raw_regression"],
            "stage0_S_c": S_c, "stage0_stable": s0r.get("stable_regression"),
            "CB": CB, "CandB": CandB, "Eq": Eq, "verdicts": verdicts,
            "pairwise_stable_regression": CB >= STABLE_VOTES,
            "pw_modal_agreement": round(max(CB, k - CB) / k, 3),          # binary: champ_better vs not
            "abs_modal_agreement": (round(max(S_c, k - S_c) / k, 3) if S_c is not None else None),
        })

    complete = [r for r in rows if not r.get("incomplete")]
    if incomplete:
        print(f"[pwdv] WARNING: {incomplete} pairs missing judgments; re-run to complete.", flush=True)

    # --- noise comparison (same 61 pairs, same binary question, k=5) ---
    pw_agree = round(statistics.mean(r["pw_modal_agreement"] for r in complete), 3)
    abs_vals = [r["abs_modal_agreement"] for r in complete if r["abs_modal_agreement"] is not None]
    abs_agree = round(statistics.mean(abs_vals), 3) if abs_vals else None

    # --- validation against the stage0 answer key ---
    stable = [r for r in complete if r.get("stage0_stable")]                       # the 2 real regressions
    ghosts = [r for r in complete if r["raw_regression"] and not r.get("stage0_stable")]  # the 7 ghosts
    def cb_profile(rs):
        return {"n": len(rs), "mean_CB": round(statistics.mean(r["CB"] for r in rs), 2) if rs else None,
                "mean_Eq": round(statistics.mean(r["Eq"] for r in rs), 2) if rs else None,
                "n_called_champ_better>=4": sum(1 for r in rs if r["CB"] >= STABLE_VOTES)}

    pw_stable_count = sum(1 for r in complete if r["pairwise_stable_regression"])
    eq_rate = round(statistics.mean(r["Eq"] / k for r in complete), 3)

    summary = {
        "EXPLORATORY": True, "k": k, "n_pairs": len(complete), "n_incomplete": incomplete,
        "answer_key": "analysis/stage0-denoise.json (2 stable regressions, 7 ghosts among 11 raw)",
        "noise_comparison": {
            "pairwise_mean_modal_agreement": pw_agree,
            "absolute_mean_modal_agreement": abs_agree,
            "quieter": (pw_agree > abs_agree) if abs_agree is not None else None,
            "note": "higher = less noisy; both binarized to 'is the candidate worse (champion better)?'",
        },
        "validation": {
            "stable_regressions": cb_profile(stable),      # want: high mean_CB, both called champ_better>=4
            "ghosts": cb_profile(ghosts),                  # want: low mean_CB, high mean_Eq, ~0 called >=4
        },
        "pairwise_stable_regressions_total": pw_stable_count,
        "equivalent_usage_rate": eq_rate,
        "rows": rows,
    }
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    out = R.PILOT / "analysis" / "pairwise-dv-probe.json"
    out.write_text(json.dumps(summary, indent=2))

    print("\n=== PAIRWISE-DV PROBE (EXPLORATORY) ===")
    print(f"  pairs judged: {len(complete)}  (incomplete: {incomplete})")
    print(f"  NOISE: pairwise modal-agreement {pw_agree}  vs  absolute DV {abs_agree}  "
          f"-> pairwise {'QUIETER' if (abs_agree is not None and pw_agree > abs_agree) else 'NOT quieter'}")
    print(f"  VALIDATION vs stage0 answer key:")
    print(f"    2 stable regressions: mean champ-better votes {cb_profile(stable)['mean_CB']}/{k}, "
          f"{cb_profile(stable)['n_called_champ_better>=4']}/{len(stable)} called champ-better>=4  (want high)")
    print(f"    7 ghosts:             mean champ-better votes {cb_profile(ghosts)['mean_CB']}/{k}, "
          f"mean equivalent {cb_profile(ghosts)['mean_Eq']}/{k}, "
          f"{cb_profile(ghosts)['n_called_champ_better>=4']}/{len(ghosts)} called champ-better>=4  (want ~0)")
    print(f"  pairwise stable-regressions total (of {len(complete)}): {pw_stable_count}  (stage0 found 2)")
    print(f"  equivalent verdict usage rate: {eq_rate}  (judge should USE the equivalent option)")
    print(f"\n  READ: if pairwise is quieter AND recovers the 2 while rejecting the 7 -> better ruler.")
    print(f"        if pairwise is also noisy -> correctness is harder to measure than hoped (a finding).")
    print(f"\nwrote {out.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
