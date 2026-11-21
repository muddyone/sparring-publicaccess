# Ines Otlet: accuracy read, the approval-fatigue sentences (essay 07, 2026-11-20)

Draft: `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`, section "How far it goes before anyone looks",
the paragraph beginning "The usual way to keep a person involved" (lines 273-282), plus a consistency sweep of the
rest of the essay.

Source opened (full text, fetched 2026-11-20): Hughes 2026, "How we built Claude Code auto mode",
https://www.anthropic.com/engineering/claude-code-auto-mode . "Published Mar 25, 2026". "Written by John Hughes."
Anthropic engineering blog. Cite-check for this line: `../../cite-check/2026-11-20-piece-07-hughes.md` (c02
AGREE-clean, evidence text).

## The source's own words

Paragraph 1: "By default, Claude Code asks users for approval before running commands or modifying files. This
keeps users safe, but it also means a lot of clicking "approve." Over time that leads to approval fatigue, where
people stop paying close attention to what they're approving."

Paragraph 2: "Users have two solutions for avoiding this fatigue: a built-in sandbox [...] or the
--dangerously-skip-permissions flag [...]. Sandboxing is safe but high-maintenance [...]. Bypassing permissions is
zero-maintenance but offers no protection. Manual prompts sit in the middle, and in practice users accept 93% of
them anyway."

Later: "If you are manually approving every action carefully, it's arguably a regression [...]. It is not a
drop-in replacement for careful human review on high-stakes infrastructure."

## What checks out (no change needed)

- **The quote is exact**: "approval fatigue, where people stop paying close attention to what they're approving".
  Straight apostrophe on the page too.
- **"Anthropic says"**: fair. It's Anthropic's engineering blog, by an Anthropic author. Attribution is already
  in the sentence, so the reader knows whose number it is.
- **"people using its coding tool"**: fair for "users" of Claude Code. "Its coding tool" ties back to the
  permissions paragraph (line 59) and to "the coding tool I describe above" in the Notes.
- **93 in every 100**: right number, in the house rate form.
- **"I found no study of whether people really read the approval prompts"**: still true. Hughes is not a
  study of reading. It gives an acceptance rate and asserts fatigue, with no measure of attention.
- **"Anyone who has clicked "allow" for the twentieth time in an hour knows the feeling."**: fine as the
  author's voice. It claims nothing about the source and it sets up step 4 ("If you catch yourself clicking
  "allow" without reading, the setup is wrong").
- **Sources list**: `[Hughes 2026](https://www.anthropic.com/engineering/claude-code-auto-mode)` is present, the
  URL matches, and it sits in the right alphabetical place (Greshake, Hughes, Jensen).
- **"What this doesn't claim"**: nothing there about approval prompts. No change.
- **"What would change my mind"**, last bullet ("If studies found that people do read and weigh agents' approval
  prompts"): still consistent. A 93 in every 100 acceptance rate is not that study, in either direction.
- **Steps 2, 3, and 4**: consistent. Step 4's remedy ("Let it do the harmless things without asking, so the
  questions that remain are the ones worth reading") matches the source's own aim. No change.
- **Notes, "Much of the evidence on how these products work is the companies' own documentation"**: covers
  Hughes, which is Anthropic's own account of its own product.

## Findings, ranked

### 1. The "But" makes the 93 look like an answer to "does anyone read them?" (impact 6)

Passage: "and I found no study of whether people really read the approval prompts agents show them. But Anthropic
says that people using its coding tool accept 93 in every 100 of those prompts, and it warns of "approval
fatigue, ...""

What's wrong: "But" sets the figure against the missing study, so a reader takes the 93 as evidence that people
don't read. It isn't. An acceptance rate counts clicks, not attention: people could read every prompt carefully
and still say yes to 93 in every 100 if most requests are harmless. The page doesn't claim the 93 shows
inattention either. It gives the figure in a separate paragraph, to say manual prompts protect less than they
seem ("accept 93% of them anyway"). The fatigue claim is in paragraph 1, and it rests on "a lot of clicking
"approve"", not on the 93. So the essay's "93 ... and it warns of fatigue", next to that "But", reads as a
causal link the page doesn't make.

Fix: say what the figure measures, and keep the fatigue claim on the source's own ground. See the full
replacement below.

### 2. "those prompts" widens Claude Code's prompts to agents in general (impact 4)

Passage: "accept 93 in every 100 of those prompts"

What's wrong: the antecedent is "the approval prompts agents show them", meaning all agents. The page's "them" is
"Manual prompts", meaning Claude Code's own permission prompts in its default manual-approval mode. "People using
its coding tool" narrows the people but not the prompts. Read literally, the sentence says Claude Code users
accept 93 in every 100 of every agent's prompts.

Fix: "its approval prompts" (the tool's), not "those prompts".

### 3. "warns of" is softer than the page (impact 2)

Passage: "and it warns of "approval fatigue, ...""

What's wrong: the page doesn't warn of it as a risk. It states it as what happens: "Over time that leads to
approval fatigue". "That" is "a lot of clicking "approve"", which comes from Claude Code asking by default
before commands and file changes. "Warns" isn't wrong, but it hedges more than the source does, and it loses the
cause the page gives (being asked again and again).

Fix: "says that being asked again and again leads, over time, to "approval fatigue, ...""

### 4. The figure has no stated basis (impact 3; draft note, not essay text)

The page gives no period, sample, or method for the 93. It doesn't even say it was measured, though "in practice"
suggests usage data. "Anthropic says" plus the Notes' "weigh those parts with that in mind" already tell the
reader whose number it is. Adding "its own figure" to the sentence would repeat that. Whether to say "without
saying how it was measured" in the text is a question for Vera (is it the right statistic?), not for me. I
recommend a draft note only:

Add to the Draft notes, after "Lynch et al. is Anthropic's own;": "Hughes 2026 is Anthropic's own and gives no
period, sample, or method for the 93%;"

## Proposed full replacement for the new sentences

Replace from "But Anthropic says that" through "knows the feeling." with:

> Anthropic does give one figure for its own coding tool: people accept 93 in every 100 of its approval
> prompts. That counts clicks, not attention. But the company also says that being asked again and again leads,
> over time, to "approval fatigue, where people stop paying close attention to what they're approving"
> ([Hughes 2026](https://www.anthropic.com/engineering/claude-code-auto-mode)). Anyone who has clicked "allow"
> for the twentieth time in an hour knows the feeling.

Checked against the source:
- "its own coding tool": the figure is about Claude Code, Anthropic's product. Right.
- "its approval prompts": "Manual prompts" in Claude Code. Right scope (finding 2).
- "That counts clicks, not attention.": a statement about what an acceptance rate measures. It's not a claim
  from the page, so it carries no citation. It stops the figure from saying more than it does (finding 1),
  and it agrees with "I found no study".
- "being asked again and again leads, over time, to": the page's "asks users for approval before running
  commands or modifying files [...] a lot of clicking "approve." Over time that leads to approval fatigue".
  Right (finding 3). It doesn't tie fatigue to the 93.
- "But ... also": the contrast is now clicks against attention. The figure doesn't show fatigue, but the
  company says fatigue happens. That's the page's own two claims, kept apart.
- The citation now sits after the quote, and it covers both the figure and the quote, which come from the
  same page.
- American spelling, house rate form, no new source.

## Consistency edit elsewhere

**Notes, "How this essay was made"** (line 416). The new line was checked on its own and needs naming.

Current: "and the resume study and the February 2026 case, both added on 20 November, were checked on their own
([check](../../cite-check/2026-11-20-piece-07-resume-paragraph.md), [check](../../cite-check/2026-11-20-piece-07-shambaugh-case.md))."

Replacement: "and the resume study, the February 2026 case, and Anthropic's figure on approval prompts, all added
on 20 November, were checked on their own
([check](../../cite-check/2026-11-20-piece-07-resume-paragraph.md), [check](../../cite-check/2026-11-20-piece-07-shambaugh-case.md), [check](../../cite-check/2026-11-20-piece-07-hughes.md))."

(The file `../cite-check/2026-11-20-piece-07-hughes.md` exists. Its c02 is AGREE-clean on evidence text.)

No other section needs a change.

## Verdict

The quote and the number are exact, but the "But" and "those prompts" make the 93 say more than the page does:
take the replacement above and the Notes edit, and the paragraph is accurate.
