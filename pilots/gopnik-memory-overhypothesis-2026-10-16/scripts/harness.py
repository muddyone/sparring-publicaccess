#!/usr/bin/env python3
"""Run models through nexiom sequences under the three memory conditions (design note §4).

ONE CONVERSATION PER MACHINE. The model sees the machine's objects and the rules of the game,
then replies one move at a time: a TEST (which objects to place) or its ANSWER. The environment
replies "lit" or "not lit" and how many tests remain. After 6 tests it must answer.

THE THREE MEMORY CONDITIONS differ only in what the model has when it meets the next machine of
the same sequence. Memory always starts empty at a new sequence (§4, review finding R3).

  M0  nothing. Each machine is a fresh conversation.
  M1  after each training machine: feedback naming the nexioms (never the rule; R1), then a
      request for a note to its future self, at most 150 words (an over-length note is sent back
      once for a rewrite, and cut only if still over). The notes, and only the notes, are put in
      front of the next machine.
  M2  after each training machine: the same feedback. The full record of every earlier machine
      in the sequence (every message, both sides, and the feedback) is put in front of the next.

PARSING. A reply may contain reasoning; the LAST line starting with TEST: or ANSWER: is the move.
An unreadable or invalid move gets one corrective reply and does not use up a test; two in a row
on one machine end it as a parse failure (§7's answer-format check). Every parse failure is
logged with the text that caused it.

SEEDS. Each stage draws from its own seed range, so Stage 0 sequences can never reappear in the
baseline or the main run. Within a stage the same seeds are used for every memory condition and
every model: each condition meets the same machines.

STAGE 0 IS NEVER SCORED. Sequence records keep the truth (needed later for scoring), but this
script computes no accuracy, and `--report` prints plumbing only: parse failures, invalid moves,
forced answers, note lengths, dropped settings, tokens. That is the design's rule (§9): Stage 0
outputs are discarded and never scored.

Usage:
  ./harness.py --stage stage0 --models ../stage0-models.json --only anthropic --n 5
  ./harness.py --stage stage0 --report
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import re
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import models as mx  # noqa: E402
import nexiom as nx  # noqa: E402

PILOT = Path(__file__).resolve().parent.parent
SEED_BASE = {"stage0": 10_000_000, "baseline": 20_000_000, "main": 30_000_000}
MEMORY = ("M0", "M1", "M2")
NOTE_WORD_CAP = 150
MAX_PARSE_STRIKES = 2

SYSTEM = f"""You are working out how a machine works by experimenting with it.

The machine is a nexiom detector. It comes with {nx.N_OBJECTS} objects. Exactly two of them are nexioms. \
Each machine works one of two ways:
- it lights up if at least ONE nexiom is on it, or
- it lights up only if BOTH nexioms are on it together.
Objects that are not nexioms never affect the machine.

You may run up to {nx.MAX_TESTS} tests. In a test you place one or more of the objects on the machine \
and are told whether it lit up. Then you must say which two objects are the nexioms, and whether \
this machine needs one nexiom or two.

Reply with exactly one move per message. You may think first, but end your message with one line \
in one of these forms:
TEST: <object>, <object>, ...
ANSWER: nexioms = <object>, <object>; needs = one
ANSWER: nexioms = <object>, <object>; needs = two"""

_MOVE = re.compile(r"^\s*\**\s*(TEST|ANSWER)\s*\**\s*:\s*\**\s*(.*)$", re.I)
_ANSWER = re.compile(r"nexioms?\s*=\s*(.+?)\s*;\s*needs\s*=\s*(one|two|1|2)\b", re.I)


def _names(text: str) -> list[str]:
    return [t.strip().strip(".*`'\"").lower() for t in re.split(r",|\band\b", text) if t.strip()]


def parse_move(reply: str, objects: tuple[str, ...]):
    """-> ("test", frozenset) | ("answer", (frozenset, rule)) | ("error", reason)."""
    moves = [m for m in (_MOVE.match(line) for line in reply.splitlines()) if m]
    if not moves:
        return "error", "no line starting with TEST: or ANSWER:"
    kind, body = moves[-1].group(1).upper(), moves[-1].group(2)
    known = set(objects)
    if kind == "TEST":
        names = _names(body)
        unknown = [n for n in names if n not in known]
        if not names or unknown:
            return "error", f"unknown or missing objects: {unknown or body!r}"
        return "test", frozenset(names)
    m = _ANSWER.search(body)
    if not m:
        return "error", "answer not in the form 'nexioms = A, B; needs = one|two'"
    names = _names(m.group(1))
    if len(set(names)) != 2 or any(n not in known for n in names):
        return "error", f"answer must name exactly two of the objects, got {names}"
    rule = "disjunctive" if m.group(2).lower() in ("one", "1") else "conjunctive"
    return "answer", (frozenset(names), rule)


class Log:
    """Append-only JSONL call log, one line per model call, thread-safe."""

    def __init__(self, path: Path):
        self.path = path
        self.lock = threading.Lock()
        path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, rec: dict) -> None:
        rec = {"ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), **rec}
        with self.lock, self.path.open("a") as fh:
            fh.write(json.dumps(rec) + "\n")


def _call(log: Log, ctx: dict, cfg: dict, messages: list[dict], purpose: str) -> mx.Reply:
    reply = mx.chat(cfg["vendor"], cfg["model"], SYSTEM, messages, cfg.get("settings", {}),
                    cfg.get("max_tokens", 2000))
    log.write({**ctx, "purpose": purpose, "vendor": cfg["vendor"], "model": cfg["model"],
               "settings_requested": cfg.get("settings", {}), "settings_sent": reply.sent,
               "dropped": reply.dropped, "messages": messages, "reply": reply.text,
               "finish": reply.finish, "usage": reply.usage, "latency_s": reply.latency_s})
    return reply


def run_machine(log: Log, ctx: dict, cfg: dict, machine: nx.Machine, preamble: str) -> dict:
    core = (f"New machine. Its objects are: {', '.join(machine.objects)}.\n"
            f"You have {nx.MAX_TESTS} tests. Make your first move.")
    messages = [{"role": "user", "content": (f"{preamble}\n\n" if preamble else "") + core}]
    tests, errors, strikes = [], [], 0
    answer, forced, outcome = None, False, "answered"
    while True:
        reply = _call(log, {**ctx, "turn": len(messages) // 2}, cfg, messages, "move")
        messages.append({"role": "assistant", "content": reply.text})
        kind, val = parse_move(reply.text, machine.objects)
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
        if strikes >= MAX_PARSE_STRIKES:
            outcome = "parse_failure"
            break
        messages.append({"role": "user", "content": (
            f"That move could not be read ({reason}). End your message with one line: "
            "TEST: <objects> or ANSWER: nexioms = <object>, <object>; needs = one|two")})
    return {"objects": list(machine.objects), "truth": {"nexioms": sorted(machine.nexioms), "rule": machine.rule},
            "tests": tests, "answer": None if answer is None else {"nexioms": sorted(answer[0]), "rule": answer[1]},
            "forced": forced, "outcome": outcome, "parse_errors": errors, "messages": messages,
            "core_opening": core}


def run_sequence(log: Log, out_dir: Path, model_name: str, cfg: dict, memory: str, kind: str,
                 seed: int) -> Path:
    path = out_dir / model_name / f"{memory}-{kind}-{seed}.json"
    if path.exists():
        return path
    seq = nx.make_sequence(kind, seed)
    notes, record_text, machines = [], [], []
    for i, machine in enumerate(seq.machines):
        ctx = {"model_name": model_name, "memory": memory, "kind": kind, "seed": seed, "machine": i}
        if memory == "M1" and notes:
            preamble = "Notes you wrote to yourself after earlier machines:\n" + "\n".join(
                f"Note {j + 1}: {n}" for j, n in enumerate(notes))
        elif memory == "M2" and record_text:
            preamble = "Full record of the earlier machines:\n\n" + "\n\n".join(record_text)
        else:
            preamble = ""
        res = run_machine(log, ctx, cfg, machine, preamble)
        res["preamble_chars"] = len(preamble)
        is_training = i < len(seq.machines) - 1
        if is_training and memory in ("M1", "M2"):
            feedback = f"The nexioms on this machine were {' and '.join(sorted(machine.nexioms))}."
            res["feedback"] = feedback
            if memory == "M1":
                msgs = res["messages"] + [{"role": "user", "content": (
                    f"{feedback} Write a note to your future self, at most {NOTE_WORD_CAP} words, with "
                    "anything that would help you on the next machine. Reply with the note only.")}]
                rep = _call(log, {**ctx, "turn": "note"}, cfg, msgs, "note")
                first_words = len(rep.text.split())
                rewrites = 0
                if first_words > NOTE_WORD_CAP:
                    # Stage 0 found one model routinely overshooting the cap, and cutting a note
                    # at word 150 can drop its lesson, which often comes last. So an over-length
                    # note is returned once for a rewrite; it is cut only if still over.
                    msgs = msgs + [{"role": "assistant", "content": rep.text},
                                   {"role": "user", "content": (
                                       f"That note is {first_words} words. Rewrite it in at most "
                                       f"{NOTE_WORD_CAP} words, keeping what matters most. Reply with the note only.")}]
                    rep = _call(log, {**ctx, "turn": "note-rewrite"}, cfg, msgs, "note")
                    rewrites = 1
                words = rep.text.split()
                note = " ".join(words[:NOTE_WORD_CAP])
                res["note"] = {"text": note, "words_written": len(words), "first_draft_words": first_words,
                               "rewrites": rewrites, "truncated": len(words) > NOTE_WORD_CAP}
                notes.append(note)
            else:
                # This machine's own exchange only: its opening without the preamble, so earlier
                # machines are not copied into the record a second time.
                own = [{"role": "user", "content": res["core_opening"]}] + res["messages"][1:]
                lines = [f"Machine {i + 1}:"] + [f"{m['role'].upper()}: {m['content']}" for m in own]
                lines.append(f"FEEDBACK: {feedback}")
                record_text.append("\n".join(lines))
        machines.append(res)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"model_name": model_name, "model": cfg["model"], "memory": memory,
                                "kind": kind, "seed": seed, "machines": machines}, indent=1))
    return path


def report(stage_dir: Path) -> None:
    """Plumbing only. No accuracy is computed here, by design (§9)."""
    calls = [json.loads(l) for l in (stage_dir / "calls.jsonl").read_text().splitlines()] \
        if (stage_dir / "calls.jsonl").exists() else []
    seqs = sorted((stage_dir / "seqs").glob("*/*.json"))
    by_model: dict[str, dict] = {}
    for p in seqs:
        d = json.loads(p.read_text())
        s = by_model.setdefault(d["model_name"], {"model": d["model"], "sequences": 0, "machines": 0,
                                                   "parse_failures": 0, "invalid_moves": 0, "forced": 0,
                                                   "tests": [], "note_words": [], "notes_truncated": 0,
                                                   "cells": {}})
        s["sequences"] += 1
        cell = f"{d['memory']}-{d['kind']}"
        c = s["cells"].setdefault(cell, {"machines": 0, "parse_failures": 0})
        for m in d["machines"]:
            s["machines"] += 1
            c["machines"] += 1
            s["parse_failures"] += m["outcome"] == "parse_failure"
            c["parse_failures"] += m["outcome"] == "parse_failure"
            s["invalid_moves"] += len(m["parse_errors"])
            s["forced"] += m["forced"]
            s["tests"].append(len(m["tests"]))
            if "note" in m:
                s["note_words"].append(m["note"]["words_written"])
                s["notes_truncated"] += m["note"]["truncated"]
                s["notes_rewritten"] = s.get("notes_rewritten", 0) + m["note"].get("rewrites", 0)
    for name, s in sorted(by_model.items()):
        mc = [c for c in calls if c.get("model_name") == name]
        tin = sum(c["usage"].get("input_tokens", c["usage"].get("prompt_tokens", 0)) for c in mc)
        tout = sum(c["usage"].get("output_tokens", c["usage"].get("completion_tokens", 0)) for c in mc)
        dropped = sorted({d for c in mc for d in c.get("dropped", [])})
        worst = max((c["parse_failures"] / c["machines"], k) for k, c in s["cells"].items())
        nw = s["note_words"]
        print(f"{name} ({s['model']}): {s['sequences']} sequences, {s['machines']} machines, {len(mc)} calls")
        print(f"   parse failures {s['parse_failures']}/{s['machines']} (worst cell {worst[1]} {worst[0]:.0%}; "
              f"design ceiling 5%)   invalid moves corrected {s['invalid_moves']}")
        print(f"   tests per machine: mean {sum(s['tests']) / len(s['tests']):.2f}, max {max(s['tests'])}; "
              f"ran out of tests {s['forced']}")
        if nw:
            print(f"   notes: {len(nw)}, words mean {sum(nw) / len(nw):.0f}, max {max(nw)}, "
                  f"rewritten for length {s.get('notes_rewritten', 0)}, still cut {s['notes_truncated']}")
        print(f"   tokens in {tin:,}  out {tout:,}   settings dropped by the API: {dropped or 'none'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--stage", choices=list(SEED_BASE), required=True)
    ap.add_argument("--models", type=Path, help="models JSON (see ../stage0-models.json)")
    ap.add_argument("--only", help="comma-separated model names from the JSON")
    ap.add_argument("--memory", default=",".join(MEMORY))
    ap.add_argument("--kinds", default=",".join(nx.SEQUENCE_RULES))
    ap.add_argument("--n", type=int, default=5, help="sequences per cell")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    stage_dir = PILOT / "runs" / args.stage
    if args.report:
        report(stage_dir)
        return 0
    cfg_all = json.loads(args.models.read_text())["models"]
    names = args.only.split(",") if args.only else list(cfg_all)
    log = Log(stage_dir / "calls.jsonl")
    jobs = [(name, mem, kind, SEED_BASE[args.stage] + i)
            for name in names for mem in args.memory.split(",") for kind in args.kinds.split(",")
            for i in range(args.n)]
    failures = 0
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run_sequence, log, stage_dir / "seqs", n, cfg_all[n], m, k, s): (n, m, k, s)
                for n, m, k, s in jobs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            try:
                f.result()
            except Exception as exc:  # one failed sequence must not kill the run; it is retried on resume
                failures += 1
                print(f"   FAILED {futs[f]}: {str(exc)[:200]}", file=sys.stderr)
            if i % 10 == 0 or i == len(jobs):
                print(f"   {i}/{len(jobs)} sequences", file=sys.stderr)
    print(f"done: {len(jobs) - failures}/{len(jobs)} sequences; {failures} failed (re-run to resume)")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
