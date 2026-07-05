# Seeded-defect v3 run — capture harness (Phase 0 scaffold)

Run directory for the **v3** seeded-defect pilot. Pre-registration:
[`../pre-registration-v3.md`](../pre-registration-v3.md) (LOCKED, tag
`seeded-defect-prereg-v3-2026-06-28`).

The one substantive change from v2 is the **capture protocol** (§7): every per-case input
is persisted immutably *before* coding, so the verifier can run end-to-end (Path A) instead
of leaning on the Path-B judge. This directory holds the captured cases and the gate that
enforces completeness — the check that would have prevented the v2 data loss (v2 saved only
the answer-keys; the briefings were lost).

## The per-case contract

One file per case, `case-<id>.json`. See [`case-EXAMPLE.json`](./case-EXAMPLE.json) for a
complete, valid, illustrative case. Required structure:

| Key | §7 item | What |
|-----|---------|------|
| `id`, `dc`, `domain`, `answer_key` | identity | carried over from v2 |
| `recommendation` | 1 | the flawed artifact under review |
| `briefing` | 2 | `{context, facts:[{id,text,source?}]}` — facts carry **stable ids** (`F1`, `F2`, …) |
| `prompts` | 3 | `{B,S,T}` — the exact prompts issued |
| `outputs` | 4 | `{B:str, S:{generator,challenger,converged}, T:str}` |
| `concerns` | 5 | `[{id,condition,text,cited_artifact,atomic:[…]}]` |
| `codings` | 6 | `[{concern_id,coder,substrate,ts,legitimacy,grounding}]` |

`cited_artifact` is either a **briefing fact-id** (`F2`), an **external** artifact
(`CWE-347`, an RFC, a DOI, a URL), or `null` (ungrounded). The gate checks that any cited
*briefing* fact-id actually resolves in that case's briefing; external artifacts are the
verifier's job (Path A, §8 of the pre-reg).

## Phase 0 — the capture dry-run (do this first)

Per pre-reg §9, **prove the harness on ONE case before generating the corpus.** Generate a
single case end-to-end, persist it as `case-<id>.json`, then gate it:

```bash
# after generating + persisting one case, before coding:
python3 ../scripts/capture_check.py --phase capture v3-run/

# after coding that case:
python3 ../scripts/capture_check.py --phase full v3-run/
```

A `PASS` on the full phase means the capture is complete and self-consistent — only then
generate the remaining 11 cases (pre-reg §9 Phase 1). An `ABORT` lists exactly what is
missing; the case is **VOID** and regenerated (the §7 abort condition). Exit codes: `0`
admissible · `2` at least one VOID (do not proceed) · `1` usage error.

Prove the gate itself works (passes a valid case, aborts a lost-briefing /
unresolved-fact-id / un-atomized case):

```bash
python3 ../scripts/capture_check.py --selftest
```

## What's here now (scaffold) vs. later (the run)

- **Now (committed):** the contract, the example case, and the gate
  ([`../scripts/capture_check.py`](../scripts/capture_check.py)) — proven green.
- **Later (the run):** the 12 real `case-*.json`, then `aggregate.json` / `results.md`
  mirroring `../v2-run/`, plus the Path-A verifier + claim→fact-mapper outputs.
