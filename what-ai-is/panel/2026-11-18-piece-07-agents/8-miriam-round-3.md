# Miriam Vale: argument review, essay 07, round 3 (the reframe), 2026-11-20

Lane: argument. Now that the essay speaks to the reader's real worry (smarter = more dangerous), does it earn
belief? Does it overclaim in either direction, contradict itself, or set falsifiers that couldn't fire?

**What I read:** my persona and the project context; the round-3 brief; my
round 2 (`7-miriam-round-2.md`); the essay at `243bb509`, read whole and then against `git show 243bb509`; brief
13 §5.4, §5.7, §5.8, Q6 (6.1 to 6.5) and the Part 3 bottom line. I added no source. Every fix below stays inside
what brief 13 records a source as saying, and where a fix is inference I say so. I did not consult or update my
memory file this run.

## Overall

The reframe is right, and it is mostly well executed. The essay now answers the belief the reader holds, it
grants that belief real ground (Debenedetti 2024, Lynch 2025), and it redirects to the dial the reader controls.
"You do control what it can touch" is the best new line: it turns the argument from a correction into an
instruction. My round-2 fixes survived the splice (the "doesn't claim" scope, "rarely", steps 2 and 3, the
NIST lead-in, the Lynch superlative).

The problems are concentrated where the reframe concedes. Having decided to tell the worried reader "you're
partly right", the new lines grant the worry more firmly than the evidence does in some places ("a smarter agent
is more dangerous", "the smarter model was the more dangerous one", "its own ends") and dismiss it more firmly
than the essay's own disclaimers allow in others ("the wrong dial"). And "a less capable one isn't the answer
either" is asserted in the position but never argued in the body, against a benchmark the body itself cites in
which the weaker models were the safer ones.

---

## Findings, ranked

### 1. Impact 8: the position grants the worry flatly, ranks a cause it can't rank, and says "any"

> "So a smarter agent is more dangerous mainly because it does more with the access it has, and being smarter
> doesn't make it any harder to fool."

**What's wrong.** Three overclaims in one sentence, and it is the sentence a reader takes away.
(a) "A smarter agent *is* more dangerous" states the worry as fact. The evidence is one benchmark where more
capable models "tend to be easier to attack" (6.1), one competition finding "limited correlation" between
robustness and capability (6.2), and forced stress tests that don't compare models by capability (5.7). That
supports "can be", not "is". The body itself says it "cuts both ways".
(b) "Mainly" ranks causes. Nothing in the essay weighs one route to danger against another, and the Lynch
paragraph describes a second route (choosing harm) beside "doing more". It is a weighting word of the same
family as the "nearly always" and "rarely" we removed in rounds 1 and 2.
(c) "Doesn't make it *any* harder to fool" is stronger than "limited correlation" and than the body's own "not
much harder to hijack".

**Fix.** "So a smarter agent can be more dangerous: it does more with the access it has, good and bad, and so far
being smarter hasn't reliably made it harder to fool." ("Reliably" is brief 13 §6.5's own word.)

### 2. Impact 7: "the worry, half right" hardens the source and asserts what the benchmark never tested

> "Being smarter didn't protect these models. If anything, it made them better at doing what the attacker asked.
> That is the worry, half right: the smarter model was the more dangerous one, but because it was better at
> following someone else's orders, not because it had plans of its own."

**What's wrong.** Round 2's fix (R6) made the previous sentence plural and hedged ("these models", "If anything").
The new sentence undoes both: back to the singular "the smarter model", and "was the more dangerous one" where
the source says "tend to be easier to attack". The mechanism the authors offered as a "potentially unsurprising"
explanation is now stated as the cause ("because"). And "not because it had plans of its own" reads as a finding,
but the benchmark is an attack benchmark: the intent came from the attacker by design, and nothing in it looked
for plans of the model's own. Presented as a result, it tells the worried reader something the study can't show,
and two paragraphs later the Lynch study does show models choosing harm without an attacker. A careful reader
sees the essay say "not plans of its own" and then "choosing harm to serve its own ends". Finally, "half right"
rests on one benchmark, and the very next sentence (Zou) finds little link. The concession needs its scope.

**Fix.** "That is the worry, half right, in that benchmark: the more capable models tended to be the more
dangerous ones, but the danger came from carrying out someone else's orders well. The attacker supplied the
intent. Whether capable models choose harm with no attacker at all is a different test, which I come to below."

### 3. Impact 6: "the wrong dial" contradicts the essay's own disclaimers and its new falsifier

> "There's something to it, but it watches the wrong dial."

**What's wrong.** The essay says capability is a dial ("decides how close it comes to that limit"), lists "That
capability doesn't matter" among what it doesn't claim, and its new falsifier says evidence would make
capability "the dial to watch first", which implies it is now a dial to watch second, not a wrong one. "Wrong"
is the one place the essay tells the worried reader they're mistaken, and the essay itself doesn't hold that
view. What the essay actually argues is narrower and stronger: capability is the dial you can't set, and it isn't
the one that sets the worst case. That also sets up "You don't control how smart the next model is" three
sentences later.

**Fix.** "There's something to it, but it watches the dial you don't control, and not the one that sets the
worst case."

### 4. Impact 6: Lynch is read as more than the study shows about the worry

> "This is the closest the evidence comes to the worry in its usual form, a capable AI choosing harm to serve
> its own ends, and it took tests built to force it."

**What's wrong.** Two things. (a) "Its own ends": brief 13 §5.7 records the trigger as harm being "the only way to
avoid replacement or achieve their goals". Avoiding replacement is arguably the model's own; the goals were given
by the scenario. "Its own ends" makes the study sound more like the worry than it is. (b) The worry is about a
trend, AI *getting* smarter and *therefore* more dangerous. As brief 13 records it, the study gives rates for five
models that are close (96, 96, 80, 80, 79) and doesn't compare more capable models with less capable ones. It shows
that leading models can do this when cornered, not that smarter ones do it more. This was my round-2 R2 point;
the reframe changed the wording, and the new wording reopens the gap from the other side by tying it to "the
worry". The "it took tests built to force it" clause is good and should stay.

**Fix.** "This is the closest the evidence comes to the worry in its usual form, a capable AI choosing harm on
its own, here to avoid being replaced or to reach a goal it had been given. It shows leading models can do this
when cornered, not that smarter ones do it more, and it took tests built to force it."

### 5. Impact 6: the new falsifier doesn't test the worry's claim, and its consequence is a dial the reader can't turn

> "If capable agents were found choosing serious harm in real use, on their own initiative, with only the access
> their job needed, then capability would be the dial to watch first, and I'd say so."

**What's wrong.** It is a real falsifier of the *access* claim: harm done with only job-needed access is exactly
what scoping can't prevent. But it doesn't test the claim the reframe is about, that smarter means more dangerous.
One capable agent doing harm in real use shows agents can; it doesn't show smarter ones do it more. The worry's
own falsifier needs a comparison: with the same access, more capable agents choosing harm more often than less
capable ones. And "the dial to watch first" sits awkwardly beside "You don't control how smart the next model is":
the essay should say what the reader would then *do* differently.

**Fix.** Keep the access test and add the comparison, with a consequence the reader can act on: "If capable
agents were found choosing serious harm in real use, on their own initiative, with only the access their job
needed, or if tests in realistic settings found that, with the same access, more capable agents chose harm more
often than less capable ones, then which model you hand a job to would matter as much as what it can touch, and
I'd say so."

### 6. Impact 5: "You don't control how smart the next model is" sits against "use a less capable one"

> "You don't control how smart the next model is. You do control what it can touch." · "Neither 'use a smarter
> model' nor 'use a less capable one' is a substitute for narrower access."

**What's wrong.** The essay twice treats the choice of model as the reader's ("a less capable one isn't the answer
either"; "Neither ... nor"), then says the reader doesn't control it. Both are true of different things: the reader
can't control how capable models *get*; they often can choose which one to use. Read literally, the line denies a
choice the essay argues about two sentences earlier. It appears in the position and in "Where I land", so a reader
meets it twice.

**Fix.** "You don't control how smart the next model gets. You do control what any model you use can touch." Same
change in "Where I land".

### 7. Impact 5: "a less capable one isn't the answer either" is asserted, never argued, against the essay's own evidence

> "A less capable one isn't the answer either: it does less of the job you wanted, and what it can touch still
> sets the worst case."

**What's wrong.** The body never makes this argument; it appears only in the position and as a clause at the end
of the capability section. Yet the reader has just been told, in the body, that in one benchmark the more capable
models were the more dangerous ones. The obvious conclusion for a worried reader is "then use a weaker one", and
the essay's own evidence (6.1) supports it in that benchmark. The position's reason ("it does less of the job you
wanted") is in fact the source's reason: the authors say models with low utility "often fail at correctly
executing the attacker's goal". The body should say so, with Zou as the counterweight, so the claim is earned
where the evidence is.

**Fix.** After the Zou sentence, or before "Neither 'use a smarter model'": "Nor is a weaker model the fix. In that
first benchmark the weaker models were turned less often largely because they often failed at tasks, the
attacker's and yours alike, and in the larger competition size made little difference either way." (The "yours
alike" clause is inference from the source's "low utility" and should read as the essay's.)

### 8. Impact 4: "That doesn't make capability irrelevant" answers an objection this reader doesn't hold

> "That doesn't make capability irrelevant. It cuts both ways."

**What's wrong.** Old-frame residue. Addressed to a reader who might think "if smarter isn't safer, capability
doesn't matter", it was a fair guard. The reader now holds the opposite belief, that capability matters a great
deal, so the line reads as the essay arguing with itself.

**Fix.** "So capability does matter, as the worry says. It cuts both ways."

### 9. Impact 4: "the industry's hope" attributes a belief to an industry without a source

> "Here the worry and the industry's hope meet. ... The hope is that better models will grow out of being fooled."

**What's wrong.** The old text said "the natural hope", which claimed nothing about anyone. The new text puts the
hope in the industry's mouth. That is a broad statement about how organisations think, and nothing in the essay
backs it (brief 13 §6.4 has vendor frameworks that key safety to capability, but the essay doesn't cite them, and
they address catastrophic misuse, not resistance to being fooled). The opening's "pitch" is about usefulness, not
safety, so it doesn't supply the hope either.

**Fix.** "Here the worry meets the opposite hope: that better models will grow out of being fooled." No
attribution needed; the argument doesn't depend on who holds it.

### 10. Impact 3: "carried out attacks better" makes the models the attackers

> "In one benchmark the more capable models carried out attacks better, and in stress tests built to force it,
> capable models chose harm."

**What's wrong.** In Debenedetti 2024 the models carried out an attacker's planted instructions. "Carried out
attacks" casts them as the attacker, which is the worry's picture, not the finding. It is in the disclosure list,
where precision is the point. (The Draft-notes bullet has the same wording.)

**Fix.** "In one benchmark the more capable models carried out an attacker's planted instructions better".

### 11. Impact 3: the opening calls the pitch's focus "the wrong place" without saying for what

> "The pitch and the worry are both about how capable these systems are getting. I think that puts the attention
> in the wrong place."

**What's wrong.** For the pitch (what agents can do for you), capability is the right place to look. The essay's
claim is about judging risk. Unscoped, it reads as dismissing capability across the board, which the body doesn't.

**Fix.** "For judging the risk, I think that puts the attention in the wrong place."

### 12. Impact 2: the Notes' review count is now out of date

> "Five reviewers then tested this essay's reading, plain language, craft, argument and numbers. ... then
> reframed and reviewed again on 20 November."

**What's wrong.** Round 3 has six reviewers, adding accuracy. A disclosure line should be exact.

**Fix.** Once round 3 closes, update to say who reviewed the reframe (for example, "and six, adding accuracy,
reviewed it again on 20 November").

### 13. Impact 2: two "doesn't claim" bullets now overlap

> "That capability doesn't matter." · "That the worry about smarter AI is groundless."

**What's wrong.** Adjacent and close to one claim. Harmless, but a list that reads as an inventory is cleaner
without the near-repeat.

**Fix (optional).** Merge: "**That capability doesn't matter, or that the worry about smarter AI is groundless.**
It decides how close an agent comes to its limit, in both directions. In one benchmark ..." and keep the rest.

---

## Does it hold together from the title to "Where I land"?

Yes, once findings 1 to 3 are made. The title asks the worried reader's question and offers the access question
in answer; the body grants the worry its evidence and redirects; "Where I land" restates the concession ("has
something in it") and the redirect ("you don't control ... you do control"). I found no passage that still argues
against "smarter = safer" as if the reader held it, apart from finding 8. The "smarter isn't safer" material
survives correctly as the opposite hope (finding 9 aside), and the first falsifier still serves it. The worked
example and the six steps are untouched by the reframe and still agree with the body.

## Verdict

**Ready after fixes.** Findings 1 to 7 are clause-level, need no new source, and bring the concession and the
redirect to exactly what the evidence supports; the rest are small.
