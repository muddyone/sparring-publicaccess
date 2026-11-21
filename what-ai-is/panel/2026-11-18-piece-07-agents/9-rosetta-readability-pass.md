# Rosetta: readability pass on essay 07 (after the Tyson rewrite, f0786a81)

_Reviewer: Rosetta (plain language). Read cold, in one sitting, from the title to the end of "Where I land",
as an everyday AI user. File: `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md` at f0786a81.
Read beforehand: my persona and the project context. I did not read the other
panel reports or my memory file for this pass. Line numbers are the draft's._

The cap limits packaging, never the message. Cut only what shouldn't be said at any length; if it needs
more room, add a numbered part. None of the rewrites below drop a claim or a caveat. Each one is a draft
for Julian.

## Overall

The rewrite is a big step up. Most sections now read easily. Sentences are short, terms are explained
before they're used, and nearly every number is "N in every 100". **The position paragraph is still the
jumpiest passage in the essay.** The problem is the order, not the words. It goes smart, then touch, then
smart, then looking, then smart, then touch. The reader gets the three settings before the reason to care
about them. In the body, the remaining trouble is a handful of overloaded sentences, two numbers that
don't say what they count, and one name the reader never sees before it's referred back to.

## Findings, ranked

### 1. Position paragraph: the order zigzags (lines 14–22). Impact 9

> That worry isn't wrong, but it watches the one thing you can't control. What sets the limit on the harm
> an agent can do is what you've let it touch … How smart it is decides … How far it goes before a person
> looks decides … And being smarter doesn't make an agent safe. Anything it reads can carry instructions …
> You can't decide how smart the next model will be. You can decide what it's allowed to touch.

**What's wrong.** There are four problems.
- (a) "It watches the one thing you can't control" is a metaphor, and the "one thing" isn't named until
  five sentences later. The reader has to hold an unnamed thing.
- (b) The paragraph jumps from "can't control" to "what sets the limit" without the bridge "here's what you
  *can* control".
- (c) The third setting, how far it goes before a person looks, appears with no signal that a new item is
  starting.
- (d) "And being smarter doesn't make an agent safe" goes back to intelligence after the paragraph has left
  it. That's the zigzag Bart felt.

"Anything it reads can carry instructions" is also abstract here. The concrete version, an email with a
planted line, doesn't arrive until line 127. Also, "My position:" is followed straight away by a definition,
so the opening has two colons in one sentence.

**Rewrite.** This gives one direction of travel: the worry, what's right in it, what's wrong in it, what you
control, and the ask. Every claim and both caveats ("isn't wrong", "so far … reliably") are kept.

> **My position. When I say "agent", I mean an AI you've let act for you: send the email, pay the bill,
> change the code. The worry I hear most is that agents keep getting smarter, and the smarter they get, the
> more dangerous they become. That worry isn't wrong. A smarter agent gets more done, the good and the bad.
> But being smarter doesn't make an agent safe. Anything it reads, an email or a web page, can carry
> instructions someone planted, and so far smarter agents haven't been reliably harder to trick. And how
> smart the next model will be isn't up to you. What's up to you is what it's allowed to touch: your inbox,
> your files, your accounts. That sets the limit on the harm it can do. How smart it is decides how much it
> gets done inside that limit. One more thing is yours to set: how far it goes before a person looks. That
> decides how much goes wrong before anyone can stop it. So before you hand an AI a job, ask what it can
> touch, not how smart it is.**

(It's about the same length. If Julian wants to keep the "watches" image, it has to name the thing in the
same sentence: "it watches how smart the agent is, the one thing you can't control.")

### 2. Section 2's closing paragraph: four ideas in one breath (lines 111–118). Impact 7

> So agency comes in degrees, and that's why this essay treats how far an agent goes on its own as a
> setting in its own right. A chat assistant with no tools is the mirror image of that script … The split
> itself is old.

**What's wrong.** The paragraph goes from degrees, to a forward reference ("a setting in its own right" is
a setting the reader hasn't met yet), to the mirror image, to 1995. "Mirror image" makes the reader hold
both senses and the script at once. "The split" has no clear referent: is it the split between the two
senses, or between workflow and agent? It's the two senses, but the sentence before it is about the
mirror image.

**Rewrite.**
> So the working definitions agree on one thing, acting for someone, and none of them makes intelligence
> the test. Where they differ is how much the thing decides for itself. Take a script that books your
> flights. It acts for you. But on Anthropic's line it's a workflow, because its steps were fixed in
> advance. So agency comes in degrees. That's why, later on, I treat how far an agent goes on its own as a
> setting you choose.
>
> A chat assistant with no tools is the opposite case. It's an agent in the philosopher's sense, but not in
> the working sense. That split between the two senses is old. In 1995, two computer scientists separated a
> "weak" notion of agency, acting on its own, from a "strong" one involving beliefs and intentions (…).

### 3. The task-length number doesn't say what it counts (lines 219–221). Impact 7

> One study measured the length of software task a leading model could finish about half the time. For
> models such as Claude 3.7 Sonnet, it was around 50 minutes …

**What's wrong.** It says 50 minutes but not whose minutes. The study measures how long the task takes a
skilled person, not how long the model runs. A reader will picture the AI working for 50 minutes. That's an
unlabelled number and a small loss of precision. "The length of software task a leading model could finish
about half the time" is also hard to parse.

**Rewrite.** Ines should confirm the "skilled person" wording against Kwa et al.
> And what agents can do on their own keeps growing. One study timed software tasks by how long they take
> a skilled person. Then it asked: how long a task can a leading model finish about half the time? For
> models such as Claude 3.7 Sonnet, the answer was around 50 minutes of a person's work when the study was
> published in 2025. That length has doubled about every seven months since 2019 (…).

### 4. "Kolt, the legal scholar quoted earlier" points back to a name the reader never saw (lines 102–104 and 294). Impact 6

> Its standard definition, from the Restatement of Agency as a legal scholar quotes it, is that …
> …
> Kolt, the legal scholar quoted earlier, argued that …

**What's wrong.** In the prose, the first mention is just "a legal scholar". "Kolt" appears only in the
link text. So "Kolt, the legal scholar quoted earlier" sends the reader back to find someone who was never
named. The first sentence is also a nested attribution: definition, source, quoter. And the gloss of
"principal" comes after the quote, when the reader needed it inside it.

**Rewrite** (line 102). Check Kolt's first name against the source before it ships.
> The law has said much the same for a long time. The standard legal definition comes from a reference
> work called the Restatement of Agency. As the legal scholar Noam Kolt quotes it, an agent acts "on the
> principal's behalf and subject to the principal's control", the principal being the person the agent
> works for (…).

Line 294 then works as written.

### 5. "All three parts of Willison's test" asks for recall from 140 lines back (lines 288–289). Impact 6

> So earned trust can widen what an agent does, but it should never hand the agent all three parts of
> Willison's test.

**What's wrong.** The three parts were listed at line 142. By now the reader holds the name and not the
contents. (The same phrase in step 6 is fine, because step 2 sits right above it.)

**Rewrite.**
> So earned trust can widen what an agent does, but it should never hand the agent all three parts of
> Willison's test at once: your private data, things anyone could have written, and a way to send things
> out.

### 6. Weaker models: a sentence broken in the middle (lines 202–203). Impact 6

> In the first benchmark, the weaker models were hijacked less often mostly, the authors suggest, because
> they often failed at the work, the attacker's and yours alike.

**What's wrong.** "Less often mostly, the authors suggest, because" splits the sentence at its hinge. The
reader has to reassemble it.

**Rewrite.**
> In the first benchmark, the weaker models were hijacked less often. The main reason, the authors
> suggest, is that they often failed at the work, the attacker's and yours alike.

### 7. The survey sentence holds too much (lines 70–72). Impact 6

> A survey of ways to improve an AI without retraining it, such as better tools and setups, estimated that
> most of them were worth as much as training the model with more than five times the computing power.

**What's wrong.** It's one sentence carrying the survey, the examples, "most of them" and a comparison. And
"five times the computing power" doesn't say five times what.

**Rewrite.**
> That isn't a one-off. One survey looked at ways to improve an AI without retraining it, such as better
> tools and setups. For most of them, it estimated the gain was worth as much as retraining the model with
> more than five times the computing power it was first trained with. Retraining is the expensive part, and
> these gains came without it (…).

(Ines should confirm that "the computing power it was first trained with" matches Davidson et al.'s
"compute-equivalent gain".)

### 8. "A protective layer around a model that controls…": who controls? (lines 170–171). Impact 6

> A research team built a protective layer around a model that controls which information can flow to which
> action.

**What's wrong.** Grammatically, "that controls" attaches to "a model". It's the layer that controls the
flow. "Follows the same logic" is also abstract. Name the logic.

**Rewrite.**
> One defense that works does the same thing: it limits what the agent can do, not how clever the model
> is. A research team wrapped a model in a protective layer. The layer controls which information can flow
> to which action. …

### 9. Essay 03 paragraph: three off-page references, and a quote that jumps sections (lines 90–97). Impact 5

**What's wrong.** "Essay 03", "the series overview", and "essay 03 also" all send the reader off the page,
three times in one paragraph. Then the Chalmers engine quote comes back to the car picture from the
previous section, in a paragraph about word senses. That's a jump.

**Rewrite.** Same content, with the quote moved to where the picture lives.
> Earlier in this series I used both. Essay 03 used the first sense. It argued that there really is
> something on the other end of the conversation: what the philosopher David Chalmers calls a
> quasi-subject, something you can accurately describe as having beliefs and aims. On that view, even a
> chat assistant that can't touch anything counts. (The series overview's phrase, "an agent on the other
> end", meant the same.) But essay 03 also called the systems I work with "several AI agents", and that was
> the working sense. Both uses are fair. They just aren't the same thing.

Then add to the end of line 45, after "who is allowed to drive it where": *Chalmers once put it this way
about an early language model: "Perhaps it is an engine that can be used under the hood to drive many
agents" (…).*

### 10. "Here's why it matters so much" … "the central problem" (lines 126–129). Impact 5

**What's wrong.** "It" has no clear referent. Is it access, or the limit? "The central problem" doesn't say
the central problem *of what*.

**Rewrite.** "Here's why access matters so much." … "Security people call this *prompt injection*, and it
is the central security problem for agents."

### 11. GitHub bullet: a gloss wedged inside a split quote (lines 162–164). Impact 5

> They said the problem was "not a flaw in the GitHub MCP server code itself", meaning the connector
> between the agent and GitHub worked as built, "but rather a fundamental architectural issue".

**Rewrite.**
> The agent reached GitHub through a connector (an "MCP server"). The researchers said the problem was
> "not a flaw in the GitHub MCP server code itself … but rather a fundamental architectural issue": the
> connector worked as built.

(Ines should check that the ellipsis joins one sentence in the source.)

### 12. "Three separate settings", but the capability setting changes its wording (lines 18, 240, 345). Impact 5

The position says capability decides "how much it gets done inside that limit". Line 240 says "how close it
gets to that limit". Line 345 says "how close an agent comes to its limit". A reader may take these as two
different claims. Pick one phrasing and use it in all three places. I'd use "how much it gets done inside
that limit", because it carries the good-and-bad point and "how close" doesn't.

### 13. Blackmail numbers: the second one doesn't say what it counts (line 228). Impact 5

> … chose blackmail in 96 runs out of 100, and models from three other companies did so in about 80.

**Rewrite.** "… did so in about 80 runs out of 100."

### 14. Line 231: "it" for a plural (line 231). Impact 4

> Here, it did so to avoid being replaced or to keep a goal it had been given.

"It" refers back to "a capable AI", which is generic, but the study is about several named models.
**Rewrite:** "Here, the models did so to avoid being replaced or to keep a goal they'd been given."

### 15. Transitions that start from nowhere (lines 206, 271, 137). Impact 4

- Line 206, "Stronger attacks also work far better." The "also" doesn't follow from the paragraph about
  weaker models. **Rewrite:** "How often an attack works also depends on the attack."
- Line 271, "None of this is new." "This" has no clear referent, because the previous section ended on
  checking reports. **Rewrite:** "Handing work to someone you can't fully check isn't new."
- Line 137, "That's why the standard industry checklist…" This reads as if the checklist was written
  *because of* the paragraph before it. **Rewrite:** "The standard industry checklist for these systems
  says the same thing. It lists the root causes of damage as …"

### 16. The 60-word conditional in "What would change my mind" (lines 357–360). Impact 4

The third bullet holds two different triggers ("in real use … or … in realistic tests"), each with its own
conditions, inside one bolded sentence. **Rewrite** as two bullets that share the consequence:
> - **If capable agents were found choosing serious harm in real use, at a measurable rate rather than in
>   single cases, with only the access their job needed,** then which model you hand a job to would matter
>   as much as what it can touch.
> - **The same goes if tests in realistic settings found that, with the same access, more capable agents
>   chose harm more often than less capable ones.**

### 17. Lines 328–333: "when one of them looked, it found…" Impact 4

"One of them" is ambiguous: the fixer, the checker, or a third agent? And "looked" doesn't say looked at
what. **Rewrite:** "But when one of them checked the setup, it found nothing that would have stopped it
putting the fix live."

### 18. Small ones. Impact 2–3

- Line 67: "it solved 18" → "it solved 18 in every 100".
- Line 183: "a benchmark" is unglossed. → "a benchmark, a standard set of test attacks, of these
  planted-instruction attacks".
- Line 197: "about 1 in 30" is the only number not given per 100. → "about 3 in every 100" keeps the
  reader on one scale.
- Line 343: "That it holds as strongly outside coding." → "That the argument holds as strongly outside
  coding."

## Whole-artifact pass (cold, start to finish)

1. **Measurement scales.** The rewrite has mostly solved this. Nearly every rate is "N in every 100". The
   remaining odd ones are "nearly two-thirds more" (keep it, it's the plain reading of 11 to 18), "more than
   five times the computing power" (label it, finding 7), "1 in 30" (switch it, finding 18) and "50 minutes …
   doubled every seven months" (label it, finding 3).
2. **Off-page sends.** Essay 02, essay 03, the series overview, Part one (twice), and the last essay in this
   part. All but the essay 03 cluster can stand alone (finding 9). One send is internal and broken: Kolt
   (finding 4).
3. **Researcher-only terms.** None are left unglossed except "benchmark". "Harness", "prompt injection",
   "MCP server", "workflow", "LLM" and "inference-time compute" are all explained where they appear.

**What language can't fix.** The "What being smarter changes" section asks the reader to hold two studies
that disagree, a third that measures attack strength, and a fourth on choice under pressure. That's built
into the evidence, not the prose. It reads all right now because each study gets its own paragraph and the
section ends on "three separate settings". I wouldn't compress it further.

## Verdict

**The body now reads easily; the position paragraph still zigzags (smart, touch, smart, look, smart,
touch) and needs reordering (finding 1) before it ships; findings 2–8 are worth doing in the same pass.**
