# Scoring every generator against the examiners' key

**Status: exploratory. One fact pattern, five generator configurations, 5 runs each,
k=2. The recall column is uninformative here and says so; the yield columns are not.**
Method: [`scoring-design.md`](./scoring-design.md), applied per rung by
`scripts/score_all.py`. Replaces generator-to-generator comparison after that was found
ill-posed ([`comparison-layer-negative.md`](./comparison-layer-negative.md)).
Raw: `runs/february-2018-family-law.key-relative-scores.json`.

---

## Result

```
rung   items  recall  yield  noise  redun  offkey  ctrl   configuration
g1        56    1.00   0.47   0.15   0.33    0.03  1.00   gpt-5.2, natural verbosity
g1n       63    1.00   0.43   0.15   0.35    0.04  1.00   gpt-5.2, ~55-item budget
g3        22    1.00   0.79   0.06   0.14    0.02  1.00   claude-opus-4-8, natural
g3n       56    1.00   0.49   0.13   0.34    0.02  1.00   claude-opus-4-8, ~55-item budget
g4        13    1.00   0.63   0.18   0.09    0.17  1.00   structured taxonomy walk
```

`recall` = share of the examiners' **weighted** points found · `yield` = share of emitted
items that were sound + raised + material + non-duplicate · `ctrl` = positive control,
**1.00 on every rung**, so the yield figures are interpretable.

## 1. Recall ceilings at 1.00. This fact pattern cannot separate generators on recall.

Every configuration found every weighted point, in every run. A 13-item structured walk
scored the same recall as a 63-item exhaustive sweep.

That is a **finding about the corpus, not about the generators**: with five key points on a
fact pattern this tractable, recall has no headroom and no discriminating power. The
obscurity-stratified recall curve that the design named as its primary endpoint
([`design-note.md`](./design-note.md) §5) **cannot be measured here at all.**

The fix is harder problems, not more generators. Candidates already in the corpus: the
cross-subject questions (*Civil Procedure / Constitutional Law*, *Decedents' Estates /
Conflict of Laws*), and fact patterns whose keys carry more points. Adding rungs to the
ladder buys nothing while the measurement is at its ceiling.

## 2. Telling a model to be more exhaustive produces more output, not more answer.

This is the clearest result in the table, and it runs in both vendors:

| | items | recall | yield | noise | redundancy |
|---|---|---|---|---|---|
| claude, natural | 22 | 1.00 | **0.79** | **0.06** | **0.14** |
| claude, ~55 budget | 56 | 1.00 | 0.49 | 0.13 | 0.34 |
| gpt, natural | 56 | 1.00 | 0.47 | 0.15 | 0.33 |
| gpt, ~55 budget | 63 | 1.00 | 0.43 | 0.15 | 0.35 |

Pushed from 22 items to 56, `claude-opus-4-8` gained **no recall** — it already had
everything — and lost **30 points of yield**, doubled its noise rate, and more than doubled
its redundancy. The extra 34 items were overwhelmingly restatement and inapplicable
doctrine.

**Redundancy tracks volume almost linearly** across all five rungs: 13 items → 0.09,
22 → 0.14, 56 → 0.33/0.34, 63 → 0.35. Whatever "be exhaustive" buys, it is not coverage.

**This retroactively explains the cross-vendor null.**
[`cross-vendor-null.md`](./cross-vendor-null.md) matched the two vendors at ~55 items and
found a second vendor worth no more than a rerun. The volume control that made the
comparison fair also **pushed both vendors into their padding regime**, where the marginal
item is restatement. A cross-vendor comparison run at each model's natural restraint might
look different, and that is now a live question rather than a settled one.

## 3. Claude at natural verbosity is the most efficient generator measured.

22 items, every weighted point, yield 0.79, noise 0.06. It finds the whole graded answer
with **a third of GPT's output and a quarter of its noise**.

But note *where* the quality lives: pushed to 56 items its noise rose to 0.13, close to
GPT's 0.15. The low noise at 22 items is a property of **restraint**, not of the model —
it produces its best 22 and then degrades toward the same floor.

## 4. The structured walk contributes something no other rung does.

It has the **highest off-key rate by four times** (0.17 against 0.02–0.04) and the **lowest
redundancy** (0.09).

Off-key items are sound, raised, and material — judged blind — yet matched to no key point.
So the taxonomy walk is not finding more of the *graded* answer; nobody needs help with
that. It is surfacing roughly **two items per run of material the examiners did not
grade**, while restating itself almost never.

That is the profile the coverage line was looking for, and it is the one thing in this
table that a key-relative instrument can see *at all* of the original question. It is also
the weakest-supported number here: ~2 items per run on one fact pattern, resting on a
blind judge whose control passes but whose off-key judgments have no gold to check against.

## 5. What this changes

- **The primary endpoint moves.** Recall-by-obscurity is unmeasurable on tractable fact
  patterns. The discriminating axes are **yield** and **off-key rate**.
- **Volume is a quality lever, not a coverage lever**, and it points the wrong way. Any
  future design that "asks for more" should expect to pay in yield and gain nothing in
  recall.
- **The cross-vendor null needs re-reading**, not retracting: it was measured in the
  padding regime both vendors were forced into.
- **Harder fact patterns come before more rungs.**

## 6. What this cannot do

- **One fact pattern**, and an easy one — that is the headline limitation, not a footnote.
- **Recall is bounded by the key**: it cannot see anything the examiners did not grade. The
  off-key column is the only window onto that, and it is judge-dependent.
- k = 2, against the design's k = 5.
- No perturbation contrast, so nothing here separates competence from contamination.
- Yield rests on a model judgment. Its positive control passes at 1.00 on every rung, which
  is the strongest available check and is not the same as being right.
