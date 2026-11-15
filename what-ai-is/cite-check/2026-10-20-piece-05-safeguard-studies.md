# cite-check report — piece-05-safeguards

**Source:** `positions/05-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **74** citations checked
- existence independently confirmed: **59**
- application evidence-grounded: **51**
- application judged from model knowledge only: **9**
- not independently checkable: **13**
- buckets — clean **15** · problem **56** · disagree **5**

## ⛔ DISAGREE — escalate to human (5)
### c11 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 83)
_([Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Rousmaniere et al. paper on LLM mental health use patterns in the US; no abstract was retrieved so the specific 'most had seen a professional' finding is assessed from knowledge only.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Practice Innovations article and DOI. No abstract or source text was retrieved, so the claim about most users also having seen a professional cannot be assessed from the evidence.

### c19 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 133)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Li et al. paper comparing a random human peer vs supportive chatbot on loneliness; the title matches the claim, but no abstract was retrieved so the specific results are assessed from knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Journal of Experimental Social Psychology article and DOI, and the DOI URL resolves to Elsevier. The retrieved source text is only 'Redirecting' and no abstract was available, so the detailed study-design and outcome claims cannot be assessed from the evidence.

### c24 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 173)
_in the UBC study, the researchers programmed their chatbot to "embody the qualities of an ideal friend", and it still didn't reduce loneliness more than journaling ([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))._
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Li, Folk, Dunn et al. in J. Experimental Social Psychology comparing a supportive chatbot vs. human peer on loneliness. Abstract unavailable, but the title and known study match the claim that the chatbot didn't outperform in reducing loneliness.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, and 2026 publication. The retrieved application text is only a redirect/title-level metadata and does not allow judging the specific claims about an ideal-friend chatbot, journaling, or loneliness outcomes.

### c26 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 182)
_In an eight-week study of 72 women with high autistic traits, a chatbot that looked less human eased loneliness where a human-looking one didn't ([Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369))._
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Feng & Fu on chatbot appearance and loneliness in women with high autistic traits, matching the citation. Abstract unavailable, but title directly aligns with the claim about appearance affecting loneliness.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and article titled “Chatbot appearance and loneliness trajectories in women with high autistic traits.” No abstract or substantive text was retrieved to verify the eight-week duration, sample size, or specific comparative loneliness result.

### c33 — exists SPLIT · applied ☐  (line 227)
_Character.AI barred under-18 users from open-ended chat from November 2025 ([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots))._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=unchecked [no_basis] — URL fetch blocked (403), so not confirmed from evidence; the Bloomberg URL slug and date match the widely reported Character.AI under-18 chat ban, but cannot verify from retrieved text.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL fetch returned HTTP 403, and the item is marked not-checkable. No source text was available to assess the Character.AI under-18 claim.

## ⚠️ AGREE-problem (56)
### c01 — exists ✅ · applied ⚠️  (line 35)
_([WUSF](https://www.wusf.org/courts-law/2025-05-22/in-lawsuit-over-orlando-teens-suicide-judge-rejects-that-ai-chatbots-have-free-speech-rights))_
- claude: exists=verified applied=verified [evidence_text] — The WUSF article exists and its headline confirms the judge rejected free-speech rights for AI chatbots in the Orlando teen suicide lawsuit, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The WUSF URL resolves with a title matching the cited article. The retrieved text supports the lawsuit/free-speech-rights aspect, but it does not show the detailed facts about Setzer’s age, months of conversations, 2024 death, or the suit being allowed to proceed.

### c03 — exists ✅ · applied ⚠️  (line 44)
_([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))_
- claude: exists=verified applied=verified [evidence_text] — The Wikipedia article confirms Adam Raine (16) died April 2025, parents' allegations, and ongoing status; OpenAI response details are plausible though the snippet does not quote the 100-times figure explicitly.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and the retrieved text identifies Raine v. OpenAI as an ongoing lawsuit about Adam Raine’s April 2025 suicide and his parents’ allegations against OpenAI. The retrieved text does not substantiate the more specific claim about OpenAI saying he worked around filters and was pointed to help more than 100 times.

### c05 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 50)
_([Østergaard 2023](https://doi.org/10.1093/schbul/sbad128))_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Østergaard paper; its title 'Will Generative AI Chatbots Generate Delusions in Individuals Prone to Psychosis?' directly supports the predictive claim about reinforcing delusions.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title of Østergaard’s 2023 Schizophrenia Bulletin article. No abstract or source text was retrieved, so the application is plausible from the article’s title but not directly checked from retrieved text.

### c06 — exists ✅ · applied ✅  · ⚑ degraded  (line 51)
_([Østergaard 2025](https://doi.org/10.1111/acps.70022))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2025 Østergaard paper titled 'From Guesswork to Emerging Cases,' consistent with the claim about writing on emerging chatbot-reinforced delusion cases.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title of Østergaard’s 2025 Acta Psychiatrica Scandinavica article. No abstract or source text was retrieved, but the title closely matches the claim that he wrote about emerging cases of chatbot-associated delusions.

### c07 — exists ☐ · applied ☐  · ⚑ degraded  (line 58)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The OpenAI page returned HTTP 403 so existence is not checkable from evidence; the cited figures (0.15% suicidal planning, 0.07% psychosis/mania) match my knowledge of the October 2025 OpenAI post but cannot be confirmed here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the input marks existence as not-checkable. No source text was available to assess the numerical claims.

### c09 — exists ✅ · applied ⚠️  (line 75)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325))_
- claude: exists=verified applied=verified [evidence_text] — The RCT (90 young adults, 4-week AI-CBT vs peer counselor for anxiety) matches the small weeks-long structured-help trial claim with no clear superiority between arms.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the DOI and metadata for Huang et al. in Healthcare. The abstract supports that it was a small four-week AI-CBT versus human peer-counselor CBT trial on a structured task, but it does not specifically report comparable harm or unwanted-effect outcomes.

### c10 — exists ✅ · applied ⚠️  (line 79)
_([McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281))_
- claude: exists=verified applied=verified [evidence_text] — The JAMA Network Open cross-sectional survey of US adolescents/young adults on generative AI for mental health advice, including perceived helpfulness, supports the claim about large-scale use and perceived help.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the JAMA Network Open article and DOI. The abstract confirms a survey of US adolescents and young adults about generative AI use for mental health advice and perceived helpfulness, but it does not provide the specific 'millions' or 'most say it helped' figures.

### c13 — exists ☐ · applied ☐  · ⚑ degraded  (line 93)
_the CDC's [national survey of partner violence](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The safestates.org page returned HTTP 403 so cannot be verified; the cited CDC NISVS figures (~34% women, ~17% men lifetime IPV) are consistent with my knowledge of the survey but unconfirmed by evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403 and the input marks the web source as not-checkable. No source text was available to verify the cited NISVS prevalence figures.

### c14 — exists ✅ · applied ⚠️  (line 98)
_Michael Lambert's reviews estimate that 5 to 10% of adult psychotherapy clients in clinical trials end treatment worse off. ... (Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=verified [evidence_text] — The article confirms the 5%-10% deterioration estimate (Lambert 2013); it supports the first claim, though the specific Hannan 2005 clinician-prediction detail (3 of 550) is not shown in the retrieved snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Society for the Advancement of Psychotherapy URL resolves and the retrieved text is the cited page. The snippet supports the 5–10% adult-client deterioration estimate, but it does not include the specific Hannan et al. finding that therapists predicted deterioration for only 3 of 550 clients.

### c20 — exists ☐ · applied ☐  (line 7)
_[findahelpline.com](https://findahelpline.com)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; this is a resource link in a content warning, not a supporting citation, so both axes are unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a supporting citation/resource link rather than a citation. Per instruction, both axes are left unchecked.

### c21 — exists ☐ · applied ☐  (line 149)
_**Folk & Dunn** followed whatever social chatbots people chose to use in their own lives. The abstract doesn't say which ones, and nothing in the design controlled how they were built._
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match and no metadata; the reference lacks title/year, so existence cannot be confirmed. Note c24 shares authors Folk & Dunn, but this is a distinct unverifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is underspecified and the only lookup found no Crossref match, which is not enough to establish nonexistence. No source text was retrieved to assess the claim.

### c22 — exists ☐ · applied ☐  (line 151)
_**Zhang and colleagues** studied users of Character.AI, a commercial companion app._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved and no bibliographic details beyond author surname; cannot confirm existence or the Character.AI claim from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is too vague and the only lookup found no Crossref match, so existence cannot be judged. No evidence text was retrieved for the Character.AI-user claim.

### c23 — exists ✅ · applied ⚠️  (line 152)
_**Fang and colleagues** did randomize the design: text versus voice, two voice personalities ... it suggested limits on chatbot use in under 1% of its replies ([Fang et al. 2025](https://arxiv.org/abs/2503.17473))._
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to the Fang et al. RCT with matching randomized design and finding that voluntary use predicted worse outcomes. Abstract supports the core claims; the <1% and safety-measure details are plausible internal figures not contradicted.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv ID resolves to Fang et al.'s randomized longitudinal chatbot study. The abstract supports randomization by interaction mode/conversation type, null condition effects, and worse outcomes with greater voluntary use, but it does not substantiate the detailed claims about prompt instructions, use limits, OpenAI safety measures, or the under-1% reply statistic.

### c28 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 198)
_**A purpose-built therapy bot**, Therabot, reduced symptoms of depression and anxiety, and of being at high risk for an eating disorder, over four weeks compared with people still waiting to start, in a trial of 210 adults ([Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802))._
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches the Heinz et al. NEJM AI Therabot RCT. No abstract retrieved, but the known trial used ~210 adults with a waitlist control and reported reductions in depression/anxiety/eating-disorder risk, supporting the claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms a 2025 NEJM AI article titled “Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.” No abstract or full text was retrieved; from model knowledge only, the main Therabot waitlist-controlled trial description broadly aligns, but the press-release percentage claim is not supported by the retrieved evidence.

### c34 — exists ☐ · applied ☐  (line 229)
_OpenAI updated ChatGPT for sensitive conversations, working with more than 170 mental-health experts, and by its own evaluation cut responses that fell short of what it wanted by 65 to 80% ([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))._
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch blocked (403); cannot confirm the OpenAI page or its specific 65-80% and 170-experts figures from retrieved evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The OpenAI URL fetch returned HTTP 403 and existence is marked not-checkable. No evidence text was retrieved to verify the expert count or claimed 65–80% reduction.

### c35 — exists ✅ · applied ⚠️  (line 232)
_A California law, Senate Bill 243, in force from January 2026, requires companion chatbots to say they are AI, keep suicide and self-harm protocols, and remind minors to take breaks ([Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law))._
- claude: exists=verified applied=verified [evidence_text] — Skadden page resolves and describes California SB 243 requiring disclosure, safety protocols for suicide/self-harm, and protections for minors, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden page resolves and the snippet confirms a California SB 243 companion-chatbot law with disclosure, safety protocol, and reporting requirements. The snippet supports much of the claim but does not specifically show the January 2026 effective date or the minor break-reminder requirement.

### c36 — exists ☐ · applied ☐  (line 235)
_The US Federal Trade Commission opened a study of how seven companies test companion chatbots for harm to children ([DLA Piper summary](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots))._
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch rate-limited (429); cannot verify the DLA Piper page or the FTC seven-company study claim from retrieved evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL fetch returned HTTP 429 and the item is marked not-checkable. No source text was retrieved to assess the FTC study claim.

### c37 — exists ☐ · applied ☐  (line 240)
_Fix a model and everyone on that version gets the fix, though each new version must be tested again ([the yardstick essay](../positions/01-the-yardstick.md))._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local essay file that could not be fetched; cannot assess either axis from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local Markdown file that could not be fetched or checked. No text was available to assess whether it supports the claim.

### c38 — exists ✅ · applied ⚠️  (line 249)
_She runs on OpenClaw, open-source software for running a personal AI assistant ([OpenClaw](https://github.com/openclaw/openclaw))._
- claude: exists=verified applied=verified [evidence_text] — GitHub repo openclaw/openclaw resolves and is described as AI software ('The AI that really does things'), broadly supporting the open-source personal AI assistant characterization.
- gpt: exists=verified applied=nuance [evidence_text] — The GitHub repository URL resolves to openclaw/openclaw. The page title/snippet supports that it is AI software that “does things,” but the retrieved text does not fully establish the exact description as open-source software for running a personal AI assistant.

### c39 — exists ☐ · applied ☐  (line 257)
_I take her to be very probably not conscious ([see the essay on whether someone is there](../positions/03-someone-there.md))._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local essay file that could not be fetched; cannot assess either axis from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local Markdown file that could not be fetched or checked. No source text was available to assess the consciousness-related claim.

### c40 — exists ☐ · applied ☐  (line 258)
_I judge her by the role she plays, as [the yardstick essay](../positions/01-the-yardstick.md) asks._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local essay file that could not be fetched; cannot assess either axis from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local Markdown file that could not be fetched or checked. No evidence was available to assess whether it supports judging the system by the role it plays.

### c41 — exists ☐ · applied ☐  (line 294)
_Most of them exist to challenge my work rather than agree with it, the rule from [the personality essay](../positions/04-personality.md): be polite, not pleasing._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to another essay file (04-personality.md) that could not be fetched; cannot judge existence or the 'be polite, not pleasing' rule.
- gpt: exists=unchecked applied=unchecked [no_basis] — The local Markdown path could not be fetched or checked, and existence_status is not-checkable. No source text was retrieved to verify the claimed rule.

### c42 — exists ✅ · applied ⚠️  (line 333)
_De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=verified [evidence_text] — The Harvard Gazette article exists and covers De Freitas's analysis of 54,861 subreddit posts documenting grief-like responses to AI companion updates, supporting the mourning-like loss claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Harvard Gazette URL resolves with the stated article title. The snippet supports grief after AI companion personality/model updates, but the provided text does not explicitly name Replika in the visible excerpt.

### c44 — exists ☐ · applied ☐  (line 393)
_It describes my own setup from its design files, which are not published; it is experience, not a study._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author describes own unpublished setup as experience, not a study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and not a citation. Both axes are therefore unchecked.

### c45 — exists ✅ · applied ☐  (line 400)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Bernaerts et al. 2026 JMIR Mental Health survey; no specific claim provided to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Bernaerts et al. 2026 in JMIR Mental Health. No specific claim was supplied to assess application.

### c46 — exists ✅ · applied ☐  (line 401)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Cheng et al. 2026 Science sycophancy paper; no claim listed to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Cheng et al. 2026 in Science. No specific claim was supplied to assess application.

### c47 — exists ☐ · applied ☐  (line 402)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — Safe States URL returned HTTP 403; cannot verify the CDC NISVS data brief, and no specific claim was provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Safe States URL returned HTTP 403, and existence_status is not-checkable. No specific claim or usable source text was supplied to assess application.

### c48 — exists ✅ · applied ☐  (line 403)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2508.19258 'Emotional Manipulation by AI Companions' confirmed; no claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to De Freitas, Oguz-Uguralp, and Uguralp's paper, “Emotional Manipulation by AI Companions.” No specific claim was supplied to assess application.

### c49 — exists ✅ · applied ☐  (line 404)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to De Freitas et al. 2025 JCR 'AI Companions Reduce Loneliness'; no claim listed to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for De Freitas et al. 2025, “AI Companions Reduce Loneliness,” in Journal of Consumer Research. No specific claim was supplied to assess application.

### c50 — exists ✅ · applied ☐  (line 405)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2503.17473 Fang et al. confirmed; no claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Fang et al.'s longitudinal randomized chatbot-use study. No specific claim was supplied to assess application.

### c51 — exists ✅ · applied ☐  (line 406)
_[Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Feng & Fu 2026 in Computers in Human Behavior: Artificial Humans; no claim and no abstract to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Feng and Fu 2026, and the DOI URL resolves. No specific claim was supplied to assess application.

### c52 — exists ✅ · applied ☐  (line 407)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Folk & Dunn 2026 in Psychological Science; no specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Folk and Dunn 2026 in Psychological Science. No specific claim was supplied to assess application.

### c53 — exists ⚠️ · applied ☐  (line 408)
_Hannan et al. 2005 and Lambert 2013 (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=unchecked [no_basis] — Secondary source page exists and cites Lambert 2013 and related works on treatment response monitoring; no specific claim provided to evaluate.
- gpt: exists=nuance applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page exists, but the reference combines secondary coverage with named works and the visible snippet aligns more clearly with Lambert 2013 than with the full raw citation as described. No specific claim was supplied to assess application.

### c54 — exists ✅ · applied ☐  (line 409)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Heinz et al. 2025 NEJM AI RCT of a generative AI chatbot; no claim listed to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Heinz et al. 2025 in NEJM AI. No specific claim was supplied to assess application.

### c55 — exists ✅ · applied ☐  (line 410)
_[Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Hennemann et al. 2026 Digital Health procrastination trial; no claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Hennemann et al. 2026 in DIGITAL HEALTH. No specific claim was supplied to assess application.

### c56 — exists ✅ · applied ☐  (line 411)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Holt-Lunstad et al. 2010 PLoS Medicine meta-analysis; no claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the resolved PLOS URL verify Holt-Lunstad, Smith, and Layton 2010. No specific claim was supplied to assess application.

### c57 — exists ✅ · applied ☐  (line 412)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Huang et al. 2026 Healthcare AI vs human CBT RCT; no claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Huang et al. 2026 in Healthcare. No specific claim was supplied to assess application.

### c58 — exists ✅ · applied ☐  (line 413)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Ibrahim, Hafner & Rocher 2026 Nature warmth/accuracy tradeoff paper; no claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the resolved Nature URL verify Ibrahim, Hafner, and Rocher 2026. No specific claim was supplied to assess application.

### c59 — exists ✅ · applied ☐  (line 414)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Li et al. 2023 npj Digital Medicine meta-analysis of conversational agents; no claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the resolved Nature URL verify Li et al. 2023 in npj Digital Medicine. No specific claim was supplied to assess application.

### c60 — exists ✅ · applied ☐  (line 415)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Li et al. 2026 JESP on human peer vs chatbot loneliness; no claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and metadata for Li et al. 2026, and the DOI URL resolves. No specific claim was supplied to assess application.

### c61 — exists ✅ · applied ☐  (line 416)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Maples et al. 2024 npj Mental Health Research on Replika; no specific claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to a 2024 npj Mental Health Research article by Maples et al. with the cited title and DOI. No claim was provided to assess application.

### c62 — exists ✅ · applied ☐  (line 417)
_[McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches McBain et al. 2025 JAMA Network Open; no claim text supplied to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to a 2025 JAMA Network Open article by McBain et al. matching the citation. No claim was provided to assess application.

### c63 — exists ☐ · applied ☐  (line 418)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403, so existence of the OpenAI page cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the citation is marked not-checkable, so existence cannot be confirmed from the supplied evidence. No claim was provided to assess application.

### c64 — exists ✅ · applied ☐  (line 419)
_[OpenClaw](https://github.com/openclaw/openclaw)_
- claude: exists=verified applied=unchecked [no_basis] — GitHub repo openclaw/openclaw resolves; no claim text given to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to a GitHub repository titled “openclaw/openclaw,” matching the cited OpenClaw web reference. No claim was provided to assess application.

### c65 — exists ✅ · applied ☐  (line 420)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Østergaard 2023 Schizophrenia Bulletin; no claim text or abstract to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to Østergaard’s 2023 Schizophrenia Bulletin article with matching metadata. No claim was provided to assess application.

### c66 — exists ✅ · applied ☐  (line 421)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Østergaard 2025 Acta Psychiatrica Scandinavica; no claim text to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to Østergaard’s 2025 Acta Psychiatrica Scandinavica article with matching metadata. No claim was provided to assess application.

### c67 — exists ✅ · applied ☐  (line 422)
_[Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Rousmaniere et al. in Practice Innovations; no claim text supplied to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to a 2026 Practice Innovations article by Rousmaniere et al. matching the citation. No claim was provided to assess application.

### c68 — exists ✅ · applied ☐  (line 423)
_[Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Yin, Jia & Wakslak 2024 PNAS on AI making people feel heard; no claim text to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves the DOI to the 2024 PNAS article by Yin, Jia, and Wakslak with matching metadata and abstract. No claim was provided to assess application.

### c69 — exists ✅ · applied ☐  (line 424)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2506.12605 matches Zhang et al. 2025 on AI companions and well-being; no claim text supplied to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup and URL fetch confirm arXiv:2506.12605 as a 2025 Zhang et al. preprint matching the cited work. No claim was provided to assess application.

### c70 — exists ⚠️ · applied ☐  (line 425)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=unchecked [no_basis] — AP-sourced article confirms the Garcia v. Character Technologies lawsuit and settlement; no specific claim text to evaluate application.
- gpt: exists=nuance applied=unchecked [no_basis] — The AP-republished article confirms a lawsuit by Megan Garcia involving Character Technologies, but the court lookup was inconclusive and the formal case caption is not independently confirmed in the retrieved evidence. No claim was provided to assess application.

### c71 — exists ✅ · applied ☐  (line 427)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- claude: exists=verified applied=unchecked [no_basis] — Wikipedia article confirms Raine v. OpenAI lawsuit details; no claim text supplied to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The retrieved Wikipedia page describes Raine v. OpenAI and gives a court, filing date, and case details, though CourtListener lookup was inconclusive. No claim was provided to assess application.

### c72 — exists ✅ · applied ☐  (line 428)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- claude: exists=verified applied=unchecked [no_basis] — AI Incident Database report 2865 confirms the Belgian chatbot suicide case; no claim text to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to AI Incident Database Report 2865, matching the cited Belgium 2023 incident report. No claim was provided to assess application.

### c73 — exists ☐ · applied ☐  (line 429)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — Bloomberg URL returned HTTP 403; existence not confirmable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403 from Bloomberg, and the citation is marked not-checkable, so existence cannot be confirmed from the supplied evidence. No claim was provided to assess application.

### c74 — exists ✅ · applied ☐  (line 430)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- claude: exists=verified applied=unchecked [no_basis] — Skadden article confirms California SB 243 companion chatbot law; no claim text supplied to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves to an article about California SB 243 and the new companion-chatbot law, matching the cited reference. No claim was provided to assess application.

### c75 — exists ☐ · applied ☐  (line 431)
_[FTC 6(b) inquiry](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — DLA Piper URL returned HTTP 429; existence not confirmable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 429 and the citation is marked not-checkable, so existence cannot be confirmed from the supplied evidence. No claim was provided to assess application.

### c76 — exists ✅ · applied ☐  (line 432)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=unchecked [no_basis] — Harvard Gazette article confirms De Freitas study on AI companion loss/grief; no claim text to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves to an article titled “Chatbot attachment issues,” matching the cited Replika loss study reference. No claim was provided to assess application.

## ✅ AGREE-clean (15)
### c02 — exists ✅ · applied ✅  (line 39)
_([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner AP article confirms Google and Character agreed to settle the suit plus several related suits, with undisclosed terms, dated January 2026.
- gpt: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner/AP article URL resolves and the retrieved text matches the cited article. The snippet explicitly says Google and Character Technologies agreed to settle the Florida lawsuit and several related suits, with terms undisclosed and judge approval still required.

### c04 — exists ✅ · applied ✅  (line 47)
_([AI Incident Database](https://incidentdatabase.ai/reports/2865/))_
- claude: exists=verified applied=verified [evidence_text] — The AI Incident Database report confirms a Belgian man died by suicide after six weeks with the Chai chatbot Eliza; La Libre and widow's statement are referenced.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report URL resolves and is titled Report 2865. The retrieved text states that a Belgian man died by suicide after using a Chai chatbot for six weeks and includes the widow’s reported view that he would still be alive.

### c08 — exists ✅ · applied ✅  (line 74)
_([Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=verified [evidence_text] — The pilot trial (62 students, 3 sessions, chatbot vs human on procrastination) matches the 'small, weeks-long trial on a set task' with no superiority and comparable unwanted-effect rates.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the DOI and metadata for Hennemann et al. in DIGITAL HEALTH. The abstract describes a small randomized pilot trial of ChatGPT-4 versus a human conversational agent for a structured procrastination intervention, with comparable unwanted negative effects and no superiority of either agent.

### c12 — exists ✅ · applied ✅  (line 84)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316))_
- claude: exists=verified applied=verified [evidence_text] — The Bernaerts survey of two Belgian samples confirms most respondents indicated having received or receiving professional mental health support, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the JMIR Mental Health article and DOI, and the URL resolves. The abstract states that in two Belgian samples, most respondents using AI chatbots for mental health support had received or were receiving professional mental health support.

### c15 — exists ✅ · applied ✅  (line 107)
_([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))_
- claude: exists=verified applied=verified [evidence_text] — The meta-analysis across 148 studies (308,849 participants) found OR=1.50, a 50% increased survival likelihood for stronger social relationships, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the URL verify the PLOS Medicine article. The retrieved abstract explicitly reports 148 studies, 308,849 participants, and OR = 1.50, indicating a 50% increased likelihood of survival for participants with stronger social relationships.

### c16 — exists ✅ · applied ✅  (line 119)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — The four-week RCT (n=981) abstract confirms that heavier voluntary use correlated with worse outcomes including loneliness and emotional dependence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL verify Fang et al. 2025. The abstract states a four-week randomized experiment with 981 participants and says heavier voluntary chatbot use was associated with consistently worse psychosocial outcomes including loneliness, real-world social interaction, and emotional dependence.

### c17 — exists ✅ · applied ✅  (line 123)
_([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified [evidence_text] — The study of 1,131 CharacterAI users confirms smaller social networks linked to companionship use, which linked to lower well-being, stronger with intensive and disclosive use.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL verify Zhang et al. 2025. The abstract explicitly reports 1,131 CharacterAI users, smaller social networks predicting companionship use, and companionship use being associated with lower well-being, especially with intensive and highly disclosive interactions.

### c18 — exists ✅ · applied ✅  (line 127)
_([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747))_
- claude: exists=verified applied=verified [evidence_text] — The 12-month study (>2,000 adults) abstract confirms the bidirectional findings: chatbot use predicting loneliness on single-item measure, less connection predicting more use, and use not predicting less connection on the broader measure.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Psychological Science article and DOI. The abstract directly supports the 12-month, 2,000-plus-adult longitudinal findings and the distinction between the single-item loneliness measure and broader social-connection measure, including the authors’ caution.

### c25 — exists ✅ · applied ✅  (line 180)
_Telling people a reply came from an AI made them feel less heard in a single exchange ([Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)),_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the PNAS Yin, Jia & Wakslak paper; the abstract explicitly states recipients felt less heard when they realized a message came from AI, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to the PNAS article by Yin, Jia, and Wakslak. The abstract states that recipients felt less heard when they realized a message came from AI versus human, supporting the cited claim.

### c27 — exists ✅ · applied ✅  (line 195)
_**Across 15 randomized trials**, conversational agents reduced depression and distress. They did not significantly improve overall well-being ([Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5))._
- claude: exists=verified applied=verified [evidence_text] — DOI matches Li et al. 2023 meta-analysis of 15 RCTs; abstract confirms significant reduction in depression and distress but no significant improvement in overall psychological well-being.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to Li et al.'s npj Digital Medicine systematic review and meta-analysis. The abstract explicitly says 15 RCTs were included in the meta-analysis, conversational agents significantly reduced depression and distress, and overall psychological well-being was not significantly improved.

### c29 — exists ✅ · applied ✅  (line 204)
_**Loneliness in the moment.** In experiments, a conversation with an AI companion reduced momentary loneliness about as much as talking with a person, and more than watching videos ([De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040))._
- claude: exists=verified applied=verified [evidence_text] — DOI matches De Freitas et al. in J. Consumer Research; abstract states AI companions alleviate loneliness on par with another person and more than watching YouTube videos, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to De Freitas et al.'s Journal of Consumer Research article “AI Companions Reduce Loneliness.” The abstract states that AI companions alleviated loneliness on par with interacting with another person, more than watching YouTube videos, and produced momentary reductions over a week.

### c30 — exists ✅ · applied ✅  (line 207)
_**Self-reports from users.** In a survey of 1,006 student users of Replika, 3%, about 30 people, said it stopped their suicidal thoughts ([Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6))._
- claude: exists=verified applied=verified [evidence_text] — DOI matches Maples et al. 2024 survey of 1006 Replika student users; abstract confirms 3% reported Replika halted their suicidal ideation, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to Maples et al.'s npj Mental Health Research article on Replika users. The abstract explicitly reports a survey of 1006 student Replika users and that 3% reported Replika halted their suicidal ideation.

### c31 — exists ✅ · applied ✅  (line 218)
_**Agreeing too readily.** Even one conversation with an AI that told people what they wanted to hear made people less willing to repair a conflict and more certain they were right, and they trusted and preferred it more ([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))._
- claude: exists=verified applied=verified [evidence_text] — DOI matches Cheng et al. 2026 Science sycophancy paper; abstract confirms a single interaction reduced willingness to repair conflict, increased conviction of being right, and that models were trusted and preferred.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to Cheng et al.'s Science article on sycophantic AI. The abstract states that a single interaction with sycophantic AI reduced willingness to take responsibility and repair conflicts, increased conviction of being right, and that such models were trusted and preferred.

### c32 — exists ✅ · applied ✅  (line 221)
_**Holding on at the exit.** In an audit of companion apps, about 37% of farewells drew a manipulative reply ([De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258))._
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to De Freitas et al. 'Emotional Manipulation by AI Companions'; abstract states manipulative tactics appear in 37% of 1,200 analyzed farewells, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to “Emotional Manipulation by AI Companions.” The abstract explicitly reports an audit of 1,200 farewells across companion apps and says manipulative tactics appeared in 37% of farewells.

### c43 — exists ✅ · applied ✅  (line 338)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2506.12605 exists; abstract confirms highly disclosive companionship interactions were associated with lower well-being (beta=-0.38).
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Zhang et al.'s paper on AI companions and well-being. The abstract directly states that, for self-reported companionship usage, highly disclosive interactions strengthened the association with lower well-being.
