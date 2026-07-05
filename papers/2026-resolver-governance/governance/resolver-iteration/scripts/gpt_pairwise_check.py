#!/usr/bin/env python3
"""Cross-vendor pairwise check on the natural corpus (EXPLORATORY) — salvage the failed gold.

natural_eval's flaw-COUNT panel failed as an independent gold: flaw-counting is the coarse method we
already discredited (0.25 reg-recall on stark constructed cases), so on subtle natural pairs it defaults
to ~EQUIVALENT and can't adjudicate pairwise's 11/12 pro-revision verdict. The right gold is the method
that WORKED (pairwise) run on a DIFFERENT vendor (GPT-5.2). If GPT-pairwise agrees R1 is better, the
verdict is vendor-robust (either both right, or a shared cross-vendor pro-revision lean — but not a
Claude-specific artifact). If it disagrees, that's a real red flag on the ruler's natural-data calibration.

Reuses the exact pairwise prompt (P.PAIR_JUDGE) and the ruler's cached Claude verdicts. Order-randomized,
k=3, resumable.

Usage: python3 gpt_pairwise_check.py [--k 3]
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L
import pairwise_dv_probe as P
from resolver_loop import _flip, _map, pairwise_verdict

CORPUS = R.PILOT / "analysis" / "natural-corpus.json"
OUT_JSON = R.PILOT / "analysis" / "natural-xvendor.json"


def gpt_pairwise(pair, k):
    problem, A, B = pair["problem"], pair["R0"], pair["R1"]
    votes = []
    for j in range(1, k + 1):
        uid = f"natgpw__{pair['id']}__rep{j}"
        rec = R.load(uid)
        if not rec:
            tag = f"gpw__{pair['id']}"
            a_in_A = _flip(tag, j)
            slotA, slotB = (A, B) if a_in_A else (B, A)
            out = L.gpt_json(R.GPT, P.PAIR_JUDGE_SYS,
                             P.PAIR_JUDGE_USER.format(problem=problem, a=slotA, b=slotB),
                             max_completion_tokens=4000)
            raw = str(out.get("verdict", "EQUIVALENT")).upper() if isinstance(out, dict) else "EQUIVALENT"
            rec = {"mapped": _map(raw, a_in_A)}
            R.save(uid, rec)
        votes.append(rec["mapped"])
    return collections.Counter(votes).most_common(1)[0][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()
    k = args.k
    pairs = json.loads(CORPUS.read_text())["problems"]

    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        gpt = dict(zip([p["id"] for p in pairs],
                       ex.map(lambda p: gpt_pairwise(p, k), pairs)))
    # ruler (Claude pairwise) verdicts are cached from natural_eval (loop_pw__nat__<id>__it0)
    rows, agree = [], 0
    for p in pairs:
        claude_v = pairwise_verdict(p["problem"], p["R0"], p["R1"], f"nat__{p['id']}__it0", k)  # cached
        g = gpt[p["id"]]
        a = (claude_v == g)
        agree += int(a)
        rows.append({"id": p["id"], "claude_ruler": claude_v, "gpt_pairwise": g, "agree": a})

    cd = collections.Counter(r["claude_ruler"] for r in rows)
    gd = collections.Counter(r["gpt_pairwise"] for r in rows)
    summary = {"EXPLORATORY": True, "k": k, "n": len(rows),
               "claude_ruler_dist": dict(cd), "gpt_pairwise_dist": dict(gd),
               "cross_vendor_agreement": f"{agree}/{len(rows)}", "rows": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== CROSS-VENDOR PAIRWISE CHECK (natural corpus) ===")
    print(f"  Claude ruler dist: {dict(cd)}")
    print(f"  GPT pairwise dist: {dict(gd)}")
    print(f"  cross-vendor agreement: {agree}/{len(rows)}")
    print(f"\n  {'id':22s} {'claude':10s} {'gpt':10s} agree")
    for r in rows:
        print(f"  {r['id']:22s} {r['claude_ruler']:10s} {r['gpt_pairwise']:10s} {'yes' if r['agree'] else 'NO'}")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
