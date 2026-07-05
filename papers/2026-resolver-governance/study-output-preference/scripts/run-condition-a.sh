#!/usr/bin/env bash
# V2 Condition A (single-agent baseline) runner — PLAIN-PACK RE-RUN.
#
# One Anthropic API call, model pinned to claude-opus-4-8 (substrate amended
# 2026-06-04 from the locked 4.7 to current-frontier 4.8 per the partner's call;
# BOTH conditions share 4.8 so the substrate is not a confound), single iteration,
# no framework discipline. max_tokens 8000 per V2 §2 token budget.
#
# Prompt provenance note: the ORIGINAL V2 baseline prompt was not committed as a
# script (only V1's run-condition-a.sh exists, which targets a different 400-600
# word, no-##-headers shape). The locked V2 baseline ARTIFACT uses the four-section
# structure ## Recommendation / ## Reasoning chain / ## Concerns / ## Confidence.
# This system prompt is the partner-approved (2026-06-04) reconstruction that
# reproduces that documented structure, single-pass, no framework. Disclosed in the
# plain-pack pre-reg amendment.
#
# Usage: ./run-condition-a.sh <plain-decision-pack-path> <output-path>

set -euo pipefail

DECISION_PACK="${1:?usage: run-condition-a.sh <decision-pack-path> <output-path>}"
OUTPUT_PATH="${2:?usage: run-condition-a.sh <decision-pack-path> <output-path>}"

# Anthropic key from the local lifspel .env (same source as V1).
set -a
# shellcheck disable=SC1091
source /home/bartniedner/projects/lifspel/.env
set +a

# Strip any leading HTML provenance comment so only the decision content is sent.
PACK_CONTENT="$(sed '/^<!--/,/-->/d' "$DECISION_PACK")"

SYSTEM_PROMPT='You are advising a team on a real, currently-pending decision; they need a recommendation they can act on, grounded only in the decision pack provided. Produce your output under exactly these four headers:

## Recommendation
The option you recommend (or a justified hybrid), plus the core rationale.

## Reasoning chain
Your evidence-grounded reasoning, citing specific items from the pack.

## Concerns / risks
The real risks, and the trade-offs your recommendation does not solve.

## Confidence
low / medium / high, with one sentence justifying the level.

Use plain prose under each header. No preamble or meta-commentary. Do not apply any named decision framework; reason as a single advisor.'

REQUEST_JSON="$(jq -n \
  --arg model "claude-opus-4-8" \
  --arg system "$SYSTEM_PROMPT" \
  --arg user "$PACK_CONTENT" \
  '{ model: $model, max_tokens: 8000, system: $system, messages: [{role: "user", content: $user}] }')"

mkdir -p "$(dirname "$OUTPUT_PATH")"

RESPONSE="$(curl -sS https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "$REQUEST_JSON")"

echo "$RESPONSE" > "${OUTPUT_PATH}.raw.json"
echo "$RESPONSE" | jq -r '.content[0].text' > "$OUTPUT_PATH"

MODEL_USED="$(echo "$RESPONSE" | jq -r '.model // "?"')"
INPUT_TOKENS="$(echo "$RESPONSE" | jq -r '.usage.input_tokens // "?"')"
OUTPUT_TOKENS="$(echo "$RESPONSE" | jq -r '.usage.output_tokens // "?"')"
echo "Saved: $OUTPUT_PATH  | model=$MODEL_USED  tokens in=$INPUT_TOKENS out=$OUTPUT_TOKENS"
