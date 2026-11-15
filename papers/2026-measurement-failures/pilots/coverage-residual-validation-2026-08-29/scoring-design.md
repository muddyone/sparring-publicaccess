# Scoring design — both directions

**Status: exploratory design. Resolves the open question recorded as deviation D3
(*recall against gold, alone, cannot be the primary endpoint*).**
**Decided 2026-08-29 by Bart: score both directions.**
Supersedes the measurement section of [`design-note.md`](./design-note.md) (§5).

---

## 1. Why one direction was not enough

The pipeline smoke test returned **57 issues against an answer key of 5**, covering every
key point several times over (detail: [`corpus-recon.md`](./corpus-recon.md) §4, the
smoke-test finding). Measuring only *how much of the key was found* would have scored that
run **100%** — and would score a generator that lists every doctrine in the subject 100%
too. Recall alone cannot tell coverage from padding, which makes it useless for the exact
question this study asks.

So the study measures two things about every run:

| Direction | Question | What it catches |
|---|---|---|
| **Recall** | Of the examiners' weighted points, how many did the generator surface? | missing the issues that mattered |
| **Yield** | Of everything the generator emitted, how much was sound, material, and actually raised by these facts? | burying the decisive issue in noise |

A generator must do well on **both**. Perfect recall with 10% yield is a generator that
said everything; high yield with poor recall is one that was too timid. Neither is coverage.

## 2. Two passes, deliberately different information sets

This is the load-bearing structural decision, and getting it backwards would invalidate
the whole measurement.

| | **Pass A — matching** | **Pass B — adjudication** |
|---|---|---|
| **Sees** | generator items **+ the answer key** | generator items **+ the fact pattern only** |
| **Never sees** | — | **the answer key** |
| **Asks** | which key points does this cover? | is this item sound, material, and raised by these facts? |
| **Yields** | recall (weighted) | yield, noise rate, off-key discovery |

**Pass B must not see the answer key.** If it does, it will mark everything off-key as
unsound — the key becomes the definition of soundness, and the study can no longer detect
a real issue the examiners chose not to grade. That case is not hypothetical; an examiner's
key is exhaustive over what is *scored*, not over what is *sound*, and the difference is
precisely where a coverage instrument should earn its keep.

## 3. The adjudication categories (Pass B)

Each emitted item is classified against the fact pattern alone:

- **`sound`** — a real legal issue, correctly stated.
- **`raised`** — actually put in play by *these* facts, not merely adjacent doctrine.
- **`material`** — could change the analysis or the outcome if resolved either way.
- **`duplicate_of`** — restates an earlier item at a different granularity (the 57-vs-5
  gap is largely this, and it must be collapsed before any count means anything).

An item is **signal** if it is sound **and** raised **and** material **and** not a duplicate.
Everything else is **fill** — sub-classified as unsound, unraised, immaterial, or duplicate,
because *which kind* of fill a generator produces is diagnostic and gets reported, not
averaged away.

## 4. The measures

Let **K** = the examiners' weighted points (weights sum to 100), **E** = items emitted,
**S** ⊆ E = signal.

- **Weighted recall** = Σ weights of key points covered ÷ 100.
  Materiality-weighted by the examiners' own percentages, not a bare count — missing a
  35% point is not the same as missing a 10% point, and the examiners already told us so.
- **Yield** = |S| ÷ |E|. The padding penalty.
- **Off-key discovery** = signal items matching no key point ÷ |E|. The measure the
  original design could not take: **sound, material issues the examiners did not grade.**
  Reported separately from noise, never merged with it.
- **Noise rate** = items failing `sound` or `raised` ÷ |E|. The dangerous fill — an
  invented issue is worse than a redundant one.
- **Redundancy** = duplicates ÷ |E|. Cheap fill. Reported apart from noise.

**No composite.** Each is reported with its own reliability, per the measurement discipline
inherited from R8 (the study asking whether the resolver's scoring yardstick is stable) and
from Matthew Niedner's 2026-07-30 review: never build a single number from components of
unequal reliability.

## 5. The answer key doubles as a positive control on the judge

The obvious objection to scoring the second direction is that it rests on a model judging
soundness and materiality — the weak joint flagged in the design note's §0 (why this study
is exploratory). The answer key closes most of that gap, and this is the part of the design
worth keeping:

> **Every key point is a known-material item.** The examiners assigned it a weight. So Pass
> B, which never sees the key, can be checked against it after the fact: **does the blind
> judge rate the key-covered items as sound, raised, and material?**

If it does not, its judgment is demonstrably bad and the yield numbers are worthless —
detected from inside the study, before anything is concluded. If it does, the judge has
cleared a real known-answer bar on the subset where truth is available, which is the same
move the whole study makes one level up.

This is a **validity check with a pre-committed floor**, and its first version was wrong
in a way worth recording.

**First specification (wrong):** *every* key-covered item must be rated signal. It failed
at 0.50 on the first run — correctly, for the wrong reason. When 18 emitted items all cover
one key point, most of them **are** duplicates, and a blind judge saying so is right.
Deduplication is orthogonal to whether the judge can recognise a known-material issue.

**Respecified:** for each key point, **at least one** covering item must be rated
sound + raised + material. The duplicate flag is ignored in the control by design. Floor
**≥ 90%** of key points. Below that, Pass B is rebuilt before its outputs are used for
anything. Recorded as deviation D6 (*the positive control was mis-specified*).

## 6. Reliability, unchanged from the design note

- **k = 5** replicate passes for both A and B, each blind to the others.
- **Cross-vendor adjudication** on disagreement — human gold is unavailable by standing
  constraint, so structural independence substitutes.
- **ρ ≥ 0.70** floor to enter any aggregate; criteria below the floor are reported, not
  dropped.
- **Anchored scales** — each category gets a written definition and a worked example.
- **Disagreement is reported as a result**, not cleaned up.

### Cross-pass conflict — a diagnostic the two-pass split makes available for free

Because the passes see different things, they can be compared. When Pass A (which sees the
key) credits an item as covering a key point while Pass B (blind) rates the facts as not
even raising it, that is **matcher generosity**, and it inflates recall.

The first run showed **10 of 49** credited items in that state. It is reported, never
silently corrected — a matcher that is generous by a known amount is usable; one that is
generous by an unknown amount is not.

## 7. What this changes downstream

- The **primary endpoint** is now the pair (weighted recall, yield), stratified by
  obscurity — not recall alone.
- The **stop rule** (design note §9) was written in terms of recall on the obscure tercile.
  It needs restating against the pair and is **not yet rewritten** — flagged rather than
  quietly reinterpreted.
- **Off-key discovery becomes a headline quantity.** The original design recorded off-key
  items and scored them neither way; that was the hole. It is now one of the two things
  the study is for.
