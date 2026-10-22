# Gopnik's overhypothesis test, with and without notes (2026-10-16)

Does an assistant that writes and rereads notes between tasks learn the **abstract rule** a
series of tasks shares, and does that overcome the disjunctive bias current models inherit
from training? Built on the blicket / overhypothesis paradigm from Alison Gopnik's group.

The Wise Witan client piece "Does it learn?" promised "a version of her test". The straight
versions turned out to be done already on newer models (design note §1), so this study asks
the part they leave open: learning across episodes through what the system writes down.

## Read in this order

| file | what it is |
|---|---|
| [`design-note.md`](design-note.md) | **The design.** DRAFT until Bart approves it and it is tagged; then it is the pre-registration |
| [`deviations.md`](deviations.md) | Every departure from the design, with its timing and what data existed |

## Status

Draft design, revised 2026-10-16 after a cross-vendor review (design note §11). Simulator and controls built and passing at 6 objects /
6 tests (adopted after the first settings proved too easy; design note §12): the adaptive explorer
always succeeds, a random one scores about 57%. The model harness is built and its Stage 0 plumbing run
passed on all four models (design note §13; outputs discarded, never scored). Bart confirmed the four
models (`models.json`); the projected cost is about $12 for the baseline and $540 for the main run at n = 86
(design note §14). Locked 2026-10-16 at four cells (design note §15). **Stopped 2026-10-17 at the baseline by the pre-registered rule:** with no memory, all three models solved every "needs two" machine, leaving no room for notes to help ([result.md](result.md)). Gemini was dropped before scoring ([deviations.md](deviations.md), D1).
