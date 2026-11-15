# Seeded-miss experiment (CourtListener), 2026-08-29

Does **off-key discovery** — the coverage line's only measure of ungraded material — recover
a consideration a real decision-maker actually failed to weigh?

Seeds come from appellate opinions holding that a tribunal below **erred by failing to
consider** something: the decisive consideration is on record precisely because someone
missed it. Opinions are filed after both vendors' training cutoffs, so contamination is
excluded rather than bounded. This is the experiment specified in the parent study's
[`seeded-holdout-result.md`](../coverage-residual-validation-2026-08-29/seeded-holdout-result.md) §4.

## Read in this order

| file | what it is |
|---|---|
| [`design-note.md`](./design-note.md) | **Pre-registration**, written before any data was pulled |
| [`result.md`](./result.md) | **The result** — 100 runs, 25 cases |
| [`deviations.md`](./deviations.md) | Every departure from the design, with its timing and what data existed |
| [`first-result.md`](./first-result.md) | Superseded interim (52 runs); kept because one of its exploratory cuts reversed |

## Headline

> *Annotation, 2026-09-16.* The figures in this README are the 33-case state. The current
> headline (47 cases scored) is **0.50, 95% interval [0.33, 0.67]**, and the "case selection dominates
> about 2:1" budget below is withdrawn: its judge term compared runs mostly scored once, and the
> tool's conversion overstates the judge term by about 30% (catalogue entries 23 and 24). The
> Measurement paper §7 and §9.2 are the current account. Kept as recorded; not rewritten.

132 runs over 33 cases, scored at k=4 with the leakage audit at k=5. Off-key recovery in the
neutral stratum = **0.58**, against raw recovery of **0.92**. The generators found what the
court missed; the exclusive-match rule discarded the evidence. Dropping that rule (partial
credit) recovers **0.92** — the shortfall was the measurement, not the generators.

But partial credit **saturates** (0.92/0.92/1.00 across strata), so the two rules have
different jobs: partial credit for "did it find it", exclusive match for "does this condition
beat that one". See `result.md` §1b.

Controls: positive **0.97** (floor 0.90); negative **0.01** false-positive over 390
inapplicable decoy seeds scored in the same shuffled call as the real seed.

**Read §5 before quoting any number here.** The headline's 95% interval is roughly
[0.33, 0.81]; differences below ~10 points are noise; and raising the replicate count was
tried and does not fix it.

## Pipeline

```
scripts/fetch_opinions.py    search + fetch, throttled and resumable
scripts/screen_cases.py      screen for a real holding, then three-call blind extraction
scripts/generate_miss.py     run generators on the situation alone
scripts/score_seed.py        four judging passes -> recovery, controls, leakage strata
```

Each stage is resumable and caches to disk; re-running skips completed work.

**Rate limits are strict and the opinions endpoint is easy to get wrong: 50/hour** (search is
5/minute). Free Law Project is a non-profit — the corpus is pulled once, not swept.

`corpus/raw/` is gitignored for size; US judicial opinions are public domain. The derived
stimulus (`corpus/cases.json`) carries the exact text handed to the generator and **is**
committed, so every number here is reproducible without a token.

## Resuming the corpus expansion (blocked until the quota resets)

**State as of 2026-08-29 evening:** 122 candidates searched, 109 opinions cached, 102
screened, 39 kept, 34 extracted, **9 in the clean (neutral) stratum** — which is the
stratum the headline is computed on and the binding constraint on its precision.

The CourtListener **125/day account cap** was exhausted widening the search. Nothing is
broken and no design work is outstanding; the widened 13-phrase query list is already in
`scripts/fetch_opinions.py`. To resume once the quota resets:

```bash
cd pilots/seeded-miss-2026-08-29
rm -f corpus/candidates.json          # force a re-search with the 13-phrase list
./scripts/fetch_opinions.py --limit 400   # exits 75 with a reset time if the cap hits again
./scripts/screen_cases.py             # resumable; skips everything already screened
./scripts/generate_miss.py -n 2       # resumable; skips runs already generated
./scripts/score_seed.py -k 4 --k-leak 5   # takes a lock; do NOT run two at once
```

**Budget it in days.** One 122-opinion pull plus its searches nearly exhausts a day's cap,
and every exploratory search spends opinions you then cannot fetch. Expect roughly one new
clean case per five new candidates, at ~7% clean-yield end to end.

**Why more cases and not more replicates** (`scripts/variance_budget.py`): on the clean
stratum, case-sampling sd is 0.119 against judge-sampling sd 0.058 — case selection
dominates about 2:1, and the headline's 95% interval spans [0.39, 0.86]. Per-case values
are near-bimodal, so each added clean case moves the estimate materially. Adding cases is
the highest-value work available on this study.

## Requires

`COURTLISTENER_TOKEN`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` in the project `.env`.
