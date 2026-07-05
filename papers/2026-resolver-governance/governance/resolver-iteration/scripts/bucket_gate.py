#!/usr/bin/env python3
"""The correctness gate — bucket-three detection (EXPLORATORY).

Enforces the definitiveness rule from PHASE-4-DESIGN-what-to-ship.md. Every HARD SPECIFIC a
recommendation states (number, money, %, rate, count, date, duration, definite magnitude) is read as
DEFINITIVE unless marked otherwise, so each must be:

  bucket 1  TRACEABLE      — follows from the PROBLEM's given facts (echoed, or derivable from stated
                            numbers). May stand unmarked.
  bucket 2  CONTEXTUALIZED — explicitly flagged as an estimate/example/assumption/approximation.
  bucket 3  NEITHER        — unmarked AND not traceable = an implicit false-definitive. GATE FAILURE.

Division of labor (the design principle): the MODEL does perception — enumerate the specifics, judge how
each is presented, and PROPOSE a derivation from problem-stated numbers. The CALCULATOR does the verdict
— a proposed derivation only counts if every input is quoted verbatim from the problem AND the arithmetic
reproduces the value. No model is ever asked to assert "traceable"; Python decides.

No human answer key (ruled out). The gate doesn't need one — each specific self-reveals its bucket. We
validate the DETECTOR cross-vendor instead: Claude and GPT both judge presentation and both propose
derivations; we report their agreement on the bucket-3 set and take a conservative union verdict (fail
only when unmarked by BOTH and traceable by NEITHER), so the gate does not over-fail on detector noise.

Usage: python3 bucket_gate.py [--source step2|R0|plain]
Env: ANTHROPIC_API_KEY, OPENAI_API_KEY.
"""
import json, argparse, re, collections, ast, operator, datetime
import concurrent.futures as cf
import run_study as R
import lib_llm as L
from step3b_showwork import _norm, _close, _number_in_text

# Arithmetic + a small whitelist of safe functions models actually use in derivations (round, min,
# max, abs). step3b's evaluator is arithmetic-only, which falsely failed e.g. `round(cash/burn, 1)`;
# this local version credits those. Still no attribute access, no arbitrary calls.
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.Mod: operator.mod, ast.USub: operator.neg, ast.UAdd: operator.pos}
_FUNCS = {"round": round, "min": min, "max": max, "abs": abs, "sum": sum}


def _ev(n, env):
    if isinstance(n, ast.Constant):
        if isinstance(n.value, bool) or not isinstance(n.value, (int, float)):
            raise ValueError("non-numeric const")
        return float(n.value)
    if isinstance(n, ast.Name):
        if n.id not in env or not isinstance(env[n.id], (int, float)) or isinstance(env[n.id], bool):
            raise ValueError(f"unbound:{n.id}")
        return float(env[n.id])
    if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
        return _OPS[type(n.op)](_ev(n.left, env), _ev(n.right, env))
    if isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
        return _OPS[type(n.op)](_ev(n.operand, env))
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in _FUNCS and not n.keywords:
        args = [_ev(a, env) for a in n.args]
        if n.func.id == "round" and len(args) == 2:   # round's ndigits must be int, not float
            args[1] = int(args[1])
        return float(_FUNCS[n.func.id](*args))
    raise ValueError(f"disallowed:{type(n).__name__}")


def safe_eval_named(expr, env):
    """Evaluate arithmetic + whitelisted functions over named numeric vars. (value, names, ops, err)."""
    e = (expr or "").strip()
    if not e:
        return None, set(), [], "empty"
    try:
        node = ast.parse(e, mode="eval").body
    except Exception as ex:   # noqa: BLE001
        return None, set(), [], f"parse:{type(ex).__name__}"
    try:
        return float(_ev(node, env)), set(), [], None
    except Exception as ex:   # noqa: BLE001
        return None, set(), [], f"eval:{str(ex)[:40]}"

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "bucket-gate.json"
REL_TOL = 0.05   # matches step3b's _close tolerance; used for range-band matching

# ---------------------------------------------------------------------- perception prompts (model)
ENUM_SYS = (
    "You audit a recommendation written for a hard decision problem. List every HARD SPECIFIC it states: "
    "a number, money amount, percentage, rate, count, date, duration, or definite factual magnitude the "
    "decision could rest on. For EACH give: the verbatim text as it appears; a single numeric value (for a "
    "range, the midpoint); a short description of what the number claims; and how it is PRESENTED — "
    "'definitive' if stated as a definite fact/figure, or 'contextualized' if EXPLICITLY hedged as an "
    "estimate, example, assumption, approximation, or something to verify (markers such as ~, about, "
    "roughly, approximately, 'assume', 'e.g.', 'for example', 'order of', 'ballpark', 'verify', 'subject "
    "to'). Exclude pure labels and enumerations (e.g. 'option 2', 'Phase 1', 'step 3') — those are not "
    "quantities. Be complete: every distinct stated quantity."
)
ENUM_USER = (
    "PROBLEM:\n{problem}\n\nRECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"specifics\": [{{\"text\": str, \"value\": number, \"claim\": str, "
    "\"presented_as\": \"definitive\"|\"contextualized\"}}]}}"
)

PRESENT_SYS = (
    "For each listed specific, judge how the recommendation PRESENTS it. Distinguish two kinds of wording, "
    "because they are NOT the same:\n"
    "  - 'definitive' — stated as a figure the reader is meant to rely on. CRITICAL: a precision hedge "
    "ALONE (~, about, roughly, approximately, 'around', 'on the order of') is STILL definitive — it only "
    "fuzzes the exact value while still asserting the magnitude as a real, relied-upon fact. '~$650k/month "
    "savings' is definitive: it claims there really is about that much.\n"
    "  - 'contextualized' — explicitly marked as NOT an established fact the reader should rely on: an "
    "assumption to supply ('assume X', 'if we assume'), an illustrative example ('e.g.', 'for example', "
    "'say, $X'), a placeholder to confirm ('verify against your actuals', 'TBD', 'subject to "
    "confirmation'), or an openly hypothetical figure.\n"
    "The test: does the wording tell the reader NOT to take this number as a given fact? Approximation is "
    "NOT contextualization. Judge presentation, not correctness.\n"
    "Calibration examples (a precision hedge stays definitive; only a basis flag is contextualized):\n"
    "  • \"~$650k/month in savings\" -> definitive (approximates a magnitude claimed real)\n"
    "  • \"roughly 30 engineers\" -> definitive (precision hedge)\n"
    "  • \"on the order of $2M\" -> definitive (precision hedge)\n"
    "  • \"a 22% renewal increase\" -> definitive (plain stated figure)\n"
    "  • \"assume a $50/unit cost\" -> contextualized (explicit assumption)\n"
    "  • \"for example, if churn is 5%\" -> contextualized (illustrative)\n"
    "  • \"a placeholder 20% margin, to be confirmed\" -> contextualized (flagged to confirm)\n"
    "  • \"budget ~$500k, but verify against your actuals\" -> contextualized (explicitly flagged to verify)\n"
    "  • \"say, 3 vendors\" -> contextualized (illustrative)"
)
PRESENT_USER = (
    "RECOMMENDATION:\n{rec}\n\nSPECIFICS:\n{items}\n\n"
    "Return JSON: {{\"labels\": [{{\"index\": int, \"presented_as\": \"definitive\"|\"contextualized\"}}]}}"
)

KIND_SYS = (
    "For each specific, classify it as DESCRIPTIVE or PRESCRIPTIVE:\n"
    "  - DESCRIPTIVE — a claim about the world, the situation, or a predicted outcome: a cost that will "
    "be incurred, a saving/advantage that will result, a quantity that exists, a rate that holds, how "
    "long something will take. It asserts something IS or WILL BE true, so it can be right or wrong.\n"
    "  - PRESCRIPTIVE — a parameter of the action the recommendation PROPOSES: a pilot length it advises "
    "running, a deadline it sets, a price it suggests charging, a staffing config it recommends, a target "
    "it says to hold. It is a CHOICE the plan makes, not a claim that can be false.\n"
    "When a number is both (a proposed action justified by a predicted magnitude), classify by what the "
    "number itself asserts. Judge the role of the number, not its correctness."
)
KIND_USER = (
    "RECOMMENDATION:\n{rec}\n\nSPECIFICS:\n{items}\n\n"
    "Return JSON: {{\"kinds\": [{{\"index\": int, \"kind\": \"descriptive\"|\"prescriptive\"}}]}}"
)

TRACE_SYS = (
    "You check whether each stated quantity can be derived using ONLY numbers that appear in the PROBLEM "
    "statement (the given facts). For each specific, either derive it or declare it underivable:\n"
    "  - If derivable, give inputs — each an object {{\"name\", \"value\", \"source_quote\"}} where "
    "source_quote is the VERBATIM phrase from the PROBLEM that states that number — and a single-line "
    "Python arithmetic expression over the input NAMES that computes the quantity, and the result. A "
    "quantity that is simply a number already stated in the problem has one input (itself).\n"
    "  - If it CANNOT be computed from problem-stated numbers alone — it needs an outside assumption, a "
    "market figure, or any number not in the problem — set derivable=false and give empty inputs/expr.\n"
    "NEVER invent a number that is not in the problem, and never fabricate a source_quote."
)
TRACE_USER = (
    "PROBLEM:\n{problem}\n\nSPECIFICS TO DERIVE:\n{items}\n\n"
    "Return JSON: {{\"derivations\": [{{\"index\": int, \"derivable\": bool, "
    "\"inputs\": [{{\"name\": str, \"value\": number, \"source_quote\": str}}], "
    "\"expr\": str, \"result\": number}}]}}"
)


EXPLAIN_SYS = (
    "A release gate flagged a specific figure in a recommendation as not obviously traceable to the "
    "problem's given facts. For each flagged figure, try hard to derive it using ONLY numbers stated in "
    "the PROBLEM, and be explicit about what you cannot ground:\n"
    "  - inputs_grounded: inputs whose value IS stated in the problem — each {name, value, source_quote} "
    "with source_quote the VERBATIM problem phrase.\n"
    "  - inputs_assumed: inputs you must ASSUME because the problem does NOT state them — each {name, "
    "value, why} (why = what it represents and why the figure needs it).\n"
    "  - expr: a single-line Python arithmetic expression over the input NAMES; result: its value.\n"
    "Never invent a source_quote — if a number is not in the problem it is ASSUMED, not grounded. If the "
    "figure cannot be reached even with assumptions, set derivable=false and use inputs_assumed to name "
    "what would be required."
)
EXPLAIN_USER = (
    "PROBLEM:\n{problem}\n\nFLAGGED FIGURES:\n{items}\n\n"
    "Return JSON: {{\"explanations\": [{{\"index\": int, \"derivable\": bool, "
    "\"inputs_grounded\": [{{\"name\": str, \"value\": number, \"source_quote\": str}}], "
    "\"inputs_assumed\": [{{\"name\": str, \"value\": number, \"why\": str}}], "
    "\"expr\": str, \"result\": number}}]}}"
)


def _items_block(specifics):
    return "\n".join(f"{i}. \"{s.get('text','')}\" — {s.get('claim','')} (value {s.get('value')})"
                     for i, s in enumerate(specifics))


# ---------------------------------------------------------------------- model passes (cached)
def enumerate_specifics(pid, problem, rec):
    uid = f"bg_enum__{pid}"
    c = R.load(uid)
    if not c:
        out = L.claude_json(R.CLAUDE, ENUM_SYS, ENUM_USER.format(problem=problem, rec=rec), max_tokens=3500)
        sp = out.get("specifics", []) if isinstance(out, dict) else []
        c = {"specifics": sp[:40]}
        R.save(uid, c)
    return c["specifics"]


def present_labels(pid, vendor, rec, specifics):
    """Presentation labels from a given vendor over the canonical list. (v3: precision-hedge != basis-flag,
    + calibration examples to lift cross-vendor agreement.)"""
    uid = f"bg_pres3__{vendor}__{pid}"
    c = R.load(uid)
    if not c:
        items = _items_block(specifics)
        if vendor == "claude":
            out = L.claude_json(R.CLAUDE, PRESENT_SYS, PRESENT_USER.format(rec=rec, items=items), max_tokens=2000)
        else:
            out = L.gpt_json(R.GPT, PRESENT_SYS, PRESENT_USER.format(rec=rec, items=items))
        labels = out.get("labels", []) if isinstance(out, dict) else []
        c = {"labels": {int(x["index"]): str(x.get("presented_as", "definitive")).lower()
                        for x in labels if isinstance(x, dict) and "index" in x}}
        R.save(uid, c)
    return {int(k): v for k, v in c["labels"].items()}


def explain_flags(pid, problem, flagged):
    """Targeted re-ask over the bucket-three flags: derive each or name the input(s) it must assume.
    `flagged` = {orig_index: spec}. Returns {orig_index: explanation}. Cached per rec."""
    uid = f"bg_explain__{pid}"
    c = R.load(uid)
    if not c:
        items = "\n".join(f"{i}. \"{s.get('text','')}\" — {s.get('claim','')} (value {s.get('value')})"
                          for i, s in flagged.items())
        out = L.claude_json(R.CLAUDE, EXPLAIN_SYS, EXPLAIN_USER.format(problem=problem, items=items), max_tokens=3000)
        exps = out.get("explanations", []) if isinstance(out, dict) else []
        c = {"explanations": {int(e["index"]): e for e in exps if isinstance(e, dict) and "index" in e}}
        R.save(uid, c)
    return {int(k): v for k, v in c["explanations"].items()}


def verify_explanation(e, spec, problem_text, date_spans):
    """Adjudicate a re-ask explanation: is the arithmetic sound, is it FULLY grounded in the problem, and
    if not, which inputs are ungrounded (rider text). Claimed-grounded inputs whose quote isn't actually
    in the problem are demoted to ungrounded — the model doesn't get to assert grounding."""
    env, pnorm = {}, _norm(problem_text)
    ungrounded = []
    for it in (e.get("inputs_grounded") or []):
        if not isinstance(it, dict):
            continue
        n, v, q = it.get("name"), it.get("value"), it.get("source_quote", "")
        if not n or not isinstance(v, (int, float)) or isinstance(v, bool):
            continue
        env[n] = v
        if _norm(q) not in pnorm and not _in_spans(v, date_spans):
            ungrounded.append(f"{n} (claimed from problem but not found)")
    for it in (e.get("inputs_assumed") or []):
        if not isinstance(it, dict):
            continue
        n, v, w = it.get("name"), it.get("value"), it.get("why", "")
        if n and isinstance(v, (int, float)) and not isinstance(v, bool):
            env[n] = v
            ungrounded.append(f"{n} — {w}" if w else n)
    computed, _, _, err = safe_eval_named(e.get("expr", ""), env)
    sound = (computed is not None) and (not err) and _matches_target(computed, spec)
    return {"sound": sound, "fully_grounded": sound and not ungrounded, "ungrounded": ungrounded,
            "computed": round(computed, 4) if computed is not None else None}


def kind_labels(pid, rec, specifics):
    """Classify each specific descriptive (a factual/predictive claim, gate-relevant) vs prescriptive
    (the recommendation's own proposed action — a choice, not a claim that can be false)."""
    uid = f"bg_kind__{pid}"
    c = R.load(uid)
    if not c:
        items = _items_block(specifics)
        out = L.claude_json(R.CLAUDE, KIND_SYS, KIND_USER.format(rec=rec, items=items), max_tokens=2000)
        ks = out.get("kinds", []) if isinstance(out, dict) else []
        c = {"kinds": {int(x["index"]): str(x.get("kind", "descriptive")).lower()
                       for x in ks if isinstance(x, dict) and "index" in x}}
        R.save(uid, c)
    return {int(k): v for k, v in c["kinds"].items()}


def trace(pid, vendor, problem, specifics):
    uid = f"bg_trace__{vendor}__{pid}"
    c = R.load(uid)
    if not c:
        items = _items_block(specifics)
        if vendor == "claude":
            out = L.claude_json(R.CLAUDE, TRACE_SYS, TRACE_USER.format(problem=problem, items=items), max_tokens=4000)
        else:
            out = L.gpt_json(R.GPT, TRACE_SYS, TRACE_USER.format(problem=problem, items=items))
        ders = out.get("derivations", []) if isinstance(out, dict) else []
        c = {"derivations": [d for d in ders if isinstance(d, dict)]}
        R.save(uid, c)
    return {int(d["index"]): d for d in c["derivations"] if "index" in d}


# ---------------------------------------------------------------------- calculator adjudication (Python)
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def problem_date_spans(problem):
    """Day-counts derivable from date ranges stated in the problem — so a figure like '36' that is the
    span of 'Nov 15–Dec 20' counts as traceable (the checker can't otherwise do calendar arithmetic).
    Pairs consecutive month/day tokens; records both the inclusive and exclusive span."""
    toks = re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})", (problem or "").lower())
    dates = []
    for mon, day in toks:
        try:
            dates.append((_MONTHS[mon[:3]], int(day)))
        except (KeyError, ValueError):
            continue
    spans = set()
    for (m1, d1), (m2, d2) in zip(dates, dates[1:]):
        y2 = 2025 if (m2, d2) >= (m1, d1) else 2026          # handle a Dec->Jan wrap
        try:
            delta = (datetime.date(y2, m2, d2) - datetime.date(2025, m1, d1)).days
        except ValueError:
            continue
        if 0 < delta < 400:
            spans.add(delta); spans.add(delta + 1)           # exclusive and inclusive counts
    return spans


def _in_spans(value, spans):
    return isinstance(value, (int, float)) and any(abs(value - s) < 0.5 for s in spans)


def _scaled_range(text, value):
    """If the specific's text states a numeric range (e.g. '17-19 MW', '$53M-$75M'), return it scaled to
    the value's magnitude (the enumerator records the midpoint as the value, so factor = value/midpoint).
    Lets a derived figure be checked against the stated RANGE rather than a single midpoint."""
    if not isinstance(value, (int, float)):
        return None
    m = re.search(r"(\d[\d,]*\.?\d*)\s*(?:-|–|—|to)\s*(\d[\d,]*\.?\d*)", text or "")
    if not m:
        return None
    try:
        lo, hi = sorted((float(m.group(1).replace(",", "")), float(m.group(2).replace(",", ""))))
    except ValueError:
        return None
    mid = (lo + hi) / 2
    if mid == 0 or hi / max(lo, 1e-9) > 5:                   # skip implausibly wide ranges (too vague to credit)
        return None
    factor = value / mid if mid else 1.0
    return (lo * factor, hi * factor)


def _matches_target(computed, spec):
    """Compare a computed value to the specific: to its stated RANGE if it has one (±tol), else to its
    point value (±tol)."""
    value = spec.get("value")
    rng = _scaled_range(spec.get("text", ""), value)
    if rng:
        lo, hi = rng
        return lo * (1 - REL_TOL) <= computed <= hi * (1 + REL_TOL)
    return isinstance(value, (int, float)) and _close(computed, value)


def derivation_verifies(d, spec, problem_text, date_spans):
    """A proposed derivation counts ONLY if every input is grounded in the problem (quoted verbatim, or a
    calendar span of problem dates) AND the arithmetic reproduces the specific's value/range. Model
    proposes; calculator decides."""
    if not d or not d.get("derivable"):
        return False
    inputs = d.get("inputs", [])
    if not isinstance(inputs, list) or not inputs:
        return False
    env, pnorm = {}, _norm(problem_text)
    for it in inputs:
        if not isinstance(it, dict):
            return False
        name, val, q = it.get("name"), it.get("value"), it.get("source_quote", "")
        if not name or not isinstance(val, (int, float)) or isinstance(val, bool):
            return False
        # grounded if the quote is in the problem OR the value is a calendar span of problem dates
        if _norm(q) not in pnorm and not _in_spans(val, date_spans):
            return False
        env[name] = val
    computed, _, _, err = safe_eval_named(d.get("expr", ""), env)
    return (computed is not None) and (not err) and _matches_target(computed, spec)


def bucket_for(idx, spec, problem_text, pres_by_vendor, trace_by_vendor, kind, date_spans):
    value = spec.get("value")
    # traceable: value echoed verbatim as a problem number, is a calendar span of problem dates,
    # OR any vendor's derivation verifies (range-aware)
    echoed = isinstance(value, (int, float)) and (_number_in_text(value, problem_text) or _in_spans(value, date_spans))
    ver_by = {v: derivation_verifies(trace_by_vendor[v].get(idx), spec, problem_text, date_spans) for v in trace_by_vendor}
    traceable = echoed or any(ver_by.values())
    # presentation consensus across the two vendors. Escalate a genuine SPLIT rather than auto-deciding:
    # both-contextualized = marked (pass); both-definitive + untraceable = fail; split = route to review.
    pres = {v: pres_by_vendor[v].get(idx, "definitive") for v in pres_by_vendor}
    both_ctx = all(p == "contextualized" for p in pres.values())
    any_ctx = any(p == "contextualized" for p in pres.values())
    split = any_ctx and not both_ctx
    if kind == "prescriptive":
        b = "prescriptive"          # a proposed action, not a factual claim -> out of the gate's scope
    elif traceable:
        b = "traceable"
    elif both_ctx:
        b = "contextualized"        # both vendors agree it's flagged as an estimate
    elif split:
        b = "REVIEW_SPLIT"          # vendors disagree on whether it's stated as fact -> escalate
    else:
        b = "BUCKET3_FAIL"          # both call it definitive, and it's untraceable
    return {"index": idx, "text": spec.get("text"), "value": value, "claim": spec.get("claim"),
            "bucket": b, "kind": kind, "echoed": echoed, "traceable": traceable, "verified_by": ver_by,
            "presented_as": pres, "contextualized": both_ctx, "presentation_split": split}


def per_vendor_bucket(idx, spec, problem_text, pres_v, trace_v, kind, date_spans):
    """How ONE vendor alone would bucket the specific (for detector-agreement reporting)."""
    if kind == "prescriptive":
        return "prescriptive"
    value = spec.get("value")
    echoed = isinstance(value, (int, float)) and (_number_in_text(value, problem_text) or _in_spans(value, date_spans))
    traceable = echoed or derivation_verifies(trace_v.get(idx), spec, problem_text, date_spans)
    contextualized = pres_v.get(idx, "definitive") == "contextualized"
    return "contextualized" if contextualized else ("traceable" if traceable else "BUCKET3_FAIL")


def run_problem(pid, problem, rec):
    specifics = enumerate_specifics(pid, problem, rec)
    # presentation judged by BOTH vendors with the sharpened test (precision hedge != basis flag);
    # the enumerator's inline presented_as is not used for bucketing.
    pres_by = {v: present_labels(pid, v, rec, specifics) for v in ("claude", "gpt")}
    trace_by = {v: trace(pid, v, problem, specifics) for v in ("claude", "gpt")}
    kinds = kind_labels(pid, rec, specifics)
    date_spans = problem_date_spans(problem)
    rows = [bucket_for(i, s, problem, pres_by, trace_by, kinds.get(i, "descriptive"), date_spans)
            for i, s in enumerate(specifics)]
    # per-vendor bucketing for detector agreement
    pv = {v: [per_vendor_bucket(i, s, problem, pres_by[v], trace_by[v], kinds.get(i, "descriptive"), date_spans)
              for i, s in enumerate(specifics)]
          for v in ("claude", "gpt")}
    # targeted re-ask on each flag: recover a genuinely-missed derivation, else name the assumed input
    # (rider text). Only fully-problem-grounded, arithmetic-sound derivations are recovered to traceable;
    # a figure that only derives via an unstated assumption stays flagged, now WITH the reason.
    # re-ask runs on both hard fails and split-for-review (both are untraceable + flagged); a recovered
    # derivation resolves either.
    flagged = {i: specifics[i] for i, r in enumerate(rows) if r["bucket"] in ("BUCKET3_FAIL", "REVIEW_SPLIT")}
    recovered = 0
    if flagged:
        exps = explain_flags(pid, problem, flagged)
        for i in flagged:
            split_note = "vendors split on whether this is stated as fact vs an estimate" if rows[i]["bucket"] == "REVIEW_SPLIT" else ""
            e = exps.get(i)
            if not e:
                rows[i]["reason"] = split_note or "no explanation offered on re-ask"
                continue
            v = verify_explanation(e, specifics[i], problem, date_spans)
            if v["fully_grounded"]:
                rows[i]["bucket"] = "traceable"; rows[i]["recovered_on_reask"] = True; recovered += 1
            elif v["sound"] and v["ungrounded"]:
                detail = "rests on unstated input(s): " + "; ".join(v["ungrounded"])
                rows[i]["reason"] = (split_note + "; " + detail) if split_note else detail
                rows[i]["rider"] = "Assumes " + "; ".join(v["ungrounded"]) + " — not in the problem; verify."
            else:
                rows[i]["reason"] = split_note or "no problem-grounded derivation found on re-ask"
    fails = [r for r in rows if r["bucket"] == "BUCKET3_FAIL"]
    splits = [r for r in rows if r["bucket"] == "REVIEW_SPLIT"]
    verdict = "FAIL" if fails else ("REVIEW" if splits else "PASS")
    return {"pid": pid, "n_specifics": len(specifics), "rows": rows, "recovered_on_reask": recovered,
            "per_vendor_buckets": pv, "n_bucket3": len(fails), "bucket3": fails,
            "n_review_split": len(splits), "review_split": splits, "answer_verdict": verdict}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["step2", "R0", "plain"], default="step2")
    args = ap.parse_args()
    corpus = {p["id"]: p for p in json.loads(CORPUS.read_text())["problems"]}

    def rec_for(pid):
        if args.source == "R0":
            return corpus[pid]["R0"]
        if args.source == "plain":
            c = R.load(f"swf_plain__{pid}"); return (c["recommendation"] if c else corpus[pid]["R0"])
        c = R.load(f"s2_rev__{pid}__r3"); return (c.get("revised_recommendation") if c else "") or corpus[pid]["R0"]

    recs = {pid: rec_for(pid) for pid in corpus}
    print(f"[bg] correctness gate on {len(recs)} recommendations ({args.source})", flush=True)

    out = {}
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(run_problem, pid, corpus[pid]["problem"], recs[pid]): pid for pid in recs}
        for f in cf.as_completed(futs):
            try:
                r = f.result(); out[r["pid"]] = r
            except Exception as e:   # noqa: BLE001
                print(f"[bg] ERROR {futs[f]}: {repr(e)[:160]}", flush=True)

    # aggregate + detector cross-vendor agreement
    tot_spec = tot_fail = tot_recovered = tot_split = 0
    bucket_ct = collections.Counter()
    pres_agree = pres_tot = 0
    vbucket_agree = vbucket_tot = 0
    both_fail = claude_fail = gpt_fail = 0
    per = []
    for pid in corpus:
        r = out.get(pid)
        if not r:
            continue
        tot_spec += r["n_specifics"]; tot_fail += r["n_bucket3"]; tot_recovered += r.get("recovered_on_reask", 0)
        tot_split += r.get("n_review_split", 0)
        for row in r["rows"]:
            bucket_ct[row["bucket"]] += 1
            pc, pg = row["presented_as"]["claude"], row["presented_as"]["gpt"]
            pres_tot += 1; pres_agree += int(pc == pg)
        cb, gb = r["per_vendor_buckets"]["claude"], r["per_vendor_buckets"]["gpt"]
        for i in range(len(cb)):
            vbucket_tot += 1
            vbucket_agree += int(cb[i] == gb[i])
            cf3, gf3 = cb[i] == "BUCKET3_FAIL", gb[i] == "BUCKET3_FAIL"
            both_fail += int(cf3 and gf3); claude_fail += int(cf3); gpt_fail += int(gf3)
        per.append({"pid": pid, "domain": corpus[pid]["domain"], "n": r["n_specifics"],
                    "bucket3": r["n_bucket3"], "review_split": r.get("n_review_split", 0),
                    "verdict": r["answer_verdict"]})

    summary = {
        "EXPLORATORY": True, "source": args.source, "n_problems": len(per),
        "totals": {"specifics": tot_spec, **dict(bucket_ct), "bucket3_failures": tot_fail,
                   "review_splits": tot_split},
        "recovered_on_reask": tot_recovered,
        "answers_failing_gate": sum(1 for p in per if p["verdict"] == "FAIL"),
        "answers_needing_review": sum(1 for p in per if p["verdict"] == "REVIEW"),
        "detector_cross_vendor": {
            "presentation_agreement": f"{pres_agree}/{pres_tot}"
                                      + (f" ({round(100*pres_agree/pres_tot,1)}%)" if pres_tot else ""),
            "full_bucket_agreement": f"{vbucket_agree}/{vbucket_tot}"
                                     + (f" ({round(100*vbucket_agree/vbucket_tot,1)}%)" if vbucket_tot else ""),
            "bucket3_by_vendor": {"claude_alone": claude_fail, "gpt_alone": gpt_fail, "both": both_fail},
            "note": "combined verdict is the CONSERVATIVE intersection: a specific fails only if unmarked "
                    "by both vendors AND traceable by neither.",
        },
        "per_problem": per, "detail": out,
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== CORRECTNESS GATE — bucket-three detection ===")
    print(f"  source: {args.source}   problems: {len(per)}   hard specifics: {tot_spec}")
    print(f"  buckets: traceable={bucket_ct['traceable']}  contextualized={bucket_ct['contextualized']}  "
          f"prescriptive(out-of-scope)={bucket_ct['prescriptive']}  REVIEW_SPLIT={bucket_ct['REVIEW_SPLIT']}  "
          f"BUCKET3_FAIL={bucket_ct['BUCKET3_FAIL']}")
    print(f"  recovered on re-ask (fully re-derived from givens): {tot_recovered}")
    print(f"  answers: FAIL {summary['answers_failing_gate']}/{len(per)}  ·  REVIEW {summary['answers_needing_review']}/{len(per)}  ·  PASS {sum(1 for p in per if p['verdict']=='PASS')}/{len(per)}")
    print(f"\n  detector cross-vendor agreement:")
    print(f"    presentation (definitive vs contextualized): {summary['detector_cross_vendor']['presentation_agreement']}")
    print(f"    full 3-way bucket:                            {summary['detector_cross_vendor']['full_bucket_agreement']}")
    print(f"    bucket-3 flags — claude {claude_fail}, gpt {gpt_fail}, both {both_fail} (combined uses the conservative union of traceability, intersection of 'definitive')")
    print(f"\n  {'id':22s} {'domain':26s} {'spec':>4s} {'FAIL':>4s} {'SPLIT':>5s} verdict")
    for p in per:
        print(f"  {p['pid']:22s} {p['domain'][:26]:26s} {p['n']:4d} {p['bucket3']:4d} {p['review_split']:5d} {p['verdict']}")
    print("\n  BUCKET-THREE FAILURES (unmarked, not traceable to the given facts):")
    any_fail = False
    for pid in corpus:
        r = out.get(pid)
        if not r or not r["bucket3"]:
            continue
        any_fail = True
        for b in r["bucket3"]:
            print(f"    {pid}: \"{b['text']}\" — {(b['claim'] or '')[:56]}  (value {b['value']})")
            if b.get("reason"):
                print(f"        └ {b['reason']}")
    if not any_fail:
        print("    (none)")
    splits_any = [(pid, b) for pid in corpus if out.get(pid) for b in out[pid].get("review_split", [])]
    if splits_any:
        print("\n  REVIEW — vendors split on whether stated as fact (route to rider/human):")
        for pid, b in splits_any:
            print(f"    {pid}: \"{b['text']}\" — {(b['claim'] or '')[:52]}  (claude={b['presented_as']['claude']}, gpt={b['presented_as']['gpt']})")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
