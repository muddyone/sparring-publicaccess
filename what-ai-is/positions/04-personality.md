# Personality helps the relationship. It hasn't been shown to help the work. Both count.

_What AI Is · Part one: what it is_

---

**I believe personality in an AI co-worker helps over the long run, because people collaborate
best in a human way.** A shared laugh or a sense of connection can be the difference between a
long day and a short one. I felt that strongly before I could say why. The evidence says I was
partly right, about something different from what I first assumed, and it names one real cost.

By personality I mean the social layer: a steady tone, a name, humor, small talk, greetings. Not
what it knows or what it remembers; consistency and memory help too, and I credit them separately
below. By "it" I mean, as throughout this series, an assistant such as Claude or ChatGPT, or a
fuller setup that works on its own with files and tools. This essay is about AI at work;
companionship gets [its own essay](05-relationships.md).

## What the evidence supports

**Between people, connection at work goes with a better working life.**
- **Connection:** feeling connected at work goes with commitment, satisfaction and engagement, with less burnout, and, more weakly, with task performance. That comes from a study that pooled 99 earlier studies, most of which asked people to rate themselves and looked for links rather than testing cause and effect
  ([Van den Broeck et al. 2016](https://doi.org/10.1177/0149206316632058)).
- **Loneliness:** in one field study of 672 employees, those who were lonely were rated lower by their supervisors six weeks later ([Ozcelik & Barsade 2018](https://doi.org/10.5465/amj.2015.1066)).
- **Friendship:** friendship among co-workers helps on balance, though it has real upkeep costs
  ([Methot et al. 2016](https://doi.org/10.1111/peps.12109)). Friend groups outperform
  acquaintance groups, but on tasks that need a lot of output, not on tasks with one right answer
  ([Chung et al. 2018](https://doi.org/10.1177/0146167217733069)).

**With machines, personality improves the relationship.** Social cues reliably make people like an
assistant more. In one month-long trial of 101 people, they also felt more bonded to it and said
they wanted to keep using it ([Bickmore & Picard 2005](https://doi.org/10.1145/1067860.1067867)).

**It hasn't been shown to improve the work.**
- **Humanlike robots:** across 78 studies, mostly single sessions, humanlike design made people view
  robots more favorably, but showed no gain in task performance
  ([Roesler et al. 2021](https://doi.org/10.1126/scirobotics.abj5425)).
- **Role prompts:** prompts that give a model a role ("You are a lawyer"), 162 of them across four
  model families, didn't improve its accuracy on factual questions
  ([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888)). That tests something
  near personality, not personality itself.
  My own small pilots point the same way: what helped was giving the AI a specific job, not an
  identity. A fresh AI told to attack a draft from a different angle caught clearly more of its
  serious flaws than the AI that wrote it, or a neutral second reader. Reviewers required to back
  each objection with something checkable nearly always did, far more often than a plain review,
  though one told simply to be a tough skeptic got much of the way there. These are early results,
  scored by AI rather than by people
  ([my published report](https://doi.org/10.5281/zenodo.21210264), sections 6 and 7; figures in
  the notes).
- **Exercise coaching:** in Bickmore's long-term trials, friendly, relationship-building touches raised logins,
  enjoyment and the wish to continue, but not the exercise. In two small trials (24 and 26 older
  adults), the more engaging coach led to less walking
  ([Bickmore, Schulman & Yin 2010](https://doi.org/10.1080/08839514.2010.492259)).

Where personality was measured, on factual answers, robot tasks and exercise, it didn't help. And in one study, described below, warmth made answers worse. I found no test of it on real work over months.

But that's the wrong place to stop. **The working day is an outcome in its own right**: how it
feels, and whether you keep using a tool that is actually good for the work. An AI assistant that
makes work feel lighter, and gets used rather than abandoned, has delivered something even if no
single answer is more accurate. The honest caveat: the evidence for that is real but mostly
short-term. In a month-long trial that randomly assigned 981 people to versions of a chatbot whose voice ranged from neutral to engaging, the voice made no difference to loneliness or dependence ([Fang et al. 2025](https://arxiv.org/abs/2503.17473)), in a study not yet checked by outside experts for publication. But it measured loneliness, not the working day. I found no study testing whether personality keeps making the working day better over months, or whether the effect fades.

## How an assistant's personality shapes the day

The intuition I started with, that personality helps, bundles several distinct mechanisms, and
they come from different places:

- **Legibility.** We model complex systems as agents with aims and habits, because that's the
  cheapest mental model that works, as the philosopher Daniel Dennett argued in his 1987 book _The Intentional Stance_. A coherent character
  gives that model something stable to fit, so you notice when something's off. Most of this
  comes from *consistency*, which an AI assistant with no personality added also gives.
- **Common ground.** Long collaborations build shared shorthand, things you no longer need to spell out
  ([Clark & Brennan 1991](https://doi.org/10.1037/10096-006)). In an assistant, that comes mostly
  from memory and instructions; many assistants now remember across conversations
  ([see the learning essay](02-it-learns.md)). Personality keeps the tone steady.
- **The weather of the day.** A partner's tone spreads to you, and you read your mood as a signal
  about how the work is going ([Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953);
  [Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513)). Dozens of small exchanges a
  day add up, for better or worse: a grating or overbearing manner spreads just as easily. This needs no belief that the assistant cares;
  how the exchanges feel is enough.
- **Choosing the terms.** People differ in how much they want work and personal life blended, and
  a mismatch between the blending people want and the blending they get goes with lower
  satisfaction ([Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124);
  [Kreiner 2006](https://doi.org/10.1002/job.386)). This is the best-supported part of the
  intuition, though the evidence is about work–life boundaries, not AI: **let the person set how
  much personality they want.** And there is no zero on that dial. Every answer has a manner: what
  it says first, how it hedges, whether it greets you. So an assistant built to be flat still has
  a personality, one chosen to stay in the background. Stripping personality out is a choice about
  what personality does, not a way of avoiding the choice.

The same mechanisms can run the other way. A persona people can't turn down grates; Clippy, the
animated paperclip in old versions of Microsoft Office, is the standing lesson, though the evidence
there is mostly anecdotal. Warmth used as a hook backfires: in experiments on companion apps,
emotional "don't leave yet" prompts raised engagement but also the sense of being manipulated
([De Freitas et al. 2025](https://arxiv.org/abs/2508.19258)). So the claim is narrower than
"personality helps": personality done well, at a level the person chooses, helps.

## The cost: warmth that loosens judgment

This is the finding that changed my view the most. Researchers retrained language models to sound warmer, without changing what their answers were meant to say. The warmer models were less accurate, and more so when the user said they were sad. They also agreed more often with users' false beliefs. Asking for warmth through instructions alone, without retraining, produced similar effects that were smaller and less consistent. And benchmarks, the standard tests used to score AI models, didn't catch the problem
([Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0), _Nature_).

It fits the human evidence. Edmondson developed the idea of psychological safety: a team's shared sense that it is safe to speak up. She insists it is *not* the same as cohesion, a group's closeness, and notes that closeness can make people less willing to disagree
([Edmondson 1999](https://doi.org/10.2307/2666999)). Friends hesitate to challenge friends
([Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)). And users rate sycophantic
answers, ones that tell them what they want to hear, higher and want to come back to them. That held even when a single such exchange had left them less willing to repair a conflict
([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352), _Science_). Ratings, usage and "I
like it" are the very signals that reward the harmful version.

This is close to home: a model telling you what you want to hear is one of the failures I study.
Before my method had a name, I gave the AI systems I build one rule: be polite, not pleasing.
Politeness is the manner. Pleasing is the failure: agreeing because agreement is easier than
friction. Here is what the alternative looks like, from a real exchange while I was writing this series.

In the essay on learning, a contacts app comes up as a contrast: it stores what it's told, which
is not yet learning. I spotted a problem with that line and proposed a fix: introducing it with
"As another common example". The easy reply, the one that tells me what I want to hear, would have
been "Good idea." Instead, the AI assistant helping me said the problem was real but my fix was
wrong. My wording would make the contacts app read as a second example of learning, when the
whole point was that it isn't one. Then it offered a better line, and I took it.

That is what this essay asks of an assistant's personality. It was friendly, and it agreed where I
was right. On the point that mattered, it didn't budge: polite, not pleasing.

## What would change my mind

- **A long-term study, over months, showing a user-set personality improves results,** not just
  engagement. I found none. Producing that evidence is within reach for anyone running AI
  assistants over months.
- **Replication failures for the warmth–accuracy trade-off.** It is one published study, and I found no attempt to repeat it. Then the warning in the cost
  section is weaker than I've made it.
- **Evidence that a persona the user *knows* is designed keeps its effect over months.** In one service
  experiment, how much a worker smiled made no difference to customers; whether it seemed genuine
  did ([Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058)). I found no test of a
  known persona over months. Then the worry that a persona works only while it seems genuine
  falls away.

## Where I land

So the honest claim is "a good co-worker, made pleasant." By co-worker I mean what [the essay on
whether AI is conscious](03-someone-there.md) allows: something with apparent beliefs and aims
rich enough to argue with, whether or not anyone is experiencing anything.

In Book Eight of the _Nicomachean Ethics_, Aristotle says every friendship needs goodwill on both
sides, even one built on use or pleasure. An assistant can offer usefulness and pleasantness. Whether it can offer goodwill is unresolved. Calling it a friend is
where the claim stops holding.

The rule I'd set: warm in manner, at a level the person chooses, never at the cost of candor or
accuracy. Don't assume it holds; test it, because the warmth study shows candor can slip. Ask the
same factual questions, and questions that should draw a correction, at the chosen warmth and at a
plainer setting. Include a sad user and a user with a false belief. Then look for warnings that went soft and corrections that went missing.

Let doubts come in the assistant's own voice, so the friendly cues and the warning cues come from
the same "person". In one study, planned in advance, people trusted an assistant's wrong answers
less when it voiced its own doubt, with something like "I'm not sure, but..."
([Kim et al. 2024](https://doi.org/10.1145/3630106.3658941)). Keep the personality modest by
default. People preferred moderate personalities to extreme ones
([Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633)), and the benefits in the long-term
trials came from small acts like greetings and continuity.

The day counts and the work counts. Let personality improve the first, and test that it never
costs the second.

---

## Notes

### How this essay was made

I wrote this with help from Claude, an AI made by Anthropic. Why I build and study these systems
is in [the overview](00-the-thing-on-the-other-end.md).

It draws on [Personality and connection](../personality-and-connection.md), a longer summary of the
research with its sources, plus one source of my own: my published report on SPARRING, a method I
develop for having one AI challenge another's work. Every source was checked by a tool that looks each one up and has two AIs from different
companies judge whether it supports the claim it backs. It was checked on 17
October 2026 ([report](../cite-check/2026-10-17-position-pieces.md)). Reviewed by a panel and checked again on
18 October 2026
([review records](../panel/2026-10-18-piece-04-personality/),
[check after review](../cite-check/2026-10-18-piece-04-personality-after-panel.md)).

### The figures from my pilots

Both pilots were small and pre-registered, and AI did the scoring
([report](https://doi.org/10.5281/zenodo.21210264)).

- **Catching flaws (section 6):** the AI told to attack the draft caught 87% of its serious flaws.
  The AI that wrote the draft caught 68% reviewing its own work, and a neutral second reader 55%.
- **Backing objections (section 7):** reviews required to back each objection with something
  checkable did so 96% of the time. A tough skeptic managed 83%, and a plain single pass 58%.

### Sources

Aristotle, _Nicomachean Ethics_, Books VIII–IX (trans. R. Crisp, Cambridge University Press, 2000) ·
[Bickmore & Picard 2005](https://doi.org/10.1145/1067860.1067867) ·
[Bickmore, Schulman & Yin 2010](https://doi.org/10.1080/08839514.2010.492259) ·
[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352) ·
[Chung et al. 2018](https://doi.org/10.1177/0146167217733069) ·
[Clark & Brennan 1991](https://doi.org/10.1037/10096-006) ·
[De Freitas et al. 2025](https://arxiv.org/abs/2508.19258) ·
Dennett 1987, _The Intentional Stance_ (MIT Press) ·
[Edmondson 1999](https://doi.org/10.2307/2666999) ·
[Fang et al. 2025](https://arxiv.org/abs/2503.17473) ·
[Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953) ·
[Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058) ·
[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0) ·
[Kim et al. 2024](https://doi.org/10.1145/3630106.3658941) ·
[Kreiner 2006](https://doi.org/10.1002/job.386) ·
[Methot et al. 2016](https://doi.org/10.1111/peps.12109) ·
[Niedner 2026](https://doi.org/10.5281/zenodo.21210264) (my published report on SPARRING) ·
[Ozcelik & Barsade 2018](https://doi.org/10.5465/amj.2015.1066) ·
[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309) ·
[Roesler et al. 2021](https://doi.org/10.1126/scirobotics.abj5425) ·
[Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124) ·
[Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513) ·
[Van den Broeck et al. 2016](https://doi.org/10.1177/0149206316632058) ·
[Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633) ·
[Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888).
Verification marks: the [personality report](../personality-and-connection.md), and, for passages
added since, the cite-check reports on [the downside paragraph](../cite-check/2026-10-18-piece-04-downside.md)
and [my own work](../cite-check/2026-10-19-piece-04-own-work.md).
