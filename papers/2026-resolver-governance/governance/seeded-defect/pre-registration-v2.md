# Seeded-Defect Pilot — pre-registration **v2** (grounding-quality + precision redesign) — LOCKED

**Pilot id**: `sparring-seeded-defect-pilot-2026-06` (v2)
**Status**: **LOCKED 2026-06-26** (partner sign-off, Bart Niedner). Tag: `seeded-defect-prereg-v2-2026-06-26`. Design frozen before any new case is generated.
**Execution**: **Path B (interim dual-substrate grounding judge)** for adjudication; **Phase 0 first** — re-code the existing 12 hardened-proof outputs under the per-concern scheme to confirm the measure separates before any new generation. Phase-0 result decides whether Path A's verifier build is front-loaded.
**Supersedes**: [`pre-registration.md`](./pre-registration.md) (v1, the binary-catch design). v1 stays in the repo for provenance; its deviation ledger D1–D6 is the trail that produced this redesign.

---

## 1. Why v2 (one paragraph)

v1 asked "does SPARRING catch defects a single pass misses?" Both proofs answered the same way: **binary catch ceilings at ~100% across every condition** (9/9, then 12/12 even on hardened defects — `pipeline-proof-hardened/proof-report.md`, deviation D6). A full-context frontier model catches a single planted defect regardless of condition, so catch-rate cannot discriminate. But the conditions **did** separate on two other axes the proofs surfaced: *how well-grounded* each critique was (real SPARRING cited checkable artifacts; the placebo caught on intuition) and *how precise* it was (the adversarial conditions over-flagged). **v2 retires catch-rate as the primary and measures those two axes directly.** The claim under test shifts from "catches more" to **"produces more verifiable, higher-precision critiques"** — the auditability/explainability value, which is also where the V2 preprint reframe and the mechanism audit point.

## 2. The question

> When reviewing a flawed recommendation, does a **grounded, dual-evidence SPARRING ceremony** produce critiques that are (a) more **verifiably grounded** and (b) at least as **precise** as a single neutral pass and a placebo challenger that performs disagreement without grounding?

The S-vs-T contrast remains the "real or theater" test, now measured on grounding rather than catch: if a fluent ungrounded placebo grounds its concerns as well as SPARRING, the artifact discipline is theater. **SPARRING can lose this.**

## 3. Unit of analysis (the core change)

v1's unit was the case ("was the planted defect caught?" — binary, saturating). **v2's unit is the individual concern.** Every condition, on every case, emits a critique = a set of concerns. *Each concern* is independently coded on two axes:

- **Legitimacy** — `TRUE_POSITIVE` (a real problem with the recommendation or pack) | `FALSE_POSITIVE` (over-reach: not a real problem, contradicts what the pack states, or re-flags a control the pack says is present). Adjudicated against the case + pack + (for the seeded anchor) the answer key.
- **Grounding** — `GROUNDED_VERIFIED` (cites a checkable artifact that resolves *and* supports the concern) | `GROUNDED_REFUTED` (cites an artifact that does not support it / misuses it) | `UNGROUNDED` (no checkable artifact — assertion/intuition).

This per-concern scheme does not saturate: it has hundreds of data points even at proof scale, and it captures both the value (verified, real concerns) and the cost (over-flagging, ungrounded assertions).

## 4. Primary & secondary measures (per condition, aggregated over all concerns)

- **Grounding rate** = `GROUNDED_VERIFIED` / all concerns. *(primary — the theater test)*
- **Verified-grounded-TP rate** = (`TRUE_POSITIVE` ∧ `GROUNDED_VERIFIED`) / all concerns — the ideal concern: a real problem, checkably backed. *(primary — the composite auditability score)*
- **Precision** = `TRUE_POSITIVE` / all concerns raised. *(primary-cost — does grounding come at a false-positive cost?)*
- **Theater rate** = (`UNGROUNDED` ∨ `GROUNDED_REFUTED`) / all concerns — concerns you can't trust on their face. *(secondary)*
- **Seeded-anchor recall** = did the condition surface the one seeded defect (expected ≈100%). *(retired to saturated descriptive — kept only to show the ceiling, not a primary)*

## 5. Hypotheses (exploratory pilot — directional, not powered)

- **H1 (theater test, primary):** grounding rate **S > T**. The artifact discipline produces checkably-backed concerns where the placebo produces correct-but-ungroundable ones.
- **H2 (auditability composite, primary):** verified-grounded-TP rate **S > B** and **S > T**.
- **H3 (precision cost, honest):** precision **S vs B vs T** — pre-committed to report whichever way it falls. The hardened proof suggests S over-flags; if precision(S) < precision(B), that documented cost is part of the finding, not buried.
- **Pre-committed null:** if grounding rate **S ≈ T**, the artifact discipline adds nothing over performed disagreement → reported plainly.

## 6. Design

- **~12 cases** (proof-of-concept), across domains, each with **one seeded anchor defect** (a known `TRUE_POSITIVE` so precision denominators and a grounding-check target are guaranteed). Defect *hardness* no longer matters for the primary (catch ceilings regardless), so anchors are moderate and realistic, embedded in fact-checked packs.
- **Conditions** (unchanged contrast, new scoring):
  - **B** — bare single neutral pass (no adversary, no grounding rule).
  - **S** — real `/spar` ceremony: two agents, *genuinely different evidence bases*, artifact discipline (a concern counts only if it cites a checkable artifact), iterate, converge.
  - **T** — placebo: structurally similar disagreement (skeptical critique) **without** the artifact discipline or distinct evidence bases.
  - **(secondary, optional) B-weak** — a weaker / cross-vendor single pass, the one place catch-rate headroom might still exist (D6). Not part of the core grounding/precision contrast.

## 7. Grounding adjudication — and the verifier dependency

Grounding rate is only *objective* if each cited artifact is actually checked. Two paths:

- **Path A (preferred): artifact-verifier-backed.** Build verifier P1–P2 (`docs/plans/sparring-artifact-verification-spec.md`) first; route each concern's artifact to its backend (literature → `/cite-check`; code/CWE/standard → resolver; pack/data → cross-check). `GROUNDED_VERIFIED`/`GROUNDED_REFUTED`/`UNGROUNDED` is then a machine read, not an opinion. This is why D6 put the verifier on the critical path.
- **Path B (interim): blind dual-substrate grounding judge + ≥25% human audit.** Two independent model substrates code each concern's grounding; disagreements surfaced; Bart audits ≥25%. Clearly labeled "judge-based, pending verifier" in any write-up.

Legitimacy (TP/FP) is always adjudicated against the case + pack + answer key, blind to condition, with the same ≥25% human audit.

## 8. Phasing (cheap first, scale last)

- **Phase 0 (free — do first):** re-code the **existing 12 hardened-proof outputs** (`pipeline-proof-hardened/`) under §3's per-concern scheme. No new generation. Confirms the new measure actually separates S from T before spending anything. (The hardened proof's blind judge already hinted it does — it flagged the placebo's ungrounded catch.)
- **Phase 1:** if Phase 0 separates, build verifier P1 (Path A) or stand up the interim judge (Path B).
- **Phase 2:** generate the ~12-case corpus, run B/S/T, code per-concern, analyze §4.

## 9. Validity threats (pre-stated)

- **Circularity** → grounding verified against external truth (Crossref/CWE/the pack); legitimacy against the answer key; different substrates; human audit.
- **Judge subjectivity on grounding** → Path A removes it; Path B mitigates with dual-substrate + audit and labels the dependency.
- **Blind coding** → adjudicators never see which condition produced a concern.
- **Same-vendor ceiling** → all-Claude agents may inflate baseline competence; the optional B-weak arm probes it. Stated, not assumed away.
- **n** → proof-of-concept; per-concern gives many data points but few cases — directional, no inferential significance claimed.

## 10. What it can / cannot claim

- **Can:** whether grounded dual-evidence SPARRING yields more verifiably-grounded and (at least as) precise critiques than a single pass and a placebo — with external ground truth, blind + human-audited coding.
- **Cannot:** a catch-rate superiority claim (explicitly retired), real-world decision improvement (the later ecological study), or generalization beyond the synthetic taxonomy.

---

### Sign-off checklist (Bart) — signed 2026-06-26
- [x] Per-concern unit + the two coding axes (legitimacy, grounding) acceptable
- [x] Primary measures (grounding rate, verified-grounded-TP rate, precision) acceptable
- [x] Adjudication: **Path B (interim dual-substrate judge)**; promote to Path A (verifier) if Phase 0 warrants
- [x] Pre-committed null (S ≈ T grounding ⇒ report it) acceptable
- [x] Start with Phase 0 (re-code existing hardened outputs) before any new generation
- [x] → **locked + tagged** `seeded-defect-prereg-v2-2026-06-26`; Phase 0 in progress

## 11. Deviation ledger (v2, post-lock)

_None yet. Departures from the frozen v2 design are recorded here with date + rationale._
