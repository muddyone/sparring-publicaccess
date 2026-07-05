---
figure: fig5-gate-null
target: OpenAI gpt-image-1 (/v1/images/edits, 1536x1024, high)
reference: submission/figures/fig5-gate-null.png (existing script-generated original, attached as edit reference)
status: DRAFT
mode: style-study — NOT data-accurate, never a replacement candidate
---

USE CASE: An exploratory alternate-style rendering of an existing, data-accurate
academic figure, for a reviewer (Minard) to compare against the committed
original. STYLE STUDY ONLY — you cannot see the underlying dataset; treat every
number/label/bar-length in the reference as an approximate visual cue for
composition, not a value to reproduce exactly.

WHAT THE CHART ARGUES (for compositional context only): a stacked horizontal
bar chart, one bar per experimental condition (roughly four conditions), each
bar split into two segments — a "still-present" segment (the reviewing
process's remaining miss rate) and a "newly introduced" segment (fresh problems
the revision itself created). Lower total bar length is better. The finding is
that the two segments roughly cancel across conditions, so the total bars land
close to equal length — that near-equality IS the point, not an artifact to
hide.

VISUAL GOAL: an honest, zero-baseline stacked horizontal bar chart, restrained
academic palette (e.g. one cool color for "still-present", one warm color for
"newly introduced"), serif typography, minimal chartjunk, generous whitespace.
The near-equal total bar lengths across conditions should read as clearly
equal, not be visually distorted to look otherwise. Explore a different
compositional treatment than the reference (e.g. different segment ordering
or annotation style) as a style alternative.

CONSTRAINTS:
- Landscape, roughly 3:2.
- Zero-based baseline — no truncated axis.
- No 3-D, no gradients, no rainbow color, no decorative icons.
- Text need not match the reference verbatim — this is a style comparison,
  not a publication candidate.
- Quality: high-fidelity, crisp, print-quality static figure.
