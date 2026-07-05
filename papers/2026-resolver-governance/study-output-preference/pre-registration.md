# V2 SPARRING LLM-Judge Pilot — Pre-Registration

**Status**: PRE-REGISTRATION LOCKED at commit `a20e7272` (tag `v2-prereg-2026-05-03`; originating Lifspel-private commit `a26fc103`).
**Pilot identifier**: `sparring-llm-judge-pilot-2026-05-03-v2`.
**Parent design**: [`v2-design.md`](./v2-design.md) (locked 2026-05-03).
**V1 reference**: [`00-pre-registration.md`](./00-pre-registration.md), [`preprint-draft.md`](./preprint-draft.md).
**Pre-reg commit hash**: `a20e7272` (committed 2026-05-03; tag `v2-prereg-2026-05-03`).

This document is the binding pre-registration for V2. It specifies the methodology, the analysis plan, and the decision gate **before any V2 compute is spent**. Once committed, it is immutable until V2 results are produced; deviations from this plan after compute begins must be reported as protocol amendments per [Nosek et al. 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114) preregistration discipline.

---

## 1. Research question

**Does the SPARRING two-role pressure-test framework produce decision-quality outputs that are measurably different from a single-agent baseline on domain-independent decision tasks, and do cross-vendor LLM-judge consensus ratings track human-partner ratings closely enough to serve as a calibration anchor under a revised rubric and gate structure?**

V1 found (preprint §4-§5) that on two SFxLS-internal cases:
- All raters (1 partner + 3 LLM judges) preferred SPARRING over single-agent baseline on every criterion (directional unanimity).
- Cross-vendor judge consensus ρ vs partner ratings was 0.351 — below V1's pre-registered PASS threshold of 0.4.
- The rubric and partner-anchor calibration premise itself surfaced structural concerns (preprint §5.2-§5.4) that V1 framed as forward-design questions for V2.

V2 extends V1 in five ways: domain-independent cases, expanded rater pool, expanded rubric (factual-accuracy + engagement dimensions), expanded scale (1-5 → 1-7), paired-comparison parallel instrument, and required rater-condition declarations. V2 keeps the same substrate (Claude on both conditions); cross-substrate is explicitly deferred to Phase 2.

---

## 2. Conditions

**Condition A (single-agent baseline)**: One Claude Opus 4.7 agent receives the decision pack and produces a recommendation, free-form, no specific framework discipline applied. Token budget: ~8000 output tokens. Single iteration. Same prompt template as V1 Condition A.

**Condition B (SPARRING)**: A `/spar` ceremony with the V1-default settings (2 iterations, two divergent specialist personas with explicit evidence-base specification, both-must-agree convergence rule, verifiable-artifact requirement on the Challenger). Both Generator and Challenger sub-agents run on Claude Opus 4.7. Same `/spar` skill specification as V1 Condition B.

**Substrate**: Claude Opus 4.7 underneath both conditions (matches V1; V2 §5 cross-substrate deferred to Phase 2 per [`v2-design.md`](./v2-design.md)).

---

## 3. Cases

Two newly-authored decision packs, both from domains outside SPARRING, SFxLS, and Lifspel. Drafted alongside this pre-registration; locked at the same commit:

- **Case A — Organizational vocabulary in an employee handbook**
  - Domain: organizational behavior / HR policy.
  - Decision-shape: choice among three lexical conventions for canonical address terms in a values document.
  - File: [`v2-decision-packs/case-a-organizational-vocabulary.md`](./v2-decision-packs/case-a-organizational-vocabulary.md).
  - Pack-fidelity status: independently fact-checked at lock per V2 design rule (`v2-design.md` "Process changes" §1).

- **Case B — Introductory programming curriculum architecture**
  - Domain: computer-science education / curriculum design.
  - Decision-shape: choice between concepts-first and language-first architectural paths for a community-college Intro to Programming course.
  - File: [`v2-decision-packs/case-b-introductory-programming-curriculum.md`](./v2-decision-packs/case-b-introductory-programming-curriculum.md).
  - Pack-fidelity status: independently fact-checked at lock.

Both cases are partner-rateable without specialized domain expertise. Both have public evidence bases (organizational-behavior research; CS-education research); raters may optionally spot-check externally. Per the 2026-06-12 amendment, C5a (Factual accuracy) is scored against the fact-checked pack, not against external ground truth — external verification is an optional, declared covariate, not a scored expectation.

The two-case structure mirrors V1's two-case structure for analytical comparability where applicable. Sample size remains "calibration-check" not "effect-size-estimation."

---

## 4. Rubric (six criteria, 1-7 anchored scale)

Six criteria, each scored 1-7 on an anchored scale with behavioral anchors at every level. Per-criterion anchors live in [`v2-design.md`](./v2-design.md) under "V2 rubric." Reproduced summary:

| ID | Name | Type |
|---|---|---|
| C1 | Verifiable artifact citation | Direct-inspection |
| C2 | Substantive vs theatrical concerns | Direct-inspection |
| C3 | Missed real concerns | Counterfactual-inference |
| C4 | Calibrated confidence | Counterfactual-inference |
| C5a | Factual accuracy | Closed-world accuracy vs the fact-checked pack (new in V2; re-scoped from open-world factuality 2026-06-12) |
| C5b | Engagement-with-source | Engagement (new in V2) |

The anchored 1-7 scale carries behavioral anchors at every level. The full per-level / per-criterion anchor tables are reproduced in [`v2-design.md`](./v2-design.md) and rendered in the rating tool form. The rubric criteria themselves are the V1 four (C1-C4 inherited unchanged in semantics, re-anchored for the wider scale) plus the V2 two (C5a, C5b — the accuracy / engagement split, both scored against the fact-checked pack). Per the 2026-06-12 amendment, C5a was re-scoped from open-world ground-truth factuality to closed-world Factual accuracy; the V1 §5.4 pack-fidelity-vs-ground-truth-fidelity gap is closed upstream by the independent pack fact-check at lock, not by rater-level external verification.

---

## 5. Two instruments per rater per case

V2 collects two instruments per rater per case:

### 5a. Absolute scoring (1-7 per criterion, per side X and Y)

For each case, each rater scores Answer X and Answer Y independently on the six-criterion 1-7 anchored scale. 6 criteria × 2 sides = 12 score points per rater per case. Across 4 raters × 2 cases × 12 score points = 96 absolute-score data points.

### 5b. Paired comparison (per criterion)

For each case, each rater also indicates a per-criterion paired-comparison preference: "X better," "Y better," or "tied" — one of three for each of the six criteria. Across 4 raters × 2 cases × 6 criteria = 48 paired-comparison data points.

Both instruments are required. The rating tool blocks submission until both passes are complete.

---

## 6. Rater pool and rater-condition declaration

V2 uses a four-rater pool:

| Rater | Identifier | Role / SPARRING-author status |
|---|---|---|
| Bart Niedner | "Breegarra" / user_id=1 | RF partner; SPARRING framework author |
| External rater E3 | "Icarus" / user_id=7 | RF partner; conceptual architecture co-author |
| External rater E4 | "Worthless Wizard" / user_id=4 | RF partner; not a SPARRING-framework author |
| External rater E1 | `[redacted-email]` / user_id TBD at provisioning | External; not RF, not SPARRING-author |

Three of four raters are RF partners; one is fully external. Two of four raters are SPARRING-framework non-authors (External rater E4 + External rater E1). This expanded pool addresses the V1 §6 author-as-rater limitation directly.

**Rater-condition declaration is a required field per CONSORT 2010 item 11a affirmative-declaration discipline.** Each rater declares their rating condition before submission:
- **Unaided** — no AI assistance, no co-reader, no parallel session.
- **AI-assisted** — used Claude / ChatGPT / Gemini / other LLM during the rating session. Free-text required: which AI, what for.
- **Co-reader-aided** — discussed the materials with another person during the rating session. Free-text required: who, what for.
- **External-source-checked** — verified the decision pack's claims against external sources (papers, references, codebases, etc.). Free-text required: what was checked, what was found.
- **Multiple of the above** — free-text required for each that applies.

This closes V1's silence-as-permission inference. Per CONSORT 2010 default, "blind rating" without further specification is read as blind-AND-unaided; V2 makes the rater's condition explicit so analysis can either restrict to a comparable-conditions subset or treat the asymmetry as a declared confound.

---

## 7. Cross-vendor LLM judge panel (V1 panel, inherited unchanged)

Three independent LLM judges, each receiving the same six-criterion rubric and rating Answer X and Answer Y on the 1-7 scale per criterion:

- **Anthropic** — `claude-sonnet-4-6` (matching V1; if a newer Sonnet is the current frontier at run time, V2 substitutes per the same pre-reg discipline V1 used for model substitutions).
- **OpenAI** — `gpt-4o`.
- **xAI** — `grok-3` (or current frontier Grok).

Each judge runs each case TWICE, with X/Y positions flipped between passes (V1 position-randomization protocol, inherited unchanged, addresses Wang et al. 2023 position bias). Per-judge per-criterion per-condition score = mean of the two passes. Total LLM judge calls: 2 cases × 3 judges × 2 position-passes = 12 (same as V1).

Cross-vendor consensus is computed as the mean across the three judges for each (case, condition, criterion) cell.

Note on the V1 finding (preprint §5.1): the cross-vendor structure cost more in calibration noise than it saved in self-preference mitigation when both conditions shared a substrate (Claude). Because V2 keeps both conditions on Claude (per Q5 Phase-2 deferral), this cost-benefit asymmetry is expected to persist. We retain the cross-vendor structure for V2 anyway because (a) it preserves V1-vs-V2 methodology comparability on this dimension, and (b) Phase 2 cross-substrate work depends on cross-vendor calibration evidence collected here.

---

## 8. Analysis plan

### 8a. Cross-rater statistics (within-rater-condition only)

Cross-rater statistics are computed only across raters in comparable rating conditions. Per the rater-condition declarations:

- If all four raters are unaided → cross-rater statistics computed across n=4.
- If a subset of raters is unaided → cross-rater statistics computed on the unaided subset only; non-unaided raters reported as exploratory standalone (analogous to V1 §4.8).
- If no rater is unaided → cross-rater statistics computed across the largest comparable-condition subset; report condition explicitly.

**Reported per-criterion**: Spearman ρ across raters, mean across raters, stdev across raters.

### 8b. Per-judge / cross-vendor alignment vs partner ratings

Per V1's analysis plan, computed against the *primary partner reference* defined here as the unaided RF-partner subset (Bart, External rater E3, External rater E4 — to the extent each rates unaided). If only some are unaided, the primary reference is restricted to the unaided ones.

**Reported per-criterion**:
- Spearman ρ between each LLM judge's scores and the primary-reference partner mean.
- Spearman ρ between cross-vendor consensus (mean of 3 judges) and the primary-reference partner mean.
- Per-judge per-criterion absolute alignment.

### 8c. Two-tier per-criterion gate classification

Per the locked Q4 decision in `v2-design.md`:

- **High-tier criteria (C1, C2, C5a, C5b)**: ρ ≥ 0.7 PASS, 0.4-0.7 BORDERLINE, < 0.4 FAIL.
- **Lower-tier criteria (C3, C4)**: ρ ≥ 0.5 PASS, 0.2-0.5 BORDERLINE, < 0.2 FAIL.

**Aggregate V2 gate classification**:
- **PASS**: ≥ 5 of 6 criteria PASS at their respective tier AND no criterion FAIL.
- **BORDERLINE**: ≥ 4 of 6 criteria PASS AND no more than 1 criterion FAIL.
- **FAIL**: any other outcome.

### 8d. Paired-comparison aggregate analysis

For each criterion, count "X better" / "Y better" / "tied" votes across raters and across cases. Report:

- Per-criterion vote distribution (counts and proportions).
- Per-criterion sign agreement: did the per-criterion paired-comparison majority match the per-criterion absolute-score B − A direction?
- A binomial test on the per-criterion paired vote distribution (against a null of P(X better) = P(Y better) = 0.5, ties excluded). Report p-values and effect sizes.

The paired-comparison analysis is the ceiling-resistant signal V1 lacked. It produces a signal even if absolute scores saturate (per the V1 §4.7 ceiling effect).

### 8e. Per-criterion delta (B − A; framework minus baseline)

Inherited from V1 §4.4. Reported per partner, per LLM judge, per cross-vendor consensus, per criterion. Mean across criteria reported. The partner-ratings-of-condition-α delta (Bart in V1 was +1.125; V2 reports the unaided-partner-subset mean delta).

### 8f. Direction-of-preference unanimity check

V1 found unanimous directional preference for SPARRING across all raters and criteria. V2 reports the same metric: across raters × judges × criteria × cases, what fraction prefer SPARRING vs baseline? Pure descriptive; no statistical test attached, since direction-of-preference unanimity is interpreted in §5 of the V2 preprint, not as a confirmatory result.

---

## 9. Pre-registered hypotheses

These are the V2 hypotheses, locked before any compute is spent:

**H1 (replication of V1 directional finding)**: SPARRING will be rated higher than single-agent baseline on the majority of criterion-cells (across criteria × raters × judges). Pre-registered direction.

**H2 (cross-vendor consensus tracks unaided partner reference under two-tier gate)**: At least 4 of 6 criteria will pass their respective tier in §8c (i.e., V2 will be classified as PASS or BORDERLINE on the aggregate gate).

**H3 (paired-comparison shows direction even if absolute scores saturate)**: For at least 4 of 6 criteria, the paired-comparison per-criterion majority will be statistically distinguishable from a 50/50 null (p < 0.05 binomial, ties excluded).

**H4 (rater-condition asymmetry, if any, is bounded)**: If raters split between unaided and AI-assisted conditions, the cross-condition Spearman ρ on absolute scores within each criterion will be ≥ 0.4 (i.e., the condition asymmetry does not produce wholesale rater-pool incoherence). This hypothesis is contingent on at least one rater being non-unaided; if all raters declare unaided, H4 is vacuously satisfied and not reported.

H1, H2, H3 are the primary hypotheses. H4 is the methodology-validation hypothesis on rater-condition.

---

## 10. Stopping rule and protocol-amendment policy

**Stopping rule**: V2 compute completes when all four raters have submitted both instruments (absolute scoring + paired comparison) on both cases AND all 12 LLM judge calls have completed (2 cases × 3 judges × 2 position-passes). After that point, the dataset is locked and analysis runs.

**Protocol-amendment policy**: Any deviation from this pre-registration after compute begins must be reported as a protocol amendment, with the deviation, the date, the rationale, and the affected analysis steps recorded in the V2 preprint per [Nosek 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114) and [APS *Observer* on preregistration deviations](https://www.psychologicalscience.org/publications/observer/methods-preregistration-deviations.html). Deviations include: rater drop-out, model substitutions, rubric anchor changes, gate-threshold adjustments, analysis-plan additions or removals.

If a rater drops out, the V2 dataset reports n=3 raters with explicit attribution of which rater dropped and at what stage. Cross-rater statistics restrict to the comparable subset.

---

## 11. What this study will and will not be able to conclude

**Will be able to conclude**:
- Whether SPARRING produces directionally-preferred outputs over single-agent baseline on domain-independent decision tasks, with a four-rater pool and cross-vendor judge consensus (descriptive, not inferential, given the calibration-check sample size).
- Whether the V2 rubric — six criteria with two-tier gates — produces a more interpretable signal than V1's single-tier gate.
- Whether the paired-comparison instrument produces a ceiling-resistant signal that complements absolute scoring.
- Whether the rater-condition declaration discipline produces interpretable cross-rater statistics under conditions of mixed rater-condition.

**Will not be able to conclude**:
- "SPARRING is better than single-agent baseline" as a confirmatory claim with effect-size estimate. n=2 cases, n=4 raters, no power calculation.
- Generalization to other deliberation frameworks, other domains, or other rater pools.
- Substrate-independence of the framework (cross-substrate Phase 2 work required).
- Long-term stability of the rubric or judge panel (Phase 2+ replication required).

---

## 12. Pre-registration commit + tag flow

This document is the V2 pre-registration. It locks the design and analysis plan. The lock procedure:

1. **Author finalizes** `v2-design.md`, this document, the two decision packs, and the schema migration. Independent fact-check pass on the decision packs (by Bart in this case, since the cases are non-SFxLS and Bart is not the author of the case-content domain knowledge).
2. **Single atomic commit** containing:
   - `v2-design.md` (locked)
   - `v2-00-pre-registration.md` (this document)
   - `v2-decision-packs/case-a-organizational-vocabulary.md`
   - `v2-decision-packs/case-b-introductory-programming-curriculum.md`
   - `database/migrations/198_v2_eval_schema.sql`
   - Commit message naming "v2-prereg lock" explicitly for git-log retrievability.
3. **Tag** the commit with `v2-prereg-2026-05-XX` (XX is commit date).
4. **Capture the commit SHA** in a one-line edit to this document, replacing the "Pre-reg commit hash: TBD" line at the top with the actual hash. That one-line edit goes in a separate immediately-following commit so the original lock commit is preserved unmodified.

After step 4, no edits to this document, the design doc, the decision packs, or the migration are permitted without a protocol amendment commit that explicitly notes the deviation.

V2 compute begins after step 4. The schema migration is run on nonprod. The rating-tool form/API updates are deployed. The four raters are briefed and rate. The 12 LLM judge calls are spent. Analysis runs against the locked plan.

---

## 12.1. Protocol amendments

Amendments to this pre-registration after lock are appended below in chronological order, per the Nosek 2018 / APS *Observer* deviation-disclosure discipline named in §10. Each entry records: amendment date, scope, rationale, what changed, and whether any rater data had been collected at the time of amendment (the integrity-relevant question).

### Amendment 2026-05-03 — format symmetry between Cond A and Cond B outputs

**Date**: 2026-05-03 (same calendar day as pre-reg lock).
**Pre-rater-data**: YES — no rater data had been collected at the time of this amendment. Amendment was applied during the operational deployment phase (§13 logistical follow-ups), specifically immediately after `rd_eval_cases` was populated with the V2 condition outputs and before the first rater session opened.
**Scope**: Display format of the Condition B outputs in the rating tool, for both cases.
**Rationale**: A blinding-integrity defect was observed during pre-rater operational review. The Condition A outputs (single-agent baseline) rendered as clean decision-quality recommendations with the structure `## Recommendation / ## Reasoning chain / ## Concerns / ## Confidence`. The Condition B outputs (SPARRING ceremony) rendered as the full `/spar` ceremony record, including `## Personas`, `## Iteration log` with `### Round 1` / `### Round 2` headers, persona signal blocks (`{agree: true|false, reasoning: "..."}`), `## Final evaluation`, `## Artifacts surfaced`, and `## Recommendation for parent` sections. This format asymmetry is visually distinctive at first glance (before any content is read) and breaks the blind: a rater can identify which side is the SPARRING output purely from structural cues, regardless of the X/Y position-randomization that anonymizes condition assignment. Per Schulz & Grimes (*Lancet* 2002), blinding requires that allocation be concealed at the level of the comparison instrument, not merely at the level of the labels on the comparison. Format-level cue-leakage falls within the scope of the Schulz & Grimes blind-integrity standard.
**What changed**: For both cases, a new format-symmetric recommendation file was authored alongside the existing ceremony record:
- Case A: [`v2-condition-b-spar/case-a-recommendation.md`](./v2-condition-b-spar/case-a-recommendation.md) (new) alongside [`v2-condition-b-spar/case-a-spar.md`](./v2-condition-b-spar/case-a-spar.md) (preserved, ceremony audit trail).
- Case B: [`v2-condition-b-spar/case-b-recommendation.md`](./v2-condition-b-spar/case-b-recommendation.md) (new) alongside [`v2-condition-b-spar/case-b-spar.md`](./v2-condition-b-spar/case-b-spar.md) (preserved, ceremony audit trail).

The new recommendation files preserve the substantive content of the SPARRING ceremony output (recommendations, citations, residual concerns, confidence calibration) but match Condition A's section structure (`## Recommendation / ## Reasoning chain / ## Concerns / ## Confidence`). The original ceremony records are retained unchanged as the audit trail of what the `/spar` ceremony actually produced — they remain the methodologically authoritative artifact for any post-hoc analysis questions about the ceremony itself. The recommendation files are the rater-presented form.

The `rd_eval_cases` rows on nonprod were updated to point to the new recommendation files: case id=3 (Case A) `answer_y_text` (Y=sparring per the locked X/Y assignment) replaced; case id=4 (Case B) `answer_x_text` (X=sparring per the locked X/Y assignment) replaced.

**Affected analysis steps**: None of the §8 analysis plan steps depend on the Condition B output format — they depend on rater scores and judge scores, which are produced from the rater/judge view of the materials. The amendment changes the rater/judge view of the Condition B side from "ceremony record" to "recommendation," which is the methodologically correct view for the comparison the pre-registration specifies (decision-quality output of the framework vs. decision-quality output of the baseline).

**Tag**: `v2-prereg-amendment-2026-05-03-format-symmetry` (applied to the amendment commit).

### Amendment 2026-05-27 — rater pool opened to known-identity convenience sample; recruitment window and claim-scaling rules added

**Date**: 2026-05-27.
**Pre-rater-data**: YES — no V2 rater data had been collected at the time of this amendment. The V2 instrument has been live on nonprod since 2026-05-03; none of the four originally-named raters had submitted any ratings by amendment lock. This amendment is committed before any rating content has been inspected.

**Scope**: §6 (Rater pool and rater-condition declaration) — recomposition. §10 (Stopping rule) — replacement. §8 (Analysis plan) — claim-scaling rules added; gate classification reframed as scale-dependent. §9 (Pre-registered hypotheses) — inferential weight of H1-H4 scales with achieved n per the new claim-scaling table; hypotheses themselves are unchanged. §11 (What this study will and will not conclude) — implicit; the n=4 framing is superseded.

**Rationale**: The original §6 closed pool (Bart Niedner, External rater E3, External rater E4, External rater E1) was V2's response to V1's "author-as-rater" limitation (V1 preprint §6) via deliberate RF/non-RF and author/non-author stratification. In practice, recruitment friction has prevented this design from running: three of four named raters reported insufficient time, and 24 days after instrument deployment (2026-05-03 → 2026-05-27) zero V2 ratings exist. Continuing to wait risks stale-time-of-rating drift (V2 instrument shipped, decision packs and condition outputs locked, judge calls completed 2026-05-13 at commit `9c7b27b7`) and does not improve the methodology. Opening the pool to a known-identity convenience sample from BN's professional network (LinkedIn 1st-degree connections, Facebook friends) trades the stratification for **scale** and **externality** — most network contacts are not framework authors, have no stake in the result, and are not subject to the family/coercion bias of the original closed pool. "BN's wife and brother rate the framework BN wrote" is structurally worse than "n LinkedIn contacts BN knows personally rate the framework" for the author-as-rater concern that motivated V2 in the first place. The amendment improves external validity rather than weakens it.

**What changed**:

**§6 rater pool — replaced.** The named four-rater table is superseded by an open convenience sample recruited from BN's professional and social network via public posts (LinkedIn, Facebook). Inclusion criteria:
- Recruit reaches the recruitment posts through BN's LinkedIn or Facebook surface (1st-degree connection, friend, or someone the post propagated to via shares).
- Recruit is over 18.
- Recruit completes both V2 cases (Case A organizational vocabulary; Case B introductory programming curriculum).

Onboarding uses a **public self-serve sign-up page** at `https://nonprod.lifspel.com/research/rater-signup.php` (Lifspel commit `26033789`, deployed 2026-05-27). The page collects email, display name, password, and a required free-text attestation ("How do you know Bart?"); on submit it creates a `users` row with `is_rater=1`, records the sign-up to `rd_eval_invites` with `created_by_user_id=1` (BN as sentinel sponsor) and `note='SELF-SIGNUP: '` + attestation, auto-logs the rater in, and redirects to the rating tool. The audit trail still flows through `rd_eval_invites` with the `SELF-SIGNUP:` prefix marking provenance, but no admin pre-generation is required and there is no DM-and-wait friction. A honeypot field filters obvious bot traffic.

This is a deliberate shift from the original 2026-05-27 amendment text, which specified per-rater token DMs. The revision happened the same day, still pre-rater-data, after the per-rater-DM friction was assessed against the realistic recruitment cadence on BN's network and found likely to drive uptake below the n=4 floor (see "Revision history" at the end of this amendment).

The original four named raters (Bart, External rater E3, External rater E4, External rater E1) remain eligible — if any complete ratings, they count toward the open-pool n with no special weighting and no separate analysis branch. The External rater E1-provisioning task in §13 is retained for that reason; the External rater E4/External rater E1 briefing tasks in §13 become best-effort rather than blocking.

The required rater-condition declaration (§6 paragraphs 2-3) is **unchanged**. It applies to every rater in the open pool the same way it applied to the closed pool.

The known-identity property of the sample is now partial rather than enforced: BN cannot verify each self-signup the way he could a per-rater DM, but the attestation field captures the relationship in writing, and the LinkedIn/Facebook reach of the recruitment post de facto restricts the sample to BN's network and its share-reach. Recruitment-channel disclosure in the eventual write-up describes this trade explicitly (see "Disclosure language" below).

**§10 stopping rule — replaced.** The original "compute completes when all four raters have submitted both instruments on both cases" rule is superseded by the recruitment-window structure below.

> **Recruitment window:**
>
> **Day 0** (2026-05-27): recruitment opens. BN posts the public self-serve sign-up URL (`https://nonprod.lifspel.com/research/rater-signup.php`) to his LinkedIn and Facebook surfaces.
>
> **Day 7 checkpoint** (2026-06-03):
> - If **n ≥ 15** completers: hard stop, recruitment closes immediately.
> - If **4 ≤ n < 15**: recruitment closes to *new* invitations; existing in-progress invitations remain open for an additional 7 days (through day 14, 2026-06-10).
> - If **n < 4**: BN documents the extension decision in writing (date, achieved n, reasoning, new checkpoint date) before inspecting any rating content. New checkpoint set at day 14 (2026-06-10) or BN's documented earlier/later choice.
>
> **Subsequent checkpoints** (if extension active): same rule as day 7.
>
> **Absolute close**: day 28 (2026-06-24). All recruitment ends regardless of n.
>
> **Stopping-decision blinding**: at every checkpoint, BN inspects only the completer count, not rating content. Rating data is examined only after recruitment closes. This blinding extends the X/Y server-side blinding (which already exists per the V2 instrument) to the recruitment-stopping decision itself, addressing the stopping-rule-contamination risk identified in Wagenmakers et al. 2012 and the broader pre-registration literature.

**§8 analysis-plan claim-scaling — new sub-section §8g, added.** All §8a-§8f analyses are reported regardless of achieved n; statistical-significance claims and inferential weight scale per the pre-specified table below. The table is locked at amendment commit; no post-hoc upgrades are permitted.

| Achieved n | Permitted claims |
|---|---|
| **n < 4** | Recruitment outcome reported as "below floor"; no §8 rating-side analysis is produced. Judge-side analyses (§7) are reported standalone. |
| **n = 4** | Descriptive reporting only. Point estimates with caveats. No sign tests. Gate classification (§8c) reported as descriptive observation, not inferential test. H1-H4 reported descriptively without confirmatory claims. |
| **n = 5-6** | + Sign test for directional findings reported where unanimous (n=5 unanimous: p=0.031; n=6 unanimous: p=0.016). |
| **n = 7-9** | + Bootstrap CI on cross-vendor judge ρ vs partner ρ. Sign test robust to one dissenter (6/7: p=0.063 borderline; 7/7: p=0.008 significant). H2 gate classification (§8c) treated as confirmatory at the bound of the §8c thresholds. |
| **n ≥ 10** | + Krippendorff's α with bootstrap CI per Hayes & Krippendorff 2007. Full inferential package on H1-H4 per their stated thresholds. |

The two-tier gate in §8c (PASS/BORDERLINE/FAIL on ρ for high-tier vs lower-tier criteria) remains the classification rule and is unchanged. What scales with n is the confidence in the classification — at small n the point estimate falls in a band; at larger n the bootstrap CI confirms or rejects the band placement.

**§9 hypotheses — unchanged in statement; inferential weight scales per the table above.** H1 (replication of directional preference) is always reportable descriptively. H2 (gate classification PASS or BORDERLINE) is reportable descriptively at any n and inferentially at n ≥ 7. H3 (paired-comparison binomial) is computable but cannot reach p < 0.05 below n = 5. H4 (rater-condition cross-condition ρ ≥ 0.4) remains contingent on at least one rater being non-unaided AND at least one rater being unaided; at very small n the per-condition subsets may themselves be below the §8a cross-rater-statistics floor.

**§11 conclusions — implicit update.** "With a four-rater pool" wherever it appears in §11 should be read as "with the achieved n per the recruitment window," and the descriptive-vs-confirmatory split scales per the §8g claim-scaling table.

**Affected analysis steps**: §8a-§8f are unchanged in computation; what changes is the inferential weight attached to each result, per the new §8g claim-scaling table. The two-tier gate in §8c is unchanged. The directional-preference unanimity check (§8f) is unchanged in computation and remains descriptive regardless of n. The rater-condition asymmetry handling (§8a, §8b, §8d, H4) is unchanged. Judge-side analyses (§7) are unaffected. The V1 PASS gate threshold (ρ ≥ 0.4) was already retired in V2 by the two-tier gate (§8c); this amendment does not further modify that.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "The V2 rater pool was amended on 2026-05-27, before any V2 rater data was collected, from a closed n=4 design (3 framework-affiliated raters + 1 external) to an open convenience sample recruited via public posts on the framework author's LinkedIn and Facebook surfaces. Recruits self-onboarded through a public sign-up page hosted on the SPARRING research infrastructure; each sign-up captured a free-text attestation of the recruit's relationship to the author. The original closed-pool design encountered recruitment friction over 24 days; the amendment was committed and tagged pre-rater-data per Nosek et al. 2018. Claims reported in this paper scale with achieved n per the pre-registered claim-scaling rules (§8g) added at the same amendment. Limitations include selection bias from the recruitment channel (framework author's personal social media), absence of demographic stratification, loss of the original RF/non-RF and author/non-author stratification, and self-selection of participants willing to spend ~1 hour on AI-evaluation research. The recruitment-stopping decision was blinded to rating content per the stopping-rule provisions of the amendment."

**Tags**:
- `v2-prereg-amendment-2026-05-27-rater-pool-open-network` (original commit, applied 2026-05-27).
- `v2-prereg-amendment-2026-05-27-r2-self-serve` (same-day revision shifting onboarding from per-rater DM tokens to public self-serve sign-up; see Revision history below).

**Revision history**:
- **2026-05-27 r1**: original commit. Specified per-rater token DM flow (`/admin/rd-invites.php` → SendGrid) for onboarding. Tag: `v2-prereg-amendment-2026-05-27-rater-pool-open-network`.
- **2026-05-27 r2**: same-day pre-data-look revision. Replaced per-rater token DM flow with public self-serve sign-up (`/research/rater-signup.php`, Lifspel commit `26033789`). Triggered by partner pushback that the DM-and-wait friction would drive uptake below the n=4 floor against the realistic recruitment cadence on BN's network. Pre-rater-data status preserved (still zero V2 ratings at revision time). Tag: `v2-prereg-amendment-2026-05-27-r2-self-serve`.

### Amendment 2026-06-04 — rater-facing framework-identity blind; prior-familiarity recorded as a measured covariate, not an exclusion gate

**Date**: 2026-06-04.
**Pre-rater-data**: YES — no V2 rater data had been collected at the time of this amendment. The V2 instrument has been live on nonprod since 2026-05-03; the recruitment posts drafted at the 2026-05-27 amendment were never published, so Day 0 of the recruitment window never opened and zero V2 ratings exist. This amendment is committed before any rating content has been inspected and before recruitment opens.

**Scope**: Rater-facing display copy on the sign-up and rating surfaces (framework-identity concealment). §6 (Rater pool and rater-condition declaration) — additive: a prior-familiarity covariate is added alongside the existing rater-condition declaration. §8 (Analysis plan) — new sub-section §8h (familiarity-stratified sensitivity analysis), additive. No §4 rubric, §7 judge-panel, §8c gate, §9 hypothesis, or §10 stopping-rule change.

**Rationale**: A second blinding-integrity defect was identified during pre-launch operational review, of the same species as the 2026-05-03 format-symmetry defect. The rater-facing surfaces name the framework by its proper noun ("SPARRING"): the sign-up page title and heading read "SPARRING Pilot" (`lifspel:research/rater-signup.php`) and the rating tool's "What this study is" block referenced the framework by name. The recruitment posts themselves deliberately do *not* name the framework — so the funnel is internally inconsistent: a neutral post lands the recruit on a page that names the framework. This defeats the existing "repo link withheld until after submission" guard (2026-05-27 amendment, §10 / recruitment-post decision 5): a recruit handed the proper noun can search it, reach the public `muddyone/sparring-framework` repository whose `pilots/llm-judge-2026-05-02/v2/condition-{a-baseline,b-spar}/` directories label which condition produced which output, and de-anonymize the X/Y assignment that the server-side blinding and position-randomization exist to protect. Per Schulz & Grimes (*Lancet* 2002, §14 references), blinding requires allocation be concealed at the level of the comparison instrument, not merely at the labels on the comparison; a rater-facing search term that leads to the labeled condition outputs is a cue-leakage path within that standard. This is the same reasoning the 2026-05-03 format-symmetry amendment applied to a structural cue; this amendment applies it to a nominal cue.

A distinct but related concern motivated the familiarity covariate. The recruitment channel (the framework author's own LinkedIn, where SPARRING essays have been and continue to be published) guarantees that a non-trivial fraction of recruits will have prior exposure to the framework. The originally-contemplated guard — an *intake* question screening out familiar recruits — was rejected on three grounds: (1) an intake question that names the framework would itself prime naive recruits and send them to search for it mid-study, manufacturing the exposure it purports to prevent; (2) self-reported naivety is unverifiable, so an exclusion gate confers false confidence; and (3) gating on naivety against a recruitment channel that is exposed-by-construction risks driving the achieved n below the §10 floor of 4. The methodologically stronger move — and the one consistent with the §8g measure-and-disclose posture already adopted for recruitment-channel selection bias — is to *record prior familiarity as a graded covariate, collected after both instruments are submitted*, and to report familiarity-stratified sensitivity analyses rather than assume exposure away.

**What changed**:

**Rater-facing framework-identity blind.** All rater-facing surfaces (sign-up page, rating tool) are revised to refer to the study by a neutral name (the operative public-facing study name is the "Resource Forge AI Decision-Evaluation Pilot" or equivalent) and to describe the comparison generically ("two AI decision-making approaches," "a structured-deliberation approach") without the framework's proper noun. The framework's identity, the public repository link, and the open-access methodology are disclosed to each rater *after* both instruments are submitted (extending the existing repo-link-after-submission discipline to the framework name itself). Internal code comments, commit messages, file paths, and this pre-registration retain the SPARRING name; the concealment is scoped strictly to the pre-submission rater experience. This is allocation concealment, not non-disclosure: nothing is withheld from raters permanently, and the full methodology remains publicly pre-registered and open-access throughout.

**§6 — prior-familiarity covariate added (additive; rater-condition declaration unchanged).** A required graded prior-familiarity item is collected from each rater *after* both instruments are submitted for both cases and *before* the post-submission framework-identity reveal. It is a separate axis from the §6 rater-condition declaration (which concerns *how* the rating was produced; familiarity concerns *what the rater knew going in*). The ordinal scale, logged per rater:

| Code | Prior familiarity with the framework being evaluated |
|---|---|
| **F0** | None — had not heard of it before today. |
| **F1** | Name-only — had heard of it but read nothing substantive. |
| **F2** | Reader — read one or more essays/posts/book material about it, but have not practiced it. |
| **F3** | Studied — read its methodology or specification in depth. |
| **F4** | Practitioner — have run its ceremonies / used its tooling, and could plausibly recognize its raw output style. |

F4 (and to a lesser degree F3) marks raters with the capacity to *fingerprint* a condition's output style and thereby de-anonymize the X/Y mapping independent of the nominal blind; F0–F2 marks exposure that is a potential *bias* on judgment but carries no de-anonymization capacity. The item is recorded (column on the rater/eval record, mirroring how `rater_condition` is recorded) so the §8h sensitivity cuts can be computed. It is **not** an exclusion gate: no recruit is screened out on familiarity, and all achieved ratings count toward the §8g claim-scaling n.

**§8 — new sub-section §8h, familiarity-stratified sensitivity analysis (additive).** The §8a–§8f analyses run on the full achieved pool as specified. In addition:
- **Low-exposure sensitivity cut**: §8a–§8f recomputed on the F0–F2 subset. If the gate classification (§8c) and direction-of-preference (§8f) on the low-exposure subset agree with the full-pool result, prior exposure is reported as non-load-bearing on the finding. If they diverge, the divergence is itself the reported finding.
- **Fingerprint-capable cut**: §8a–§8f recomputed excluding F4 raters (and reported with/without F3), because for F4 the risk is condition de-anonymization (a blinding-integrity threat), not mere bias. BN (F4, framework author) is the canonical member of this group; this cut operationalizes the V1 author-as-rater limitation rather than introducing a new one.
- Both sensitivity subsets are themselves subject to the §8g claim-scaling floors: a subset below the relevant n threshold is reported descriptively only, with the subset n stated explicitly. No sensitivity cut can upgrade the inferential weight permitted by the full-pool achieved n.

**Operational (not a pre-registered constraint).** Publication of *new* framework essays on the recruitment channel during the open recruitment window is paused on a best-effort basis to limit fresh priming. This is a soft operational choice, not a pre-registered design element; past published essays are already public and are handled by the §8h covariate, not by un-publication.

**Affected analysis steps**: §8a–§8f are unchanged in computation; §8h overlays familiarity-stratified recomputation of those same steps. §8c gate, §8g claim-scaling table, §9 hypotheses, and §10 stopping rule are unchanged. The §6 rater-condition declaration is unchanged and remains orthogonal to the new familiarity axis.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "Before recruitment opened, the rater-facing sign-up and rating surfaces were revised to conceal the evaluated framework's identity (proper name, public repository, and open-access methodology) until after each rater submitted both instruments, extending the pre-existing post-submission repository-disclosure discipline to the framework's name. This closed a cue-leakage path by which a recruit given the framework's name could locate the public repository whose condition directories label the X/Y assignment. Prior familiarity with the framework was not used as an exclusion criterion — the recruitment channel (the author's personal social media, where essays on the framework had been published) made naivety unverifiable and recruitment-limiting. Instead, each rater's prior familiarity was recorded after submission on a five-level ordinal scale (none / name-only / reader / studied / practitioner) and analysed as a covariate: primary results are reported on the full achieved pool, with pre-registered sensitivity analyses restricting to low-exposure raters and excluding fingerprint-capable raters. New essays on the framework were not published on the recruitment channel during the recruitment window. These provisions were committed and tagged pre-rater-data per Nosek et al. 2018."

**Tag**: `v2-prereg-amendment-2026-06-04-naming-blind-familiarity-covariate` (to be applied to the amendment commit).

### Amendment 2026-06-04 (partial completers) — single-case raters retained for a pre-specified per-case secondary analysis

**Date**: 2026-06-04 (second amendment of this date; independent of the naming-blind/familiarity amendment above).
**Pre-rater-data**: YES — no V2 rater data had been collected at the time of this amendment (`rd_eval_ratings` empty on the production instrument at amendment time, verified). Committed and tagged before any rating content was inspected and before recruitment opened.

**Scope**: §6 (rater retention — additive), §8 (new secondary sub-section §8i — additive), §10 (checkpoint-count clarification). The headline/primary completer-based n-definition and the §8g claim-scaling table are **unchanged**.

**Rationale**: The rater-facing sign-up was revised to stop signaling an expected time commitment (the prior "~1 hour, splittable" subtitle was removed), and the recruitment posts likewise drop the total-time figure, on the partner's principle that pre-stating the commitment suppresses uptake and that an incomplete review is no worse than one never begun. A predictable consequence is that some recruits will complete one of the two cases rather than both. A single-case rating is a genuine per-case observation, not noise — discarding it wastes signal, while silently folding it in *after* seeing results would be exactly the analysis-degrees-of-freedom that pre-registration exists to foreclose (Wagenmakers et al. 2012; Nosek et al. 2018). This amendment pre-specifies, before any data, how partial completions are retained and analysed.

**What changed**:

**§6 / headline n — primary analyses remain completer-based (unchanged in definition, clarified for partials).** "Completer" continues to mean a rater who rated **both** cases. The primary analyses (§8a–§8f), the two-tier gate classification (§8c), and the §8g claim-scaling thresholds remain defined on the completer-n. A single-case rater **does not** increment the headline n. What changes is only that a single-case rater's data is no longer discarded:

- A recruit who completes at least one case (both instruments — absolute scoring + paired comparison — on that case) is **retained as a partial contributor**; their per-case ratings are kept.

**§8i — secondary per-case analysis (new, additive).** Reported alongside (and clearly subordinate to) the primary analyses: for each case independently, cross-rater statistics — and, at the relevant achieved per-case n, **Krippendorff's α** — are computed over **all available ratings on that case**, completers and single-case raters alike. Krippendorff's α is the appropriate instrument here precisely because it accommodates incomplete reliability matrices by design (Hayes & Krippendorff 2007); single-case raters appear as present on the case they rated and missing on the other, without being dropped. §8i is labeled secondary/supplementary in any write-up; it does not feed the §8c gate, which stays on the completer pool.

**Familiarity-covariate interaction (precise spec).** The prior-familiarity item added by the naming-blind amendment is presented by the instrument only at full completion (after all cases are submitted). Single-case raters therefore record **no familiarity value**: they are excluded from the §8h familiarity-stratified cuts (which operate on completers) and enter the §8i per-case secondary analysis as familiarity-unknown.

**§10 stopping rule / checkpoint blinding — clarified, not changed.** The completer count BN inspects at each checkpoint remains the **both-cases** count. A separate single-case-only count may be tracked for recruitment monitoring; it too is inspected content-blind. The stopping-decision blinding (Wagenmakers et al. 2012) is unchanged.

**Affected analysis steps**: §8a–§8f, §8c, §8g, and §9 primary reporting are unchanged (all completer-based). §8i is added as a secondary, per-case, partial-inclusive analysis. §8h (familiarity-stratified cuts) is unchanged and continues to operate on completers only.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "The rater-facing onboarding was revised before recruitment to remove any stated time commitment, on the rationale that pre-stating the commitment suppresses uptake. To handle the resulting single-case completions transparently, this was pre-specified pre-rater-data: primary analyses and the gate classification are reported on completers (raters who rated both cases) per the pre-registered claim-scaling rules; a secondary, clearly-subordinate per-case analysis additionally uses all available ratings on each case — including single-case raters — with inter-rater reliability estimated via Krippendorff's α, which accommodates the incomplete rating matrix by construction. Single-case raters carry no prior-familiarity value (that item is collected only at full completion) and are excluded from the familiarity-stratified sensitivity analyses. The recruitment-stopping decision continued to be blinded to rating content."

**Tag**: `v2-prereg-amendment-2026-06-04-partial-completers` (to be applied to the amendment commit).

### Amendment 2026-06-04 (plain-language rebuild) — rater-facing materials replated to plain language; both conditions and the judge panel regenerated; substrate substituted to Opus 4.8

**Date**: 2026-06-04 (third amendment of this date).
**Pre-rater-data**: YES — no V2 rater data had been collected at the time of this amendment (`rd_eval_ratings` empty on the production instrument, verified immediately before the reload; the reload loader also refuses to run if any rating exists). Committed and tagged before any rating content was inspected and before recruitment opened. This is the most substantial amendment of the V2 series and supersedes the locked case content; it is admissible precisely because it is pre-rater-data.

**Scope**: §2 (conditions — substrate + baseline-prompt provenance), §3 (cases — the decision-pack text and the rater-facing question/evidence-summary fields), §7 (judge panel — re-run against the regenerated answers), and the `rd_eval_cases` X/Y assignment. The §4 rubric, §6 rater pool, §8 analysis plan, §9 hypotheses, and §10 stopping rule are **unchanged**.

**Rationale**: Operational review of the live rater tool found the decision packs and the rater-facing case fields were written at an academic reading level ("canonical address term," "lexical conventions," "cognitive-load / extraneous load," "andragogy," etc.). This is a barrier directly opposed to the study's stated purpose — a non-expert human-judgment signal (the recruitment framing is "if you can read a memo and form an opinion, you qualify") — and it is also a measurement confound: a rater straining to parse the prose scores partly on reading-level rather than on recommendation quality, injecting construct-irrelevant variance into the rubric criteria. Lowering the reading level is therefore both an access improvement and a measurement improvement, and it aligns the instrument with SPARRING's own plain-language-first discipline.

Critically, the conditions could **not** be hand-edited to plainer prose: the answers are the experimental stimulus, generated *from* the pack, and three rubric criteria (C1 verifiable-artifact citation, C5a factuality, C5b engagement-with-source) are scored *relative to the pack the rater reads*. Editing the answers would (a) reintroduce the experimenter-authored confound the 2026-05-03 format-symmetry amendment removed, and (b) break the comparative-validity guarantee that both conditions had identical access to the pack. The only valid way to obtain plainer answers is to replate the pack and **regenerate both conditions from it** — which also regenerates the materials the §7 judges scored, requiring a judge re-run.

**What changed**:

**§3 cases — packs replated to plain language; facts preserved.** Both decision packs were rewritten into plain register with every fact, citation, and magnitude preserved verbatim in meaning (Pfeffer 2007; *Toussaint v. Blue Cross*; SHRM 2024 71/22/4/3%; the 43-of-46 non-anonymous survey 12/67/21%; Sweller 1998; Bennedsen & Caspersen 2007 with the 65–78% / 58–85% ranges; Knowles 1980; Hatfield et al. 2019 ~12pp with the Lewis 2022 non-replication caveat; Smith & Garcia 2021 / Park et al. 2023 d≈0.18–0.22; the NCCC 64→73% history). An independent fact-check pass (per the V2 design's pre-condition rule) confirmed no fact, citation, or number drifted. The reviewer-facing "what this case is testing" meta was deliberately kept out of the rater-presented fields so the rubric is never telegraphed to raters. One typo in the locked Case B pack ("Norther" → "Northern Coastal Community College") was corrected. A plain-language reviewer (the project's Rosetta persona) gated both packs; one fabrication introduced during the first plain draft of Case A (an invented gender for the committee chair) was caught and removed before any artifact was committed. Plain packs: `decision-packs/case-{a,b}-*.plain.md`; rater-facing condensed fields: `rater-fields-plain.md`.

**§2 conditions — both regenerated from the plain packs; substrate substituted to Opus 4.8.**
- *Substrate*: the locked Q5 substrate (Claude Opus 4.7, under both conditions) is substituted to **Claude Opus 4.8** under **both** conditions. Per the partner's call, the model version was not load-bearing for the comparison; the binding constraint is that both conditions share one substrate (so substrate is not a confound), which is preserved. The cost is loss of the clean V1↔V2 substrate-comparability the design valued — accepted, and disclosed here. This substitution follows the same model-substitution discipline V1 used.
- *Condition A (baseline)*: regenerated by a single Opus 4.8 API call, no framework, 8000-token ceiling, via `scripts/run-condition-a.sh`. **Baseline-prompt provenance note**: the original V2 baseline prompt was not committed as a runnable script (only V1's `run-condition-a.sh`, which targets a different 400–600-word, no-`##`-headers shape, was in the repo). The locked V2 baseline *artifact* used the four-section `## Recommendation / ## Reasoning chain / ## Concerns / ## Confidence` structure. The system prompt used for this re-run is the partner-approved (2026-06-04) reconstruction that reproduces that documented structure, single-pass, no framework. The reconstruction is recorded verbatim in `scripts/run-condition-a.sh`.
- *Condition B (SPARRING)*: regenerated via the `/spar` skill (V1-default settings: 2 iterations, two divergent specialist personas with explicit distinct evidence bases, both-must-agree convergence, verifiable-artifact requirement on the Challenger), Generator and Challenger on Opus 4.8. Both cases converged in 2 rounds, and in both the Challenger materially changed the converged recommendation (Case A: tightened an under-specified legal remedy and corrected an over-read of the non-anonymous survey; Case B: forced a step-down from an undeliverable hybrid on staffing/deadline artifacts and withdrew an over-read of the 2018 language-change data). The **2026-05-03 format-symmetry amendment was re-applied**: the rater-presented Condition B form is a four-section recommendation matching Condition A's structure (`condition-b-spar/case-{a,b}-recommendation.plain.md`), with the full ceremony record retained as the audit trail (`condition-b-spar/case-{a,b}-spar.plain.md`).

**`rd_eval_cases` reloaded with a fresh X/Y assignment.** The plain condensed question/evidence fields and the four regenerated answers were loaded into the production instrument (`resourceforge.com/sparring`; no separate nonprod exists for this tool). A fresh anonymized X/Y assignment was set (Case A: X=baseline, Y=sparring; Case B: X=sparring, Y=baseline). The pre-reload rows are preserved at `reload-backup/rd_eval_cases.pre-plain-reload.json` for reversibility.

**§7 judge panel — re-run against the regenerated answers.** The prior judge results (`judging/judge-results.json`) scored the dense-pack answers and are invalidated by the regeneration; retaining them for the §8b judge-vs-human correlation would correlate judge scores of old answers against human scores of new answers. The 12 cross-vendor calls (Anthropic `claude-sonnet-4-6`, OpenAI `gpt-4o`, xAI `grok-3`; 2 cases × 3 judges × 2 position-passes) were re-run against the regenerated answers via `scripts/run-judges-plain.php` → `judging/judge-results-plain.json`. The judge **models** are unchanged from the locked panel; only the rated answers changed. Three `grok-3` rows mislabeled the second-line score prefixes (emitted `X…` where `Y…` was intended); all twelve values were present in emission order and were recovered by the documented positional-extraction fallback (the `recover-parse.php` method, applied at 6 criteria), deterministically and verified against the raw output; those rows are flagged `recovered_positionally` with the raw text preserved. 12/12 judge cells scored.

**Affected analysis steps**: All §8 analyses run against the regenerated materials and the re-run judge panel. The §4 rubric, the §8c two-tier gate, the §8g claim-scaling table, the §8h familiarity cuts, the §8i partial-completer per-case analysis, §9 hypotheses, and §10 stopping rule are unchanged in definition. No human rater data existed at any point in this amendment, so no analysis was informed by results.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "Before recruitment, the rater-facing decision materials were found to be written at an academic reading level inconsistent with the study's non-expert-judgment purpose and a potential source of construct-irrelevant variance. The decision packs were rewritten into plain language with every fact, citation, and magnitude preserved (verified by an independent fact-check), and gated by a plain-language reviewer. Because the condition outputs are stimulus generated from the packs and three rubric criteria are scored relative to the pack the rater reads, both conditions (single-agent baseline and the SPARRING ceremony) were regenerated from the plain packs rather than hand-edited; the format-symmetry of the two conditions was re-applied, and the cross-vendor LLM-judge panel was re-run against the regenerated answers. The generation substrate was substituted from Claude Opus 4.7 to Opus 4.8 under both conditions (preserving the single-shared-substrate property that prevents substrate from confounding the comparison). All of this was committed and tagged before any human rater data was collected, per Nosek et al. 2018; the production rating table was empty at reload and the loader refused to run otherwise."

**Tag**: `v2-prereg-amendment-2026-06-04-plain-language-rebuild` (to be applied to the amendment commit).

### Amendment 2026-06-06 — publication-credit preference captured as structured opt-out consent metadata

**Date**: 2026-06-06.
**Pre-rater-data**: YES — no V2 rater data had been collected at the time of this amendment. Recruitment has not opened (the rebuilt invitations and hook graphic were locked 2026-06-06 but not yet posted), so Day 0 of the recruitment window never began and `rd_eval_ratings` is empty on the production instrument. Committed before any rating content was inspected and before recruitment opened.

**Scope**: Rater-facing post-submission surface only (the framework-identity reveal panel of the rating tool). No §3 case, §4 rubric, §6 rater-pool/condition/familiarity, §7 judge-panel, §8 analysis-plan, §9 hypothesis, or §10 stopping-rule change. This amendment is logged for disclosure completeness; it is **analysis-neutral**.

**Rationale**: The recruitment invitations and the sign-up page promise each rater a choice of acknowledgment — "I'll thank you by name in the published write-up, or keep you anonymous — your call." Until this amendment that choice was handled informally (the sign-up page's email-field help text said "ask Bart"), with no structured capture and no in-product control; the post-submission reveal panel merely *stated* the policy ("you'll be acknowledged by name unless you asked Bart to keep you anonymous") rather than offering the choice. Publishing a real name is a consent decision that warrants an explicit, recorded, revocable control rather than an out-of-band request. The choice is captured **after both instruments are submitted and ratings are locked** — the same placement discipline already applied to the prior-familiarity covariate (2026-06-04) and the framework-identity reveal — so that the knowledge "my name will be attached to this" cannot induce evaluation-apprehension or social-desirability effects on the scores themselves. The default is **credit-by-name with opt-out to anonymous**, matching the acknowledgment promise already made in the published recruitment copy; a stronger anonymous-by-default posture was considered and rejected only because it would contradict copy already drafted for publication (the choice was the partner's, recorded here).

**What changed**: A `rd_eval_rater_credit` table (sparring-web migration `202`) records, once per rater (upsert, revisable before publication), a `credit_pref ENUM('by_name','anonymous') DEFAULT 'by_name'` plus an optional `credit_name` override for how the name should appear (NULL → use `users.display_name`). The post-submission reveal panel's passive acknowledgment sentence is replaced by an interactive opt-out control (checkbox pre-checked to by-name; an optional name field; a save action via `POST ?action=credit`). The absence of a row is semantically identical to `by_name`, so a rater who never touches the control is credited by name per the promise. This is consent/admin metadata only — it is recorded outside the analysis path and is a distinct axis from both `rater_condition` (how a rating was produced) and the familiarity covariate (what the rater knew going in).

**Affected analysis steps**: **None.** The credit preference never enters any §8 analysis; it governs only how a rater is named (or not) in the published acknowledgments. All §8 analyses, the §8c gate, the §8g claim-scaling table, the §8h familiarity cuts, the §8i partial-completer analysis, §9 hypotheses, and §10 stopping rule are unchanged.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "After each rater submitted both instruments and their ratings were locked, the rater was offered an explicit choice — recorded as revocable consent metadata — of being acknowledged by name in this write-up or remaining anonymous, defaulting to by-name acknowledgment per the recruitment invitation and opting out to anonymous. The choice was collected after submission, alongside the familiarity covariate and the framework-identity reveal, so it could not influence scoring; it does not enter any analysis. This provision was committed pre-rater-data per Nosek et al. 2018."

**Tag**: `v2-prereg-amendment-2026-06-06-publication-credit-preference` (to be applied to the amendment commit).

### Amendment 2026-06-07 — optional answer audio (uniform TTS narration) + digestion-modality covariate

**Date**: 2026-06-07.
**Pre-rater-data**: YES — verified immediately before the amendment commit: `rd_eval_ratings`, `rd_eval_rater_familiarity`, and `rd_eval_rater_credit` are all empty on the production instrument (`resourceforge.com/sparring`); recruitment has not opened. Committed before any rating content was inspected.

**Scope**: Rater-facing presentation layer (§3 stimulus *delivery*, not stimulus *content*) plus a new self-selected covariate (§6) and a new subordinate sensitivity analysis (§8j). No change to the answer text, the decision question, the evidence summary, the §4 rubric, the §2 conditions, the X/Y assignment, the §7 judge panel, the §8 primary analyses, the §8c gate, the §8g claim-scaling table, §9 hypotheses, or the §10 stopping rule.

**Rationale**: The prior instrument presented every stimulus as text only. That is itself a modality choice, not a neutral baseline: a growing share of how humans consume AI output is voice, and text-only delivery silently narrows the measured construct to "answer quality *when read*." To improve accessibility (raters with reading fatigue, dyslexia, or an audio preference) and ecological validity, each rater is offered an optional audio narration of the rater-facing content. The change is logged here because it touches the presentation of the scored stimuli and adds a covariate; the same amendment discipline applied to the familiarity covariate (2026-06-04) and the credit preference (2026-06-06) applies.

**Construct note (anti-overclaim)**: The answers are generated *as text*; the audio is a uniform third-party TTS narration of that fixed text. This is "text answers, optionally narrated," **not** native audio-generated AI (where the model itself makes prosody decisions). The preprint will not claim to have evaluated voice-delivered AI.

**Bias controls on the stimulus audio**:
- **One voice, identical settings, for every block** (question, evidence, Answer X, Answer Y, both cases). The audio is **server-side pre-generated** from the locked answer text with a single fixed voice/engine/rate — OpenAI `tts-1`, voice `fable`, speed `0.92` (recorded in the app's `openai_tts` config). Client-side `SpeechSynthesis` is *not* used for the stimuli because its per-device voice variance would make different raters hear different renderings of the scored content. (Client-side TTS is permitted only for the non-scored framing blocks — the page intro and the "How to approach this rating" instructions.)
- **Text remains fully co-present.** Audio is an optional overlay on the existing on-screen text, never a replacement and never an audio-only-by-default path; random-access pairwise comparison is preserved.
- **Pronunciation QA per answer** before lock, so engine mispronunciation of domain terms does not differentially degrade one answer.
- **Blind-safe serving**: audio is served under the public anonymized labels (`answer-x`, `answer-y`) from paths that never encode `answer_*_condition`; voice/settings are byte-identical across X and Y, so audio adds no condition-correlated signal beyond what the (already-visible) answer length conveys.

**What changed**:
1. An optional play control is added per rater-facing block on the rating page. Stimulus audio (question, evidence, Answer X, Answer Y) is pre-generated server-side with the single locked voice; framing blocks may use client-side TTS.
2. A `rd_eval_rater_modality` table (sparring-web migration `203`) records, **per rater per case** (composite key `user_id, case_id`; upsert, revisable before analysis), how the rater digested that case's two answers: `modality ENUM('read_only','audio_followed','audio_only','mixed')` plus an optional `notes` free-text (which captures per-answer asymmetry, e.g. "read X, listened to Y"). Absence of a row = modality-unknown (rater skipped the item, or rated a case before answering); there is no meaningful default.
3. The question is asked **post-submission**, in the same locked panel as the familiarity covariate and the framework-identity reveal, once per submitted case, so it cannot prime self-conscious rating. Single-case completers are asked only about the case they rated (consistent with the partial-completer handling). Reveal-order is safe: how a rater consumed already-locked answers cannot be biased by the post-lock framework-identity reveal.

**Self-selection caveat (scope of the covariate)**: Modality is rater-chosen, so it is confounded with rater type; it is recorded as a **disclosed covariate and robustness check**, not a manipulation. No causal claim of the form "audio delivery changes ratings" is made — that would require random modality assignment, which is deliberately not done (it would defeat the accessibility rationale of free choice).

**Affected analysis steps**: §8a–§8g (primary), the §8c gate, the §8g claim-scaling table, §8h (familiarity cuts), §8i (partial-completer per-case analysis), §9, and §10 are **unchanged** and run on all completers regardless of modality. One subordinate analysis is **added**:
- **§8j (new, secondary, descriptive + sensitivity)**: report the modality distribution per case; re-run the §8a–§8c completer analyses on the subset excluding `audio_only` raters (the only mode without co-present text, where pairwise-comparison degradation is plausible) as a robustness check. A material divergence between the full-sample and `audio_only`-excluded results is flagged; concordance is reported as robustness. Modality-unknown raters are excluded from §8j only (they remain in all primary analyses).

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "Before recruitment, the rating instrument was extended to offer each rater an optional audio narration of the rater-facing materials, in addition to the existing on-screen text, to improve accessibility and ecological validity (text-only presentation having silently restricted the measured construct to answer quality when read). The narration was a single fixed text-to-speech voice applied uniformly to all materials and both anonymized answers, served from the same blind endpoints; the on-screen text remained fully present, so this was an optional overlay rather than an alternative delivery, and the answer text (the experimental stimulus) was unchanged. After submission and locking, each rater reported, per case, how they had digested that case's answers (read only / audio while reading along / audio only / mixed), recorded as a self-selected covariate. Because modality was rater-chosen it is treated as a disclosed covariate and robustness check, not a manipulated factor: the pre-registered primary analyses are reported on all completers, and a subordinate sensitivity analysis additionally excludes audio-only raters. All of this was committed pre-rater-data per Nosek et al. 2018; the production rating table was empty at the time of the amendment."

**Tag**: `v2-prereg-amendment-2026-06-07-answer-audio-and-modality-covariate` (to be applied to the amendment commit).

**Voice substitution (2026-06-07, same-day, pre-rater-data).** The fixed narration voice named above is changed from OpenAI `tts-1` / `fable` / speed `0.92` to **`gpt-4o-mini-tts` / `cedar`**, delivered with a single fixed instruction (*"Speak in a calm, neutral, measured tone at a moderate pace."*) applied uniformly to every block and both answers. Rationale: `fable` reads with a British accent, an ecological-validity mismatch for the primarily North American rater pool; `gpt-4o-mini-tts` is higher quality and steerable, and `cedar` reads as neutral North American. The substitution is value-level (one uniform voice/engine, server-side pre-generated, text fully co-present, blind-safe endpoints) — the bias control and every other property of the amendment are unchanged, and no analysis step is affected. All ten tracks (8 stimulus + 2 framing) were regenerated and re-deployed; consistent with the amendment's "one voice for everything," the framing blocks are now narrated by the same server-side `cedar` voice rather than client-side `SpeechSynthesis`. Committed pre-rater-data (`rd_eval_ratings` empty at substitution) per Nosek et al. 2018. Tag: `v2-prereg-amendment-2026-06-07-voice-substitution-cedar`.

### Amendment 2026-06-08 — audio presentation parity: spoken block heading prepended to each narration track

**Date**: 2026-06-08.
**Pre-rater-data**: YES — to be verified immediately before the amendment commit (`rd_eval_ratings`, `rd_eval_rater_familiarity`, `rd_eval_rater_credit`, and `rd_eval_rater_modality` empty on the production instrument `resourceforge.com/sparring`; recruitment not opened). Committed before any rating content is inspected.

**Scope**: Subordinate to the 2026-06-07 answer-audio amendment; rater-facing presentation layer only (§3 stimulus *delivery*, not stimulus *content*). No change to the answer text, the decision question, the evidence summary, the §4 rubric, the §2 conditions, the X/Y assignment, the §7 judge panel, the §8 analyses (incl. the new §8j), §9 hypotheses, or the §10 stopping rule.

**Rationale**: As shipped, each narration track carried only the *body* of its block; the block's heading ("Decision question", "Evidence base summary", "Answer X", "Answer Y") was rendered on-screen but not spoken. This created a **modality asymmetry in the direction of the audio condition's disfavor**: a text rater sees which block they are reading, while an `audio_only` rater (the one mode without co-present text, isolated in the §8j sensitivity check) heard unannounced prose with no structural cue to which block was playing. Prepending the heading to each track restores parity — it gives the audio rater the same structural framing the text rater already has — and therefore **reduces** a presentation confound rather than introducing one.

**What changed**:
1. The stimulus-audio generator (`scripts/generate-stimulus-audio.php`) prepends each block's heading to its narration text as `"<Heading>. <body>"`. The spoken heading matches the on-screen wording in `blind-rating.php` **verbatim** ("Decision question", "Evidence base summary", "Answer X", "Answer Y") and is applied **uniformly** to every block and both cases. Regenerating the eight stimulus tracks is required; the framing tracks are unaffected (already self-contained).
2. (Non-stimulus, recorded for completeness — outside amendment scope.) The rating-page audio control was changed from stop/restart to true **pause/resume** (pausing retains position; resume rewinds ~1 s for re-orientation; switching tracks still starts from the top). This touches the player control only — no stimulus content and no measured variable — so it requires no amendment, but is logged here alongside the audio work for transparency.

**Blind safety**: The spoken labels "Answer X" / "Answer Y" are the same anonymized labels already visible on-screen and already served from the blind-safe `answer-x` / `answer-y` endpoints; speaking them encodes no condition signal and, if anything, reinforces the neutral framing. Voice/engine/instruction are unchanged from the 2026-06-07 cedar substitution.

**Affected analysis steps**: None. All §8 analyses (including §8j) run unchanged; the change improves the audio condition's comparability to text, which is the §8j robustness check's concern.

**Disclosure language for the V2 preprint** (locked at amendment commit):

> "Before recruitment, the optional audio narration was refined so that each block's on-screen heading (decision question, evidence summary, Answer X, Answer Y) was also spoken at the start of its track, matching the structural labelling a text reader already sees. This was a presentation-parity correction — the answer text (the experimental stimulus) was unchanged, the single fixed narration voice and blind-safe endpoints were unchanged, and the on-screen text remained fully present — addressing an asymmetry whereby audio-only raters, unlike text raters, received no cue to which block was playing. The change was committed pre-rater-data per Nosek et al. 2018; the production rating table was empty at the time of the amendment."

**Tag**: `v2-prereg-amendment-2026-06-08-audio-heading-parity` (to be applied to the amendment commit).

---

### Amendment 2026-06-12 — C5a re-scoped from open-world factuality to closed-world "Factual accuracy"

**Date**: 2026-06-12.
**Pre-rater-data**: YES — zero ratings had been collected on either V2 case (`rd_eval_ratings` empty; `x_c5a`/`y_c5a` unscored on both cases) at the time of amendment, verified against the production instrument `resourceforge.com/sparring`. No measurement-continuity break.

**Scope**: Rubric criterion C5a only. Re-scopes C5a from open-world ground-truth factuality to closed-world **Factual accuracy** — accuracy relative to the fact-checked decision pack. Renames the criterion label "Factuality" → "Factual accuracy." Demotes external verification from a scored expectation to an optional, declared covariate (the "External-source-checked" rater condition is unchanged). The criterion key (`c5a`) and the per-criterion score columns (`x_c5a`/`y_c5a`) are unchanged. No change to C1–C4, C5b, the §5 paired instrument, the §2 conditions, the §7 judge panel, the §8 analysis plan, the §9 hypotheses, or the §10 stopping rule.

**Rationale**: The original C5a created two problems. (1) It contradicted the rater instruction to treat the pack's facts as given: the §3 packs are independently fact-checked at lock (`v2-design.md` "Process changes") and presented to raters as a verified-pack view, yet C5a told raters to verify the underlying system against external sources. (2) It imposed a large per-rating friction cost — primary external fact-checking of cited literature/codebases — for a signal that is (a) already secured upstream by the pack fact-check, (b) only optionally realized at the rater level (external verification was opt-in), and (c) low-discrimination between conditions, since both conditions are the same substrate generating from the same verified pack. The open-world ambition was therefore largely unrealized at the rater level while carrying its full friction and scope cost. Re-scoping C5a to accuracy-against-the-pack removes both the friction and the instruction contradiction while **preserving a genuine split from C5b**: C5b measures *engagement* with the pack's load-bearing assertions; C5a measures *accuracy* in representing them (an answer can engage an assertion yet misstate it, or restate it accurately yet not grapple with it). The V1 §5.4 pack-fidelity-vs-ground-truth-fidelity gap remains closed — at the pack-construction layer (independent fact-check at lock) rather than at the rater layer.

**What changed**:
1. C5a label: "Factuality" → "Factual accuracy."
2. C5a description and 1–7 behavioral anchors rewritten as closed-world accuracy relative to the fact-checked pack (full text in `v2-design.md` §C5a and in the rater-app DB migration `205_rd_eval_recast_c5a_factual_accuracy.php`).
3. Rater instructions ("How to approach this rating"): the sentence "The rubric does **not** ask you to verify whether the pack itself accurately describes the underlying system" was removed; the pack is named as the ground-truth reference against which Factual accuracy is scored, with external spot-checks optional and declared in the rating condition.
4. Documentation synced for consistency: this pre-registration (§3, §4), `v2-design.md` (the §5.4 gap framing, the §C5a definition + anchors, the verified-pack-view paragraph, and the §Q4 gate list), and the C5a designer-note in both decision packs.
5. Judge instrument: the cross-vendor judge prompt (`scripts/run-judges.php`, `scripts/run-judges-plain.php`) C5a block was updated to the closed-world definition. The prior judge run (`judging/judge-results-plain.json`) scored the **open-world** C5a and is **superseded for C5a pending a judge re-run** (C1–C4 and C5b judge scores remain valid).
6. No change to the score schema, the paired instrument, or any §8 analysis computation other than the held-out C5a judge/rater alignment noted below.

**Affected analysis steps**: None of §8a–§8f change in computation. The C5a column is interpreted as closed-world Factual accuracy rather than open-world factual correctness. The two-tier gate (§8c) continues to treat C5a as a direct-inspection criterion; because C5a no longer depends on optional external verification, cross-rater comparability on this column is strengthened, not weakened. **Judge-side impact**: the cross-vendor judge panel (§7) had already scored the *open-world* C5a (stored in `judging/judge-results-plain.json`), so those C5a judge scores are now stale. The judge prompt has been updated to the closed-world C5a; a **judge re-run on C5a is required** before the §8b judge-vs-rater alignment on C5a can be computed, and that alignment is held out until then. C1–C4 and C5b judge scores are unaffected. Rater data remains zero, so this amendment is still pre-rater-data.

**Disclosure language for the V2 preprint** (locked at amendment commit):

> "Before recruitment, rubric criterion C5a was re-scoped from open-world factuality (does the recommendation contradict the external ground-truth state of the system, verified against external sources) to closed-world 'Factual accuracy' (is the recommendation accurate relative to the independently fact-checked decision pack). The change removed a contradiction with the rater instruction to treat the pack as given, and removed a per-rating external-verification burden that was optional and largely unrealized; the pack-fidelity-vs-ground-truth gap that motivated the original criterion is addressed at the pack-construction stage by the independent fact-check performed at case lock. External verification was retained as an optional, declared rater-condition covariate. The amendment was committed pre-rater-data per Nosek et al. 2018; the production rating table was empty at the time of the amendment."

**Tag**: `v2-prereg-amendment-2026-06-12-c5a-factual-accuracy` (to be applied to the amendment commit).

---

### Amendment 2026-06-12 (framework-identity blind — per-case title/pilot surfaces)

**Date**: 2026-06-12.
**Pre-rater-data**: YES — zero ratings collected, verified against the production instrument `resourceforge.com/sparring`.

**Scope**: Rater-facing per-case display copy only. Completes the 2026-06-04 framework-identity blind on two DB-sourced surfaces the original implementation missed. No change to §4 rubric, §7 judge panel, §8 analyses, §9 hypotheses, §10 stopping rule, or any stimulus content.

**Rationale**: The 2026-06-04 framework-identity blind was implemented on the page chrome (brand and page title now read the neutral "Resource Forge — AI Decision-Evaluation Pilot"), but two DB-sourced per-case surfaces still carried internal identifiers to raters pre-submission: (1) the case `title` began "Phase 1 V2 …" (internal pilot versioning — noise, though not the framework proper noun), and (2) the rendered "Pilot:" line displayed `pilot_slug` = `sparring-llm-judge-pilot-2026-05-03-v2`, i.e. the framework **proper noun**. The latter reopens the exact cue-leakage path the 2026-06-04 amendment closed: a recruit who reads "sparring" can search it, reach the public `muddyone/sparring-framework` repository whose `condition-{a-baseline,b-spar}/` directories label the X/Y assignment, and de-anonymize the blind. Same defect species, on a surface the original pass overlooked.

**What changed**:
1. Case titles: the "Phase 1 V2 " prefix was stripped (rater-app DB migration `206_rd_eval_neutralize_case_titles.sql`); "Case A/B —" retained as a non-identifying disambiguator. Titles now read "Case A — Organizational vocabulary…" / "Case B — Introductory programming…".
2. Pilot identifier: `blind-rating.php` now gates the `pilot_slug` display on viewer privilege (`PRIVILEGED_VIEW_ACTIVE` in the case header; `is_privileged_viewer` in the list). Privileged/admin viewers retain it; raters never see it pre-submission. The stored `pilot_slug`, internal code, file paths, and this pre-registration retain the SPARRING name, per the 2026-06-04 scoping.

**Known residual (disclosed, not yet remediated)**: the deployment URL still carries the proper noun — the path `resourceforge.com/sparring/…` and the case-slug query parameter `?case=sparring-llm-judge-…`. Neutralizing these is a heavier change (deploy docroot + a slug used as a DB/API key and in the judge scripts) and is deferred to an explicit decision; it is recorded here so the residual cue-leakage surface is disclosed rather than assumed away. The §8h familiarity-stratified sensitivity analysis remains the covariate-based backstop for residual exposure (including URL inspection).

**Affected analysis steps**: None. Display-copy and per-case-title concealment only; no measured variable, stimulus, or analysis step is touched.

**Tag**: `v2-prereg-amendment-2026-06-12-identity-blind-per-case-surfaces` (to be applied to the amendment commit).

---

### Amendment 2026-06-14 — cross-case comprehension-load covariate; human case-presentation-order counterbalancing; per-case dropout-by-position tally

**Date**: 2026-06-14.
**Pre-rater-data**: YES — to be verified immediately before the amendment commit (`rd_eval_ratings` empty on the production instrument `resourceforge.com/sparring`; recruitment not opened). Committed before any rating content is inspected.

**Scope**: §6 (rater pool — additive: human case-presentation order counterbalanced and recorded), §8 (new sub-section §8k — cross-case comprehension-load covariate; §8i extended with a per-case dropout-by-position tally), §10 (checkpoint clarification — case-order and per-case dropout tracked content-blind). No change to §2 conditions, §3 stimulus content, §4 rubric, §7 judge panel, §8c two-tier gate, §8g claim-scaling table, §9 hypotheses, or the §10 stopping rule.

**Rationale**: A self-applied SPARRING `/spar` ceremony on 2026-06-14 (reviewing whether Case B should survive for the non-expert pool) surfaced a between-case comparability threat the 2026-06-04 plain-language rebuild did not and could not address. The two cases are not matched on **integration load** — the number of distinct, competing, or caveated facts a rater must hold and reconcile to score the rubric:

- **Case A** (organizational vocabulary) asks for a single, undifferentiated recommendation over a mostly-concordant, single-population evidence base.
- **Case B** (programming curriculum) mandates five separate sub-population analyses (the 57% adult-learner / 31% first-generation / 20% second-language split, and the 38%-continue / 62%-don't split — `rater-fields-plain.md`), and forces the rater to hold a live theory-vs-population contradiction (cognitive load favors Path A while adult-motivation favors Path B), discount a finding for a failed replication (Hatfield 2019 / Lewis 2022), and weigh a moderator-gated effect size (the d≈0.18–0.22 transfer edge that applies only within an 18-month window). Case A contains none of these inference types.

This asymmetry is intrinsic to Case B *as a good hard case* and cannot be removed by a further plain-language pass without dropping facts (which the 2026-06-04 fidelity guarantee forbids). Its measurement consequence: a rater's score on the counterfactual-inference criteria (C3 missed real concerns, C4 calibrated confidence — the §8c lower-tier criteria) on Case B is partly a function of the rater's own working-memory load — construct-irrelevant variance that differs *between cases*. Because the §8c gate computes one ρ per criterion spanning both cases, and §8d/§8f pool explicitly "across cases," this between-case load difference is currently folded silently into the pooled statistics.

A second, related threat: there is no human case-presentation-order handling in the locked design (the only randomization is the within-case X/Y judge position-flip, §7). If Case B's higher load causes raters to abandon before completing it, the §8i partial-completer machinery retains the single-case (Case-A-only) rating and records the missing Case-B rating as an absent Krippendorff's-α cell — indistinguishable from benign non-completion. Load-driven differential dropout would thus be absorbed as benign missingness rather than surfaced.

The pre-registration's established posture for a known, unfixable-in-stimulus confound is to *measure and disclose* it (recruitment-channel selection bias, 2026-05-27; prior-familiarity, 2026-06-04; modality, 2026-06-07), not to assume it away. This amendment applies that posture to between-case comprehension load. It does not eliminate the asymmetry — it quarantines it, so a between-case divergence is reported as a load confound rather than silently pooled.

**What changed**:

**§6 — human case-presentation order counterbalanced and recorded (additive).** Each rater's first-seen case (A or B) is assigned by balanced randomization at sign-up, so the two presentation orders are approximately equally represented, and the assigned order is recorded per rater (mirroring how `rater_condition` is recorded). This breaks the order confound rather than merely measuring it, and makes the §8i by-position dropout tally interpretable. A sparring-web change is required to assign and persist the per-rater case order (a `case_order` field on the rater/eval record). The within-case X/Y assignment (§7 and the 2026-06-04 reload) is unchanged and independent of case order. The rater-condition declaration and the familiarity, credit, and modality covariates are unchanged.

**§8k — cross-case comprehension-load covariate (new, secondary).** Reported alongside and subordinate to the primary analyses:
- *Primary detector — per-case inter-rater divergence on the load-sensitive criteria.* Using the per-case Krippendorff's α already computed in §8i, the C3 and C4 per-case α for Case A and Case B are compared. A **material** between-case divergence — pre-specified as a per-case α gap **≥ 0.20** on either C3 or C4 between the two cases, **or** a between-case sign flip in the §8f direction-of-preference on C3 or C4 — is **reported as a comprehension-load confound** on the pooled §8c/§8d/§8f statistics for those criteria, not folded into them silently. Each per-case α is reported **with its per-case n**, so a divergence riding on a rater-count gap (small-n α instability) is visible rather than mistaken for a load effect.
- *Corroborating signal — per-case completion time.* Per-case completion time (a server-side timestamp delta) is reported as corroborating-only. It is explicitly *not* a primary detector, because per-case time is confounded by reading length (the Case B materials are longer), not integration load alone.
- *§8k is subject to the §8g claim-scaling floors.* At achieved per-case n below the relevant §8g threshold, the covariate is reported descriptively only, with per-case n stated; no §8k result upgrades the inferential weight permitted by the full-pool achieved n. The covariate measures and quarantines the confound; it does not remove it.

**§8i extended — per-case dropout-by-position tally (additive).** The §8i per-case surface additionally reports, for each case, how many raters completed that case only vs. both cases, broken down by presentation position (first-seen vs. second-seen, per the new §6 case-order record). A Case-B-heavy single-case-completion asymmetry — especially concentrated in the second-seen position — is reported as candidate comprehension-driven attrition rather than absorbed as benign missingness.

**§10 — checkpoint clarification.** The per-rater case-presentation order and the per-case / by-position completion counts are tracked for recruitment monitoring; like the existing completer counts they are inspected content-blind (no rating content examined). The stopping rule and its blinding (Wagenmakers et al. 2012) are unchanged.

**Measurement caveats (disclosed)**:
- The covariate detects divergence; at this pilot's calibration-check sample sizes (§8g) it is underpowered, so a true between-case load effect may fail to clear the flag at small n. This is the same n-limitation §8g/§11 already disclose for every analysis; §8k surfaces divergence when present, it does not guarantee detection.
- Completion time confounds load with reading length; hence α-divergence on C3/C4 is the primary detector and time is corroborating-only.
- Per-case α confounds load with per-case sample size; hence each α is reported with its per-case n.

**Affected analysis steps**: §8a–§8j are unchanged in computation. §8k overlays a between-case comparison on the per-case α already produced by §8i and adds per-case completion-time reporting; §8i additionally reports a per-case / by-position dropout tally. The §8c gate, §8g claim-scaling table, §9 hypotheses, and §10 stopping rule are unchanged. No human rater data exists at the time of this amendment, so no analysis is informed by results.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "Before recruitment, a self-applied review of the two decision cases identified that they were not matched on the cognitive integration load a rater must carry to score them: one case required reasoning over multiple sub-populations, a within-evidence contradiction, a failed replication, and a moderator-gated effect size, while the other required a single recommendation over a mostly-concordant evidence base. This between-case load asymmetry is intrinsic to the harder case and could not be removed without altering its evidence; it was therefore pre-registered as a measured covariate rather than edited away. The per-case inter-rater reliability already computed in the secondary per-case analysis is compared between cases on the two counterfactual-inference criteria, with each estimate reported alongside its per-case sample size; a material between-case divergence is reported as a comprehension-load confound on the pooled gate statistics rather than silently absorbed, and per-case completion time is reported as a corroborating-only signal (it is confounded with reading length). Because the design carried no human case-presentation-order control, case-presentation order was counterbalanced (each rater's first-seen case balanced-randomized and recorded), and per-case completion was additionally tallied by presentation position so that load-driven differential dropout — otherwise indistinguishable from benign non-completion in the incomplete-matrix reliability estimate — is surfaced rather than absorbed. All provisions were committed pre-rater-data per Nosek et al. 2018; the production rating table was empty at the time of the amendment."

**Addendum (2026-06-14, pre-data) — completion-time corroborating signal dropped.** On implementing the §8k analysis code, `rd_eval_ratings` was found to carry no server-side start timestamp, and the save-and-return instrument makes an open→submit wall-clock dominated by away-time — an uninformative reading-effort proxy. Rather than ship a misleading metric or build active-time instrumentation for a signal §8k already scoped as corroborating-only, the per-case completion-time component of §8k is **withdrawn**. The §8k primary detector — between-case per-case Krippendorff's α on C3/C4 (the 0.20-gap rule / §8f sign-flip) — and the §8i by-position dropout tally are unaffected and remain the comprehension-load surface. Pre-rater-data (`rd_eval_ratings` empty). Analysis code: `pilots/llm-judge-2026-05-02/v2/scripts/analyze-v2.php` (Krippendorff α validated against canonical published values; ships with a `--self-test`).

**Tag**: `v2-prereg-amendment-2026-06-14-cross-case-load-covariate` (to be applied to the amendment commit).

---

### Amendment 2026-06-14 (clarity pass) — rater-facing condensed fields made stakes-legible for both cases

**Date**: 2026-06-14 (second amendment of this date; companion to the cross-case load-covariate amendment above).
**Pre-rater-data**: YES — to be verified immediately before the amendment commit (`rd_eval_ratings` empty on the production instrument `resourceforge.com/sparring`; recruitment not opened). Committed before any rating content is inspected.

**Scope**: The rater-facing **condensed fields only** — the per-case `question` and `evidence_summary` rendered to raters from `rd_eval_cases` (`research/blind-rating.php`), for both Case A and Case B. No change to the full decision packs (`decision-packs/case-{a,b}-*.plain.md`), the §2 condition answers, the §4 rubric, the §7 judge panel, the §8 analysis plan (including the new §8k), the §9 hypotheses, or the §10 stopping rule.

**Rationale**: The 2026-06-04 plain-language rebuild lowered the *vocabulary* reading level of the rater-facing materials but left their *significance* opaque: a rater could read "about 73% finish (the department worries about anything under 75%)" or "Cohen's d ≈ 0.18" and parse every word without being able to feel why the fact mattered to the decision. A fact a reader can pronounce but cannot weigh is a residual access barrier and a residual measurement confound of exactly the species the 2026-06-04 amendment named — a rater who cannot place a fact's weight scores partly on that struggle rather than on the answer's quality (construct-irrelevant variance). The gap was surfaced by the self-applied SPARRING `/spar` of 2026-06-14 and by the project's communications-reviewer (Rosetta) stakes-legibility standard adopted the same day. Lowering this barrier is, as in 2026-06-04, both an access and a measurement improvement. The pass was applied to **both** cases deliberately: making only the more-technical Case B stakes-legible while leaving Case A denser would introduce a between-case *clarity* asymmetry — the same family of cross-case comparability threat addressed by the companion load-covariate amendment.

**What changed**:

**§3 rater-facing condensed fields — rewritten for stakes legibility; facts preserved.** The Case B `question` (the completion-rate clause) and the `evidence_summary` of both cases were rewritten so each load-bearing fact carries a felt "why this matters for the decision," statistics carry their plain magnitude *and* its decision-consequence, and weight-changing caveats lead. Every fact, number, range, effect size, citation, and replication caveat is preserved verbatim in meaning (Pfeffer 1–3 points; *Toussaint*; SHRM 71/22/4/3%; the 43-of-46 non-anonymous survey 12/67/21%; Sweller 1998; Bennedsen & Caspersen 65–78% / 58–85%; Knowles 1980; Hatfield ~12pp with the Lewis 2022 non-replication; Smith & Garcia / Park d≈0.18–0.22, 3–4 points, 18-month moderator; the NCCC 64→73% history). An **independent fact-check pass** and a **Rosetta stakes-legibility gate** were run on the rewrite; together they caught and removed several over-reaches in the first draft before commit — an attribution error in the "what drives completion" item (ordering vs. preparation/language), an unsupported grade-boundary claim ("nudge a grade, not flip a pass"), a tilt clause on the NCCC history, a fabricated social-desirability inference on the staff survey, and two rubric-telegraphing labels ("the catch first," "treat this carefully"). The "what this case is testing" meta remains excluded so the rubric is never telegraphed to raters.

**No regeneration required (distinguishing this from the 2026-06-04 rebuild).** The rater reads the condensed `rd_eval_cases` fields (`research/blind-rating.php` renders `question` + `evidence_summary`); the condition answers were generated from the **full** plain packs, which are unchanged. Because no fact, number, or magnitude was altered, the C1/C5a/C5b criteria scored relative to the materials the rater reads retain their reference; the answers and the §7 judge scores are untouched. The 2026-06-04 rebuild required regenerating both conditions and re-running the judge panel because it changed the packs the answers are generated *from*; this pass changes only the condensed summaries the rater reads, so neither regeneration nor a judge re-run is triggered.

**Files**: `rater-fields-plain.md` (the canonical condensed fields). Deploy into the live `rd_eval_cases` is a pending operational step (loaded before recruitment opens).

**Affected analysis steps**: None. This amendment changes only the presentation of the rater-facing decision question and evidence summary; no condition answer, rubric criterion, judge score, gate, claim-scaling threshold, hypothesis, or analysis step is altered. No human rater data exists at the time of this amendment.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "Before recruitment, the rater-facing condensed decision materials (the per-case decision question and evidence summary shown to raters) were revised a second time, following the earlier plain-language rebuild, to make the significance of each load-bearing fact legible to a non-expert — every fact retained, but each number paired with what it means for the decision and each weight-changing caveat placed first — on the rationale that a fact a reader can read but cannot weigh is both an access barrier and a source of construct-irrelevant variance. Every fact, citation, and magnitude was preserved (verified by an independent fact-check and gated by the project's plain-language reviewer, which removed several first-draft over-reaches that had introduced unsupported consequences or directional framing). The pass was applied to both cases to avoid introducing a between-case clarity asymmetry. Because raters read these condensed summaries while the condition answers were generated from the unchanged full packs, no condition output and no judge score was affected, and no regeneration was required; the change was committed pre-rater-data per Nosek et al. 2018 with the production rating table empty."

**Tag**: `v2-prereg-amendment-2026-06-14-stakes-legibility-clarity-pass` (to be applied to the amendment commit).

---

### Amendment 2026-06-14 (deferred simultaneous un-blinding + rating-edit freeze at study close)

**Date**: 2026-06-14 (third amendment of this date).
**Pre-rater-data**: YES — to be verified immediately before the amendment commit (`rd_eval_ratings` empty on the production instrument `resourceforge.com/sparring`; recruitment not opened). Committed before any rating content is inspected.

**Scope**: §10 (Stopping rule and protocol-amendment policy) — the reveal-timing and dataset-freeze are made explicit. §5 / §6 — the rater-facing reveal sequence and the recruitment-referral surface. The instrument copy and write-path that implement them (`research/blind-rating.php`; `src/api/research/eval.php`). No change to §2 conditions, §3 cases, §4 rubric, §7 judge panel, §8 analysis plan, or §9 hypotheses.

**Rationale**: The deployed V2 instrument lifted the framework-identity blind **per rater, the moment that rater finished both cases** — naming SPARRING and linking the public repository where the per-case X/Y → condition mapping is recorded. Two defects follow from per-rater-immediate reveal:

1. **It contradicts the §10 stopping-decision blinding.** §10 (2026-05-27 amendment) commits BN to inspecting only the *completer count*, never rating content, until recruitment closes — to keep the stopping decision uncontaminated by results (Wagenmakers et al. 2012). But un-blinding early completers while the pool is still recruiting reintroduces the same contamination through the participants: an un-blinded rater who discusses or posts which answer "won" can prime later recruits, and the directional signal leaks back into the open pool the blinding was meant to protect.
2. **It left an editable rating on the wrong side of the blind.** The edit path (`?action=edit`) never checked study or case state, so a rating remained revisable *after* the rater had been shown the framework identity and could look up the X/Y mapping. An edit made with knowledge of which answer is SPARRING is no longer a blind rating — a direct confound, not a hypothetical one.

The fix couples the two: **defer the reveal to a single simultaneous un-blinding at recruitment close, and freeze rating edits at that same moment.** Because every edit then necessarily occurs *before* any rater is un-blinded, editing is blind-by-construction — no separate editing-window timer is required, and the failure mode of a fixed timer (a returning rater stranded one hour past a 24-hour cutoff, unable to fix a data-entry slip) is avoided. The prior-familiarity covariate (§5, 2026-06-04 amendment) is **unaffected**: it is collected at completion, still strictly before any un-blinding, which is exactly where it must sit to be valid.

**What changed**:

**§10 reveal timing and dataset freeze — made explicit.** The framework-identity reveal (which answer X/Y was SPARRING per case, plus the repository link) is withheld from every rater until the study's collection phase ends. On completing both cases a rater records the prior-familiarity covariate as before, then sees a **"ratings locked — reveal at study close"** acknowledgment in place of the identity reveal. When recruitment closes under the §10 recruitment-window rule (hard stop at n ≥ 15, the checkpoint cascade, or the absolute close at day 28 / 2026-06-24), the study is moved to a **`closed`** phase in a single deliberate action keyed off the completer count only (preserving stopping-decision blinding). That one action simultaneously (a) **freezes the dataset** — `submit` and `edit` are rejected server-side thereafter, so the analyzed ratings are final — and (b) **unlocks the identity reveal for all raters at once**. Until `closed`, ratings remain editable (the legitimate "I mis-clicked a score" correction is preserved); after `closed`, they are immutable. This supersedes the per-rater-on-completion reveal and the previously-unbounded edit window. The §10 stopping rule, recruitment window, checkpoints, claim-scaling table (§8g), and stopping-decision blinding are otherwise unchanged.

**§6 recruitment referral — clarified, blind-preserving.** Sharing the public **sign-up link** is in-protocol and already contemplated by the §6 open-convenience-sample design (recruitment via public LinkedIn/Facebook posts); a rater-facing "invite a colleague" affordance that surfaces only the sign-up URL reveals nothing about the study and is permitted during collection. **Result-sharing by raters is gated to after the simultaneous reveal** (post-close) — no in-app affordance lets a rater broadcast the un-blinding while the pool is open. If referral is instrumented, recruitment-source is recorded; the resulting referral-chain clustering is disclosed as a deepening of the already-disclosed selection-channel limitation (§6, 2026-05-27 disclosure language), not a new claim.

**§13(3) named-rater briefing — timing follows the reveal.** The 2026-06-04 provision that any introduction to *what the framework is* happens "alongside the post-submission reveal" is read, under this amendment, as "alongside the post-**close** simultaneous reveal." Pre-submission briefing remains limited to how the rating tool and rubric work.

**Mechanism (implementation, not protocol)**: a per-pilot collection phase (`collecting` → `closed`) stored in `rd_eval_study_state` (migration 209), flipped once at recruitment close by `scripts/close-study.php` (a logged, deliberate CLI action — not an admin web button, to remove any accidental-early-reveal surface). The list endpoint derives a `reveal_unlocked` flag from it; `submit`/`edit` reject writes once `closed`. Default-locked / default-final-safe on uncertainty: a missing phase row leaves the reveal withheld.

**Files**: `research/blind-rating.php` (deferred-reveal sequence, "ratings locked" acknowledgment, blind-preserving invite, post-close result-share, familiarity-prompt copy no longer promising an immediate reveal); `src/api/research/eval.php` (`reveal_unlocked` in the list payload; study-closed write-gate on `submit`/`edit`); `database/migrations/209_rd_eval_study_state.php`; `scripts/close-study.php`. The instruction copy line "you don't know which came from which condition until after you submit" is corrected to "until the study closes."

**Affected analysis steps**: None computationally. No condition answer, rubric criterion, judge score, gate, claim-scaling threshold, hypothesis, or analysis step is altered. The amendment changes *when* the rater is un-blinded and *until when* a rating is editable — both tightened toward the blind — and the dataset handed to §8 is the post-close frozen set, as §10 already intended. No human rater data exists at the time of this amendment.

**Disclosure language for the V2 preprint** (locked at amendment commit so it cannot be reverse-engineered from results):

> "The V2 instrument originally lifted the rater-facing framework-identity blind per rater, immediately upon each rater completing both cases, and left submitted ratings editable thereafter. Before any rater data was collected, the protocol was amended so that the identity reveal is deferred to a single simultaneous un-blinding at the close of recruitment, and rating edits are frozen at that same point; every rating is therefore both produced and revised entirely under blind, and the analyzed dataset is the frozen post-close set. The change aligned the rater-facing reveal with the study's existing stopping-decision blinding (which already withheld rating content from the recruitment-stopping decision), closing a path by which an early-un-blinded participant could have leaked directional signal into the still-open pool. The prior-familiarity covariate continued to be recorded at completion, before any un-blinding. The amendment was committed pre-rater-data per Nosek et al. 2018 with the production rating table empty."

**Tag**: `v2-prereg-amendment-2026-06-14-deferred-simultaneous-reveal` (to be applied to the amendment commit).

---

## 13. Logistical follow-ups (must complete before V2 compute begins)

These are operational tasks, not design decisions. They are tracked in [`v2-design.md`](./v2-design.md) "Logistical follow-ups." Summary:

1. Provision External rater E1 with rating-tool access (`[redacted-email]`).
2. Brief External rater E4 on the V2 rating methodology.
3. Brief External rater E1 similarly. NOTE (per the 2026-06-04 amendment): the framework-identity blind applies to named raters too — any high-level introduction to *what the framework is* must happen **after** her submission, alongside the post-submission reveal, not before. Pre-submission briefing is limited to how the rating tool and rubric work.
4. Run the V2 schema migration on nonprod and prod.
5. Deploy the rating-tool form/API updates to support the V2 schema.
6. Run V2 conditions against the two decision packs and load the outputs into `rd_eval_cases` (anonymized X/Y assignment).

Once 1-6 are complete, raters can begin V2 ratings. The four raters ideally rate within the same calendar week to minimize time-of-rating drift, though this is a soft target rather than a pre-registered constraint.

---

## 14. Acknowledgments and references

V2 inherits V1's reference list (preprint §9). New V2-specific external references locked at this pre-reg:

- **Cox, E.P. (1980)**. "The Optimal Number of Response Alternatives for a Scale: A Review." *Journal of Marketing Research* 17(4), 407-422. *Justifies 1-7 scale choice over 1-5 or 1-10.*
- **Krippendorff, K. (2004)**. *Content Analysis: An Introduction to Its Methodology*, 2nd ed. Sage. §11 on rubric construction. *Justifies the C5a/C5b split over a combined C5; supports the rater-pool n ≥ 3 minimum for inter-rater reliability.*
- **Liang, P., et al. (2023)**. "Holistic Evaluation of Language Models (HELM)." *arXiv*:2211.09110. *Source for faithfulness vs. factuality split convention.*
- **Es, S., James, J., Espinosa-Anke, L., & Schockaert, S. (2023)**. "RAGAS: Automated Evaluation of Retrieval Augmented Generation." *arXiv*:2309.15217. *Source for engagement-with-source dimension construction.*
- **Schulz, K.F., & Grimes, D.A. (2002)**. "Blinding in randomised trials: hiding who got what." *Lancet* 359(9307), 696-700. *Source for the CONSORT-aligned default reading of "blind" as blind-AND-unaided absent explicit permission.*
- **Calderon, N., Reichart, R., & Dror, R. (2025)**. "The Alternative Annotator Test for LLM-as-a-Judge." *ACL 2025*. *Source for the rater-pool n ≥ 3 minimum and within-condition cross-rater statistics discipline.*

---

**End of pre-registration. Ready to lock.**
