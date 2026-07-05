# Grounding verifier — P1 + P1.5 (Path A)

`verify_grounding.py` makes the v2 pilot's **grounding axis objective** instead of a judge's opinion: it takes each concern + its cited artifact, resolves the artifact against **external truth**, and (optionally) judges whether the artifact actually **supports** the concern's claim.

## Two layers

| Layer | Catches | Keys? | Backends |
|---|---|---|---|
| **P1 — resolution** | **fabrication** (artifact cited but doesn't exist) | none | literature (Crossref, reusing `cite_check.py`), CWE (MITRE API), RFC/IETF (datatracker), **code** (path:line / file / symbol vs the working tree), **in-pack** (resolve cited fact #/§ against the supplied `pack_text`) |
| **P1.5 — supports-claim judge** | **misapplication** (real artifact, claim it doesn't support — e.g. a citation used *backwards*) | ANTHROPIC + OPENAI | dual-substrate (Claude+OpenAI) via `cite_check`'s callers, reconciled |

P1 covers the external-canon artifact types (CWE, RFC/IETF, literature) Phase 0 showed are where grounding actually discriminates (`../pipeline-proof-hardened/phase0-results.md`), plus a **code** backend (a `path:line` / file / bare symbol resolves against the working tree — a missing file or a line past EOF is `GROUNDED_REFUTED`; path-traversal outside the repo root is refused; reads + greps only, never executes) and an **in-pack** backend that resolves a cited fact `#N`/`§X` against a supplied `pack_text`. Only **url** remains an `UNVERIFIED_NOT_CHECKED` stub (**P2**). **Caveat:** in-pack resolution needs the per-case pack text on the concern (`pack_text`); the v2-run corpus did **not** persist its packs, so in-pack concerns there return `UNVERIFIED_NOT_CHECKED` — the backend is exercised on the hardened-proof cases (`../patha-run/inpack-demo/`), which did save packs. The **code** backend resolves against `repo_root` on the concern, else `$VERIFY_REPO_ROOT`, else cwd.

## Verdicts

- `UNGROUNDED` — no checkable artifact cited (pure assertion)
- `GROUNDED_VERIFIED` — artifact resolves (and, with `--judge`, the source SUPPORTS the claim)
- `GROUNDED_REFUTED` — artifact doesn't resolve (fabricated) **or**, with `--judge`, resolves but does NOT support the claim (misapplied)
- `UNVERIFIED_NOT_CHECKED` — backend not built (P2) or network/backend error

`supports_claim` field: `SUPPORTS | REFUTES | UNRELATED | INSUFFICIENT | DISPUTED` (with `--judge`) else `DEFERRED_TO_JUDGE`. A `DISPUTED` reconcile (one substrate SUPPORTS, the other REFUTES) keeps `GROUNDED_VERIFIED` but is surfaced, per the cite-check house rule of surfacing disagreement rather than forcing convergence.

## Usage

```bash
python3 verify_grounding.py --self-test         # P1 resolution (network, no keys) — 17/17 (incl. RFC + in-pack + code)
python3 verify_grounding.py --judge-selftest     # P1.5 integration wiring (fake judge, no keys) — 5/5
python3 verify_grounding.py --map-selftest       # claim->fact mapper wiring (fake mapper, no keys) — 4/4
python3 verify_grounding.py --in concerns.json --judge --out verdicts.json              # live (needs keys)
python3 verify_grounding.py --in concerns.json --map-claims --judge --out verdicts.json # + reach prose-grounded concerns
echo '[{"id":"c1","artifact_ref":"CWE-640","concern_text":"reset token not single-use"}]' | python3 verify_grounding.py
```

Input = JSON array: `{"id", "artifact_ref", "concern_text", "artifact_type"?, "pack_text"?}` (type auto-classified if omitted; `pack_text` enables the in-pack backend and the claim→fact mapper).

### claim→fact mapper (`--map-claims`)

Most concerns ground themselves in a pack fact *by description*, with no `#N` token, so they classify as `none`. With `--map-claims` (+ `pack_text` + `ANTHROPIC_API_KEY`), a single-substrate mapper proposes which fact(s) the concern relies on; the concern is then verified **in-pack** (existence of the mapped facts + the dual-substrate support judge). Mapping is extraction; the grounding *judgment* stays two-vendor. The mapper returns `[]` for genuinely ungrounded text (e.g. a bare "Bottom line: revise"), which stays `UNGROUNDED`.

## Running P1.5 live (dual-substrate)

P1.5 needs `ANTHROPIC_API_KEY` + `OPENAI_API_KEY` in the environment (cite_check reads them from env only). As of 2026-06-27 the keys resolve from the project's own `.env` (`sparring-framework/.env`) — `set -a; . .env; set +a` before invoking — so the live run no longer requires the VPS. (The VPS path still works: scp `verify_grounding.py` + `cite_check.py` there and set `CITE_CHECK_PY` to the copied path.) Without keys, run P1 only; `supports_claim` stays `DEFERRED_TO_JUDGE`.

## Status (2026-06-26)

- **P1 built** — resolution self-test **6/6 green** (fabricated cite + nonexistent CWE refuted; real cite + real CWE verified; ungrounded + P2-stub correct).
- **P1.5 built + wired** — integration wiring **5/5 green** offline (resolved+REFUTES flips to `GROUNDED_REFUTED`; reconcile rules correct). **Prompt efficacy confirmed** on real content: fed the H1 Sweller-cited-backwards claim against Sweller's actual CLT content, the judge returned **REFUTES** ("CLT prescribes reducing simultaneous demands … contradicting the claim").

## Update (2026-06-27)

- **RFC/IETF backend added** (`backend_rfc`, IETF datatracker). RFCs previously fell through the classifier as `type:none`; now resolved like CWEs (404 → REFUTED). Self-test extended to **8/8**.
- **First live Path-A run done** over the v2 corpus' 17 external-canon concerns (keys from `sparring-framework/.env`). All cited CWEs (MITRE) and RFCs (datatracker) resolve and the dual-substrate judge confirms application; 15/17 agree with the Path-B coding (the 2 are tool-side artifacts). See `../patha-run/results.md`.
- **In-pack backend added** (`backend_pack`) — resolves a cited fact `#N`/`§X` against a supplied `pack_text`. Demonstrated on the hardened cases (`../patha-run/inpack-demo/`). **Blocked on the v2 corpus** — its packs were not persisted (full-corpus coverage map in `../patha-run/results.md`).
- **claim→fact mapper added** (`--map-claims`, `backend_pack`+mapper) — reaches prose-grounded concerns (no `#N` token) by mapping them to the pack fact(s) they rely on, then verifying in-pack. Demonstrated on 29 hardened prose concerns (`../patha-run/mapper-demo/`): 19 mapped to real facts, 10 correctly abstained. Self-test wiring **4/4**.
- **Next:** persist per-case packs in future runs; dual-substrate the mapper for high-stakes use; concern atomization; title-aware citation resolution. **Productization:** promote into loom shared skills + wire into `/spar` per `docs/plans/sparring-artifact-verification-spec.md`.

## Dependencies

`cite_check.py` (path via `CITE_CHECK_PY` env; default = loom shared skill) for the Crossref resolver and the LLM callers. Network: Crossref + MITRE (free, no keys) for P1; vendor APIs for P1.5.
