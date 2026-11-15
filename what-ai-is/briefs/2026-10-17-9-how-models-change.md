# How a model moves from version to version, and whether the line of models learns (as of 2026-10-17)

_Cite-checked 2026-10-17 ([report](../cite-check/2026-10-17-the-how-models-change-brief.md))._

_Research brief for position piece 02 (`positions/02-it-learns.md`), and relevant to piece 01's
"fix it once and it's fixed for everyone." Gathered 2026-10-17 by direct retrieval of papers and
vendor pages. Marks: **[abstract]** checked against the abstract; **[text]** checked against the
full text, quoted; **[record]** existence confirmed by a bibliographic record, content from the
standard description; **[page]** a vendor or extension web page, quoted; **[inference]** my
reasoning from the sources, not a finding._

## The questions under test

Bart, 2026-10-17, after the panel on piece 02 objected to the second-grader analogy (a new
release is not the same learner grown older):

1. What does moving from one model version to the next actually involve, and what training goes
   with it?
2. Is the objection about form again? His position is about the *results* of learning, not how
   it happens.
3. Why do engineers make the next version, and would they make it the same way if the previous
   version contributed nothing? Is that contribution a kind of reconstitution, like a
   caterpillar becoming a butterfly?
4. Are there biological examples closer to how models change than a child moving up a grade:
   a hive that nearly dies and is re-established, for instance?

## Bottom line

- **A model is made in two broad stages:** pretraining (predicting the next word across a huge
  corpus) and post-training (worked examples, ratings from people or other models, and practice
  on checkable tasks). Once released, its weights don't change.
- **Versions relate in two ways, and vendors rarely say which.** Some versions are new pretraining
  runs, with a new corpus and often a new design. Others are built on top of an existing model:
  DeepSeek-R1 was trained "on top of DeepSeek-V3-Base."
- **The earlier version shapes the next through at least four channels:** people's conversations
  and ratings (where policy and settings allow), the earlier model writing or filtering training
  data, the earlier model grading or teaching the new one, and what engineers learned from its
  failures. Remove those, and the next version comes out different.
- **So the line of models does carry experience forward,** mostly through people and data
  pipelines, while each major version is a new individual. "Lineage-level learning" is a real
  idea in biology: Watson & Szathmáry argue that evolution itself can learn, in the formal sense
  learning theory uses.
- **How much of a successor's improvement comes from its predecessor's experience is not public.**
  It may be small beside new data, more computing power and new methods.
- **The closest biological comparisons**, each fitting a different part of the picture:
  - **selective breeding** for major versions (a breeder chooses from the last generation's
    performance; the next generation is a new individual);
  - **cultural transmission**, such as songbirds learning song from adults, for the
    teacher channel;
  - **the honey bee colony** for "the line, not the individual";
  - **metamorphosis**, where a moth kept an aversion learned as a caterpillar, for a version built
    on top of the old one.

## Q1. How a model is made

**1.1 Pretraining.** The model learns to predict the next piece of text across a very large corpus.
DeepSeek-V3, for example, was pre-trained "on 14.8 trillion diverse and high-quality tokens,
followed by Supervised Fine-Tuning and Reinforcement Learning stages"
([DeepSeek-AI 2024](https://arxiv.org/abs/2412.19437)). **[abstract]** Llama 3 was pre-trained on
"about 15T multilingual tokens, compared to 1.8T tokens for Llama 2"
([Grattafiori et al. 2024](https://arxiv.org/abs/2407.21783), §1). **[text]**

**1.2 Post-training from human examples and ratings.** InstructGPT set the common pattern:
fine-tune on labelers' demonstrations, then on their rankings of model outputs, using
"reinforcement learning from human feedback"
([Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)). Its prompts included ones "submitted
through the OpenAI API": users' requests were part of the training material. **[abstract]**

**1.3 Post-training from AI feedback.** In Constitutional AI, a model critiques and revises its own
outputs against a list of principles, and "a model" judges which of two samples is better, with
no human labels for harm ([Bai et al. 2022](https://arxiv.org/abs/2212.08073)). RLAIF reached
results comparable to human feedback, "even when the AI labeler is the same size as the policy, or
even the exact same checkpoint as the initial policy"
([Lee et al. 2023](https://arxiv.org/abs/2309.00267)). **[abstract]**

**1.4 Practice on checkable tasks.** DeepSeek-R1 showed that reasoning "can be incentivized
through pure reinforcement learning," rewarded on tasks whose answers can be verified, such as
mathematics and coding ([DeepSeek-AI 2025](https://arxiv.org/abs/2501.12948)). **[abstract]**
Tülu 3 is an openly documented post-training recipe of this kind, built on Llama 3.1 base models
([Lambert et al. 2024](https://arxiv.org/abs/2411.15124)). **[abstract]** This is the nearest thing
to a model learning from its own attempts. It happens in training, not in use.

**1.5 After release.** The weights are fixed. What looks like learning in use (remembering a name)
comes from memory the product stores outside the model. **[inference]**, consistent with
piece 02.

## Q2. How one version relates to the next

**2.1 Built on top of an earlier model.** DeepSeek's paper says it plainly: "DeepSeek-R1 and
DeepSeek-R1-Zero are trained on top of DeepSeek-V3-Base and DeepSeek-R1 leverages non-reasoning
data from DeepSeek-V3 SFT data" ([DeepSeek-AI 2025](https://arxiv.org/abs/2501.12948), App. A.1).
**[text]** Here "the same model, changed by more training" is close to the truth.

**2.2 A new pretraining run.** Llama 3 used a corpus roughly eight times larger than Llama 2's
(1.1 above). The paper does not state how its weights were initialized. A new corpus of that size
is normally a new pretraining run, but that is **[inference]**, not something the paper says.

**2.3 Vendors rarely document it.** Of the cases checked, only DeepSeek states the relationship
outright. **[inference]** from the sources read; Anthropic, OpenAI and Google publish little on
how their successive models are initialized.

## Q3. Channels that carry a predecessor's experience forward

**3.1 People's conversations and ratings.**
- Anthropic, 2025-08-28: "We will train new models using data from Free, Pro, and Max accounts
  when this setting is on"; retention extends to five years for users who allow it; deleted
  conversations are not used; commercial and API use are excluded
  ([Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms)). **[page]**
- OpenAI says ChatGPT improves by further training on users' conversations unless they opt out,
  and that feedback a user gives may still be used after opting out
  ([OpenAI](https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/)).
  **[page, via search summary; the help-centre page returned 403 to direct fetch]**

**3.2 The earlier model filters or writes training data.** Llama 3's pretraining data was filtered
by a classifier built from Llama 2: "instruct Llama 2's chat model to determine if the documents
meets these requirements" ([Grattafiori et al. 2024](https://arxiv.org/abs/2407.21783), §3.1.1).
**[text]**

**3.3 The earlier or larger model teaches or grades.**
- Distillation compresses "the knowledge in an ensemble" into a single, smaller model
  ([Hinton, Vinyals & Dean 2015](https://arxiv.org/abs/1503.02531)). **[abstract]**
- Llama 3: "We use the flagship model to further improve the quality of those smaller models
  during post-training" (§1). **[text]**
- DeepSeek distilled R1 into smaller models (§1). **[text]**
- AI feedback (1.3) is the earlier model acting as grader.

**3.4 What engineers learned.** Failures, complaints and test results shape the next data mix and
training goals. **[inference]**; no source checked quantifies it.

**3.5 A limit on this channel.** Training indiscriminately on model-generated content "causes
irreversible defects" in later models, which the authors call model collapse
([Shumailov et al. 2024](https://doi.org/10.1038/s41586-024-07566-y)). **[abstract]** A
predecessor's output is not automatically good for its successor; it has to be selected.

## Q4. Does the line of models learn, by the functional definition?

**4.1 Piece 02's definition:** a lasting change, caused by experience, in what a system knows and
can do. Applied to the line of models: deployment experience (3.1–3.4) causes lasting changes in
what later models can do. At the level of the lineage, the definition is met. **[inference]**

**4.2 Lineage-level learning has a precedent.** Watson & Szathmáry argue that "new results
formally linking evolutionary processes to the principles of learning" show evolution can learn,
which "might explain how it produces such apparently intelligent designs"
([Watson & Szathmáry 2016](https://doi.org/10.1016/j.tree.2015.11.009)). **[abstract]** On that view a
species can be said to learn although no individual lives through the whole process.
**[inference]**; the abstract does not put it that way.

**4.3 What the objection gets right, on Bart's own terms.** "The results, not the process" can set
aside *how* the change happens (biological self-organization versus engineers retraining). It
cannot set aside *which system* changed, because the definition names one. The answer is to name
the unit: the assistant learns in use through its notes, and the line learns across versions.
Each meets the definition at its own level. **[inference]**

**4.4 The engineers' role.** Teachers train a child into third grade, and engineers train the next
version. On a results view, the mechanism is the "how." What matters is that experience, partly
the predecessor's own, caused a lasting change in capability. **[inference]** The open empirical
question is how large the predecessor's share is (Q3), and that is not public.

## Q5. Biological comparisons

**5.1 Selective breeding** (major versions). A breeder chooses which animals reproduce based on how
the last generation performed, and the next generation is a new individual. Darwin opened _On the
Origin of Species_ (1859) with "Variation under Domestication" for this reason. **[record]**
- Fit: a selector outside the line (breeder, engineers) uses the predecessor's performance; the
  successor is new.
- Misfit: breeding passes genes, while a model's successor inherits mainly through data and
  training choices.

**5.2 Cultural transmission** (the teacher channel).
- Songbirds "must hear the sounds of adults during a sensitive period" to learn their song
  ([Brainard & Doupe 2002](https://doi.org/10.1038/417351a)). **[abstract]**
- Chimpanzee communities show 39 behaviour patterns, including tool use, that are customary in
  some communities and absent in others where ecological explanations have been discounted
  ([Whiten et al. 1999](https://doi.org/10.1038/21415)). **[abstract]**
- Fit: each generation is new and learns from what the previous one produces, which is how
  distillation and model-written training data work.

**5.3 The honey bee colony** ("the line, not the individual").
- Workers live five to six weeks in the active season, and overwintering workers four to six months
  ([Bee Health, extension.org](https://bee-health.extension.org/how-long-do-worker-honey-bees-live)). **[page]**
- The colony outlasts its workers many times over, and when it swarms, a queen and thousands of
  workers re-establish elsewhere (Seeley 2010, _Honeybee Democracy_, Princeton University Press).
  **[record]**
- Fit: Bart's image of a hive re-established elsewhere. The colony is the unit that persists and
  adapts while individuals turn over.
- Misfit: a colony runs continuously; model versions are discrete.

**5.4 Metamorphosis** (a version built on an earlier model).
- Caterpillars of the tobacco hawkmoth trained to avoid an odour still avoided it as adult moths.
  The aversion was not explained by chemicals carried over from the larval environment
  ([Blackiston, Silva Casey & Weiss 2008](https://doi.org/10.1371/journal.pone.0001736)).
  **[abstract]**
- Fit: the body is largely rebuilt, yet learning survives, much as R1 kept what V3-Base had learned.
- Misfit: it is one organism throughout, which fits continued training better than a new
  pretraining run.

**Summary of fit [inference]:**

| Kind of change | Nearest biological comparison |
|---|---|
| New pretraining run, shaped by predecessor's performance | Selective breeding |
| Earlier model writes, filters, teaches or grades | Cultural transmission (song learning, chimpanzee traditions) |
| The product line persisting while individual versions turn over | The bee colony |
| New version built on an existing model | Metamorphosis |
| Child moving up a grade | Fits the assistant learning in use, not version to version |

## Bearing on piece 02

- **The second-grader analogy** fits two points: the frozen model got where it is by learning, and
  the assistant in use keeps learning through its notes. Read as release to release, it implies
  the same learner grows older, which is true only for versions built on an earlier model (2.1).
- **"The line learns" can be stated on the piece's own definition** (4.1–4.2), provided the piece
  names the unit and admits the predecessor's share of the improvement is unknown.
- **One of the comparisons above could carry the lineage point.** Selective breeding is the most
  accurate for major versions; the bee colony is the most vivid.

## Gaps and cautions

- **Vendors' practice for their own successive models is largely undisclosed.** That includes
  Anthropic's for the Claude models, and therefore the model that drafted this brief.
- **The share of improvement due to predecessor experience is unknown,** and may be modest.
- **Llama 3's initialization is not stated** in the paper; 2.2 is inference.
- **OpenAI's data-use page was read via a search summary,** not directly (403).
- **Bee figures come from an extension page,** not a peer-reviewed review; Seeley 2010 and
  Darwin 1859 are [record] only.
- **Every comparison is partial.** None of them is how models change; each fits one part.
