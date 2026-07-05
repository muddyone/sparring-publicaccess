# Plain-language readings — v3-focused presentation

Figure set: **fig1 + fig2-grounding-v3**. The v2 grounding slopegraph (`fig2-grounding-gap`) and the v2 verifier-ceiling (`fig3`) are **superseded** for this presentation.

_Drafted by **Rosetta** (plain-language), accuracy-checked by **Minard** (data-graphics) against the rendered SVG + frozen `v3-run/aggregate.json` (realistic-placebo, Path-A judged)._

---

## fig1 — the redirect spine (unchanged)

Reads from the rater/output-preference study, not v3 — the narrative hinge. Plain read unchanged: see [`figure-readings.plain.md`](./figure-readings.plain.md) §"Figure 1".

## fig2-grounding-v3 — rigor map (§7, v3)

**Graph title (plain):** "SPARRING raises real, checkable objections — far more than a raw single pass"

**What you're looking at.** Every objection raised gets scored on two things: is it a *real* problem (left → right), and is it *backed by something you can actually check* (bottom → top). Each method is one dot; top-right is the good place — real *and* checkable.

**The one thing to take away.** **SPARRING** (green, top-right) raises objections that are real (100%) *and* grounded in checkable, machine-verified evidence (96%) — **far above a raw single pass** (amber, bottom-middle: real 50%, checkable 58%), which tends to nod along instead of scrutinize. *That gap — SPARRING vs a plain pass — is the everyday "I need rigor" win, and it's in the data.* A dedicated skeptic (red) gets *almost* as far (83%) — but only because the facts it needs are sitting in the briefing.

**Don't read this into it — this is the important part.** This measures the *quality* of objections on **easy, planted** mistakes. It **cannot** measure the thing practitioners value most — *catching subtle, real problems a raw prompt would miss* — because these planted mistakes are obvious enough that any strong model catches them, and the deciding fact is handed to every reviewer. That catch-the-hard-stuff value is shown by the **real would-have-shipped catches (the mechanism audit, §6)**, not here. Also: the skeptic's 83% is fragile — a strawman skeptic told to cite nothing dropped to 15% — so don't read the SPARRING-vs-skeptic gap as a fixed number. Small pilot (12 cases), single-AI-written, legitimacy still needs a domain expert.

---

### Minard's accuracy note
Axes are the two coded measures: x = precision (legitimacy), y = grounding rate (machine existence + cross-vendor supports-judge). The figure deliberately **drops the earlier "theater" framing** — with a realistic skeptic the placebo is *not* theater (it grounds 83%), so calling it theater would mislead. The on-figure caveats state plainly that catch-rate is out of scope and that the skeptic grounds only because the evidence is in-hand. The headline centers the **S-vs-B** comparison (the one a practitioner actually faces) rather than S-vs-T (a control), which is the honest emphasis.
