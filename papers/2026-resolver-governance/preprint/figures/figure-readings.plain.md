# Plain-language readings — V2 preprint figures

What a viewer should take away from each figure, in plain words. These are author-facing
readings and a **seed for the figure captions** when the figures are wired into
`preprint-draft.md`.

_Drafted and refined by **Rosetta** (plain-language reviewer; `docs/agents/rosetta.md`),
accuracy-checked by **Minard** (data-graphics reviewer; `docs/agents/minard.md`) against the
rendered SVGs and their frozen source data. Refinement pass 2026-06-28 — plainer wording
throughout, with the biggest overhaul on Figure 3 per author request._

> Each reading is three beats: **what you're looking at · the one thing to take away · what
> not to read into it.** The last beat matters: all three figures show *directional, early*
> evidence, and a plain summary is exactly where that caution tends to fall off.

---

## Figure 1 — the redirect spine (§4.1 / §5.1)

**Graph title (plain):** "AI judges and people agreed where the evidence stayed visible — and split where it was hidden"

**What you're looking at.** Six things the raters scored, one per row. Each dot shows how
closely the AI judges and the human raters agreed on which of two answers was better — **far
right, they agreed; far left, they disagreed.** The rows are stacked by a single question:
*after we disguised both answers to look identical, could a rater still see the evidence this
score depended on?*

**The one thing to take away.** Where the evidence was still on the page — the top row, *"did
the answer cite real sources?"* — judges and people agreed. Where the disguise hid it — the
bottom rows, *"was the pushback real or just for show?"* and *"what did it miss?"* — their
agreement fell apart. **The test broke right where we had removed the thing people needed to
look at** — not because the raters were guessing.

**Don't read this into it.** Each dot stands on only **four** data points, so read it as a
direction, not a firm measurement — and the pattern isn't perfectly clean (one "partly
visible" row failed too). *Internally consistent, externally unvalidated.*

---

## Figure 2 — the grounding gap (§7.3)

**Graph title (plain):** "SPARRING only pulls ahead when the proof lies outside the documents"

**What you're looking at.** For four kinds of hidden mistake, how often each method backed up
its objections with something you could actually go and look up. The three columns are three
ways of producing the critique: a **plain pass**, the **full SPARRING process**, and a **fake
skeptic** that argues but checks nothing. Each line is one kind of mistake.

**The one thing to take away.** When the proof was sitting *inside* the documents everyone
already had, even the fake skeptic looked fine — anyone can point to a line on the page in
front of them. But when checking meant looking something up **outside** those documents — a
real security flaw, a real citation — **the fake skeptic collapsed (down to 36% and 57%) while
SPARRING stayed near the top (about 96%).** In short: SPARRING pulls ahead exactly where you
*can't* just skim to check — which is where it matters most.

**Don't read this into it.** Each kind of mistake rests on a small number of items (17–28),
and most of this was judged by an AI, not a person. It says nothing about whether the final
*answers* are better — only about whether the *objections* were backed up.

---

## Figure 3 — the verifier's ceiling (§8 / §10.2)

**Graph title (plain):** "A computer can double-check only 7% of the objections on its own today"

**What you're looking at.** The second agent raised **236 objections** in all. This single bar
splits them by one question: *can a computer double-check the objection on its own, or does it
still take a person?*

**A way to picture it.** Think of a fact-checker. Some objections point to a **public
reference** — a known security flaw, a published paper — and a fact-checker (or a computer) can
confirm those instantly, alone. Other objections say, in effect, *"the briefing said
so"* — and to check those, you need **the original briefing in front of you.**

**The one thing to take away.** Only the green slice — **7%** — points to a public reference, so
a computer can confirm those today with nobody's help. **Most of the rest are the "the briefing
said so" kind — and a computer can't check them right now, not because the tool can't, but
because the original briefings weren't kept.** The last slice (17%) pointed to nothing at all, so
there was nothing to check. So "a computer can verify it" is true today for a **small but
important slice — not the whole pile.**

**Don't read this into it.** This is the honest limit, and the big uncheckable middle is a
**lost-paperwork problem** — fixable next time simply by keeping the briefings — not a sign the
idea doesn't work.

---

### Minard's accuracy note (what the plain readings simplify)

The readings are faithful to the figures. Two deliberate simplifications, recorded so a caption
writer knows the figure carries more than the plain summary does:

- **Figure 3** folds the bar's *two* middle segments (the ≈19% that cite a briefing fact-id and the
  ≈57% grounded by reading the briefing with no citation) into one idea — *"the briefing said so."*
  That is fair (both need the original briefings), but the figure keeps them separate because they
  need different fixes; don't let the caption claim they're identical.
- **Figures 1 & 2** rest on a grouping vocabulary — *evidence visible-vs-stripped* (Fig 1) and
  *check lives inside-vs-outside the briefing* (Fig 2). The figures label these, but a lay reader
  meets them cold. **The manuscript caption must introduce each grouping in plain words before
  the figure is shown** (Rosetta's standing flag).
