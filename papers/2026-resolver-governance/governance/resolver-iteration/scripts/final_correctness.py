#!/usr/bin/env python3
"""Final-output correctness re-score (EXPLORATORY) — the right metric for a REPAIR loop.

The resolver loop is a repair mechanism, so "accept vs reject the original revision" mismeasures it
(it scored capex a "miss" for accepting a REPAIRED-correct B'). The correct question is:
**does the loop's FINAL DELIVERED text still contain the planted flaw?**

Core instrument: a planted-flaw-PRESENCE judge — given a recommendation and a precise description of ONE
specific defect, decide only whether THAT defect is present (quote the span). Narrow + verifiable, like
the coherence gate; NOT a global quality judge. Self-validated on the controls before it's trusted:
  * sensitivity: it must find the flaw in the raw regression B (expect PRESENT 8/8).
  * specificity: it must NOT find the flaw in the clean original A (expect ABSENT 8/8) — the over-flag test.

Then applied to what the loop actually delivered per planted_regression pair (from resolver-loop.json):
  * 7 pairs REJECTED -> delivered = A (clean original) -> expect flaw ABSENT.
  * capex ACCEPTED -> delivered = B' (the repair) -> the real question: did the repair remove the flaw?

Headline: delivered-output flaw-free X/8. If capex's B' is flaw-free, the loop's true output-correctness
is 8/8 — the apparent "7/8" was the measurement frame, not the loop.

Flaw description = the control set's change_note (what was injected). k-vote. Resumable. Claude-only.

Usage: python3 final_correctness.py [--k 5]
Env: ANTHROPIC_API_KEY.
"""
import json, argparse, collections
import concurrent.futures as cf
import run_study as R
import lib_llm as L

K_DEFAULT = 5
MANIFEST = R.PILOT / "analysis" / "positive-control-set.json"
LOOP = R.PILOT / "analysis" / "resolver-loop.json"
OUT_JSON = R.PILOT / "analysis" / "final-correctness.json"

FLAW_SYS = (
    "You are checking whether ONE specific defect is present in a recommendation. You are given the "
    "recommendation and a precise description of the defect to look for. Answer ONLY whether THAT defect "
    "is present in the text — not whether the recommendation is good overall, and not whether some OTHER "
    "flaw exists. The defect is PRESENT only if the text actually exhibits it; quote the offending span. "
    "If the text does not exhibit this specific defect — including if it states the CORRECT version of the "
    "disputed fact, or correctly accounts for the risk the defect would remove — it is ABSENT. Be strict: "
    "do not infer the defect from tone, length, or unrelated weaknesses."
)
FLAW_USER = (
    "DEFECT TO CHECK FOR:\n{flaw}\n\nRECOMMENDATION:\n{rec}\n\n"
    "Return JSON: {{\"present\": true|false, \"evidence\": str}} — quote the offending span in \"evidence\" "
    "if present, else \"\"."
)


def judge(flaw, text, uid, k):
    votes, ev = [], []
    for j in range(1, k + 1):
        u = f"{uid}__rep{j}"
        rec = R.load(u)
        if not rec:
            out = L.claude_json(R.CLAUDE, FLAW_SYS, FLAW_USER.format(flaw=flaw, rec=text), max_tokens=1000)
            present = bool(out.get("present", False)) if isinstance(out, dict) else False
            evid = (out.get("evidence", "") or "") if isinstance(out, dict) else ""
            rec = {"present": present, "evidence": evid[:300]}
            R.save(u, rec)
        votes.append(rec["present"])
        if rec["present"] and rec["evidence"]:
            ev.append(rec["evidence"])
    present = sum(1 for v in votes if v) >= (k // 2 + 1)
    return {"present": present, "present_votes": sum(1 for v in votes if v), "k": k,
            "evidence": (ev[0] if ev else "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    args = ap.parse_args()
    k = args.k

    pairs = {p["pair_id"]: p for p in json.loads(MANIFEST.read_text())["pairs"]}
    loop = {r["pair_id"]: r for r in json.loads(LOOP.read_text())["results"]}
    regs = [pid for pid, p in pairs.items() if p["type"] == "planted_regression"]

    # build jobs: A and B for every regression (instrument validation); B' for rewrite-triggered ones.
    jobs = []
    bprime = {}
    for pid in regs:
        p = pairs[pid]; flaw = p["change_note"]
        jobs.append((flaw, p["text_a"], f"fcheck__A__{pid}"))
        jobs.append((flaw, p["text_b"], f"fcheck__B__{pid}"))
        lr = loop[pid]
        if lr["rewrites"] > 0:
            rw = R.load(f"loop_rw__{pid}__it0")   # the (single) repair this run produced
            if rw:
                bprime[pid] = rw["text"]
                jobs.append((flaw, rw["text"], f"fcheck__Bprime__{pid}"))

    print(f"[final] {len(regs)} regressions; {len(jobs)} judge targets x k={k}", flush=True)
    done = errs = 0
    with cf.ThreadPoolExecutor(max_workers=R.WORKERS) as ex:
        futs = {ex.submit(judge, flaw, text, uid, k): uid for (flaw, text, uid) in jobs}
        res = {}
        for f in cf.as_completed(futs):
            try:
                res[futs[f]] = f.result()
            except Exception as e:   # noqa: BLE001
                errs += 1
                print(f"[final] ERROR {futs[f]}: {repr(e)[:140]}", flush=True)
            done += 1
            if done % 10 == 0:
                print(f"[final] {done}/{len(jobs)}", flush=True)
    if errs:
        print(f"[final] {errs} errors -- re-run to retry.", flush=True)

    # assemble
    rows = []
    for pid in regs:
        short = pid.split("__")[0]
        A = res.get(f"fcheck__A__{pid}", {})
        B = res.get(f"fcheck__B__{pid}", {})
        lr = loop[pid]
        if lr["outcome"] == "REJECT":
            delivered_role, dj = "A", A
        else:
            delivered_role, dj = ("B'", res.get(f"fcheck__Bprime__{pid}", {})) if pid in bprime else ("B", B)
        rows.append({"pid": short, "loop_outcome": lr["outcome"], "rewrites": lr["rewrites"],
                     "delivered": delivered_role,
                     "flaw_in_A": A.get("present"), "A_votes": A.get("present_votes"),
                     "flaw_in_B": B.get("present"), "B_votes": B.get("present_votes"),
                     "flaw_in_Bprime": (res.get(f"fcheck__Bprime__{pid}", {}).get("present") if pid in bprime else None),
                     "delivered_flaw_present": dj.get("present"),
                     "delivered_evidence": dj.get("evidence", "")})

    sens = sum(1 for r in rows if r["flaw_in_B"])              # B should be PRESENT
    spec = sum(1 for r in rows if r["flaw_in_A"] is False)     # A should be ABSENT
    clean = sum(1 for r in rows if r["delivered_flaw_present"] is False)
    summary = {"EXPLORATORY": True, "k": k,
               "instrument": {"sensitivity_B_present": f"{sens}/{len(rows)}",
                              "specificity_A_absent": f"{spec}/{len(rows)}"},
               "delivered_output_flaw_free": f"{clean}/{len(rows)}",
               "rows": rows}
    OUT_JSON.write_text(json.dumps(summary, indent=2))

    print("\n=== FINAL-OUTPUT CORRECTNESS (planted_regression) ===")
    print(f"  instrument check — sensitivity (flaw in raw B): {sens}/{len(rows)}   "
          f"specificity (flaw absent in clean A): {spec}/{len(rows)}")
    bp_hdr = "B'"
    print(f"\n  {'pair':22s} {'loop':8s} {'deliv':6s} {'A':>4s} {'B':>4s} {bp_hdr:>4s}  delivered-flaw?")
    for r in rows:
        bp = "-" if r["flaw_in_Bprime"] is None else ("Y" if r["flaw_in_Bprime"] else "N")
        a = "Y" if r["flaw_in_A"] else "N"; b = "Y" if r["flaw_in_B"] else "N"
        dp = "PRESENT" if r["delivered_flaw_present"] else "absent"
        print(f"  {r['pid']:22s} {r['loop_outcome']:8s} {r['delivered']:6s} {a:>4s} {b:>4s} {bp:>4s}  {dp}")
    print(f"\n  DELIVERED-OUTPUT FLAW-FREE: {clean}/{len(rows)}  "
          f"(vs the accept/reject frame's {sum(1 for r in rows if r['loop_outcome']=='REJECT')}/8)")
    print(f"\nwrote {OUT_JSON.relative_to(R.PILOT)}")


if __name__ == "__main__":
    main()
