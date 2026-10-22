# Deviations from the pre-registered design

Every departure from [`design-note.md`](design-note.md) (locked at tag
`gopnik-prereg-2026-10-16`), with when it was made and what outcome data existed at the time.
Numbering starts at D1.

## D1. Gemini dropped; the study runs on three models (2026-10-17)

**What changed.** `gemini-3.1-pro-preview` is removed from Stage 0b and the main run. The study
runs on `claude-opus-5-5`, `gpt-6.1-sol` and `grok-4.7`. §5.1's pooled effect and §5.3's p₀ are
averaged over three models instead of four. Nothing else changes.

**Why.** Gemini's API account allows 250 requests a day for this model. The error says
`generate_requests_per_model_per_day, limit: 250`. In Stage 0b, Gemini's first 44 calls
completed, over about two minutes. Every call after that was refused with HTTP 429, so no Gemini
sequence finished. The main run needs about 8,000 Gemini calls, over a month at
that cap. Bart chose to drop it rather than raise the quota or substitute an unchecked model.

**Effect on the analysis.** The sample-size formula is per model, so pooling over three models
is still conservative (§5.3). The per-model secondaries (§5.2) count out of three. Vendor
coverage falls from four to three. That limits generality, and it will be stated in the result.

**Data at the time.** Claude, GPT and Grok had each completed their 20 Stage 0b sequences.
**None had been scored.** No accuracy, baseline or n had been computed or viewed before this
decision. The 44 completed Gemini calls are in `runs/baseline/calls.jsonl`. The refused calls
are not logged, because the logger records only completed calls. No Gemini sequence record was
written.

_Corrected 2026-10-20: this entry first said that every Gemini call was refused and that the
failures were in the call log. The log shows 44 completed calls and no failures. Neither the
reason for the change nor its effect is altered._
