# Cite-check: the curiosity brief (2026-10-17)

Run on `briefs/2026-10-17-7-curiosity.md` with `/cite-check`. The raw report follows.

**Summary.** 19 items. **No citation was found wrong or invented.**
- **Clean (2):** Krishnamurthy et al. 2024, Pathak et al. 2017.
- **Disagreements** are the bottom line's short mentions. The bibliography lookup can't match
  those, and each points to a checked full entry. Schmidhuber 1991: both models agree on the
  content; existence rests on the record (Open Library had no match).
- **Resolved after the run (brief and position piece corrected):**
  - **Kidd & Hayden:** "a drive state for information" is not in the abstract. It is now
    paraphrased, and the brief attributes the phrase to coverage.
  - **Yiu, Kosoy & Gopnik:** "never chooses its own experience" was stronger than the abstract.
    It is now stated as transmission versus truth.
  - **Samiei et al.:** the abstract doesn't name gpt-5. It is now "leading models".
  - **Burda et al.:** "fixates on noise" is the field's gloss. The piece now states the abstract's
    claim: limits in stochastic settings.
- **Interpretive links, flagged and kept as ours:** OMNI and Voyager connected to Gopnik's
  framing.

---

# cite-check report — curiosity-brief

**Source:** `briefs/2026-10-17-7-curiosity.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **19** citations checked
- existence independently confirmed: **9**
- application evidence-grounded: **9**
- application judged from model knowledge only: **10**
- not independently checkable: **0**
- buckets — clean **2** · problem **10** · disagree **10**

## ⛔ DISAGREE — escalate to human (10)
### c02 — exists SPLIT · applied ✅  · ⚑ degraded  (line 16)
_The working definition in neuroscience is behavioural, "a drive state for information" (Kidd & Hayden 2015)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This bare in-text citation matches the fully verified Kidd & Hayden 2015 Neuron paper (c11); the 'drive state for information' framing is consistent with that work's information-seeking emphasis.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup found no match for the underspecified author-year reference, so existence is not confirmed from the provided evidence. From model knowledge, Kidd and Hayden 2015 is commonly associated with framing curiosity as a drive state for information, but no retrieved source text was supplied for this record.

### c03 — exists SPLIT · applied ✅  · ⚑ degraded  (line 19)
_In simple bandit tasks, GPT-3.5, GPT-4 and Llama 2 explored adequately in only one configuration: GPT-4 with step-by-step reasoning and an externally summarized history (Krishnamurthy et al. 2024)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This in-text citation matches the fully verified Krishnamurthy et al. 2024 arXiv paper (c13), whose abstract confirms GPT-4 with chain-of-thought and externally summarized history was the only configuration exploring satisfactorily.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence for this abbreviated reference is a failed Crossref match, so existence is not confirmed on this record. From model knowledge, the stated result matches the Krishnamurthy et al. 2024 bandit-exploration paper, but no source text was retrieved for this citation.

### c04 — exists SPLIT · applied SPLIT  · ⚑ degraded  (line 22)
_Gopnik's group found models explore less efficiently than people (Samiei et al. 2026)._
- **escalate:** existence: verified vs unchecked; application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This in-text citation matches the verified Samiei et al. 2026 paper (c14) with Gopnik as author, whose abstract states models exhibit less efficient exploration strategies than humans.
- gpt: exists=unchecked applied=unchecked [no_basis] — The provided lookup for this abbreviated future-dated reference found no Crossref match, and no source text was retrieved for this record. Because the claim depends on a 2026 work beyond model knowledge, the application cannot be judged here.

### c05 — exists SPLIT · applied ✅  · ⚑ degraded  (line 25)
_Schmidhuber's 1991 proposal of curiosity and boredom as rewards for improving a world model_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This refers to the well-known Schmidhuber 1991 curiosity/boredom proposal (full ref at c16); the claim accurately describes it from established knowledge.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup did not match this incomplete reference, so existence is not confirmed from the provided evidence. From model knowledge, Schmidhuber’s 1991 curiosity/boredom proposal did use improvement in a world model as an intrinsic reward idea.

### c06 — exists SPLIT · applied ✅  · ⚑ degraded  (line 26)
_Oudeyer & Kaplan's 2007 typology of "intrinsic motivation"_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This in-text reference matches the fully verified Oudeyer & Kaplan 2007 intrinsic motivation typology (c17).
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is a failed Crossref match for the abbreviated reference. From model knowledge, Oudeyer and Kaplan 2007 is indeed a typology of computational approaches to intrinsic motivation.

### c07 — exists SPLIT · applied ✅  · ⚑ degraded  (line 27)
_Pathak et al.'s 2017 curiosity reward from prediction error, which explored games with no external reward_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This matches the verified Pathak et al. 2017 paper (c18), whose abstract confirms curiosity as prediction error and exploration with no extrinsic reward.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The provided retrieval found no Crossref match, so existence is not established by this record’s evidence. From model knowledge, Pathak et al. 2017 formulated curiosity as prediction error and tested exploration without external reward.

### c08 — exists SPLIT · applied ✅  · ⚑ degraded  (line 29)
_Prediction-error curiosity can be captured by randomness it can never learn to predict (Burda et al. 2019, the "noisy TV" problem)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This matches the verified Burda et al. 2019 paper (c19), whose abstract demonstrates limitations of prediction-based rewards in stochastic setups (the 'noisy TV' problem).
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The abbreviated reference has only a failed Crossref lookup, so existence is not confirmed from retrieved evidence. From model knowledge, Burda et al. 2019 discusses limits of prediction-error curiosity in stochastic/noisy settings, commonly linked to the noisy-TV problem.

### c09 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 31)
_OMNI uses a language model as a model of what humans find interesting, to choose what an agent should learn next (Zhang et al. 2024)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This matches the verified OMNI paper (c20), whose abstract confirms using a foundation model as a model of interestingness to prioritize tasks.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only retrieved evidence is a failed Crossref match, so existence is not confirmed on this abbreviated record. From model knowledge, OMNI uses foundation models as models of human interestingness for task selection, but the connection to Gopnik’s cultural-technology framing is interpretive rather than directly established by the citation.

### c10 — exists SPLIT · applied ✅  · ⚑ degraded  (line 33)
_Voyager has GPT-4 propose its own next tasks in Minecraft, based on what it has explored so far (Wang et al. 2023)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — This refers to the well-known Wang et al. 2023 Voyager paper, which uses GPT-4 to propose its own next tasks in Minecraft based on prior exploration; claim is accurate.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieval did not match the abbreviated Wang et al. reference in Crossref, so existence is not confirmed from this record. From model knowledge, Voyager uses GPT-4 in Minecraft with an automatic curriculum that proposes next tasks based on exploration progress.

### c16 — exists SPLIT · applied ✅  · ⚑ degraded  (line 82)
_Schmidhuber, J. (1991). A possibility for implementing curiosity and boredom in model-building neural controllers. In J.-A. Meyer & S. W. Wilson (Eds.), _From Animals to Animats: Proceedings of the First International Conference on Simulation of Adaptive Behavior_ (pp. 222–227). MIT Press. **[record + secondary]**_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library returned no match, but this is a well-documented 1991 Schmidhuber conference paper in the SAB proceedings; the claim accurately describes its curiosity/boredom reward proposal.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved lookup was an Open Library no-match, so the work’s existence is not confirmed from the provided evidence. From model knowledge, the description matches Schmidhuber’s early curiosity/boredom proposal, but no retrieved source text was available for application.

## ⚠️ AGREE-problem (10)
### c01 — exists ☐ · applied ☐  (line 9)
_Bart, 2026-10-17: the real missing ingredient is curiosity. There is little evidence of natural curiosity in these systems, and curiosity is at the heart of the human-learning discussion. A system could be designed to be curious. But most of what looks like curiosity, absent instructions that mimic it, is explained by ordinary reasoning._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; a first-hand observation by the author under test, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are treated as unchecked. It is a first-hand claim rather than an external cited work.

### c11 — exists ✅ · applied ⚠️  (line 45)
_Kidd, C., & Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. _Neuron_, 88(3), 449–460. https://doi.org/10.1016/j.neuron.2015.09.010 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed Neuron 2015 paper; abstract supports lack of agreed definition and the proposal to study motivations for information-seeking rather than define curiosity.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI, title, journal, year, volume, issue, and pages are confirmed by Crossref and EuropePMC. The abstract supports the lack of a widely agreed delineation and the information-seeking framing, but it does not itself contain the exact quoted phrase 'a drive state for information' or all details of the claim.

### c12 — exists ⚠️ · applied ⚠️  (line 53)
_Yiu, E., Kosoy, E., & Gopnik, A. (2023). Transmission versus truth, imitation versus innovation. _Perspectives on Psychological Science_ 19. https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/ **[report]**_
- claude: exists=verified applied=verified [evidence_text] — Verified Yiu, Kosoy & Gopnik paper; abstract supports the contrast between children's innovation and text-trained models, consistent with the claim about self-driven exploration.
- gpt: exists=nuance applied=nuance [evidence_text] — The work exists, but the reference gives a shortened title and incomplete publication details compared with the Crossref record. The abstract supports the contrast between children and LLMs as imitation/cultural technologies needing more than language-image data for innovation, but it does not directly establish the stronger claim that children are self-driven explorers while text-trained models never choose their own experience.

### c14 — exists ✅ · applied ⚠️  (line 71)
_Samiei, M., Yiu, E., … Gopnik, A., et al. (2026). Human adults and LLMs as scientists: Who benefits from active exploration? arXiv:2606.06464. https://arxiv.org/abs/2606.06464 **[report]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms the paper; abstract states models approach human-level accuracy but exhibit less efficient exploration, supporting the claim (though specifically 'gpt-5' is not named in abstract).
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv URL resolves to the cited 2026 paper and the retrieved snippet lists the title and authors including Samiei, Yiu, and Gopnik. The abstract supports that some state-of-the-art models approach human-level accuracy while exploring less efficiently, but the retrieved text does not specifically identify GPT-5.

### c15 — exists ☐ · applied ☐  (line 76)
_The locked Gopnik pilot (this project, 2026-10-17). All three models identified every "needs two" machine within their test budgets, but every test was one the task asked for. `pilots/gopnik-memory-overhypothesis-2026-10-16/result.md`. **[internal]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited; internal project pilot, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked is_citation=false and deliberately_uncited=true, so both axes are unchecked. It is an internal project pilot rather than an external cited work.

### c17 — exists ⚠️ · applied ✅  (line 89)
_Oudeyer, P.-Y., & Kaplan, F. (2007). What is intrinsic motivation? A typology of computational approaches. _Frontiers in Neurorobotics_, 1, 6. https://doi.org/10.3389/neuro.12.006.2007 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed Frontiers in Neurorobotics 2007 paper; abstract directly supports the synthesis of psychological accounts, the non-operational critique, and the proposed computational typology.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI, title, journal, year, and URL are confirmed, though the retrieved Crossref metadata shown lists only Oudeyer and does not confirm Kaplan in the author field. The abstract directly supports the synthesis of psychological accounts, the claim that they are not operational and sometimes inconsistent when read computationally, and the proposed formal typology for psychology/developmental robotics.

### c19 — exists ✅ · applied ⚠️  (line 102)
_Burda, Y., Edwards, H., Pathak, D., Storkey, A., Darrell, T., & Efros, A. A. (2019). Large-scale study of curiosity-driven learning. _ICLR 2019_. https://arxiv.org/abs/1808.04355 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms the paper; abstract supports the 54-environment study and limitations in stochastic setups. Author note correctly flags that 'noisy TV' is the field's label, not the paper's own term.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv page resolves to the cited title and authors. The abstract supports purely curiosity-driven learning over 54 environments including Atari and limitations in stochastic setups, but the 'noisy TV' label and fixation-on-noise formulation are interpretive/common-field language rather than stated in the retrieved abstract.

### c20 — exists ✅ · applied ⚠️  (line 114)
_Zhang, J., Lehman, J., Stanley, K., & Clune, J. (2024). OMNI: Open-endedness via models of human notions of interestingness. _ICLR 2024_. https://arxiv.org/abs/2306.01711 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms the OMNI paper; abstract supports using FMs as models of interestingness and outperforming uniform sampling or learning-progress baselines.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv page resolves to the cited OMNI paper with the listed authors and 2024 revision. The abstract directly supports the model-of-human-interestingness approach and improvement over uniform sampling or learning progress alone, but the Gopnik cultural-technology connection is an external interpretive fit rather than a claim established by this source.

### c21 — exists ✅ · applied ⚠️  (line 123)
_Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., & Anandkumar, A. (2023). Voyager: An open-ended embodied agent with large language models. arXiv:2305.16291 (_TMLR_ 2024). https://arxiv.org/abs/2305.16291 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — The arXiv abstract confirms the automatic curriculum, skill library, iterative GPT-4 prompting, and the 3.3x more unique items/15.3x faster milestones, supporting the self-directed exploration claims.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv URL resolves to the cited Voyager paper with matching title and authors. The abstract directly supports the automatic curriculum, skill library, iterative prompting, GPT-4 use, and reported gains, but the Gopnik/children framing is an external interpretive comparison not established by this evidence.

### c22 — exists ☐ · applied ☐  (line 135)
_**No study found that tests unprompted information-seeking in today's assistant products.** Bart's observation is first-hand, and Krishnamurthy et al. is the nearest controlled evidence._
- claude: exists=unchecked applied=unchecked [no_basis] — This is a gaps/cautions note, not a citation (is_citation=false), so neither axis is assessable.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation, so both axes are unchecked. No retrieved evidence is provided to assess the stated literature-gap claim.

## ✅ AGREE-clean (2)
### c13 — exists ✅ · applied ✅  (line 61)
_Krishnamurthy, A., Harris, K., Foster, D. J., Zhang, C., & Slivkins, A. (2024). Can large language models explore in-context? _NeurIPS 2024_. https://arxiv.org/abs/2403.15371 **[abstract + secondary]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms the paper and its abstract directly supports the bandit setup, the single successful configuration, and the conclusion about non-trivial interventions.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv URL resolves to the titled paper with the listed authors. The retrieved abstract directly states the bandit setting, tested models, the single satisfactory GPT-4 chain-of-thought plus summarized-history configuration, and the conclusion about needing non-trivial interventions.

### c18 — exists ✅ · applied ✅  (line 96)
_Pathak, D., Agrawal, P., Efros, A. A., & Darrell, T. (2017). Curiosity-driven exploration by self-supervised prediction. _ICML 2017_, 2778–2787. https://arxiv.org/abs/1705.05363 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms the paper; abstract supports curiosity as prediction error in learned feature space, tested in VizDoom and Super Mario Bros including no-extrinsic-reward exploration.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv page resolves to the cited title and authors. The abstract directly states curiosity as prediction error in a learned visual feature space and evaluation in VizDoom and Super Mario Bros, including exploration with no extrinsic reward.
