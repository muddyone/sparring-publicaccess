# Stage 0 run: DISCARDED, never scored

Plumbing only (design note §9, stage 0). These sequences use the Stage 0 seed range
(10,000,000+), which neither the baseline nor the main run draws from. **No accuracy has been or
will be computed from them.** They are kept for provenance: the call log shows exactly what each
model was sent and returned, and under which settings.

- `calls.jsonl`: one line per model call (messages, reply, settings requested and sent, dropped
  settings, usage, latency).
- `seqs/<model>/<memory>-<kind>-<seed>.json`: per-sequence records, truth included (needed by the
  scorer later; not read by anyone for Stage 0).

Plumbing report: `../../scripts/harness.py --stage stage0 --report`. Summary and what it changed:
design note §13.
