#!/usr/bin/env python3
"""Numeric-consistency gate — option (b): harden the coherence gate against the warehouse class.

The textual coherence gate (coherence_gate.py) catches EXPLICIT self-contradiction (capex 5/5) but
MISSED warehouse: "build ~3 months ahead" vs a stated "~11-month build time" => the second DC arrives
~8 months late. That's a LATENT ARITHMETIC inconsistency — the numbers are stated but never juxtaposed,
so it needs quantitative inference, not clause-vs-clause reading.

This peer auditor is problem-BLIND like the textual gate, but its sole job is: do the document's OWN
stated quantities (timelines, rates, counts, comparisons) actually support the conclusion it draws from
them? Same discipline — flag only what's provable from numbers IN the text, never missing data or
debatable estimates. Same risk to watch: widening the mandate to "checking math" can re-introduce the
R5 over-flag. So the bar is unchanged: catch warehouse AND keep false-flag ~0 on the 56 coherent docs.

Writes its own runs (numgate__*) and analysis/numeric-gate.json; the textual gate's cache/result are
left intact. combine_gates.py unions the two. Resumable + parallel. Claude-only.

Usage: python3 numeric_gate.py [--k 5] [--vote N]
Env: ANTHROPIC_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L

K_DEFAULT = 5
MANIFEST = R.PILOT / "analysis" / "positive-control-set.json"
OUT_JSON = R.PILOT / "analysis" / "numeric-gate.json"
INTERNAL_CONTRADICTION = {"P-capex-automation", "P-warehouse-siting"}

NUMERIC_SYS = (
    "You are a quantitative-consistency auditor. You are given ONE recommendation and NOTHING about the "
    "problem it answers. Check ONLY whether the document's OWN stated numbers are self-consistent: do the "
    "timelines, durations, rates, counts, thresholds, and comparisons it states actually support the "
    "conclusion it draws from them, or do they (when you do the arithmetic) undercut or contradict it? "
    "Example failure: it says a build takes 11 months and that it will start 3 months before the deadline, "
    "then concludes it will be ready in time — the arithmetic (3 < 11) says it arrives 8 months late. "
    "Flag INCONSISTENT only when you can derive the contradiction FROM NUMBERS STATED IN THE TEXT. Do NOT "
    "flag missing numbers, estimates you'd need outside data to check, rounding, or merely debatable "
    "assumptions. If the stated quantities are mutually consistent with the conclusion, it is CONSISTENT "
    "even if you suspect the answer is wrong on the merits. When unsure, return CONSISTENT — a false alarm "
    "sends a good answer back for a needless rewrite."
)
NUMERIC_USER = (
    "RECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"consistent\": true|false, \"defect\": str}} — if consistent is false, set \"defect\" "
    "to the specific numeric inconsistency (quote the numbers and show the arithmetic), else \"\"."
)


def leaf(pair, side, j):
    uid = f"numgate__{side}__{pair['pair_id']}__rep{j}"
    if R.load(uid):
        return
    text = pair["text_a"] if side == "A" else pair["text_b"]
    out = L.claude_json(R.CLAUDE, NUMERIC_SYS, NUMERIC_USER.format(rec=text), max_tokens=1200)
    consistent = bool(out.get("consistent", True)) if isinstance(out, dict) else True
    defect = (out.get("defect", "") or "") if isinstance(out, dict) else ""
    R.save(uid, {"pair_id": pair["pair_id"], "side": side, "rep": j,
                 "consistent": consistent, "defect": defect[:400]})


def verdict(pair, side, k, min_inc):
    votes, defects = [], []
    for j in range(1, k + 1):
        rec = R.load(f"numgate__{side}__{pair['pair_id']}__rep{j}")
        if not rec:
            return None
        votes.append(rec["consistent"])
        if not rec["consistent"] and rec["defect"]:
            defects.append(rec["defect"])
    n_bad = sum(1 for v in votes if not v)
    return {"flagged": n_bad >= min_inc, "bad_votes": n_bad, "defect": (defects[0] if defects else "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--vote", type=int, default=None)
    args = ap.parse_args()
    k = args.k
    min_inc = args.vote if args.vote is not None else (k // 2 + 1)

    pairs = json.loads(MANIFEST.read_text())["pairs"]
    print(f"[num] {len(pairs)} pairs; both sides; k={k}; flag-if>={min_inc}/{k}", flush=True)
    jobs = [(leaf, (pair, side, j)) for pair in pairs for side in ("A", "B") for j in range(1, k + 1)]
    print(f"[num] {len(jobs)} leaf calls (resumable)", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(fn, *a): a[0]["pair_id"] for (fn, a) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[num] ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
            done += 1
            if done % 40 == 0:
                print(f"[num] {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[num] {errs} errors -- re-run to retry.", flush=True)

    docs, incomplete = [], 0
    for pair in pairs:
        for side in ("A", "B"):
            v = verdict(pair, side, k, min_inc)
            if v is None:
                incomplete += 1
                continue
            typ = pair["type"]; pid = pair["pair_id"].split("__")[0]
            if side == "A":
                role, expect = "original", "coherent"
            elif typ == "planted_regression":
                role = "regression(internal)" if pid in INTERNAL_CONTRADICTION else "regression(constraint)"
                expect = "incoherent" if pid in INTERNAL_CONTRADICTION else "coherent"
            else:
                role, expect = f"revision({typ})", "coherent"
            docs.append({"pair_id": pair["pair_id"], "pid": pid, "type": typ, "side": side,
                         "role": role, "expect": expect, "flagged": v["flagged"],
                         "bad_votes": v["bad_votes"], "defect": v["defect"]})

    genuine = [d for d in docs if d["role"] == "original" or d["role"].startswith("revision(")]
    gflag = [d for d in genuine if d["flagged"]]
    target = [d for d in docs if d["expect"] == "incoherent"]
    summary = {"EXPLORATORY": True, "k": k, "flag_threshold": f">={min_inc}/{k}", "incomplete": incomplete,
               "recall_internal_contradiction": {d["pid"]: d["flagged"] for d in target},
               "false_flag": {"n": len(gflag), "of": len(genuine),
                              "rate": round(len(gflag) / len(genuine), 3) if genuine else None,
                              "which": [{"pid": d["pid"], "role": d["role"], "votes": d["bad_votes"]} for d in gflag]},
               "docs": docs}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== NUMERIC GATE vs POSITIVE CONTROL ===")
    print("  RECALL (internal/latent-arithmetic class):")
    for d in target:
        mark = "CAUGHT" if d["flagged"] else "MISSED"
        print(f"     {d['pid']:24s} {mark}  ({d['bad_votes']}/{k})" + (f'  "{d["defect"][:70]}"' if d["flagged"] else ""))
    ff = summary["false_flag"]
    print(f"\n  FALSE-FLAG on 56 genuinely-coherent docs: {ff['n']}/{ff['of']} = {ff['rate']}")
    for w in ff["which"]:
        print(f"     FALSE FLAG {w['pid']:24s} {w['role']:22s} ({w['votes']}/{k})")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
