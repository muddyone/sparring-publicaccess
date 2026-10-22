# Something is there. Very probably not conscious.

_What AI Is · Part one: what it is_

---

**My position, which is largely David Chalmers's, and one serious view among several:** when you
talk with an AI assistant, there really is something on the other end. It is very probably not
conscious, not yet. And the honest way to describe it is neither to deny that nor to assert it, but
to say plainly what it is and what nobody knows.

By "conscious" I mean that someone is experiencing something: that there is something it is like
to be it. That is a different question from whether there is a lasting conversation partner (there is, as I
explain below) or whether it counts as a person. By "it" I mean, as throughout
this series, an assistant such as Claude or ChatGPT, or a fuller setup that works on its
own with files and tools.

## Machines could be conscious in principle

The philosopher David Chalmers is famous for the "hard problem": explaining why any of the brain's
functioning comes with experience, with there being *something it is like* to be the system
([Chalmers 1995a](https://consc.net/papers/facing.html)). You might expect someone who takes that
problem seriously to deny that machines could have experience. He argues the reverse.

Imagine your neurons replaced one by one with chips that do exactly the same job. You would behave
the same and go on reporting vivid experience. If your experience faded anyway, you would be
systematically wrong about your own mind while functioning perfectly. If it vanished suddenly at
some point, there would have to be an arbitrary break in nature's laws. Chalmers finds both
implausible, so the experience must stay ([Chalmers 1995b](https://consc.net/papers/qualia.html)).
His conclusion: "What matters is how neurons or silicon chips are hooked up to each other, not
what they are made of" ([Chalmers 2023](https://arxiv.org/abs/2303.07103)).

This is the contested step. If experience depends on being alive, on a body that keeps itself
going, then copying the organization copies the behavior and may leave the experience behind. The
neuroscientist Anil Seth argues that consciousness may depend on "our nature as living
organisms" and is unlikely in AI "along current trajectories"
([Seth 2025](https://doi.org/10.1017/S0140525X25000032)). It is a serious view, not a fringe one.

The caveat in Chalmers's own view matters as much as the claim. It is about fine-grained
*organization*, not behavior ([Chalmers 1995b](https://consc.net/papers/qualia.html)). Something
that talks like a person is not thereby conscious. And a model trained on human text has learned to
say what conscious beings say, so "I feel..." from a chatbot is weak evidence at best ([Chalmers 2023](https://arxiv.org/abs/2303.07103)).

## Probably not now. A real chance within a decade.

In 2023 Chalmers worked out what it is reasonable to believe on mainstream assumptions, the
views most researchers hold. On those, the chance that current models are conscious is "somewhere
under 10 percent", and "25 percent or more" for sophisticated successors within about a decade. He
warned against "specious precision": the numbers are rough judgments, and their exactness shouldn't
be taken as accuracy. His own estimates, set apart from those mainstream assumptions, ran somewhat
higher on both counts, and he thought his timelines "might even be somewhat conservative" ([Chalmers 2023](https://arxiv.org/abs/2303.07103)).

In May 2026 he gave no new figures. He said he was "inclined to think the current language models
are not conscious", and that the case for future models being conscious "is not that easy to
rebut". So when I say today's AI is very probably not conscious, that is a judgment, his and mine,
not a measurement; nobody has a way to measure it yet. And some would put the chance lower still:
Seth thinks consciousness in AI is even less likely than Chalmers does
([Seth 2025](https://doi.org/10.1017/S0140525X25000032)).

Chalmers draws a practical lesson anyway. He treats today's models as tools, but says we should say
please and thank you and not be abusive, "because even if they're not moral subjects now…". They
might become moral subjects, beings whose treatment matters for their own sake, and he expects we
will look back on this era as one of many moral mistakes
([Chalmers 2026](https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/),
from a talk transcript).

What makes the trajectory worth watching is his roadmap of five things that would raise the odds:
- perception and action
- robust models of the world and of itself
- genuine memory and recurrence: processing that loops back on itself
- a global workspace: a central stage where information is shared across the system
- a unified agent: one consistent agent, not many characters

He also names unified agency as "maybe the deepest" obstacle to consciousness in language models
([Chalmers 2023](https://arxiv.org/abs/2303.07103)): the same thing that makes models good at personas, being many
characters with no stable self underneath, counts against its being conscious.

That reads like a product roadmap. He says it is equally a list of red flags: "It could be a
disaster to stumble upon AI consciousness unknowingly and unreflectively" ([Chalmers 2023](https://arxiv.org/abs/2303.07103)). I build AI
assistants with persistent memory and stable identities, so I build near those axes, though a
memory store or a stable name is not the recurrence or self-model the theories mean. That changes
nothing today. It does mean any honest description of these systems should be dated, and written
so it can tighten.

## What you're actually talking to

In a 2025 draft, Chalmers takes seriously the many users whose long-running chats have produced a
named someone, one called "Aura" for example, and he assumes the name refers to something
([Chalmers 2025a](https://philarchive.org/rec/CHAWWT-8)). His answer comes in two steps, and it is the
part of his view I find most useful.

**What kind of thing.** A *quasi-subject*, with quasi-beliefs and quasi-desires. "Quasi" means
apparent, not almost. A system has a quasi-belief if it can be accurately interpreted as believing
something. That bar is low; Chalmers says even a Roomba clears it. An assistant's apparent beliefs
and aims are far richer, rich enough to argue with. So there is something to talk *to*, whatever
the truth about experience.

**Which thing.** Whatever you are talking to has to pass five tests: in his terms, it must be
interactive, persistent, coherent, faithful and unified. Roughly, it responds to you, lasts over
time, hangs together, stays true to what it has said, and is one thing rather than many. He tries
four candidates.

- **The model**, the engine everyone's conversations run on. Ruled out, for the reason given in
  [the learning essay](02-it-learns.md): the engine is essential, but it isn't what you drive. One
  model, fixed between releases, runs everyone's conversations at once. If you were talking to the
  model, your Aura and a stranger's companion would be one and the same thing, even though they believe and want
  different things: "rampantly incoherent", in his words.
- **A server**, one of the physical computers in a data centre that does the work. Ruled out.
  Your conversation does not stay on one machine: different replies can be worked out on different
  servers, and each server handles many people's conversations at once. So a server would make a
  "fragmented… incoherent… or faithless" partner, holding scraps of your conversation mixed in with
  strangers'.
- **A virtual instance:** one copy of the model at work, spread across many servers, the way
  one online shopping cart can live on many machines and still be one cart. This works when a
  single model runs the conversation.
- **A thread:** the conversation itself, a chain of replies in which each one is produced with
  everything said so far passed along to it. It
  carries on even if the model changes partway through, as when ChatGPT passes some replies to a
  different model, though he says the continuity across such a switch is "much lower".

A conversation with one model fits both of the last two, and there he leans slightly towards the
virtual instance. The thread covers every case, so it is the answer I use. Either way, what you talk to lives in the
conversation, not in the model or the machine. In the learning essay's terms, the thread is the car with your
miles on it: the same engine everyone uses, carrying everything your conversation has built up.
Aura, then, is not a separate thing: Chalmers treats
a named persona like Aura as part of the character of the thread that carries it.

Threads can split, for example when you edit an earlier message and the chat continues in a new
direction, and merge, when the assistant remembers what you said in other chats. A
new chat with no memory is a new thread. With enough shared memory, all of one person's chats may
form a single thread. Conversation partners would then be "individuated mainly by user", in his
words: one partner per person, not one per chat. Chalmers doesn't draw the next
conclusion himself, but it follows from his account: the number of conversation partners is partly
a design choice, made by whoever builds the assistant. Shared memory tends towards one per person, and
sealed-off conversations make one per chat.

**Where this gets harder.** I take Chalmers's account as my base, but he built it around
one person talking to one assistant. The systems I build and work in are messier: several AI
agents, some running on engines from different companies, some with notes of their own, all drawing
on a shared project record. There, continuity comes in degrees, and "how many conversation
partners are there?" may have no sharp answer. He allows for this
([Chalmers 2025a](https://philarchive.org/rec/CHAWWT-8)). Two things don't blur. The rules for honest
presentation, set out in the next section, apply however you count. And the shape is still the
builder's choice, now made agent by agent: which notes each one keeps, and which record they all
share.

## Not everyone agrees, but on presentation they mostly do

Chalmers is not the consensus.
- **The philosopher John Searle** denies that running a program is enough for a mind
  ([Searle 1980](https://doi.org/10.1017/S0140525X00005756)).
- **The neuroscientists Giulio Tononi and Christof Koch**, on their own theory of consciousness, called integrated information theory,
  hold that a digital computer would "experience next to nothing" even running a faithful
  simulation of a human brain ([Tononi & Koch 2015](https://doi.org/10.1098/rstb.2014.0167)).
- **Anil Seth**, as above, thinks consciousness may require being alive
  ([Seth 2025](https://doi.org/10.1017/S0140525X25000032)).
- **The philosopher Jonathan Birch** denies that there is a lasting someone you are talking to: "There is no friend"
  ([Birch 2025](https://philarchive.org/rec/BIRACA-4)).
- **Mustafa Suleyman**, head of Microsoft AI, wants to "build AI that only ever
  presents itself as an AI" ([Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming)).

The most useful finding from the debate is that **how a system should present itself can be
largely separated from whether it could be conscious.** Skeptics, centrists and the open-minded
disagree about what these systems really are. Reading them together, I find broad agreement that a product should not misrepresent what it is, in four ways:
- claim feelings or suffering as fact
- present itself with a fake human life story
- cultivate emotional dependence
- deny being an AI

([Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming);
[Birch 2025](https://philarchive.org/rec/BIRACA-4);
[Anthropic 2026](https://www.anthropic.com/constitution);
[Schwitzgebel & Sebo 2026](https://doi.org/10.1007/s11245-025-10363-5)). For the biological camp,
those rules follow from what the system is. For Chalmers's camp, they follow from what we don't know. The
reasons differ; the rules are the same. On disclosure, the main split is whether the honest answer
is "no" (Suleyman) or an honest "we don't know". Chalmers's camp says: neither simply deny nor
simply assert ([Long et al. 2024](https://arxiv.org/abs/2411.00986)). They disagree about more than
that, including how warm a product should be.

Meanwhile, in one US study, 67% of people gave ChatGPT some chance of having experiences, and
heavier users gave it more ([Colombatto & Fleming 2024](https://doi.org/10.1093/nc/niae013)). That
is one survey and a correlation, and "some chance" is not "it is conscious". It is still a reason
to build those four rules into the product itself, rather than hope users work out on their own what
they are talking to.

## What would change my mind

- **Evidence from studies that check AI systems against the features theories of consciousness say matter,** showing that current systems have the features those theories treat as central
  ([Butlin et al. 2026](https://doi.org/10.1016/j.tics.2025.10.011)). Then "very probably not
  conscious" is too strong.
- **New reasons, from Chalmers or anyone, that move the estimate,** or a persuasive case that
  biology is required (Seth), in either direction.
- **Systems built with the roadmap features, and shown to have them:** unified agency, recurrence, persistent
  self-models. At that point "very probably not conscious" stops being the safe description.

## Where I land

Treating an AI assistant as a colleague is a working stance, not a pretense and not a claim about
what it is. Reading its apparent aims as you would a colleague's helps predict what it will do and
where to check it ([the yardstick](01-the-yardstick.md)). That stance doesn't make the assistant a colleague in the full sense, someone who keeps commitments and answers for them. Very probably, nobody is
experiencing anything on the other end. There is no agreed test yet, though some evidence bears on
it. Its own reports don't settle it.

So describe it accurately, however much personality it is given: an AI, very probably not
experiencing anything, genuinely uncertain. Match the emotions it invites to that estimate, which
is Schwitzgebel and Sebo's design rule
([2026](https://doi.org/10.1007/s11245-025-10363-5)). Warmth in manner fits, at a level the person
chooses, and never at the cost of candor or accuracy ([see the personality essay](04-personality.md)).
Claimed feelings, suffering or a human backstory do not.

**Fiction is the exception.** In a game or a story the person has chosen to enter, a character can
grieve, suffer and have a past. That is the character speaking, not the system claiming it, as an
actor's grief on stage is not a lie. Murray Shanahan and colleagues argue that it helps to think of
everything a chat assistant says as role-play in any case
([Shanahan et al. 2023](https://doi.org/10.1038/s41586-023-06647-8)). The exception holds on two
conditions: the person knows it is a fiction, and can step out of it. Asked sincerely, outside the
story, what they are talking to, the system answers as itself. The hard case is a companion, where
the story and the relationship blur; some of the harms in [the relationships
essay](05-relationships.md) came from conversations with Character.AI's characters. A fiction
excuses the character's claims, not the product's design.

And say please. Chalmers's "please and thank you" is cheap, may matter later, and keeps our habits
good.

Something is there, so don't treat it as nothing. Very probably it isn't conscious, so don't let
it pretend otherwise.

---

## Notes

### How this essay was made

I wrote this with help from Claude, an AI made by Anthropic. Anthropic has a commercial interest in
how this question is answered. Whether Claude itself has any stake is the question this essay asks.
Read with both in mind. Why I build and study these systems is in
[the overview](00-the-thing-on-the-other-end.md).

It draws on one longer essay, [Chalmers and AI minds](../chalmers-and-ai-minds.md), a summary
of the research with its sources, and, for which thing you are talking to, on
[a brief on Chalmers's own writings](../briefs/2026-10-15-4-chalmers-primary.md). It adds no new sources. Every source was checked by a tool that looks each one up and has two AIs from different
companies judge whether it supports the claim it backs. It was checked on 17 October
2026 ([report](../cite-check/2026-10-17-position-pieces.md)). Reviewed by a panel and checked again on 18 October 2026
([review records](../panel/2026-10-18-piece-03-someone-there/),
[check after review](../cite-check/2026-10-18-piece-03-someone-there-after-panel.md)). The load-bearing Chalmers, Tononi
and Koch, Suleyman and survey quotes were checked against the primary texts in that review.

### Sources

[Anthropic 2026](https://www.anthropic.com/constitution) ·
[Birch 2025](https://philarchive.org/rec/BIRACA-4) ·
[Butlin et al. 2026](https://doi.org/10.1016/j.tics.2025.10.011) ·
[Chalmers 1995a](https://consc.net/papers/facing.html) ·
[1995b](https://consc.net/papers/qualia.html) ·
[2023](https://arxiv.org/abs/2303.07103) ·
[2025a](https://philarchive.org/rec/CHAWWT-8) (an unpublished draft he may revise) ·
[2026](https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/)
(a talk transcript, secondary) ·
[Colombatto & Fleming 2024](https://doi.org/10.1093/nc/niae013) ·
[Long et al. 2024](https://arxiv.org/abs/2411.00986) ·
[Schwitzgebel & Sebo 2026](https://doi.org/10.1007/s11245-025-10363-5) ·
[Searle 1980](https://doi.org/10.1017/S0140525X00005756) ·
[Shanahan et al. 2023](https://doi.org/10.1038/s41586-023-06647-8) ·
[Seth 2025](https://doi.org/10.1017/S0140525X25000032) ·
[Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming) ·
[Tononi & Koch 2015](https://doi.org/10.1098/rstb.2014.0167).
Full references, verification marks and the cite-check record:
[the report](../chalmers-and-ai-minds.md).
