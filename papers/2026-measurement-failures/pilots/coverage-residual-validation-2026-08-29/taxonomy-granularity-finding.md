# The structured walk's performance is inherited from its taxonomy, not from its method

**Status: exploratory. Three fact patterns, one prediction stated in advance and confirmed,
one confound acknowledged.**
Extends [`harder-pattern-scores.md`](./harder-pattern-scores.md) and
[`structured-enumerator.md`](./structured-enumerator.md).
Raw: `runs/july-2020-secured-transactions.key-relative-scores.json`.

---

## The prediction, stated before the run

The structured walk scored recall **1.00** on Family Law and **0.35** on Decedents' Estates
/ Conflict of Laws. The proposed explanation was that the NCBE taxonomy is drawn at wildly
uneven granularity across subjects, and the walk can only be as specific as its map.

Measured on the taxonomy itself, that unevenness is real:

| subject | nodes | median words per leaf | vague headings |
|---|---|---|---|
| **Secured Transactions** | 29 | **7** | **0%** |
| Family Law | 39 | 3 | 0% |
| Decedents' Estates | 22 | **2** | 0% |
| Conflict of Laws | 16 | 4 | **19%** |

So: **July 2020 Secured Transactions**, 6 weighted points, in the most finely-drawn subject
in the map. Prediction recorded before running — *the walk should score substantially above
0.35, approaching its Family Law performance. If it collapses on the most specific subject
available, the granularity explanation is wrong and the mechanism itself is broken.*

## Result

```
rung   items  recall  yield  noise  redun  offkey  ctrl   configuration
g1        34    1.00   0.65   0.12   0.19    0.10  1.00   gpt-5.2, natural
g3        18    1.00   0.79   0.00   0.20    0.05  1.00   claude-opus-4-8, natural
g4         9    1.00   0.89   0.02   0.00    0.35  1.00   structured taxonomy walk
```

**The walk posts the best numbers of any rung on any pattern in this study** — full recall
on nine items, 2% noise, zero redundancy, and the highest off-key rate yet recorded.

## The three-point relationship

| fact pattern | taxonomy granularity | walk recall | walk yield | walk noise |
|---|---|---|---|---|
| Feb 2018 Family Law | medium — 3 words/leaf | 1.00 | 0.63 | 0.18 |
| Jul 2019 Decedents' / Conflict | lowest — 2 words, 19% vague | **0.35** | 0.34 | **0.64** |
| Jul 2020 Secured Transactions | highest — 7 words, 0% vague | 1.00 | **0.89** | **0.02** |

Monotonic in granularity on every column. And the mechanism is visible in the raw output —
the Secured Transactions nodes carry **statutory citations**:

```
Enforceability (§ 9-203) · Priority over unperfected security interests (§ 9-317)
Priority among conflicting security interests (§§ 9-322 through 9-329)
Classification of goods (§ 9-102) · After-acquired property; future advances (§ 9-204)
```

against Decedents'/Conflict's *"Basic concepts"*, *"Meaning and legal consequences"*,
*"Application in specific areas"*.

## What this means, and it is uncomfortable

**The structured rung's value is inherited from an external document's editorial quality,
not produced by the method.** Where a committee happened to write §-level detail, the walk
is the best generator measured. Where they wrote chapter headings, it fails outright.

That is a real constraint on the independence ladder. The walk was the last rung whose
failure mode is not drawn from the model distribution — human evaluation is unavailable by
standing constraint, and the cross-vendor pass measured worth nothing over a rerun
([`cross-vendor-null.md`](./cross-vendor-null.md)). So the one remaining independent
generator **works only where somebody else already did the taxonomy work carefully**, and
nothing in the method detects when that is not the case.

The practical form: before using a structured enumerator on a domain, **measure its map's
granularity first**. Median words per leaf and share of vague headings took one pass over
the taxonomy and predicted performance across three fact patterns.

## The confound, which I should have seen before choosing the case

This key is **two parallel three-part problems** over two items. (The key's points, issue statements and weights
are withheld; see the archive README, "Withheld material".)

That is unusually **mechanical** — enumerable from the fact pattern's structure rather than
requiring anyone to notice something subtle. So Secured Transactions is both the most
finely-drawn subject *and* the most checklist-amenable key, and a success here cannot fully
separate the two.

**What the confound does not explain:** `gpt-5.2` scored yield 0.65 and noise 0.12 on the
*same* mechanical pattern. If a tractable key automatically produced clean output, GPT would
have posted it too. The walk's 0.89 / 0.02 is distinctive to the walk.

A cleaner test would hold key structure fixed and vary only taxonomy granularity. That is
available in the corpus and has not been run.

## Recall ceilinged again — 1 of 3 patterns discriminates

All three rungs hit 1.00 here, as on Family Law. Only the Decedents'/Conflict pattern
separated them. So **recall discriminates on roughly one fact pattern in three**, and
corpus selection matters more than adding rungs: two-thirds of the available problems
cannot answer the question the design's primary endpoint asks.

Yield discriminated on all three (0.34–0.89), which strengthens the case for it as the
working primary measure.

## What this cannot do

- Three fact patterns, one per granularity level. The relationship is suggestive, not
  established.
- The granularity proxy (median words per leaf, share of vague headings) is crude and was
  built after seeing the first failure — it is a post-hoc measure that then made a
  successful forward prediction, which is worth something but is not a validated instrument.
- The mechanical-key confound above is unresolved.
- k = 2, against the design's k = 5.
