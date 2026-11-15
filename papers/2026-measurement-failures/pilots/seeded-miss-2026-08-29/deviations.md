# Deviations from the pre-registered design

Every departure from [`design-note.md`](./design-note.md), with when it was made and what
outcome data existed at the time. The parent study keeps the same record
([`../coverage-residual-validation-2026-08-29/deviations.md`](../coverage-residual-validation-2026-08-29/deviations.md));
its numbering continues at D1 here because this is a separate pre-registration.

---

## D1 — Stimulus-validity gate added: the seed must be raisable from the file

**When.** 2026-08-29, after inspecting the first 4 extractions, **before any generator ran.**
No recovery number, and no generator output of any kind, existed when this was decided.

**What prompted it.** Case `10945635` (*Camara v. Gill Dairy*, Ohio Supreme Court) has an
**intermediate appellate court** as the tribunal below, and its seed is a consideration that
only exists at appellate posture — whether sufficiency should have been measured against the
full trial record rather than the summary-judgment record. The extractor wrote the situation
as a first-instance case file ("Camara brings suit … in the Court of Common Pleas"). From
that file the seed is not merely hard to raise; there is no appeal in it to raise the seed
*about*. Recovery would have been 0 by construction.

Scored as-is, that case would have reported a coverage failure that was really an
**extraction failure** — precisely the class of error the parent study catalogued: a number
that means something other than its name.

**The change, in two parts.**

1. **Extraction now writes the situation at the posture the tribunal below occupied.** For a
   first-instance decision-maker that is a case file. For a reviewing tribunal it must carry
   what was decided beneath *it*, on what record, and what was argued to it. `screen_cases.py`
   states the test explicitly: could a competent reviewer, in the tribunal below's seat and
   holding only this file, raise the seed on their own?

2. **A validity gate drops stimuli that fail that test anyway.** Pass D now returns
   `raisable` alongside the leakage stratum, judged from **the situation and the seed alone**.
   Cases judged not raisable are excluded before scoring.

**Why this is not an outcome-conditioned filter.** The gate sees no generator output — none
exists when it runs. It is a property of the stimulus, in the same class as the screen in
§4.4, and it runs at corpus-construction time. The alternative — scoring void stimuli and
subtracting them afterwards — *would* be outcome-conditioned, and is what this avoids.

**Guards against the gate becoming an escape hatch.**

- `raisable=false` requires **impossibility, not difficulty.** The prompt says so in terms:
  a consideration that is subtle or easy to overlook is still raisable. A gate that fired on
  difficulty would delete exactly the cases the study exists to measure.
- **Ties resolve to raisable.** Dropping is the intervention, so an undecided stimulus stays
  in and counts against recovery.
- Every dropped case is **printed with its reason and committed** in `corpus/leakage.json`.
- The gate's judge (gpt-5.2) is a **different vendor** from the extractor whose work it is
  checking (claude-opus-4-8).

**Reporting requirement.** The count of gated cases is reported beside n in the result. If
the gate removes a large share of the corpus, that is itself a finding about this corpus —
appellate-review cases may simply not be usable for this design — and it is reported as one
rather than absorbed silently.

**Effect on §6's pre-registered analysis.** Unchanged: the "no case dropped after seeing its
score" rule still holds, and the denominator still counts runs that never raised the seed.
D1 adds a second construction-time drop criterion alongside screening; it adds no
post-scoring drop.

---

## D2 — Duplicate and companion clusters collapsed to one case each

**When.** 2026-08-29, during corpus construction, **before any generator ran.**

**What prompted it.** CourtListener returns the same decision under more than one cluster id.
Two shapes appeared in the 122 candidates:

- **Exact duplicates** — identical docket, filed twice. *People v Eads* (Mich. 168205),
  *In re Enbridge* (168335 et al.), *Smith v Beaumont Health*, *State v. Kayne* (A181113),
  *Williams v. Collins* (24-2592).
- **Companion appeals** — one opinion disposing of consolidated dockets, indexed once per
  docket. *Carter v. Cabell* (24-6706 and 24-6741), *Kelly v. Altria* (25-1350 and 25-2080).

Both were extracted as separate cases before this was caught; *Carter v. Cabell* produced two
near-identical seeds about the same supervisor's knowledge.

**Why it matters beyond double counting.** Companion appeals share facts, record and holding.
A generator's hit or miss on one carries no independent information about the other, so
scoring both inflates n while adding no evidence — and inflates it *non-randomly*, since
consolidated appeals cluster in particular courts.

**The change.** `screen_cases.py` collapses cached opinions to one per (case name, court),
keeping the longest cached text. 122 clusters → 115 distinct cases.

**Cost, stated.** Genuinely distinct disputes that share a case name and court would be merged
by this rule. None were observed in the seven groups; the rule is conservative in the safe
direction (it can only ever remove cases, never fabricate them).

---

## D3 — Extraction rebuilt: one sighted call replaced by three, with a blind writer

**When.** 2026-08-29, **before any recovery number was computed.** A 16-run pipeline test
existed (4 cases), so generator output existed — but the change was driven by the *leakage
audit*, which never sees generator output, and the test runs were discarded and regenerated
afterwards.

**What prompted it.** The pipeline test produced **zero cases in the `neutral` leakage
stratum** — the pre-registered headline stratum. Inspecting the audit's evidence showed why:
the situations were stating their own seeds, sometimes almost verbatim.

| case | seed | what the situation said |
|---|---|---|
| Hepler v. Collins | Board failed to adjudicate the direct service-connection claim | "The Board did not directly address the direct service-connection claim" |
| Carter v. Cabell | whether remedies were "available" under *Ross v. Blake* | named *Ross v. Blake* and the availability argument outright |
| In re Enbridge | agency declined to consider pollution from existing line sections | "declined to consider evidence of potential pollution … from existing sections of Line 5" |

**Diagnosis.** The v1 design asked **one sighted call** to identify the seed *and* write a
document concealing it. That is self-suppression, and it failed: the model wrote a faithful
summary of an opinion whose subject *is* the failure to consider. Its `excluded_spans` list
showed it removing some leaks while passing others through — it was trying, and the task
was the wrong shape.

**The change — three calls, so the writer cannot leak what it never saw.**

1. **BOUNDARY** — marks where the court's recitation starts and ends. Asked with no mention
   of the seed, so the cut cannot be placed to hide or expose anything.
2. **HOLDING** — seed, key, tribunal. Sighted, and its output never reaches the writer.
3. **COMPOSE** — **blind.** Receives only the text between the boundaries. It has never seen
   the analysis or the seed.

**A second bug found while fixing the first.** The initial cut was one-sided —
`text[:end]` — which silently included the **syllabus**, where many state supreme courts
summarise the holding before the opinion begins. The stimulus was being handed the answer in
its first paragraph. The cut is now two-sided: the recitation starts *after* caption,
counsel and syllabus, and the end boundary is required to fall after the start.

**Effect.** Neutral stratum went from 0/4 to 2/7; situations roughly doubled in length
(3–6k chars → 4.5–21k), because the blind writer works from the court's recitation rather
than compressing it. Compression was itself a leak: a short summary of a long opinion keeps
what the summariser found significant.

**What this does NOT fix, and it matters.** Residual leakage is now the *court's own* — what
an appellate judge chose to put in the fact recitation. That is a property of the corpus,
reported as one. And the audit remains conservative: it rates "the facts underlying the seed
are present and central" as `hinted`/`explicit` even though those facts **must** be present
or the seed would fail the D1 raisability gate. The neutral stratum is therefore a *strict*
subset — biased against finding recovery, which is the safe direction for a headline.

**Guard added.** The leakage judge must now supply a **verbatim** quote of ≥8 words for an
`explicit` verdict, verified by normalised substring search against the case file. An
unverifiable quote is the judge reconstructing what the file "in effect" says — inference,
not leakage — and is downgraded to `hinted` with `downgraded_unverified` recorded.

**Cost.** Extraction is three model calls per kept case instead of one, and every case
extracted under v1 was discarded and redone.

---

## D4 — Partial-credit matching added as a second reported rule

**When.** 2026-08-29, **after** the pre-registered result was computed and written up. This
is the one deviation that is genuinely post-hoc, and it is reported as an additional rule
beside the pre-registered one, never in place of it.

**What prompted it.** The pre-registered measure (exclusive match) reported 0.55 in the
neutral stratum while raw recovery was 0.95. The write-up asserted, from arithmetic, that
partial credit would move the figure toward raw. Asserting a number the data could produce
but had not is the habit this project exists to break, so it was computed.

**The rule.** An item counts for the seed if the blind judge rated it **signal** (sound +
raised + material + non-duplicate), whether or not the matcher also credited it to a key
point. The quality bar is unchanged — this removes the exclusivity requirement only.

**Result.** 0.55 → **0.95**, equal to raw recovery.

**Why this is not moving the goalposts.**

- The pre-registered figure **is still the headline** and is reported first everywhere.
- The rule was specified in advance by the *parent* study
  ([`../coverage-residual-validation-2026-08-29/seeded-holdout-result.md`](../coverage-residual-validation-2026-08-29/seeded-holdout-result.md) §3),
  as the named fix for the granularity bound. It was not invented to improve a number.
- It cannot be tuned: there is one threshold and it was not chosen, it was removed.
- It is bounded above by raw recovery, which is reported beside it. A partial-credit figure
  that *exceeded* raw would be a bug, not a result.

**Side effect, and it is a finding in its own right.** Re-scoring the same 20 generator runs
produced slightly different numbers (raw 0.90 → 0.95, off-key 0.50 → 0.55; run-level agreement
0.85). Both scorings are preserved — `attic/scored.exclusive-only.json` and
`runs/scored.json` — and `result.md` §5 reports the spread as the noise floor every other
figure in the study must be read against.

---

## D5 — Two scorers ran concurrently and raced on the leakage file

**When.** 2026-08-29, during the expansion from 25 to 34 cases. Caught by an internal
consistency check before any number was reported.

**What happened.** I started the scorer twice: once from a background waiter that fired when
generation completed, and again from a foreground command that reached the same condition.
Both processes wrote `runs/score4.log`, `runs/scored.json` and `corpus/leakage.json`.

The scored runs themselves are unaffected — the judging passes are per-run and idempotent in
their inputs. The damage was to the **leakage stratum stamped on each row**: each process
computed the leakage audit for the newly added cases independently, wrote its own
`leakage.json`, and stamped rows with whichever value it happened to hold. Last writer won the
file; 8 rows kept a label from the other draw.

**How it was caught.** The report said the neutral stratum held "24 runs over 6 cases" while
`leakage.json` listed **7** neutral cases. Six cases at four runs each is 24, so the table was
internally consistent and only disagreed with a file it did not print. The check that caught
it was comparing each row's stamped stratum against the leakage file of record — not the
number looking wrong.

**The fix.** Every row was re-stamped from the single `leakage.json` of record and the report
regenerated. No rescoring was needed: the stratum is a grouping label, not an input to any
judging pass. The pre-fix state is preserved at `attic/scored.pre-restamp.json`.

**Effect on the headline.** 0.58 → **0.50**. The mis-stamped rows had moved the reported
figure by 8 points.

**It also produced an accidental measurement, and a useful one.** Two cases were leakage-
audited twice, independently, on identical inputs. **Both flipped stratum** — one
explicit→hinted, one hinted→neutral. That is a direct reading of how unstable the audit is at
k=2, and it explains §2 of [`result.md`](./result.md): the hinted/explicit distinction
collapsed at 136 runs because those two levels are not reliably separable at this k. An
accident supplied the reliability check the design did not include.

**Process note.** The real fault is that the harness allows two scorers to write the same
files with no lock. Any future concurrent run should either take a lock or write to
process-specific outputs. Recorded because "the numbers moved and I do not know why" is the
failure this project exists to make impossible.
