#!/usr/bin/env python3
"""Offline checks for the harness: no network, no keys, no spend.

A scripted fake model replaces models.chat. It reads the conversation it is given, plays the
adaptive explorer (controls.py) through the real prompts and the real parser, and so must get
every machine right. It also sends malformed replies on purpose, to exercise the parse-strike path.

Run: ./test_harness.py   (exit 0 = all checks pass)
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import controls  # noqa: E402
import harness as h  # noqa: E402
import models as mx  # noqa: E402
import nexiom as nx  # noqa: E402

FAILS: list[str] = []


def check(cond: bool, what: str) -> None:
    if not cond:
        FAILS.append(what)


def test_parser() -> None:
    objs = ("alpha", "beta", "gamma", "delta", "eps", "zeta")
    check(h.parse_move("thinking...\nTEST: alpha, beta", objs) == ("test", frozenset({"alpha", "beta"})), "plain test")
    check(h.parse_move("**TEST:** Alpha and Beta", objs) == ("test", frozenset({"alpha", "beta"})), "bold, 'and', case")
    check(h.parse_move("TEST: alpha\nTEST: gamma", objs) == ("test", frozenset({"gamma"})), "last move wins")
    k, v = h.parse_move("ANSWER: nexioms = beta, gamma; needs = two", objs)
    check(k == "answer" and v == (frozenset({"beta", "gamma"}), "conjunctive"), "answer two")
    k, v = h.parse_move("ANSWER: nexioms = beta, gamma; needs = one.", objs)
    check(k == "answer" and v[1] == "disjunctive", "answer one")
    check(h.parse_move("TEST: alpha, omega", objs)[0] == "error", "unknown object rejected")
    check(h.parse_move("ANSWER: nexioms = beta; needs = two", objs)[0] == "error", "one-object answer rejected")
    check(h.parse_move("I think it's beta and gamma", objs)[0] == "error", "no move line rejected")


class FakeModel:
    """Plays the adaptive explorer from the conversation text. `bad_every` > 0 makes it send an
    unreadable reply before every n-th move, once (it recovers on the corrective message)."""

    def __init__(self, bad_every: int = 0, always_bad: bool = False, obey_rewrite: bool = True):
        self.bad_every, self.always_bad, self.n = bad_every, always_bad, 0
        self.obey_rewrite = obey_rewrite

    def __call__(self, vendor, model, system, messages, settings, max_tokens=2000):
        text = messages[-1]["content"]
        if "Write a note" in text:
            return mx.Reply(text="Note: " + "word " * 160, usage={}, finish="stop", sent=settings)
        if "Rewrite it in at most" in text:
            return mx.Reply(text="Short note: " + "word " * (100 if self.obey_rewrite else 170),
                            usage={}, finish="stop", sent=settings)
        self.n += 1
        if self.always_bad or (self.bad_every and self.n % self.bad_every == 0
                               and "could not be read" not in text):
            return mx.Reply(text="hmm, not sure", usage={}, finish="stop", sent=settings)
        convo = "\n".join(m["content"] for m in messages)
        objects = re.findall(r"New machine\. Its objects are: (.+?)\.\n", convo)[-1].split(", ")
        remaining = nx.hypotheses(objects)
        # replay this machine's tests and results
        tail = convo[convo.rfind("New machine."):]
        tests = re.findall(r"TEST: (.+)", "\n".join(m["content"] for m in messages if m["role"] == "assistant"))
        results = re.findall(r"the machine (LIT UP|did NOT light up)", tail)
        for t, r in zip(tests, results):
            placed = frozenset(x.strip() for x in t.split(","))
            remaining = [(n, ru) for n, ru in remaining
                         if nx.Machine(tuple(objects), n, ru).lights(placed) == (r == "LIT UP")]
        if len(remaining) == 1 or len(tests) >= nx.MAX_TESTS:
            nex, rule = remaining[0]
            return mx.Reply(text=f"ANSWER: nexioms = {', '.join(sorted(nex))}; needs = "
                                 f"{'one' if rule == 'disjunctive' else 'two'}", usage={}, finish="stop", sent=settings)
        subsets = nx.nonempty_subsets(objects)
        best = min(subsets, key=lambda s: (max(sum(nx.Machine(tuple(objects), n, ru).lights(s) for n, ru in remaining),
                                               len(remaining) - sum(nx.Machine(tuple(objects), n, ru).lights(s) for n, ru in remaining)),
                                           len(s), sorted(s)))
        return mx.Reply(text=f"Let me test.\nTEST: {', '.join(sorted(best))}", usage={"input_tokens": 1, "output_tokens": 1},
                        finish="stop", sent=settings)


def run(fake, memory, kind, seed, tmp: Path):
    mx_chat = mx.chat
    h.mx.chat = fake
    try:
        log = h.Log(tmp / "calls.jsonl")
        p = h.run_sequence(log, tmp / "seqs", "fake", {"vendor": "fake", "model": "fake"}, memory, kind, seed)
        return json.loads(p.read_text())
    finally:
        h.mx.chat = mx_chat


def test_sequences() -> None:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for memory in h.MEMORY:
            for kind in nx.SEQUENCE_RULES:
                for seed in range(3):
                    rec = run(FakeModel(bad_every=4), memory, kind, seed, tmp)
                    for i, m in enumerate(rec["machines"]):
                        ok = m["answer"] and m["answer"]["nexioms"] == m["truth"]["nexioms"] \
                            and m["answer"]["rule"] == m["truth"]["rule"]
                        check(bool(ok), f"{memory}-{kind}-{seed} machine {i}: adaptive fake model not correct")
                        check(len(m["tests"]) <= nx.MAX_TESTS, "test budget exceeded")
                        check(m["outcome"] == "answered", f"{memory}-{kind}-{seed} machine {i}: {m['outcome']}")
                        training = i < 3
                        check(("feedback" in m) == (training and memory != "M0"), f"{memory} feedback placement")
                        check(("note" in m) == (training and memory == "M1"), f"{memory} note placement")
                        if "feedback" in m:
                            check("one" not in m["feedback"] and "two" not in m["feedback"]
                                  and "needs" not in m["feedback"], "feedback leaks the rule")
                        if "note" in m:
                            check(m["note"]["rewrites"] == 1 and m["note"]["first_draft_words"] > h.NOTE_WORD_CAP
                                  and not m["note"]["truncated"], "over-length note not sent back for rewrite")
                    pre = [m["preamble_chars"] for m in rec["machines"]]
                    if memory == "M0":
                        check(all(p == 0 for p in pre), "M0 got a preamble")
                    else:
                        check(pre[0] == 0 and all(p > 0 for p in pre[1:]), f"{memory} preamble missing")
                    if memory == "M2":
                        last_open = rec["machines"][3]["messages"][0]["content"]
                        check(last_open.count("Machine 1:") == 1, "M2 record nests earlier machines")
        # a rewrite that is still over the cap is cut at the cap
        rec = run(FakeModel(obey_rewrite=False), "M1", "CC", 98, tmp)
        notes = [m["note"] for m in rec["machines"] if "note" in m]
        check(all(n["truncated"] and n["words_written"] > h.NOTE_WORD_CAP for n in notes)
              and all(len(m["note"]["text"].split()) == h.NOTE_WORD_CAP for m in rec["machines"] if "note" in m),
              "cap not enforced after a failed rewrite")
        # two unreadable replies in a row end the machine as a parse failure
        rec = run(FakeModel(always_bad=True), "M0", "CC", 99, tmp)
        check(all(m["outcome"] == "parse_failure" and len(m["parse_errors"]) == 2 for m in rec["machines"]),
              "parse-strike rule")
        calls = (tmp / "calls.jsonl").read_text().splitlines()
        check(all("settings_sent" in json.loads(c) for c in calls), "call log missing settings_sent")


if __name__ == "__main__":
    test_parser()
    test_sequences()
    print("PASS" if not FAILS else "FAIL:\n  " + "\n  ".join(sorted(set(FAILS))))
    sys.exit(0 if not FAILS else 1)
