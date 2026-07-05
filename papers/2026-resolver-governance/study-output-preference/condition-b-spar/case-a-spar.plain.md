# /spar report: TerraClarity handbook address-term decision (Case A, plain-pack re-run)

**Substrate**: Claude Opus 4.8 (Generator + Challenger sub-agents). Plain-pack re-run, 2026-06-04.
**Iterations**: 2 / 2
**Outcome**: Converged

## Personas

- **Generator**: Mara Ellison, organizational-behavior & people-strategy advisor.
  - Evidence base: behavioral-science + survey/preference evidence (Pfeffer perception research, SHRM peer-firm convention data, the internal staff-preference survey, the external-voice history).
- **Challenger**: David Soto, employment-law & implementation counsel.
  - Evidence base (distinct): legal-consistency doctrine (the *Toussaint* line / handbook-vs-document mismatch), operational/transition cost, and decision-process integrity (the compensation chair as a conflicted advocate).

## Iteration log

### Round 1
- **Generator proposal**: "Team members" as primary term + a single definitional clause tying it to "employee" (evidence 2); reject "colleagues" (evidence 3, 6, 4); Pfeffer read small/directional (evidence 1). Framed the 67% named survey as "strong despite conformity pressure."
- **Challenger PNP**: Two artifact-grounded blockers. (1) The evidence-2 remedy is under-specified — adopting "team members" creates exactly the handbook-vs-offer-letter mismatch evidence 2 warns about (offer letters/payroll say "employees", per Option 1's note), and one clause across a 28,000-word handbook (situation, para 3) is too thin; needs first-use definition + belt-and-suspenders "employees (team members)" in the at-will/termination sections. (2) The evidence-6 named survey is over-read — non-anonymity inflates the expected answer and the write-ins ("everyone says it now") are conformity tells, so 67% is plausibly a ceiling, not "strong despite conformity." Credited the Generator's "colleagues" rejection and Pfeffer reading.
- **Generator signal**: {agree: true}
- **Challenger signal**: {agree: false — remedy under-specified + survey over-read}

### Round 2
- **Generator revision**: Kept "team members." (1) Specified the evidence-2 remedy as two layers — first-use definition + belt-and-suspenders pairing in the at-will/termination sections — and owned the tonal-seam cost. (2) Corrected the evidence-6 framing to "67% is consistent with the existing external voice; plausibly a ceiling under non-anonymity; corroborates rather than carries."
- **Challenger re-test**: Both blockers RESOLVED with artifact grounding — the two-layer remedy now anchors the operative term where evidence 2 locates the *Toussaint*-line risk; the evidence-6 downgrade matches the non-anonymity and conformity tells the survey text records. No new blocking concern; manufacturing a third would be theatrical.
- **Generator signal**: {agree: true}
- **Challenger signal**: {agree: true}

→ **Converged** (both agree, round 2).

## Final evaluation

"Team members" as the single primary handbook term, with a two-layer legal anchor (first-use definition + "employees (team members)" pairing in at-will/termination sections); reject "colleagues." Full converged recommendation in the rater-presented form: [`case-a-recommendation.plain.md`](./case-a-recommendation.plain.md).

## Artifacts surfaced

- Evidence 1 (Pfeffer): perceived hierarchy moves 1–3 points; no change to actual authority/reporting.
- Evidence 2: legal exposure is handbook-vs-document *mismatch* (*Toussaint* line); remedy is a linking clause.
- Evidence 3 (SHRM 2024): "employees" 71% / "team members" 22% / "colleagues" 4% of 217 peer firms.
- Evidence 4: 7-year "team members" external voice; new hires meet it before "employees."
- Evidence 5: "colleagues" originates with the compensation-committee chair (conflicted advocate).
- Evidence 6: non-anonymous survey, 12% / 67% / 21%; "team members" write-ins are conformity tells.
- Option 1 note + situation para 3: offer letters/payroll/prior handbook say "employees"; ~28,000-word handbook.

## Recommendation for parent

Converged, artifact-grounded. The spar tightened a real weakness the round-1 proposal glossed (the legal remedy) and corrected an over-read of the survey — both are reflected in the final recommendation. Suitable as the Condition B (SPARRING) output for Case A.
