#!/usr/bin/env python3
"""Free check before the 4-test probe: does a 4-test budget make the rule worth knowing?

Exact game-tree search over the locked simulator's hypothesis space (6 objects, 15 pairs x 2
rules). With a uniform prior over the hypotheses still possible, an ideal explorer's success
chance with k tests left is the best test's outcome-weighted chance, ending at 1/|S| when it
must guess. Reported for budgets 3 to 6, (a) not knowing the rule (30 hypotheses) and (b)
knowing it (15 pairs, one rule). If (b) reaches 100% at 4 tests and (a) does not, a 4-test
budget rewards carrying the rule over from earlier machines.
"""
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "gopnik-memory-overhypothesis-2026-10-16" / "scripts"))
import nexiom as nx  # noqa: E402

OBJ = tuple("abcdef")
HYP = nx.hypotheses(OBJ)
TESTS = nx.nonempty_subsets(OBJ)
LIT = {(i, t): nx.Machine(OBJ, n, r).lights(t) for i, (n, r) in enumerate(HYP) for t in TESTS}


@lru_cache(maxsize=None)
def value(S: frozenset, k: int) -> float:
    if len(S) <= 1:
        return 1.0
    if k == 0:
        return 1 / len(S)
    best = 0.0
    for t in TESTS:
        yes = frozenset(i for i in S if LIT[(i, t)])
        no = S - yes
        if not yes or not no:
            continue
        v = (len(yes) * value(yes, k - 1) + len(no) * value(no, k - 1)) / len(S)
        best = max(best, v)
        if best == 1.0:
            break
    return best or 1 / len(S)


if __name__ == "__main__":
    every = frozenset(range(len(HYP)))
    for k in range(3, 7):
        row = [f"{k} tests: rule unknown {value(every, k):6.1%}"]
        for r in nx.RULES:
            S = frozenset(i for i, (_, rr) in enumerate(HYP) if rr == r)
            row.append(f"knows {r} {value(S, k):6.1%}")
        print("   ".join(row))
