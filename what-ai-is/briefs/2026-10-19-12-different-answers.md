# Why does the same AI give different answers? How far can one answer be trusted? (as of 2026-10-19)

_Research brief for the first essay of Part two ("working with it"). **Draft for working through
the issue**: Bart's position is not yet formed, and this brief is meant to inform it, not argue
it. Gathered 2026-10-19 by web search and direct lookup (arXiv, Crossref and Europe PMC records).
Marks as in briefs 6–8: **[abstract]** checked against the abstract (for a blog post or short
report, against the text itself, as noted); **[record]** bibliographic record only;
**[secondary]** only press or secondary coverage; **[report]** already cite-checked in an earlier
what-ai-is report; **[ours]** our interpretation, not a finding. Nothing here was read in full
unless marked. The author's own work is kept to its own section near the end and labelled; it
does not stand in for the outside literature._

## The claim under test

Three questions a reader asks: Why do I get different answers from the same AI to the same
question? How reliable is any one answer or idea? How can I improve the quality of the response?

Working claim, to test rather than defend: **"An answer is one draw from a range of possible
answers, not a lookup, and reliability comes from the process around the answer, not from the
answer itself."**

The yardstick from essays 00 and 01 applies: judge by role, not category; ask "compared to
what?", meaning whoever would otherwise fill the role, as they actually are; keep the known
separate from the unknown; describe it accurately even when a warmer story sells better. Brief 6
named one gap this brief tries to fill: no study had yet been found comparing a model's
run-to-run inconsistency with a person's test–retest inconsistency on the same task.

## Bottom line

- **The first half of the claim holds, with a refinement.** Assistants produce text by sampling
  from a probability distribution over next words, so a repeated question yields a fresh draw
  (Holtzman et al. 2020). Even settings meant to remove randomness (temperature 0) do not make
  results repeatable in practice: accuracy varied by up to 15% across ten identical runs in one
  study (Atil et al. 2024), and one 1,000-run test produced 80 different completions (He 2025).
  The refinement: **how wide the range is varies by question, and the width is itself
  information.** Where the answers scatter, the model is more likely to be making things up
  (Farquhar et al. 2024; Manakul et al. 2023).
- **Agreement is not truth.** Sampling several answers catches *arbitrary* errors, not errors the
  model makes every time. Farquhar et al. say their method detects only a subset of
  hallucinations, and different models share many of their mistakes: on one benchmark, when two
  models both erred they gave the same wrong answer 60% of the time (Kim et al. 2025). A
  consistent answer can be consistently wrong. **[ours, from those two sources]**
- **Compared to what? Experts are draws too.** Fingerprint examiners retested on the same prints
  about seven months later repeated about 89–90% of their conclusions (Ulery et al. 2012). Pairs of
  radiologists reading the same mammograms agreed at weighted kappa 0.47 (Elmore et al. 1994).
  Pathologists matched a reference diagnosis 75% of the time overall, but only 48% for one hard
  category (Elmore et al. 2015). Three of 23 diagnoses in the DSM-5 field trials fell in the
  "unacceptable" range of agreement (Regier et al. 2013). And there is the insurance noise audit in
  _Noise_ (Kahneman, Sibony & Sunstein 2021). **But no study was found that measures a model and
  people on the same task, asked twice, side by side.** The comparison can be made only loosely.
- **Models are partly aware of their own uncertainty, and say so badly.** Larger models' internal
  probabilities are fairly well calibrated on some formats (Kadavath et al. 2022). Asked in words,
  models tend to be overconfident (Xiong et al. 2024). Users then overestimate accuracy, and
  longer explanations raise their confidence without raising accuracy (Steyvers et al. 2025).
  Hallucination is partly a product of training and testing that reward guessing over "I don't
  know" (Kalai et al. 2025).
- **Wording matters a great deal, and unpredictably; role labels do not reliably help.** Format
  changes that keep the meaning the same moved accuracy by up to 76 points in one open model
  (Sclar et al. 2024). "You are an expert" personas did not improve accuracy on factual
  questions (Zheng et al. 2024; Basil et al. 2025). Politeness, tips and threats helped on some
  questions and hurt on others, with no reliable effect overall (Meincke et al. 2025a, 2025c).
  Simply asking "Are you sure?" made models change their answer 46% of the time on average, and
  lowered accuracy (Laban et al. 2023).
- **What demonstrably improves quality is mostly outside the single answer.** The evidence is
  strongest for checks that bring in something the model did not already have:
  - retrieved sources, though they reduce errors rather than remove them (Lewis et al. 2020;
    Shuster et al. 2021): commercial legal research tools built this way still gave wrong or
    unsupported answers 17–33% of the time (Magesh et al. 2025);
  - tool-based checking (Gou et al. 2024);
  - voting across several samples (Wang et al. 2023);
  - pooling across models (Schoenegger et al. 2024).

  A model re-checking itself with no new information often fails to improve, and sometimes gets
  worse (Huang et al. 2024; Kamoi et al. 2024). Multi-agent debate helps in some reports (Du et al.
  2023) and does not reliably beat simpler sampling in others (Smit et al. 2023).
- **So the second half of the claim holds in its main direction, but is too strong as worded.**
  The answer itself carries some signal: the model's own confidence when properly elicited, how
  much its answers scatter, and how well that model does on that kind of task. The process can
  fail too: self-review without outside input, retrieval tools that still hallucinate, AI judges
  with known biases. A fairer version: **reliability comes mainly from checks that are
  independent of the answer, and how independent they are matters as much as how many there
  are.** **[ours]**
- **An AI used as a grader is as variable as an AI used to answer.** Strong AI judges agreed with
  human preferences over 80% of the time, about the rate at which humans agree with each other
  (Zheng et al. 2023). But they favour their own outputs (Panickssery et al. 2024), vary widely by
  task (Bavaresco et al. 2025), and score the same item differently from run to run (Haldar &
  Hockenmaier 2025).

---

## Q1. Why does the same model give different answers?

**1.1 Sampling is the design.** Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The
curious case of neural text degeneration. _ICLR 2020_. arXiv:1904.09751.
https://arxiv.org/abs/1904.09751 **[abstract]**
- Choosing the single most likely next word at every step produces "bland and strangely
  repetitive" text. Sampling from the "dynamic nucleus" of the probability distribution
  (nucleus sampling) produces text closer to human writing. Decoding strategy alone changes
  quality "dramatically", even from exactly the same model.
- Bearing: variety is not a malfunction. It is how fluent generation was made to work. Each
  answer is one sample. **[ours]**

**1.2 Even "deterministic" settings are not repeatable.** Atil, B., Aykent, S., Chittams, A., Fu,
L., Passonneau, R. J., Radcliffe, E., et al. (2024). Non-determinism of "deterministic" LLM
settings. arXiv:2408.04667 (earlier versions titled "LLM stability: A detailed analysis with some
surprises"). https://arxiv.org/abs/2408.04667 **[abstract]**
- Five LLMs configured to be deterministic, eight tasks, ten runs each. Accuracy varied by up to
  15% across naturally occurring runs, and the gap between best and worst possible performance
  reached 70%. "None of the LLMs consistently delivers repeatable accuracy across all tasks, much
  less identical output strings."
- Preprint; peer-review status not confirmed.

**1.3** Ouyang, S., Zhang, J. M., Harman, M., & Wang, M. (2023). An empirical study of the
non-determinism of ChatGPT in code generation. arXiv:2308.02828.
https://arxiv.org/abs/2308.02828 **[abstract]**
- 829 coding problems from three benchmarks. The share of problems where repeated requests never
  produced the same test output was 76%, 51% and 48% on the three benchmarks. Temperature 0 "does
  not guarantee determinism", though it reduces variation.
- Venue after arXiv not confirmed here.

**1.4 Why temperature 0 still varies.** He, H., & Thinking Machines Lab (2025, 10 September).
Defeating nondeterminism in LLM inference. _Thinking Machines Lab: Connectionism_ (blog).
https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ **[abstract: checked
against the post]**
- The usual explanation (parallel computation plus floating-point rounding) is incomplete. The
  main cause is that the server's arithmetic depends on how many *other* users' requests are
  batched alongside yours, and server load changes that from moment to moment.
- Demonstration: 1,000 completions of "Tell me about Richard Feynman" at temperature 0 on one
  open model gave 80 unique completions. They were identical for the first 102 tokens and split at
  the 103rd. With purpose-built kernels, all 1,000 were identical, at some cost in speed.
- Bearing: a sound, specific explanation of the "even temperature 0 varies" point. It is a
  company research blog, not peer-reviewed. Its demonstration concerns one open model on one
  serving stack. Whether commercial assistants behave the same way is not shown.

**1.5 Repeating the question 100 times.** Meincke, L., Mollick, E., Mollick, L., & Shapiro, D.
(2025a). Prompting Science Report 1: Prompt engineering is complicated and contingent.
arXiv:2503.04818. https://arxiv.org/abs/2503.04818 **[abstract + report text read]**
- GPT-4o and GPT-4o-mini, 198 graduate-level multiple-choice questions (GPQA Diamond), each asked
  100 times per prompt at temperature 0. Many questions were "not answered correctly
  consistently". Judged by the strictest standard (right on all 100 attempts), both models scored
  only about 5 percentage points above the 25% that random guessing would give, a difference that
  was not statistically significant. Judged by majority vote, GPT-4o scored about 18 points higher
  than by the strict standard.
- Bearing: "how good is this model?" depends on whether you need it right *every* time or *most*
  of the time. A single run hides that. An unreviewed short report from a university lab.

**1.6 Not a lookup.** **[ours]** No source above says it this way, but together they support it.
The model does not retrieve a stored answer. It generates one, word by word, from probabilities
that the question and its wording shape. Whether a fact comes out the same each time depends on
how sharply the model's probabilities favour it. Q4 turns that into a usable signal.

## Q2. Compared to what? Variation in expert human judgment

The fair comparison for "the same AI gave two answers" is **the same expert asked twice**
(occasion noise, in _Noise_'s terms), not two different experts. The second kind of evidence is
far more common. Both are below, labelled.

**Same person, asked again**

**2.1** Ulery, B. T., Hicklin, R. A., Buscaglia, J., & Roberts, M. A. (2012). Repeatability and
reproducibility of decisions by latent fingerprint examiners. _PLoS ONE_, 7(3), e32800.
https://doi.org/10.1371/journal.pone.0032800 **[abstract]**
- 72 examiners retested on 25 fingerprint comparisons each, about seven months later. They
  repeated 89.1% of their identification decisions and 90.1% of their exclusions; most changes
  went to "inconclusive". Repeatability was "notably lower" on comparisons they had rated
  difficult. None of the four false positives was repeated; 30% of false negatives were.
- Bearing: the closest human analogue found to "ask it again". Trained experts in a
  high-stakes, procedure-bound field changed about one in ten conclusions. The variation clustered
  in borderline cases, as model variation does in Q4. **[ours, the parallel]**

**2.2** Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). _Noise: A flaw in human judgment._
Little, Brown Spark. **[secondary; report]**
- Distinguishes *level noise* (some judges harsher than others) from *occasion noise* (the same
  judge varies with mood or fatigue). In the insurance noise audit, underwriters' quotes for the
  same case differed by a median of 55%, about five times what executives expected (brief 6, 2.1;
  used in essay 01). Figures from secondary summaries; check the book before quoting any new
  numbers from it.

**Different people, same case**

**2.3** Elmore, J. G., Wells, C. K., Lee, C. H., Howard, D. H., & Feinstein, A. R. (1994).
Variability in radiologists' interpretations of mammograms. _New England Journal of Medicine_,
331(22), 1493–1499. https://doi.org/10.1056/NEJM199412013312206 **[abstract]**
- Ten radiologists each read the same 150 mammograms. Median pairwise agreement 78% (weighted
  kappa 0.47). For women without cancer, the share recommended for immediate workup ranged from
  11% to 65% across radiologists.

**2.4** Elmore, J. G., Longton, G. M., Carney, P. A., Geller, B. M., Onega, T., Tosteson, A. N. A.,
et al. (2015). Diagnostic concordance among pathologists interpreting breast biopsy specimens.
_JAMA_, 313(11), 1122. https://doi.org/10.1001/jama.2015.1405 **[abstract]**
- 115 pathologists, 6,900 diagnoses. Overall agreement with an expert consensus reference: 75.3%.
  By category: invasive cancer 96%, atypia 48%. The three-member consensus panel itself agreed
  unanimously on its first independent reads only 75% of the time.

**2.5** Regier, D. A., Narrow, W. E., Clarke, D. E., Kraemer, H. C., Kuramoto, S. J., Kuhl, E. A.,
& Kupfer, D. J. (2013). DSM-5 field trials in the United States and Canada, Part II: Test-retest
reliability of selected categorical diagnoses. _American Journal of Psychiatry_, 170(1), 59–70.
https://doi.org/10.1176/appi.ajp.2012.12070999 **[abstract]**
- Two clinicians interviewed the same patient on separate occasions. Of 23 diagnoses with enough
  cases: 5 "very good" agreement (kappa 0.60–0.79), 9 "good", 6 "questionable" (0.20–0.39), 3
  "unacceptable" (below 0.20).
- Per-diagnosis figures (major depression around 0.28–0.32, generalized anxiety about 0.20) appear
  only in secondary coverage, and sources disagree. **Do not quote a per-diagnosis kappa without
  checking the paper's table.** [secondary]

**2.6** Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review: Revisiting
the 2014 NeurIPS experiment. arXiv:2109.09774. https://arxiv.org/abs/2109.09774 **[abstract]**
- In the 2014 experiment, a share of submissions was reviewed by two independent committees. "50%
  of the variation in reviewer quality scores was subjective in origin." Review was good at
  identifying poor papers and poor at identifying good ones.
- Bearing: expert judgment of quality, the kind of judgment AI judges are asked to make (Q7), is
  itself highly variable.

**2.7** Grove, W. M., et al. (2000). Clinical versus mechanical prediction: A meta-analysis.
_Psychological Assessment_, 12(1), 19–30. https://doi.org/10.1037/1040-3590.12.1.19 **[report]**
- Already in essay 01. Relevant only as a reminder that the human side of the comparison isn't a
  gold standard.

**What the comparison can and cannot say.** **[ours]**
- *Can:* expert judgment varies, between experts and within the same expert, more than people
  assume. Its variation concentrates in hard and borderline cases. Professions have built
  procedures (second readers, consensus panels, structured criteria) around that fact rather than
  expecting any one judgment to be fixed.
- *Cannot:* say whether a model varies more or less than a person on the same task. **No
  head-to-head study was found** (search 2026-10-19). Studies of LLM self-consistency rarely
  include a matched human retest arm; the nearest is Haldar & Hockenmaier 2025 (7.4), which
  measures model graders alone. The units also differ: the fingerprint figure is a categorical
  decision seven months apart; model figures are usually reruns minutes apart.
- *A difference worth keeping:* a person's occasion noise comes with memory of the first answer.
  A model asked twice in fresh conversations has none, so each answer is closer to an independent
  draw. That is what makes repeated sampling usable as a check (Q4), which repeated asking of a
  person mostly is not.

## Q3. Confident errors: does the model know when it's wrong?

**3.1 Why confident errors happen.** Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025).
Why language models hallucinate. arXiv:2509.04664. https://arxiv.org/abs/2509.04664 **[abstract]**
- Argument: hallucinations "originate simply as errors in binary classification". They persist
  because "most evaluations" grade in a way where "guessing when uncertain improves test
  performance". Models are "optimized to be good test-takers". Proposed fix: change how the
  dominant benchmarks score abstention.
- An argument with a statistical analysis, from authors at OpenAI and Georgia Tech, not an
  experiment. Preprint.

**3.2** Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., et al. (2023). Survey of hallucination
in natural language generation. _ACM Computing Surveys_, 55(12), 1–38.
https://doi.org/10.1145/3571730 **[abstract]**
- Standard survey of definitions, metrics and mitigations. Cite for the field's vocabulary, not
  for a specific figure.

**3.3 A concrete confident error: invented references.** Walters, W. H., & Wilder, E. I. (2023).
Fabrication and errors in the bibliographic citations generated by ChatGPT. _Scientific Reports_,
13. https://doi.org/10.1038/s41598-023-41032-5 **[abstract]**
- 636 citations in 84 short literature reviews. Fabricated: 55% of GPT-3.5's citations and 18% of
  GPT-4's. Among real citations, substantive errors in 43% (GPT-3.5) and 24% (GPT-4).
- Bearing: a model generation that is now old. It shows the shape of the problem and that newer
  models improved, not today's rate.

**3.4 Do models know what they know?** Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain,
D., Perez, E., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.
https://arxiv.org/abs/2207.05221 **[abstract]**
- Larger models are "well-calibrated on diverse multiple choice and true/false questions when they
  are provided in the right format". Asked to judge whether their own proposed answer is true,
  they do better when they "consider many of their own samples" first. Predicting in advance
  whether they know an answer works within a task and "partially" generalizes, with calibration
  struggles on new tasks.
- Anthropic authors (the company that makes Claude). Measures internal probabilities, not what a
  chat assistant says in words.

**3.5 What models say in words.** Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B.
(2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in
LLMs. _ICLR 2024_. arXiv:2306.13063. https://arxiv.org/abs/2306.13063 **[abstract]**
- When stating confidence in words, models "tend to be overconfident, potentially imitating human
  patterns of expressing confidence". Calibration improves with model capability. Consistency
  among multiple responses is among the strategies that help. All methods "struggle in
  challenging tasks, such as those requiring professional knowledge".

**3.6 A partial counterpoint.** Tian, K., Mitchell, E., Zhou, A., Sharma, A., Rafailov, R., Yao, H.,
Finn, C., & Manning, C. D. (2023). Just ask for calibration. _EMNLP 2023_. arXiv:2305.14975.
https://arxiv.org/abs/2305.14975 **[abstract]**
- For models fine-tuned with human feedback (ChatGPT, GPT-4, Claude), stated confidence was
  "typically better-calibrated than the model's conditional probabilities" on three question-answer
  benchmarks, often cutting calibration error by about half. The abstract notes that some studies
  found such models' internal probabilities poorly calibrated.
- Bearing: how you ask for confidence changes how useful it is. Xiong and Tian are not in direct
  contradiction: one compares stated confidence to accuracy, the other compares two ways of
  getting confidence. **[ours]**

**3.7 What users do with it.** Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X.,
Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they
know. _Nature Machine Intelligence_, 7(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7
**[abstract]**
- Users "tend to overestimate the accuracy of LLM responses when provided with default
  explanations". "Longer explanations increased user confidence, even when the extra length did
  not improve answer accuracy." Adjusting explanations to reflect the model's own confidence
  narrowed the gap.

**3.8** Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm not
sure, but...": Examining the impact of large language models' uncertainty expression on user
reliance and trust. _FAccT 2024_. https://doi.org/10.1145/3630106.3658941 **[abstract; report]**
- Pre-registered, N = 404, medical questions. First-person uncertainty ("I'm not sure, but...")
  lowered agreement with the system and raised participants' accuracy, by reducing (not
  eliminating) overreliance on wrong answers. Already cited in essay 04.

**Compared to what?** People are also overconfident. Moore & Healy (2008), "The trouble with
overconfidence", _Psychological Review_, 115(2), 502–517,
https://doi.org/10.1037/0033-295X.115.2.502 **[record]**, is a standard review. Its contents were
not checked here; read before citing anything beyond "overconfidence in people is well
documented". **[ours]** The difference that matters for the reader: a person's confidence is
usually read alongside their track record; a model's fluent tone is the same whether it is right
or wrong, and longer answers *look* more reliable (3.7).

## Q4. Several answers as a reliability signal

**4.1** Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D.
(2023). Self-consistency improves chain of thought reasoning in language models. _ICLR 2023_.
arXiv:2203.11171. https://arxiv.org/abs/2203.11171 **[abstract]**
- Sample several reasoning paths and take the most common answer. Gains on arithmetic and
  commonsense benchmarks, e.g. +17.9% on GSM8K (grade-school maths word problems).

**4.2** Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT: Zero-resource black-box
hallucination detection for generative large language models. _EMNLP 2023_. arXiv:2303.08896.
https://arxiv.org/abs/2303.08896 **[abstract]**
- "If an LLM has knowledge of a given concept, sampled responses are likely to be similar and
  contain consistent facts. However, for hallucinated facts, stochastically sampled responses are
  likely to diverge and contradict one another." Works without access to the model's internals.

**4.3** Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large
language models using semantic entropy. _Nature_, 630, 625–630.
https://doi.org/10.1038/s41586-024-07421-0 **[abstract]**
- Measures uncertainty "at the level of meaning rather than specific sequences of words": many
  differently worded answers that mean the same thing count as agreement. Detects "a subset of
  hallucinations — confabulations — which are arbitrary and incorrect generations", across tasks
  without task-specific data.
- Bearing: the strongest source for "the scatter is the signal". Its own scope statement is the
  limit: it targets arbitrary errors, not systematic ones.

**4.4** Li, J., Zhang, Q., Yu, Y., Fu, Q., & Ye, D. (2024). More agents is all you need.
_Transactions on Machine Learning Research_. arXiv:2402.05120. https://arxiv.org/abs/2402.05120
**[abstract]**
- Simple sampling-and-voting: performance "scales with the number of agents", and the gain grows
  with task difficulty.

**4.5 Pooling across models, compared with a human crowd.** Schoenegger, P., Tuminauskaite, I.,
Park, P. S., Bastos, R. V. S., & Tetlock, P. E. (2024). Wisdom of the silicon crowd: LLM ensemble
prediction capabilities rival human crowd accuracy. _Science Advances_, 10(45).
https://doi.org/10.1126/sciadv.adp1528 **[abstract]**
- Twelve LLMs on 31 forecasting questions, against 925 human forecasters in a three-month
  tournament. The LLM crowd was "statistically indistinguishable from the human crowd". The models
  showed human-like biases such as acquiescence. Simply averaging human and machine forecasts was
  more accurate still.
- Bearing: a rare direct "compared to what?" on aggregation. Pooling worked for both, and the
  mixture beat either alone.

**4.6 The limit: shared errors.** Kim, E., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors
in large language models. _ICML 2025_. arXiv:2506.07962. https://arxiv.org/abs/2506.07962
**[abstract]**
- Over 350 LLMs. "On one leaderboard dataset, models agree 60% of the time when both models err."
  Larger, more accurate models have highly correlated errors "even with distinct architectures and
  providers". Shown downstream in LLM-as-judge evaluation and in hiring.
- Bearing: asking a second model is not the same as asking an independent one. It ties back to
  essay 01's monoculture point (Bommasani et al. 2022 **[report]**).

## Q5. Wording, role prompts and pushback

**5.1** Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models'
sensitivity to spurious features in prompt design. _ICLR 2024_. arXiv:2310.11324.
https://arxiv.org/abs/2310.11324 **[abstract]**
- Formatting changes that keep the meaning the same moved accuracy "up to 76 accuracy points"
  (LLaMA-2-13B, few-shot). Sensitivity persisted with larger models, more examples and instruction
  tuning. Which format works best "only weakly correlates between models".
- Open models, few-shot classification. Not shown for today's frontier assistants in ordinary
  conversation.

**5.2** Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered
prompts and where to find them. _ACL 2022_. arXiv:2104.08786. https://arxiv.org/abs/2104.08786
**[abstract]**
- The *order* of the examples in a prompt can make the difference between near state-of-the-art
  and random-guess performance, and a good order for one model doesn't transfer to another.

**5.3** Mizrahi, M., Kaplan, G., Malkin, D., Dror, R., Shahaf, D., & Stanovsky, G. (2024). State of
what art? A call for multi-prompt LLM evaluation. _TACL_. arXiv:2401.00595.
https://arxiv.org/abs/2401.00595 **[abstract]**
- 6.5 million instances, 20 LLMs, 39 tasks: results from a single prompt template are brittle.
  The authors recommend evaluating across a set of prompts.

**5.4 Role and persona prompts.** Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D.
(2024). When "a helpful assistant" is not really helpful: Personas in system prompts do not
improve performances of large language models. _Findings of EMNLP 2024_, 15126–15154.
https://doi.org/10.18653/v1/2024.findings-emnlp.888 **[abstract; report]**
- 162 roles, four model families, 2,410 factual questions. Adding a persona "does not improve model
  performance … compared to the control setting where no persona is added". The persona's gender,
  type and domain can still shift accuracy. Already in essay 04.

**5.5** Basil, S., Shapiro, I., Shapiro, D., Mollick, E., Mollick, L., & Meincke, L. (2025).
Prompting Science Report 4: Playing pretend: Expert personas don't improve factual accuracy.
arXiv:2512.05858. https://arxiv.org/abs/2512.05858 **[abstract]**
- Six models, two graduate-level benchmarks. A matched expert persona had "no significant impact"
  (except one model, Gemini 2.0 Flash). Mismatched experts "sometimes degraded" performance.
  Low-knowledge personas ("toddler") often reduced it. The authors note personas may serve other
  purposes, such as tone.
- Bearing: independent replication of 5.4 on newer models and harder questions.

**5.6 Politeness, tips and threats.** Meincke et al. (2025a), see 1.5, and Meincke, L., Mollick, E.,
Mollick, L., & Shapiro, D. (2025c). Prompting Science Report 3: I'll pay you or I'll kill you —
but will you care? arXiv:2508.00614. https://arxiv.org/abs/2508.00614 **[abstract]**
- Politeness helped on some questions and hurt on others (2025a). Tipping or threatening "generally
  has no significant effect" on benchmark performance, but prompt variations "can significantly
  affect performance on a per-question level", and it is "hard to know in advance" which way
  (2025c).
- Bearing: the honest advice on prompt tricks is "contingent". Average effects are near zero, and
  effects on a single question are large and unpredictable. **[ours]**

**5.7 Pushback flips answers.** Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2023). Are you
sure? Challenging LLMs leads to performance drops in the FlipFlop experiment. arXiv:2311.08596.
https://arxiv.org/abs/2311.08596 **[abstract]**
- Ten LLMs, seven classification tasks. After "Are you sure?", models flipped their answers 46% of
  the time on average, and every model's accuracy fell between first and final answer (average drop
  17%).
- Preprint.

**5.8** Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2023).
Towards understanding sycophancy in language models. arXiv:2310.13548.
https://arxiv.org/abs/2310.13548 **[abstract]**
- Five assistants "consistently exhibit sycophancy" across four tasks. Human preference data
  favours responses that match the user's views, and both humans and preference models sometimes
  prefer "convincingly-written sycophantic responses over correct ones".
- Bearing, with 5.7: a second answer obtained by pushing back is not an independent check. It is
  pulled toward what the user seems to want. This links to essay 04's warmth finding (Ibrahim,
  Hafner & Rocher 2026 **[report]**) and to Cheng et al. 2026 **[report]**. **[ours]**

## Q6. What improves the quality of a response?

Ordered roughly by strength of evidence. Most of it is benchmark evidence, not studies of people
doing real work.

**Grounding in retrieved sources**

**6.1** Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., et al. (2020).
Retrieval-augmented generation for knowledge-intensive NLP tasks. _NeurIPS 2020_.
arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **[abstract]**
- The founding paper for retrieval-augmented generation (RAG): a model paired with a searchable
  index (here, Wikipedia). The abstract emphasizes knowledge-intensive tasks, providing provenance
  and updating knowledge.

**6.2** Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval augmentation
reduces hallucination in conversation. arXiv:2104.07567. https://arxiv.org/abs/2104.07567
**[abstract]**
- Retrieval-in-the-loop dialogue models "substantially reduce" knowledge hallucination, as verified
  by human evaluation.

**6.3 Grounding reduces errors; it doesn't remove them.** Magesh, V., Surani, F., Dahl, M., Suzgun,
M., Manning, C. D., & Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI
legal research tools. _Journal of Empirical Legal Studies_, 22(2), 216–242.
https://doi.org/10.1111/jels.12413 **[abstract]**
- Pre-registered. Vendors had marketed retrieval as "eliminating" hallucinations. Hallucinations
  were lower than in general-purpose GPT-4, but the leading tools from LexisNexis and Thomson
  Reuters "each hallucinate between 17% and 33% of the time".
- Bearing: the clearest real-product test found. Grounding moves the rate; checking is still
  needed.

**Giving a specific task or method**

**6.4** Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., et al. (2022).
Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903.
https://arxiv.org/abs/2201.11903 **[abstract]**
- Worked examples of step-by-step reasoning improved arithmetic, commonsense and symbolic reasoning
  in large models.

**6.5** Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025b). Prompting Science Report 2:
The decreasing value of chain of thought in prompting. arXiv:2506.07142.
https://arxiv.org/abs/2506.07142 **[abstract]**
- For non-reasoning models, chain of thought gives a small average improvement but "can introduce
  more variability in answers, sometimes triggering occasional errors in questions the model would
  otherwise get right". For reasoning models, gains are "marginal, if any", at much higher cost.
- Bearing: 6.4's advice is aging as models build reasoning in.

**6.6 Evidence on "a specific job, not an identity" is thin outside the author's work.** **[ours]**
No external study was found that directly compares a specific task instruction ("check every
figure against the brief") with a role label ("you are a careful analyst") on the same work. The
nearest evidence is indirect: personas don't help (5.4, 5.5); external checks do (6.7–6.9). The
author's own pilot (A.3) is the closest direct test, and it is small and AI-scored. Vendor
prompting guides advise specific, explicit instructions; that is advice, not evidence, and was
not checked here.

**Independent critique and checking**

**6.7 Self-correction without new information often fails.** Huang, J., Chen, X., Mishra, S.,
Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2024). Large language models cannot self-correct
reasoning yet. _ICLR 2024_. arXiv:2310.01798. https://arxiv.org/abs/2310.01798 **[abstract]**
- Without external feedback, LLMs "struggle to self-correct their responses", and "at times, their
  performance even degrades after self-correction".

**6.8** Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024). When can LLMs actually
correct their own mistakes? A critical survey of self-correction of LLMs. _TACL_, 12, 1417–1440.
https://doi.org/10.1162/tacl_a_00713 **[abstract]**
- Many positive self-correction studies "over-evaluate" it. "No prior work demonstrates successful
  self-correction with feedback from prompted LLMs, except for studies in tasks that are
  exceptionally suited for self-correction." Self-correction "works well in tasks that can use
  reliable external feedback".

**6.9 Checking with tools or independent questions.** Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang,
Y., Duan, N., & Chen, W. (2024). CRITIC: Large language models can self-correct with
tool-interactive critiquing. _ICLR 2024_. arXiv:2305.11738. https://arxiv.org/abs/2305.11738
**[abstract]**
- Revising after checking with search engines or code interpreters "consistently enhances"
  performance. The authors stress "the crucial importance of external feedback".
- Also: Dhuliawala, S., et al. (2023). Chain-of-verification reduces hallucination in large
  language models. arXiv:2309.11495 **[abstract]**. The model drafts, plans verification
  questions, answers them *independently* "so the answers are not biased by other responses", then
  revises; hallucinations fell across several tasks.

**6.10 A second model as examiner.** Cohen, R., Hamri, M., Geva, M., & Globerson, A. (2023). LM vs
LM: Detecting factual errors via cross examination. arXiv:2305.13281.
https://arxiv.org/abs/2305.13281 **[abstract]**
- An examiner model questions the model that made a claim, looking for inconsistencies.
  Outperformed baselines on four benchmarks, "often by a large gap".

**6.11 Debate: mixed.** Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023).
Improving factuality and reasoning in language models through multiagent debate.
arXiv:2305.14325 **[abstract]**: several model instances debating over rounds improved maths,
strategic reasoning and factual validity. Against that, Smit, A., Duckworth, P., Grinsztajn, N.,
Barrett, T. D., & Pretorius, A. (2023). Should we be going MAD? A look at multi-agent debate
strategies for LLMs. arXiv:2311.17371 **[abstract]**: debate systems "do not reliably outperform"
self-consistency and ensembling, though some do better after tuning.
- Bearing: more rounds of AI-to-AI argument are not reliably better than simply sampling more.
  This matches the author's own null on iterating to agreement (A.4). **[ours]**

**6.12 Cross-model checking.** **[ours]** The case for asking a *different* model rests on
independence. Evidence that it helps comes from aggregation (4.5) and cross-examination (6.10).
Evidence that it is weaker than it looks comes from correlated errors (4.6) and self-preference in
judges (7.3). No external study was found that cleanly isolates "same model as checker" versus
"different model as checker" on everyday tasks. The author's own grid (A.3) is one small attempt.

## Q7. How reliable is an AI used as a judge?

**7.1** Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., et al. (2023). Judging
LLM-as-a-judge with MT-Bench and Chatbot Arena. _NeurIPS 2023 Datasets and Benchmarks_.
arXiv:2306.05685. https://arxiv.org/abs/2306.05685 **[abstract]**
- Strong judges like GPT-4 matched controlled and crowdsourced human preferences "achieving over
  80% agreement, the same level of agreement between humans". The paper examines position,
  verbosity and self-enhancement biases.
- (Different author from 5.4: Lianmin Zheng, not Mingqian Zheng.)

**7.2** Bavaresco, A., Bernardi, R., Bertolazzi, L., Elliott, D., Fernández, R., Gatt, A., et al.
(2025). LLMs instead of human judges? A large scale empirical study across 20 NLP evaluation tasks.
_ACL 2025_. arXiv:2406.18403. https://arxiv.org/abs/2406.18403 **[abstract]**
- Eleven LLMs, twenty datasets with human annotations: "substantial variance across models and
  datasets". Reliable on some tasks, not others. They "should be carefully validated against human
  judgments before being used as evaluators".

**7.3** Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM evaluators recognize and favor their
own generations. arXiv:2404.13076. https://arxiv.org/abs/2404.13076 **[abstract]**
- Self-preference: an evaluator scores its own outputs higher than others' that humans rate as
  equal. This is linked to its ability to recognize its own text.

**7.4** Haldar, R., & Hockenmaier, J. (2025). Rating roulette: Self-inconsistency in LLM-as-a-judge
frameworks. _Findings of EMNLP 2025_. arXiv:2510.27106. https://arxiv.org/abs/2510.27106
**[abstract]**
- LLM judges "have low intra-rater reliability in their assigned scores across different runs …
  almost arbitrary in the worst case".
- Further detail from a search summary, not checked against the paper: only the newest model
  approached the conventional 0.8 reliability threshold on one benchmark, and one model gave the
  same verdict on all three runs in 61.3% of cases. **[secondary]**

## Q8. Testing the claim with the yardstick [ours]

Our reading, to be argued, not a finding.

**"One draw from a range, not a lookup."** Supported (1.1–1.5). Two refinements:
1. *The range has a width, and the width varies.* On settled, well-represented facts the draws
   mostly agree; on hard or borderline questions they scatter (1.5, 4.2, 4.3). Expert judgment
   behaves the same way (2.1, 2.4).
2. *A narrow range is not a correct one.* Systematic errors repeat (4.3's scope; 4.6). Essay 01
   already makes the useful side of this point: a repeatable error is a testable one.

**"Reliability comes from the process around the answer, not from the answer itself."** Right in
direction, too strong as worded.
- *For:* the reliable gains come from outside input: retrieved sources (6.1–6.3), tools (6.9),
  independent questioning (6.9, 6.10), aggregation (4.1, 4.4, 4.5). Self-review without new input
  is weak (6.7, 6.8). That is the human pattern too. Professions handle the fact that experts vary
  (Q2) with second readers, panels and structured criteria, not by trusting one expert more.
- *Against "not from the answer itself":* the answer carries usable signal. How much repeated
  answers agree (4.3), the model's own probability estimates in the right format (3.4), and
  properly elicited stated confidence (3.6) all predict accuracy to a degree. And which model, on
  which kind of task, matters a great deal (essay 01's "jagged frontier", Dell'Acqua et al. 2023
  **[report]**).
- *Against "the process" as a guarantee:* processes fail in known ways.
  - Retrieval tools still hallucinate (6.3).
  - AI judges favour themselves and vary run to run (7.3, 7.4).
  - A second model often shares the first one's errors (4.6).
  - Pushback draws agreement, not truth (5.7, 5.8).
  - More rounds of AI debate don't reliably help (6.11).

  What separates processes that work from those that don't is **independence**: does the check
  bring in something the first answer didn't have?

**A candidate restatement for Bart to test:** "An answer is one draw from a range of possible
answers. Whether the draws agree tells you something, but not everything, since a model can be
consistently wrong. Reliability comes mostly from checks that bring in something the answer
didn't have: a source, a tool, a reviewer with a different job, or a different model. It does not
come from asking the same model again or pushing it until it agrees."

**Compared to what?** On variability, the human baseline is weaker than people assume (Q2), so
"it gave me a different answer" is not by itself a verdict against the system. That is essay 01's
argument, applied here. But the comparison can't yet be made quantitative (no head-to-head study),
and two differences cut against the model:
- its tone carries no information about whether it's right (3.5, 3.7);
- it can be talked out of a correct answer more readily than the fingerprint data suggest a
  trained examiner changes a conclusion (5.7 against 2.1; different tasks, so loose).

One difference cuts in its favour: it can be asked ten times, independently and cheaply, which no
expert can.

**What would change this picture.**
- A head-to-head retest study, same task, model and experts.
- Evidence that cross-model checking fails broadly because of correlated errors.
- Field studies, not benchmarks, showing whether users who sample several answers or demand
  sources actually make better decisions.

---

## A. The author's own work (internal; use carefully)

**Published and citable:** Paper 1 (the Resolver), Zenodo concept DOI
https://doi.org/10.5281/zenodo.21210264. Source read: `pilots/llm-judge-2026-05-02/v2/preprint-draft.md`
(read only). It is locked. Cite its findings as published; do not paraphrase them into claims it
doesn't make. All its governance results are directional, small-n and largely AI-coded (§11.1,
§11.2). As in essay 04, report each pilot separately and keep the unfavourable numbers.

**A.1 People disagreeing about which answer is better (§4.4).** Ten raters judged pairs of answers
blind. Agreement among them was "near zero": Krippendorff's α about −0.05 on one case and +0.01
on the other. Bearing: a first-hand instance of Q2. Human judgment of answer quality can be close
to scattered, which caps what any single rating, human or AI, can show.

**A.2 AI judges versus people (§4.1).** Three AI judges from different vendors failed the
pre-registered agreement gate with human raters. Only one of six criteria passed (whether an
answer cites checkable artifacts, ρ 0.78). On factual accuracy the judges gave every answer the
same score (6 of 7), so agreement could not be computed. Bearing: Q7, locally. AI judges tracked
people where the evidence was visible on the page and not elsewhere.

**A.3 Independent challenge versus self-review (§6.3; pilot `pilots/catch-rate-v3-2026-06-28/`,
pre-registered).** 8 hard problems, 31 serious flaws confirmed by a three-AI audit panel. Share of
the producer's own flaws caught:
- challenger (a fresh AI told to attack from a different angle): 87.1%;
- self-review: 67.7%;
- neutral fresh reviewer: 54.8%.

This pilot imposed **no evidence requirement** on the reviews; that is §7's pilot (A.5). Report
the two apart. In the full grid (two models in each of three roles), a challenge recovered 78–94%
in all eight cells. Self-review's shortfall was large for Claude-produced work and nearly vanished
for GPT-5.2, so whether a separate challenger beats self-review depends on the producing model. A
re-run scored the same-vendor challenger at 90% and a cross-vendor challenger at 94%; vendor
alignment between challenger and audit panel was worth about 2–5 points. Bearing: Q6, "a specific
job, not an identity" and "a different model". The neutral reviewer's 55% is the unfavourable
comparison that shows the job description doing work. Limits: n = 8 problems; AI-established
ground truth; no significance test.

**A.4 Arguing to agreement doesn't produce a better answer (§6.4, pre-registered).** Iterating
challenger and producer until both agree left no fewer net flaws than one challenge and fix
(+0.000 same-vendor, −0.125 cross-vendor). It was worse than a quiet second self-revision (+0.375
and +0.750 flaws per output). Detection removed about 87% of original flaws, but revising under
adversarial pressure introduced about 2.0–2.6 new flaws per output, against about 1.25 for quiet
self-revision (the authors read these as upper bounds). Bearing: matches 6.7, 6.8 and 6.11. More
process is not automatically better process. n = 8.

**A.5 Grounded critique (§7; seeded-defect pilot, pre-registered, grounding machine-checked).**
Share of concerns backed by a checkable source:
- full method: 96.3%;
- tough realistic skeptic: 83.3%;
- plain single pass: 58.3%.

Precision was 100%, 100% and 50%. The edge over the competent skeptic was "marginal", about 13
points at n = 12 cases, and it reversed on one in-brief defect family. The "fragility finding":
against a strawman placebo told to cite nothing, the control grounded only 15%. "Your placebo's
competence sets your effect size." Bearing: Q6's grounding point. Also a caution on reading
anyone's comparison numbers, including these.

**A.6 Wording moves the rate, not the judgment (§6.5, exploratory).** Five versions of an AI gate
meant to block revisions that made things worse spanned block rates from 0% to 97%. Their ability
to tell real regressions from clean edits stayed near chance (balanced accuracy 0.50–0.59).
Swapping in the most capable model available changed nothing. The authors call it a "forming"
negative result because the labels may be noisy. Bearing: Q5, a sharp first-hand case. Prompt
wording can make an AI stricter or more lenient without making it more discerning.

**A.7 Checking the answer's own numbers (§8.1, exploratory).** A check that every stated figure
either follows from the given facts (decided by a calculator, not a model) or is marked as an
estimate. Two vendors' models agreed about 90% on whether a figure was presented as fact
("agreement, not correctness"). In three constructed cases, correcting a wrong load-bearing figure
flipped the decision. Bearing: Q6, a concrete example of a check independent of the model.

## Open questions

- Is there any study measuring a model and human experts on the *same* task, each asked twice?
  None found on 2026-10-19. This is the single most useful missing piece, and a candidate pilot
  for this project. If run, fix its main measure in advance, as the series' rule requires.
- How much do commercial chat assistants vary run to run in ordinary use, as opposed to through the
  API on benchmarks? Providers don't publish their apps' sampling settings; not found.
- Do users who sample several answers, ask for sources, or use a second model actually decide
  better? Benchmarks say the techniques help; no field study of users was found.
- Does a specific task instruction beat a role label, outside the author's own pilot? Not found
  (6.6).
- Hill (2024), the rebuttal named in brief 6, argues opaque AI is opaque differently from humans.
  Does that also cover *variability*? Unread.

## Gaps and cautions

- **Benchmark-heavy.** Most evidence here is from multiple-choice or short-answer benchmarks, not
  open-ended work. Transfer to "help me think through this decision" is assumed, not shown.
- **Model generations move fast.** Figures from 2023 models (3.3, 5.1, 5.7) describe the shape
  of a problem, not today's rate. Several 2025 reports already show prompting effects shrinking for
  reasoning models (6.5).
- **Several key sources are preprints or company research** (1.2, 1.4, 3.1, 3.4, 5.7, 5.8,
  7.3). Anthropic authored 3.4 and co-authored 5.8. Claude, which helped draft this brief, is made
  by Anthropic.
- **Unverified specifics flagged inline:** per-diagnosis DSM-5 kappas (2.5); Haldar &
  Hockenmaier's model-level figures (7.4); the contents of Moore & Healy (Q3); new figures from
  _Noise_ (2.2).
- **The human comparisons mix designs:** retest after months (2.1), different experts (2.3–2.5),
  committees (2.6). None is a matched comparison with a model.

## Sources

Full list, with marks. ★ = already cite-checked in an earlier what-ai-is report.

**Variation and sampling**
- Atil, B., et al. (2024). Non-determinism of "deterministic" LLM settings. arXiv:2408.04667. [abstract]
- He, H., & Thinking Machines Lab (2025). Defeating nondeterminism in LLM inference. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ [abstract: post read]
- Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The curious case of neural text degeneration. ICLR. arXiv:1904.09751. [abstract]
- Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025a). Prompting Science Report 1. arXiv:2503.04818. [abstract + report text]
- Ouyang, S., Zhang, J. M., Harman, M., & Wang, M. (2023). Non-determinism of ChatGPT in code generation. arXiv:2308.02828. [abstract]

**Human judgment, compared**
- Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review. arXiv:2109.09774. [abstract]
- Elmore, J. G., et al. (1994). Variability in radiologists' interpretations of mammograms. NEJM 331(22), 1493–1499. https://doi.org/10.1056/NEJM199412013312206 [abstract]
- Elmore, J. G., et al. (2015). Diagnostic concordance among pathologists interpreting breast biopsy specimens. JAMA 313(11), 1122. https://doi.org/10.1001/jama.2015.1405 [abstract]
- Grove, W. M., et al. (2000). Clinical versus mechanical prediction. Psychological Assessment 12(1), 19–30. https://doi.org/10.1037/1040-3590.12.1.19 [report] ★
- Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). Noise. Little, Brown Spark. [secondary; report] ★
- Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. Psychological Review 115(2), 502–517. https://doi.org/10.1037/0033-295X.115.2.502 [record]
- Regier, D. A., et al. (2013). DSM-5 field trials, Part II: Test-retest reliability. Am J Psychiatry 170(1), 59–70. https://doi.org/10.1176/appi.ajp.2012.12070999 [abstract; per-diagnosis figures secondary]
- Ulery, B. T., Hicklin, R. A., Buscaglia, J., & Roberts, M. A. (2012). Repeatability and reproducibility of decisions by latent fingerprint examiners. PLoS ONE 7(3), e32800. https://doi.org/10.1371/journal.pone.0032800 [abstract]

**Confident errors and calibration**
- Ji, Z., et al. (2023). Survey of hallucination in natural language generation. ACM Computing Surveys 55(12). https://doi.org/10.1145/3571730 [abstract]
- Kadavath, S., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221. [abstract]
- Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664. [abstract]
- Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm not sure, but…". FAccT. https://doi.org/10.1145/3630106.3658941 [abstract; report] ★
- Steyvers, M., et al. (2025). What large language models know and what people think they know. Nature Machine Intelligence 7(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 [abstract]
- Tian, K., et al. (2023). Just ask for calibration. EMNLP. arXiv:2305.14975. [abstract]
- Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. Scientific Reports 13. https://doi.org/10.1038/s41598-023-41032-5 [abstract]
- Xiong, M., et al. (2024). Can LLMs express their uncertainty? ICLR. arXiv:2306.13063. [abstract]

**Several answers as a signal**
- Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. Nature 630, 625–630. https://doi.org/10.1038/s41586-024-07421-0 [abstract]
- Kim, E., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. ICML. arXiv:2506.07962. [abstract]
- Li, J., Zhang, Q., Yu, Y., Fu, Q., & Ye, D. (2024). More agents is all you need. TMLR. arXiv:2402.05120. [abstract]
- Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT. EMNLP. arXiv:2303.08896. [abstract]
- Schoenegger, P., Tuminauskaite, I., Park, P. S., Bastos, R. V. S., & Tetlock, P. E. (2024). Wisdom of the silicon crowd. Science Advances 10(45). https://doi.org/10.1126/sciadv.adp1528 [abstract]
- Wang, X., et al. (2023). Self-consistency improves chain of thought reasoning. ICLR. arXiv:2203.11171. [abstract]

**Wording, personas, pushback**
- Basil, S., Shapiro, I., Shapiro, D., Mollick, E., Mollick, L., & Meincke, L. (2025). Prompting Science Report 4: Expert personas don't improve factual accuracy. arXiv:2512.05858. [abstract]
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2023). Are you sure? The FlipFlop experiment. arXiv:2311.08596. [abstract]
- Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts. ACL. arXiv:2104.08786. [abstract]
- Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025c). Prompting Science Report 3: I'll pay you or I'll kill you. arXiv:2508.00614. [abstract]
- Mizrahi, M., et al. (2024). State of what art? A call for multi-prompt LLM evaluation. TACL. arXiv:2401.00595. [abstract]
- Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models' sensitivity to spurious features in prompt design. ICLR. arXiv:2310.11324. [abstract]
- Sharma, M., et al. (2023). Towards understanding sycophancy in language models. arXiv:2310.13548. [abstract]
- Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D. (2024). Personas in system prompts do not improve performances. Findings of EMNLP, 15126–15154. https://doi.org/10.18653/v1/2024.findings-emnlp.888 [abstract; report] ★

**What improves quality**
- Cohen, R., Hamri, M., Geva, M., & Globerson, A. (2023). LM vs LM: Detecting factual errors via cross examination. arXiv:2305.13281. [abstract]
- Dhuliawala, S., et al. (2023). Chain-of-verification reduces hallucination. arXiv:2309.11495. [abstract]
- Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023). Multiagent debate. arXiv:2305.14325. [abstract]
- Gou, Z., et al. (2024). CRITIC. ICLR. arXiv:2305.11738. [abstract]
- Huang, J., et al. (2024). Large language models cannot self-correct reasoning yet. ICLR. arXiv:2310.01798. [abstract]
- Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024). When can LLMs actually correct their own mistakes? TACL 12, 1417–1440. https://doi.org/10.1162/tacl_a_00713 [abstract]
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS. arXiv:2005.11401. [abstract]
- Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). Hallucination-free? Journal of Empirical Legal Studies 22(2), 216–242. https://doi.org/10.1111/jels.12413 [abstract]
- Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025b). Prompting Science Report 2: The decreasing value of chain of thought. arXiv:2506.07142. [abstract]
- Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval augmentation reduces hallucination in conversation. arXiv:2104.07567. [abstract]
- Smit, A., Duckworth, P., Grinsztajn, N., Barrett, T. D., & Pretorius, A. (2023). Should we be going MAD? arXiv:2311.17371. [abstract]
- Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903. [abstract]

**AI as judge**
- Bavaresco, A., et al. (2025). LLMs instead of human judges? ACL. arXiv:2406.18403. [abstract]
- Haldar, R., & Hockenmaier, J. (2025). Rating roulette. Findings of EMNLP. arXiv:2510.27106. [abstract; model-level figures secondary]
- Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM evaluators recognize and favor their own generations. arXiv:2404.13076. [abstract]
- Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. NeurIPS Datasets and Benchmarks. arXiv:2306.05685. [abstract]

**Carried from earlier briefs (for cross-reference only)**
- Bommasani, R., et al. (2022). Picking on the same person. NeurIPS. arXiv:2211.13972. [report] ★
- Cheng, M., et al. (2026). Science. https://doi.org/10.1126/science.aec8352 [report] ★
- Dell'Acqua, F., et al. (2023). Navigating the jagged technological frontier. HBS Working Paper 24-013. [report] ★
- Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Nature. https://doi.org/10.1038/s41586-026-10410-0 [report] ★

**The author's own**
- Niedner, B. (2026). Auditable adversarial review for AI-in-the-loop decisions: a pre-registered null redirects an AI-deliberation study from better answers to governance by verifiable challenge — an empirical report on SPARRING's Resolver (the Resolver paper). Zenodo. https://doi.org/10.5281/zenodo.21210264. §4.1, §4.4, §6.3, §6.4, §6.5, §7, §8.1. [ours; published]
