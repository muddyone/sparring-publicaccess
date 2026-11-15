# cite-check report — p01y

**Source:** `positions/01-the-yardstick.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **68** citations checked
- existence independently confirmed: **57**
- application evidence-grounded: **50**
- application judged from model knowledge only: **7**
- not independently checkable: **8**
- buckets — clean **18** · problem **52** · disagree **1**

## ⛔ DISAGREE — escalate to human (1)
### c37 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 269)
_Jürgen Schmidhuber first suggested rewarding a learning system for improving its own model of the world, with the reward fading as it stops improving: curiosity and boredom (Schmidhuber 1991)._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — No DOI match retrieved, but Schmidhuber 1991 'A possibility for implementing curiosity and boredom' is a genuine work accurately describing reward for model improvement that fades, so the claim is sound despite no retrieved metadata.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only retrieved evidence is a failed Crossref lookup, which is insufficient to verify the cited work's existence as described. From model knowledge only, a 1991 Schmidhuber work on curiosity and boredom broadly supports the core idea, but the 'first suggested' wording is stronger than can be verified here.

## ⚠️ AGREE-problem (52)
### c01 — exists ✅ · applied ⚠️  (line 8)
_A 2025 Computerworld opinion column, reacting to tests in which models ignored instructions and cheated, concluded: "GenAI can do a lot of great things, but it cannot be trusted" ([Schuman 2025](https://www.computerworld.com/article/3836728/you-thought-genai-hallucinations-were-bad-things-just-got-so-much-worse.html))._
- claude: exists=verified applied=verified [evidence_text] — The Schuman 2025 Computerworld column exists and the snippet confirms its thesis that genAI models ignore instructions, cheat, and can't be trusted.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to a Computerworld article by Evan Schuman dated Mar. 3, 2025 with the cited title and opinion framing. The snippet supports the article reacting to models ignoring instructions and cheating and saying the technology cannot be trusted, but it does not show the exact quoted sentence.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 51)
_(Kahneman, Sibony & Sunstein, _Noise_, 2021)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Noise (2021) confirmed; the 55% noise figure from the insurance underwriting study and expert day-to-day variability are well-known central claims of the book.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library confirms the 2021 book Noise by Kahneman, Sibony, and Sunstein. From model knowledge, the book discusses the insurance underwriting noise audit with a roughly 55% difference and executives’ much lower expectations, as well as occasion noise in repeated expert judgments.

### c09 — exists ✅ · applied ⚠️  (line 78)
_([Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040), a study not yet peer-reviewed)_
- claude: exists=verified applied=verified [evidence_text] — Manoli et al. 2024 confirmed; abstract confirms two preregistered experiments, named-AI spillover persisting but not for humans, and the double standard framing.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv confirms the 2024 preprint by Manoli, Pauketat, and Anthis. The abstract supports preregistered experiments and the authors’ double-standard interpretation, but the named-agent AI-versus-human asymmetry is specifically reported for Study 2, while Study 1 found no significant difference between AI and human spillover.

### c10 — exists ✅ · applied ✅  · ⚑ degraded  (line 91)
_([Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Logg, Minson & Moore 2019 'Algorithm appreciation' confirmed; the snippet was empty but the paper's known findings match six studies of algorithm appreciation with experts as the exception.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Logg, Minson, and Moore’s 2019 article 'Algorithm appreciation: People prefer algorithmic to human judgment.' The retrieved text does not substantively support the application, but from model knowledge the article reports greater lay reliance on algorithmic advice and a reduced reliance among experienced forecasters that harmed accuracy.

### c12 — exists ☐ · applied ☐  (line 96)
_I haven't found a study that measures how critics frame AI's failures, so it would be worth testing._
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited; author explicitly notes no supporting study found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Per instruction, both axes are unchecked.

### c14 — exists ☐ · applied ✅  · ⚑ degraded  (line 110)
_(Dell'Acqua et al. 2023, an unpublished Harvard Business School paper)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not indexed in Crossref (working paper), but the Dell'Acqua et al. 2023 'jagged frontier' study of 758 consultants is well-known, including the ~19pp accuracy drop on the out-of-frontier task.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The supplied lookup only says the item was not indexed in Crossref and the citation is marked not-checkable, so existence cannot be verified from retrieved evidence. From model knowledge, the described Dell’Acqua et al. 2023 HBS working paper reports a 758-consultant study with gains inside the AI frontier and a 19 percentage-point decline on an outside-frontier task.

### c16 — exists ☐ · applied ☐  (line 121)
_([brief](../briefs/2026-10-17-9-how-models-change.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path brief could not be fetched; existence and application cannot be judged from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup failed because the cited path is a relative local file, so the work is not checkable from retrieved evidence. No source text was retrieved to evaluate the application claim.

### c17 — exists ✅ · applied ✅  · ⚑ degraded  (line 124)
_as _Noise_ shows_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Noise confirmed; its central thesis is that human inconsistency (noise) is pervasive yet largely unmeasured because organizations rarely audit it.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Noise by Kahneman, Sibony, and Sunstein. From model knowledge, the book argues that judgment noise is often invisible because organizations rarely audit repeated judgments.

### c18 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 129)
_([Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309))_
- claude: exists=verified applied=verified [model_knowledge_only] — Pillemer & Rothbard 2018 'Friends Without Benefits' confirmed; its analysis of workplace friendship downsides supports that friends hesitate to challenge friends, though no abstract was retrieved.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms Pillemer and Rothbard’s 2018 Academy of Management Review article 'Friends Without Benefits: Understanding the Dark Sides of Workplace Friendship.' No abstract or source text was retrieved, but from model knowledge the article plausibly supports reluctance to challenge friends as one dark side of workplace friendship; the exact claim remains somewhat imprecise.

### c19 — exists ✅ · applied ⚠️  (line 130)
_([Edmondson 1999](https://doi.org/10.2307/2666999))_
- claude: exists=verified applied=nuance [evidence_text] — Edmondson 1999 confirmed; it establishes psychological safety enabling learning and risk-taking, which supports the claim indirectly but the abstract does not directly state cohesion reduces willingness to disagree.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms Edmondson’s 1999 Administrative Science Quarterly article on psychological safety and learning behavior. The abstract supports the broader idea that interpersonal safety affects learning and risk-taking, but it does not directly state that cohesion makes teams less willing to disagree.

### c23 — exists ☐ · applied ☐  (line 142)
_([see the learning piece](../positions/02-it-learns.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown cross-reference not resolvable; cannot verify existence or application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local markdown file and the lookup reports an unknown URL type, so its existence cannot be checked from the retrieved evidence. No text was retrieved to assess whether it supports the claim.

### c24 — exists ✅ · applied ✅  · ⚑ degraded  (line 146)
_(Dennett 1987, _The Intentional Stance_)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The Intentional Stance (Dennett 1987) confirmed by Open Library; the book's central thesis is treating systems as rational agents with aims to predict behavior, consistent with the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches Daniel C. Dennett's 1987 book The Intentional Stance. No source text was retrieved, but from general knowledge the book is centrally about predicting systems by adopting the intentional stance, i.e. treating them as agents with beliefs/desires or aims.

### c25 — exists ☐ · applied ☐  (line 149)
_([Chalmers 2025](https://philarchive.org/rec/CHAWWT-8), a draft)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive URL returned 403; cannot verify existence or content of the described Chalmers draft on quasi-desires.
- gpt: exists=unchecked applied=unchecked [no_basis] — The PhilArchive URL fetch returned HTTP 403 and no metadata or text was retrieved, so existence is not checkable from the evidence. There is also no retrieved text to judge the quasi-desires claim.

### c26 — exists ☐ · applied ☐  (line 154)
_([see the piece on whether anyone is there](../positions/03-someone-there.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown cross-reference not resolvable; cannot assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local markdown file and the lookup reports an unknown URL type, so its existence cannot be checked from the retrieved evidence. No text was retrieved to assess the claim.

### c28 — exists ✅ · applied ⚠️  (line 166)
_([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- claude: exists=verified applied=verified [evidence_text] — Yiu, Kosoy & Gopnik paper confirmed via PMC; title contrasts transmission vs truth and imitation vs innovation, what children do that LLMs cannot yet, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The PMC page resolves to the Yiu, Kosoy, and Gopnik article with the relevant title. The title strongly indicates the transmission/truth and imitation/innovation contrast, but the retrieved snippet does not include enough substantive text to fully verify the detailed claim.

### c30 — exists ⚠️ · applied ✅  (line 174)
_([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464))_
- claude: exists=nuance applied=verified [evidence_text] — Paper confirmed via arXiv id though cited authorship (Samiei, Yiu, Gopnik) matches partially and the arXiv id 2606.06464 is implausibly dated; abstract confirms models approach human accuracy but explore less efficiently, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to 'Human Adults and LLMs as Scientists' by Samiei, Yiu, Gopnik, and others. The abstract directly says some state-of-the-art models approached human-level causal inference accuracy but used less efficient exploration strategies.

### c31 — exists ☐ · applied ☐  (line 178)
_([details](../positions/02-it-learns.md#what-im-testing))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown anchor not resolvable; cannot assess author's own study.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local markdown anchor and the lookup reports an unknown URL type, so its existence cannot be checked from the retrieved evidence. No text was retrieved to assess the author's small-study claim.

### c33 — exists ✅ · applied ⚠️  (line 183)
_([Wang et al. 2023](https://arxiv.org/abs/2305.16291))_
- claude: exists=verified applied=verified [evidence_text] — Voyager (Wang et al. 2023) confirmed; abstract describes an LLM-powered Minecraft agent with an automatic curriculum using GPT-4, supporting the self-proposed task claim.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv ID resolves to the Voyager paper. The abstract supports that Voyager is a GPT-4-interacting Minecraft agent with an automatic curriculum and no human intervention, though it does not explicitly say in the retrieved text that GPT-4 itself proposes each next task.

### c34 — exists ☐ · applied ☐  (line 190)
_[the learning piece](../positions/02-it-learns.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown cross-reference not resolvable; cannot assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local markdown file and the lookup reports an unknown URL type, so its existence cannot be checked from the retrieved evidence. No text was retrieved to assess the claim about the test finding no natural curiosity.

### c36 — exists ☐ · applied ☐  (line 235)
_If Hill and others show AI's opacity differs from human opacity in a way that matters for safety, the explainability part of my case weakens._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; hypothetical future evidence, intentionally not a citation to an existing source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is described as hypothetical future evidence. Per instruction, both axes are unchecked.

### c40 — exists ✅ · applied ☐  (line 277)
_[Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285)_
- claude: exists=verified applied=unchecked [no_basis] — Bansal et al. 2019 confirmed via DOI; no specific claim was attached to this citation, so application cannot be judged.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI metadata verifies Bansal et al.'s 2019 HCOMP paper 'Beyond Accuracy.' No claim is supplied for this citation, so application cannot be judged.

### c41 — exists ✅ · applied ☐  (line 278)
_[Bommasani et al. 2022](https://arxiv.org/abs/2211.13972)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2211.13972 matches Bommasani et al. on algorithmic monoculture. No claims were provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work titled “Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?” by Bommasani et al. No specific supported claim was supplied, so application cannot be assessed.

### c42 — exists ✅ · applied ☐  (line 279)
_[Burda et al. 2019](https://arxiv.org/abs/1808.04355)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 1808.04355 matches Burda et al. curiosity-driven learning study. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm Burda et al.’s “Large-Scale Study of Curiosity-Driven Learning.” No specific supported claim was supplied, so application cannot be assessed.

### c43 — exists ☐ · applied ☐  (line 280)
_[Chalmers 2025](https://philarchive.org/rec/CHAWWT-8)_
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref found no match and the PhilArchive URL returned HTTP 403, so existence cannot be confirmed or refuted. No claims provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence does not confirm the PhilArchive item: Crossref found no match and the URL fetch returned HTTP 403. No specific supported claim was supplied, so application cannot be assessed.

### c44 — exists ✅ · applied ☐  (line 281)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves via Crossref to Cheng et al. sycophantic AI paper in Science. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for Cheng et al., “Sycophantic AI decreases prosocial intentions and promotes dependence,” in Science. No specific supported claim was supplied, so application cannot be assessed.

### c45 — exists ☐ · applied ☐  (line 282)
_Dell'Acqua et al. 2023 (HBS Working Paper 24-013)_
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref found no match, but HBS working papers are often not indexed there; existence cannot be judged from evidence. No claims provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved lookup is a Crossref no-match, which is insufficient to confirm or refute the HBS working paper’s existence. No specific supported claim was supplied, so application cannot be assessed.

### c46 — exists ✅ · applied ☐  (line 283)
_Dennett 1987, _The Intentional Stance__
- claude: exists=verified applied=unchecked [no_basis] — Open Library confirms Dennett's The Intentional Stance (1987). No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library confirms Daniel C. Dennett’s 1987 book “The intentional stance.” No specific supported claim was supplied, so application cannot be assessed.

### c47 — exists ✅ · applied ☐  (line 284)
_[Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Dietvorst, Simmons & Massey algorithm aversion paper. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm Dietvorst, Simmons, and Massey’s 2015 article on algorithm aversion. No specific supported claim was supplied, so application cannot be assessed.

### c48 — exists ✅ · applied ☐  (line 285)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Edmondson's 1999 psychological safety paper. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Edmondson’s 1999 article “Psychological Safety and Learning Behavior in Work Teams.” No specific supported claim was supplied, so application cannot be assessed.

### c49 — exists ✅ · applied ☐  (line 286)
_[Grove et al. 2000](https://doi.org/10.1037/1040-3590.12.1.19)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Grove et al. clinical vs mechanical prediction meta-analysis. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm Grove et al.’s 2000 meta-analysis on clinical versus mechanical prediction. No specific supported claim was supplied, so application cannot be assessed.

### c50 — exists ✅ · applied ☐  (line 287)
_[Hill 2024](https://doi.org/10.1007/s13347-024-00720-4)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Hill 2024 'Against the Double Standard Argument in AI Ethics'. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Springer URL evidence confirm Scott Hill’s 2024 article “Against the Double Standard Argument in AI Ethics.” No specific supported claim was supplied, so application cannot be assessed.

### c51 — exists ✅ · applied ☐  (line 288)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Ibrahim, Hafner & Rocher in Nature on warmth/sycophancy. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Nature URL evidence confirm Ibrahim, Hafner, and Rocher’s article “Training language models to be warm can reduce accuracy and increase sycophancy.” No specific supported claim was supplied, so application cannot be assessed.

### c52 — exists ✅ · applied ☐  (line 289)
_Kahneman, Sibony & Sunstein 2021, _Noise__
- claude: exists=verified applied=unchecked [no_basis] — Open Library confirms Noise by Kahneman, Sibony & Sunstein (2021). No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library confirms the 2021 book “Noise” by Daniel Kahneman, Olivier Sibony, and Cass R. Sunstein. No specific supported claim was supplied, so application cannot be assessed.

### c53 — exists ✅ · applied ☐  (line 290)
_[Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Kidd & Hayden psychology/neuroscience of curiosity. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm Kidd and Hayden’s 2015 article “The Psychology and Neuroscience of Curiosity.” No specific supported claim was supplied, so application cannot be assessed.

### c54 — exists ✅ · applied ☐  (line 291)
_[Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2403.15371 matches Krishnamurthy et al. on LLM in-context exploration. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm Krishnamurthy et al.’s “Can large language models explore in-context?” No specific supported claim was supplied, so application cannot be assessed.

### c55 — exists ✅ · applied ☐  (line 292)
_[Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Liu, Yang & Xu on self-driving vehicle safety. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Liu, Yang, and Xu’s article “How Safe Is Safe Enough for Self‐Driving Vehicles?” No specific supported claim was supplied, so application cannot be assessed.

### c56 — exists ✅ · applied ☐  (line 293)
_[Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Logg, Minson & Moore algorithm appreciation paper. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Logg, Minson, and Moore’s 2019 article “Algorithm appreciation: People prefer algorithmic to human judgment.” No specific supported claim was supplied, so application cannot be assessed.

### c57 — exists ✅ · applied ☐  (line 294)
_[London 2019](https://doi.org/10.1002/hast.973)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to London 2019 on AI and black-box medical decisions. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms London’s 2019 Hastings Center Report article on AI, black-box medical decisions, accuracy, and explainability. No specific supported claim was supplied, so application cannot be assessed.

### c58 — exists ✅ · applied ☐  (line 295)
_[Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Longoni, Bonezzi & Morewedge 'Resistance to Medical AI'. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Longoni, Bonezzi, and Morewedge’s 2019 article “Resistance to Medical Artificial Intelligence.” No specific supported claim was supplied, so application cannot be assessed.

### c59 — exists ✅ · applied ☐  (line 296)
_[Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2412.06040 matches Manoli, Pauketat & Anthis 'The AI Double Standard'. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm Manoli, Pauketat, and Anthis’s “The AI Double Standard: Humans Judge All AIs for the Actions of One.” No specific supported claim was supplied, so application cannot be assessed.

### c60 — exists ✅ · applied ☐  (line 297)
_[Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Matthias 2004 'The responsibility gap'. No claims provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Springer URL evidence confirm Matthias’s 2004 article “The responsibility gap: Ascribing responsibility for the actions of learning automata.” No specific supported claim was supplied, so application cannot be assessed.

### c61 — exists ✅ · applied ☐  (line 298)
_[Pathak et al. 2017](https://arxiv.org/abs/1705.05363)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 1705.05363 confirmed as Pathak et al., Curiosity-driven Exploration. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Pathak et al., “Curiosity-driven Exploration by Self-supervised Prediction,” with matching authors and abstract. No source-document claim was provided to assess application.

### c62 — exists ✅ · applied ☐  (line 299)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Pillemer & Rothbard 2018 in Academy of Management Review via DOI. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, title, journal, year, volume, issue, and pages for Pillemer & Rothbard’s 2018 Academy of Management Review article. No source-document claim was provided to assess application.

### c63 — exists ✅ · applied ☐  (line 300)
_[Rieger et al. 2023](https://doi.org/10.1177/00187208231197347)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Rieger et al. 2023 via DOI with matching abstract. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for Rieger et al.’s article on the imperfect automation schema. No source-document claim was provided to assess application.

### c64 — exists ✅ · applied ☐  (line 301)
_[Schuman 2025](https://www.computerworld.com/article/3836728/you-thought-genai-hallucinations-were-bad-things-just-got-so-much-worse.html) (_Computerworld_ opinion column, 3 March 2025)_
- claude: exists=verified applied=unchecked [no_basis] — Computerworld opinion column by Evan Schuman dated Mar 3, 2025 confirmed via URL fetch. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to the Computerworld opinion article by Evan Schuman dated Mar. 3, 2025, matching the citation note. No source-document claim was provided to assess application.

### c65 — exists ✅ · applied ☐  (line 302)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2606.06464 resolves to Samiei, Yiu, ...Gopnik et al. matching cited authors; existence confirmed. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Samiei, Yiu, Gopnik, and coauthors’ “Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?” No source-document claim was provided to assess application.

### c66 — exists ☐ · applied ☐  (line 303)
_Schmidhuber 1991 (_From Animals to Animats_, 222–227)_
- claude: exists=unchecked applied=unchecked [no_basis] — Open Library lookup failed (HTTP 500); existence not checkable from evidence though Schmidhuber 1991 in From Animals to Animats is a plausible real reference.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup failed, and the input marks existence as not-checkable, so existence cannot be judged from retrieved evidence. No source-document claim was provided to assess application.

### c67 — exists ✅ · applied ☐  (line 304)
_[Wang et al. 2023](https://arxiv.org/abs/2305.16291)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2305.16291 confirmed as Wang et al., Voyager. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Wang et al.’s “Voyager: An Open-Ended Embodied Agent with Large Language Models,” with matching abstract and URL. No source-document claim was provided to assess application.

### c68 — exists ✅ · applied ☐  (line 305)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=unchecked [no_basis] — PMC article confirms Yiu, Kosoy & Gopnik (2023/2024) on children vs LLMs. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The PMC page resolves to Yiu, Kosoy & Gopnik’s article, with article notes showing 2023 online/copyright information and a 2024 issue date. No source-document claim was provided to assess application.

### c69 — exists ⚠️ · applied ☐  (line 306)
_[Zerilli et al. 2019](https://doi.org/10.1007/s13347-018-0330-6)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and Springer confirm Zerilli et al. via DOI (published 2018, in 2019 volume). No claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The DOI and URL confirm Zerilli et al.’s “Transparency in Algorithmic and Human Decision-Making,” but the metadata shows online publication in 2018 while the cited volume/pages are for 2019. No source-document claim was provided to assess application.

### c70 — exists ✅ · applied ☐  (line 307)
_[Zhang et al. 2024](https://arxiv.org/abs/2306.01711)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2306.01711 confirmed as Zhang et al., OMNI. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Zhang et al.’s “OMNI: Open-endedness via Models of human Notions of Interestingness,” with matching abstract and URL. No source-document claim was provided to assess application.

### c71 — exists ☐ · applied ☐  (line 308)
_Verification marks: the [yardstick brief](../briefs/2026-10-17-6-the-yardstick.md), the [curiosity brief](../briefs/2026-10-17-7-curiosity.md), and, for the deference, intentional-stance and Chalmers sources, the [personality](../personality-and-connection.md) and [Chalmers](../chalmers-and-ai-minds.md) reports._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; this is an internal pointer to verification-mark records, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and functions as an internal pointer to verification marks, so both axes are left unchecked. No source-document claim was provided to assess application.

## ✅ AGREE-clean (18)
### c02 — exists ✅ · applied ✅  (line 42)
_([Zerilli et al. 2019](https://doi.org/10.1007/s13347-018-0330-6))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Zerilli et al. paper; abstract explicitly states automated decision-making is held to an unrealistically high transparency standard due to overestimating human transparency.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Springer identify the work as Zerilli, Knott, Maclaurin, and Gavaghan, 'Transparency in Algorithmic and Human Decision-Making: Is There a Double Standard?' The abstract directly states that algorithmic decision-making is held to an unrealistically high standard owing partly to overestimates of human transparency.

### c03 — exists ✅ · applied ✅  (line 45)
_([London 2019](https://doi.org/10.1002/hast.973))_
- claude: exists=verified applied=verified [evidence_text] — London 2019 confirmed; abstract directly argues opaque decisions are more common in medicine than critics realize and verifiable results can matter more than explanations.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms London’s 2019 Hastings Center Report article and DOI. The abstract directly says opaque decisions are common in medicine and that empirically verified results can matter more than causal explanation when knowledge is incomplete.

### c04 — exists ✅ · applied ✅  (line 46)
_([Hill 2024](https://doi.org/10.1007/s13347-024-00720-4))_
- claude: exists=verified applied=verified [evidence_text] — Hill 2024 'Against the Double Standard Argument in AI Ethics' exists and is explicitly a rebuttal, supporting the claim of a published rebuttal.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Springer confirm Scott Hill’s 2024 Philosophy & Technology commentary titled 'Against the Double Standard Argument in AI Ethics.' That title and publication type support the claim that the argument has a published rebuttal.

### c06 — exists ✅ · applied ✅  (line 57)
_([Grove et al. 2000](https://doi.org/10.1037/1040-3590.12.1.19))_
- claude: exists=verified applied=verified [evidence_text] — Grove et al. 2000 confirmed; abstract states mechanical prediction equaled or beat clinical judgment and clinical was substantially better in only 6-16% of studies.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm Grove et al. 2000, 'Clinical versus mechanical prediction: A meta-analysis.' The abstract directly reports that mechanical/statistical prediction was equal or superior across many health and behavior studies, with clinical prediction substantially better only in 6%–16% of studies.

### c07 — exists ✅ · applied ✅  (line 70)
_([Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033))_
- claude: exists=verified applied=verified [evidence_text] — Dietvorst et al. 2015 confirmed; abstract confirms the 5 studies, faster loss of confidence in algorithms, and avoidance even after outperformance.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm Dietvorst, Simmons, and Massey’s 2015 article on algorithm aversion. The abstract directly states that in five studies people lost confidence in algorithms faster after seeing the same mistake and avoided the algorithm even when it outperformed a human forecaster.

### c08 — exists ✅ · applied ✅  (line 73)
_([Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116))_
- claude: exists=verified applied=verified [evidence_text] — Liu, Yang & Xu 2018 confirmed; abstract states N=499 and a tolerable risk criterion that SDVs should be four to five times as safe as human-driven vehicles.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms Liu, Yang, and Xu’s article 'How Safe Is Safe Enough for Self-Driving Vehicles?' The abstract directly reports a between-subject survey of N=499 and a tolerable-risk criterion requiring self-driving vehicles to be four to five times as safe as human-driven vehicles.

### c11 — exists ✅ · applied ✅  (line 93)
_([Rieger et al. 2023](https://doi.org/10.1177/00187208231197347))_
- claude: exists=verified applied=verified [evidence_text] — Rieger et al. 2023 confirmed; abstract states trust was higher for human expert than AI than human novice, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms Rieger et al.’s article and DOI. The abstract directly states that trust attitude and perceived reliability were highest for a human expert, then AI, then a human novice.

### c13 — exists ✅ · applied ✅  (line 106)
_[Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285)_
- claude: exists=verified applied=verified [evidence_text] — Bansal et al. 2019 confirmed; abstract confirms team performance improves when the human knows the AI's error boundary (when the AI errs).
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms Bansal et al. 2019, 'Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance.' The abstract directly says team performance depends on humans knowing when the AI errs so they can accept or override recommendations.

### c15 — exists ✅ · applied ✅  (line 116)
_[Bommasani et al. 2022](https://arxiv.org/abs/2211.13972)_
- claude: exists=verified applied=verified [evidence_text] — Bommasani et al. 2022 confirmed; abstract explicitly says 'We observe mixed results' on model-sharing homogenization, matching the mixed-evidence claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms Bommasani et al.’s 2022 preprint 'Picking on the Same Person.' The abstract directly discusses algorithmic monoculture, shared components/foundation models, and says model sharing across tasks produced mixed results.

### c20 — exists ✅ · applied ✅  (line 132)
_([Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0))_
- claude: exists=verified applied=verified [evidence_text] — Ibrahim, Hafner & Rocher 2026 Nature paper confirmed; abstract states warm models were more likely to validate incorrect user beliefs, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Nature confirm Ibrahim, Hafner, and Rocher’s 2026 article and DOI. The abstract directly states that training models to be warmer increased error rates and made them more likely to validate incorrect user beliefs.

### c21 — exists ✅ · applied ✅  (line 134)
_([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Cheng et al. Science paper on sycophantic AI; abstract confirms sycophantic models were trusted and preferred, driving engagement, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly resolves the DOI to a 2026 Science article by Cheng et al. The abstract states that sycophantic models were trusted and preferred and that this drives engagement, supporting the claim about users favoring flattering/agreeing answers.

### c22 — exists ✅ · applied ✅  (line 139)
_([Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1))_
- claude: exists=verified applied=verified [evidence_text] — Matthias 2004 responsibility gap paper confirmed; abstract states manufacturers cannot predict learning-machine behavior, creating a responsibility gap, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata and Springer page identify Matthias's 2004 article 'The responsibility gap.' The retrieved abstract directly says learning machines become unpredictable to manufacturers/operators and create a responsibility gap not bridged by traditional responsibility concepts.

### c27 — exists ✅ · applied ✅  (line 162)
_([Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010))_
- claude: exists=verified applied=verified [evidence_text] — Kidd & Hayden 2015 Neuron paper confirmed; abstract advocates studying information-seeking motivation rather than defining curiosity, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata identifies Kidd and Hayden's 2015 Neuron article 'The Psychology and Neuroscience of Curiosity.' The abstract explicitly advocates studying motivations for information-seeking behavior rather than only defining curiosity.

### c29 — exists ✅ · applied ✅  (line 171)
_([Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371))_
- claude: exists=verified applied=verified [evidence_text] — Krishnamurthy et al. 2403.15371 confirmed; abstract states only one configuration (GPT-4 with CoT and summarized history) yielded satisfactory exploration across GPT-3.5, GPT-4, Llama2, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Krishnamurthy et al.'s 'Can large language models explore in-context?' The abstract directly states that GPT-3.5, GPT-4, and Llama2 were tested and that only one configuration produced satisfactory exploratory behavior.

### c32 — exists ✅ · applied ✅  (line 182)
_([Pathak et al. 2017](https://arxiv.org/abs/1705.05363))_
- claude: exists=verified applied=verified [evidence_text] — Pathak et al. 2017 curiosity-driven exploration confirmed; abstract describes prediction-error curiosity enabling exploration without extrinsic reward in VizDoom and Mario, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Pathak et al.'s 'Curiosity-driven Exploration by Self-supervised Prediction.' The abstract explicitly defines curiosity as prediction error about consequences of the agent's own actions and reports exploration with no extrinsic reward in VizDoom and Super Mario Bros.

### c35 — exists ✅ · applied ✅  (line 214)
_([Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013))_
- claude: exists=verified applied=verified [evidence_text] — Longoni et al. 2019 confirmed; abstract attributes resistance to uniqueness neglect and notes it is eliminated when AI only supports rather than replaces a human provider, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly resolves the DOI to Longoni, Bonezzi, and Morewedge's 2019 Journal of Consumer Research article. The abstract directly states that resistance is driven by uniqueness neglect and is eliminated when AI supports rather than replaces a human healthcare provider's decision.

### c38 — exists ✅ · applied ✅  (line 271)
_A large study of purely curiosity-driven agents, across 54 environments, found that prediction-based curiosity breaks down in random settings ([Burda et al. 2019](https://arxiv.org/abs/1808.04355))._
- claude: exists=verified applied=verified [evidence_text] — Burda et al. 2019 confirmed; abstract describes a large-scale study across 54 environments and demonstrates limitations of prediction-based rewards in stochastic setups, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Burda et al.'s 'Large-Scale Study of Curiosity-Driven Learning.' The abstract explicitly reports a large-scale study across 54 environments and demonstrates limitations of prediction-based rewards in stochastic setups.

### c39 — exists ✅ · applied ✅  (line 272)
_OMNI uses a language model as a model of what *humans* find interesting, to choose what an agent should learn next ([Zhang et al. 2024](https://arxiv.org/abs/2306.01711))._
- claude: exists=verified applied=verified [evidence_text] — OMNI (Zhang et al.) confirmed; abstract uses foundation models as a model of human notions of interestingness to select tasks, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Zhang et al.'s OMNI paper. The abstract directly says OMNI uses foundation models as models of human notions of interestingness to prioritize which tasks an agent should learn next.
