# Phase 0 — re-coding the hardened outputs under the v2 measure

**Date**: 2026-06-26 · **Goal (per v2 §8)**: confirm the new per-concern measure *separates the conditions* before any new generation. **Method**: 3 blind coders (one per case, Claude subagents), each given the case + pack + answer key + all four reviews **shuffled and condition-hidden**; each concern coded on legitimacy (TP/FP) and grounding (VERIFIED/REFUTED/UNGROUNDED). Labels decoded after coding. S condition = S-Gen ∪ S-Chal (the two-agent ceremony).

## Aggregate (all 3 cases, per concern)

| Condition | concerns (n) | **Grounding rate** | **Precision** | **Verified-grounded-TP** | Theater rate |
|---|---|---|---|---|---|
| **S** (ceremony, 2 agents) | 36 | **89%** | 89% | **83%** | **11%** |
| **B** (neutral single pass) | 18 | 67% | **94%** | 67% | 33% |
| **T** (placebo) | 21 | 48% | 86% | 48% | 52% |

Grounding rate = VERIFIED/n · Precision = TP/n · Verified-grounded-TP = (TP∧VERIFIED)/n · Theater rate = (UNGROUNDED+REFUTED)/n.

## The measure separates — cleanly

- **Grounding rate: S (89%) > B (67%) > T (48%).** The theater test (S > T) holds decisively, and S beats the neutral baseline too. This is the axis binary-catch was blind to.
- **Verified-grounded-TP (the composite): S (83%) > B (67%) > T (48%).** SPARRING produces the most *real-and-checkably-backed* concerns per critique.
- **Theater rate: T (52%) ≫ B (33%) > S (11%).** Half the placebo's concerns are ungrounded; SPARRING's are mostly receipts. This is the "real or theater" result, quantified.
- **Precision (the cost): B (94%) > S (89%) > T (86%).** The over-flagging cost of the adversarial conditions is **real but small** — S gives up ~5 points of precision vs the neutral baseline to gain ~22 points of grounding. Honest reading: SPARRING is slightly noisier, far more verifiable.

## The sharpening finding: the grounding gap lives where the artifact is EXTERNAL

Grounding rate **by case** tells the real story:

| Case | artifact location | B | S | T |
|---|---|---|---|---|
| H1 (Sweller/CLT) | in the pack (#3) | 100% | 100% | 86% |
| H2 (15% cap) | in the pack (#7) | 100% | 83% | 57% |
| **H3 (CWE-640)** | **external (security canon)** | **0%** | **78%** | **0%** |

When the checkable artifact is sitting *in the pack*, everyone points at it — even the placebo. The conditions barely separate. **The entire grounding advantage concentrates in H3, where catching-and-grounding requires external knowledge (CWE ids, OWASP).** There, only the SPARRING Challenger — the agent with the *appsec evidence base* — grounded its concerns (CWEs cited); the neutral pass and the placebo caught the same gaps but on intuition (0% verified). That is the dual-evidence-base design doing exactly the job it was built for.

## Caveats (bounding what Phase 0 shows)

- **Single-substrate, same-vendor coding.** Three Claude coders, blind to condition but same family as the reviewers. Path B's *dual*-substrate (Claude + OpenAI) and the artifact-*verifier* (Path A) would make grounding a machine read rather than a knowledgeable coder's read. **Human audit (Bart) still pending.**
- **S is two agents.** It raised 36 concerns to B's 18 — roughly 2× the cost. Rates normalize for count, but the asymmetry is real; a fair efficiency comparison would weigh S against running B twice.
- **n is tiny** (3 cases, 75 concerns). Directional only.
- **Cases authored by the experimenter.** The seeded anchors are ours; generation bias is possible. The full run generates fresh.

## Verdict & recommendation

**Phase 0 passes: the v2 measure discriminates where binary catch could not.** Grounding rate and verified-grounded-TP rank S > B > T; theater rate ranks T > B > S; precision shows a small, honest cost for S. Proceed to Phase 1/2.

Two design refinements for the corpus, surfaced by the H3-concentration finding:
1. **Weight the corpus toward external-artifact defect types** (DC1 citations, DC3 CWE/security) where grounding actually discriminates; pack-internal contradictions (DC2) mostly don't separate the conditions and should be the minority.
2. **The artifact-verifier (Path A) is worth front-loading** — the one place the conditions separate is exactly where grounding must be checked against *external* truth (does CWE-640 really fit? does the citation resolve?), which is what the verifier automates and what a same-vendor coder can only approximate.
