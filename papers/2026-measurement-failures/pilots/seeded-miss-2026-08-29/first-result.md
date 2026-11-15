# First scored batch: the measure works, and the granularity problem is the binding constraint

> **SUPERSEDED by [`result.md`](./result.md)** (100 runs, 25 cases). Kept as the interim
> record. Its controls and its main finding held. Its one exploratory cut — first-instance
> tribunals recovering better than reviewing ones, 0.90 vs 0.50 — **did not**: at 100 runs
> the gap is 0.66 vs 0.64. That reversal is why the cut was labelled exploratory here.

**Status: exploratory, and UNDERPOWERED by its own pre-registration.** 52 scored runs over
13 cases; the neutral leakage stratum — the pre-registered headline — holds only 16 runs
over 4 cases, below the n≥20 floor set in [`design-note.md`](./design-note.md) §6. Reported
here as reconnaissance. A second batch is running.

Raw: `runs/seed-recovery-report.json`.

---

## What ran

Appellate opinions filed 2026-06-01 or later, holding that a tribunal below erred by failing
to consider something. Each split into a **situation** (the generator's only input, composed
blind), a **seed** (what was missed), and a **key** (what the tribunal did address). Two
fine-grained generators, two replicates each.

## The controls first, because they decide whether anything else is readable

| control | result | reading |
|---|---|---|
| **positive** — over key points a run covered, does the blind judge rate ≥1 covering item sound + raised + material? | **0.98** (floor 0.90) | PASS. The blind judge is reliable where a human answer exists. |
| **negative** — decoy seeds from other cases, scored in the same shuffled call, judged not applicable | **0.02** over n=152 | **CLEAN.** The seed judge does not endorse items for considerations that do not apply. |

The negative control is the one that mattered. It was built because the parent study's
sharpest failure was a sanity test that could only detect error in one direction; a generous
seed judge would have inflated every number below, and it would have looked like success.
At 0.02 it is not doing that. The four decoys the judge rated *applicable* recovered at
1.00 — those are generic considerations (make findings, state reasons) that genuinely do
apply to any case, and separating them is why the `applicable` field exists.

## The result

```
stratum       n    raw  offkey  absorb  decoy*
neutral      16   0.88    0.38    0.50    0.04
hinted       20   1.00    0.65    0.35    0.02
explicit     16   1.00    0.94    0.06    0.00
ALL          52   0.96    0.65    0.31    0.02
```

`raw` = any emitted item addresses the seed. `offkey` = such an item is *also* off-key
(sound, raised, material, non-duplicate, and matched to no key point) — **the measure under
validation**. `absorb` = the seed was addressed but every citing item was absorbed into the
key. `decoy*` = false-positive floor.

### 1. The leakage audit is validated by its own gradient

Off-key recovery rises monotonically with leakage: **0.38 → 0.65 → 0.94**. The more a
stimulus telegraphs its seed, the more reliably the generator recovers it. That is what
leakage *should* do, and it is the strongest available evidence that the audit is measuring
something real rather than sorting cases arbitrarily. It also vindicates the pre-registered
decision to headline the neutral stratum: pooling all 52 runs would report 0.65, and roughly
half of that is the stimulus handing over the answer.

### 2. Raw recovery is high; off-key recovery is not

In the neutral stratum the generators *addressed* the seed 88% of the time but produced an
**off-key** item addressing it only 38% of the time. The 0.50 gap is not a coverage failure.
It is **deviation D14 — the granularity problem — measured on independent data.**

The parent study inferred this effect from item-to-key-point ratios and could only say
recovery was "undefined" for coarse generators. Here it is counted: half the time the seed is
raised, the matcher also credits that same item against a key point, the exclusive-match rule
strips it from the off-key set, and the measure reports nothing found.

**This is the binding constraint on off-key as an instrument**, and it is now a number
rather than a caveat.

### 3. Both vendors, same story

| rung | items/run | raw | offkey | offkey (neutral only) |
|---|---|---|---|---|
| g1 gpt-5.2 | 64 | 1.00 | 0.69 | 0.38 |
| g3 claude-opus-4-8 | 22 | 0.92 | 0.62 | 0.38 |

Identical in the neutral stratum despite a **3× difference in output volume**. The parent
study's finding that expansion produces more output rather than more answer survives contact
with this corpus: gpt-5.2 emitted three times as many items and recovered the same share of
seeds.

### 4. Exploratory, not pre-registered: first-instance vs reviewing tribunals

| tribunal below | runs | cases | raw | offkey | share neutral |
|---|---|---|---|---|---|
| first-instance | 20 | 5 | 1.00 | 0.90 | 0.20 |
| reviewing | 32 | 8 | 0.94 | 0.50 | 0.38 |

Seeds from reviewing bodies (an intermediate appellate court, the BIA adopting an IJ, a court
on certiorari review) recover far less well. The likely mechanism is the one D1 was written
for: their seeds concern *how the earlier decision should have been reviewed*, so they need
the posture in the file, and the posture is exactly what the leakage audit reacts to. The two
effects are confounded here and this cut cannot separate them. **Flagged for corpus design,
not reported as a finding.**

## What this does not establish

- **Underpowered on the pre-registered headline.** 4 cases in the neutral stratum. The 0.38
  is a reconnaissance figure and could move substantially.
- **One case was dropped by a bug, not a criterion.** `10951893` failed all four runs on a
  key returned as strings rather than objects. Fixed; it re-scores in the next batch. Noted
  because a case lost to a crash and a case that scored zero are indistinguishable in a
  summary table, and that is exactly the confusion this study exists to avoid.
- **Selection remains inflationary** (§4.2): a miss reaches an appellate holding because it
  was arguable, preserved, briefed and consequential.
- **The seed's doctrine is usually mainstream.** What is outside the model ecosystem is that
  this consideration was decisive and overlooked *in this situation* — not the rule itself.

## What it points at

The pre-registered question was whether off-key discovery is a validated probe for ungraded
material. On this batch the answer is **conditionally yes, and the condition is granularity,
not blindness.** The generators find the missed consideration far more often than the off-key
measure reports, because the exclusive-match rule discards the evidence. That makes the fix
specified in the parent study — replace exclusive matching with partial credit — the next
concrete step rather than an open question.
