#!/usr/bin/env bash
# Fetch the free NCBE MEE administrations that carry BOTH questions and analyses,
# plus the MEE Subject Matter Outline (the fixed doctrinal taxonomy used as the
# G4 non-model enumerator).
#
# NCBE materials are copyrighted. They are NOT redistributed in this repo: this
# script reproduces the corpus from NCBE's own public URLs into a gitignored
# directory. Only DERIVED structured gold (issue labels + weights + citation)
# is committed.
#
# Usage:  ./fetch_corpus.sh [dest_dir]     (default: ../corpus)
set -euo pipefail

DEST="${1:-"$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/corpus"}"
BASE="https://www.ncbex.org"
mkdir -p "$DEST"

# Free Questions+Analyses administrations, oldest first. Verified 2026-08-29.
PATHS=(
  "/sites/default/files/2023-03/MEE_Feb_2016.pdf"
  "/sites/default/files/2023-03/MEE_July_2016.pdf"
  "/sites/default/files/2023-03/MEE_Feb_2017.pdf"
  "/sites/default/files/2023-03/MEE_July_2017.pdf"
  "/sites/default/files/2023-06/Feb_2018_MEE_QuestionsAnalyses.pdf"
  "/sites/default/files/2024-05/July2018_MEEQuestionsAnalyses_ONLINE.pdf"
  "/sites/default/files/2024-10/February%202019%20MEE_COMPLETE_BOOK.pdf"
  "/sites/default/files/2025-05/July%202019%20MEE_Complete.pdf"
  "/sites/default/files/2025-10/February%202020%20MEE_Complete.pdf"
  "/sites/default/files/2026-06/July%202020%20MEEs%20and%20Analyses.pdf"
  # Taxonomy for the G4 structured enumerator (not an administration).
  "/sites/default/files/2025-07/NCBE%20MEE%20Subject%20Matter%20Outline.pdf"
)

command -v pdftotext >/dev/null || { echo "need poppler-utils (pdftotext)" >&2; exit 1; }

for p in "${PATHS[@]}"; do
  fn="$(basename "$p" | sed 's/%20/_/g')"
  if [ ! -f "$DEST/$fn" ]; then
    echo "fetch  $fn"
    curl -sL --fail --max-time 120 "$BASE$p" -o "$DEST/$fn"
  fi
  txt="$DEST/${fn%.pdf}.txt"
  [ -f "$txt" ] || pdftotext -layout "$DEST/$fn" "$txt"
  printf "  %-46s %8s bytes\n" "$fn" "$(stat -c%s "$DEST/$fn")"
done

echo
echo "corpus at: $DEST"
echo "next: ./extract_gold.py"
