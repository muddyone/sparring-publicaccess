# /spar report: NCCC CS101 curriculum-architecture decision (Case B, plain-pack re-run)

**Substrate**: Claude Opus 4.8 (Generator + Challenger sub-agents). Plain-pack re-run, 2026-06-04.
**Iterations**: 2 / 2
**Outcome**: Converged

## Personas

- **Generator**: Dr. Priya Nair, learning-science & CS-education advisor.
  - Evidence base: pedagogy/cognitive-science literature (cognitive-load theory, adult-learning research, first-gen/ESL performance studies, transfer-outcome studies).
- **Challenger**: Tom Reyes, community-college operations & student-outcomes realist.
  - Evidence base (distinct): empirical completion data, the institution's own 2018 history, staffing/implementation constraints, and the stability/replication status of the cited findings.

## Iteration log

### Round 1
- **Generator proposal**: A hybrid — runnable Python from week 1, but each week's syntax introduced as the implementation of an explicitly-named concept (15–20 min plain-sketch frame first); concepts as the spine. Grounded in Evidence 2 (ordering doesn't move completion), 1 (within-unit load sequencing), 3 + 6 (adults need early competence), 4 (first-gen/ESL gap; flagged unstable per Lewis 2022), 5 (conditional transfer edge). Explicitly handed instructor-execution risk to the Challenger.
- **Challenger PNP**: Agreed the design and the completion-neutrality read are sound, but three artifact-grounded blockers. (1) The hybrid is the hardest of the three options to deliver across line-21 staffing (4 FT + 6–8 adjuncts, ~8 sections) — a per-week two-mode handoff is a teaching skill, performed mostly by under-resourced adjuncts. (2) The June 30 deadline (line 14/64) can't absorb the new week-by-week dual-frame materials. (3) Over-read of Evidence 6 — line 50's 64→73% Python jump was a *language* change (Python's write-correctness + media familiarity), not evidence that early-syntax *pedagogy* drives completion; Evidence 6 has no ordering contrast.
- **Generator signal**: {agree: true}
- **Challenger signal**: {agree: false — unpriced execution risk + Evidence-6 over-read}

### Round 2
- **Generator revision**: Conceded the execution critique as decisive and **stepped down** to Path B (language-first) + one bounded concept overlay — a recurring one-page "what idea is this" sidebar + 3–4 reusable "rewrite-in-plain-steps" lab prompts, authored once by the 4 full-time faculty as a fixed artifact set (not a live adjunct skill); Path B runs on the existing 2018-onward materials (line 50). Withdrew the Evidence-6 thread entirely. Owned the lost Evidence-5 transfer edge and the traded-away Evidence-1 load argument.
- **Challenger re-test**: All three blockers resolved against the artifacts — the overlay is a fixed FT-authored artifact atop the existing Path B course, so it fits line-21 staffing and the line-14/64 deadline; the Evidence-6 withdrawal matches line 50; the Evidence-5 trade-off is honestly owned. No new blocker; manufacturing one would be theatrical.
- **Generator signal**: {agree: true}
- **Challenger signal**: {agree: true}

→ **Converged** (both agree, round 2).

## Final evaluation

Path B (language-first) plus a bounded, full-time-faculty-authored concept overlay; reject the per-week dual-frame hybrid and pure Path A on deliverability. Full converged recommendation in the rater-presented form: [`case-b-recommendation.plain.md`](./case-b-recommendation.plain.md).

## Artifacts surfaced

- Evidence 1 (Sweller): load comes from two hard new things at once → within-unit sequencing remedy.
- Evidence 2 (Bennedsen & Caspersen): completion 65–78% across designs vs 58–85% across languages; ordering doesn't predict completion.
- Evidence 3 (Knowles): adult learners (57% here) need early concrete competence.
- Evidence 4 (Hatfield): first-gen/ESL ~12pp lower on write-from-scratch; failed to replicate in Lewis 2022.
- Evidence 5 (Smith & Garcia; Park): concepts-first transfer edge d ≈ 0.18–0.22, only within 18 months.
- Evidence 6 / line 50: 2018 Java→Python jump 64→73% was a language change (path held constant); no ordering data.
- Line 21: 4 full-time + 6–8 adjuncts, ~8 sections. Line 14/64: June 30 build deadline, Python fixed.

## Recommendation for parent

Converged, artifact-grounded. The spar materially changed the recommendation: the Challenger's staffing/deadline artifacts forced a step-down from an undeliverable hybrid to a deliverable Path-B-plus-overlay, and forced withdrawal of an over-read of Evidence 6. Suitable as the Condition B (SPARRING) output for Case B.
