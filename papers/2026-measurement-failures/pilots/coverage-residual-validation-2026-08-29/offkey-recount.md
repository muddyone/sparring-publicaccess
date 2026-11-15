# Recount under partial-credit matching: the published off-key numbers were about right, and I was wrong about why they weren't

**Status: exploratory recount of already-published numbers. It corrects a prediction made in
the seeded-miss study, not the numbers in this one.**
Raw: `runs/*.offkey-recount.json`. Script: `scripts/recount_offkey.py`.

---

## What prompted it

The seeded-miss study
([`../seeded-miss-2026-08-29/result.md`](../seeded-miss-2026-08-29/result.md)) found that the
exclusive-match rule — an item counts for one thing only — badly undercounted recovery of a
seeded miss: 0.55 reported against 0.95 actual, with the entire 0.40 gap caused by the rule.

On that basis its §8 predicted that **this study's off-key rates were understated**, and
singled out the **0.49 structured-walk figure** as "the number most likely to be understated"
and one that "must not travel into a paper as written."

That prediction has now been tested. **It was wrong**, and the reason it was wrong is worth
more than the prediction would have been.

## How the recount works

Relaxing the rule wholesale is not available here. In the seeded-miss study there was a
*target* — one seed, and a decoy control to keep the judge honest. Off-key in this study is a
*residual* over everything emitted; counting every signal item as off-key just returns the
yield.

So the recount asks the question the exclusive rule was standing in for:

> For a signal item the matcher **did** credit to a key point, does that item raise material
> the key point does not cover?

Two passes, the second built to falsify the first:

- **Pass E** (claude-opus-4-8) must *name* the extra material in a short phrase. An
  unstated claim is not counted.
- **Pass F** (gpt-5.2 — a different vendor, and the same one that built the original match)
  receives those phrases **without knowing which item they came from** and asks whether each
  is on the key after all. Anything it matches is struck.

A claim survives only if one model can name the extra material and a second, looking at the
key alone, agrees it is not there.

## Result

```
fact pattern                  rung           excl  partial  delta  claimed  struck
February 2018 / Family Law    g1             0.03     0.06  +0.04     18.4    16.2
                              g1n            0.05     0.07  +0.03     14.4    12.8
                              g3             0.02     0.07  +0.06      7.0     5.8
                              g3n            0.03     0.05  +0.02     13.8    12.8
                              g4             0.16     0.16  +0.00      0.8     0.8
July 2019 / Decedents’ Est.   g1             0.15     0.20  +0.05      3.2     1.6
                              g3             0.18     0.26  +0.08      2.8     1.2
                              g4             0.03     0.03  +0.00      0.4     0.4
July 2020 / Secured Trans.    g1             0.10     0.12  +0.02     13.6    13.0
                              g3             0.10     0.13  +0.04      7.6     7.0
                              g4             0.53     0.58  +0.04      1.6     1.2
                              g4collapse     0.32     0.32  +0.00      0.0     0.0
                              g4relabel      0.27     0.27  +0.00      0.0     0.0
```

**The correction is +0.00 to +0.08, median +0.04.** Nothing here resembles the 0.40 gap the
seeded-miss study found. The published off-key numbers are approximately right under the
corrected rule.

**The granularity ordering survives.** The structured walk's arms stay monotonic — 0.53 >
0.32 > 0.27 exclusive, 0.58 > 0.32 > 0.27 partial — so
[`taxonomy-granularity-finding.md`](./taxonomy-granularity-finding.md) does not change.

## 1. Why the same defect is severe in one study and negligible in the other

This is the substantive lesson, and it generalises past both studies.

**A targeted recovery measure and a population rate fail differently under the same rule.**

- The seeded-miss measure asks *"does any item address this one seed?"* — a binary question
  per case. One absorbed item destroys the signal entirely. The failure is all-or-nothing,
  which is why *Eqbal v. Blanche* scored 0.00 against a true 1.00.
- Off-key here is a *rate over everything emitted*, typically 9–56 items. Absorbing a handful
  moves a denominator of 34 by a few points and no more.

So "the exclusive-match rule is broken" is true, and "therefore every number computed with it
is badly wrong" does not follow. **The rule's damage scales with how concentrated the measure
is**, and off-key-as-a-rate is about as diffuse as a measure gets.

## 2. The guard is why this recount is trustworthy, and it nearly wasn't

Pass E claimed extra material at a startling rate — **18.4 claims per run** on February 2018
g1, on runs emitting 56 items. Pass F struck **16.2 of them**, about 88%.

Had the recount stopped at pass E, February 2018 g1's off-key would have gone from 0.03 to
roughly **0.36** — a twelve-fold "correction" that would have looked like a dramatic
vindication of the seeded-miss prediction, and would have been an artifact of a model asked
a leading question.

Struck rates run 75–94% wherever claims were made at volume. That is the ninth entry in
[`implications-for-the-proposer-paper.md`](./implications-for-the-proposer-paper.md) §4's catalogue, caught before
it was written down rather than after: **an instrument that produces a confident number
meaning something other than its name.** The only reason it is not in the table is that the
falsification pass was built into the recount from the start, on the strength of that
catalogue.

What the strike rate also says substantively: on this corpus, items the matcher credits to a
key point genuinely *are* restatements of that key point most of the time. The examiners'
key is exhaustive over graded material, so an item covering a key point rarely carries much
else. **The exclusive rule is approximately correct here** — not by luck, but because of a
property of the corpus that does not hold for the CourtListener seeds.

## 3. The real problem with the 0.49 is not the matching rule

While recounting, the same five runs of the same rung on the same fact pattern turned out to
have been scored three separate times, with identical models, identical `k=2`, and the
identical definition:

| artifact | g4 off-key |
|---|---|
| `runs/july-2020-secured-transactions.key-relative-scores.json` | **0.354** |
| `runs/july-2020-secured-transactions.granularity-arms.json` | **0.491** |
| this recount's exclusive column | **0.531** |

Same runs (9.4 items emitted in all three), same judges, three answers spanning **0.18**.

That spread is larger than every partial-credit correction in the table above, and it is
comparable to the entire range the granularity experiment reports across its three arms
(0.49 → 0.31 = 0.18). The seeded-miss study measured the same instability independently and
put it at ~5 points on a 20-run aggregate; on a 5-run aggregate it is evidently much worse.

**So the caution about the 0.49 stands, and the reason changes.** It should not travel into
any paper as a two-decimal figure — not because the matching rule understates it, but because
**the measure is not stable enough at k=2 and n=5 runs to support two decimal places.**

One nuance that protects the granularity finding: comparisons made **within a single scoring
pass** share the judge draw, and the arm ordering held in both passes that measured all three
arms. Cross-document comparison of levels is what this instability forbids.

## 4. What changes

- **In this study:** nothing. The published off-key rates stand, and the granularity finding
  stands. This document is added beside them.
- **In the seeded-miss study:** its §8 prediction that these numbers were understated is
  **retracted** and replaced with what was measured. `result.md` and the annotation on
  `implications-for-the-proposer-paper.md` §6 are corrected.
- **For the papers:** off-key rates from this study may be used as *directional, within-pass
  comparisons*. They may not be quoted as stable point estimates to two decimals, and any
  cross-document comparison of levels is unsupported.

## 5. What this does not establish

- Pass E and pass F are both models. Pass F's strikes are not human-verified; the guard
  removes a generosity that would otherwise be invisible, but it cannot prove the survivors
  are genuinely off-key.
- `k=2` throughout, matching the original scoring. Raising `k` is the obvious way to shrink
  the instability in §3 and was not done here — this recount deliberately reproduced the
  original conditions so the comparison isolates the matching rule.
- Three fact patterns, five runs per rung. The instability in §3 is measured on one rung of
  one pattern across three historical scorings, not designed as a reliability study.
