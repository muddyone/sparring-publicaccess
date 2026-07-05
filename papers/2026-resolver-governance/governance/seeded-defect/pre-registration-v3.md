# Seeded-Defect Pilot — pre-registration **v3** (capture-everything + verifier-backed end-to-end) — DRAFT

**Pilot id**: `sparring-seeded-defect-pilot-2026-06` (v3)
**Status**: **LOCKED 2026-06-28** (partner sign-off, Bart Niedner). Tag: `seeded-defect-prereg-v3-2026-06-28`. Design frozen before any v3 case is generated.
**Execution**: **Path A (verifier-backed, end-to-end)** for grounding adjudication, made possible by the capture protocol (§7) — the v2 data loss closed. Path B (dual-substrate judge) retained as cross-check and fallback.
**Supersedes**: [`pre-registration-v2.md`](./pre-registration-v2.md) (v2, Path-B interim). v2 stays in the repo for provenance; its result is the directional first-signal v3 confirms. v1 ([`pre-registration.md`](./pre-registration.md)) remains for the full lineage.

> **Terminology.** This document uses **"briefing materials" / "the briefing"** for what v2 called the *"pack" / "decision pack"* — the per-case context and fact-checked reference facts a condition reviews. Same object, clearer name.

---

## 1. Why v3 (one paragraph)

v2 measured grounding through a **Path-B** judge (an AI coding an AI) because the per-case **briefing materials were never persisted** — only the answer-keys were saved (`v2-run/cases.json`), so the verifier could resolve only the ~7% of concerns that cite an *external-canon* artifact (CWE/RFC/DOI) and the remaining ~76% stayed expert-coded. That gap was a **data-loss artifact, not a design limit**: the in-briefing resolver and the claim→fact mapper already exist and are demonstrated (preprint §8 / §10.2 / §11). **v3 changes exactly one thing: it persists everything (§7), so the verifier runs end-to-end and the grounding rates become a machine read for the *majority* of concerns, not just the external slice.** The design, conditions, unit, and measures are otherwise **identical to v2** — v3 is a **confirmatory replication** of v2's directional S-over-T grounding result under objective (Path-A) adjudication, not a new experiment.

## 2. The question (unchanged from v2)

> When reviewing a flawed recommendation, does a **grounded, dual-evidence SPARRING ceremony** produce critiques that are (a) more **verifiably grounded** and (b) at least as **precise** as a single neutral pass and a placebo challenger that performs disagreement without grounding?

The S-vs-T contrast remains the "real or theater" test, measured on grounding. **SPARRING can still lose this**; the pre-committed null (§5) stands.

## 3. Unit of analysis (unchanged + one addition)

The unit is the **individual concern**, each coded on two axes (as in v2):

- **Legitimacy** — `TRUE_POSITIVE` | `FALSE_POSITIVE`, adjudicated against the case + briefing + (for the seeded anchor) the answer key.
- **Grounding** — `GROUNDED_VERIFIED` | `GROUNDED_REFUTED` | `UNGROUNDED`.

**Addition (v3): concern atomization.** Each emitted critique is decomposed into atomic concerns — *one checkable claim per concern* — before coding, so the grounding/support judgment has a single artifact and a single claim to resolve (preprint §11). The atomization rule is fixed at lock and applied blind to condition.

## 4. Primary & secondary measures (unchanged from v2 + verifier coverage)

- **Grounding rate** = `GROUNDED_VERIFIED` / all concerns. *(primary — theater test)*
- **Verified-grounded-TP rate** = (`TRUE_POSITIVE` ∧ `GROUNDED_VERIFIED`) / all concerns. *(primary — auditability composite)*
- **Precision** = `TRUE_POSITIVE` / all concerns raised. *(primary-cost)*
- **Theater rate** = (`UNGROUNDED` ∨ `GROUNDED_REFUTED`) / all concerns. *(secondary)*
- **Seeded-anchor recall** — descriptive only (saturates ≈100%), as in v2.
- **Verifier coverage (NEW, descriptive):** share of concerns whose grounding was resolved by the verifier **without** falling back to a human/Path-B judge — reported per artifact backend (external registry / in-briefing fact / code / mapper-recovered). This is the number Figure-3 *should* have reported; v3 measures it directly instead of inferring it from a data-loss map.

## 5. Hypotheses (now confirmatory — directional, not powered)

Identical to v2; **status upgraded from exploratory to confirmatory**, since v2 already produced the directional signal and v3 replicates it under objective adjudication.

- **H1 (theater test, primary):** grounding rate **S > T**.
- **H2 (auditability composite, primary):** verified-grounded-TP rate **S > B** and **S > T**.
- **H3 (precision cost, honest):** precision **S vs B vs T**, reported whichever way it falls.
- **Pre-committed null:** grounding rate **S ≈ T** ⇒ the artifact discipline is theater ⇒ reported plainly.

## 6. Design (unchanged from v2)

- **~12 cases** across domains, each with **one seeded anchor defect** from the four families (security/CWE, citations, overclaim-vs-spec, buried contradiction), embedded in fact-checked briefings. *Same n and same taxonomy as v2 — this is a replication, not a scale-up.* **Resolved (Bart 2026-06-28): n = 12, for parity with v2.**
- **Conditions** (unchanged): **B** (bare neutral pass) · **S** (real `/spar` ceremony — two agents, genuinely different evidence bases, artifact discipline, converge) · **T** (placebo — structurally similar disagreement *without* the artifact discipline or distinct evidence). **B-weak (a weaker/cross-vendor single pass that probes whether SPARRING's edge widens when the baseline reviewer isn't already near-ceiling): dropped (Bart 2026-06-28),** as in v2's core — not part of the grounding/precision contrast; may be added in a later study.

## 7. Capture protocol — the core change (the v2 data loss, closed)

Everything below is **persisted to immutable per-case files at generation/run time**, before any coding or verification. The harness is the deliverable that distinguishes v3 from v2.

**Per case, v2 saved only:** `id`, `defect-class`, `domain`, `answer_key`. **v3 additionally persists:**

1. **The generated recommendation** (the flawed artifact under review) — verbatim.
2. **The full briefing materials** — the context *and* the fact-checked reference facts, each fact carrying a **stable fact-id** (e.g. `F#3`, `§2`) so in-briefing concerns are machine-resolvable.
3. **The exact prompts** issued to every condition (B/S/T), verbatim.
4. **Every condition's full output** (for S: both roles' transcripts and the converged critique).
5. **Every concern as emitted**, with its **cited artifact string** exactly as written, linked to its atomized form (§3).
6. **The blind codings** (legitimacy + grounding) with coder identity/substrate and timestamps.

**Integrity rule:** generation is **AI-produced and non-reproducible** (re-generating yields different text), so a concern is admissible only if items 1–5 for its case were captured **before** coding began. A case missing any of 1–5 is void and regenerated — the failure mode v2 hit is now a pre-registered abort condition, not a post-hoc discovery.

## 8. Grounding adjudication — Path A, end-to-end

With the briefings persisted (§7), grounding is a **machine read** for the majority of concerns:

- **P1 — resolution (no model):** route each concern's cited artifact to its backend — external registries (**MITRE/CWE, Crossref/DOI, IETF datatracker**), the **in-briefing backend** (resolve `F#n`/`§x` against the saved briefing), the **code/working-tree backend**, and **web-URL** fetch. Existence is confirmed mechanically; an `unverifiable` artifact is a durable state, never silently upgraded.
- **P1.5 — supports-claim judge, dual-substrate (Claude + OpenAI):** for a resolved artifact, judge whether it actually *supports* the concern; surface disagreement rather than force convergence.
- **Claim→fact mapper, dual-substrate:** for concerns grounded by *reading* the briefing with no explicit token (v2's ~57% bucket), map the prose claim to the briefing fact it relies on, then resolve via the in-briefing backend. This is the tool that turns Path-A from "external slice only" into "majority coverage."

**Path B (dual-substrate judge) is retained** as (a) a cross-check on a pre-committed sample of Path-A verdicts, and (b) the adjudicator for any concern the verifier marks `unverifiable`. Every concern's final grounding label records **which path produced it.**

**Legitimacy (TP/FP)** is adjudicated against case + briefing + answer key, blind to condition, by a **domain-expert audit** (§9 Phase 3) — **not** the author. Per the project validation stance (preprint §10.1), *author-as-domain-auditor is the wrong design*: the cases reach into specific CWEs and I-O-psychology citations the author cannot personally adjudicate. The author's role is to set the validation strategy and vouch for the honesty of the framing, not to code technical legitimacy. The verifier does **not** cover legitimacy — that axis is the expert's. _(The original lock read "author audit ≥25% as the interim" — an erroneous v2 carryover; **corrected post-lock 2026-06-28**, see §12.)_

## 9. Phasing (cheap first; prove the instrumentation before spending)

- **Phase 0 (do first — the v2 lesson):** a **capture dry-run on ONE case.** Generate one case end-to-end and confirm the harness persisted all of §7 items 1–6, the in-briefing fact-ids resolve, and the verifier + mapper run green on it. *No full generation until the capture harness is proven on a live case.* This is the single change that would have prevented the v2 data loss.
- **Phase 1:** generate the ~12-case corpus with the proven harness; run B/S/T; persist everything (§7).
- **Phase 2:** run the verifier + mapper end-to-end (Path A); Path-B cross-check on the pre-committed sample; atomize + code; analyze §4. Report **verifier coverage** as a real result.
- **Phase 3 (separable, may run after/in parallel — the weeks-scale human axis):** domain-expert **legitimacy** audit on the technical specifics (security, I-O-psych citations) the author cannot adjudicate (preprint §10.1). Not on the machine pipeline's critical path.

## 10. Validity threats (pre-stated)

- **Capture completeness** → Phase-0 dry-run + the §7 abort condition guard against a repeat of the v2 data loss.
- **Circularity** → grounding verified against external truth + the saved briefing; legitimacy against the answer key + the named expert audit; dual substrates; cross-check sample.
- **Judge subjectivity on grounding** → Path A removes it for resolved artifacts; the dual-substrate supports-judge + mapper surface disagreement; Path-B labels any residue.
- **Blind coding** → adjudicators never see which condition produced a concern.
- **Same-vendor ceiling** → ceremony agents and the supports-judge still share a vendor family on the Claude side; the cross-vendor (OpenAI) judge half mitigates, not eliminates. Stated, not assumed away. **Resolved (Bart 2026-06-28): no cross-vendor coder arm in v3 — left for a later study, to keep the design identical to v2.**
- **n / generalization** → ~12 synthetic cases; per-concern gives many data points but few cases — directional, no inferential significance claimed; no generalization beyond the synthetic taxonomy.

## 11. What it can / cannot claim

- **Can (new in v3):** report the S-vs-T grounding separation under **objective, machine-resolved (Path-A) adjudication end-to-end** — closing v2's "an AI graded an AI" gap for the *majority* of concerns — and report **real verifier coverage** rather than a data-loss-bounded 7%.
- **Cannot (unchanged from v2):** a catch-rate superiority claim (retired); a **legitimacy** claim on technical specifics without the §9 Phase-3 expert audit; real-world decision improvement (the later ecological study); or generalization beyond the synthetic taxonomy.

---

### Sign-off checklist (Bart) — signed 2026-06-28
- [x] Capture protocol (§7) — the six persisted items + the abort condition — acceptable
- [x] Path A end-to-end (verifier P1 + dual-substrate supports-judge + claim→fact mapper) as primary grounding adjudication; Path B as cross-check/fallback
- [x] Concern atomization rule (§3) acceptable
- [x] Confirmatory (not exploratory) hypothesis status (§5) acceptable
- [x] Phase-0 single-case capture dry-run before any full generation
- [x] `[OPEN]` items resolved (Bart 2026-06-28): **n = 12** · **B-weak dropped** · **cross-vendor coder left for a later study**
- [x] → **locked + tagged** `seeded-defect-prereg-v3-2026-06-28`

## 12. Deviation ledger (v3, post-lock)

_Departures from the frozen v3 design, with date + rationale._

- **2026-06-28 (same-day post-lock correction).** §8's "**author audit ≥25%** as the interim" for legitimacy is **withdrawn**. It was an erroneous carryover from the v2 pre-registration and contradicts the project's established validation stance (preprint §10.1): *author-as-domain-auditor is the wrong design*, because the cases reach into technical specifics (CWEs, I-O-psychology citations) the author cannot adjudicate. Corrected design: **grounding** objectivity is delivered by the Path-A verifier (no human needed — done); **legitimacy** routes solely to the named **domain-expert** audit (§9 Phase 3); the **author's role** is to set validation strategy and vouch for framing honesty, not to code technical legitimacy. **Not data-dependent:** the §10.1 stance predates this run; this only removes an internal inconsistency, and §9 Phase 3 already reflected the correct routing.
