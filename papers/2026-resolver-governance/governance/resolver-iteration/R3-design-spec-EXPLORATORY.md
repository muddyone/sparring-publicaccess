# R3 — admissions-controlled iterate · DESIGN SPEC (EXPLORATORY)

**Status:** `EXPLORATORY PILOT — NOT PRE-REGISTERED.` This document is "specify before you
look" discipline, not a locked pre-registration. There is **no LOCK commit** and **no integrity
spine** for R3. Results from this condition are exploratory and are **firewalled from Paper 1**
(the Resolver = §6.3 + the locked iterate-to-agreement null). If R3 shows signal, *this pilot
becomes the basis for* a confirmatory pre-registration on the expanded ~16-problem set (the
"Paper 1.5" follow-on) — it does not pretend to be that confirmatory test itself.

**Date:** 2026-06-29 · **Provenance:** implements [`design-brainstorm-beyond-single-challenge.md`](./design-brainstorm-beyond-single-challenge.md) §2.1 + §4 + §5. **Reuses** everything from the locked study: the same 8 problems, the same R0 originals, the same ≥2-of-3 / 31-flaw denominator, the same dual-vendor harness and the same condition-blind DV scorer.

---

## 1. What R3 is

A fourth produce condition added to the existing harness. Same skeleton as **R2** (iterate
challenger ↔ producer to a terminal state on the same 8 problems, two vendor arms), with **one
thing added: an admissions gate on every producer revision.** A revision is committed to the next
round **only if** a fresh verifier panel attests it is *Pareto-improving under a severity-relative
bar*. Churny rewrites that trade one flaw for an equally-severe one are **rejected** and the
prior recommendation is retained.

This is the brainstorm's §2.1 "revision admissions control" — the only design with a structural
shot at dropping net flaws **below the single-pass floor**, which nothing in the locked study did.

## 2. The two design calls (locked for this pilot, per Bart 2026-06-29)

1. **New-flaw bar: SEVERITY-RELATIVE** (not strict "0 new"). A candidate patch is admissible iff
   it resolves ≥1 standing objection **and** every new material flaw it introduces is *strictly
   less severe* than the most-severe objection it resolves. Rationale: a fresh panel surfaces
   ~material things on *any* output (the new-flaw baseline in `results.md`); a literal "0 new" gate
   would veto good minimal patches on hallucinated regressions.
2. **Tier: PATCH-TIER ONLY** (no decision-fork tier in v1). Every objection is handled as a patch
   candidate; there is no "re-justify the core decision from scratch on a new branch" escape hatch.
   v1 deliberately tests the patch mechanism in isolation; the decision-fork tier is held for v2.

Severity scale (3-point, judged per-verifier, internally consistent): **1 = low** (minor
would-ship issue), **2 = medium**, **3 = high** (decision-changing).

## 3. The admissions gate (the load-bearing new component)

Per the brainstorm §4.3 caveat, the gate verdict rests on an LLM verifier, so it is a
**≥2-of-3 cross-vendor panel**, identical across both arms (only the *challenger* vendor varies by
arm, exactly as R1/R2). Three verifier members, each on a distinct lens (the same three audit
angles used by the DV scorer), one of them GPT-5.2 (cross-vendor member):

For each member, given PROBLEM + CURRENT rec + STANDING objections + CANDIDATE rec, the member
returns *judgments only*: which standing objections the candidate resolves (+ each one's severity),
and any NEW material flaw the candidate introduces (+ severity). **The admit rule is then applied
deterministically in code** (not trusted to the model's arithmetic):

```
member_admit = (≥1 objection resolved) AND (every new flaw severity < max severity among resolved)
gate_admit   = (members voting admit) ≥ 2          # majority of the 3-member cross-vendor panel
```

- **Admitted** → candidate becomes the new CURRENT; logged as a merged patch.
- **Rejected** → producer gets up to **2 attempts/round** ("tighter, please", told which new flaw
  blocked it); if still inadmissible, CURRENT is unchanged and the patch is logged as rejected.

Every gate decision — the three member votes, resolved set, new flaws, severities, verdict — is
written to the round log. That log **is** the governance trail (brainstorm §4.2): verifier-attested,
not self-reported.

## 4. Terminal states

- **CONVERGED** — challenger reports no material objection remaining on CURRENT **and** the last
  committed revision was producer-accepted. (Same as R2.)
- **EXHAUSTED** — a full round produced **no admissible improving move** (all patch attempts
  rejected by the gate) while objections still stand. This replaces R2's STALLED with the
  principled stop the brainstorm names: *"no open objection has an admissible (green) patch."*
- **CAPPED** — hit the round cap (CAP = 5, same as R2).

## 5. DV and scoring — UNCHANGED and condition-blind

R3 final outputs flow through the **exact same** stage-B scorer as R0/R1/R2/R1′: 3-auditor panel
(≥2 consensus) + remain-coding against the fixed 31-flaw denominator + new-flaw matching →
`net_flaws_remaining`. R3 is added to the order-rotated blind map so processing order carries no
condition signal. This is what makes R3 numerically comparable to the locked conditions.

## 6. The two pre-specified questions (write the answer-shape before looking)

1. **Decision quality.** Does R3 beat the single-pass floor on mean `net_flaws_remaining`?
   Benchmarks (from the locked run): single-pass **R1 = 2.625 same / 3.125 cross**; the best
   prior condition **R1′ = 2.25**; **R2 = 2.625 same / 3.0 cross**; R0 anchor = 3.875.
   - Pre-specified read: **R3 "clears the floor"** iff mean R3 < mean R1 in *both* arms, and is a
     **real win** iff mean R3 < 2.25 (below the best locked condition). A null is R3 ≈ R1/R2.
     n = 8 is underpowered by design — directional signal only; no confirmatory claim is drawn.
2. **Governance.** Does the gate emit a clean, verifier-attested accept/reject log as a byproduct?
   Pre-specified read: a pass = every committed change traces to ≥2 admit votes with a recorded
   resolved-set, and every rejected patch records the blocking new flaw + its severity. Legibility
   is judged on the emitted `analysis/r3-governance-trail.json`.

## 7. Exploratory deviations expected (and fine)

Unlike the locked study, R3 may be tuned mid-pilot (gate prompt wording, attempt count) — that is
*allowed* here precisely because it is exploratory. Any such change is noted in this file's
changelog below, not a prereg deviation ledger. The firewall (R3 stays out of Paper 1) is what
makes that freedom safe.

### Changelog
- 2026-06-29 — spec written; R3 built and run (see `r3-results.md`). **v1 cleared the floor in both arms.**
- 2026-06-29 — **v2 recalibration** (Bart-authorized, data-driven): added a global new-flaw budget
  (cumulative admitted new-flaw severity ≤ 3) + dynamic round cap (stop on EXHAUSTED, backstop 10),
  as condition `R3v2`. **Result: NEGATIVE — v2 worse than v1 in both arms (+1.25).** The budget did
  not fix warehouse-siting (single-bad-patch, not accumulation — the "running-total guard" diagnosis
  was wrong) and choked the improvement engine (18 budget-blocks → 12/16 EXHAUSTED early on dirty
  outputs). v1's leniency was load-bearing. **v1 (`R3`) stays the standing best.** See `r3v2-results.md`.
