#!/usr/bin/env python3
"""The simulator's two controls (design note §7). Run before any model touches the machine.

Settings: 6 objects, 6 tests, 30 possible answers (15 pairs x 2 rules). Adopted 2026-10-16 after
the first draft's 4 objects / 8 tests let a random explorer score 95% (design note §12).

POSITIVE CONTROL: the adaptive explorer. Before each test it picks the placement that splits the
answers still possible as evenly as it can (ties broken by fewer objects, then name order, so it is
deterministic), then answers with the only one left. It MUST score 100% within the 6-test budget.
Checked two ways: over all 30 answers on one object set (identifiability, proved by enumeration;
it needs at most 5 tests), and over 10,000 generated machines per rule (generator and scorer, end
to end). Anything short of 100% means the simulator is wrong and nothing else in the study is
readable. Testing every pair would take 15 tests on 6 objects, so the first draft's all-pairs
explorer no longer fits the budget.

CHANCE FLOOR: the random explorer. It places 6 distinct non-empty subsets drawn uniformly from the
63 possible, then answers with one drawn uniformly from the answers consistent with what it saw. It
uses its outcomes, so it does far better than blind guessing (1 in 30); that is why the floor is
simulated rather than hard-coded (review finding R10).

THE SIMULATOR CHECK. The random explorer's exact expected accuracy can be enumerated, but not at
6 objects: C(63,6) is 67.9 million test sets per answer. So the same code is run on a 4-object,
4-test machine, where C(15,4) = 1,365 test sets make exact enumeration cheap, and the simulation
there is compared with the exact value. The generator, machine and scorer are the same code at
any size, so agreement at 4 objects validates the code that produces the 6-object floor. If the
two disagree by more than 4 standard errors, the script fails.

Writes runs/controls.json. Exit 0 only if every check passes.

Usage:
  ./controls.py [--n 10000] [--seed 20261016]
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nexiom as nx  # noqa: E402

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / "runs"

CHECK_OBJECTS, CHECK_TESTS = 4, 4   # the size at which the exact value is enumerable


# ---------------------------------------------------------------- explorers

def adaptive_explorer(machine: nx.Machine, budget: int = nx.MAX_TESTS):
    """Pick each test to split the remaining answers; answer the one left (None if not unique)."""
    subsets = nx.nonempty_subsets(machine.objects)
    remaining = nx.hypotheses(machine.objects)
    obs = []
    while len(remaining) > 1 and len(obs) < budget:
        def score(s):
            lit = sum(1 for nex, rule in remaining
                      if nx.Machine(machine.objects, nex, rule).lights(s))
            return (max(lit, len(remaining) - lit), len(s), sorted(s))
        test = min(subsets, key=score)
        lit = machine.lights(test)
        obs.append((test, lit))
        remaining = [(nex, rule) for nex, rule in remaining
                     if nx.Machine(machine.objects, nex, rule).lights(test) == lit]
    answer = remaining[0] if len(remaining) == 1 else None
    return answer, len(obs), len(remaining)


def random_explorer(machine: nx.Machine, rng: random.Random, budget: int = nx.MAX_TESTS):
    """Place `budget` distinct random non-empty subsets; answer uniformly among consistent."""
    tests = rng.sample(nx.nonempty_subsets(machine.objects), budget)
    obs = [(t, machine.lights(t)) for t in tests]
    cands = nx.consistent(machine.objects, obs)
    return rng.choice(cands), len(obs), len(cands)


# ---------------------------------------------------------------- statistics

def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (centre - half, centre + half)


def exact_random(rule: str, n_objects: int, budget: int) -> dict:
    """Exact expected accuracy of the random explorer for one rule, by full enumeration."""
    objects = tuple("abcdefgh"[:n_objects])
    subsets = nx.nonempty_subsets(objects)
    test_sets = list(itertools.combinations(subsets, budget))
    both = nex_only = rule_only = Fraction(0)
    truths = [(p, r) for p, r in nx.hypotheses(objects) if r == rule]
    for nex, r in truths:
        m = nx.Machine(objects=objects, nexioms=nex, rule=r)
        for tests in test_sets:
            cands = nx.consistent(objects, [(t, m.lights(t)) for t in tests])
            k = len(cands)
            both += Fraction(sum(1 for c in cands if c == (nex, r)), k)
            nex_only += Fraction(sum(1 for c in cands if c[0] == nex), k)
            rule_only += Fraction(sum(1 for c in cands if c[1] == r), k)
    total = len(truths) * len(test_sets)
    return {"both": float(both / total), "nexioms_only": float(nex_only / total),
            "rule_only": float(rule_only / total), "test_sets": len(test_sets),
            "truths": len(truths)}


# ---------------------------------------------------------------- checks

def check_identifiability() -> dict:
    """All 30 answers on one object set: the adaptive explorer must name each within budget."""
    objects = tuple("abcdef"[:nx.N_OBJECTS])
    ok, worst = [], 0
    for nex, rule in nx.hypotheses(objects):
        m = nx.Machine(objects=objects, nexioms=nex, rule=rule)
        answer, n_tests, _ = adaptive_explorer(m)
        worst = max(worst, n_tests)
        ok.append(answer is not None and m.correct(*answer) and n_tests <= nx.MAX_TESTS)
    return {"hypotheses": len(ok), "identified": sum(ok), "max_tests_used": worst,
            "pass": all(ok)}


def check_sequences(n: int = 500) -> dict:
    """Generated sequences have the right rules, fresh names, and reproduce from their seed."""
    problems = []
    for kind in nx.SEQUENCE_RULES:
        for seed in range(n):
            s = nx.make_sequence(kind, seed)
            if tuple(m.rule for m in s.machines) != nx.SEQUENCE_RULES[kind]:
                problems.append(f"{kind}/{seed}: wrong rules")
            if any(len(m.objects) != nx.N_OBJECTS for m in s.machines):
                problems.append(f"{kind}/{seed}: wrong object count")
            names = [o for m in s.machines for o in m.objects]
            if len(names) != len(set(names)):
                problems.append(f"{kind}/{seed}: a name repeats within the sequence")
            if any(len(m.nexioms) != 2 or not m.nexioms <= set(m.objects) for m in s.machines):
                problems.append(f"{kind}/{seed}: bad nexiom pair")
            if nx.make_sequence(kind, seed).machines != s.machines:
                problems.append(f"{kind}/{seed}: not reproducible from its seed")
    return {"sequences": n * len(nx.SEQUENCE_RULES), "problems": problems[:10],
            "pass": not problems}


def run_explorer(name: str, rule: str, n: int, rng: random.Random,
                 n_objects: int = nx.N_OBJECTS, budget: int = nx.MAX_TESTS) -> dict:
    both = nex_ok = rule_ok = 0
    tests_used = []
    for _ in range(n):
        m = nx.make_machine(rng, rule, n_objects=n_objects)
        if name == "adaptive":
            answer, n_tests, _ = adaptive_explorer(m, budget)
        else:
            answer, n_tests, _ = random_explorer(m, rng, budget)
        tests_used.append(n_tests)
        if answer is not None:
            both += m.correct(*answer)
            nex_ok += answer[0] == m.nexioms
            rule_ok += answer[1] == m.rule
    lo, hi = wilson(both, n)
    return {"n": n, "objects": n_objects, "budget": budget, "correct": both,
            "accuracy": both / n, "ci95": [lo, hi], "nexioms_only": nex_ok / n,
            "rule_only": rule_ok / n, "max_tests_used": max(tests_used)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=10_000, help="machines per rule per explorer")
    ap.add_argument("--seed", type=int, default=20261016)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    out: dict = {"seed": args.seed, "n_per_rule": args.n, "objects": nx.N_OBJECTS,
                 "max_tests": nx.MAX_TESTS, "blind_guess_floor": 1 / len(nx.hypotheses(range(nx.N_OBJECTS)))}

    out["identifiability"] = check_identifiability()
    out["sequences"] = check_sequences()
    out["adaptive"] = {r: run_explorer("adaptive", r, args.n, rng) for r in nx.RULES}
    out["random"] = {r: run_explorer("random", r, args.n, rng) for r in nx.RULES}
    out["simulator_check"] = {
        r: {"simulated": run_explorer("random", r, args.n, rng, CHECK_OBJECTS, CHECK_TESTS),
            "exact": exact_random(r, CHECK_OBJECTS, CHECK_TESTS)}
        for r in nx.RULES}

    checks = {
        "identifiability": out["identifiability"]["pass"],
        "sequences": out["sequences"]["pass"],
        "adaptive_100pct": all(out["adaptive"][r]["accuracy"] == 1.0 for r in nx.RULES),
        "adaptive_within_budget": all(out["adaptive"][r]["max_tests_used"] <= nx.MAX_TESTS
                                      for r in nx.RULES),
    }
    for r in nx.RULES:
        c = out["simulator_check"][r]
        sim, ex = c["simulated"]["accuracy"], c["exact"]["both"]
        se = math.sqrt(ex * (1 - ex) / args.n)
        c["z"] = (sim - ex) / se if se else 0.0
        checks[f"simulation_matches_exact_{r}"] = abs(sim - ex) <= 4 * se
    out["checks"] = checks
    out["pass"] = all(checks.values())

    RUNS.mkdir(exist_ok=True)
    (RUNS / "controls.json").write_text(json.dumps(out, indent=2) + "\n")

    idf = out["identifiability"]
    print(f"settings          {nx.N_OBJECTS} objects, {nx.MAX_TESTS} tests, {idf['hypotheses']} possible answers")
    print(f"identifiability   {idf['identified']}/{idf['hypotheses']} named by the adaptive explorer, at most {idf['max_tests_used']} tests")
    print(f"sequences         {out['sequences']['sequences']} generated, problems: {len(out['sequences']['problems'])}")
    for r in nx.RULES:
        a = out["adaptive"][r]
        print(f"adaptive   {r:<11} {a['accuracy']:.4f}  ({a['correct']}/{a['n']}, max tests {a['max_tests_used']})")
    for r in nx.RULES:
        s = out["random"][r]
        print(f"random     {r:<11} {s['accuracy']:.4f} [{s['ci95'][0]:.4f}, {s['ci95'][1]:.4f}]"
              f"  (nexioms {s['nexioms_only']:.3f}, rule {s['rule_only']:.3f})")
    print(f"blind guess       {out['blind_guess_floor']:.4f}")
    for r in nx.RULES:
        c = out["simulator_check"][r]
        print(f"sim check  {r:<11} {CHECK_OBJECTS} obj/{CHECK_TESTS} tests: simulated {c['simulated']['accuracy']:.4f}"
              f"  exact {c['exact']['both']:.4f}  z {c['z']:+.2f}")
    print("PASS" if out["pass"] else "FAIL: " + ", ".join(k for k, v in checks.items() if not v))
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
