# Rosetta: plain-language review, essay 08 (first panel read), 2026-11-23

Reviewer: Rosetta (communications / plain language). Reader held throughout: an everyday AI user who has
heard "AI is making us stupid", wonders whether leaning on it costs them their own skills, and will act on
the six steps and on one rule (choose on purpose which skills to keep, starting with the ones you need to
judge the work, and keep learning them on purpose).

What I read: the brief (`brief.md` in this folder); the essay (`positions/08-worse-at-own-work.md`, body
and Notes); brief 14 and brief 14b, only to keep every rewrite inside what they say a source says (sections
named where it mattered); my persona and memory (the entries that bore on this: the whole-artifact pass,
the 2026-10-28 "hear it through the narration builder" lesson, the 2026-09-14 rule that a presupposing
word needs its pair on the page, and essay 07's lesson that a word the series has defined must not be
reused for something else). I ran `newsletter-what-ai-is/narration/build-scripts.py`'s `speakable()` on the
body; quotes marked **aloud** are its output. No new source is proposed anywhere below.

Each finding: impact (1-10), the passage, the reader's problem, the fix. The drafter rewrites every adopted
fix; my wording is a target, not copy. The cap limits packaging, never the message: nothing below cuts a
concept, and every additive fix says what it buys the reader.

---

## Findings, ranked

### 1. The specialists paragraph sets up a question the essay answers 160 lines later, and "the same pattern" points two ways (impact 7; flag 3)

> "I don't have those skills, and I don't need them. Leaning on other people's skills is how working life
> has always run.
>
> AI follows the same pattern. Here's where the cost lands."

The section has just given two patterns: tools cost you the skill they take over, and leaning on other
people is normal. "The same pattern" can be either. If it is the second, the reader has just been told
there is no cost (I don't need those skills), so "Here's where the cost lands" contradicts the sentence
before it. The reader also notices that you don't *manage* your surgeon, so the paragraph seems to step
outside the management frame, and nothing tells them it will come back. It does, well, in "Where the
comparison needs care" (licenses and track records do the judging), but by then the reader has either
stalled or forgotten.

Fix (additive, about 25 words): plant the hook where the setup is, and name which pattern AI follows.
Target:

> "...Leaning on other people's skills is how working life has always run. And I don't check their work
> myself: something else does that for me, which I'll come back to.
>
> With AI, the first pattern holds: it costs you the skills you hand it. Here's where that cost lands."

Buys the reader: no contradiction at the turn into the evidence, and a reason to hold the specialists in
mind until the pay-off.

### 2. The AI-employee study names "the label" before the reader knows there are labels, and then leaves the reader with only a "don't" (impact 7; flag 4)

> "So be the manager, but don't think of the AI as an employee. In a study of 1,261 managers reviewing the
> same drafts with planted errors, the label made little difference on average. But in organizations that
> already put AI agents on their org charts, managers told the draft came from an 'AI employee' caught
> fewer errors than those told it came from an 'AI tool'"

"The label" presupposes a pair the reader hasn't met; the two labels arrive one sentence later, inside a
36-word sentence. The reader then reaches "don't think of the AI as an employee" with no picture of what to
think of it as, in an essay titled "moving into management". The reader asks: manage *what*, if not staff?

The study itself supplies the answer: the "AI tool" label is the one under which managers kept checking
(brief 14b §5.5). So the positive image is derivable, not new.

Fix: introduce the two labels first, then the result, then the image to carry away. Target:

> "So be the manager, but don't think of the AI as an employee. In one study, 1,261 managers reviewed the
> same drafts with planted errors. Some were told the draft came from an 'AI employee', others from an 'AI
> tool'. On average the label made little difference. But in organizations that already list AI agents on
> their org charts, managers told 'AI employee' caught fewer errors. Think of it as a tool you direct and
> check: that's the label under which they kept looking."

Buys the reader: a "do" to go with the "don't", and the management frame survives the caution intact.
(The last sentence is our reading of the study's comparison; if Vera thinks it goes further than §5.5,
keep "Think of it as a tool you direct and check" and drop the clause after the colon.)

### 3. The Notes put the cite-check link where it reads as checking the second brief, which hasn't been checked (impact 7; honest claim)

> "Three of its sources were checked again against the originals before drafting, and a second brief
> gathered the evidence on the management comparison (brief) (check)."

The "check" link sits directly after the second brief, so the reader takes it as that brief's check. It is
the three-source check of brief 14's sources. Brief §4 says brief 14b has **not** been cite-checked. The
paragraph before also says brief 14 "was checked by a tool that looks each source up", which primes the
reader to assume the same for the second brief.

Fix: move the link to the sentence it belongs to, and say the second brief's status in plain words.
Target:

> "Three of its sources were checked again against the originals before drafting (check). A second
> brief gathered the evidence on the management comparison (brief); it has not yet been through the
> same tool."

(If `/cite-check` runs on 14b before publication, say so instead.) Buys the reader: the Notes say exactly
how far the evidence was checked, which is the series' own rule.

### 4. "Any more than calculators did" will be heard as "calculators cost nothing" (impact 6; flag 7)

> "Handing work to AI won't make you stupid, any more than calculators did."

In plain reading, "any more than calculators did" means "calculators didn't". The reader has just been
shown that calculators did cost fourth graders their pencil-and-paper skills, and the essay itself said
the worry "has something real in it". So the landing's first sentence seems to take back the essay's most
careful point, in the place the reader is most likely to quote.

Fix: keep "won't make you stupid" (the evidence supports rejecting the broad claim) and say what
calculators actually did. Target:

> "Handing work to AI won't make you stupid. Like calculators, it costs you the particular skills you hand
> it, most of all while you're still learning them."

Then "It's closer to a promotion..." follows unchanged. Buys the reader: the landing agrees with the
evidence they just read. (The argument call on whether "stupid" is earned at all is Miriam's and Vera's;
this is about what the sentence says to a plain reader.)

### 5. The developers' numbers switch from speed to time mid-sentence, and 24% "faster" is not what the study counted (impact 6; flag 6)

> "Before they started, they expected AI to make them 24% faster. Afterwards, they believed it had made
> them about 20% faster. In fact, with AI they took 19% longer"

The source counts time: developers forecast AI would "reduce completion time by 24%", estimated afterwards
it "reduced completion time by 20%", and in fact it "increases completion time by 19%" (brief 14 §2.4).
"24% faster" and "24% less time" are not the same number, and the reader has to switch from a speed scale
to a time scale for the punchline. The felt point (they were wrong about the direction, not just the size)
is left for the reader to work out.

Fix: one scale, time, in words the reader can weigh, and the felt point said. Target:

> "Before they started, they expected AI to cut their time by about a quarter. Afterwards, they believed it
> had cut it by about a fifth. In fact, with AI they took about a fifth longer. They didn't just
> overestimate the gain; the gain was a loss, and they didn't notice."

Buys the reader: the second trap ("losing touch without noticing") shown in one sentence they can repeat.

### 6. The pilots study says physical skills held up; the next paragraph opens with "physical skills deteriorate" (impact 6)

> "their hand-flying skills were mostly intact... What had slipped were the *thinking* parts of flying by
> hand"
>
> "In 1983, the engineering psychologist Lisanne Bainbridge put it plainly: 'physical skills deteriorate
> when they are not used'."

"Put it plainly" tells the reader Bainbridge is summarizing what they just read. But what they just read is
the opposite: the physical skill held. The reconciliation (thinking skills fade faster than physical ones,
Arthur et al. 1998) arrives four sentences later. A careful reader stalls here and wonders which is true.

Fix: open the Bainbridge paragraph from the pilots, not as a summary of them. Target:

> "None of this is new. In 1983, the engineering psychologist Lisanne Bainbridge warned that 'physical
> skills deteriorate when they are not used'..."

and then let Arthur's sentence close the loop explicitly: "...and thinking skills faded faster than
physical ones, which is what the pilots showed." Buys the reader: the two findings read as one story
instead of a contradiction.

### 7. "The two habits cancelled out" says more than the source does, and "the effect" has no object (impact 6; honest claim)

> "Overall, the effect came out at zero, because the two habits cancelled out"

Brief 14 §1.3: the pre-registered experiments found "no effect of LLMs on overall learning outcomes"; the
split by habit came from "exploratory analyses and a field study". The source does not say the zero is
*because* of the split. "The effect" also has no object: the effect of what, on what? (And "cancelled" is
British; American is "canceled". The fix removes the word.)

Fix: Target:

> "Overall, using AI made no difference to how much they learned. The split by habit came from a looser,
> follow-up analysis, but it points the same way as the rest of this section."

(The second clause is our framing; Vera may prefer just "came from a looser, follow-up analysis".) Buys
the reader: an accurate picture, and the habit finding keeps its force without carrying a causal claim.

### 8. Two key rates are on scales the reader can't weigh: "28.4 of every 100" and "19 percentage points" (impact 5; flag 6)

> "they found such growths in 28.4 of every 100... the rate was 22.4 in every 100"
>
> "consultants using AI were 19 percentage points less likely to get the right answer"

"28.4 of every 100" asks the reader to picture four-tenths of a colonoscopy, and gives no felt size for the
drop. "Percentage points" is a research term the reader can't distinguish from "percent". The essay
already uses "in every 100" well; put both on it, whole numbers, with the stake. Brief 14 §2.1 gives the
absolute difference (6.0 in 100), so the stake is derivable.

Fix: Target:

> "...they found such growths in about 28 of every 100. In the three months after..., about 22 in every
> 100: six fewer patients in every 100 whose growths were found."
>
> "On a task just outside them, for every 100 consultants, about 19 fewer got the right answer with AI
> than without it."

(Keep the decimals in the Notes or the brief if Vera wants them on the record.) Buys the reader: one
scale for both numbers, and a consequence they can feel.

### 9. "One version worked like ordinary ChatGPT": the other version is 200 lines away, and 48% / 17% have no felt size (impact 5; flag 6)

> "One version worked like ordinary ChatGPT. While students had it, their grades on practice problems rose
> 48%. Then it was taken away. After that, those students' grades were 17% lower..."

"One version" presupposes a second; the reader looks for it and doesn't find it until "What I'd do with
this" ("a second tutor was built to guide students"). Meanwhile 48% and 17% are relative changes the reader
may read as points.

Fix: name the pair here and promise the second; say the sizes in words beside the figures. Target:

> "The researchers built two versions. One worked like ordinary ChatGPT; I'll come back to the other.
> While students had the ChatGPT-like one, their grades on practice problems rose by about half (48%).
> Then it was taken away. After that, their grades were about a sixth lower (17%) than those of students
> who had never had it."

Buys the reader: no dangling "one", and the shape of the finding (help while you have it, harm after) in
words they can repeat.

### 10. "Agent" means people three times in an essay where the series has made it mean AI (impact 5)

> "machines were far more likely than human agents to carry out fully unethical instructions"
> "In a study of 5,172 customer-support agents, AI help raised productivity"
> "But that held only for agents who had followed the AI closely"

Essay 07 defined "agent" as an AI you've let act for you, and this essay uses it that way ("the kind of AI
the last essay called an agent", "AI agents on their org charts"). Then three times it means a person. The
customer-support ones are recoverable; "agents who had followed the AI closely" is not, two sentences
after "AI help", and the Köbis quote, set right after "a team pushes back", briefly reads as "AI agents".

Fix: "customer-support workers" (both places). For Köbis, keep the quote but gloss the word in the same
sentence: "...machines 'were far more likely than human agents', people given the same instructions, 'to
carry out fully unethical instructions'", or quote shorter. Buys the reader: one meaning for the series'
key word.

### 11. "Observational" is the essay's main caveat word, and it is never explained (impact 5)

> "That's one observational study, and it's contested" · "Both are observational studies, and they show..."

The reader is meant to weigh the colonoscopy finding and the management evidence by this word, and it is
a research term. They can't tell what it takes away.

Fix: gloss it once, at its first use (Budzyń), with what it means for the number. Target: "That's one
observational study, meaning the researchers watched what happened rather than testing it, so something
else that changed in those months could explain the drop." The Artz sentence can then stand. Buys the
reader: every later "observational" carries its weight.

### 12. Bart's own moment doesn't say whether the outside review happened (impact 5)

> "so I didn't count my own review of the AI-assisted work as the check. The paper sends that part to a
> named outside expert review instead"

"Sends that part to a named outside expert review" can mean the review was done, or that the paper names
it as the check still owed. A reader can't tell, and it is the essay's only first-hand example of step 3.
I'm not changing the fact (it is first-hand and §4 says don't ask for more); the drafter knows which it is.

Fix: say which in plain words ("...so the paper names an outside expert to check that part", or "...so an
outside expert checked that part"). Optional link back to finding 1's hook: "That's the specialist route:
where I couldn't judge, I handed the judging to someone who answers for it." Buys the reader: the example
shows the rule in action rather than gesturing at it.

### 13. "Relative to other groups" is the comparison the reader needs and the one they don't get (impact 5)

> "Early hiring data shows employment falling 13%, relative to other groups, for 22-to-25-year-olds in the
> jobs most exposed to AI"

"Other groups" is vague, and the comma placement makes the sentence hard to hear. Brief 14 §3.5 gives the
comparison: more experienced workers in the same jobs held steady or grew.

Fix: Target: "Early hiring data shows employment for 22-to-25-year-olds in the jobs most exposed to AI
falling 13%, while older workers in the same jobs held steady or grew." Buys the reader: the number now
says what it means for juniors specifically, which is the section's question.

### 14. Aloud: four citations garble, and three prose-tail parentheses are read mid-sentence (impact 5)

**aloud:** "the rate was 22.4 in every 100 (Budzyń et al. 202500133-5))."
**aloud:** "'may now be an inexperienced one' (Bainbridge 198390046-8))." (twice)
**aloud:** "'...at all grade levels'). In 1986..."

The Budzyń and Bainbridge DOIs contain parentheses, so the builder's link pattern stops early and the
listener hears digit strings; the NCTM URL's "(1980s)" leaves a stray ")". Separately, the parentheses
"(Leyden & Scur 2026; a working paper, not yet reviewed)", "(Wiles et al. 2026; a working paper, and
three of its four authors work at BCG...)" and "(Shen & Tamkin 2026; small groups, and not proof of
cause)" are kept and read aloud mid-sentence. The Wiles one is 20 words.

Fix: encode the parentheses in those three URLs (`%28` / `%29`). For the prose tails, either accept them
being read (they are caveats the listener should hear) or move each into its sentence: "...two economists
recently proposed, in a working paper not yet reviewed, 'that...'". Same builder limitation as essay 07
finding 17.

### 15. Step 3's "it" and step 6 overlap (impact 4; the reader acts on these)

> "3. **Keep practicing what you need in order to judge it,** even where the AI is better at it than you."
> "6. **Check on purpose, not by feel.** Every so often, do a piece of the work yourself and see how it goes."

"Judge it": the nearest noun is step 2's "the answer", and "better at it" adds a second "it". Step 6 then
says "do a piece of the work yourself", which is also what step 3 means by practicing; the reader can't
tell the difference. The difference is real: step 3 keeps the skill, step 6 *tests* whether you still have
it.

Fix: step 3, "what you need in order to judge the work". Step 6, lead with the test: "**Test yourself now
and then, not by feel.** Every so often, do a piece of the work without the AI and see how it goes: that's
how you find out whether step 3 is working." Buys the reader: six steps that are six different things.

### 16. "The skill collapses": which skill? (impact 4)

> "As the tools improve, fewer tasks seem worth checking, and in their words, 'the skill collapses'"

The paper's skill is verification (brief 14b §4.1); the reader may read "the skill" as the work skill.
Fix: "...fewer tasks seem worth checking, so the checking skill withers. In their words, 'the skill
collapses'."

### 17. "Goes with leading it well" says a little more than the outcome measured (impact 4; honest claim)

> "they show that having done the work goes with leading it well, not that keeping it sharp does"

Artz et al. measured workers' job satisfaction, with competence rated by the worker (brief 14b §2.1);
Formula One measured team results. "Leading it well" stretches the first. Fix: "...having done the work
goes with happier workers and better team results, not that keeping it sharp does." The sentence's real
job (the second half) is untouched.

### 18. Two small garden paths in the opening (impact 4)

> "'AI is making us stupid' is a worry I hear often, and one I've asked about myself."

"Asked about myself" first reads as "asked about me". Fix: "one I've wondered about myself."

> "Work that used to need a skill in us becomes a tool we use and manage."

Work becoming a tool is a mixed image. Fix: "Work that used to need our own skill becomes work we hand to a
tool and manage."

### 19. Small fixes (impact 3)

- Calculators: "That same year, two researchers pulled together 79 studies. Calculators used alongside..."
  The finding lacks its subject and reads as a general fact. Add "They found that calculators...".
- Gajos & Mamykina: "they learned" (learned what?). Brief 14 §6.3: nutrition choices with a simulated AI.
  "In a study of nutrition choices, when people were shown...".
- The FAA sentence is 43 words; split after "errors": "In 2013, the US Federal Aviation Administration
  found an increase in manual handling errors. It urged airlines...".
- Position: "As AI agents take on whole jobs" uses "agents" before the essay says what it means here; a
  bare "As AI takes on whole jobs" loses nothing, and line 28 introduces the word properly.

---

## Whole-artifact pass (read last, cold, start to finish, as the reader)

1. **Kinds of number the reader must hold: four, where two would do.** Relative change in percent (48%,
   17%, 24% / 20% / 19%, 13%); a quiz score (50% vs 67%, which reads fine as "half against two in three");
   a rate per 100 with decimals (28.4 / 22.4); and percentage points (19). Plus many plain counts (79, 53,
   86 studies; 16 pilots; 1,261 managers), which need no re-orientation. The reader acts on none of these
   numbers; each is a reason to believe. So put every rate on "in every 100" in whole numbers (finding 8),
   and say every relative change in words beside its figure (findings 5, 9). That leaves two scales, both
   familiar.
2. **Off-page sends:** "the kind of AI the last essay called an agent" (restated, fine); "as essay 06
   showed, an AI sounds just as sure when it's wrong" (restated, fine); "the subject of the next essay"
   (forward pointer, fine); "the coding study I mentioned", "the math study" (on-page, fine). The one that
   stalls is internal: the specialists set-up whose pay-off is far away (finding 1), and the tutor's
   second version (finding 9).
3. **Research terms near-meaningless to this reader:** observational (finding 11), percentage points
   (finding 8), field experiment and randomized trial (both clear enough from context), replicate ("failed
   to replicate" is explained by "didn't hold up" just before; fine), working paper (glossed as "not yet
   reviewed"; fine).

The spine is easy to follow, and the management frame carries the essay: the move, two places the cost
lands, two traps, where the comparison breaks, what to do. Paragraphs open from where the last ended. The
best lines should be protected from any trim: "Reading an AI's answer is the rereading. Working it out is
the test."; "You don't get worse at everything. You get worse at the parts you've stopped doing."; "The
common thread: the person still produces something first."; "It's slower and it's less pleasant. That's
the point."; and the "done when it hadn't happened" moment. What the reader can't yet do is pass through
two turns without stalling (findings 1, 6) or take the caution about "AI employees" home as something to do
(finding 2).

## Register (brief §3)

Body (title to "Where I land", via `speakable()`): 281 sentences, about 3,930 words.

- **Under eight words:** 64 of 281, 23%. Below 30%, but flow outranks the ratio and the flow is good. The
  short sentences land deliberately. Don't chop to reach 30%.
- **30 words or more:** 16. The longest: FAA (43, finding 19), Leyden & Scur (36), Wiles (36, finding 2),
  Artz (35), the "as it starts carrying out whole jobs" sentence (34). The Wiles fix splits one.
- **Explainer connectives:** "In other words" (1), "So" opening a consequence (6), "because" (6), "That's
  the same pattern / That's the closest older case / That's a prediction..." as gloss lines. Target met.
- **Demeaning / self-deprecating:** none found. The Kosmyna line ("the weakest evidence in this essay and
  the most widely quoted") judges the evidence, not the researchers, and the essay quotes the authors' own
  caution first; fair. The vendor notes (Anthropic, Microsoft, BCG) are stated plainly, without sneer.
- **Spelling and commas:** "cancelled" is British (finding 7 removes it). Serial commas present in every
  list I checked. No AI-tells from the voice profile found; the fragments ("That's the point.") are his.

## Verdicts on my flags

**Flag 4, "Where the comparison needs care": honest and clear, and it does not undercut the title, with
one gap.** The team-keeps-the-skill and team-pushes-back paragraphs are among the clearest in the essay.
The Wiles paragraph needs its labels introduced first and a positive image after the "don't" (finding 2);
the Köbis quote needs "human agents" glossed (finding 10). The specialists pay-off works, if it is planted
earlier (finding 1).

**Flag 6, numbers: usable after fixes.** 50 vs 67 and the counts are usable as written. 28.4 / 22.4 and
"19 percentage points" should move to whole numbers "in every 100" (finding 8); 24% / 20% / 19% should be
on one scale, time, as the source counts it (finding 5); 48% / 17% need words beside them (finding 9); 13%
needs its comparison (finding 13).

**Flag 8, the title: keep it.** Both halves are short and plain, and "Choose the skills you keep" matches
the rule's wording in the position and the landing, so the reader carries one rule with one name. One
mild ambiguity: "Choose the skills you keep" can be heard as "pick among the skills you already have".
"Choose which skills to keep" removes it, at no cost; the drafter's call.

**Flag 3 (asked of others; my read only): it supports the frame once planted.** The specialists are a
third kind of leaning (not tool, not team), and the pay-off (they answer for their work; AI doesn't yet)
is one of the essay's sharpest points. Its problem is distance and the ambiguous "same pattern", not
direction (finding 1).

---

**Verdict: ready after fixes.** The argument is clear, the frame carries, and the steps are usable.
Findings 1-7 are the ones a reader would stall on or misread; finding 3 is an accuracy fix about how far
the essay's own evidence was checked.
