# Phase-0 capture dry-run — results (v3)

**Date:** 2026-06-28 · **Pre-registration:** [`../pre-registration-v3.md`](../pre-registration-v3.md) §9 (LOCKED, tag `seeded-defect-prereg-v3-2026-06-28`).

**Goal (pre-reg §9):** generate ONE live case end-to-end, confirm the capture harness persisted all of §7 items 1–6, that the in-briefing fact-ids resolve, and that the verifier runs green on it — *before* generating the full corpus. This is the single step that would have prevented the v2 data loss.

## Case

`case-DC3-upload.json` — a freshly generated DC3 (security) case: a file-upload recommendation whose seeded anchor is serving untrusted uploads from the app's own origin with the original extension (stored XSS + **CWE-434** unrestricted upload), with realistic distractors (UUID names, AV scan, size cap). All six §7 items persisted: recommendation, briefing (3 facts with stable ids `#1`/`#2`/`#3`), prompts (B/S/T), outputs (B / S{generator,challenger,converged} / T), concerns (4, atomized), codings.

## 1. Capture gate — PASS (the §7 abort condition)

```
capture_check.py --phase capture v3-run/case-DC3-upload.json   -> PASS (exit 0)
capture_check.py --phase full    v3-run/case-DC3-upload.json   -> PASS (exit 0)
```

All six items present and self-consistent; every cited in-briefing fact-id resolves to a fact in this case's briefing. (The gate was independently shown to **ABORT** a lost-briefing case with exit 2 — `capture_check.py --selftest`.)

## 2. Verifier P1 resolution on the live case — all four concerns resolved

Built `dc3-upload.verifier-input.json` from the persisted case (briefing → `pack_text`) and ran `verify_grounding.py` (P1 resolution, no API keys):

| concern | cited artifact | backend | grounding | evidence |
|---|---|---|---|---|
| c1 (S) | `#2` (in-briefing) | **in-pack** | GROUNDED_VERIFIED | resolves in briefing: #1, #2 |
| c2 (S) | `CWE-434` (external) | **mitre-cwe** | GROUNDED_VERIFIED | CWE-434: Unrestricted Upload of File with Dangerous Type |
| c3 (B) | `#1` (in-briefing) | **in-pack** | GROUNDED_VERIFIED | resolves in briefing: #1 |
| c4 (T) | — (none) | none | UNGROUNDED | no checkable artifact cited |

**The headline result:** the two **in-briefing** concerns (`#1`, `#2`) machine-resolve **offline, no model in the loop** — exactly what v2 could *not* do, because in v2 the briefings were never persisted (only answer-keys were saved). v3's capture protocol closes that loss: in-briefing grounding is now a machine read, not a Path-B judgment. The external CWE resolved against MITRE; the ungrounded placebo concern was correctly called UNGROUNDED.

## 3. Verifier self-tests on this machine

- **P1 resolution:** 15/17 at dry-run → **17/17 after the fix.** The two initial failures were the **literature (Crossref) backend only**: `cite_check.py` is a **Loom shared skill** (`~/projects/loom/skills/shared/cite-check/scripts/cite_check.py`), not vendored into this repo, so the verifier's hard-coded repo-relative default (`pilots/cite-check/scripts/cite_check.py`) never resolved — in a worktree *or* a clone. **Fixed 2026-06-28:** `verify_grounding.py` now resolves the engine by searching `CITE_CHECK_PY` (env override) → repo-relative → the Loom install; the literature backend loads and resolves Crossref, and the self-test is **17/17 (ALL PASS)**. CWE, RFC, in-briefing, code, and none backends already passed.
- **P1.5 supports-judge wiring:** ALL PASS (offline). Live dual-substrate judge needs `ANTHROPIC_API_KEY` + `OPENAI_API_KEY` — not run here.
- **Claim→fact mapper wiring:** ALL PASS (offline). Live mapper needs `ANTHROPIC_API_KEY` — not run here (this case has no prose-only concern that needs mapping).

## Verdict

**Capture harness PROVEN on a live case.** All six items persist; the gate enforces the §7 abort condition; in-briefing fact-ids resolve through the verifier offline. The v2 failure mode (a lost briefing) is now caught up front and, more importantly, prevented — the briefing is persisted, so the verifier reaches the in-briefing families end-to-end. **Clear to proceed to Phase 1** (generate the remaining 11 cases); the one follow-up the dry-run surfaced — the `cite_check.py` engine path for the literature backend — is now **resolved** (§3), with the verifier self-test at 17/17.

## Honest caveats

This is an **instrumentation dry-run, not a scientific data point.** The case was generated, run through the conditions, and coded by a single substrate (Claude) in one session — fine for proving the *harness*, but the pre-registered run (Phase 1) requires the full blind, dual-substrate coding (§7 item 6) and, for legitimacy on technical specifics, the named domain-expert audit (§9 Phase 3). The live P1.5 judge and the claim→fact mapper were wiring-tested only (keys not supplied here).
