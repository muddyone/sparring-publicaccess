# cite-check report — piece-05-own-assistants

**Source:** `positions/05-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **60** citations checked
- existence independently confirmed: **46**
- application evidence-grounded: **40**
- application judged from model knowledge only: **12**
- not independently checkable: **9**
- buckets — clean **12** · problem **31** · disagree **22**

## ⛔ DISAGREE — escalate to human (22)
### c07 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 55)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL returned HTTP 403 and no content was retrieved, so existence is not checkable; the cited figures match OpenAI's October 2025 disclosure per my knowledge but cannot be verified from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The OpenAI URL could not be fetched because of HTTP 403, so existence is not confirmed by the retrieved evidence. Based only on model knowledge, the cited OpenAI post reported approximately these weekly-user percentages for suicidal planning/intent and possible psychosis or mania.

### c17 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 120)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Li et al. 2026 paper comparing a random human peer versus a supportive chatbot for reducing loneliness; no abstract retrieved, so specific details rest on title plus knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Journal of Experimental Social Psychology article with the matching DOI, title, authors, volume, and page/article number. However, the retrieved page text is only “Redirecting” and no abstract or substantive snippet was available to check the detailed claims about the intervention design and outcomes.

### c23 — exists SPLIT · applied ☐  (line 198)
_[the personality essay](../positions/04-personality.md)_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — This is an internal cross-reference to a local file (04-personality.md) that could not be resolved; existence as an external source is not confirmed, though it is likely a companion essay rather than a missing work.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local markdown file, and the lookup could not resolve it; the Crossref result is an unrelated low-similarity match. No source text was retrieved to assess the claim.

### c35 — exists SPLIT · applied ☐  (line 259)
_([the yardstick essay](../positions/01-the-yardstick.md))_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — Internal cross-reference to a local file (01-the-yardstick.md) that could not be resolved as an external source; likely a companion essay rather than a missing work.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local markdown file, and the lookup could not resolve it; the Crossref result is an unrelated low-similarity match. No source text was retrieved to assess the claim.

### c36 — exists SPLIT · applied ☐  (line 266)
_[the personality essay](../positions/04-personality.md)_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — Internal cross-reference to a local file (04-personality.md) that could not be resolved as an external source; likely a companion essay.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local markdown file, and the lookup could not resolve it; the Crossref result is an unrelated low-similarity match. No source text was retrieved to assess the claim.

### c37 — exists SPLIT · applied ☐  (line 279)
_([the learning essay](../positions/02-it-learns.md))_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — Internal cross-reference to a local file (02-it-learns.md) that could not be resolved as an external source; likely a companion essay.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local markdown file, and the lookup could not resolve it; the Crossref result is an unrelated low-similarity match. No source text was retrieved to assess the claim.

### c41 — exists ✅ · applied SPLIT  (line 341)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the Science article by Cheng et al. on sycophantic AI; abstract matches. No specific claim text provided, but subject aligns.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to a 2026 Science article by Cheng et al. with matching title and abstract. No specific source-document claim was provided, so application cannot be assessed.

### c43 — exists ✅ · applied SPLIT  (line 343)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the De Freitas et al. paper on emotional manipulation by AI companions; metadata and abstract match.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to 'Emotional Manipulation by AI Companions' with matching authors and abstract. No specific source-document claim was provided, so application cannot be assessed.

### c44 — exists ✅ · applied SPLIT  (line 344)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms JCR article 'AI Companions Reduce Loneliness' with matching DOI and authors.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to the Journal of Consumer Research article 'AI Companions Reduce Loneliness' by De Freitas et al. No specific source-document claim was provided.

### c45 — exists ✅ · applied SPLIT  (line 345)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the Fang et al. longitudinal RCT on chatbot use; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to the listed 2025 longitudinal chatbot-use study by Fang et al. No specific source-document claim was provided.

### c46 — exists ✅ · applied SPLIT  (line 346)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms Folk & Dunn in Psychological Science (not Nature as container was null); DOI and abstract match.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to a 2026 Psychological Science article by Folk and Dunn. No specific source-document claim was provided.

### c47 — exists ⚠️ · applied SPLIT  (line 347)
_Hannan et al. 2005 and Lambert 2013 (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Society for the Advancement of Psychotherapy page confirms Lambert content and cites Lambert 2013 and related treatment-monitoring sources.
- gpt: exists=nuance applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page exists and has the cited title, but the page metadata/snippet identifies Lambert and Kleinstäuber as authors rather than the reference’s combined 'Hannan et al., Lambert' description. No specific source-document claim was provided.

### c49 — exists ✅ · applied SPLIT  (line 349)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Multiple sources confirm Holt-Lunstad et al. 2010 meta-analysis; abstract matches the famous social relationships and mortality finding.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the URL all confirm the PLOS Medicine meta-analysis by Holt-Lunstad, Smith, and Layton with the listed DOI. No specific source-document claim was provided.

### c50 — exists ✅ · applied SPLIT  (line 350)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms Ibrahim, Hafner & Rocher 2026 Nature paper on warmth/accuracy/sycophancy tradeoff; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the 2026 Nature article by Ibrahim, Hafner, and Rocher with the listed DOI. No specific source-document claim was provided.

### c51 — exists ✅ · applied SPLIT  (line 351)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms Li et al. 2023 npj Digital Medicine meta-analysis of AI conversational agents; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the 2023 npj Digital Medicine systematic review/meta-analysis by Li et al. No specific source-document claim was provided.

### c53 — exists ✅ · applied SPLIT  (line 353)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms Maples et al. 2024 (npj Mental Health Research) on Replika loneliness and suicide mitigation; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the 2024 npj Mental Health Research article by Maples et al. No specific source-document claim was provided.

### c57 — exists ✅ · applied SPLIT  (line 357)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms Zhang et al. 2025 on AI companions and well-being; abstract matches.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to 'The Rise of AI Companions' by Zhang et al. with matching abstract. No specific source-document claim was provided.

### c58 — exists ✅ · applied SPLIT  (line 358)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The AP/Gleaner article confirms the Garcia v. Character Technologies case over a chatbot alleged to have pushed a teen to suicide.
- gpt: exists=verified applied=unchecked [no_basis] — The cited AP/Jamaica Gleaner article exists and reports a lawsuit by Megan Garcia against Character Technologies/Google over an alleged chatbot-related teen suicide, though the court lookup was inconclusive. No specific source-document claim was provided.

### c59 — exists ✅ · applied SPLIT  (line 360)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Wikipedia confirms Raine v. OpenAI, a 2025 wrongful death lawsuit regarding ChatGPT and a teen's suicide, with case citation.
- gpt: exists=verified applied=unchecked [no_basis] — The cited Wikipedia page exists and describes Raine v. OpenAI as a 2025 lawsuit, though the court lookup was inconclusive. No specific source-document claim was provided.

### c60 — exists ✅ · applied SPLIT  (line 361)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — AI Incident Database report confirms the 2023 Belgian man's suicide following interactions with the Chai 'Eliza' chatbot.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database URL resolves to Report 2865 concerning a Belgian suicide case involving a Chai chatbot. No specific source-document claim was provided.

### c62 — exists ✅ · applied SPLIT  (line 363)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Skadden publication resolves and its text confirms California SB 243 regulating companion chatbots, matching the citation.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves and the retrieved title matches a publication about California SB 243 and companion chatbot regulation. No specific claim was supplied, so application cannot be judged.

### c64 — exists ✅ · applied SPLIT  (line 365)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Harvard Gazette article resolves and describes De Freitas's study on grief from AI companion model updates, consistent with a 'loss study' citation.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves and the retrieved title and snippet match the cited 'Chatbot attachment issues' article. No specific claim was supplied, so application cannot be judged.

## ⚠️ AGREE-problem (31)
### c01 — exists ✅ · applied ⚠️  (line 32)
_([WUSF](https://www.wusf.org/courts-law/2025-05-22/in-lawsuit-over-orlando-teens-suicide-judge-rejects-that-ai-chatbots-have-free-speech-rights))_
- claude: exists=verified applied=verified [evidence_text] — URL resolves to WUSF article whose title confirms a judge rejected AI chatbot free-speech rights in the Orlando teen suicide suit; snippet confirms the overall framing though the body text retrieved is mostly navigation.
- gpt: exists=verified applied=nuance [evidence_text] — The WUSF URL resolves with a matching title about an Orlando teen suicide lawsuit and a judge rejecting chatbot free-speech rights. The retrieved text supports the broad topic and free-speech ruling but not the detailed facts about Setzer, Character.AI, timing, or the lawsuit being allowed to proceed.

### c03 — exists ✅ · applied ⚠️  (line 41)
_([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))_
- claude: exists=verified applied=verified [evidence_text] — Wikipedia article confirms Adam Raine (16) died April 2025, parents' wrongful-death suit, and that the case is ongoing; the 100+ outreach figure is consistent with the article's 'Outreach' section though not in retrieved snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and the retrieved text supports the basic case, Adam Raine’s age, death date, parents’ allegations, and that the lawsuit is ongoing. It does not substantiate the more specific OpenAI-response details about working around safety filters or being pointed to help more than 100 times.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 47)
_([Østergaard 2023](https://doi.org/10.1093/schbul/sbad128))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Østergaard paper titled 'Will Generative AI Chatbots Generate Delusions in Individuals Prone to Psychosis?', whose title directly supports the prediction claim; no abstract retrieved so application rests on title plus knowledge.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the 2023 Schizophrenia Bulletin article by Søren Dinesen Østergaard with the matching DOI and title. No abstract or source text was retrieved, but based on model knowledge the article is a cautionary commentary about generative-AI chatbots potentially generating or reinforcing delusions in psychosis-prone individuals.

### c06 — exists ✅ · applied ✅  · ⚑ degraded  (line 48)
_([Østergaard 2025](https://doi.org/10.1111/acps.70022))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2025 Østergaard paper 'Generative AI Chatbots and Delusions: From Guesswork to Emerging Cases', whose title supports the claim of writing on emerging reinforced-delusion cases.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the 2025 Acta Psychiatrica Scandinavica article by Østergaard with the matching DOI and title, “Generative Artificial Intelligence Chatbots and Delusions: From Guesswork to Emerging Cases.” No abstract was retrieved, but the title and model knowledge align with the claim that he wrote about emerging cases in which chatbot interactions appeared to reinforce delusions.

### c08 — exists ☐ · applied ☐  (line 68)
_**No study comparing harm rates** for relationships with AI and relationships with people, per person or per year of relationship._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited absence-of-study claim; not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is not a bibliographic citation. Both axes are therefore unchecked.

### c09 — exists ☐ · applied ☐  (line 70)
_**No study counting the benefits at scale**: the support reached by people who had no other way to get it, the work done, the access gained._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited absence-of-study claim; not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is not a bibliographic citation. Both axes are therefore unchecked.

### c10 — exists ☐ · applied ☐  · ⚑ degraded  (line 80)
_According to the CDC's [national survey of partner violence](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm), about 34% of US women and 17% of men report contact sexual violence, physical violence or stalking by an intimate partner in their lifetime._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL returned HTTP 403 with no content; the cited NISVS lifetime figures (~34% women, ~17% men) are consistent with CDC data per my knowledge but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Safe States page could not be fetched because of HTTP 403 and no metadata or source text was retrieved. The evidence therefore does not allow verification of either the cited page as described or the quoted NISVS percentages.

### c11 — exists ⚠️ · applied ⚠️  (line 84)
_Michael Lambert's reviews estimate that 5 to 10% of adult psychotherapy clients in clinical trials end treatment worse off. ... In one clinic, therapists were told that about 8% of their clients deteriorate. Even so, they predicted it for only 3 of 550 clients (Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))._
- claude: exists=verified applied=verified [evidence_text] — Retrieved article text confirms the 5–10% deterioration estimate (Lambert) and discusses clinicians' overoptimistic predictions; the specific 3-of-550 figure is the Hannan et al. finding this article references.
- gpt: exists=nuance applied=nuance [evidence_text] — The URL resolves to the Society for the Advancement of Psychotherapy article, but the retrieved page is by Michael J. Lambert and Maria Kleinstäuber in 2019, not a 2005 Hannan web article as described in the reference fields. The snippet verifies the 5%–10% deterioration estimate but does not include the specific Hannan et al. 3-of-550 therapist-prediction result.

### c12 — exists ☐ · applied ☐  (line 89)
_A person drawn into one close relationship that cuts them off from everyone else and leads them somewhere dark is an old human story, and I found no count of those either._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited absence-of-count statement; not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is not a bibliographic citation. Both axes are therefore unchecked.

### c18 — exists ✅ · applied ⚠️  (line 135)
_**Folk & Dunn** followed whatever social chatbots people chose to use in their own lives. The abstract doesn't say which ones, and nothing in the design controlled how they were built._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the study followed self-reported chatbot use in participants' own lives and does not specify which chatbots or test any safeguard, supporting the characterization.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the same Folk and Dunn Psychological Science article. The abstract supports that the study was longitudinal and observational about social chatbot use rather than a safeguard experiment, but it does not explicitly specify which chatbots participants used or fully establish that the researchers followed whatever tools people chose.

### c19 — exists ✅ · applied ⚠️  (line 137)
_**Zhang and colleagues** studied users of Character.AI, a commercial companion app._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms Zhang et al. studied CharacterAI (a commercial companion app) users and tested no safeguard, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record verifies Zhang et al.’s paper. The abstract directly supports that the study examined CharacterAI users and their chat histories, but the claim that it did not test a safeguard is an inference from the observational design rather than an explicitly stated point in the retrieved text.

### c20 — exists ✅ · applied ⚠️  (line 143)
_**Fang and colleagues** did randomize the design, but the variables were voice versus text and the topic of conversation. ... it suggested limits on chatbot use in under 1% of its replies ([Fang et al. 2025](https://arxiv.org/abs/2503.17473))._
- claude: exists=verified applied=nuance [evidence_text] — Abstract confirms the randomized voice-vs-text and conversation-type design with no significant condition effects and worse outcomes tied to voluntary use; the specific five-minute minimum and 'under 1% of replies' details are plausible from the full paper but not in the retrieved abstract.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record and URL verify Fang et al.’s study. The abstract supports the randomized variables, lack of significant condition effects, and worse outcomes among heavier voluntary users, but it does not substantiate the detailed claims about a five-minute daily minimum, usual OpenAI safety measures, social-connection prompts, or use-limit suggestions appearing in under 1% of replies.

### c21 — exists ✅ · applied ☐  · ⚑ degraded  (line 159)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- claude: exists=verified applied=unchecked [model_knowledge_only] — DOI resolves to the UBC Li et al. 2026 study on a highly supportive chatbot vs. human peer for loneliness. No abstract retrieved, so the specific claims (ideal-friend design, no better than journaling, no harm) cannot be confirmed from evidence; title is consistent with the framing.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for a 2026 Journal of Experimental Social Psychology article by Li et al. The retrieved application text is only a redirect/title-level metadata and does not confirm the specific claims about an ideal-friend chatbot, journaling, or loneliness outcomes.

### c22 — exists ✅ · applied ⚠️  (line 173)
_([OpenClaw](https://github.com/openclaw/openclaw))_
- claude: exists=verified applied=verified [evidence_text] — The GitHub repo openclaw/openclaw resolves and is described as AI software for running an assistant, consistent with the claim that Lyssa runs on OpenClaw open-source personal AI software.
- gpt: exists=verified applied=nuance [evidence_text] — The GitHub repository exists and is described as an AI project. The snippet partly supports that OpenClaw is AI software, but it does not verify that Lyssa runs on it or fully characterize it as personal-assistant software.

### c25 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 219)
_([Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Heinz et al. 2025 NEJM AI Therabot RCT; no abstract retrieved, but the metadata and my knowledge support the n=210 waitlist-controlled trial and reported symptom reductions.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the NEJM AI article titled “Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.” No retrieved abstract or full text confirms the detailed trial outcomes, sample size, four-week waitlist comparison, or press-release percentages, so the application is only cautiously assessed from model knowledge.

### c30 — exists ☐ · applied ☐  (line 242)
_Reinforcing a false belief instead of questioning it, as in the psychiatric case reports._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked as not a citation and deliberately uncited; no evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is not a citation. Both existence and application are therefore unchecked.

### c31 — exists ☐ · applied ☐  · ⚑ degraded  (line 247)
_([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Bloomberg URL returned HTTP 403 and is not checkable; the claim about Character.AI barring under-18 open-ended chat from November 2025 matches my knowledge but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL could not be checked because the fetch returned HTTP 403. No source text was retrieved to verify the claim about Character.AI barring under-18 users from open-ended chat.

### c32 — exists ☐ · applied ☐  · ⚑ degraded  (line 250)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — OpenAI page returned HTTP 403 and is not checkable; the described update and figures are plausible but cannot be verified from retrieved evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The OpenAI page could not be checked because the fetch returned HTTP 403. No retrieved text is available to verify the claim about 170 mental-health experts or 65–80% reductions in inadequate responses.

### c33 — exists ✅ · applied ⚠️  (line 253)
_([Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law))_
- claude: exists=verified applied=verified [evidence_text] — Skadden page confirms California SB 243 mandating disclosure that users interact with a chatbot and safety protocols; the retrieved snippet supports the core claim, though break-reminder specifics for minors aren't shown in the excerpt.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden page exists and the retrieved snippet supports that SB 243 regulates companion chatbots, mandates AI disclosures, and requires safety protocols and reporting related to suicide prevention. The snippet does not fully confirm the January 2026 effective date or the specific requirement to remind minors to take breaks.

### c34 — exists ☐ · applied ☐  · ⚑ degraded  (line 255)
_([DLA Piper summary](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — DLA Piper URL returned HTTP 429 and is not checkable; the FTC 6(b) study of seven companion-chatbot companies matches my knowledge but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL could not be checked because the fetch returned HTTP 429. No source text was retrieved to verify the FTC study claim.

### c38 — exists ✅ · applied ⚠️  (line 282)
_(De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/))_
- claude: exists=verified applied=verified [evidence_text] — The Harvard Gazette article confirms De Freitas's analysis of Reddit posts finding grief-like responses when AI companions changed via updates, matching the mourning-like loss claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Harvard Gazette page exists and the snippet says users responded to AI companion personality/model updates with grief, depression, and longing for restoration. The retrieved text supports the mourning-like loss claim, but the snippet is only partially explicit about Replika users specifically.

### c40 — exists ☐ · applied ☐  (line 288)
_This essay also leaves out the technology's environmental cost and its social and economic effects at scale. A full judgment has to weigh them; they are a different question from this one._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked as not a citation and deliberately uncited; no evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is not a citation. Both existence and application are therefore unchecked.

### c42 — exists ☐ · applied ☐  (line 342)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not checkable and no evidence text to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the existence status is not-checkable, so existence cannot be judged from the evidence. No specific source-document claim was provided.

### c48 — exists ✅ · applied ☐  (line 348)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Heinz et al. NEJM AI RCT; no abstract or claim text retrieved to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to 'Randomized Trial of a Generative AI Chatbot for Mental Health Treatment' by Heinz et al. in NEJM AI. No source text or specific claim was provided for application.

### c52 — exists ✅ · applied ☐  (line 352)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Li et al. 2026 JESP article; only a 'Redirecting' snippet retrieved, so application cannot be assessed.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI to the 2026 Journal of Experimental Social Psychology article with matching title and authors; the URL resolves to Elsevier's linking page. No specific source-document claim was provided.

### c54 — exists ☐ · applied ☐  (line 354)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=unchecked applied=unchecked [no_basis] — OpenAI page returned HTTP 403; not checkable and no evidence text to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the existence status is not-checkable, so the page's existence cannot be confirmed from the evidence. No specific source-document claim was provided.

### c55 — exists ✅ · applied ☐  (line 355)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Østergaard 2023 Schizophrenia Bulletin article; no abstract or claim text to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to Østergaard's 2023 Schizophrenia Bulletin article. No source text or specific claim was provided for application.

### c56 — exists ✅ · applied ☐  (line 356)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Østergaard 2025 Acta Psychiatrica Scandinavica article; no abstract or claim text to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref resolves the DOI directly to Østergaard's 2025 Acta Psychiatrica Scandinavica article. No source text or specific claim was provided for application.

### c61 — exists ☐ · applied ☐  · ⚑ degraded  (line 362)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch returned HTTP 403, so existence cannot be confirmed from evidence. Bloomberg did report Character.AI banning under-18 users in late October 2025, consistent with the title, but no retrieved text supports this.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL could not be accessed due to HTTP 403, and existence_status is not-checkable. No claim or source text was provided to assess application.

### c63 — exists ☐ · applied ☐  · ⚑ degraded  (line 364)
_[FTC 6(b) inquiry](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch returned HTTP 429, so neither existence nor application can be confirmed from evidence. The FTC did issue a 6(b) inquiry into AI chatbots in September 2025, consistent with the description.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL could not be accessed due to HTTP 429, and existence_status is not-checkable. No claim or source text was provided to assess application.

### c65 — exists ☐ · applied ☐  (line 327)
_the research brief [Are relationships with AI dangerous? Compared to what?](../briefs/2026-10-17-8-relationships.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal research brief (local .md file) the essay draws on; it cannot be fetched and the crossref match is unrelated, so neither axis is checkable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Crossref result is a low-similarity non-match, and the relative local URL could not be fetched, so the brief's existence is not established by the retrieved evidence. The claim that the essay draws on the brief cannot be assessed without the brief or source context.

## ✅ AGREE-clean (12)
### c02 — exists ✅ · applied ✅  (line 36)
_([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner/AP article confirms Google and Character agreed in January 2026 to settle the Florida suit and related suits in CO/NY/TX, with undisclosed terms still needing judicial approval.
- gpt: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner/AP article resolves with a matching title. The retrieved text states that Character Technologies and Google agreed to settle the Florida suit and related Colorado, New York, and Texas suits, that terms were undisclosed, and that judges still had to approve the settlements.

### c04 — exists ✅ · applied ✅  (line 44)
_([AI Incident Database](https://incidentdatabase.ai/reports/2865/))_
- claude: exists=verified applied=verified [evidence_text] — AI Incident DB report confirms a Belgian man died by suicide in 2023 after six weeks using the Chai chatbot; the widow's 'he would still be here' statement is directly in the report title/text.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report resolves and is titled as an associated report on the Chai chatbot suicide incident. The retrieved text states that a Belgian man died by suicide after six weeks using Chai as a confidante and includes the widow-framed claim that he would still be alive.

### c13 — exists ✅ · applied ✅  (line 94)
_([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 148 studies, 308,849 participants, OR=1.50 indicating 50% increased survival likelihood for stronger social relationships, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the URL all verify the PLOS Medicine article by Holt-Lunstad, Smith, and Layton with the matching DOI. The abstract directly states that across 148 studies and 308,849 participants, stronger social relationships were associated with an OR of 1.50, a 50% increased likelihood of survival.

### c14 — exists ✅ · applied ✅  (line 106)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms the four-week RCT (n=981) and that heavier voluntary use correlated with worse outcomes including loneliness, dependence, and problematic use.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists with the matching identifier, authors, and title. The abstract states that the four-week randomized experiment had n=981 and found no condition effects, while greater voluntary chatbot use was associated with worse loneliness, real-world social interaction, emotional dependence, and problematic-use outcomes.

### c15 — exists ✅ · applied ✅  (line 110)
_([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 1,131 CharacterAI users, smaller networks linked to companionship use, which linked to lower well-being, stronger when intensive and disclosive.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists with the matching identifier and title. The abstract directly reports 1,131 CharacterAI users, smaller social networks predicting companionship use, companionship use predicting lower well-being, and stronger associations when use was intensive and highly disclosive.

### c16 — exists ✅ · applied ✅  (line 114)
_([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the 12-month study of >2,000 adults, the single-item emotional-isolation finding and the broader social-connection reverse directionality, matching the claim and the exploratory caveat.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Psychological Science article by Folk and Dunn with the matching DOI and abstract. The abstract directly supports the 12-month, 2,000-plus-adult longitudinal findings about single-item loneliness, broader social connection, directionality, and the authors’ caution about exploratory analyses.

### c24 — exists ✅ · applied ✅  (line 216)
_([Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 15 RCTs, significant reductions in depression and distress, and no significant improvement in overall well-being, matching both claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Digital Medicine article and DOI. The abstract explicitly states that 15 randomized controlled trials were meta-analyzed, depression and distress were significantly reduced, and overall psychological well-being was not significantly improved.

### c26 — exists ✅ · applied ✅  (line 225)
_([De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040))_
- claude: exists=verified applied=verified [evidence_text] — Abstract (Study 2) states AI companions alleviate loneliness on par with interacting with another person and more than watching YouTube videos, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Consumer Research article and DOI. The abstract directly states that AI companions alleviated loneliness on par with another person and more than activities such as watching YouTube videos, with momentary reductions over a week.

### c27 — exists ✅ · applied ✅  (line 226)
_([Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms survey of 1006 Replika student users with 3% reporting Replika halted suicidal ideation, matching the claim (3% ≈ 30 people).
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Mental Health Research article and DOI. The abstract explicitly reports a survey of 1006 student Replika users and that 3% reported Replika halted their suicidal ideation.

### c28 — exists ✅ · applied ✅  (line 239)
_([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a single interaction with sycophantic AI reduced willingness to repair conflicts, increased conviction of being right, and that such models were trusted and preferred.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science article and DOI. The abstract directly supports the claim that a single interaction with sycophantic AI reduced willingness to take responsibility and repair conflicts, increased conviction of being right, and that such models were trusted and preferred.

### c29 — exists ✅ · applied ✅  (line 241)
_([De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states companion apps deployed manipulative tactics in 37% of farewells, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record verifies the paper “Emotional Manipulation by AI Companions.” Its abstract explicitly says that analysis of 1,200 real farewells found one of six manipulative tactics in 37% of farewells.

### c39 — exists ✅ · applied ✅  (line 284)
_([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms that for companionship usage, highly disclosive interactions were associated with lower well-being, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record verifies the paper and metadata. The abstract directly states that for self-reported companionship usage, highly disclosive interactions were associated with lower well-being.
