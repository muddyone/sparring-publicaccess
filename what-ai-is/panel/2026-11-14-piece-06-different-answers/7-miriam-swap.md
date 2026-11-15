# Miriam Vale: re-read of the swapped worked example (essay 06)

_Scope: one paragraph, "What I'd do with this", beginning "Here's a time it happened to me." (draft lines
200-204, after commits df1d6c1e and 2f8b71cd). Read against the source record:
`docs/chatlogs/202609041804.the-diffusion-thesis-fails-and-agreeableness-outran-accuracy.md`, "Bugs found and fixed"
("Four fabricated quotations returned by a WebFetch summariser from arXiv:2605.18840, which also mis-described the
paper's entire subject. Caught by extracting the PDF and grepping."), and
`docs/research/what-ai-is/positions-drafts/06-moment-candidates.md` #1. I also read the rest of the draft's
routine and its "what does: a check that brings in something new" section. I did not consult my memory file.
No new sources were used._

**Verdict: ship after fixes.** The swap is a real improvement. A true, plain moment replaces a made-up one, and
it is explicitly tied to step 4. Three phrases say a little more than the record does, and the opening "it" lets
readers assume two answers disagreed when they didn't.

---

## (a) Does each claim trace to the record?

| Phrase | Traces? | Note |
|---|---|---|
| "I had an AI tool read a research paper and summarize it" | Yes | "WebFetch summariser". First person is accurate (staff work under Bart's direction). |
| "four quotations and an account of what the paper was about" | Yes | "Four fabricated quotations… mis-described the paper's entire subject." |
| "I pulled the paper's own PDF and searched it for the four quotes" | Yes | "extracting the PDF and grepping". |
| "None of them was there" | Yes | "fabricated" quotations, caught by a grep. |
| "the paper turned out to be about something else entirely" | Yes | "mis-described the paper's entire subject". |
| "and it read perfectly" | **No** | The record says nothing about how the summary read. This comes from the candidate write-up ("The summary read perfectly"), which cites no source for it. |
| "Nothing in how the summary sounded gave that away" | **No** | Same gap, and a stronger claim. The record shows *that* the quotes were checked, not that nothing prompted the check. It may be true, but the record doesn't say so. |
| "the one thing it didn't have, the paper itself" | **Overstated** | A WebFetch summariser fetches the page and summarises what it fetched, so the tool did have the paper in some form. What was new was the paper's full text read by a plain text search, not by another model's account of it. As written, this is the one line that could be factually wrong, and it is the line that ties the moment to the essay's thesis. |

**Fixes, impact order:**

1. **(Impact 7)** "checking the answer against the one thing it didn't have, the paper itself" → "checking the
   answer against the paper itself, searched word for word instead of summarized again." This traces to "extracting
   the PDF and grepping" and still makes the essay's point, since a text search brings in something no summary
   has. It also avoids claiming the tool never saw the paper.
2. **(Impact 5)** Cut ", and it read perfectly". The sentence works without it: "It came back with four quotations
   and an account of what the paper was about."
3. **(Impact 5)** Cut "Nothing in how the summary sounded gave that away." The essay already makes the
   "fluent isn't accurate" point, with sources, under "Trusting how it sounds" (lines 96-99), so the paragraph
   doesn't need an unsourced version of it. If Bart remembers the summary looking clean and wants the line, he can
   vouch for it. It should not stand on the current record alone.

## (b) Does it fairly illustrate the routine?

Mostly, yes. The paragraph itself names step 4, which is honest. The problem is the opening sentence. "Here's a time
it happened to me" follows the five steps in an essay titled for different answers. "It" has no clear antecedent,
so a reader can fairly take it to mean "two answers disagreed and I checked." In fact there was **one** answer, checked
against a source. The record shows one summary and no second draw.

4. **(Impact 6)** "Here's a time it happened to me." → "Here's a time step 4 caught something for me." This names the
   part of the routine up front and removes the implied disagreement. If the closing sentence changes as in fix 1,
   drop its "What caught it was step 4" so step 4 isn't named twice: "What caught it was checking the answer
   against the paper itself, searched word for word instead of summarized again."

The moment is still the right one. It shows the essay's harder half (lines 90-91): one confident answer that
nothing internal flagged, and that only an outside check could catch. It's fine that it doesn't show steps 1-3. Don't
add a sentence speculating about what a second summary would have said. The record doesn't say.

## (c) Does dropping the drug-interaction caution lose a point?

No. The caution was "check even if both answers agreed when being wrong would cost too much". The essay still
makes that point three times: step 3 ("If they agree, let your confidence rise, but don't stop there when being
wrong would cost you"), lines 90-91 ("a confident, consistent wrong answer passes the ask-twice test every time"),
and the paragraph right after the example ("Match the effort to what's at stake… For a decision that has to hold
up, it isn't"). The new moment also lands the point better than the caution did. It was one answer, untested by
agreement, and it was wrong. No clause is needed.

## Checks against the brief

- The paragraph names no exchange, date or paper. Good, and nothing here proposes adding them.
- No new sources are used or proposed.

## Fixed paragraph, for convenience (with fixes 1-4)

> Here's a time step 4 caught something for me. I had an AI tool read a research paper and summarize it. It came
> back with four quotations and an account of what the paper was about. I pulled the paper's own PDF and searched
> it for the four quotes. None of them was there, and the paper turned out to be about something else entirely.
> What caught it was checking the answer against the paper itself, searched word for word instead of summarized
> again.
