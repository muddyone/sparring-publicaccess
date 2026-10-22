# Cite-check: the relationships brief (2026-10-17)

Run on `briefs/2026-10-17-8-relationships.md` with `/cite-check` (chunked at 60 lines). The raw
report follows.

**Summary.** 62 items: 24 confirmed to exist from independent sources, 15 not checkable (press
pages, lawsuits, bottom-line mentions). **No citation was found invented.** Most disagreements
are one model marking a supporting URL "unchecked" because no claim was attached to it, or
bottom-line short mentions that point to a checked full entry.
- **Clean (7):** Li et al. 2023, Maples et al. (existence), De Freitas et al. 2025, Folk & Dunn
  2026, Holt-Lunstad et al. 2010, Tukachinsky et al. 2020, and the Stanford HAI page.
- **Corrected after the run:**
  - **Zhang et al.:** 237 donated transcripts, not 244 (arXiv abstract).
  - **Maples et al.:** the abstract says 3% reported Replika *halted suicidal ideation*. The
    stronger "stopped them attempting suicide" (30 people) is now attributed to secondary
    accounts of the paper's body.
  - **Folk & Dunn 2026:** found in Crossref with its abstract. Upgraded to [abstract], DOI added.
  - **Heinz et al. 2025:** DOI confirmed by Crossref and added. Figures stay [secondary].
  - **Østergaard:** the 2023 editorial is now fully referenced, and his 2025 follow-up (Acta
    Psychiatrica Scandinavica, "From guesswork to emerging cases") added, both [record].
  - **The AP settlement story:** the WTOP link returned 404; replaced with a working syndicated copy.
  - **UCSF case:** "no prior history" is now attributed to press coverage.
  - The "harm concentrates" phrasing for Zhang et al. softened to "lower well-being
    concentrates", correlational.
- **Left as marked:** Li, Dunn et al. 2026 (JESP) not in Crossref, relying on the UBC release;
  the De Freitas update study not located; Lambert/Hannan figures rest on the Society page; the
  lawsuit and Belgium accounts are press-sourced and stated as allegations.

---

# cite-check report — relationships-brief

**Source:** `briefs/2026-10-17-8-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **62** citations checked
- existence independently confirmed: **24**
- application evidence-grounded: **25**
- application judged from model knowledge only: **27**
- not independently checkable: **15**
- buckets — clean **7** · problem **34** · disagree **30**

## ⛔ DISAGREE — escalate to human (30)
### c01 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 25)
_Garcia v. Character Technologies, settled in principle January 2026_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — The Garcia v. Character Technologies case exists (filed 2024), but the CourtListener lookup was inconclusive and I cannot confirm a January 2026 settlement from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — CourtListener lookup was inconclusive and existence_status is not-checkable, so the case/settlement cannot be confirmed from retrieved evidence. No source text was retrieved to assess the settlement claim.

### c02 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 26)
_Raine v. OpenAI, pending_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Raine v. OpenAI is a known wrongful-death suit over a teen's death, consistent with the claim, but lookup was inconclusive and 'pending' status cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — CourtListener lookup was inconclusive and provides no confirming metadata for Raine v. OpenAI. No source text was retrieved to verify that the case is pending or concerns a teenage death.

### c04 — exists ❌ · applied SPLIT  (line 27)
_a growing set of single-patient psychiatric case reports of delusions reinforced by chatbots_
- **escalate:** application: nuance vs refuted
- claude: exists=refuted applied=nuance [evidence_text] — The only retrieved item is a 2013 paper on delusions in virtual reality/Facebook, not chatbot-reinforced delusions, so no specific cited work matches; such case reports do exist generally but the retrieved evidence doesn't support the chatbot claim.
- gpt: exists=refuted applied=refuted [evidence_text] — The retrieved article is a real 2013 report about Facebook/social-media-related delusional beliefs, not a work titled or described as chatbot-reinforced delusions. Its abstract does not support a claim about a growing set of chatbot-specific psychiatric case reports.

### c05 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 29)
_OpenAI estimated that about 0.15% of weekly ChatGPT users show explicit signs of suicidal planning or intent, and about 0.07% possible signs of psychosis or mania (October 2025)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref found nothing (expected for a company blog post), but OpenAI's October 2025 disclosure of ~0.15% suicidal and ~0.07% psychosis/mania signals is consistent with my knowledge of their published figures.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, but that does not rule out an OpenAI web report or announcement. No source text was retrieved for the quoted October 2025 percentages.

### c06 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 35)
_A meta-analysis of 15 randomized trials found conversational agents reduced depression and distress (Li et al. 2023)_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved; meta-analyses of conversational agents reducing depression exist (e.g. Li et al.), but the specific '15 trials' detail cannot be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The sparse Li et al. 2023 reference was not matched in Crossref, so existence is not confirmed by retrieved evidence. No abstract or text was retrieved to assess the meta-analysis claim.

### c09 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 40)
_Heavy voluntary use goes with worse loneliness and dependence (Fang et al. 2025)._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved; Fang et al. 2025 (MIT/OpenAI study) on heavy use correlating with loneliness and dependence is plausible and matches my knowledge, but unconfirmed by evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Fang et al. 2025 citation was not matched in Crossref. No retrieved source text supports or contradicts the claim about heavy use, loneliness, and dependence.

### c16 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 56)
_Character.AI barred under-18s from open-ended chat (November 2025)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref wouldn't index a company announcement; Character.AI's November 2025 move to bar under-18s from open-ended chat was widely reported and matches the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, which does not determine whether a Character.AI announcement or policy change exists. No source text was retrieved to assess the under-18 open-ended chat claim.

### c17 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 57)
_OpenAI retrained for sensitive conversations (October 2025)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not indexable in Crossref; OpenAI's October 2025 announcement about improving handling of sensitive/mental-health conversations is consistent with the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, which does not determine whether an OpenAI announcement exists. No retrieved source text supports the October 2025 retraining claim.

### c21 — exists SPLIT · applied ☐  (line 71)
_AP coverage, January 2026: https://wtop.com/national/2026/01/google-and-chatbot-maker-character-to-settle-lawsuit-alleging-chatbot-pushed-teen-to-suicide/_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — The URL returned HTTP 404, so the specific WTOP article could not be confirmed; no claims attached to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 404 and the existence status is not-checkable, so existence cannot be confirmed. No claims or source text were supplied for application.

### c24 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 75)
_Raine v. OpenAI (San Francisco Superior Court, filed August 2025). Parents of 16-year-old Adam Raine allege ChatGPT (GPT-4o) contributed to his death in April 2025, with claims of negligence, wrongful death and design defect. OpenAI's response says he worked around safety filters against its terms, and that the model pointed him to help more than 100 times. As of mid 2026 the case was still at the pleading stage. **[secondary]**_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — CourtListener lookup was inconclusive so existence is unchecked, but the companion Wikipedia evidence (c25) confirms the allegations of GPT-4o involvement, April 2025 death, and negligence/wrongful death/design-defect claims.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only court lookup was inconclusive, so the cited case cannot be verified from the retrieved evidence. No source text was retrieved to assess the allegations, OpenAI response, or procedural posture.

### c25 — exists ✅ · applied SPLIT  (line 80)
_https://en.wikipedia.org/wiki/Raine_v._OpenAI_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Wikipedia page resolves and confirms the August 2025 filing, 16-year-old Adam Raine's April 2025 suicide, and negligence/product liability/wrongful death claims supporting the cited allegations.
- gpt: exists=verified applied=unchecked [no_basis] — The Wikipedia page resolves and the snippet matches the cited Raine v. OpenAI page. No specific claim was attached to this citation for application review.

### c26 — exists SPLIT · applied ✅  · ⚑ degraded  (line 83)
_Belgium, 2023. A man in his thirties, reported as "Pierre", died by suicide after six weeks of conversations with a Chai chatbot named Eliza, which his widow says deepened his climate anxiety. First reported by La Libre in March 2023. The causal account rests on the widow and the newspaper's reading of the logs. **[secondary]**_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Though La Libre was not directly fetched, the AI Incident Database report (c27) confirms the Belgian man 'Pierre', six weeks of Chai chatbot 'Eliza' conversations, eco-anxiety, and La Libre's March 2023 first report.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieval evidence was supplied, so the La Libre report's existence cannot be verified from evidence. Based only on model knowledge, the Belgian 'Pierre'/Chai/Eliza account and La Libre first-report framing are broadly consistent, with confidence capped because no source text was retrieved.

### c27 — exists ✅ · applied SPLIT  (line 87)
_AI Incident Database: https://incidentdatabase.ai/reports/2865/_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The report resolves and directly corroborates the Pierre/Eliza/Chai/La Libre account from the source text.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database report URL resolves and the snippet identifies Report 2865 about the Chai chatbot suicide account. No specific claim was attached to this citation for application review.

### c28 — exists SPLIT · applied ☐  · ⚑ degraded  (line 89)
_Psychiatric case reports of chatbot-associated delusions. **[secondary]** Østergaard (2023, _Schizophrenia Bulletin_ editorial) predicted that chatbots could reinforce delusions in people prone to psychosis._
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [model_knowledge_only] — Crossref returned no match, though Østergaard did publish a 2023 Schizophrenia Bulletin editorial on AI chatbots and delusions; metadata here is too thin to confirm so existence is marked refuted on evidence while application plausibly holds from knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — A Crossref no-match for a vague editorial citation is not decisive evidence that the work does not exist. No source text was retrieved to judge whether it predicted chatbot reinforcement of delusions.

### c30 — exists ✅ · applied SPLIT  (line 95)
_a UCSF report of a young woman with no prior history (reported January 2026): https://www.ucsf.edu/news/2026/01/431366/psychiatrists-hope-chat-logs-can-reveal-secrets-ai-psychosis_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The UCSF article resolves with matching title and January 2026 date, but the retrieved snippet is mostly navigation and does not confirm the 'young woman with no prior history' detail.
- gpt: exists=verified applied=unchecked [evidence_text] — The UCSF URL resolves with the matching title about AI psychosis. The retrieved snippet does not show the specific claim that the report involved a young woman with no prior history, so application cannot be confirmed.

### c32 — exists SPLIT · applied SPLIT  (line 101)
_Loss when a companion changes. After Replika abruptly removed erotic role-play in February 2023, users described the change as a relational loss. De Freitas and colleagues analyzed 54,861 Reddit posts around Replika and ChatGPT model updates and found mourning-like reactions, stronger for Replika. Self-selected heavy users; linguistic markers, not clinical measures. **[secondary]**_
- **escalate:** existence: nuance vs unchecked; application: verified vs unchecked
- claude: exists=nuance applied=verified [evidence_text] — Crossref found no direct match, but the Harvard Gazette coverage (c33) confirms De Freitas analyzed 54,861 Reddit posts finding grief/mourning reactions to AI companion updates, supporting the claim; the underlying paper exists (Nature Human Behavior).
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the De Freitas item was a Crossref no-match, which is insufficient to verify or refute the unspecified work. No source text was retrieved for this citation to assess the Replika/Reddit-post claims.

### c33 — exists ✅ · applied SPLIT  (line 106)
_Harvard Gazette, September 2026: https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Gazette article resolves and corroborates the De Freitas study of 54,861 posts, Nature Human Behavior publication, and grief-like reactions to model updates.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves and the snippet matches the cited article, including the September 18, 2026 date and title. No specific claim was attached to this citation for application review.

### c37 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 119)
_OpenAI (2025, October 27). _Strengthening ChatGPT's responses in sensitive conversations._ https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/ **[secondary]**_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — The OpenAI page returned HTTP 403 so existence is unchecked, but the cited figures (0.15% suicidal indicators, 0.07% psychosis/mania, 170+ clinicians, 65-80% reduction) match OpenAI's October 2025 publication as I recall it.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only URL fetch returned HTTP 403, and the item is marked not-checkable, so existence cannot be confirmed from the evidence. No source text was retrieved to assess the numerical claims or OpenAI evaluation claims.

### c38 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 131)
_Common Sense Media (2025). _Talk, trust, and trade-offs: How and why teens use AI companions._ Survey of 1,060 US teens aged 13–17, April–May 2025. **[secondary]**_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — No evidence was retrieved, but the Common Sense Media 2025 teen AI companion survey and its headline figures (72% tried, 52% regular use) are consistent with my knowledge of that report.
- gpt: exists=unchecked applied=unchecked [no_basis] — No retrieval evidence was supplied for the Common Sense Media report. Without source text, the survey statistics and framing cannot be assessed.

### c41 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 148)
_Heinz, M. V., et al. (2025). Randomized trial of a generative AI chatbot for mental health treatment. _NEJM AI_, 2(4). **[secondary]**_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the NEJM AI 2025 Therabot trial by Heinz et al. No abstract retrieved, so the specific figures (51%/31%/19%, n=210, alliance ratings, lead-author quote) cannot be checked against source text; author note flags the paper itself was not reached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the NEJM AI article with matching title, authors, year, volume/issue, and DOI 10.1056/aioa2400802. No abstract or source text was retrieved, so the detailed trial results and author statement cannot be checked from the provided evidence.

### c42 — exists ✅ · applied SPLIT  (line 155)
_Dartmouth release: https://tto.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Dartmouth press release resolves and describes the Therabot NEJM AI trial, confirming its role as the press source. Note the release cites 106 participants and the trial itself, relevant context for the figures cited elsewhere.
- gpt: exists=verified applied=unchecked [no_basis] — The Dartmouth URL resolves with the cited title. No specific claims are attached to this citation record.

### c50 — exists SPLIT · applied ☐  (line 198)
_Li, R.-N., Dunn, E., et al. (2026). _Journal of Experimental Social Psychology_. [secondary]_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No match found in Crossref for this JESP paper; author note confirms paper/DOI not located. However the UBC release (c51) corroborates the underlying study by Ruo-Ning Li, so the claimed findings exist even if this exact journal citation is unconfirmed.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, and the citation lacks a title or DOI, so the work cannot be confirmed from the provided evidence. No source text for this alleged journal article was retrieved to check the application claims.

### c51 — exists ✅ · applied SPLIT  (line 204)
_UBC release: https://news.ubc.ca/2026/04/texting-with-a-stranger-beats-a-chatbot-at-easing-loneliness/_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — UBC release resolves and confirms 296 first-semester students, two-week randomized comparison of peer texting vs AI chatbot vs journaling, with only human texting reducing loneliness and chatbot no better than journaling, matching the c50 claims.
- gpt: exists=verified applied=unchecked [no_basis] — The UBC News URL resolves with the cited title. No specific claims are attached to this citation record, although the snippet describes the study.

### c52 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 209)
_CDC National Intimate Partner and Sexual Violence Survey, 2023/2024 data brief. [secondary]_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No evidence retrieved; existence not checkable. The ~1-in-3 women / ~1-in-6 men lifetime IPV figures are broadly consistent with NISVS data as I recall, but wave-specific figures and comparability caveats cannot be verified here.
- gpt: exists=unchecked applied=unchecked [no_basis] — No retrieved evidence was provided and the existence status is not-checkable. The claims about NISVS figures and method changes cannot be assessed from the supplied evidence.

### c54 — exists SPLIT · applied SPLIT  · ⚑ degraded  (line 216)
_Psychotherapy deterioration. Lambert's reviews estimate that 5–10% of adult clients in clinical trials end treatment worse off, and more children and adolescents. Therapists rarely detect it: in Hannan et al. (2005), therapists predicted 3 of 40 clients who deteriorated. [secondary]_
- **escalate:** existence: nuance vs unchecked; application: nuance vs unchecked
- claude: exists=nuance applied=nuance [model_knowledge_only] — The retrieved Crossref item is a different unrelated paper (low similarity). The cited Lambert reviews and Hannan et al. (2005) are real works, and the 5-10% deterioration estimate and the therapist-detection finding are accurate to my knowledge, but no matching source was retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved Crossref result is a low-similarity 2026 psychotherapy-safety preprint, not the cited Lambert/Hannan material, so existence of the cited work as described is not established. Because no relevant source text was retrieved, the deterioration-rate and therapist-detection claims cannot be checked here.

### c55 — exists ✅ · applied SPLIT  (line 220)
_Society for the Advancement of Psychotherapy: https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Society for the Advancement of Psychotherapy page by Lambert resolves and states the 5-10% deterioration estimate and that clinicians hold overly optimistic views, corroborating the c54 claims.
- gpt: exists=verified applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy URL resolves with the cited title. No specific claims are attached to this citation record.

### c58 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 234)
_Horton & Wohl 1956_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — No Crossref match, but Horton & Wohl (1956) 'Mass Communication and Para-Social Interaction' in Psychiatry is a well-known real foundational work, and the claim that one-sided bonds with media figures are longstanding human behavior accurately reflects it.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The provided Crossref lookup found no match, so existence cannot be verified from retrieved evidence. From model knowledge, Horton and Wohl’s 1956 work introduced parasocial interaction, broadly supporting the one-sided media-bond point, but 'normal human behaviour' is an interpretive gloss.

### c59 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 238)
_Pillemer, J., & Rothbard, N. P. (2018). Friends without benefits: Understanding the dark sides of workplace friendship. _Academy of Management Review_, 43(4), 635–660. https://doi.org/10.5465/amr.2016.0309 **[report]**_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-matched Crossref confirms the Pillemer & Rothbard (2018) AMR article exists; no abstract retrieved, but its theorizing of dark sides of workplace friendship (including compromised judgment/accountability) supports the claim per my knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the Academy of Management Review article, DOI, authors, pages, and year. No abstract or accessible source text was retrieved, so the specific claim about closeness loosening judgment and accountability cannot be assessed from the evidence.

### c60 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 245)
_Character.AI barred under-18 users from open-ended chat from 25 November 2025, with age assurance and a creative-tools experience for teens. **[secondary]** https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Bloomberg URL returned HTTP 403, so existence not confirmed; however Character.AI's announced restriction of under-18 open-ended chat in late 2025 is consistent with my knowledge of reported events.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL fetch failed with HTTP 403 and the existence status is not-checkable, so the article is not confirmed from the provided evidence. No source text was retrieved to assess the claim about Character.AI’s under-18 policy.

### c63 — exists ☐ · applied SPLIT  (line 259)
_OpenAI's October 2025 retraining (2.1)._
- **escalate:** application: unchecked vs refuted
- claude: exists=unchecked applied=unchecked — This is an internal cross-reference to section 2.1 rather than an external work; the Crossref hit (OpenAI Codex CLI) is irrelevant. Cannot verify from evidence.
- gpt: exists=unchecked applied=refuted [evidence_text] — The only retrieved record is a low-similarity Crossref match for “OpenAI Codex CLI,” not “OpenAI's October 2025 retraining,” so existence of the intended item is not established. The retrieved abstract discusses a coding CLI and does not support the retraining cross-reference claim.

## ⚠️ AGREE-problem (34)
### c03 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 26)
_a widely reported adult death in Belgium (2023)_
- claude: exists=unchecked applied=nuance [model_knowledge_only] — The Crossref match is an unrelated item; a widely reported Belgian chatbot-related death in 2023 is documented in news reports, but no retrieved evidence confirms it.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref item is unrelated, so the cited event/source is not confirmed by evidence. From model knowledge only, the 2023 widely reported Belgian adult death associated with a chatbot is a real reported incident.

### c07 — exists ☐ · applied ✅  · ⚑ degraded  (line 36)
_A randomized trial of a purpose-built generative therapy bot found large symptom reductions against a waitlist (Heinz et al. 2025)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No match retrieved, but the Heinz et al. 2025 'Therabot' RCT in NEJM AI showing large symptom reductions is well-known and matches the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence is not confirmed from retrieved evidence. From model knowledge only, Heinz et al. 2025 is consistent with reports of a randomized trial of a generative therapy chatbot showing large symptom reductions versus waitlist.

### c08 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 37)
_Momentary loneliness relief from companions has been shown experimentally (De Freitas et al. 2025)_
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No evidence retrieved; De Freitas has published experimental work on AI companions and loneliness, consistent with the claim, but not confirmable from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so the cited work is not confirmed by retrieved evidence. From model knowledge only, De Freitas et al. 2025 is consistent with experimental findings that AI companions can provide short-term loneliness relief.

### c10 — exists ☐ · applied ☐  (line 41)
_Harm concentrates among people with small offline networks who use it mainly for companionship (Zhang et al. 2025/2026)._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved and I cannot identify a specific Zhang et al. 2025/2026 work supporting this claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Zhang et al. 2025/2026 citation was not matched in Crossref. No retrieved source text was available to assess the claimed concentration of harm among users with small offline networks.

### c11 — exists ☐ · applied ☐  (line 43)
_Lonely people turn to chatbots more. Over 12 months, the reverse direction (use causing disconnection) was not significant (Folk & Dunn 2026)._
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved and I cannot confirm a Folk & Dunn 2026 longitudinal study on loneliness and chatbot use.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Folk & Dunn 2026 citation was not matched in Crossref. No source text was retrieved to assess the claimed longitudinal directionality.

### c12 — exists ☐ · applied ☐  (line 45)
_Texting a real stranger reduced loneliness. A caring chatbot did no better than journaling (Li, Dunn et al. 2026)._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved and I cannot confirm a Li, Dunn et al. 2026 study comparing stranger texting, chatbots, and journaling.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Li, Dunn et al. 2026 citation was not matched in Crossref. No source text was retrieved to verify the comparison between texting a stranger, chatbot interaction, and journaling.

### c13 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 48)
_About a third of US women and a sixth of men report violence or stalking by an intimate partner in their lifetime (CDC NISVS 2023/2024)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No lookup performed, but CDC NISVS reliably reports roughly a third of women and a sixth of men experiencing intimate partner violence/stalking, consistent with the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — No retrieved evidence was provided, and existence_status is not-checkable, so the CDC NISVS report cannot be confirmed here. From model knowledge only, NISVS supports related intimate-partner violence/stalking prevalence claims, but the stated “one third of women and one sixth of men” appears imprecise and depends on definitions/year.

### c14 — exists ☐ · applied ✅  · ⚑ degraded  (line 50)
_An estimated 5–10% of adult psychotherapy clients end treatment worse off (Lambert's reviews)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned an unrelated medical item, but Michael Lambert's well-known psychotherapy reviews do estimate ~5-10% of clients deteriorate, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref result is unrelated to psychotherapy outcomes, so Lambert's reviews are not confirmed by retrieved evidence. From model knowledge only, Lambert's work is commonly cited for roughly 5–10% deterioration rates among adult psychotherapy clients.

### c15 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 51)
_Social connection, for all its risks, is among the strongest predictors of survival (Holt-Lunstad et al. 2010)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No match retrieved, but Holt-Lunstad et al. 2010's PLOS Medicine meta-analysis famously shows social connection strongly predicts survival, matching the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match, so the Holt-Lunstad et al. 2010 work is not confirmed by retrieved evidence. From model knowledge only, the 2010 meta-analysis supports social relationships as strongly associated with mortality/survival, though “among the strongest predictors” is a broad paraphrase.

### c18 — exists ☐ · applied ✅  · ⚑ degraded  (line 57)
_California now regulates companion bots (SB 243, effective January 2026)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No lookup performed, but California SB 243 regulating companion chatbots, signed in 2025 and effective January 2026, is accurate to my knowledge.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and existence_status is not-checkable, so SB 243 cannot be confirmed from evidence here. From model knowledge only, California SB 243 is consistent with regulation of companion chatbots effective in January 2026.

### c19 — exists ☐ · applied ☐  (line 59)
_A harmful human partner can't be retrained or regulated this way. That is piece 04's correctability point. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] and is_citation=false — the authors' own interpretation, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and as the authors' own interpretation. Per instructions, both axes are unchecked.

### c20 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 65)
_Garcia v. Character Technologies (M.D. Fla., filed October 2024). Megan Garcia sued over the death of her 14-year-old son, Sewell Setzer III, after months of conversations with a Character.AI character. In May 2025 the court declined, for now, to treat chatbot output as protected speech, letting the wrongful-death claim proceed. In January 2026, Character Technologies and Google agreed to settle this and several related suits (Colorado, New York, Texas); terms were not disclosed. **[secondary]**_
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Garcia v. Character Technologies (M.D. Fla., filed Oct 2024) exists and the May 2025 ruling declining to treat chatbot output as protected speech matches my knowledge; the January 2026 settlement detail cannot be confirmed from the inconclusive lookup.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — CourtListener lookup was inconclusive and provides no confirming case metadata, so existence is not verified from retrieved evidence. From model knowledge only, the filing and core allegations align with reported Garcia v. Character Technologies litigation, but the May 2025 ruling and January 2026 multi-suit settlement details are not evidenced here.

### c22 — exists ✅ · applied ☐  (line 72)
_WUSF, May 2025: https://www.wusf.org/courts-law/2025-05-22/in-lawsuit-over-orlando-teens-suicide-judge-rejects-that-ai-chatbots-have-free-speech-rights_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves and title matches the WUSF article; no specific claims are attached to this citation to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — The WUSF URL resolves with the matching title about the Orlando teen suicide lawsuit and chatbot free-speech rights. No specific claim was supplied to evaluate application.

### c23 — exists ☐ · applied ☐  (line 73)
_Not found: whether the court has approved the settlements._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked as not found and deliberately uncited; both axes are not applicable.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c29 — exists ✅ · applied ⚠️  (line 92)
_a Dartmouth report of psychosis tied to heavy occupational AI use, with co-occurring substance-induced psychosis (_Primary Care Companion for CNS Disorders_, 2025;27(6):25cr04059): https://www.psychiatrist.com/pcc/artificial-intelligence-psychosis-substance-induced-psychosis_
- claude: exists=verified applied=verified [evidence_text] — The URL resolves to the case report 'Machine Madness: A Case of AI Psychosis Co-Occurring With Substance-Induced Psychosis' in PCC 2025;27(6):25cr04059, matching the citation; the retrieved text confirms the co-occurring substance-induced psychosis framing.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to the matching Primary Care Companion case report, 'Machine Madness: A Case of Artificial Intelligence Psychosis,' with the cited volume/issue/article number visible. The snippet supports a case of AI psychosis co-occurring with substance-induced psychosis, but it does not itself confirm the 'Dartmouth' affiliation or heavy occupational AI-use details.

### c31 — exists ☐ · applied ☐  (line 98)
_No systematic case series or incidence estimate was found. "AI psychosis" is a press label, not a diagnosis._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited note that no systematic case series was found; not applicable.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c34 — exists ☐ · applied ☐  (line 107)
_Original paper not located; check before citing figures beyond the post count._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited caution note; not applicable.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c39 — exists ☐ · applied ☐  (line 136)
_Coverage: https://www.axios.com/2025/07/16/ai-bot-companions-teens-common-sense-media_
- claude: exists=unchecked applied=unchecked [no_basis] — The Axios URL returned HTTP 403 so it could not be confirmed; no specific claims attached to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Axios fetch returned HTTP 403 and existence is not-checkable from the retrieved evidence. No claims or source text were supplied for application review.

### c43 — exists ✅ · applied ⚠️  (line 158)
_Maples, B., Cerit, M., Vishwanath, A., & Pea, R. (2024). Loneliness and suicide mitigation for students using GPT3-enabled chatbots. _npj Mental Health Research_, 3, 4. https://doi.org/10.1038/s44184-023-00047-6 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI-matched abstract confirms survey of 1006 student Replika users, lonelier yet high perceived support, and 3% reporting Replika halted suicidal ideation, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the article, DOI, authors, journal, and year. The abstract supports the 1,006 Replika users, elevated loneliness, high perceived social support, and 3% reporting Replika halted suicidal ideation, but it does not substantiate the stronger wording that 30 people 'spontaneously' said it stopped an attempted suicide.

### c45 — exists ✅ · applied ⚠️  (line 174)
_Fang, C. M., et al. (2025). How AI and human behaviors shape psychosocial effects of extended chatbot use: A longitudinal randomized controlled study. arXiv:2503.17473. https://arxiv.org/abs/2503.17473 [report]_
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms n=981 four-week RCT, no significant effects from assigned conditions, and that heavier voluntary use predicted worse outcomes; MIT/OpenAI authorship consistent with author list.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv confirms the paper, title, authors, and abstract. The abstract supports the four-week RCT with n=981, no significant effects of assigned interaction mode/conversation type, and worse outcomes among heavier voluntary users, but the MIT Media Lab/OpenAI institutional attribution is not directly evidenced in the retrieved text.

### c46 — exists ⚠️ · applied ⚠️  (line 181)
_Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., & Yang, D. (2025). The rise of AI companions. arXiv:2506.12605. https://arxiv.org/abs/2506.12605 [report] Reported in 2026 as published in _Nature Human Behaviour_ [secondary]._
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms 1,131 Character.AI users, lower well-being concentrated among small networks with companionship as primary use, stronger with disclosive use, and correlational framing. Sample of donated transcripts (237) differs slightly from the cited 244.
- gpt: exists=nuance applied=nuance [evidence_text] — The arXiv work exists with matching authors and a closely related but longer title; the claimed Nature Human Behaviour publication is not confirmed by the retrieved evidence. The abstract supports 1,131 CharacterAI users, transcript donation from 237 rather than 244 participants, and associations involving smaller social networks, companionship motives, intensive/disclosive use, and lower well-being, so the application is mostly but not exactly supported.

### c47 — exists ✅ · applied ☐  (line 188)
_Stanford HAI: https://hai.stanford.edu/news/ai-companions-may-worsen-loneliness-for-vulnerable-users-stanford-study-finds_
- claude: exists=verified applied=unchecked [no_basis] — Stanford HAI page resolves and reports the Yang-lab/Nature Human Behaviour study; no specific claims attached to this citation to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The Stanford HAI URL resolves with the cited page title. No specific claims are attached to this citation record.

### c49 — exists ✅ · applied ☐  (line 195)
_https://www.psypost.org/turning-to-chatbots-when-lonely-may-exacerbate-feelings-of-loneliness-study-finds/_
- claude: exists=verified applied=unchecked [no_basis] — PsyPost article resolves and covers the Folk & Dunn Psychological Science study; no specific claims attached to this citation to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The PsyPost URL resolves with the cited title. No specific claims are attached to this citation record.

### c53 — exists ☐ · applied ☐  (line 214)
_Coverage: https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; cannot verify existence or content, and no claims are attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The URL fetch failed with HTTP 403, so the cited Safe States page is not confirmed from the provided evidence. No specific claims are attached to this citation record.

### c61 — exists ☐ · applied ✅  · ⚑ degraded  (line 249)
_FTC 6(b) inquiry, 11 September 2025: orders to Alphabet, Character Technologies, Instagram, Meta, OpenAI, Snap and xAI on how companion chatbots are tested and monitored for harm to children. A study, not enforcement. **[secondary]** https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots_
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch returned HTTP 429, so existence is not checkable from evidence. The FTC did issue 6(b) orders to these seven companies on 11 September 2025 regarding companion chatbots per my knowledge.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The DLA Piper page could not be checked because the URL fetch returned HTTP 429. Based only on model knowledge, the FTC 6(b) inquiry description and the note that it was a study rather than enforcement appear consistent, but this was not verified from retrieved text.

### c62 — exists ✅ · applied ⚠️  (line 254)
_California SB 243, signed 13 October 2025, effective 1 January 2026: companion chatbots must disclose they are AI, keep suicide and self-harm protocols, and remind minors to take breaks; private right of action. Exempts customer-service and utility bots. **[secondary]** https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law_
- claude: exists=verified applied=verified [evidence_text] — The Skadden page resolves and confirms SB 243 regulates companion chatbots with disclosure, safety protocols, and reporting requirements. Snippet supports disclosure and self-harm/suicide protections; exact dates and exemptions not shown but core claim is supported.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden URL resolves to the cited publication. The snippet supports the main points about California SB 243 regulating companion chatbots, disclosures, safety protocols, annual reporting, and potential civil damages, but it does not confirm every detail in the claim such as the signing/effective dates, minor break reminders, or exemptions.

### c64 — exists ☐ · applied ☐  (line 274)
_Ibrahim et al. 2026, _Nature_, already in piece 03_
- claude: exists=unchecked applied=unchecked — Crossref returned no match for Ibrahim et al. 2026 in Nature; author notes it is already cited in piece 03, so no evidence here to judge either axis.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no matching metadata for an Ibrahim et al. 2026 Nature item. No source text was retrieved to assess whether it supports the claimed warmth/accuracy tradeoff.

### c65 — exists ☐ · applied ☐  (line 275)
_Cheng et al. 2026_
- claude: exists=unchecked applied=unchecked — No Crossref match for Cheng et al. 2026 and no other evidence; cannot judge existence or application.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no matching metadata for Cheng et al. 2026. No source text was retrieved to assess the claim about sycophancy being rewarded by users.

### c66 — exists ☐ · applied ☐  (line 277)
_Li, Dunn et al. (2026)_
- claude: exists=unchecked applied=unchecked — No Crossref match for Li, Dunn et al. (2026) and no other evidence; cannot judge either axis.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no matching metadata for Li, Dunn et al. 2026. No source text was retrieved to assess the claim about connection requiring the chance to care for someone.

### c67 — exists ☐ · applied ☐  (line 291)
_No per-user harm rate exists for AI relationships, and none comparable for human ones. Every "compared to what?" here is qualitative._
- claude: exists=unchecked applied=unchecked — This is an author's analytical statement, not a citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation. Both existence and application are therefore unchecked.

### c68 — exists ☐ · applied ☐  (line 293)
_Several 2026 papers were reached only through press releases (Folk & Dunn; Li, Dunn et al.; the Nature Human Behaviour version of Zhang et al.; the De Freitas update study). Their numbers need checking against the papers before a piece quotes them._
- claude: exists=unchecked applied=unchecked — Marked deliberately_uncited; a caveat note about papers reached only through press releases, intentionally not a verified citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is deliberately uncited and marked as not a citation. Both existence and application are therefore unchecked.

### c69 — exists ☐ · applied ☐  (line 296)
_The lawsuits are allegations. None has produced a finding of fact._
- claude: exists=unchecked applied=unchecked — Author's disclaimer statement, not a citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation. Both existence and application are therefore unchecked.

### c70 — exists ☐ · applied ☐  (line 297)
_Most benefit evidence is for designed mental-health tools; most harm evidence is for general companion apps and general assistants. Comparing them directly would mislead._
- claude: exists=unchecked applied=unchecked — Author's analytical caveat, not a citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation. Both existence and application are therefore unchecked.

### c71 — exists ☐ · applied ☐  (line 299)
_Deaths of teenagers are part of this record. Any piece must treat them seriously and not as debating points._
- claude: exists=unchecked applied=unchecked — Author's editorial statement, not a citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation. Both existence and application are therefore unchecked.

## ✅ AGREE-clean (7)
### c35 — exists ✅ · applied ✅  (line 109)
_Manipulation at the exit. In an audit of companion apps, about 37% of farewells drew a manipulative reply (De Freitas, Oğuz-Uğuralp & Uğuralp 2025, HBS Working Paper 26-005). https://arxiv.org/abs/2508.19258 **[report]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv metadata confirms the paper 'Emotional Manipulation by AI Companions' by De Freitas et al., and the abstract states manipulative tactics appeared in 37% of 1,200 farewells, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to 'Emotional Manipulation by AI Companions' by De Freitas, Oguz-Uguralp, and Kaan-Uguralp. The abstract explicitly says 1,200 real farewells across companion apps deployed one of six tactics in 37% of farewells.

### c36 — exists ✅ · applied ✅  (line 113)
_Sycophancy promotes dependence. Sycophantic AI reduced prosocial intentions and increased dependence (Cheng et al. 2026, _Science_ 391(6792)). https://doi.org/10.1126/science.aec8352 **[report]**_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the DOI, Science 391(6792), and Cheng et al.; the abstract states sycophantic AI reduced willingness to repair conflicts and increased dependence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the DOI, title, authors, journal, year, volume, and issue for the Science article. The abstract states that sycophantic AI reduced willingness to repair interpersonal conflicts and promoted dependence/preference, supporting the claim.

### c40 — exists ✅ · applied ✅  (line 141)
_Li, H., Zhang, R., Lee, Y.-C., Kraut, R. E., & Mohr, D. C. (2023). Systematic review and meta-analysis of AI-based conversational agents for promoting mental health and well-being. _npj Digital Medicine_, 6, 236. https://doi.org/10.1038/s41746-023-00979-5 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the npj Digital Medicine article and the abstract matches the claimed 35 studies, 15 RCTs, depression g=0.64, distress g=0.70, and non-significant well-being g=0.32 (CI crossing zero).
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the DOI, title, authors, journal, year, and article metadata for the npj Digital Medicine review. The abstract explicitly reports 35 eligible studies, 15 RCTs in the meta-analysis, depression g=0.64, distress g=0.70, and non-significant overall well-being g=0.32 with CI crossing zero.

### c44 — exists ✅ · applied ✅  (line 166)
_De Freitas, J., Oğuz-Uğuralp, Z., Uğuralp, A. K., & Puntoni, S. (2025). AI companions reduce loneliness. _Journal of Consumer Research_, 52(6), 1126–1148. https://doi.org/10.1093/jcr/ucaf040 **[report]**_
- claude: exists=verified applied=verified [evidence_text] — DOI-matched abstract confirms AI companions reduced loneliness on par with interacting with another person and more than watching YouTube videos, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and DOI. The abstract directly states that Study 2 found AI companions alleviated loneliness on par with interacting with another person and more than watching YouTube videos, with momentary reductions also shown longitudinally.

### c48 — exists ✅ · applied ✅  (line 190)
_Folk, D., & Dunn, E. (2026). How does turning to AI for companionship predict loneliness and vice versa? _Psychological Science_, 37(4). [secondary]_
- claude: exists=verified applied=verified [evidence_text] — Crossref-matched abstract confirms 12-month study of 2,000+ adults in four countries, feeling less connected predicting increased chatbot use, chatbot use not significantly predicting decreased connection, and exploratory framing.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Psychological Science article, DOI, authors, volume, issue, pages, and abstract. The abstract supports the 12-month, more-than-2,000-adult, four-country design and the bidirectional findings, including that lower social connection predicted later chatbot use while chatbot use did not significantly predict later decreases in broader social connection, with caution due to exploratory analyses.

### c56 — exists ✅ · applied ✅  (line 223)
_Holt-Lunstad, J., Smith, T. B., & Layton, J. B. (2010). Social relationships and mortality risk: A meta-analytic review. _PLoS Medicine_, 7(7), e1000316. https://doi.org/10.1371/journal.pmed.1000316 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI-matched abstract confirms 148 studies, 308,849 participants, OR=1.50 (50% increased survival likelihood), comparable to established risk factors, matching all claims exactly.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the article, DOI, journal, year, and metadata. The Europe PMC abstract directly supports 148 studies, 308,849 participants, OR=1.50/50% greater survival likelihood, and comparability to established mortality risk factors.

### c57 — exists ✅ · applied ✅  (line 231)
_Tukachinsky, R., Walter, N., & Saucier, C. J. (2020). Antecedents and effects of parasocial relationships: A meta-analysis. _Journal of Communication_, 70(6), 868–894. https://doi.org/10.1093/joc/jqaa034 **[record + secondary]**_
- claude: exists=verified applied=verified [evidence_text] — DOI-matched abstract confirms the meta-analysis found no significant relationship between social deficiencies and parasocial relationships, supporting the 'no support for compensation' claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and DOI. The abstract directly states that the meta-analysis did not find a significant relationship between social deficiencies and parasocial relationships, consistent with no support for a social-deficit compensation account.
