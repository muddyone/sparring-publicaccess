---
figure: fig6-verifier-pipeline
target: OpenAI gpt-image-1 (/v1/images/edits, 1536x1024, high)
reference: submission/figures/fig6-verifier-pipeline.png (existing hand-authored diagram, attached as edit reference)
status: DRAFT
mode: redesign-candidate — no underlying dataset, diagram-clarity task
---

USE CASE: An alternate, more polished render of an existing hand-authored
schematic diagram for an academic preprint. Reproduce the SAME structure and
SAME text verbatim — this is a visual-polish pass, not a content change. The
existing version already reads fine; the goal is a cleaner, more refined
execution of the identical diagram, not a redesign of its logic.

DIAGRAM CONTENT (reproduce exactly):
Title: "How one concern is checked, end to end"

A left-to-right chain of 5 rounded-rectangle boxes, connected by simple
rightward arrows, each box with a bold header line and a smaller subtitle line:
1. "Concern cites" / "e.g. CWE-640"
2. "Classify" / "by shape (regex)"
3. "Look up" / "MITRE · 1 API call"
4. "Exists?" / "404 → refuted"
5. "Backs claim?" / "cross-vendor LLM" — this LAST box only should be filled
   in a warm gold/amber accent color; the first four are a neutral cool
   teal-on-white outline.

Below boxes 1-4, a horizontal bracket spanning all four, labeled underneath in
italics: "existence — no model, no web search (also: DOI→Crossref, RFC→IETF,
path→repo, URL→fetch, #fact→briefing)"

Below box 5, a separate bracket labeled underneath in italics: "the only model"

Below everything, a centered caption line: "The classifier reads the
citation's type, never the topic; a citation matching no backend is counted
ungrounded."

VISUAL GOAL: clean, minimal, academic-preprint schematic — serif typography
for the caption, a clear sans or serif for box labels, muted teal/charcoal
palette with the single gold accent box exactly as in the reference, generous
whitespace, even stroke weight on all boxes and arrows, no gradients/shadows/
3-D/icons/clip-art. Crisper edges and more even spacing than the reference if
possible, but the SAME 5-box + 2-bracket layout and the SAME text.

CONSTRAINTS:
- Landscape, roughly 5:2 (wide and short, matching the reference's proportions).
- All text must be legible and spelled exactly as given above.
- Quality: high-fidelity, sharp, crisp edges — vector-diagram quality, not a
  hand-drawn or sketchy look.
