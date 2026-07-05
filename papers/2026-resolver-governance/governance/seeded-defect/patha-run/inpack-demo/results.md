# In-pack backend — demonstration on the hardened-proof cases (H1–H3)

**Date:** 2026-06-27 · keys from `sparring-framework/.env` · `verify_grounding.py --judge`, `backend_pack`

## Why this is a *demonstration*, not a corpus re-run

The in-pack backend resolves a cited pack fact (`#N` / `§X`) against the **supplied pack text** — existence mechanically (is the fact in the pack?), support via the dual-substrate judge. It needs the per-case pack. **The v2-run corpus did not persist its packs** (`v2-run/cases.json` saved only answer-keys), so it cannot be run there. The **hardened-proof cases (H1–H3)** did save full packs (`pipeline-proof-hardened/cases.md`) and verbatim reviewer concerns (`condition-outputs.md`), so the backend is exercised on those — a capability proof.

Input: 49 in-pack-citing concerns extracted from H1–H3 × {B, S-Gen, S-Chal, T}, each carrying its case pack as `pack_text` (`inpack-demo` input in the session scratch; verdicts here).

## Result

- **Existence resolution works:** of 49 concerns, the cited fact-id was found in the real pack and the dual-substrate support-judge agreed on **43**; **6** flipped to `GROUNDED_REFUTED` (judge said the cited fact does not support the claim); **4** came back `DISPUTED` (the two vendors split — surfaced, not forced, per the cite-check house rule).
- Existence-resolved rate by condition (small n): **B 12/13, S-Gen 13/14, S-Chal 12/14, T 6/8** — the placebo resolves a cited pack fact-id least often, directionally consistent with §7.3 (the placebo cites checkable artifacts less).

## Honest limitation the demo surfaced

The 6 REFUTES and 4 DISPUTED are **mostly granularity artifacts, not refuted concerns.** The hardened reviewer outputs are *bundled* bullets ("Rate limiting on the wrong half (#5); enumeration response (#6) should be constant-time. Bottom line: revise…"; "#1 cohort most exposed to #3 load risk"). Asking the judge "does bare fact #5 support this whole multi-point bullet?" yields REFUTES even when the concern is sound, because the bullet's claim is broader than (or an inference over) the single cited fact. So:

- **Existence** (is the cited fact in the pack?) is clean and mechanical — the load-bearing thing the in-pack backend adds.
- **Support-judging on terse, bundled concerns is noisy.** To make in-pack *support* trustworthy, concerns must be **atomized** (one claim ↔ one cited fact) before judging, or the splits routed to human review. This is the in-pack analogue of the external-canon "rhetorical mention vs. grounding citation" gap.

## Bearing on the paper

This demonstrates the in-pack machinery end-to-end but does **not** upgrade the §7 in-pack grounding rates — those are a different corpus (v2, no packs) and the support axis needs concern-atomization first. §10.2 carries the resulting ceiling: on the v2 corpus, only the external-canon explicitly-cited slice (~7%) is machine-verified; in-pack verification awaits persisted packs + atomization + a claim→fact mapper.

## Files
- `verdicts.json` — raw verifier output for the 49 hardened in-pack concerns.
