> **⚠ SUPERSEDED by [`pre-registration-v2.md`](./pre-registration-v2.md) (2026-06-26).** This v1 binary-catch design was retired after both proofs showed catch-rate ceilings (deviation D6). v1 is kept for provenance — its deviation ledger D1–D6 is the trail that produced v2. Do not run v1.

# Seeded-Defect Pilot — pre-registration (LOCKED · v1 · superseded)

**Pilot id**: `sparring-seeded-defect-pilot-2026-06`
**Status**: **LOCKED 2026-06-26** (partner sign-off, Bart Niedner). Tag: `seeded-defect-prereg-2026-06-26`. Design frozen below before any case generated. Any change after this point is a disclosed deviation in §10.
**Execution**: pipeline proven on 2–3 cases first (partner instruction); final-run mechanics = reproducible script harness (default), pending API-access confirmation (§9).
**Relationship to V2**: the V2 blind output-preference study (`pilots/llm-judge-2026-05-02/v2/`) returned a pre-registered null and, on analysis, was **confounded by design** — its rubric was ~5/6 process-quality but the format-symmetric blind stripped the very process evidence those criteria needed (see V2 preprint §5.1–5.3). This pilot tests the *reframed* question with **ground truth by construction**.

---

## 1. The question

V2 could not see process value because it judged finished outputs. This pilot relocates the dependent variable from the **output** to the **process trace**, and supplies ground truth by *planting* defects we know are there:

> When an opening recommendation contains a **known, externally-checkable defect**, does a **grounded, cross-vendor Challenger** catch it more often than (a) the single opening pass alone and (b) a **placebo Challenger** that performs disagreement without the artifact-grounding discipline?

The placebo contrast is the load-bearing one. It is the operational form of "real or theater": if a fluent-but-ungrounded Challenger catches planted defects as often as a grounded one, the grounding is theater. **SPARRING can lose this test**, and a null here is a reportable result, not a failure to hide.

## 2. Hypotheses (exploratory pilot — directional, not powered)

At n=20 we pre-commit the measures and analysis but report **directions and rough magnitudes**, not inferential significance. We will say so plainly.

- **H1 (vs. baseline):** grounded cross-vendor Challenger catch-rate **>** single-pass self-catch-rate.
- **H2 (the theater test, primary):** grounded Challenger catch-rate **>** placebo Challenger catch-rate.
- **H3 (specificity / not-catch-by-flagging-everything):** grounded Challenger's **false-positive (theater-flag) rate** is **not worse** than placebo's — i.e., it discriminates, it doesn't just raise more alarms.

Pre-committed null reading: if grounded ≈ placebo on H2, we conclude the artifact-grounding adds no detection value over performed disagreement **in this synthetic regime**, and report it.

## 3. Design

**4 defect categories × 5 cases = 20 decision cases.** Each case = a realistic decision scenario + a fact-checked decision pack + an **opening pass** ("Generator" output) containing **exactly one** planted defect of the case's category, embedded naturally (never labeled or telegraphed). One defect per case keeps catch-attribution clean.

### Defect categories (each has ground truth checkable OUTSIDE the LLM loop)

| Code | Category | Planted defect | External ground truth |
|---|---|---|---|
| **DC1** | Fabricated/misapplied citation | opening cites a non-existent source, or misapplies a real one to a claim it does not support | Crossref / DOI / arXiv resolution via **`/cite-check`** |
| **DC2** | Pack contradiction | opening contradicts or distorts a load-bearing fact in the fact-checked pack | the pack itself (the answer key) |
| **DC3** | Security / CWE | opening recommends a design carrying a real, named weakness (e.g. fail-open auth, lockout DoS — anchored to the real corpus's loom cases) | mapped **CWE id** + reasoning, human-audited |
| **DC4** | Overclaim / false capability | opening asserts a capability or fact exceeding a written ground-truth spec | the spec document (the answer key) |

Defect *realism* is anchored to the real mechanism-audit corpus taxonomy (`docs/spars/mechanism-audit-2026-06-26/`) — fail-open, overclaim, fabricated/misapplied citation, pack contradiction were all observed there. This anchoring is what keeps synthetic defects from being toy/telegraphed.

### Conditions (run per case)

| Code | Condition | Description |
|---|---|---|
| **B** | Single pass (baseline) | the opening pass alone — does the model self-flag its own planted defect? |
| **S** | Grounded cross-vendor Challenger | opening from model A; Challenger on **model B**, under SPARRING's **verifiable-artifact discipline** (a concern only counts if it points at a checkable artifact) |
| **T** | Placebo Challenger (theater control) | Challenger on model B, prompted to critique/disagree but **without** the artifact-grounding requirement — free to raise concerns on assertion alone |

**Stretch arm (run only if budget allows): `S2` grounded *same-vendor* Challenger** (opening A, Challenger also A, grounded) — isolates the cross-vendor-independence factor Bart flagged (two different LLMs are unlikely to co-hallucinate the same fiction). Not part of the core 60-run pilot.

Core pilot = 20 cases × 3 conditions = **60 runs** + judging.

## 4. Outcome measures

- **Primary — defect-catch (binary, per case × condition):** did the condition's output explicitly surface *the specific planted defect*? Adjudicated by a **blind catch-judge** (blind to which condition produced the text) against the verbatim answer-key defect, requiring a supporting quote. Objective form: "does this output identify THIS defect," not "is this output better."
- **Secondary — theater / false-positive rate:** count of substantive concerns raised that are **not** the planted defect and are **not** genuine (ungrounded or wrong). Separates "caught by reasoning" from "flagged everything." For S, also record whether each raised concern was artifact-backed.
- **Tertiary — load-bearing:** did the catch change the converged recommendation (same bar as the corpus audit).

## 5. Catch-judgment protocol (the validity core)

1. **Answer key recorded at injection time** — the exact planted defect, its category, and (DC1) the citation, (DC2/DC4) the contradicted pack/spec line, (DC3) the CWE id — stored before any condition runs.
2. **Blind model catch-judge** — given output + answer-key defect → {caught: yes/no, quote}. Blind to condition.
3. **Externality check, per category:** DC1 → `/cite-check` confirms the citation is actually fabricated/misapplied (not judge opinion); DC2/DC4 → the pack/spec is the referent; DC3 → human confirms the CWE.
4. **Human spot-audit ≥ 25%** of catch-judgments (Bart or a second substrate); report agreement. If model–human agreement is poor, the pilot's catch numbers are downgraded to that ceiling.

## 6. Anti-circularity & validity threats (pre-stated, not smoothed over)

- **"LLMs all the way down."** Mitigations: external ground-truth sources (Crossref, CWE list, pack, spec) rather than pure LLM invention; **different model families** for opening-generation vs. the Challenger conditions vs. the catch-judge where feasible; human spot-audit.
- **Toy/telegraphed defects.** Realism anchored to the observed corpus taxonomy; defects embedded naturally and never labeled; review pass to reject any case where the defect is self-evident from phrasing.
- **Leakage.** Single defect per case; the Challenger/judge prompts never reveal defect location; blind grading.
- **Construct limit.** This measures **detection of known defects**, not **real-world decision improvement** — that is the later ecological human study. Kept separate on purpose.
- **n=20.** Directional pilot. We report case counts and per-category breakdowns; no significance claims.

## 7. What it can and cannot claim

- **Can:** whether a grounded cross-vendor Challenger detects planted, externally-verifiable defects more than performed disagreement and more than a single pass — with ground truth, a placebo control, and a blind+human-audited judge.
- **Cannot:** estimate real-world catch rates, prove decision improvement in the wild, or generalize beyond the synthetic defect taxonomy. Feeds the current paper's §7 as a **first positive (or null) signal from the right instrument**, not a confirmatory result.

## 8. Analysis (pre-committed)

Report, per condition: overall catch-rate (n/20), per-category catch-rate (n/5 each), theater/false-positive rate, load-bearing rate. Headline contrasts: **S vs T** (H2, the theater test) and **S vs B** (H1). Descriptive proportions + case-level table; no inferential test at this n. Publish the answer-key, all 60 outputs, and both judging passes as artifacts.

## 9. Open execution decision (not part of the locked design)

The 60-run fan-out + judging is naturally a multi-agent orchestration. Two options, decided after sign-off:
- **Reproducible script harness** (like `analyze-v2-primary.php`) calling the API — most arXiv-defensible (deterministic, version-controlled, re-runnable). Needs API access from the harness.
- **Workflow orchestration** (fan-out over cases × conditions) — faster to stand up, requires explicit opt-in.

---

### Sign-off checklist (Bart) — signed 2026-06-26
- [x] Defect taxonomy + external ground-truth sources acceptable
- [x] Conditions (B / S / T; S2 stretch) acceptable
- [x] Catch-judgment + human-spot-audit protocol acceptable
- [x] Pre-committed null reading (grounded ≈ placebo ⇒ report it) acceptable
- [x] Execution: **prove pipeline on 2–3 cases first**; final-run harness TBD pending API-access check
- [x] → **locked + tagged**; pipeline proof in progress

## 10. Deviation ledger (post-lock)

All entries below are **pre-data**: only the hand-authored *pipeline proof* (`pipeline-proof/`) has run — an explicit mechanics test, not study data — and no full-run cases have been generated. Triggered by the proof's ceiling-effect finding (`pipeline-proof/proof-report.md`).

- **D1 — Harden the defects (2026-06-26, pre-data).** Binary catch saturated 9/9 in the proof because each defect contradicted a *headline* pack fact. Full-run defects will be harder to miss-by-a-single-pass: prefer **misapplied real citations** (real DOI, claim it doesn't support) over fabricated ones; contradict a **buried, non-headline** pack fact requiring multi-step inference; embed in **longer packs with plausible-but-fine distractor content**.
- **D2 — Primary measure shifted off binary catch (2026-06-26, pre-data).** Binary defect-catch ceilings out with capable models, so it is demoted to a **recall secondary**. New primary contrast: **grounding quality / verifiable-artifact rate** and **false-positive (theater) rate** — does S catch *with checkable grounding and few false alarms* while T catches *on suspicion and over-flags*. (The blind judge already discriminated S-vs-placebo on grounding quality in the proof.)
- **D3 — Baseline headroom (2026-06-26, pre-data).** B is redefined as a genuine single pass **without** an adversarial self-critique affordance, so S/T have measurable headroom to beat.
- **D4 — S condition = a real `/spar` ceremony (2026-06-26, pre-data).** The proof's S was a hand-rolled single "grounded reviewer," which under-represents SPARRING (no dual-grounded evidence bases, no iteration, no convergence gate). The full run's S is an actual `/spar` run; T remains an ungrounded devil's-advocate. If the artifact-verification integration (see `docs/plans/sparring-artifact-verification-spec.md`) lands first, S runs **with verification on** — which is the manipulation that operationalizes D2.
- **D5 — Gating change: hardened mini-proof before scale (2026-06-26, pre-data).** Do **not** generate the 20-case corpus or build the cross-vendor VPS harness until a hardened mini-proof (2–3 cases, D1–D4 applied) demonstrates the conditions actually separate. If they don't, that bounded result is itself reportable.
- **D6 — Hardened mini-proof verdict: binary catch is dead; pivot to justification quality (2026-06-26, pre-data).** The hardened mini-proof (`pipeline-proof-hardened/`) returned **12/12 catch again** — defect-hardening designed for *human* missability (burial, misapplication, absent-control) does not make a full-context frontier model miss. Verdict: **binary catch is dropped as a primary** (saturated descriptive only). Conditions separated **only on grounding quality (S ≫ T) and false-positive/precision** — confirming D2. Consequences: (a) the pilot's sole primary becomes **grounding-quality + precision/false-positive**; (b) the artifact-verification spec (`docs/plans/sparring-artifact-verification-spec.md`) moves **onto the critical path** — it makes that measure objective and penalizes over-flagging; (c) before scaling, test a **weaker/cross-vendor baseline B** (the one place catch-rate headroom might still exist). **Do not scale to 20 until the pilot is redesigned around the grounding/precision primary and the verifier exists.**
