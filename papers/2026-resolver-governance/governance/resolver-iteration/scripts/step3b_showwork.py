#!/usr/bin/env python3
"""Step 3b (grounding) — PRODUCER-AUTHORED show-your-work (EXPLORATORY).

Step 3 (grounding_verify.py) found the bottleneck: a *post-hoc extractor* rebuilds the
recommendation's arithmetic from finished prose, so a "MISMATCH" is far more likely an
extraction artifact (the extractor guessed the wrong formula) than a real rec error. Both
step-2 "caught errors" were exactly that.

Step 3b removes the extractor. The PRODUCER — the author of the recommendation — externalizes
its own load-bearing derivations: named inputs, a Python expression over those names, the value
its own derivation yields, and the number the *prose actually asserts* (with the verbatim snippet
it comes from). Python is then ground truth on TWO independent things:

  1. worksheet self-consistency:  eval(expr, inputs)  ==  the result the producer claims
  2. prose faithfulness:          eval(expr, inputs)  ==  the number the recommendation asserts

Because the producer authored inputs+expr, a prose-faithfulness failure is a GENUINE internal
inconsistency in the shipped recommendation (a real caught error), not an extraction artifact —
that is the whole explainability payoff we are testing.

Metrics (gold-free):
  (a) VERIFIABLE-DERIVATION COVERAGE — of an independent inventory of the decision's load-bearing
      quantitative claims (reuse Step-3's audit extractor as the yardstick), what fraction does
      producer show-your-work externalize as a fully-verified derivation (input-grounded +
      non-trivial + self-consistent + prose-faithful)?  Match is judged CROSS-VENDOR (GPT), so
      Claude does not grade its own coverage.
  (b) FAITHFUL MECHANICAL-CHECK CATCH-RATE — among producer derivations, how often does the
      deterministic check FAITHFULLY fire: worksheet-arithmetic slips and prose contradictions
      surfaced, weak/vacuous derivations flagged. Precision of the check is definitional (it is
      arithmetic); the scientific question is whether producer authorship makes a fired check MEAN
      a real error. The head-to-head answers it: re-run the SAME two Step-3 mismatches under
      producer authorship — if they come out self-consistent + prose-faithful, they were
      extraction artifacts (Step-3's claim, now proven mechanically).

Retrofit on the step-2 converged finals (the same recommendations Step-3 verified) so the ONLY
variable vs Step-3 is who authors the derivation. Resumable; cross-vendor where noted.

Usage: python3 step3b_showwork.py [--source step2|R0]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, ast, operator, re, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
AUDIT = R.PILOT / "analysis" / "grounding-verify.json"   # Step-3 independent claim inventory
OUT_JSON = R.PILOT / "analysis" / "step3b-showwork.json"

REL_TOL = 0.05   # 5% tolerance (rounding/approximation in prose), matches Step 3

# --------------------------------------------------------------------------- producer show-your-work
SYW_SYS = (
    "You are the senior expert who AUTHORED the recommendation below. Show your work: externalize "
    "every load-bearing quantitative derivation the recommendation's DECISION actually rests on "
    "(costs, timelines, rates, capacities, thresholds, ratios, comparisons). For EACH such derivation:\n"
    "  - desc: what quantity it is and why the decision depends on it\n"
    "  - inputs: an object mapping short variable names to their NUMERIC values, each value drawn "
    "from the problem statement or a stated assumption. Name the source in the description if it is "
    "an assumption. Every number your expression uses MUST appear here as a named input.\n"
    "  - expr: a single-line Python arithmetic expression over ONLY those input variable NAMES "
    "(operators + - * / ** %, parentheses). No bare magic numbers — put every number in inputs and "
    "reference it by name. The expression must be the ACTUAL computation behind the quantity, not a "
    "restatement of the answer.\n"
    "  - result: the numeric value your expression yields (your own computed result)\n"
    "  - asserted_in_prose: the number your recommendation's TEXT actually states for this quantity "
    "(what a reader sees)\n"
    "  - used_in: the exact verbatim sentence or clause from the recommendation where this number "
    "drives the decision (copy it word-for-word)\n"
    "Include ONLY genuinely decision-load-bearing quantities reducible to arithmetic on stated "
    "numbers. If the decision rests on no quantitative derivation (pure judgment), return an empty "
    "list — that is a valid, expected answer. Do not invent derivations to fill the list."
)
SYW_USER = (
    "PROBLEM:\n{problem}\n\nYOUR RECOMMENDATION (you wrote this):\n{rec}\n\n"
    "Return JSON: {{\"derivations\": [{{\"desc\": str, \"inputs\": {{name: number, ...}}, "
    "\"expr\": str, \"result\": number, \"asserted_in_prose\": number, \"used_in\": str}}]}}  "
    "— empty list if nothing is load-bearing-and-arithmetic."
)

# --------------------------------------------------------------------------- coverage judge (cross-vendor)
COV_SYS = (
    "You are matching two lists of quantitative claims about the SAME recommendation. List A is an "
    "independent auditor's inventory of the load-bearing quantitative claims. List B is the author's "
    "own show-your-work derivations. For EACH claim in List A, decide whether ANY derivation in List B "
    "covers the SAME underlying quantity (same thing being computed), and give its B-index (or -1 if "
    "no derivation covers it). Two phrasings of the same quantity count as a match; a different "
    "quantity does not."
)
COV_USER = (
    "LIST A (independent auditor claims):\n{a}\n\nLIST B (author derivations):\n{b}\n\n"
    "Return JSON: {{\"matches\": [{{\"a_index\": int, \"b_index\": int, \"note\": str}}]}}  "
    "— one entry per List A claim; b_index -1 means uncovered."
)

# --------------------------------------------------------------------------- safe arithmetic over named vars
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
        ast.USub: operator.neg, ast.UAdd: operator.pos}


def _eval_node(n, env, names_used, ops_used):
    if isinstance(n, ast.Constant):
        if isinstance(n.value, bool) or not isinstance(n.value, (int, float)):
            raise ValueError("non-numeric const")
        return float(n.value)
    if isinstance(n, ast.Name):
        if n.id not in env or not isinstance(env[n.id], (int, float)) or isinstance(env[n.id], bool):
            raise ValueError(f"unbound:{n.id}")
        names_used.add(n.id)
        return float(env[n.id])
    if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
        ops_used.append(type(n.op).__name__)
        return _OPS[type(n.op)](_eval_node(n.left, env, names_used, ops_used),
                                _eval_node(n.right, env, names_used, ops_used))
    if isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
        ops_used.append(type(n.op).__name__)
        return _OPS[type(n.op)](_eval_node(n.operand, env, names_used, ops_used))
    raise ValueError(f"disallowed:{type(n).__name__}")


def safe_eval_named(expr, env):
    """Evaluate an arithmetic expr over named numeric vars. Returns (value, names_used, ops_used, err)."""
    e = (expr or "").strip()
    if not e:
        return None, set(), [], "empty"
    try:
        node = ast.parse(e, mode="eval").body
    except Exception as ex:   # noqa: BLE001
        return None, set(), [], f"parse:{type(ex).__name__}"
    names, ops = set(), []
    try:
        v = _eval_node(node, env, names, ops)
        return float(v), names, ops, None
    except Exception as ex:   # noqa: BLE001
        return None, names, ops, f"eval:{str(ex)[:40]}"


def _close(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return False
    denom = max(abs(a), abs(b), 1e-9)
    return abs(a - b) / denom <= REL_TOL


def _number_in_text(val, text):
    """Is the numeric value asserted anywhere in the prose (tolerant of formatting/commas/units)?"""
    if not isinstance(val, (int, float)):
        return False
    nums = re.findall(r"-?\d[\d,]*\.?\d*", text or "")
    for tok in nums:
        try:
            if _close(float(tok.replace(",", "")), val):
                return True
        except ValueError:
            continue
    return False


def _norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


# --------------------------------------------------------------------------- per-derivation mechanical verdict
#
# DESIGN NOTE (revised after first run): the producer's self-reported `asserted_in_prose` is UNRELIABLE
# — it routinely reports a salient INPUT (the deadline, the rate) instead of the derived quantity. Asking
# the producer "what does the prose say for this?" re-introduces exactly the fallible extraction step
# Step-3 identified. So the verdict does NOT gate on `asserted_in_prose`. The extraction-free faithfulness
# test is: does the producer's OWN computed result (from named inputs) actually appear in the rec text
# (deterministic number search)? That, plus worksheet self-consistency, are the only extraction-free signals.
def verify_derivation(d, rec_text):
    inputs = d.get("inputs", {}) if isinstance(d.get("inputs"), dict) else {}
    env = {k: v for k, v in inputs.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
    expr = d.get("expr", "")
    result = d.get("result", None)
    asserted = d.get("asserted_in_prose", None)
    used_in = d.get("used_in", "")

    computed, names_used, ops_used, err = safe_eval_named(expr, env)

    input_grounded = bool(names_used) and (not err) and all(n in env for n in names_used)
    nontrivial = bool(ops_used) and len(names_used) >= 1        # a real computation over ≥1 named input
    self_consistent = (computed is not None) and _close(computed, result)
    result_in_prose = (computed is not None) and _number_in_text(computed, rec_text)   # extraction-free faithfulness
    snippet_present = bool(used_in) and _norm(used_in) in _norm(rec_text)
    # diagnostic only (NOT a verdict gate): does the producer's self-report of the prose number line up?
    self_report_matches_computed = (computed is not None) and _close(computed, asserted)

    # verdict priority: mechanical failures first, then genuine-derivation quality, then prose grounding
    if err or not isinstance(result, (int, float)):
        status = "UNCHECKABLE"        # producer didn't give a computable derivation
    elif not input_grounded or not nontrivial:
        status = "WEAK"               # checkable but vacuous (literals-only / restates the answer)
    elif not self_consistent:
        status = "WORKSHEET_ERROR"    # producer's own expr ≠ producer's own stated result (a REAL arithmetic slip)
    elif result_in_prose:
        status = "GROUNDED"           # sound, input-grounded derivation whose result IS the number in the prose
    else:
        status = "UNCONFIRMED"        # sound derivation of an intermediate/unstated quantity (not text-matched)

    return {
        "desc": d.get("desc"), "expr": expr, "inputs": inputs,
        "computed": round(computed, 4) if computed is not None else None,
        "result_claimed": result, "asserted_in_prose": asserted,
        "input_grounded": input_grounded, "nontrivial": nontrivial,
        "self_consistent": self_consistent, "result_in_prose": result_in_prose,
        "snippet_present": snippet_present,
        "self_report_matches_computed": self_report_matches_computed,
        "eval_error": err, "status": status,
    }


# A "genuine externalized derivation": input-grounded, non-trivial, and internally sound — regardless of
# whether its output happens to appear verbatim in the prose (intermediates legitimately don't).
GENUINE_STATUSES = {"GROUNDED", "UNCONFIRMED"}
VERIFIED_STATUSES = {"GROUNDED"}   # coverage's strict bar: also text-grounded


# --------------------------------------------------------------------------- stages
def annotate(pid, problem, rec):
    uid = f"s3b_syw__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, SYW_SYS, SYW_USER.format(problem=problem, rec=rec), max_tokens=4000)
        ders = out.get("derivations", []) if isinstance(out, dict) else []
        c = {"derivations": ders[:16]}
        R.save(uid, c)
    return c["derivations"]


def coverage_match(pid, audit_claims, producer_ders):
    """Cross-vendor (GPT) match of producer derivations to the independent audit inventory."""
    uid = f"s3b_cov__{pid}"
    c = R.load(uid)
    if c:
        return c["matches"]
    if not audit_claims:
        R.save(uid, {"matches": []})
        return []
    a = "\n".join(f"{i}. {c.get('desc','')}" for i, c in enumerate(audit_claims))
    b = "\n".join(f"{i}. {d.get('desc','')}" for i, d in enumerate(producer_ders)) or "(none)"
    out = L.gpt_json(R.GPT, COV_SYS, COV_USER.format(a=a, b=b))
    matches = out.get("matches", []) if isinstance(out, dict) else []
    R.save(uid, {"matches": matches})
    return matches


def run_problem(pid, problem, rec, audit_claims):
    ders = annotate(pid, problem, rec)
    verified = [verify_derivation(d, rec) for d in ders]
    matches = coverage_match(pid, audit_claims, ders)
    # coverage: an audit claim is COVERED iff matched to a GENUINE producer derivation
    # (input-grounded, non-trivial, self-consistent); GROUNDED subset also text-matches the prose.
    covered = grounded = 0
    cov_detail = []
    for m in matches:
        bi = m.get("b_index", -1)
        st = verified[bi]["status"] if (isinstance(bi, int) and 0 <= bi < len(verified)) else None
        ok = st in GENUINE_STATUSES
        gr = st in VERIFIED_STATUSES
        covered += 1 if ok else 0
        grounded += 1 if gr else 0
        cov_detail.append({"a_index": m.get("a_index"), "b_index": bi, "b_status": st,
                           "covered": ok, "grounded": gr})
    return {"pid": pid, "n_derivations": len(ders), "n_audit_claims": len(audit_claims),
            "n_covered": covered, "n_grounded": grounded, "derivations": verified, "coverage_detail": cov_detail}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["step2", "R0"], default="step2")
    args = ap.parse_args()

    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}
    if args.source == "step2":
        finals = {}
        for pid in corpus:
            rev = R.load(f"s2_rev__{pid}__r3")
            finals[pid] = (rev.get("revised_recommendation", "") if rev else "") or corpus[pid]["R0"]
    else:
        finals = {pid: corpus[pid]["R0"] for pid in corpus}

    audit = json.loads(AUDIT.read_text())["detail"]     # pid -> {results:[...]}
    audit_claims = {pid: audit.get(pid, {}).get("results", []) for pid in corpus}
    # the two Step-3 mismatches, to re-test under producer authorship
    step3_mismatches = {pid: [c for c in audit_claims[pid] if c.get("status") == "MISMATCH"] for pid in corpus}

    print(f"[s3b] producer show-your-work on {len(finals)} recommendations ({args.source})", flush=True)

    rows = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_problem, pid, corpus[pid]["problem"], finals[pid], audit_claims[pid]): pid
                for pid in finals}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); rows[r["pid"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[s3b] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)

    # -------- aggregate
    status_tot = collections.Counter()
    tot_der = tot_audit = tot_cov = tot_grd = 0
    genuine_ct = grounded_ct = selfrep_noise = 0
    per = []
    for pid in corpus:
        r = rows.get(pid, {"n_derivations": 0, "n_audit_claims": 0, "n_covered": 0, "n_grounded": 0, "derivations": []})
        st = collections.Counter(d["status"] for d in r["derivations"])
        status_tot.update(st)
        tot_der += r["n_derivations"]; tot_audit += r["n_audit_claims"]
        tot_cov += r["n_covered"]; tot_grd += r.get("n_grounded", 0)
        for d in r["derivations"]:
            if d["status"] in GENUINE_STATUSES:
                genuine_ct += 1
            if d["status"] in VERIFIED_STATUSES:
                grounded_ct += 1
            # self-extraction noise: derivation is sound+genuine, but the producer's self-reported
            # prose number disagrees with its own computed result → the field is unreliable.
            if d["status"] in GENUINE_STATUSES and not d["self_report_matches_computed"]:
                selfrep_noise += 1
        per.append({"pid": pid, "domain": corpus[pid]["domain"],
                    "n_der": r["n_derivations"], "grounded": st["GROUNDED"],
                    "unconfirmed": st["UNCONFIRMED"], "worksheet_err": st["WORKSHEET_ERROR"],
                    "weak": st["WEAK"], "uncheckable": st["UNCHECKABLE"],
                    "audit_claims": r["n_audit_claims"], "covered": r["n_covered"], "cov_grounded": r.get("n_grounded", 0)})

    worksheet_err = status_tot["WORKSHEET_ERROR"]

    # -------- head-to-head: re-test the two Step-3 mismatches under producer authorship
    h2h = []
    for pid, mms in step3_mismatches.items():
        if not mms:
            continue
        # find the producer derivation covering the same quantity (best desc overlap)
        ders = rows.get(pid, {}).get("derivations", [])
        for mm in mms:
            best = None
            mwords = set(_norm(mm.get("desc", "")).split())
            for d in ders:
                overlap = len(mwords & set(_norm(d.get("desc", "")).split()))
                if best is None or overlap > best[0]:
                    best = (overlap, d)
            match = best[1] if best else None
            h2h.append({
                "pid": pid, "audit_desc": mm.get("desc"),
                "audit_expr": mm.get("python_expr"), "audit_computed": mm.get("computed"),
                "audit_asserted": mm.get("asserted"),
                "producer_status": match["status"] if match else "NO_PRODUCER_DERIVATION",
                "producer_expr": match["expr"] if match else None,
                "producer_inputs": match["inputs"] if match else None,
                "producer_computed": match["computed"] if match else None,
                "producer_asserted_in_prose": match["asserted_in_prose"] if match else None,
                "extraction_artifact_confirmed": bool(match and match["status"] in VERIFIED_STATUSES),
            })

    summary = {
        "EXPLORATORY": True, "source": args.source, "n_problems": len(corpus),
        "totals": {"derivations": tot_der, **dict(status_tot)},
        "coverage": {
            "audit_claims_total": tot_audit,
            "covered_by_genuine_derivation": tot_cov,
            "covered_and_text_grounded": tot_grd,
            "coverage_pct": round(100 * tot_cov / tot_audit, 1) if tot_audit else None,
            "grounded_pct": round(100 * tot_grd / tot_audit, 1) if tot_audit else None,
            "note": "covered = a cross-vendor-matched producer derivation that is input-grounded, "
                    "non-trivial and self-consistent; text-grounded also matches a number in the prose.",
        },
        "genuine_derivation_rate": f"{genuine_ct}/{tot_der}",
        "text_grounded_rate": f"{grounded_ct}/{tot_der}",
        "faithful_catches": {
            "worksheet_arithmetic_slips": worksheet_err,
            "weak_or_vacuous": status_tot["WEAK"],
            "uncheckable": status_tot["UNCHECKABLE"],
            "note": "worksheet slips are the extraction-free catch: producer expr != producer's own stated "
                    "result. Zero here means the finals' load-bearing arithmetic is internally sound.",
        },
        "self_extraction_noise": {
            "genuine_derivations_whose_self_reported_prose_number_is_wrong": selfrep_noise,
            "of_genuine": genuine_ct,
            "note": "asking the producer to ALSO self-report 'what the prose asserts' re-introduces the "
                    "Step-3 extraction bottleneck: this many sound derivations carry a wrong self-report. "
                    "The verdict deliberately does NOT gate on that field.",
        },
        "head_to_head_vs_audit": h2h,
        "per_problem": per, "detail": rows,
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    # -------- console report
    print("\n=== STEP 3b — PRODUCER-AUTHORED SHOW-YOUR-WORK (grounding) ===")
    print(f"  source: {args.source} finals   problems: {len(corpus)}")
    print(f"  total producer derivations: {tot_der}")
    print(f"  verdicts: " + "  ".join(f"{k}={v}" for k, v in sorted(status_tot.items())))
    print(f"\n  (a) VERIFIABLE-DERIVATION COVERAGE (vs independent audit inventory, cross-vendor matched):")
    print(f"      genuine derivation covers   {tot_cov}/{tot_audit} audit claims"
          + (f"  ({round(100*tot_cov/tot_audit,1)}%)" if tot_audit else ""))
    print(f"      AND text-grounded in prose  {tot_grd}/{tot_audit} audit claims"
          + (f"  ({round(100*tot_grd/tot_audit,1)}%)" if tot_audit else ""))
    print(f"      producer derivations genuine (input-grounded+nontrivial+consistent): {genuine_ct}/{tot_der}"
          f"   text-grounded: {grounded_ct}/{tot_der}")
    print(f"  (b) FAITHFUL MECHANICAL-CHECK CATCHES (extraction-free):")
    print(f"      worksheet arithmetic slips (producer expr != own stated result): {worksheet_err}")
    print(f"      weak/vacuous derivations flagged: {status_tot['WEAK']}   uncheckable: {status_tot['UNCHECKABLE']}")
    print(f"  (!) SELF-EXTRACTION NOISE: {selfrep_noise}/{genuine_ct} sound derivations carry a WRONG "
          f"producer self-report of the prose number")
    print(f"      → confirms Step-3's lesson: even producer self-extraction of 'what the prose says' is unreliable.")
    print(f"\n  {'id':22s} {'domain':26s} {'der':>3s} {'GRD':>3s} {'unc':>3s} {'wsE':>3s} {'wk':>3s} {'cov(grd)':>9s}")
    for p in per:
        print(f"  {p['pid']:22s} {p['domain'][:26]:26s} {p['n_der']:3d} {p['grounded']:3d} "
              f"{p['unconfirmed']:3d} {p['worksheet_err']:3d} {p['weak']:3d} "
              f"{p['covered']:>3d}({p['cov_grounded']})/{p['audit_claims']:<3d}")
    print("\n  HEAD-TO-HEAD — Step-3 mismatches re-tested under producer authorship:")
    if not h2h:
        print("    (none)")
    for h in h2h:
        tag = "EXTRACTION ARTIFACT CONFIRMED (Step-3 false catch)" if h["extraction_artifact_confirmed"] else f"producer={h['producer_status']} (ambiguous — inspect)"
        print(f"    {h['pid']}: {(h['audit_desc'] or '')[:56]}")
        print(f"      audit:    {h['audit_expr']} -> {h['audit_computed']} vs asserted {h['audit_asserted']}")
        print(f"      producer: {h['producer_expr']} = {h['producer_computed']}  => {tag}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
