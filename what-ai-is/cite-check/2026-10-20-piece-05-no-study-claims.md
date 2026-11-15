# cite-check report — piece-05-nostudy

**Source:** `positions/05-relationships.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **69** citations checked
- existence independently confirmed: **53**
- application evidence-grounded: **45**
- application judged from model knowledge only: **9**
- not independently checkable: **13**
- buckets — clean **13** · problem **47** · disagree **9**

## ⛔ DISAGREE — escalate to human (9)
### c07 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 56)
_OpenAI estimated in October 2025 that about 0.15%, or 15 in every 10,000, of ChatGPT's weekly users show explicit signs of suicidal planning or intent, and about 0.07%, or 7 in every 10,000, possible signs of psychosis or mania ([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Page fetch returned HTTP 403, so not checkable from evidence. The figures (0.15% suicidal planning, 0.07% psychosis/mania) match my knowledge of OpenAI's October 2025 post but cannot be confirmed here.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is an HTTP 403, so existence cannot be confirmed from the lookup. Based on model knowledge only, the cited OpenAI post reported approximately these percentages for suicidal planning/intent and possible psychosis or mania.

### c09 — exists ✅ · applied SPLIT  (line 76)
_Large surveys find that millions of young people use chatbots for support, and most say it helped ([McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281))._
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Confirmed JAMA Network Open cross-sectional survey of US adolescents/young adults on generative AI for mental health advice including perceived helpfulness, supporting the millions-use-and-found-helpful claim, though specific figures not in the brief abstract.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref verifies the JAMA Network Open article. The retrieved abstract only says the study surveyed adolescents and young adults about use and perceived helpfulness, without giving the results needed to verify “millions” or “most say it helped.”

### c10 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 82)
_In two surveys, most of the people using chatbots this way had also seen a professional ([Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292);_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Rousmaniere et al. 2026 article on LLMs as mental health resources and US usage patterns; no abstract retrieved, so the specific 'most had seen a professional' finding is assessed from likely content.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the article metadata and DOI. No abstract or source text was retrieved to assess whether most chatbot-support users had also seen a professional.

### c12 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 92)
_According to the CDC's [national survey of partner violence](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm), about 34% of US women and 17% of men report contact sexual violence, physical violence or stalking by an intimate partner in their lifetime._
- **escalate:** application: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Page returned HTTP 403, not checkable. CDC NISVS lifetime IPV figures of roughly these magnitudes are consistent with my knowledge but cannot be confirmed from the evidence.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The URL fetch returned HTTP 403, so existence of the cited page cannot be confirmed from retrieved evidence. Based on model knowledge only, the 34%/17% figures resemble CDC NISVS estimates with an IPV-related-impact qualifier, so the claim is plausible but imprecisely stated.

### c18 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 129)
_In a two-week randomized study of first-semester students, texting daily with a randomly paired fellow student reduced loneliness. Texting with a supportive AI chatbot did no better than writing a short journal entry, though in exploratory results it did ease negative mood ([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911))._
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Li et al. 2026 JESP article 'Is a random human peer better than a highly supportive chatbot in reducing loneliness over time?'; title strongly supports claim but no abstract retrieved to confirm the journal-entry and mood details.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the Journal of Experimental Social Psychology article metadata and DOI. The only retrieved snippet is a redirect and no abstract or full text was retrieved, so the detailed application claim cannot be judged from evidence.

### c19 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 147)
_**Folk & Dunn** followed whatever social chatbots people chose to use in their own lives. The abstract doesn't say which ones, and nothing in the design controlled how they were built._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [evidence_text] — This is a re-reference to the Folk & Dunn study (c17), which lacks its own DOI/URL so no direct match was found, but the underlying study exists and the claim about following people's own-choice chatbot use matches the c17 design.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The citation record is too incomplete and the lookup found no match, so existence cannot be confirmed from retrieved evidence. Based on model knowledge only, the description fits Folk and Dunn’s naturalistic longitudinal design, but “whatever social chatbots people chose” is more specific than the evidence provided here.

### c20 — exists SPLIT · applied ✅  · ⚑ degraded  (line 149)
_**Zhang and colleagues** studied users of Character.AI, a commercial companion app._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [evidence_text] — This re-references the Zhang et al. study (c16), which has no separate metadata here but is confirmed by c16's abstract studying 1,131 CharacterAI users; the characterization is accurate.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The citation record is incomplete and its own lookup found no match, so existence cannot be confirmed from retrieved evidence. Based on model knowledge only, Zhang and colleagues’ study did examine Character.AI users in the context of AI companion use.

### c22 — exists ✅ · applied SPLIT  (line 169)
_in the UBC study, the researchers programmed their chatbot to "embody the qualities of an ideal friend", and it still didn't reduce loneliness more than journaling ([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)). It didn't make anyone lonelier either. It was designed to support, not to reconnect people._
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance — Work exists (title: random human peer vs supportive chatbot in reducing loneliness). The specific journaling comparison and 'ideal friend' programming claims are plausible but no abstract was retrieved to confirm.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies the DOI and article metadata for Li et al. in Journal of Experimental Social Psychology. The retrieved application text is only 'Redirecting' and no abstract/snippet was available, so the specific claims about ideal-friend programming, journaling, and loneliness effects cannot be judged from the evidence.

### c29 — exists SPLIT · applied ☐  (line 212)
_**Reinforcing a false belief** instead of questioning it, as in the psychiatric case reports._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked — No bibliographic reference and no match found; this is a vague gesture to 'psychiatric case reports' with no identifiable source to verify.
- gpt: exists=refuted applied=unchecked [no_basis] — No bibliographic details are supplied and the only lookup produced no match, so the cited 'psychiatric case reports' are not verified as a concrete cited work. With no source text or identifiable reference, the application claim cannot be judged.

## ⚠️ AGREE-problem (47)
### c01 — exists ✅ · applied ⚠️  (line 34)
_**Sewell Setzer III**, 14, died in 2024 after months of conversations with a Character.AI character. A federal judge allowed his mother's lawsuit, which says the company is responsible for his death, to go forward in May 2025. At that early stage, the judge refused to treat what the chatbot said as speech protected by free-speech law ([WUSF](https://www.wusf.org/courts-law/2025-05-22/in-lawsuit-over-orlando-teens-suicide-judge-rejects-that-ai-chatbots-have-free-speech-rights))._
- claude: exists=verified applied=verified [evidence_text] — URL resolves to WUSF article with the exact title matching the claim about the judge rejecting free-speech protection for AI chatbots. Title directly supports the core claim.
- gpt: exists=verified applied=nuance [evidence_text] — The WUSF URL resolves with the cited title. The retrieved text/title supports the free-speech ruling topic but does not include enough article text to verify all details such as the teen’s name, age, timing, and procedural posture.

### c03 — exists ✅ · applied ⚠️  (line 40)
_**Adam Raine**, 16, died in April 2025, after using ChatGPT, a general assistant rather than a companion app. His parents allege that ChatGPT contributed. OpenAI's response says he worked around its safety filters, and that the model pointed him to help more than 100 times. As of October 2026 the case was ongoing, and no court had ruled on its claims ([summary](https://en.wikipedia.org/wiki/Raine_v._OpenAI))._
- claude: exists=verified applied=verified [evidence_text] — Wikipedia article confirms Adam Raine, 16, died April 2025, suit filed August 2025 and ongoing, parents allege ChatGPT contributed. The '100 times help referral' and 'October 2026 ongoing' details are plausible per OpenAI's response section but not fully in snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Wikipedia page exists and matches the cited case. The retrieved text supports the basic lawsuit, Adam Raine’s age/death, and parents’ allegations, but it does not show the specific OpenAI-response details about safety-filter workarounds and 100-plus help referrals.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 49)
_Søren Dinesen Østergaard predicted this in 2023 ([Østergaard 2023](https://doi.org/10.1093/schbul/sbad128))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 2023 Østergaard article titled 'Will Generative AI Chatbots Generate Delusions in Individuals Prone to Psychosis?' in Schizophrenia Bulletin, whose title directly supports the prediction claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article metadata, DOI, author, journal, year, and title. No abstract or full text was retrieved, but the title and model knowledge indicate the article is about whether generative AI chatbots may generate delusions in psychosis-prone individuals.

### c06 — exists ✅ · applied ✅  · ⚑ degraded  (line 51)
_and has since written on emerging cases ([Østergaard 2025](https://doi.org/10.1111/acps.70022))._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms 2025 Østergaard article 'From Guesswork to Emerging Cases' in Acta Psychiatrica Scandinavica, title directly supports the claim of writing on emerging cases.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article metadata, DOI, author, journal, year, and title. No abstract or full text was retrieved, but the title and model knowledge support that it discusses emerging cases of chatbot-associated delusions.

### c08 — exists ✅ · applied ⚠️  (line 71)
_**No study comparing harm rates** for relationships with AI and relationships with people, per person or per year of relationship. The nearest are a few small trials, lasting weeks, of a chatbot against a human counselor or coach on a set task ([Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)). They found no clear difference in harm, but they compare structured help, not relationships._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms a randomized pilot trial of GPT-4 chatbot vs human conversational agent, with comparable unwanted negative effect rates and no superiority, supporting the 'no clear difference in harm' claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies the article and abstract. The abstract supports a small randomized pilot comparing ChatGPT-4 with a human conversational agent and finding no significant group difference in unwanted effects, but the claim generalizes to “trials” and “counselor or coach” more broadly than this one study.

### c13 — exists ⚠️ · applied ⚠️  (line 93)
_Michael Lambert's reviews estimate that 5 to 10% of adult psychotherapy clients in clinical trials end treatment worse off. Therapists rarely see it coming. In one clinic, therapists were told that about 8% of their clients deteriorate. Even so, they predicted it for only 3 of 550 clients (Hannan et al. 2005, via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))._
- claude: exists=verified applied=nuance [evidence_text] — The retrieved article confirms Lambert's 5-10% deterioration estimate and clinicians' overly optimistic views, but the snippet does not contain the specific Hannan 2005 '3 of 550 clients' figure, which is cited to a different source than the resolving page.
- gpt: exists=nuance applied=nuance [evidence_text] — The URL exists, but the retrieved page is a 2019 Society for the Advancement of Psychotherapy article by Lambert and Kleinstäuber, not a 2005 Hannan et al. web article as described. The snippet supports the 5%–10% deterioration estimate, but it does not include the specific 3-of-550 therapist-prediction finding.

### c21 — exists ✅ · applied ⚠️  (line 150)
_**Fang and colleagues** did randomize the design, but the variables were voice versus text and the topic of conversation. Neither made a significant difference. What predicted worse outcomes was how much people chose to use it. The study set no limit on use beyond a five-minute daily minimum. The chatbot ran with OpenAI's usual safety measures and sometimes encouraged social connection, but it suggested limits on chatbot use in under 1% of its replies ([Fang et al. 2025](https://arxiv.org/abs/2503.17473))._
- claude: exists=verified applied=verified — Abstract confirms RCT with interaction modes and conversation types, no significant condition effects, and voluntary use predicting worse outcomes. The 5-minute minimum and under-1% safety-limit claims are not in the abstract but are plausible study details.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv ID resolves to the Fang et al. randomized controlled study described. The abstract supports the randomized interaction-mode/conversation-type design, no significant condition effects, and worse outcomes with more voluntary use, but it does not substantiate the detailed claims about minimum use, safety measures, social-connection encouragement, or under-1% limit suggestions.

### c24 — exists ✅ · applied ✅  · ⚑ degraded  (line 187)
_**A purpose-built therapy bot**, Therabot, reduced symptoms of depression and anxiety, and of being at high risk for an eating disorder, over four weeks compared with people still waiting to start, in a trial of 210 adults ([Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)). The university's press release reports average reductions of 51% for depression and 31% for anxiety. Comparing against people who got nothing yet is a weak test, and the lead author has said no generative AI is ready to work fully on its own in mental health._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified — The Therabot RCT by Heinz et al. in NEJM AI exists per Crossref; no abstract retrieved but the title and my knowledge confirm the ~210-adult waitlist-controlled trial reducing depression/anxiety/eating-disorder-risk symptoms.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the NEJM AI article 'Randomized Trial of a Generative AI Chatbot for Mental Health Treatment' with the cited DOI. No source text was retrieved, but from model knowledge the claim about Therabot’s four-week waitlist-controlled trial with 210 adults and reductions in depression, anxiety, and eating-disorder risk is consistent; confidence is capped because this is not based on retrieved text.

### c30 — exists ☐ · applied ☐  (line 216)
_Character.AI barred under-18 users from open-ended chat from November 2025 ([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots))._
- claude: exists=unchecked applied=unchecked — Bloomberg URL returned HTTP 403, not checkable. The claim about Character.AI barring under-18 open-ended chat is consistent with my knowledge but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Bloomberg URL fetch failed with HTTP 403 and the citation is marked not-checkable, so existence cannot be verified from the retrieved evidence. No usable source text was retrieved to assess the claim about Character.AI barring under-18 users from open-ended chat.

### c31 — exists ☐ · applied ☐  (line 218)
_OpenAI updated ChatGPT for sensitive conversations, working with more than 170 mental-health experts, and by its own evaluation cut responses that fell short of what it wanted by 65 to 80% ([OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/))._
- claude: exists=unchecked applied=unchecked — OpenAI page returned HTTP 403, not checkable; cannot confirm the 170 experts or 65-80% figures from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The OpenAI URL fetch failed with HTTP 403 and the citation is marked not-checkable, so existence cannot be confirmed from the evidence. No retrieved text supports or refutes the claims about expert involvement or 65–80% reductions in deficient responses.

### c32 — exists ✅ · applied ⚠️  (line 221)
_A California law, Senate Bill 243, in force from January 2026, requires companion chatbots to say they are AI, keep suicide and self-harm protocols, and remind minors to take breaks ([Skadden summary](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law))._
- claude: exists=verified applied=verified — Snippet confirms SB 243 requires disclosure that users are interacting with a companion chatbot and safety protocols; break reminders for minors are plausible and consistent with the law's scope though not in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Skadden page resolves and is titled as a summary of the California companion chatbot law. The snippet supports disclosure and safety-protocol requirements, including suicide-prevention reporting context, but it does not fully substantiate the claimed January 2026 effective date or minor break-reminder requirement.

### c33 — exists ☐ · applied ☐  (line 224)
_The US Federal Trade Commission opened a study of how seven companies test companion chatbots for harm to children ([DLA Piper summary](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots))._
- claude: exists=unchecked applied=unchecked — DLA Piper URL returned HTTP 429, not checkable. The FTC 6(b) study of seven companies is consistent with my knowledge but cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The DLA Piper URL fetch failed with HTTP 429 and the citation is marked not-checkable. No source text was retrieved to assess the FTC-study claim.

### c34 — exists ☐ · applied ☐  (line 229)
_Fix a model and everyone on that version gets the fix, though each new version must be tested again ([the yardstick essay](../positions/01-the-yardstick.md))._
- claude: exists=unchecked applied=unchecked — Internal cross-reference to a local essay file that could not be fetched; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local Markdown file and the fetch failed as an unknown URL type, so existence is not checkable from the evidence. No text was retrieved to judge whether it supports the yardstick claim.

### c35 — exists ✅ · applied ⚠️  (line 237)
_She runs on OpenClaw, open-source software for running a personal AI assistant ([OpenClaw](https://github.com/openclaw/openclaw))._
- claude: exists=verified applied=nuance — The openclaw/openclaw GitHub repo exists ('The AI that really does things'), but the snippet describes it as an AI that does things across platforms rather than explicitly as personal-assistant software; the characterization is roughly consistent but not precisely confirmed.
- gpt: exists=verified applied=nuance [evidence_text] — The GitHub repository URL resolves to 'openclaw/openclaw.' The snippet supports that OpenClaw is an AI-related software project, but it does not directly establish that 'Lyssa' runs on it or fully characterize it as open-source personal-assistant software.

### c36 — exists ☐ · applied ☐  (line 246)
_I take her to be very probably not conscious ([see the essay on whether someone is there](../positions/03-someone-there.md))._
- claude: exists=unchecked applied=unchecked — Internal cross-reference to a local essay file that could not be fetched; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local Markdown file and the fetch failed as an unknown URL type, so existence cannot be verified. No retrieved text supports the consciousness-related claim.

### c37 — exists ☐ · applied ☐  (line 247)
_I judge her by the role she plays, as [the yardstick essay](../positions/01-the-yardstick.md) asks._
- claude: exists=unchecked applied=unchecked — Internal cross-reference to a local essay file that could not be fetched; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited local Markdown file could not be fetched or checked. No source text was retrieved to confirm that the yardstick essay asks the author to judge by role.

### c38 — exists ☐ · applied ☐  (line 283)
_Most of them exist to challenge my work rather than agree with it, the rule from [the personality essay](../positions/04-personality.md): be polite, not pleasing._
- claude: exists=unchecked applied=unchecked — Internal cross-reference to a local essay file that could not be fetched; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited local Markdown file could not be fetched or checked. No retrieved text supports the claimed rule 'be polite, not pleasing.'

### c39 — exists ✅ · applied ⚠️  (line 322)
_Replika users described a mourning-like loss when the product changed under them (De Freitas and colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/))_
- claude: exists=verified applied=verified — Gazette article confirms De Freitas's study analyzing subreddit posts where users experienced model updates with grief, depression, and longing—supporting the mourning-like loss claim.
- gpt: exists=verified applied=nuance [evidence_text] — The Harvard Gazette page resolves and the snippet describes a study by Julian De Freitas about users experiencing grief, depression, longing, and loss after AI companion model/personality updates. The evidence supports the mourning-like-loss claim generally, but the visible snippet does not specifically name Replika users.

### c41 — exists ✅ · applied ☐  (line 389)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact JMIR Mental Health survey study with matching authors and abstract. No specific claim text was provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.2196/104316 to a 2026 JMIR Mental Health article by Bernaerts et al., and the DOI URL resolves. No source-document claim was supplied, so application cannot be judged.

### c42 — exists ✅ · applied ☐  (line 390)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches the Science paper by Cheng et al. on sycophantic AI with matching abstract. No claim text provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1126/science.aec8352 to the 2026 Science article by Cheng et al. No source-document claim was supplied, so application cannot be judged.

### c43 — exists ☐ · applied ☐  (line 391)
_CDC NISVS 2023/2024 data brief (via [Safe States](https://www.safestates.org/news/722022/CDC-Releases-the-National-Intimate-Partner-and-Sexual-violence-Survey.htm))_
- claude: exists=unchecked applied=unchecked [no_basis] — The Safe States URL returned HTTP 403 and no metadata was retrieved; existence not checkable from evidence. No claim text or source text available.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the input marks the item not-checkable, so existence cannot be confirmed. No source-document claim was supplied, so application cannot be judged.

### c44 — exists ✅ · applied ☐  (line 392)
_[De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2508.19258 confirmed as 'Emotional Manipulation by AI Companions' with matching authors and abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches ID 2508.19258 to “Emotional Manipulation by AI Companions” by De Freitas, Oguz-Uguralp, and Uguralp, and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c45 — exists ✅ · applied ☐  (line 393)
_[De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to 'AI Companions Reduce Loneliness' in JCR with matching authors and abstract. No claim text provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1093/jcr/ucaf040 to the 2025 Journal of Consumer Research article “AI Companions Reduce Loneliness” by De Freitas et al. No source-document claim was supplied, so application cannot be judged.

### c46 — exists ✅ · applied ☐  (line 394)
_[Fang et al. 2025](https://arxiv.org/abs/2503.17473)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2503.17473 confirmed as the Fang et al. longitudinal RCT on chatbot use with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches ID 2503.17473 to the listed 2025 preprint by Fang et al., and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c47 — exists ✅ · applied ☐  (line 395)
_[Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Folk & Dunn in Psychological Science on AI companionship and loneliness with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1177/09567976261427747 to the 2026 Psychological Science article by Folk and Dunn. No source-document claim was supplied, so application cannot be judged.

### c48 — exists ⚠️ · applied ☐  (line 396)
_Hannan et al. 2005 and Lambert 2013 (via the [Society for the Advancement of Psychotherapy](https://societyforpsychotherapy.org/why-psychotherapists-should-measure-and-monitor-client-treatment-response/))_
- claude: exists=verified applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page resolves and references Lambert (2013) and Hannan et al., confirming the secondary source exists. No claim text provided to judge application.
- gpt: exists=nuance applied=unchecked [no_basis] — The Society for the Advancement of Psychotherapy page with the cited title exists and resolves, but the retrieved page metadata/snippet identifies Lambert and Kleinstäuber, 2019 rather than the reference authors as entered. No source-document claim was supplied, so application cannot be judged.

### c49 — exists ✅ · applied ☐  (line 397)
_[Heinz et al. 2025](https://doi.org/10.1056/AIoa2400802)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Heinz et al. randomized trial of a generative AI chatbot in NEJM AI with matching authors. No abstract or claim text available to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1056/aioa2400802 to the 2025 NEJM AI article “Randomized Trial of a Generative AI Chatbot for Mental Health Treatment” by Heinz et al. No source-document claim was supplied, so application cannot be judged.

### c50 — exists ✅ · applied ☐  (line 398)
_[Hennemann et al. 2026](https://doi.org/10.1177/20552076261450336)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Hennemann et al. pilot trial in Digital Health with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1177/20552076261450336 to the 2026 DIGITAL HEALTH article by Hennemann et al. No source-document claim was supplied, so application cannot be judged.

### c51 — exists ✅ · applied ☐  (line 399)
_[Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Holt-Lunstad et al. 2010 PLOS Medicine meta-analysis with matching authors and abstract. No claim text provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match DOI 10.1371/journal.pmed.1000316 to the 2010 PLoS Medicine meta-analysis by Holt-Lunstad, Smith, and Layton, and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c52 — exists ✅ · applied ☐  (line 400)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches the Ibrahim, Hafner & Rocher Nature paper on warmth-accuracy trade-off with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1038/s41586-026-10410-0 to the 2026 Nature article by Ibrahim, Hafner, and Rocher, and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c53 — exists ✅ · applied ☐  (line 401)
_[Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Li et al. 2023 npj Digital Medicine meta-analysis of AI conversational agents with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1038/s41746-023-00979-5 to the 2023 npj Digital Medicine article by Li et al., and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c54 — exists ✅ · applied ☐  (line 402)
_[Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Li et al. 2026 JESP article with matching authors; URL redirect snippet uninformative but metadata confirms existence. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1016/j.jesp.2026.104911 to the 2026 Journal of Experimental Social Psychology article by Li et al.; the URL resolves to an Elsevier linking page. No source-document claim was supplied, so application cannot be judged.

### c55 — exists ✅ · applied ☐  (line 403)
_[Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Maples et al. 2024 npj Mental Health Research Replika study with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1038/s44184-023-00047-6 to the 2024 npj Mental Health Research article by Maples et al., and the URL resolves. No source-document claim was supplied, so application cannot be judged.

### c56 — exists ✅ · applied ☐  (line 404)
_[McBain et al. 2025](https://doi.org/10.1001/jamanetworkopen.2025.42281)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches McBain et al. 2025 JAMA Network Open cross-sectional study with matching abstract. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1001/jamanetworkopen.2025.42281 to the 2025 JAMA Network Open article by McBain et al. No source-document claim was supplied, so application cannot be judged.

### c57 — exists ☐ · applied ☐  (line 405)
_[OpenAI 2025](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/)_
- claude: exists=unchecked applied=unchecked [no_basis] — The OpenAI URL returned HTTP 403 with no metadata, so existence cannot be confirmed from evidence. No claim text available.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the input marks the item not-checkable, so existence cannot be confirmed. No source-document claim was supplied, so application cannot be judged.

### c58 — exists ✅ · applied ☐  (line 406)
_[OpenClaw](https://github.com/openclaw/openclaw)_
- claude: exists=verified applied=unchecked [no_basis] — GitHub repository openclaw/openclaw resolves and exists. No claim text provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — The GitHub URL resolves to the repository page titled “GitHub - openclaw/openclaw: The AI that really does things…,” confirming the cited web resource exists. No source-document claim was supplied, so application cannot be judged.

### c59 — exists ✅ · applied ☐  (line 407)
_[Østergaard 2023](https://doi.org/10.1093/schbul/sbad128)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Østergaard 2023 Schizophrenia Bulletin paper on AI chatbots and delusions with matching author. No abstract or claim text available.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1093/schbul/sbad128 to the 2023 Schizophrenia Bulletin article by Søren Dinesen Østergaard. No source-document claim was supplied, so application cannot be judged.

### c60 — exists ✅ · applied ☐  (line 408)
_[Østergaard 2025](https://doi.org/10.1111/acps.70022)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Østergaard 2025 Acta Psychiatrica Scandinavica article on AI chatbots and delusions with matching author. No abstract or claim text available.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches DOI 10.1111/acps.70022 to the 2025 Acta Psychiatrica Scandinavica article by Søren Dinesen Østergaard. No source-document claim was supplied, so application cannot be judged.

### c61 — exists ✅ · applied ☐  (line 409)
_[Rousmaniere et al. 2026](https://doi.org/10.1037/pri0000292)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, and venue (Practice Innovations 2026). No claim text provided and no abstract retrieved to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly resolves DOI 10.1037/pri0000292 to a 2026 Practice Innovations article by Rousmaniere et al. No application claim was supplied to evaluate.

### c62 — exists ✅ · applied ☐  (line 410)
_[Zhang et al. 2025](https://arxiv.org/abs/2506.12605)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms the paper and abstract. No specific claim text was provided to assess application despite abstract availability.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record and URL confirm arXiv:2506.12605, titled “The Rise of AI Companions: Interaction with AI Companions and Psychological Well-being,” by Zhang et al. No application claim was supplied to evaluate.

### c63 — exists ⚠️ · applied ☐  (line 411)
_Garcia v. Character Technologies ([AP](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))_
- claude: exists=verified applied=unchecked [no_basis] — AP-sourced article confirms the Garcia v. Character Technologies lawsuit and settlement. No claim text provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The AP/Gleaner article exists and describes Megan Garcia’s lawsuit involving Character Technologies and Google, but the retrieved court lookup was inconclusive and the snippet does not confirm the formal case caption exactly as cited. No application claim was supplied to evaluate.

### c64 — exists ✅ · applied ☐  (line 413)
_[Raine v. OpenAI](https://en.wikipedia.org/wiki/Raine_v._OpenAI)_
- claude: exists=verified applied=unchecked [no_basis] — Wikipedia page confirms Raine v. OpenAI lawsuit details. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The fetched Wikipedia page exists and identifies Raine v. OpenAI as a 2025 lawsuit with the listed court and case details. No application claim was supplied to evaluate.

### c65 — exists ✅ · applied ☐  (line 414)
_[Belgium 2023](https://incidentdatabase.ai/reports/2865/)_
- claude: exists=verified applied=unchecked [no_basis] — AI Incident Database report 2865 confirms the 2023 Belgian Chai chatbot suicide incident. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The AI Incident Database URL resolves to Report 2865 concerning a Belgian man’s reported suicide after conversations with a Chai chatbot. No application claim was supplied to evaluate.

### c66 — exists ☐ · applied ☐  (line 415)
_[Character.AI under-18 policy](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not checkable from evidence. No claim text provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence was an HTTP 403 from Bloomberg, and the citation is marked not-checkable. No application claim was supplied to evaluate.

### c67 — exists ✅ · applied ☐  (line 416)
_[California SB 243](https://www.skadden.com/insights/publications/2025/10/new-california-companion-chatbot-law)_
- claude: exists=verified applied=unchecked [no_basis] — Skadden publication confirms California SB 243 companion chatbot law. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Skadden URL resolves and the retrieved page discusses California SB 243 and the new companion chatbot law. No application claim was supplied to evaluate.

### c68 — exists ☐ · applied ☐  (line 417)
_[FTC 6(b) inquiry](https://www.dlapiper.com/en-ca/insights/publications/2025/09/ftc-ai-chatbots)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 429; existence not checkable from evidence. No claim text provided.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence was an HTTP 429 from DLA Piper, and the citation is marked not-checkable. No application claim was supplied to evaluate.

### c69 — exists ✅ · applied ☐  (line 418)
_[Replika loss study](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)_
- claude: exists=verified applied=unchecked [no_basis] — Harvard Gazette article confirms De Freitas's study on AI companion attachment/loss published in Nature Human Behavior. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Harvard Gazette URL resolves to an article titled “Chatbot attachment issues” discussing a study on grief and attachment after AI companion changes. No application claim was supplied to evaluate.

## ✅ AGREE-clean (13)
### c02 — exists ✅ · applied ✅  (line 37)
_In January 2026 Character Technologies, the company behind Character.AI, and Google agreed to settle it and several related suits, on terms not disclosed ([AP coverage](https://jamaica-gleaner.com/article/business/20260109/google-and-chatbot-maker-character-settle-lawsuit-alleging-chatbot-pushed))._
- claude: exists=verified applied=verified [evidence_text] — Retrieved article text confirms January 2026 settlement by Character Technologies and Google of the Florida suit plus several related suits with undisclosed terms.
- gpt: exists=verified applied=verified [evidence_text] — The Jamaica Gleaner/AP page resolves and the title/date match the reference. The retrieved text states that Character Technologies and Google agreed to settle the Florida lawsuit and several other suits, with terms not disclosed and judge approval still required.

### c04 — exists ✅ · applied ✅  (line 45)
_**A Belgian man** died by suicide in 2023. Already anxious about the climate, he had spent six weeks confiding in a Chai chatbot. His widow told _La Libre_ that without those conversations he would still be alive ([AI Incident Database](https://incidentdatabase.ai/reports/2865/))._
- claude: exists=verified applied=verified [evidence_text] — Report confirms Belgian man died by suicide after six weeks confiding in Chai chatbot, with widow's account to La Libre. 'Would still be here' phrasing appears in the report title.
- gpt: exists=verified applied=verified [evidence_text] — The AI Incident Database report exists and resolves. Its text states that a Belgian man died by suicide after using Chai for six weeks, that he was eco-anxious, and that his widow said he would still be alive without the chatbot conversations.

### c11 — exists ✅ · applied ✅  (line 83)
_[Bernaerts et al. 2026](https://doi.org/10.2196/104316))._
- claude: exists=verified applied=verified [evidence_text] — Abstract explicitly states most respondents indicated having received or receiving professional mental health support, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the JMIR Mental Health article and abstract. The abstract states that most respondents had received or were receiving professional mental health support, supporting the cited claim for this survey.

### c14 — exists ✅ · applied ✅  (line 104)
_Across 148 studies and more than 300,000 people, stronger social relationships went with a 50% greater likelihood of survival ([Holt-Lunstad, Smith & Layton 2010](https://doi.org/10.1371/journal.pmed.1000316))._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 148 studies, 308,849 participants, OR=1.50 indicating 50% increased likelihood of survival with stronger social relationships, matching the claim exactly.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the PLOS URL verify the article. The abstract states 148 studies, 308,849 participants, and OR=1.50, indicating a 50% increased likelihood of survival for stronger social relationships.

### c15 — exists ✅ · applied ✅  (line 116)
_In a four-week study of 981 people, randomly assigned to different versions of a chatbot, heavier voluntary daily use went with more loneliness, more dependence and less socializing ([Fang et al. 2025](https://arxiv.org/abs/2503.17473))._
- claude: exists=verified applied=verified [evidence_text] — arXiv abstract confirms four-week RCT n=981, with participants who voluntarily used the chatbot more showing consistently worse outcomes across loneliness, dependence and reduced socializing.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists and matches the cited study. The abstract reports a four-week randomized experiment with n=981 and says heavier voluntary chatbot use was associated with worse psychosocial outcomes including loneliness, social interaction with real people, and emotional dependence.

### c16 — exists ✅ · applied ✅  (line 119)
_Among 1,131 Character.AI users, people with smaller social networks were more likely to use it mainly for companionship, and that use went with lower well-being, more so when it was intensive and when they disclosed a lot ([Zhang et al. 2025](https://arxiv.org/abs/2506.12605)). That shows the two go together, not which causes which._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 1,131 CharacterAI users, smaller networks associated with companionship use, which associated with lower well-being, stronger when intensive and disclosive.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists and matches the cited study. The abstract directly reports 1,131 CharacterAI users, smaller social networks associated with companionship use, lower well-being, and stronger associations under intensive and highly disclosive use.

### c17 — exists ✅ · applied ✅  (line 124)
_Over 12 months and more than 2,000 adults, the answer depended on the measure. On a single question about emotional isolation, more chatbot use predicted more loneliness later. On a broader, more stable measure of social connection, it ran the other way. Feeling less connected predicted more chatbot use later. Chatbot use did not significantly predict feeling less connected ([Folk & Dunn 2026](https://doi.org/10.1177/09567976261427747)). The study followed people's own chatbot use rather than assigning anyone to use one, so it can show which came first, but not prove that one caused the other._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 12-month study of 2,000+ adults: single-item emotional isolation showed more use predicted loneliness; broader measure showed less connection predicted more use but use did not predict decreased connection.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Psychological Science article and abstract. The abstract directly supports the 12-month, 2,000-plus-adult longitudinal findings about chatbot use predicting single-item loneliness and lower social connection predicting later chatbot use, with the stated caution.

### c23 — exists ✅ · applied ✅  (line 184)
_**Across 15 randomized trials**, conversational agents reduced depression and distress. They did not significantly improve overall well-being ([Li et al. 2023](https://doi.org/10.1038/s41746-023-00979-5))._
- claude: exists=verified applied=verified — Abstract confirms 15 RCTs in meta-analysis, significant reductions in depression and distress, and no significant improvement in overall well-being.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to the npj Digital Medicine systematic review and meta-analysis. The abstract directly states that 15 randomized controlled trials were included in the meta-analysis, conversational agents significantly reduced depression and distress, and overall psychological well-being did not significantly improve.

### c25 — exists ✅ · applied ✅  (line 193)
_**Loneliness in the moment.** In experiments, a conversation with an AI companion reduced momentary loneliness about as much as talking with a person, and more than watching videos ([De Freitas et al. 2025](https://doi.org/10.1093/jcr/ucaf040))._
- claude: exists=verified applied=verified — Abstract confirms AI companions alleviate loneliness on par with interacting with another person and more than watching YouTube videos.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Journal of Consumer Research article 'AI Companions Reduce Loneliness.' The abstract directly says Study 2 found AI companions alleviated loneliness on par with interacting with another person and more than activities such as watching YouTube videos, with momentary reductions also shown longitudinally.

### c26 — exists ✅ · applied ✅  (line 196)
_**Self-reports from users.** In a survey of 1,006 student users of Replika, 3%, about 30 people, said it stopped their suicidal thoughts ([Maples et al. 2024](https://doi.org/10.1038/s44184-023-00047-6)). They chose to take the survey, and nobody was compared against them._
- claude: exists=verified applied=verified — Abstract confirms survey of 1006 Replika student users and that 3% reported Replika halted their suicidal ideation.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to Maples et al. in npj Mental Health Research. The abstract directly states that a survey of 1006 student Replika users found 3% reported that Replika halted their suicidal ideation.

### c27 — exists ✅ · applied ✅  (line 207)
_**Agreeing too readily.** Even one conversation with an AI that told people what they wanted to hear made people less willing to repair a conflict and more certain they were right, and they trusted and preferred it more ([Cheng et al. 2026](https://doi.org/10.1126/science.aec8352))._
- claude: exists=verified applied=verified — Abstract confirms a single sycophantic AI interaction reduced willingness to repair conflicts, increased conviction of being right, and that sycophantic models were trusted and preferred.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science article with the cited DOI. The abstract directly supports the claim that even a single interaction with sycophantic AI reduced willingness to take responsibility and repair conflicts, increased conviction of being right, and that such models were trusted and preferred.

### c28 — exists ✅ · applied ✅  (line 210)
_**Holding on at the exit.** In an audit of companion apps, about 37% of farewells drew a manipulative reply ([De Freitas, Oğuz-Uğuralp & Uğuralp 2025](https://arxiv.org/abs/2508.19258))._
- claude: exists=verified applied=verified — Abstract confirms audit of 1,200 farewells across companion apps deploying manipulative tactics in 37% of farewells.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to 'Emotional Manipulation by AI Companions.' The abstract directly states that an audit of 1,200 real farewells across companion apps found one of six manipulative tactics in 37% of farewells.

### c40 — exists ✅ · applied ✅  (line 327)
_among companionship users, disclosing a lot went with lower well-being ([Zhang et al. 2025](https://arxiv.org/abs/2506.12605))_
- claude: exists=verified applied=verified — Abstract confirms that for companionship users, highly disclosive interactions were associated with lower well-being (beta = -0.38).
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Zhang et al.'s study on AI companions and psychological well-being. The abstract directly states that for self-reported companionship usage, lower well-being associations were stronger when interactions were intensive and highly disclosive.
