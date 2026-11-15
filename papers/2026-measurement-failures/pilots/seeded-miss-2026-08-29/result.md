# Off-key discovery is validated as a probe — and its reported number is mostly a matching artifact

> ### ⚠ SUPERSEDED IN PART — the corpus was expanded on 2026-08-30
>
> This document records the **33-case / 132-run** scoring, and stands as that record. The corpus
> was then widened to **47 cases / 188 runs**, clean stratum **9 → 15 cases**, at the same k and
> with the same models and settings so the two are comparable. What changed:
>
> | | this document (9 clean cases) | current (15 clean cases) |
> |---|---|---|
> | off-key, clean stratum | 0.58 | **0.50** |
> | raw recovery | 0.92 | **0.90** |
> | partial credit | 0.92 | **0.85** |
> | absorbed only | 0.33 | **0.40** |
> | 95% interval | [0.33, 0.81] | **[0.33, 0.67]** |
> | leakage gradient | 0.58 / 0.61 / 0.75 | **0.50 / 0.65 / 0.71** |
>
> **The headline moved less than its own stated interval** — and this is the **fifth** reading,
> not a first correction. §8 item 2 already records 0.55, 0.50, 0.64 and 0.58 across corpus
> sizes and scoring settings; 0.50 joins that series. All five sit inside the interval. Read it
> as §7.3 says to: **the level is not quotable to two decimals, and the interval has been honest
> every time.** The Measurement paper §7.6 carries this reading.
>
> **One claim here did not survive and is corrected inline at §1a below** — partial credit no
> longer recovers the raw upper bound exactly. It is flagged rather than rewritten because that
> claim was quoted forward into the Measurement paper, and the correction needs to be findable
> from either end.
>
> Live figures: `runs/seed-recovery-report.json`. Neither this file nor the report is the paper;
> the paper reports the current scoring.

**Status: exploratory result, pre-registered analysis. 132 scored runs over 33 cases**
(34 extracted, 1 removed by the stimulus-validity gate), above the pre-registered floor of
20; the headline stratum holds 9 of those cases. Scored at **k=4** with the leakage audit at
**k=5**. Raw: `runs/seed-recovery-report.json`. Supersedes [`first-result.md`](./first-result.md)
(52 runs) and the 25-case pass it replaced.

---

## What was asked

Off-key discovery — items a blind judge rates sound, raised and material that match no key
point — is the only measure in the coverage line that looks at ungraded material, and the one
number nothing could check
([`../coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md`](../coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md) §3).
The hold-out attempt closed only part of the gap because every seed was an examiner-graded
item in disguise.

This experiment supplies the seed its §4 specified: **a consideration a real decision-maker
actually failed to weigh**, on record because an appellate court said so, in opinions filed
after both vendors' training cutoffs.

## The controls, first

| control | result | reading |
|---|---|---|
| **positive** — over key points a run covered, does the blind judge rate ≥1 covering item sound + raised + material? | **0.97** (floor 0.90) | PASS |
| **negative** — decoy seeds from other cases, scored in the *same shuffled call* as the real seed, and judged not applicable to these facts | **0.01**, n=390 | **CLEAN** |

The negative control decides whether anything else can be read. It exists because the parent
study's sharpest failure was a sanity test that could only detect error in one direction. A
generous seed judge would have inflated every figure below and looked like success; at 0.02
over 404 inapplicable decoys, it is not doing that.

## The result

```
stratum       n    raw  offkey  partial  absorb  decoy*
neutral      36   0.92    0.58     0.92    0.33    0.02
hinted       36   0.94    0.61     0.92    0.33    0.02
explicit     60   1.00    0.75     1.00    0.25    0.01
ALL         132   0.96    0.67     0.95    0.30    0.01
```

**Headline, as pre-registered: off-key recovery in the neutral leakage stratum = 0.58**
(raw 0.92, n=36 runs over 9 cases).

## 1. The finding: the loss is the matching rule, not blindness

In the neutral stratum the numbers decompose:

```
raw recovery              0.92     the generators DID surface the missed consideration
  reported as off-key     0.58     the measure counted it
  absorbed into the key   0.33     the measure discarded it
never raised at all       0.08
```

**Off-key reports 0.58 where the generators actually found the seed 0.92 of the time.**
Almost the whole shortfall is the exclusive-match rule: the matcher credits the same item
against a key point, the item is stripped from the off-key set, and a hit is recorded as a
miss.

Per case, in the clean stratum, the effect is not an averaging artifact:

| case | raw | off-key | partial |
|---|---|---|---|
| Shane Roy Needham v. Janet Lea Nee | 0.75 | 0.00 | 0.75 |
| Keith Thaete, Steve King, Lance Th | 0.75 | 0.00 | 0.75 |
| Qoye v. United States | 1.00 | 0.50 | 1.00 |
| Mbueno-Vita v. Blanche | 0.75 | 0.50 | 0.75 |
| Stephen Roberts v. Mark Engelke | 1.00 | 0.75 | 1.00 |
| Century Campus Housing Management, | 1.00 | 0.75 | 1.00 |
| Davis v. United States | 1.00 | 0.75 | 1.00 |
| Sussex County Planning & Zoning Co | 1.00 | 1.00 | 1.00 |
| Friends of Animals v. FWS | 1.00 | 1.00 | 1.00 |

**Two cases recover nothing under the exclusive rule and everything under partial credit**
(*Needham*, *Thaete*): every run that raised the seed had its citing item absorbed into the
key, so the measure reported zero while the generator had in fact found the consideration
three times in four.

An earlier draft used *Eqbal v. Blanche* as the showcase for this — raw 1.00, off-key 0.00
across every run. **That example is withdrawn.** Once the leakage audit was reliable enough
(k=5) to fire it, the stimulus-validity gate removed *Eqbal* from the corpus: its seed turns
on calendar-date discrepancies its case file never mentions. Its raw 1.00 was the seed judge
crediting a topical near-miss, not a recovery (§6).

This is **deviation D14 — the granularity problem — measured on independent data.** The parent
hold-out could only infer it from item-to-key-point ratios and had to report the structured
walk's recovery as *undefined*. Here it is a counted quantity, against human-authored seeds
the instrument has never seen.

The consequence cuts against the pessimistic reading of the coverage line: **the generators
are not blind to what a real court missed.** The instrument was.

### 1a. The fix, run rather than predicted

Drop the exclusive-match rule: an item counts for the seed whether or not the matcher also
credits it to a key point. The quality bar is unchanged — still sound, raised, material,
non-duplicate. It is not a looser measure, only one that stops discarding evidence for being
dual-purpose.

| rule | neutral stratum |
|---|---|
| exclusive match (as reported) | 0.58 |
| **partial credit** | **0.92** |
| raw (upper bound) | 0.92 |

**Partial credit recovers the upper bound exactly.** Nothing is lost between "the generator
addressed the seed" and "the corrected measure counts it."

> ⚠ **CORRECTED 2026-08-30 — this held at 9 clean cases and does not at 15.** The widened
> corpus gives partial credit **0.85** against raw **0.90**: in **3 runs of 60** the only item
> addressing the seed failed the blind judge's quality bar, so raw counts it and partial credit
> does not. *Something* is lost between the two, and it is a quality-bar effect rather than a
> matching-rule one.
>
> **What is unaffected:** the exclusive-match rule still accounts for the bulk of the shortfall
> — 0.35 of the 0.40 gap — which is this section's actual finding. What does not survive is the
> word *exactly*, which was a property of nine cases.
>
> *Sheffield v. State* is the case that shows the two apart: its generators raised the seed in
> all four runs (raw 1.00) and partial credit returns 0.75.

### 1b. But the corrected rule cannot compare — it saturates

Partial credit lands at **0.92 / 0.92 / 1.00** across neutral, hinted and explicit. It is at
ceiling everywhere, so it has no room to discriminate between conditions.

That gives the two rules different jobs, and neither replaces the other:

- **Partial credit is a validation measure.** It answers "did the generator find it?" and it
  is the honest answer to that question.
- **Exclusive match is a comparison measure.** It still separates conditions (0.58 / 0.61 /
  0.75) precisely because it is lossy — but its *level* is not a coverage rate and must never
  be read as one.

Reporting partial credit as though it were a coverage improvement would be its own confident
wrong number. It is a ceiling effect.

## 2. Leakage: only the clean-vs-leaky split survives re-measurement

Off-key recovery by how much the stimulus telegraphs its seed: **0.58 → 0.61 → 0.75**.

Neutral is lowest, and that is what the pre-registration turns on: pooling all 132 runs
reports **0.67** against a neutral-only **0.58**.

But the *shape* of this gradient is not stable. Across three measurements of the same
quantity it has read 0.38/0.65/0.94 (52 runs, k=2 strata), 0.64/0.64/0.68 (k=5 strata, k=2
scoring) and 0.58/0.61/0.75 (k=5 strata, k=4 scoring). The neutral-lowest ordering survives
all three; nothing else does. **Read the audit as separating clean from leaky, not as a
three-level scale** — §5 gives the reason.

An earlier draft cited the monotonic gradient as evidence that the leakage audit validates
itself. That argument is **withdrawn**: it rested on the version measured with the least
reliable strata.

## 3. Both vendors: same raw recovery on 3x the output

| rung | items/run | raw | off-key | off-key (neutral) |
|---|---|---|---|---|
| g1 gpt-5.2 | 59 | 0.97 | 0.76 | 0.67 |
| g3 claude-opus-4-8 | 22 | 0.95 | 0.58 | 0.50 |

At k=2 the neutral-stratum figures read 0.50 / 0.50; at k=4, 0.67 / 0.50. **The gap is not
stable across scorings and must not be reported as a vendor effect** (§5).

What *is* stable is raw recovery — 0.97 vs 0.95 — despite gpt-5.2 emitting nearly three times
as many items. The parent study's result, that expansion produces more output rather than more
answer, survives contact with an entirely different corpus and a human-authored seed.

## 4. An exploratory cut that reversed twice, and why it is reported anyway

The 52-run batch showed first-instance tribunals recovering far better than reviewing ones —
0.90 vs 0.50 — with a plausible mechanism ready to explain it. At 132 runs the gap is gone and
has changed sign twice across scorings (0.66/0.61 at k=2; 0.62/0.73 at k=4).

| tribunal below | runs | cases | raw | off-key |
|---|---|---|---|---|
| first-instance | 80 | 20 | 0.99 | 0.66 |
| reviewing | 56 | 14 | 0.98 | 0.61 |

It was labelled exploratory when it looked strongest, which is the only reason it is a
footnote instead of a finding. A 40-point difference over 13 cases with a ready-made mechanism
is exactly the shape of a ninth entry in the parent study's catalogue of confident wrong
numbers.

## 5. Measurement noise: raising the replicate count does not fix it

The whole corpus was scored twice — once at **k=2** and once at **k=4**, identical in every
other respect — specifically to find out whether more judging replicates stabilise the
measure. **They do not.**

**Aggregate drift is modest**, which is the reassuring half:

| stratum | raw | off-key | partial |
|---|---|---|---|
| neutral | 0.97 → 0.92 | 0.64 → **0.58** | 0.96 → 0.92 |
| hinted | 0.97 → 0.94 | 0.64 → 0.61 | 1.00 → 0.92 |
| explicit | 1.00 → 1.00 | 0.68 → 0.75 | 0.95 → 1.00 |
| **ALL** | 0.98 → 0.96 | 0.66 → **0.67** | 0.96 → 0.95 |

**Run-level agreement is not.** On the measure under validation, **only 0.81 of individual
verdicts survived doubling k** — 25 of 132 runs flipped. Seventeen of 33 cases moved, two by
±0.50. Agreement was 0.98 on raw recovery and 0.96 on partial credit; it is *off-key
specifically* that is unstable, which makes sense: it is the only measure depending on the
matcher's absorption decision as well as the judge's.

The pooled number looks steady only because the flips cancel. That is a property of this
sample, not a reason to trust an individual figure.

**Why more replicates cannot help.** Each pass is already a majority vote. Where an item's
underlying probability of reading as off-key sits near 0.5 — a genuinely borderline absorption
call — majority-voting more samples converges on a coin flip, not on the truth. Raising k buys
precision only for items that were already decided.

**Where the variance actually lives** (`scripts/variance_budget.py`, bootstrapping over cases
against the observed flip rate):

```
clean stratum, k=4:   case sampling   sd 0.118   95% interval [0.33, 0.81]
                      judge sampling  sd 0.062   per-run flip rate 0.167
```

Case sampling dominated at k=2 (0.119 vs 0.058) and still leads at k=4. **The headline's 95%
interval spans roughly [0.33, 0.81]** — nearly half the scale — and per-case values are close
to bimodal (cases sit near 0 or near 1, rarely between), so a mean over nine cases is a coarse
instrument.

`scripts/case_profile.py` asked whether anything predicts *which* cases recover, so expansion
could be targeted. Nothing does: high- and low-recovery cases match on items emitted, off-key
pool, key size, recall, seed length and leakage stratum — **and on raw recovery** (1.00 vs
0.97). The low group raised the seed just as reliably and simply had its citing items
absorbed. The split is each case's key-versus-seed geometry, not case difficulty, and it is
not forecastable before scoring.

**What this means for reading anything here.**

- **Differences below ~10 points mean nothing.** The leakage scale in §2 moved from
  0.64/0.64/0.68 at k=2 to 0.58/0.61/0.75 at k=4; the per-generator gap in §3 moved from
  0.50/0.50 to 0.67/0.50. Neither is a finding.
- **Read the strata as clean vs leaky**, never as a graded scale.
- **The lever is more cases, not a higher k.** That is now measured rather than argued, and
  it is why corpus expansion rather than a k=8 run is the queued next step.

## 6. What this does not establish

- **The headline rests on 9 cases**, though the corpus is 33 scored. Its 95% interval is
  roughly [0.33, 0.81] (§5) — the point estimate should not be quoted without it. The neutral stratum is also a
  *strict* subset: the audit rates "the facts underlying the seed are present and central" as
  leaky even though those facts must be present for the seed to be raisable at all.
- **Selection is inflationary** (design-note §4.2): a miss reaches an appellate holding
  because it was arguable, preserved, briefed, and consequential. Seeds skew findable.
- **The doctrine in a seed is usually mainstream.** What lies outside the model ecosystem is
  that this consideration was decisive and overlooked *in this situation* — not the rule.
- **One control cannot be built.** Nothing here detects a blind spot shared by the generator,
  the blind judge and the seed judge. That objection from the parent study's §3 stands
  untouched.
- **The stimulus-validity gate fired once** *(annotation 2026-09-16: once at this pass; on the 49-case expansion it fired a second time, on* People v. Occhipinti *(`10937255`), before that case was scored — see the Measurement paper §7.1)*, on *Eqbal v. Blanche*, and only once the leakage
  audit was reliable enough (k=5) to fire it. That case had shown raw recovery 1.00 on a seed
  its case file cannot support — it turns on calendar dates the file never mentions — so the
  **seed judge was crediting a topical near-miss**. The decoy control cannot see that: decoys
  are drawn from *unrelated* cases, so it measures far-off generosity only. One observed
  instance, but it is a hole in the study's best control.
- **k=4 scoring, k=5 leakage audit.** Raising k further is not the fix (§5).

## 7. What it does to the papers

*(Renumbered 2026-08-30: this study is now evidence for the **Measurement paper** (Paper 2); "Paper 2" below meant the **Proposer paper**, now Paper 3.)*

`implications-for-the-proposer-paper.md` §1 recorded that the Proposer paper had lost its planned
instrument, and §6 named this experiment as the highest-value unrun item — anticipating
validation *or* a sharper negative.

The outcome is neither: **the probe works, and the number it reported was wrong in a specific,
fixable way.**

- Off-key discovery **is** a real probe for ungraded material. It surfaces a consideration a
  human decision-maker missed, in a corpus that post-dates training, with a false-positive
  floor of 0.02.
- **The two rules have different jobs** (§1b) and no paper may conflate them: partial
  credit for "did it find it", exclusive match for "does this condition beat that one".
- The prediction this study made about the parent study's own numbers — that they were
  understated by the same defect — **was tested and refuted**; see §8.

## 8. Follow-ups, and how they came out

1. ~~Re-score with partial credit.~~ **Done** (§1a): 0.50 -> 0.96, with §1b as the caveat that
   came with it.
2. ~~Extend the corpus.~~ **Done**: 25 → 34 cases (33 scored), 132 runs — and again on
   2026-08-30 to 49 cases (47 scored), 188 runs. The headline has read 0.55, 0.50, 0.64, 0.58
   and now **0.50** across corpus sizes and scoring settings — all five inside the interval in
   §5, which is the only thing about this number that has been stable.
3. ~~Re-read the parent study's off-key numbers under the corrected rule.~~ **Done, and it
   refuted the prediction made here.**
   ([`../coverage-residual-validation-2026-08-29/offkey-recount.md`](../coverage-residual-validation-2026-08-29/offkey-recount.md))

   Every rung on all three fact patterns, recounted under partial credit: the correction is
   **+0.00 to +0.08, median +0.04** — not the large understatement predicted. The granularity
   ordering survives unchanged.

   **Why the same defect is severe here and negligible there** is the transferable lesson.
   This study's measure is *targeted* — "does any item address this one seed?" — so a single
   absorbed item destroys a binary signal. The parent study's off-key is a *rate over 9–56
   emitted items*, where absorbing a handful moves it by a few points. **The rule's damage
   scales with how concentrated the measure is.** A broken rule does not make every number
   computed with it wrong.
4. ~~Raise k above 2.~~ **Done, and it did not work** (§5). Scoring at k=4 left run-level
   agreement on off-key at **0.81** — a quarter of individual verdicts flip — while moving the
   pooled figure by 0.01. Raising the leakage audit to k=5 changed 10 of 34 case strata and
   flattened the gradient that had been cited as self-validation. Neither knob stabilises the
   measure, because the variance is at case level and the borderline calls are genuinely
   near-coin-flips.
5. **Extend the corpus — the one lever that remains.** Blocked on the CourtListener 125/day
   account cap (see README); the widened 13-phrase query list is already in place. Expect
   roughly one new clean case per five candidates. The binding constraint is the *neutral*
   stratum at 9 cases, and its interval will not narrow until that number does.
