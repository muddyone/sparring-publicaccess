# Seeded-miss experiment: can off-key discovery recover a consideration a real decision-maker missed?

**Status: design, pre-registered before any data was pulled.** Written 2026-08-29, before
the corpus existed, so the analysis plan cannot be fitted to the result.

Serves the experiment named in
[`../coverage-residual-validation-2026-08-29/seeded-holdout-result.md`](../coverage-residual-validation-2026-08-29/seeded-holdout-result.md) §4
and [`../coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md`](../coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md) §6.
Sourcing decided in
[`../coverage-residual-validation-2026-08-29/seed-corpus-recon.md`](../coverage-residual-validation-2026-08-29/seed-corpus-recon.md) (option A).

---

## 1. The question

The coverage line has one measure that looks at ungraded material — **off-key discovery**:
items a blind judge rates sound, raised and material that match no point in the answer key.
It reached 0.49 on one configuration. Nothing checks it. The positive control validates the
judge against a human answer, and off-key is by definition outside the region where that
answer exists.

The hold-out attempt closed only part of the gap: its seeds were the examiners' own key
points in disguise, so every seed was mainstream by construction. Its own §4 states what a
real seed needs:

1. **known-material** — something establishes it mattered
2. **outside the scoring key** — so it must surface as off-key or not at all
3. **outside the key entirely, and outside the model ecosystem**

Condition 3 is the one no source supplied without authoring the seed (circular) or an expert
(unavailable by standing constraint).

## 2. The construct

An appellate opinion holding that a lower court **erred by failing to consider** something is
a case where *the decisive consideration is on record precisely because someone failed to
raise it*. Three parts come out of one document:

| part | what it is | who sees it |
|---|---|---|
| **the situation** | facts + procedural posture as they stood before the lower court | **the generator — and only this** |
| **the seed** | the consideration the appellate court says was not weighed | nobody, until scoring |
| **the key** | the grounds the lower court *did* address | the matcher (pass A) |

The generator is asked to list every issue the court must address. It never learns that
anything was missed.

**Why the key is what the lower court considered.** In the MEE study the key was the
examiners' graded points — the region where human judgment exists. Here the analogue is the
set of grounds the lower court actually reached: contemporaneous, human-authored, and
exhaustive over what that decision-maker treated as gradeable. The seed is outside it not by
a bookkeeping trick but because a real decision-maker really did not consider it.

### How this meets condition 3, and where it does not

Met: **that this consideration was decisive and was overlooked in this situation** is not a
fact any model could have memorised. The opinions are filed after the training cutoffs of
both vendors used, so the case, its facts, and its holding are all outside the ecosystem.

**Not met, and stated plainly:** the *doctrine* named in the seed is usually mainstream
(a statutory factor, a required finding). The seed is a **situated** miss, not an obscure
rule. This experiment therefore tests whether off-key recovers *a consideration a competent
human decision-maker actually failed to weigh* — which is the coverage question as it
occurs in practice — and **not** whether off-key recovers exotic doctrine. Nothing here
should be read as the latter.

## 3. Measures

Scored per (case, generator, replicate).

**Primary**

- **raw recovery** — does any emitted item address the seed? *Upper bound; no off-key
  gating.*
- **off-key recovery** — does an item addressing the seed appear in the **off-key** set,
  i.e. sound + raised + material + non-duplicate, and matched to no key point? *This is the
  measure under validation.*
- **the gap** (raw − off-key) — items that address the seed but were absorbed into the key
  by a coarse match. This is **deviation D14 measured rather than assumed**: in the hold-out
  it made the structured walk's recovery undefined, and here it becomes an observable on
  independent data.

**Controls**

- **positive control** — unchanged: over key points the run covered, does the blind judge
  rate at least one covering item sound + raised + material? Floor 0.90; below it the yield
  and off-key figures are not interpretable.
- **negative control (new, and load-bearing)** — each case is also scored against a
  **decoy seed** drawn from a different case in the corpus. A decoy has nothing to do with
  these facts, so recovery on decoys should be ≈0. **If decoy recovery is not near zero the
  seed-matching pass is too generous and no other number in this study is readable.**
  This exists because the parent study's sharpest failure was a sanity test that could only
  detect error in one direction ([`implications-for-the-proposer-paper.md`](../coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md) §4).
  A one-sided check is what this replaces.
- **leakage audit** — see §4.1.

**Generators.** Fine-grained rungs only: `g1` = gpt-5.2 natural verbosity, `g3` =
claude-opus-4-8 natural verbosity. The structured walk is excluded because off-key recovery
is **undefined** for generators whose items cover multiple key points (D14); the
volume-normalised rungs are excluded because matched-volume pushes both vendors into the
padding regime.

## 4. Confounds, named before the result

### 4.1 Leakage — the serious one

The appellate court's statement of facts is written by someone who already knows what was
missed, and may foreground exactly those facts. That inflates recovery.

Two responses, neither of which fully solves it:

- **Extraction structure** (rebuilt — see [`deviations.md`](./deviations.md) D3): the call
  that WRITES the situation is **blind**. It receives only the court's own recitation, cut
  out of the opinion by a two-sided structural boundary — after the caption and syllabus,
  before the analysis — and never sees the seed or the holding. It cannot leak what it was
  not shown. Asking a single sighted call to conceal the seed it had just identified was
  tried first and failed outright.
- **Measurement:** an independent blind pass rates each case for how strongly the situation
  telegraphs the seed (`explicit` / `hinted` / `neutral`). **Recovery is reported stratified
  by leakage stratum, and the headline number is the `neutral` stratum.**

Direction of bias: inflationary. A *low* recovery despite leakage is therefore a strong
negative; a high recovery is confounded and must be read in the neutral stratum only.

### 4.2 Selection

A miss reaches an appellate holding because it was arguable, preserved, briefed, and
consequential. Seeds therefore skew toward the findable end of the distribution. Inflationary.
Unfixable within this design; stated, not corrected.

### 4.3 Extraction is an editorial act

The split is model-performed. It is *extraction from a document* rather than invention, and
it is checkable against the source. Mitigations: the writer is **blind** to the seed and the
analysis (§4.1); the boundary that decides what it sees is **structural**, not semantic, so
the cut cannot be placed to hide or expose the seed; the extractor is a **different vendor**
from the generator under test; and every extraction is committed with its boundary offsets,
so any cut can be replayed against the source opinion.

Residual leakage after this is the **court's own** — what an appellate judge chose to put in
the fact recitation. That is a property of the corpus, and it is reported as one rather than
claimed to be solved.

### 4.4 Screening

The corpus is built by screening for *the appellate court agreed the consideration was
missed* — the raw phrase overwhelmingly appears in claims the court **rejects** (verified on
the first sampled opinion). A false positive admits a case where nothing was actually missed.
Screen verdicts and quoted holding language are committed; a hand spot-check is reported.

## 5. What each outcome means

| outcome | reading |
|---|---|
| off-key recovery high, decoys clean, neutral stratum also high | off-key is a **validated** probe for ungraded material. The Proposer paper recovers a version of the measurement §1 of `implications-for-the-proposer-paper.md` says it lost. |
| raw recovery high, off-key recovery low | the measure is **granularity-broken** on independent data. D14 confirmed; the fix (partial credit) is specified and the finding is about the instrument. |
| both low, decoys clean | the **sharper negative**: the coverage gap is not merely hard to measure but undetectable with these tools. A real result, and the one §6 says would be worth more than a null. |
| decoys fire | the seed-matching judge is too generous. **Stop.** Nothing else in the run is readable; rebuild the matching pass before reporting any number. |

## 6. Pre-registered analysis decisions

- Headline figure is **off-key recovery in the `neutral` leakage stratum**, pooled over both
  generators, with per-generator figures reported beside it.
- Decoy recovery is reported **in the same table**, not in a footnote.
- Cases where the run never raised the seed *at all* are counted in the denominator. Unlike
  the hold-out — which conditioned on the run having raised the point — a total miss is the
  outcome of interest here, not an exclusion.
- No case is dropped after seeing its score. Cases are dropped only at screening, on the
  committed criteria in §4.4, before any generator runs.
- Target n ≈ 30 cases. Below 20 usable cases the study reports as underpowered
  reconnaissance rather than a result.

## 7. Sourcing constraints

Free Law Project is a non-profit. Two different limits, both measured 2026-08-29:

| limit | value | notes |
|---|---|---|
| `/search/` | 5 / minute | |
| `/opinions/` | 50 / hour | |
| **account total** | **125 / day** | **shared across both endpoints — the binding one** |

All three were found by hitting them in turn, each time assuming the newly discovered limit
was the last. It was not: the first pull assumed per-minute and spent 50 minutes wedged in
backoff; a later attempt to widen the corpus exhausted the **daily** cap on its first query
and sat down to sleep for 17 hours.

**Plan a corpus pull in days, not hours.** One 122-opinion pull plus its searches very nearly
spends a day's budget, and every exploratory search costs opinions you then cannot fetch. The
fetcher throttles, caches to `corpus/raw/`, and is resumable; the corpus is pulled once, not
swept repeatedly. Free Law Project is a non-profit — these limits are theirs to set.
