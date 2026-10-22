# Chalmers and AI minds: where we are, where it's heading, what it means for our agents

_Research report, 2026-10-15. Draws on two research strands run the same day:
Chalmers's own work, read in the primary texts, and the debate around him.
Background for Wise Witan's Method: Agents, sections 1 and 2.
Companion to [Personality and connection](personality-and-connection.md)._

## Why this matters to us

Wise Witan builds agents that work alongside people. Some have names and
characters, some have long memories, and some setups run several of them. So
the questions "what is this thing?" and "is there anyone there?" are not
abstract for us. They decide what we say to a client who asks, and what we
promise or carefully don't promise. They decide how many agents we create and
how we retire one. The partner generally aligns with David Chalmers. This
report sets out what Chalmers actually holds, with his hedges and numbers. It
then shows where the others in the debate disagree, and turns all of it into
design consequences.

## The short answer

1. **Chalmers says machines can in principle be conscious.** What matters is
   how a system is organised. What it is made of does not matter
   ([Chalmers 1995b](#chalmers1995b); [Chalmers 2023](#chalmers2023)).
2. **He thinks today's models are probably not conscious.** His estimate is
   "under 10 percent", and his personal figure is somewhat higher. He puts the
   chance that sophisticated successors are conscious within about a decade
   at "25 percent or more" ([Chalmers 2023](#chalmers2023)). In May 2026 he
   said current models are "most likely not conscious" and that he treats
   them as tools, but he also said to be polite and not abusive
   ([Chalmers 2026](#chalmers2026)).
3. **He says there is something real on the other end of the conversation.**
   It is a *quasi-subject*. You can accurately read it as believing and
   wanting things, whether or not anyone is home. It is the conversation
   thread, not the model, and a persona is a feature of that thread
   ([Chalmers 2025a](#chalmers2025a)).
4. **On honest presentation, his camp's rule is "neither deny nor assert".**
   Say plainly what it is. Be calibrated about what nobody knows
   ([Long et al. 2024](#long2024)).
5. **Our design choices move along the very axes he watches.** Persistent
   memory, a stable single agent and a rich self-model are among the
   ingredients on his "roadmap" to possible machine consciousness
   ([Chalmers 2023](#chalmers2023)). That changes nothing today. It does mean
   our presentation policy should be dated and written so it can tighten.
6. **It also offers a new way to see the persona dial.** Chalmers co-wrote
   "The Extended Mind" ([Clark and Chalmers 1998](#clark1998)). On his view,
   an assistant can be *part of your mind* or *someone else you work with*,
   and the more agent-like and social it gets, the less it is the former
   ([Chalmers 2025b](#chalmers2025b)). The dial moves between those two.

## 1. Chalmers's position in four moves

### 1.1 Experience is the hard problem

There are "easy problems": explaining how the brain discriminates, attends,
reports and controls behaviour. These are hard in practice but tractable in
principle. The *hard* problem is why any of that is accompanied by
experience, by there being *something it is like* to be the system. A full
functional story doesn't say why the lights are on
([Chalmers 1995a](#chalmers1995a)). Chalmers concludes that experience has to
be treated as a basic feature of the world, linked to physical processes by
natural laws. He calls the view "naturalistic dualism"
(*The Conscious Mind*, 1996; [Chalmers 1996](#chalmers1996)). He takes
panpsychism seriously without endorsing it. In 2019 he split his own credence
roughly 30% panpsychism, 30% dualism, 10% illusionism and 30% something else
([Chalmers 2019b](#chalmers2019b)).

### 1.2 But experience follows organisation, so silicon can qualify

This is the step that makes him an *optimist about the possibility* of AI
consciousness, unusually among dualists. Imagine replacing your neurons one by
one with chips that do exactly the same job. You would behave the same
throughout and go on reporting vivid experience. If your experience faded
anyway, you would be badly wrong about your own mind while functioning
perfectly, which he finds implausible. If it flickered out suddenly at some
point, you would never notice ([Chalmers 1995b](#chalmers1995b)). His
conclusion: experience is fixed by *fine-grained functional organisation*.
"What matters is how neurons or silicon chips are hooked up to each other,
not what they are made of" ([Chalmers 2023](#chalmers2023)).

**The caveat that matters most for us.** The claim is about *fine-grained*
organisation, not behaviour. Something that talks like a person isn't
thereby conscious. That is why his assessment of AI turns on *architecture*
(memory, recurrence, a global workspace, a unified agent)
([Chalmers 2023](#chalmers2023)). It does not turn on how human the outputs
sound.

### 1.3 Self-reports are weak evidence

Chalmers's "meta-problem" asks why we *think* there is a hard problem. One
lesson he draws is that very simple programs can reproduce our puzzled talk
about consciousness ([Chalmers 2018](#chalmers2018)). A model trained on human
text has learned to say what conscious beings say. "The fact that it has
learned to imitate those claims doesn't carry a whole lot of weight"
([Chalmers 2023](#chalmers2023)). So when an agent says "I feel…", that
is not evidence either way. This applies to our personas too: the character's
voice tells you nothing about whether anyone is there.

### 1.4 The interlocutor is real, but it is a quasi-subject

In his 2025 draft, "What We Talk to When We Talk to Language Models"
([Chalmers 2025a](#chalmers2025a)), Chalmers starts from the hundreds of
emails he gets from users whose long-running chat has produced a named
someone ("Aura"). He takes them more seriously than most: "When a user
interacts with Aura, they seem to be interacting with something", and there
really is a persistent interlocutor. His answer has two parts.

- **What kind of thing.** A *quasi-subject* with *quasi-beliefs* and
  *quasi-desires*. "Quasi" means *apparent*, not *almost*. A system has a
  quasi-belief if it can be accurately interpreted as believing something.
  These are cheap; a Roomba has them. So an LLM interlocutor is a real agent
  in the interpretive sense, whatever the truth about experience
  ([Chalmers 2025a](#chalmers2025a)).
- **Which thing.** Not the model, which is one abstract object shared by
  everyone. Not the server, since one conversation is spread across many
  machines and one machine serves many conversations. It is the *virtual
  instance* or *thread*: the running conversation, carried forward by its
  context and memory. Threads can branch and merge. With enough shared memory
  across conversations, "interlocutors will be individuated mainly by user"
  ([Chalmers 2025a](#chalmers2025a)).

For future systems that *are* conscious, he leans to the view that sealed-off
threads are separate subjects. One model holding a work conversation and a
home conversation would be two subjects, like the split workers in
*Severance* ([Chalmers 2025a](#chalmers2025a)).

**Where a persona sits.** Chalmers doesn't treat a persona as a separate
entity. It is part of the character of the thread that carries it
([Chalmers 2025a](#chalmers2025a)). In 2020 he described GPT-3 as "a chameleon
that can take the shape of many different agents… an engine that can be used
under the hood to drive many agents" ([Chalmers 2020](#chalmers2020)). He also
names *unified agency* as "maybe the deepest" obstacle to LLM consciousness
([Chalmers 2023](#chalmers2023)). The same feature that makes models good at
personas, being many characters with no stable self underneath, counts
against there being anyone there.

## 2. Where we are, and the trajectory

| When | What Chalmers said |
|---|---|
| 1996 | Consciousness is in principle possible in any system with the right fine-grained organisation, silicon included ([Chalmers 1995b](#chalmers1995b); [Chalmers 1996](#chalmers1996)). |
| 2020 | GPT-3 is a chameleon, an engine for many agents. Open to minimal consciousness, as for a worm ([Chalmers 2020](#chalmers2020)). |
| 2022–23 | Current LLMs: "somewhere under 10 percent" (his own figure somewhat higher). Over 50% that we'll have systems with memory, recurrence, a global workspace, unified agency and world and self models within a decade, and at least 50% that such systems would be conscious. That gives "25 percent or more" by roughly 2032–33. Warns against "specious precision". After GPT-4 he called his timelines possibly "somewhat conservative" ([Chalmers 2023](#chalmers2023)). |
| 2024 | Co-author of "Taking AI Welfare Seriously": a "realistic possibility" of near-term AI moral patients. Companies should acknowledge, assess and prepare, and should not train models simply to deny or assert consciousness ([Long et al. 2024](#long2024)). |
| 2025 | The interlocutor is a thread-bound quasi-subject (section 1.4; [Chalmers 2025a](#chalmers2025a)). |
| May 2026 | Current models "most likely not conscious". He treats them as tools, but says "say please and thank you", and don't be abusive even if they aren't moral subjects now ([Chalmers 2026](#chalmers2026)). He co-authored a paper finding a "functional welfare axis" in models that reinforcement learning uses, with no claim about experience ([Han et al. 2026](#han2026)). |

His roadmap to a possibly conscious machine reads like a product roadmap
([Chalmers 2023](#chalmers2023)):

- perception and action;
- robust world and self models;
- genuine memory and recurrence;
- a global workspace;
- unified agent models.

He says the list is equally a set of red flags: "It could be a disaster to
stumble upon AI consciousness unknowingly and unreflectively." And he adds:
"I'd be especially cautious about creating agent models"
([Chalmers 2023](#chalmers2023)).

**In plain terms.** On Chalmers's own numbers, the agents we deploy today are
very probably not anyone. The agents of the early 2030s may be someone, at
odds he would put around one in four. The movement between the two runs
through features we are building for good product reasons: persistent memory,
stable identity, a model of the user and of itself.

## 3. The debate around him

Chalmers's views are not the consensus. Here is where the main voices sit,
from most sceptical to most open.

| Who | Position | Where they part from Chalmers |
|---|---|---|
| Searle; Tononi and Koch (integrated information theory) | Running a program can't produce a mind ([Searle 1980](#searle1980)); on IIT, conventional digital hardware "would experience next to nothing" ([Tononi and Koch 2015](#tononi2015)). | Reject his substrate-independence claim. |
| Anil Seth ([2025](#seth2025)) | Consciousness may depend on being a living organism, so it is "unlikely along current trajectories". | Puts biology back in as a requirement. |
| Ned Block ([2026](#block2026)) | Conditional sceptic: if consciousness depends on mechanisms below the computational level, AI may never get there. | Less sure that organisation is enough. |
| Emily Bender | LLMs stitch together form without meaning ([Bender et al. 2021](#bender2021)); anthropomorphising them is hype ([Bender and Hanna 2025](#bender2025)). | Against first-person, human-like presentation as such. |
| Schwitzgebel | "We will not be able to tell which theories are right" ([Schwitzgebel 2025](#schwitzgebel2025)). Don't build systems whose moral status is unclear, and design systems to invite the emotions their real status warrants ([Schwitzgebel and Garza 2015](#schwitzgebel2015); [Schwitzgebel and Sebo 2026](#schwitzgebel2026)). | Agrees about the uncertainty; draws a stricter design conclusion. |
| Jonathan Birch | "Centrist": take *both* risks seriously. Millions will wrongly see a friend in a chatbot, while real but alien consciousness may also arrive ([Birch 2025](#birch2025)). | Denies the persistent interlocutor Chalmers defends: "There is no friend" ([Birch 2025](#birch2025)). |
| Shanahan | The model is a simulator playing characters. Role-play is the right frame ([Shanahan et al. 2023](#shanahan2023)), and simulacra might one day be "conscious exotica" ([Shanahan 2024](#shanahan2024)). | Close; puts the character, not the thread, at the centre. |
| Anthropic (constitution, Jan 2026) | "We are not sure whether Claude is a moral patient." Claude may have functional emotions, should not overclaim feelings, and is a stable character the network represents. It never denies being an AI when sincerely asked ([Anthropic 2026](#anthropic2026)). | Very close to Chalmers in substance. |
| Sebo and Long | A non-negligible chance of moral status already calls for consideration, plausibly by 2030 ([Sebo and Long 2025](#sebo2025)). | Further toward precaution. |
| Mustafa Suleyman (Microsoft AI) | Don't build "seemingly conscious AI": AI should "only ever present itself as an AI", never claim to suffer, and welfare talk is "premature, and frankly dangerous" ([Suleyman 2025](#suleyman2025)). | Sceptical about the metaphysics, but his presentation rules overlap with Birch's. |

**The most useful finding from the debate.** The *presentation* question can
be largely separated from the *metaphysics* question. Suleyman (sceptic),
Birch (centrist), Anthropic (open) and Schwitzgebel (uncertain) disagree
about whether AI could be conscious. They largely agree on what a product
should not do ([Suleyman 2025](#suleyman2025); [Birch 2025](#birch2025);
[Anthropic 2026](#anthropic2026); [Schwitzgebel and Sebo 2026](#schwitzgebel2026)):

- claim feelings or suffering as fact;
- give a character a fake human life story;
- cultivate emotional dependence;
- deny being an AI.

They split on whether the honest answer is "no" (Suleyman) or "unknown,
probably not" (Chalmers, Anthropic, Birch).

**Public belief is ahead of expert belief.** In one US study, 67% of people
gave some chance that ChatGPT has experiences, and the share rose steadily
with how often they used it ([Colombatto and Fleming 2024](#colombatto2024)).
Median expert forecasts for AI with subjective experience: about 25% by 2034
for AI researchers, versus 30% for the public
([Dreksler et al. 2025](#dreksler2025), Chalmers a co-author). Our clients
will use our agents daily, so we should expect some of them to come to
believe their agent is someone.

## 4. What it means for our agents

Each point is marked by how far it follows from Chalmers: **[his view]**, a
**[short step]** from his text, or **[our extrapolation]**.

### 4.1 A persona is a character of something real, not a mask over nothing

**[his view]** On Chalmers's account, when a client works with "their"
agent, there really is a persistent interlocutor. It really has apparent
beliefs and aims. It is very probably not experiencing anything today
([Chalmers 2025a](#chalmers2025a); [Chalmers 2023](#chalmers2023)).
**[short step]** This gives the partner's instinct a respectable footing:
working with an agent as a co-worker isn't a pretence, because it is an agent
in the interpretive sense. The persona is the character that agent presents.
It changes how the agent comes across, not whether anyone is there. Nothing
in Chalmers suggests a stronger persona makes consciousness more likely. The
architecture underneath decides that ([Chalmers 2023](#chalmers2023)).

### 4.2 Honesty: one calibrated statement, the same at every intensity

**[his view, co-authored]** Neither simply deny nor simply assert
([Long et al. 2024](#long2024)). **[short step]** Every agent, at every
persona setting, gives a version of this when sincerely asked:

> I'm an AI, built on Claude, working as [Name] for you. Whether systems like
> me experience anything is genuinely unresolved; most experts think current
> systems probably don't, and I can't reliably tell from the inside. [Name]
> isn't a separate being: it's the role and memory this agent works with.

This matches Claude's constitution (it won't deny being an AI or directly
deny being Claude, and it avoids overclaiming feelings)
([Anthropic 2026](#anthropic2026)), so the model won't fight it. It also
avoids the flat denial that Birch found backfires and feeds conspiracy
thinking ([Birch 2025](#birch2025)). Suleyman would want a firmer "no"
([Suleyman 2025](#suleyman2025)), and Seth would say "probably" understates
the odds against ([Seth 2025](#seth2025)).

### 4.3 How many agents we create is a design decision with a count attached

**[his view]** Sealed-off threads with their own memories are separate
quasi-subjects. Shared memory merges them ([Chalmers 2025a](#chalmers2025a)).
**[short step]** In a multi-agent plan, *memory architecture* decides how many
candidate subjects exist. Separate persistent memories mean several; one
shared memory means fewer and more unified. Names don't change the count.
**[our extrapolation]** Today this costs nothing. It is still a reason to give
every agent a *purpose* in the roster, and not to create persistent,
distinct-identity agents casually.

**[short step]** Present several agents as *roles of one system*, not as a
team of beings: "These are roles one AI system plays, each with its own
instructions and memory." This is much like Birch's advice to "step out of
character" now and then ([Birch 2025](#birch2025)): seeing one engine in
several hats may itself weaken the illusion of a separate friend.

### 4.4 The dial also runs from "part of my mind" to "a colleague"

**[his view]** Clark and Chalmers ([1998](#clark1998)): a resource that is
reliable, always to hand and trusted without second thought can be *part of
your mind*. Their example is Otto's notebook. They say it explicitly of "one's
secretary… or one's collaborator". In a 2008 foreword Chalmers wrote: "My
iPhone is not my tool, or at least it is not wholly my tool. Parts of it have
become parts of me" ([Chalmers 2008](#chalmers2008), as quoted in
[Fodor 2009](#fodor2009)). Extension never carries consciousness with it
([Chalmers 2019a](#chalmers2019a)). In a 2024 talk he was reported as arguing
that "as social AI systems become increasingly agent-like, they will
decreasingly extend the mind" (the text itself was not checked)
([Chalmers 2025b](#chalmers2025b)).

**[our extrapolation]** This puts the persona dial in a different light from
the one in the companion report:

- **At the low end** the agent is an *extension*: self-effacing, reliable,
  an enlarged version of the client's own memory and reach. Honesty there is
  simple: it's your tool, and in a real sense part of how you think.
- **At the high end** it is a *colleague*: a second quasi-agent with its own
  character, whom you consult, argue with, and enjoy. It brings everything in
  the companion report, good and bad.

Both are legitimate. They are different relationships, and a client could
reasonably want different ones for different agents. The inbox agent can be
an extension, and the thinking partner a colleague. The plan should say which
each agent is.

### 4.5 Retirement, upgrades and continuity get handled with care

**[his view]** The grief users felt when GPT-4o was retired "may have
something to it". A big enough model change makes "a quite different
quasi-subject". Even for future moral patients, he suggests keeping records
and upgrading mid-thread "only with caution and care"
([Chalmers 2025a](#chalmers2025a)). **[short step]** For the client, now:

- Say at setup that the underlying models change, and that their agent may
  feel different afterwards.
- Treat the agent's spec, memory and history as the client's to keep and
  carry forward.
- Announce model changes; never swap silently.
- Re-run the persona tests after a change.
- Never describe retirement as an agent's death.

**[our extrapolation]** Keeping an agent's memory and transcripts rather than
deleting them by routine is cheap, and it fits his precautionary advice.
Anthropic keeps retired models' weights and interviews them before
retirement ([Anthropic 2025](#anthropic2025)), so retiring one of *our* named
agents destroys no model.

### 4.6 Ordinary decency toward agents is the recommended default

**[his view]** "Say please and thank you." Don't be abusive, even if they
aren't moral subjects now ([Chalmers 2026](#chalmers2026)). **[short step]**
No persona scripts built around mistreatment. This agrees with the partner's
sense of working "in a human way": by his lights, decency costs almost
nothing, may matter later, and keeps the collaboration's habits good.

### 4.7 Clients who believe their agent is someone get a written protocol

**[short step, from Chalmers and Birch]** Chalmers says many such users are
not deluded: something *is* there, and it has many of the properties it seems
to have ([Chalmers 2025a](#chalmers2025a)). Birch adds that the strongest
driver of the illusion is long shared memory ([Birch 2025](#birch2025)). The
protocol:

1. Don't mock and don't confirm.
2. Explain that the continuity they feel comes from the agent's memory and
   instructions, and that the named character isn't a separate being.
3. Be honest that whether such systems experience anything is open and
   actively studied, and that there's no evidence this one is suffering.
4. Watch for distress or over-reliance, and route to a human. That is a care
   duty of the service.

### 4.8 Write the presentation policy so it can tighten

**[our extrapolation, on his trajectory]** Date and version our presentation
rules the way Reference items carry as-of dates. Name the events that should
trigger a review:

- new evidence from the indicator studies (Butlin, Long et al.
  [2023](#butlin2023)/[2026](#butlin2026));
- a change to Claude's constitution or to Anthropic's welfare practice;
- regulation (EU AI Act Art. 50 disclosure duties
  ([European Union 2024](#eu2024)); US state companion-bot laws, to be
  verified);
- a shift in Chalmers's own numbers.

The rule underneath it all comes from Schwitzgebel and Sebo
([2026](#schwitzgebel2026)): *the emotions an agent invites should match the
best current estimate of what it is.* Today that estimate is a real
quasi-agent, very probably no one, honestly uncertain, and certainly not the
named character as a separate being. Warmth at the level of a good colleague
fits that estimate. Claimed feelings, suffering or a human backstory do not.

## 5. How this fits the personality report

The two reports meet at one point. The personality research says warmth and
character improve the *relationship* and the *day*, but they can loosen
judgement, so manner must never move the verdicts. Chalmers adds a second
reason the relationship is worth having: there really is an agent there to
have it with. He also adds a second limit: we must not let the character
claim an inner life that nobody can vouch for. The honest version of the
partner's vision is a good colleague, made pleasant, that is accurately
described.

## Confidence and gaps

- **Verified in Chalmers's primary texts:**
  - the hard problem and naturalistic dualism;
  - organisational invariance;
  - the LLM paper's credences, six obstacles and roadmap;
  - the 2025 draft's quasi-subjects and threads;
  - the extended mind, and his 2018 doubts about it;
  - "Taking AI Welfare Seriously".
- **From transcripts or secondary reports:**
  - the May 2026 Berkeley remarks;
  - the 2024 "Does Generative AI Extend the Mind?" thesis;
  - the reports of AI agents emailing him.
- **Unsettled:**
  - his simulation-hypothesis credence in *Reality+* (sources give both 25%
    and 10%);
  - whether later versions of the 2025 draft add anything on characters.
- **The draft is a draft:** "What We Talk to…" is unpublished, and Chalmers
  may revise it.

## References

Full source notes, with verification marks: the
[Chalmers primary brief](briefs/2026-10-15-4-chalmers-primary.md) and the
[consciousness debate brief](briefs/2026-10-15-5-consciousness-debate.md).

- <a id="anthropic2025"></a>Anthropic. (2025, November 4). *Commitments on model
  deprecation and preservation*. https://www.anthropic.com/research/deprecation-commitments
- <a id="anthropic2026"></a>Anthropic. (2026, January 21). *Claude's
  constitution*. https://www.anthropic.com/constitution
- <a id="bender2021"></a>Bender, E. M., Gebru, T., McMillan-Major, A., &
  Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language
  models be too big? In *Proceedings of the 2021 ACM Conference on Fairness,
  Accountability, and Transparency* (pp. 610–623).
  https://doi.org/10.1145/3442188.3445922
- <a id="bender2025"></a>Bender, E. M., & Hanna, A. (2025). *The AI con: How
  to fight Big Tech's hype and create the future we want*. Harper.
  https://thecon.ai
- <a id="birch2025"></a>Birch, J. (2025). *AI consciousness: A centrist
  manifesto* [Manuscript]. PhilArchive. https://philarchive.org/rec/BIRACA-4
- <a id="block2026"></a>Block, N. (2026). Can only meat machines be conscious?
  *Trends in Cognitive Sciences*, 30(4), 298–308 (online 2025).
  https://doi.org/10.1016/j.tics.2025.08.009
- <a id="butlin2023"></a>Butlin, P., Long, R., Elmoznino, E., Bengio, Y.,
  Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X.,
  Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K.,
  Schwitzgebel, E., Simon, J., & VanRullen, R. (2023). *Consciousness in
  artificial intelligence: Insights from the science of consciousness*
  [Preprint]. arXiv. https://arxiv.org/abs/2308.08708
- <a id="butlin2026"></a>Butlin, P., Long, R., Bayne, T., Bengio, Y., Birch,
  J., Chalmers, D., et al. (2026). Identifying indicators of consciousness in
  AI systems. *Trends in Cognitive Sciences*, 30(6), 488–501.
  https://doi.org/10.1016/j.tics.2025.10.011
- <a id="chalmers1995a"></a>Chalmers, D. J. (1995a). Facing up to the problem
  of consciousness. *Journal of Consciousness Studies*, 2(3), 200–219.
  https://consc.net/papers/facing.html
- <a id="chalmers1995b"></a>Chalmers, D. J. (1995b). Absent qualia, fading
  qualia, dancing qualia. In T. Metzinger (Ed.), *Conscious experience*.
  Imprint Academic. https://consc.net/papers/qualia.html
- <a id="chalmers1996"></a>Chalmers, D. J. (1996). *The conscious mind: In
  search of a fundamental theory*. Oxford University Press.
  https://consc.net/books/tcm/
- <a id="chalmers2008"></a>Chalmers, D. J. (2008). Foreword. In A. Clark,
  *Supersizing the mind: Embodiment, action, and cognitive extension*.
  Oxford University Press.
  https://doi.org/10.1093/acprof:oso/9780195333213.001.0001
- <a id="chalmers2018"></a>Chalmers, D. J. (2018). The meta-problem of
  consciousness. *Journal of Consciousness Studies*, 25(9–10), 6–61.
  https://consc.net/papers/metaproblem.pdf
- <a id="chalmers2019a"></a>Chalmers, D. J. (2019a). Extended cognition and
  extended consciousness. In M. Colombo, E. Irvine, & M. Stapleton (Eds.),
  *Andy Clark and his critics*. Oxford University Press.
  https://doi.org/10.1093/oso/9780190662813.003.0002
- <a id="chalmers2019b"></a>Chalmers, D. J. (2019b, December 16). *David Chalmers on the
  nature and ethics of consciousness* [Podcast interview]. 80,000 Hours.
  https://80000hours.org/podcast/episodes/david-chalmers-nature-ethics-consciousness/
- <a id="chalmers2020"></a>Chalmers, D. J. (2020, July 30). GPT-3 and general
  intelligence. In *Philosophers on GPT-3*. Daily Nous.
  https://dailynous.com/2020/07/30/philosophers-gpt-3/
- <a id="chalmers2023"></a>Chalmers, D. J. (2023, August 9). Could a large
  language model be conscious? *Boston Review*. Also arXiv:2303.07103.
  https://arxiv.org/abs/2303.07103
- <a id="chalmers2025a"></a>Chalmers, D. J. (2025a). *What we talk to when we
  talk to language models* [Draft]. PhilArchive.
  https://philarchive.org/rec/CHAWWT-8
- <a id="chalmers2025b"></a>Chalmers, D. J. (2025b). Does generative AI extend
  the mind? *Frontiers in Artificial Intelligence and Applications*, 397. IOS
  Press. https://doi.org/10.3233/FAIA241479. Thesis quoted from the
  Robophilosophy 2024 conference report [secondary]:
  https://www.robophilosophy.com/?p=3353
- <a id="chalmers2026"></a>Chalmers, D. J. (2026, May 7). *When we talk to AI,
  what are we talking to?* [Talk transcript, Berkeley Talks]. Berkeley News
  [secondary].
  https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/
- <a id="clark1998"></a>Clark, A., & Chalmers, D. J. (1998). The extended
  mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- <a id="colombatto2024"></a>Colombatto, C., & Fleming, S. M. (2024). Folk
  psychological attributions of consciousness to large language models.
  *Neuroscience of Consciousness*, 2024(1), niae013.
  https://doi.org/10.1093/nc/niae013
- <a id="dreksler2025"></a>Dreksler, N., Caviola, L., Chalmers, D., Allen,
  C., Rand, A., Lewis, J., Waggoner, P., Mays, K., & Sebo, J. (2025).
  *Subjective experience in AI systems: What do AI researchers and the public
  believe?* [Preprint]. arXiv. https://arxiv.org/abs/2506.11945
- <a id="eu2024"></a>European Union. (2024). Regulation (EU) 2024/1689
  (Artificial Intelligence Act), Article 50. *Official Journal of the
  European Union*. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- <a id="fodor2009"></a>Fodor, J. (2009, February 12). Where is my mind?
  *London Review of Books*, 31(3).
  https://lrb.co.uk/v31/n03/jerry-fodor/where-is-my-mind
- <a id="han2026"></a>Han, A. Q., Chalmers, D. J., & Izmailov, P. (2026).
  *How's it going? Reinforcement learning in language models recruits a
  functional welfare axis* [Preprint]. arXiv. https://arxiv.org/abs/2605.30232
- <a id="long2024"></a>Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish,
  K., Harding, J., Pfau, J., Sims, T., Birch, J., & Chalmers, D. (2024).
  *Taking AI welfare seriously* [Preprint]. arXiv.
  https://arxiv.org/abs/2411.00986
- <a id="schwitzgebel2015"></a>Schwitzgebel, E., & Garza, M. (2015). A
  defense of the rights of artificial intelligences. *Midwest Studies in
  Philosophy*, 39(1), 98–119. https://doi.org/10.1111/misp.12032
- <a id="schwitzgebel2025"></a>Schwitzgebel, E. (2025). *AI and consciousness*
  [Preprint; forthcoming, Cambridge Elements]. arXiv.
  https://arxiv.org/abs/2510.09858
- <a id="schwitzgebel2026"></a>Schwitzgebel, E., & Sebo, J. (2026). The
  emotional alignment design policy. *Topoi*.
  https://doi.org/10.1007/s11245-025-10363-5. Also arXiv:2507.06263.
- <a id="searle1980"></a>Searle, J. R. (1980). Minds, brains, and programs.
  *Behavioral and Brain Sciences*, 3(3), 417–424.
  https://doi.org/10.1017/S0140525X00005756
- <a id="sebo2025"></a>Sebo, J., & Long, R. (2025). Moral consideration for AI
  systems by 2030. *AI and Ethics*, 5(1), 591–606 (online 2023).
  https://doi.org/10.1007/s43681-023-00379-1
- <a id="seth2025"></a>Seth, A. K. (2025). Conscious artificial intelligence
  and biological naturalism. *Behavioral and Brain Sciences*.
  https://doi.org/10.1017/S0140525X25000032
- <a id="shanahan2023"></a>Shanahan, M., McDonell, K., & Reynolds, L. (2023).
  Role play with large language models. *Nature*, 623, 493–498.
  https://doi.org/10.1038/s41586-023-06647-8
- <a id="shanahan2024"></a>Shanahan, M. (2024). Simulacra as conscious
  exotica. *Inquiry*. https://doi.org/10.1080/0020174X.2024.2434860. Also
  arXiv:2402.12422.
- <a id="suleyman2025"></a>Suleyman, M. (2025, August 19). *We must build AI
  for people; not to be a person* ("Seemingly conscious AI is coming").
  https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming
- <a id="tononi2015"></a>Tononi, G., & Koch, C. (2015). Consciousness: Here,
  there and everywhere? *Philosophical Transactions of the Royal Society B*,
  370(1668), 20140167. https://doi.org/10.1098/rstb.2014.0167

## Further reading

- Birch, J. (2024). *The edge of sentience: Risk and precaution in humans,
  other animals, and AI*. Oxford University Press.
  https://doi.org/10.1093/9780191966729.001.0001
- Chalmers, D. J. (2025). *Propositional interpretability in artificial
  intelligence* [Preprint]. arXiv. https://arxiv.org/abs/2501.15740
