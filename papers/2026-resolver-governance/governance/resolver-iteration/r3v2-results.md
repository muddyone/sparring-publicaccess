# R3 v2 — recalibration (new-flaw budget + dynamic cap) · RESULTS (EXPLORATORY · NEGATIVE)

**Status:** `EXPLORATORY · NOT PRE-REGISTERED · firewalled from Paper 1.` n=8 × 2 arms.
**Verdict: the recalibration backfired — v2 is worse than [v1](./r3-results.md) in both arms.** v1
(`R3`, lenient gate, fixed cap 5) remains the better design and the standing best condition.

**Date:** 2026-06-29 · Dials changed from v1 (Bart-authorized data-driven rerun, then this result):
severity-relative bar **unchanged**; **added** a global new-flaw budget (cumulative admitted
new-flaw severity ≤ 3); round cap 5 → **dynamic** (stop on CONVERGED/EXHAUSTED, hard backstop 10).
Artifacts: `analysis/results-aggregate-r3v2.json`, `analysis/r3v2-governance-trail.json`.

## Headline

| Condition | mean net (lower better) |
|---|---|
| R1 single-pass (the floor) | 2.625 same / 3.125 cross |
| R1′ best locked | 2.25 |
| **R3 v1** (lenient gate, cap 5) | **1.75 / 1.125** |
| **R3 v2** (budget≤3 + dynamic cap) | **3.0 / 2.375** |

v2 is **+1.25 worse than v1 in both arms** (paired: v2 fewer 0/8 same, 2/8 cross). v2.same (3.0)
fell back *above* the single-pass floor; v1's "beats the floor in both arms" property is lost.

## Both changes failed, and the diagnosis behind them was wrong

**1. The budget did not fix its target regression.** warehouse-siting/same is net **5 in both v1
and v2** — unchanged. The v2 trail: the 4 new flaws entered through a **single round-1 patch**
(`new_flaw_cost=3`, admitted because 0+3 is not > 3 — it spent the whole budget at once). The v1
failure was **single-bad-patch, not slow accumulation.** The "no running-total guard" diagnosis
(Rosetta's reading + my recommendation) was incorrect; a per-ceremony severity budget cannot catch
a one-shot bad rewrite without being so tight it blocks legitimate patches everywhere.

**2. The budget choked the mechanism that made v1 win.** Governance: v1 admitted **53** / rejected
**8**; v2 admitted **37** / rejected **28**, of which **18 were budget-blocks**. Consequence in
terminal states:

| | CONVERGED | EXHAUSTED | CAPPED |
|---|---|---|---|
| v1 | 5 (net 1.8) | 4 (net 3.0) | **7 (net 0.286)** |
| v2 | 3 (net 3.0) | **12 (net 2.75)** | 1 (net 1.0) |

v1's strength was admitting Pareto-improving patches over many rounds — CAPPED (ran the full cap,
still improving) was *cleanest*. v2 inverts it: once the budget is spent, nearly any further patch
trips a panel-flagged new flaw and is blocked, so **12/16 ceremonies run out of admissible moves and
stop early on dirty outputs.** The budget strangled the improvement engine.

**3. The dynamic cap got no fair test.** Ceremonies exhausted early (only 2 of 16 reached cap 10),
so the cap change is confounded by the budget — neither creditable nor blamable from this run.

## What it teaches (the useful part of a negative result)

- **v1's leniency was load-bearing, not a bug.** The per-patch new flaws the panel reports are
  largely **panel noise** (a fresh panel finds something on almost any output — the §4.3 baseline).
  v1 admitted patches and let that noise wash out across continued rounds of real improvement; the
  budget treated the noise as accumulating cost and shut the machine off. We penalized false
  positives and starved the gains.
- **warehouse-siting was an outlier to leave alone.** It is 1 of 16, and **v1 beat the floor
  decisively with it included.** The recalibration over-fit the mechanism to a single bad case and
  lost the win on the other 15.
- **Governance stayed legible** under v2 (every reject records a blocker, incl. all 18 budget-blocks)
  — the trail machinery is sound; the policy it enforced was wrong.

## Standing recommendation

**Keep v1 (`R3`) as the standing best.** If warehouse-siting is worth addressing later, the lever is
the gate's admission decision on the single bad patch — e.g. require a **unanimous 3/3** panel for any
patch that introduces *any* new flaw, or a ceremony-level **stop-loss** (never finalize an output the
gate scores worse than R0) — **not** a global new-flaw budget and **not** a longer cap. That is a
future exploratory knob, not this result. v2 does not change the Paper 1.5 prereg picture: the
condition that earned the confirmatory test is **v1**.
