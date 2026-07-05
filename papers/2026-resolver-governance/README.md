# Auditable adversarial review for AI-in-the-loop decisions

**An empirical report on SPARRING's Resolver: a pre-registered null redirects an
AI-deliberation study from "better answers" to governance by verifiable challenge.**

Author: Barton Niedner ([ORCID 0009-0003-4117-3426](https://orcid.org/0009-0003-4117-3426)), Resource Forge LLC.

> Archival DOI: _minted on first release (`paper-2026-resolver-v1`); see repository releases._

## What's here → where it maps in the paper

| Folder | Contents | Paper |
|---|---|---|
| [`preprint/`](preprint/) | Draft source (`preprint-draft.md`), `refs.bib`, figures, build recipe | the report itself |
| [`study-output-preference/`](study-output-preference/) | Pre-registration, design, frozen results, analysis code, decision packs, both conditions' outputs, rater rubric | §3–§5 (the rater study + its null) |
| [`governance/mechanism-audit/`](governance/mechanism-audit/) | Would-have-shipped catches; both coding passes; ledger | §6 (consequential) |
| [`governance/seeded-defect/`](governance/seeded-defect/) | Pre-registrations, cases, the **grounding verifier + self-tests**, run results | §7–§8 (grounded, machine-checked) |
| [`governance/resolver-iteration/`](governance/resolver-iteration/) | Pre-registration, blind codings, per-round results, analysis, code | §6.4 (iterate-to-agreement null) |
| [`prior-pilot/`](prior-pilot/) | V1 pre-registration, results, preprint | §5.2 (the "V1 reversal"; the paper does **not** stand on it) |

## Reproducing the core claims

- **Pre-registration lock** — `study-output-preference/pre-registration.md`. The plan
  was locked before any rater data existed (originally git tag `v2-prereg-2026-05-03`
  in the author's working repository, 2026-05-03; see the paper's §3.1 and limitations
  for how the lock is anchored).
- **The null** — run `study-output-preference/scripts/analyze-v2-primary.php` against
  `study-output-preference/analysis/primary-results.json`.
- **Machine-checkable grounding** — `governance/seeded-defect/scripts/` contains the
  grounding verifier and its `--self-test` suites; the existence check uses no model.

## De-identification

Raters appear only as `External rater E1`…`E5` and user ids — no names or emails.
The mechanism-audit corpus is the author's own commercial codebases; only derived
findings/codings are included, never source. Raw per-run transcripts for §6.4 are
omitted (see `governance/resolver-iteration/RAW-RUNS-OMITTED.md`).
