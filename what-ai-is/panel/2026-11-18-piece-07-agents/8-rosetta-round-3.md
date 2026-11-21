# Rosetta: plain-language review, essay 07, round 3 (the reframe), 2026-11-20

Reviewer: Rosetta (plain language and structure). The reader throughout: an everyday AI user who has heard
agents are getting smarter, half-fears it, and will act on the six steps and on one rule.

What I read: `brief-round-3-reframe.md`; the draft at `243bb509` start to finish, cold, as that reader (body
only, plus the first Draft-notes bullet); `git show 243bb509`; my own round-1 report (`2-rosetta.md`) so I
don't re-raise settled items; my persona, `project-context.md` and memory. I did not read the other round-3
reports. No new source is proposed. My wording below is a target for Julian, not copy.

The cap limits packaging, never the message. Nothing below cuts a concept. Where a fix adds words, it says
what the reader gets for them.

---

## Findings, ranked

### 1. The title garden-paths: "Worried AI agents" reads first as agents that are worried (impact 8)

> "Worried AI agents are getting too smart? Ask what they can touch."

In a feed, read at speed, "Worried AI agents" parses as a noun phrase: *AI agents who are worried*. The
reader then hits "are getting too smart?" and has to go back and re-read it as "[Are you] worried AI agents
are getting too smart?" A title gets one glance, and this one spends it on a stumble. It also breaks the
series form (two short sentences, the second an instruction: "Ask the AI twice. Believe the disagreement.").
The "Worried X? Do Y." shape reads like an ad.

Fix, in order of preference:

- **"Don't ask how smart an AI agent is. Ask what it can touch."** Series form. It is the rule from step 1,
  word for word, so the title, step 1 and the landing all use one name for it (the round-1 lesson). It speaks
  to the worry without telling the reader the worry is wrong.
- "Worried an AI agent is too smart? Ask what it can touch." If Bart wants to keep naming the worry. Using
  "an ... is" removes the garden path, and the singular matches "it" in the rule.
- Avoid anything like "Fear the access, not the intelligence." That tells a worried reader they are wrong,
  which the essay is careful not to do.

### 2. "Half right", "a different route" and "in its usual form" all lean on a picture of the worry the page hasn't drawn yet (impact 7)

> "...and it gives the worry part of what it fears, by a different route."
> "That is the worry, half right: ... not because it had plans of its own."
> "This is the closest the evidence comes to the worry in its usual form, a capable AI choosing harm to serve its own ends..."

Up to the section "What being smarter changes", the worry is only ever "smarter means more dangerous". The
part that makes "half right" mean something, *an AI with plans of its own*, appears only as a "not" clause in
the middle of the Debenedetti paragraph. It gets spelled out in full three paragraphs later, at Lynch. So
"by a different route" points at a route the reader hasn't been shown. "Half right" cuts the worry in two
before the reader knows which half is theirs.

Fix: name the usual form once, early, where the worry is first stated (opening paragraph), as Bart's
experience of what he hears:

> "The worry I hear most often runs the other way: these systems keep getting smarter, and something
> smarter is more dangerous, because one day it might want things we don't."

(Or "...might start acting on aims of its own"; the wording is Julian's.) Then "a different route", "half
right" and "its usual form" all have an antecedent on the page. This adds about a dozen words, and the
reader gets the frame the whole middle section is measured against.

### 3. A splice cut "ask that in advance" off from its antecedent (impact 6)

> "It's what we let it do, and who was looking. The worry that it's getting too smart has something in it: a
> smarter model will do more of whatever it's allowed to do, good and bad. But you don't control how smart
> the next model is. You do control what it can touch. Before you hand one a job, ask that in advance: what
> can it touch, not how smart is it."

Before the reframe, "ask that" pointed back at "what we let it do, and who was looking", in the sentence
just before it. Three new sentences now sit between them. "That" has nothing behind it and only works by
pointing forward to the colon. "One" now follows "the next model", not "an agent". And "touch" lands three
times in two sentences, which reads as a stutter rather than an echo.

Fix: let the new sentences carry the rule, and end the paragraph on the instruction in the same words as
step 1:

> "...You do control what it can touch. So before you hand an agent a job, ask what it can touch, not how
> smart it is. Set the limit the way you'd set it for a person in that job..."

### 4. The position paragraph still rebuts "smarter = safer" without saying whose belief that is (impact 6)

> "So a smarter agent is more dangerous mainly because it does more with the access it has, and being
> smarter doesn't make it any harder to fool."

The worried reader never thought being smarter made an agent harder to fool. Unattributed, "doesn't make it
any harder to fool" answers a belief they don't hold, which is exactly what the reframe set out to remove.
The body handles this well by naming it as the industry's hope. The bolded box, which many readers will read
alone, doesn't.

Fix: attribute it in a few words.

> "...because it does more with the access it has. And whatever the industry hopes, being smarter doesn't
> make it any harder to fool."

### 5. "The industry's hope" arrives with a definite article and no introduction, and it's easy to confuse with "the pitch" (impact 6)

> "Here the worry and the industry's hope meet. The worry is that a smarter agent is more dangerous. The hope
> is that better models will grow out of being fooled. The evidence so far, from test benchmarks, doesn't
> support the hope, and it gives the worry part of what it fears, by a different route."

The opening paragraph set up two things side by side: the industry's *pitch* (agents will do your errands)
and the reader's *worry*. Now "the industry's hope" appears, as if already met. A reader will reasonably take
it to be the pitch, and it isn't. "Meet" is vague, since these are two opposite predictions. And in "it gives
the worry part of what it fears" the two "it"s point at different things (the evidence, then the worry), with
a worry doing the fearing.

Fix: introduce the hope as new, say they are opposite, and give each "it" one job.

> "The worry says a smarter agent is more dangerous. Some in the industry hope the opposite: that better
> models will grow out of being fooled. The test results so far don't support that hope. They do give the
> worry part of what it expects, by a different route than it imagines."

(If Finding 2's fix goes in, "than it imagines" has a referent.)

### 6. Zou is placed after "half right", so it reads as being about the worry, but it answers the hope (impact 5)

> "That is the worry, half right: the smarter model was the more dangerous one, but because it was better at
> following someone else's orders, not because it had plans of its own. A large public competition ... found
> that bigger or more capable models ... were not much harder to hijack..."

The paragraph runs: hope fails (Debenedetti), worry half right, hope fails again (Zou). With no signal of the
switch back, a worried reader reads "not much harder to hijack" as being about danger. It's a weaker point
than the one they just heard, so it seems to walk "half right" back.

Fix: put both hope findings together, then give the worry its line as the paragraph's close. Debenedetti
finding, then Zou, then: "Being smarter didn't protect these models. In the first study it did the opposite,
and that is the worry, half right: ..." (The 60,000 / 1-in-30 sentence goes with Zou, before the close.) This
only moves words.

### 7. The position paragraph puts the definition of "agent" between "the wrong dial" and the right one (impact 5)

> "There's something to it, but it watches the wrong dial. By 'agent' I mean an AI you've let act for you.
> That's a role you give it, not a measure of how clever it is, and the same AI model, set up differently,
> is a different worker. What it's allowed to touch sets the limit..."

The reader is told the worry watches the wrong dial, then has to hold that for two sentences of definition
before learning what the right dial is. "It" also changes referent three times in four sentences: the worry,
then an AI, then the agent. Fix:

- Make the first one a noun: "There's something to that worry, but it's watching the wrong dial."
- Move the definition ahead of the worry, or after the three dials. The cleanest order: worry, then
  "something to it, wrong dial", then the three dials, then "That's because an agent is a role you give an
  AI, not a measure of how clever it is: the same model, set up differently, is a different worker." Then
  the "smarter" and "less capable" sentences, then the rule.

Same content, and the payoff follows the setup without a break.

### 8. "A less capable one isn't the answer either" has its reason in the box, but not where the body says it (impact 5)

> "Neither 'use a smarter model' nor 'use a less capable one' is a substitute for narrower access."

The body has just shown the reader that weaker models *failed to carry out* attacks (Debenedetti 2024). A
reader who is paying attention will think "then a less capable one is safer". At this line the body offers
no reason why not. The reason sits only in the bolded position paragraph, a page earlier ("it does less of
the job you wanted, and what it can touch still sets the worst case"). Fix: carry the reason to the line
where it's needed.

> "Neither 'use a smarter model' nor 'use a less capable one' is a substitute for narrower access. A less
> capable one does less of the job you wanted, and its access still sets the worst case."

### 9. "That third setting" now counts intelligence as a setting, a page after "you don't control how smart it is" (impact 4)

> "That third setting is separate from both access and intelligence: how many steps the agent takes before a
> person looks."

"Third" makes access and intelligence settings one and two. The reframe's strongest new line is that you
*don't* set intelligence ("You don't control how smart the next model is"). The dial metaphor also splits
here: the box has "dial", the body has "setting", and "the dial to watch" (capability) differs from "the
dial you can set" (access). Fix: "The third of these is separate from both, and like access, it's yours to
set: how many steps the agent takes before a person looks." Use "dial" for all three and "set" only for the
two you control.

### 10. One "doesn't claim" bullet is a triple negative, and it points the old way (impact 4)

> "**That smarter models make no fewer plain mistakes.**"

"Doesn't claim that ... make no fewer" is three negatives, and it takes two passes to parse. Fix: "**That
smarter models make just as many plain mistakes.**" Same claim, one negative.

### 11. The first "would change my mind" bullet uses the hope as its premise but doesn't name it as the hope (impact 3)

> "**If more capable models turned out to be reliably harder to manipulate,** then capability would start to
> stand in for narrower access..."

Fine as logic. For a worried reader, though, it's a surprising premise to see unlabeled. Fix: "**If the
industry's hope came true, and more capable models turned out to be reliably harder to manipulate,** ..."

### 12. The bolded box and the opening both open on "the worry I hear most" (impact 3)

> Position: "the worry I hear most about AI agents is that they're getting too smart"
> Opening: "The worry I hear most often runs the other way: these systems keep getting smarter"

Two sentences apart, near-verbatim. A reader who reads the box, then the opening, gets an echo that reads as
a seam. Fix: the opening can point back instead of restating: "The worry runs the other way: ..." It's
already been owned as Bart's experience in the box.

### 13. The Notes undercount the reviewers (impact 2)

> "Five reviewers then tested this essay's reading, plain language, craft, argument and numbers."

This round ran six, including an accuracy reader. If the line will say "reframed and reviewed again on 20
November", the count should match whatever actually ran. It's a small honesty point, but it's on a line about
honesty.

---

## Whole-artifact pass (cold, one sitting)

- **Does the reframe read through from title to "Where I land"?** Mostly, yes. The arc (worry, granted in
  part, the dial you control) is clear and well paced by the end. The two weak points are the middle section's
  dependence on a version of the worry the page hasn't stated yet (Finding 2) and the box's one unattributed
  rebuttal (Finding 4). With those fixed, the essay speaks to the reader's real belief throughout.
- **Measurement scales.** The reframe adds none. The per-100 convention from round 1 holds.
- **Off-page sends.** The reframe adds none. "Essay 02/03" and "Part one" are unchanged and were handled in
  round 1.
- **Researcher-only terms.** None new. "Dial" is the only new image, and Finding 9 covers it.
- **What reads well and should stay:** "the smarter model was the more dangerous one, but because it was
  better at following someone else's orders, not because it had plans of its own". It's the best new sentence
  in the piece, plain and exact. "You don't control how smart the next model is. You do control what it can
  touch." gives the reader the reason to act, not just the instruction.

## Verdict

Ready after fixes: Findings 1 through 5 at minimum (the title, the unstated "usual form", the "ask that"
splice, and the two places that still argue the old way). None needs another full round.
