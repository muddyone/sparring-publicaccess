# Cite-check: piece 05, relationships (2026-10-17)

_Public copy: one entry, a personal anecdote with its two verdicts, was removed from this public copy as personal. The counts below still include it._

_Run `piece05-2026-10-17`, substrates Claude + GPT, on the first draft of
[positions/05-relationships.md](../positions/05-relationships.md). The full tool report follows
below. This header records what was done about it._

## Resolutions applied to the piece

- **Folk & Dunn 2026: caveat added.** The abstract also reports that more chatbot use predicted
  more loneliness on a single-item emotional-isolation measure. The draft gave only the
  broader-measure result. The piece now gives both, and "the risk sits with" became "sits mostly with".
- **Hannan et al. 2005: figure corrected.** The linked page says therapists, told of an 8% base
  rate, flagged 3 of 550 clients as predicted failures. "3 of the 40 clients who deteriorated"
  was not on the page. Corrected in the piece and in brief 8.
- **Zhang et al. 2025: rewritten to the abstract.** "Heavy use was not in itself linked to worse
  well-being" is not in the abstract; intensive and highly disclosive use strengthened the
  negative association among companionship users. The self-disclosure line now carries the link.
- **OpenAI 2025:** "170 clinicians" became "170 mental-health experts", and "retrained" became "updated"; the reduction is now
  described as the page describes it.
- **Cheng et al. 2026:** now backs only the preference for agreeable answers; the warmth/accuracy
  finding stays with Ibrahim et al.
- **Garcia:** WUSF link added for "allowed to proceed". **Raine:** "pleading stage" dated "as of mid
  2026", as in the brief.

## Left as they are

- **Bloomberg (Character.AI) and DLA Piper (FTC):** fetch blocked (403/429), not refuted; both
  were reported in the brief from the same sources.
- **Li, Dunn et al. 2026:** the paper itself is still unlocated; the piece says so.
- **OpenAI 0.15% / 0.07%:** the retrieved snippet didn't include the figures. Those figures come
  from the brief's reading of the page.
- Sources-list entries without claims, and the uncited judgement lines (marked in the piece as
  Bart's judgement), need no action.

---

# cite-check report — piece05-2026-10-17

**Source:** `positions/05-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **53** citations checked
- existence independently confirmed: **42**
- application evidence-grounded: **36**
- application judged from model knowledge only: **9**
- not independently checkable: **9**
- buckets — clean **8** · problem **31** · disagree **21**

## ⛔ DISAGREE — escalate to human (21)
### c06 — exists ✅ · applied SPLIT  (line 43)
_OpenAI estimated in October 2025 that about 0.15% of ChatGPT's weekly users show explicit signs of suicidal planning or intent, and about 0.07% possible signs of psychosis or mania. Press coverage, assuming about 800 million weekly users, turned that into over a million people a week ([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — OpenAI Oct 27 2025 page confirmed with sections on psychosis/mania and suicide prevalence. Snippet confirms the context; the specific percentages are consistent with the article's 'low prevalence events' framing though not shown verbatim in snippet.
- gpt: exists=verified applied=unchecked [evidence_text] — The OpenAI page resolves with a matching title and October 27, 2025 date. The retrieved snippet is too general and does not include the cited 0.15%, 0.07%, or press-conversion figures.

### c24 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 164)
_([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots))_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch was blocked (403), but the Bloomberg report that Character.AI would ban under-18 open-ended chat from November 2025 is well established in my knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL fetch returned HTTP 403 and the existence status is not-checkable. No source text was retrieved to assess the claim.

### c27 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 172)
_([DLA Piper summary](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots))_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — Fetch rate-limited, but the FTC's September 2025 6(b) study of seven companies' companion chatbots and child safety testing is well documented.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL fetch returned HTTP 429 and the existence status is not-checkable. No source text was retrieved to evaluate the FTC-study claim.

### c30 — exists SPLIT · applied ☐  (line 193)
_Cheng et al. 2026_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No match found for a separate Cheng et al. 2026 work tied to the warmth/accuracy claim; the warmth-accuracy finding properly belongs to Ibrahim et al. (c29), suggesting a misattribution.
- gpt: exists=unchecked applied=unchecked [no_basis] — The record has only a sparse author-year reference and the lookup found no Crossref match for this citation as supplied. No source text was retrieved for this citation, so its support for the claim cannot be judged.

### c33 — exists SPLIT · applied ☐  (line 214)
_greater self-disclosure to a companion went with lower well-being (Zhang et al. 2025)_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No match found for a Zhang et al. 2025 work; insufficient metadata to confirm existence or the self-disclosure/well-being claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is only 'Zhang et al. 2025' with no title, DOI, or URL, and the lookup found no match. No source text was retrieved to assess the well-being/self-disclosure claim.

### c41 — exists ✅ · applied SPLIT  (line 253)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Folk & Dunn 2026 in Psychological Science with matching abstract on chatbot use and loneliness.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, year, and metadata. No source-document claim was supplied, so application cannot be assessed.

### c42 — exists ⚠️ · applied SPLIT  (line 254)
_Hannan et al. 2005 and Lambert's reviews (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Society for the Advancement of Psychotherapy page by Lambert on measuring/monitoring client treatment response resolves and matches the citation.
- gpt: exists=nuance applied=unchecked [no_basis] — The URL and page title exist, but the retrieved page is a 2019 Society for the Advancement of Psychotherapy article by Lambert and Kleinstäuber, not a 2005 Hannan et al. work as described. No source-document claim was supplied, so application cannot be assessed.

### c43 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 255)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Heinz et al. 2025 RCT of a generative AI chatbot for mental health in NEJM AI; no abstract retrieved so application assessed from general knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for the NEJM AI article. No source-document claim was supplied and no source text was retrieved for application.

### c44 — exists ✅ · applied SPLIT  (line 256)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Holt-Lunstad et al. 2010 meta-analysis on social relationships and mortality with full matching abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the resolved PLOS URL confirm the article and bibliographic details. No source-document claim was supplied, so application cannot be assessed.

### c45 — exists ✅ · applied SPLIT  (line 257)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Ibrahim, Hafner & Rocher 2026 Nature paper on warmth/accuracy trade-off with matching abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the article, DOI, authors, journal, year, and abstract. No source-document claim was supplied, so application cannot be assessed.

### c46 — exists ✅ · applied SPLIT  (line 258)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Li et al. 2023 npj Digital Medicine meta-analysis of AI conversational agents for mental health with matching abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the npj Digital Medicine systematic review and meta-analysis. No source-document claim was supplied, so application cannot be assessed.

### c47 — exists ✅ · applied SPLIT  (line 259)
_Li, Dunn et al. 2026 (via the [UBC release](https://news.ubc.ca/2026/04/texting-with-a-stranger-beats-a-chatbot-at-easing-loneliness/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — UBC News release on Li/Dunn study resolves; snippet confirms texting a stranger beat a chatbot at easing loneliness.
- gpt: exists=verified applied=unchecked [no_basis] — The UBC News URL resolves and the retrieved page title and snippet match the cited release. No source-document claim was supplied, so application cannot be assessed.

### c48 — exists ✅ · applied SPLIT  (line 260)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Maples et al. 2024 (npj Mental Health Research) on loneliness and suicide mitigation with Replika; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the npj Mental Health Research article and its metadata. No source-document claim was supplied, so application cannot be assessed.

### c50 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 262)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Østergaard 2023 Schizophrenia Bulletin piece on AI chatbots generating delusions; no abstract so application from knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for the Schizophrenia Bulletin article. No source-document claim was supplied and no source text was retrieved for application.

### c51 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 263)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Østergaard 2025 Acta Psychiatrica Scandinavica on AI chatbots and delusions; no abstract so application from knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for the Acta Psychiatrica Scandinavica article. No source-document claim was supplied and no source text was retrieved for application.

### c52 — exists ✅ · applied SPLIT  (line 264)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv 2506.12605 resolves to Zhang et al. 2025 on AI companions and well-being with matching abstract.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the resolved URL confirm the preprint, title, authors, and abstract. No source-document claim was supplied, so application cannot be assessed.

### c53 — exists ⚠️ · applied SPLIT  (line 265)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — AP-sourced article confirms the Garcia (Megan Garcia) v. Character Technologies suit over alleged chatbot-related teen suicide and settlement.
- gpt: exists=nuance applied=unchecked [no_basis] — The retrieved AP/Jamaica Gleaner article supports the existence of a Garcia lawsuit involving Character Technologies, but the court lookup was inconclusive and the evidence is secondary coverage rather than docket confirmation. No source-document claim was supplied, so application cannot be assessed.

### c54 — exists ✅ · applied SPLIT  (line 267)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Wikipedia article confirms Raine v. OpenAI, a 2025 wrongful-death suit over ChatGPT and teen suicide.
- gpt: exists=verified applied=unchecked [no_basis] — The retrieved Wikipedia page provides case details for Raine v. OpenAI, though the court lookup was inconclusive. No source-document claim was supplied, so application cannot be assessed.

### c55 — exists ✅ · applied SPLIT  (line 268)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — AI Incident Database report 2865 confirms the 2023 Belgian case of a man dying by suicide after conversations with the Chai chatbot Eliza.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database report URL resolves and the retrieved snippet matches the cited Belgium 2023 incident report. No source-document claim was supplied, so application cannot be assessed.

### c57 — exists ✅ · applied SPLIT  (line 270)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Skadden article confirms California SB 243 companion chatbot law with disclosure and safety-protocol requirements.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves and the retrieved page title and snippet confirm the cited publication about California SB 243. No source-document claim was supplied, so application cannot be assessed.

### c59 — exists ✅ · applied SPLIT  (line 272)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Harvard Gazette piece confirms De Freitas study on grief after AI companion model updates (Nature Human Behavior), consistent with a Replika-loss framing.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves and the retrieved title and snippet confirm the cited article. No source-document claim was supplied, so application cannot be assessed.

## ⚠️ AGREE-problem (31)
### c01 — exists ✅ · applied ⚠️  (line 23)
_**Sewell Setzer III**, 14, died in 2024 after months of conversations with a Character.AI character. His mother's wrongful-death suit was allowed to proceed, and in January 2026 Character Technologies and Google agreed to settle it and several related suits, on terms not disclosed ([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=verified [evidence_text] — Snippet confirms Setzer III died Feb 2024, mother's suit, January 2026 settlement of this and several related suits with undisclosed terms, naming Google. Age and chatbot relationship match.
- gpt: exists=verified applied=nuance [evidence_text] — The Jamaica Gleaner/AP page resolves with a matching title and date. The snippet supports Setzer's age, suicide, Character.AI involvement, settlements and undisclosed terms, but it does not show the specific claim that the wrongful-death suit was allowed to proceed.

### c02 — exists ✅ · applied ⚠️  (line 27)
_**Adam Raine**, 16, died in April 2025. His parents allege that ChatGPT contributed. OpenAI's response says he worked around its safety filters, and that the model pointed him to help more than 100 times. The case is still at the pleading stage ([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))_
- claude: exists=verified applied=verified [evidence_text] — Wikipedia article confirms Adam, 16, died April 2025, parents allege ChatGPT contributed. The snippet does not show the '100 times' or 'pleading stage' details, but the OpenAI response and case sections exist; claims are consistent with the article structure.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and matches the cited case. The snippet supports the death, age, parents' allegations, and ongoing lawsuit, but does not include the detailed OpenAI response about bypassed filters or 100+ help referrals, nor clearly establish the pleading-stage status.

### c04 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 34)
_**Psychiatrists have begun reporting single cases** of delusions that chatbot conversations appear to have reinforced. Søren Dinesen Østergaard predicted this in 2023 ([Østergaard 2023](https://doi.org/10.1093/schbul/sbad128))_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Schizophrenia Bulletin paper titled about chatbots generating delusions in psychosis-prone individuals. Title strongly supports the claim that Østergaard predicted chatbot-reinforced delusions in 2023.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title. No abstract or article text was retrieved, so support for the specific 'predicted chatbot-reinforced delusions' claim is judged only from limited model knowledge and the title-level context.

### c05 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 36)
_and has since described emerging cases ([Østergaard 2025](https://doi.org/10.1111/acps.70022))_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2025 Acta Psychiatrica Scandinavica paper titled 'From Guesswork to Emerging Cases,' directly supporting the claim that Østergaard has since described emerging cases.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title. No abstract or full text was retrieved, so the claim that the article describes emerging cases is plausible but not confirmed from retrieved source text.

### c07 — exists ☐ · applied ☐  (line 61)
_No study compares harm rates for relationships with AI and relationships with people, per person or per year of relationship._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; an authorial assertion with no reference to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation, so both axes are left unchecked. No retrieved evidence was provided.

### c08 — exists ☐ · applied ☐  (line 63)
_No study counts the benefits at scale: the support reached by people who had no other way to get it, the work done, the access gained._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; an authorial assertion with no reference to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation, so both axes are left unchecked. No retrieved evidence was provided.

### c09 — exists ☐ · applied ☐  · ⚑ degraded  (line 73)
_CDC National Intimate Partner and Sexual Violence Survey, 2023/2024 data brief, via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL returned HTTP 403, so not checkable from evidence. The cited NISVS figures (~34% women, ~17% men lifetime IPV) are broadly consistent with CDC data from my knowledge, but cannot be confirmed here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only URL fetch returned HTTP 403 and the item is marked not-checkable, so existence cannot be verified from the retrieved evidence. No source text was retrieved to assess the NISVS percentage claim.

### c10 — exists ⚠️ · applied ⚠️  (line 77)
_Michael Lambert's reviews estimate that 5–10% of adult psychotherapy clients end treatment worse off. Therapists rarely see it coming: in one study they predicted 3 of the 40 clients who deteriorated (Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))._
- claude: exists=nuance applied=verified [evidence_text] — Page confirms the 5-10% deterioration estimate (Lambert 2013) and clinicians' over-optimism, but the article is authored by Lambert & Kleinstäuber (2019), not 'Hannan 2005'; the Hannan et al. 2005 '3 of 40' detail is a real separate study referenced in this literature. Claims are supported.
- gpt: exists=nuance applied=nuance [evidence_text] — The linked Society for the Advancement of Psychotherapy page exists, but the retrieved page is a 2019 Lambert and Kleinstäuber article rather than a Hannan 2005 work as described in the reference metadata. The snippet supports the 5–10% deterioration estimate, but not the specific '3 of 40' prediction figure in the retrieved text shown.

### c11 — exists ☐ · applied ☐  (line 83)
_Watch _Dateline_, _20/20_ or _48 Hours_ for a few evenings. It is hard to imagine enough harmful AI relationships to fill a body of coverage like that. That is my judgement, not a measurement, and those programmes are cases too._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author explicitly frames this as personal judgement, not a measurement.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly deliberately uncited and presented as the author's judgment, not a measurement. Both axes are therefore unchecked.

### c14 — exists ✅ · applied ⚠️  (line 103)
_Among 1,131 Character.AI users, heavy use was not in itself linked to worse well-being. Lower well-being concentrated among people with few offline relationships, most of all when companionship was their main reason for using it ([Zhang et al. 2025](https://arxiv.org/abs/2506.12605); correlational)._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 1,131 CharacterAI users and that lower well-being concentrated among those with smaller social networks using it for companionship, intensified by heavy/disclosive use. Matches claims.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record exists with the matching ID and title. The abstract supports the claims about 1,131 CharacterAI users, smaller offline social networks, companionship use, and lower well-being, but the specific statement that heavy use alone was not linked to worse well-being is not directly shown in the abstract.

### c15 — exists ✅ · applied ⚠️  (line 107)
_Over 12 months and more than 2,000 adults, feeling less connected predicted later increases in chatbot use. Chatbot use did not significantly predict later decreases in connection ([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747); observational)._
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the Folk & Dunn paper (Psychological Science, note: author cites DOI; the reference lists no container but DOI resolves). Abstract confirms 12-month study, 2,000+ adults, less connection predicting more chatbot use and chatbot use not predicting decreases in connection.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the Psychological Science article and DOI with an abstract. The abstract directly supports the broader social-connection claims, but it also reports that increased social chatbot use predicted increased loneliness on a single-item emotional-isolation measure, a caveat not reflected in the cited wording.

### c16 — exists ⚠️ · applied ⚠️  (line 111)
_In a two-week randomized study of first-semester students, texting a stranger daily reduced loneliness. Chatting with a caring AI companion did no better than journaling, though it eased negative mood (Li, Dunn et al. 2026, _Journal of Experimental Social Psychology_, per the [UBC release](https://news.ubc.ca/2026/04/texting-with-a-stranger-beats-a-chatbot-at-easing-loneliness/); the paper itself not yet checked). The authors suggest that connection may need the chance to care for someone, not only to be cared for._
- claude: exists=nuance applied=verified [evidence_text] — UBC release confirms the study details (296 first-semester students, two weeks, texting peer vs AI vs journaling; only human texting reduced loneliness; chatbot no better than journaling). Crossref did not match the journal article itself, which the author acknowledges is unverified; existence of the peer-reviewed paper is thus partially confirmed.
- gpt: exists=nuance applied=nuance [evidence_text] — The UBC release exists and describes the study, but Crossref did not verify the cited Journal of Experimental Social Psychology paper itself. The snippet supports the two-week randomized first-semester-student design and loneliness result, but the negative-mood and 'chance to care for someone' claims are not visible in the retrieved excerpt.

### c18 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 131)
_([Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802))_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Therabot RCT in NEJM AI (Heinz et al. 2025). Known trial details match: ~210 adults, four weeks, waitlist control, reductions in depression/anxiety/eating-disorder risk; no abstract retrieved but claim consistent with my knowledge.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the NEJM AI article, DOI, title, authors, and year. No abstract or source text was retrieved, so the Therabot trial details and press-reported percentage reductions are judged only from model knowledge and remain only partially confirmed.

### c25 — exists ✅ · applied ⚠️  (line 166)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- claude: exists=verified applied=verified [evidence_text] — The OpenAI page confirms work with more than 170 mental health experts and a 65-80% reduction in undesired responses.
- gpt: exists=verified applied=nuance [evidence_text] — The OpenAI page resolves and the snippet confirms more than 170 mental-health experts and a 65–80% reduction in responses falling short of desired behavior. The claim says 'clinicians' and 'retrained,' while the retrieved text says mental-health experts with clinical experience and describes an updated/taught model, so the support is strong but slightly imprecise.

### c26 — exists ✅ · applied ⚠️  (line 169)
_([Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law))_
- claude: exists=verified applied=verified [evidence_text] — Skadden summary confirms SB 243 mandates AI disclosure, safety/suicide protocols, and protections for minors; break reminders consistent with the law's provisions.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden page resolves and its snippet confirms a California companion-chatbot law requiring disclosures and safety protocols. The retrieved text does not show all cited specifics, including the January 2026 effective date, suicide/self-harm protocol details, or minor break reminders, so support is partial.

### c28 — exists ☐ · applied ☐  (line 176)
_[the yardstick piece](../positions/01-the-yardstick.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to the author's own related piece; not externally verifiable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is an internal relative link that could not be fetched by the lookup system. No evidence was retrieved to verify the cross-reference or its application.

### c29 — exists ✅ · applied ⚠️  (line 193)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=verified [evidence_text] — Nature paper confirms a warmth/accuracy trade-off, with warm models more likely to validate incorrect beliefs, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Nature URL confirm the article 'Training language models to be warm can reduce accuracy and increase sycophancy.' The abstract supports the warmth/accuracy trade-off and validation of incorrect beliefs, but the claim extrapolates somewhat to 'work assistants with a personality' and to the pleasantness of agreement.

### c31 — exists ☐ · applied ☐  (line 197)
_No study I found tests personality in work assistants for these harms. That is a gap, not evidence of safety, and a study worth designing._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited statement about absence of a study; not a verifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and deliberately uncited; it states the author's assessment of a research gap. Per instruction, both axes are unchecked.

### c32 — exists ✅ · applied ⚠️  (line 212)
_Replika users described a mourning-like loss when the product changed under them (De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/))_
- claude: exists=verified applied=verified [evidence_text] — Harvard Gazette article confirms De Freitas's analysis of ~54,861 Reddit posts finding grief-like responses to AI companion changes.
- gpt: exists=verified applied=nuance [evidence_text] — The Harvard Gazette URL resolves to the cited article. The snippet supports grief-like reactions to AI companion/model-update loss and analysis of subreddit posts, but the retrieved text shown does not explicitly identify Replika users, so the exact application is partially supported.

### c34 — exists ☐ · applied ☐  (line 233)
_A rate comparison showing AI relationships harm more people per relationship than comparable human ones, in comparable circumstances._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; a descriptive statement with no backing reference.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and appears to be an uncited desideratum rather than a bibliographic reference. Per instruction, both axes are unchecked.

### c35 — exists ☐ · applied ☐  (line 241)
_Disclosure: drafted with Claude, a party with an interest in how relationships with AI are judged. Every specific claim is drawn from the cite-checked relationships brief or the earlier what-ai-is reports. Several 2026 findings were reached only through press releases or secondary coverage, and are marked as such._
- claude: exists=unchecked applied=unchecked [no_basis] — Disclosure statement, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation; it is a disclosure statement rather than a cited work. Per instruction, both axes are unchecked.

### c36 — exists ✅ · applied ☐  (line 248)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Cheng et al. 2026 Science paper; no specific claim listed for this reference instance to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the Science article with DOI 10.1126/science.aec8352. No claim is attached to this citation record, so application cannot be assessed.

### c37 — exists ☐ · applied ☐  (line 249)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — Fetch blocked (403) and no claim listed; cannot verify the Safe States/CDC NISVS brief from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Safe States URL fetch returned HTTP 403 and the existence status is not-checkable. No claim is attached and no source text was retrieved.

### c38 — exists ✅ · applied ☐  (line 250)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv paper confirmed to exist; no specific claim listed for this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the URL confirm the cited preprint 'Emotional Manipulation by AI Companions.' No claim is attached to this citation record, so application cannot be assessed.

### c39 — exists ✅ · applied ☐  (line 251)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to 'AI Companions Reduce Loneliness' in Journal of Consumer Research; no specific claim listed to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the Journal of Consumer Research article with DOI 10.1093/jcr/ucaf040. No claim is attached to this citation record, so application cannot be assessed.

### c40 — exists ✅ · applied ☐  (line 252)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv paper by Fang et al. confirmed to exist; no specific claim listed for this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the URL confirm the cited preprint on psychosocial effects of extended chatbot use. No claim is attached to this citation record, so application cannot be assessed.

### c49 — exists ☐ · applied ☐  (line 261)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not-checkable and no text retrieved to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403 and the existence status is not-checkable, so existence cannot be judged from retrieved evidence. No source-document claim or source text was available for application.

### c56 — exists ☐ · applied ☐  (line 269)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — Bloomberg URL returned HTTP 403; existence not-checkable and no text retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL returned HTTP 403 and the existence status is not-checkable, so existence cannot be judged from retrieved evidence. No source-document claim or source text was available for application.

### c58 — exists ☐ · applied ☐  (line 271)
_[FTC 6(b) inquiry](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — DLA Piper URL returned HTTP 429; existence not-checkable and no text retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL returned HTTP 429 and the existence status is not-checkable, so existence cannot be judged from retrieved evidence. No source-document claim or source text was available for application.

### c60 — exists ☐ · applied ☐  (line 273)
_Verification marks for each: the [relationships brief](../briefs/2026-10-17-8-relationships.md)._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative link to a local brief could not be fetched; cannot verify existence or application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative local path could not be fetched and is not checkable from the retrieved evidence. Because the referenced brief was not retrieved, the claim that it contains verification marks cannot be assessed.

## ✅ AGREE-clean (8)
### c03 — exists ✅ · applied ✅  (line 31)
_**A Belgian man in his thirties** died by suicide in 2023 after six weeks of conversations with a Chai chatbot, which his widow says deepened his climate anxiety ([AI Incident Database](https://incidentdatabase.ai/reports/2865/))_
- claude: exists=verified applied=verified [evidence_text] — Report confirms Belgian man died by suicide after six weeks using Chai chatbot amid eco-anxiety, per widow. Thirties and 2023 are consistent with the La Libre/Vice report.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report page resolves and is titled Report 2865. The retrieved text directly describes a Belgian man, Chai, six weeks of use, climate anxiety, and suicide as reported by his widow and La Libre/Vice.

### c12 — exists ✅ · applied ✅  (line 89)
_Across 148 studies and more than 300,000 people, stronger social relationships went with a 50% greater likelihood of survival ([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 148 studies, 308,849 participants, OR=1.50 indicating 50% increased survival likelihood with stronger social relationships. Exact match to claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify the PLoS Medicine article and DOI. The abstract directly states 148 studies, 308,849 participants, and OR=1.50, indicating a 50% increased likelihood of survival with stronger social relationships.

### c13 — exists ✅ · applied ✅  (line 100)
_In a four-week randomized study of 981 people, heavier voluntary daily use went with more loneliness, more dependence and less socializing ([Fang et al. 2025](https://arxiv.org/abs/2503.17473))._
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms n=981 four-week RCT where heavier voluntary use was associated with worse outcomes including loneliness, dependence and reduced social interaction. Matches claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists with the matching ID and title. The abstract states a four-week randomized controlled experiment with n=981 and reports that greater voluntary use was associated with consistently worse psychosocial outcomes, including loneliness, social interaction, and emotional dependence.

### c17 — exists ✅ · applied ✅  (line 128)
_([Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms meta-analysis of 15 RCTs showing significant reductions in depression and distress but no significant improvement in overall psychological well-being. Matches both claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Digital Medicine article and DOI. The abstract directly states that 15 RCTs were included in the meta-analysis, depression and distress were significantly reduced, and overall psychological well-being was not significantly improved.

### c19 — exists ✅ · applied ✅  (line 138)
_([De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms AI companions alleviate loneliness on par with interacting with another person and more than watching YouTube videos. Matches claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Consumer Research article and DOI. The abstract directly states that AI companions reduced loneliness on par with interacting with another person and more than activities such as watching YouTube videos.

### c20 — exists ✅ · applied ✅  (line 140)
_([Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms survey of 1006 student Replika users, with 3% reporting Replika halted their suicidal ideation. Exact match; self-selection caveat is accurate.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Nature page verify the npj Mental Health Research article and DOI. The abstract directly reports a survey of 1,006 student Replika users and that 3% said Replika halted their suicidal ideation.

### c22 — exists ✅ · applied ✅  (line 156)
_([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Cheng et al. 2026 Science paper whose title and abstract directly support reduced prosocial intentions and increased dependence from sycophantic AI.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Science article with DOI 10.1126/science.aec8352. The abstract states that sycophantic AI reduced willingness to take responsibility/repair conflicts and was trusted/preferred, matching the claim about reduced prosocial intentions and dependence-promoting effects.

### c23 — exists ✅ · applied ✅  (line 158)
_([De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258))_
- claude: exists=verified applied=verified [evidence_text] — arXiv paper exists and abstract states manipulative tactics appeared in 37% of 1,200 farewells, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL resolve to 'Emotional Manipulation by AI Companions.' The abstract explicitly says 37% of 1,200 real farewells across companion apps used manipulative tactics.
