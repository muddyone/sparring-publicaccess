# Vera Tukey: numbers review, essay 07 (first panel read), 2026-11-18

Lane: every figure, date and quoted fact in `drafts/2026-11-18-07-agents.md`, checked against brief 13
(`briefs/2026-10-19-13-agents.md`). For the two places where the essay reports the series' own earlier
essays, I also checked the essays themselves: `positions/03-someone-there.md` and `positions/02-it-learns.md`.

**What shaped this, disclosed.** No web. Every outside figure is checked only as far as brief 13's entry
goes, and most of those entries are abstract-level. Marks from the brief, for the sources behind a number:
Yang 2024 [abstract; Tables 1 and 3 read], Davidson 2023 [abstract], Kapoor 2025 [abstract; selected
passages], Zou 2025 [abstract], NIST 2025 [page read], Debenedetti 2025 (CaMeL) [abstract], Debenedetti
2024 (AgentDojo) [full text], Green 2022 [abstract], Kwa 2025 [abstract], Lynch 2025 [abstract; blog
read; Anthropic authors]. I added no source, and every fix below stays inside what the brief records.
Impact is on a 1 to 10 scale.

**The cap limits packaging, never the message.** Several fixes add words. Each one says what it adds.

---

## 1. Every figure and quoted fact

| # | Essay text (quoted) | Brief 13 | Matches? | Labelled on a scale the reader knows? | Fix |
|---|---|---|---|---|---|
| 1 | "it solved 11 out of 100 … 18 out of 100" | 2.2: 11.00% vs 18.00%, GPT-4 Turbo, SWE-bench Lite, shell only vs SWE-agent | yes | **partly**: "out of 100" suggests a set of 100 problems; the model is unnamed | "11 in every 100" (F5) |
| 2 | "an improvement of more than half from the setup alone" | 2.2: "a 64% relative increase" | yes (64% is more than half) | **no**: an everyday reader can hear "solved more than half"; and "more than half" undersells 64 | "7 more in every 100: nearly two-thirds more" (F5) |
| 3 | "most were worth more than a fivefold increase in the computing power spent training the model" | 2.5: "most surveyed enhancements improve benchmark performance by more than a 5x increase in training compute" | figure yes; **"such improvements" narrows the scope** | **no**: the reader has no idea whether 5x training compute is a lot | F4 |
| 4 | "in one large comparison across nine models, which setup worked best depended on which model was in it" | 2.6: 9 models, 9 benchmarks, 21,730 runs; "Claude models perform better with BrowserUse, while OpenAI models achieve higher accuracy with SeeAct" | yes, but the support is one named pair of setups | the count "nine" is fine; the finding it carries is unstated | F11 |
| 5 | "there's no neutral setup in which to measure 'the model itself'" | 2.6 bearing, **[ours]** | ours, presented as a finding | n/a | F11 |
| 6 | "people made 1.8 million attempts to hijack 22 agents" | 5.4: "1.8 million prompt-injection attacks"; "22 frontier AI agents across 44 realistic deployment scenarios" | yes | yes | optional: "about 60,000 of them worked" (F12) |
| 7 | "limited correlation between agent robustness and model size, capability, or inference-time compute" | 6.2, exact | yes | "inference-time compute" unglossed | F12 |
| 8 | "their success rate rose from 11 tries in 100 to 81" | 5.4: "from 11% for the strongest baseline attack to 81% for the strongest new attack", upgraded Claude 3.5 Sonnet, AgentDojo | figure yes | yes as a scale; **wrong job in the argument** | F2 |
| 9 | "completed 77 out of 100 tasks, against 84 with no protection" | 5.8: "77% of tasks with provable security (compared to 84% with an undefended system)" | yes | yes. "7 in 100" would make the cost read on sight | F7 |
| 10 | "It stopped the attacks they tested 'even when underlying models are susceptible'" | 5.8: "securing it even when underlying models are susceptible to attacks"; "provable security" | **no**: "stopped the attacks they tested" is not the brief's wording | n/a | F7 |
| 11 | "more capable models tend to be easier to attack" | 6.1, exact | yes | yes | none |
| 12 | "The reason is uncomfortable: weaker models often fail to carry out the attacker's instructions" | 6.1: "potentially unsurprising result, as models with low utility often fail at correctly executing the attacker's goal"; bottom line: "partly because" | **overstated**: offered by the authors as a likely explanation, not "the reason" | n/a | F6 |
| 13 | "leading models from several companies sometimes chose harmful actions, such as blackmail" | 5.7: 16 models; blackmail in one scenario at 96% (Claude Opus 4, Gemini 2.5 Flash), 80% (GPT-4.1, Grok 3 Beta), 79% (DeepSeek-R1) | **"sometimes" understates** | no figure | F8 |
| 14 | "not seen evidence of agentic misalignment in real deployments" / "caution about deploying … sensitive information" | 5.7, exact | yes | n/a | none |
| 15 | "has been doubling about every seven months" | 2.8: "doubling approximately every seven months since 2019"; 50% horizon ~50 min for Claude 3.7 Sonnet; software tasks; METR's scaffolds | yes | **no**: a doubling with no starting value, no start date, no domain | F10 |
| 16 | "A review of 41 government policies … found that 'people are unable to perform the desired oversight functions'" | 7.5: surveys "41 policies"; "evidence suggests that people are unable to perform the desired oversight functions"; "a false sense of security" | count yes; **quote trimmed in a way that strengthens it** | "41 policies" is labelled | F3 |
| 17 | "July 2025" (database) | 5.6: Fortune, 23 July 2025 | yes | yes | none |
| 18 | "May 2025" (GitHub) | 5.6: 26 May 2025 | yes | yes | none |
| 19 | "1975" (least privilege) | 4.2 | yes | yes | none |
| 20 | "1976" (Jensen & Meckling, in the Sources link) and the "won't always act in your interests" paraphrase | 4.1: that sentence "completed from the standard wording … confirm against the page before quoting" | date yes; **paraphrase rests on the unconfirmed sentence** | n/a | F13 |
| 21 | "back in 1995" (weak vs strong agency) | 3.2 | yes | yes | none |
| 22 | "In essay 03 I said there really is an agent on the other end" | 3.4 says this; **essay 03 itself says "there really is something on the other end"** | **no, against essay 03's text** | n/a | F1 |
| 23 | "In essay 02 I called the model the engine and the system the car" | essay 02 l.33 | yes | n/a | none |
| 24 | "you always send the full conversational history" | 1.1, exact | yes | n/a | none |
| 25 | chat app's standing instructions "at the start of every conversation", not in developer access | 1.2 | yes (paraphrase) | n/a | none |
| 26 | tools add "yet another set of instructions" | 1.3 | yes | n/a | none |
| 27 | "asks before each new kind of action" … "asks about nothing" | 1.4: "Prompts for permission on first use of each tool"; `bypassPermissions` | close; drafter already flagged | n/a | F15 |
| 28 | "only… in isolated environments like containers or VMs" | 1.4, exact (case aside) | yes | n/a | none |
| 29 | "Perhaps it is an engine that can be used under the hood to drive many agents" | 3.4, exact | yes, hedge kept | n/a | none |
| 30 | "systems that independently accomplish tasks on your behalf" | 3.6, exact | yes | n/a | none |
| 31 | "dynamically direct[s] [its] own processes and tool usage" | 3.5: "LLMs dynamically direct their own processes and tool usage" | yes, brackets fair | n/a | none |
| 32 | "on the principal's behalf and subject to the principal's control" (via Kolt) | 3.10, second-hand, labelled | yes | n/a | none |
| 33 | "act as arbitrary code execution" / "control how and if other APIs are called" | 5.1, exact | yes | n/a | none |
| 34 | "excessive functionality; excessive permissions; excessive autonomy" / "regardless of what is causing the LLM to malfunction" | 5.2, exact | yes | n/a | none |
| 35 | Willison's three conditions and "an attacker can easily trick it …" | 5.3, exact | yes | n/a | none |
| 36 | "unacceptable", "should never be possible"; "separating the test database from the real one" | 5.6: CEO as quoted by Fortune; "automatic separation between development and production databases" | yes; "test" for "development" is a fair plain gloss | n/a | none |
| 37 | "coerce" … "into leaking data from private repositories"; "not a flaw in the… server code itself, but rather a fundamental architectural issue"; "granular permission controls" | 5.6, exact (ellipsis drops "GitHub MCP") | yes | n/a | none |
| 38 | "should operate using the least set of privileges necessary to complete the job" / "limits the damage that can result from an accident or error" | 4.2, exact | yes | n/a | none |
| 39 | "does 'not determine'" / "need not be the maximum achievable" | 3.12: "Increasing capabilities unlock new interaction paradigms, but do not determine them" | yes; "unlocks more autonomy" is a paraphrase of "interaction paradigms" | n/a | F14 |
| 40 | "can be treated as a deliberate design decision, separate from its capability" | 3.13, exact (truncated before "and operational environment") | yes | n/a | none |
| 41 | "that make uninterpretable decisions and operate at unprecedented speed and scale" | 4.3, exact | quote yes; **"for exactly these reasons" no** | n/a | F9 |
| 42 | "with models from 2023 to 2025" | Gaps and cautions | yes | yes | none |
| 43 | "for the twentieth time in an hour" | rhetorical, no source, framed as a guess | n/a | fine | none |

---

## 2. Ranked findings

### F1 (Impact 7). Essay 07 misquotes essay 03, and the misquote is what the "Two meanings" section corrects

> "In essay 03 I said there really is an agent on the other end of the conversation."

- **What's wrong.** Essay 03's position says "there really is **something** on the other end" (l.8). The
  word "agent" isn't in that sentence. The error is inherited: brief 13 §3.4 says "Essay 03 uses this to say
  'there really is an agent on the other end'", and the drafter took it from there. Essay 03's own claim is
  that the thing is a *quasi-subject*, something with "quasi-beliefs and quasi-desires" (l.125–126). That
  is the philosopher's sense the essay means, so the substance of the correction stands. But a reader who
  goes back to essay 03 won't find the sentence the correction is correcting. That is unfair to essay 03,
  and it undercuts the series' credibility in the very paragraph about getting words right.
- **A second fact the section misses.** Essay 03 *also* used "agents" in the working sense, in "Where this
  gets harder" ("several AI agents, some running on engines from different companies", l.171–172), and it
  listed "a unified agent" as something models *lack* (l.105, after Chalmers 2023). So essay 03 used the
  word in both senses, which makes "this series itself muddied" truer than the draft shows.
- **Fix.** *"In essay 03 I said there really is something on the other end of the conversation: in
  Chalmers's terms, a quasi-subject, something you can accurately describe as having beliefs and aims. That
  is an agent in the philosopher's sense. The same essay also called my own AI helpers 'agents', meaning
  something else."* Then carry on to the industry sense. Adds about 25 words, and every one of them makes
  the correction checkable. The brief's §3.4 line should get a note too, but that's outside this file.

### F2 (Impact 6). The NIST figure is doing the wrong job in "A smarter model isn't a safer one"

> "And when US government testers built stronger attacks against one leading model, their success rate
> rose from 11 tries in 100 to 81"

- **What's wrong.** The figure is correct (brief 5.4). But it measures **attack strength against one model
  held fixed**, an upgraded Claude 3.5 Sonnet. It says nothing about whether more capable models are more
  or less robust, which is what the section's other two sources are about and what its heading claims.
  Stacked with "And", it reads as a third capability finding. That makes the case look broader than it is
  (two sources on capability, not three), which is part of my flag 4 verdict.
- **What it does show,** and it's a strong point for this reader: a leading model that looked hard to fool
  (11 in 100) was fooled 81 times in 100 once the testers tried harder. A low attack rate measures the
  attack as much as the model.
- **Also.** "One leading model" is vaguer than it needs to be. The essay discloses its Anthropic ties in
  the Notes. Naming the model (the drafter's notes already record it) is more honest than hiding it.
- **Fix.** Give it its own sentence and its own point: *"And a low attack rate isn't a measure of safety.
  When US government testers built stronger attacks against an upgraded Claude 3.5 Sonnet, their success
  rate rose from 11 tries in 100 to 81."* It could sit in this section after the capability findings, or in
  "What it's allowed to touch", next to Greshake. Adds about ten words.

### F3 (Impact 6). Green 2022: the quote is trimmed so it says more than the source, and the policy count is made to carry a finding about people

> "A review of 41 government policies that require people to oversee automated decisions found that
> "people are unable to perform the desired oversight functions""

- **What's wrong.** Brief 7.5 records the abstract as "**evidence suggests that** people are unable to
  perform the desired oversight functions". Dropping "evidence suggests" turns a hedged reading of other
  research into a flat finding. Second, the 41 is a count of *policies*. Reviewing policies can't by
  itself show what *people* can do. That part comes from the evidence Green draws on. "A review of 41
  policies … found that people are unable" puts the policy count behind a claim about people.
- **Fix.** *"Ben Green reviewed 41 government policies that require people to oversee automated decisions.
  He wrote that 'evidence suggests that people are unable to perform the desired oversight functions', and
  that the requirement can give 'a false sense of security'."* Same length, give or take. Keep the next
  sentence ("That was about government systems, not AI agents …") as it is. It's good.

### F4 (Impact 6, flag 3). "more than a fivefold increase in the computing power" is right, but the reader can't use it

> "A survey of such improvements estimated that most were worth more than a fivefold increase in the
> computing power spent training the model"

- **What's wrong for the reader.** Nobody outside the field knows whether five times the training compute
  is a little or a lot, so the number can't do its job, which is to make the harness feel as big as the
  model. Second, the scope. "Such improvements" ties the survey to the setups just described. The brief's
  entry (2.5) says "most surveyed enhancements", and the paper's title is about improving systems "without
  expensive retraining". Only the brief's bottom line glosses this as "scaffolding and tool
  enhancements". "Such" is close, but it's narrower than the source entry.
- **Fix.** The paper's own title is the yardstick, and it's in the brief: *"A survey of ways to improve an
  AI without retraining it, including better setups and tools, estimated that most were worth as much as
  training the model again with more than five times the computing power. Retraining is the expensive
  part. These gains came without it."* Adds about 20 words. Every one of them tells the reader why five
  times matters. Don't add a dollar figure. None is in the brief.

### F5 (Impact 5, flag 3). "11 out of 100 … 18 out of 100 … more than half": correct, but misreadable twice

> "With a plain command line, it solved 11 out of 100. With an interface built for the job, it solved 18
> out of 100, an improvement of more than half from the setup alone"

- **Matches.** 11.00% against 18.00%, GPT-4 Turbo, SWE-bench Lite (2.2). "More than half" is right for a
  64% relative gain. The drafter avoided the paper's misleading 10.7-point figure, as the brief asked.
- **Problem 1.** "Out of 100" reads as if there were 100 problems. These are rates. "11 in every 100" says
  the same thing without suggesting a set of 100.
- **Problem 2.** "An improvement of more than half", right after "18 out of 100", can be heard as "it
  solved more than half". It also undersells: 64% is nearly two-thirds. Give both the gap and the ratio,
  in counts: *"7 more in every 100, or nearly two-thirds more than before."*
- **Optional, for honesty about whose model.** *"the same model (OpenAI's GPT-4 Turbo)"*. The essay names
  Anthropic all through. Naming a non-Anthropic model here shows the harness effect isn't one vendor's.
- **Fix.** *"With a plain command line, it solved 11 problems in every 100. With an interface built for
  the job, it solved 18: seven more in every 100, nearly two-thirds more, from the setup alone."*

### F6 (Impact 5, flag 4). AgentDojo: the authors' likely explanation is presented as "the reason"

> "The reason is uncomfortable: weaker models often fail to carry out the attacker's instructions even
> when they've been fooled, and stronger models carry them out well"

- **What's wrong.** Brief 6.1 quotes the authors (full text read): "This is a potentially unsurprising
  result, as models with low utility often fail at correctly executing the attacker's goal". The brief's
  bottom line says "*partly* because". It's the authors' account, offered tentatively, not a measured
  cause. There's a numbers point under the wording too. If weaker models are "harder to attack" mainly
  because they fail at everything, the inverse-scaling result says **capability doesn't protect you**. It
  doesn't say capability makes a model easier to fool. The essay's position only needs the first, and the
  first is what the evidence carries. "Uncomfortable" against the authors' "unsurprising" is a tone call
  I'll leave to the others, but it pulls in the opposite direction from the source.
- **Fix.** *"Part of the reason, the authors suggest, is that weaker models often fail to carry out the
  attacker's instructions even when they've been fooled, while stronger ones carry them out well. Being
  smarter didn't make the model harder to fool. It made it better at doing what the attacker asked."* Adds
  about 15 words, and it states what the result actually supports.

### F7 (Impact 5). CaMeL: "stopped the attacks they tested" and "made the agent safe" go beyond the brief

> "It stopped the attacks they tested "even when underlying models are susceptible", at a cost … It made
> the agent safe without making the model any harder to fool."

- **What's wrong.** The brief's entry is abstract-level: a layer "securing it even when underlying models
  are susceptible to attacks", "solving 77% of tasks with provable security". "Stopped the attacks they
  tested" is a claim about attack outcomes that the brief doesn't record in those words. "Safe" is broader
  than "secure against prompt injection". The quote is also cut mid-phrase, so "susceptible" hangs without
  "to attacks".
- **Fix.** *"Its authors describe the security as provable, holding 'even when underlying models are
  susceptible to attacks'. The cost: it completed 77 tasks in every 100, against 84 with no protection,
  about 7 in 100 fewer. It made the agent secure against these attacks without making the model any harder
  to fool."* Adds about ten words. "7 in 100 fewer" is the number the reader weighs.

### F8 (Impact 5). Lynch 2025: "sometimes" understates rates the brief records

> "leading models from several companies sometimes chose harmful actions, such as blackmail"

- **What's wrong.** In the scenario the brief records (5.7), blackmail rates were 96 runs in 100 for Claude
  Opus 4 and Gemini 2.5 Flash, 80 for GPT-4.1 and Grok 3 Beta, and 79 for DeepSeek-R1. "Sometimes" softens
  a fact, and the series' register is generous in tone but unsoftened on facts. The contrived setup is
  already disclosed in the same sentence ("deliberately set up to leave no other way out") and in the
  authors' own caveat. That's the right hedge. The rate doesn't need a second one.
- **The disclosure that matters.** These are Anthropic's own tests, and Claude is the top figure. Saying
  so is a point in the essay's favour.
- **Fix.** *"In one such scenario, Anthropic's own Claude Opus 4 and a Google model chose blackmail in 96
  runs out of 100, and models from three other companies in about 80."* Then the authors' caveat, as now.
  Adds about 25 words. Keep "in one such scenario". The rates are from one scenario, not the whole study.

### F9 (Impact 5). Kolt: "for exactly these reasons" claims a match the quote doesn't show

> "A legal scholar who applied agency law to AI agents found its usual remedies strained for exactly these
> reasons: agents "that make uninterpretable decisions and operate at unprecedented speed and scale""

- **What's wrong.** The essay's two differences are (1) any text it reads can redirect it, and (2) machine
  speed, many copies. Kolt's reasons (brief 4.3) are uninterpretable decisions, and speed and scale. Only
  the second matches. "Redirected by text it reads" and "uninterpretable decisions" are different
  problems. "Strained" for the brief's "might not be effective" is fine.
- **Fix.** *"…found its usual remedies strained for the second of these reasons, and for one more: agents
  'that make uninterpretable decisions and operate at unprecedented speed and scale'."* Adding "you can't
  see why it did what it did" as a third difference is the drafter's call. If it goes in, it should be
  credited to Kolt.

### F10 (Impact 4). "doubling about every seven months" has no starting point, so the reader can't picture the growth

> "One measure of the length of task agents can complete has been doubling about every seven months"

- **What's wrong.** A doubling rate with no base gives the reader nothing to hold. The brief has the base
  and the scope: a "50% time horizon of around 50 minutes" for models such as Claude 3.7 Sonnet, doubling
  "since 2019", on software tasks, using METR's own setups (itself a harness result, which suits this
  essay).
- **Fix.** *"On one measure, the length of software task a leading model finishes half the time was around
  50 minutes for models such as Claude 3.7 Sonnet, and it has doubled about every seven months since
  2019."* Don't convert "50 minutes" into how long a person would take, or project it forward. Neither is
  in the brief. Adds about 25 words.

### F11 (Impact 4, flag 3). Kapoor 2025: "nine models" is fine, but the finding it carries is unstated, and "no neutral setup" is ours

> "And there's no neutral setup in which to measure "the model itself": in one large comparison across
> nine models, which setup worked best depended on which model was in it"

- **What's wrong.** The count is right (2.6). What supports "depended on which model" is one passage:
  Claude models did better with one ready-made setup (BrowserUse), OpenAI models with another (SeeAct).
  The reader can't see that. "No neutral setup" is the brief's bearing, marked **[ours]**, and the colon
  presents it as the study's finding.
- **Fix.** *"In one large comparison across nine models, Claude models did better in one ready-made setup
  and OpenAI's in another. So I don't think there's a neutral setup in which to measure 'the model
  itself'."* Inference first-person, the evidence concrete. Don't call the setups "web-browsing" unless the
  cite-check confirms it. The brief only names them.

### F12 (Impact 3). Zou 2025: "limited correlation" becomes "no link" later, and one term is jargon

- "What would change my mind" says the findings "point the other way or show no link". The source says
  "**limited** correlation". *"Show little link"* matches it.
- "inference-time compute" is unglossed for this reader. *"…or how much computing it was given to work out
  each answer"* (plain gloss only, no new claim).
- Optional, and usable: *"about 60,000 of the 1.8 million attempts worked"* (brief 5.4: "over 60,000").
  That's about 1 in 30, a scale the reader gets on sight.

### F13 (Impact 3). Jensen & Meckling: the paraphrase rests on the sentence the brief says is unconfirmed

> "Economists built a whole theory on the fact that someone acting for you won't always act in your
> interests, whoever they are"

- Brief 4.1 says the "will not always act in the best interests" sentence was "completed from the standard
  wording … confirm against the page before quoting". Paraphrasing instead of quoting doesn't remove the
  dependency, and the drafter's note treats it as if it did. "Whoever they are" is ours.
- **Fix.** Either the cite-check confirms p. 308, or rest on the confirmed definition: *"Economists built a
  whole theory of what it costs to hand decision-making authority to someone acting for you."*

### F14 (Impact 2). Morris: "unlocks more autonomy" paraphrases "unlock new interaction paradigms"

Close enough for the argument. But "does 'not determine' it" splices the quote onto a paraphrased subject.
Suggest *"greater capability opens up new ways of working with AI, but does 'not determine' them"*. Minor:
Morris's levels are named by the AI's role (tool, consultant … agent). Operator-to-observer is Feng's. The
brief's bottom line blurs the two as well. "From operator to observer" is fine if it's credited to the
second team.

### F15 (Impact 2). Claude Code mode wording

Agree with the drafter's own note. "Asks before each new kind of action" should become the page's sense,
*"asks the first time it uses each tool"*. The cite-check should settle it.

---

## 3. Verdicts on my §6 flags

### Flag 3. The harness numbers (11 vs 18 out of 100; fivefold; nine models): usable as written?

**Partly. One of the three is usable after a small fix, one isn't usable as written, and one is a count
standing in for a finding.**

- **11 vs 18: usable after F5.** It's the cleanest same-model comparison in the brief, and the right
  figures were chosen. Change "out of 100" to "in every 100", and replace "more than half" with "seven more
  in every 100, nearly two-thirds more". Then a reader gets it on first read.
- **Fivefold: not usable as written (F4).** It's accurate, but it lands on a scale nobody outside the field
  knows. The fix uses the source's own frame (gains without expensive retraining) to make "five times"
  mean something.
- **Nine models: usable as a count, but the finding behind it is missing (F11).** Say what differed
  (Claude models in one setup, OpenAI's in another) and mark "no neutral setup" as the inference it is.

### Flag 4. "A smarter model isn't a safer one": stronger than Debenedetti 2024, Zou 2025 and NIST 2025? Does "ceiling" vs "how much of it it reaches" hold?

**The heading and title hold as "capability doesn't buy safety". The section's support is presented as
broader and more one-directional than it is, in three places. The ceiling framing holds.**

- **What the evidence carries.** There are two capability findings, not three. AgentDojo (one benchmark)
  found more capable models easier to attack, with the authors' tentative explanation that weaker models
  fail to carry out attacks at all. Zou found "limited correlation". NIST is about attack strength against
  one model (F2). Brief 13's own open questions call the direction "unsettled": the two sources disagree
  in direction and agree that capability doesn't reliably protect you. "A smarter AI isn't a safer one"
  claims exactly that much if it's read as "isn't *thereby* safer". It doesn't claim "smarter is less
  safe". I'd keep the title. The section's opening line, "The evidence so far says no", is fair if it's
  scoped: *"The evidence so far, from test benchmarks, says not yet."*
- **Where it overreaches.** "The reason" (F6), NIST counted as a capability finding (F2), and "show no
  link" for "limited correlation" (F12). Fix those three and the section claims what its sources show.
- **Ceiling vs reach.** This holds, and it's honestly framed as the author's synthesis ("So here's how I'd
  put it", brief 6.5 **[ours]**). The ceiling half is close to a logical bound: an agent that can't send
  email can't leak by email (brief 6.5). The reach half has real support. Lynch (F8) shows capable models
  finding harmful routes inside the access they had, and Kwa (F10) shows what a given permission allows
  growing. One caution, not a fix: the incidents and benchmarks show the shape, not rates. The essay
  already says so in "What this doesn't claim", and it should keep saying it.

---

## 4. One line

**Ready after fixes.** Every outside figure and date matches brief 13. The fixes are to the scale the
reader reads them on (F4, F5, F10), quotes trimmed or framed past their source (F3, F6, F7, F9), one
softened rate (F8), one figure in the wrong job (F2), and one misquote of our own essay 03 (F1), which
should be fixed before anything else because a reader can check it in one click.
