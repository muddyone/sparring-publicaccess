# Errata and queued corrections — *Governance by Verifiable Challenge*

**Concept DOI:** [10.5281/zenodo.21210264](https://doi.org/10.5281/zenodo.21210264) (resolves to
the latest version). **Currently published:** v6, record 21272051.

This is the standing register of corrections **confirmed but not yet in the published record.**
It exists so that a reader of the current version can see what the authors already know is wrong
with it, without waiting for the next version to be cut.

## Why corrections are batched rather than shipped one at a time

Every Zenodo version is a separate citable record. Cutting a new one per typo dilutes the record
and scatters citations across versions that differ trivially. Corrections are therefore
accumulated here and applied in batches.

**The queue is short by construction.** A published paper is a record of an experiment, not
documentation of current tooling, so only one class of change is ever eligible:

> **Eligible:** it makes the paper *more accurate about what was actually run.*
>
> **Never eligible:** it makes the paper *more current with the tooling.* Not as a small sync,
> not while we are in there anyway.

That test is why this register can be public without embarrassment — everything on it is an
erratum in the ordinary scholarly sense, and nothing on it is housekeeping.

**An item is added when it is confirmed, not when it is suspected.** Open questions live in the
authors' working notes until they resolve one way or the other.

---

## Queued

### Q1 · §13 — Zenodo DOI corrected in the source, not yet in the published PDF

**Status:** correction written and approved 2026-07-16; rides into the next version cut.
**Affects:** the archive link in §13 of the published v6 PDF.

The §13 DOI was wrong in a way that made the paper less accurate about the location of its own
archived record. It is fixed in the working source. Zenodo v6 still serves the uncorrected PDF,
so the published artifact and the source deliberately diverge until the next cut.

**Why it qualifies:** a broken pointer to the paper's own archive is an accuracy defect about
what was run and where it lives.

### Q2 · §13 — the catch-rate study's data is now public and is not listed

**Status:** confirmed 2026-09-02. **Affects:** the availability statement in §13.

§6.3's controlled catch-rate study (A-v3) had no public data at the time of publication; its
whole public presence was one rendered figure. The full pilot — pre-registration, the
generator × auditor × condition grid, the panel-confirmed flaw sets, the blind catch-codings, the
problems, the recommendations under test, and the figure code — is now published at
[`governance/catch-rate/`](./governance/catch-rate/). §13's availability statement should list it.

**Why it qualifies:** the availability statement is a claim about what a reader can check. It is
now understated, which makes the paper less accurate about its own evidence.

---

## Applied

*(Nothing yet. Items move here, with the version they landed in, when a cut ships.)*

---

## What is deliberately **not** here

- **Anything that would resync the paper with current tooling.** The Rapier engine, the skills,
  the ledger fields and the framework spec have all moved since publication. The paper describes
  the instrument as it was when the study ran, and it stays that way.
- **New findings.** A result that arrived after publication belongs in its own study, not as an
  amendment. That includes new findings about the same subject.
- **Disagreements with the paper's conclusions.** Those are arguments, and they belong in the
  literature rather than in a correction notice.
