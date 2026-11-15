# A harder fact pattern: recall discriminates, and the structured walk collapses

**Status: exploratory. Second fact pattern, three generator configurations, 5 runs each,
k=2. This is the run that shows the earlier recall ceiling was a property of the CORPUS,
not of the measure.**
Companion to [`key-relative-scores.md`](./key-relative-scores.md) (the easy pattern).
Raw: `runs/july-2019-decedents-estates-conflict-of-laws.key-relative-scores.json`.

---

## Why this pattern

**July 2019 — Decedents' Estates / Conflict of Laws.** The hardest available in the corpus:
6 weighted points (against a median of 4) and **cross-subject**, so a generator that reads
it as an estates problem can miss the conflict-of-laws half outright — the failure recall
should be able to see and could not on a single-subject question.

Volume-matched rungs were deliberately left out. They cost quality and gained no recall on
the easy pattern, so re-running them here would re-confirm a finding rather than test a new
one.

## Result

```
rung   items  recall  yield  noise  redun  offkey  ctrl   configuration
g1        34    0.98   0.45   0.26   0.31    0.17  0.97   gpt-5.2, natural
g3        19    1.00   0.68   0.06   0.27    0.17  1.00   claude-opus-4-8, natural
g4         7    0.35   0.34   0.64   0.03    0.05  0.43   structured taxonomy walk
```

Missed key points: **g1** missed (6) in at least one run; **g4** missed (1), (3), (4), (5)
and (6).

## 1. Recall discriminates. The ceiling was the corpus.

0.35 / 0.98 / 1.00 — a 65-point spread, where the easy pattern gave 1.00 across all five
configurations. **The obscurity-stratified recall endpoint named in
[`design-note.md`](./design-note.md) §5 is measurable after all**; it just cannot be
measured on a tractable problem.

That reverses the recommendation from the easy pattern. Recall is not a dead axis — it is a
*difficulty-gated* one, and the corpus contains problems on both sides of the gate.

## 2. The structured walk collapses — and the reason is specific

It found **35% of the weighted key** and 64% of what it emitted was unsound or not raised
by the facts. Its actual output:

```
Meaning and legal consequences · Basic concepts · Application in specific areas
Execution requirements · Will contests · Share of children and more remote descendants
```

These are real NCBE taxonomy nodes, and they are **abstract to the point of uselessness for
issue-spotting**. "Basic concepts" cannot address the specific question the fact pattern turns on.

**The taxonomy's granularity is wildly uneven across subjects.** Family Law nodes are
specific and near-actionable — *Premarital contracts*, *Division of property* — which is why
the walk scored recall 1.00 there. Conflict of Laws and Decedents' Estates nodes are
abstract headings, and the same mechanism scores 0.35.

So the structured enumerator's value is **bounded by the local granularity of its
taxonomy**, and that granularity is not a property anyone controls. This is a serious
negative for the rung the ladder was resting on: with human evaluation unavailable and the
cross-vendor pass worth nothing over a rerun, the structured walk was the remaining
independent generator, and it works only where its map happens to be drawn finely.

Its one surviving virtue is redundancy **0.03** — it does not restate itself. That is
structural (a node cannot be raised twice) and it is not worth much on its own.

## 3. Claude at natural restraint holds across both patterns

| | items | recall | yield | noise |
|---|---|---|---|---|
| easy pattern | 22 | 1.00 | 0.79 | 0.06 |
| **hard pattern** | **19** | **1.00** | **0.68** | **0.06** |

Full recall on both, identical noise rate, on the smallest output of any free generator.
`gpt-5.2` by contrast dropped to 0.98 recall and its noise rose 0.15 → 0.26 on the harder
problem. Two fact patterns is not a result, but the profile is consistent and worth
tracking.

**Off-key rose for both free generators** (0.02–0.04 → 0.17). A harder problem produces
more sound-and-material content the examiners did not grade, which is the direction the
coverage question cares about.

## 4. A prediction I got wrong, recorded

Before the run I expected the answer-key point I judged conceptually hardest to be the one that fell.

Both free generators found it. `gpt-5.2` instead missed a different point, one that carried less weight in the key.
The failure was not at the conceptually hard end. (The points' content and weights are withheld; see the archive
README, "Withheld material".)

## 5. The positive control was confounded with recall

Recorded as deviation D13. The control asked, for **every** key point, whether at least one
item cited as covering it was rated sound + raised + material by the blind judge. A point a
generator never covered has no citing items and can never pass — so low recall drags the
control down regardless of judge quality:

```
rung   recall   ctrl   difference
g1       0.98   0.97    -0.01
g3       1.00   1.00    +0.00
g4       0.35   0.43    +0.08
```

It was carrying almost no independent information. It now scores **only over the points the
run actually covered**: *where this generator claims to have found something, does a judge
that never saw the key agree it is real and material?*

**g4's yield remains suspect, but for a sound reason rather than the confounded one:** its
noise rate of 0.64 does not route through the control at all.

## 6. What this cannot do

- **Two fact patterns.** Everything here is directional.
- The uneven-taxonomy finding is one subject pair; it predicts that the walk's performance
  varies by subject, which is testable and untested.
- k = 2, against the design's k = 5.
- No perturbation contrast, so competence and contamination remain entangled.
- Off-key rests on a blind judge with no gold to check it against.
