# Catch-rate study (A-v3) — the producer's-own-blind-spot test

The controlled study behind **§6.3** of *Governance by Verifiable Challenge*. It asks one
question: when a model **writes** a recommendation and embeds its own blind spots, how many of
those flaws does each kind of review catch?

Run 2026-06-28. This directory is the pilot as it ran.

## What was compared

Four review conditions on the *same* recommendation, each blind to the others:

| condition | what it is |
|---|---|
| **SELF** | the model that wrote it, reviewing its own work |
| **NEUTRAL** | a fresh model, not the author, told to review neutrally |
| **CHAL (same vendor)** | a fresh instance of the *same* model, told to attack |
| **CHAL (cross vendor)** | a model from the *other* vendor, told to attack |

Ground truth is an independent 3-agent audit panel, blind to all reviews, with a flaw counted
only if at least 2 of 3 raise it. Each review was then blind-coded against that flaw set.

**NEUTRAL is the condition that separates "fresh eyes" from "an adversarial instruction,"** and
it was pre-registered for exactly that purpose (§3, Step 2). It matters: on Claude-written work
NEUTRAL lands *below* SELF. Fresh eyes alone do not help. The adversarial framing is what moves
the number.

## Where each reported figure comes from

| claim | file |
|---|---|
| The 2×2×2 grid — every generator × auditor × condition | `results-2x2-grid.json` |
| Single-vendor headline (self 67.7 / neutral 54.8 / challenger 87.1) | `results-aggregate.json` |
| Cross-vendor replication | `results-aggregate-xvendor.json` |
| The 31 panel-confirmed material flaws (the denominator) | `consensus-flaws.json`, `gpt-consensus-flaws.json`, `gptaudit-*-consensus.json` |
| Blind catch-coding, per flaw × condition | `map_*.json`, `coding-blind-map.json`, `gpt-coding-blind-map.json` |
| The eight problems | `problems.json` |
| The recommendations under test | `recommendations.json`, `gpt-recommendations.json` |
| The reviews being scored | `reviews.json`, `gpt-reviews.json`, `*-chal-on-*.json` |
| The audit panels' raw enumerations | `audits.json`, `gpt-audits.json`, `gpt-audit-of-*.json` |
| Figures, with the code that draws them | `figures/` |

Narrative and interpretation: `results.md`. Design: `pre-registration.md`.

## Three things to read this against

**1. The cross-vendor grid was an extension, not part of the locked design.** The
pre-registration covers the **single-vendor** study and says in as many words that it cannot
tell you whether the result holds once vendors are mixed. The full
generator × auditor × condition grid was run afterward. It is the more interesting evidence and
the weaker kind; read it accordingly.

**2. Publishing this now does not by itself prove when it was written.** The design was locked
before the run and tagged `catchrate-v3-prereg-2026-06-28` in the author's working repository,
which is private. That tag is the timestamp evidence, and it is not visible here. Stating the
limitation rather than implying more than the artifact proves.

**3. Ground truth is model-established, not human.** Every number here rests on one model,
run three times, agreeing with itself about what mattered — 2 of 3 to carry. That is the
load-bearing weakness of the study, and no amount of published data repairs it. There is no
significance test either: read the gaps as direction, not size.

## Note on paths

`pre-registration.md` refers to a sibling pilot at `../catch-rate-2026-06-28/` (Study A, the
Test-A design this one supersedes). That directory is not part of this archive; the reference is
left as written rather than edited, because a pre-registration is a dated record and is not
revised after the fact.
