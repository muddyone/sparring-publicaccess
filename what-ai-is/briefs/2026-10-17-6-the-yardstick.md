# The yardstick: are generative AI systems judged by the wrong standard? (as of 2026-10-17)

_Research brief for a sixth piece in `what-ai-is/` and the fifth position piece. Gathered
2026-10-16/17 by web search. Each source was checked against its abstract, a publisher record or
a repository record; none was read in full unless marked. Verification marks: **[abstract]**
checked against the abstract; **[record]** bibliographic record only; **[secondary]** only
secondary coverage; **[report]** already cite-checked in an earlier what-ai-is report._

## The claim under test

The thesis under test: people, and academics and commentators in particular, judge generative AI as they
would a calculator or ordinary software. It must be correct or incorrect, perfectly consistent,
and fully trustworthy and explainable before it counts as valuable or safe. None of that is
demanded of a new intern. The wrong yardstick produces poor, oddly binary conclusions, and as
these systems take on roles people fill, the error makes public understanding unproductive and
inaccurate.

Refined with Bart on 2026-10-17: **judge AI by the role it plays, not the category it belongs
to.** Ask "compared to what?", meaning the realistic alternative, usually the person who would
otherwise do the work. Then add the checks that AI's real differences call for.

## Bottom line

- **The core holds, and part of it is an established academic argument.** Zerilli et al. (2019)
  argue that AI is held to "an unrealistically high standard" of transparency, partly because
  human decision-making is overestimated as transparent. London (2019) argues that in medicine,
  verified accuracy can matter more than explanation.
- **Human judgment is far noisier than people assume** (Kahneman, Sibony & Sunstein 2021). And
  mechanical prediction has matched or beaten expert clinical judgment for decades (Grove et al.
  2000). The consistency and correctness bars set for AI are not bars human experts clear.
- **People do penalize machine errors more than human ones.** Confidence in an algorithm falls
  faster after the same mistake (Dietvorst, Simmons & Massey 2015). In one survey, self-driving
  cars had to be four to five times safer than human drivers to be accepted (Liu, Yang & Xu
  2018). And one AI's misdeed spills over to "all AIs" in a way one human's doesn't spill over to
  all humans (Manoli, Pauketat & Anthis 2024).
- **But "most people use the calculator yardstick" is too strong as a general claim.** The
  evidence is mixed: people sometimes *prefer* algorithmic advice (Logg, Minson & Moore 2019), and
  in one study trusted AI more than a human novice, though less than an expert (Rieger et al.
  2023). The thesis is best aimed at a *style of critique*, not at all users. No study was found
  that measures how academics and commentators frame AI's failures; that part is observation.
- **Some differences in yardstick are justified,** and the piece must build them in:
  - error shape: AI fails in places people don't predict (Bansal et al. 2019; Dell'Acqua et al. 2023)
  - scale: one model's error repeats across everyone it serves (Bommasani et al. 2022)
  - accountability: nobody may be answerable for what a learning system does (Matthias 2004)

---

## Q1. Is explainability demanded of AI beyond what's demanded of people?

**1.1** Zerilli, J., Knott, A., Maclaurin, J., & Gavaghan, C. (2019). Transparency in algorithmic
and human decision-making: Is there a double standard? _Philosophy & Technology_, 32(4), 661–683.
https://doi.org/10.1007/s13347-018-0330-6 **[abstract]**
- Argument: concerns about algorithmic opacity hold automated decisions to an unrealistically
  high standard, possibly because of an unrealistically high estimate of how transparent human
  decision-makers are. The paper reviews evidence that much human decision-making has
  transparency problems of its own. It warns that some explainable-AI regulatory proposals could
  set the bar too high.
- Framework: Dennett's intentional stance. Human action is justified by intentional-stance
  explanation, so algorithmic decisions should be justified in the same form.
- Bearing: the closest existing statement of Bart's explainability point.

**1.2** Hill, S. (2024). Against the double standard argument in AI ethics. _Philosophy &
Technology_, 37, 23. https://doi.org/10.1007/s13347-024-00720-4 **[record]**
- A direct rebuttal of 1.1. The abstract could not be retrieved (Springer requires sign-in;
  PhilArchive refused the automated fetch). A search-index summary says it argues that opaque AI
  is opaque in a very different way from humans, and that what matters is how stable, uniform
  and safe a class of decision-makers' opaque processes are. **Unverified; read the paper before
  citing its content.**
- Bearing: the strongest named counter-argument. A piece entering this debate must answer it.

**1.3** London, A. J. (2019). Artificial intelligence and black-box medical decisions: Accuracy
versus explainability. _Hastings Center Report_, 49(1), 15–21. https://doi.org/10.1002/hast.973
**[abstract]**
- Argument: opaque decisions are more common in medicine than critics realize. Where causal
  knowledge is incomplete, accurate results that can be verified empirically can matter more than
  being able to explain how they were produced.
- Bearing: "we already accept unexplained decisions when they demonstrably work," in a domain
  where stakes are high.

## Q2. Are people as consistent and correct as AI is required to be?

**2.1** Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). _Noise: A flaw in human judgment._
Little, Brown Spark. **[secondary]**
- A noise audit at an insurance company: underwriters priced the same cases independently, and
  the median difference was 55%, about five times what most people expected, the company's
  executives included. Two psychiatrists diagnosing the same 426 hospital patients agreed on the
  illness in only half the cases. The book distinguishes *level noise* (some judges are harsher
  than others) from *occasion noise* (the same judge varies with mood or fatigue).
- Figures from secondary summaries and publisher excerpts; check the book before quoting numbers.
- Bearing: inconsistency is the normal condition of expert human judgment, and it is rarely
  measured.

**2.2** Grove, W. M., Zald, D. H., Lebow, B. S., Snitz, B. E., & Nelson, C. (2000). Clinical versus
mechanical prediction: A meta-analysis. _Psychological Assessment_, 12(1), 19–30.
https://doi.org/10.1037/1040-3590.12.1.19 **[abstract]**
- Across studies of human health and behaviour, mechanical prediction averaged about 10% more
  accurate than clinical prediction. Clinical prediction was substantially more accurate in only
  a few studies (6–16%). The advantage held regardless of task, type of judge, the judges'
  experience or the data combined.
- Bearing: the right comparison for a judgment system is the human alternative's real record,
  which is often weaker than assumed.

## Q3. Do people judge machine errors more harshly, or more binarily?

**For:**

**3.1** Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People
erroneously avoid algorithms after seeing them err. _Journal of Experimental Psychology: General_,
144(1), 114–126. https://doi.org/10.1037/xge0000033 **[abstract]**
- Five studies. People who saw an algorithm forecast became more averse to it, even when they saw
  it outperform a human forecaster. Confidence fell faster for algorithms than for humans after
  the *same* mistake.
- Bearing: direct evidence of an asymmetric, near-binary response to machine error.

**3.2** Liu, P., Yang, R., & Xu, Z. (2018). How safe is safe enough for self-driving vehicles?
_Risk Analysis_. https://doi.org/10.1111/risa.13116 **[abstract + secondary]**
- 499 residents of Tianjin, China: self-driving vehicles should be about four to five times as safe
  as human-driven ones. Respondents were much less willing to accept them at the same risk as
  human driving.
- Limits: one convenience-sample survey in one city (Tianjin is from press coverage; the abstract
  doesn't name the city); the lead author calls it not conclusive.

**3.3** Manoli, A., Pauketat, J. V. T., & Anthis, J. R. (2024). The AI double standard: Humans
judge all AIs for the actions of one. arXiv:2412.06040. https://arxiv.org/abs/2412.06040
**[abstract]**
- Two pre-registered experiments (N = 720, N = 684). An agent's immoral action changed attitudes
  to the agent and to its whole group. When the agent was individuated with a name, the spillover
  persisted for AIs but not for humans. The authors call this "a double standard whereby AIs are
  judged more harshly than humans when one agent morally transgresses."
- Preprint; not yet peer-reviewed as far as the record shows.
- Bearing: one AI's failure gets read as a verdict on all AI. That is binary judgment at the
  level of the category.

**Against, or complicating:**

**3.4** Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer
algorithmic to human judgment. _Organizational Behavior and Human Decision Processes_, 151,
90–103. https://doi.org/10.1016/j.obhdp.2018.12.005 **[abstract]**
- Six experiments: lay people followed advice more when they thought it came from an algorithm.
  The effect weakened when people chose between their own estimate and the algorithm's, and among
  experienced forecasters, who relied on it less and lost accuracy as a result.
- Bearing: people do not uniformly demand perfection of machines. Experts were the most
  resistant.

**3.5** Burton, J. W., Stein, M.-K., & Jensen, T. B. (2020). A systematic review of algorithm
aversion in augmented decision making. _Journal of Behavioral Decision Making_, 33(2), 220–239.
https://doi.org/10.1002/bdm.2155 **[abstract]**
- 61 articles, 1950–2018. Causes and fixes grouped into five themes: expectations and expertise,
  decision autonomy, incentives, cognitive compatibility, and divergent rationalities.
- Bearing: "expectations" is a recognized driver of aversion. The yardstick is part of the
  established explanation, not a new idea.

**3.6** Rieger, T., Kugler, L., Manzey, D., & Roesler, E. (2023). The (im)perfect automation
schema: Who is trusted more, automated or human decision support? _Human Factors_.
https://doi.org/10.1177/00187208231197347 **[abstract]**
- Simulated X-ray task. Trust and perceived reliability: human expert > AI > human novice.
  Forgiveness after a failure did not differ between agents. The authors read it as evidence of an
  *imperfect* automation schema, against the older idea that people expect automation to be
  perfect.
- Bearing: a caution against claiming people expect AI to be perfect. Users may already have
  moved; the critique style may not have.

**3.7** Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial
intelligence. _Journal of Consumer Research_, 46(4), 629–650. https://doi.org/10.1093/jcr/ucz013
**[abstract]**
- People resist medical AI because they believe it can't account for their unique
  circumstances ("uniqueness neglect"). The resistance disappears when the AI's care is framed as
  personalized, or when it supports rather than replaces a physician.
- _(The cite-check could not confirm this reply exists; do not cite until found.)_ Pezzo &
  Beckstead (2020, _Judgment and Decision Making_ 15(3)) argue the preference for humans
  held only when the two providers' records were equal; when the AI was known to outperform, people
  preferred it. **[secondary]**
- Bearing: role framing ("supports a human" versus "replaces one") changes the verdict. That is the
  role yardstick at work.

## Q4. Which differences justify a different yardstick?

**4.1 Error shape.** Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E.
(2019). Beyond accuracy: The role of mental models in human–AI team performance. _HCOMP_ 7, 2–11.
https://doi.org/10.1609/hcomp.v7i1.5285 **[report]**
- Human–AI teams do better when the user has an accurate mental model of *when the AI will be
  wrong* (its "error boundary"). That a human-shaped model of its errors misleads is our
  extrapolation, not the paper's claim (cite-check, 2026-10-17).

**4.2 Error shape, in the field.** Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf,
H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). _Navigating
the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge
worker productivity and quality._ Harvard Business School Working Paper 24-013 (also on SSRN).
**[abstract, via the cite-check]**
- Pre-registered field experiment, 758 BCG consultants. On tasks inside GPT-4's abilities, more
  tasks were done, faster and at higher quality. On a task outside them, consultants using AI
  were 19 percentage points less likely to produce correct solutions (abstract, retrieved by the
  2026-10-17 cite-check).
- Bearing: "jagged" capability is why an intern analogy needs care. The ability doesn't degrade
  smoothly the way a person's does.

**4.3 Scale.** Bommasani, R., Creel, K. A., Kumar, A., Jurafsky, D., & Liang, P. (2022). Picking on
the same person: Does algorithmic monoculture lead to outcome homogenization? _NeurIPS_ 35.
https://arxiv.org/abs/2211.13972 **[abstract]**
- When deployments share data or models, the same individuals tend to get the same outcomes
  everywhere. Greater data sharing reliably intensified this on fairness benchmarks; for
  foundation models, the results were mixed and depended on how the model was adapted.
- Bearing: a legitimate reason to audit consistency *across the system*, even while tolerating
  variation *within* a single answer as we do with people.

**4.4 Accountability.** Matthias, A. (2004). The responsibility gap: Ascribing responsibility for
the actions of learning automata. _Ethics and Information Technology_, 6(3), 175–183.
https://doi.org/10.1007/s10676-004-3422-1 **[abstract + secondary]**
- Designers of learning machines cannot foresee what the machines will do, so traditional
  responsibility ascription leaves a gap. Society must either give up such machines or accept
  the gap.
- Bearing: an intern is answerable; a model is not. Part of what makes a person's imperfection
  tolerable is the accountability that surrounds it.

## Q5. What does a role yardstick look like in practice?

**5.1** Frank, M. C. (2023). Baby steps in evaluating the capacities of large language models.
_Nature Reviews Psychology_, 2, 451–452. https://doi.org/10.1038/s44159-023-00211-x **[record]**
- Comment piece: methods from developmental psychology can help work out what these models
  represent, where standard computational evaluation may not.
- Bearing: evaluate the system as a mind-like performer, with the methods used for minds.

**5.2** Mollick, E. (2024). _Co-intelligence: Living and working with AI._ Portfolio. **[secondary]**
- His third principle: "Treat AI like a person (but tell it what kind of person it is)." Mollick
  himself calls the analogy imperfect, saying it is easiest to picture the AI as an "alien person"
  rather than a machine.
- Bearing: a popular statement of the intern frame, for using AI rather than evaluating it.
  Reviewers note the anthropomorphism concerns.

**5.3 Tension with the presentation consensus.** [report] The Chalmers report found that
sceptics and optimists agree a product should not present itself as a person. A role yardstick
must therefore be about *how to evaluate and rely on* the system, not about *what the system
is*. "Judge it as you would whoever fills the role; describe it as what it is."

## Gaps and cautions

- **No study found of how academics and commentators frame AI errors.** The claim that critics
  use a calculator yardstick is observation. A content analysis would turn it into evidence.
- **Hidalgo et al. (2021), _How Humans Judge Machines_ (MIT Press)** reports dozens of experiments
  comparing reactions to the same act by a human or a machine. **[record]** Its specific findings
  were not confirmed and should not be cited until read.
- **Hill (2024)** is cited for existing, not for its content (1.2).
- **The BCG "outside the frontier" figure** is now confirmed from the abstract (4.2).
- **Not yet searched:** studies of LLM run-to-run inconsistency compared with human
  test–retest inconsistency on the same task. This would be the most direct test of the
  consistency point.
