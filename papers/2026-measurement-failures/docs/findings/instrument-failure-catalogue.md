# Catalogue: instruments that reported something other than their name

**Status: standing catalogue, and the SPINE of the Measurement paper (Paper 2).** Append, do
not prune. **n = 24** as of 2026-09-16.

> ⚠ **The paper now carries all 24.** The Measurement paper draft reported **n = 18** while entries
> 19–24 landed, and reconciled the count once rather than on every append. On 2026-09-16 that hold
> was lifted: the draft now carries every entry here, 1–24, in its Appendix A and its §4.2 shapes
> table, and reports the catalogue as it stood on 2026-09-16. Entries appended after that date
> extend this artifact, not the paper. *(Decided 2026-08-30, §7 Q3 of `../../pilots/proposer-2026-07-06/coverage-instrument-status.md`:
this is not a section inside another paper — it is the argument of its own paper, with the
coverage-residual and seeded-miss studies as its evidence, presented as cases making its claim.
**Structural test:** a reader who skips both studies must still get the paper's claim.)*

Started 2026-08-29 by consolidating the
eight cases recorded in the coverage study's
[`implications-for-the-proposer-paper.md`](../../pilots/coverage-residual-validation-2026-08-29/implications-for-the-proposer-paper.md) §4
with those found since.

---

## Why this exists

SPARRING's subject is whether a system can be trusted to report on its own reliability. This
is a running record of cases where **an instrument built by careful people, in a project
explicitly about this failure mode, produced a confident number that meant something other
than its name** — together with what caught it.

Two properties make the collection worth more than its entries:

1. **Not one of these was caught by the number looking implausible.** Every single one was
   caught by an internal check, a cross-comparison, or an inspection of what the number was
   actually counting. Plausibility is not a filter.
2. **It is the evidence most projects throw away.** Failed instruments are normally deleted
   in the commit that fixes them. Here they are the on-thesis data.

**Rules.** Append every new case, including — especially — ones found in work that
succeeded. Record what the number *said*, what was *true*, and **how it was caught**. Never
remove an entry because it was later fixed; the fix is part of the record.

---

## The shapes

Entries cluster into recurring failure modes. The shape is the transferable part.

| shape | what happens |
|---|---|
| **A. The check measures something else** | A validation appears to test the judge and actually tests deduplication, or recall, or itself. |
| **B. Direction averaged away** | Two different quantities are averaged into one number that describes neither. |
| **C. Identity mismatch** | Two names or filings for the same thing fail to match, so the measure counts a difference that is orthographic, lexical, or the same doctrine filed under two headings. |
| **D. The judge over-credits** | A matching or membership pass says yes to something adjacent, and the yes is invisible because nothing tests near-misses. |
| **E. Real at small n only** | A large, mechanistically plausible effect that dissolves as data is added. |
| **F. Stale or raced state** | The number is computed from inputs that have since changed, silently. |
| **G. Instability read as signal** | A gradient or ordering that is a property of the estimator's variance, not the world. |

*Revised 2026-09-16: shape B's earlier gloss did not fit entry 4, whose two averaged directions are both positive and measure different things (what the second vendor added, and what it lacked; the saved, corrected run reads them as 0.038 and 0.553, `runs/cross-residual.json`. The first run's clustering was not saved, and its write-ups mix the two runs' figures — [`cross-vendor-null.md`](../../pilots/coverage-residual-validation-2026-08-29/cross-vendor-null.md) §5), so B now names what happened. Entry 7, one doctrine filed under two headings, moved from B to C, whose gloss widened to cover it.*

---

## Entries

### From the coverage study (1–9)

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 1 | C | weighted recall **0.00** | recall was 1.00 | key ids did not round-trip (`1(a)` vs `(1)(a)`) |
| 2 | A | a **consensus** clustering | one clustering; threshold 0.5 returns it unchanged | replicate-count check |
| 3 | A | control **FAIL at 0.50** | judge was correct; the control measured deduplication | inspecting the four "failures" |
| 4 | B | cross-vendor lift **+0.130, SUBSTANTIAL** | two directions averaged: −0.114 once separated — and that was itself partly a volume artifact; matched for output volume it is **+0.008**, a null (`cross-vendor-null.md` §4, corrected here 2026-09-16) | the pool shape: B-only clusters a small fraction of A-only. The saved clustering reads 5 against 37; the study's narrative gives 4 against 40 for the first run, whose clustering was not saved |
| 5 | C | structured novelty **+0.305** | vocabulary mismatch, not novelty | the "novel" set contained the 30%- and 35%-weighted key points |
| 6 | D | a 10-item list covering **261 of 281** | membership judge over-merging | plausibility guard on covers/own ratio |
| 7 | C | projection lift **+0.207** | a filing artifact; both sides raised the doctrine | inspecting which nodes were "B-only" |
| 8 | A | positive control **0.43** | the control was confounded with recall | control tracked recall to ±0.08 |
| 9 | A | a sanity test **passing** | the instrument it guarded was broken | it could only detect failure in one direction — it tested for false novelty and was blind to everything reading as identical |

Entry 9 is the sharpest of the nine and is not a measurement but a *check*: **a guard that
passes because it cannot see the failure it was built for.** It is the direct ancestor of the
two-sided decoy control in the seeded-miss study.

### From the seeded-miss study and the recount (10–15), 2026-08-29

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 10 | E + G | first-instance tribunals recover far better than reviewing ones, **0.90 vs 0.50**, with a ready mechanism | the **sign does not hold**. Four scorings of the same design read 0.90/0.50, then 0.66/0.61, then **0.62/0.73** — reversed — then 0.61/0.66. The cut is a property of the estimator, not of tribunals | more data, then more scorings. It was labelled exploratory *when it looked strongest*, which is the only reason it became a footnote and not a finding |
| 11 | E | (a prediction) the coverage study's off-key rates are **understated** by the exclusive-match rule | correction is **+0.00 to +0.08**, median +0.04 | running it. The defect is severe for a *targeted* measure and negligible for a *rate* — the rule's damage scales with how concentrated the measure is |
| 12 | D | the recount's "material beyond the key" pass claimed **18.4 items per run** | **88% struck** by a second, different-vendor pass blind to which item each phrase came from | the falsification pass, built in from the start *because of this catalogue*. Stopping at the first pass would have moved a rung 0.03 → ~0.36 and looked like a triumphant confirmation of entry 11 |
| 13 | F | headline off-key **0.58** | **0.50** | two scorers run concurrently raced on the leakage file; 8 rows kept a label from the losing draw. Caught by cross-checking each row's stamp against the file of record — the report was internally consistent and only disagreed with a file it did not print |
| 14 | G | a monotonic leakage gradient, **0.38 → 0.65 → 0.94**, cited as the audit validating itself | **0.62 / 0.64 / 0.68** — flat | raising the leakage audit from k=2 to k=5. 10 of 34 cases changed stratum. Confirmed not to be a threshold artifact: even *unanimously* neutral cases sit at 0.62 |
| 15 | D | raw recovery **1.00** on *Eqbal v. Blanche* | the seed was **not raisable from that case file at all** — it turns on calendar dates the file never mentions | the stimulus-validity gate, once the audit was reliable enough to fire it. The seed judge had been crediting topically adjacent items |

**Entry 10 was restated on 2026-09-16, and it got stronger.** It was filed as shape E alone —
*real at small n only* — on the reading that the effect shrank to nothing as data arrived. A
third and fourth scoring make that reading too kind. The cut has now been measured four times
on the same design and the **sign reversed in the middle**: 0.90/0.50, 0.66/0.61, 0.62/0.73,
0.61/0.66. An effect that dissolves is one thing; an ordering that changes direction between
scorings of the same data is shape **G** — *instability read as signal* — and that is the more
useful lesson, because "gone" invites the reader to think something converged. Nothing
converged. The original headline was a draw from the estimator's variance with a mechanism
attached afterwards, and the mechanism is what made it persuasive.

### From the tooling, not the measurements (16–17), 2026-08-29

The catalogue's subject is instruments that misreport. A *harness* that misreports its own
completion is the same failure one layer down, and it corrupts measurements just as well.

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 16 | A | a corpus pull **completing** — final cache count printed, `next: ./screen_cases.py`, exit 0 | the daily API quota was exhausted on the first request; every remaining candidate failed in turn | reading the output. A broad `except Exception`, there so one malformed opinion could not kill a long pull, also swallowed quota exhaustion — and the success message printed regardless of whether anything was fetched |
| 17 | F | an edit **applied** — the file parsed, the script ran, no error anywhere | a string-replace had silently matched nothing; the intended change was absent | the behaviour it was supposed to produce did not appear later. `assert old in s` was added afterwards to every such edit, which is the whole fix |
| 18 | G | doubling the judging replicates (k=2 → k=4) would **stabilise** the measure — the premise the whole rescore was launched on | aggregate moved 0.01 while **19% of individual verdicts flipped**; agreement on off-key 0.81. More replicates do not help, because a borderline absorption call has an underlying probability near 0.5 and majority-voting more samples converges on a coin flip | scoring the entire corpus twice and comparing run by run (`scripts/compare_k.py`), rather than comparing the two headline numbers — which agreed, and would have looked like confirmation |

Entry 18 is the one that cost the most compute: a two-hour run whose *headline* barely moved
and whose *verdicts* barely held. Had it been read at the aggregate level — 0.66 → 0.67 — it
would have been filed as "k=2 was fine all along." The run-level comparison says something
close to the opposite, and the two readings are only distinguishable because both scorings
were kept.

Entry 16 is shape A one level down: **the check (exit code, success message) measured
"the loop finished" rather than "the work happened."** Entry 17 is the same hazard in an
editing tool — a verification (`does it parse?`) that cannot detect the failure mode it is
standing in for (`did the edit land?`).

Both were cheap to fix and neither touched a reported number. They are here because the
shapes are identical to entries that did.

### From the corpus-expansion run (19–20), 2026-08-30

Both found during the run that took the clean stratum from 9 to 15 cases — work that
otherwise **succeeded**, which is exactly the kind the rules say to record.

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 19 | F | the variance budget on the freshly-scored corpus: **9 cases, 36 runs, off-key 0.639, 95% interval [0.39, 0.86]** — a confident, correctly-formatted, internally consistent result | the corpus had just grown to **15 cases / 60 runs at 0.500**, interval **[0.33, 0.67]**. `variance_budget.py`'s `--scored` default is hard-wired to `../attic/scored.k2.json`, an **archived** snapshot; run bare after a new scoring it silently analyses superseded data and never names the file it read | knowing the corpus was 15 cases and seeing the header say 9. **Not** the number looking implausible — 0.639 over 9 cases is perfectly reasonable — but a **metadata mismatch against known ground truth**. Taken at face value it would have reported the interval **unchanged at 0.47 wide** and no progress toward the §4a bar, when it had in fact narrowed to 0.33 wide *(corrected 2026-09-16: this cell read "WIDENING (0.47 → 0.47)", which is flat)* |
| 20 | A | a screening run that had **vanished** — no process, a **0-byte log**, no error anywhere: observationally identical to "never started" | it had screened **7 opinions and extracted 2** before dying. Python buffers stdout when it is not a tty, so the buffer died with the process and every available signal said nothing had happened | checking the corpus state rather than the process state — `screen.json` had moved 102 → 109 and `cases.json` 34 → 36. The fix is `python3 -u` plus a harness-tracked launch, so output is captured and an exit is reported |

**Entry 19 is the sharpest entry in this catalogue, and it is about the catalogue's own
defences.** The five catching mechanisms in the write-up are presented as what works — but they
are themselves *tooling*, and tooling holds state. Here the instrument used to *check* the
instrument reported on a corpus that no longer existed, in the correct format, without
complaint. A checking layer is not automatically outside the failure mode it checks for.

The transferable fix is narrow and cheap: **an analysis tool must print the path of every input
it read.** Had the header said `attic/scored.k2.json` the error would have been visible in the
first second. It said nothing, and the only thing standing between a stale default and a
published interval was someone happening to remember the case count.

**Entry 20 is entry 16's exact shape in a different tool**: the observable — exit status,
process table, log file — measured *"is a process running"* rather than *"did work happen."*
Where 16's success message printed over a failed pull, 20's silence printed over a partial
success. Both directions of that error are available, and neither is visible from the signal
the operator actually watches.

### From the programme's own governance (21), 2026-09-16

Every entry above was found in an experiment. This one was found in a **gate** — the
pre-registered rule that decides which measure a future study is allowed to promote to primary.
It had not yet been run, so nothing was misreported to anyone. It is here because the shape is
identical to entries that did misreport, and because a catalogue that only records failures in
the measurements, and never in the machinery that governs them, is itself a one-sided check.

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 21 | A | a **reopening condition** with two bars that, if both cleared, would license promoting the coverage measure to a study's primary DV — "precision" and "reproducibility," each with a number attached | **neither bar measured what its name said.** Bar 1's precision figure was the *seeded-miss recovery* interval while the hypothesis it gates is about *off-key material* — it certified an instrument that is not the one carrying the claim. Bar 2 was stated on a **pooled** figure, and entry 18 had already established that this project's pooled figure can move **0.01 while 19% of individual verdicts flip**. A gate written that way passes in precisely the situation it exists to catch | reading the gate against the catalogue rather than against itself. Entry 18 is the counter-example, and it was already in this file when the gate was written |

**This is entry 9's shape one level up.** Entry 9 was a sanity test that passed because it could
only detect failure in one direction. Entry 21 is a **promotion gate** that would pass because
it reads an aggregate the underlying instability does not disturb. In both cases the check was
built by people who had just been burned by the exact failure it was blind to — entry 21 was
written *after* entry 18 was catalogued, by someone who had read it.

The transferable fix is the same one entry 18 implies and nobody applied to the gate: **state a
reproducibility bar at the level the decision is made at.** The decision here is per-run — does
this arm beat that one on this problem — so the bar belongs on run-level verdict agreement, not
on the pooled rate. The amended condition is in
[`../../pilots/proposer-2026-07-06/pilot-design.md`](../../pilots/proposer-2026-07-06/pilot-design.md) §4a,
with the superseded text kept beside it.

**Nothing was chosen against a result.** The amendment was made before the check ran and before
any factorial data existed. That timing is what separates it from the thing this catalogue
exists to document, and it is recorded here rather than asserted later.

### From the paper's own citation gate (22), 2026-09-16

Found while discharging the Measurement paper's citation gate — in the **verification tool**,
not in a measurement. It belongs here for the same reason entries 16–17 do: a checking layer
that misreports is the catalogued failure one level down, and it corrupts what it checks.

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 22 | A | two citations as carrying **no identifier at all** — `not-checkable`, with the report's recommended action being *"adding identifiers would take existence to 14–15 of 15"* | **both carried a correct arXiv id**, and had for six days. `/cite-check`'s BibTeX join reads an entry's `doi` field but not `eprint` / `archivePrefix`, so the identifiers were invisible to the tool — which then reported their absence, and a report turned that into an action item for work already done | reading `refs.bib` directly instead of the tool's summary of it. The ids are plainly there. Nothing in the output distinguished *"the bib lacks an id"* from *"the join did not read the id"* |

**The shape is the check asking a narrower question than its name.** "Is there an identifier"
was really "is there a `doi` key," and every consumer downstream — the retriever, the report,
the reader — saw only the answer. Hand-supplying the two ids and re-running resolved both
**with abstracts**, which also moved them from unverifiable to application-grounded.

**Why it took two passes to catch.** The 2026-09-05 report was right that those two citations
were not resolving, right that it could not resolve them, and explicit that it was *deliberately
not* filling the ids from model memory — good discipline, correctly applied, on a diagnosis that
was wrong about the cause. **A conclusion can be careful, honest, hedged in the right places and
still wrong**, when the thing it is careful about is downstream of the error.

The transferable fix is the same as entry 19's: **an analysis tool must distinguish "absent"
from "not read."** Filed at
[`../chatlogs/202609161104.inflight.cite-check-bib-join-ignores-eprint.md`](../chatlogs/202609161104.inflight.cite-check-bib-join-ignores-eprint.md).

**One more thing this gate produced, which is not an entry but belongs next to them.** The same
pass found that the paper's *own* citation banner reported a number scoped to existence in a
place a reader would take as covering application too — shape A again, in this paper's account
of its own verification. It is not catalogued separately because it is recorded in the paper at
§2.7, where a reader meets it in context rather than as a numbered case.

---

### From the paper's own panel review of its variance figures (23–24), 2026-09-16

Found while the Measurement paper's round-2 and round-3 panels re-checked §9.2 against committed
data. Both sit in the seeded-miss study's variance budget: the step that decided the study should add
cases rather than judging replicates.

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 23 | A | a **judge term** at k=2 — case sd 0.119 against judge sd **0.058** — read as "case selection dominates about 2:1" (the study's README), and used to redirect effort to adding cases | not two independent scorings of the same runs. Of the 28 clean-stratum runs the two files shared, **12 were the same scoring** (identical but for the restamped stratum label), so they could not disagree — and all 3 flips fell among the other 16. Across all 100 shared rows, 80 were scored once (44 byte-identical; 36 differ only in a stratum label rewritten by a later audit). The k=4 judge term paired two different configurations. **No judge term for a single configuration was ever measured** | diffing the two archived scorings row by row (`attic/scored.k2.json` against `attic/scored.exclusive-only.json`), rather than reading the flip rate the tool printed |
| 24 | A | `variance_budget.py`'s judge term, "implied sd of the stratum mean" — **0.062** at k=4 — and the tool's verdict **COMPARABLE** (case 0.118 < 2 × 0.062) | the conversion is √(p(1−p)/n), but the standard deviation of one scoring's mean implied by a disagreement rate p is √(p/2n). The right figure is **0.048**, and 0.118 against 0.048 **clears** the tool's own 2× rule: the verdict reverses. Too large by about 30% | deriving the conversion by hand and checking it against a case with a known answer: 36 runs, 12 of them coin flips and 24 settled, give a flip rate of 0.167, a true sd of one scoring's mean of 0.048 (√3/36; 0.048 in 40,000 simulated pairs), √(p/2n) 0.048, and the tool's formula 0.062 — Vera Tukey, round 3, correcting her own round-1 V21, which had the direction wrong |

**What they share.** Both labels were true to the code and false to the question. "Judge sd" was a
number computed from judge disagreement — just not a disagreement that could measure the judge (23),
nor converted to the quantity the label named (24). Neither changes the paper's conclusion that which
lever was bigger has not been measured; both are why that is now its conclusion rather than the
opposite one. The tool's owner fixes the formula; this entry records that it was wrong.

---

## Corrections, 2026-09-16 (Measurement paper round-2 and round-3 assembly)

Entries above are kept as recorded. These notes say where the record, re-checked against source, reads
differently; the Measurement paper's Appendix A carries the corrected readings.

- **Entry 4.** +0.008 is a volume-matched *exploratory re-run on the same fact pattern*, a null. It is
  not the established true effect (`cross-vendor-null.md` §4).
- **Entry 6** *(restated in round-3 assembly)*. The plausibility guard is the *response* to this error,
  not the check that established it. Its code comment already names the first build's reading, a 10-item
  walk covering 275 of 281 candidates, as "membership over-merging" (coverage `scripts/residual.py`
  l.158–162), and commit `89364e90` records a tightened prompt tried before the guard was added. Nothing
  on file says what established the error, so the catch cell names a later safeguard, not the catch.
  This bounds "Why this exists" item 1: of the 23 entries whose record says what established the error,
  none was established by the number looking implausible; entry 6's record does not say. *(Count
  updated 2026-09-16 when the paper took in entries 19–24: this note first read 17, of entries 1–18.
  Each of 19–24 records the check that established its error.)*
- **Entry 14** *(extended in round-3 assembly)*. The "it was" cell should read **0.64 / 0.64 /
  0.68** (`f34fe596:result.md` l.138; recomputed), on the k=2 scoring with the audit at k=5. 0.62 is the
  figure for cases rated neutral *unanimously* (15 of 24), which is the threshold-artifact check. "Flat"
  holds for that scoring only. The original 0.38 / 0.65 / 0.94 gradient, a 0.56-point spread, shrank to
  0.04–0.21 in later readings: k=2 scoring 0.64 / 0.64 / 0.68; k=4 scoring 0.58 / 0.61 / 0.75
  (`f34fe596:result.md` l.139); current corpus 0.50 / 0.65 / 0.71 (Measurement paper §7.3). No reading
  since has separated it from zero. The self-validation stays withdrawn.
- **Entry 18.** The k=2 and k=4 scorings also differed in tie threshold (a tie counts as yes, so k=2 is "at
  least 1 of 2", k=4 "at least 2 of 4") and in decoy draws (matched in 2 of 132 runs). So 19% is
  disagreement between two scoring configurations. How much doubling k alone would remove was not
  measured, and "more replicates do not help" and the coin-flip mechanism are not established by it.
  What holds: the pooled figures agreed within 0.01 while a fifth of verdicts disagreed. *Added in
  round-3 assembly:* the "headline" in the prose under the table is that pooled figure (0.66 → 0.67).
  The clean-stratum figure, the one the paper headlines, moved from 0.64 to 0.58 (`compare_k.py`, `0d1445f9` against `f34fe596`).
- **Entry 12 and the method note** *(restated in round-3 assembly; the round-2 note said two of the three
  safeguards trace to entry 9, which is stronger than the record)*. Written at the time, one safeguard is
  credited to a specific entry: the two-sided decoy control, to entry 9 (seeded-miss `design-note.md`
  l.92–93, part of the pre-registered design). The recount's falsification pass was built "on the
  strength of" the list of failures then written down, which held entry 9's failure among others
  (coverage `offkey-recount.md` l.102–104, commit `6ec4acec`); entry 12's own catch cell, "because of
  this catalogue", says the same. The method note's "existed only because entry 9 had been written down"
  came later (`d6888c57`) and is stronger than that record. No record traces the verbatim-quote
  requirement to an entry; the seeded-miss study added it as the guard in its deviation D3.
- **"Open", shared blind spots** *(added in round-3 assembly)*. The appellate courts are not the only
  human-authored element. The coverage study's examiners' answer key is one too, and it served as a
  positive control on the blind judge (coverage `scoring-design.md` §5, floor ≥ 90% of key points); the
  seeded-miss decoys are seeds from other cases. Each checks a judge only on what it names, so the open
  problem stands.
- **Entry 19** *(added when the paper took in entries 19–24)*. "The corpus had just grown to 15 cases"
  means the clean stratum: the corpus grew to 49 extracted cases, 47 scored. The figures re-derive:
  the pre-fix `variance_budget.py` (`60896070^`) run bare on `attic/scored.k2.json` gives 9 cases,
  36 runs, 0.639, [0.39, 0.86]; on the new scoring, 15 cases, 60 runs, 0.500, [0.33, 0.67].
- **Entry 20** *(added when the paper took in entries 19–24)*. The in-between counts were never
  committed. `screen.json` and `cases.json` are committed at 102 and 34 before the run (`e1a44c03`)
  and at 163 and 49 after the relaunch (`831b1dd5`). "Screened 7 opinions and extracted 2" rests on
  that commit's message. 109 and 36 appear only in this entry, written the same night (`aacd4c24`),
  and agree with those counts added to the committed starting state.
- **Entry 21** *(added when the paper took in entries 19–24)*. Bar 1's "≈ 0.24" is the half-width
  of the seeded-miss headline interval, [0.33, 0.81], and that headline is itself computed with the
  exclusive-match rule (`offkey_recovery`). What separates it from the gated hypothesis is the
  question each asks: whether one planted missed point was recovered, against how much off-key
  material a generator emits. `coverage-instrument-status.md` §1 lists them as two instruments
  (`f34f72f5`, before the gate was written). The paper states the distinction so that a reader who
  knows §7 calls the headline off-key does not read the cell as a contradiction. That both defects
  were found by reading the gate against the catalogue rests on the amending commit (`7d54271d`),
  and only bar 2 has a named counter-example, entry 18.

## What entries 14 and 15 cost, stated plainly

**Entry 14 removed an argument, not just a number.** The monotonic gradient was the evidence
cited for the leakage audit measuring something real. With a more reliable audit it is flat *(corrected 2026-09-16: not flat — the spread shrank from 0.56 to 0.04–0.21 and no later reading separates the levels; see Corrections)*,
so that self-validation is withdrawn. The pre-registered decision to headline the clean
stratum now buys little (0.64 neutral vs 0.66 pooled) — which is a *better* result for the
study's headline and a *worse* one for its methodology.

**Entry 15 exposed a hole in the study's own best control.** The two-sided decoy control
(clean at 0.02 over ~400 trials) draws decoys from *unrelated* cases, so it tests whether the
judge endorses far-off considerations. It cannot see a **near-miss** — a seed in the same
topical territory as the emitted items. *Eqbal* is one observed instance of exactly that, and
it was invisible to the control that exists to catch generosity.

The general lesson, which is entry 9 wearing new clothes: **a control tests the failure it was
shaped to test.** A clean far-off control says nothing about near-misses, and reporting it as
"the judge is not generous" overstates what it establishes.

---

## Method note: this catalogue changes how the work is done

The two-sided decoy control, the verbatim-quote requirement in the leakage audit, and the
falsification pass in the recount were all built *because of entries already in this list*.
Entry 12 is the clearest case — the guard that caught it existed only because entry 9 had been
written down.

That is the argument for keeping the catalogue rather than the fixes alone: **the entries are
reusable, the fixes are not.**

## Open, and not fixable by more care

- **Shared blind spots.** Where the generator and every judge are blind together, all of these
  instruments read clean, and nothing in this catalogue detects it.
- **No human evaluation** (standing project constraint), so every check here is a model
  checking a model. The appellate courts in the seeded-miss corpus are the one genuinely
  human, genuinely independent element, and they validate the *seed*, never the judges.
