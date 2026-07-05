# Resolver-iteration study — design note (pre-registration draft)

**Status:** SUPERSEDED 2026-06-29 by [`pre-registration.md`](./pre-registration.md) (LOCKED, tag `resolver-iteration-prereg-2026-06-29`). Kept for provenance — the pre-registration is the integrity spine. Parameters settled 2026-06-29 (below); created 2026-06-29.

**Why this study exists:** it is the *completing study* of the Resolver paper (the V2 governance preprint, `pilots/llm-judge-2026-05-02/v2/preprint-draft.md`). That paper establishes the value of a **single** adversarial challenge (§6.3). The Resolver is not fully characterized until we also test its deepest setting — the **both-must-agree gate that iterates to a revised, agreed output**, which §2 names as SPARRING's distinctive niche. This study isolates it.

---

## The question (plain)

Does making the challenger and the proposer **go back and forth — revising, re-challenging, until both agree** — produce a **better final answer** than a single challenge-and-fix?

## Why §6.3's measurement can't answer it

§6.3 measured *flaws flagged* on a fixed recommendation, with **no revision step** — the challenger points, nobody fixes. That DV (a) ceilings (single pass already catches 87%, 27/31), and (b) misses the point: the gate's value is in the **revised output**, not in flagging. So this study needs a different dependent variable and a revision step §6.3 never had.

## Conditions

Each condition produces a **final deliverable** scored the same way. Same producer, same problems.

| Condition | What runs | Final output scored |
|---|---|---|
| **R0 — ship as-is** | producer's original recommendation, no review | the original (definitional anchor: all flaws remain) |
| **R1 — single challenge + one revision** | one challenger pass; producer revises **once** | the once-revised recommendation |
| **R2 — iterate to agreement (the gate)** | challenger ↔ producer back-and-forth, producer revising each round, until **both agree**, **stall**, or hard cap (three terminal states, below) | the output at stop — converged, stalled, or capped |
| **R1′ — effort-matched control** | producer revises a second time **on its own**, no adversarial round (matches R2's extra passes without the gate) | the twice-revised recommendation |

- **R1 vs R0** = value of a single challenge-and-fix (the "does the Resolver do anything" floor, now on a *fixed-output* DV).
- **R2 vs R1** = **the load-bearing contrast** — the marginal value of *iterating to agreement* beyond one challenge.
- **R2 vs R1′** = isolates the **adversarial iteration** from "just more revising" (the compute/effort confound; parallel to §7.2's realistic-skeptic placebo).

## Dependent variable

**Material would-ship flaws *remaining* in the final output** (lower is better). No ceiling: R0 leaves all of them in; a working gate leaves fewer.

- **Denominator:** reuse §6.3's machinery — an independent **≥2-of-3 audit panel** enumerates the material would-ship flaws in the *original* recommendation. That panel-confirmed set is fixed before any condition runs.
- **Coding:** for each condition's final output, blind-code which panel-confirmed flaws **remain**.
- **Net, not just removed:** also count **new material flaws introduced by revision**. Iteration that fixes two flaws and adds one is not a two-flaw win. The honest DV is *net* material flaws in the final output.
- **Secondary:** did the recommendation's **core decision change** across iteration (decision-change rate); **rounds to convergence**.

## Hypotheses (to lock)

- **H1 (floor):** R1 leaves fewer net flaws than R0. (Expected; sanity that a challenge-and-fix helps at all on this DV.)
- **H2 (load-bearing):** R2 leaves fewer net flaws than R1 — iterating to agreement beats one challenge.
- **H3 (anti-confound):** R2 leaves fewer net flaws than R1′ — the gain is the *adversarial* iteration, not just extra revising.
- **Pre-committed null, reported either way:** if R2 ≈ R1 (and/or R2 ≈ R1′), iterating-to-agreement adds little beyond a single challenge — **reported as a finding, not buried.** This is the Resolver paper being honest about its own headline mechanism.

## Honesty controls (how to keep it clean)

1. **Pre-register first.** Lock question, conditions, DV, hypotheses, analysis, sample, and the report-either-way commitment before running. Tag it. (The paper's integrity spine; a controlled gate test must not be exploratory.)
2. **Blind, order-rotated coding.** The flaw-remaining coder never sees which condition produced an output.
3. **New-flaw accounting** (above) — guards against overcrediting iteration.
4. **Effort-matched control (R1′)** — separates structure from sheer compute.
5. **Convergence-gaming watch.** The gate stops when "both agree." A too-agreeable agent could **fake agreement to stop early** — the exact failure SPARRING is built against. The three terminal states (control 6) give this teeth: *CONVERGED-with-flaws-remaining* is the fake-agreement signature; *STALLED-with-flaws-remaining* is genuine deadlock — same flaw count, different failure. Test whether early convergence correlates with *more* flaws remaining; if it does, the gate is failing at its own job — a finding in itself, and a direct test of the §2 niche claim. The **cross-vendor arm** is where this bites hardest (same-vendor agents are the likeliest fake-agreers).
6. **Three terminal states + a qualified stall-stop.** A ceremony ends in one of three pre-registered states: **CONVERGED** (both agree), **STALLED**, or **CAPPED** (hard cap = 5 rounds). The **stall rule** (mechanical, tied to the flaw set): STALLED if, for **2 consecutive rounds**, neither side moves on the open flaws — the proposer's revision changes its handling of *no* still-open panel-confirmed flaw, **and** the challenger raises *no* flaw not already on the table (movement is per-flaw disposition — addressed / not-addressed — not text similarity). Minimum 2 rounds before it can fire; the cap is the backstop above it. Oscillation (positions cycling A↔B) is logged as a secondary signal but does not gate in v1. The final output is scored at the stop **regardless** of state, and flaws-remaining is **reported broken down by terminal state** — a method that "converges" by stalling-then-giving-up is not the same as one that converges on a clean output.
7. **Cross-vendor caveat.** Same limit as the rest of the paper — ceremony agents share a vendor family; run cross-vendor where feasible, flag where not.

## Settled parameters (2026-06-29; pending pre-registration lock + tag)

- **Problem set — reuse §6.3's 8 problems and their panel-confirmed flaw sets.** The denominator is already built, and R1/R2 then sit on the *same flaws* as §6.3's single-pass result — one comparable ground for the whole Resolver story. Selection-bias caveat carried over (problems authored to a difficulty bar, not sampled). The audit panel **re-runs on each condition's final output** to catch flaws the revision introduces (net-flaw accounting).
- **n / power — 8 problems, paired within-problem design.** R2 vs R1 is within-problem (same problem, same flaws, two depths), far more powerful than between-problem. **Directional, matching the paper's first-signal posture; no significance claim unless the data support it.** Pre-registered expansion trigger: extend to ~16 problems if the R2-vs-R1 effect is small or noisy.
- **Round cap / terminal states — hard cap 5 rounds, with the qualified stall-stop (control 6) firing earlier.** Three terminal states recorded per ceremony: CONVERGED · STALLED · CAPPED; log the round distribution.
- **Vendor — two arms, both in the first run.** *Same-vendor* (Claude produces, Claude challenges) for comparability with §6.3; *cross-vendor* (Claude produces, GPT challenges) as a first-class arm — the sharpest test of the gate, since same-vendor agents are the likeliest to fake-agree via shared training and the gate's rationale is resisting exactly that coordinated agreement.

## Relationship to the rest of the program

- **Completes Paper 1 (the Resolver).** R1 connects to §6.3 (single challenge); R2 is the gate.
- **Independent of Paper 2 (the Proposer).** This study holds the *Proposer* out — it starts from the producer's naive proposal and tests only what the Resolver does to it. The Proposer's value is its own report (preprint §11 item 5).
