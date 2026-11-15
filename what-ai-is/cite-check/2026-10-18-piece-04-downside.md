# cite-check report — piece-04-downside

**Source:** `positions/04-personality.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **28** citations checked
- existence independently confirmed: **25**
- application evidence-grounded: **15**
- application judged from model knowledge only: **9**
- not independently checkable: **3**
- buckets — clean **5** · problem **25** · disagree **4**

## ⛔ DISAGREE — escalate to human (4)
### c01 — exists ✅ · applied SPLIT  (line 19)
_Van den Broeck et al. 2016 (https://doi.org/10.1177/0149206316632058)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the correct SDT meta-analysis of 99 studies; abstract supports a correlational review of need satisfaction linked to well-being outcomes, consistent with the claim and author note.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref directly matches the DOI to Van den Broeck et al.'s 2016 Journal of Management review/meta-analysis of 99 studies. The abstract confirms a meta-analytic review of basic need satisfaction at work, but does not provide the specific outcome pattern claimed for commitment, satisfaction, engagement, burnout, or task performance.

### c06 — exists ✅ · applied SPLIT  (line 34)
_Roesler et al. 2021 (https://doi.org/10.1126/scirobotics.abj5425)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI matches the anthropomorphism meta-analysis; abstract is terse but the title and framing support the claim, which aligns with this paper's known finding of favorable perception without performance gains.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref directly matches the DOI to Roesler, Manzey, and Onnasch's 2021 Science Robotics meta-analysis. The retrieved abstract only says the paper quantifies when anthropomorphic robot features facilitate HRI, and does not state the number of studies, attitude effects, session length, or task-performance result.

### c08 — exists ✅ · applied SPLIT  (line 42)
_Bickmore, Schulman & Yin 2010 (https://doi.org/10.1080/08839514.2010.492259)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI matches Bickmore, Schulman & Yin; abstract confirms two longitudinal RCTs on engagement manipulations, consistent with the claims about raised engagement but not exercise outcomes.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and Europe PMC confirm the DOI and title for Bickmore, Schulman, and Yin's 2010 article. The retrieved abstract says only that two longitudinal randomized experiments assessed engagement manipulations, without the specific login, enjoyment, continuation, exercise, sample-size, or walking outcomes claimed.

### c27 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 127)
_people preferred moderate personalities to extreme ones ([Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — Paper on user preference for chatbot agreeableness exists; without abstract, the specific claim that moderate personalities were preferred over extremes is plausible but not confirmed.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the CUI 2021 paper on user preference for agreeableness in chatbots. No abstract or text was retrieved, and the metadata alone is insufficient to judge whether it supports the specific claim about preferring moderate rather than extreme personalities.

## ⚠️ AGREE-problem (25)
### c02 — exists ✅ · applied ✅  · ⚑ degraded  (line 21)
_Ozcelik & Barsade 2018 (https://doi.org/10.5465/amj.2015.1066)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Confirmed as Ozcelik & Barsade's loneliness and job performance study; no abstract retrieved, but the claim about a field study linking loneliness to lower supervisor ratings matches this well-known paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref directly matches the DOI to Ozcelik and Barsade's 2018 Academy of Management Journal article. No abstract or source text was retrieved, but based on model knowledge the article reports workplace loneliness predicting lower supervisor-rated performance in a field study of 672 employees.

### c03 — exists ⚠️ · applied ✅  (line 23)
_Methot et al. 2016 (https://doi.org/10.1111/peps.12109)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Methot et al. on workplace friendships; abstract frames friendships as a 'mixed blessing' with benefits offset by maintenance costs, directly supporting the claim (note year is 2015/2016).
- gpt: exists=nuance applied=verified [evidence_text] — The DOI matches the Methot et al. Personnel Psychology article, though the retrieved metadata lists 2015 rather than the cited 2016 year. The abstract directly supports the mixed-blessing claim: workplace friendships are associated with performance benefits but also costs via emotional exhaustion or maintenance difficulty.

### c04 — exists ⚠️ · applied ✅  (line 25)
_Chung et al. 2018 (https://doi.org/10.1177/0146167217733069)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the friendship-group meta-analysis; abstract explicitly states friendship benefits tasks requiring high quantity of output but not single/high-quality output, matching the claim.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI matches the Chung et al. article, though the retrieved metadata gives 2017 while the citation uses 2018. The abstract directly states that friendship groups outperform acquaintance groups on high-quantity-output tasks, with no benefit for single or high-quality-output tasks.

### c05 — exists ✅ · applied ⚠️  (line 29)
_Bickmore & Picard 2005 (https://doi.org/10.1145/1067860.1067867)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Bickmore & Picard; abstract confirms the month-long 101-user trial where the relational agent was liked/trusted more and users wanted to continue, supporting both claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref directly matches the DOI to Bickmore and Picard's 2005 ACM TOCHI article. The abstract supports the month-long 101-user trial and greater liking, trust, respect, and desire to continue for a relational agent, but the broader wording about personality/social cues reliably improving assistants is a generalization beyond the abstract.

### c07 — exists ✅ · applied ⚠️  (line 37)
_Zheng et al. 2024 (https://doi.org/10.18653/v1/2024.findings-emnlp.888)_
- claude: exists=verified applied=verified [evidence_text] — DOI and URL confirm the persona study; the title itself ('Personas...Do Not Improve Performances') supports the claim that role prompts did not improve accuracy.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the ACL Anthology URL confirm the 2024 Findings of EMNLP paper. The retrieved title/snippet supports the broad claim that personas in system prompts do not improve LLM performance, but not the specific details about 162 prompts, four model families, or factual-question accuracy.

### c10 — exists ✅ · applied ✅  · ⚑ degraded  (line 58)
_the philosopher Daniel Dennett argued in his 1987 book _The Intentional Stance__
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dennett's 1987 The Intentional Stance; the claim about adopting an agentive stance as an economical predictive strategy is the book's central thesis.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches Daniel C. Dennett's 1987 book The Intentional Stance. No source text was retrieved, but based on model knowledge Dennett's intentional stance is the strategy of predicting complex systems by treating them as agents with beliefs, desires, and rational aims when that is the most effective predictive model.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 62)
_([Clark & Brennan 1991](https://doi.org/10.1037/10096-006))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Clark & Brennan 'Grounding in communication' (correct chapter); the claim about building shared common ground over collaboration aligns with grounding theory.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref directly matches the DOI to Clark and Brennan's 1991 chapter, “Grounding in communication.” No source text was retrieved, but based on model knowledge the chapter concerns common ground and grounding, including how shared understanding supports efficient shorthand in collaboration.

### c12 — exists ☐ · applied ☐  (line 64)
_([see the learning essay](../positions/02-it-learns.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal relative-path link to another essay that could not be fetched; not externally checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a relative local file path, and the lookup reports an unknown URL type, so existence cannot be checked from the evidence. No source text was retrieved to evaluate whether it supports the claim about assistants remembering across conversations.

### c13 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 66)
_([Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953)_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Hatfield et al. 'Emotional Contagion'; the claim that a partner's emotional tone spreads is the core of emotional contagion theory.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref directly matches the DOI to Hatfield, Cacioppo, and Rapson's 1993 “Emotional Contagion.” No source text was retrieved; based on model knowledge it supports emotional contagion or a partner's tone spreading, but not the separate mood-as-information part of the claim.

### c14 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 67)
_[Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches the classic Schwarz & Clore mood-as-information paper; the claim that one reads one's mood as a signal matches its affect-as-information thesis.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref directly matches the DOI to Schwarz and Clore's 1983 article on mood, misattribution, and judgments of well-being. No source text was retrieved; based on model knowledge it supports the idea that mood informs judgments, though applying this specifically to judging how work is going is an extrapolation.

### c17 — exists ☐ · applied ☐  (line 78)
_Clippy, the animated paperclip in old versions of Microsoft Office, is the standing lesson, though the evidence there is mostly anecdotal_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited; the Clippy reference is an intentional anecdote, not a formal citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and not a citation. Per instructions, both existence and application are unchecked.

### c19 — exists ✅ · applied ⚠️  (line 88)
_([Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0), _Nature_)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Nature warmth/sycophancy paper; abstract supports warmth reducing accuracy (especially with user sadness), increased validation of incorrect beliefs, and effects undetected by standard tests, covering the claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Nature URL confirm the DOI, title, authors, journal, and publication metadata. The abstract supports the main claims about warmth training reducing accuracy, increasing validation of false beliefs especially with sadness, and standard benchmarks missing the problem, but it does not mention the claim about instruction-only warmth producing smaller and less consistent effects.

### c20 — exists ✅ · applied ⚠️  (line 91)
_([Edmondson 1999](https://doi.org/10.2307/2666999))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Edmondson 1999, the foundational psychological safety paper; abstract confirms the construct as a shared belief about interpersonal risk, distinct from efficacy, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref directly matches the DOI to Edmondson's 1999 Administrative Science Quarterly article. The abstract directly supports the definition of team psychological safety as a shared belief that the team is safe for interpersonal risk taking, but the retrieved text does not support the additional claim about distinguishing it from cohesion or closeness reducing disagreement.

### c21 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 92)
_([Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to the real Pillemer & Rothbard 2018 paper on dark sides of workplace friendship. No abstract retrieved, but the paper's documented themes support the claim that friends hesitate to challenge friends.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, year, and pages for Pillemer and Rothbard's 2018 Academy of Management Review article. The specific claim is plausible for this article's argument about dark sides of workplace friendship, but no abstract or text was retrieved, so application is based only on model knowledge.

### c22 — exists ✅ · applied ⚠️  (line 94)
_([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352), _Science_)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms sycophantic AI was trusted/preferred (users rate higher, want to return) while reducing willingness to repair conflicts even after a single interaction.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the Science article and provides an abstract matching the DOI and authors. The abstract supports reduced willingness to repair conflicts and that sycophantic models were trusted/preferred and drove engagement, though 'rate higher' and 'want to come back' are slightly more specific phrasing than the abstract itself.

### c23 — exists ☐ · applied ☐  (line 108)
_It is one published study, and no one has yet repeated it to see whether the result holds._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and not a citation. Per instructions, both axes are unchecked.

### c25 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 117)
_For Aristotle, every friendship needs goodwill on both sides, even one built on use or pleasure (in Book Eight of the _Nicomachean Ethics_)._
- claude: exists=verified applied=verified [model_knowledge_only] — Nicomachean Ethics exists; Book VIII of the work does discuss friendship and the requirement of reciprocal goodwill across use/pleasure friendships, consistent with the claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Open Library confirms a work titled Nicomachean Ethics by Aristotle. The claim matches the standard reading of Book VIII that friendship requires reciprocal goodwill, including imperfect friendships of utility or pleasure, but no source text was retrieved and the formulation is somewhat simplified.

### c26 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 125)
_when the assistant voiced its own doubt, saying something like "I'm not sure, but...", people trusted its wrong answers less, in a study whose plan was fixed before it ran ([Kim et al. 2024](https://doi.org/10.1145/3630106.3658941))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to the Kim et al. 2024 FAccT paper on LLM uncertainty expression; title and topic support that expressed uncertainty reduced reliance/trust in wrong answers, though no abstract was retrieved.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the ACM FAccT 2024 paper with the quoted title and DOI. The application is plausible from the title and known topic, but no abstract or full text was retrieved to verify the specific wrong-answer/trust and preregistration claims.

### c28 — exists ☐ · applied ☐  (line 128)
_and the benefits in the long-term trials came from small acts like greetings and continuity._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; no reference provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and has no retrieved evidence. Per instructions, both axes are unchecked.

### c29 — exists ☐ · applied ☐  (line 142)
_It draws only on [Personality and connection](../personality-and-connection.md), a longer summary of the research with its sources, and adds no new sources._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited internal methodological note.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and not a citation. Per instructions, both axes are unchecked.

### c30 — exists ☐ · applied ☐  (line 144)
_It was checked on 17 October 2026 ([report](../cite-check/2026-10-17-position-pieces.md))._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; internal process note link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and has no retrieved evidence. Per instructions, both axes are unchecked.

### c31 — exists ☐ · applied ☐  (line 146)
_Reviewed by a panel and checked again on 18 October 2026 ([review records](../panel/2026-10-18-piece-04-personality/), [check after review](../cite-check/2026-10-18-piece-04-personality-after-panel.md))._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; internal process note link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and has no retrieved evidence. Per instructions, both axes are unchecked.

### c32 — exists ☐ · applied ☐  (line 152)
_Full references, verification marks and the cite-check record: [the report](../personality-and-connection.md). Dennett 1987 and Aristotle's _Nicomachean Ethics_ (VIII–IX) are cited there in full._
- claude: exists=unchecked applied=unchecked [no_basis] — Local markdown link could not be fetched; existence not checkable and no evidence to assess the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative URL could not be checked, and the existence status is not-checkable. No source text was retrieved to verify the claim that the report contains full references, verification marks, and the cite-check record.

### c33 — exists ☐ · applied ☐  (line 152)
_Dennett 1987_
- claude: exists=unchecked applied=unchecked [no_basis] — Open Library lookup failed with HTTP 500; existence not checkable from evidence, though Dennett 1987 (The Intentional Stance) is a known work. No claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup failed with an Open Library HTTP 500, and existence is marked not-checkable, so existence cannot be judged from retrieved evidence. There are no claims to assess for application.

### c34 — exists ✅ · applied ☐  (line 153)
_Aristotle's _Nicomachean Ethics_ (VIII–IX)_
- claude: exists=verified applied=unchecked [no_basis] — Nicomachean Ethics confirmed to exist; no specific claim attached to this reference to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library confirms a work titled Nicomachean Ethics by Aristotle. There are no claims attached to this citation to assess for application.

## ✅ AGREE-clean (5)
### c09 — exists ✅ · applied ✅  (line 50)
_Fang et al. 2025 (https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to the four-week RCT (n=981) with text/neutral/engaging voice conditions; abstract explicitly reports no significant effects from conditions on loneliness or dependence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the 2025 preprint and title. The abstract directly supports a four-week randomized experiment with n=981 testing text, neutral voice, and engaging voice modes, with no significant effects of experimental conditions on outcomes including loneliness and emotional dependence.

### c15 — exists ✅ · applied ✅  (line 72)
_([Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Rothbard, Phillips & Dumas; abstract confirms segmentation/integration preferences and fit effects on satisfaction/commitment, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly matches the DOI to Rothbard, Phillips, and Dumas's 2005 Organization Science article. The abstract directly supports individual differences in desired segmentation/integration and fit effects on satisfaction and commitment, with the caveat that the context is work–nonwork boundaries rather than AI.

### c16 — exists ✅ · applied ✅  (line 73)
_[Kreiner 2006](https://doi.org/10.1002/job.386))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Kreiner 2006; abstract confirms person-environment fit between segmentation preference and workplace provision affecting conflict, stress, and job satisfaction, supporting the mismatch claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly matches the DOI to Kreiner's 2006 Journal of Organizational Behavior article. The abstract directly states that the fit between work-home segmentation preference and perceived workplace segmentation affects work-home conflict, stress, and job satisfaction.

### c18 — exists ✅ · applied ✅  (line 81)
_([De Freitas et al. 2025](https://arxiv.org/abs/2508.19258))_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to De Freitas et al. 'Emotional Manipulation by AI Companions'; abstract confirms farewell prompts boost engagement while also elevating perceived manipulation, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the 2025 preprint “Emotional Manipulation by AI Companions.” The abstract directly supports that emotional goodbye prompts in companion apps increase engagement and also elevate perceived manipulation and related negative reactions.

### c24 — exists ✅ · applied ✅  (line 111)
_([Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms extent of smiling did not influence customer emotions while authenticity of the emotional display did, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the DOI, title, authors, journal, year, volume, issue, and pages. The retrieved abstract directly states that smiling extent did not influence customer emotions, while authenticity of emotional labor display directly affected customer emotional states.
