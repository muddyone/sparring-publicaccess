# cite-check report — p04-personality

**Source:** `positions/04-personality.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **27** citations checked
- existence independently confirmed: **23**
- application evidence-grounded: **14**
- application judged from model knowledge only: **9**
- not independently checkable: **4**
- buckets — clean **5** · problem **24** · disagree **3**

## ⛔ DISAGREE — escalate to human (3)
### c06 — exists ✅ · applied SPLIT  (line 37)
_([Roesler et al. 2021](https://doi.org/10.1126/scirobotics.abj5425))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI matches the anthropomorphism HRI meta-analysis. Abstract is minimal; the specific figures (78 studies, favorable perception but no performance gain) are plausible but not confirmed in retrieved text.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI and metadata confirm the Science Robotics meta-analysis exists. The retrieved abstract only says the meta-analysis quantifies anthropomorphism in HRI and does not provide the claimed 78-study count, favorable-view result, or null task-performance result.

### c08 — exists ✅ · applied SPLIT  (line 45)
_([Bickmore, Schulman & Yin 2010](https://doi.org/10.1080/08839514.2010.492259))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Bickmore relational agents engagement paper with two longitudinal RCTs. Abstract confirms two trials on engagement; the specific sample sizes and decreased walking outcome are not in the abstract.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI and Europe PMC metadata confirm the Bickmore, Schulman, and Yin article exists. The retrieved abstract mentions two longitudinal randomized experiments on engagement but does not give the claimed results about logins, enjoyment, continuation desire, exercise, sample sizes, or reduced walking.

### c19 — exists ✅ · applied SPLIT  (line 93)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — DOI matches Edmondson (1999), the foundational psychological-safety paper. Abstract introduces the construct and distinguishes it from team efficacy, but the specific claims about cohesion vs safety and disagreement are not explicit in the retrieved abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Edmondson's 1999 Administrative Science Quarterly article. The retrieved abstract defines team psychological safety and links it to learning behavior, but it does not address cohesion or whether cohesion reduces disagreement.

## ⚠️ AGREE-problem (24)
### c01 — exists ✅ · applied ⚠️  (line 22)
_([Van den Broeck et al. 2016](https://doi.org/10.1177/0149206316632058))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the SDT meta-analysis of 99 studies. Abstract confirms meta-analysis of need satisfaction (incl. relatedness) and outcomes; the specific outcome list (commitment, engagement, burnout, task performance) is plausible for this review but not spelled out in the abstract.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI resolves to the 2016 Journal of Management meta-analytic review by Van den Broeck et al. The abstract confirms a 99-study meta-analysis of basic psychological need satisfaction at work, including relatedness, but it does not specifically enumerate commitment, satisfaction, engagement, burnout, or task-performance effect sizes.

### c02 — exists ✅ · applied ✅  · ⚑ degraded  (line 24)
_([Ozcelik & Barsade 2018](https://doi.org/10.5465/amj.2015.1066))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to the Ozcelik & Barsade workplace loneliness/job performance paper. No abstract retrieved; from knowledge, the study found loneliness linked to lower supervisor-rated performance, consistent with the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, and year. No abstract or source text was retrieved, but from model knowledge the article reports a field study of workplace loneliness predicting later supervisor-rated job performance.

### c03 — exists ⚠️ · applied ✅  (line 26)
_([Methot et al. 2016](https://doi.org/10.1111/peps.12109))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the workplace friendships 'mixed blessing' paper. Abstract supports that friendships aid performance but with depleting upkeep costs.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI resolves to the Methot et al. Personnel Psychology article, though Crossref lists year 2015 while the citation uses 2016. The abstract directly supports the claim that workplace friendships are a mixed blessing, improving performance through resources such as trust/positive affect while imposing costs such as emotional exhaustion and maintenance difficulty.

### c04 — exists ⚠️ · applied ✅  (line 28)
_([Chung et al. 2018](https://doi.org/10.1177/0146167217733069))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the friendship/group-performance meta-analysis. Abstract directly states benefit on high-quantity-output tasks but not single/high-quality-output tasks, matching the claim precisely.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI resolves to the cited article, though Crossref lists 2017 while the citation uses the 2018 volume/issue year. The abstract directly states that friendship groups outperform acquaintance groups on high-quantity-output tasks, with no benefit on single or high-quality-output tasks.

### c07 — exists ✅ · applied ⚠️  (line 40)
_([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888))_
- claude: exists=verified applied=verified [evidence_text] — DOI and URL confirm the personas/system-prompts paper. Title and snippet confirm personas do not improve LLM performance; the specific count (162 roles, four families) is not in the snippet but consistent with the paper.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI and ACL Anthology page confirm the EMNLP Findings paper exists. The retrieved title/snippet supports the broad claim that personas in system prompts do not improve LLM performance, but it does not verify the details about 162 prompts, four model families, or factual-question accuracy.

### c10 — exists ☐ · applied ☐  (line 14)
_[its own piece](../positions/05-relationships.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; internal cross-reference to another piece, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and is an internal cross-reference to another piece. Per instruction, both axes are left unchecked.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 64)
_Dennett 1987, _The Intentional Stance__
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dennett's The Intentional Stance (1987). The intentional-stance idea (treating systems as agents for predictive economy) matches the claim per known content.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Daniel C. Dennett's The Intentional Stance from 1987. No source text was retrieved, but from model knowledge the intentional stance is the strategy of predicting complex systems by treating them as agents with beliefs, desires, or aims when that model works.

### c12 — exists ✅ · applied ✅  · ⚑ degraded  (line 68)
_[Clark & Brennan 1991](https://doi.org/10.1037/10096-006)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Clark & Brennan 'Grounding in communication' (1991). The grounding framework supports that collaborators develop shared conventions/shorthand over time.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Clark and Brennan's 1991 chapter “Grounding in communication.” No source text was retrieved, but from model knowledge the chapter concerns common ground and coordination in communication, which supports the idea that repeated collaboration enables shared shorthand.

### c13 — exists ☐ · applied ☐  (line 70)
_[see the learning piece](../positions/02-it-learns.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to another local markdown file; not externally checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only supplied URL is a local Markdown filename that could not be fetched, so existence is not checkable from the evidence. No source text supports the claim about assistants remembering across conversations.

### c14 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 72)
_[Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953)_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Hatfield et al. 'Emotional Contagion' (1993). Supports that a partner's emotional tone spreads to oneself (contagion), the first half of the claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms Hatfield, Cacioppo, and Rapson's 1993 article “Emotional Contagion.” No abstract was retrieved; from model knowledge it supports the tone/mood-spread part of the claim, but not the separate mood-as-information judgment claim.

### c15 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 73)
_[Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513)_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Schwarz & Clore (1983) mood-as-information paper. Supports the 'read your mood as a signal' portion of the claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms Schwarz and Clore's 1983 article on mood, misattribution, and judgments of well-being. No source text was retrieved; from model knowledge it supports the idea that people use mood as information in judgments, but not the emotional-contagion part of the combined claim.

### c18 — exists ✅ · applied ⚠️  (line 89)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0), _Nature__
- claude: exists=verified applied=verified [evidence_text] — DOI and URL confirm the Nature warmth/accuracy paper. Abstract supports reduced accuracy when trained for warmth, worse when users express sadness, and increased validation of false beliefs; prompt-only effects not detailed in abstract but consistent.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Nature URL confirm the article and DOI. The abstract supports the main claims that warmer models had higher error rates, more validation of false beliefs especially under sadness, and preserved standard-benchmark performance, but it does not verify the prompt-only warmth manipulation or the exact “content held constant” framing.

### c20 — exists ✅ · applied ✅  · ⚑ degraded  (line 94)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Pillemer & Rothbard 'Friends Without Benefits' on dark sides of workplace friendship. The claim that friends hesitate to challenge friends aligns with the paper's thesis per title/known content.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Pillemer and Rothbard's 2018 Academy of Management Review article “Friends Without Benefits.” No source text was retrieved, but from model knowledge the article discusses dark sides of workplace friendship, including constraints on candor and challenge among friends.

### c21 — exists ✅ · applied ⚠️  (line 97)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352), _Science__
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Cheng et al. Science paper; abstract confirms sycophantic AI reduced willingness to repair conflict yet was trusted/preferred, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the Science article with DOI 10.1126/science.aec8352 and matching title/authors. The abstract supports reduced willingness to repair conflicts after one interaction and preference/trust/engagement, though the exact wording 'rate higher' and 'want to come back' is more specific than the retrieved abstract.

### c22 — exists ☐ · applied ☐  (line 110)
_A long-term study, over months, showing a user-set personality improves results... I know of none._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author explicitly states no such study exists.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is deliberately uncited/non-citation material stating the author knows of no such study. Per instruction, both axes are left unchecked.

### c24 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 125)
_([Kim et al. 2024](https://doi.org/10.1145/3630106.3658941))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Kim et al. 2024 FAccT paper on LLM uncertainty expression; title supports that first-person uncertainty affects user reliance, consistent with the claim, though no abstract retrieved.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the ACM FAccT 2024 paper with the stated DOI and matching title. No abstract or full text was retrieved, so the application judgment relies only on model knowledge and the claim is plausible but not fully checkable from the provided evidence.

### c25 — exists ✅ · applied ☐  · ⚑ degraded  (line 129)
_([Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633))_
- claude: exists=verified applied=unchecked [model_knowledge_only] — DOI matches Völkel & Kaya 2021 chatbot agreeableness study; no abstract retrieved to confirm the specific 'moderate over extreme personalities' finding.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the CUI 2021 paper with DOI 10.1145/3469595.3469633 and matching authors/title. No abstract, snippet, or full text was retrieved, so the claim about preference for moderate rather than extreme personalities cannot be judged from the evidence.

### c26 — exists ☐ · applied ☐  (line 133)
_the piece on whether anyone is there](03-someone-there.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local markdown file; not fetchable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The referenced local Markdown path could not be fetched and is marked not-checkable. No source text was retrieved to assess whether it supports the claim.

### c27 — exists ✅ · applied ✅  · ⚑ degraded  (line 134)
_(_Nicomachean Ethics_ VIII)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Nicomachean Ethics confirmed via Open Library; Book VIII indeed holds that all three friendship types require mutual goodwill (eunoia), matching the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Aristotle's Nicomachean Ethics exists, though the metadata match is broad/fuzzy. No relevant text was retrieved, but from model knowledge Book VIII defines friendship in terms of reciprocal recognized goodwill, including friendships of utility and pleasure.

### c28 — exists ☐ · applied ☐  (line 148)
_[the overview](../positions/00-the-thing-on-the-other-end.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked non-citation pointer to an overview; not a supporting claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a supporting citation. Per instruction, both axes are left unchecked.

### c29 — exists ☐ · applied ☐  (line 150)
_[Personality and connection](../personality-and-connection.md), a summary of the research with its sources, and adds no new sources._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal self-reference to a local markdown summary; not fetchable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The referenced relative Markdown path could not be fetched and is marked not-checkable. No text was retrieved to verify either the existence of the report or the claim about its contents.

### c30 — exists ☐ · applied ☐  (line 153)
_([report](../cite-check/2026-10-17-position-pieces.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked non-citation internal cite-check report link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a supporting citation. Per instruction, both axes are left unchecked.

### c31 — exists ☐ · applied ☐  (line 155)
_([review records](../panel/2026-10-18-piece-04-personality/))_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked non-citation internal panel review records link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a supporting citation. Per instruction, both axes are left unchecked.

### c32 — exists ☐ · applied ☐  (line 160)
_[the report](../personality-and-connection.md). Dennett 1987 and Aristotle's _Nicomachean Ethics_ (VIII–IX) are cited there in full._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal reference to a local report file; not fetchable, so the pointer cannot be verified.
- gpt: exists=unchecked applied=unchecked [no_basis] — The referenced relative Markdown path could not be fetched and is marked not-checkable. No source text was retrieved to verify the claimed contents of the report.

## ✅ AGREE-clean (5)
### c05 — exists ✅ · applied ✅  (line 32)
_([Bickmore & Picard 2005](https://doi.org/10.1145/1067860.1067867))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Bickmore & Picard relational agents paper. Abstract confirms the month-long trial with 101 users, greater liking/trust, and greater desire to continue, supporting both claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the ACM TOCHI article by Bickmore and Picard. The abstract reports a month-long controlled experiment with 101 users in which a relational agent was liked, respected, and trusted more and users had a greater desire to continue using it.

### c09 — exists ✅ · applied ✅  (line 57)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches the four-week RCT (n=981) varying interaction mode including neutral vs engaging voice. Abstract confirms no significant effects of conditions on loneliness or emotional dependence.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL confirm the 2025 preprint exists. The abstract directly reports a four-week randomized controlled experiment with n=981 comparing text, neutral voice, and engaging voice, with no significant effects of experimental conditions on outcomes including loneliness and emotional dependence.

### c16 — exists ✅ · applied ✅  (line 77)
_[Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Rothbard, Phillips & Dumas (2005). Abstract confirms individual differences in integration/segmentation desire and fit effects on satisfaction/commitment, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Rothbard, Phillips, and Dumas Organization Science article. The abstract directly supports individual differences in desired work/nonwork segmentation and shows that fit between preferences and boundary-management policies affects satisfaction and commitment.

### c17 — exists ✅ · applied ✅  (line 78)
_[Kreiner 2006](https://doi.org/10.1002/job.386)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Kreiner (2006). Abstract confirms person-environment fit of segmentation preference affects conflict, stress, and job satisfaction, supporting the mismatch claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms Kreiner's Journal of Organizational Behavior article. The abstract directly states that the interaction between work-home segmentation preference and perceived workplace segmentation affects work-home conflict, stress, and job satisfaction.

### c23 — exists ✅ · applied ✅  (line 116)
_[Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Hennig-Thurau et al. 2006 Journal of Marketing study; abstract confirms extent of smiling did not affect customers while authenticity did.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the 2006 Journal of Marketing article with DOI 10.1509/jmkg.70.3.058. The abstract directly says smiling extent did not influence customer emotions, while authenticity of emotional labor display directly affected customers' emotional states.
