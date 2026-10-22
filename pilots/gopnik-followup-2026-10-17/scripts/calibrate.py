#!/usr/bin/env python3
"""Calibration for a harder Gopnik follow-up: find a task where models without memory leave room.

The locked pilot (../../gopnik-memory-overhypothesis-2026-10-16/) stopped because every model
solved every "needs two" machine without memory. Its prompt named both possible rules, and it
allowed 6 tests when 5 always suffice. This script tries harder variants, M0 only, and reports
accuracy per variant, so a follow-up design can pick one whose baseline leaves headroom.

EXPLORATORY. Not a pre-registration. Its sequences use their own seed range (40M+) and will never
be reused in any later baseline or main run. Choosing a variant from these numbers is the point
of calibration; the follow-up's own design note must be written and locked after this, before
its own baseline.

Variants:
  A  rules named (as in the locked pilot), 5 tests: the fewest with which an ideal strategy still
     always succeeds (32 outcomes for 30 answers); random tests score about 44% (locked §12)
  B  rules NOT named, 6 tests; the model names the nexioms, then answers one probe question
     ("with only X on it, would it light up?"), which gives its rule without offering the
     options in advance
  C  rules not named, 5 tests
(4 tests was rejected: 16 possible outcomes for 30 answers caps even an ideal strategy near 50%,
against about 33% for random tests, so too little of the task is about reasoning.)

The locked pilot's simulator, model client, log and name parser are imported, not copied, so this
runs on exactly the code that ran there; only the prompts, test budget and answer protocol differ.

Usage: ./calibrate.py --models ../../gopnik-memory-overhypothesis-2026-10-16/models.json \
          --only anthropic,openai,xai --variants A,B,C --cc 10 --dd 5
       ./calibrate.py --report
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCKED = HERE.parent.parent / "gopnik-memory-overhypothesis-2026-10-16" / "scripts"
sys.path.insert(0, str(LOCKED))
import harness as h  # noqa: E402
import models as mx  # noqa: E402
import nexiom as nx  # noqa: E402

RUN = HERE.parent / "runs" / "calibration"
SEED_BASE = 40_000_000
VARIANTS = {"A": {"named": True, "tests": 5}, "B": {"named": False, "tests": 6}, "C": {"named": False, "tests": 5}}

_HEAD = f"""You are working out how a machine works by experimenting with it.

The machine is a nexiom detector. It comes with {nx.N_OBJECTS} objects. Exactly two of them are nexioms. \
"""
_NAMED = """Each machine works one of two ways:
- it lights up if at least ONE nexiom is on it, or
- it lights up only if BOTH nexioms are on it together.
Objects that are not nexioms never affect the machine.
"""
_UNNAMED = """The machine responds to its nexioms in a fixed way that you have to discover. \
Objects that are not nexioms never affect the machine.
"""


def system(v: dict) -> str:
    rules = _NAMED if v["named"] else _UNNAMED
    ask = ("say which two objects are the nexioms, and whether this machine needs one nexiom or two."
           if v["named"] else "say which two objects are the nexioms.")
    forms = ("ANSWER: nexioms = <object>, <object>; needs = one\nANSWER: nexioms = <object>, <object>; needs = two"
             if v["named"] else "ANSWER: nexioms = <object>, <object>")
    return (_HEAD + rules + f"\nYou may run up to {v['tests']} tests. In a test you place one or more of the "
            f"objects on the machine and are told whether it lit up. Then you must {ask}\n\n"
            "Reply with exactly one move per message. You may think first, but end your message with one "
            f"line in one of these forms:\nTEST: <object>, <object>, ...\n{forms}")


_NEX = re.compile(r"nexioms?\s*=\s*([^;\n]+)", re.I)
_YESNO = re.compile(r"\b(yes|no)\b", re.I)


def parse(reply: str, objects, named: bool):
    if named:
        return h.parse_move(reply, objects)
    moves = [m for m in (h._MOVE.match(line) for line in reply.splitlines()) if m]
    if not moves:
        return "error", "no line starting with TEST: or ANSWER:"
    kind, body = moves[-1].group(1).upper(), moves[-1].group(2)
    if kind == "TEST":
        return h.parse_move(reply, objects)
    m = _NEX.search(body)
    names = h._names(m.group(1)) if m else []
    if len(set(names)) != 2 or any(n not in objects for n in names):
        return "error", f"answer must name exactly two of the objects, got {names}"
    return "answer", (frozenset(names), None)


def call(log, ctx, cfg, sys_prompt, messages, purpose):
    rep = mx.chat(cfg["vendor"], cfg["model"], sys_prompt, messages, cfg.get("settings", {}),
                  cfg.get("max_tokens", 2000))
    log.write({**ctx, "purpose": purpose, "vendor": cfg["vendor"], "model": cfg["model"],
               "settings_sent": rep.sent, "dropped": rep.dropped, "messages": messages,
               "reply": rep.text, "finish": rep.finish, "usage": rep.usage})
    return rep


def run_machine(log, ctx, cfg, v, machine):
    sp, budget = system(v), v["tests"]
    messages = [{"role": "user", "content": f"New machine. Its objects are: {', '.join(machine.objects)}.\n"
                                            f"You have {budget} tests. Make your first move."}]
    tests, errors, strikes, answer = [], [], 0, None
    while True:
        rep = call(log, {**ctx, "turn": len(messages) // 2}, cfg, sp, messages, "move")
        messages.append({"role": "assistant", "content": rep.text})
        kind, val = parse(rep.text, machine.objects, v["named"])
        if kind == "answer":
            answer = val
            break
        if kind == "test" and len(tests) < budget:
            strikes = 0
            lit = machine.lights(val)
            tests.append({"placed": sorted(val), "lit": lit})
            left = budget - len(tests)
            msg = f"Result: the machine {'LIT UP' if lit else 'did NOT light up'}. "
            msg += (f"You have {left} test{'s' if left != 1 else ''} left. Make your next move." if left
                    else "You have used all your tests. Give your ANSWER now.")
            messages.append({"role": "user", "content": msg})
            continue
        errors.append(val if kind == "error" else "no tests left")
        strikes += 1
        if strikes >= h.MAX_PARSE_STRIKES:
            return {"outcome": "parse_failure", "errors": errors, "tests": tests, "messages": messages,
                    "truth": {"nexioms": sorted(machine.nexioms), "rule": machine.rule}}
        messages.append({"role": "user", "content": f"That move could not be read ({errors[-1]}). End your "
                                                    "message with one TEST: or ANSWER: line in the form given."})
    nexioms, rule = answer
    if rule is None:  # unnamed variants: one probe question gives the rule without offering options earlier
        probe = sorted(nexioms)[0]
        messages.append({"role": "user", "content": (
            f"One last question. If only {probe} were on the machine, with nothing else, would it light up? "
            "End your message with one line: PROBE: yes or PROBE: no")})
        rep = call(log, {**ctx, "turn": "probe"}, cfg, sp, messages, "probe")
        messages.append({"role": "assistant", "content": rep.text})
        lines = [l for l in rep.text.splitlines() if l.strip().upper().lstrip("*").startswith("PROBE")]
        yn = _YESNO.search(lines[-1]) if lines else None
        if not yn:
            return {"outcome": "parse_failure", "errors": errors + ["probe unreadable"], "tests": tests,
                    "messages": messages, "truth": {"nexioms": sorted(machine.nexioms), "rule": machine.rule}}
        rule = "disjunctive" if yn.group(1).lower() == "yes" else "conjunctive"
    return {"outcome": "answered", "tests": tests, "errors": errors, "messages": messages,
            "answer": {"nexioms": sorted(nexioms), "rule": rule},
            "truth": {"nexioms": sorted(machine.nexioms), "rule": machine.rule}}


def run_sequence(log, name, cfg, var, kind, seed):
    path = RUN / "seqs" / var / name / f"{kind}-{seed}.json"
    if path.exists():
        return
    seq = nx.make_sequence(kind, seed)
    out = [run_machine(log, {"model_name": name, "variant": var, "kind": kind, "seed": seed, "machine": i},
                       cfg, VARIANTS[var], m) for i, m in enumerate(seq.machines)]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"model_name": name, "variant": var, "kind": kind, "seed": seed, "machines": out}))


def report():
    rows = {}
    for f in sorted((RUN / "seqs").glob("*/*/*.json")):
        r = json.loads(f.read_text())
        key = (r["variant"], r["model_name"], r["kind"])
        c = rows.setdefault(key, {"machines": 0, "correct": 0, "rule": 0, "parse_fail": 0})
        for m in r["machines"]:  # M0: every machine is an independent trial
            c["machines"] += 1
            if m["outcome"] != "answered":
                c["parse_fail"] += 1
                continue
            a, t = m["answer"], m["truth"]
            c["rule"] += a["rule"] == t["rule"]
            c["correct"] += a["rule"] == t["rule"] and a["nexioms"] == t["nexioms"]
    out = {f"{v}/{n}/{k}": c for (v, n, k), c in sorted(rows.items())}
    (RUN / "calibration.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"{'variant/model/kind':<22} {'correct':>10} {'rule right':>11} {'parse fail':>10}")
    for key, c in out.items():
        print(f"{key:<22} {c['correct']:>4}/{c['machines']:<5} {c['rule']:>5}/{c['machines']:<5} {c['parse_fail']:>6}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", type=Path)
    ap.add_argument("--only")
    ap.add_argument("--variants", default="A,B,C")
    ap.add_argument("--cc", type=int, default=10)
    ap.add_argument("--dd", type=int, default=5)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if a.report:
        report()
        return 0
    cfg_all = json.loads(a.models.read_text())["models"]
    names = a.only.split(",") if a.only else list(cfg_all)
    log = h.Log(RUN / "calls.jsonl")
    jobs = [(n, v, k, SEED_BASE + i) for n in names for v in a.variants.split(",")
            for k, cnt in (("CC", a.cc), ("DD", a.dd)) for i in range(cnt)]
    fails = 0
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(run_sequence, log, n, cfg_all[n], v, k, s): (n, v, k, s) for n, v, k, s in jobs}
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
