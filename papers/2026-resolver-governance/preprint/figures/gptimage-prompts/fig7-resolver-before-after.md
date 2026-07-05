---
figure: fig7-resolver-before-after
target: OpenAI gpt-image-1 (/v1/images/edits, 1536x1024, high)
reference: submission/figures/fig7-resolver-before-after.png (existing hand-authored diagram, attached as edit reference — has known rendering defects, see FIX LIST)
status: DRAFT
mode: redesign-candidate — no underlying dataset, diagram-clarity task
---

USE CASE: A corrected, more polished render of an existing hand-authored
schematic diagram for an academic preprint. Reproduce the SAME structure and
SAME text verbatim — this is a defect-fix and polish pass, not a content
change. The reference image has specific known rendering problems (listed
below under FIX LIST) that must NOT be reproduced in the new render.

DIAGRAM CONTENT (reproduce exactly):
Title (top, centered): "The test that reshaped the Resolver: iterate-to-
agreement out, one grounded pass in"

TOP PANEL, labeled "BEFORE · ITERATE-TO-AGREEMENT (AS FIRST BUILT)" —
four boxes left to right, connected by rightward arrows:
1. "proposal in"
2. "challenge ⇄ revise" / "N rounds · until both agree" — this box has a
   small looping "×N" arrow above it indicating repetition
3. "both-must-agree gate" / "proposer can't close alone"
4. "answer" / "(single part)"

From box 2, a gray downward-diagonal arrow to the bottom panel, labeled:
"collapses to one pass / pre-registered null (n = 8) / §6.4 / Fig 5"

From box 3, a dark-red downward arrow ending in a red "X" mark, labeled
"gate retired as a default stage / (optional sign-off only)"

From box 3, a second, separate teal downward arrow to the bottom panel,
labeled "its one job → report disagreement"

From box 4 ("answer"), a teal downward arrow to the bottom panel, labeled
"carried, unchanged"

BOTTOM PANEL, labeled "AFTER · THE ACCOUNTABILITY PASS" — five boxes left
to right:
1. "S1 · One grounded pass" / "run once, then stop" — solid teal outline,
   receives the gray arrow from box 2 above; has a small pill/badge attached
   reading "+ verifier §8"
2. "S2 · Definitiveness gate" / "exploratory → §12" — dashed outline
3. "S3 · The answer" / "the deliverable" — solid GOLD-filled box (the one
   deliverable, visually distinct from all others)
4. "S4 · Trust rider" / "exploratory → §12" — dashed outline, receives the
   "its one job → report disagreement" arrow from box 3 above
5. "S5 · Anchored correction" / "exploratory → §12" — dashed outline

Below the row: small italic "new" labels under S2 and S5. A centered line:
"operating order: S1 → S5 → S2 → S3 + S4"

Legend line near the bottom: "solid = measured (S1) · dashed = exploratory
(§12) · gold = the deliverable · X = retired stage · grey = the null that
drove the change"

Final italic caveat line at the very bottom: "S1 is pre-registered and
measured (directional, n = 8); S2/S4/S5 are exploratory, confirmatory test
pending (§12). A design-evolution schematic — not an effect size."

FIX LIST (the specific defects in the reference render — correct all of these):
1. Remove the two short, disconnected diagonal tick-mark line fragments that
   appear near the top-left corner of the "S1 · One grounded pass" box in the
   reference — they connect to nothing and read as stray artifacts. Every line
   in the new render must visibly start at one box and end at another (or at
   its label) — no floating line fragments anywhere.
2. Use ONE consistent connector style throughout the whole diagram: right-angle
   ("elbow"/orthogonal) connectors only, not a mix of free diagonal lines and
   right-angle bends. Every arrow — including the gray "collapses to one pass"
   arrow, the red "gate retired" arrow, the teal "report disagreement" arrow,
   and the teal "carried, unchanged" arrow — should share the same elbow-
   routing style and the same corner radius, so the connector grammar reads as
   one system rather than several improvised ones.
3. Route every connector so it never crosses through any text. In the
   reference, the elbow line from "both-must-agree gate" down to S4 crosses
   directly through the "AFTER · THE ACCOUNTABILITY PASS" section label, and
   the "carried, unchanged" text sits on top of the line from "answer" to S4.
   In the new render, bend lines around section labels and captions, and place
   inline labels (like "carried, unchanged" and "its one job → report
   disagreement") in clear space beside or above their line, never crossing it.

VISUAL GOAL: clean, minimal, academic-preprint schematic — serif typography,
muted teal/charcoal palette with dark-red for the retired path and gold for
the single deliverable box, exactly as in the reference's color semantics,
generous whitespace, even stroke weight, no gradients/shadows/3-D/icons.

CONSTRAINTS:
- Landscape, roughly 16:9 (wide format, matching the reference's proportions).
- All text must be legible and spelled/punctuated exactly as given above
  (including the ⇄ and → glyphs).
- Quality: high-fidelity, sharp, crisp edges — vector-diagram quality.
