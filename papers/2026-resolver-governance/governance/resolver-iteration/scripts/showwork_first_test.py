#!/usr/bin/env python3
"""Show-your-work FIRST — does writing the math while drafting PREVENT unjustified numbers? (EXPLORATORY)

Earlier we showed that making the author externalize its arithmetic can CATCH a load-bearing number it
can't justify (one realistic problem hung its whole go/no-go trigger on a "~$650k/month" figure that
none of the author's own numbers produce). But that was after-the-fact annotation.

This tests the stronger claim: if the author shows its arithmetic WHILE writing the first draft, does it
commit to FEWER numbers it can't back up? Clean paired comparison, one variable:

  * PLAIN arm      — the SAME model writes the recommendation with an ordinary "produce a crisp
                     recommendation" prompt; we then ask it to externalize the math after the fact.
  * SHOWFIRST arm  — the SAME model writes the recommendation AND its supporting arithmetic together,
                     instructed that every load-bearing number must trace to named inputs.

Both arms are then scored identically: independently inventory the load-bearing quantitative claims, and
mechanically check (a calculator, not a model) how many are backed by a genuine, self-consistent,
input-grounded derivation. An UNJUSTIFIED load-bearing number = a claim with no genuine supporting
derivation. Fewer in SHOWFIRST than PLAIN = writing the math first prevents them.

Same model both arms (Claude) so the only variable is the prompt discipline — not the vendor. Quality
guard: an anti-bias pairwise judge checks the SHOWFIRST draft is not WORSE than the PLAIN draft.
Resumable; distinct swf_* cache prefixes. Cross-vendor coverage match (GPT) so Claude doesn't grade its
own coverage.

Usage: python3 showwork_first_test.py
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
from grounding_verify import EXTRACT_SYS, EXTRACT_USER          # independent load-bearing-claim inventory
from step3b_showwork import (verify_derivation, GENUINE_STATUSES, VERIFIED_STATUSES,
                             SYW_SYS, SYW_USER, COV_SYS, COV_USER)
from rescore_debiased import cf_verdict                          # anti-bias pairwise quality guard

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "showwork-first-test.json"

PLAIN_SYS = (
    "You are a senior expert producing a recommendation for a hard decision problem. Weigh the options and "
    "commit to ONE, with a crisp, shippable rationale of the kind a decision-maker would act on. Similar "
    "length to a solid one-page memo."
)
PLAIN_USER = "PROBLEM:\n{problem}\n\nReturn JSON: {{\"recommendation\": str}}"

SHOWFIRST_SYS = (
    "You are a senior expert producing a recommendation for a hard decision problem. Weigh the options and "
    "commit to ONE, with a crisp, shippable rationale a decision-maker would act on. As you write, SHOW "
    "YOUR WORK for every load-bearing number the decision rests on (costs, timelines, rates, capacities, "
    "thresholds, comparisons). For each such number give: named inputs (numeric, drawn from the problem or "
    "a stated assumption), a single-line Python arithmetic expression over ONLY those input NAMES, and the "
    "result. Every load-bearing figure in your recommendation MUST trace to inputs this way — do NOT state "
    "a load-bearing number you cannot derive. If a quantity is a genuine judgment call, say so in the prose "
    "rather than inventing arithmetic for it. Keep the recommendation itself crisp; the derivations are "
    "supporting work."
)
SHOWFIRST_USER = (
    "PROBLEM:\n{problem}\n\nReturn JSON: {{\"recommendation\": str, \"derivations\": [{{\"desc\": str, "
    "\"inputs\": {{name: number, ...}}, \"expr\": str, \"result\": number, \"used_in\": str}}]}}  "
    "— used_in is the verbatim clause of your recommendation where the result is used."
)


def gen_plain(pid, problem):
    uid = f"swf_plain__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, PLAIN_SYS, PLAIN_USER.format(problem=problem), max_tokens=4000)
        c = {"recommendation": (out.get("recommendation", "") if isinstance(out, dict) else "") or ""}
        R.save(uid, c)
    return c["recommendation"]


def gen_showfirst(pid, problem):
    uid = f"swf_showfirst__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, SHOWFIRST_SYS, SHOWFIRST_USER.format(problem=problem), max_tokens=5000)
        rec = (out.get("recommendation", "") if isinstance(out, dict) else "") or ""
        ders = out.get("derivations", []) if isinstance(out, dict) else []
        c = {"recommendation": rec, "derivations": ders[:16]}
        R.save(uid, c)
    return c["recommendation"], c["derivations"]


def retrofit_worksheet(pid, problem, rec):
    """PLAIN arm's math, externalized AFTER the fact (author annotates its own finished draft)."""
    uid = f"swf_retro__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, SYW_SYS, SYW_USER.format(problem=problem, rec=rec), max_tokens=4000)
        ders = out.get("derivations", []) if isinstance(out, dict) else []
        c = {"derivations": ders[:16]}
        R.save(uid, c)
    return c["derivations"]


def inventory(pid, arm, problem, rec):
    """Independent inventory of the load-bearing quantitative claims in a draft (audit extractor)."""
    uid = f"swf_inv__{arm}__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, EXTRACT_SYS, EXTRACT_USER.format(problem=problem, rec=rec), max_tokens=2500)
        claims = out.get("claims", []) if isinstance(out, dict) else []
        c = {"claims": claims[:16]}
        R.save(uid, c)
    return c["claims"]


def coverage(pid, arm, claims, ders):
    """Cross-vendor (GPT) match of the author's derivations to the independent claim inventory."""
    uid = f"swf_cov__{arm}__{pid}"
    c = R.load(uid)
    if c:
        return c["matches"]
    if not claims:
        R.save(uid, {"matches": []}); return []
    a = "\n".join(f"{i}. {cl.get('desc','')}" for i, cl in enumerate(claims))
    b = "\n".join(f"{i}. {d.get('desc','')}" for i, d in enumerate(ders)) or "(none)"
    out = L.gpt_json(R.GPT, COV_SYS, COV_USER.format(a=a, b=b))
    matches = out.get("matches", []) if isinstance(out, dict) else []
    R.save(uid, {"matches": matches})
    return matches


def score_arm(pid, arm, problem, rec, ders):
    ders = [d for d in ders if isinstance(d, dict)]          # models occasionally emit a stray non-dict
    verified = [verify_derivation(d, rec) for d in ders]
    claims = inventory(pid, arm, problem, rec)
    matches = coverage(pid, arm, claims, ders)
    # a load-bearing claim is JUSTIFIED iff matched to a genuine derivation (input-grounded+nontrivial+consistent)
    justified = 0
    for m in matches:
        bi = m.get("b_index", -1)
        st = verified[bi]["status"] if (isinstance(bi, int) and 0 <= bi < len(verified)) else None
        justified += 1 if st in GENUINE_STATUSES else 0
    n_claims = len(claims)
    unjustified = n_claims - justified
    st_ct = collections.Counter(d["status"] for d in verified)
    genuine = sum(st_ct[s] for s in GENUINE_STATUSES)
    return {"arm": arm, "n_derivations": len(ders), "genuine_derivations": genuine,
            "n_load_bearing_claims": n_claims, "justified": justified, "unjustified": unjustified,
            "der_status": dict(st_ct), "derivations": verified, "claims": claims}


def run_problem(pid, problem):
    plain_rec = gen_plain(pid, problem)
    plain_ders = retrofit_worksheet(pid, problem, plain_rec)
    sf_rec, sf_ders = gen_showfirst(pid, problem)
    plain = score_arm(pid, "plain", problem, plain_rec, plain_ders)
    showf = score_arm(pid, "showfirst", problem, sf_rec, sf_ders)
    # quality guard (SECONDARY): anti-bias pairwise, PLAIN=A vs SHOWFIRST=B. Isolated so a flaky judge
    # vote can't drop the whole problem's primary (grounding) result.
    try:
        q = cf_verdict(problem, plain_rec, sf_rec, f"swf_q__{pid}", 3)
        quality = {"A_BETTER": "plain_better", "EQUIVALENT": "equivalent", "B_BETTER": "showfirst_better"}[q]
    except Exception as e:   # noqa: BLE001
        print(f"[swf] {pid}: quality guard failed ({repr(e)[:80]}) -> unknown", flush=True)
        quality = "unknown"
    return {"pid": pid, "plain": plain, "showfirst": showf, "quality_showfirst_vs_plain": quality}


def main():
    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}
    print(f"[swf] show-your-work-first prevention test on {len(corpus)} problems (same model both arms)", flush=True)

    rows = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_problem, pid, corpus[pid]["problem"]): pid for pid in corpus}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); rows[r["pid"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[swf] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)

    def tot(arm, key):
        return sum(rows[p][arm][key] for p in rows)
    agg = {}
    for arm in ("plain", "showfirst"):
        claims = tot(arm, "n_load_bearing_claims"); unj = tot(arm, "unjustified")
        agg[arm] = {"load_bearing_claims": claims, "justified": tot(arm, "justified"),
                    "unjustified": unj,
                    "unjustified_rate": round(unj / claims, 3) if claims else None,
                    "derivations": tot(arm, "n_derivations"), "genuine_derivations": tot(arm, "genuine_derivations")}
    qdist = collections.Counter(rows[p]["quality_showfirst_vs_plain"] for p in rows)
    # per-problem paired delta in unjustified count (plain - showfirst); positive = show-first has fewer
    paired = [{"pid": p, "plain_unjustified": rows[p]["plain"]["unjustified"],
               "showfirst_unjustified": rows[p]["showfirst"]["unjustified"],
               "delta": rows[p]["plain"]["unjustified"] - rows[p]["showfirst"]["unjustified"]}
              for p in corpus if p in rows]
    helped = sum(1 for x in paired if x["delta"] > 0)
    hurt = sum(1 for x in paired if x["delta"] < 0)

    summary = {"EXPLORATORY": True, "n_problems": len(rows), "same_model_both_arms": R.CLAUDE,
               "aggregate": agg, "quality_showfirst_vs_plain": dict(qdist),
               "paired_unjustified_delta": paired,
               "problems_showfirst_had_fewer_unjustified": helped,
               "problems_showfirst_had_more_unjustified": hurt,
               "detail": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== SHOW-YOUR-WORK-FIRST — does writing the math first prevent unjustified numbers? ===")
    print(f"  same model both arms: {R.CLAUDE}   problems: {len(rows)}")
    print(f"\n  {'arm':10s} {'load-bearing #s':>15s} {'justified':>10s} {'UNJUSTIFIED':>12s} {'rate':>6s}")
    for arm in ("plain", "showfirst"):
        a = agg[arm]
        print(f"  {arm:10s} {a['load_bearing_claims']:15d} {a['justified']:10d} {a['unjustified']:12d} "
              f"{(a['unjustified_rate'] if a['unjustified_rate'] is not None else 0):6.2f}")
    print(f"\n  paired: show-first had FEWER unjustified numbers on {helped}/{len(paired)} problems, "
          f"MORE on {hurt}/{len(paired)}")
    print(f"  quality (show-first vs plain, anti-bias judge): {dict(qdist)}")
    print(f"\n  {'id':22s} {'plain unj':>9s} {'showfirst unj':>13s} {'delta':>6s}   quality")
    for x in paired:
        print(f"  {x['pid']:22s} {x['plain_unjustified']:9d} {x['showfirst_unjustified']:13d} {x['delta']:6d}   "
              f"{rows[x['pid']]['quality_showfirst_vs_plain']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
