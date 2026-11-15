_Substrate: Claude (subagent as Rosetta). All edits applied except item 18 (a word in Bart's approved paragraph, left for him). The Samiei comparison in item 3 was confirmed against the abstract ("conjunctive rules still require more tests to infer than disjunctive rules"). The endnote's cite-check line was updated to three runs. The optional one-line note under the title was added._

I'm reviewing this as Rosetta. The piece holds together. A general reader can follow the argument from the opening to the last line, and earlier rounds already cleared most of the jargon: "Bayesian" and "interventions" are gone, and "pre-registered" now comes after a plain explanation. What's left is mostly small things, plus three that are bigger: the header, a few words a lay reader has never seen (one of them, "weights", sits inside a quote that carries the argument), and two places where a sentence points at something the reader was never given.

I made no edits to any file. The two paragraphs you approved are untouched; I flag one word in one of them (item 18).

## Edits, in order of importance

**1. The header** (Impact 8). Delete lines 3–13, from "_Position piece, Bart Niedner, drafted…" through the `---` rule, and put the endnote below in its place. It's the first thing a reader meets and it's lab paperwork. In Speechify it means listening to six link labels before the first sentence.

There's also a disclosure gap the move should fix. The header says "revised after panel review", and a general reader will picture human reviewers. Every reviewer's record shows an AI: Claude, Gemini and GPT-6.1 Sol. The citation check also used two AIs, Claude and GPT. The endnote says so.

**2. QUOTE:** `once trained, "the weights no longer change,"`
**REPLACEMENT:** `once trained, "the weights no longer change" (the weights are the millions of numbers that training sets inside the model),`
Reason: a lay reader doesn't know what "weights" are, and this quote is the objection the whole section answers. The quote itself stays word for word.

**3. QUOTE:** `though it still takes them more tests`
**REPLACEMENT:** `though "needs two" still takes them more tests to work out than "any one" does`
Reason: it answers "more than what?". The paper's summary says "conjunctive rules still require more tests", and the natural reading is "more than the any-one rule". That comparison is my reading of the summary, so check it against the paper's body. If the paper doesn't support it, use `though it is still the harder of the two rules for them`.

**4. The blicket bullet. QUOTE (the whole text after the bold lead-in):** `A "blicket detector" is a machine that lights up when the right blocks are put on it, and the learner tries blocks to work out which ones those are. Some machines light up for any one of the right blocks. Others light up only when two particular blocks are on together: they "need two". Models working this out for themselves learn the "any one" rule well and the "needs two" rule poorly. Adults do the same, expecting causes to work alone, while young children take up "needs two" more readily (Lucas et al. 2014); the models' pattern matches the adults' (GX-Chen et al. 2025).`
**REPLACEMENT:** `A "blicket detector" is a machine that lights up when the right blocks are put on it. The learner tries blocks to work out which ones those are. Some machines light up for any one of the right blocks. Others light up only when two particular blocks are on together; call that "needs two". Models working this out for themselves learn the "any one" rule well and the "needs two" rule poorly. Adults have the same weakness: they tend to expect each cause to work alone. Young children take up "needs two" more readily (Lucas et al. 2014). The models' pattern matches the adults' (GX-Chen et al. 2025).`
Reason: the same facts and citations, cut into one idea per sentence, which matters most when it's heard rather than read. It also brings in the word "weakness", which items 7 and 8 need.

**5. QUOTE:** `On these tasks, then, accuracy has narrowed; exploring efficiently has not caught up.`
**REPLACEMENT:** `On these tasks, then, the gap in accuracy has narrowed; the gap in exploring efficiently has not closed.`
Reason: accuracy itself didn't narrow, the gap did. As written, the sentence says the opposite of what's meant.

**6. QUOTE:** `Without notes, Claude usually guessed the rule (8 times in 10 on the final machine)`
**REPLACEMENT:** put this sentence just before it: `Each run was a short series of machines that shared one rule, ending on a final machine where the notes could show their worth.`
Reason: "the final machine" shows up with no setup. The piece never says that a run was a series of machines. The follow-up README confirms the design (machines 1 to 3 or 1 to 4, then a test machine).

**7. QUOTE:** `Either the bias has closed in these newer models, or my task removed it,`
**REPLACEMENT:** `Either these newer models no longer have the "needs two" weakness, or my task removed it,`
Reason: "the bias" points back to nothing, because the word hasn't appeared before. And a bias doesn't "close".

**8. QUOTE:** `So the notes didn't overcome a bias; Claude already leaned the right way.`
**REPLACEMENT:** `So the notes didn't fix a weakness; Claude already leaned the right way.`
Reason: keeps the same word as items 4 and 7.

**9. QUOTE:** `In May 2026 Alison Gopnik told Chris Hayes that`
**REPLACEMENT:** `In May 2026 Alison Gopnik, who studies how children learn, told Chris Hayes on his podcast that`
Reason: the reader has never heard of either person. I left out a job title such as "developmental psychologist" because the synthesis doesn't source one. "Studies how children learn" comes from what the piece itself says about her.

**10. QUOTE:** `Others may change what the learner can do, and can be tested: a written rule has to be looked up at the right moment.`
**REPLACEMENT:** `Others may change what the learner can do, and can be tested. A written rule, for example, only helps if it is looked up at the right moment; a habit fires on its own.`
Reason: as written, the example after the colon doesn't show what it's an example of. The added clause comes from the piece's own "never becomes a reflex".

**11. QUOTE:** `None of these tests the part of Gopnik's paradigm that is about learning across tasks.`
**REPLACEMENT:** `None of these tests the part of Gopnik's work that is about learning across tasks.`
Reason: "paradigm" is a research word.

**12. QUOTE:** `People turn rules into reflexes (John Anderson's proceduralization; Anderson 1982).`
**REPLACEMENT:** `People turn rules into reflexes, as the psychologist John Anderson described (Anderson 1982).`
Reason: the label adds nothing for this reader, and read aloud it's a tongue-twister followed by a semicolon. The claim and the citation stay.

**13. Table row label. QUOTE:** `| Rules over impulses |`
**REPLACEMENT:** `| Rules you have to remember |`
Reason: both cells in that row are about remembering to follow a rule until it becomes habit. "Over impulses" doesn't tell the reader that.

**14. Table row label. QUOTE:** `| Know-how that's hard to say |`
**REPLACEMENT:** `| Know-how that's hard to put into words |`
Reason: heard aloud, "hard to say" sounds like "hard to tell".

**15. QUOTE:** `and that model read the notes without blinding.`
**REPLACEMENT:** `and that model read and sorted the notes itself, with no check by a reader who didn't know where each note came from.`
Reason: "blinding" is research jargon. The README says the notes were "read by one Claude session, not coded blind".

**16. QUOTE:** `ten runs per condition.`
**REPLACEMENT:** `ten runs with notes and ten without.`
Reason: "condition" is study jargon.

**17. QUOTE:** `Her published case is more careful than the two-year-old who outsmarts the best AI`
**REPLACEMENT:** `Her published case is more careful than the soundbite about a two-year-old outsmarting the best AI`
Reason: as written, it compares her case to a toddler. Nadia flagged this, and it's still open.

**18. Your approved paragraph, a word only.** In "Vendors now say so in their terms", a lay reader would say "AI companies" and "terms of service". I'm flagging it, not rewriting it.

**19. QUOTE:** `In her group's tool-innovation scenarios, children had to`
**REPLACEMENT:** `In her group's tests of tool innovation, finding a new use for an everyday object, children had to`
Reason: "tool-innovation scenarios" is a label with no explanation.

**20. QUOTE:** `On the matching *imitation* question ("which goes best with a compass?"), they did well.`
**REPLACEMENT:** `On the matching *imitation* question, which only asks what usually goes together ("which goes best with a compass?"), they did well.`
Reason: says why the contrast matters in the same breath. Nadia flagged it as unclear.

**21. QUOTE:** `Judged by function, a language model with memory does learn:`
**REPLACEMENT:** `Judged by function, an AI assistant that keeps a memory does learn:`
Reason: "language model" is the reader's first technical term, and it arrives in the thesis sentence. The piece's own conclusion is that the assistant is the thing that learns, so this wording also matches it. Optional if you want to keep the precise term here.

**22. Tool-innovation bullet. QUOTE:** `on 20 freshly written items, GPT-4o scored 81.3% against adults' 88.2%, and 86.0% with step-by-step reasoning`
**REPLACEMENT:** `on 20 newly written puzzles, GPT-4o scored 81.3% against adults' 88.2%, rising to 86.0% when it reasoned step by step`
Reason: "items" is test jargon, and "and 86.0%" has an unclear subject. The numbers are unchanged.

**23. QUOTE:** `It got the final machine right 8 times in 10 with notes and 6 without, which is within chance.`
**REPLACEMENT:** `It got the final machine right 8 times in 10 with notes and 6 without, a gap small enough to be chance.`
Reason: "within chance" is statistician's shorthand.

**24. Read-aloud fixes:**
- `Those were 2022–23 models` → `Those were 2022 and 2023 models`. Speechify may read the dash as "minus" or "dash".
- `Clark and Chalmers' extended-mind argument applies the same logic to people:` → `The philosophers Andy Clark and David Chalmers apply the same logic to people, in what they call the extended mind:`. This puts the plain words before the label. The first names come from the synthesis's reference list. This one is optional.

**25. Spelling** (Impact 2). "practised" and "analyse" are British spellings, and the rest of the piece reads American. It makes no difference aloud.

## The header as an endnote

Put this after the last line of the essay ("…whether it can find out what nobody has told it."), just before `## Sources`:

```markdown
## How this piece was made

I wrote this with help from Claude, an AI made by Anthropic. So an AI helped write a piece about
whether AI learns, and it has a stake in the answer. Keep that in mind when you read my study
results.

It draws on two longer pieces: [Does it learn?](../../learning-and-gopnik.md), a summary of the
research with its sources, and
[How a model moves from version to version](../../briefs/2026-10-17-9-how-models-change.md). Three
sources added later (Shardlow & Przybyła 2024; Lucas et al. 2014; Anthropic 2025) and my
follow-up study are linked where they are used.

Every source was checked twice by a tool that looks each one up and has two AIs from different
companies judge whether it supports the claim it backs
([first check](../../cite-check/2026-10-17-position-pieces.md),
[after revision](../../cite-check/2026-10-17-piece-01-revised.md)). Reviewers then tested the
argument, the evidence and the writing. Those reviewers were AIs too, from three companies, each
given a reviewer's role ([review records](./)). Drafted 16 October
2026; checked and revised 17 October 2026.
```

Two notes on it:
- "Two AIs from different companies" means Claude and GPT, as the cite-check skill describes. "Three companies" means Anthropic, Google and OpenAI, taken from each reviewer record's first line.
- If you want readers to see the AI's role before they start, add one plain line under the title: `_Written with help from Claude, an AI. See "How this piece was made" at the end._` That's your call. The brief was to move the note to the end, and the endnote works without this line.

## What I couldn't fix with wording

Most of the reading effort comes from how many different number formats the reader has to switch between: 85% and 76%, then 81.3%, 88.2% and 86.0%, then 240 machines, "three times in four", 27 of 40 against 22 of 40, and "8 in 10", "2 in 10", "3 in 10", "10 out of 10". That's roughly four different kinds of number. Better sentences can't remove that without dropping facts, and you've said the content is settled.

The earliest percentages (85% and 76%, from the 2022 and 2023 models) are the ones a reader only needs as a conclusion, "children did better than the models". If you ever loosen the "content is settled" rule, those are what I'd turn into words first. That's a decision for you, or for Vera (who checks the measurement claims), not a wording fix.

Read aloud, the table is the weakest part. Speechify reads it cell by cell and doesn't repeat the column headings. The prose around it carries the same point, so the table can stay. Just expect that section to sound choppy.

## The takeaway

The three edits that matter most are moving the header to the end, explaining "weights", and finishing the Samiei comparison. Before applying the Samiei edit, check in the paper itself that "more tests" means more than the "any one" rule. Two more sentences need a fix because they point at something the reader was never given: "the bias" and "the final machine". Everything else is quick, small wording. No number, citation, caveat or claim changes. The endnote also fixes a real gap: it tells the reader that the reviewers were AIs, which the current header never says.
