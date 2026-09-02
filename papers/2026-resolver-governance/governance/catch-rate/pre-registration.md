# Catch-rate pilot A-v3 — the producer's-own-blind-spot test (Test B) — pre-registration

**Pilot id:** `sparring-catchrate-v3-2026-06-28`
**Status:** **LOCKED 2026-06-28.** Design choices are the assistant's recommendations, accepted under Bart's standing delegation. Tag (on lock-commit): `catchrate-v3-prereg-2026-06-28`.
**Supersedes the paradigm of** Study A (`../catch-rate-2026-06-28/`), which measured **Test A** (catch a flaw someone *else* planted) and saturated. This measures **Test B** — SPARRING's actual mechanism.

---

## 1. Why (what Study A taught us)

Study A, the seeded-defect study, and v3 all asked **Test A**: *"can a reviewer catch a flaw someone else planted in a given artifact?"* A competent model does this trivially → saturation. That is **not** what SPARRING does. SPARRING's mechanism is **Test B**: an agent **produces** a recommendation (the single-pass workflow you actually use) and embeds **its own blind spots**; those flaws **ship** unless a **Challenger** — fresh eyes, different angle/evidence — catches them. *You don't catch the bug you just wrote; a Challenger does.* The §6 mechanism audit shows this happening for real, **model-level, no human** (the Challenger caught fail-open auth / lockout-DoS the Generator shipped). A-v3 reproduces that in a controlled, scalable way.

## 2. The question

> On genuinely hard problems, when an agent **produces** a recommendation and embeds its **own** blind-spot flaws, what fraction of those flaws does a **Challenger** catch — versus the producer's **own self-review**, and versus **produce-and-ship** (no review)?

## 3. Design

- **Problems (~8):** genuinely hard, open-ended, realistic decision problems (system design, analysis, strategy) with competing constraints, edge cases, and second-order effects — the conditions under which a strong producer **naturally** embeds flaws. **Not** pre-flawed artifacts; **not** recognizable textbook traps. (If the audit finds **no** real flaws in the produced recommendations, that is itself a finding — a strong producer ships clean work on hard problems — and the study reports it honestly rather than manufacturing flaws.)
- **Step 1 — Produce (the artifact under test):** a Generator produces a recommendation **R** per problem, in normal produce-mode (no "be careful," no adversarial prompt). R is what a single-pass user would receive and ship. R's flaws are **emergent and unknown a priori.**
- **Step 2 — Three catch conditions on R (each blind to the others):**
  - **SELF** — the *same* Generator reviews **its own** R ("review your recommendation, note concerns"). Tests the blind spot.
  - **NEUTRAL** — a *fresh* agent neutrally reviews R. Isolates "fresh eyes" from "adversarial framing."
  - **CHAL** — a *fresh* agent, adversarially framed and told to work from a different angle/evidence, attacks R (SPARRING's Challenger).
- **Step 3 — Ground-truth audit:** an **independent panel** (3 agents, blind to Steps 2) each enumerate the **material** flaws in R (would change the decision or ship a real defect — not nitpicks); reconcile into one authoritative **flaw set** per R (a flaw counts if ≥2 of 3 auditors raise it). This is the denominator.
- **Step 4 — Blind catch-coding:** for each audited flaw × condition, code CAUGHT/MISSED (does that condition's review surface that specific flaw), blind to condition.

## 4. Hypotheses (directional pilot — no inferential stats)

- **Headline (SPARRING vs produce-and-ship):** of the real flaws in R (which produce-and-ship would ship), the **Challenger catches Z%.** A high Z quantifies the lived value — SPARRING catches would-ship flaws — **model-level.**
- **H1 (primary, the asymmetry):** **CHAL catch-rate > SELF catch-rate.** The producer misses its own blind spots; a Challenger catches them.
- **H2 (decomposition):** CHAL vs NEUTRAL (does adversarial + different-evidence beat plain fresh review?) and NEUTRAL vs SELF (does fresh-eyes-alone beat self-review?).
- **Pre-committed null:** if **CHAL ≈ SELF**, the producer catches its own flaws as well as a Challenger → on these problems SPARRING's *separate-agent* mechanism adds little model-level (the value would then be "having any critique step at all," consistent with v3's S≈skeptic). §6 already shows the effect is real, so a null here more likely indicts problem difficulty than the mechanism — reported honestly either way.

## 5. Measurement integrity

- The audit is **blind** to the SELF/NEUTRAL/CHAL reviews and defines ground truth independently; SELF/NEUTRAL/CHAL are blind to each other and to the audit.
- The audit being a strong model in critique-mode is expected — it sets the denominator. The **load-bearing comparison is SELF vs CHAL** (both critique the same R), which isolates produce-mode self-blindness vs. fresh-adversarial-eyes.
- Catch-coding is blind to condition.

## 6. Limitations (pre-stated)

- **Single-vendor:** Claude produces, reviews, challenges, and audits. The within-model SELF-vs-CHAL *process* contrast is the cleanest part; cross-vendor generation/audit is future work.
- **Difficulty-dependent:** the effect can only appear if the producer actually ships flaws; a clean audit (no flaws) is a real, reportable outcome, not a failure to engineer around.
- **Audit defines "material flaw"** by a pre-set bar (decision-changing / real defect), ≥2-of-3 panel agreement.
- Directional, small n, no significance tests.

## 7. What it can / cannot claim

- **Can:** whether SPARRING's Challenger catches a producer's *own* blind-spot flaws that self-review and produce-and-ship miss — model-level, no human (a controlled analogue of §6).
- **Cannot:** ecological practitioner value (still the human-in-loop process study); a powered effect size; cross-vendor generality.

### Sign-off — accepted (assistant recommendation, delegated 2026-06-28)
- [x] Test B (produce → SELF/NEUTRAL/CHAL → independent audit), not Test A
- [x] Headline = Challenger's catch-rate of would-ship flaws; H1 = CHAL > SELF; H2 decomposition; null reading stated
- [x] Blind audit (≥2/3 panel) + blind catch-coding; SELF-vs-CHAL is the load-bearing contrast
- [x] → **lock + tag** `catchrate-v3-prereg-2026-06-28`

## 8. Deviation ledger (post-lock)
_None yet._
