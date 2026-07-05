#!/usr/bin/env bash
# build-submission.sh — assemble the V2 governance preprint into submission formats
# with a citeproc-generated bibliography from the cite-checked refs.bib.
#
# NON-DESTRUCTIVE: never mutates preprint-draft.md. It builds a transient copy in
# which the "## N. References" section's draft reference-narrative is replaced by
# the pandoc citeproc bibliography div (::: {#refs}), then renders HTML (always)
# and PDF (best-effort). The gated draft stays the single source of truth; re-run
# any time to refresh.
#
# Usage:  scripts/build-submission.sh
# Output: submission/preprint-submission.html, submission/preprint-submission.pdf
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # the v2 pilot dir
cd "$HERE"

SRC="preprint-draft.md"
META="submission/metadata.yaml"
OUTDIR="submission"
BUILD="$(mktemp -t preprint-submission.XXXXXX.md)"
BUILD_DOCX="$(mktemp -t preprint-submission-docx.XXXXXX.md)"
PNGDIR="$(mktemp -d -t preprint-figs.XXXXXX)"
trap 'rm -f "$BUILD" "$BUILD_DOCX"; rm -rf "$PNGDIR"' EXIT

command -v pandoc >/dev/null || { echo "[build] pandoc not found." >&2; exit 1; }
[ -f "$SRC" ]  || { echo "[build] missing $SRC" >&2; exit 1; }
[ -f "refs.bib" ] || { echo "[build] missing refs.bib" >&2; exit 1; }
mkdir -p "$OUTDIR"

# 1. Build copy: swap the References section's prose body for the citeproc
#    bibliography div, keeping the "## N. References" heading and everything
#    after it (the appendices). Matched by heading text, not a hardcoded section
#    number -- the number drifts whenever a section is inserted/removed/renumbered
#    (this broke silently once already: the script targeted "## 14. References"
#    after the heading had moved to "## 15.", so the div was never inserted and
#    pandoc's citeproc fell back to appending an unlabeled bibliography after the
#    appendices while the stale prose paragraph stayed put -- a duplicated,
#    broken References section in every rendered output until this fix).
awk '
  /^## [0-9]+\. References/ { print; print ""; print "::: {#refs}"; print ":::"; print ""; skip=1; next }
  skip && /^## / { skip=0 }
  skip { next }
  { print }
' "$SRC" > "$BUILD"

# Pick a serif for xelatex, preferring a scholarly text face that ALSO covers the
# paper's Greek/math glyphs (α ρ ∪ ≈ ≥ § → ✓ ± —). TeX Gyre Pagella (a Palatino-family
# academic typeface) is first: it is glyph-complete for this draft (0 missing) and looks
# like a paper rather than a screen font. DejaVu Serif et al. remain as portable fallbacks
# for machines without the TeX Gyre fonts (both also cover the glyphs).
# NOTE: capture fc-list ONCE into a var and grep the var with the FULL family name —
# piping into `grep -q` under `set -o pipefail` makes fc-list catch SIGPIPE (grep -q exits
# on first match) and the pipeline reports failure, so the font silently never gets picked.
ALLFONTS="$(fc-list 2>/dev/null || true)"
MAINFONT=""
for f in "TeX Gyre Pagella" "DejaVu Serif" "Noto Serif" "FreeSerif" "Liberation Serif"; do
  if grep -qi "$f" <<<"$ALLFONTS"; then MAINFONT="$f"; break; fi
done

COMMON=(--from=markdown --citeproc --metadata-file="$META" --resource-path=".:$OUTDIR")

# 2. HTML — always the clean artifact (handles every glyph; self-contained).
pandoc "${COMMON[@]}" --to=html5 --standalone --embed-resources \
  --metadata pagetitle="SPARRING V2 governance preprint (submission build)" \
  -o "$OUTDIR/preprint-submission.html" "$BUILD"
echo "[build] HTML -> $OUTDIR/preprint-submission.html"

# 3. PDF — best-effort. Unicode glyphs may warn under some fonts; don't fail the build.
PDF_ARGS=(--pdf-engine=xelatex)
[ -n "$MAINFONT" ] && PDF_ARGS+=(-V mainfont="$MAINFONT")
if pandoc "${COMMON[@]}" "${PDF_ARGS[@]}" --to=pdf \
     -o "$OUTDIR/preprint-submission.pdf" "$BUILD" 2> "$OUTDIR/.pdf-build.log"; then
  echo "[build] PDF  -> $OUTDIR/preprint-submission.pdf  (font: ${MAINFONT:-xelatex default})"
  grep -qi "missing character" "$OUTDIR/.pdf-build.log" 2>/dev/null \
    && echo "[build] note: some glyphs missing in PDF — see $OUTDIR/.pdf-build.log; HTML is glyph-complete."
else
  echo "[build] PDF FAILED (see $OUTDIR/.pdf-build.log) — HTML is the clean submission artifact." >&2
fi

# 3b-pre. Rasterize SVG figures to PNG for the DOCX build ONLY. Word 2016+ prefers
#     an embedded SVG and renders it with its OWN text-layout engine, which overlaps
#     matplotlib's multi-line figure titles and overflows the wide canvas past the
#     page margin (pandoc otherwise dual-embeds .svgz + a fallback .png, and Word
#     picks the SVG). A pre-rasterized PNG — via rsvg-convert, the same engine that
#     renders the SVG correctly everywhere else — renders in Word exactly as intended.
#     HTML and PDF keep the crisp vector SVG (they render it fine); only the .docx
#     source is swapped. We also pin each figure to the text-column width so nothing
#     runs off-page regardless of the SVG's native canvas size.
if command -v rsvg-convert >/dev/null; then
  for svg in figures/*.svg; do
    rsvg-convert -w 2000 "$svg" -o "$PNGDIR/$(basename "${svg%.svg}").png"
  done
  sed -E "s#\(figures/([A-Za-z0-9_-]+)\.svg\)#(${PNGDIR}/\1.png){width=100%}#g" "$BUILD" > "$BUILD_DOCX"
else
  echo "[build] note: rsvg-convert not found — DOCX will embed SVG, which Word may mis-render (overlapping titles, off-page overflow)." >&2
  cp "$BUILD" "$BUILD_DOCX"
fi

# 3b. DOCX — MS Word review copy. Same citeproc bibliography; figures pre-rasterized
#     above so Word renders them faithfully.
#     The tracked reference doc (submission/reference.docx, generated by
#     scripts/make-reference-docx.py) carries a centered "Page X of Y" footer so
#     the review copy has live page numbers. Absent it, pandoc's default is used.
DOCX_ARGS=()
[ -f "$OUTDIR/reference.docx" ] && DOCX_ARGS+=(--reference-doc="$OUTDIR/reference.docx")
if pandoc "${COMMON[@]}" "${DOCX_ARGS[@]}" --to=docx \
     -o "$OUTDIR/preprint-submission.docx" "$BUILD_DOCX" 2> "$OUTDIR/.docx-build.log"; then
  echo "[build] DOCX -> $OUTDIR/preprint-submission.docx${DOCX_ARGS:+  (page-numbered)}"
else
  echo "[build] DOCX FAILED (see $OUTDIR/.docx-build.log) — HTML is the clean submission artifact." >&2
fi

# 4. Verify the citeproc bibliography actually rendered (refs.bib → 25 entries).
if grep -q 'id="refs"' "$OUTDIR/preprint-submission.html" \
   && grep -q "Nosek" "$OUTDIR/preprint-submission.html"; then
  n=$(grep -oE 'class="csl-entry"' "$OUTDIR/preprint-submission.html" | wc -l | tr -d ' ')
  echo "[build] OK: citeproc bibliography rendered — ${n} reference entries from refs.bib."
else
  echo "[build] ERROR: bibliography did not render — check refs.bib / metadata.yaml." >&2
  exit 1
fi
