_Substrate: Claude (subagent as Julian Crest). All 16 line edits applied; the README-baseline point he routed to Miriam was added as one sentence in the third-version paragraph._

I've read the piece, my persona, memory and the project context, and Nadia's and Miriam's panel records. I edited no files and wrote nothing to memory. I also looked at the follow-up pilot's README to make sure none of my edits shift a number. The GPT note quote ("Do not assume the next machine uses the same rule") matches the raw run file.

## Overall diagnosis

The piece now argues one thing, and the Gopnik section no longer breaks the thread where Nadia lost it. Its best line is the close of that section: "Judging by function doesn't answer her claim. It is how her claim gets heard." H.M. is still the best passage.

The remaining slack is in three places:
- **The word "discover" goes missing.** The opening promises the question "discover, or only receive?" The testing section, which is where the piece answers it, never uses the word.
- **The testing section is too heavy.** It runs 938 words. The next longest section has 451.
- **The ending doesn't land.** It stops on a concession and never comes back to the opening.

## 1. Through-line: where it slackens

1. **Nickname, "easy case" paragraph (Impact 6).** It points ahead to the harder case but never names what makes the nickname easy: the assistant was told it.
2. **Profiles close (Impact 8).** "What kind of learner" has two parts, and the piece still runs them together without saying so. One part is what a learner can keep (the H.M.-style profile). The other is where its knowledge comes from (received or discovered). This is Miriam's S2 and Nadia's blend, still half-open.
3. **The test payoff (Impact 8).** The probe 2c rule had to be found, so the result is evidence about discovery. The text never says so.
4. **The ending (Impact 7).** It closes on "larger than the nickname test suggests", which measures against the case the piece itself called easy. Nothing returns to the opening promise.
5. **"My comeback had a further flaw" (Impact 3).** This is the third time Bart's comeback is corrected: once in "Where this started", once in the soundbite sentence, and here. Each correction does different work, so I'd keep all three. I note it only because a fourth would tip it into self-flagellation.

## 2. Section weight: the testing section

Almost all of its length carries weight, so cutting won't fix the "lab report" feel. The fix is structure:
- Split it into two sections, about 230 and 700 words.
- Turn the two-readings bullets into prose.
- Remove three small bits of clutter.
- Make the payoff answer the opening question, so the study reads as the climax of the argument rather than an appendix.

These edits save about 50 to 70 words and drop nothing. Every number stays: 240 machines, four tests, 27/40 against 22/40, 8 in 10, 2 in 10, about 3 in 10, nine of ten notes, 10 of 10, and GPT's 8 against 6. All four limits stay word for word.

## 3. Repetition and echoes

- **Tolman's rats appear three times.** Cut the middle one, in the nickname section, where Otto already does that job. The rats then frame the piece from the definition to the payoff, and the callback lands harder across that distance.
- **"Doesn't really learn" appears three times.** Cut the second.
- **Agreement with Gopnik is stated three times in one section** (the heading, "largely right", and "and I think it's right"). Cut the third.
- **"Never becomes automatic" and "never becomes a reflex"** sit four sentences apart. Keep the reflex sentence, which has Anderson behind it.
- **Eight paragraphs or sentences open with "So".** My edits remove five.
- **"The harder case" and the nickname callbacks:** keep them. They are the piece's deliberate setup and payoff.

## 4. The ending

It doesn't land yet. One added sentence after the bullets closes the opening promise without adding a claim (edit 4 below).

## Line edits, most important first

**1. Payoff names discovery (Impact 8)**
- QUOTE: "And the rule was one Claude found in its own trials and chose to write down, which is the harder case the nickname test only pointed to."
- REPLACEMENT: "And the rule was one Claude found in its own trials and chose to write down: discovered, not received. That is the harder case the nickname test only pointed to."
- Why: the opening's question gets its answer in the opening's own words.

**2. Profiles close names both parts and hands off to the study (Impact 8)**
- QUOTE: "So the useful question isn't "does it learn?" Every learner has a profile. Ask what this one's is, and where its knowledge comes from: received, or discovered."
- REPLACEMENT: "The useful question, then, isn't "does it learn?" It is what kind of learner this is, and that has two parts: what it can keep, which is its profile, and where its knowledge comes from, received or discovered. My own study ended up asking both at once: can a rule a model discovers be kept in writing and carried to the next task?"
- Why: it ends the blend, echoes the title once at the pivot, and sets up the payoff. "Ended up" is accurate: the pre-registered study named the rules, and only the third follow-up version did not.

**3. Split the testing section (Impact 7)**
- QUOTE: "## What I'm testing"
- REPLACEMENT: "## Her claim, tested"
- Then insert "## What I'm testing" as a new heading directly before "None of these tests the part of Gopnik's paradigm…".
- Why: the first part finishes the Gopnik argument and the second is Bart's study. Separate headings break up the longest section and match each to its job. The "(below)" in the Gopnik section still points correctly.

**4. Ending lands (Impact 7)**
- QUOTE: "…and the distance between these learners is larger than the nickname test suggests."
- REPLACEMENT: "…and the distance between these learners is larger than I have allowed here."
- Then add a closing line after the bullets, before Sources: "That is where the argument belongs now: not whether it learns, but whether it can find out what nobody has told it."
- Why: the piece already concedes the nickname is the easy case, so measuring against it undersells the bullet. The new line returns to the opening promise in plain words and adds no claim.

**5. Two readings: bullets to prose, and the stray link attached (Impact 6)**
- QUOTE: "With nothing left to improve, there was nothing for notes to show. Two readings were open:" followed by the two bullets, the "The follow-up below leans…" paragraph and "(The result.)"
- REPLACEMENT: "With nothing left to improve, there was nothing for notes to show ([the result](../../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md)). Either the bias has closed in these newer models, or my task removed it, since the prompt named both possible rules up front. The follow-up below leans toward the first: even with the rules unnamed, the models usually named "needs two" correctly, about three times in four. Whichever it was, testing whether notes carry a rule needed a harder task."
- Why: two short bullets make this read like a lab report, and the standalone "(The result.)" reads like a footnote that slipped. Nothing is lost.

**6. Nickname section plants the word "received" (Impact 6)**
- QUOTE: "The nickname is the easy case, because the user supplied it."
- REPLACEMENT: "The nickname is the easy case, because the user supplied it: the assistant received it."
- Why: it plants the word the payoff will answer.

**7. Give "which thing learns" its own heading (Impact 6)**
- Insert "## Which thing learns" before "A common objection points at the frozen model".
- Why: "The nickname test" no longer describes the last two paragraphs. The nickname section then ends on its forward pointer to the study. "Each learner meets the definition at its own level" becomes the new section's close, and it is a strong one. No wording in the approved paragraphs changes.

**8. Anchor GPT's numbers (Impact 5)**
- QUOTE: "GPT's notes treated each machine as new ("Do not assume the next machine uses the same rule"), and its 8 against 6 is within chance."
- REPLACEMENT: "GPT's notes treated each machine as new ("Do not assume the next machine uses the same rule"). It got the final machine right 8 times in 10 with notes and 6 without, which is within chance."
- Why: "8 against 6" makes the reader work out what is being compared. This matches the README table (8/10 with notes, 6/10 without).

**9. Imitation contrast placed next to its result (Impact 5)**
- QUOTE: "The 2023 models did worse, pulled toward the object most associated with the usual tool. GPT-4 did best, at 76%. Those were 2022–23 models, and newer ones have narrowed the gap (below). On the matching *imitation* question ("which goes best with a compass?"), the models did well."
- REPLACEMENT: "The models did worse, pulled toward the object most associated with the usual tool. GPT-4 did best, at 76%. On the matching *imitation* question ("which goes best with a compass?"), they did well. Those were 2022–23 models, and newer ones have narrowed the gap (below)."
- Why: innovation against imitation is the point of the experiment, and the dating caveat currently splits the pair. It also removes the mismatch between "2023 models" and "2022–23 models".

**10. Soundbite sentence (Impact 5)**
- QUOTE: "Her soundbite was ("don't learn or think the way we do"), and so was my comeback."
- REPLACEMENT: "Her soundbite was about form ("don't learn or think the way we do"), and so was my comeback."
- Why: read aloud, "was" followed by a parenthesis sounds like a fragment.

**11. Third statement of agreement (Impact 5)**
- QUOTE: "So her real claim stands, and I think it's right: **a learner"
- REPLACEMENT: "Her real claim stands: **a learner"
- Why: the heading and "largely right" have already said it.

**12. Profiles paragraph: remove the repeat and split (Impact 5)**
- QUOTE: "a written rule has to be looked up at the right moment, and it never becomes automatic."
- REPLACEMENT: "a written rule has to be looked up at the right moment."
- Also start a new paragraph at "My guess is that for knowledge work…".
- Why: "never becomes a reflex" says the same thing three sentences later, with the citation. The paragraph carries five ideas; splitting it separates the profile from Bart's estimate.

**13. "Built one" sentence (Impact 4)**
- QUOTE: "So I built one, in small, tightly funded steps, each designed from what the last one showed"
- REPLACEMENT: "I built one, in small steps, each designed from what the last one showed"
- Why: "tightly funded" is clutter, and the Grok sentence already carries the spending limit. "Each designed from what the last one showed" stays because it supports the exploratory caveat.

**14. Middle Tolman echo (Impact 4)**
- QUOTE: "A note that sits unused until it's needed is like what Tolman's rats had: knowledge waiting for its moment. "
- REPLACEMENT: delete the sentence.
- Why: it is the second of three rats, and Otto does this job here. Cutting a comparison is not softening a claim.

**15. Third "doesn't really learn" (Impact 4)**
- QUOTE: "Most claims that AI "doesn't really learn" quietly add a requirement about form"
- REPLACEMENT: "Most objections quietly add a requirement about form"

**16. Two more "So" openers (Impact 3)**
- QUOTE: "So on these tasks, accuracy has narrowed" → REPLACEMENT: "On these tasks, then, accuracy has narrowed"
- QUOTE: "So it suggests, short of proving it, that" → REPLACEMENT: "It suggests, short of proving it, that"

## The approved paragraphs (flag only, no rewrite)

- **Second-grader paragraph:** the reader hears the objection twice before the answer, first in the setup sentence and then in the Shardlow quote.
- **Line-of-models paragraph:** no craft problem. Its last sentence closes the new section well.

## For Miriam

The README warns that the unnamed prompt widened what the models considered, which lowered Claude's no-notes baseline. That was part of Miriam's item 3, and I can't find it in the text. If it was left out on purpose, fine. If not, it goes back to her, not to me.

## For Rosetta

- The italic header is still lab paperwork.
- "Gopnik's paradigm" is jargon.
- In the Samiei bullet, "still takes them more tests" doesn't say more than what. Nadia raised it and it is still open.
- The blicket bullet is dense.
- The table row "Rules over impulses" is unclear.
- "Proceduralization" is jargon.

## Verdict

As argument, the piece works. Edits 1 to 4 make it work as nonfiction too: the reader is promised one question, follows it, sees it tested, and is handed back to it at the end.
