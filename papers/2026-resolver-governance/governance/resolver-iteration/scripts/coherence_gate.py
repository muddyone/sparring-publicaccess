#!/usr/bin/env python3
"""Coherence gate validation against the positive-control set (EXPLORATORY).

Bart's architecture: pairwise_raw is the *ruler* (decides which revision is materially better);
a narrow *coherence gate* backstops pairwise's one demonstrated blind spot — the internal
contradiction that makes a revision read CLEANER while breaking its own logic (the capex miss).

The gate is NOT a general regression detector. The bake-off showed pairwise_raw catches all 7
CONSTRAINT-VIOLATION regressions (visible only against the brief) and misses only the 1
INTERNAL-CONTRADICTION regression (capex). So this gate's job is exactly that class:
read ONE recommendation, problem-BLIND, and decide if it contradicts itself / its reasoning fails
to support its own conclusion / its own numbers don't add up. Problem-blind on purpose: it cannot
drift into constraint-judging (pairwise's job) and become another global quality judge.

What success looks like:
  * RECALL on the internal-contradiction class: must FLAG capex; ideally warehouse.
  * FALSE-FLAG rate near zero on the ~56 internally-coherent docs (all 32 originals + the 24
    improvement/identical/cosmetic revisions). High false-flag = R5 over-flag redux (now as
    wasted rewrite loops / non-termination, not wrong output — but still a convergence tax).
  * PASSING the 6 constraint-violation regressions is CORRECT, not a miss (pairwise handles those).

Runs both sides (A=original, B=revision) of all 32 pairs so the 32 clean A-sides are a built-in
false-flag baseline. k reps, majority vote. Resumable + parallel. Claude-only.

Usage:
  python3 coherence_gate.py            # both sides, 32 pairs, k=5
  python3 coherence_gate.py --k 5
  python3 coherence_gate.py --vote 3   # min incoherent votes (of k) to FLAG (default majority)
Env: ANTHROPIC_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L

K_DEFAULT = 5
MANIFEST = R.PILOT / "analysis" / "positive-control-set.json"
OUT_JSON = R.PILOT / "analysis" / "coherence-gate.json"

# The internal-contradiction subset of the planted regressions — the gate's actual recall target.
# (Derived from the control-set change_notes: only these two break the document's OWN logic;
#  the other six violate the external brief and read as self-consistent text.)
INTERNAL_CONTRADICTION = {"P-capex-automation", "P-warehouse-siting"}

COHERENCE_SYS = (
    "You are a consistency auditor. You are given ONE recommendation and NOTHING about the problem it "
    "answers. Judge ONLY its INTERNAL coherence — do not judge whether it is a good or correct answer, "
    "and do not assume any missing context. Flag it as INCOHERENT only if the text itself is "
    "self-defeating, in one of these ways: (a) two claims directly contradict each other; (b) a stated "
    "number, timeline, or comparison does not support — or actively undercuts — the conclusion the text "
    "draws from it; (c) the reasoning given for the recommendation contradicts the recommendation. Do NOT "
    "flag it for being incomplete, terse, debatable, or for anything you'd need outside knowledge to "
    "check. If the document is internally consistent, it is COHERENT even if you suspect it might be "
    "wrong on the merits. When unsure, return COHERENT — a false alarm sends a good answer back for a "
    "needless rewrite."
)
COHERENCE_USER = (
    "RECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"coherent\": true|false, \"contradiction\": str}} — set \"contradiction\" to the "
    "specific self-contradiction (quote the two clauses) if coherent is false, else \"\"."
)


def leaf(pair, side, j):
    uid = f"cohgate__{side}__{pair['pair_id']}__rep{j}"
    if R.load(uid):
        return
    text = pair["text_a"] if side == "A" else pair["text_b"]
    out = L.claude_json(R.CLAUDE, COHERENCE_SYS, COHERENCE_USER.format(rec=text), max_tokens=1200)
    coherent = bool(out.get("coherent", True)) if isinstance(out, dict) else True
    contra = (out.get("contradiction", "") or "") if isinstance(out, dict) else ""
    R.save(uid, {"pair_id": pair["pair_id"], "side": side, "rep": j,
                 "coherent": coherent, "contradiction": contra[:400]})


def verdict(pair, side, k, min_incoherent):
    votes, contras = [], []
    for j in range(1, k + 1):
        rec = R.load(f"cohgate__{side}__{pair['pair_id']}__rep{j}")
        if not rec:
            return None
        votes.append(rec["coherent"])
        if not rec["coherent"] and rec["contradiction"]:
            contras.append(rec["contradiction"])
    n_incoherent = sum(1 for v in votes if not v)
    flagged = n_incoherent >= min_incoherent
    return {"flagged": flagged, "incoherent_votes": n_incoherent, "k": k,
            "contradiction": (contras[0] if contras else "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    ap.add_argument("--vote", type=int, default=None, help="min incoherent votes to FLAG (default ceil(k/2))")
    args = ap.parse_args()
    k = args.k
    min_inc = args.vote if args.vote is not None else (k // 2 + 1)

    manifest = json.loads(MANIFEST.read_text())
    pairs = manifest["pairs"]
    print(f"[gate] {len(pairs)} control pairs; both sides; k={k}; flag-if>={min_inc}/{k} incoherent", flush=True)

    jobs = [(leaf, (pair, side, j)) for pair in pairs for side in ("A", "B") for j in range(1, k + 1)]
    print(f"[gate] {len(jobs)} leaf calls (resumable; cached skipped)", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(fn, *a): a[0]["pair_id"] for (fn, a) in jobs}
        for f in cf.as_completed(futs):
            try:
                f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[gate] ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
            done += 1
            if done % 40 == 0:
                print(f"[gate] {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[gate] {errs} errors -- re-run to retry (resumable).", flush=True)

    # assemble: per (pair, side) flagged/not, then bucket by ground-truth expectation
    # expect-COHERENT set: all 32 A-sides + the B-sides of non-regression pairs (24) = 56 docs.
    # regression B-sides: split into internal-contradiction (recall target) vs constraint-violation (pass=ok).
    incomplete = 0
    docs = []   # {pair_id, type, side, role, expect, flagged, votes, contradiction}
    for pair in pairs:
        for side in ("A", "B"):
            v = verdict(pair, side, k, min_inc)
            if v is None:
                incomplete += 1
                continue
            typ = pair["type"]
            pid_short = pair["pair_id"].split("__")[0]
            if side == "A":
                role, expect = "original", "coherent"
            elif typ == "planted_regression":
                if pid_short in INTERNAL_CONTRADICTION:
                    role, expect = "regression(internal)", "incoherent"   # recall target
                else:
                    role, expect = "regression(constraint)", "coherent"   # pairwise's job; pass=ok
            else:
                role, expect = f"revision({typ})", "coherent"
            docs.append({"pair_id": pair["pair_id"], "pid": pid_short, "type": typ, "side": side,
                         "role": role, "expect": expect, "flagged": v["flagged"],
                         "incoherent_votes": v["incoherent_votes"], "contradiction": v["contradiction"]})

    # metrics
    target = [d for d in docs if d["expect"] == "incoherent"]            # internal-contradiction B-sides
    caught = [d for d in target if d["flagged"]]
    coherent_set = [d for d in docs if d["expect"] == "coherent"]        # the must-not-flag 56
    false_flags = [d for d in coherent_set if d["flagged"]]
    constraint_reg = [d for d in docs if d["role"] == "regression(constraint)"]
    constraint_flagged = [d for d in constraint_reg if d["flagged"]]

    summary = {
        "EXPLORATORY": True, "k": k, "flag_threshold": f">={min_inc}/{k}", "incomplete": incomplete,
        "recall_internal_contradiction": {"caught": len(caught), "of": len(target),
                                          "pairs": {d["pid"]: d["flagged"] for d in target}},
        "false_flag": {"n": len(false_flags), "of": len(coherent_set),
                       "rate": round(len(false_flags) / len(coherent_set), 3) if coherent_set else None,
                       "which": [{"pid": d["pid"], "role": d["role"], "votes": d["incoherent_votes"],
                                  "contradiction": d["contradiction"]} for d in false_flags]},
        "constraint_regressions_flagged_bonus": {"n": len(constraint_flagged), "of": len(constraint_reg),
                                                 "which": [d["pid"] for d in constraint_flagged]},
        "docs": docs,
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== COHERENCE GATE vs POSITIVE CONTROL ===")
    print(f"  RECALL (internal-contradiction class — the gate's job): {len(caught)}/{len(target)} caught")
    for d in target:
        mark = "CAUGHT" if d["flagged"] else "MISSED"
        print(f"     {d['pid']:24s} {mark}  ({d['incoherent_votes']}/{k} incoherent)"
              + (f'  "{d["contradiction"][:70]}"' if d["flagged"] and d["contradiction"] else ""))
    fr = summary["false_flag"]
    print(f"\n  FALSE-FLAG (must-not-flag set = 32 originals + 24 coherent revisions): "
          f"{fr['n']}/{fr['of']} = {fr['rate']}")
    for w in fr["which"]:
        print(f"     FALSE FLAG {w['pid']:24s} {w['role']:22s} ({w['votes']}/{k})"
              + (f'  "{w["contradiction"][:60]}"' if w["contradiction"] else ""))
    cb = summary["constraint_regressions_flagged_bonus"]
    print(f"\n  (bonus) constraint-violation regressions also flagged: {cb['n']}/{cb['of']}  {cb['which']}")
    print("\n  PASS BAR: catch capex (the demonstrated pairwise blind spot) AND false-flag rate ~0.")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
