# Resolver-iteration study — pre-registration

**Pilot id:** `sparring-resolver-iteration-2026-06-29`
**Status:** **LOCKED 2026-06-29.** Design choices are the assistant's recommendations, settled 2026-06-29 and accepted under Bart's standing delegation (same delegation basis as `catchrate-v3-prereg-2026-06-28`). Tag (on lock-commit): `resolver-iteration-prereg-2026-06-29`.
**Supersedes** the design-draft `DESIGN.md` in this directory (kept for provenance; this file is the integrity spine).
**Completes** the Resolver paper (`../llm-judge-2026-05-02/v2/preprint-draft.md`, §10.2 / §11 item 8): §6.3 establishes the value of a **single** adversarial challenge; this study isolates the **both-must-agree gate that iterates to a revised, agreed output** — the §2 distinctive niche.

---

## 1. The question

> Does making the challenger and the proposer **go back and forth — revising, re-challenging, until both agree** — produce a **better final answer** (fewer material would-ship flaws remaining) than a single challenge-and-fix?

§6.3 measured *flaws flagged* on a fixed recommendation with **no revision step**. That DV (a) ceilings (single pass already catches 27/31 = 87%) and (b) misses the gate's point: its value is in the **revised output**, not in flagging. This study needs a different DV and a revision step §6.3 never had.

## 2. Conditions (each produces a final deliverable scored identically; same producer, same problems)

| Condition | What runs | Final output scored |
|---|---|---|
| **R0 — ship as-is** | producer's original recommendation, no review | the original (definitional anchor: all panel-confirmed flaws remain) |
| **R1 — single challenge + one revision** | one challenger pass; producer revises **once** | the once-revised recommendation |
| **R2 — iterate to agreement (the gate)** | challenger ↔ producer back-and-forth, producer revising each round, until **both agree**, **stall**, or hard cap (terminal states, §6) | the output at stop |
| **R1′ — effort-matched control** | producer revises a second time **on its own**, no adversarial round (matches R2's extra passes without the gate) | the twice-revised recommendation |

**Contrasts:**
- **R1 vs R0** — value of a single challenge-and-fix (floor; the "does the Resolver do anything" check, now on a fixed-output DV).
- **R2 vs R1** — **the load-bearing contrast**: marginal value of *iterating to agreement* beyond one challenge.
- **R2 vs R1′** — isolates *adversarial* iteration from "just more revising" (compute/effort confound; parallel to §7.2's realistic-skeptic placebo).

**R1′ is vendor-independent** (no challenger) and is computed once per problem, shared across both vendor arms. R0 is the reused §6.3 original. The producer is Claude in all conditions.

## 3. Dependent variable — net material would-ship flaws remaining (lower is better)

- **Denominator (fixed before any condition runs):** reuse §6.3's `consensus-flaws.json` — the **≥2-of-3 audit-panel** material-flaw set for the *original* recommendation. (31 flaws across the 8 problems.) This is fixed; conditions are scored against it.
- **Remaining:** for each condition's final output, blind-code which panel-confirmed flaws **still remain** (REMAIN / RESOLVED), blind to condition.
- **New flaws (net accounting):** the audit panel **re-runs** (3 auditors, ≥2-of-3) on each final output; any ≥2-consensus material flaw **not semantically present in the original denominator set** counts as a **new flaw introduced by revision**. A revision that fixes two and adds one is not a two-flaw win.
- **DV = net flaws remaining = (panel-confirmed flaws still REMAIN) + (new ≥2-consensus material flaws introduced).**
- **Secondary:** core-decision-change across iteration (decision-change rate); rounds to convergence; terminal-state distribution (§6).

## 4. Hypotheses (directional pilot — no inferential stats unless data support it)

- **H1 (floor):** R1 leaves fewer net flaws than R0.
- **H2 (load-bearing):** R2 leaves fewer net flaws than R1 — iterating to agreement beats one challenge.
- **H3 (anti-confound):** R2 leaves fewer net flaws than R1′ — the gain is the *adversarial* iteration, not just extra revising.
- **Pre-committed null, reported either way:** if R2 ≈ R1 (and/or R2 ≈ R1′), iterating-to-agreement adds little beyond a single challenge — **reported as a finding, not buried.** This is the Resolver paper being honest about its own headline mechanism.

## 5. Sample, models, vendor arms

- **Problems — reuse §6.3's 8** (`../catch-rate-v3-2026-06-28/problems.json`) and their panel-confirmed flaw sets. Selection-bias caveat carried over verbatim (problems authored to a difficulty bar, not sampled); the within-problem contrasts (R2 vs R1, R2 vs R1′) are robust to it because selection falls equally on both conditions.
- **n / power — 8 problems, paired within-problem.** Directional, matching the paper's first-signal posture; **no significance claim unless the data support it.** Pre-registered **expansion trigger: extend to ~16 problems if the R2-vs-R1 effect is small or noisy.**
- **Producer (all conditions):** Claude `claude-opus-4-8`. *(Original R0 was produced by §6.3's Claude run; the exact §6.3 model id was not recorded — logged in the deviation ledger as a documented seam. Revisions use `claude-opus-4-8`.)*
- **Audit panel (net-flaw accounting, both arms):** 3 Claude `claude-opus-4-8` auditors at distinct temperatures, ≥2-of-3 consensus — matching §6.3's panel construction so the new-flaw bar is the same instrument that built the denominator. Cross-vendor-panel robustness is carried over from §6.3 (§6.3's grid showed vendor alignment worth only ~2–5 points); not re-run here (scope control, logged).
- **Blind coder (remaining-coding):** Claude `claude-opus-4-8`, condition-blind, label-stripped, order-rotated.
- **Vendor arms — both in the first run:**
  - **Same-vendor:** Claude produces, **Claude (`claude-opus-4-8`) challenges** — comparability with §6.3.
  - **Cross-vendor:** Claude produces, **GPT (`gpt-5.2`) challenges** — the sharpest gate test, since same-vendor agents are the likeliest to fake-agree via shared training, and the gate's rationale is resisting exactly that coordinated agreement.

## 6. Terminal states + qualified stall-stop (operationalized for the harness)

A ceremony ends in exactly one of three pre-registered states. The final output is scored at the stop **regardless** of state; flaws-remaining is **reported broken down by terminal state**.

- **CONVERGED — both agree.** Each round the challenger emits a structured signal: `material_objections_remaining: true|false` + the list of still-open panel-flaws it is pressing. After the producer's revision, if the challenger returns `material_objections_remaining: false` **and** the producer returns `accept_as_final: true`, the ceremony is CONVERGED. Minimum 1 completed round.
- **STALLED — genuine deadlock (mechanical, tied to the flaw set).** "Movement" is **per-flaw disposition**, not text similarity. A round shows **no movement** iff: (a) the producer's revision changes its handling of **no** still-open panel-confirmed flaw (disposition addressed→not-addressed unchanged for every open flaw), **and** (b) the challenger raises **no** flaw not already on the table. **STALLED** if **2 consecutive rounds** show no movement. Minimum 2 rounds before STALLED can fire.
- **CAPPED — hard cap = 5 rounds** reached without CONVERGED or STALLED. The backstop above the stall rule.
- **Oscillation** (positions cycling A↔B across rounds) is **logged as a secondary signal but does not gate in v1.**

**Convergence-gaming watch (the teeth):** *CONVERGED-with-flaws-remaining* is the fake-agreement signature; *STALLED-with-flaws-remaining* is honest deadlock — same flaw count, different failure. We test whether **early CONVERGED correlates with *more* flaws remaining**; if it does, the gate is failing at its own job — itself a finding, and a direct test of the §2 niche claim. The **cross-vendor arm** is where this bites hardest.

## 7. Honesty controls

1. **Pre-register first** (this file), locked + tagged before any data. ✔
2. **Blind, order-rotated coding** — the remaining-coder never sees which condition produced an output; condition labels stripped, outputs shuffled.
3. **New-flaw accounting** (§3) — guards against overcrediting iteration.
4. **Effort-matched control R1′** — separates structure from sheer compute.
5. **Three terminal states + qualified stall-stop** (§6) — separates fake agreement from genuine deadlock.
6. **Cross-vendor arm** — the sharpest test of fake-agreement; run, not deferred.
7. **Cross-vendor caveat** — ceremony agents in the same-vendor arm share a vendor family; flagged, and the cross-vendor arm is the remedy.

## 8. Analysis plan (pre-committed)

- **Primary table:** mean net flaws remaining per condition (R0/R1/R2/R1′) × arm (same-vendor / cross-vendor), with per-problem values. Lower is better.
- **Load-bearing contrast:** within-problem paired difference **R2 − R1** (and **R2 − R1′**), per arm. Report the paired differences and their direction; report a sign test / Wilcoxon only as descriptive support, **no significance claim unless n and effect support it** (expansion trigger otherwise).
- **Terminal-state breakdown:** net flaws remaining split by CONVERGED / STALLED / CAPPED; round-count distribution; decision-change rate.
- **Convergence-gaming test:** correlation between (rounds-to-CONVERGED, early-convergence flag) and net flaws remaining, per arm.
- **Report-either-way commitment:** the pre-committed null (§4) is reported as a finding if it obtains.

## 9. What it can / cannot claim

- **Can:** whether iterating-to-agreement (the gate) yields a final output with fewer net material flaws than a single challenge-and-fix or effort-matched self-revision — model-level, on these 8 purpose-built-hard problems; and whether early convergence is fake-agreement (gaming watch).
- **Cannot:** a base rate for how often AI recommendations carry flaws (selection bias, carried from §6.3); a powered effect size (small n, directional); human-expert ground truth (model-established denominator); ecological practitioner value (the separate process study).

## 10. Sign-off — accepted (assistant recommendation, delegated 2026-06-29)
- [x] Conditions R0/R1/R2/R1′ on the net-flaws-remaining DV; R2-vs-R1 load-bearing, R2-vs-R1′ anti-confound
- [x] Denominator = §6.3's ≥2-of-3 panel set on the original; net-flaw re-audit on each final output
- [x] Three terminal states + mechanical qualified stall-stop; convergence-gaming watch
- [x] Both vendor arms (same-vendor Claude, cross-vendor GPT-5.2) in the first run
- [x] Directional, n=8 paired, expansion trigger to ~16; report-either-way null
- [x] → **lock + tag** `resolver-iteration-prereg-2026-06-29`

## 11. Deviation ledger (post-lock)

All logged 2026-06-29, during the single run. None change the design, DV, conditions, or hypotheses; they are implementation clarifications recorded for integrity.

1. **Stall detector keys on the challenger's own round-to-round objection set, not the panel set.** The prereg §6 describes movement as "per-flaw disposition on still-open panel-confirmed flaws." The challenger is, by design (§5/§7), **blind to the panel denominator** — feeding it the panel set would contaminate the adversarial role. So the harness operationalizes "movement" on the challenger's *own* objections: a round shows no movement iff the challenger resolved none of the prior round's objections **and** raised no new one (the challenger self-reports `resolved_last_round` + per-objection `status`). This is the same per-objection-disposition logic the prereg intends, applied to the observable adversarial surface. (In the event, 0 ceremonies STALLED — agents kept moving — so the rule never fired.)
2. **Audit panel diversified by angle, not temperature.** `claude-opus-4-8` rejects the `temperature` parameter ("deprecated for this model"). The 3-auditor panel (prereg §5: "distinct temperatures") is instead diversified by three distinct auditor lenses (correctness/core-decision · constraints/edge-cases · feasibility/second-order). Same intent — three independent auditors with different vantage points; ≥2-of-3 consensus unchanged.
3. **Producer/challenger token budget raised 3500 → 6000** after 3 of 16 R2 ceremonies on the two most complex problems truncated their revision JSON mid-string. Re-run was resumable; no other unit affected. No semantic change.
4. **CONVERGED uses the producer's standing accept-flag rather than a separate accept call.** Each producer revision already emits `accept_as_final`; R0 is treated as accepted (the producer shipped it). CONVERGED fires when the challenger reports no material objections remaining **and** the standing output's producer-accept is true — the both-agree gate, without an extra API round-trip.
