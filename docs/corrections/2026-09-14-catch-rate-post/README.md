# Catch-rate post: the numbers behind the correction (2026-09-14)

This folder backs a correction to the LinkedIn post *"Adding a model to your pipeline buys you almost
nothing"* (2026-09-05). It sits outside the evidence folder of the paper that reports the study (the
[preprint](https://doi.org/10.5281/zenodo.21272051)), and the paper is unchanged.

## What the correction says

The post said that when a challenged model revised its own work, it *"gave back roughly two-thirds of what
it caught"*, introducing about 2 new flaws per answer. That figure is the grader's reading, not a
measurement of what the revision did.

**The same grader, run on the original drafts that nobody revised, finds an average of 1.95 "new" flaws
per draft.** So "two-thirds" is the top of the possible range for what the revision gave back, not a
measurement of it. The paper already says to read these counts as upper bounds (§6.4 of the preprint).
The post left that out.

**What still holds.** These results compare drafts graded the same way. So the grader's baseline, the
1.95 "new" flaws it finds in a draft nobody touched, should cancel out of them, and if anything it would
make the gap in new flaws look smaller than it is. "Why only comparisons carry" explains why.

- **It fixed more.** The challenged revision fixed more of the original flaws than the model revising on
  its own: 27 of the 31 original flaws across the eight drafts, against 23 of 31.
- **It added more.** It also ended with more new flaws: about 0.9 more per draft when the challenger was
  the same model, and about 1.4 more when it was a different model.
- **It came out no cleaner.** It left 2.625 and 3.125 flaws per draft, against 2.25 for the model
  revising on its own.
- **It replaced more of the text.** The challenged writer replaced far more of its original text: about
  80% of the original's words, against 58%. Both drafts grew to about 1.8 times the original's length.

These are small numbers: eight problems, one run each, and no statistical test. Read them as directions.

## Why only comparisons carry

The grader counts any flaw that wasn't on the original list as "new", and it finds an average of 1.95 of
them in a draft nobody touched. So a count of "new flaws the revision introduced" mixes real new flaws
with the grader's own baseline, and the data can't separate the two.

A difference between two drafts graded the same way cancels that baseline, as long as the baseline is
the same for both. Two things bear on that here:
- **Length.** The challenged and self-revised drafts grew to about the same length. So any baseline that
  comes from the grader reading a draft of that length should be about equal in both.
- **Text kept.** The challenged drafts kept less of the original text: about 20% of its words, against
  42%. So any part of the 1.95 that is flaws already in the original text should be smaller in them. That
  would make the gap in the counts smaller than the real one, not larger.

A size doesn't cancel the baseline, and neither does a ratio.

## What each file is

| file | what it is |
|---|---|
| `denoise-new-counts.json` | The grader's "new"-flaw count for each of the 8 original drafts, graded 5 times each: 40 counts, with a mean of 1.95. It also holds the same grader's counts on three sets of revised drafts, and the comparisons above. Numbers only, no draft text. |
| `denoise_new_counts.py` | The script that reads the 40 grading records of the original drafts, and the 24 of the revised drafts behind the comparisons, and writes `denoise-new-counts.json`. |
| `preservation.py` | The script that measures how much of a draft each revision kept. |
| `preservation-results.json` | The script's full output: every draft and every patch. |
| `preservation-results.md` | The same results as tables. It includes a note correcting a misleading label in one of the study's earlier summary files. |

**Folder names in the hashes.** The input hashes use the study's working folder names.
`resolver-iteration-2026-06-29/…` is
[`papers/2026-resolver-governance/governance/resolver-iteration/…`](https://github.com/muddyone/sparring-publicaccess/tree/main/papers/2026-resolver-governance/governance/resolver-iteration)
in this repository, and `catch-rate-v3-2026-06-28/…` is
[`…/governance/catch-rate/…`](https://github.com/muddyone/sparring-publicaccess/tree/main/papers/2026-resolver-governance/governance/catch-rate).

**Condition names used in the files:**
- **R0** is the original draft.
- **R1** is one challenge, after which the writer revises once. `same` means the challenger was the same
  model as the writer; `cross` means a different one.
- **R1′** (`R1prime`) is the writer revising twice on its own, with no challenger.
- **R2** is challenger and writer going back and forth until they agree, or for up to five rounds.
- **R3** is a later, smaller test. The writer was told to make minimal patches, and a check could reject
  a patch.

## How the numbers were derived

**The 40 counts.** On 2026-06-30, each original draft was re-graded five times with the study's own
grader: one AI auditing from three angles, and the same step that decides which flaws are "new". This is the
"denoise" run: it re-graded every draft in a later test's 61 revision decisions five times, the eight
untouched originals among them, to see how much the grader's scores move. The file and script names come
from it. Its code and summary are public:
[`stage0_denoise.py`](https://github.com/muddyone/sparring-publicaccess/blob/main/papers/2026-resolver-governance/governance/resolver-iteration/scripts/stage0_denoise.py)
and
[`stage0-denoise.json`](https://github.com/muddyone/sparring-publicaccess/blob/main/papers/2026-resolver-governance/governance/resolver-iteration/analysis/stage0-denoise.json).
`denoise_new_counts.py` reads the 40 grading records and writes only the counts (78 in total; 78 / 40 =
1.95).

**The comparison counts.** These come from the study's 24 grading records for the revised drafts, which
`denoise_new_counts.py` also reads. They match
the table in the study's
[`results.md`](https://github.com/muddyone/sparring-publicaccess/blob/main/papers/2026-resolver-governance/governance/resolver-iteration/results.md).

**How much of a draft was kept.** Each revised draft's words are compared with the prior version's. Words
are split on whitespace and matched in order with Python's `difflib` (`autojunk=False`). The script always
reports three numbers:
- the share of the prior version's words not kept;
- the share of the new draft's words that are new;
- the length ratio.

Any one alone can mislead. A draft that keeps every word and appends five times as much scores zero on the
first.

## What you can and can't recompute from what's public

- **Checkable against public files:**
  - each original draft's five grading totals match the round-1 `champ_nets` in the public
    `stage0-denoise.json`;
  - the three comparison means (new flaws per draft for R1 same, R1 cross and R1′) match the public
    `results.md`;
  - 78 / 40 = 1.95 is arithmetic on the file.

  **The division is checkable, but the 78 itself is not.** It comes from the split below. You can
  confirm it only by matching the hashes of the omitted files, or estimate it afresh by re-grading.
- **Resting on files the public archive omits (available on request):**
  - how each total splits into listed flaws and "new" flaws. That split is what gives the 78 "new"
    flaws behind the 1.95;
  - the per-draft counts for the revised drafts;
  - every preservation figure.

  They come from the raw run files
  ([`RAW-RUNS-OMITTED.md`](https://github.com/muddyone/sparring-publicaccess/blob/main/papers/2026-resolver-governance/governance/resolver-iteration/RAW-RUNS-OMITTED.md)),
  which are available from the author on request. Each JSON file lists a SHA-256 hash for every input, so
  you can confirm you received the same files.
- **Re-gradable from public files, with model API access:** the eight original drafts. Their texts, flaw
  list and problems are public, and so is the grader. A new run gives new counts, not the same 40.
- **Re-running the two scripts** needs those raw run files, so neither can be re-run from public files
  alone. Both also expect the study's own folder layout (see the folder-name mapping above).

## Licence

As for the rest of this repository: text and data are CC-BY-4.0
([`LICENSE`](https://github.com/muddyone/sparring-publicaccess/blob/main/LICENSE)), and code is Apache-2.0
([`LICENSE-CODE`](https://github.com/muddyone/sparring-publicaccess/blob/main/LICENSE-CODE)).
