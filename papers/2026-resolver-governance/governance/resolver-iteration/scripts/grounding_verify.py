#!/usr/bin/env python3
"""Step 3 (grounding), audit version — mechanical verification of load-bearing claims (EXPLORATORY).

Grounding's likely payoff is NOT convergence (step 2 near-ceilinged that) but (a) a VERIFIABLE explanation
and (b) the only untainted correctness signal we have: a calculator's verdict is ground truth, not a
model opinion. Restricted to checkable substructure, so expect an UNEVEN lift (quantitative problems bite;
judgment problems don't) — that unevenness is itself the finding.

Design discipline: the CHECK must be real computation, not an LLM asserting "verified", or we've just
added another fallible judge. So:
  * LLM EXTRACTS each load-bearing quantitative claim as structured data: the numbers the recommendation
    states, a Python expression for the computation it relies on, and the value/relation it ASSERTS.
  * PYTHON COMPUTES the truth from that expression (the grounded step).
  * Compare computed vs asserted -> VERIFIED / MISMATCH (a caught error) / UNCHECKABLE (judgment, no math).

Metrics (gold-free): verified-claim coverage, and verifier-caught errors (arithmetic the rec got wrong).
Run on the step-2 converged finals (default) — the recommendations we'd actually ship. Resumable.

Usage: python3 grounding_verify.py [--k 1]
Env: ANTHROPIC_API_KEY.
"""
import json, argparse, collections, math
import concurrent.futures as cf
import run_study as R
import lib_llm as L

STEP2 = R.PILOT / "analysis" / "step2-convergence.json"
CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "grounding-verify.json"

EXTRACT_SYS = (
    "You extract the LOAD-BEARING quantitative claims from a recommendation — the numeric facts its "
    "DECISION actually depends on (timelines, costs, rates, capacities, thresholds, comparisons). For each, "
    "give: a short description; the exact numbers the recommendation states; a single-line Python "
    "expression that computes the quantity the recommendation relies on, using ONLY those stated numbers "
    "and plain arithmetic (+ - * / , parentheses, ** ); and the numeric value the recommendation ASSERTS "
    "for that quantity (its claimed result). Only include claims that are genuinely decision-load-bearing "
    "AND reducible to arithmetic on stated numbers. Do NOT include judgment claims, forecasts, or anything "
    "not computable from the stated numbers — those are not checkable here. If the recommendation has no "
    "checkable quantitative substructure, return an empty list (that is a valid, expected answer)."
)
EXTRACT_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"claims\": [{{\"desc\": str, \"stated_numbers\": str, \"python_expr\": str, "
    "\"asserted_value\": number}}]}}  — python_expr must be evaluable with only arithmetic; asserted_value "
    "is the numeric result the recommendation claims. Empty list if nothing is checkable."
)

_ALLOWED = set("0123456789.+-*/() eE")   # arithmetic-only guard


def safe_eval(expr):
    """Evaluate an arithmetic-only expression. Returns (value, error)."""
    e = (expr or "").strip()
    if not e or any(c not in _ALLOWED for c in e):
        return None, "non-arithmetic"
    try:
        v = eval(e, {"__builtins__": {}}, {})   # arithmetic-only; chars whitelisted above
        return (float(v), None) if isinstance(v, (int, float)) else (None, "non-numeric")
    except Exception as ex:   # noqa: BLE001
        return None, f"eval:{type(ex).__name__}"


def extract(pid, problem, rec):
    uid = f"grd_ext__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, EXTRACT_SYS, EXTRACT_USER.format(problem=problem, rec=rec), max_tokens=2500)
        claims = out.get("claims", []) if isinstance(out, dict) else []
        c = {"claims": claims[:12]}
        R.save(uid, c)
    return c["claims"]


REL_TOL = 0.05   # 5% tolerance for "matches" (rounding/approximation in the prose)


def verify_claim(cl):
    expr = cl.get("python_expr", "")
    asserted = cl.get("asserted_value", None)
    computed, err = safe_eval(expr)
    if computed is None:
        return {"status": "UNCHECKABLE", "reason": err, "computed": None, "asserted": asserted}
    if not isinstance(asserted, (int, float)):
        return {"status": "UNCHECKABLE", "reason": "no asserted number", "computed": computed, "asserted": asserted}
    denom = max(abs(computed), abs(asserted), 1e-9)
    match = abs(computed - asserted) / denom <= REL_TOL
    return {"status": "VERIFIED" if match else "MISMATCH", "computed": round(computed, 4), "asserted": asserted}


def run(pid, problem, rec):
    claims = extract(pid, problem, rec)
    results = []
    for cl in claims:
        v = verify_claim(cl)
        results.append({**{k: cl.get(k) for k in ("desc", "stated_numbers", "python_expr", "asserted_value")}, **v})
    return {"pid": pid, "n_claims": len(claims), "results": results}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["step2", "R0"], default="step2",
                    help="which recommendation to verify (step2 converged final vs the original R0)")
    args = ap.parse_args()

    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}
    if args.source == "step2":
        s2 = json.loads(STEP2.read_text())
        finals = {}
        for pid in corpus:
            # step2 trajectories are cached as s2_rev__<pid>__r3
            rev = R.load(f"s2_rev__{pid}__r3")
            finals[pid] = (rev.get("revised_recommendation", "") if rev else "") or corpus[pid]["R0"]
    else:
        finals = {pid: corpus[pid]["R0"] for pid in corpus}
    print(f"[grd] verifying {len(finals)} recommendations ({args.source}); mechanical arithmetic check", flush=True)

    rows = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run, pid, corpus[pid]["problem"], finals[pid]): pid for pid in finals}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); rows[r["pid"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[grd] ERROR {futs[f]}: {repr(e)[:140]}", flush=True)

    # aggregate
    tot_claims = tot_ver = tot_mis = tot_unc = 0
    per = []
    for pid in corpus:
        r = rows.get(pid, {"results": [], "n_claims": 0})
        st = collections.Counter(x["status"] for x in r["results"])
        tot_claims += r["n_claims"]; tot_ver += st["VERIFIED"]; tot_mis += st["MISMATCH"]; tot_unc += st["UNCHECKABLE"]
        per.append({"pid": pid, "domain": corpus[pid]["domain"], "n": r["n_claims"],
                    "verified": st["VERIFIED"], "mismatch": st["MISMATCH"], "uncheckable": st["UNCHECKABLE"],
                    "mismatches": [x for x in r["results"] if x["status"] == "MISMATCH"]})

    checkable = tot_ver + tot_mis
    summary = {"EXPLORATORY": True, "source": args.source, "n_problems": len(corpus),
               "totals": {"claims": tot_claims, "verified": tot_ver, "mismatch": tot_mis, "uncheckable": tot_unc},
               "checkable_coverage": f"{checkable}/{tot_claims}" if tot_claims else "0/0",
               "caught_errors": tot_mis, "per_problem": per, "detail": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== GROUNDING (mechanical arithmetic verification) ===")
    print(f"  source: {args.source} recommendations")
    print(f"  total load-bearing quantitative claims extracted: {tot_claims}")
    print(f"  VERIFIED (arithmetic checks out): {tot_ver}")
    print(f"  MISMATCH (verifier CAUGHT an arithmetic error): {tot_mis}")
    print(f"  UNCHECKABLE (extraction non-arithmetic): {tot_unc}")
    n_quant = sum(1 for p in per if p["n"] > 0)
    print(f"  problems WITH checkable substructure: {n_quant}/{len(corpus)}  (the uneven-lift finding)")
    print(f"\n  {'id':22s} {'domain':28s} {'clm':>3s} {'ver':>3s} {'MIS':>3s} {'unc':>3s}")
    for p in per:
        flag = "  <-- CAUGHT" if p["mismatch"] else ""
        print(f"  {p['pid']:22s} {p['domain'][:28]:28s} {p['n']:3d} {p['verified']:3d} {p['mismatch']:3d} {p['uncheckable']:3d}{flag}")
    if tot_mis:
        print("\n  caught arithmetic errors (verifiable explanation failures):")
        for p in per:
            for m in p["mismatches"]:
                print(f"    {p['pid']}: {m['desc'][:60]} | expr={m['python_expr']} -> computed {m['computed']} vs asserted {m['asserted']}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
