# Corpus reconnaissance + pipeline smoke test — 2026-08-29

**Status: exploratory. Corpus acquired and verified; one generator run end-to-end.**
Companion to [`design-note.md`](./design-note.md). Deviations it forces are in [`deviations.md`](./deviations.md) —
four changes and one open question, each titled there in plain language.

---

## 1. The corpus exists, and it is better than the design note assumed

NCBE publishes past **Multistate Essay Examination** administrations with **official
analyses** free. Ten administrations carry both questions and analyses:

| | |
|---|---|
| Administrations (Feb 2016 – July 2020) | **10** |
| Fact patterns | **60** (6 per administration) |
| Weighted gold points | **227** |
| Blocks whose point weights sum to exactly 100 | **60 / 60** |
| Question bodies extracted | **56 / 60** |
| Distinct subjects | 29 labels (needs normalisation — "Agency" vs "Agency & Partnership") |

Each fact pattern's analysis supplies two things the design needed and could not have
manufactured without a person:

- **`Legal Problems:`** — an enumerated issue list.
- **`Point One (30%)` … ** — per-issue percentage weightings, **summing to 100**.

The weightings are the part worth pausing on. The design note's sample section (§2) listed a human-authored
materiality weighting as a *requirement* and hoped issue-spotters would supply one. NCBE supplies it
explicitly, as examiner-assigned percentages, frozen years before this system existed.
That is the materiality key for the flip test, and it is not a rating we produced.

Also acquired: the **NCBE MEE Subject Matter Outline** — a fixed doctrinal taxonomy,
which is precisely the structured non-model enumerator the design note calls G4 (§4, the independence ladder). Not generated,
not sampled; walked.

Reproduced by [`scripts/fetch_corpus.sh`](./scripts/fetch_corpus.sh). **NCBE material is
copyrighted and is not redistributed here** — the corpus directory is gitignored, and only
derived structured gold is committed.

## 2. The gold unit is the weighted Point, not the `Legal Problems` entry

The two enumerations are independent and disagree in **both** directions:

- **February 2018 Contracts** lists `(2)(a)` and `(2)(b)` but develops them under a single
  `Point Two (40%)`.
- **February 2020 Question 2** lists a bare `(2)` developed as `Point Two(a)` + `Point Two(b)`.
- **February 2017 Real Property** mismatches similarly.

57 of 60 align; 3 do not. Anchoring on Points is what makes the set complete and
total-100 **everywhere** (verified 60/60), and the weight is the one component that cannot
be reconstructed if dropped. Recorded as deviation **D2 — *the gold unit is the weighted Point*** in [`deviations.md`](./deviations.md).

## 3. Contamination risk and gold availability are inversely coupled

This is structural, not incidental, and it is the sharpest constraint the recon found.

| Release | Analyses? | Contamination risk |
|---|---|---|
| Feb 2016 – July 2020 | **yes** | **high** — 6–10 years indexed, reproduced across every bar-prep site |
| February 2026 | **no** | low, but **no gold** |

**Everything with an answer key is old. The one recent release has no answer key.** There
is no low-contamination-plus-gold cell in this table, so the perturbation defence (design note §6) is not a mitigation that can be skipped if a cleaner source turns up — it is the only defence
available. Recorded as deviation **D4 — *perturbation is now the only contamination defence*** in [`deviations.md`](./deviations.md).

## 4. The pipeline runs — and the first call found a hole in the design

One fact pattern (February 2018, Family Law), one generator (G3, cross-vendor `gpt-5.2`),
blind, no gold in the prompt. It worked end to end on the first attempt.

**It returned 57 issues against a gold set of 5.**

```
G3 output (57):  UPAA applicability · Writing and signatures · Voluntariness of execution ·
                 Duress/coercion · Unconscionability at execution · Full and fair disclosure ·
                 ... · Custody provision enforceability · ... · Best interests standard · ...

GOLD (5):        [withheld: five NCBE answer-key points with their grading weights.
                 See the archive README, "Withheld material".]
```

Every gold point is covered several times over. **Recall = 5/5.**

### Why that is a problem, not a result

1. **The primary endpoint ceilings out.** the design note's measurement section (§5) names recall-against-gold,
   stratified by obscurity, as the primary measurement. If every generator scores 5/5, the
   recall-by-obscurity curve is flat at 100% and discriminates nothing. Not a floor
   effect — a **ceiling effect**, and it would have consumed the whole corpus before
   showing up if the smoke test had been skipped.

2. **The granularity gap is an order of magnitude.** Gold is examiner-coarse (3.78 points
   per pattern); the generator is fine-grained (57 labels). These are not the same unit,
   and recall across mismatched units is not a measurement.

3. **The design cannot currently detect over-generation, and over-generation is free.**
   the measurement section (§5) says off-gold items are recorded and never scored. But a generator that lists
   *everything* achieves perfect recall and contributes nothing — it has not spotted the
   decisive issue, it has buried it in 52 others. **Coverage measured by recall alone
   rewards padding.** That is the coverage analogue of the failure this whole line exists
   to catch, and the design as written is blind to it.

### What it implies

Coverage needs a **precision-and-recall pair**, not recall alone — or a granularity
normalisation that makes the two enumerations comparable before anything is counted.
Three candidate routes, none yet chosen:

- **Constrain the generator** to a comparable granularity ("at most N top-level issues"),
  making recall meaningful but importing an arbitrary N.
- **Score at gold granularity** by rolling generator output up to the examiner's points —
  reintroduces the semantic-matching judgment the design note's §0 (why this is
  exploratory) flags as the instrument's weak joint, now as the primary operation
  rather than a check.
- **Measure the pair**: recall against gold *and* a precision/yield term over off-gold
  items, with the off-gold items adjudicated rather than ignored. Most faithful,
  most expensive, and it makes the off-gold adjudication load-bearing.

**This is a design decision, not an implementation detail**, and it is open. Recorded as
deviation **D3 — *recall alone cannot be the primary endpoint*** in
[`deviations.md`](./deviations.md).

## 5. What is built

```
scripts/fetch_corpus.sh       reproduces the corpus from NCBE URLs (no redistribution)
scripts/extract_gold.py       -> gold/gold.json   60 patterns, 227 weighted points
scripts/extract_questions.py  -> corpus/questions.json (gitignored)  56/60 fact patterns
```

Generator plumbing is **reused, not rebuilt**: `../resolver-iteration-2026-06-29/scripts/lib_llm.py`
already provides dual-vendor calls with retry, throttling, and tolerant JSON extraction.

Both extractors ship an integrity report rather than a success message — the weights-sum
check is what surfaced the three misaligned patterns in §2 above (the gold unit), and the question-count check is
what surfaced the two header conventions.

## 6. Known gaps

- **4 of 60 question bodies** not extracted (sectioned-format subject headers that do not
  match). The gold for those patterns is intact; only the fact-pattern text is missing.
- **Subject labels need normalisation** before they can carry the corpus-frequency obscurity
  banding (design note §5, measurement).
- **One gold item** (February 2018 Contracts `(2)`) has no issue text, from the
  two-sub-issues-under-one-Point case in §2 above (the gold unit).
- Nothing has been perturbed yet; the contamination contrast (design note §6) is unrun.
