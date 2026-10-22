# Can notes carry a rule? The study, step by step (as of 2026-10-18)

_Research brief for essay 02 (`positions/02-it-learns.md`), which summarizes it in "What I
tested". This is the full account of the author's own study: the pre-registered test and the
exploratory follow-up. Numbers were checked against the study records by the 2026-10-17 panel
(a reanalysis by Vera Tukey (an AI review agent), `panel/2026-10-17-piece-01/3-vera.md`; the follow-up's paired McNemar
test gives p ≈ 0.008). Records:
[pre-registered pilot](../../pilots/gopnik-memory-overhypothesis-2026-10-16/) and
[follow-up](../../pilots/gopnik-followup-2026-10-17/README.md)._

## The question

None of these tests the part of Gopnik's work that is about learning across tasks. Children
who see several machines that all "need two" carry that rule to a new one. Can an assistant that
writes itself notes between tasks do the same? That puts the learning profile to a test: does a
rule kept in writing, rather than in the learner, work as well? I designed a study to find out,
and wrote down its design and what would count as success before collecting any data
(pre-registered on 16 October 2026; [pre-registration and result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/)).

It stopped at the first step, by a rule I'd fixed in advance. Before testing notes, it measured
how the models did *without* them on "needs two" machines. Claude Opus 5.5, GPT-6.1 Sol and Grok
4.7 got the rule right on all 240 machines, choosing their own experiments. With nothing left to
improve, there was nothing for notes to show
([the result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md)). Either these newer
models no longer have the "needs two" weakness, or my task removed it, since the prompt named both possible rules
up front. The follow-up below leans toward the first: even with the rules unnamed, the models
usually named "needs two" correctly, about three times in four. Whichever it was, testing whether
notes carry a rule needed a harder task.

I built one, in small steps, each designed from what the last one showed
([details](../../pilots/gopnik-followup-2026-10-17/README.md)). Each machine now allowed only
four tests: too few to be sure of both the rule and which two blocks it uses. I ran Claude and GPT.

In the first two versions, both possible rules were named on every machine. Notes made no clear
difference (27 of 40 machines right with notes, 22 of 40 without), and the notes kept both rules
open. That may have been the sensible reading: naming both rules each time suggests each machine is a fresh draw.

In the third version the rules were never named, so each machine's rule had to be discovered.
That also made the task harder without notes, since the models now weighed more possible rules,
which left notes more room to help.
Each run was a short series of machines that shared one kind of rule, ending on a final machine
where the notes could show their worth. Without notes, Claude usually guessed the rule (8 times in 10 on the final machine) but found the
right pair of blocks only 2 times in 10, and about 3 in 10 across all its machines. With notes, nine of its
ten notes told it to expect "needs two" ("treat 'both needed' as the default rule"), it opened
every final machine with a test suited to that rule, and it got both the rule and the pair right
10 times out of 10. GPT's notes treated each machine as new ("Do not assume the next machine uses the same rule"). It
got the final machine right 8 times in 10 with notes and 6 without, a gap small enough to be chance.

So the notes didn't correct a wrong belief; Claude already leaned toward "needs two." What they
changed is closer to Gopnik's point: Claude spent its few tests the way a learner who knows the rule would.
That is the efficiency gap her group found, closed for one model on one task. And the rule was one
Claude found in its own trials and chose to write down: discovered, not received. That is the
harder case the nickname test only pointed to. Its notes held the rule, like the rats' map, until the next machine called for it.

The limits matter:
- **It is small:** one task, two models, ten runs with notes and ten without.
- **The positive result came on the third version,** after two that showed nothing. That is how
  exploratory work goes, and it is also why the result needs a confirmation run designed in
  advance before it carries weight.
- **Nobody tested whether the expectation gives way** when a machine breaks the pattern, as a
  learner's should. Two of Claude's notes told it to trust the rule over the evidence.
- **The model that showed the effect is made by the same company** as the model that helped me
  draft and analyze this, and that model read and sorted the notes itself, with no check by a reader who didn't know where
  each note came from.

It suggests, short of proving it, that a rule a system finds and keeps in writing can form from
a few examples and carry over to the next task, for at least one model.
