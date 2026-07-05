#!/usr/bin/env python3
"""DV de-noise -- exploration probe (EXPLORATORY).

Method note: ../stage0-denoise-method-note.md  (a learning probe, NOT a prereg -- no locked rule).

The R5/R6 gate-discrimination metrics score each of the 61 candidate decisions as a regression iff
`cand_net > champ_before_net` -- a comparison of TWO single-panel net-flaw scores, so scoring noise
enters twice. Only 11 of 61 are labelled regressions, and an unknown share are +/-1 jitter (C12). This
probe replicate-scores the DV instrument k times per unique output and recomputes the regression label
per MATCHED replicate, so we can SEE how stable the labels are before reading into the R5/R6 numbers or
designing the paper's multi-round-spar section.

What it shows (look at the distribution, don't collapse to a threshold):
  - the S_c histogram over the 11 raw regressions -- how many survive re-scoring as stable positives;
  - sigma_DV = mean within-output SD of net_flaws_remaining -- the noise floor that sizes a real
    (paper-grade) Stage-1 test on fresh items.
The S_c>=4 "stable" lens and the surv_rate readout below are reading aids, not a locked decision rule.

Resumable + parallel: each replicate writes runs/score__s0__<sha>__rep<j>.json via run_study.score_output
(cached scores are skipped). Re-run to retry any errored replicate.

Deviation from prereg cost note (logged): all k replicates are drawn fresh under uniform s0__ keys rather
than reusing the heterogeneous main-study score (traj__* for admitted, r5rej__* for rejected) as rep0.
This is strictly cleaner (k independent draws, uniform instrument) and costs ~k fresh panels per output
instead of (k-1); it does not change any definition or the decision rule.

Usage:
  python3 stage0_denoise.py                 # k=5 (pre-registered)
  python3 stage0_denoise.py --k 5
  python3 stage0_denoise.py --score-only    # run the scoring pool only, skip assembly
Env: ANTHROPIC_API_KEY + OPENAI_API_KEY must be in the environment (same as r5/r6).
"""
import sys, json, hashlib, statistics, argparse
import concurrent.futures as cf
import run_study as R

# Reading aids only -- not locked decision rules. Adjust freely; this is exploration.
K_DEFAULT = 5
STABLE_VOTES = 4          # S_c >= 4 of 5 -> "stable-ish" regression lens
MARGIN_DELTA = 1.0        # mean(cand) - mean(champ) >= 1.0 flaw -> stable by margin
GO_SURV_RATE = 0.50       # soft readout: "looks real" if surv_rate >= 0.50 AND
GO_MIN_COUNT = 6          #               S >= 6  -- a heuristic, look at the histogram

R5_JSON = R.PILOT / "analysis" / "r5-challenge-gate.json"
OUT_JSON = R.PILOT / "analysis" / "stage0-denoise.json"


def sha_of(pid, text):
    return hashlib.sha1((pid + "::" + text).encode("utf-8")).hexdigest()[:16]


def champion_texts(u, pid):
    """round -> committed champion TEXT after that round; round 0 = R0[pid].

    Mirrors r5_challenge_gate.committed_per_round: the champion advances to the last admitted patch
    attempt of a round, else carries forward. champion-before round r == champion-after round r-1.
    """
    out = {0: R.R0[pid]}
    cur = R.R0[pid]
    for e in u["round_log"]:
        adm = None
        for a in e.get("patch_attempts", []):
            if a["gate"]["admit"]:
                adm = a["candidate"]
        if adm is not None:
            cur = adm
        out[e["round"]] = cur
    return out


def gather_items():
    """Per candidate decision (aid): pid, candidate text, champion-before text, joined to the raw R5
    regression label. Mirrors r5_challenge_gate.gather() so the unit set is exactly the same 61."""
    r5 = json.loads(R5_JSON.read_text())
    raw = {row["aid"]: row for row in r5["rows"]}
    items = []
    for pid in R.PIDS:
        for arm in ("same", "cross"):
            u = R.load(f"R3__{arm}__{pid}")
            if not u:
                continue
            champs = champion_texts(u, pid)
            for e in u["round_log"]:
                r = e["round"]
                champ_before = champs[r - 1]
                for i, a in enumerate(e.get("patch_attempts", [])):
                    aid = f"R3__{arm}__{pid}__r{r}__a{i}"
                    row = raw.get(aid)
                    if row is None:
                        continue   # r5 dropped it (missing score) -> not one of the 61
                    items.append({
                        "aid": aid, "pid": pid, "arm": arm, "round": r,
                        "cand_text": a["candidate"], "champ_text": champ_before,
                        "raw_regression": bool(row["dv_regression"]),
                        "raw_champ_net": row.get("champ_before_net"),
                        "raw_cand_net": row.get("cand_net"),
                        "cand_sha": sha_of(pid, a["candidate"]),
                        "champ_sha": sha_of(pid, champ_before),
                    })
    return items


def score_uid(sha, j):
    return f"s0__{sha}__rep{j}"


def run_scoring(items, k):
    """Score every unique (pid, text) output k times. Resumable (score_output caches) + parallel."""
    uniq = {}   # sha -> (pid, text)
    for it in items:
        uniq[it["cand_sha"]] = (it["pid"], it["cand_text"])
        uniq[it["champ_sha"]] = (it["pid"], it["champ_text"])
    jobs = [(sha, pid, text, j)
            for sha, (pid, text) in uniq.items()
            for j in range(1, k + 1)]
    print(f"[stage0] {len(uniq)} unique outputs x k={k} = {len(jobs)} replicate scores "
          f"(resumable; cached scores skipped)", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(R.score_output, score_uid(sha, j), pid, text): (sha, j)
                for (sha, pid, text, j) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[stage0] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)
            done += 1
            if done % 25 == 0:
                print(f"[stage0] scored {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[stage0] {errs} scoring errors -- re-run to retry (resumable).", flush=True)
    return uniq


def nets_for(sha, k):
    """The k replicate net_flaws_remaining for one output, or None if any replicate is missing."""
    out = []
    for j in range(1, k + 1):
        s = R.load(f"score__{score_uid(sha, j)}")
        if not s or s.get("net_flaws_remaining") is None:
            return None
        out.append(s["net_flaws_remaining"])
    return out


def _hist(rows, k):
    h = {v: 0 for v in range(k + 1)}
    for r in rows:
        h[r["S_c"]] += 1
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--score-only", action="store_true")
    args = ap.parse_args()
    k = args.k

    items = gather_items()
    n_raw_reg = sum(1 for it in items if it["raw_regression"])
    print(f"[stage0] {len(items)} candidate decisions; {n_raw_reg} raw regressions "
          f"(prereg expects 61 / 11)", flush=True)
    if not items:
        print("[stage0] no items -- is analysis/r5-challenge-gate.json present and the R3 runs in place?")
        sys.exit(1)

    uniq = run_scoring(items, k)
    if args.score_only:
        print("[stage0] --score-only: scoring pass complete; skipping assembly.")
        return

    # Q2: noise floor sigma_DV = mean over unique outputs of stdev(k reps)
    out_nets, out_sds, incomplete = {}, [], 0
    for sha in uniq:
        nets = nets_for(sha, k)
        out_nets[sha] = nets
        if nets is None:
            incomplete += 1
        elif len(nets) >= 2:
            out_sds.append(statistics.stdev(nets))
    sigma_dv = round(statistics.mean(out_sds), 3) if out_sds else None
    if incomplete:
        print(f"[stage0] WARNING: {incomplete} unique outputs still missing replicate scores; "
              f"re-run to complete before trusting the verdict.", flush=True)

    # Per-item matched-replicate regression tally S_c
    rows = []
    for it in items:
        c, p = out_nets.get(it["cand_sha"]), out_nets.get(it["champ_sha"])
        base = {kk: it[kk] for kk in ("aid", "pid", "arm", "round", "raw_regression")}
        if not c or not p:
            rows.append({**base, "incomplete": True})
            continue
        votes = sum(1 for j in range(k) if c[j] > p[j])
        mean_diff = statistics.mean(c) - statistics.mean(p)
        rows.append({**base, "cand_nets": c, "champ_nets": p, "S_c": votes,
                     "mean_diff": round(mean_diff, 3),
                     "stable_regression": votes >= STABLE_VOTES,
                     "stable_by_margin": mean_diff >= MARGIN_DELTA})

    complete = [r for r in rows if not r.get("incomplete")]
    raw_reg_rows = [r for r in complete if r["raw_regression"]]
    raw_clean_rows = [r for r in complete if not r["raw_regression"]]
    S = sum(1 for r in raw_reg_rows if r["stable_regression"])
    surv_rate = round(S / len(raw_reg_rows), 3) if raw_reg_rows else None
    S_margin = sum(1 for r in raw_reg_rows if r["stable_by_margin"])
    new_stable = sum(1 for r in raw_clean_rows if r["stable_regression"])   # missed by the raw score

    looks_real = (surv_rate is not None and surv_rate >= GO_SURV_RATE and S >= GO_MIN_COUNT)
    readout = "labels look mostly real" if looks_real else "labels look noise-heavy"

    summary = {
        "EXPLORATORY": True,
        "method_note": "stage0-denoise-method-note.md",
        "k": k,
        "rule": {"stable_votes": STABLE_VOTES, "margin_delta": MARGIN_DELTA,
                 "go_surv_rate": GO_SURV_RATE, "go_min_count": GO_MIN_COUNT},
        "n_candidates": len(complete),
        "n_incomplete": len(rows) - len(complete),
        "n_raw_regressions": len(raw_reg_rows),
        "stable_survivors_S": S,
        "surv_rate": surv_rate,
        "stable_survivors_by_margin": S_margin,
        "new_stable_positives_missed_by_raw": new_stable,
        "sigma_dv_noise_floor": sigma_dv,
        "S_c_hist_raw_regressions": _hist(raw_reg_rows, k),
        "S_c_hist_raw_clean": _hist(raw_clean_rows, k),
        "readout": readout,
        "rows": rows,
    }
    (R.PILOT / "analysis").mkdir(exist_ok=True)
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== DV DE-NOISE PROBE (EXPLORATORY -- a look, not a verdict) ===")
    print(f"  candidates scored : {len(complete)}  (incomplete: {len(rows) - len(complete)})")
    print(f"  raw regressions   : {len(raw_reg_rows)}")
    print(f"  S_c histogram (raw regressions): {_hist(raw_reg_rows, k)}   <- the main thing to look at")
    print(f"  stable-ish survivors (S_c >= {STABLE_VOTES} of {k}): {S}   surv_rate {surv_rate}")
    print(f"    secondary (margin >= {MARGIN_DELTA}): {S_margin}")
    print(f"  stable regressions the raw score MISSED (raw-clean): {new_stable}")
    print(f"  sigma_DV noise floor (mean within-output SD of net): {sigma_dv}   <- keep this; it sizes Stage-1")
    print(f"\n  heuristic readout: {readout}  (surv_rate {surv_rate} vs ~{GO_SURV_RATE}, S {S} vs ~{GO_MIN_COUNT})")
    print("  -- this is a reading aid; look at the histogram + sigma_DV and decide what it means for")
    print("     the multi-round-spar design. Rigor (fixed rule, fresh items) belongs to Stage-1 if/when")
    print("     it becomes a paper claim. EXPLORATORY; does not touch Paper 1.")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
