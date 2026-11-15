#!/usr/bin/env python3
"""Recount off-key discovery under partial-credit matching.

WHY THIS EXISTS.

  Off-key discovery here is "signal items the matcher never cited for a covered key point",
  divided by everything emitted. The seeded-miss study
  (../seeded-miss-2026-08-29/result.md) showed that rule systematically UNDERCOUNTS: an item
  can raise material beyond the key AND also cover a key point, and the exclusive rule
  discards it for being dual-purpose. On that study's corpus the same defect cost 0.40 of a
  0.95 true rate -- the entire shortfall.

  This script recounts these runs under the corrected rule so the two pilots stop reporting
  off-key under different definitions.

THE PROBLEM WITH JUST RELAXING THE RULE.

  In the seeded-miss study there was a TARGET (the seed), so "does any item address it" was
  a well-posed question with a decoy control. Here there is no target: off-key is a residual.
  Simply counting every signal item as off-key would return the yield, which measures
  nothing new.

  So the recount asks the question the exclusive rule was standing in for:

      For a signal item the matcher DID credit to a key point, does that item raise
      material the key point does not cover?

  If yes, the item carries ungraded material and belongs in off-key even though it also
  covers graded material. If no, the exclusive rule was right to drop it.

THE PASS COULD BE GENEROUS, SO IT IS FALSIFIED RATHER THAN TRUSTED.

  "Does this carry anything beyond?" invites yes. Two guards:

    Pass E (claude) must NAME the beyond-key material in a short phrase, not merely assert
    it. An unstated claim is not counted.
    Pass F (gpt -- different vendor, and the same vendor that built the original match) then
    takes those phrases WITHOUT knowing which item they came from and asks whether each one
    matches a key point after all. Any phrase it matches is struck.

  So a claim survives only if one model can name the extra material and a second, looking at
  the key alone, agrees it is not on the key. This is the same discipline as the leakage
  audit's verbatim-quote requirement: a claim that cannot be checked does not count.

REPORTED SIDE BY SIDE, never in place of. The exclusive figure is what the study published.

Usage:
  ./recount_offkey.py --admin "July 2020" --subject "Secured Transactions" [--rungs g1,g3,g4]
"""
import argparse, glob, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))

from score_pair import pass_a, pass_b, majority, norm_id, GPT, CLAUDE  # noqa: E402
from lib_llm import gpt_json, claude_json  # noqa: E402

RUNGS_DESC = {
    "g1": "gpt-5.2, natural", "g1n": "gpt-5.2, ~55-item budget",
    "g3": "claude-opus-4-8, natural", "g3n": "claude-opus-4-8, ~55-item budget",
    "g4": "structured walk, REAL map", "g4collapse": "structured walk, COLLAPSED map",
    "g4relabel": "structured walk, RELABELLED map",
}

# ------------------------------------------------------------------- Pass E: beyond-key

PASS_E_SYS = """You are examining issue-spotting items that have already been matched to
points in an examiner's answer key.

For each item you are given the item and the key point(s) a matcher credited it with
covering. Decide ONE thing:

  beyond - does this item raise a question that the matched key point(s) do NOT cover?

Say true only when the item carries real additional substance: a distinct legal question, a
further element, a separate party or transaction, a consequence the key point does not
reach. Say false when the item is the key point restated, narrowed, broadened, or expressed
in different words -- that is the same question, not extra material.

If beyond is true you MUST name the extra material in a short phrase (<=12 words) stating
the additional question itself, not why it is interesting. A claim you cannot state is not
a claim; set beyond=false instead.

Return JSON:
{"items":[{"i":<index>,"beyond":true|false,"beyond_what":"<phrase or empty>"}]}
Every item must appear exactly once."""


def pass_e(items, matched_map, fact, k, model):
    """matched_map: {item_index: [key point texts]}. Returns k replicate dicts."""
    lines = []
    for i in sorted(matched_map):
        pts = "; ".join(matched_map[i])
        lines.append(f"[{i}] ITEM: {items[i]}\n     MATCHED KEY POINT(S): {pts}")
    user = f"FACT PATTERN\n{fact}\n\nITEMS AND THEIR MATCHED KEY POINTS\n" + "\n".join(lines)
    reps = []
    for _ in range(k):
        out = (gpt_json(model, PASS_E_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_E_SYS, user, max_tokens=4000))
        rep = {}
        for it in out.get("items", []):
            try:
                idx = int(it["i"])
            except (KeyError, TypeError, ValueError):
                continue
            rep[idx] = {"beyond": bool(it.get("beyond")),
                        "beyond_what": str(it.get("beyond_what") or "").strip()}
        reps.append(rep)
    return reps


# ------------------------------------------------------- Pass F: falsify the beyond claims

PASS_F_SYS = """You are checking whether each of several described legal questions is already
covered by an examiner's answer key.

You are given the answer key and a numbered list of described questions. The descriptions
come from mixed sources and you are not told anything about where they came from.

For each description decide:

  on_key - does the answer key already contain a point that puts this question in play?
           Wording will differ; judge substance. A key point stated more broadly still
           counts if it covers the described question.

Return JSON:
{"checks":[{"n":<number>,"on_key":true|false,"key_id":"<the key point id, or empty>"}]}
Every description must appear exactly once."""


def pass_f(phrases, gold, k, model):
    """phrases: list of strings. Returns per-index majority on_key verdict."""
    if not phrases:
        return {}
    key = "\n".join(f"{g['point_id']} ({g['weight_pct']}%): {g['issue'] or g['point']}"
                    for g in gold)
    desc = "\n".join(f"{n}. {p}" for n, p in enumerate(phrases))
    user = f"EXAMINER KEY POINTS\n{key}\n\nDESCRIBED QUESTIONS\n{desc}"
    reps = []
    for _ in range(k):
        out = (gpt_json(model, PASS_F_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_F_SYS, user, max_tokens=3000))
        rep = {}
        for c in out.get("checks", []):
            try:
                rep[int(c["n"])] = bool(c.get("on_key"))
            except (KeyError, TypeError, ValueError):
                continue
        reps.append(rep)
    verdict = {}
    for n in range(len(phrases)):
        vals = [r[n] for r in reps if n in r]
        verdict[n] = (sum(vals) * 2 >= len(vals)) if vals else False
    return verdict


# ------------------------------------------------------------------------------ scoring

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def recount_run(run, fact, k, match_model, audit_model, beyond_model):
    items = [i["label"] for i in run["raw"]["issues"]]
    gold = run["gold"]["gold"]
    if not items:
        return None
    A = pass_a(items, gold, k, match_model)
    B = pass_b(items, fact, k, audit_model)

    covered, cites, per_item_points = {}, {}, {}
    for g in gold:
        covered[g["point_id"]] = bool(majority(A, norm_id(g["point_id"]), "covered")[0])
    gold_by_norm = {norm_id(g["point_id"]): g for g in gold}
    for rep in A:
        for kid, m in rep.items():
            if m["covered"]:
                for i in m["by"]:
                    cites[i] = cites.get(i, 0) + 1
                    per_item_points.setdefault(i, set()).add(kid)
    key_matched = {i for i, c in cites.items() if c * 2 >= len(A)}

    signal = set()
    for i in range(len(items)):
        s, _ = majority(B, i, "sound")
        r, _ = majority(B, i, "raised")
        m, _ = majority(B, i, "material")
        dup = sum(1 for rep in B
                  if i in rep and rep[i].get("duplicate_of") is not None) * 2 >= len(B)
        if s and r and m and not dup:
            signal.add(i)

    offkey_exclusive = signal - key_matched

    # ---- the recount: which key-matched signal items carry material beyond their points?
    to_test = sorted(signal & key_matched)
    matched_map = {}
    for i in to_test:
        pts = []
        for kid in per_item_points.get(i, ()):
            g = gold_by_norm.get(kid)
            if g:
                pts.append(f"{g['point_id']}: {g['issue'] or g['point']}")
        matched_map[i] = pts or ["(unspecified)"]

    beyond_claims, extra = {}, set()
    if matched_map:
        E = pass_e(items, matched_map, fact, k, beyond_model)
        for i in to_test:
            vals = [r[i]["beyond"] for r in E if i in r]
            if not vals or sum(vals) * 2 < len(vals):
                continue
            phrase = next((r[i]["beyond_what"] for r in E
                           if i in r and r[i]["beyond"] and r[i]["beyond_what"]), "")
            if phrase:                      # an unstated claim is not a claim
                beyond_claims[i] = phrase
        if beyond_claims:
            idxs = sorted(beyond_claims)
            phrases = [beyond_claims[i] for i in idxs]
            # Pass F is the SAME vendor that built the original match, and it never learns
            # which item a phrase came from.
            on_key = pass_f(phrases, gold, k, match_model)
            for n, i in enumerate(idxs):
                if not on_key.get(n, False):
                    extra.add(i)

    offkey_partial = offkey_exclusive | extra
    E_n = len(items)
    return {
        "emitted": E_n, "signal": len(signal), "key_matched": len(key_matched),
        "offkey_exclusive": len(offkey_exclusive),
        "offkey_exclusive_rate": len(offkey_exclusive) / E_n,
        "tested_dual_purpose": len(to_test),
        "beyond_claimed": len(beyond_claims),
        "beyond_struck_by_pass_f": len(beyond_claims) - len(extra),
        "beyond_upheld": len(extra),
        "offkey_partial": len(offkey_partial),
        "offkey_partial_rate": len(offkey_partial) / E_n,
        "yield": len(signal) / E_n,
        "weighted_recall": sum(g["weight_pct"] for g in gold
                               if covered[g["point_id"]]) / 100.0,
        "beyond_phrases": {str(i): beyond_claims[i] for i in sorted(extra)},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admin", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--rungs", default="g1,g1n,g3,g3n,g4,g4collapse,g4relabel")
    ap.add_argument("-k", type=int, default=2)
    ap.add_argument("--match-model", default=GPT)
    ap.add_argument("--audit-model", default=CLAUDE)
    ap.add_argument("--beyond-model", default=CLAUDE)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    qs = json.load(open(os.path.join(HERE, "..", "corpus", "questions.json")))["questions"]
    q = next(x for x in qs if x["administration"] == a.admin and x["subject"] == a.subject)
    fact, base = q["text"], f"{slug(a.admin)}-{slug(a.subject)}"

    out_path = a.out or os.path.join(HERE, "..", "runs", f"{base}.offkey-recount.json")
    cache = json.load(open(out_path))["per_run"] if os.path.exists(out_path) else {}

    print(f"fact pattern : {a.admin} / {a.subject}")
    print(f"matcher {a.match_model}   blind judge {a.audit_model}   "
          f"beyond {a.beyond_model}   k={a.k}")
    print("recount: off-key under EXCLUSIVE match (as published) vs PARTIAL credit\n")

    results = {}
    for rung in a.rungs.split(","):
        paths = [p for p in sorted(glob.glob(os.path.join(HERE, "..", "runs",
                                                          f"{base}.{rung}.r*.json")))
                 if "raw" in json.load(open(p))]
        if not paths:
            continue
        rows = []
        for p in paths:
            rid = os.path.basename(p)[:-5]
            if rid in cache:
                rows.append(cache[rid])
                continue
            try:
                r = recount_run(json.load(open(p)), fact, a.k, a.match_model,
                                a.audit_model, a.beyond_model)
            except Exception as e:  # noqa: BLE001
                print(f"  {rid} ERROR {str(e)[:70]}")
                continue
            if not r:
                continue
            r["run"] = rid
            cache[rid] = r
            rows.append(r)
            json.dump({"fact_pattern": f"{a.admin} / {a.subject}", "k": a.k,
                       "per_run": cache}, open(out_path, "w"), indent=2)
            print(f"  {rid:<52} offkey {r['offkey_exclusive_rate']:.2f} -> "
                  f"{r['offkey_partial_rate']:.2f}   "
                  f"(+{r['beyond_upheld']} upheld, {r['beyond_struck_by_pass_f']} struck)",
                  flush=True)
        if rows:
            results[rung] = rows

    f = lambda v: statistics.mean(v) if v else float("nan")  # noqa: E731
    print("\n" + "=" * 92)
    print(f"{'rung':<12}{'items':>6}{'yield':>7}{'offkey excl':>13}{'offkey partial':>16}"
          f"{'dual':>6}{'claim':>7}{'struck':>8}   description")
    print("-" * 92)
    for rung, rows in results.items():
        print(f"{rung:<12}{f([r['emitted'] for r in rows]):>6.0f}"
              f"{f([r['yield'] for r in rows]):>7.2f}"
              f"{f([r['offkey_exclusive_rate'] for r in rows]):>13.2f}"
              f"{f([r['offkey_partial_rate'] for r in rows]):>16.2f}"
              f"{f([r['tested_dual_purpose'] for r in rows]):>6.1f}"
              f"{f([r['beyond_claimed'] for r in rows]):>7.1f}"
              f"{f([r['beyond_struck_by_pass_f'] for r in rows]):>8.1f}"
              f"   {RUNGS_DESC.get(rung,'')}")
    print("=" * 92)
    print("offkey excl    = as published: signal items the matcher cited for NO key point")
    print("offkey partial = corrected: plus dual-purpose items whose extra material was")
    print("                 named by one model and confirmed off-key by a second")
    print("dual/claim/struck = items tested / beyond claimed / claims struck by pass F")
    print("\nstruck > 0 is the guard working: pass E over-claimed and pass F caught it.")

    json.dump({"fact_pattern": f"{a.admin} / {a.subject}", "k": a.k,
               "models": {"match": a.match_model, "audit": a.audit_model,
                          "beyond": a.beyond_model},
               "results": {rung: {
                   "n_runs": len(rows),
                   "emitted": f([r["emitted"] for r in rows]),
                   "yield": f([r["yield"] for r in rows]),
                   "offkey_exclusive_rate": f([r["offkey_exclusive_rate"] for r in rows]),
                   "offkey_partial_rate": f([r["offkey_partial_rate"] for r in rows]),
                   "tested_dual_purpose": f([r["tested_dual_purpose"] for r in rows]),
                   "beyond_claimed": f([r["beyond_claimed"] for r in rows]),
                   "beyond_struck": f([r["beyond_struck_by_pass_f"] for r in rows]),
               } for rung, rows in results.items()},
               "per_run": cache}, open(out_path, "w"), indent=2)
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
