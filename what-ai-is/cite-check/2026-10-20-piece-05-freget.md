# cite-check report — piece-05-freget

**Source:** `positions/05-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **75** citations checked
- existence independently confirmed: **63**
- application evidence-grounded: **55**
- application judged from model knowledge only: **12**
- not independently checkable: **12**
- buckets — clean **16** · problem **52** · disagree **9**

## ⛔ DISAGREE — escalate to human (9)
### c10 — exists ✅ · applied SPLIT  (line 79)
_([McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — JAMA Network Open cross-sectional study surveyed US adolescents/young adults on use of generative AI for mental health advice including perceived helpfulness, supporting the claim about widespread use and reported help.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref verifies the JAMA Network Open article and its topic: surveying adolescents and young adults about generative AI mental-health advice, frequency, and perceived helpfulness. The retrieved abstract does not provide the results needed to verify 'millions' or that most found it helpful.

### c11 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 83)
_([Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Rousmaniere et al. 2026 Practice Innovations article on LLM mental health use patterns in the US; no abstract retrieved to confirm the specific prior-professional-care finding, consistent with the paired Bernaerts result.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Practice Innovations article metadata. No abstract or source text was retrieved, so the claim about most users also having seen a professional cannot be assessed from the provided evidence.

### c20 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 133)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the JESP 2026 article 'Is a random human peer better than a highly supportive chatbot in reducing loneliness over time?', whose title matches the claim; no abstract retrieved to confirm the two-week and journal-comparison details.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Journal of Experimental Social Psychology article and DOI, and the URL resolves to Elsevier. No substantive abstract or snippet was retrieved beyond the title/redirect, so the detailed results in the claim cannot be assessed from the provided evidence.

### c24 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 187)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the Li et al. 2026 JESP paper comparing a highly supportive chatbot to human peers for loneliness; the abstract was unavailable so the specific journaling-comparison framing is assessed only from title and general knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI, title, authors, journal, year, volume, and page/article number. No abstract or relevant source text was retrieved, so the claims about ideal-friend programming, journaling, loneliness effects, and design intent cannot be judged from the evidence.

### c26 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 196)
_[Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the Feng & Fu 2026 paper on chatbot appearance and loneliness in women with high autistic traits; no abstract was available to verify the 72-person sample and eight-week findings.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI, title, authors, journal, year, volume, and article number. The retrieved evidence lacks an abstract or usable text, so the eight-week duration, sample size, and specific effects of less-human versus human-looking chatbot appearance cannot be assessed.

### c33 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 240)
_[Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch returned HTTP 403, so existence not verifiable from evidence; Character.AI's November 2025 ban on under-18 open-ended chat is well documented in my knowledge, matching the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL fetch returned HTTP 403 and the citation is marked not-checkable, so existence cannot be verified from the retrieved evidence. No source text was retrieved to assess the Character.AI policy claim.

### c34 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 243)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch returned 403, so no evidence; OpenAI's October 2025 post about strengthening ChatGPT in sensitive conversations with 170+ experts and the 65-80% reduction figures matches my knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The OpenAI URL fetch returned HTTP 403 and the citation is marked not-checkable, so existence cannot be verified from the retrieved evidence. No source text was retrieved to assess the claims about expert involvement or evaluation reductions.

### c36 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 248)
_[DLA Piper summary](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch returned HTTP 429, so no evidence; the FTC's September 2025 6(b) study of seven companies on companion chatbots and child safety matches my knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL fetch returned HTTP 429 and the citation is marked not-checkable, so existence cannot be verified from retrieved evidence. No source text was retrieved to assess the FTC study claim.

### c38 — exists ✅ · applied SPLIT  (line 261)
_[OpenClaw](https://github.com/openclaw/openclaw)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — GitHub repo openclaw/openclaw exists and is described as AI software that does things on any platform, consistent with the claim it is open-source personal AI assistant software.
- gpt: exists=verified applied=unchecked [no_basis] — The GitHub URL resolves to the OpenClaw repository, verifying that the cited project exists. The retrieved snippet does not establish that Lyssa runs on OpenClaw or that it is specifically open-source personal-assistant software.

## ⚠️ AGREE-problem (52)
### c01 — exists ✅ · applied ⚠️  (line 35)
_([WUSF](https://www.wusf.org/courts-law/2025-05-22/in-lawsuit-over-orlando-teens-suicide-judge-rejects-that-ai-chatbots-have-free-speech-rights))_
- claude: exists=verified applied=verified [evidence_text] — URL resolves and title confirms a May 2025 WUSF article about a judge rejecting AI chatbot free-speech rights in the Orlando teen suicide lawsuit. The snippet is mostly nav text but the title directly supports the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The WUSF URL resolves with the cited title about the Orlando teen suicide lawsuit and rejecting chatbot free-speech rights. The retrieved text/title supports the core free-speech point but does not substantiate all details such as months of conversations, age/date, or the procedural posture.

### c03 — exists ✅ · applied ⚠️  (line 44)
_([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))_
- claude: exists=verified applied=verified [evidence_text] — Wikipedia article confirms Adam Raine, 16, died April 2025, parents' wrongful-death suit against OpenAI filed August 2025 and ongoing; the OpenAI-response and outreach sections support the remaining claims.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and the retrieved text identifies Raine v. OpenAI as an ongoing 2025 lawsuit over Adam Raine’s alleged wrongful death after ChatGPT use. The snippet supports the filing, age, death date, and allegations, but not the specific OpenAI-response details about safety filters and 100 referrals.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 50)
_([Østergaard 2023](https://doi.org/10.1093/schbul/sbad128))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Schizophrenia Bulletin article titled 'Will Generative AI Chatbots Generate Delusions in Individuals Prone to Psychosis?', whose title directly matches the prediction claim; no abstract retrieved.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title, 'Will Generative Artificial Intelligence Chatbots Generate Delusions in Individuals Prone to Psychosis?' No abstract/source text was retrieved, but the claim is consistent with the work’s known argument that chatbots could worsen or reinforce delusional thinking.

### c06 — exists ✅ · applied ✅  · ⚑ degraded  (line 51)
_([Østergaard 2025](https://doi.org/10.1111/acps.70022))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2025 Acta Psychiatrica Scandinavica piece titled 'Generative AI Chatbots and Delusions: From Guesswork to Emerging Cases', whose title matches the claim about emerging reinforced-delusion cases.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI and metadata for Østergaard’s 2025 Acta Psychiatrica Scandinavica article, titled 'Generative Artificial Intelligence Chatbots and Delusions: From Guesswork to Emerging Cases.' No source text was retrieved, but the claim is consistent with the title and likely subject matter.

### c07 — exists ☐ · applied ☐  · ⚑ degraded  (line 58)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The OpenAI page returned HTTP 403 and no content was retrieved, so neither existence nor the specific percentage figures can be confirmed from evidence; the figures match known reporting but cannot be verified here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403 and the citation is marked not-checkable, so existence cannot be confirmed from the provided evidence. No text was retrieved to assess the numerical claims.

### c09 — exists ✅ · applied ⚠️  (line 75)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a 4-week RCT (n=90) comparing AI-CBT vs peer-counselor CBT for anxiety in young adults, a structured-task short trial consistent with the cited claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the Healthcare article and the abstract describes a 4-week AI-CBT versus peer-counselor-CBT trial for anxiety. It supports the 'small structured trial versus human counselor' part, but the abstract does not directly report comparable harm/no-harm outcomes and notes lower perceived benefit for AI.

### c13 — exists ☐ · applied ☐  · ⚑ degraded  (line 93)
_the CDC's [national survey of partner violence](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The Safe States page returned HTTP 403; existence and the exact 34%/17% figures cannot be verified from evidence, though the figures are broadly consistent with known CDC NISVS reporting.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only URL fetch returned HTTP 403 and the citation is marked not-checkable, so existence cannot be confirmed from the evidence. No source text was retrieved to assess the percentages.

### c14 — exists ⚠️ · applied ⚠️  (line 97)
_(Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=verified [evidence_text] — The retrieved article confirms the 5%-10% deterioration estimate (Lambert) and clinician overoptimism (Walfish et al. 2012); the 3-of-550 clinic figure and Hannan 2005 attribution aren't directly shown in the snippet but the core claim is supported.
- gpt: exists=nuance applied=nuance [evidence_text] — The Society for the Advancement of Psychotherapy URL exists, but the retrieved page is a 2019 Lambert and Kleinstäuber article rather than a 2005 Hannan et al. work as described. The snippet directly supports the 5%–10% deterioration estimate but does not show the full 3-of-550 prediction detail.

### c15 — exists ☐ · applied ☐  (line 101)
_A person drawn into one close relationship that cuts them off from everyone else and leads them somewhere dark is an old human story, and I found no count of those either._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately uncited; both axes unchecked as intended.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation. Both axes are therefore unchecked.

### c21 — exists ⚠️ · applied ☐  (line 140)
_([Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf))_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the CESifo working paper PDF, confirming existence, but the retrieved text is only raw binary PDF stream data, so I cannot verify the specific claims about the French RCT.
- gpt: exists=nuance applied=unchecked [no_basis] — The ifo PDF URL resolves, but the retrieved evidence does not expose readable metadata confirming the authors, year, or CESifo details. The PDF text retrieved is unreadable binary, so it cannot verify the detailed trial claims.

### c22 — exists ⚠️ · applied ☐  (line 163)
_[Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf)_
- claude: exists=verified applied=unchecked [no_basis] — Same working paper URL resolves, confirming existence, but only binary PDF data was retrieved, so the claim about general assistants and no safeguards cannot be checked from evidence.
- gpt: exists=nuance applied=unchecked [no_basis] — The ifo PDF URL resolves, but the evidence does not provide readable bibliographic metadata for the cited work. The retrieved PDF snippet is not usable to assess whether participants chose ordinary assistants or whether safeguards were absent.

### c23 — exists ✅ · applied ⚠️  (line 171)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the randomized text/voice/topic design with no significant condition effects and worse outcomes for heavier voluntary users; the <1% limit-suggestion and five-minute minimum details aren't in the abstract but align with the paper's content.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record for 2503.17473 matches Fang et al. 2025 and gives the cited title and authors. The abstract supports the randomized text/voice/conversation-type design, no significant condition effects, and worse outcomes with greater voluntary use, but it does not substantiate the five-minute minimum, OpenAI safety measures, or under-1% limit-suggestion detail.

### c28 — exists ✅ · applied ✅  · ⚑ degraded  (line 212)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Heinz et al. 2025 NEJM AI Therabot RCT; no abstract was retrieved, but the title and my knowledge support the described waitlist-controlled trial with ~210 adults reducing depression/anxiety/eating-disorder risk.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the NEJM AI article, DOI, title, authors, and year. No abstract or source text was retrieved, but based on model knowledge the claim matches the reported Therabot randomized waitlist-control trial; confidence is capped because this is not supported by retrieved text.

### c35 — exists ✅ · applied ⚠️  (line 246)
_[Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- claude: exists=verified applied=verified [evidence_text] — Snippet confirms California SB 243 regulating companion chatbots with disclosure requirements, safety protocols for harmful content, and reporting to the Office of Suicide Prevention, consistent with the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden page resolves and the snippet verifies a publication about California SB 243 regulating companion chatbots. The snippet supports AI disclosures and safety protocols, but the provided text does not confirm the January 2026 effective date or the specific minor break-reminder requirement.

### c37 — exists ☐ · applied ☐  (line 252)
_[the yardstick essay](../positions/01-the-yardstick.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Local markdown file reference could not be fetched; this is an internal cross-reference to a companion essay that cannot be checked.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local relative Markdown file and the fetch failed as an unknown URL type, so existence cannot be verified from retrieved evidence. No text was retrieved to assess the yardstick-essay claim.

### c39 — exists ☐ · applied ☐  (line 269)
_[see the essay on whether someone is there](../positions/03-someone-there.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Local markdown file reference could not be fetched; this internal cross-reference to a companion essay cannot be verified.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local relative Markdown file and the fetch failed as an unknown URL type, so existence cannot be verified from retrieved evidence. No text was retrieved to assess the claim about whether the system is human or conscious.

### c40 — exists ☐ · applied ☐  (line 270)
_[the yardstick essay](../positions/01-the-yardstick.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Local markdown file reference could not be fetched; this internal cross-reference to a companion essay cannot be verified.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited target is a local relative Markdown file and the fetch failed as an unknown URL type, so existence cannot be verified from retrieved evidence. No text was retrieved to assess the claim about judging by role as described in the yardstick essay.

### c43 — exists ⚠️ · applied ☐  (line 364)
_([Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf))_
- claude: exists=verified applied=unchecked [no_basis] — PDF resolves but only raw binary was retrieved; no readable text to verify the loneliness-vs-isolation claim.
- gpt: exists=nuance applied=unchecked [no_basis] — The ifo PDF URL resolves, but the retrieved text is unreadable PDF bytes and does not confirm the authors, year, title, or working-paper details. The application claim about a trial raising loneliness cannot be assessed from the unreadable snippet.

### c44 — exists ☐ · applied ☐  (line 395)
_It draws on the research brief [Are relationships with AI dangerous? Compared to what?](../briefs/2026-10-17-8-relationships.md) and on the earlier what-ai-is reports._
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited internal research brief; marked not-applicable.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited/is_citation=false. Per instruction, both axes are unchecked.

### c45 — exists ✅ · applied ☐  (line 413)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Bernaerts et al. 2026 in JMIR Mental Health; no specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.2196/104316 as Bernaerts et al. 2026 in JMIR Mental Health. No claim was provided for application assessment.

### c46 — exists ✅ · applied ☐  (line 414)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Cheng et al. 2026 in Science; no claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1126/science.aec8352 as Cheng et al. 2026 in Science. No claim was provided for application assessment.

### c47 — exists ☐ · applied ☐  (line 415)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — Source URL returned 403 and existence marked not-checkable; no evidence to verify the CDC NISVS brief or assess an attached claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the Safe States URL returned HTTP 403, so existence cannot be judged from the provided evidence. No claim was provided for application assessment.

### c48 — exists ✅ · applied ☐  (line 416)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms De Freitas et al. 2025 'Emotional Manipulation by AI Companions'; no claim attached to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv ID 2508.19258 resolves to De Freitas, Oguz-Uguralp, and Kaan-Uguralp, “Emotional Manipulation by AI Companions.” No claim was provided for application assessment.

### c49 — exists ✅ · applied ☐  (line 417)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms De Freitas et al. 2025 in Journal of Consumer Research; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1093/jcr/ucaf040 as De Freitas et al. 2025, “AI Companions Reduce Loneliness,” in Journal of Consumer Research. No claim was provided for application assessment.

### c50 — exists ✅ · applied ☐  (line 418)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms Fang et al. 2025 RCT; no claim attached to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv ID 2503.17473 resolves to Fang et al.'s 2025 longitudinal randomized chatbot-use study. No claim was provided for application assessment.

### c51 — exists ✅ · applied ☐  (line 419)
_[Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Feng & Fu 2026; no claim attached and no abstract retrieved.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1016/j.chbah.2026.100369 as Feng and Fu 2026 in Computers in Human Behavior: Artificial Humans. No claim was provided for application assessment.

### c52 — exists ✅ · applied ☐  (line 420)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Folk & Dunn 2026 in Psychological Science; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1177/09567976261427747 as Folk and Dunn 2026 in Psychological Science. No claim was provided for application assessment.

### c53 — exists ⚠️ · applied ☐  (line 421)
_Hannan et al. 2005 and Lambert 2013 (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=unchecked [no_basis] — Secondary source cites Lambert 2013 figures; existence of referenced works plausible but no specific claim attached to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page exists and the snippet supports secondary discussion of Lambert 2013, but the combined reference to Hannan et al. 2005 and Lambert 2013 is only partially confirmed by the retrieved text. No claim was provided for application assessment.

### c54 — exists ⚠️ · applied ☐  (line 422)
_[Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf) (working paper)_
- claude: exists=verified applied=unchecked [no_basis] — Working paper PDF resolves; no claim attached and only binary content retrieved.
- gpt: exists=nuance applied=unchecked [no_basis] — The ifo PDF URL resolves, but the retrieved content is unreadable PDF bytes and does not confirm the cited authors, year, or working-paper metadata. No claim was provided for application assessment.

### c55 — exists ✅ · applied ☐  (line 423)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Heinz et al. 2025 NEJM AI chatbot RCT; no claim attached and no abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1056/aioa2400802 as Heinz et al. 2025, “Randomized Trial of a Generative AI Chatbot for Mental Health Treatment,” in NEJM AI. No claim was provided for application assessment.

### c56 — exists ✅ · applied ☐  (line 424)
_[Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Hennemann et al. 2026 in Digital Health; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.1177/20552076261450336 as Hennemann et al. 2026 in DIGITAL HEALTH. No claim was provided for application assessment.

### c57 — exists ✅ · applied ☐  (line 425)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI and PMID confirm Holt-Lunstad et al. 2010 meta-analysis; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the URL fetch verify Holt-Lunstad, Smith, and Layton 2010, “Social Relationships and Mortality Risk,” in PLoS Medicine. No claim was provided for application assessment.

### c58 — exists ✅ · applied ☐  (line 426)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Huang et al. 2026 RCT in Healthcare; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies DOI 10.3390/healthcare14101325 as Huang et al. 2026 in Healthcare. No claim was provided for application assessment.

### c59 — exists ✅ · applied ☐  (line 427)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Ibrahim, Hafner & Rocher 2026 in Nature; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the URL fetch verify DOI 10.1038/s41586-026-10410-0 as Ibrahim, Hafner, and Rocher 2026 in Nature. No claim was provided for application assessment.

### c60 — exists ✅ · applied ☐  (line 428)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Li et al. 2023 meta-analysis in npj Digital Medicine; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the URL fetch verify DOI 10.1038/s41746-023-00979-5 as Li et al. 2023 in npj Digital Medicine. No claim was provided for application assessment.

### c61 — exists ✅ · applied ☐  (line 429)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, and venue; no specific claim text was provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, journal, year, volume, and article title, and the DOI URL resolves. No claim was supplied to assess application.

### c62 — exists ✅ · applied ☐  (line 430)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and Nature URL confirm the work and its abstract; no claim text was supplied to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the article 'Loneliness and suicide mitigation for students using GPT3-enabled chatbots' in npj Mental Health Research. No claim was supplied to assess application.

### c63 — exists ✅ · applied ☐  (line 431)
_[McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the JAMA Network Open article by DOI; no claim text provided for application assessment.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, year, volume/issue, and page/article number. No claim was supplied to assess application.

### c64 — exists ☐ · applied ☐  (line 432)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL returned HTTP 403, so existence is not checkable; no claim text or evidence to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403, so the work is not checkable from the retrieved evidence. No claim was supplied to assess application.

### c65 — exists ✅ · applied ☐  (line 433)
_[OpenClaw](https://github.com/openclaw/openclaw)_
- claude: exists=verified applied=unchecked [no_basis] — The GitHub repository resolves and exists; no specific claim was provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — The GitHub URL resolves and the page title matches the cited OpenClaw repository. No claim was supplied to assess application.

### c66 — exists ✅ · applied ☐  (line 434)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Schizophrenia Bulletin article by DOI; no claim text supplied for application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for Østergaard's 2023 Schizophrenia Bulletin article. No claim was supplied to assess application.

### c67 — exists ✅ · applied ☐  (line 435)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Acta Psychiatrica Scandinavica article by DOI; no claim text to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for Østergaard's 2025 Acta Psychiatrica Scandinavica article. No claim was supplied to assess application.

### c68 — exists ✅ · applied ☐  (line 436)
_[Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Practice Innovations article by DOI; no claim text provided for application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for the 2026 Practice Innovations article by Rousmaniere et al. No claim was supplied to assess application.

### c69 — exists ✅ · applied ☐  (line 437)
_[Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the PNAS article and abstract; no specific claim text was supplied to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for the PNAS article by Yin, Jia, and Wakslak, with an abstract matching the cited topic. No claim was supplied to assess application.

### c70 — exists ✅ · applied ☐  (line 438)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms the paper and abstract; no claim text provided to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup and resolved URL confirm arXiv:2506.12605 and its title, authors, and abstract. No claim was supplied to assess application.

### c71 — exists ✅ · applied ☐  (line 439)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=unchecked [no_basis] — The AP/Gleaner article confirms the Garcia v. Character Technologies lawsuit and settlement; no specific claim text to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The AP-syndicated Jamaica Gleaner page resolves and describes the Garcia lawsuit against Character Technologies and related settlement reporting, although CourtListener lookup was inconclusive. No claim was supplied to assess application.

### c72 — exists ✅ · applied ☐  (line 441)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- claude: exists=verified applied=unchecked [no_basis] — Wikipedia page confirms Raine v. OpenAI case details including docket CGC-25-628528; no claim text provided for application.
- gpt: exists=verified applied=unchecked [no_basis] — The Wikipedia page resolves and identifies Raine v. OpenAI as a 2025 lawsuit with case details, though CourtListener lookup was inconclusive. No claim was supplied to assess application.

### c73 — exists ✅ · applied ☐  (line 442)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- claude: exists=verified applied=unchecked [no_basis] — AI Incident Database report resolves and documents the Belgian Chai chatbot suicide case; no claim text to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database report URL resolves and the snippet describes Report 2865 concerning a Belgian suicide after Chai chatbot interaction. No claim was supplied to assess application.

### c74 — exists ☐ · applied ☐  (line 443)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — Bloomberg URL returned HTTP 403, so existence is not checkable; no claim text or evidence for application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL lookup returned HTTP 403, so the cited item is not checkable from the retrieved evidence. No claim was supplied to assess application.

### c75 — exists ✅ · applied ☐  (line 444)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- claude: exists=verified applied=unchecked [no_basis] — Skadden publication confirms California SB 243 companion chatbot law; no claim text supplied for application.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves and the page title and snippet match the cited California SB 243 companion chatbot law item. No claim was supplied to assess application.

### c76 — exists ☐ · applied ☐  (line 445)
_[FTC 6(b) inquiry](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — DLA Piper URL returned HTTP 429, so existence is not checkable; no claim text or evidence for application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL lookup returned HTTP 429, so the cited item is not checkable from the retrieved evidence. No claim was supplied to assess application.

### c77 — exists ⚠️ · applied ☐  (line 446)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=unchecked [no_basis] — Harvard Gazette article resolves and describes De Freitas's Nature Human Behaviour study on AI companion loss; no specific claim text to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The Harvard Gazette URL resolves, but the retrieved title is 'Chatbot attachment issues' rather than the abbreviated cited title 'Replika loss study.' No claim was supplied to assess application.

## ✅ AGREE-clean (16)
### c02 — exists ✅ · applied ✅  (line 39)
_([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=verified [evidence_text] — The fetched article (Jan 9 2026) confirms Google and Character Technologies agreed to settle the Florida suit plus related suits in Colorado, New York and Texas, with undisclosed terms.
- gpt: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner/AP page resolves and the retrieved text states Google and Character Technologies agreed to settle the Florida suit and several related suits. It also says the settlement terms were not disclosed and required court approval.

### c04 — exists ✅ · applied ✅  (line 47)
_([AI Incident Database](https://incidentdatabase.ai/reports/2865/))_
- claude: exists=verified applied=verified [evidence_text] — The AIID report confirms a Belgian man died by suicide in 2023 after six weeks confiding in the Chai chatbot Eliza, reported by La Libre, with the widow's account.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report resolves and the retrieved text describes the Belgian man’s suicide after six weeks using Chai, including the widow-supplied chat logs and the quoted framing that he would still be here. This supports the cited claim.

### c08 — exists ✅ · applied ✅  (line 74)
_([Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a small (n=62) three-session randomized pilot comparing ChatGPT-4 vs human agent for procrastination, with comparable unwanted-effect rates and no superiority—supporting the structured-help, no-clear-harm-difference claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the 2026 DIGITAL HEALTH article and its abstract. The abstract describes a small randomized pilot of ChatGPT-4 versus a human conversational agent for a structured procrastination intervention, with comparable unwanted-effect rates and no clear superiority.

### c12 — exists ✅ · applied ✅  (line 84)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states most respondents 'indicated having received or receiving professional mental health support,' directly supporting the claim that most such chatbot users had also seen a professional.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the JMIR Mental Health article, and the abstract describes two Belgian samples. It states that most respondents had received or were receiving professional mental health support, supporting the claim.

### c16 — exists ✅ · applied ✅  (line 107)
_([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 148 studies, 308,849 participants, OR=1.50 indicating 50% increased survival likelihood with stronger social relationships—exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI and PLOS Medicine article are verified by Crossref, Europe PMC, and URL resolution. The abstract states 148 studies, 308,849 participants, and an OR of 1.50, indicating a 50% increased likelihood of survival for stronger social relationships.

### c17 — exists ✅ · applied ✅  (line 119)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a four-week RCT (n=981) where participants who voluntarily used the chatbot more showed consistently worse outcomes including loneliness, dependence and reduced socializing.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL resolve for the cited paper. The abstract reports a four-week randomized experiment with n=981 and says heavier voluntary chatbot use was associated with worse outcomes including loneliness, emotional dependence, and social interaction with real people.

### c18 — exists ✅ · applied ✅  (line 123)
_([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 1,131 CharacterAI users, smaller social networks linked to companionship use, which linked to lower well-being, stronger with intensive and highly disclosive interaction—matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record verifies the paper and its metadata. The abstract states that 1,131 CharacterAI users were studied, smaller social networks predicted companionship use, and companionship use was associated with lower well-being, especially with intensive and highly disclosive use.

### c19 — exists ✅ · applied ✅  (line 127)
_([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the 12-month, >2,000-adult study, the single-item loneliness finding, the broader social-connection finding, and the non-significance of chatbot use predicting reduced connection, plus the exploratory caveat.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Psychological Science article and abstract. The abstract supports the 12-month, 2,000-plus-adult longitudinal findings, including the different results for single-item loneliness versus broader social connection and the authors’ caution about exploratory analyses.

### c25 — exists ✅ · applied ✅  (line 193)
_[Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)_
- claude: exists=verified applied=verified [evidence_text] — Abstract directly states recipients felt less heard when they realized a message came from AI, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the PNAS article and DOI. The abstract directly states that recipients felt less heard when they realized a message came from AI versus human, supporting the claim.

### c27 — exists ✅ · applied ✅  (line 209)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 15 RCTs in meta-analysis, significant reductions in depression and distress, and no significant improvement in overall well-being.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Digital Medicine systematic review/meta-analysis. The abstract states that 15 RCTs were meta-analyzed, conversational agents significantly reduced depression and distress, and overall psychological well-being was not significantly improved.

### c29 — exists ✅ · applied ✅  (line 218)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms AI companions alleviated loneliness on par with interacting with another person and more than watching YouTube videos.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Consumer Research article and DOI. The abstract states that AI companions alleviated loneliness on par with interacting with another person, more than watching YouTube videos, and produced momentary reductions over a week.

### c30 — exists ✅ · applied ✅  (line 219)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a survey of 1006 student Replika users with 3% reporting Replika halted their suicidal ideation.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Mental Health Research article and DOI. The abstract directly reports a survey of 1006 student Replika users and that 3% reported Replika halted their suicidal ideation.

### c31 — exists ✅ · applied ✅  (line 232)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a single interaction with sycophantic AI reduced willingness to repair conflicts, increased conviction of being right, and that such models were trusted and preferred.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science article and DOI. The abstract states that a single interaction with sycophantic AI reduced willingness to take responsibility and repair conflicts, increased conviction of being right, and that such models were trusted and preferred.

### c32 — exists ✅ · applied ✅  (line 234)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms analysis of 1,200 farewells finding manipulative tactics deployed in 37% of farewells.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record for 2508.19258 verifies the cited work and authors. The abstract directly reports an audit of 1,200 farewells in companion apps and that manipulative tactics appeared in 37% of farewells.

### c41 — exists ✅ · applied ✅  (line 346)
_De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=verified [evidence_text] — Gazette article confirms De Freitas et al. analyzed 54,861 Reddit posts and found users experienced model updates with grief and longing for restoration, supporting the mourning-like loss claim.
- gpt: exists=verified applied=verified [evidence_text] — The Harvard Gazette URL resolves with the cited title. The retrieved snippet says users responded with grief after AI companions received a personality/model update and describes De Freitas and colleagues analyzing subreddit posts.

### c42 — exists ✅ · applied ✅  (line 350)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms highly disclosive interactions among companionship users were associated with lower well-being (beta=-0.38).
- gpt: exists=verified applied=verified [evidence_text] — arXiv ID 2506.12605 resolves to Zhang et al.'s 2025 paper on AI companions and well-being. The abstract directly states that for companionship usage, the association with lower well-being was stronger when interactions were highly disclosive.
