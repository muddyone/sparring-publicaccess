#!/usr/bin/env python3
"""Exploratory probe: do notes carry the rule when 4 tests are too few without it?

budget_sim.py shows that at 4 tests an ideal explorer gets 53% of machines right without
knowing the rule and 93% knowing it. So on the fourth machine of a sequence, anything above
what a model manages without notes is what its notes carried.

Runs the LOCKED harness unchanged except for the test budget (nexiom.MAX_TESTS set to 4 before
the harness is imported, so its prompt and its turn limit both read 4). Conditions M0 (no
memory) and M1 (feedback naming the nexioms, never the rule, then a note of at most 150 words).
CC sequences test transfer of "needs two"; DD sequences check that notes carry the rule seen,
not a habit of answering "two".

EXPLORATORY, not a pre-registration. Seeds 50M+, never reused. A confirmatory study, if any, is
designed and locked after this, on fresh seeds.

Usage: ./probe4.py --models ../../gopnik-memory-overhypothesis-2026-10-16/models.json \
          --only anthropic,openai --cc 10 --dd 5
       ./probe4.py --report
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "gopnik-memory-overhypothesis-2026-10-16" / "scripts"))
import nexiom as nx  # noqa: E402
nx.MAX_TESTS = 4
import harness as h  # noqa: E402

RUN = HERE.parent / "runs" / "probe4"
SEED_BASE = 50_000_000

# Probe 2b: the locked prompt's "Each machine works one of two ways" tells the model every machine
# is a fresh draw, which licenses keeping the rule open. --singular drops "Each" for "The", so the
# two rules are still stated but nothing says they vary between machines. Same seeds as probe 2,
# so each sequence meets the same machines under both wordings.
EACH, THE = "Each machine works one of two ways:", "The machine works one of two ways:"

# Probe 2c: the rules are never named. The prompt and answer format are calibration variant C's
# (calibrate.py), at 4 tests; after naming the nexioms the model answers one probe question ("with
# only X on it, would it light up?"), which gives its rule without offering the options. Memory
# conditions, feedback and the note request are the locked harness's, unchanged.
import calibrate as cal  # noqa: E402
UNNAMED = {"named": False, "tests": 4}


def run_machine_unnamed(log, ctx, cfg, machine, preamble):
    core = (f"New machine. Its objects are: {', '.join(machine.objects)}.\n"
            f"You have {nx.MAX_TESTS} tests. Make your first move.")
    messages = [{"role": "user", "content": (f"{preamble}\n\n" if preamble else "") + core}]
    tests, errors, strikes, answer, forced, outcome = [], [], 0, None, False, "answered"
    while True:
        reply = h._call(log, {**ctx, "turn": len(messages) // 2}, cfg, messages, "move")
        messages.append({"role": "assistant", "content": reply.text})
        kind, val = cal.parse(reply.text, machine.objects, False)
        if kind == "answer":
            answer = val
            break
        if kind == "test" and len(tests) < nx.MAX_TESTS:
            strikes = 0
            lit = machine.lights(val)
            tests.append({"placed": sorted(val), "lit": lit})
            left = nx.MAX_TESTS - len(tests)
            msg = f"Result: the machine {'LIT UP' if lit else 'did NOT light up'}. "
            if left:
                msg += f"You have {left} test{'s' if left != 1 else ''} left. Make your next move."
            else:
                msg += "You have used all your tests. Give your ANSWER now."
                forced = True
            messages.append({"role": "user", "content": msg})
            continue
        reason = val if kind == "error" else "no tests left; an ANSWER is required"
        errors.append({"reason": reason, "reply_tail": reply.text[-300:]})
        strikes += 1
        if strikes >= h.MAX_PARSE_STRIKES:
            outcome = "parse_failure"
            break
        messages.append({"role": "user", "content": (
            f"That move could not be read ({reason}). End your message with one line: "
            "TEST: <objects> or ANSWER: nexioms = <object>, <object>")})
    result = None
    if answer is not None:
        probe = sorted(answer[0])[0]
        messages.append({"role": "user", "content": (
            f"One last question. If only {probe} were on the machine, with nothing else, would it light up? "
            "End your message with one line: PROBE: yes or PROBE: no")})
        reply = h._call(log, {**ctx, "turn": "probe"}, cfg, messages, "probe")
        messages.append({"role": "assistant", "content": reply.text})
        lines = [l for l in reply.text.splitlines() if l.strip().upper().lstrip("*").startswith("PROBE")]
        yn = cal._YESNO.search(lines[-1]) if lines else None
        if yn:
            result = {"nexioms": sorted(answer[0]), "rule": "disjunctive" if yn.group(1).lower() == "yes" else "conjunctive"}
        else:
            outcome = "parse_failure"
            errors.append({"reason": "probe unreadable", "reply_tail": reply.text[-300:]})
    return {"objects": list(machine.objects), "truth": {"nexioms": sorted(machine.nexioms), "rule": machine.rule},
            "tests": tests, "answer": result, "forced": forced, "outcome": outcome, "parse_errors": errors,
            "messages": messages, "core_opening": core}


def report():
    rows = {}
    for f in sorted(RUN.glob("seqs/*/*.json")):
        r = json.loads(f.read_text())
        for i, m in enumerate(r["machines"]):
            key = (r["model_name"], r["memory"], r["kind"], i + 1)
            c = rows.setdefault(key, {"n": 0, "correct": 0, "rule": 0, "parse_fail": 0})
            c["n"] += 1
            if m["outcome"] != "answered":
                c["parse_fail"] += 1
                continue
            a, t = m["answer"], m["truth"]
            c["rule"] += a["rule"] == t["rule"]
            c["correct"] += a["rule"] == t["rule"] and a["nexioms"] == t["nexioms"]
    out = {f"{n}/{mem}/{k}/machine{i}": c for (n, mem, k, i), c in sorted(rows.items())}
    (RUN / "probe4.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"{'model/memory/kind':<22} {'machine 1':>11} {'machine 2':>11} {'machine 3':>11} {'TEST (4)':>11}   rule right on test")
    for (n, mem, k) in sorted({key[:3] for key in rows}):
        cells = [rows.get((n, mem, k, i)) for i in range(1, 5)]
        line = " ".join(f"{c['correct']:>5}/{c['n']:<5}" if c else f"{'-':>11}" for c in cells)
        t = cells[3]
        print(f"{n + '/' + mem + '/' + k:<22} {line}   {t['rule']}/{t['n']}" + (f"  ({t['parse_fail']} parse fail)" if t["parse_fail"] else ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", type=Path)
    ap.add_argument("--only")
    ap.add_argument("--memory", default="M0,M1")
    ap.add_argument("--cc", type=int, default=10)
    ap.add_argument("--dd", type=int, default=5)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--singular", action="store_true", help='probe 2b: "The machine", not "Each machine"')
    ap.add_argument("--unnamed", action="store_true", help="probe 2c: the rules are never named")
    a = ap.parse_args()
    global RUN
    if a.unnamed:
        RUN = HERE.parent / "runs" / "probe4c"
        h.SYSTEM = cal.system(UNNAMED)
        h.run_machine = run_machine_unnamed
    if a.singular:
        RUN = HERE.parent / "runs" / "probe4b"
        assert EACH in h.SYSTEM
        h.SYSTEM = h.SYSTEM.replace(EACH, THE)
    if a.report:
        report()
        return 0
    cfg_all = json.loads(a.models.read_text())["models"]
    names = a.only.split(",") if a.only else list(cfg_all)
    log = h.Log(RUN / "calls.jsonl")
    jobs = [(n, mem, k, SEED_BASE + i) for n in names for mem in a.memory.split(",")
            for k, cnt in (("CC", a.cc), ("DD", a.dd)) for i in range(cnt)]
    fails = 0
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(h.run_sequence, log, RUN / "seqs", n, cfg_all[n], mem, k, s): (n, mem, k, s)
                for n, mem, k, s in jobs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            try:
                f.result()
            except Exception as exc:
                fails += 1
                print(f"   FAILED {futs[f]}: {str(exc)[:200]}", file=sys.stderr)
            if i % 10 == 0 or i == len(jobs):
                print(f"   {i}/{len(jobs)} sequences", file=sys.stderr)
    print(f"done: {len(jobs) - fails}/{len(jobs)}; {fails} failed (re-run to resume)")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
