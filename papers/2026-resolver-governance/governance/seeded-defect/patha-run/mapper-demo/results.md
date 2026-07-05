# claim→fact mapper — demonstration on the hardened prose concerns

**Date:** 2026-06-27 · keys from `sparring-framework/.env` · `verify_grounding.py --map-claims --judge`

## What the mapper is for

~57% of the v2 corpus's concerns ground themselves in a pack fact **by description**, with no `#N` token, so they classify as `none` and the verifier can't reach them. The claim→fact mapper closes that gap: a single-substrate mapper proposes which pack fact(s) a prose concern relies on; the concern is then verified **in-pack** (existence of the mapped facts + the dual-substrate support judge). Mapping is extraction; the grounding *judgment* stays two-vendor.

It needs the pack — so, like the in-pack backend, it can be **demonstrated** on the hardened H1–H3 cases (which saved packs), not the v2 corpus (which did not). This is forward infrastructure for future runs, not a retroactive fix to v2.

## Input

29 **prose** concerns from H1–H3 × {B, S-Gen, S-Chal, T} — only those with **no explicit `#N`/`§` token** (the slice the mapper targets), each carrying its case pack as `pack_text`.

## Result

| | n |
|---|---|
| Mapped to a pack fact → verified in-pack | **19** |
| Left `UNGROUNDED` (mapper returned `[]`) | 10 |
| — of the 19 mapped: GROUNDED_VERIFIED | 15 |
| — of the 19 mapped: GROUNDED_REFUTED (support judge) | 4 |

**The mapper reaches genuinely pack-grounded prose** — e.g. the H2 concerns about the unreachable credit tiers map to **#7, the planted 15%-cap defect**; an H1 concern maps to #3 (the misapplied CLT fact). **And it abstains correctly:** the 10 it left ungrounded are bare bottom-lines ("Bottom line: revise (Python-first)"), an empty bullet, and concerns grounded **externally** rather than in the pack (an MFA best-practice point; a `CWE-521` cite) — for which `[]` is the right answer. So the mapper extends reach **without** hallucinating pack mappings for non-grounded text.

## Caveats (same shape as the in-pack demo)

- The 4 REFUTED-among-mapped are the familiar granularity nuance — terse, bundled reviewer bullets judged against a single mapped fact. Concern atomization would tighten this.
- The mapper is **single-substrate** (extraction); only the support *judgment* is dual-substrate. A mis-map sends the judge the wrong fact — so a mapped GROUNDED_VERIFIED is "this fact is in the pack and supports the claim," not "this is the only/best fact." For high-stakes use, dual-substrate the mapping too and surface disagreement.

## Files
- `input.json` — the 29 prose concerns (with `pack_text`).
- `verdicts.json` — raw verifier output (`backend` shows `in-pack+mapper`; `evidence` carries the `[mapped to …]` note).
