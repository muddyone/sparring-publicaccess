# cite-check report — piece-04-own-work

_Public-copy note: "unchecked" verdicts on the author's own published report are failed lookups, not wrong sources: its DOI is a Zenodo concept DOI, which resolves to the latest version's record number ([Paper 1](https://doi.org/10.5281/zenodo.21210264)). The figures were checked by hand against the report (see the [cite-check index](README.md))._

**Source:** `positions/04-personality.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **28** citations checked
- existence independently confirmed: **25**
- application evidence-grounded: **16**
- application judged from model knowledge only: **10**
- not independently checkable: **1**
- buckets — clean **6** · problem **25** · disagree **6**

## ⛔ DISAGREE — escalate to human (6)
### c01 — exists ✅ · applied SPLIT  (line 19)
_([Van den Broeck et al. 2016](https://doi.org/10.1177/0149206316632058))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the SDT meta-analysis of 99 studies on relatedness/need satisfaction at work; abstract confirms correlational meta-analysis supporting the claim about connection and workplace outcomes.
- gpt: exists=verified applied=unchecked [evidence_text] — The DOI resolves via Crossref to Van den Broeck et al.'s 2016 Journal of Management meta-analytic review of 99 studies. The abstract confirms the broad topic and study count but does not provide the specific outcome pattern for commitment, satisfaction, engagement, burnout, or task performance.

### c06 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 34)
_([Roesler et al. 2021](https://doi.org/10.1126/scirobotics.abj5425))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Meta-analysis on anthropomorphism in HRI confirmed; abstract too brief to verify specifics but title and my knowledge support the favorable-perception/no-performance-gain claim.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref verifies the Science Robotics meta-analysis on anthropomorphism in HRI. The retrieved abstract is only a one-sentence description and does not confirm the 78-study count, mostly single-session characterization, favorable-view effects, or lack of task-performance gain.

### c08 — exists ⚠️ · applied SPLIT  (line 45)
_([my published report](https://doi.org/10.5281/zenodo.21210264), sections 6 and 7)_
- **escalate:** application: verified vs unchecked
- claude: exists=nuance applied=verified [evidence_text] — The Zenodo DOI resolves to a self-authored pre-registered report on adversarial AI review matching the described content, though the DOI redirected to a different record number and Crossref didn't index it. Claims are plausibly the author's own pilot results as noted.
- gpt: exists=nuance applied=unchecked [no_basis] — The DOI URL resolves to a Zenodo record with a relevant report-like title, but the DOI appears to redirect to a different record number and Crossref did not verify the cited DOI. No retrieved text from the report's sections 6 and 7 supports the specific pilot-result percentages.

### c09 — exists ✅ · applied SPLIT  (line 49)
_([Bickmore, Schulman & Yin 2010](https://doi.org/10.1080/08839514.2010.492259))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Confirmed as the Bickmore relational-agents engagement paper with two longitudinal RCTs; abstract confirms engagement manipulations but not the specific walking/adherence figures, so partial support.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and Europe PMC verify the article and DOI. The abstract confirms two longitudinal randomized experiments on engagement with relational agents, but it does not state the specific results about logins, enjoyment, desire to continue, exercise, or walking.

### c28 — exists SPLIT · applied ☐  (line 130)
_the warmth study shows candor drifts_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Bare in-text reference with no identifiable source metadata and no crossref match, so neither axis can be judged.
- gpt: exists=refuted applied=unchecked [no_basis] — No bibliographic details are provided and the lookup produced no match for a work identifiable as 'the warmth study.' With no identified source text, the application cannot be assessed.

### c31 — exists SPLIT · applied ☐  (line 135)
_the benefits in the long-term trials came from small acts like greetings and continuity_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Bare reference with no identifiable source metadata and no crossref match; neither axis judgeable.
- gpt: exists=refuted applied=unchecked [no_basis] — No identifiable bibliographic reference is provided and the lookup returned no match. With no source text or identified work, the application cannot be judged.

## ⚠️ AGREE-problem (25)
### c02 — exists ✅ · applied ✅  · ⚑ degraded  (line 21)
_([Ozcelik & Barsade 2018](https://doi.org/10.5465/amj.2015.1066))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the loneliness-and-job-performance field study; no abstract retrieved but the title and my knowledge support the lower supervisor ratings for lonely employees claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI, title, authors, journal, and year. No abstract/source text was retrieved, but from model knowledge the AMJ article reports a field study linking workplace loneliness to later supervisor-rated job performance, consistent with the claim.

### c03 — exists ⚠️ · applied ✅  (line 23)
_([Methot et al. 2016](https://doi.org/10.1111/peps.12109))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms workplace friendships are a 'mixed blessing' with performance benefits offset by maintenance costs, matching the claim.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI and metadata match Methot et al.'s Personnel Psychology article, though Crossref gives 2015 while the citation says 2016. The abstract directly describes workplace friendships as a mixed blessing, improving performance through positive mechanisms while imposing emotional exhaustion/maintenance costs.

### c04 — exists ⚠️ · applied ✅  (line 25)
_([Chung et al. 2018](https://doi.org/10.1177/0146167217733069))_
- claude: exists=verified applied=verified [evidence_text] — Abstract explicitly states friendship groups outperform on high-quantity-output tasks but not single/high-quality-output tasks, matching the claim closely.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI and article metadata match Chung et al., though Crossref lists 2017 while the citation says 2018. The abstract directly states friendship groups outperform acquaintance groups for high-quantity-output tasks, with no benefit for single/high-quality-output tasks.

### c05 — exists ✅ · applied ⚠️  (line 29)
_([Bickmore & Picard 2005](https://doi.org/10.1145/1067860.1067867))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the 101-user month-long trial where the relational agent was liked more and users wanted to continue, supporting both claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the Bickmore and Picard TOCHI article. The abstract supports the 101-user month-long trial and greater liking, bonding-adjacent evaluations, trust, and desire to continue, but the broader phrasing that social cues 'reliably' make people like assistants more is stronger than this single study alone establishes.

### c07 — exists ✅ · applied ⚠️  (line 37)
_([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888))_
- claude: exists=verified applied=verified [evidence_text] — Title and venue confirm the persona-in-system-prompts study finding personas do not improve LLM performance, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI and ACL Anthology page verify the paper and title. The retrieved snippet/title supports the general point that personas in system prompts did not improve LLM performance, but it does not confirm the specific 162-role, four-model-family, factual-question details.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 65)
_the philosopher Daniel Dennett argued in his 1987 book _The Intentional Stance__
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dennett's 1987 The Intentional Stance; the intentional-stance thesis as described matches the book's well-known argument.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library verifies Dennett's 1987 book The Intentional Stance. No source text was retrieved, but from model knowledge the intentional stance is Dennett's strategy of predicting complex systems by treating them as agents with beliefs/desires when that strategy works economically.

### c12 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 69)
_[Clark & Brennan 1991](https://doi.org/10.1037/10096-006)_
- claude: exists=verified applied=verified [model_knowledge_only] — Confirmed as Clark & Brennan's 'Grounding in communication'; the common-ground/shared-shorthand claim aligns with the chapter's central argument.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies Clark and Brennan's 1991 chapter 'Grounding in communication.' No source text was retrieved, but from model knowledge the chapter supports common ground and coordination in communication; the specific 'long collaborations build shorthand' wording is a plausible but somewhat imprecise extension.

### c13 — exists ☐ · applied ☐  (line 71)
_[see the learning essay](../positions/02-it-learns.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited internal cross-reference, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not an external citation but an internal cross-reference. Per instructions, both axes are left unchecked.

### c14 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 73)
_[Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953)_
- claude: exists=verified applied=verified [model_knowledge_only] — Confirmed as Hatfield et al.'s 'Emotional Contagion'; supports the claim that a partner's tone spreads, though the mood-as-signal part is more Schwarz & Clore's contribution.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies Hatfield, Cacioppo, and Rapson's 1993 'Emotional Contagion' article. No source text was retrieved, but from model knowledge it supports the emotional-contagion half of the claim, not the mood-as-information half.

### c15 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 74)
_[Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513)_
- claude: exists=verified applied=verified [model_knowledge_only] — Confirmed as Schwarz & Clore's mood-as-information paper; supports the claim about reading one's mood as a signal about how things are going.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies Schwarz and Clore's 1983 article on mood, misattribution, and judgments of well-being. No source text was retrieved, but from model knowledge it supports the mood-as-information half of the claim, not the partner-tone contagion half.

### c18 — exists ☐ · applied ☐  (line 84)
_Clippy, the animated paperclip in old versions of Microsoft Office, is the standing lesson, though the evidence there is mostly anecdotal_
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation (anecdotal Clippy mention); flagged is_citation=false.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and has no retrieved evidence. Per instructions, both axes are left unchecked.

### c20 — exists ✅ · applied ⚠️  (line 95)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0), _Nature__
- claude: exists=verified applied=verified [evidence_text] — Nature abstract confirms training for warmth reduces accuracy, increases validation of false beliefs especially when users express sadness, and effects evaded standard benchmarks—supporting all claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Nature URL verify the 2026 Nature article. The abstract supports reduced accuracy, increased validation of false beliefs/sycophancy under warmth training, sadness-related vulnerability effects, and standard benchmarks missing the issue, but it does not mention the additional claim about instruction-only warmth producing smaller and less consistent effects.

### c21 — exists ✅ · applied ⚠️  (line 98)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- claude: exists=verified applied=nuance [evidence_text] — Edmondson 1999 confirmed; abstract directly supports psychological safety as shared belief for interpersonal risk taking. The second claim (safety ≠ cohesion, closeness can reduce dissent) is not addressed in the abstract, so partial support.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies Edmondson's 1999 Administrative Science Quarterly article with DOI 10.2307/2666999. The abstract directly supports the definition of team psychological safety as a shared belief that interpersonal risk taking is safe, but the retrieved text does not address the cohesion/closeness-disagreement distinction.

### c22 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 99)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- claude: exists=verified applied=verified [model_knowledge_only] — Pillemer & Rothbard 2018 'Friends Without Benefits' confirmed; no abstract retrieved, but the paper's focus on dark sides of workplace friendship plausibly supports the claim that friends hesitate to challenge friends.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the article 'Friends Without Benefits: Understanding the Dark Sides of Workplace Friendship' by Pillemer and Rothbard. No abstract or source text was retrieved, so the application is judged only from general knowledge and the claim is plausible but not directly evidenced here.

### c24 — exists ☐ · applied ☐  (line 115)
_Replication failures for the warmth–accuracy trade-off. It is one published study, and no one has yet repeated it to see whether the result holds._
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited; listed as evidence that does not yet exist (hypothetical replication).
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited, describing evidence that does not yet exist. Both axes are therefore unchecked.

### c26 — exists ☐ · applied ☐  (line 123)
_[the essay on whether AI is conscious](../positions/03-someone-there.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal essay cross-reference; local markdown file could not be fetched, so neither axis is judgeable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The referenced internal Markdown file could not be checked because the URL type was unknown. No source text was retrieved, so the application cannot be judged.

### c27 — exists ✅ · applied ✅  · ⚑ degraded  (line 125)
_in Book Eight of the _Nicomachean Ethics__
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Nicomachean Ethics confirmed via Open Library; Book VIII discusses the three types of friendship, and Aristotle indeed holds goodwill is required in all, supporting the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library verifies the existence of Aristotle's Nicomachean Ethics. No passage text was retrieved, but from general knowledge Book VIII does describe friendship as involving mutual goodwill, including friendships of utility and pleasure.

### c29 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 132)
_in a study whose plan was fixed before it ran ([Kim et al. 2024](https://doi.org/10.1145/3630106.3658941))_
- claude: exists=verified applied=verified [model_knowledge_only] — Kim et al. 2024 on LLM uncertainty expression confirmed; title directly matches, and the paper examines how uncertainty expressions reduce reliance/trust, supporting the claim though no abstract was retrieved.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the ACM FAccT 2024 paper with the stated DOI and title. No abstract or full text was retrieved, so the specific result about reduced trust in wrong answers is plausible from general knowledge of the paper but not directly evidenced here.

### c30 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 134)
_([Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633))_
- claude: exists=verified applied=verified [model_knowledge_only] — Völkel & Kaya 2021 on agreeableness in chatbots confirmed; the study examines preference for agreeableness levels, consistent with preferring moderate over extreme personalities, though no abstract confirms the specific framing.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the CUI 2021 paper 'Examining User Preference for Agreeableness in Chatbots.' No abstract or source text was retrieved, and the claim broadens the likely finding about agreeableness into 'moderate personalities' generally.

### c32 — exists ☐ · applied ☐  (line 147)
_[the overview](../positions/00-the-thing-on-the-other-end.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; internal cross-reference, not a research citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a research citation, but an internal overview cross-reference. Both axes are therefore unchecked.

### c33 — exists ☐ · applied ☐  (line 149)
_[Personality and connection](../personality-and-connection.md), a longer summary of the research with its sources_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; source-list reference, not an in-text claim citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not an in-text claim citation, but a source-list or internal report reference. Both axes are therefore unchecked.

### c34 — exists ☐ · applied ☐  (line 153)
_([report](../cite-check/2026-10-17-position-pieces.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; cite-check process metadata link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a research citation, but a cite-check report link. Both axes are therefore unchecked.

### c35 — exists ☐ · applied ☐  (line 155)
_([review records](../panel/2026-10-18-piece-04-personality/))_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; panel review process metadata link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a research citation, but a panel review records link. Both axes are therefore unchecked.

### c36 — exists ☐ · applied ☐  (line 156)
_[check after review](../cite-check/2026-10-18-piece-04-personality-after-panel.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; post-review cite-check process metadata link.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a research citation, but a post-review cite-check link. Both axes are therefore unchecked.

### c37 — exists ☐ · applied ☐  (line 161)
_[the report](../personality-and-connection.md). Dennett 1987 and Aristotle's _Nicomachean Ethics_ (VIII–IX) are cited there in full._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; report link with no in-text claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a direct claim citation, but an internal report reference noting where full references are located. Both axes are therefore unchecked.

## ✅ AGREE-clean (6)
### c10 — exists ✅ · applied ✅  (line 57)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the n=981 four-week RCT with neutral/engaging voice conditions and no significant effects on loneliness or emotional dependence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv verifies the 2025 preprint and URL. The abstract directly reports a four-week RCT with n=981 testing text, neutral voice, and engaging voice conditions and finding no significant effects of experimental conditions on loneliness or emotional dependence/problematic use outcomes.

### c16 — exists ✅ · applied ✅  (line 79)
_[Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms individuals differ in desire to integrate/segment work and nonwork, and fit/mismatch affects satisfaction and commitment, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Organization Science article by Rothbard, Phillips, and Dumas. The abstract directly supports individual differences in desired integration/segmentation and fit effects on satisfaction and commitment, with the caveat already noted that this concerns work-family boundaries rather than AI.

### c17 — exists ✅ · applied ✅  (line 80)
_[Kreiner 2006](https://doi.org/10.1002/job.386)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms person-environment fit between segmentation preference and workplace provision affects job satisfaction, matching the mismatch-lowers-satisfaction claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies Kreiner's Journal of Organizational Behavior article. The abstract directly states that fit between work-home segmentation preference and perceived workplace segmentation affects work-home conflict, stress, and job satisfaction.

### c19 — exists ✅ · applied ✅  (line 88)
_[De Freitas et al. 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms emotionally manipulative farewell prompts in companion apps boost engagement while also elevating perceived manipulation, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv verifies the 2025 preprint 'Emotional Manipulation by AI Companions.' The abstract directly reports farewell-based emotional manipulation tactics in companion apps that increase engagement while also increasing perceived manipulation and related negative reactions.

### c23 — exists ✅ · applied ✅  (line 101)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352), _Science__
- claude: exists=verified applied=verified [evidence_text] — Cheng et al. 2026 Science confirmed; abstract states sycophantic models were trusted/preferred and even a single interaction reduced willingness to repair conflicts, supporting both claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science article and DOI metadata. The abstract directly states that sycophantic models were trusted and preferred, drove engagement, and that even a single interaction reduced willingness to repair interpersonal conflicts.

### c25 — exists ✅ · applied ✅  (line 118)
_[Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058)_
- claude: exists=verified applied=verified [evidence_text] — Hennig-Thurau et al. 2006 confirmed; abstract explicitly states extent of smiling did not influence customer emotions while authenticity did, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Marketing article and DOI metadata. The abstract supports the claim that smiling extent did not influence customer emotions, while authenticity of emotional labor display did.
