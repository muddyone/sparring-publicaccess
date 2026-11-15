# It learns. The better question is what kind of learner it is.

_What AI Is · Part one: what it is_

---

**My position: judge learning by its function, not its form, and let a difference in form count
once someone shows what it changes.** The common argument that AI "doesn't really learn" is that it
doesn't learn the way people do: no brain, no childhood, no practice slowly turning into habit.
That is a test of form. Judged by function, an AI assistant with a memory does learn: it keeps
what its experience gives it and uses that later. What's left of the disagreement is narrower and
more interesting: what kind of learner it is, and whether it can *discover* things or only receive
them. That is a question we can test, not just argue.

## Where this started

In May 2026 Alison Gopnik, who studies how children learn, told Chris Hayes on his podcast that a two-year-old routinely outsmarts the best AI
models ([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f)).
She holds the common view that large models don't learn or think the way we do. My reaction was
simple: humans are pattern machines too. We learn by finding and internalizing patterns, and we
think by recognizing, connecting and extending them. So what, exactly, is supposed to be
different?

Working that out took me somewhere more useful than "she's wrong." My own first impulse,
"we're pattern machines too," answered a claim about form with another claim about form. The
better move is to stop arguing about form and ask what each learner can do.

## What I mean by "it"

By "it" I mean an AI system as people use it now: an AI assistant such as Claude or ChatGPT, or a
fuller setup in which an AI works on its own, with files and tools, over days, like the ones I
build. At its core is a large language model, the program a company trains and releases in
versions. The model is the engine and the system is the car: the engine is essential, but it isn't what
you drive. When I say "it," I mean the whole car. The engines improve too, version by version, and that series is a
second learner, which I call "the line of models" and take up below.

The car hasn't always kept what it learns. Since at least 2020, a model has been able to
pick up a pattern from examples within one conversation, but conversations were short, and when
one ended, everything in it was gone. Then systems began to keep things. ChatGPT added standing
instructions (a note the user writes once that applies to every conversation) in 2023 and memory across conversations in 2024. Claude's app gained memory in 2025,
and by then AI setups that work on their own were keeping written notes. Researchers had built AI
with written memory earlier ([Shinn et al. 2023](https://arxiv.org/abs/2303.11366)). What changed
in 2024 and 2025 is that written memory reached the tools people use every day (sources in
[the brief](../briefs/2026-10-18-10-when-assistants-began-to-remember.md)). That is the change that matters here. The definition below asks for a lasting
change, so before memory arrived, "it doesn't really learn" was close to true of the AI assistant, though never of
the line of models. My claims are about the system since then.

## What learning means, before we argue about it

A common working definition: learning is a lasting change, caused by experience, in what a system
knows, which changes what it can do or predict later. "What it knows" matters. It means
information the system takes from its experience and uses to guide what it does next, and it can
sit quietly until it's needed. Edward Tolman's rats learned a maze while exploring it for no
reward, and showed it only when food appeared
([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)). So function here means what
a learner can do, not only what you happen to see it doing.

The definition says nothing about brains or biology. Most objections quietly add a requirement
about form: what the learner is made of, and whether its learning looks
like ours. Form can matter. A body, or having something at stake, might change what a learner can
do. But whoever claims a difference in form matters should show what it changes. It can't simply
be assumed.

## The nickname test

Ask an AI assistant to call you by a nickname. It saves the request and uses the name from then on.
Every part of the definition is met: experience caused it, it lasts, it changed what the system
knows, and it changes what it does later.

The usual reply is "that's just a note in a file." That is an objection to form: it is about
where the knowledge is kept, not what it does. The philosophers Andy Clark and David Chalmers
apply the same logic to people, in what they call the extended mind: for Otto, a man with memory loss who relies on a
notebook he always carries, the notebook functions as memory
([Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7)). So the unit that learns is not
the bare model. **It is the assistant as a whole: the model with its memory and notes.**

The nickname is the easy case, because the user supplied it: the assistant received it. But a contacts app does that much:
it stores what it's told. The harder case is an assistant choosing what to record from its own trials, and then acting
on it. That is what my study tested (below).

## Which thing learns

A common objection points at the frozen model: between releases it never changes, so it never
really learns. Shardlow and Przybyła, arguing that a language model can't be conscious, put it
plainly: once trained, "the weights no longer change" (the weights are the billions of numbers that training sets inside the model), so models "have no capacity to learn beyond
their initial training" ([Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521)).
That is like looking at a second grader and concluding she never learned anything, because today
she knows only what a second grader knows. She got there by learning, and she is still learning.
The frozen model got there by training, which is learning by any definition. What keeps learning
after that is the assistant built around it, the whole car, through its notes.

There is a second learner here: the line of models. A new version is usually a new model, trained
by engineers, much as a breeder raises the next generation from the last. What shapes it includes
how its predecessor did: the conversations people had with it, the training data it wrote or
filtered, the failures its engineers saw
([brief](../briefs/2026-10-17-9-how-models-change.md)). AI companies now say so in their terms of service.
Anthropic, for one, trains new models on consumer conversations when users allow it
([Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms)). A conversation
like the one that shaped this essay can become part of what the next model learns from. No version
remembers it, but the line changes with that experience. Each learner meets the definition at its
own level: the assistant within a version, the line across versions.

## What Gopnik actually argues, and why I agree with most of it

Her published case is more careful than the soundbite about a two-year-old outsmarting the best AI
([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)). Models are
*cultural technologies*, like writing, print and libraries: superb at gathering and passing on
what people already know. Children are *truth-seekers* who experiment on the world. In her group's
tests of tool innovation, finding a new use for an everyday object, children had to draw a circle with no compass, choosing among a ruler,
a round-bottomed teapot and a stove; the teapot works, because you can trace its base. Children
aged 3 to 7 picked the object that would work 85% of the time on average. The models did
worse, pulled toward the object most associated with the usual tool. GPT-4 did best, at 76%. On the
matching *imitation* question, which only asks what usually goes together ("which goes best with
a compass?"), they did well. Those were
2022 and 2023 models, and newer ones have narrowed the gap (below).

That is not an argument about form. Her soundbite was about form ("don't learn or think the way we do"), and
so was my comeback. Her paper is about function: what each learner can do with evidence, and who
chooses the evidence. On that, I think she is largely right.

Two points from her own field sharpen her claim rather than undercut it. Her theory of children is
itself statistical: children update their guesses as evidence comes in, but from experiments they
run themselves rather than from text. And much human learning is imitation too. So the difference
isn't pattern learning against something else. It is what evidence a learner learns from, and who
chose it.

My comeback had a further flaw. "Pattern machine" is too broad to prove anything: a thermostat
qualifies. Worse, it hides a real difference. A person predicts, acts, lives with the result and
adjusts, with something at stake. A model learns mostly from what others have written, and the
model itself doesn't change from its own experience between releases. Two learners can reach the
same answer by very different routes, and different routes break in different places.

Her real claim stands: **a learner that experiments on the world fails
differently from one that reads about it.** Her distinction was never learning versus not
learning. It is passing knowledge along versus discovering it. That is a claim about function, and
the kind worth having: it predicts what each learner will get wrong. Judging by function doesn't
answer her claim. It is how her claim gets heard.

## Learning profiles

Henry Molaison, known for decades as patient H.M., could form almost no new memories of facts or
events after his 1953 surgery. Yet when Brenda Milner had him trace a star seen only in a mirror,
he learned the skill and kept it across three days, with no memory of ever having practiced
([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023)). No one concluded he couldn't learn
because his learning no longer looked like other people's. They looked at what he could do, and
concluded memory has separate systems.

Today's AI assistants with memory have roughly the opposite profile. H.M. could gain skills but
not new facts. The assistant gains new facts easily, by writing them down, but practice never
becomes skill on its own; to keep a lesson, it has to put it into words, as a fact.

- **Facts and preferences.** A person remembers them after a telling or two. An assistant with
  memory writes them down and rereads them every time.
- **Rules you have to remember.** A person is reminded until the rule becomes habit. The assistant
  follows it every time from a note. It never becomes habit, but rereading costs it almost nothing.
- **Skills from practice.** For a person, practice slowly becomes automatic. The assistant records
  what worked, and the lesson has to be put into words.
- **Know-how that's hard to put into words.** A person's goes straight into body and brain. The
  assistant learned its know-how from images, sound and video in training, and its day-to-day
  notes are mostly text.
- **Big leaps in ability.** A person's take years of growing up. The assistant's come with each
  model release: the line of models learns, not the individual version.

Some of these differences are only form: the same result, reached another way. Others may change
what the learner can do, and can be tested. A written rule, for example, only helps if it is looked up at the right
moment; a habit fires on its own. The largest, for today's assistants, is that **between model
releases their learning must pass through a record kept outside the model**, mostly written notes;
a person's can also go straight into the brain. People turn rules into reflexes, as the psychologist John
Anderson described ([Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)). A stored record
can be followed reliably, but it never becomes a reflex.

My guess is that for knowledge work, where
nearly everything can be written, that gap is small. For discovery, which depends on noticing what
nobody has written down yet, it may not be. Not every AI system shares this profile: one that keeps
updating the model itself, or remembers mainly in images and sound, would learn differently.

The useful question, then, isn't "does it learn?" It is what kind of learner this is, and that has
two parts: what it can keep, which is its profile, and where its knowledge comes from, received or
discovered. My own study ended up asking both at once: can a rule the system discovers be kept in
writing and carried to the next task?

## Her claim, tested

This is where judging by function pays off: a claim about what a learner can do can be tested.
Gopnik's claim is one of these, and newer models have already been run on close versions of her
group's tasks:
- **Tool innovation:** on 20 newly written puzzles, GPT-4o scored 81.3% against adults' 88.2%,
  rising to 86.0% when it reasoned step by step
  ([Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)).
- **The blicket task, with models exploring for themselves.** A "blicket detector" is a machine
  that lights up when the right blocks are put on it. The learner tries blocks to work out which
  ones those are. Some machines light up for any one of the right blocks. Others light up only
  when two particular blocks are on together; call that "needs two". Models working this out for
  themselves learn the "any one" rule well and the "needs two" rule poorly. Adults have the same
  weakness: they tend to expect each cause to work alone. Young children take up "needs two" more
  readily ([Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010)). The models'
  pattern matches the adults' ([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)).
- **Gopnik's own group** then found that leading models approach human accuracy but explore less
  efficiently, with the same weakness on "needs two". Human adults who run their own tests get
  much better at "needs two", though "needs two" still takes them more tests to work out than "any one" does
  ([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)).

On these tasks, then, the gap in accuracy has narrowed; the gap in exploring efficiently has not closed. That second
half is her claim, still standing.

## What I tested

None of these studies tests the part of Gopnik's work that is about learning across tasks. Children
who see several machines that all "need two" expect the same of the next one
([Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010)). Can an AI assistant that
keeps notes between tasks do the same, keeping the rule in its notes rather than inside the model?

I tested it in small steps, each built on what the last one showed
([the full account](../briefs/2026-10-18-11-notes-and-rules-study.md)). In the first test, the three
models I tried already got the rule right on every machine, so notes had nothing to add. So I made
the task harder: each machine allowed only four tries. In the first two versions of that harder
task, where the possible rules were spelled out, notes made no clear difference. In the third,
nobody told the models what kinds of rule to look for. There Claude worked out "needs two" for
itself and wrote it down. After each machine, the version with notes was told which blocks had
been the right ones, never the rule, and then wrote its note; the version without notes was told
neither. That is roughly what an assistant has when a user corrects it and it writes the lesson
down. With those notes, it got both the rule and the right pair of blocks on
the last machine in each series 10 times out of 10, against 2 out of 10 without them. GPT's notes
treated each machine as new and made no clear difference.

The notes didn't correct a wrong belief; Claude already leaned toward the rule. They made its
exploring efficient. That was the gap Gopnik's group found, and here it closed, for one model on
one task. And the rule was one Claude found and chose to write down: discovered, not received. That
is the harder case the nickname test only pointed to. Its notes held the rule, the way the rats
held their map of the maze, until the next machine called for it.

This result has real limits. It comes from one small, exploratory study, not planned in advance. The result came
only on that third version. Nobody tested whether the rule gives way when the pattern changes. And
the model that showed it is made by the same company as the AI that helped me write this. So it
suggests, short of proving it, that a rule a system finds and keeps in writing can carry over to
the next task.

## What would change my mind

Each of these is a way form could turn out to matter, by changing what the learner can do.

- **If a repeat of the study, planned in advance, finds that the notes don't pass the rule on to
  the next puzzle,** or that the rule they pass on doesn't give way when the pattern changes, the "learning must pass through writing" gap matters more
  than I've claimed, at least for discovering cause and effect.
- **If someone shows that having something at stake,** a body or a life that can go wrong, changes
  what a learner can do, then the "it doesn't learn the way we do" argument is right on that point.
  Today's assistants, with nothing at stake, would be weaker learners than I've claimed, and I should
  say so.
- **If studies show that choosing one's own experiments is what lets a learner discover causes
  that others miss,** and models keep falling short of it, Gopnik's claim is the deeper point, and the distance between these learners is
  larger than I have allowed here.

## Where I land

Judged by what it does rather than what it is made of, an AI system with memory,
whether an assistant or a setup that works on its own, holds on to what its experience gives it and
uses that later. The line of models learns too, across versions, partly from how each one did. The
common argument against all this rests on form: it doesn't learn the way we do.
That is true, and it isn't enough. A difference in form should count once someone shows what it
changes.

What has been shown so far is narrower. Between releases, this learner keeps what it learns in
writing, not in reflexes, and its model was built mostly to gather what people already know. Gopnik is
right that the hard test is discovery. My small, exploratory study found one model, on one task,
finding a rule in its own trials, writing it down, and using it on the next task. That is one step, not proof.

Judged by what it does, today's AI learns. So stop asking. Ask whether it can find out what nobody has told it.

---

## Notes

### How this essay was made

I wrote this with help from Claude, an AI made by Anthropic. So an AI helped write an essay about
whether AI learns, and it has a stake in the answer. Weigh my study results with that in mind.

It draws on four longer documents: [Does it learn?](../learning-and-gopnik.md), a summary of the
research with its sources;
[How a model moves from version to version](../briefs/2026-10-17-9-how-models-change.md);
[When AI assistants began to remember](../briefs/2026-10-18-10-when-assistants-began-to-remember.md); and
[Can notes carry a rule?](../briefs/2026-10-18-11-notes-and-rules-study.md), the full account of my
own study. Four
sources added later (Shardlow & Przybyła 2024; Lucas et al. 2014; Anthropic 2025; Shinn et al. 2023) are linked
where they are used.

Every source was checked by a tool that looks each one up and has two AIs from different
companies judge whether it supports the claim it backs. It ran four times
([first check](../cite-check/2026-10-17-position-pieces.md),
[after revision](../cite-check/2026-10-17-piece-01-revised.md),
[after review](../cite-check/2026-10-17-piece-01-after-panel.md),
[after the second review](../cite-check/2026-10-18-piece-01-revisions.md)). Reviewers then tested
the argument, the evidence and the writing, twice. Those reviewers were AIs too, from three
companies, each given a reviewer's role ([first review](../panel/2026-10-17-piece-01/),
[second review](../panel/2026-10-18-piece-01-revisions/)). Checked and reviewed on 17 and 18 October 2026.

### Sources

[Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369) ·
[Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms) (consumer terms,
2025-08-28) ·
[Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7) ·
[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606) ·
[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614) ·
[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f)
(the interview; not machine-checkable, and no claim here rests on it beyond the quoted line) ·
[Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010) (Lucas, Bridgers, Griffiths
& Gopnik, _Cognition_) ·
[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464) ·
[Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521) (_PLOS ONE_; quotes
checked against the published text 2026-10-17) ·
[Shinn et al. 2023](https://arxiv.org/abs/2303.11366) (Reflexion) ·
[Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023) ·
[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm) ·
[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/).
Full references and the cite-check records: [the synthesis](../learning-and-gopnik.md) and
[brief 9](../briefs/2026-10-17-9-how-models-change.md) and
[brief 10](../briefs/2026-10-18-10-when-assistants-began-to-remember.md) and
[brief 11](../briefs/2026-10-18-11-notes-and-rules-study.md).
