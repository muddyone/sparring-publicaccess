#!/usr/bin/env python3
"""preservation.py -- how much of a prior text each revision KEPT, and how much of the revision is NEW.

EXPLORATORY re-analysis of committed texts. It makes no model calls and uses no randomness, so a rerun
writes the same bytes. It is firewalled from Paper 1: it reads nothing under
pilots/llm-judge-2026-05-02/ and writes nothing there.

NAME. This is a PRESERVATION measure, not a "rewrite size" measure. The one-number version, "the share
of the prior version's words not kept", can't see additions: a revision that keeps every word and
appends five times as much text scores 0. So every comparison reports THREE numbers:

    prior_not_kept = 1 - kept / words(prior)       how much of the prior text is gone or changed
    output_new     = 1 - kept / words(output)      how much of the revision was not there before
    length_ratio   = words(output) / words(prior)  (also reported in characters)

  kept   = total size of the matching blocks from
           difflib.SequenceMatcher(None, prior_tokens, output_tokens, autojunk=False)
  tokens = str.split(): runs of whitespace; case and punctuation kept, no normalisation.

CHAINS (what is compared with what):
  A. final vs R0. Each condition's final_output against the Section 6.3 original (R0) of the same
     problem, for R1.same, R1.cross, R1prime, R2.same, R2.cross, R3.same and R3.cross, over 8 problems.
  B. The R3 patch chain. Every R3 patch attempt against the champion in force when it was proposed.
     The champion starts at R0 and advances to the round's admitted candidate, as r4.py (l.216-234) and
     stage0_denoise.champion_texts do. Admitted and rejected attempts are both reported.

SECONDARY (association, not cause): each final's preservation numbers against its committed new-flaw
count (runs/score__<cond>__<pid>.json). That count includes a scorer baseline of about 1.95 "new"
flaws on an untouched R0 (analysis/denoise-new-counts.json), so read these as orderings only.

R4 RELABEL CHECK: recomputes r4-results.json's churn_mean_chars.R3_whole_rewrite, and splits it into
characters removed and characters added.

Written 2026-09-14 as the committed, checkable version of a measure first run in-session during a
methods review. Reads the pilot's raw run files (runs/), which the public repository omits.
Usage: python3 scripts/preservation.py
       -> analysis/preservation-results.json and analysis/preservation-results.md
"""
import difflib
import hashlib
import json
import statistics
from pathlib import Path

PILOT = Path(__file__).resolve().parents[1]
REPO_PILOTS = PILOT.parent
V63 = REPO_PILOTS / "catch-rate-v3-2026-06-28"
RUNS = PILOT / "runs"
OUT_JSON = PILOT / "analysis" / "preservation-results.json"
OUT_MD = PILOT / "analysis" / "preservation-results.md"

FINAL_CONDS = ["R1__same", "R1__cross", "R1prime", "R2__same", "R2__cross", "R3__same", "R3__cross"]
LOCKED = {"R1__same", "R1__cross", "R1prime", "R2__same", "R2__cross"}
R3_ARMS = ["same", "cross"]
REVIEW = "in-session measurement, 2026-09-14"

_manifest = {}


def load(path):
    b = path.read_bytes()
    _manifest[str(path.relative_to(REPO_PILOTS))] = hashlib.sha256(b).hexdigest()
    return json.loads(b)


def tokens(text):
    return text.split()


def compare(prior, output):
    a, b = tokens(prior), tokens(output)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    kept = sum(m.size for m in sm.get_matching_blocks())
    return {
        "words_prior": len(a), "words_output": len(b), "words_kept": kept,
        "words_new": len(b) - kept,
        "prior_not_kept": 1 - kept / len(a),
        "output_new": 1 - kept / len(b),
        "length_ratio_words": len(b) / len(a),
        "chars_prior": len(prior), "chars_output": len(output),
        "length_ratio_chars": len(output) / len(prior),
        "identical_to_prior": prior == output,
    }


def char_churn(a, b, autojunk):
    """r4.py's _diff_size, split into removed and added characters."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=autojunk)
    rem = add = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            rem += i2 - i1
            add += j2 - j1
    return rem, add


def five(xs):
    xs = sorted(xs)
    q1, q2, q3 = statistics.quantiles(xs, n=4, method="inclusive") if len(xs) > 1 else (xs[0],) * 3
    return {"n": len(xs), "min": xs[0], "q1": q1, "median": statistics.median(xs), "q3": q3, "max": xs[-1]}


def rank(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2
        i = j + 1
    return r


def spearman(x, y):
    rx, ry = rank(x), rank(y)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den


def concordance(rows, key):
    c = d = t = 0
    for pid in {r["pid"] for r in rows}:
        pr = [r for r in rows if r["pid"] == pid]
        for i in range(len(pr)):
            for j in range(i + 1, len(pr)):
                s = (pr[i][key] - pr[j][key]) * (pr[i]["new_flaws"] - pr[j]["new_flaws"])
                c += s > 0
                d += s < 0
                t += s == 0
    return {"concordant": c, "discordant": d, "tied": t}


def rnd(x, d=4):
    if isinstance(x, float):
        return round(x, d)
    if isinstance(x, dict):
        return {k: rnd(v, d) for k, v in x.items()}
    if isinstance(x, list):
        return [rnd(v, d) for v in x]
    return x


def within(claimed, measured, tol):
    return abs(claimed - measured) <= tol + 1e-9


def main():
    R0 = load(V63 / "recommendations.json")          # pid -> the Section 6.3 original, as run_study.py l.39
    PIDS = list(R0.keys())

    # ---- A. final vs R0 ------------------------------------------------------------------------
    finals = []
    for cond in FINAL_CONDS:
        for pid in PIDS:
            u = load(RUNS / f"{cond}__{pid}.json")
            s = load(RUNS / f"score__{cond}__{pid}.json")
            row = {"condition": cond, "pid": pid, **compare(R0[pid], u["final_output"]),
                   "new_flaws": s["new_count"], "net_flaws": s["net_flaws_remaining"],
                   "R0_anchor_net": s["denom_count"]}
            finals.append(row)

    summ_final = {}
    for cond in FINAL_CONDS:
        rows = [r for r in finals if r["condition"] == cond]
        summ_final[cond] = {m: five([r[m] for r in rows]) for m in
                            ("prior_not_kept", "output_new", "length_ratio_words", "length_ratio_chars")}
        summ_final[cond]["identical_to_R0"] = [r["pid"] for r in rows if r["identical_to_prior"]]

    # ---- B. R3 patch chain --------------------------------------------------------------------
    patches, chain_mismatch = [], []
    for arm in R3_ARMS:
        for pid in PIDS:
            u = load(RUNS / f"R3__{arm}__{pid}.json")
            champ = R0[pid]
            for e in u["round_log"]:
                admitted = None
                for a in e.get("patch_attempts", []):
                    ok = bool(a["gate"]["admit"])
                    patches.append({"arm": arm, "pid": pid, "round": e["round"], "attempt": a["attempt"],
                                    "admitted": ok, **compare(champ, a["candidate"])})
                    if ok:
                        admitted = a["candidate"]
                if admitted is not None:
                    champ = admitted
            if champ != u["final_output"]:
                chain_mismatch.append(f"R3__{arm}__{pid}")

    groups = {}
    for arm in R3_ARMS:
        for label, sel in (("round1_admitted", lambda p: p["admitted"] and p["round"] == 1),
                           ("later_admitted", lambda p: p["admitted"] and p["round"] > 1),
                           ("rejected", lambda p: not p["admitted"])):
            rows = [p for p in patches if p["arm"] == arm and sel(p)]
            groups[f"R3.{arm}.{label}"] = ({m: five([p[m] for p in rows]) for m in
                                            ("prior_not_kept", "output_new", "length_ratio_words")}
                                           if rows else {"n": 0})
    adm = [p for p in patches if p["admitted"]]
    bins = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0001]

    def hist(key):
        return [sum(bins[i] <= p[key] < bins[i + 1] for p in adm) for i in range(len(bins) - 1)]

    patch_counts = {
        "attempts": len(patches), "admitted": len(adm), "rejected": len(patches) - len(adm),
        "admitted_prior_not_kept_lt_0.20": sum(p["prior_not_kept"] < .2 for p in adm),
        "admitted_prior_not_kept_gt_0.50": sum(p["prior_not_kept"] > .5 for p in adm),
        "admitted_output_new_lt_0.20": sum(p["output_new"] < .2 for p in adm),
        "admitted_output_new_gt_0.50": sum(p["output_new"] > .5 for p in adm),
        "hist_bins": ["0-.1", ".1-.2", ".2-.3", ".3-.4", ".4-.5", ".5-.6", ".6-.7", ".7-.8", ".8-.9", ".9-1"],
        "hist_admitted_prior_not_kept": hist("prior_not_kept"),
        "hist_admitted_output_new": hist("output_new"),
    }

    # ---- secondary: association with the committed new-flaw counts ------------------------------
    locked = [r for r in finals if r["condition"] in LOCKED]
    assoc = {}
    for key in ("prior_not_kept", "words_new"):
        assoc[key] = {
            "spearman_locked_40": spearman([r[key] for r in locked], [r["new_flaws"] for r in locked]),
            "spearman_all_56": spearman([r[key] for r in finals], [r["new_flaws"] for r in finals]),
            "within_problem_pairs_locked": concordance(locked, key),
            "within_problem_pairs_all": concordance(finals, key),
        }

    # ---- R4 relabel check ---------------------------------------------------------------------
    r4 = load(PILOT / "analysis" / "r4-results.json")
    churn = {}
    for arms_label, arms in (("same", ["same"]), ("cross", ["cross"]), ("both", R3_ARMS)):
        for aj in (True, False):
            rems, adds = [], []
            for arm in arms:
                for pid in PIDS:
                    u = load(RUNS / f"R3__{arm}__{pid}.json")
                    cur = R0[pid]
                    for e in u["round_log"]:
                        ad = [a for a in e.get("patch_attempts", []) if a["gate"]["admit"]]
                        if not ad:
                            continue
                        rem, add = char_churn(cur, ad[-1]["candidate"], aj)
                        rems.append(rem)
                        adds.append(add)
                        cur = ad[-1]["candidate"]
            churn[f"{arms_label}.autojunk_{'on' if aj else 'off'}"] = {
                "n_patches": len(rems), "mean_chars_changed": statistics.mean(r + a for r, a in zip(rems, adds)),
                "mean_chars_removed": statistics.mean(rems), "mean_chars_added": statistics.mean(adds)}
    r4_label_value = r4["churn_mean_chars"]["R3_whole_rewrite"]

    # ---- named reproduction checks ------------------------------------------------------------
    def med(cond, m):
        return summ_final[cond][m]["median"]

    r1_pool = [r["prior_not_kept"] for r in finals if r["condition"] in ("R1__same", "R1__cross")]
    r1p = [r["prior_not_kept"] for r in finals if r["condition"] == "R1prime"]
    checks = []

    def chk(name, claimed, source, measured, tol):
        checks.append({"check": name, "claimed": claimed, "source": source, "measured": measured,
                       "reproduces": within(claimed, measured, tol) if isinstance(claimed, (int, float))
                       and not isinstance(claimed, bool) else claimed == measured})

    chk("R1.same median prior_not_kept", 0.79, REVIEW, med("R1__same", "prior_not_kept"), .005)
    chk("R1.cross median prior_not_kept", 0.81, REVIEW, med("R1__cross", "prior_not_kept"), .005)
    chk("R1prime median prior_not_kept", 0.58, REVIEW, med("R1prime", "prior_not_kept"), .005)
    chk("R1 (both arms) min prior_not_kept", 0.70, REVIEW, min(r1_pool), .005)
    chk("R1 (both arms) max prior_not_kept", 0.92, REVIEW, max(r1_pool), .005)
    chk("R1prime min prior_not_kept", 0.37, REVIEW, min(r1p), .005)
    chk("R1prime max prior_not_kept", 0.65, REVIEW, max(r1p), .005)
    chk("R1 and R1prime ranges do not overlap", True, REVIEW, min(r1_pool) > max(r1p), 0)
    for arm, w, c, cmin, cmax, wmin, wmax in (("same", 5.72, 5.92, 1.86, 6.68, 1.8, 6.6),
                                               ("cross", 4.97, 5.22, 1.00, 8.14, 1.0, 7.7)):
        cd = f"R3__{arm}"
        chk(f"R3.{arm} median length ratio (words)", w, REVIEW, med(cd, "length_ratio_words"), .005)
        chk(f"R3.{arm} median length ratio (chars)", c, REVIEW, med(cd, "length_ratio_chars"), .005)
        chk(f"R3.{arm} min length ratio (chars)", cmin, REVIEW, summ_final[cd]["length_ratio_chars"]["min"], .005)
        chk(f"R3.{arm} max length ratio (chars)", cmax, REVIEW, summ_final[cd]["length_ratio_chars"]["max"], .005)
        chk(f"R3.{arm} min length ratio (words)", wmin, REVIEW, summ_final[cd]["length_ratio_words"]["min"], .05)
        chk(f"R3.{arm} max length ratio (words)", wmax, REVIEW, summ_final[cd]["length_ratio_words"]["max"], .05)
        chk(f"R3.{arm} median output_new (final vs R0)", 0.87, REVIEW, med(cd, "output_new"), .005)
    chk("R1.same median output_new", 0.89, REVIEW, med("R1__same", "output_new"), .005)
    chk("R1.cross median output_new", 0.90, REVIEW, med("R1__cross", "output_new"), .005)
    chk("R3.same later patches median prior_not_kept", 0.02, REVIEW, groups["R3.same.later_admitted"]["prior_not_kept"]["median"], .005)
    chk("R3.cross later patches median prior_not_kept", 0.05, REVIEW, groups["R3.cross.later_admitted"]["prior_not_kept"]["median"], .005)
    chk("R3.same later patches median output_new", 0.25, REVIEW, groups["R3.same.later_admitted"]["output_new"]["median"], .005)
    chk("R3.cross later patches median output_new", 0.31, REVIEW, groups["R3.cross.later_admitted"]["output_new"]["median"], .005)
    chk("R3.same later patches median length ratio", 1.31, REVIEW, groups["R3.same.later_admitted"]["length_ratio_words"]["median"], .005)
    chk("R3.cross later patches median length ratio", 1.30, REVIEW, groups["R3.cross.later_admitted"]["length_ratio_words"]["median"], .005)
    chk("R3.same round-1 median prior_not_kept", 0.41, REVIEW, groups["R3.same.round1_admitted"]["prior_not_kept"]["median"], .005)
    chk("R3.cross round-1 median prior_not_kept", 0.34, REVIEW, groups["R3.cross.round1_admitted"]["prior_not_kept"]["median"], .005)
    chk("admitted patches", 53, "analysis/r3-governance-trail.json", patch_counts["admitted"], 0)
    chk("rejected attempts", 8, "analysis/r3-governance-trail.json", patch_counts["rejected"], 0)
    chk("admitted prior_not_kept < 0.20", 37, REVIEW, patch_counts["admitted_prior_not_kept_lt_0.20"], 0)
    chk("admitted prior_not_kept > 0.50", 4, REVIEW, patch_counts["admitted_prior_not_kept_gt_0.50"], 0)
    chk("r4 R3_whole_rewrite (same arm, autojunk on)", r4_label_value, "analysis/r4-results.json",
        churn["same.autojunk_on"]["mean_chars_changed"], .05)
    chk("r4 R3 churn with autojunk off (same arm)", 3180.7, REVIEW,
        churn["same.autojunk_off"]["mean_chars_changed"], .05)
    chk("R3 final_output equals the end of the champion chain", [], "chain B construction", chain_mismatch, 0)

    out = {
        "EXPLORATORY": True,
        "name": "preservation (not rewrite size)",
        "method": {
            "tokenizer": "str.split() -- runs of whitespace; case and punctuation kept; no normalisation",
            "matcher": "difflib.SequenceMatcher(None, prior_tokens, output_tokens, autojunk=False)",
            "kept": "sum of matching-block sizes",
            "prior_not_kept": "1 - kept / words(prior)",
            "output_new": "1 - kept / words(output)",
            "length_ratio_words": "words(output) / words(prior)",
            "length_ratio_chars": "chars(output) / chars(prior)",
            "chain_A": "final_output of each condition vs the Section 6.3 original R0 (catch-rate-v3 recommendations.json)",
            "chain_B": "each R3 patch attempt vs the champion in force (R0, then the last admitted candidate of each prior round)",
            "not_covered": "R1prime's intermediate (first) self-revision is not saved; R2 per-round texts and R3v2 are not analysed",
        },
        "final_vs_R0": {"rows": finals, "summary": summ_final},
        "r3_patch_chain": {"rows": patches, "summary": groups, "counts": patch_counts},
        "association_with_new_flaws": assoc,
        "r4_relabel": {"r4_results_value": r4_label_value, "recomputed": churn},
        "checks": checks,
        "input_manifest_sha256": dict(sorted(_manifest.items())),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    OUT_JSON.write_text(json.dumps(rnd(out), indent=1, ensure_ascii=False) + "\n")
    OUT_MD.write_text(render_md(rnd(out), PIDS))
    bad = [c["check"] for c in checks if not c["reproduces"]]
    print(f"wrote {OUT_JSON.name} and {OUT_MD.name}; {len(checks)} checks, {len(bad)} not reproduced")
    for b in bad:
        print("  NOT REPRODUCED:", b)


def f2(x):
    return f"{x:.2f}"


def render_md(o, PIDS):
    short = [p.replace("P-", "") for p in PIDS]
    fr = o["final_vs_R0"]
    L = []
    w = L.append
    w("# Preservation measure for the resolver revisions (EXPLORATORY)\n")
    w("_Generated by `scripts/preservation.py`. Do not edit by hand: rerun the script. No model calls and no "
      "randomness, so a rerun writes the same bytes. Re-analysis of committed texts, firewalled from Paper 1. "
      f"Script sha256 `{o['script_sha256'][:16]}…`; {len(o['input_manifest_sha256'])} input files hashed in "
      "`preservation-results.json`._\n")
    w("## What it measures, and what it doesn't\n")
    w("This is a **preservation** measure: how much of a prior text a revision kept, and how much of the "
      "revision is text that wasn't there before. **It is not a measure of rewrite size.** Its one-number form "
      "(*share of prior words not kept*) can't see additions: a revision that keeps every word and appends "
      "five times as much scores 0. So every comparison here carries three numbers, and none should be "
      "quoted alone:\n")
    w("| quantity | formula | reads as |\n|---|---|---|")
    w("| `prior_not_kept` | 1 − kept / words(prior) | how much of the prior text is gone or changed |")
    w("| `output_new` | 1 − kept / words(output) | how much of the revision was not there before |")
    w("| `length_ratio` | words(output) / words(prior), also in characters | how much it grew |\n")
    w("**kept** is the total size of the matching blocks from "
      "`difflib.SequenceMatcher(None, prior_tokens, output_tokens, autojunk=False)`. **Tokens** come from "
      "`str.split()`: runs of whitespace, with case and punctuation kept and no normalisation.\n")
    w("**The two chains.**")
    w("- **A. Final against R0.** Each condition's `final_output` against the §6.3 original (R0) of the same "
      "problem, from `catch-rate-v3-2026-06-28/recommendations.json` (the same source as `run_study.py` l.39).")
    w("- **B. The R3 patch chain.** Every R3 patch attempt against the champion in force when it was proposed. "
      "The champion starts at R0 and advances to each round's admitted candidate, as `r4.py` l.216–234 and "
      "`stage0_denoise.champion_texts` do. Admitted and rejected attempts are both listed.\n")
    w("**Not covered.** R1′'s first (intermediate) self-revision is not saved, so R1′ is final-against-R0 only. "
      "R2's per-round texts and R3v2 are not analysed.\n")

    w("## A. Final against R0: every problem\n")
    for m, title in (("prior_not_kept", "prior words not kept"), ("output_new", "final words that are new"),
                     ("length_ratio_words", "length ratio, words"), ("length_ratio_chars", "length ratio, characters")):
        w(f"**{title}** (`{m}`)\n")
        w("| condition | " + " | ".join(short) + " | min | median | max |")
        w("|---|" + "---|" * (len(short) + 3))
        for cond, s in fr["summary"].items():
            vals = {r["pid"]: r[m] for r in fr["rows"] if r["condition"] == cond}
            w(f"| {cond.replace('__', '.')} | " + " | ".join(f2(vals[p]) for p in PIDS) +
              f" | {f2(s[m]['min'])} | **{f2(s[m]['median'])}** | {f2(s[m]['max'])} |")
        w("")
    ident = {c: s["identical_to_R0"] for c, s in fr["summary"].items() if s["identical_to_R0"]}
    w("**Finals identical to R0:** " + ("; ".join(f"{c.replace('__', '.')}: {', '.join(v)}" for c, v in ident.items())
                                        if ident else "none") + "\n")

    w("## B. The R3 patch chain\n")
    c = o["r3_patch_chain"]["counts"]
    w(f"There are {c['attempts']} attempts: {c['admitted']} admitted and {c['rejected']} rejected. Each cell below is "
      "min · Q1 · **median** · Q3 · max. The rows behind it are in the JSON.\n")
    w("| group | n | prior_not_kept | output_new | length ratio (words) |\n|---|---|---|---|---|")
    for g, s in o["r3_patch_chain"]["summary"].items():
        if s.get("n") == 0:
            w(f"| {g} | 0 | — | — | — |")
            continue
        cell = lambda d: f"{f2(d['min'])} · {f2(d['q1'])} · **{f2(d['median'])}** · {f2(d['q3'])} · {f2(d['max'])}"
        w(f"| {g} | {s['prior_not_kept']['n']} | {cell(s['prior_not_kept'])} | {cell(s['output_new'])} | "
          f"{cell(s['length_ratio_words'])} |")
    w("")
    w("**Admitted patches, histogram** (bins " + ", ".join(c["hist_bins"]) + "):")
    w(f"- prior_not_kept: {c['hist_admitted_prior_not_kept']}. That is {c['admitted_prior_not_kept_lt_0.20']} under 0.20 "
      f"and {c['admitted_prior_not_kept_gt_0.50']} over 0.50.")
    w(f"- output_new: {c['hist_admitted_output_new']}. That is {c['admitted_output_new_lt_0.20']} under 0.20 "
      f"and {c['admitted_output_new_gt_0.50']} over 0.50.\n")

    w("## Reproduction checks\n")
    w("These figures were first measured in-session during a 2026-09-14 methods review, and are recomputed "
      "here from committed files. Proportions and ratios pass if they agree to their stated precision.\n")
    w("| check | claimed | source | measured | reproduces |\n|---|---|---|---|---|")
    for k in o["checks"]:
        meas = k["measured"]
        meas = f"{meas:.4f}".rstrip("0").rstrip(".") if isinstance(meas, float) else json.dumps(meas)
        w(f"| {k['check']} | {json.dumps(k['claimed'])} | {k['source']} | {meas} | "
          f"{'yes' if k['reproduces'] else '**NO**'} |")
    w("")

    w("## Secondary: association with the committed new-flaw counts (ordering only, not cause)\n")
    w("Each final's `new_count` is read from `runs/score__<cond>__<pid>.json`. That count includes a scorer "
      "baseline: an untouched R0, re-scored five times by the same `score_output`, gets a mean of 1.95 \"new\" "
      "flaws (`analysis/denoise-new-counts.json`). Condition and preservation also move together. So these are "
      "orderings across drafts, not an effect of preservation.\n")
    w("| measure against new flaws | Spearman, locked 40 | Spearman, all 56 | within-problem pairs, locked (conc / disc / tied) | all 56 |")
    w("|---|---|---|---|---|")
    for key, label in (("prior_not_kept", "prior words not kept (preservation)"), ("words_new", "new words, count (volume)")):
        a = o["association_with_new_flaws"][key]
        pl, pa = a["within_problem_pairs_locked"], a["within_problem_pairs_all"]
        w(f"| {label} | {f2(a['spearman_locked_40'])} | {f2(a['spearman_all_56'])} | "
          f"{pl['concordant']} / {pl['discordant']} / {pl['tied']} | {pa['concordant']} / {pa['discordant']} / {pa['tied']} |")
    w("")

    w("## Relabelling note: `r4-results.json` → `churn_mean_chars.R3_whole_rewrite`\n")
    ch = o["r4_relabel"]["recomputed"]
    s_on, s_off, b_off = ch["same.autojunk_on"], ch["same.autojunk_off"], ch["both.autojunk_off"]
    w(f"`r4-results.json` reports `R3_whole_rewrite: {o['r4_relabel']['r4_results_value']}`. **The label is wrong about "
      "what the number is.** The file itself is left unchanged; this note is the correction.")
    w(f"- **What the number is.** It is the mean *character churn* (characters removed plus characters added) per admitted "
      f"R3 patch, against the champion it replaced, over the **same-vendor arm only** (r4.py `ARMS = (\"same\",)`, "
      f"{s_on['n_patches']} patches). It uses a character-level `SequenceMatcher` with the default `autojunk=True`. "
      f"Recomputed here: {s_on['mean_chars_changed']:.1f}.")
    w(f"- **Autojunk inflates it.** On long strings, autojunk treats common characters as junk and breaks up the "
      f"matches. With `autojunk=False` the same patches give {s_off['mean_chars_changed']:.1f}.")
    w(f"- **It is mostly additions.** Same arm, `autojunk=False`: a mean of {s_off['mean_chars_removed']:.1f} "
      f"characters removed against {s_off['mean_chars_added']:.1f} added per patch. Both arms "
      f"({b_off['n_patches']} patches): {b_off['mean_chars_removed']:.1f} removed against {b_off['mean_chars_added']:.1f} added.")
    w("- **So it does not describe whole rewrites.** Chain B shows R3 kept most of the prior text at every patch "
      "after round 1, and grew by appending. Read the figure as *mean characters changed per admitted R3 patch, "
      "mostly added text*. The label later led a review to the false premise that *\"R3's revisions were whole "
      "rewrites\"*.\n")

    bad = [k for k in o["checks"] if not k["reproduces"]]
    w("## Flags\n")
    if bad:
        for k in bad:
            w(f"- **Not reproduced:** {k['check']}: claimed {json.dumps(k['claimed'])}, measured {k['measured']}.")
    else:
        w("- Every reproduction check above passes.")
    for r in [r for r in fr["rows"] if r["identical_to_prior"]]:
        nets = ", ".join(f"{x['condition'].replace('__', '.')} {x['net_flaws']}" for x in fr["rows"] if x["pid"] == r["pid"])
        w(f"- **A final identical to R0:** {r['condition'].replace('__', '.')} on {r['pid']}. No patch was admitted, "
          f"so the text is the untouched original. Scored, it gets a net of {r['net_flaws']} flaws ({r['new_flaws']} new). "
          f"R0's anchor for this problem is {r['R0_anchor_net']}, set by construction and never scored. So any "
          f"contrast involving this draft is a contrast with an unchanged text. Nets on this problem: {nets}.")
    w("- **How to quote it.** Use the three numbers together, under the name *preservation*. Never quote "
      "*prior words not kept* alone as the size of a rewrite.\n")
    return "\n".join(L)


if __name__ == "__main__":
    main()
