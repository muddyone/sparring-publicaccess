# Catch-rate v3 figures (§6.3)

Reproducible figures for the A-v3 (Test B) controlled catch-rate study. Generators read the
frozen `../results-*.json` and write byte-stable SVGs (fixed `svg.hashsalt`, `metadata Date None`).

> Data-graphics discipline (Minard, `docs/agents/minard.md`): earn the ink, tell the truth,
> make the uncertainty visible — and **consolidate, don't proliferate.**

## WIRED into the manuscript — ONE figure

- **`catch-rate-2x2.{py,svg}`** → **§6.3** of `pilots/llm-judge-2026-05-02/v2/preprint-draft.md`.
  The full Generator×Challenger×Audit 2×2×2 grid. It is the **only** catch-rate cut that preserves
  §6.3's load-bearing hedge: a challenge recovers 78–94% of flaws in all cells, but whether a
  *separate* challenger beats self-review is **generator-dependent** (large for Claude-produced
  work, marginal for GPT-5.2; the Claude blind-spot persists under a GPT audit → real, not
  same-vendor favoritism). Reads `../results-2x2-grid.json`.
  The rendered `.svg` is **copied** to `llm-judge-2026-05-02/v2/figures/catch-rate-2x2.svg` so the
  manuscript references it by a local path; regenerate **here**, then re-copy.

## CUT — NOT FOR THE MANUSCRIPT (kept for provenance only)

- **`catch-rate-v3.{py,svg}`** — single-vendor (Claude) 4-condition bar. Duplicates §6.3's in-text
  table (a clean 4-row table needs no chart) **and** re-flattens the generator-dependence hedge by
  presenting the Claude-only 87.1% challenger number as the universal result. Do not wire.
- **`catch-rate-v3-xvendor.{py,svg}`** — Claude-internal vs cross-vendor 2-series bar. Subsumed by
  the 2×2×2 grid, and it conflates the generator swap with the challenger swap (its "cross-vendor"
  series has GPT both producing and challenging). Do not wire.

> Note: "challenger" is sliced differently across these three artifacts — the single/xvendor bars
> use a *pooled* challenger (87.1% Claude-internal), while the grid *splits* same-vendor (90.3%) vs
> cross-vendor (93.5%) for the same Claude-gen/Claude-audit cell. Another reason to ship only the
> grid; if §6.3's table (87.1%) and the grid are both shown, the caption must say the table figure
> is a pooled challenger.

## Regenerating

```bash
python3 figures/catch-rate-2x2.py          # needs matplotlib; reads ../results-2x2-grid.json
# then copy into the manuscript figures dir:
cp figures/catch-rate-2x2.svg ../../llm-judge-2026-05-02/v2/figures/catch-rate-2x2.svg
```

## catch-rate-grid-plain-language

`catch-rate-grid-plain-language.png`, drawn by `catch-rate-grid-plain-language.html`.

A plain-language rendering of the same generator × auditor × condition grid as
`catch-rate-v3-xvendor.svg`, written for a working engineer rather than a reader of the paper.
Every value is read directly from `../results-2x2-grid.json`; nothing is rounded differently or
re-derived.

It carries the **NEUTRAL** condition in a separate strip below the grid, because that condition is
what separates "fresh eyes" from "an adversarial instruction" — and on Claude-written work it
lands *below* self-review. A version of this figure that omits it invites the reader to credit the
gain to non-authorship, which the data does not support.

To re-render: open the HTML, set `document.documentElement.style.zoom = '2'`, screenshot full-page.
