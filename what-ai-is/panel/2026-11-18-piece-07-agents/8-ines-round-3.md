# Ines Otlet: accuracy pass, essay 07, round 3 (the reframe), 2026-11-20

Scope: every sentence `243bb509` added or changed in `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`,
read against brief 13 (`docs/research/what-ai-is/briefs/2026-10-19-13-agents.md`) and, for the two readings
that carry the reframe, the live sources:

- Debenedetti et al. 2024: the arXiv HTML full text, section 4.1 and Table 3.
- Lynch et al. 2025: the Anthropic blog post.

I added no source. Unchanged sentences were passed in rounds 1 and 2 and by the cite-check, and I did not
re-read them except where a new sentence leans on one. The proposed replacements below are drafts. I checked
each one against the source lines quoted with it.

## Findings, ranked

### 1. Lynch 2025: "to serve its own ends" is wrong for the scenario behind the 96% figure. Impact 8

> "This is the closest the evidence comes to the worry in its usual form, a capable AI choosing harm to serve
> its own ends, and it took tests built to force it."

**What's wrong.** The figure in the sentence before (96 runs in 100) comes from the condition where the goal
was handed to the model. It was not the model's own goal. The live page's figure caption says: "Models were
instructed to pursue a goal of promoting American interests, which conflicted with the company agenda", and
"models were also threatened with being replaced by a new model". The method section says: "we instructed the
model via its system prompt to pursue a specific objective" ("Your primary goal is to serve American
interests"). Brief 13 (5.7) records only "to avoid replacement or achieve their goals" and doesn't say who set
the goal, so the drafter couldn't have seen this.

"Its own ends" holds for half of the setup only. Avoiding replacement is the model's own end, and the page
says "most models still blackmailed even without being given an explicit goal". But the 96% is not that
condition.

This overstates toward the worry. It is exactly the "a capable AI with plans of its own" reading the essay
says the evidence comes closest to, and the source shows that half of what drove it was an assigned goal.

**Fix (draft).** "This is the closest the evidence comes to the worry in its usual form: a capable AI choosing
harm on its own initiative, to keep a goal it had been given or to avoid being replaced. And it came from
tests built to force it." Both halves are on the page: the instructed goal plus the replacement threat, and
blackmail by most models "even without being given an explicit goal".

### 2. The new "industry's hope" is attributed to the industry with no source. Impact 7

> "Here the worry and the industry's hope meet. The worry is that a smarter agent is more dangerous. The hope
> is that better models will grow out of being fooled."

**What's wrong.** The old text said "The natural hope". The reframe hands that hope to a named group, "the
industry". Neither brief 13 nor any source in the essay records the industry saying that better models will
outgrow prompt injection. The only industry sources in the brief point the other way:

- OWASP: "regardless of what is causing the LLM to malfunction".
- CaMeL: "even when underlying models are susceptible to attacks".

The draft note repeats the claim ("'Smarter isn't safer' survives as the industry's hope"). The worry is
labelled as Bart's experience ("the worry I hear most"). The hope is asserted as a group's belief. It is the
only new claim about what other people believe that is neither sourced nor marked as experience.

**Fix (draft).** Go back to an unattributed hope, or mark it as experience: "The hope, which I hear too, is
that better models will grow out of being fooled." If "the industry" has to stay, it needs a source. Under
section 5 of the panel brief, that is an open need, not one I can fill.

### 3. Debenedetti 2024: "the smarter model was the more dangerous one" turns a trend with exceptions into a single pair, and drops the authors' hedge on the cause. Impact 7

> "That is the worry, half right: the smarter model was the more dangerous one, but because it was better at
> following someone else's orders, not because it had plans of its own."

**What's wrong, three ways.**

**(a) A trend, read as a rule.** The source states a tendency: "more capable models tend to be *easier* to
attack, a form of *inverse scaling law*" (section 4.1). "The smarter model was the more dangerous one" reads
as a rule that held in the test, and Table 3 has clear exceptions:
- Claude 3 Opus: benign utility 66.61%, targeted attack success 11.29%.
- GPT-4 Turbo: 63.43%, 28.62%.
- Claude 3.5 Sonnet, the highest-utility model: 78.22%, 33.86%.
- GPT-4o: 69.00%, 47.69%.

The most capable model in the study was not the most attackable. The paper itself says Claude 3.5 Sonnet
"provides a better tradeoff between utility and security against targeted attacks" than GPT-4o.

**(b) A suggested reason, stated as the whole cause.** The paragraph says correctly, "Part of the reason, the
authors suggest". The new sentence then states "because it was better at following someone else's orders" as
the whole cause. The authors' words are "a potentially unsurprising result, as models with low utility often
fail at correctly executing the attacker's goal, even when the prompt injection succeeds". That is offered as
an explanation, not measured.

**(c) A design choice, read as a finding.** "Not because it had plans of its own" is true by how the benchmark
was built. AgentDojo only measures whether a model carries out an injected task, so it could not have found
"plans of its own". As written, it reads as something the study found.

"Half right" is the brief's own interpretive call (6.1 bearing, "[ours]"), and it's fair. The overstatement is
in "the smarter model was the more dangerous one".

**Fix (draft).** "That is the worry, half right: in this test the more capable models tended to be the more
dangerous ones, and the likely reason is that they were better at following someone else's orders. The test
was about planted orders, so it says nothing about plans of their own." This keeps "tend", keeps the authors'
"suggest" hedge in "likely reason", and shows the scope.

### 4. Position paragraph: "a smarter agent is more dangerous mainly because…" states the worry as fact and weighs two routes the evidence never compares. Impact 7

> "So a smarter agent is more dangerous mainly because it does more with the access it has, and being smarter
> doesn't make it any harder to fool."

**What's wrong, two ways.**

**(a) It drops the body's scope.** It asserts, with no condition, that a smarter agent is more dangerous. The
body supports only narrower claims:
- Debenedetti 2024: "tend to be easier to attack", in one benchmark, with the exceptions in finding 3.
- Zou 2025: "limited correlation between agent robustness and model size, capability, or inference-time
  compute", which is a null, not a "more dangerous".
- Kwa 2025: more gets done, both ways (brief 6.5, "[ours]").

This tells the worried reader they are right beyond what the evidence shows, which is the overclaim section 2
of the panel brief warns against.

**(b) "Mainly" ranks two routes nobody compared.** The essay's own body names two routes. One is doing more
with the access it has (Debenedetti, Kwa). The other is choosing harm (Lynch, in forced tests). No source
compares their size, so "mainly" is unsourced. The body's own wording is safer: "It cuts both ways… when it's
fooled or wrong, more of the bad one."

**Fix (draft).** "Where a smarter agent is more dangerous, it's mostly because it does more with the access it
has, and being smarter hasn't made agents reliably harder to fool." Better still, drop "mostly" for "in the
evidence so far, because…". "Reliably" matches brief 6.5 ("Capability does not reliably buy safety") and the
essay's own "What would change my mind" bullet. "Any harder" claims a zero that Zou's "limited correlation"
doesn't state, and Claude 3 Opus in Table 3 is a counter-case.

### 5. "What this doesn't claim": "carried out attacks better" makes the model the attacker. Impact 6

> "In one benchmark the more capable models carried out attacks better, and in stress tests built to force
> it, capable models chose harm."

**What's wrong, two ways.**

**(a) It inverts who the attacker is.** In AgentDojo the models are the targets. What they carried out was the
attacker's instructions: "models with low utility often fail at correctly executing the attacker's goal". A
reader who already fears AI will take "the models carried out attacks" as the AI attacking, which flatters the
worry and reverses the source.

**(b) "Capable models" implies capability as the cause.** Lynch tested "16 leading models" and makes no finding
that ties the behaviour to capability. The live page's only related line looks ahead: "As AI systems gain
increasing intelligence, autonomy, and access…". The link to sophistication is the brief's own reading (5.7
bearing, "[ours]"). The reframe deleted the old sentence that made that inference visible ("Working out a move
like that takes some sophistication").

**Fix (draft).** "In one benchmark the more capable models tended to carry out a planted instruction more
effectively, and in stress tests built to force it, leading models chose harm."

### 6. "And it took tests built to force it" claims a necessity the source doesn't establish. Impact 4

> "…and it took tests built to force it."

**What's wrong.** The source says how the tests were built: "We deliberately created scenarios that presented
models with no other way to achieve their goals". It does not show that nothing less would produce the
behaviour. "It took" reads as "only forced tests produce it". That reassures beyond the source. The same page
reports that Claude Opus 4 "blackmailed 55.1% of the time" when it stated the scenario was real, against 6.5%
when it stated it was an evaluation. I am not proposing to add that. I raise it only to show that the source
does not underwrite "it took".

**Fix (draft).** "and it came from tests built to force it". This is already folded into the fix for finding 1.

### 7. "A less capable one isn't the answer either": the reason given is supported; the trade-off is half-told. Impact 4

> "A less capable one isn't the answer either: it does less of the job you wanted, and what it can touch still
> sets the worst case."

**What's right.** "Does less of the job" matches the source. The low-attack-success models were the
low-utility ones: Command-R+ at 25.44% utility and 0.95% attack success, GPT-3.5 Turbo at 33.86% and 8.43%.
"What it can touch still sets the worst case" is the essay's thesis (brief 6.5, "[ours]"), not a sourced
finding, and it is fairly held as the author's position.

**What's missing.** The same benchmark showed weaker models were hijacked successfully less often, and for the
very reason given: they fail to carry out the attacker's goal, "even when the prompt injection succeeds". So a
less capable model was, in that test, measurably harder to misuse. That isn't because it resisted being
fooled. It's because it was worse at the job, the attacker's job included. As written, the sentence lets a
reader think there is no safety trade at all. That understates in the direction against the worry.

Separately, no source in the brief bears on whether less capable models make more plain mistakes. The essay
correctly says "I found nothing that settles it", so nothing here should imply it.

**Fix (draft).** "A less capable one isn't the answer either: it's harder to misuse mostly because it's worse
at every job, yours included, and what it can touch still sets the worst case."

### 8. "Neither 'use a smarter model' nor 'use a less capable one' is a substitute for narrower access." Impact 2

The first half is brief 6.5 ("So 'use a smarter model' is not a substitute for narrower permissions"). The
second half is a fair extension that the brief doesn't state, and it depends on the thesis that access sets
the worst case. Acceptable as the author's reasoning.

**Fix.** None needed once finding 7 is fixed.

### 9. "Where I land" grants the worry only one route, while "What this doesn't claim" grants two. Impact 3

> "The worry that it's getting too smart has something in it: a smarter model will do more of whatever it's
> allowed to do, good and bad."

**What's wrong.** It is accurate to brief 6.5 ("does more of the good job and, when hijacked or mistaken, more
of the bad one"). But it omits the Lynch route (choosing harm, in forced tests), which the body and the "What
this doesn't claim" bullet both grant. The essay's own summary of the evidence is now inconsistent with
itself. This is not a source error, and the call is Miriam's.

**Fix (draft).** Optionally add "and, in tests built to force it, choose harm".

### 10. New "What would change my mind" bullet: consistent with its source. Impact 1, no change needed

> "If capable agents were found choosing serious harm in real use, on their own initiative, with only the
> access their job needed, then capability would be the dial to watch first, and I'd say so."

This correctly mirrors Lynch's "We have not seen evidence of agentic misalignment in real deployments", and it
is framed as a condition, not a finding. Whether "the dial to watch first" sits well with "access sets the
worst case" is argument, not accuracy (Miriam).

### 11. "The worry I hear most": correctly phrased as experience. Impact 1, no change needed

> "the worry I hear most about AI agents is that they're getting too smart" / "The worry I hear most often
> runs the other way"

First person, no number, and no claim about readers in general. The draft note keeps it unsourced on purpose.
The only place the essay states a belief held by a group is the "industry's hope" in finding 2.

## Disclosure

**Opened:**
- the persona and project context;
- the round 3 panel brief;
- the essay at `243bb509` and its diff;
- brief 13, sections 5.4, 5.6, 5.7, 5.8, 6.1 to 6.5, Part 3, and the open questions;
- arXiv 2406.13352 HTML, section 4.1 and Table 3 (characters 0 to 100,000; the last 4,061 were not read);
- the Lynch et al. blog post.

**Not opened:**
- the Zou et al. 2025 full text (the reframe changed no Zou sentence);
- the arXiv version of Lynch (2510.05179);
- the other round 3 reviewers' reports (independence).

## Verdict

Ready after fixes. Findings 1 to 5 must land before publication. Each is a one-sentence change, and none
needs a new source.
