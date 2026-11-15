# Does it learn? Gopnik, the pattern-machine view, and learning profiles

_Research synthesis, 2026-10-16. Assembled from two working documents written 2026-10-15/16:
the notes "Do LLMs Learn and Think? Gopnik vs. the Pattern-Machine View" and the explainer
"Does it learn? How your assistant learns, and where it can't yet". This file keeps their
research content. The explainer's sections about a particular assistant setup were not
brought in._

> **Status: cite-checked 2026-10-16** ([report](cite-check/2026-10-16-learning-and-gopnik.md)).
> No citation was found wrong or invented. Claims the automated check could not reach were then
> checked by hand against full texts: the Gopnik figures and blicket result (her paper, via
> Europe PMC), Tolman's latent learning, and H.M.'s mirror drawing (Squire 2009). That pass
> corrected one overstatement (how the 2023 models did on the tool task) and replaced a dead
> link. The Hayes interview could not be fetched and is unchecked.
>
> **Disclosure carried from the source:** this analysis was written by Claude, an interested
> party.

## The question

The question came from Alison Gopnik's May 2026 interview with Chris Hayes
([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f)).
She holds the common view that large models don't learn or think the way humans do. Bart's view:
humans are pattern machines too. We learn by discovering and internalizing patterns, and we think
by recognizing, connecting and extrapolating them. So what is supposed to be different?

## Position, in brief

- **What learns is the whole system,** not the bare model: the model plus memory, notes and
  regular upgrades.
- **By any functional definition, a model plus memory learns.** The remaining differences are
  mechanical, and they matter mainly for skills, not for facts and preferences.
- **Gopnik's real distinction is between passing knowledge along and discovering it,** not
  between learning and not learning. Her surviving claim is narrow and empirical, and testable.
- **The useful question is not "does it learn?" but "what is its learning profile?"** Every
  learner has one.

## What "learning" means

In cognitive science, learning is a lasting change in what a system knows, caused by experience,
that changes what it can do or predict later. Each part of that rules something out:

- **Caused by experience,** not by growing up, tiredness or medication.
- **Lasting,** not a passing state like being warmed up.
- **A change in what the system knows,** not only in what it does. In Edward Tolman's classic
  maze studies, rats that explored without any reward learned the layout and only showed it once
  food appeared ([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)).
- **Changes what it can do later,** ideally in situations it hasn't seen before.

The definition says nothing about brains, biology or how the change is stored.

## What Alison Gopnik argues

Gopnik's point isn't that humans are magic. It's that children and language models get their
knowledge in different ways, and that this shows up in what each can do. In the Hayes interview
she put it as a two-year-old routinely outsmarting the best AI models. Her published work makes
the case more carefully
([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)).

1. **Models are cultural technologies.** She compares them to writing, print, libraries and the
   internet. They gather what people have already written and pass it on very efficiently. That
   makes them superb imitators.
2. **Children are truth-seekers.** They experiment on the world, like scientists. In her
   "blicket detector" studies, 4-year-olds work out which blocks make a new machine light up from
   a handful of tries. The language models tested on the same evidence did not.
3. **Imitation isn't innovation.** In her group's tool-innovation scenarios (the paper's example:
   draw a circle with no compass, choosing between a ruler, a round-bottomed teapot and a stove),
   children aged 3 to 7 chose the functional object 85% of the time, averaged across scenarios.
   The 2023 models did worse, drawn toward the object most associated with the usual tool. GPT-4
   did best at 76%; the Claude version then tested scored 58%; two of the five models tested fell below half. On
   the matching imitation task ("which goes best with a compass?"), the models did well.
4. **Children are curious and self-driven.** They choose what to explore. A model trained on text
   never chooses its own experience.

She says other AI designs that act on the world come closer to how children learn. Her argument
is about models trained on text alone, not about machines in general.

## Where each side overreaches

**Where Gopnik's side overreaches.**

- Her own theory of children is statistical. She models them as Bayesian learners who weigh
  evidence: pattern learning over interventions rather than over text.
- Most human learning is imitation too. Few of us invent anything; we inherit language, tools
  and ideas, the same cultural transmission she credits to models.
- Comparing amounts of data is unfair. Babies start with priors that evolution spent hundreds of
  millions of years building, a kind of pretraining.
- Her tests are aging. They used 2022–23 models. Current models write code, run it, see what
  happens and try again, which is a crude form of experiment.
- "It doesn't learn" usually means the bare model. Real assistants come with memory, and that
  changes the answer.

**Where the pattern-machine side overreaches.**

- "Pattern machine" is too broad to prove anything. A thermostat, a spam filter, a dog and a
  physicist all qualify. The real questions are which patterns, learned from what, inside what
  loop.
- The loop is different. A person predicts, acts, lives with the result and adjusts, all day,
  with something at stake. A model was trained and then fixed in place. Similar outputs can come
  from very different processes.
- Gopnik's narrower claim stands: a learner that experiments on the world fails differently from
  one that reads about it.

What survives both critiques is a functional question. Can it take in experience and do better
afterwards? For a well-set-up assistant, yes.

| Dimension | Human child | Current LLM |
| --- | --- | --- |
| How knowledge gets in | Experiments on the world, chosen by the learner | A passive record of text others wrote |
| Data needed | A handful of examples, on top of evolved priors | More text than thousands of lifetimes |
| Learning after training | Never stops | Frozen; only temporary in-context learning |
| Stakes for the learner | Hunger, pain, embarrassment, goals | None |
| Strongest at | Discovery and causal insight | Retrieving and recombining what's known |

## Why what it's made of shouldn't decide the question

Whether something learns should be judged by what it does, not by what it's made of.
Philosophers call the opposite assumption substrate chauvinism; Carl Sagan's version was "carbon
chauvinism", the belief that a mind must be built from the same material as ours to count. The
view held here, functionalism, says a memory is a memory whether it lives in brain cells, in a
notebook or in a computer file.

- **Words aren't the essence for either of us.** Nothing in a brain is stored as words; it's
  stored in the connections between neurons. For today's AI systems, text plays the same role: a
  convenient storage format, not the learning itself.
- **Other senses count too.** Current models learn from images, sound and video, and robots
  learn grasping and balance from camera and sensor data.
- **The fair test.** Differences in material sometimes matter: a system with no lasting memory
  really can't learn across conversations. So a difference should count only when you can show it
  changes what the system can do. Most claims that AI "doesn't really learn" fail that test.

## The refined position

1. **Definition.** As above: a lasting change in a system's internal knowledge, caused by
   experience, that changes what it can do or predict later.
2. **The nickname test.** If a user asks to be called by a nickname and the assistant saves it
   and uses it from then on, all four criteria are met. "It's only a notebook" doesn't hold up: by
   Clark and Chalmers' extended-mind argument (Otto's notebook), a reliably consulted note
   functions as memory
   ([Clark & Chalmers 1998](https://en.wikipedia.org/wiki/Extended_mind_thesis)).
3. **Rules over impulses.** People hold learned rules that override unchanged urges (inhibitory
   control). That is the same structure as a fixed model following a note. What differs is that a
   person's rule becomes automatic with repetition (proceduralization, in John Anderson's account
   of skill acquisition, [Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)); a note
   never does. For a model, rereading costs almost nothing, so this matters less than it would for
   a person.
4. **Integration and "dreaming".** A nightly job that reorganizes and links memory files mirrors
   half of sleep consolidation. In complementary learning systems theory, the hippocampus (fast,
   like notes) replays to the neocortex (slow, like weights), which changes
   ([McClelland, McNaughton & O'Reilly 1995](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf)).
   The job improves the notebook, but nothing transfers into the weights. Between upgrades the
   cortex is frozen; each model upgrade acts as a kind of generational dreaming that updates it.
5. **New model versions.** Each release does learn, but it learns as a lineage, not as an
   individual. A new version is trained on a newer, larger body of human experience and can be
   much better, but a user's own notes aren't trained into it. That is closer to a new generation
   inheriting improved culture than to one person growing. How much each version builds on the
   previous one's weights is not published (unconfirmed).

**Working hypothesis:** for practical purposes these models learn. A well-built system (model
plus memory, skills and notes it writes itself) also improves with practice, as Bart has observed
with new software and email tone. The one structural difference left is that its learning must
pass through something written; a person's can also go straight into the brain. For knowledge
work, where nearly everything can be written, that difference is small.

## Learning profiles

The clearest human example is Henry Molaison, known for decades as patient H.M. After brain
surgery in 1953 he could no longer form new memories of facts or events. Yet when Brenda Milner
had him trace a star seen only in a mirror, he learned the skill and kept it across three days,
with no memory of ever having done the task
([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023), describing Milner 1962). No one concluded he
couldn't learn. They concluded memory has separate systems. A memory-equipped assistant has
roughly the opposite profile.

| Kind of learning | How a person learns it | How an assistant learns it | Gap |
| --- | --- | --- | --- |
| Facts and preferences ("call me Bart") | Remembered after being told once or twice | Written to memory and reread every time | Small |
| People, context, ongoing work | Builds up over weeks | Memory files, project notes, past chats | Small |
| Rules over impulses ("don't reply while angry") | Reminded until it becomes habit | Instructions it follows every time | Small; it never becomes habit, but rereading costs it nothing |
| Voice and tone | Absorbed from feedback and replies | A voice profile, updated when drafts are corrected | Small |
| Connecting what it knows | Partly automatic, especially in sleep | Only when items are read together or a nightly job links them | Small with a nightly tidy-up |
| Skills from practice | Practice slowly becomes habit | Records what worked and uses it next time | Small; the lesson must be put into words |
| Know-how that's hard to put into words | Goes straight into the body and brain | Learned from images, sound and video in training; day-to-day notes are mostly text | Moderate today, narrowing as memory goes beyond text |
| Big leaps in ability | Years of growing up | Each model upgrade (generational dreaming) | Small; upgrades draw on everyone's experience, not only the user's |

The explainer also carried a diagram, "How your assistant learns · notes, nightly tidy-up,
new versions". It lives in the working document and was not brought in.

## How Gopnik might answer

On whether these systems learn, the pushback holds. But Gopnik's real distinction is between
passing knowledge along and discovering it. Her strongest replies:

1. **"You changed the subject from discovering to remembering."** Most of the examples are
   learning from people: a nickname, a writing voice, replies to email. Memory makes the assistant
   a better personal cultural technology; Otto's notebook helps him remember, not discover.
2. **"Your evidence is anecdotal."** Her paper treats a striking conversation as the start of a
   study, not a result. An assistant learning new software quickly may be drawing on thousands of
   similar programs it already knows.
3. **"Who is doing the truth-seeking?"** Often the human notices the mistake and supplies the
   correction. Model upgrades compress human-produced data, which is cultural transmission at
   scale.
4. **"Who chooses what to explore?"** Children pick their own experiments. An assistant mostly
   works on goals it's given.

**What survives, and how narrow it is.** Her defensible claim becomes: systems that learn mostly
from human-produced data, without exploring the world on their own, are weaker at discovering new
cause and effect. Two things narrow even that:

- **Assistants now explore.** They search the web, run code and check results. Writing the
  explainer, the assistant fetched her paper and corrected its own earlier account of her numbers.
  That is evidence-seeking, the thing she credits to children. Her paper itself says AI that acts
  on the world comes closer to how children learn.
- **Imagining is exploring too.** Her own research links children's pretend play to reasoning
  about what could happen
  ([Wente, Gopnik et al. 2022](https://sites.brown.edu/cocodevlab/files/2023/03/Causal-learning-counterfactual-reasoningand-pretend-play.pdf)).
  An assistant inventing options is doing something similar. What turns it into learning is a
  loop: the result comes back from outside and is kept.

Her remaining claim is an empirical one about how well current systems discover new cause and
effect from their own experiments. That can be tested. The explainer commits to "setting up a
version of her test"; the pilot designed for it is
`pilots/gopnik-memory-overhypothesis-2026-10-16/`, pre-registered here before it runs.

## Open questions

- **Will the model itself update as it works?** Letting a model update its own skills as it
  works, without forgetting what it already knows, is an active research problem. If it could,
  lessons wouldn't need to be written down, though the result for a user might look much the same.
- **How would current models do on Gopnik's tests?** Newer models have since been tested on close
  variants of both tasks. On 20 freshly written tool-innovation items, GPT-4o scored 81.3%
  against humans' 88.2%, and with step-by-step reasoning was not significantly different from
  humans ([Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)). On blicket-style
  tasks where models explore for themselves, they infer "any one will do" rules well and "needs
  two" rules poorly, a bias that looks like adults' rather than children's
  ([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)); gpt-5 approaches human accuracy but
  explores less efficiently and keeps that gap
  ([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)). No study re-ran her
  original items, which are unpublished. _(Corrected 2026-10-16: this bullet first said no newer
  results had been found.)_
- **Can written notes carry the rule from one task to the next?** Not tested by any of the above.
  The pilot designed to find out (`pilots/gopnik-memory-overhypothesis-2026-10-16/`) stopped at
  its baseline on 2026-10-17, by its pre-registered rule. Without any memory, Claude Opus 5.5,
  GPT-6.1 Sol and Grok 4.7 solved all 240 of their "needs two" machines, so there was no room for
  notes to help ([result](../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md)).
  That task named both possible rules in the prompt, which may be why no disjunctive bias showed.
  The notes question needs a harder task.
- **Does acting on the world matter more than learning continuously?** Gopnik's view suggests
  that exploring is what gives children their edge.
- **Is a lineage of models one learner or many?** Whether a new version is the same assistant
  grown up or a new one is partly a matter of how you choose to see it.
- **Does "thinking" need experience or stakes, or is it a kind of computation?** Where the
  definitions split.
- **Would continual learning close the gap, or is embodiment the real difference?**

## References

- [Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369). John R. Anderson, "Acquisition of
  Cognitive Skill," _Psychological Review_ 89.
- [Clark & Chalmers 1998](https://en.wikipedia.org/wiki/Extended_mind_thesis). Andy Clark and
  David Chalmers, "The Extended Mind," _Analysis_ 58. Linked to an overview; the paper is
  [doi:10.1093/analys/58.1.7](https://doi.org/10.1093/analys/58.1.7).
- [Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606). "Reasoning about
  Affordances: Causal and Compositional Reasoning in LLMs." arXiv:2502.16606.
- [GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614). Anthony GX-Chen, Dongyan Lin, Mandana
  Samiei, Doina Precup, Blake A. Richards, "Language Agents Mirror Human Causal Reasoning Biases.
  How Can We Help Them Think Like Scientists?" arXiv:2505.09614 (COLM 2025).
- [Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f).
  "The AI End Game: Two-Year-Olds vs. AI with Alison Gopnik," _Why Is This Happening?_, 19 May
  2026. The Pocket Casts page refuses automated fetches, so this episode was not checked by
  `/cite-check`; the Gopnik claims in this file rest on her paper, not the interview.
- [McClelland, McNaughton & O'Reilly 1995](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf).
  "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex," _Psychological
  Review_ 102. [doi:10.1037/0033-295X.102.3.419](https://doi.org/10.1037/0033-295X.102.3.419).
- [Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464). Mandana Samiei, Eunice
  Yiu, Anthony GX-Chen, Dongyan Lin, Jocelyn Shen et al., "Human Adults and LLMs as Scientists:
  Who Benefits from Active Exploration?" arXiv:2606.06464 (CogSci 2026).
- [Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023). Larry R. Squire, "The Legacy of
  Patient H.M. for Neuroscience," _Neuron_ 61. Describes Milner's 1962 mirror-drawing results and
  the 1953 surgery.
- [Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm). Edward C. Tolman,
  "Cognitive Maps in Rats and Men," _Psychological Review_ 55.
- [Wente, Gopnik et al. 2022](https://sites.brown.edu/cocodevlab/files/2023/03/Causal-learning-counterfactual-reasoningand-pretend-play.pdf).
  "Causal learning, counterfactual reasoning and pretend play: a cross-cultural comparison."
  Builds on Buchsbaum, Bridgers, Weisberg & Gopnik 2012, "The power of possibility,"
  _Philosophical Transactions of the Royal Society B_ 367,
  [doi:10.1098/rstb.2012.0122](https://doi.org/10.1098/rstb.2012.0122).
- [Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/). "Transmission
  Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and
  Language-and-Vision Models Cannot (Yet)," _Perspectives on Psychological Science_ 19.
