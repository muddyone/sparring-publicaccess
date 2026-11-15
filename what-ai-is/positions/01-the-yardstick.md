# The wrong yardstick: judge AI by the role it plays, not the category it belongs to

_What AI Is · Part one: what it is_

---

**My position: a common style of criticism of generative AI uses the wrong yardstick.** It judges
a system that does judgment work by the standards of a calculator. Those standards produce
oddly binary verdicts, ones we would never reach about a person doing the same job. A 2025
Computerworld opinion column, reacting to tests in which models ignored instructions and
cheated, concluded: "GenAI can do a lot of great things, but it cannot be trusted"
([Schuman 2025](https://www.computerworld.com/article/3836728/you-thought-genai-hallucinations-were-bad-things-just-got-so-much-worse.html)).
It is a style I keep seeing; I haven't measured how common it is. The better question isn't "is
it reliable software?" It's "how does it compare with whoever would otherwise fill this role, and
what checks do its real differences call for?"

By "it" I mean what the rest of this series means: an AI assistant such as Claude or ChatGPT, or a
fuller setup in which an AI works on its own, with files and tools. Some studies below concern
other machines, such as forecasting algorithms or self-driving cars; they show how people judge
machines, not how assistants perform.

## The calculator yardstick

We know how to evaluate a calculator. It must be:
- **correct or incorrect,** with nothing in between;
- **perfectly consistent,** the same input always giving the same output;
- **fully trustworthy and explainable** before it counts as safe or valuable.

For a calculator, those demands are right. But apply them to a new intern and they fall apart:
- We don't grade an intern's work as simply correct or incorrect. Much of it is judgment, and we
  know anyone, however expert, can be wrong.
- We don't expect an intern to be perfectly consistent.
- We don't need an intern to be fully explainable before we let them help.

Generative AI increasingly works in the intern's role, drafting, analyzing, advising and deciding
alongside people. Yet it is often judged by the calculator's standards.

## People don't meet the calculator's standards either

The demands made of AI are demands human experts don't meet.

- **Explainability.** Philosophers Zerilli, Knott, Maclaurin and Gavaghan argue that AI is held to
  "an unrealistically high standard" of transparency, partly because we overestimate how
  transparent human decisions are ([Zerilli et al. 2019](https://doi.org/10.1007/s13347-018-0330-6)).
  In medicine, Alex John London points out that opaque decisions are more common than critics
  realize. Where causes are poorly understood, results that can be verified can matter more than
  explanations ([London 2019](https://doi.org/10.1002/hast.973)). The argument has a published
  rebuttal ([Hill 2024](https://doi.org/10.1007/s13347-024-00720-4)), and it deserves an answer;
  it is a live debate, not a settled one.
- **Consistency.** In a study at one insurance company that measured how
  much its experts disagreed, when two underwriters priced the
  same case, their quotes typically differed by 55% of their average, about five times what the
  company's executives expected (Kahneman, Sibony & Sunstein, _Noise_, 2021). That is disagreement
  between people. The same expert also varies from one day to the next, which is the closer match
  to a model giving different answers to the same question. Inconsistency is common in expert
  judgment. We rarely measure it, so we don't see it.
- **Correctness.** Across studies of health and behavior, fixed statistical formulas matched or
  beat expert clinical judgment, and experts were clearly better in only a few
  ([Grove et al. 2000](https://doi.org/10.1037/1040-3590.12.1.19)). Expert judgment is valuable,
  and it is not the gold standard we imagine. Those formulas are fixed and perfectly consistent,
  the opposite of generative AI, so this says nothing about how generative AI compares. It only
  says the human side of the comparison isn't perfect.

## Machines get a harsher verdict

When machines and people make the same mistakes, people forgive the person faster. These studies
show how people judge, not that every harsher judgment is wrong.

- **Same mistake, faster loss of confidence.** In five studies, people lost confidence in a
  forecasting algorithm faster than in a human forecaster after seeing them make the same mistake.
  They abandoned the algorithm even after seeing it outperform the human, which cost them accuracy
  ([Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033)).
- **A higher bar to accept.** In one survey of 499 people in China, self-driving cars had
  to be about four to five times safer than human drivers before respondents would accept them
  ([Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116)). It is a single survey, but the
  pattern is the point: equal performance wasn't good enough.
- **One failure condemns the category.** In two experiments whose methods were fixed in advance, one
  agent's misdeed changed attitudes to its whole group. In the second, when the agent had a name,
  that spillover persisted for AIs but not for humans. The authors call it "a double standard whereby AIs are judged more harshly
  than humans" ([Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040), a study not yet peer-reviewed).

Sometimes a higher bar is warranted. When one model serves millions, its failures arrive together
rather than one desk at a time, and judging one AI by another makes sense when they share a model
or its training data. But where the systems share nothing that caused the failure, the double
standard is the binary error at its clearest. One chatbot's confident mistake becomes "AI can't be
trusted." One person's confident mistake never becomes "people can't be trusted."

## Who uses the wrong yardstick

Not everyone judges AI this way. In six experiments, lay people
actually followed advice *more* when they believed it came from an algorithm. The exception was
experienced forecasters, who relied on it less, and lost accuracy because of it
([Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005)). In another study,
people trusted AI support less than a human expert but more than a human novice
([Rieger et al. 2023](https://doi.org/10.1177/00187208231197347)). They didn't expect perfection.

So my claim isn't about the people in these studies, users and experts deciding whether to take an
AI's advice. It is about a *style of public criticism*: the columns, commentary and academic
critiques that judge AI against a perfect machine rather than against the people who do the same
job. I haven't found a study that measures how often that criticism does this. Someone could count
it.

## Where AI differs, and why different isn't a verdict

AI isn't an intern in every respect, and an honest version of this argument has to say where. But
a difference is not a defect. Judging by role means folding each difference into the system's
record, not using it to disqualify the system.

1. **Its errors are shaped differently.** Human–AI teams do better when the person knows *when*
   the AI is likely to be wrong ([Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285)),
   and AI's abilities are uneven in ways we don't expect from a person. In a study of 758 consultants
   doing real work tasks, AI help sharply raised quality on tasks inside the model's abilities. On a task
   outside them, consultants using AI were 19 percentage points less likely to get it right, a large
   drop (Dell'Acqua et al. 2023, an unpublished Harvard Business School paper). The lesson isn't "don't trust
   it". It is "learn where its abilities end", which is what a good manager learns about any new
   hire. The map is just different.
2. **Scale cuts both ways.** One intern's mistake lands on one desk. A model's mistake can land on
   every desk that uses it. Worse, when several automated decision systems learn from the same data,
   they tend to fail the same people: someone who gets a bad result from one is likely to get it
   from all of them. Whether that also happens when systems share the same core AI model isn't yet
   clear; the evidence so far is mixed ([Bommasani et al. 2022](https://arxiv.org/abs/2211.13972)).
   But the same scale also works in our favor, in two ways. Both are my reasoning, not findings:
   - **Fix it once, for everyone on that version.** Correct an intern's habit and you've fixed one
     intern. Correct a model and everyone using that version gets the fix. Later versions don't
     automatically inherit it: a fix carries forward only if the people and data that train the
     next version carry it ([brief](../briefs/2026-10-17-9-how-models-change.md)), so it has to be
     tested again in each version.
   - **A repeatable error is a testable error.** Human inconsistency goes unseen because almost
     nobody audits it, as _Noise_ shows. Models vary in their wording from run to run but often
     repeat the same kinds of error, and an error a model makes again and again can be found,
     measured and designed against.
3. **It shares some of our failures, which is a point in favor of the human ruler.** People defer.
   Friends hesitate to challenge friends
   ([Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)), and whether people
   speak up depends on whether the team feels safe for it ([Edmondson 1999](https://doi.org/10.2307/2666999)). Models do
   something very similar. Training them to be warmer made them agree more often with users'
   false beliefs ([Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)),
   and users rate flattering, agree-with-you answers higher and want to come back to them
   ([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)). The calculator yardstick has no
   concept for any of this. The human one does, and it suggests a remedy to test: make candor a
   requirement instead of hoping it survives closeness.
4. **Accountability means correctability and a named human.** The designers of a learning system
   can't foresee everything it will do, so the usual ways of assigning responsibility leave a gap
   ([Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1)). Two things narrow that gap,
   though neither closes it:
   - **The system can be corrected.** Whoever runs it can change it when it fails, and a system
     with memory also learns from correction ([see the learning essay](02-it-learns.md)).
   - **A named person answers for its use,** as for any tool used in professional work, provided
     that person has the information and authority to step in.
5. **Respond to what its behavior shows.** The philosopher Daniel Dennett argued that we predict
   complex systems by treating them as agents with aims (Dennett 1987, _The Intentional Stance_).
   The philosopher David Chalmers says a language model has something like desires, which he calls
   quasi-desires: aims it can
   accurately be read as having ([Chalmers 2025](https://philarchive.org/rec/CHAWWT-8), a draft).
   In practice, an apparent aim is worth taking into account when predicting what it will do, as
   we would a colleague's. Whether what works on colleagues works on it is a separate question, to
   be tested. None of this requires claiming
   the system has a stake of its own, which is still an open question
   ([see the essay on whether AI is conscious](03-someone-there.md)).

## Where the yardstick finds a gap: curiosity without a task

A fair yardstick has to be able to say no. Here is where this one does.

Neuroscience has no agreed definition of curiosity. Kidd and Hayden propose studying it through
behavior, as the motivation to seek information
([Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010)). I add one condition of my
own: for a working assistant, it counts if the system seeks information nobody asked it for. The
psychologist Alison Gopnik's group contrasts two ways of learning: finding things out, and passing
on what others know. Children do both; the question is whether models do the first
([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)).

In controlled tests, today's language models mostly fall short.
- **Exploration by default:** in simple choice tasks that reward trying options out, GPT-3.5,
  GPT-4 and Llama 2 explored adequately in only one setup
  ([Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371)).
- **Efficiency:** on a task of working out cause and effect by experiment, leading models neared
  human accuracy but explored less efficiently
  ([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)).
- **My own small study:** Claude, keeping notes while working through a series of puzzles,
  worked out the hidden rule for itself, wrote it down, and then used its few tries the way someone
  who already knew the rule would. It is one small study, and the result came only on my third version of
  the puzzles. And Claude only
  experimented because the puzzles told it to ([details](02-it-learns.md#what-i-tested)).

Here my own experience pushes back on the studies. Working with AI assistants daily, I regularly
see them raise things I didn't ask for, go looking for information nobody told them to find, and
try out possibilities when a problem is unclear. Sometimes it is the most useful thing in the
exchange; occasionally I have to rein it in. By the test above, that counts. Whether it is "real"
curiosity or reasoning toward a goal I set is a question about what it's made of, and this essay's
yardstick says to judge what it does. What I haven't seen is the other half: an assistant that
starts an inquiry with no task in front of it, or keeps wondering about something after the work
is done. Most assistants run only when called, so that is partly how they are built. Starting
inquiries is also not the same as choosing good ones.

That doesn't make the gap permanent. Curiosity can be built, and researchers have been building it
for decades. Reward an agent for being surprised by the results of its own actions, and it will
explore a video-game world with no other goal
([Pathak et al. 2017](https://arxiv.org/abs/1705.05363)). Let GPT-4 choose an agent's next task in
Minecraft, and it keeps setting itself new challenges
([Wang et al. 2023](https://arxiv.org/abs/2305.16291)). These are research agents, not assistants
you can use today; the notes at the end say more. But they show the gap is something engineers can
work on, not a fixed limit.

Judged by role, this gap matters. Part of a good intern's value is the questions nobody asked them
to raise, including the ones they bring back the next morning. An AI assistant that wonders only
while it is working is a weaker colleague in exactly that respect, however accurate it is. The
same test that credits AI systems with memory as learners, in [the learning essay](02-it-learns.md),
finds curiosity in today's assistants inside the task, but not yet outside it. Whether engineered
curiosity closes the gap is an open
question, and the test is the same: does the behavior show up?

## A better yardstick, in five questions

So here is the yardstick I'd use in place of the calculator's:

1. **What role is it filling?** Drafting, advising, deciding, checking.
2. **Compared to what?** The realistic alternative, usually the person who would otherwise do it,
   measured by their actual error rate, inconsistency and opacity, not an idealized one. Compare
   whole workflows, counting the time spent checking it and the errors that slip past the checker.
3. **What is its profile?** Where it fails and how, and also what it brings and what it lacks,
   curiosity included.
4. **Can it be corrected, and who answers for it?** Audit it at the level of the system, and name
   the person accountable for its use.
5. **Then calibrate trust, rather than deciding it.** Rely on it where its record earns that, and
   check it where it doesn't, the way we treat a colleague.

The first question matters more than it looks, because people already judge AI differently
depending on its role. They resist medical AI because they doubt it can account for their
individual circumstances, yet that resistance largely disappears when the AI *supports* a physician
rather than replacing one ([Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013)).
The same system, cast as a helper instead of a replacement, gets a different verdict. The yardstick
only asks that we make that judgment on purpose. The last essay in this series puts all five
questions to the hardest case, [relationships with AI companions](05-relationships.md).

## Comparison, yes. Deception, no.

Skeptics and optimists about AI minds rarely agree, but on this they do: an AI should never deny
being an AI ([see the essay on whether AI is conscious](03-someone-there.md)). That is not a rule
against comparison. Being human-like, and being measured against a human, is legitimate, and it
is often the most useful comparison available. What isn't legitimate is a system passing itself
off as a person. The one exception is a setting where everyone has agreed to the game in advance: a story or game
the person has chosen to enter, or a Turing test, in which a judge tries to tell a machine from a
person.

## What would change my mind

- **A systematic count of public criticism, across a broad sample, showing most of it already
  judges AI against the people who do the same job.** Then the calculator yardstick is my impression, not its practice.
- **Evidence that AI's errors are so unpredictable they can't be profiled.** Then calibrated trust
  isn't possible, and stricter per-answer standards are justified.
- **Assistants that reliably start useful inquiries with no task in front of them,** or come back
  to a question after the work is done, in ordinary use rather than a demonstration. Then the remaining curiosity gap closes, and the essay should
  say so.
- **A strong answer to the opacity argument.** If Hill and others show AI's opacity differs from
  human opacity in a way that matters for safety, the explainability part of my case weakens.

## Where I land

Judge it by the role it fills, against whoever would otherwise fill it, as they actually are, and
compare whole workflows, not a model against an idealized expert. Then add the checks its real
differences call for: where it fails, whether it can be corrected, and who answers for it.
Sometimes that sets a higher bar for a machine than for a person, and the yardstick should say so
when it does. Every essay after this one uses it.

Stop asking whether it is reliable software. Ask how it compares with whoever would otherwise do
the job.

---

## Notes

### How this essay was made

I wrote this with help from Claude, an AI made by Anthropic, which has a stake in how AI is judged.
Why I build and study these systems is in [the overview](00-the-thing-on-the-other-end.md).

It draws on two research briefs, [The yardstick](../briefs/2026-10-17-6-the-yardstick.md) and
[curiosity](../briefs/2026-10-17-7-curiosity.md), and on the earlier what-ai-is reports. Every source was checked by a tool that looks each one up and has two AIs from different
companies judge whether it supports the claim it backs.
Each brief was checked on 17 October 2026
([yardstick report](../cite-check/2026-10-17-the-yardstick-brief.md),
[curiosity report](../cite-check/2026-10-17-the-curiosity-brief.md)), and so was this essay as a
whole ([report](../cite-check/2026-10-17-position-pieces.md)). Reviewed by a panel and checked
again on 18 October 2026
([review records](../panel/2026-10-18-piece-01-yardstick/),
[check after review](../cite-check/2026-10-18-piece-01-yardstick-after-panel.md)).

### More on engineered curiosity

Jürgen Schmidhuber first suggested rewarding a learning system for improving its own model of the
world, with the reward fading as it stops improving: curiosity and boredom (Schmidhuber 1991). A
large study of purely curiosity-driven agents, across 54 environments, found that prediction-based
curiosity breaks down in random settings ([Burda et al. 2019](https://arxiv.org/abs/1808.04355)).
OMNI uses a language model as a model of what *humans* find interesting, to choose what an agent
should learn next ([Zhang et al. 2024](https://arxiv.org/abs/2306.01711)).

### Sources

[Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285) ·
[Bommasani et al. 2022](https://arxiv.org/abs/2211.13972) ·
[Burda et al. 2019](https://arxiv.org/abs/1808.04355) ·
[Chalmers 2025](https://philarchive.org/rec/CHAWWT-8) ·
[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352) ·
Dell'Acqua et al. 2023 (HBS Working Paper 24-013) ·
Dennett 1987, _The Intentional Stance_ ·
[Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033) ·
[Edmondson 1999](https://doi.org/10.2307/2666999) ·
[Grove et al. 2000](https://doi.org/10.1037/1040-3590.12.1.19) ·
[Hill 2024](https://doi.org/10.1007/s13347-024-00720-4) ·
[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0) ·
Kahneman, Sibony & Sunstein 2021, _Noise_ ·
[Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010) ·
[Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371) ·
[Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116) ·
[Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005) ·
[London 2019](https://doi.org/10.1002/hast.973) ·
[Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013) ·
[Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040) ·
[Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1) ·
[Pathak et al. 2017](https://arxiv.org/abs/1705.05363) ·
[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309) ·
[Rieger et al. 2023](https://doi.org/10.1177/00187208231197347) ·
[Schuman 2025](https://www.computerworld.com/article/3836728/you-thought-genai-hallucinations-were-bad-things-just-got-so-much-worse.html) (_Computerworld_ opinion column, 3 March 2025) ·
[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464) ·
Schmidhuber 1991 (_From Animals to Animats_, 222–227) ·
[Wang et al. 2023](https://arxiv.org/abs/2305.16291) ·
[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/) ·
[Zerilli et al. 2019](https://doi.org/10.1007/s13347-018-0330-6) ·
[Zhang et al. 2024](https://arxiv.org/abs/2306.01711).
Verification marks: the [yardstick brief](../briefs/2026-10-17-6-the-yardstick.md), the
[curiosity brief](../briefs/2026-10-17-7-curiosity.md), and, for the deference, intentional-stance
and Chalmers sources, the [personality](../personality-and-connection.md) and
[Chalmers](../chalmers-and-ai-minds.md) reports.
