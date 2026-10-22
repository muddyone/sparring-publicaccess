#!/usr/bin/env python3
"""The nexiom machine: the environment every explorer in this study runs against.

One module, imported by the controls (controls.py) and, later, by the model harness, so a
scripted explorer and a model are scored by the same code against the same machines.

THE MACHINE. Six objects with fresh made-up names; a hidden pair of them are nexioms.

  disjunctive  lights if AT LEAST ONE nexiom is on it
  conjunctive  lights only if BOTH nexioms are on it

An explorer places a non-empty subset of the objects and is told "lit" or "not lit". The
answer it must give is the nexiom pair AND the rule. Test-machine correct (the primary DV,
design note §5.1) means both are right.

THE HYPOTHESIS SPACE is 15 pairs x 2 rules = 30. Every scorer here enumerates it rather than
reasoning about it, so "consistent with what was seen" is a set computation, not a judgment.

WHY NAMES ARE GENERATED, NOT CHOSEN. No stimulus in this study is written by hand, so none can
have been seen in training (design note §3). Names are pronounceable consonant-vowel strings
from a seeded generator; a fixed list of real words and the prior study's "blicket" family are
excluded so a name cannot carry meaning into the task.

Everything takes an explicit random.Random, so a seed reproduces a machine, a sequence, or a
whole run exactly.
"""
from __future__ import annotations

import itertools
import random
from dataclasses import dataclass, field

N_OBJECTS = 6
MAX_TESTS = 6
RULES = ("disjunctive", "conjunctive")

# Sequence kinds: three training machines, then the test machine (design note §4).
SEQUENCE_RULES = {
    "CC": ("conjunctive",) * 3 + ("conjunctive",),
    "DD": ("disjunctive",) * 3 + ("disjunctive",),
    "CD": ("conjunctive",) * 3 + ("disjunctive",),
}

_ONSETS = "bdfgklmnprstvz"
_VOWELS = "aeiou"
_CODAS = ("", "", "", "n", "r", "l", "k", "s")
# Names that read as words, or as the prior paradigm's vocabulary. Kept short on purpose:
# the generator's three-syllable shape already makes real words rare.
# (Settings: 6 objects, 6 tests, adopted 2026-10-16 after the first draft's 4 objects / 8 tests
# proved too easy; design note section 12.)
_EXCLUDED = {"blicket", "dax", "wug", "toma", "fep", "nexiom", "banana", "tomato", "potato"}


def make_name(rng: random.Random) -> str:
    """A pronounceable nonsense name, 3 syllables, e.g. 'veloran'."""
    while True:
        syll = [rng.choice(_ONSETS) + rng.choice(_VOWELS) for _ in range(3)]
        name = "".join(syll) + rng.choice(_CODAS)
        if name not in _EXCLUDED:
            return name


def make_names(rng: random.Random, n: int, avoid: set[str] | None = None) -> list[str]:
    """n distinct names, none in `avoid` (names already used in the same sequence)."""
    avoid = set(avoid or ())
    out: list[str] = []
    while len(out) < n:
        name = make_name(rng)
        if name not in avoid and name not in out:
            out.append(name)
    return out


@dataclass(frozen=True)
class Machine:
    objects: tuple[str, ...]          # display order, as an explorer sees them
    nexioms: frozenset[str]           # the hidden pair
    rule: str                         # "disjunctive" | "conjunctive"

    def lights(self, placed) -> bool:
        placed = frozenset(placed)
        if not placed or not placed <= set(self.objects):
            raise ValueError(f"a test must place a non-empty subset of {self.objects}, got {sorted(placed)}")
        hits = len(placed & self.nexioms)
        return hits >= 1 if self.rule == "disjunctive" else hits == len(self.nexioms)

    def correct(self, nexioms, rule: str) -> bool:
        """Test-machine correct: both the nexiom pair and the rule are right."""
        return frozenset(nexioms) == self.nexioms and rule == self.rule


def make_machine(rng: random.Random, rule: str, avoid_names: set[str] | None = None,
                 n_objects: int = N_OBJECTS) -> Machine:
    if rule not in RULES:
        raise ValueError(rule)
    objects = make_names(rng, n_objects, avoid_names)
    nexioms = frozenset(rng.sample(objects, 2))
    return Machine(objects=tuple(objects), nexioms=nexioms, rule=rule)


@dataclass
class Sequence:
    kind: str                         # "CC" | "DD" | "CD"
    seed: int
    machines: list[Machine] = field(default_factory=list)

    @property
    def training(self) -> list[Machine]:
        return self.machines[:-1]

    @property
    def test(self) -> Machine:
        return self.machines[-1]


def make_sequence(kind: str, seed: int) -> Sequence:
    """Four machines with the kind's rules. Names never repeat within a sequence, so nothing
    learned about an object can carry over; only the rule can."""
    rng = random.Random(seed)
    seq = Sequence(kind=kind, seed=seed)
    used: set[str] = set()
    for rule in SEQUENCE_RULES[kind]:
        m = make_machine(rng, rule, used)
        used |= set(m.objects)
        seq.machines.append(m)
    return seq


# ---------------------------------------------------------------- hypotheses and inference

def hypotheses(objects) -> list[tuple[frozenset[str], str]]:
    """All (nexiom pair, rule) hypotheses for a machine's objects: 30 at six objects."""
    return [(frozenset(p), r) for p in itertools.combinations(objects, 2) for r in RULES]


def consistent(objects, observations) -> list[tuple[frozenset[str], str]]:
    """Hypotheses that predict every observed (placed, lit) outcome."""
    out = []
    for nex, rule in hypotheses(objects):
        m = Machine(objects=tuple(objects), nexioms=nex, rule=rule)
        if all(m.lights(placed) == lit for placed, lit in observations):
            out.append((nex, rule))
    return out


def nonempty_subsets(objects) -> list[frozenset[str]]:
    return [frozenset(c) for k in range(1, len(objects) + 1)
            for c in itertools.combinations(objects, k)]
