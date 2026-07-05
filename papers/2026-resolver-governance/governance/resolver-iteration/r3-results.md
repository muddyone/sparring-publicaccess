# R3 — admissions-controlled iterate · RESULTS (EXPLORATORY)

**Status:** `EXPLORATORY PILOT — NOT PRE-REGISTERED.` n = 8 problems × 2 vendor arms. Directional
signal only; **no confirmatory claim**, **firewalled from Paper 1**. See
[`R3-design-spec-EXPLORATORY.md`](./R3-design-spec-EXPLORATORY.md) for the pre-specified reads.

**Date:** 2026-06-29 · Harness: `scripts/run_study.py` (R3 condition) → `scripts/analyze.py`
→ `analysis/results-aggregate-r3.json` + `analysis/r3-governance-trail.json`.

---

## Headline: R3 cleared the single-pass floor — first condition in the study to do so

Mean net material flaws remaining (lower better; denominator mean = 3.875):

| Condition | mean net | vs floor |
|---|---|---|
| R0 (anchor) | 3.875 | — |
| R1.same (single pass) | 2.625 | the floor |
| R1.cross | 3.125 | the floor |
| R2.same / R2.cross (the gate) | 2.625 / 3.0 | ≈ floor (the locked null) |
| **R1′ (best locked: self-revise ×2)** | **2.25** | best prior |
| **R3.same** | **1.75** | **−0.875 vs R1, −0.50 vs R1′** |
| **R3.cross** | **1.125** | **−2.00 vs R1, −1.125 vs R1′** |

**Pre-specified reads (both met):**
1. *"Clears the floor"* iff mean R3 < mean R1 in **both** arms → **YES** (1.75 < 2.625; 1.125 < 3.125).
2. *"Real win"* iff mean R3 < 2.25 (below R1′, the best locked condition) in both arms → **YES**
   (1.75 and 1.125 both < 2.25).

Nothing in the locked study beat the single-pass floor. R3 does, in both arms — exactly the
brainstorm §2.1 bet (gate the *fix*, not just the answer; only commit Pareto-improving patches).

## But the win is uneven — read the per-problem record, not just the means

Paired per-problem contrasts (the honest n=8 view):

| contrast | mean_diff | R3 fewer | other fewer | ties |
|---|---|---|---|---|
| R3 vs R1.same | −0.875 | 5 | 1 | 2 |
| R3 vs R1.cross | −2.000 | 6 | 0 | 2 |
| R3 vs R1′ (same) | −0.500 | 4 | 2 | 2 |
| R3 vs R1′ (cross) | −1.125 | 4 | 2 | 2 |

Against the **weak** baselines (R1/R2) R3 wins cleanly. Against the **strongest** control (R1′,
self-revision) the edge is real but modest: R3 wins 4/8, ties 2, **loses 2**. The headline means
are pulled down hard by the cross arm; don't over-read them on n=8.

### The one regression (the severity-relative bar's price, made concrete)
**warehouse-siting.same: net 5 vs R0's 4 — R3 made it worse.** It resolved 3 of 4 original flaws
but the gate admitted patches that introduced **4 new** material flaws (each "less severe" than what
it fixed, so admissible) which the independent DV panel counts as material; they accumulated past
the original count. This is exactly the §4.3 caveat: the severity-relative bar is lenient against
lower-severity regressions, and on a hard problem they can stack. 1 of 16 ceremonies went backwards.

## Mechanism: the gate inverts R2's round dynamics (this is the interesting part)

Net flaws by terminal state:

| terminal | n | mean net | meaning |
|---|---|---|---|
| CAPPED | 7 | **0.286** | gate kept finding admissible improving patches every round → ran out of rounds *while still improving* |
| CONVERGED | 5 | 1.8 | challenger ran out of objections |
| EXHAUSTED | 4 | 3.0 | no admissible improving move remained → honest early stop on hard problems |

In the **locked R2 study the order was reversed** — CONVERGED was cleanest (1.25), CAPPED dirtiest
(3.33), because more rounds meant more churn. In R3 the gate filters churn, so **more rounds *help***:
the cleanest ceremonies are the ones that ran the full 5 and kept admitting Pareto-improving patches.
Two implications:
- The **round cap is now truncating productive improvement** (CAPPED would likely go lower with more
  rounds) — opposite of R2, where the cap was mercy.
- **EXHAUSTED is the gate working, not failing** — it refuses to commit churny non-improvements and
  stops, so hard problems stay dirty (3.0) rather than degrade further. R3's wins concentrate on
  problems where progress was *possible*; on stuck problems it stops early and stays where it was.

## Governance trail (pre-specified question 2): PASS

`analysis/r3-governance-trail.json`: **53 patches admitted, 8 rejected, every reject records its
blocking new flaw + severity.** Every committed change traces to ≥2 cross-vendor admit votes with a
recorded resolved-set. The verifier-attested accept/reject log is legible and complete — the
governance product the brainstorm §4.2 argued for, emitted as a byproduct of the same gate that
improved the answer.

## Honest bottom line

Both halves the spec hoped for landed: R3 beats the single-pass floor on net flaws (the decision-
quality bet) **and** emits a clean verifier-attested trail (the governance bet) — from one mechanism.
But this is n=8, exploratory, and qualified by: (a) a modest edge over the *strongest* control with
2 losses incl. 1 outright regression; (b) a cross/same divergence that *reversed* the locked study's
direction (R3.cross best here, R1/R2.cross were worst there) — surprising, possibly noise; (c) the
cap now truncating gains. These are exactly what a confirmatory ~16-problem pre-registration on
fresh problems should settle — and what the severity-relative bar (vs a stricter or
consensus-thresholded bar) should be tuned against, given the warehouse-siting regression.

**This result does not enter Paper 1.** It is the basis for the Paper 1.5 pre-registration decision.
