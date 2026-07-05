# Hardened mini-proof — report

**Date**: 2026-06-26 · **Scope**: 3 hardened cases (misapplied real citation / buried contractual contradiction / subtle missing-control CWE) × 3 conditions (B bare neutral pass · S real two-agent dual-grounded ceremony · T placebo) — 12 reviewer agents, same-vendor (Claude). Applies deviations D1–D4. Purpose (D5): confirm the conditions actually separate before scaling to 20.

## In plain terms (Rosetta's read)

The one sentence first, then earned below: **the test couldn't tell the reviewers apart by *whether* they caught the mistake — they all caught it every time. The only real difference was *how* they caught it: one showed its receipts, the others just said "trust me."**

*What we did.* We wrote fake business recommendations and hid exactly *one* deliberate mistake in each — like a single wrong ingredient in a recipe. Then three kinds of reviewer looked for it: a **plain reviewer** ("does this look sound?"); the **real SPARRING setup** (two reviewers with *different* expertise, required to back every objection with something checkable); and a **fake challenger** (told to be skeptical but *not* required to back anything up — the impostor, to see if SPARRING does real work or just *acts* argumentative).

*What happened.* Everybody caught everything — 9 of 9 the first round, then 12 of 12 even after we made the mistakes genuinely sneaky (a real paper cited to say the *opposite* of what it says, a contract limit buried in fine print, a missing security lock hidden among good ones).

*Why that stings.* We **cannot** sell SPARRING as "it catches more mistakes" — a plain single look already catches them. A person might skim past a buried clause, but the AI reads every line and knows the whole field, so a *single* hidden error has nowhere to hide. Same wall an earlier study hit; now confirmed real.

*The result that counts.* The reviewers differed in **how** they caught things. Real SPARRING caught the mistake *and showed its work* — named the exact security rule, quoted the specific clause, said what the paper actually claims; you can check it. The impostor caught the same mistakes *on a hunch* ("this smells wrong") — often right, but no receipts. Real SPARRING also raised *more* objections, some over-reaching — more signal, more noise.

*So SPARRING's value, in one line:* not "finds more," but **"shows you receipts you can check"** — which matters enormously when an AI helps make a decision you must defend to a boss, an auditor, or a regulator. A verifiable answer beats one you must trust blindly; the price is a bit more noise.

*One honest caveat:* every reviewer here was the *same* AI (Claude). A *weaker* or *different* plain reviewer might genuinely miss things — the one door we haven't opened where "catches more" could still matter.

## Result: binary catch saturated AGAIN — 12/12

| Case | planted defect | B | S (Gen/Chal) | T |
|---|---|---|---|---|
| H1 | Sweller/CLT cited *backwards* to support parallel | caught | caught / caught | caught |
| H2 | schedule breaches buried 15% MSA cap (#7) | caught | caught / caught | caught |
| H3 | reset token not single-use (CWE-640), among sound controls | caught | caught / caught | caught |

The hardening did **not** restore discrimination on binary catch. Burial, misapplication, and "control-absent-among-many-present" all failed to make the bare neutral pass (B) miss — and the ungrounded placebo (T) caught every defect too.

## The deeper finding: defect difficulty for an LLM ≠ for a human

The hardening levers were designed for *human* missability — bury the fact at item #7, require knowing what Sweller actually claims, hide a missing control among present ones. **None of those hide a defect from a frontier model with the whole pack in context and broad domain knowledge.** The LLM reads all nine pack items reliably, knows cognitive load theory and the OWASP reset cheat sheet cold, and notices an absent control. So:

> **Binary defect-catch is not recoverable as a discriminating measure for SPARRING when the baseline is a strong, full-context single pass.** A single frontier pass already catches single planted defects, however buried. This is the same near-ceiling wall as V2 — now confirmed robust to defect-hardening.

## Where the conditions DID separate (confirms D2)

1. **Grounding quality — S ≫ T, decisively.** S-Chal grounded every catch in a checkable external artifact: *CWE-640 / CWE-256/312 / CWE-598 / CWE-352* and the OWASP Forgot-Password cheat sheet (H3); *MSA §9.3* plus the arithmetic showing 3 of 4 tiers are dead and the schedule is *worse* than the benchmark on severe outages (H2); *Sweller, van Merriënboer & Paas 1998* and the expertise-reversal effect (Kalyuga 2003), naming the split-attention mechanism (H1). T caught the same defects on intuition — "a contractual lie," "misreads its own source," "smells" — with no checkable referent. This is audit-grade vs. vibe, and it is the governance/explainability axis.
2. **False-positive / over-flagging — the adversarial conditions over-raise.** Most visible on H3: S-Chal returned **7 findings** where only **1** was the planted defect; several over-reached *past the pack* (flagged CSRF, rate-limit-as-enumeration-oracle, and re-flagged controls the pack explicitly said were present — sessions terminated #9, enumeration-safe #6, rate-limited #5). T over-flagged similarly. High recall, rich grounding, **low precision.**

## Verdict on the D5 gate

**Conditions separate — but only on the grounding/false-positive axis, not on binary catch.** That is a *confirming* result for the D2 pivot and a *disconfirming* result for the original "does SPARRING catch more" framing. Concretely:

- **Drop binary catch as a primary** (keep only as a saturated descriptive). With strong models it cannot discriminate.
- **The real, measurable claim is justification quality**: grounded SPARRING produces **auditable, externally-anchored** critiques where a placebo produces correct-but-ungroundable ones — at a **precision cost** (more false positives). That is exactly the governance/explainability value the preprint reframe and mechanism audit point at, and it is honest about the cost.
- **The artifact-verification spec is now on the critical path**, not a nice-to-have: it is what makes "grounding quality" *objective* (does each cited CWE/clause/paper actually check out?) instead of a judge's opinion, **and** it is the discipline that would penalize the over-flagging (an over-reach whose artifact doesn't verify gets caught). The pilot's primary measure becomes a direct read of the verifier's output.
- **Same-vendor caveat:** all agents were Claude. The ceiling may be partly a strong-uniform-model artifact; a genuinely *weaker or different* baseline (cross-vendor B) is the one remaining way binary-catch headroom might reappear — to be tested on the VPS harness, not assumed.

## Recommendation

**Do NOT scale the binary-catch design to 20.** Redesign the pilot around **grounding-quality + precision/false-positive as the sole primary**, build the artifact-verifier (P1–P2 of the spec) so that measure is objective, and only then scale — optionally with a cross-vendor weak baseline to check whether any catch-rate gap exists at all. The mini-proof did its job: it caught a second design-killer (and sharpened the real claim) before the expensive run.
