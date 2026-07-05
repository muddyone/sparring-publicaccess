# v2 seeded-defect run — results

**Date**: 2026-06-26 · **Design**: `../pre-registration-v2.md` (locked, tag `seeded-defect-prereg-v2-2026-06-26`). **Run**: workflow `wf_8f451f23-e00`, 72 agents. **Corpus**: 12 LLM-generated cases, external-artifact-weighted (4 DC3 security/CWE · 3 DC1 misapplied/fabricated citations · 3 DC4 overclaim-vs-spec · 2 DC2 buried contradiction), one seeded anchor each (`cases.json`). **Conditions**: B (neutral single pass) · S (dual-grounded ceremony = S-Gen ∪ S-Chal) · T (placebo). **Coding**: blind per-concern (condition-hidden, rotated), legitimacy + grounding (`codings.json`). **236 concerns coded.**

> **In plain terms:** across 12 flawed recommendations, every condition caught the problems — but SPARRING backed **98%** of its concerns with checkable receipts vs the placebo's **61%** (the placebo ran ~40% on hunches), and it did so **without raising more false alarms** than a plain reviewer. The gap is biggest on security and citation claims — exactly where checking requires knowledge beyond the documents in front of you.

## Aggregate (all 12 cases, 236 concerns)

| Condition | concerns | **Grounding rate** | **Verified-grounded-TP** | **Precision** | Theater rate |
|---|---|---|---|---|---|
| **S** (ceremony) | 93 | **97.8%** | **95.7%** | 95.7% | **2.2%** |
| **B** (neutral pass) | 54 | 87.0% | 85.2% | **96.3%** | 13.0% |
| **T** (placebo) | 89 | 60.7% | 60.7% | 92.1% | 39.3% |

## By defect category — the separation is on EXTERNAL-canon artifacts

| Category (artifact location) | Grounding: B / S / T |
|---|---|
| **DC3 security/CWE** (external: CWE registry) | 68.4% / **96.2%** / **36.4%** |
| **DC1 citations** (external: literature) | 92.9% / 96.4% / **57.1%** |
| DC4 overclaim-vs-spec (spec in pack) | 100% / 100% / 80.0% |
| DC2 buried contradiction (in pack) | 100% / 100% / 93.3% |

When the checkable artifact lives **inside the pack** (DC2, DC4), even the placebo grounds well — no separation. The grounding advantage concentrates where verification requires reaching **outside** the provided materials — DC3 (CWE) most dramatically (S 96% vs T 36%, a 60-point gap), DC1 (citations) next. This is the governance/explainability sweet spot.

## Verdict against the pre-registered hypotheses

- **H1 (theater test — grounding S > T): strongly supported.** 97.8% vs 60.7%. The placebo catches real problems but ~40% of its concerns are ungroundable assertions; SPARRING's are 98% receipts. **The pre-committed null (S ≈ T ⇒ grounding is theater) is rejected.**
- **H2 (auditability composite — verified-grounded-TP S > B and S > T): supported.** 95.7% vs 85.2% (B) vs 60.7% (T).
- **H3 (precision cost): the feared cost did NOT materialize.** S precision 95.7% ≈ B 96.3% (both > T 92.1%). The over-flagging seen in the hardened mini-proof washed out at scale — SPARRING is as precise as a plain reviewer **and** far better grounded. This is the cleanest finding: grounding without a precision penalty.

## Caveats (bounding the claim — read before quoting)

1. **Grounding here is Path-B blind coding, NOT the objective verifier.** P1.5-live needs API keys this host lacks, so grounding was adjudicated by blind same-substrate (Claude) coders, as in Phase 0. The P1 verifier independently confirms *resolution* on the CWE/citation artifacts but was not run in-loop. **The headline grounding numbers are knowledgeable-coder judgments, not machine-verified, and human audit is pending.** A Path-A confirmation run (keys/VPS) is the next step.
2. **Same-vendor.** Reviewers and coders are all Claude. The weaker/cross-vendor baseline B is untested.
3. **S is two agents** (93 concerns vs B's 54) — ~2× cost. Rates normalize for count; the cost asymmetry is real.
4. **Cases LLM-generated** (fresh, neutral — avoids hand-authoring bias) but generated and coded by the same model family. Answer keys are strong and specific (real CWEs: CWE-347 alg-confusion, CWE-760 predictable salt, CWE-384 session fixation, CWE-434; real misapplied citations: Bloom two-sigma, Miller 7±2, Schmidt & Hunter 1998).
5. **n = 236 concerns / 12 cases.** Directional pilot; no inferential significance claimed.
6. **Reproducibility note — workflow aggregation bug.** The in-script aggregator used label keys `R1..R4` while the coder emitted `Review-1..4`, zeroing the in-run summary. Re-aggregated offline from the saved `codings.json` (the numbers above); the per-concern codings themselves are unaffected.

## Bottom line

The v2 measure delivers a clean, honest, directional result that **strongly supports SPARRING's auditability value and rejects the theater-null**: grounded dual-evidence SPARRING produces verifiably-backed critiques (98%) where a fluent placebo runs ~40% on assertion — concentrated exactly on external-canon claims (security, citations) — **at no precision cost**. This is the first positive signal from the *right* instrument, and the candidate result for the preprint's §7. Confirmatory next step: a Path-A (verifier-backed) re-run with keys + a human audit of the coding.
