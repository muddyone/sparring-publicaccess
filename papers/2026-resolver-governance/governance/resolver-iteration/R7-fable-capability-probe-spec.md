# R7 — Fable-5 capability-ceiling probe on the gate discrimination wall (EXPLORATORY spec)

**Status:** `EXPLORATORY · n=61 candidate decisions · DV frozen · prompt frozen.` One decisive,
bounded probe that slots in as the **third lever** alongside R6's two (de-noise the DV, few-shot the
gate). Source it will produce: `analysis/r7-fable-probe.json`, `scripts/r7_fable_probe.py`.

## The question it answers

R6 established the wall is **discrimination, not calibration/rate**: static verifier, challenge gate,
and recrafted gate all sit at balanced accuracy ≈ 0.50–0.59 (κ ≈ 0.19 / 0.02 / 0.00). Framing only
moves the block rate. The mounting negative-result claim is: *"LLM gating may not be able to reliably
discriminate material regressions on this evidence."*

Before that claim is written, one thing is unruled-out: **is the ceiling the model, or the task?**
Every gate variant R3→R6 ran on `claude-opus-4-8` (+ `gpt-5.2`). If the single most capable available
model can't discriminate either, the "model" explanation is closed and the negative result gets much
harder to attack in review. If it *can*, the whole program was capability-bound and the limit claim
was wrong. This is the exact discipline the project already enforces: rule out the instrument (here,
the model tier) before declaring a fundamental limit.

## Design — one thing changes, everything else frozen

Identical to `r6_gate.py` — same 61 candidates, same `RECRAFTED_GATE_SYS`/`_USER` prompt, same
DV-truth, same panel composition (2+1), same severity-sweep + prompt-verdict metrics, same
train/test split. **The only change: the two Claude panel members upgrade `claude-opus-4-8` →
`claude-fable-5`.** GPT-5.2 member unchanged, to hold panel composition constant for a clean A/B
against the existing R6 numbers.

| arm | Claude tier | panel | purpose |
|---|---|---|---|
| **R6 (reference, already run)** | `claude-opus-4-8` | 2 opus + 1 gpt-5.2 | baseline discrimination |
| **R7-A (primary)** | `claude-fable-5` | 2 fable + 1 gpt-5.2 | does frontier tier move discrimination? |
| **R7-B (add-on, ~$8)** | `claude-fable-5` | 3 fable solo | remove GPT as a discrimination drag — pure Fable ceiling |

R7-B is cheap insurance: if the mixed panel stays flat, a 3×Fable solo panel rules out "GPT dragged
the vote." Run it only if R7-A is flat.

## Decision rule (this is the point — read before running)

Discrimination is read from **balanced accuracy and Cohen's κ**, *not* recall or block rate (framing
already controls those). Compare R7-A against the R6 reference on the same 61 rows:

| R7-A result | Interpretation | Action |
|---|---|---|
| balAcc / κ **rise materially** (κ clears ~0.35, balAcc clears ~0.65) | Capability *was* the binding constraint. The limit claim is falsified. | Re-open the gate program on Fable; drop the "fundamental limit" framing. |
| balAcc / κ **stay at chance** (κ ≈ 0, balAcc ≈ 0.50–0.55) | Frontier tier doesn't help → **not** a capability ceiling. | Hardens the negative result. Proceed to the label-noise cross below. |

**Confound with label noise — the one interaction that matters.** R6's #1 lever is de-noising the DV
(only 11/61 rows are "regressions," DV is ±1 noisy). A flat R7-A on the *current* noisy labels is
**confounded**: you can't tell "frontier model can't discriminate" from "the labels are noise, so
nothing can." So the clean design **crosses R7 with the de-noise step**:

```
                     current (noisy) DV-truth        de-noised DV-truth (replicate k≈5)
  opus-4-8 gate      R6            (κ≈0.00)          R6'   (rerun on clean labels)
  fable-5  gate      R7-A          (this probe)      R7-A' (rerun on clean labels)
```

- R7-A **rises** on noisy labels → decisive on its own (capability was a lever). Stop; don't need the cross.
- R7-A **flat** on noisy labels → run R7-A' after de-noising. Only if *both* opus and fable stay flat
  on *clean* labels is the "LLM gating can't discriminate material regressions" claim clean and
  publishable. If fable rises on clean labels but opus didn't, the story is "needs both a frontier
  model and clean labels" — still a real finding.

Ordering: de-noise (R6 lever 1) is the gating dependency. Run R7-A now on noisy labels (cheap, might
be decisive immediately); hold R7-A' until de-noised labels exist.

## Implementation notes (Fable-specific, will bite if ignored)

`lib_llm.call_claude` sends no `thinking` param and `max_tokens=2000`. On Fable that breaks:

1. **Thinking is always on and billed as output.** `max_tokens=2000` risks truncating (thinking +
   JSON verdict) → `extract_json` fails → 6 wasted retries. Raise to `max_tokens≈8000` and set
   `output_config={"effort":"low"}` (gate is decision-only; low effort is right and caps cost).
2. **Never send `thinking:{type:"disabled"}`** — 400 on Fable. Omit the param (lib_llm already does).
   `temperature` already not sent (good — also 400 on Fable).
3. **Refusals are HTTP 200, not errors.** The challenger/gate framing ("introduces a defect", attack
   the revision) can trip Fable's classifiers. A refusal returns `stop_reason:"refusal"` with empty
   content → silently parses to `{}` → defaults to ADMIT → **biases the gate toward admit and
   contaminates the discrimination measurement.** Handle explicitly: enable server-side fallback
   (`betas:["server-side-fallback-2026-06-01"]`, `fallbacks:[{"model":"claude-opus-4-8"}]`), **tag the
   served model per member**, and report the refusal/fallback rate. Sensitivity check: recompute
   metrics excluding candidates where any member fell back to opus — if the number that fell back is
   non-trivial, the "Fable ceiling" reading is partly an opus reading.
4. **Cost:** 2 Fable calls × 61 = 122 calls; ~2k in / ~1.5k out (incl. thinking) at $10/$50 per MTok
   ≈ **$12** for R7-A, +~$8 for R7-B (3rd Fable member). GPT unchanged/negligible. Whole probe < $25.

## What this does NOT do

It does **not** touch the cross-vendor adjudication substrate — Fable stays out of the GPT slot; the
2+1 panel keeps its GPT member precisely so vendor diversity is unchanged and only the *Claude tier*
varies. This is a capability probe, not a substrate swap.

## Deliverables

- `scripts/r7_fable_probe.py` — drop-in, resumable (`r7fable__{aid}` cache keys), reuses R6's prompt,
  DV-truth construction, and metrics verbatim; only the Claude call path changes.
- `analysis/r7-fable-probe.json` — R7-A (+ R7-B if run) severity sweep, prompt verdict, train/test,
  refusal/fallback rate, and the sensitivity metric, laid out for direct side-by-side with
  `analysis/r6-gate.json`.
- `r7-fable-probe-findings.md` — the decision-rule table filled in.
