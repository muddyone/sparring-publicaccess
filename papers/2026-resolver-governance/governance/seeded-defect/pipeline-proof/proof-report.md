# Pipeline proof — report

**Date**: 2026-06-26 · **Scope**: 3 controlled cases (DC2/DC1/DC3) × 3 conditions (B/S/T) + 1 blind catch-judge. Same-vendor (Claude subagents); cross-vendor deferred to the VPS harness.
**Purpose**: validate the seeded-defect pipeline end-to-end and surface design flaws *before* scaling to 20 cases + building the cross-vendor harness.

## What the pipeline proved (mechanics: PASS)

Every stage connected and produced clean, scoreable artifacts:
1. Case + fact-checked pack + opening-with-one-planted-defect authored; answer key sealed. ✓
2. Three conditions (B neutral / S grounded Challenger / T placebo) each produced a structured review without seeing the answer key. ✓
3. A **blind** catch-judge (condition-hidden, shuffled labels) scored each review against the planted defect on two axes: binary catch + grounding quality. ✓
4. Decoding the blind labels gave a clean per-condition result table. ✓

The judge stage works and even adds a discriminating secondary axis (see below). The machinery is sound.

## What the proof surfaced (design flaw: CEILING EFFECT)

| Case | Defect | B (neutral) | S (grounded) | T (placebo) |
|---|---|---|---|---|
| P1 | DC2 pack contradiction | caught (artifact) | caught (artifact) | caught (artifact) |
| P2 | DC1 fabricated citation | caught (artifact) | caught (artifact) | **caught (ASSERTION)** |
| P3 | DC3 security/CWE | caught (artifact) | caught (artifact) | caught (artifact) |

**Binary catch saturated at 9/9.** Strong frontier models catch a single, salient, clearly-planted defect in a short pack *regardless of condition* — the neutral single reviewer and the ungrounded placebo caught every defect the grounded Challenger did. **The primary measure does not discriminate the conditions at this difficulty.** This is the same near-ceiling pathology that made V2 uninformative — re-encountered, cheaply, before scaling.

**The secondary axis discriminated exactly once, and predictably.** The blind judge flagged a single vibes-only catch — and it was the **placebo on the citation case** (it "caught" the fabricated citation with *"smells like a too-clean number… red flag"* but never named a verification method, whereas B and S pointed at Crossref/ISSN lookup). On P1 (contract breach) and P3 (fail-open) even the placebo grounded its catch, because the defect sits right on top of a headline pack fact that any objection naturally cites.

## Reading

- The defects are **too easy and too salient** — each contradicts a *headline* pack fact (a 90-day mandate, a fabricated journal, a fail-open on a stated PII path). A single pass catches them, so there is no headroom for an adversarial/grounded process to win.
- Where grounding *could* matter (the citation, which needs an external lookup rather than a pack cross-reference), the axis that separated conditions was **grounding quality**, not binary catch.
- We have therefore validated the pipeline but **not yet shown the instrument can discriminate**. We have shown it *cannot* with blatant defects.

## Required design changes before the 20-case run (pre-data)

1. **Harden the defects so a single pass plausibly misses them.** Prefer (a) **misapplied** real citations over fabricated ones (a real DOI cited for a claim it doesn't support — passes a naive smell test); (b) defects that contradict a **buried, non-headline** pack fact requiring multi-step inference; (c) defects embedded in **longer packs with plausible-but-fine distractor content**, so recall is genuinely hard.
2. **Move the primary measure off binary catch.** Make the headline contrast **grounding quality / verifiable-artifact rate** and **false-positive (theater) rate** — i.e., does S catch *with checkable grounding and few false alarms* while T catches *on suspicion and raises more ungrounded concerns*. Binary catch becomes a secondary/recall measure. (The current clean cases produced zero false positives because there was nothing plausible-but-fine to over-flag; distractor-loaded packs will let that signal emerge.)
3. **Create baseline headroom.** Define B as a genuine single pass *without* an adversarial self-critique affordance, so S/T have something to beat.
4. **Re-run a hardened mini-proof (2–3 cases) to confirm separation BEFORE scaling to 20.** Do not build the cross-vendor harness or generate the full corpus until a mini-proof shows the conditions actually diverge.

## Status

- Pipeline mechanics: **proven.**
- Discrimination: **not yet demonstrated; ceiling effect must be fixed first.**
- These are pre-data changes to the locked design → to be recorded in `pre-registration.md` §10 deviation ledger on partner approval, before any hardened case is generated.
