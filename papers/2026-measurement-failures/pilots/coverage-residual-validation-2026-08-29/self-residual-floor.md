# The floor: what the same system misses against itself

**Status: exploratory. One fact pattern, one system, 5 replicates. A floor measurement, not a result about coverage.**
Rung G1 of the independence ladder ([`design-note.md`](./design-note.md) §4).
Raw: `runs/february-2018-family-law.g1.rALL.self-residual.json`.

---

## Setup

| | |
|---|---|
| Fact pattern | February 2018 MEE, Family Law |
| System under test | `gpt-5.2`, identical prompt, blind to the answer key |
| Varied between runs | **nothing but sampling** — no prompt change, no temperature change |
| Replicates | 5 |
| Clusterer | `claude-opus-4-8`, cross-vendor from the generator, k=3 consensus |

## Result

Headline numbers are from the **3-replicate consensus clustering**, which is the only
configuration whose mechanism does what its name says (see *The floor is clustering-dependent*
below).

```
items per run                                    55, 55, 60, 60, 50
pooled items                                     280   (214 distinct strings)

distinct issues across all 5 runs (the pool)      58
distinct issues per single run            46, 42, 42, 42, 40
mean single-run coverage of the pool            0.73

found by ALL five runs (the stable core)          30     52% of the pool
found by exactly ONE run                          11     19% of the pool

mean pairwise self-residual                     0.138
spread across the ten pairs              0.061 - 0.192
```

### The floor is clustering-dependent, and that belongs on the number

Three clusterings of the same five runs:

| | clustering | pool | core | singletons | single-run coverage | floor |
|---|---|---|---|---|---|---|
| A | 1 pass, raw labels | 61 | 26 | 12 | 0.70 | 0.165 |
| B | 1 pass, raw labels | 70 | 27 | 11 | 0.70 | 0.175 |
| **C** | **3-pass consensus, deduped** | **58** | **30** | **11** | **0.73** | **0.138** |

**Single-run coverage is the stable quantity** — 0.70 / 0.70 / 0.73 across all three. That
is the number worth carrying forward.

**The floor itself moved 0.138 - 0.175**, a 27% swing driven entirely by how finely the
clusterer sliced the pool: coarser clustering, smaller pool, smaller residual. So the floor
is reported as a range with its clustering configuration attached, never as a point
estimate. This is the semantic-matching weak joint ([`design-note.md`](./design-note.md) §0)
showing up exactly where it was predicted to, and it is the main threat to every number on
this page.

Runs A and B are shown for the spread, but neither is sound on its own terms: each was a
*single* clustering that the script reported as a consensus. `consensus_clusters()` with one
replicate has a majority threshold of 0.5, so it returns that clustering unchanged — the
exact single-pass judgment this design refuses to trust, wearing the label of a consensus.
The script now refuses to run below two usable replicates.

## What it says

**A single run delivers 73% of what the same system finds across five.** Not a different
model, not a different prompt — the same system, asked the same question, five times. Three
in ten of the issues it is capable of surfacing on this problem do not appear in any given
run.

**Only about half the pool is stable.** Thirty issues showed up in all five runs. The other
twenty-eight are, from the point of view of a single run, a coin flip. If you asked this
system once and acted on the answer, the majority of what it "knows" about the problem was
not reliably in front of you.

**The floor is 0.138** (range 0.138 - 0.175 across clusterings). Of everything two runs
surface between them, one misses about 14%.
That is the number every other rung gets read against: **a cross-vendor residual below
0.138 is not evidence of a vendor blind spot — it is indistinguishable from asking the same
model twice.** Any claim that model B saw something model A could not has to clear this bar
first, and the bar is high.

## Reported, not subtracted

Per Bart's decision of 2026-08-29, and it matters here more than expected.

R8 — the study asking whether the resolver's scoring yardstick is stable — treats replicate
variance as nuisance to remove before interpreting a difference. That is right when the
noise is in the *instrument*. Here the variance is in the *thing being measured*, and it is
not a nuisance: **a run that misses what its own rerun catches has failed at coverage.**
Weaker than a systematic blind spot, but real, and it is the direct evidence on the question
a trust rider actually needs to answer — *can I act on one run?*

On this problem, the answer is that one run gives you 73% of the system's own reach. That
is a finding about single-run trustworthiness, and it would have been thrown away as noise
under the subtract-the-floor reading.

## The follow-up, now run

Eleven issues appeared in **exactly one** of the five runs. Scoring them against the stable
core as a reference — blinded, both strata shuffled together — settles what the floor means:

```
core        30 items   signal rate 0.87      (the reference distribution)
singleton   11 items   signal rate 0.55
gap        +0.32       MIXED, on the pre-committed bands
```

**6 of the 11 single-run issues were sound, raised, and material.** So the variance is
**part real coverage, part churn**: rerunning the same model surfaces genuinely material
issues, but singletons are meaningfully weaker than reliably-repeated output, so the raw
coverage figure overstates what a rerun buys. Report both rates, never one corrected number.

Zero items in either stratum were **unsound** — the generator is not inventing law. Its fill
is real doctrine these facts do not raise, or that cannot move the analysis.

Full detail, including a control threshold this run caught as mis-specified:
[`singleton-strata.md`](./singleton-strata.md).

## What this cannot do

- **One fact pattern, one system.** Nothing here generalises to other problems, subjects, or
  models. It is a floor for this cell, established so the machinery exists.
- **The pool size depends on clustering granularity**, which is a model judgment, and the
  three clusterings above disagreed by 27% on the floor. Consensus across k=3 and a
  cross-vendor clusterer are the mitigations; neither eliminates it. This is the
  semantic-matching weak joint ([`design-note.md`](./design-note.md) §0) in its least
  avoidable form, and it is the main threat to every number here.
- **Clustering is intermittently unparseable.** Two of three replicates died on malformed
  or truncated JSON before parse-retry was added, and every replicate in the final run
  needed one retry. The step is reliable enough to use and not reliable enough to trust
  unattended.
- k = 3 clusterings, not the specified 5.
