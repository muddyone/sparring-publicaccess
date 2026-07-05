# SPARRING mechanism audit — does the Challenger actually matter?

**Date**: 2026-06-26
**Question**: Across the SPARRING ceremonies we have actually run, how often was the Challenger *load-bearing* — i.e. did it change the converged recommendation, or catch a specific error/risk the opening pass missed — versus producing presentation theater?

This is the **mechanism** question, deliberately distinct from the V2 blind-rater study. The V2 study asked "do uninvested strangers prefer the SPARRING *output*?" (answer: no measurable preference). This audit asks "did the SPARRING *process* change or correct the decision?" — a different claim, measured against the work itself.

---

## The bar (set by Bart)

The Challenger counts as **load-bearing** only if it either:
- **changed the converged recommendation** materially (a replaced approach, a reversed call, a dropped/added option family, a real scope change), **or**
- **surfaced a specific error/risk the opening pass missed** that would plausibly have shipped otherwise.

Cosmetic / wording / framing changes — *"presentation theater"* — do **not** count, unless the wording itself was the substance of the decision.

## Method

1. **Extraction.** Swept every registered project's git repo **and** every Claude Code session transcript under `~/.claude/projects/`. 47 candidate ceremony blocks → 35 genuine candidates after dropping skill-definitions, pre-registrations, the v1 preprint, reference docs, and chatlogs.
2. **Lenient coding.** 35 parallel agents, one per ceremony, each classifying real-run-vs-not and coding against the bar. Result: 24 real ceremonies, 11 not (single-turn prompts, status notes, design specs — correctly filtered).
3. **Adversarial verification.** Because near-universal "mattered" is a red flag, a second, independent pass of 24 skeptical judges re-scored every real ceremony **refute-by-default** against a strict reading of the bar.

Raw data: [`ledger.jsonl`](./ledger.jsonl) (one coded row per real ceremony, both verdicts + provenance + quotes), [`raw-lenient-coding.json`](./raw-lenient-coding.json), [`raw-strict-verify.json`](./raw-strict-verify.json).

---

## Result — base rate

| Pass | Load-bearing | Rate |
|---|---|---|
| Lenient (per-ceremony coder) | 23 / 24 | 96% |
| **Strict adversarial re-judge** | **16 / 24** | **67%** |

The strict pass downgraded **7** ceremonies the lenient pass had called load-bearing. The downgrades are the verifier working as intended:

- **loom 022** (post-remediation eval) — "8 elaborately-cited residual gaps (Leveson/Vaughan/Dekker…)" judged **presentation theater**: lots of citation, no change to what gets built.
- **resourceforge 006 / 007 / 008** — single SPARK-phase task-notification fragments, not full runs; wording/jargon polish on marketing copy.
- **lifspel 042** (racial-taxonomy naming) & **TerraClarity Case A 044** — the converged call was **identical to the Generator's opening**; the Challenger added residuals but didn't change the decision. *(Note: 044 is one of the V2 study cases — consistent with the study's own finding that Case A's core call didn't move.)*
- **sparring 018** (submission-worthiness) — Generator opened with the decision already settled.

## The honest caveats (these bound what we can claim)

1. **Survivorship bias — the big one.** This is the corpus of ceremonies that left a *saved artifact or a rich transcript*. People save the **hard, contested** decisions. The trivial spars that didn't matter were never saved. So **67% is "of the ceremonies substantial enough to leave a trace, the Challenger was load-bearing in two-thirds"** — NOT "two-thirds of all spars matter." Bart's lived "9 of 10 don't matter" intuition is about *all* spars including the throwaways; this audit can't see those. **Only the going-forward ledger (below) can measure the true all-ceremony base rate.**
2. **Small n.** 24 ceremonies. Directional, not precise.
3. **LLM-coded.** Both passes are model judgments, not human adjudication. The strict pass corrects *leniency*; it cannot correct *survivorship*.

So the defensible sentence is: **"Among the SPARRING ceremonies substantial enough to be recorded, an adversarially-verified two-thirds had a load-bearing Challenger — it changed the decision or caught a real defect, not just dressed it up."**

---

## Case-study shortlist (survives strict verification, real product/engineering decisions)

These are the strongest documented instances — *real* product work, not the study's synthetic cases, where the Challenger demonstrably mattered:

- **loom — auth standardization (14.2).** Challenger caught that the minimal tier's identity stubs run `auth=open|none` and therefore **fail OPEN** (unresolved identity silently authorized) — a secure-defaults inversion that would have shipped under the proposed flat opt-in. Reversed the recommendation to a mandatory fail-*closed* identity contract.
- **loom — security baseline (14.4).** Challenger reversed a proposed **hard per-account lockout** as a **DoS footgun** (CWE-307: low-entropy cohort usernames let anyone lock out real users), replacing it with throttle + backoff, and added a break-glass recovery path for the sole-admin lockout case the opening missed (CWE-640).
- **loom — runtime/surface architecture (Phase 14).** Challenger flagged that an "additive field" was quietly **smuggling the full EIP Request-Reply pattern** (return address, correlation id, dead-letter channel, idempotent receiver) — a scope explosion the opening framed as trivial.
- **lifspel — motion-accuracy coupling (CRv2).** Challenger pushed back with historical evidence (May 2007 ch.3; Karasulas 2004) that *trained* mounted archers still degrade at gallop — forcing a change to the curve-shape design.
- **resourceforge — landing-page honesty.** Challenger refused to ship marketing copy claiming Loom "builds the page" (it's hand-written PHP) and that personas are a "standing crew that coordinate across projects" (they're invoked in-session, no autonomous runtime) — catching **false claims about our own product** before they went live. *(This honesty catch recurs across ceremony rounds 005/010/011/012 — count it as one decision, not four.)*

**Distinct, verified, real-product case studies: ~5** (3 loom, 1 lifspel, 1 resourceforge). That is a real, citable evidence base for "SPARRING catches things that would have shipped" — the process claim, not the blinded-output claim.

---

## Going forward — the prospective instrument

A retrospective dig can only ever approximate this. The fix is auto-capture: `/spar` and `/full-sparring` now self-code each run against this same bar and append to a per-project `docs/spars/ledger.jsonl` + a global roll-up (loom branch `spar-ledger-autocapture`, pending rollout). Within weeks that yields the **prospective, unbiased** base rate across *all* ceremonies — trivial ones included — which is the number that actually answers Bart's "9 of 10" intuition, honestly collected from the start.
