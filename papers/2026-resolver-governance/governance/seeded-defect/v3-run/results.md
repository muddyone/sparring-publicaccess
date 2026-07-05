# Seeded-defect v3 — results (realistic placebo, Path-A judged)

**Date:** 2026-06-28 · **Pre-reg:** [`../pre-registration-v3.md`](../pre-registration-v3.md) (LOCKED). **Data:** [`aggregate.json`](./aggregate.json), the 12 `case-*.json`, [`verdicts-T.json`](./verdicts-T.json) (realistic placebo grounding) + [`verdicts-judged.json`](./verdicts-judged.json) (B/S + the superseded strawman-placebo run).

> **What this is.** Machine-complete, audit-pending: 12 cases → conditions → blind legitimacy coding → full Path-A grounding (machine existence + dual-substrate Claude+OpenAI supports-judge + claim→fact mapper) → aggregate. The placebo (T) was **regenerated as a realistic skeptic** (a tough reviewer that points at facts in the briefing but cannot look up CWEs/citations), superseding an earlier no-discipline strawman placebo.

## The aggregate (per condition; Path-A judged)

| Condition | concerns | Grounding | Verified-grounded-TP | Precision | Theater |
|---|---|---|---|---|---|
| **B** neutral single pass | 12 | 58.3% | 33.3% | 50.0% | 41.7% |
| **S** SPARRING | 27 | **96.3%** | **96.3%** | 100.0% | 3.7% |
| **T** realistic skeptic | 60 | 83.3% | 83.3% | 100.0% | 16.7% |

## What this study can and cannot show — read this before quoting

Three layers, kept separate on purpose:

1. **SPARRING vs a raw single pass (S vs B) — the practically-relevant comparison — SPARRING wins clearly.** Its objections are **96% grounded and 100% precise**, versus a raw pass's **58% / 50%**. SPARRING's concerns are far more grounded, checkable, and on-target than an un-adversarial pass. *This is the lived "godsend for rigor," and it is in the data.* (Magnitude caveat: B's exact numbers are generation-sensitive — the neutral pass emitted some "looks fine, ship it" statements that code as false positives; the **direction** — adversarial review is more rigorous than a raw pass — is robust, the precise gap is soft.)

2. **This study CANNOT measure catch-rate — which is SPARRING's *main* practical value — and that is a design limit, not a verdict.** *"It catches things a raw prompt wouldn't"* is a **catch-rate** claim. Seeded defects are obvious enough that a strong model catches them under **any** condition (v1's catch-rate saturated at ~100% — which is exactly why it was retired), and these cases put the decisive fact **in the briefing**, so even a no-discipline skeptic grounds. So this design is structurally **blind** to "catches what a raw prompt misses." That value is evidenced by the **mechanism audit (§6)** — the real would-have-shipped catches (fail-open auth, the lockout DoS) on real decisions — **not here.** A marginal S-vs-T result here is *not* evidence SPARRING adds little; it's evidence the easy synthetic test can't see where SPARRING earns its keep.

3. **SPARRING vs a dedicated skeptic (S vs T) — the artifact-discipline isolation — marginal.** S grounds 96% vs a realistic skeptic's 83% — a ~13-point edge at n=12, no significance test. The skeptic grounds well **because the checkable evidence is in the briefing**. So the artifact-citation discipline adds a modest grounding edge on easy, evidence-in-hand cases; most of the rigor advantage over a raw pass comes from **having a genuine challenger at all.**

## The fragility finding (why regenerating the placebo mattered)

An earlier strawman placebo (told to cite nothing) grounded **15%** — making S look like a crushing 96-vs-15 win. A realistic skeptic grounds **83%**. The measured "theater" gap is therefore **fragile**: it depends entirely on how weak the control is and whether the evidence is in-hand. Reporting the 15% would have badly overclaimed; the 83% is the honest number. (This is itself a useful methodological result for anyone evaluating deliberation methods.)

## The methodological contribution (objective, cross-vendor)

Grounding is resolved by **machine existence** (cited CWE/RFC/DOI against public registries, in-briefing facts against the persisted briefing — *no model*) plus a **dual-substrate Claude+OpenAI supports-judge** (does the artifact actually back the claim) + a claim→fact mapper. So grounding is **verified, not AI-rubber-stamped, and cross-vendor** — closing the v2 data-loss gap. This holds regardless of the S-vs-T effect size.

## What remains (per the §10.1 validation stance — not author tasks)

1. **Domain-expert legitimacy audit** (§9 Phase 3) — the only human gate; not the author.
2. **Cross-vendor / de-constructed generation** — to make any effect a finding rather than a construction.
3. **To capture SPARRING's catch-rate value:** harder, real, non-obvious cases where the defect is *not* in-hand — the **§6 mechanism audit** and the prospective ledger, not synthetic seeded defects.

## Verdict

Honestly scoped, v3 shows: **SPARRING produces real, machine-verifiable objections far more than a raw pass** (lived rigor confirmed); the artifact-discipline edge over a *competent* skeptic is marginal on easy, evidence-in-hand cases; and this design **cannot** measure SPARRING's catch-rate value — that lives in §6. The numbers deliberately don't overclaim, which is the point — and which is why the practical value claim should lead with the real catches (§6), with v3 as the supporting "the grounding is real and checkable."
