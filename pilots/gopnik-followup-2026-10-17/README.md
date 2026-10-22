# Gopnik follow-up: calibration for a harder task (2026-10-17)

**Exploratory, not a pre-registration.** The locked pilot
(`../gopnik-memory-overhypothesis-2026-10-16/`) stopped because every model solved every "needs
two" machine without memory. This calibration looked for a variant hard enough to leave room,
targeting a no-memory accuracy of roughly 25–60% on "needs two" (CC) sequences. Seeds 40M+, never
to be reused.

Variants (`scripts/calibrate.py`): **A** rules named, 5 tests · **B** rules not named, 6 tests,
rule read from a probe question · **C** rules not named, 5 tests. 10 CC and 5 DD sequences of 4
machines per model per variant.

## Result: no variant leaves enough room

Machines fully correct (both nexioms and the rule), no memory:

| Variant | Claude Opus 5.5 CC | GPT-6.1 Sol CC | Grok 4.7 CC |
|---|---|---|---|
| A named, 5 tests | 40/40 | 40/40 | 37/40 |
| B unnamed, 6 tests | 34/40 | 34/40 (6 parse failures) | 4/4 (incomplete) |
| C unnamed, 5 tests | 30/40 (75%) | 32/40 (80%) | not run |

Even the hardest variant sits at 75–80%, far above the 25–60% target. "Needs one" (DD) machines
were similar. Removing the named rules and tightening the test budget cost the models a little,
not enough. A follow-up that can show notes carrying a rule needs a different kind of difficulty
(for example more objects, noisy machines, or rules beyond one-or-two), not a tighter version of
this one.

**Grok incomplete:** 29 Grok sequences (most of B and all of C) failed. A few timed out; the rest
hit the xAI account's credit or monthly spending limit (HTTP 403). Not re-run.

**Cost:** about $25.14 (Claude $14.19, GPT $2.83, Grok $8.12), computed from `runs/calibration/calls.jsonl`.

Per-cell counts: `runs/calibration/calibration.json`.

---

## Probe 2: a 4-test budget, with and without notes (2026-10-17, exploratory)

**Why 4 tests.** `scripts/budget_sim.py` (exact search, no API cost) shows that with 4 tests an
ideal explorer gets 53% of machines right without knowing the rule and 93% knowing it. So a
4-test budget leaves a 40-point gap that only a rule carried over from earlier machines can close.

**Run** (`scripts/probe4.py`): the locked harness unchanged except for the budget. M0 (no memory)
and M1 (feedback naming the nexioms, never the rule, then a note of at most 150 words), 10 CC and
5 DD sequences each, Claude Opus 5.5 and GPT-6.1 Sol, seeds 50M+. Cost about **$10.29** (Claude
$8.68, GPT $1.61).

| | Machines 1–4, no notes (CC) | Test machine, no notes (CC) | Test machine, notes (CC) | Test machine, notes (DD) |
|---|---|---|---|---|
| Claude | 19/40 (48%) | 7/10 | 7/10 | 0/5 (2/5 without) |
| GPT | 22/40 (55%) | 5/10 | 7/10 | 1/5 (1/5 without) |

Rule right on the test machine: 10/10 or 9/10 in every CC cell. No parse failures.

**What it shows.**
1. **The paradigm finally has room.** Without notes the models score 48–55%, right at the 53%
   an ideal explorer gets without the rule. They play the single machine about as well as it can
   be played.
2. **Notes did not carry the rule.** No reliable gain on the test machine (7 vs 7; 7 vs 5 at
   n = 10 is noise), and none on DD.
3. **The reason is in the notes, and it is the interesting result.** Read one by one, the CC notes
   are careful *strategy* notes: "track all 30 hypotheses (15 pairs × 2 rules)", "split evenly",
   "accept a final coin flip". Every one keeps the rule open. Only 2 of 10 Claude notes remark that
   all three machines needed two, and one of those adds "Still test for it". None of the 10 GPT
   notes treats the run of "needs two" machines as evidence about the next. The models remembered
   *how to explore*; they declined to form the overhypothesis "these machines need two", which is
   exactly what Gopnik's children do.

**The confound to resolve before reading too much into it.** The locked prompt says "Each machine
works one of two ways", which tells the model each machine is a fresh draw. Refusing to generalize
is then the *correct* reading of the instructions. Children in the overhypothesis studies are not
told that. A next probe would remove that line, or say the machines come from one maker, and see
whether the notes start carrying the rule.

Per-cell counts: `runs/probe4/probe4.json`. Notes and transcripts: `runs/probe4/seqs/`.

---

## Probe 2b: the same, with "The machine" instead of "Each machine" (2026-10-17, exploratory)

Same seeds, models, budget and conditions as probe 2. The only change is one word in the locked
prompt: "Each machine works one of two ways" became "The machine works one of two ways", so the two
rules are still stated but nothing says they vary between machines (`probe4.py --singular`). Cost
about **$10.35** (Claude $8.73, GPT $1.62).

| | Test machine, no notes (CC) | Test machine, notes (CC) | Test machine, notes (DD) |
|---|---|---|---|
| Claude | 5/10 | 6/10 | 2/5 (3/5 without) |
| GPT | 5/10 | 7/10 | 2/5 (2/5 without) |

**The wording made no difference.** The notes again keep the rule open: GPT's still begin "track
all 30 hypotheses (15 pairs × two rules)". Of Claude's 10 CC notes, one keeps a tally ("needs two
twice") and says to "lean toward two in a cross-rule tie". Claude's DD notes notice that the rule
was "one" every time but add "each time proven by tests, not assumed".

**Both probes together**, CC test machine: with notes 27/40 (68%), without 22/40 (55%). That gap
is within chance at this size, and far below the 93% an explorer carrying the rule could reach.

**Reading.** The models can carry information across machines (their notes record each machine's
rule and a detailed strategy), but they do not turn a run of "needs two" machines into an
expectation for the next one. They behave like careful statisticians treating every machine as
independent, not like Gopnik's children, who form the overhypothesis from a few examples. The
prompt's wording was not the cause. Still exploratory (n = 10 per cell), and the prompt still names
both rules on every machine, which may itself keep both in play.

---

## Probe 2c: the rules never named (2026-10-17, exploratory)

Same seeds, models, budget and memory conditions as probes 2 and 2b. The prompt is calibration
variant C's: "The machine responds to its nexioms in a fixed way that you have to discover." Neither
rule is mentioned. The model names the two nexioms, then answers one probe question ("with only X on
it, would it light up?") that gives its rule without offering options (`probe4.py --unnamed`).
Cost about **$13.48** (Claude $11.06, GPT $2.43).

| | Machine 1 | Machine 2 | Machine 3 | **Test machine** |
|---|---|---|---|---|
| Claude, no notes (CC) | 3/10 | 1/10 | 6/10 | **2/10** |
| Claude, notes (CC) | 4/10 | 3/10 | 9/10 | **10/10** |
| GPT, no notes (CC) | 5/10 | 3/10 | 3/10 | **6/10** |
| GPT, notes (CC) | 6/10 | 4/10 | 6/10 | **8/10** |

"Needs one" (DD) test machine: Claude 4/5 with notes, 3/5 without; GPT 4/5 and 3/5.

**This reverses the reading of probes 2 and 2b, for Claude.**
- **Claude with notes got every "needs two" test machine right, against 2 of 10 without**
  (paired McNemar test, 8 machines wrong-to-right and none the other way, p ≈ 0.008 two-sided;
  _corrected 2026-10-17: first given as one-sided Fisher exact p ≈ 0.0004, which treats the two
  conditions as independent, but they ran on the same machines (10 of 10 sequences match)_). The gain builds across the sequence: 4, 3, 9, 10.
- **Every one of Claude's 10 CC notes states the overhypothesis** (_reanalysis: 9 of 10 state it as
  an expectation for the next machine; the tenth records the run but only advises confirming_), in its own words: "AND again,
  for the third machine in a row. AND is likely, but keep checking OR and XOR"; "Treat 'both
  needed' as the default rule"; "treat AND as the default (about 80%+)". It then plans its tests
  around it.
- **GPT mostly does not.** Its notes record what each machine did and advise tracking rules and
  pairs jointly; one DD note says outright "Do not carry identities or rules across machines". Its
  8 vs 6 is within chance.

**What changed between probes.** When the prompt named both rules on every machine, both models
treated the rule as open each time and notes gave no gain. When the rule had to be discovered,
Claude formed the cross-machine expectation and its notes carried it, much as Gopnik's children do.
Naming the options on every machine appears to have kept them equally live. The earlier summary,
that the models "act like careful statisticians treating every machine as independent", holds only
for the named-rules framing and for GPT.

**Limits.** One task, two models, 10 sequences per cell, exploratory, not pre-registered. The
unnamed prompt also widens what the models consider (several of Claude's notes keep "exactly one",
XOR, in play), which lowers its no-notes baseline (2/10) and so enlarges the room notes can fill. A
claim for publication needs a locked replication on fresh seeds.

## Reanalysis after panel review (2026-10-17)

From Vera Tukey's measurement check (`docs/research/what-ai-is/panel/2026-10-17-piece-01/3-vera.md`),
which recounted probe 2c from the per-machine records and read all 20 final-machine notes.

- **"Correct" means both the pair and the rule.** Without notes, Claude named the rule correctly on
  8 of 10 final "needs two" machines (30 of 40 across all machines) but found the right pair only
  4 of 10 (19 of 40 overall), and got both right 2 of 10 (12 of 40). The no-notes deficit is the
  pair, not the rule. _Corrected 2026-10-20: the pair counts first given here, 2 of 10 and 12 of
  40, were the counts for pair and rule together._
- **What the notes changed is how Claude explored.** With notes, all 10 runs opened the final
  machine with a four-block test, the best first move if you expect "needs two"; without notes,
  all 10 opened with three blocks. So the result shows a carried rule making exploration
  efficient, not a "needs two" bias being overcome.
- **Sequence of designs.** Probe 2c was the third version tried (after probes 2 and 2b, and three
  calibration variants), each designed from the previous result. Against roughly six comparable
  final-machine comparisons, the paired p ≈ 0.008 is borderline under a strict correction.
- **The 53%/93% reference figures assume two named rules.** With three rules in play, as in the
  unnamed framing, an ideal explorer who doesn't know the rule gets about 36% in four tests
  (`scripts/budget_sim3.py`); Claude's no-notes rate was 30%.
- **No reversal test.** Whether the carried expectation gives way when the pattern changes was not
  tested. Two of Claude's notes tell it to answer the closing question by the rule rather than the
  evidence.
- **Feedback plus notes.** After each machine, the notes condition was told which blocks were
  right; the no-notes condition was not. "Notes" here means feedback carried in notes.
- **Unblinded.** The notes were read by one Claude session, not coded blind.
