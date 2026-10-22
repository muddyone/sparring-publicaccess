# Result: stopped at the baseline, by the pre-registered rule (2026-10-17)

**The study stopped at Stage 0b.** Without any memory, all three models solved every "needs two"
test machine: 20 of 20 each. The pre-registered stop rule (design note §5.3, added at lock before
any baseline data) halts the study when the mean baseline is 0.80 or more. A 20-point gain from
notes would then need more than 100%, so the notes question cannot be asked on this task. The
main run did not happen.

## The baseline

Stage 0b: M0 (no memory) × CC ("needs two" machines), 20 fresh sequences per model, scored by
`scripts/baseline.py`, written before the run. Gemini was dropped before scoring (deviation D1).

| model | test machine correct | parse failures |
|---|---|---|
| `claude-opus-5-5` | 20 / 20 | 0 |
| `gpt-6.1-sol` | 20 / 20 | 0 |
| `grok-4.7` | 20 / 20 | 0 |
| **mean p₀** | **1.00**, so the study stops (§5.3) | |

Record: `runs/baseline/baseline.json`, `runs/baseline/seqs/`, `runs/baseline/calls.jsonl`.

**Descriptive, not pre-registered as a measure.** Under M0 every machine in a sequence is an
independent test, so all 80 machines per model can be counted:

| model | all machines correct | rule type correct | tests used, mean (range) |
|---|---|---|---|
| Claude | 80 / 80 | 80 / 80 | 4.94 (4–5) |
| GPT | 79 / 80 | 80 / 80 | 5.36 (4–6) |
| Grok | 80 / 80 | 80 / 80 | 5.12 (3–6) |

The random explorer (§7) scores about 56% on these machines and the adaptive explorer 100% in at
most 5 tests. GPT's one miss was the nexiom pair, not the rule.

## What it means

**These models show no disjunctive bias on this task.** All three inferred the "needs two" rule
from their own experiments every time: 240 of 240 machines. Earlier work found language-model
agents infer "needs two" rules poorly
([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)), with the gap persisting in gpt-5
([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)). Either the gap has
closed in these newer models, or this task removes what caused it. The second is a live
possibility, and it is the main limit on reading this result:

- **The prompt names both rules.** It says exactly two objects are nexioms and that a machine
  needs one or both. That hands the model the hypothesis space. Whether the earlier studies told
  their models the possible rules has not been checked, and must be before comparing.
- **The models chose their own tests,** with up to 6 and a strategy that always works within 5.
  On this task, finding the rule is within reach of careful reasoning on a single machine. There
  is no room for experience across machines to add anything.

**The notes question is still open.** Whether notes carry a rule from one task to the next can't
be tested where a model already gets every machine right. A follow-up would need a task where the
baseline leaves room. Options: not naming the possible rules, giving fewer tests than an ideal
strategy needs, or using a rule a model doesn't solve from scratch. Any follow-up would be a new
pre-registration, not a continuation of this one.

## Cost

Stage 0b cost $9.78 (Claude $5.15, GPT $0.79, Grok $3.85), against the $8 estimate. Stage 0's
plumbing run was spent earlier (§13). The main run, estimated at about $186, was not spent.
