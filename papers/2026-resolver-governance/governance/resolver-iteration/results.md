# Resolver-iteration study — results: does iterating-to-agreement beat a single challenge?

**Date:** 2026-06-29 · **Pre-reg:** [`pre-registration.md`](./pre-registration.md) (LOCKED, tag `resolver-iteration-prereg-2026-06-29`). **Data:** [`runs/`](./runs/) (40 final outputs + 40 score records) → [`analysis/results-aggregate.json`](./analysis/results-aggregate.json). **Harness:** [`scripts/run_study.py`](./scripts/run_study.py). Producer/auditors/coder = `claude-opus-4-8`; cross-vendor challenger = `gpt-5.2`. Reuses §6.3's 8 problems, R0 originals, and ≥2-of-3 panel denominator (31 flaws).

> **Headline (the result, stated honestly — and it is the pre-committed null).** On the same 8 hard problems as §6.3, iterating the challenge **to agreement** (the both-must-agree gate, R2) leaves **no fewer net material flaws** in the final output than a **single** challenge-and-fix (R1) — and **neither beats simply having the producer revise twice on its own** (R1′, the effort-matched control). The mechanism is the interesting part: the adversarial challenge is a **better flaw *detector*** — it removes **87%** of the producer's original blind-spot flaws (matching §6.3 exactly), versus **74%** for self-revision — but revising **under adversarial pressure introduces *new* material flaws** (~2.1 per output) that quiet self-revision largely avoids (~1.25). The detection win and the churn cost cancel. **On output quality, the gate's distinctive iterate-to-agreement mechanism does not earn its keep here.** Reported as a finding, per the pre-registration.

## Net material flaws remaining (the pre-registered DV; lower is better; denominator mean = 3.875/problem)

| Condition | Mean net flaws remaining | of which: original flaws still remaining | of which: new flaws introduced |
|---|---|---|---|
| **R0** — ship as-is (anchor) | **3.875** | 3.875 (all, by construction) | 0 |
| **R1′** — producer self-revises ×2 (no challenger) | **2.250** | 1.000 | 1.250 |
| **R1** — single challenge + revise (same-vendor) | 2.625 | 0.500 | 2.125 |
| **R1** — single challenge + revise (cross-vendor) | 3.125 | 0.500 | 2.625 |
| **R2** — iterate to agreement (same-vendor) | 2.625 | 0.625 | 2.000 |
| **R2** — iterate to agreement (cross-vendor) | 3.000 | 0.750 | 2.250 |

The two columns on the right are the whole story. **Flaw removal** (middle): every challenged condition removes ~87% of the original panel-confirmed flaws (0.5 remaining of 3.875) — better than self-revision's 74% (1.0 remaining). The challenger catches the producer's blind spots, exactly as §6.3 found, now measured on the *revised output* rather than on flags. **New flaws** (right): challenged revisions seed ~2.0–2.6 new material flaws; self-revision seeds ~1.25. The net (left) is a wash, and self-revision quietly wins it.

## Hypotheses — verdicts

- **H1 (floor): R1 < R0 — supported (same-vendor), weak (cross-vendor).** A single challenge-and-fix beats shipping as-is: same-vendor −1.25 net (5 of 8 problems improved, 1 worse, 2 tie); cross-vendor −0.75 but mixed (3 improved, 4 worse, 1 tie). A challenge helps on net — but less than the raw removal rate suggests, because of the new flaws it introduces.
- **H2 (load-bearing): R2 < R1 — NULL.** R2 vs R1 is **+0.000** same-vendor (2 better / 2 worse / 4 tie) and **−0.125** cross-vendor (3/3/2). Iterating to agreement does **not** beat a single challenge on output quality. *This is the pre-committed null, and it is the headline.*
- **H3 (anti-confound): R2 < R1′ — NULL, and reversed.** R2 is **worse** than effort-matched self-revision: +0.375 (same-vendor), +0.750 (cross-vendor). The extra adversarial passes did not beat the producer simply revising twice on its own. The *adversarial* structure is not what produces a cleaner output here — and on this DV it slightly hurts, by inducing churn.

## Terminal states + the convergence-gaming watch

Of 16 ceremonies: **4 CONVERGED** (3 same-vendor, 1 cross-vendor), **12 CAPPED** at 5 rounds, **0 STALLED**. Same-vendor agents reached agreement more often (3/8 vs 1/8) — consistent with the prereg's expectation that same-vendor agents are likelier to agree.

**The fake-agreement pathology did not appear.** The gaming watch asked whether early CONVERGED correlates with *more* flaws remaining (agreeing to stop while flaws survive — the sycophancy the gate exists to stop). The opposite held: CONVERGED outputs averaged **1.25** net flaws, CAPPED **3.33**. When the agents agreed, they agreed on genuinely cleaner outputs (two converged at net 0; worst converged at net 3). So the null here is **"the gate adds little,"** not **"the gate is gamed."** (Caveat: this is confounded with problem difficulty — convergence was reachable on the cleaner problems and the cap bound the hard ones — so read it as *absence of a fake-agreement signal at n=8*, not proof the gate can't be gamed. The cross-vendor arm, where gaming was predicted to bite hardest, converged only once — and that once was a clean net-0 output shared with the same-vendor arm.)

## Why the net-flaw accounting was load-bearing (a methods note)

Without new-flaw accounting (control 3), this study would have reported a large false win: challenged conditions leave only 0.5 of 3.875 original flaws (an 87% "catch," headline-friendly). The net DV reveals that the revisions buy that removal by **seeding new defects** — and once you count them, and compare against an **effort-matched self-revision control** (R1′), the gate's advantage disappears. The between-condition contrast (R1′ vs R1 vs R2) holds the audit-panel instrument constant, so the *difference* in new-flaw counts is clean even though the *absolute* new-flaw counts include the panel's baseline propensity to surface ~material issues on any output (see caveats).

## Internal consistency with §6.3 (a validity check)

The challenged conditions removed **87.1%** of the producer's original flaws (0.5 of 3.875 remaining) — numerically identical to §6.3's single-vendor Challenger catch-rate (27/31 = 87.1%). Self-revision removed **74%** (1.0 of 3.875), bracketing §6.3's self-review 67.7%. The harness reproduces §6.3's detection result on the same problems via a different instrument (output re-audit vs flag-coding) — evidence the machinery is measuring the same thing.

## Honest scope and caveats

- **Directional, n=8, no inferential stats.** Paired within-problem, but small. The **pre-registered expansion trigger is met** (R2-vs-R1 ≈ 0): before treating the null as settled, extend to ~16 problems — which requires authoring 8 new problems *and* building their ≥2-of-3 denominators (a §6.3-style ground-truth run), so it is genuine future work, not a re-run.
- **Absolute new-flaw counts include panel baseline.** A fresh 3-auditor panel finds ~material flaws on *any* recommendation (that is how the §6.3 denominator was built). "New flaw" = a ≥2-consensus panel flaw on the revised output not semantically in the original denominator; some fraction reflects the panel's baseline flaw-finding on a new artifact, not pure revision damage. The load-bearing result is the **between-condition difference** (adversarial conditions seed more new flaws than self-revision), which is robust to that baseline; the absolute net levels should be read as upper-ish bounds.
- **Same caveats as §6.3, carried:** problems authored to a difficulty bar (selection bias, washes out of within-problem contrasts); model-established ground truth (≥2-of-3 panel, not human expert); same producer family throughout. The **cross-vendor arm** addresses the sharpest version (a GPT challenger against a Claude producer) and the null holds — if anything more strongly — there too.
- **DV scope.** This measures *output quality* (net flaws remaining). It does not measure governance properties §6 establishes (consequential catches, grounding) — those are not in question here; what is in question is whether *iterating to agreement* yields a cleaner final answer, and on these problems it does not.

## What this means for the Resolver paper

The Resolver's value, as established, is **detection**: a challenge — especially a different-vendor one — recovers material blind-spot flaws a single pass would ship (§6.1–§6.3). This study tested the deeper claim — that driving the challenge **to a both-agree revised output** (§2's distinctive niche) yields a **better answer** — and finds it **does not**, on net output quality, at n=8: the gate adds nothing over a single challenge, and a single challenge adds nothing over effort-matched self-revision once revision churn is counted. The honest read for Paper 1: **the Resolver is a strong flaw-detector but its iterate-to-agreement gate is not a demonstrated output-quality improver** — the gate may still matter for governance reasons (auditability, the non-bypassable stop) that this output-quality DV does not capture, but its *answer-quality* value is, on this evidence, unproven. Reported either way, as pre-committed.

> **Integration note (for author review — not yet executed in the preprint).** The pre-registration commits that on completion this moves into the paper body as a result. Because it lands a **null on the §2 distinctive-niche claim**, the framing of §2/§10.2/§11-item-8 is a load-bearing authorial call (the kind Julian's craft lane routes to the author/Miriam, not an autonomous edit). The result and its honest framing are captured here; folding it into the manuscript body is left for Bart's review.
