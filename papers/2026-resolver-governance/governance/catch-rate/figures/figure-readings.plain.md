# Plain-language readings — A-v3 catch-rate figures

Rosetta's plain-language reads (plain-language reviewer; `docs/agents/rosetta.md`) for the three catch-rate figures in `pilots/catch-rate-v3-2026-06-28/figures/`, checked against the study writeup in `results.md`. These are author-facing readings and a seed for the figure captions.

> Each reading is three beats: **what you're looking at · the one thing to take away · what not to read into it.** One thing to hold onto before you start: the grey "no review" bar at 0% is **not a result we measured** — it's just the starting line. It says "if nobody takes a second look, every flaw the work already had walks straight into your decision." The real story is in the colored bars, and the honest yardstick to judge them against is the producer's **own self-review**, not that grey zero.

---

## Figure 1 — one AI doing every job (`catch-rate-v3.svg`)

**Graph title (plain):** "An AI's draft already carries about four serious flaws — and even its own second look misses a third of them"

**What you're looking at.** The setup first, because it's the whole point. We asked an AI to do a hard job: produce a real recommendation. On its own, before anyone touched it, each recommendation already carried about **four serious flaws** — the kind big enough to change the decision. We know that because a separate panel of AI auditors went looking, and they were free to come back with "none" and didn't. So four-ish flaws-per-draft is a fact about the work, not a number we dialed in.

Now the bars. Of those flaws the draft already had, how many does each kind of review actually catch? **Grey (the starting line): no review, 0% — every flaw stays in.** A fresh neutral reader catches **55%**. The same AI critiquing its *own* work catches **68%**. And a deliberately adversarial challenger — a fresh reader told to go looking for trouble — catches **87%**.

**The one thing to take away.** Even when the AI turns around and grades its own homework, it still misses about a third of its own serious flaws (the 68% bar leaves 32% behind). A challenger that comes in *looking* for problems closes most of that gap. The cleanest way to see it: of the flaws the two disagreed on, the challenger caught **8** that self-review missed, while self-review caught only **2** the challenger missed. That lopsidedness — 8 against 2 — is the blind spot, made visible. You don't catch your own blind spot as well as someone hunting for it does.

**Don't read this into it.** This is one small pilot — 8 problems, about 4 flaws each — and the same AI (Claude) played every role here: it wrote, reviewed, challenged, *and* judged. The "flaws" were called by AI auditors, not yet by human experts. And nobody ran a significance test. Read the order of the bars as a direction, not a settled measurement. *Internally consistent, externally unvalidated.*

---

## Figure 2 — does it hold with a different AI? (`catch-rate-v3-xvendor.svg`)

**Graph title (plain):** "Switch to a different AI brand and the pattern holds — a challenge still recovers most of the flaws"

**What you're looking at.** The same four conditions as Figure 1, but now each row has **two bars side by side.** The left bar is the all-Claude run from Figure 1. The right bar is a different setup: a different AI family, **GPT-5.2**, does the producing, the self-review, and the challenging — and Claude, independently, plays auditor and grader. So a *different* brand establishes what counts as a flaw and scores the catches. If the whole idea only worked because one AI was marking its own family's exam, this is where it would fall apart.

It doesn't. Neutral review: 55% / 65%. Self-review: 68% / 74%. Challenger: 87% / 77%. Both brands tell the same story — a draft full of flaws, a self-review that leaves a chunk behind, and a challenge that recovers the large majority.

**The one thing to take away.** The headline survives the brand swap: across two different AI families, a challenger recovers roughly **77 to 87%** of the producer's own serious flaws, and it's the top condition in both. That's the robust, load-bearing finding.

But there's one honest wrinkle, and it leads rather than trails. The challenger's *edge over self-review* is big for Claude (87 vs 68 — a 19-point lead) and small for GPT-5.2 (77 vs 74 — barely 3 points). The reason is plain: **GPT-5.2 is unusually good at catching its own mistakes**, so a separate challenger has less left to find. The value of the challenge holds for both; the value of making it a *separate* agent depends on how blind the writer already is to its own work.

**Don't read this into it.** Part of that dramatic Claude gap had a quiet helper: in the all-Claude run, the challenger and the auditor were the same brand, which can nudge them toward agreeing on what counts as a "real" flaw. The cross-vendor run removes that overlap — which is exactly why the gap shrinks here, and why Figure 3 splits the question apart properly. Same small pilot, same AI-judged flaws, no significance test.

---

## Figure 3 — the full test, every combination (`catch-rate-2x2.svg`)

**Graph title (plain):** "However you mix the AIs, a real challenge recovers most of the flaws — and a *different* AI was best-or-tied in three of the four pairings"

**What you're looking at.** This is the complete cross-check, laid out as a grid. Two things are being varied at once: **which AI wrote the work** (Claude or GPT), and **which AI did the challenging** (the same brand as the writer, or a different one). And every combination was graded by *both* auditors, so no single brand's opinion of "a flaw" runs the table. The four columns are the four writer-and-grader pairings; each colored row is a way of reviewing, and the number is the share of the writer's own serious flaws it caught. The grey top row is still the 0% starting line — no review, nothing caught — there only as a reference, not a contestant.

Read down any column and the catch-rate mostly climbs — neutral, self-review, then the challengers, mostly landing in the 80s and 90s. The one exception is the GPT-writes/GPT-grades column, where GPT's own self-review (84%) is already the column's high point and the challengers sit just below it.

**The one thing to take away.** Three things, in plain order:

1. **A real challenge works no matter who wrote or graded it.** Across all eight live cells, a challenger recovers between **78 and 94%** of the writer's own serious flaws. This is the finding you can lean on.

2. **Whether a *separate* challenger beats the writer's own self-review depends on who wrote it.** When Claude wrote the work, a challenger helps a lot — Claude has a genuine blind spot for its own mistakes (and this holds up *even when GPT does the grading*, so it's real, not brand favoritism). When GPT wrote it the picture is mixed: with a Claude auditor a challenger still adds about 10 points over GPT's self-review, but with a GPT auditor GPT's self-review (84%) actually edges out both challengers. GPT self-checks well enough that a separate challenger adds little — and in one cell, slightly less. The blind spot is a property of the *writer*, not of the setup.

3. **A challenger that is a *different* AI was best-or-tied in three of the four pairings**, and it helped most exactly where the writer is blindest to itself (the Claude-written columns, 94% and 87% — beating the same-brand challenger by 3 and 7 points). In the fourth pairing (GPT writes, GPT grades) the different model came in 3 points *below* the same-brand challenger (78% vs 81%). So the practical rule, stated honestly: **use a challenger; in this pilot a different model was usually as good or better, and only once slightly worse.**

**Don't read this into it.** The grid does show a small real effect where a reviewer and an auditor share a brand they agree slightly more often, worth about 2 to 5 points. It's measurable but minor, and — importantly — it is *not* what's driving the blind-spot story, since that story survives being graded by the other brand. All the usual limits still apply: 8 problems, about 4 flaws each, flaws judged by AI auditors rather than human experts, and this measures AI-reviewing-AI — not yet a person-in-the-loop workflow. Read the grid as a strong, consistent direction, not a final tally. *Internally consistent, externally unvalidated.*
