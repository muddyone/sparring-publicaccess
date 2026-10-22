# What AI Is: the essays and their records (Part one)

An overview and the five short essays of Part one (what it is) by Bart Niedner, written as an
honest account of what people are working with when they use AI. Part two (what working with it is
like) follows. It asks the questions people who work with AI assistants every day
end up asking. Does it learn? Is anyone there? Is its warmth good for me, or just pleasant? Is a
relationship with it dangerous? And underneath all of them: how should I judge it at all?

Every essay applies the same yardstick. Judge it by what it does and the role it fills, not by
what it is made of. Ask "compared to what?". Keep what we know separate from what nobody knows.

This folder holds Part one: the essays, the research behind them, and the records of how each
claim was checked and how each essay was reviewed.

## This is a cleaned-up copy of the working records

The files here are a public snapshot, made by a script from the author's private working
records. They are the records as written, with these changes only:

- A small number of personal passages were removed, and each removal is noted where it was made.
- Three review records of essay 05's section on the author's own assistants are not published.
  They quote his private design files and the assistants' memory.
- Local file paths, machine names, internal file references, token-usage lines and commit
  hashes were removed. Links to files that are not part of this snapshot became plain text.
- A few lines written for one service's clients were reworded to neutral terms ("users", "an
  assistant builder"). No client is named anywhere.
- Short notes were added: the AI-reviewer note on each review folder, and a note under the title
  of the working briefs.

The working records themselves are not edited to make this copy.

## Reading order

Start with the essays, in this order:

| | Essay | What it argues |
|---|---|---|
| 00 | [The thing on the other end](positions/00-the-thing-on-the-other-end.md) | The overview, and the yardstick the series uses |
| 01 | [The wrong yardstick](positions/01-the-yardstick.md) | Judge AI by the role it plays, not the category it belongs to |
| 02 | [It learns. The better question is what kind of learner it is.](positions/02-it-learns.md) | Learning, judged by what a system does, including the author's own small study |
| 03 | [Something is there. Very probably not conscious.](positions/03-someone-there.md) | What you are talking to, and what nobody knows yet |
| 04 | [Personality helps the relationship. It hasn't been shown to help the work.](positions/04-personality.md) | What warmth and personality in an assistant do and do not do |
| 05 | [We don't ask whether friendship is safe. We ask which ones are.](positions/05-relationships.md) | Whether relationships with AI are dangerous, compared to what |

Each essay ends with notes that link to its sources, its cite-check reports and its review
records.

## What each folder holds

- **[`positions/`](positions/)**: the overview and the five essays of Part one.
- **The three research syntheses** behind essays 02 to 04:
  [Personality and connection in AI co-workers](personality-and-connection.md),
  [Chalmers and AI minds](chalmers-and-ai-minds.md), and
  [Does it learn? Gopnik, the pattern-machine view, and learning profiles](learning-and-gopnik.md).
  The first two were written as background for an assistant-design method, so they include
  sections on design consequences.
- **[`briefs/`](briefs/)**: eleven research briefs, with full source lists and marks for how each
  source was verified. Briefs 1 to 5 sit behind the personality and Chalmers syntheses. Briefs 6
  to 11 sit behind the essays: the yardstick, curiosity, relationships, how models change between
  versions, when assistants began to remember, and the author's notes-and-rules study.
- **[`cite-check/`](cite-check/README.md)**: the citation-check reports, one or more per
  document, and an index that summarizes each run and what was corrected afterwards.
- **[`panel/`](panel/)**: the review records, one folder per review round.

## How the checks work

**Citation checks.** Each document was run through an automated citation checker. It resolves
every citation against live sources (Crossref, arXiv, Europe PMC, Open Library, and the cited
page itself). Then two models from different vendors (Claude and GPT) judge each citation
separately: does the source exist, and does it support the claim it is cited for? Their
disagreements are reported rather than settled. A verdict marked "model knowledge only" or
"degraded" is not a verification. Most "problem" and "disagree" entries mean the checker could
reach only an abstract or a blocked page. Some "refuted" verdicts are failed lookups, for example
on the author's own published report; the reports and the index say where. Where a claim
mattered and the checker could not reach it, it was checked by hand against the full text, and
the report or index says so. Each report shows the text as it was checked, so a later correction
appears in the index, not in the report.

**Review panels.** Each essay was then reviewed in stages. Typical roles are a cold read by a
general reader, outside critiques from models made by other companies (Gemini and OpenAI), an
argument review that ranks fixes by impact, checks of the numbers and of fidelity to the sources,
a craft edit, and a plain-language pass. Each folder's README lists the stages and what was
applied or declined.

**All panel reviewers are AI review agents, not people.** The named reviewers (for example Nadia
Okonkwo, Miriam Vale, Vera Tukey, Ines Otlet, Julian Crest, Rosetta, Anselm Kade and Rhea
Castellan) are AI models given assigned review roles: Claude subagents, or Gemini and OpenAI
models where a header says so. The author made the final calls.

## Reading the older records

The essays were renumbered on 18 October 2026 so that the method comes first. Records written
before then use the old numbers: old 01 is "it learns" (now 02), old 02 is "someone there" (now
03), old 03 is "personality" (now 04), and old 04 is "the yardstick" (now 01). The records'
folder and file names keep the old numbers.

The briefs and many review records were written for the author while the work was in progress.
They are published as written, so they speak to the author directly and sometimes refer to what
the research was commissioned for.

## The pilot records

The study that essay 02 reports is in `../pilots/`. There are two folders: the pre-registered
study (`gopnik-memory-overhypothesis-2026-10-16`), which stopped at its baseline by its own rule,
and the exploratory follow-up (`gopnik-followup-2026-10-17`), which produced the result. They hold
the design notes, the code, the per-run records and the results. The raw call logs
(`calls.jsonl`, which repeat each whole conversation, about 28 MB) are left out. The reported
numbers come from the per-run records, and the code reproduces them. The pre-registration was
locked at the tag `gopnik-prereg-2026-10-16`, commit `37567f2`, in the private working repository.
