# Miriam Vale: argument review, essay 06 (first panel read), 2026-11-14

Lane: argument. Does the essay prove its position or only assert it, and is any sentence stronger than its
evidence?

**What I read:** my persona and memory (standing positions, plus
the craft notes on comparators, disclosure gestures, and the 2026-09-02 entry on "the effort-matched self-revision
control has the lowest net of all", which applies directly below); the panel brief; the draft; brief 12 (Bottom
line, Q2–Q6, Q8, A, Gaps and cautions); the options page; Paper 1 §6.3–§6.4
(`pilots/llm-judge-2026-05-02/v2/preprint-draft.md`, read only); and
`pilots/resolver-iteration-2026-06-29/results.md` (the §6.4 study's own record, to check what the paper's
summary leaves out). I added no new sources.

## Overall diagnosis

The essay is honest, warm and mostly well scoped. "Agreement isn't proof" is the best argument in it. It keeps
the unfavourable 55%, keeps the GPT exception, marks the Kim reading as ours, and scopes He to one open model.
The position is right in direction. **But the unifying principle ("a check that brings in something new",
summed up as "how independent they are") is stated more cleanly than the evidence allows, and the author's own
§6.4 study is the main thing it leaves out.** A fair critic will find that study, because it's ours and it's
published, and will ask why the essay reports half of it. Two lines also contradict the essay's own routine
("asking again brings in nothing" against "ask twice"). These are fixable without changing the position.
Verdict at the end.

**Strongest objection a fair critic would raise.** *"Your own published data says that the model quietly
revising its own work, with nothing new, ended with the fewest flaws, and that a self-review beat a fresh
neutral reader. So 'brings in something new' and 'independence' aren't what separates the checks that work.
On your own evidence, the job given to the check matters more, and so does who does the fixing."* As drafted,
the essay doesn't answer this. With findings 1 and 2 adopted it does, and the advice gets better.

---

## Ranked plan

### 1. Impact 9: the §6.4 study is reported selectively, and the omitted half cuts against the essay's thesis

> "The argument removed old flaws, but revising under that pressure added new ones. The final answers had about
> the same number of flaws as after one challenge and one fix ([Niedner 2026], §6.4)."

> "and models asked to correct themselves with no new information often fail, and sometimes get worse
> ([Huang et al. 2024])."

> "A check that brings nothing new mostly hands you the same answer back."

**The problem.** Everything quoted is true, but it isn't the whole result. Paper 1 §6.4 also reports that the
effort-matched control, the producer revising twice **on its own with no challenger**, came out *better* than
arguing to agreement (+0.375 and +0.750 flaws per output). Figure 4's caption says in words that "the
effort-matched self-revision control has the lowest net of all". The study's own record goes further: "neither
beats simply having the producer revise twice on its own" (`resolver-iteration-2026-06-29/results.md`:
self-revision 2.25 net flaws, one challenge and fix 2.625 same-vendor and 3.125 cross-vendor). So:

- The essay puts Huang ("with no new information often fail … sometimes get worse") right after a study of ours
  in which the no-new-information option did best. A reader of Paper 1 sees the contradiction at once. I
  recorded this caption as "the most findable error there is" on 2026-09-02, and it applies here again.
- The "reviewer with a different job" bullet relies on the 87% *catch* rate. The essay doesn't say that, in our
  own follow-up, those catches did not become a cleaner final answer once the model rewrote its work under the
  challenge. The challenger is a better *finder*; the rewrite is where new flaws came in.
- The cross-vendor arm (a different model as challenger) finished *worse* on net than the same-vendor one. That
  bears on the "a different model" step too.

This is selective disclosure in the direction that flatters the thesis, inside an essay with a "What this
doesn't claim" section. Having that section raises the standard for everything it leaves out.

**The fix.** Report the whole result. Then let it sharpen the advice rather than weaken it: the evidence
supports using a challenger to *find* problems and then checking those points yourself, not accepting the
challenger's rewrite. A sketch in Bart's register (the drafter rewrites):

> "I tested a structured version of this myself, with AI on both sides. In a pre-registered study, a second AI
> challenged the first one's work and the two argued until both agreed, or ran out of rounds, which happened
> more often. I compared that with one challenge and one fix. The challenge was good at finding the old flaws,
> but rewriting under that pressure added new ones, so the final answers came out about even. The plain option
> surprised me: the original model quietly revising its own work twice, with no challenger, ended with the
> fewest flaws of all (§6.4). That was 8 problems, with the flaws judged by AI, so it's a small result. What I
> take from it: a challenger is worth having for what it finds. The rewrite is a fresh chance to add mistakes,
> so check the fix as well."

Then reconcile the Huang line so it doesn't sit next to an unexplained counterexample. One clause does it:
quiet self-revision found fewer of the old flaws than the challenge did, and it also broke less. Huang is about a
model finding its *own* mistakes with nothing new, and that still holds. Paper 1 §6.4 supports "the challenge is
a genuinely better *detector*". Don't cite the 74% self-revision removal figure to the paper; it is in the study
record, not in the §6.4 text I read.

Carry the result into the reviewer bullet in one sentence: *"In a follow-up, those catches didn't turn into a
cleaner final answer when the model rewrote under the challenge (below), so the value is the list of problems,
which you then check."* Also replace "A check that brings nothing new mostly hands you the same answer back"
(see 2).

**Neighbourhood check for the drafter.** The new sentence sits between the Laban/Sharma paragraph and Smit/Huang.
After the edit, re-read "It matches the wider research, though": it now matches *part* of the wider research.
Narrow it to something like "That part matches the wider research".

### 2. Impact 8: the closing principle is contradicted by the essay's own numbers

> "What separates the checks that work from the ones that don't isn't how many there are. It's how independent
> they are. A check that brings nothing new mostly hands you the same answer back."

**The problem.** It fails on two counts, both within the essay.

- **"How independent."** A neutral fresh reviewer is *more* independent than self-review. It didn't write the
  work. Yet it caught 55% against self-review's 68%. A same-model challenger (Claude on Claude) brings in no new
  information, only a different job and no stake in defending the work, and it caught the most. The essay's own
  takeaway two bullets earlier is the correct one: "The job you give the check matters." The closing sentence
  replaces that with "independence", which the data doesn't support.
- **"Isn't how many."** The essay's own Wang result is *how many*: sample more answers, vote, and accuracy
  rises. Schoenegger is pooling twelve models. Brief 12 says "how independent they are matters **as much as** how
  many there are" (Bottom line, ours). The draft turned "as much as" into "not … but", which overclaims the
  brief's own reading.

**The fix.** Name the two things the evidence does show: what the check brings in (a source, a tool, a
different model), and the job it's given (find what's wrong, with no stake in the answer). Restore the brief's
weighting. For example: *"What separates the checks that work isn't how many you run or how hard you push. It's
what each one brings that the answer didn't have: a source, a tool, a different model, or a reader with no
stake in the answer and the job of finding what's wrong. Asking again with nothing new can show you where it's
guessing. It can't show you the mistake it makes every time."* That last pair also replaces "hands you the same
answer back", which Wang contradicts.

In "What does", make the reviewer bullet say what that reviewer brings: it didn't write the work and is told to
find fault. Otherwise the heading "a check that brings in something new" doesn't visibly cover it.

### 3. Impact 8: the position and "Where I land" contradict the essay's own routine

> (Position) "You don't make an answer reliable by asking the same model again or by pushing back until it
> agrees."

> (Where I land) "That makes the second answer useful. When the draws disagree, the disagreement is a warning
> you got for free. … Asking the same model again, or arguing it into agreement, brings in nothing."

**The problem.** The routine's first step is "ask twice". Wang says asking several times and voting raises
accuracy. "Where I land" calls the second answer useful and then, five lines later, says asking again "brings in
nothing". A careful reader catches this immediately, and it lands in the position itself. What the essay means is
that asking again is a *test*, not a *cure*: it exposes arbitrary errors and can't vouch for a consistent one.
The sentences don't yet say that.

**The fix.** Keep the bold voice and change the verb. Position: *"Asking the same model again can show you where
it's guessing, but it can't prove it right. Pushing back until it agrees proves nothing."* Where I land:
*"Asking the same model again can warn you; it can't vouch for the answer. Arguing it into agreement does
neither."* The position stays as strong, and it stops contradicting step 1.

### 4. Impact 7: "Compared to what?" sets a pushback figure against a no-pushback figure (flag 2, verdict below)

> "And it appears easier to talk out of a correct answer: models asked "are you sure?" changed their answer 46%
> of the time, while those examiners changed about one in ten on a plain retest, with nobody pushing back and on
> a different task. So the comparison is loose."

**The problem.** Three things differ at once: pushback against none, short classification tasks against
fingerprint decisions, minutes against seven months. Every difference makes the AI look worse. The sentence
labels them, but the labels come *after* the two numbers, and the reader remembers "46% against 10%". The
qualifiers don't undo the gap that the pairing creates. Separately, "talk out of a **correct** answer" is stronger
than 46%: that figure is the rate of *any* flip. The supported claim is that pushback alone moved the answer
nearly half the time and lowered accuracy on average. This is the inaccuracy that feels like rigour: unfair to
the AI in an essay whose yardstick is "describe it accurately".

**The fix.** Make the point without the mismatched pair. *"And it may be easier to sway. Asked nothing more than
'are you sure?', models changed their answer nearly half the time, and got less accurate. I couldn't find a study
that puts experts under the same push, so I can't say how they'd compare."* The concept stays and only the
invalid comparison goes, which is a cut of something that shouldn't be said at any length, not a cut for size.
Evidence that would make it a real comparison: a study of experts asked to reconsider a judgment under bare
challenge or social pressure. Don't name one from memory; it needs a search and the cite-check.

### 5. Impact 7: step 2 will misfire on the questions this reader actually asks

> "2. **If the answers scatter, believe the scatter.** Treat the subject as one where the model may be guessing"

**The problem.** Two scope gaps, and both make the step stronger than its evidence.

- **Wording against meaning.** Two answers from a chat assistant will almost always be worded differently. The
  essay's best source counts disagreement "in *meaning*, not just in wording" (Farquhar), and the body says so,
  but the step doesn't. A reader following the step literally will treat every rephrasing as a warning.
- **Questions with a right answer.** The evidence (Manakul, Farquhar, Wang) is about factual and maths questions.
  Ask for ten ideas twice and you get different ideas. That isn't guessing. "For a quick idea, one draw is fine"
  covers part of this but not the case where the reader wants a list or a draft.

This links to a limit the brief lists first under "Gaps and cautions" and the essay drops: the evidence is
"benchmark-heavy … transfer to 'help me think through this decision' is assumed, not shown".

**The fix.** Step 2: *"If the answers disagree on the facts, not just the wording, believe the scatter."* Add one
clause scoping the routine to questions that have a right answer. Add a "What this doesn't claim" bullet:
*"That this was tested on open-ended work. Most of the evidence is short questions with a right answer; whether
the scatter test works the same way on 'help me think this through' hasn't been shown."*

### 6. Impact 7: "Arguing with it" and step 5 treat bare pushback and pushback with evidence as the same thing

> "5. **Don't argue it into agreement, and don't judge it by its tone.** Neither tells you much."

> "So an answer you got by pushing too often just agrees with you."

**The problem.** Laban's pushback is a bare "are you sure?", with nothing new. The essay's own thesis implies that
pushback carrying a source ("this page says otherwise") is a check that brings in something new, which is step 4.
As written, step 5 tells the reader not to correct the model even when they hold the evidence. That's stronger
than Laban and works against the essay's own principle.

**The fix.** Step 5: *"Don't push back without a reason. 'Are you sure?' mostly gets you agreement. If you have
a source that says otherwise, give it the source: that's step 4, not arguing."* In the body, add "with nothing
new" after "pushing".

### 7. Impact 6: the radiologist figure measures different experts, and the essay presents it as if it were the same expert asked twice

> "When ten radiologists read the same mammograms, the share of cancer-free women each one recommended for
> immediate workup ranged from 11% to 65%"

**The problem.** Brief 12 Q2 separates these on purpose: the fair comparison for "the same AI gave two answers"
is the same expert asked twice, and Elmore 1994 is "Different people, same case". In the draft it sits straight
after the fingerprint retest as a second example of the same thing. The radiologist range is the counterpart of
asking a *different model*.

**The fix.** Label it, and let the label do work: *"And different experts, looking at the same case, disagree far
more: when ten radiologists read the same mammograms…"* Then one clause links it to the second-model point the
essay already makes.

### 8. Impact 6: "Nobody has yet run the study" certifies an absence; the brief says only "none found"

> "Nobody has yet run the study that would settle the comparison"

**The problem.** Brief 12: "No head-to-head study was found (search 2026-10-19)." A sentence saying what a
literature lacks is a claim about the whole literature, and one study proves it false. The essay gets this right
elsewhere ("I found no field study").

**The fix.** *"I couldn't find a study that settles the comparison…"* Use the same wording in "What would change
my mind" bullet 1 if needed.

### 9. Impact 6: "Its tone tells you nothing about whether it's right" goes beyond Q3

> "Its tone tells you nothing about whether it's right."

**The problem.** Brief 12 Q3 says that models are "partly aware of their own uncertainty, and say so badly", that
calibration improves with capability (Xiong), and that stated confidence elicited the right way was fairly well
calibrated (Tian, 3.6). The brief's own supportable line is narrower: "a model's fluent tone is the same whether
it is right or wrong". "Nothing" also conflicts with step 3's "raise your confidence" logic, and a reader might
start ignoring an "I'm not sure", which is itself a signal.

**The fix.** *"Its fluent, confident tone sounds the same whether it's right or wrong."* Make the matching change
in "Trusting how it sounds" if needed. Optional, and only with the essay's cite-check: brief 3.8 (Kim et al. 2024,
already cite-checked in essay 04) would support "if it tells you it isn't sure, take that seriously".

### 10. Impact 6: "What would change my mind" bullet 2 is already close to met, and the essay's most exposed claim has no falsifier

> "If checking with a second model turned out to fail broadly, because models share most of their errors"

**The problem.** The essay has just cited Kim: 60% the same wrong answer when both err, and larger models highly
correlated across companies. A critic will say "most" is already close to met. The condition needs to be something
the current evidence doesn't already approach. Separately, the claim the essay rests most on (checks that bring
in something new beat a model working with nothing new) has no falsifier, and our own §6.4 is the nearest
evidence against it (finding 1).

**The fix.** Bullet 2: *"If a different model turned out to catch no more of the first model's mistakes than
the same model checking itself…"*. That condition is measurable and it is the real question. Add: *"If a larger
version of my own study, with people judging the flaws, found that a model quietly revising its own work does as
well as a challenger at finding problems, not just at the final count, I'd drop the challenger from the list."*
Optionally add one for the first half: if the scatter test didn't track wrong answers in the chat apps people
actually use.

### 11. Impact 5: "Clever wording doesn't help either" and the 76-point result argue opposite ways

> "Clever wording doesn't help either. … And small changes of format that didn't change the meaning moved one
> open model's accuracy by as much as 76 points … An answer's polish and its accuracy are different things."

**The problem.** A reader hears "wording doesn't help" and then "wording moved accuracy 76 points". The real point
(brief 5.6, ours) is that the effects are large on single questions, unpredictable, and near zero on average. The
closing line is also about the answer's polish, while Sclar is about the prompt's format, so the paragraph's
evidence and its conclusion don't line up.

**The fix.** *"Wording can swing an answer a lot, but unpredictably: the same trick helps on one question and
hurts on the next. You can't word your way to a reliable answer."* End the paragraph on both: polish of the
answer, cleverness of the question.

### 12. Impact 5: "Ask a different model" rests on pooling twelve models; the evidence for a single second opinion is thinner

> "On 31 forecasting questions, the pooled forecasts of twelve models were statistically indistinguishable…"

**The problem.** The reader's step is "ask a different model", meaning one. The evidence is a crowd of twelve.
Brief 6.12: "No external study was found that cleanly isolates 'same model as checker' versus 'different model
as checker'". Our grid's cross-vendor advantage is one flaw (90% against 94%), and on net output it was worse
(finding 1). The step is reasonable advice, but the bullet reads as if it had been shown.

**The fix.** One sentence: *"The evidence is strongest for pooling many models; for a single second opinion it's
thinner, so treat it as one check among several."* If the drafter wants support from the brief, its 6.10 (Cohen et
al., an examiner model cross-examining another) is the kind of source that would carry it, and it goes through
the essay's cite-check.

### 13. Impact 4: the §6.4 setup needs two words of precision

> "I had a challenger and the original model argue until both agreed"

**The problem.** "A challenger" could be a person to this reader. Also, 12 of 16 runs hit the five-round cap
rather than agreeing (results.md; the §6.4 text says "twelve hit the cap").

**The fix.** It's folded into the sketch in finding 1: "a second AI", and "or ran out of rounds, which happened
more often".

### 14. Impact 3 (optional): an unmeasured superlative in the opening

> "And what you do next matters far more than which answer you started with."

This is rhetoric, and nothing in the essay measures it. "Matters more" keeps the voice and claims less. Optional.

---

## Clean checks (reported so they aren't re-litigated)

- §6.3 figures 87 / 68 / 55, "8 problems, flaws judged by AI", "Claude had produced", and the GPT exception all
  match Paper 1 §6.3. "The job you give the check matters" is the paper's own reading (the neutral 55% is "the
  attack posture is doing the work"). Fair.
- "That was one open model on one setup, and whether the assistants you use behave the same way hasn't been
  shown" (He) is correctly scoped.
- The Kim gloss is marked "My reading … though the study doesn't say why". Correct.
- Magesh: "sold as free of invented answers" is within the abstract ("eliminating" hallucinations) and the
  paper's title, and the register isn't demeaning. "So a source helps most when you … actually check" is our
  inference, but it reads that way and is reasonable.
- "What this doesn't claim" correctly carries the brief's three named limits. Its gaps are open-ended tasks
  (finding 5) and the §6.4 half (finding 1), not the three it lists.

## Flag 2 verdict: "Compared to what?"

**Honestly labelled, but not fair as built, and not clear enough for this reader.** Pairing the two numbers
creates a gap that the trailing caveats don't close, and every mismatch runs against the AI. "Talk out of a
correct answer" also says more than an any-flip rate shows. Keep the point and drop the pairing (finding 4).
Separately, label the radiologists as different experts, not the same expert asked twice (finding 7), and change
"nobody has run" to "I couldn't find" (finding 8). The section's *argument* is sound once those are fixed:
experts vary, professions build in second readers, so variation alone isn't a verdict. That is Part one's
yardstick, used correctly.

## Flag 3 verdict: "What I'd do with this"

**It reads as advice ("I'd suggest", "Match the effort"), which is right, but three steps are stronger than their
evidence.** Step 2 needs "on the facts, not just the wording" and a scope to questions with a right answer
(finding 5). Step 4's reviewer needs "then check what it finds, rather than taking its rewrite", from our own
§6.4 (finding 1), and "a different model" should be framed as one check among several (finding 12). Step 5 must
not forbid pushback that brings a source (finding 6). Steps 1 and 3 are well supported as written. None of these
fixes weakens the routine; each makes it safer for someone who will follow it.

## One-line verdict

**Needs another round.** The position survives, but findings 1–3 change what the essay says about its own
evidence and its central principle, and the result should be re-read as a whole rather than patched.
