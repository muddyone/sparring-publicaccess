# Rosetta: plain language and comprehension, essay 06 (first review), 2026-11-14

Reviewer: Rosetta (communications / plain-language). Reader held throughout: an everyday AI user who
has seen ChatGPT or Claude give two different answers and wants to know what to do.

What I read: the brief (`brief.md` in this folder); the draft
(`drafts/2026-11-14-06-different-answers.md`); Part one's `positions/02-it-learns.md` and all six
Part one titles; brief 12 (only to check that each rewrite below stays inside its claim, with the
lines named where it mattered); my persona and memory (the two entries that bore on this: the
2026-10-28 "hear it through the narration builder" lesson and the whole-artifact pass in my charter).
I ran `newsletter-what-ai-is/narration/build-scripts.py`'s `speakable()` on the draft; quotes marked
**aloud** are its output. No new source is proposed anywhere below.

Each finding: impact (1-10), the passage, the reader's problem, the fix. The drafter rewrites every
adopted fix; my wording is a target, not copy.

---

## Findings, ranked

### 1. The rule the reader acts on has two names, and its "it" points at the wrong thing (impact 9)

> Title: "Believe the disagreement, then check **it** against something new."
> Position and routine step 2: "believe the **scatter**"
> Where I land: "Believe the disagreement. Then check **it** against something new."

The brief says the reader will act on exactly one rule of thumb. The draft gives it two names,
"scatter" (position, "The disagreement is information" section, step 2) and "disagreement" (title,
landing). A reader carrying the rule away has to work out that they are the same instruction. And
"check it" grammatically checks *the disagreement*, which you can't do: you check *the answer*.

Fix: one name, everywhere the reader is told what to do. "Disagreement" is the plainer word, so keep
it and retire "scatter" as an instruction (it can stay as a description: "the answers scatter").
Title: "Believe the disagreement, then check the answer against something new." Step 2: "If the
answers disagree, believe the disagreement." Landing: "Then check the answer against something new."

### 2. "17.9 percentage points" is a unit the reader doesn't use, and it is the third spelling of one scale (impact 8; drafter flag 5)

> "On a set of grade-school maths word problems, accuracy rose by 17.9 percentage points"
> elsewhere: "accuracy still varied by up to 15%" and "by as much as 76 points"

Whole-artifact count first: the essay carries about seven kinds of number (shares of the time,
x-in-ten, a range across people, counts of runs and versions, catch rates, score swings, a crowd size).
That is fine for an essay in which every number is a reason to believe. But **one** of those kinds,
the change in a score out of 100, is written three ways in three sections: "15%", "17.9 percentage
points", "76 points". The reader has to wonder whether these are three different things. They are one.

"Percentage points" is a researcher's unit; the reader hears "17.9%" and can't feel it either way. The
decimal adds nothing they act on.

Fix: one spelling, in words the reader counts in: **"points out of 100"**, then the plain meaning.

> "Ask several times and keep the answer that comes up most often, and on grade-school math word
> problems a model got about 18 more problems right out of every 100."

Constraint for Vera: this rewrite is correct only if Wang's +17.9 is an absolute gain in accuracy (the
abstract writes "+17.9%"; brief 12 line 319). I suspect it is (the draft's "percentage points" reading
assumes the same), but I can't confirm it from the brief, and the rewrite must wait on her. If it turns
out to be relative, the sentence becomes "about 18% better than its usual score". Apply the same spelling
to the other two: "its score still swung by as much as 15 points out of 100 between identical runs"
(Vera: same check, since Atil's "15%" is abstract-level, brief 12 line 108) and finding 6 for the 76.

**Verdict on flag 5:** not usable as written. Usable as "about 18 more right out of every 100" once
Vera confirms it is absolute.

### 3. The "are you sure?" 46% lands before it is explained, and the comparison sentence is the hardest in the essay (impact 8)

> "And it appears easier to talk out of a correct answer: models asked "are you sure?" changed their
> answer 46% of the time, while those examiners changed about one in ten on a plain retest, with
> nobody pushing back and on a different task. So the comparison is loose."

Three problems in one sentence. (a) The reader meets 46% here with no source and no setup, then meets
it again, properly introduced, two sections later ("Arguing with it"). The first meeting is the
confusing one. (b) It sets "46%" against "one in ten", two scales in one breath; the reader has to
convert to compare. (c) "with nobody pushing back and on a different task" is three qualifiers stacked
after a comma; on first read it isn't clear they are the reasons the comparison is loose.

Fix: same scale, the caveats as their own sentence, and a pointer forward.

> "And it seems easier to talk out of a right answer. Ask a model "are you sure?" and it changes its
> answer nearly half the time (more on that below). The fingerprint examiners changed about one in ten
> of theirs, but nobody was pushing them: they were shown the same prints again, months later, on a
> different kind of task. So this comparison is loose."

### 4. "Its tone tells you nothing" needs the half that makes it a difference (impact 7, additive)

> "And two differences cut against the AI. Its tone tells you nothing about whether it's right."

This is meant as a difference between AI and experts, but the reader is given only the AI half. Why
would an expert's tone tell you more? Without that, the sentence reads as a general complaint, not a
comparison.

Fix (brief 12 supports it, line ~310: experts are "usually read alongside their track record; a model's
fluent tone is the same whether it is right or wrong"):

> "An expert's confidence comes with a track record you can check. A model sounds just as sure when
> it's wrong as when it's right."

### 5. "The same idea works the other way", then "That gives everyone a test": two connectives that don't connect (impact 7, flow)

> "The same idea works the other way: ask several times and take the most common answer, and accuracy
> goes up. [...] That gives everyone a test they can run for free."

"The other way" from what? The reader has to work out that the first two studies *flag* bad answers and
Wang *improves* them. Then "That gives everyone a test" points back at Wang (the nearest thing), but the
test it introduces is the warning test (scatter means guessing), not majority voting. The paragraph
opens from the wrong predecessor.

Fix:

> "The same signal can improve answers as well as flag bad ones. Ask several times and keep the answer
> that comes up most often [...]."
> "All three findings point the same way: whether the answers agree tells you something. That gives
> everyone a test they can run for free."

### 6. "76 points" on "one open model": two terms the reader doesn't have (impact 6)

> "small changes of format that didn't change the meaning moved one open model's accuracy by as much as
> 76 points"

"Open model" first appears in the He sentence ("one open model on one setup") and is never said in
words. To an everyday user, "open" might mean "OpenAI's". "Points" of what (finding 2). "Changes of
format" is abstract.

Fix: define once at first use (the He paragraph): "one open model (one anyone can download and run)".
Here: "Changing only the layout of a question, not its meaning, swung one such model's score by as much
as 76 points out of 100." Don't name specific formatting (spacing, punctuation) unless Vera confirms it
from the paper; brief 12 says only "formatting changes" (line 369).

### 7. A forward promise that skips a section (impact 6, flow)

> End of "Agreement isn't proof": "That's where the second half of my position comes in."
> Next section: "Compared to what?" ("Before going further...")

The reader is promised the second half, then given a detour, then two habits that don't work, and only
then the second half ("What does"). By then the promise has gone cold.

Fix: end the section on the need, and flag the detour.

> "So you need a check that can catch a consistent error. I'll come to those after one fair question."

"Before going further" can then stay.

### 8. Words that mean two things, or three words for one thing (impact 6)

- **"Sampling"** means *picking the next word* in "Why the answers differ" ("sampling from among the
  likely words") and *asking the question again* in "Agreement isn't proof" ("Sampling catches errors
  that come out differently each time"). Fix: "Asking again catches errors that come out differently
  each time." Same in "simply sampling several answers" (Smit): "simply asking for several answers and
  taking the most common".
- **The no-randomness setting** has three names in one paragraph: "a setting that turns the randomness
  off", "set to be deterministic", "the "no randomness" setting". Fix: name it once ("the setting that
  turns randomness off") and say "set that way" after. "Deterministic" then never appears.
- **"Completions"** ("gave 80 different completions"): "80 different versions of the answer".

### 9. "The arbitrary kind" names a category without saying what it is (impact 6, additive)

> "used it to flag one kind of invented answer, the arbitrary kind, across many tasks"

The reader can't picture an "arbitrary" invented answer, and the whole of "Agreement isn't proof" rests
on the difference between that kind and the consistent kind.

Fix (inside Farquhar's own wording, "arbitrary and incorrect generations", brief 12 line 333):

> "...to flag one kind of invented answer: the kind the model makes up fresh each time, so it comes out
> differently on every try."

Then "the arbitrary ones" in the next section can read "the ones that change from try to try", which
sets up "an error the model makes the same way every time" by direct contrast.

### 10. "Part one kept asking: compared to what?" sends the reader off-page (impact 5, additive)

> "it's worth asking the question Part one kept asking: compared to what?"

This is Part two's first essay. A reader arriving here may not have read Part one, and the sentence's
force depends on knowing what the question meant there.

Fix: say it in place. "...the question Part one kept asking: compared to what? Not compared to a
perfect answer no one gives, but to the people who'd otherwise do the job."

### 11. Step 1 tells the reader to use a fresh conversation without saying why (impact 5, additive; the reader acts on this)

> "1. **For anything that matters, ask twice,** in a fresh conversation. It costs a minute."

A reader who doesn't know why will ask again in the same chat, and the routine breaks. The reason is in
brief 12 (line 230, marked as the brief's own reasoning): in a fresh conversation the model has no memory
of its first answer, so the second is closer to an independent draw.

Fix: "...in a new conversation, so it can't see its first answer. It costs a minute." The same reason
makes "you can ask it ten times, independently" (in "Compared to what?") land: add "in fresh
conversations" there.

Also step 4, "give a reviewer a specific job": say who, for this reader. "Give a colleague, or a fresh AI
chat, a specific job".

### 12. "An answer you got by pushing too often just agrees with you" garden-paths (impact 5)

> "So an answer you got by pushing too often just agrees with you."

On first read it parses as "pushing too often", then has to be re-parsed. Fix: "So when you push until
it agrees, the answer you end up with is often just your own view handed back."

### 13. Research words that are near-meaningless to this reader (impact 5)

State the thing, not the term.

- **"pre-registered study"**: "a study whose test I wrote down and fixed before running it". Once.
- **"a challenger"** (§6.4 paragraph): undefined. "a second AI told to find flaws".
- **"a neutral fresh reviewer"**: "a fresh AI asked simply to review it".
- **"the self-review gap nearly vanished"**: "When the work came from GPT, GPT checking its own work did
  nearly as well as the challenger" (brief 12 A.3: self-review's shortfall "nearly vanished for GPT-5.2").
- **"87% of the serious flaws"**: of what? Add once: "of the 31 serious flaws a panel of three AIs had
  confirmed" (brief 12 A.3). Keep the percentages, since three catch rates on one scale compare cleanly.
- **"statistically indistinguishable from those of a crowd of 925"**: "about as accurate as a crowd of
  925 people; the study couldn't tell the two apart". Don't write "as accurate as": that overclaims.
- **"benchmark"** (three uses): "a standard test set" at first use.
- **"developer access"**: "the versions companies sell to programmers, not the chat apps".
- **"immediate workup"** (Elmore): "sent straight for more tests".
- **"17–33% of the time"** (Magesh): "between about one answer in six and one in three".

### 14. The radiologist figure switches what is being measured without saying so (impact 5)

> "When ten radiologists read the same mammograms, the share of cancer-free women each one recommended
> for immediate workup ranged from 11% to 65%"

The fingerprint sentence is *the same person, twice*, which is the essay's subject. The radiologist
sentence is *different people, once*. The reader isn't told about the switch, so the two read as one
kind of evidence. The sentence is also the densest in the section: a share of a subgroup, ranged across
people, as a percentage range.

Fix: signal the switch and use counts the reader can picture.

> "Different experts disagree with each other, too. Ten radiologists read the same mammograms. For
> women who turned out not to have cancer, the most cautious sent about 2 in 3 for more tests; the least
> cautious, about 1 in 10."

(11% to 65% across radiologists, brief 12 line 186. "Most and least cautious" is my reading of highest
and lowest share; Vera may prefer "one ... another".)

### 15. Aloud: three citations get read out mid-sentence (impact 4)

`speakable()` output:

> **aloud:** "...had no significant effect overall (Meincke et al. 2025a; Meincke et al. 2025c)."
> **aloud:** "...after one challenge and one fix (Niedner 2026, §6.4)."
> **aloud:** "...a neutral fresh reviewer caught 55% (Niedner 2026, §6.3)."
> **aloud:** "...a method introduced by Lewis et al. 2020, substantially reduced..."

The Meincke pair is read because the builder's citation pattern allows "2025a/b" and not "2025c"; the
Niedner pair because of the section locator. "Section sign six point four" is noise to a listener.
Fix: either widen the builder's pattern (`[ab]?` to `[a-z]?`, and allow a ", §n.n" tail), or move the
section numbers into the link text and the notes. For Lewis, keep the verifier's Lewis/Shuster split but
take the cite out of the sentence: "Giving the model documents to answer from, a method first described
in 2020 (Lewis et al. 2020), ..." A single-link parenthesis drops cleanly.

### 16. Spelling drifts from the series (impact 3)

"grade-school **maths**" and "in the AI's **favour**". Part one writes "favor" and "behavior"
(`positions/01`, `03`, `05`), and "grade-school maths" mixes an American phrase with British spelling.
Fix: "math", "favor".

---

## Verdicts on the drafter's flags

**Flag 1, length (2,151 words): under-explained, not over-long.** The essay is clear in its spine and
thin in about ten specific places, all listed above as additive: findings 3, 4, 9, 10, 11, 13, 14. Taken
together they add perhaps 200-300 words and stay below Part one's range. Nothing needs cutting for the
reader. Nothing needs a new source.

**Flag 4, the title: length is fine, one word is wrong.** Two sentences, 15 words, is in the series
pattern (`02`, `04`). The problem is "check *it*": the disagreement can't be checked, the answer can.
Recommend "Same question, different answer. Believe the disagreement, then check the answer against
something new." Keep the rule's name identical in title, position, step 2 and landing (finding 1).

**Flag 5, "17.9 percentage points": not usable as written.** Use "about 18 more right out of every 100",
after Vera confirms the gain is absolute (finding 2).

---

**Verdict: ready after fixes.** The argument is clear; the fixes change how the claims are carried,
never what they claim. Findings 1-3 are the ones a reader would stall on.
