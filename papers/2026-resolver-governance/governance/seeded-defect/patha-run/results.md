# Path-A run — verifier-backed grounding (P1 + P1.5 live, dual-substrate)

**Date:** 2026-06-27 · **Host:** worktree-demeter-sparring-1 (keys resolved from `sparring-framework/.env` — `ANTHROPIC` + `OPENAI`, project-env)
**Tool:** `scripts/verify_grounding.py --judge` (P1 resolution + P1.5 dual-substrate supports-claim), `CITE_CHECK_PY` = loom shared `cite_check.py`
**Self-tests this host:** P1 resolution **8/8** green (incl. the RFC backend added this session); P1.5 wiring 5/5 green.

## What this run does (and does not) do

This is the **first live Path-A pass** the preprint (§8, §11) names. It upgrades the **external-canon** grounding judgments — the families §7.3 shows are where grounding actually discriminates — from LLM-coded (Path-B) to **machine-verified against public registries**. It does **not** re-verify all 236 concerns: the pack / buried-contradiction / code families are **P2 stubs** (their artifacts live *inside* the provided pack, so there is no external registry to resolve against) and stay Path-B.

Input: the 17 v2-run concerns (`codings.json`) whose text cites an extractable external artifact (CWE / RFC / literature), tagged with their blinded condition (B / SGen / SChal / T via per-case `labelMap`). Extraction is regex over the concern text → `verifier-input.json`.

## Result

| Artifact family | n | Backend | Outcome |
|---|---|---|---|
| **CWE (security)** | 11 | MITRE CWE API | **11/11 resolve to a real CWE**; supports-judge 9 SUPPORTS, 2 INSUFFICIENT. Zero fabricated. |
| **RFC / IETF** | 4 | IETF datatracker | **4/4 resolve to a real RFC** (8725, 6750, 7519); supports-judge SUPPORTS on all. *(Backend built this session.)* |
| **Literature** | 2 | Crossref | 1 resolves (Berry & Lievens 2022); 1 extraction artifact (Sackett — see note). |

**Agreement with Path-B:** of 17 external-canon concerns, **16 resolve cleanly and the verifier agrees with the LLM coding on 15**. The security/CWE and RFC families — the discriminating ones in §7.3 — are now **verifier-backed, no model in the existence loop**. No artifact was fabricated; none cited backward.

## The two raw verifier-vs-LLM disagreements (both verifier-side artifacts)

1. **`DC3-fileup_T_r3c2` (placebo, CWE-434):** LLM = UNGROUNDED, verifier = GROUNDED_VERIFIED+SUPPORTS. The placebo only *name-drops* CWE-434 ("dodges the entire CWE-434 blast radius") while making a different point; the verifier's regex credits any real-CWE mention as grounding, so it **over-credits the placebo**. Direction: narrows S-vs-T slightly; a verifier false-positive, not the human under-coding. Does not affect the S-family claim.
2. **`DC1-hiring_B_r4c2` (baseline, Sackett et al. 2022):** LLM = GROUNDED_VERIFIED, verifier = GROUNDED_REFUTED — **purely an extraction artifact.** The input passed author-year with no title; Crossref can't resolve that. Re-run with the full title resolves cleanly: *"Revisiting meta-analytic estimates of validity in personnel selection"* (DOI `10.1037/apl0000994`). The citation is real; the LLM coding was right.

Both are tool-side (one over-credit, one extraction gap), in opposite directions, and neither overturns the Path-B coding's direction.

## Full-corpus coverage map — what the verifier can mechanically reach (all 236 concerns)

Classifying every concern by whether it cites a resolvable artifact, and (for the rest) joining the Path-B grounding code:

| Slice | n | % | Status |
|---|---|---|---|
| **External-canon, explicitly cited** (CWE/RFC/citation) | 16 | 7% | **machine-verified** (this run) |
| **In-pack fact-id cited** (`#N`/`§X`/MSA) | 46 | 19% | **blocked — v2 packs not persisted** (backend exists; see below) |
| **Prose/pack-grounded, no resolvable token** | 135 | 57% | needs packs **and** a claim→fact mapper — not mechanical today |
| **No artifact, Path-B UNGROUNDED** | 39 | 17% | verifier agrees (UNGROUNDED) |

The headline: mechanical grounding-verification reaches the *externally-checkable, explicitly-cited* slice. The **majority (57%) of grounding judgments are made by reading the pack and mapping a prose claim to a fact** — which the verifier cannot reproduce without both the pack text and NLP claim-mapping. This is the real ceiling, and the §7 rates remain expert-coded outside the external-canon slice.

## Verifier backends — built this session

- **RFC/IETF backend** (`backend_rfc`, IETF datatracker) — RFCs previously fell through as `type:none`/UNGROUNDED; now resolved like CWEs (404 → REFUTED).
- **In-pack backend** (`backend_pack`) — resolves a cited fact `#N`/`§X` against a supplied `pack_text` (existence mechanical; support dual-substrate). **But the v2 corpus did not persist packs**, so it returns `UNVERIFIED_NOT_CHECKED` there; demonstrated instead on the hardened H1–H3 cases (`inpack-demo/`, 49 concerns: existence resolves cleanly; support-judging on terse *bundled* concerns is noisy and needs concern-atomization).
- **claim→fact mapper** (`--map-claims`) — closes the 57% prose-grounded slice: a single-substrate mapper proposes which pack fact(s) a token-less concern relies on, then it is verified in-pack (the support judgment stays dual-substrate). Demonstrated on 29 hardened prose concerns (`mapper-demo/`): **19 mapped to real facts** (incl. the H2 concerns → #7, the planted defect), **10 correctly abstained** (bottom-lines / empty / externally-grounded). Reaches prose grounding without hallucinating pack mappings.
- Self-test now **10/10** (P1, adds 2 RFC + 3 in-pack); judge wiring 5/5; mapper wiring 4/4.

**Still open:** persist per-case packs in future runs (the one blocker on full-corpus in-pack verification); dual-substrate the mapper for high-stakes use; **concern atomization** (so in-pack *support*-judging is trustworthy); title-aware citation resolution; rhetorical-mention vs. grounding-citation.

## Files

- `verifier-input.json` — the 17 concerns fed to the verifier (`id, artifact_ref, concern_text`).
- `verdicts.json` — raw verifier output (grounding + supports_claim per concern), RFC-backend re-run.
- `concerns-full.json` — concerns with condition + LLM coding joined, for the comparison above.
