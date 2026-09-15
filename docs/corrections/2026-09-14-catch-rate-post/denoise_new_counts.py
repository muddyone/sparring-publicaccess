#!/usr/bin/env python3
"""denoise_new_counts.py -- how many "new" flaws the study's scorer finds in drafts nobody touched.

EXPLORATORY and derived. It makes no model calls and uses no randomness, so a rerun writes the same
bytes. It writes numbers only: no recommendation text and no audit text.

WHAT IT READS. The 2026-06-30 de-noise probe (scripts/stage0_denoise.py) re-scored each of the 8 original
recommendations (R0) five times through the study's own scorer (run_study.score_output). That is the same
audit panel and the same new-flaw matcher that scored every revised draft. This script reads those 40
score files (runs/score__s0__<sha>__rep<j>.json, where sha = sha1(pid + "::" + R0 text)[:16], as in
stage0_denoise.py), plus the 24 committed score records for R1 same-vendor, R1 cross-vendor and R1prime.

WHY IT MATTERS. The main study never scored R0. Its 3.875 net flaws were set by construction, with 0
new. Every revised draft was scored, and the scorer counts any flaw not on the original list as "new".
So "new flaws introduced by the revision" includes whatever the scorer finds in a draft nobody changed.
Only comparisons between drafts scored the same way cancel that baseline out.

COMPARISON MEANS. No committed aggregate stores new-flaw means: analysis/results-aggregate.json holds net
flaws only. So they are recomputed here from the per-draft score records, and checked against the table
in results.md l.12-14 (1.250 / 2.125 / 2.625).

Usage: python3 scripts/denoise_new_counts.py  ->  analysis/denoise-new-counts.json
"""
import hashlib
import json
import statistics
from pathlib import Path

PILOT = Path(__file__).resolve().parents[1]
REPO_PILOTS = PILOT.parent
RUNS = PILOT / "runs"
OUT = PILOT / "analysis" / "denoise-new-counts.json"
K = 5
COMPARE = {"R1__same": 2.125, "R1__cross": 2.625, "R1prime": 1.25}   # results.md l.12-14, "new flaws introduced"

_manifest = {}


def load(path):
    b = path.read_bytes()
    _manifest[str(path.relative_to(REPO_PILOTS))] = hashlib.sha256(b).hexdigest()
    return json.loads(b)


def sha_of(pid, text):                      # identical to stage0_denoise.sha_of
    return hashlib.sha1((pid + "::" + text).encode("utf-8")).hexdigest()[:16]


def paired(a, b):
    d = [x - y for x, y in zip(a, b)]
    sd = statistics.stdev(d)
    return {"per_problem": d, "mean": statistics.mean(d), "sd": sd, "se": sd / len(d) ** 0.5,
            "higher": sum(x > 0 for x in d), "lower": sum(x < 0 for x in d), "tied": sum(x == 0 for x in d)}


def rnd(x, d=4):
    if isinstance(x, float):
        return round(x, d)
    if isinstance(x, dict):
        return {k: rnd(v, d) for k, v in x.items()}
    if isinstance(x, list):
        return [rnd(v, d) for v in x]
    return x


def main():
    R0 = load(REPO_PILOTS / "catch-rate-v3-2026-06-28" / "recommendations.json")
    PIDS = list(R0.keys())

    # ---- the untouched originals, five scores each ------------------------------------------------
    untouched, all_new, all_short = {}, [], []
    for pid in PIDS:
        sha = sha_of(pid, R0[pid])
        reps = []
        for j in range(1, K + 1):
            s = load(RUNS / f"score__s0__{sha}__rep{j}.json")
            assert s["net_flaws_remaining"] == s["remain"] + s["new_count"]
            reps.append({"rep": j, "new_count": s["new_count"], "remain": s["remain"],
                         "listed_flaws": s["denom_count"], "net": s["net_flaws_remaining"]})
        news = [r["new_count"] for r in reps]
        untouched[pid] = {"score_file_sha": sha, "listed_flaws": reps[0]["listed_flaws"], "replicates": reps,
                          "new_count_mean": statistics.mean(news),
                          "new_count_min": min(news), "new_count_max": max(news)}
        all_new += news
        all_short += [r["listed_flaws"] - r["remain"] for r in reps]
    mean_new = statistics.mean(all_new)

    # cross-check: the nets must match the public stage0-denoise.json champion nets for round 1 (R0 is the champion)
    st0 = load(PILOT / "analysis" / "stage0-denoise.json")
    xcheck = {}
    for pid in PIDS:
        champ = {tuple(r["champ_nets"]) for r in st0["rows"] if r["pid"] == pid and r["round"] == 1}
        mine = [r["net"] for r in untouched[pid]["replicates"]]
        xcheck[pid] = len(champ) == 1 and sorted(next(iter(champ))) == sorted(mine)

    # ---- the same scorer on the revised drafts ---------------------------------------------------
    revised = {}
    for cond in COMPARE:
        recs = [load(RUNS / f"score__{cond}__{pid}.json") for pid in PIDS]
        new = [r["new_count"] for r in recs]
        remain = [r["remain"] for r in recs]
        listed = sum(r["denom_count"] for r in recs)
        revised[cond] = {
            "new_count_per_problem": new, "new_count_mean": statistics.mean(new),
            "listed_flaws_left_per_problem": remain,
            "listed_flaws_fixed_share": 1 - sum(remain) / listed,
            "net_mean": statistics.mean(r["net_flaws_remaining"] for r in recs),
            "new_count_mean_minus_untouched": statistics.mean(new) - mean_new,
        }
    base = [untouched[p]["new_count_mean"] for p in PIDS]
    comparisons = {
        "R1.same_minus_R1prime_new": paired(revised["R1__same"]["new_count_per_problem"], revised["R1prime"]["new_count_per_problem"]),
        "R1.cross_minus_R1prime_new": paired(revised["R1__cross"]["new_count_per_problem"], revised["R1prime"]["new_count_per_problem"]),
        "R1prime_minus_untouched_new": paired(revised["R1prime"]["new_count_per_problem"], base),
        "R1.same_minus_untouched_new": paired(revised["R1__same"]["new_count_per_problem"], base),
        "R1.cross_minus_untouched_new": paired(revised["R1__cross"]["new_count_per_problem"], base),
    }

    checks = [
        {"check": "untouched score files found", "claimed": 40, "measured": len(all_new)},
        {"check": "mean new flaws on untouched R0", "claimed": 1.95, "measured": mean_new},
        {"check": "sum of new flaws on untouched R0", "claimed": 78, "measured": sum(all_new)},
        {"check": "mean listed flaws marked fixed on untouched R0", "claimed": 0.275, "measured": statistics.mean(all_short)},
        {"check": "nets match stage0-denoise.json round-1 champion nets", "claimed": True, "measured": all(xcheck.values())},
    ] + [{"check": f"{c} mean new flaws (results.md)", "claimed": v, "measured": revised[c]["new_count_mean"]}
         for c, v in COMPARE.items()]
    for c in checks:
        c["reproduces"] = (c["claimed"] == c["measured"]) if isinstance(c["claimed"], bool) \
            else abs(c["claimed"] - c["measured"]) < 1e-9

    out = {
        "EXPLORATORY": True,
        "what": "'New' flaws found by the study's own scorer in the 8 original recommendations (R0), scored "
                "5 times each and never revised; plus the same scorer's counts on three revised conditions.",
        "problems": PIDS,
        "untouched_R0": {"per_problem": untouched, "new_count_mean": mean_new, "n_scores": len(all_new),
                         "listed_flaws_marked_fixed_mean": statistics.mean(all_short)},
        "revised_same_scorer": revised,
        "comparisons": comparisons,
        "how_to_read": "Sizes of 'new flaws introduced by revision' do not carry: the scorer finds about "
                       "this many in a draft nobody touched. Differences between drafts scored the same "
                       "way do carry, because a constant baseline cancels out of a difference (not out of a ratio).",
        "cross_check_with_stage0_denoise_json": xcheck,
        "checks": checks,
        "input_manifest_sha256": dict(sorted(_manifest.items())),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    OUT.write_text(json.dumps(rnd(out), indent=1) + "\n")
    bad = [c["check"] for c in checks if not c["reproduces"]]
    print(f"wrote {OUT.name}; mean new on untouched R0 = {mean_new} (n={len(all_new)}); "
          f"{len(checks)} checks, {len(bad)} not reproduced")
    for b in bad:
        print("  NOT REPRODUCED:", b)


if __name__ == "__main__":
    main()
