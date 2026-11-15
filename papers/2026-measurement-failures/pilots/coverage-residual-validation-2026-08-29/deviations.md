# Deviations from the design note

Every departure from [`design-note.md`](./design-note.md), with its date and reason.
Cheap to keep, and the only thing that makes an exploratory result auditable after the fact
(design note §13, deviations).

---

### D1 — the estimate of gold items per question was wrong. Conclusion survives; reasoning did not.
*(design note §2, sample)*
**2026-08-29 · corrected**

The sample section reasoned: *"a typical issue-spotter carries 8–15 gold issues, so 20 problems yields
roughly 200–300 gold items."* The MEE carries **3.78** weighted points per fact pattern,
not 8–15.

The target range still lands — because the free corpus turned out to hold **60** fact
patterns rather than the 20–30 the design note planned for, giving **227** gold items. So the numbers
work out, by a route the design note did not anticipate. Recorded because a conclusion that
survives on different grounds than the ones written down is exactly the kind of thing that
looks like confirmation later.

**Effect:** the sample section's arithmetic is superseded. n = 60 fact patterns, 227 gold items, no sampling
needed — the whole free corpus is usable.

---

### D2 — the gold unit is the weighted `Point`, not the `Legal Problems` entry.
*(design note §2, sample)*
**2026-08-29 · design change**

The design note treated the enumerated issue list as the gold set and the point weightings as a separate
materiality key. They are two independent enumerations that disagree in both directions in
3 of 60 fact patterns (detail: [`corpus-recon.md`](./corpus-recon.md) §2, the gold unit).

Anchoring on Points makes the set complete and total-100 in **60/60** blocks, and preserves
the weight, which cannot be reconstructed if dropped. `Legal Problems` text is attached to
each Point where the ids resolve.

**Effect:** gold granularity is the examiner's grading rubric rather than the examiner's
issue preview. This is the more defensible unit — it is what the examiners actually scored.

---

### D3 — recall against gold, alone, cannot be the primary endpoint. **RESOLVED.**
*(design note §5, measurement — and §9, the stop rule, which depends on it)*
**2026-08-29 · unresolved design question, surfaced by the pipeline smoke test**

The first generator run returned **57 issues against a gold set of 5**, covering every gold
point several times over. Recall = 5/5.

Two consequences, both fatal to the measurement design as written:

1. **Ceiling effect.** If every generator scores at or near 5/5, the recall-by-obscurity
   curve — the study's primary measurement — is flat and discriminates nothing.
2. **Over-generation is unpenalised and free.** The measurement section records off-gold items and explicitly
   scores them neither way. A generator that lists everything therefore achieves perfect
   recall while contributing nothing: it has not surfaced the decisive issue, it has buried
   it among 52 others. **Recall alone rewards padding** — the coverage analogue of the very
   failure this line exists to detect.

Three candidate remedies are laid out in [`corpus-recon.md`](./corpus-recon.md) §4 (the smoke-test finding)
(constrain generator granularity / roll up to gold granularity / measure a
precision-and-recall pair). **None is chosen.** This gates Phase 1, and it is a design
decision rather than an implementation detail.

**Effect:** the primary endpoint (design note §5, measurement) is suspended pending this
decision. The stop rule (design note §9), stated in terms of recall on the obscure tercile, inherits the
same suspension.

---

### D4 — perturbation is promoted from mitigation to primary measurement.
*(design note §6, contamination)*
**2026-08-29 · design change**

The contamination section (§6) treated it as a threat with a preference order, the first option being
*"prefer sources unlikely to be indexed."* The recon establishes that option does not exist
in this corpus: **every administration carrying an answer key is 2016–2020, and the only
recent release (February 2026) has no analyses** (detail: [`corpus-recon.md`](./corpus-recon.md) §3, contamination vs gold availability).
Gold availability and contamination risk are inversely coupled, structurally.

**Effect:** the perturbed/unperturbed paired contrast is no longer one mitigation among
three — it is the only available defence, and the gap between the pair is a primary
reported quantity rather than a validity side-check. The contamination section's preference order is superseded: perturbation and
risk-tiering stand, but "prefer un-indexed sources" is unavailable.

---

### D5 — corpus is reproduced, not redistributed.
*(no design-note section; this decision was unstated)*
**2026-08-29 · clarification, no design change**

NCBE materials are copyrighted. The corpus directory is gitignored; `fetch_corpus.sh`
rebuilds it from NCBE's public URLs. Only derived structured gold (issue text, ids, weights,
citation) is committed. Not a departure from the design note, which is silent on this —
recorded so the decision is visible rather than assumed.

---

### D6 — the positive control on the blind judge was mis-specified.
*(scoring-design.md §5, the judge's positive control)*
**2026-08-29 · corrected on first run**

The control asked whether **every** key-covered item was rated signal. It failed at 0.50 —
correctly, for the wrong reason: when 18 emitted items cover one key point, most **are**
duplicates, and the blind judge flagging them is right. The control was measuring
deduplication, not judgment.

Respecified: for each key point, **at least one** covering item must be rated
sound + raised + material; the duplicate flag is ignored. Re-run: **5/5 = 1.00, PASS.**

Recorded because a control that fails for the wrong reason is more dangerous than one that
fails outright — it invites rebuilding the thing being measured to satisfy a broken test.

---

### D7 — key-id normalisation, and why a silent zero is worth a deviation entry.
*(implementation, `scripts/score_pair.py`)*
**2026-08-29 · fixed**

The matcher returns key ids with punctuation stripped (`1(a)` for `(1)(a)`). The first
scored run therefore matched nothing and reported **weighted recall 0.00** — a plausible-
looking number produced by a string mismatch, not a measurement. Ids are now compared on
alphanumerics only.

Recorded rather than fixed silently: this is exactly the failure class the study exists to
study — an instrument returning a confident number that means nothing. Its own scorer did
it on the first attempt, which is a useful thing for this study to have on record.

---

### D8 — the stable-core control borrowed a threshold that did not apply to it.
*(scoring-design.md §5, the judge's positive control)*
**2026-08-29 · corrected after seeing the number, and the reason it is legitimate matters**

The singleton-vs-core scoring gated on "core signal rate >= 0.90" and fired at 0.87.

That 0.90 came from the **key-based** control, where items are known-material *by
construction* — NCBE's examiners assigned them percentage weights. The **stable core** has
no such guarantee: "all five runs said it" does not mean "it matters." The four core items
rated non-signal were all sound-but-inapplicable (waiver of disclosure where the party did
disclose; writing and signature where nothing is disputed). Correct judgments about an
over-generating generator, not judge failures.

The judge's real validation already existed and passed: the key-based control scored **1.00**
on this same fact pattern with this same judge model.

**The gap bands (<=0.15 / >=0.35) were NOT changed.** They decide the actual question and
stand where they were pre-committed; the result reads MIXED under the original bands either
way. Correcting a control after seeing a number is defensible only when the
mis-specification is visible independently of the result — it is here — and only when the
decision thresholds are left alone. Both conditions held, and the distinction is recorded
so a later reader can check it rather than take it on trust.

**Effect:** the core rate is now used as a *reference distribution*, not a gate. Judge
validation routes to the key-based control. `score_strata.py --reread` recomputes a verdict
from a saved artifact without new model calls, so a corrected interpretation does not
require resampling the data it interprets.

---

### D9 — the cross-vendor residual averaged two directions that mean different things.
*(scripts/cross_residual.py; scoring-design.md's residual definition)*
**2026-08-29 · corrected before any result was reported**

The first cross-vendor measurement printed **"lift +0.130, SUBSTANTIAL"**. The corrected
metric on the same data gives **-0.114, NO EFFECT**.

`mean_pairwise` averaged both directions of the one-run-vs-one-run residual. That is fine
within a vendor, where the two sides are interchangeable, and wrong across vendors whenever
they differ in verbosity — which they do, 2.5x (gpt-5.2 56 items/run, claude-opus-4-8 22).
The symmetric mean fused *what B adds over A* (0.038, the question) with *what B lacks from
A* (0.553, a granularity difference) and reported 0.304 as a blind-spot effect.

Caught by the pool shape rather than by the number: B-only = 4 clusters against A-only = 40
is not the shape of a cross-vendor gain.

> *Annotation, 2026-09-16.* The figures above are the pool shape recorded for the **first**
> run. The only saved clustering, `runs/cross-residual.json` (one committed version, `689332a7`),
> is from the corrected run and reads **A-only 37, B-only 5** against a joint pool of 69. Cluster
> sets were persisted only after this fix, so the first run's shape cannot be checked against data.
> The catching signal is the same under either figure. Kept as recorded; not rewritten.

**Effect:** the residual is directional. LIFT = (what an A run misses vs a B run) − (what an
A run misses vs another A run), comparing like with like. A verbosity-asymmetry warning
fires at ≥1.5× and states that the directions are not interchangeable. Per-run cluster sets
are now persisted so a directional re-analysis never requires re-clustering.

Detail: [`cross-vendor-null.md`](./cross-vendor-null.md) §5.

---

### D10 — pooled clustering under-merges across vocabularies, inflating novelty.
*(scripts/cross_residual.py, scripts/self_residual.py — the comparison layer)*
**2026-08-29 · diagnosed, NOT fixed**

The structured enumerator (rung G4) emits terse formal taxonomy headings; free generators
emit descriptive fact-tied phrases. Clustering the pooled set across those two vocabularies
under-merges, so the structured walk's items read as novel when they name ground the free
generator covered.

**Caught by inspection, not by the number.** The supposedly-novel set included *"Premarital
contracts"* and *"Division of property"*, two items the examiners' key also covers
(which points, and their weights, are withheld), which `gpt-5.2` covered with 45 distinct labels. They cannot
be novel.

**The attempted fix made it worse.** Clustering on label + rationale, to bridge the
vocabularies, moved novelty lift +0.274 → +0.305. Mechanically: rationales made nearly
every item unique, pooled distinct strings rose 281 → 377, exact-duplicate savings vanished,
and the clusterer got a harder task rather than a better-informed one.

**Recommended fix, not yet implemented: replace pooled clustering with directed membership
queries.** The matching pass in scoring-design.md — "does this list contain key point K?" —
scores unanimity 1.00. Closed-set membership against a fixed reference works; open
clustering of a 300-400 item pool has produced every instability in this study (the 27%
floor swing, the intermittent unparseable replicates, this). Measure the residual as one
directed question per item against a fixed list. Generator runs already collected stay
valid.

**Effect:** the structured-enumerator novelty number (+0.305) is **not quotable**. The
fraction-of-union lift (-0.030) is less exposed but is measured through the same clustering
and is not independent evidence. Vendor-vs-vendor comparisons are *within*-vocabulary and
much less affected, but not immune.

Detail: [`structured-enumerator.md`](./structured-enumerator.md) §4.

---

### D11 — directed membership over-merges: the mirror image of the clustering bug.
*(scripts/residual.py — the second comparison-layer attempt)*
**2026-08-29 · built, measured, rejected**

Replacing pooled clustering with "is candidate X present in this list?" failed in the
opposite direction: a 10-item walk of broad taxonomy headings was judged to cover **261 of
281** specific candidates, collapsing the floor to 0.004 and marking nearly everything
shared. Tightening the prompt with explicit anti-inflation instruction barely moved it.

**The sanity check I built passed while the measurement was broken**, because it was
one-sided: it tested only for false novelty (does a gold point wrongly read as unfound?)
and was structurally blind to everything reading as present. A plausibility guard now
flags any run covering >3x its own item count and states that downstream numbers are
inflated toward "shared".

**Lesson worth keeping: a check that can only detect one direction of failure will pass
while the instrument fails the other way.**

---

### D12 — taxonomy projection is not well-defined either; the residual is ill-posed.
*(scripts/project_residual.py — the third attempt; supersedes the comparison layer)*
**2026-08-29 · NEGATIVE RESULT**

Projecting both generators onto the 350-node NCBE taxonomy produced plausible numbers
(9-15 nodes per run, floor 0.128) and reported **LIFT +0.207** for the structured
enumerator. It is a **filing artifact**: the "B-only" nodes include Contracts > Defenses >
Duress and undue influence, while gpt-5.2 explicitly produced "Defenses: duress/undue
influence". Both raised the doctrine; the projection filed one under Family Law and the
other under Contracts. The taxonomy carries the same doctrine in several places, so the
coordinate system is not unique.

**Three mechanisms, three failures, three directions** — clustering toward "different",
membership toward "same", projection toward "wherever it was filed". The generator-to-
generator residual is not noisy; it is **ill-posed**, and replication cannot fix an
underdetermined question.

**Effect:** the comparison layer of scoring-design.md is superseded. The recommendation is
to measure every generator **against the human-authored key** (weighted recall + yield,
both already built and reliable) and compare generators through their scores rather than
through a direct residual. The cost is stated plainly: a key-relative instrument cannot see
what the examiners did not grade, which is the original coverage question.

Detail: [`comparison-layer-negative.md`](./comparison-layer-negative.md).

---

### D13 — the positive control was confounded with recall.
*(scripts/score_all.py; scoring-design.md §5, the judge's positive control)*
**2026-08-29 · corrected**

The control asked, for **every** key point, whether at least one item cited as covering it
was rated sound + raised + material by the blind judge. A point the generator never covered
has no citing items, so it can never pass — the control is dragged down by low recall
rather than by a bad judge.

Measured on the July 2019 pattern the two are near-identical (recall/ctrl: 0.98/0.97,
1.00/1.00, 0.35/0.43). The control was carrying almost no independent information, and on a
low-recall generator it reads as "the judge is broken" when the finding is "the generator
missed things".

**Effect:** the control now scores only over the points a run actually covered — where this
generator claims to have found something, does a judge that never saw the key agree it is
real and material? Noise rate is unaffected either way; it never routed through the control,
which is why the structured walk's 0.64 noise stands as a finding while its control number
does not.

This is the third control-specification error in this study (D6, D8, D13). All three shared
a shape: a check that looked like it tested the judge but actually tested something else.

Detail: [`harder-pattern-scores.md`](./harder-pattern-scores.md) §5.

---

### D14 — hold-out recovery is undefined for coarse generators, and near-tautological for fine ones.
*(scripts/seeded_holdout.py — validation of the off-key measure)*
**2026-08-29 · found on inspection of a clean-looking result**

The leave-one-out hold-out printed recovery 1.00 / 1.00 / 0.00 across three rungs and 0.67
overall, identical in every weight band.

**The 0.00 is an artifact.** Every cited item in the structured walk covers 2.5 key points
on average (4 of 4 multi-cited), so hiding one point leaves the item matched to the others,
removes it from the off-key set, and makes recovery impossible by construction. The metric
is undefined for coarse generators; the 0.67 average is two rungs at 1.00 plus one the
metric cannot score.

**The 1.00 is weaker than designed.** Recovery needs (a) the item to match only the
held-out point and (b) the blind judge to rate it signal. For generators matching ~1:1
onto key points, (a) is automatic, so the measure reduces to (b) — which is what the
positive control already tests. The judge never saw the key in either case; hiding a point
from the SCORING key changes the bookkeeping, not the judgment.

**Effect:** the hold-out confirms the off-key bookkeeping does not leak known-material
content for fine-grained generators (60/60). It does NOT independently validate the judge
on ungraded material, because every seed was an examiner-graded item in disguise. The
control still cannot reach content that would never be on a key — which is the coverage
question. Genuinely obscure seeds, sourced outside the key and outside the model ecosystem,
remain the unrun experiment.

Detail: [`seeded-holdout-result.md`](./seeded-holdout-result.md).
