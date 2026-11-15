# Deposit archive: the SPARRING Measurement paper

This archive holds the data and code behind the paper *Twenty-four results that didn't mean what
their labels said: measurement failures from a project testing whether AI systems can be trusted
to report on their own reliability* (Barton Niedner, Resource Forge LLC, 2026). Section 12 of the
paper ("Data and code availability") describes what the archive contains, and this file is the
archive README that section refers to.

The work was done in the author's private working repository. Everything here is copied from it,
and the paths are the working repository's paths, so references in the paper and in the study
write-ups resolve inside this archive. `PROVENANCE.md` gives the source commit, date and SHA-256 of
every file.

Text is licensed under CC BY 4.0 and code under Apache 2.0, as stated in the paper.

---

## What is here, and which part of the paper it supports

| path | what it is | paper |
|---|---|---|
| `pilots/measurement-2026-08-30/paper-draft.md`, `refs.bib` | the paper's source and its bibliography | all |
| `docs/findings/instrument-failure-catalogue.md` | the full instrument-failure catalogue at 24 entries. The paper condenses it as Appendix A. The working repository keeps adding to it; this copy is the one the paper reports | §4, §5, §8, Appendix A |
| `pilots/seeded-miss-2026-08-29/` | **the seeded-miss study (Case B)** | §7, §8.1, §9.1, §9.2, Appendix B |
| `…/design-note.md` | the design note, which fixed the analysis decisions in advance (see "Timing" below) | §3.2, §7.1 |
| `…/deviations.md` | the deviation ledger: each departure from the design, dated, with what data existed at the time | §7, §12 |
| `…/result.md`, `first-result.md`, `README.md` | the study's write-ups. They record the 33-case state and carry dated annotations pointing to the current figures | §7 |
| `…/scripts/` | fetch (`fetch_opinions.py`), screen (`screen_cases.py`), generate (`generate_miss.py`), score (`score_seed.py`), and the variance and profiling tools (`variance_budget.py`, `compare_k.py`, `case_profile.py`) | §7, §9.2 |
| `…/corpus/cases.json` | the stimulus exactly as handed to the generators (append-only, so it serves every pass) | §7.1 |
| `…/corpus/screen.json`, `candidates.json` | the screening record and the candidate list | §7.1 |
| `…/corpus/leakage.json` | the current leakage audit (five replicates), including the two cases the stimulus-validity gate removed | §7.1, §8.1 |
| `…/runs/<case>.g{1,3}.r{1,2}.json` | all 196 generator run outputs (49 cases × 4), including the 8 runs of the two gated cases, *Eqbal v. Blanche* (`10941690`) and *People v. Occhipinti* (`10937255`) | §7 |
| `…/runs/scored.json` | the current scoring, pass 5: 47 cases, 188 runs, four scoring replicates | §7.1–7.5, §7.6 |
| `…/runs/seed-recovery-report.json` | the current report, derived from `scored.json` | §7 |
| `…/history/pass1-2fb281f0/` … `pass4-f34fe596/` | **scorings that existed only in version history**, exported as files: passes 1 to 4, each `scored.json` with the `leakage.json` it was read under | §7.6, §9.1, §9.2, Appendix B |
| `…/attic/scored.k2.json` | the k=2 scoring of the earlier corpus, with leakage labels re-stamped under the five-replicate audit | §9.1, §12 |
| `…/attic/scored.pre-restamp.json` | the pre-correction state behind catalogue entry 13 (the raced 0.58) | §4.3, §7.6 |
| `…/attic/scored.exclusive-only.json` | pass 2's first scoring (0.50, before the 0.55 re-scoring) | §7.6 |
| `pilots/coverage-residual-validation-2026-08-29/` | **the coverage study (Case A)** | §6, §9.3 |
| `…/design-note.md` | expectations written before the data. It was declared exploratory and is not a pre-registration | §6 |
| `…/deviations.md` and the other `*.md` files | the deviation ledger and the study's write-ups | §6, §9.3 |
| `…/scripts/` | 16 scripts: corpus rebuild (`fetch_corpus.sh`, `extract_questions.py`, `extract_gold.py`, `extract_taxonomy.py`), generation, scoring, residual and recount tools | §6, §9.3 |
| `…/runs/*.offkey-recount.json`, `runs/recount.log` | the off-key recount outputs | §9.3 |
| `…/runs/` (other files) | derived scorings: key-relative scores, cross-vendor and self residuals, the seeded holdout, the granularity arms, and the scorer smoke test's scored output | §6 |
| `pilots/resolver-iteration-2026-06-29/scripts/lib_llm.py` | the shared model-calling helper both studies import. It is deposited unchanged. A check on 2026-09-16 found it byte-identical to the copy in the Resolver paper's public archive (`papers/2026-resolver-governance/governance/resolver-iteration/scripts/lib_llm.py`) | §12 |

`pilots/coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md` is **not
included**: it is planning for a companion paper that has not been published, and working material
for unpublished papers stays out of public archives. Some write-ups here still link to it, and
`implications-for-paper-2.md` is a redirect to it left over from a series renumbering; those links
do not resolve in this archive.

### Timing of the seeded-miss design note

The design note says it was written before any data was pulled. It was first committed together
with the initial corpus, so there is no separate timestamp for it. The ordering rests on the note's
own statement, and on the deviation ledger, which dates each departure and says what data existed
when it was made.

---

## What is not here, and why

### Withheld material: NCBE-derived answer keys

The coverage study used the National Conference of Bar Examiners' (NCBE) Multistate Essay
Examination questions and model analyses. Those are NCBE's copyright, and the fact patterns were
never committed anywhere. The study derived a structured answer key from NCBE's analyses: issue
statements plus the percentage weight of each point. **That key is withheld from this archive.**
NCBE's analyses are third-party copyrighted material, and the author decided (2026-11-15) not to place an
answer key derived from them in a public archive without clear rights to redistribute it. The paper's §12
provides for this: material is deposited only as far as NCBE's terms allow, and anything withheld is listed
here. Withheld:

- `pilots/coverage-residual-validation-2026-08-29/gold/gold.json`: the structured answer key
  (60 fact patterns, 227 weighted points).
- **66 of the 83 files** in `pilots/coverage-residual-validation-2026-08-29/runs/`: the 65
  generator run outputs (`<fact-pattern>.<rung>.r<N>.json`) and the scorer smoke-test input
  (`smoke-feb2018-familylaw.gpt52.json`). Each of them carries its fact pattern's full answer key in
  a `gold` block. The fact pattern itself is already a placeholder in every one.

- **Excerpts trimmed from deposited write-ups**, which otherwise carried NCBE-derived text:
  `corpus-recon.md` (one fact pattern's answer-key points and weights, replaced by a note),
  `harder-pattern-scores.md` (one quoted issue statement and two point weights, replaced by a note), and
  `runs/july-2020-secured-transactions.seeded-holdout.json` (NCBE point IDs replaced by opaque labels
  p01–p06 and weights set to null; recovery results unchanged), and the answer-key point IDs, weights,
  ranks or issue statements in `comparison-layer-negative.md`, `structured-enumerator.md`, `deviations.md`,
  `first-scored-run.md` and `taxonomy-granularity-finding.md`. `PROVENANCE.md` §3a records these
  changes, which were made in this archive only.

**Deliberately kept.** These are not the answer key and stay in the archive: the headings of NCBE's public
MEE Subject Matter Outline (for example "Premarital contracts"), which the study's structured walk used as its
taxonomy; the generators' own labels and outputs as scored; lists of missed points by point ID alone, without text or
weights (for example in the `key-relative-scores` files); and counts of points per fact pattern.

`PROVENANCE.md` §4 lists every withheld file by name, with its SHA-256, so the files can be matched
exactly if they are ever released.

**Where the source is.** NCBE publishes the MEE questions and analyses the key was built from on its own
site, https://www.ncbex.org. The exact files the study used are listed in `scripts/fetch_corpus.sh`, which
downloads them.

**Effect on re-derivation.** The §9.3 recount outputs and the other derived coverage scorings *are*
deposited, so §9.3's figures re-derive from this archive. Re-running the coverage scorers from
scratch needs the answer key and the generator outputs. A reader can rebuild the corpus and the key
from NCBE's published PDFs with `scripts/fetch_corpus.sh`, then `scripts/extract_questions.py` and
`scripts/extract_gold.py`. The generator outputs can only be regenerated, not recovered, and model
outputs are not deterministic.

### Excluded

- **The CourtListener opinion cache** (`pilots/seeded-miss-2026-08-29/corpus/raw/`). This is
  excluded for size, not rights: US judicial opinions are public domain. `scripts/fetch_opinions.py`
  rebuilds the cache, and `corpus/cases.json` already holds the exact text given to the generators.
- **NCBE fact patterns and model analyses** (`coverage…/corpus/`, `runs/*.raw.json`). These are
  NCBE copyright and were never committed.
- **Machine state** (`seeded-miss…/runs/.quota_reset`).
- **Code for figures computed during review.** This covers §7.3's between-stratum intervals and power
  estimate, §7.4's paired vendor comparisons, the gate's 0.06–0.08 share in §7.6, and the simulation
  behind catalogue entry 24. Section 12 says so, each passage states its method, and the data those
  figures were computed from are here.

---

## Re-running

### Requirements

Python 3 and `requests` (`pip install requests`). No other package outside the standard library is
imported. `fetch_corpus.sh` also needs `curl` and `pdftotext` (poppler-utils), and the NCBE
extractors read the `.txt` files it produces.

The scripts find their default data relative to their own location (`scripts/../corpus`,
`scripts/../runs`). They import shared code through relative `sys.path` entries:
`../../resolver-iteration-2026-06-29/scripts` for all of them, plus
`../../coverage-residual-validation-2026-08-29/scripts` for the seeded-miss scorer. Keep this
archive's layout intact. File paths you pass as arguments are relative to your working directory.

### API keys: environment variables

**Nothing that re-derives a figure from the deposited scorings calls a model or needs a key.** For
example, from `pilots/seeded-miss-2026-08-29/`:

```sh
./scripts/variance_budget.py                     # variance budget on the current scoring
./scripts/compare_k.py --a attic/scored.k2.json --b history/pass4-f34fe596/scored.json \
                       --label-a k=2 --label-b k=4   # the §9.1 replicate comparison
./scripts/case_profile.py --scored runs/scored.json
```

These three were run from this archive, with no keys set, as it was built. They reproduced §7's
headline (clean stratum 0.500, 15 cases, 95% interval [0.33, 0.67]) and §9.1's comparison
(clean stratum 0.64 → 0.58, off-key run-level agreement 0.81, partial credit 50 of 52, 17 of 33
cases moved).

Re-running a **model pass** (generating, screening, scoring or recounting) calls vendor APIs at your
own cost, and needs your own keys:

| variable | used by |
|---|---|
| `ANTHROPIC_API_KEY` | every Claude call (`lib_llm.py`) |
| `OPENAI_API_KEY` | every GPT call (`lib_llm.py`) |
| `COURTLISTENER_TOKEN` | `seeded-miss…/scripts/fetch_opinions.py` |
| `SPARRING_ENV_FILE` (optional) | path to a `KEY=VALUE` file to load the variables above from, instead of exporting them |

**The archive copies differ from the working repository here, and only here.** In the working
repository, ten scripts read keys from a hard-coded `.env` path on the author's machine. In this
archive that lookup reads the environment variables above instead. `PROVENANCE.md` §3 lists the ten
files with their before and after hashes. No other code was changed. Some of the study write-ups
still say keys go "in the project `.env`", which describes the working repository.

The model versions the studies pinned (for example `gpt-5.2`, `claude-opus-4-8`) are named in the
scripts and recorded in each output file. A re-run on later model versions is a new measurement, not
a reproduction.
