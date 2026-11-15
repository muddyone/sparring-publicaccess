# Coverage-instrument study — does the coverage residual find the things worth finding?

**Status: exploratory design note. No data collected. Nothing locked.** *(Annotation 2026-09-16: that was the status when this README was written. The study ran on 2026-08-29; its results are in this directory's write-ups and in the Measurement paper §6.)*

Tests the **instrument** before building on it. `docs/research/verifiable-trust-rider-claims.md`
§3 proposes measuring coverage by running an independent generator and counting what it
surfaces that the first run missed — and puts that count on the same footing as the
grounding rate.

It is not on the same footing. The *generation* is independent; the *measurement* is a
semantic-matching judgment of unmeasured reliability. As specified, the coverage residual
is the analogue of **the rubric**, not of the model-free existence check.

It also has a blind spot shaped exactly like the failure it was built to catch: **two
generators that share a blind spot produce a residual of zero, and zero reads as good
coverage.** A false-clean, from an instrument invented to detect false confidence.

This study puts the instrument on a corpus where the answer is already known — law-school
issue-spotters with published model answers — and asks whether it finds the **obscure**
items, which are the only ones that matter.

Contents:

- [`design-note.md`](./design-note.md) — the design. Exploratory; §0 explains why that is
  the correct status and §11 says what would have to be true to earn a real
  pre-registration later.
- `deviations.md` — created when work starts.

**Read before working here:**

- [`../../docs/research/verifiable-trust-rider-claims.md`](../../docs/research/verifiable-trust-rider-claims.md)
  §3 (the coverage proposal this study tests) and §5 (its open questions, two of which
  this design answers).
- [`../resolver-dv-reliability-2026-08-28/design-note.md`](../resolver-dv-reliability-2026-08-28/design-note.md)
  — R8. The measurement discipline here is imported from its §3–§4, and R8 phase 1 is the
  working rehearsal of that machinery on a smaller problem. **Run it first if it has not run.**
- [`../../docs/research/paper-1-followups-register.md`](../../docs/research/paper-1-followups-register.md)
  — the 2026-08-28 coverage entry this study descends from.

**No human evaluation.** SPARRING has none available; live expert rating is deferred and
disclosed, as in Paper 1. The design's anchor outside the model ecosystem is a **frozen
human-authored gold set** — an answer key written before this system existed — not a
recruited rater. §3 of the design note explains why that satisfies the same requirement.

**Governance:** a Proposer-line study. Routes to the **Measurement paper** (Paper 2, renumbered 2026-08-30) and to the coverage
instrument. **Not** errata for the published Resolver paper (`10.5281/zenodo.21210264`,
locked).
