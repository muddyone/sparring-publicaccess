# First scored run — both directions working

**Status: exploratory. One fact pattern, one generator, k=3. A pipeline proof, not a result.**
Design: [`scoring-design.md`](./scoring-design.md). Raw: `runs/smoke-feb2018-familylaw.gpt52.scored.json`.

---

## Setup

| | |
|---|---|
| Fact pattern | February 2018 MEE, Family Law |
| Generator | `gpt-5.2`, blind (no answer key in the prompt) |
| Matcher (Pass A — sees the key) | `gpt-5.2` |
| Blind judge (Pass B — sees only the facts) | `claude-opus-4-8` — cross-vendor from the generator |
| Replicates | k = 3 (design calls for 5; reduced for a pipeline proof) |

## Result

```
direction 1 -- recall against the examiners' key
  HIT on all 5 key points   (point IDs and weights withheld; see the archive README)
  weighted recall  1.00      unanimity 1.00

direction 2 -- yield over what it emitted        [run 1]   [run 2, committed]
  emitted                                            57          57
  signal                                             29          27
  yield                                            0.51        0.47
  noise      (unsound or not raised by the facts)    12          12    0.21
  duplicates                                         15          17    0.30
  off-key signal (sound+material, ungraded)           3           5    0.09

positive control     5/5 = 1.00   PASS (floor 0.90)      -- both runs
cross-pass conflict  10/49                9/49           credited-but-"not raised"
```

**Two runs are shown because the second one disagreed with the first.** Same inputs, same
models, k=3, nothing changed but the sampling: yield moved 0.51 -> 0.47, duplicates 15 -> 17,
off-key signal 3 -> 5. That is the **scorer's own run-to-run instability**, and it is
roughly the size of the differences the study will want to detect between generators.

Recorded rather than smoothed, because it decides something: at k=3 this instrument cannot
resolve a 4-point yield difference. Either k rises to the specified 5 (and the residual
variance gets reported as an error term) or small differences between generators are not
claimable. The design already calls for k=5; this run is the evidence for why that number
is not decorative.

Note the shape of the disagreement: **recall, noise, and the positive control were stable;
duplicates and off-key discovery were not.** The unstable pair are exactly the two judgments
that require comparing items *to each other* rather than to a fixed referent -- the
semantic-matching weak joint, showing up right where the design predicted it would.

## What it shows

**The pair discriminates where recall alone did not.** Recall says this run was perfect.
The second direction says **half of what it produced was fill and a fifth was noise** — 12
items either misstate the law or are doctrine the facts never put in play. A generator
scoring 1.00 / 0.51 and one scoring 1.00 / 0.90 are very different instruments, and the
original single-direction design could not tell them apart. That was the whole reason for
the change.

**Off-key discovery is small but non-zero.** Three to five items (it moved between runs)
were sound, raised, and material yet matched no key point — real issues the examiners chose not to grade. Under the original
design these were recorded and scored neither way; they are now one of the two things the
study is for. Three is too few to mean anything from one fact pattern; the point is the
measurement now exists.

**The blind judge cleared its positive control.** For every key point, at least one covering
item was independently rated sound, raised, and material by a judge that never saw the key.
That is the check that makes the second direction usable at all, and it passed on
known-material items — the subset where truth is available.

**The matcher is generous, by a measured amount.** Nine to ten of the 49 items Pass A credited were
rated *not raised by these facts* by Pass B. The two passes see different things, so this
comparison is free, and it means recall is probably inflated even at 1.00. Reported rather
than corrected: generous-by-a-known-amount is usable, generous-by-an-unknown-amount is not.

## Two bugs the run caught, both recorded as deviations

- **The control was mis-specified** and failed at 0.50 for the wrong reason — it required
  *every* key-covering item to be signal, so it was measuring deduplication rather than
  judgment. Respecified to "at least one per key point"; now 1.00.
  (deviation D6, *the positive control was mis-specified*)
- **Key ids did not round-trip.** The matcher returns `1(a)` where the key says `(1)(a)`,
  so the first scored run reported **weighted recall 0.00** — a plausible-looking number
  produced by a string mismatch rather than a measurement. Fixed by comparing on
  alphanumerics only. (deviation D7, *key-id normalisation*)

The second one is worth keeping in view: this study exists because instruments return
confident numbers that mean nothing, and its own scorer did exactly that on the first
attempt. The integrity checks are the only reason it was visible.

## Not yet done

- k = 3 here; the design calls for **k = 5**, and the two-run disagreement above shows why
  that matters — at k=3 the scorer cannot resolve differences the size of the ones being
  looked for.
- Run on **one** fact pattern of 60. No obscurity stratification yet — that needs subject
  normalisation and the corpus-frequency banding.
- **No perturbation contrast**, so nothing here separates competence from contamination.
- The **stop rule** (design note §9) is still written in terms of recall alone and needs
  restating against the pair.
- Only the cross-vendor generator (G3) has run. The same-system replicate (G1), the
  structured non-model enumerator (G4), and grounded retrieval (G5) are unbuilt.
