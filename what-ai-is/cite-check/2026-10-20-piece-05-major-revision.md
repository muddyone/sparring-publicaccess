# cite-check report — piece-05-major-revision-2026-10-20

**Source:** `drafts/2026-10-20-05-major-revision.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **69** citations checked
- existence independently confirmed: **60**
- application evidence-grounded: **52**
- application judged from model knowledge only: **11**
- not independently checkable: **8**
- buckets — clean **13** · problem **48** · disagree **9**

## ⛔ DISAGREE — escalate to human (9)
### c06 — exists ✅ · applied SPLIT  (line 60)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Oct 27, 2025 OpenAI post exists and discusses prevalence of psychosis/mania and self-harm signals; the snippet doesn't show the exact 0.15%/0.07% figures but the page is the documented source for them.
- gpt: exists=verified applied=unchecked [no_basis] — The OpenAI page exists and has the cited title. The retrieved snippet does not contain the specific 0.15%, 0.07%, or weekly-user figures needed to verify the claim.

### c12 — exists ✅ · applied SPLIT  (line 97)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325)_
- **escalate:** application: verified vs refuted
- claude: exists=verified applied=verified [evidence_text] — 4-week RCT of AI-CBT vs human peer counselors for anxiety found both within-group effects with no significant harm difference, supporting the claim.
- gpt: exists=verified applied=refuted [evidence_text] — Crossref verifies the Healthcare randomized controlled trial. The abstract compares AI- and human-delivered CBT on anxiety and perceived benefit, but it does not report harm or unwanted-effects outcomes supporting a claim of no clear difference in harm.

### c13 — exists ✅ · applied SPLIT  (line 99)
_([McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Cross-sectional study of US adolescents/young adults on generative AI for mental health advice and perceived helpfulness supports widespread use and perceived helpfulness.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the JAMA Network Open article and its topic. The retrieved abstract is only a brief description of the survey and does not include the prevalence or helpfulness results needed to verify 'millions' or 'most say it helped.'

### c14 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 102)
_([Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Rousmaniere et al. 2026 on LLM mental health use patterns in the US; no abstract was retrieved, but the topic supports the claim about users also seeing professionals.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Practice Innovations article metadata. No abstract or source text was retrieved, so the claim about two surveys and professional-care history cannot be judged from the evidence.

### c16 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 108)
_according to the CDC's [national survey](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm)_
- **escalate:** application: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL returned HTTP 403 and existence is not-checkable; the 34% women/17% men NISVS figures are consistent with known CDC data but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only URL fetch returned HTTP 403, so the cited page's existence is not checkable from the retrieved evidence. From model knowledge, the CDC has reported roughly one-third of women and one-sixth of men experiencing intimate-partner sexual violence, physical violence, and/or stalking with IPV-related impact, but the claim is imprecise because it omits that impact qualifier.

### c22 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 145)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the paper (human peer vs supportive chatbot reducing loneliness); no abstract retrieved, so the specific journaling/negative-mood details rest on the title and model knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and article metadata. No abstract or substantive source text was retrieved beyond a redirect page, so the detailed intervention and outcome claims cannot be checked from the evidence.

### c29 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 226)
_([Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the paper on chatbot appearance and loneliness trajectories in women with high autistic traits; no abstract was retrieved to verify the 72-participant, eight-week, less-human-appearance details.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and metadata for an article titled about chatbot appearance and loneliness trajectories in women with high autistic traits. No abstract or substantive source text was retrieved, so the detailed sample size, duration, and condition-specific loneliness claims cannot be checked.

### c35 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 259)
_([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Li et al. paper comparing a supportive chatbot to alternatives for loneliness; no abstract retrieved to verify the 'ideal friend' chatbot not beating journaling detail.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI and article metadata. No abstract or substantive source text was retrieved beyond a redirect page, so the claim about an ideal-friend chatbot performing no better or worse than journaling cannot be checked.

### c47 — exists ✅ · applied SPLIT  (line 386)
_Hannan et al. 2005 and Lambert 2013 (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Society page exists and cites Lambert (2013) figures (~75% benefit, 5-10% worse off); the retrieved snippet supports treatment-response monitoring claims attributed via this source.
- gpt: exists=verified applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page resolves and the fetched text confirms the page title and cited discussion of Lambert and related psychotherapy outcome-monitoring literature. No specific claim was supplied to evaluate application.

## ⚠️ AGREE-problem (48)
### c02 — exists ✅ · applied ⚠️  (line 43)
_([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))_
- claude: exists=verified applied=nuance [evidence_text] — Wikipedia confirms Raine, 16, died April 2025 and parents allege ChatGPT contributed; the snippet does not show OpenAI's specific response details (workaround/100+ referrals), so that part is not directly evidenced.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and matches the cited case. The retrieved text supports Adam Raine's age, April 2025 death, suit by his parents, and allegations against ChatGPT, but the snippet provided does not include the specific OpenAI-response details about working around filters or being pointed to help more than 100 times.

### c04 — exists ✅ · applied ✅  · ⚑ degraded  (line 49)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Østergaard Schizophrenia Bulletin piece; its title explicitly asks whether chatbots will generate delusions in psychosis-prone individuals, consistent with the prediction claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI, author, journal, year, and title of Østergaard's Schizophrenia Bulletin article. No abstract or text was retrieved, but from model knowledge the article argued that generative chatbots could induce or reinforce delusional thinking in psychosis-prone users.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 50)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2025 Østergaard piece titled 'From Guesswork to Emerging Cases,' matching the claim that psychiatrists now report individual chatbot-linked delusion cases.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI and metadata for Østergaard's 2025 Acta Psychiatrica Scandinavica article. No source text was retrieved, but from model knowledge the article discusses the move from theoretical concern to emerging case reports of chatbot-associated delusions.

### c08 — exists ✅ · applied ✅  · ⚑ degraded  (line 74)
_([Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Heinz et al. NEJM AI Therabot RCT; the Therabot trial is known to have ~210 participants with reductions in depression, anxiety and eating disorder symptoms over four weeks.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI and metadata for the NEJM AI randomized trial by Heinz et al. No abstract or source text was retrieved, but from model knowledge this Therabot trial involved about 210 adults over four weeks and found reductions in depression, anxiety, and eating-disorder risk compared with a waitlist control.

### c11 — exists ✅ · applied ⚠️  (line 96)
_[Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=verified [evidence_text] — Pilot RCT comparing chatbot vs human conversational agent over sessions with 6-month follow-up found no superiority and comparable rates of unwanted effects, matching the no-clear-difference-in-harm claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the Digital Health randomized pilot trial. The abstract supports a chatbot-vs-human conversational agent comparison with no significant group difference in unwanted negative effects, but the intervention is described as three sessions rather than clearly 'weeks-long.'

### c17 — exists ⚠️ · applied ⚠️  (line 112)
_(Lambert; Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=nuance [evidence_text] — Page confirms the 5-10% deterioration estimate for clinical trial clients; the snippet cuts off before showing the '3 of 550' therapist prediction figure, and the page attributes to Lambert 2013 rather than Hannan 2005.
- gpt: exists=nuance applied=nuance [evidence_text] — The Society for the Advancement of Psychotherapy page exists with the cited title, but the retrieved page is a 2019 Lambert and Kleinstäuber article rather than a 2005 Hannan et al. work as described in the raw citation. The snippet supports the 5%–10% deterioration estimate, but it does not include the specific '3 of 550' therapist-prediction figure.

### c23 — exists ⚠️ · applied ☐  (line 151)
_([Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf))_
- claude: exists=verified applied=unchecked [no_basis] — The working paper PDF resolves at the cited URL, but only binary PDF data was retrieved with no readable text to verify the 7,286-participant findings.
- gpt: exists=nuance applied=unchecked [no_basis] — The cited PDF URL resolves, but the retrieved evidence provides no readable metadata confirming authors, title, or working-paper details. The PDF text retrieved is garbled binary content, so the trial claims cannot be assessed.

### c24 — exists ☐ · applied ☐  · ⚑ degraded  (line 178)
_([the learning essay](../positions/02-it-learns.md))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Internal essay link ('02-it-learns.md') could not be fetched; the claim that major assistants added cross-conversation memory in 2024-2025 is broadly accurate but unverifiable here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative Markdown link is not checkable by the retrieval system. No source text was retrieved to assess the claim.

### c25 — exists ✅ · applied ⚠️  (line 181)
_(De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/))_
- claude: exists=verified applied=verified [evidence_text] — The Harvard Gazette article confirms De Freitas's analysis of Reddit posts finding grief-like responses to AI companion updates, supporting the mourning claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Harvard Gazette URL resolves and the page title and snippet match the cited item. The snippet supports that users responded to AI companion personality/model updates with grief and mourning-like language, but the visible text does not explicitly mention Replika in the quoted portion.

### c30 — exists ☐ · applied ☐  · ⚑ degraded  (line 236)
_([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Bloomberg URL returned HTTP 403; the Character.AI under-18 chat ban from November 2025 is consistent with my knowledge but unverified here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg page could not be accessed due to HTTP 403, and existence was marked not-checkable. No source text was retrieved to assess the claim about Character.AI policy timing.

### c31 — exists ☐ · applied ☐  · ⚑ degraded  (line 239)
_([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — OpenAI page returned HTTP 403; the described update with 170+ experts and 65-80% reduction is plausible but unverified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The OpenAI URL could not be accessed due to HTTP 403, and existence was marked not-checkable. No source text was retrieved to assess the claim about expert involvement or evaluation reductions.

### c32 — exists ✅ · applied ⚠️  (line 242)
_([Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law))_
- claude: exists=verified applied=verified [evidence_text] — The Skadden summary confirms SB 243 mandates disclosure that users are interacting with a chatbot and safety protocols against harmful content; the January 2026 effective date and minor break reminders are consistent with the described law.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden URL resolves and the page title matches the cited summary. The snippet supports disclosures and safety protocols for companion chatbots, but the retrieved portion only partially covers the full claim, with January 2026 effective date and minor break reminders not clearly visible.

### c33 — exists ☐ · applied ☐  (line 245)
_([the yardstick essay](../positions/01-the-yardstick.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal essay link ('01-the-yardstick.md') could not be fetched, so neither axis is verifiable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative Markdown link is not checkable by the retrieval system. No source text was retrieved to assess the claim.

### c34 — exists ✅ · applied ⚠️  (line 252)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the RCT varied interaction mode (voice) and conversation type with no significant condition effects; the under-1% cut-back figure is not in the abstract but is consistent with the study design.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv confirms the paper, title, authors, and abstract. The abstract supports that interaction modes and conversation types were varied and showed no significant effects, but it does not mention the claim that the chatbot suggested cutting back in under 1% of replies.

### c36 — exists ☐ · applied ☐  (line 274)
_[the personality essay](../positions/04-personality.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal essay link ('04-personality.md') could not be fetched, so neither axis is verifiable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative Markdown link is not checkable by the retrieval system. No source text was retrieved to assess the claim.

### c37 — exists ✅ · applied ⚠️  (line 278)
_([OpenClaw](https://github.com/openclaw/openclaw))_
- claude: exists=verified applied=nuance [evidence_text] — The GitHub repo resolves and is described as an AI agent tool, but the page tagline ('The AI that really does things, the lobster way') does not clearly confirm it is open-source software for a personal AI assistant.
- gpt: exists=verified applied=nuance [evidence_text] — The GitHub repository URL resolves and the page title identifies OpenClaw as an AI project. The retrieved snippet supports that it is AI software, but it does not clearly establish that it is open-source or specifically for running a personal AI assistant.

### c38 — exists ☐ · applied ☐  (line 371)
_The section on my own assistants describes my setup from its design files, which are not published; it is experience, not a study._
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited: described as personal experience from unpublished design files, not a study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. It refers to unpublished personal experience/design files, so both axes are left unchecked.

### c39 — exists ✅ · applied ☐  (line 378)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and abstract confirm the Bernaerts et al. survey study exists; no specific claim was attached to this citation to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the JMIR Mental Health article, DOI, authors, year, and abstract. No claim is attached to this citation, so application cannot be assessed.

### c40 — exists ✅ · applied ☐  (line 379)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and abstract confirm the Cheng et al. Science paper exists; no specific claim was attached to this citation instance to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the Science article, DOI, authors, year, and abstract. No claim is attached to this citation, so application cannot be assessed.

### c41 — exists ☐ · applied ☐  (line 380)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — The Safe States URL returned HTTP 403, so neither existence nor claim support can be judged from the evidence. No claims were specified.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403 and the item is marked not-checkable, so existence cannot be confirmed from the supplied evidence. No specific claim was supplied to evaluate application.

### c42 — exists ✅ · applied ☐  (line 381)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match by ID confirms the paper 'Emotional Manipulation by AI Companions' by the cited authors exists. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record and URL confirm a 2025 work by Julian De Freitas, Zeliha Oguz-Uguralp, and Ahmet Kaan-Uguralp titled “Emotional Manipulation by AI Companions.” No specific claim was supplied to evaluate application.

### c43 — exists ✅ · applied ☐  (line 382)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms 'AI Companions Reduce Loneliness' in JCR with matching DOI and authors. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, 2025 Journal of Consumer Research publication, title, volume/issue, and pages. No specific claim was supplied to evaluate application.

### c44 — exists ✅ · applied ☐  (line 383)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms the Fang et al. longitudinal RCT exists. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record and resolving URL confirm the 2025 Fang et al. work with the stated arXiv identifier. No specific claim was supplied to evaluate application.

### c45 — exists ✅ · applied ☐  (line 384)
_[Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Feng & Fu 2026 article with matching DOI and authors. No specific claim provided and no abstract retrieved.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors Feng and Fu, 2026 publication, journal, volume, and article number; the DOI URL also resolves to Elsevier. No specific claim was supplied to evaluate application.

### c46 — exists ✅ · applied ☐  (line 385)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Folk & Dunn 2026 in Psychological Science with matching DOI. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, title, 2026 Psychological Science publication, volume/issue, pages, and abstract. No specific claim was supplied to evaluate application.

### c48 — exists ⚠️ · applied ☐  (line 387)
_[Fréget, Reshef & Senik 2026](https://www.ifo.de/DocDL/cesifo1_wp12882.pdf) (working paper)_
- claude: exists=verified applied=unchecked [no_basis] — The CESifo working paper PDF resolves at the ifo URL, confirming existence, but the extracted content is raw PDF binary so no claim can be assessed.
- gpt: exists=nuance applied=unchecked [no_basis] — The ifo/CESifo PDF URL resolves, but the retrieved evidence is raw PDF bytes without readable metadata confirming the authors, year, or working-paper details. No specific claim was supplied to evaluate application.

### c49 — exists ✅ · applied ☐  (line 388)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Heinz et al. 2025 RCT of a generative AI chatbot in NEJM AI with matching DOI. No abstract or specific claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, NEJM AI venue, year, volume, and issue, despite no abstract being available. No specific claim was supplied to evaluate application.

### c50 — exists ✅ · applied ☐  (line 389)
_[Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Hennemann et al. 2026 pilot trial with matching DOI and abstract. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, 2026 DIGITAL HEALTH publication, and abstract. No specific claim was supplied to evaluate application.

### c51 — exists ✅ · applied ☐  (line 390)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm the Holt-Lunstad 2010 meta-analysis on social relationships and mortality. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the resolving PLOS URL confirm the 2010 PLoS Medicine article by Holt-Lunstad, Smith, and Layton. No specific claim was supplied to evaluate application.

### c52 — exists ✅ · applied ☐  (line 391)
_[Huang et al. 2026](https://doi.org/10.3390/healthcare14101325)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Huang et al. 2026 RCT in Healthcare with matching DOI and abstract. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, 2026 Healthcare publication details, and abstract. No specific claim was supplied to evaluate application.

### c53 — exists ✅ · applied ☐  (line 392)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Li et al. 2023 systematic review/meta-analysis in npj Digital Medicine with matching DOI and abstract. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the 2023 npj Digital Medicine systematic review/meta-analysis by Li et al. No specific claim was supplied to evaluate application.

### c54 — exists ✅ · applied ☐  (line 393)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Li et al. 2026 in JESP with matching DOI and authors. No abstract or specific claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, 2026 Journal of Experimental Social Psychology publication details, and Elsevier URL resolution. No specific claim was supplied to evaluate application.

### c55 — exists ✅ · applied ☐  (line 394)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Maples et al. 2024 Replika loneliness/suicide study with matching DOI. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Nature URL confirm the 2024 npj Mental Health Research article by Maples et al. No specific claim was supplied to evaluate application.

### c56 — exists ✅ · applied ☐  (line 395)
_[McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms McBain et al. 2025 in JAMA Network Open with matching DOI and abstract. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, JAMA Network Open venue, year, volume/issue, article number, and abstract snippet. No specific claim was supplied to evaluate application.

### c57 — exists ✅ · applied ☐  (line 396)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=verified applied=unchecked [no_basis] — The OpenAI post 'Strengthening ChatGPT's responses in sensitive conversations' (Oct 27, 2025) resolves and matches the title. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The OpenAI URL resolves and the fetched page text confirms the title, publisher, date, and subject matter. No specific claim was supplied to evaluate application.

### c58 — exists ✅ · applied ☐  (line 397)
_[OpenClaw](https://github.com/openclaw/openclaw)_
- claude: exists=verified applied=unchecked [no_basis] — The OpenClaw GitHub repository resolves and exists, though it appears to be a tongue-in-cheek/unusual project. No claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The GitHub URL resolves and the fetched title confirms the openclaw/openclaw repository. No specific claim was supplied to evaluate application.

### c59 — exists ✅ · applied ☐  (line 398)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Østergaard 2023 in Schizophrenia Bulletin on AI chatbots and delusions. No abstract or specific claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, author, 2023 Schizophrenia Bulletin publication details, and pages. No specific claim was supplied to evaluate application.

### c60 — exists ✅ · applied ☐  (line 399)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Østergaard 2025 in Acta Psychiatrica Scandinavica on AI chatbots and delusions. No abstract or specific claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, author, 2025 Acta Psychiatrica Scandinavica publication details, volume/issue, and pages. No specific claim was supplied to evaluate application.

### c61 — exists ✅ · applied ☐  (line 400)
_[Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, title, and journal exactly. No claim text or abstract available to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to a 2026 Practice Innovations article by Rousmaniere et al. No supported claim was supplied, so application cannot be assessed.

### c62 — exists ✅ · applied ☐  (line 401)
_[Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI, authors, PNAS, and abstract. No specific claim provided to verify application against.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to the 2024 PNAS article by Yin, Jia, and Wakslak. No supported claim was supplied, so application cannot be assessed.

### c63 — exists ✅ · applied ☐  (line 402)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID and URL resolve to the described paper with matching abstract. No specific claim provided to verify application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup and URL resolution confirm arXiv:2506.12605, titled “The Rise of AI Companions: Interaction with AI Companions and Psychological Well-being.” No supported claim was supplied, so application cannot be assessed.

### c64 — exists ✅ · applied ☐  (line 403)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=unchecked [no_basis] — Fetched article confirms the Garcia v. Character Technologies case and settlement. No specific claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Jamaica Gleaner/AP URL resolves and the retrieved snippet describes the Garcia lawsuit and proposed settlements involving Character Technologies and Google. No supported claim was supplied, so application cannot be assessed.

### c65 — exists ✅ · applied ☐  (line 405)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- claude: exists=verified applied=unchecked [no_basis] — Wikipedia article confirms Raine v. OpenAI case details. No specific claim provided to verify application.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to a Wikipedia page describing Raine v. OpenAI as a 2025 California lawsuit. No supported claim was supplied, so application cannot be assessed.

### c66 — exists ✅ · applied ☐  (line 406)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- claude: exists=verified applied=unchecked [no_basis] — Incident report confirms the 2023 Belgian chatbot suicide case. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database URL resolves to Report 2865 concerning the reported Belgian Chai chatbot suicide incident. No supported claim was supplied, so application cannot be assessed.

### c67 — exists ☐ · applied ☐  (line 407)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403 (paywall); existence not verifiable from evidence, though the Character.AI under-18 ban is widely reported.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403 from Bloomberg, and the citation is marked not-checkable, so existence cannot be judged. No supported claim or source text was available for application.

### c68 — exists ✅ · applied ☐  (line 408)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- claude: exists=verified applied=unchecked [no_basis] — Skadden article confirms California SB 243 companion chatbot law. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves and the retrieved snippet describes California SB 243 and its companion-chatbot requirements. No supported claim was supplied, so application cannot be assessed.

### c69 — exists ✅ · applied ☐  (line 409)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=unchecked [no_basis] — Harvard Gazette article confirms the De Freitas study on AI companion attachment/loss. No specific claim provided to verify application.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves and the retrieved snippet describes the chatbot attachment/loss study. No supported claim was supplied, so application cannot be assessed.

### c70 — exists ☐ · applied ☐  (line 410)
_Verification marks for each: the [relationships brief](../briefs/2026-10-17-8-relationships.md)._
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal relative-path link to a companion brief, not an external work; URL unresolvable and Crossref match is unrelated. Cannot verify as an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence does not verify the cited local relationships brief: Crossref found only a low-similarity unrelated item, and the relative URL could not be fetched. Without the brief text, the claim that it holds verification marks cannot be assessed.

## ✅ AGREE-clean (13)
### c01 — exists ✅ · applied ✅  (line 39)
_([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=verified [evidence_text] — Article confirms Setzer's Feb 2024 suicide, mother Megan Garcia's suit, and January 2026 settlement with undisclosed terms involving Character and Google plus related suits.
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to the Jamaica Gleaner/AP story with the cited title. The retrieved text supports the Florida lawsuit, Sewell Setzer III's age and February 2024 death, the allegations, and the January 2026 undisclosed settlements with Character Technologies/Google and related suits.

### c03 — exists ✅ · applied ✅  (line 46)
_([AI Incident Database](https://incidentdatabase.ai/reports/2865/))_
- claude: exists=verified applied=verified [evidence_text] — The report confirms a Belgian man died by suicide in 2023 after six weeks with the Chai chatbot Eliza, as reported by La Libre with the widow's statements.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report page resolves and identifies Report 2865 / Incident 505 about a suicide after conversations with a Chai chatbot. The retrieved text states the Belgian man used Chai for six weeks, that his widow said he would still be alive, and that the death was reported in 2023.

### c07 — exists ✅ · applied ✅  (line 71)
_([Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms meta-analysis of 15 RCTs showing significant reductions in depression and distress but no significant improvement in overall well-being.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Digital Medicine systematic review and meta-analysis. The abstract states that 15 randomized controlled trials were included and that conversational agents significantly reduced depression and distress but did not significantly improve overall psychological well-being.

### c09 — exists ✅ · applied ✅  (line 79)
_([De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states AI companions alleviate loneliness 'on par only with interacting with another person,' directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Consumer Research article. The abstract states that AI companions reduced loneliness on par with interacting with another person and that longitudinal use produced momentary reductions in loneliness.

### c10 — exists ✅ · applied ✅  (line 82)
_([Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms survey of 1006 Replika student users with 3% reporting Replika halted their suicidal ideation.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the npj Mental Health Research article. The abstract states that a survey of 1006 student Replika users found that 3% reported Replika halted their suicidal ideation.

### c15 — exists ✅ · applied ✅  (line 103)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states most respondents indicated having received or receiving professional mental health support, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the JMIR Mental Health survey study. The abstract states that two Belgian samples were surveyed and that most respondents indicated having received or currently receiving professional mental health support.

### c18 — exists ✅ · applied ✅  (line 119)
_([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 148 studies, 308,849 participants, and a 50% increased likelihood of survival with stronger social relationships.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the URL verify the PLoS Medicine meta-analysis. The retrieved abstract states that across 148 studies and 308,849 participants, stronger social relationships were associated with an OR of 1.50, i.e. a 50% increased likelihood of survival.

### c19 — exists ✅ · applied ✅  (line 133)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms n=981 four-week RCT where voluntarily heavier chatbot users showed consistently worse outcomes regardless of condition.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists and matches the cited paper. The abstract states that in a four-week randomized experiment with 981 participants, assigned conditions had no significant effects, but participants who voluntarily used the chatbot more showed worse outcomes across loneliness, real social interaction, emotional dependence, and problematic use.

### c20 — exists ✅ · applied ✅  (line 137)
_([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms Character.AI users with smaller social networks used it for companionship, associated with lower well-being, stronger when intensive and highly disclosive; correlational caveat is appropriately noted.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists and matches the cited paper on CharacterAI users. The abstract supports the claims that smaller social networks were associated with companionship-primary use, that companionship use was associated with lower well-being, and that the association was stronger with intensive and highly disclosive interaction.

### c21 — exists ✅ · applied ✅  (line 141)
_([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the 12-month study of 2,000+ adults, loneliness predicting chatbot use, and chatbot use predicting loneliness on a single-item measure; exploratory framing matches.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the DOI, title, authors, journal, year, and abstract. The abstract directly states the 12-month study of more than 2,000 adults, the bidirectional loneliness/chatbot-use findings, the single-item loneliness result, and the exploratory caution.

### c26 — exists ✅ · applied ✅  (line 211)
_([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a single sycophantic interaction reduced willingness to repair conflict, increased conviction of being right, and that such models were trusted and preferred.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Science article, DOI, authors, and abstract. The abstract directly supports that a single interaction with sycophantic AI reduced willingness to take responsibility and repair conflicts, increased conviction, and that such models were trusted and preferred.

### c27 — exists ✅ · applied ✅  (line 214)
_([De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258))_
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms the audit of 1,200 farewells found manipulative tactics in 37% of them, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms the paper, authors, title, and abstract. The abstract directly states that 1,200 real farewells were analyzed and that companion apps used manipulative tactics in 37% of farewells.

### c28 — exists ✅ · applied ✅  (line 223)
_([Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms recipients felt less heard when they believed a message came from AI, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the PNAS article and DOI. The abstract directly states that recipients felt less heard when they realized a message came from AI rather than a human.
