# cite-check report — brief14-worse-at-work

**Source:** `briefs/2026-10-19-14-worse-at-my-own-work.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **165** citations checked
- existence independently confirmed: **83**
- application evidence-grounded: **73**
- application judged from model knowledge only: **51**
- not independently checkable: **12**
- buckets — clean **24** · problem **129** · disagree **57**
- self-test vs human marks: existence agreed on **1/1**

## ⛔ DISAGREE — escalate to human (57)
### c15 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 74)
_The MIT "Your Brain on ChatGPT" EEG study (Kosmyna et al. 2025) is a preprint, not peer-reviewed as of its project page, with 54 participants and only 18 in the session that tested what happens afterwards. Its own authors ask the press not to say "brain rot", "harm" or "damage"_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=nuance [model_knowledge_only] — The Crossref hit is a different work (metadata drift), but the MIT Media Lab 'Your Brain on ChatGPT' preprint by Kosmyna et al. 2025 does exist with ~54 participants; the preprint/sample characterization is accurate to my knowledge.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref item is a different 2026 work by Kusano with a related title, not the cited MIT/Kosmyna study, so the cited work is not verified from the retrieved evidence. From model knowledge, the Kosmyna et al. MIT preprint is commonly described as non-peer-reviewed, with 54 participants and an 18-participant follow-up/session subset, and its authors cautioned against press terms such as “brain rot” or “damage.”

### c21 — exists SPLIT · applied ✅  · ⚑ degraded  (line 87)
_The famous "Google effect" on memory (Sparrow, Liu & Wegner 2011) failed to replicate in the part that was retested (Camerer et al. 2018; Hesselmann 2020)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Sparrow, Liu & Wegner (2011) 'Google Effects on Memory' in Science is a well-known real paper despite the no-match; it coined the Google effect on memory.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup did not match a work, so existence cannot be confirmed from the provided evidence. From general knowledge, Sparrow, Liu, and Wegner 2011 is the standard paper associated with the 'Google effect' on memory.

### c22 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 88)
_failed to replicate in the part that was retested (Camerer et al. 2018; Hesselmann 2020)_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=nuance [model_knowledge_only] — Camerer et al. 2018 (Nature Human Behaviour) replicated social-science experiments; the Sparrow Exp. relevant item did fail to replicate, though details are from memory.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence contains no matching bibliographic record. From general knowledge, Camerer et al. 2018 is a large replication project that included a retest of part of the Sparrow et al. Google-effect finding and reported non-replication.

### c23 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 88)
_Hesselmann 2020_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved; Hesselmann 2020 is plausible as a replication discussion but I cannot confirm specifics.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved record verifies a Hesselmann 2020 source. From general knowledge, Hesselmann has discussed the failed replication of the Google-effect result, but this is not confirmed by retrieved text here.

### c27 — exists SPLIT · applied ✅  · ⚑ degraded  (line 99)
_Bainbridge called this the irony of asking the operator to monitor a system installed because it does the job better._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Lisanne Bainbridge's 'Ironies of Automation' (1983) is a real, famous paper that makes exactly this point about operators monitoring automation installed to do the job better.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The Crossref lookup did not retrieve a matching Bainbridge record. From general knowledge, Bainbridge's 'Ironies of Automation' makes the point that operators are left monitoring systems introduced because they are better at the task.

### c29 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 102)
_on a task outside its abilities, consultants using AI were 19 percentage points less likely to be right (Dell'Acqua et al. 2023)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — Dell'Acqua et al. 2023 'Navigating the Jagged Technological Frontier' is a real HBS working paper; it reports consultants using AI were ~19 points less likely correct on out-of-frontier tasks.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No matching bibliographic record was retrieved. From general knowledge, Dell'Acqua et al. 2023's 'jagged frontier' study reports that consultants using AI on tasks outside the AI's frontier were about 19 percentage points less likely to produce correct solutions.

### c30 — exists SPLIT · applied ✅  · ⚑ degraded  (line 105)
_Experienced developers believed AI had made them about 20% faster when it had made them 19% slower (Becker et al. 2025)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — The METR 2025 study (Becker et al.) found experienced developers expected ~20% speedup but were actually ~19% slower using AI tools.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup found no match. From general knowledge of the 2025 developer-productivity study, the cited contrast between perceived AI speedup and measured slowdown is broadly consistent, though not verified from retrieved text.

### c31 — exists SPLIT · applied ✅  · ⚑ degraded  (line 107)
_Students who reread rather than tested themselves were more confident and remembered less (Roediger & Karpicke 2006)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Roediger & Karpicke 2006 'Test-Enhanced Learning' is a real, well-known paper showing rereading boosted confidence but retrieval practice improved retention.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No Crossref match was retrieved. From general knowledge, Roediger and Karpicke 2006 supports the testing-effect claim that rereading can produce greater confidence but poorer later retention than retrieval practice.

### c32 — exists SPLIT · applied ✅  · ⚑ degraded  (line 108)
_less experienced customer-support agents improved most (Brynjolfsson, Li & Raymond 2025)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Brynjolfsson, Li & Raymond 'Generative AI at Work' found less-experienced customer-support agents gained the most, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved lookup did not verify the bibliographic record. From general knowledge, Brynjolfsson, Li, and Raymond's customer-support AI study finds the largest productivity gains for less experienced or lower-skill agents and discusses learning/best-practice transfer.

### c33 — exists SPLIT · applied ✅  · ⚑ degraded  (line 109)
_and so did lower-ability writers (Noy & Zhang 2023)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Noy & Zhang 2023 (Science) on ChatGPT and writing productivity found lower-ability writers benefited most, as claimed.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No matching record was retrieved. From general knowledge, Noy and Zhang 2023 reports that ChatGPT assistance improved writing productivity/quality, with larger gains for lower-ability participants.

### c35 — exists SPLIT · applied ✅  · ⚑ degraded  (line 113)
_robotic surgery, where most residents lost the practice they needed (Beane 2019)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Matt Beane's 2019 ASQ study on robotic surgery and the loss of trainee practice ('shadow learning') is a real, well-known paper supporting this claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup did not match a Beane 2019 work. From general knowledge, Beane's research on robotic surgery and shadow learning supports the claim that robotic systems reduced ordinary practice opportunities for residents.

### c36 — exists SPLIT · applied ✅  · ⚑ degraded  (line 115)
_13% lower employment for 22-to-25-year-olds in the most AI-exposed jobs (Brynjolfsson, Chandar & Chen 2025, working paper)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Brynjolfsson, Chandar & Chen 2025 Stanford working paper on 'Canaries in the Coal Mine' reports ~13% relative employment decline for young workers in AI-exposed occupations.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No matching working-paper record was retrieved. From general knowledge, the cited Brynjolfsson, Chandar, and Chen 2025 working paper is associated with a finding of roughly 13% lower employment for young workers in highly AI-exposed jobs.

### c38 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 118)
_A tutor designed to guide rather than answer removed most of the harm (Bastani et al.'s "GPT Tutor")_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — The retrieved match is irrelevant, but Bastani et al.'s study of a guided 'GPT Tutor' preventing the learning harm of unrestricted AI is a real 2024/2025 working paper.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved Crossref result is a low-similarity, unrelated tutor-time chapter and does not verify the Bastani GPT Tutor work. From general knowledge, Bastani et al.'s GPT Tutor condition was designed to guide rather than merely answer and mitigated much of the learning harm, though 'removed most' is a somewhat compressed phrasing.

### c39 — exists SPLIT · applied ✅  · ⚑ degraded  (line 119)
_a carefully designed AI tutor beat a strong active-learning class (Kestin et al. 2025)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Kestin et al. 2025 (Harvard physics) found an AI tutor outperformed an active-learning class, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No matching Kestin et al. 2025 record was retrieved. From general knowledge, Kestin et al. is associated with an AI-tutor study reporting better outcomes than a strong active-learning comparison, but this is not confirmed by retrieved text.

### c40 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 121)
_Showing people an AI's explanation without its answer, so they had to decide for themselves, produced learning, where answer-plus-explanation did not (Gajos & Mamykina 2022)._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match retrieved; Gajos & Mamykina are real HCI researchers studying AI explanations and decision-making, but I cannot confirm this specific 2022 finding.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No matching Gajos and Mamykina 2022 record was retrieved. From general knowledge, their work supports the claim that withholding the AI's answer while showing an explanation can promote learning more than answer-plus-explanation.

### c41 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 123)
_An AI that asked questions, rather than gave explanations, improved people's own reasoning (Danry et al. 2023)._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match found but reference is sparse (author/year only); Danry et al. 2023 (MIT Media Lab) work on AI that asks questions improving reasoning is plausible, matching my knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved Crossref lookup found no match, which is not decisive evidence of nonexistence. No source text was retrieved to assess the claim about question-asking AI improving reasoning.

### c49 — exists SPLIT · applied ☐  · human ⚠️  (line 154)
_Venue verified: published in PNAS (June 2025, issue 26); earlier versions circulated on SSRN (4895486). **A correction notice exists** (PNAS 122(34), e2518204122, 20 August 2025, per its Crossref record); its content could not be fetched (PNAS refused automated access). Check it before quoting any figure._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=unchecked [no_basis] — The main PNAS paper is confirmed (c46, issue 26); the correction notice (122(34), e2518204122) could not be fetched and is not independently confirmed by retrieved evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The supplied lookup for this correction notice found no Crossref match, and the notice content was not fetched. The claim about the correction notice therefore cannot be evaluated from the provided evidence.

### c55 — exists ⚠️ · applied SPLIT  (line 172)
_Blog figures: 52 software engineers, "mostly junior"; the AI group "averaged 50% on the quiz, compared to 67%"; it finished about two minutes faster, not statistically significant._
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The blog (c52) confirms it is an RCT with developers and a quiz on mastery, but the specific figures (52 engineers, 50% vs 67%, two minutes) are not in the retrieved snippet, so only partially verifiable.
- gpt: exists=nuance applied=unchecked [no_basis] — The related Anthropic blog page exists, but this item lacks standalone bibliographic metadata. The retrieved snippet does not include the specific figures of 52 engineers, 50% versus 67%, or two minutes faster, so the application cannot be checked.

### c56 — exists SPLIT · applied ☐  (line 174)
_Limitations, in the authors' words: "Our sample was relatively small, and our assessment measured comprehension shortly after the coding task."_
- **escalate:** existence: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [no_basis] — The specific limitations quote was not retrieved; the paper exists (c51) but this exact text is not in the available evidence.
- gpt: exists=nuance applied=unchecked [no_basis] — The related Shen and Tamkin arXiv work exists, but this item has no standalone metadata. The retrieved abstract does not contain the quoted limitations language, so the application cannot be assessed from evidence.

### c63 — exists ☐ · applied SPLIT  (line 198)
_A randomised experiment with 117 university students on a writing task: "ChatGPT group outperformed in the essay score improvement but their knowledge gain and transfer were not significantly different". The authors suggest ChatGPT "may promote learners' dependence on technology and potentially trigger 'metacognitive laziness'". That phrase is the authors' interpretation, not a measured outcome. (Published online December 2024.)_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [evidence_text] — This refers to the same Fan et al. study as c62; crossref returned no separate match here but the c62 abstract confirms 117 students, essay improvement without knowledge gain, and the authors' metacognitive laziness interpretation.
- gpt: exists=unchecked applied=unchecked [no_basis] — No bibliographic metadata was supplied and the only lookup returned no match, so existence cannot be judged from the retrieved evidence. No abstract, snippet, or full text was retrieved for this item to assess the application claims.

### c64 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 204)
_Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. _Computers in Human Behavior_, 160, 108386. https://doi.org/10.1016/j.chb.2024.108386 **[abstract, as reproduced on repository pages; full text not read]**_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI and title confirmed via Crossref; no abstract retrieved, but the title itself ('LLMs reduce mental effort but compromise depth') supports the 'less effort, weaker reasoning' note.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, venue, year, volume, and article number, and the DOI URL resolves. The retrieved application text is only a redirect/title-level metadata, not an abstract or source text sufficient to verify the substantive 'less effort, weaker reasoning' use.

### c65 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 208)
_91 university students randomly assigned to ChatGPT-3.5 or Google to research a science question. The ChatGPT group "experienced significantly lower cognitive load" but "demonstrated lower-quality reasoning and argumentation in their final recommendations". The diversity of recommendations did not differ._
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — Claims (91 students, ChatGPT-3.5 vs Google, lower cognitive load, lower-quality reasoning) describe the Stadler et al. study (c64); no abstract retrieved to verify the exact figures, so judged from knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — No bibliographic reference is provided for this item and the lookup returned no match. With no retrieved source text, the detailed participant and outcome claims cannot be checked.

### c89 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 345)
_The 2023 working-paper version (SSRN 4375283, 444 participants) adds: "ChatGPT mostly substitutes for worker effort rather than complementing worker skills" **[abstract]**. That sentence is not in the Science abstract; check the published text before quoting it._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved for the SSRN working-paper version; the author themself flags the quoted sentence as unverified pending the published text.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided, so existence cannot be verified from the supplied lookups. Based on model knowledge only, the SSRN working-paper version is associated with the 444-participant version and the statement that ChatGPT mostly substitutes for worker effort rather than complementing skills.

### c95 — exists ✅ · applied SPLIT  (line 372)
_Brynjolfsson, E., Chandar, B., & Chen, R. (2025, August). Canaries in the coal mine? Six facts about the recent employment effects of artificial intelligence. Stanford Digital Economy Lab / SIEPR working paper. https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial **[abstract: page read, via summary]**_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The SIEPR working paper exists (URL resolves with matching title); the retrieved page is navigation chrome and does not contain the 13% figure, so the specific numeric claim is not confirmed from evidence though it matches the known paper.
- gpt: exists=verified applied=unchecked [no_basis] — The Stanford/SIEPR URL resolves to a page with the matching working-paper title. The retrieved snippet does not include the employment-decline figures or automate-versus-augment claims, so application cannot be judged from the supplied evidence.

### c97 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 389)
_Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. P. Shimamura (Eds.), _Metacognition: Knowing about knowing_ (pp. 185–205). MIT Press. **[record; summaries only]**_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — Open Library returned no match, but Bjork's 1994 chapter in Metcalfe & Shimamura's Metacognition is a real, well-known work that coined 'desirable difficulties'; the claim accurately reflects it.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only retrieved evidence is an Open Library no-match, which is insufficient to verify existence from the supplied evidence. Based on model knowledge only, Bjork's 'desirable difficulties' framing supports the general claim, but the wording here is from secondary summaries and should be checked against the chapter.

### c106 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 463)
_Ellington, A. J. (2003). A meta-analysis of the effects of calculators on students' achievement and attitude levels in precollege mathematics classes. _Journal for Research in Mathematics Education_, 34(5), 433–463. https://doi.org/10.2307/30034795 [record; findings from secondary summaries]. Summaries describe improved operational and problem-solving skills when calculators were part of both teaching and testing. The "neither helped nor hindered" wording often attributed to it comes from her 2000 dissertation; not checked against the 2003 article._
- **escalate:** application: unchecked vs verified
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Ellington 2003 meta-analysis via DOI. No abstract or full text retrieved, and the author explicitly flags the claim as from secondary summaries, so application cannot be verified from evidence.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article metadata and DOI, though only the first page is listed in the retrieved metadata. No source text was retrieved; the application is judged from model knowledge and is consistent with commonly reported findings of the 2003 meta-analysis.

### c116 — exists SPLIT · applied ☐  (line 514)
_Bainbridge 1983 (4.4)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=unchecked [no_basis] — This is an internal cross-reference to the Bainbridge 1983 work (verified in c101) with a section pointer; no distinct claim to assess and no match needed beyond the already-confirmed source.
- gpt: exists=unchecked applied=unchecked [no_basis] — The lookup for this abbreviated cross-reference returned no match, and the record lacks enough bibliographic detail to verify it independently from the retrieved evidence. No application claim is supplied.

### c119 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 530)
_Federal Aviation Administration (2013, 4 January). Safety Alert for Operators (SAFO) 13002: Manual flight operations. https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/airline_operators/airline_safety/SAFO13002.pdf **[secondary: the PDF refused automated access; content from secondary quotation]**. Encourages operators to promote manual flight "when appropriate", citing an increase in manual handling errors in flight operations data; continuous autoflight use is described as not reinforcing manual skills. Quote the PDF itself before the essay does._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The FAA PDF returned HTTP 403 so existence is not decisively verified from evidence; SAFO 13002 on manual flight operations is a real FAA document per my knowledge, and the paraphrase is consistent with it, but the author marks it [secondary].
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The PDF could not be retrieved due to HTTP 403, so existence is unchecked under the not-checkable rule. With no source text available, the application is judged from model knowledge only and matches the known FAA SAFO 13002 content.

### c122 — exists ✅ · applied SPLIT  (line 547)
_Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. _Trends in Cognitive Sciences_, 20(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002 **[abstract]**_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI match confirms the work; abstract matches the definition and framing cited.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm the DOI, title, authors, journal, year, volume/issue, and pages. No specific supported claim was provided for application assessment.

### c128 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 589)
_Secondary reports give 194 students, two weeks, at Harvard, with each student in each condition for one week **[secondary]**. One course, two topics, short term._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Marked [secondary] reporting details of the Kestin Harvard RCT; the ~194 students, Harvard, within-subject design is consistent with public reporting of that study.
- gpt: exists=unchecked applied=unchecked [no_basis] — No identifiable secondary source is specified, and Crossref found no match. With no retrieved text, the claims about 194 Harvard students and study design cannot be assessed.

### c147 — exists SPLIT · applied ☐  (line 722)
_A.1 Supervision is bounded by the supervisor's own skill (the paper's responsibility statement). "The author directed the work, reviewed all content, and verified what is mechanically checkable; the domain-technical legitimacy he cannot personally adjudicate is routed to the named future expert audit." And: "The author takes full responsibility for every claim, number, and citation in this paper. The AI tools are not authors and bear no accountability."_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=unchecked [no_basis] — Same self-authored Zenodo work (same DOI as c146) exists; the retrieved abstract about fiscal legislation is an unrelated crossref mismatch, so the responsibility-statement quote cannot be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence did not resolve the Zenodo DOI and instead produced an unrelated low-similarity SSRN result about a fiscal responsibility bill. Because the relevant source text was not retrieved, the quoted responsibility statement cannot be checked.

### c163 — exists ✅ · applied SPLIT  (line 795)
_Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences, 122(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref DOI match confirms all metadata; abstract supports the finding that unguarded GenAI access can harm learning in high school math.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the DOI, title, authors, journal, volume, issue, and year. No specific claim was provided to assess application.

### c165 — exists ⚠️ · applied SPLIT  (line 797)
_Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., & Gašević, D. (2025). Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance. British Journal of Educational Technology, 56(2), 489–530. https://doi.org/10.1111/bjet.13544 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref DOI match confirms metadata (year differs 2024 vs 2025 online/issue); abstract supports metacognitive laziness / dependence finding.
- gpt: exists=nuance applied=unchecked [no_basis] — Crossref directly verifies the DOI, title, authors, journal, volume, issue, pages, and abstract, but lists the year as 2024 rather than the cited 2025. No specific claim was provided to assess application.

### c166 — exists ✅ · applied SPLIT  (line 798)
_Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., & Maes, P. (2025). Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task. arXiv:2506.08872. https://arxiv.org/abs/2506.08872 [abstract; preprint]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv match confirms paper; abstract confirms 18 completed session 4, matching the small-sample note.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the resolving URL verify the preprint title, authors, arXiv ID, and abstract. No specific claim was provided to assess application.

### c167 — exists ✅ · applied SPLIT  (line 799)
_Lehmann, M., Cornelius, P. B., & Sting, F. J. (2024). AI meets the classroom: When do large language models harm learning? arXiv:2409.09047. https://arxiv.org/abs/2409.09047 [abstract; preprint]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv match confirms paper and metadata; abstract supports substitute-vs-complement usage effects on learning.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the resolving URL verify the preprint title, authors, arXiv ID, and abstract. No specific claim was provided to assess application.

### c168 — exists ✅ · applied SPLIT  (line 800)
_MIT Media Lab. Your brain on ChatGPT (project page). https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/ (accessed 2026-10-19). [abstract: page read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — MIT Media Lab project page fetched and confirms study description including 54 participants, 18 in session 4.
- gpt: exists=verified applied=unchecked [no_basis] — The MIT Media Lab URL resolves to a page titled “Your Brain on ChatGPT” with matching project-page content. No specific claim was provided to assess application.

### c169 — exists ✅ · applied SPLIT  (line 801)
_Shen, J. H., & Tamkin, A. (2026). How AI impacts skill formation. arXiv:2601.20245. https://arxiv.org/abs/2601.20245 [abstract; Anthropic authors; preprint]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv match confirms paper and authors; abstract supports six AI interaction patterns and skill-formation impairment claims.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the resolving URL verify the preprint title, authors, arXiv ID, and abstract. No specific claim was provided to assess application.

### c170 — exists ✅ · applied SPLIT  (line 802)
_Anthropic (2026, 29 January). How AI assistance impacts the formation of coding skills. https://www.anthropic.com/research/AI-assistance-coding-skills [abstract: page read; vendor]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Anthropic page fetched, dated Jan 29, 2026, confirms RCT finding of decreased mastery from AI assistance.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to a page with the cited title and date. No specific claim was provided to assess application.

### c171 — exists ✅ · applied SPLIT  (line 803)
_Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. Computers in Human Behavior, 160, 108386. https://doi.org/10.1016/j.chb.2024.108386 [abstract, as reproduced]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref DOI match confirms title, authors, and metadata; abstract not retrieved (page returned 'Redirecting'), but title directly supports the cited claim.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the DOI, title, authors, journal, volume, year, and article number. No specific claim was provided to assess application.

### c172 — exists ⚠️ · applied SPLIT  (line 804)
_Stanković, M., Hirche, E., Kollatzsch, S., & Doetsch, J. N. (2025). Comment on: Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing tasks. arXiv:2601.00856. https://arxiv.org/abs/2601.00856 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv match confirms the comment paper; abstract confirms critique including limited sample size and methodological concerns.
- gpt: exists=nuance applied=unchecked [no_basis] — arXiv verifies the title, authors, abstract, and arXiv ID, but the cited year 2025 is potentially inconsistent with the 2601 arXiv identifier. No specific claim was provided to assess application.

### c173 — exists ✅ · applied SPLIT  (line 807)
_Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. https://arxiv.org/abs/2507.09089 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv match confirms paper; abstract confirms 16 developers and the 19% slowdown finding.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and the resolving URL verify the preprint title, authors, arXiv ID, and abstract. No specific claim was provided to assess application.

### c174 — exists ✅ · applied SPLIT  (line 808)
_Becker, J., Rush, N., Cunningham, T., Rein, D., & Mahamud, K. (2026, 24 February). We are changing our developer productivity experiment design. METR. https://metr.org/blog/2026-02-24-uplift-update/ [abstract: post read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — METR blog post fetched, dated Feb 24, 2026, confirms the authors and the revised experiment design content.
- gpt: exists=verified applied=unchecked [no_basis] — The METR URL resolves to a page with the cited title, authors, and date. No specific claim was provided to assess application.

### c175 — exists ✅ · applied SPLIT  (line 809)
_Budzyń, K., Romańczyk, M., Kitala, D., Kołodziej, P., Bugajski, M., Adami, H. O., Blom, J., Buszkiewicz, M., Halvorsen, N., Hassan, C., Romańczyk, T., Holme, Ø., Jarus, K., Fielding, S., Kunar, M., Pellise, M., Pilonis, N., Kamiński, M. F., et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. The Lancet Gastroenterology & Hepatology, 10(10), 896–903. https://doi.org/10.1016/S2468-1253(25)00133-5 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the paper; abstract supports the deskilling finding (ADR decline after AI exposure).
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC verify the DOI, title, journal, authors, volume, issue, pages, year, and abstract. No specific claim was provided to assess application.

### c176 — exists ✅ · applied SPLIT  (line 810)
_Lam, K. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy [correspondence]. The Lancet Gastroenterology & Hepatology, 10(12), 1060. https://doi.org/10.1016/S2468-1253(25)00290-0 [record]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the Lam correspondence item, author, volume/issue/page; cited as a record, which the metadata supports.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the correspondence title, author, journal, year, volume, issue, page, and DOI. No specific claim was provided to assess application.

### c177 — exists ✅ · applied SPLIT  (line 811)
_Levartovsky, A., & Kopylov, U. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy [correspondence]. The Lancet Gastroenterology & Hepatology, 10(12), 1060–1061. https://doi.org/10.1016/S2468-1253(25)00289-4 [record]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms Levartovsky & Kopylov correspondence with matching metadata; cited as a record.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the correspondence title, authors, journal, year, volume, issue, pages, and DOI. No specific claim was provided to assess application.

### c178 — exists ✅ · applied SPLIT  (line 812)
_van de Sande, D., Sleijfer, S., Buijsman, S. N. R., Gommers, D., & van Genderen, M. E. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy [correspondence]. The Lancet Gastroenterology & Hepatology, 10(12), 1061–1062. https://doi.org/10.1016/S2468-1253(25)00288-2 [record]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms van de Sande et al. correspondence with matching authors and page range; cited as a record.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the correspondence title, authors, journal, year, volume, issue, pages, and DOI. No specific claim was provided to assess application.

### c179 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 813)
_Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. Harvard Business School Working Paper 24-013. [report] ★_
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [model_knowledge_only] — No evidence retrieved (existence not-checkable); from my knowledge this well-known HBS Working Paper 24-013 exists with these authors and describes the jagged frontier field experiment.
- gpt: exists=unchecked applied=unchecked [no_basis] — The item is marked not-checkable and no retrieved evidence was supplied, so existence cannot be judged under the evidence-only rule. No specific claim or source text was provided to assess application.

### c180 — exists ✅ · applied SPLIT  (line 814)
_Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. Societies, 15(1), 6. https://doi.org/10.3390/soc15010006 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref DOI match confirms metadata; abstract supports the cognitive offloading / critical thinking negative correlation claim.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the DOI, title, author, journal, volume, issue, article number, year, and abstract. No specific claim was provided to assess application.

### c201 — exists ✅ · applied SPLIT  (line 841)
_Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. Human Factors, 52(3), 381–410. https://doi.org/10.1177/0018720810376055 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms exact DOI, authors, journal, volume/issue/pages; abstract matches. No specific claim text provided, but the abstract supports the general topic of complacency/automation bias.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, journal, year, volume/issue, and pages. No application claim was supplied to assess.

### c202 — exists ⚠️ · applied SPLIT  (line 842)
_Plato. Phaedrus. In Plato in Twelve Volumes, Vol. 9, trans. H. N. Fowler (Loeb Classical Library). Harvard University Press; London: William Heinemann, 1925. Perseus Digital Library. https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0174:text=Phaedrus:page=275 [abstract: text read, 275a–b]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Perseus URL resolves to Plato's Phaedrus page 275; the snippet shows the 275a passage about writing producing forgetfulness, consistent with the cited text. Open Library drift is immaterial given the resolving URL.
- gpt: exists=nuance applied=unchecked [no_basis] — The Perseus URL resolves to Plato, Phaedrus page 275 and shows the relevant passage, but the retrieved metadata does not fully confirm the cited 1925 Fowler/Loeb volume details. No application claim was supplied to assess.

### c203 — exists ✅ · applied SPLIT  (line 843)
_Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. Trends in Cognitive Sciences, 20(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the DOI, authors, and venue; abstract matches cognitive offloading topic.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC metadata match the DOI, title, authors, journal, year, volume/issue, and pages. No application claim was supplied to assess.

### c204 — exists ✅ · applied SPLIT  (line 844)
_Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory: Cognitive consequences of having information at our fingertips. Science, 333(6043), 776–778. https://doi.org/10.1126/science.1207745 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms exact DOI, authors, Science 333(6043):776-778; abstract matches the Google-effects finding.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, journal, year, volume/issue, pages, and abstract. No application claim was supplied to assess.

### c205 — exists ✅ · applied SPLIT  (line 847)
_Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1), 1–21. https://doi.org/10.1145/3449287 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms DOI, authors, venue; abstract directly supports cognitive forcing functions reducing overreliance on AI.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, venue, year, volume/issue, pages, and abstract. No application claim was supplied to assess.

### c206 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 848)
_Danry, V., Pataranutaporn, P., Mao, Y., & Maes, P. (2023). Don't just tell me, ask me: AI systems that intelligently frame explanations as questions improve human logical discernment accuracy over causal AI explanations. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (pp. 1–13). ACM. https://doi.org/10.1145/3544548.3580672 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms exact title, authors, venue, DOI; no abstract retrieved, so application assessed from title/known work which matches the cited framing of question-based explanations improving discernment.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, CHI proceedings venue, year, and pages. No application claim was supplied to assess.

### c207 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 849)
_Gajos, K. Z., & Mamykina, L. (2022). Do people engage cognitively with AI? Impact of AI assistance on incidental learning. In Proceedings of the 27th International Conference on Intelligent User Interfaces (IUI '22) (pp. 794–806). ACM. https://doi.org/10.1145/3490099.3511138 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms title, authors, IUI '22 venue, DOI; no abstract retrieved, but the title directly matches the cited topic of AI assistance and incidental learning.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, IUI proceedings venue, year, and pages. No application claim was supplied to assess.

### c208 — exists ✅ · applied SPLIT  (line 850)
_Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. Scientific Reports, 15, 17458. https://doi.org/10.1038/s41598-025-97652-6 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm DOI, authors, Scientific Reports 2025; abstract matches the AI tutoring RCT claim.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, EuropePMC, and the resolved Nature URL confirm the article title, authors, journal, year, volume, DOI, and abstract; the cited article number is not contradicted by the evidence. No application claim was supplied to assess.

### c209 — exists ✅ · applied SPLIT  (line 853)
_Niedner, B. (2026). Auditable adversarial review for AI-in-the-loop decisions: a pre-registered null redirects an AI-deliberation study from better answers to governance by verifiable challenge — an empirical report on SPARRING's Resolver (the Resolver paper). Zenodo. https://doi.org/10.5281/zenodo.21210264. §6.3, responsibility statement. [ours; published]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Zenodo page resolves and confirms title and author (Niedner), a self-citation; snippet confirms the SPARRING Resolver report exists though the specific §6.3 responsibility statement text was not retrieved.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI URL resolves to a Zenodo record with the matching title, author, publication date, version, and file, though Crossref returned 404 and the final Zenodo record URL differs from the DOI suffix. No application claim was supplied to assess.

## ⚠️ AGREE-problem (129)

_Public copy: two entries (c150, c210) are withheld here. Both point to an unpublished record; the counts above include them._

### c01 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 44)
_Nearly a thousand high-school maths students with an unrestricted GPT-4 tutor did better on practice problems (grades up 48%), then did 17% worse than students who never had it once it was taken away (Bastani et al. 2025, PNAS)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match, but a widely-cited 2024/2025 Bastani et al. study on GPT-4 tutors and Turkish high-school students exists (originally a working paper); PNAS venue and exact figures are uncertain. Claim roughly matches that study's finding that unrestricted GPT access boosted practice but hurt later unaided performance.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no matching metadata, so existence is not confirmed from the retrieved evidence. From model knowledge, the Bastani et al. study is commonly reported as finding large practice gains with GPT-4 followed by worse performance when access was removed.

### c02 — exists ☐ · applied ☐  (line 45)
_Developers learning a new programming library with an AI assistant scored lower on a comprehension quiz afterwards (50% against 67%), with no significant time saving (Shen & Tamkin 2026, Anthropic authors, preprint)._
- claude: exists=unchecked applied=unchecked [no_basis] — A 2026 preprint would not yet be reliably indexed; no evidence retrieved and I cannot confirm this specific work or its figures.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match, which is insufficient to confirm or disprove a preprint. No source text or reliable model-knowledge basis is available to assess the claimed quiz and time-saving results.

### c03 — exists ☐ · applied ☐  (line 48)
_Students who used a model to produce solutions covered more topics but understood each less; those who asked it for explanations understood more (Lehmann, Cornelius & Sting 2024, preprint)._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved; cannot confirm this preprint or its claims from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, and no preprint text or metadata was retrieved. The application claim cannot be assessed from the provided evidence.

### c04 — exists ☐ · applied ✅  · ⚑ degraded  (line 53)
_The mechanism is old and well established: what you generate, retrieve and struggle with, you keep (Bjork 1994; Slamecka & Graf 1978; Bertsch et al. 2007; Roediger & Karpicke 2006)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Grouped citation; no evidence retrieved, but the generation, retrieval-practice and desirable-difficulties effects cited are well-established findings matching these classic authors.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — This is a grouped citation rather than a single bibliographic work, and the lookup did not retrieve matching metadata. From model knowledge, the cited literature on generation, retrieval practice, and desirable difficulties broadly supports the claim that effortful generation/retrieval aids retention.

### c05 — exists ☐ · applied ☐  (line 53)
_Bjork 1994_
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved; Bjork's 1994 work on desirable difficulties is well known to me but cannot be confirmed from evidence here, and no specific claim is attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Bjork 1994 reference, so existence is not verified from the evidence. No claim was attached to this sub-citation record.

### c06 — exists ☐ · applied ☐  (line 53)
_Slamecka & Graf 1978_
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved; Slamecka & Graf's 1978 generation-effect paper is a real classic but unconfirmed here, and no claim is attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Slamecka & Graf 1978 reference, so existence is not verified from the evidence. No claim was attached to this sub-citation record.

### c07 — exists ☐ · applied ☐  (line 53)
_Bertsch et al. 2007_
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved; cannot confirm this work, and no claim is attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Bertsch et al. 2007 reference, so existence is not verified from the evidence. No claim was attached to this sub-citation record.

### c08 — exists ☐ · applied ☐  (line 53)
_Roediger & Karpicke 2006_
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved; Roediger & Karpicke's 2006 testing-effect work is well known to me but unconfirmed here, and no claim is attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Roediger & Karpicke 2006 reference, so existence is not verified from the evidence. No claim was attached to this sub-citation record.

### c09 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 57)
_Experienced endoscopists' detection rate on colonoscopies done *without* AI fell from 28.4% to 22.4% in the three months after AI was introduced at their centres (Budzyń et al. 2025; observational, contested)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No Crossref match, but a 2025 Lancet Gastroenterology & Hepatology study (Budzyń et al.) reported a drop in non-AI colonoscopy adenoma detection after AI exposure, consistent with the claim; venue and exact figures unconfirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a Crossref no-match, so existence is not confirmed from the lookup. From model knowledge, the Budzyń et al. observational report is described as finding a drop in non-AI adenoma detection from about 28.4% to 22.4% after AI introduction.

### c10 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 59)
_Airline pilots kept their hand-flying skills under automation but showed problems with the *thinking* tasks of manual flight, linked to how often their minds wandered while the automation flew (Casner et al. 2014, 16 pilots)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved, but Casner et al. published work around 2014 on pilots' manual flying and cognitive skills under automation; the specific framing is plausible but not confirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no matching metadata, so the work is not verified from the retrieved evidence. From model knowledge, Casner and colleagues’ work on airline-pilot automation is consistent with preserved manual control but weakened cognitive/manual-flight management associated with automation and mind-wandering.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 62)
_Bainbridge's 1983 "Ironies of automation" said it first: skills "deteriorate when they are not used", and an operator's working knowledge "develops only through use and feedback about its effectiveness"._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Bainbridge, 'Ironies of automation', Automatica 1983. The quoted themes about skill deterioration and knowledge developing through use match this well-known paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Lisanne Bainbridge’s 1983 article “Ironies of automation” in Automatica, 19(6), 775–779, DOI 10.1016/0005-1098(83)90046-8. Although no source text was retrieved, from model knowledge the quoted claim matches the paper’s argument about unused operator skills and knowledge developing through use and feedback.

### c12 — exists ☐ · applied ☐  (line 66)
_A fairer Part 1: handing over a task costs you the skill where the doing was how you learned it, or how you kept it. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — the authors' own framing, not an external citation, so neither axis is assessable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The note marks this as the authors’ own framing rather than an external bibliographic work, and Crossref returned no match. There is no external source text to assess application.

### c13 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 71)
_In a survey of 319 knowledge workers (936 examples), higher confidence in AI went with less critical thinking, and higher confidence in oneself with more. The thinking that remained moved toward checking, combining and overseeing the AI's output (Lee et al. 2025, Microsoft Research authors; self-report)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved, but Lee et al. (Microsoft Research) published a 2025 CHI study of 319 knowledge workers on GenAI and critical thinking matching these figures and findings; venue unconfirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no matching metadata, so existence is not verified from the retrieved evidence. From model knowledge, the Microsoft Research Lee et al. 2025 survey of 319 knowledge workers and 936 examples reported lower critical-thinking effort with greater AI confidence, higher effort with self-confidence, and a shift toward verification/integration/oversight.

### c14 — exists ☐ · applied ☐  (line 73)
_Students researching with ChatGPT reported less mental effort and produced weaker reasoning than students using Google (Stadler, Bannert & Sailer 2024)._
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved; cannot confirm this 2024 work or its specific comparison of ChatGPT vs Google users from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no matching metadata for the sparse Stadler, Bannert & Sailer 2024 reference. No source text or sufficient independent basis is available to judge whether it supports the claimed ChatGPT-versus-Google result.

### c16 — exists ☐ · applied ☐  (line 78)
_a published comment raises concerns about its sample, its EEG analysis and its reporting (Stanković et al. 2025)_
- claude: exists=unchecked applied=unchecked [no_basis] — No evidence retrieved; cannot confirm this published comment or its critique from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Stanković et al. 2025 reference. No comment text or abstract was retrieved, so the claim about its criticisms cannot be assessed.

### c17 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 79)
_The correlational survey often cited beside it (Gerlich 2025) cannot show cause._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved, but a Gerlich 2025 correlational survey on AI tools and critical thinking exists; the claim that correlational data cannot show cause is a valid characterization.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a Crossref no-match, so existence is not confirmed from the lookup. From model knowledge, the Gerlich 2025 work cited in this context is a correlational/self-report survey, so the statement that it cannot establish causation is supported.

### c18 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 81)
_Calculators used alongside ordinary teaching did not harm basic skills at most grades, but sustained use in Grade 4, while those skills were being formed, did (Hembree & Dessart 1986, 79 studies)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved, but Hembree & Dessart's 1986 meta-analysis of calculator effects (reviewing ~79 studies) is well established and matches the claim's nuance about Grade 4.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match for the sparse Hembree & Dessart 1986 reference. From model knowledge, their calculator meta-analysis generally found no broad harm to basic skills and did report grade-level qualifications, but the specific “sustained use in Grade 4 while skills were being formed” wording is an interpretive compression.

### c19 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 84)
_Heavier GPS users have worse spatial memory, and in a small three-year follow-up their memory declined faster (Dahmani & Bohbot 2020)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No match retrieved, but Dahmani & Bohbot published 2020 work linking GPS use to worse spatial memory; the three-year follow-up detail is plausible but unconfirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no matching metadata, so existence is not verified from the retrieved evidence. From model knowledge, Dahmani & Bohbot 2020 reported associations between habitual GPS use and poorer spatial memory, including a small longitudinal follow-up showing greater decline.

### c20 — exists ☐ · applied ✅  · ⚑ degraded  (line 85)
_London taxi drivers who navigated from memory had larger posterior hippocampi (Maguire et al. 2000)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No match retrieved, but Maguire et al. 2000 (PNAS) on London taxi drivers' enlarged posterior hippocampi is a famous, well-documented study matching the claim precisely.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match for the sparse Maguire et al. 2000 reference, so existence is not verified from the evidence. From model knowledge, Maguire et al. 2000 reported larger posterior hippocampi in London taxi drivers compared with controls.

### c24 — exists ⚠️ · applied ✅  · ⚑ degraded  (line 89)
_Plato's Socrates made the same complaint about writing: "this invention will produce forgetfulness in the minds of those who learn to use it" (Phaedrus 275a, Fowler translation)._
- claude: exists=verified applied=verified [model_knowledge_only] — Plato's Phaedrus exists; the Theuth/Thamus passage at 275a does make this complaint about writing producing forgetfulness, consistent with Fowler's translation.
- gpt: exists=nuance applied=verified [model_knowledge_only] — The Open Library metadata confirms a work titled Phaedrus associated with Plato, though the matched metadata is for a Jowett edition rather than the cited Fowler translation. From general knowledge, Phaedrus 275a contains the quoted complaint that writing will produce forgetfulness.

### c25 — exists ☐ · applied ☐  (line 92)
_The pattern: a tool costs the specific skill it replaces, most when it replaces the practice that forms the skill. Panics about general decline have tended to overreach. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' own synthesis, not a cited external work.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own synthesis rather than a specific external work, and no bibliographic match was retrieved. There is no source text or identifiable cited work against which to check the application.

### c26 — exists ☐ · applied ☐  (line 94)
_Where AI differs from the older tools, and from a colleague. [ours, from the sources cited]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' own synthesis, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own synthesis from other sources, and no specific work was retrieved. The claim cannot be checked as an application of this empty citation.

### c28 — exists ☐ · applied ☐  · ⚑ degraded  (line 100)
_Shen & Tamkin frame skill loss as a threat to "the skills required to effectively supervise AI"._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match retrieved; Tamkin is a known AI-safety author but I cannot confirm this specific Shen & Tamkin framing.
- gpt: exists=unchecked applied=unchecked [no_basis] — No matching Shen and Tamkin source was retrieved. Without source text, the quoted framing about skills required to supervise AI cannot be checked.

### c34 — exists ☐ · applied ☐  · ⚑ degraded  (line 111)
_Lehmann et al. found AI widened the gap between students with more and less prior knowledge._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match retrieved and I cannot confirm this specific Lehmann et al. finding on AI widening prior-knowledge gaps.
- gpt: exists=unchecked applied=unchecked [no_basis] — No Lehmann et al. source was retrieved. Without source text or a clear bibliographic record, the claim that AI widened the prior-knowledge gap cannot be checked.

### c37 — exists ☐ · applied ☐  (line 115)
_For AI's effect on how juniors develop, I found no direct evidence; it is still a forecast._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author explicitly notes absence of evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Per instruction, both axes are unchecked.

### c42 — exists ☐ · applied ✅  · ⚑ degraded  (line 125)
_Forcing people to think before seeing the AI's answer reduced over-reliance, though they liked it least (Buçinca, Malaya & Gajos 2021)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match but Buçinca, Malaya & Gajos 2021 (CSCW, cognitive forcing functions reduce over-reliance, least preferred) is a real paper I recognize, and the claim matches its findings.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The provided lookup found no Crossref match, so existence cannot be verified from the retrieved evidence. From model knowledge, this appears to refer to Buçinca, Malaya, and Gajos on cognitive forcing functions reducing overreliance, including lower user preference, but no retrieved text was available.

### c44 — exists ☐ · applied ☐  · ⚑ degraded  (line 131)
_The longest AI-specific follow-up found is four months (Kosmyna et al., small and unreviewed)_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match found; Kosmyna et al. (MIT 'Your Brain on ChatGPT') is a known preprint with a four-month follow-up framing, but I cannot verify the specific claim from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Crossref lookup found no match, and no other metadata or source text was retrieved. The broad claim that the longest AI-specific follow-up found is four months cannot be evaluated from the provided evidence.

### c45 — exists ☐ · applied ☐  (line 133)
_I found no study of what years of everyday AI use does to a working professional's skills._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited; author explicitly notes absence of evidence, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c47 — exists ⚠️ · applied ✅  (line 146)
_"We study this question via a field experiment where we provide nearly a thousand high school math students with access to generative AI tutors." Two tutors: one "that mimics a standard ChatGPT interface ('GPT Base')" and one "with prompts designed to safeguard learning ('GPT Tutor')"._
- claude: exists=verified applied=verified [evidence_text] — These are direct quotes from the Bastani et al. abstract (c46), which confirms nearly a thousand students and the two tutors (GPT Base, GPT Tutor).
- gpt: exists=nuance applied=verified [evidence_text] — The item itself lacks bibliographic metadata and its own lookup failed, but the quoted text is directly present in the verified Bastani et al. PNAS abstract. The abstract exactly supports the claims about nearly a thousand students and the two tutor designs.

### c48 — exists ⚠️ · applied ✅  (line 150)
_With access: "48% improvement in grades for GPT Base and 127% for GPT Tutor". After access was removed: "students actually perform worse than those who never had access (17% reduction in grades for GPT Base)". "These negative learning effects are largely mitigated by the safeguards in GPT Tutor." Students "attempt to use GPT-4 as a 'crutch'"._
- claude: exists=verified applied=verified [evidence_text] — All quoted figures (48%, 127%, 17% reduction, crutch, mitigation by GPT Tutor) appear verbatim in the Bastani et al. abstract (c46).
- gpt: exists=nuance applied=verified [evidence_text] — The item itself has no complete reference and its own lookup failed, but the figures and wording are directly from the verified Bastani et al. PNAS abstract. The abstract supports the 48%, 127%, 17% reduction, mitigation by GPT Tutor, and “crutch” claims.

### c50 — exists ☐ · applied ☐  (line 158)
_Bearing: the cleanest evidence for "the doing was the learning". Same students, same problems. An unrestricted assistant improved practice and harmed learning; a tutor built to make them do the work did not. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; this is the authors' own interpretation (marked [ours]), not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and as the authors’ own interpretation. Both axes are therefore unchecked.

### c53 — exists ⚠️ · applied ✅  (line 167)
_"We find that AI use impairs conceptual understanding, code reading, and debugging abilities, without delivering significant efficiency gains on average. Participants who fully delegated coding tasks showed some productivity improvements, but at the cost of learning the library."_
- claude: exists=verified applied=verified [evidence_text] — These quotes match the Shen & Tamkin abstract (c51) verbatim regarding impaired understanding and delegation effects.
- gpt: exists=nuance applied=verified [evidence_text] — This item has no standalone bibliographic metadata, but the quoted claims are exactly present in the verified Shen and Tamkin arXiv abstract. The abstract supports both the impairment claim and the delegation/productivity-learning tradeoff claim.

### c54 — exists ⚠️ · applied ✅  (line 170)
_The abstract's framing: "how this assistance affects the development of skills required to effectively supervise AI remains unclear"._
- claude: exists=verified applied=verified [evidence_text] — The quoted framing about skills required to supervise AI appears verbatim in the Shen & Tamkin abstract (c51).
- gpt: exists=nuance applied=verified [evidence_text] — This item lacks its own checkable reference, but the quoted framing is present in the verified Shen and Tamkin arXiv abstract. The abstract directly supports the claim about uncertainty over skill development needed to supervise AI.

### c57 — exists ☐ · applied ☐  (line 176)
_Anthropic makes Claude, which helped draft this brief. A study by an AI company finding a cost of its own product cuts against its commercial interest, which counts somewhat in its favour; it is still a preprint. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; this is the authors' own disclosure note (marked [ours]), not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and as the authors’ own note. Both axes are therefore unchecked.

### c59 — exists ⚠️ · applied ✅  (line 183)
_"In two pre-registered and incentivized laboratory experiments, we find no effect of LLMs on overall learning outcomes." In exploratory analyses and a field study: "Students who substitute some of their learning activities with LLMs (e.g., by generating solutions to exercises) increase the volume of topics they can learn about but decrease their understanding of each topic. Students who complement their learning activities with LLMs (e.g., by asking for explanations) do not increase topic volume but do increase their understanding." Also: "LLMs widen the gap between students with low and high prior knowledge."_
- claude: exists=verified applied=verified [evidence_text] — All quotes (null overall effect, substitute vs complement behaviors, widening gap) match the Lehmann et al. abstract (c58) verbatim.
- gpt: exists=nuance applied=verified [evidence_text] — This item lacks standalone bibliographic metadata, but its quoted claims are directly present in the verified Lehmann, Cornelius, and Sting arXiv abstract. The abstract supports the null overall result, substitution/complement findings, and widening-gap claim.

### c60 — exists ⚠️ · applied ✅  (line 190)
_Preprint; the usage-pattern findings are exploratory, and the pre-registered result is a null._
- claude: exists=verified applied=verified [evidence_text] — The abstract (c58) confirms it is a preprint with exploratory usage-pattern analyses and a null pre-registered result, supporting the caveat.
- gpt: exists=nuance applied=verified [evidence_text] — This item has no standalone metadata, but it clearly refers to the verified Lehmann, Cornelius, and Sting arXiv preprint. The abstract supports that the pre-registered lab result is null and that the usage-pattern findings come from exploratory analyses and a field study.

### c61 — exists ☐ · applied ☐  (line 191)
_Bearing: the overall effect can be zero while the effect of *how* someone uses it is not. That matches Part 3 of the claim, choosing which parts to hand over. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own interpretation; is_citation=false. Both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an authors' own interpretation, so both axes are treated as intentionally uncited/unchecked.

### c62 — exists ⚠️ · applied ⚠️  (line 194)
_Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., & Gašević, D. (2025). Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance. _British Journal of Educational Technology_, 56(2), 489–530. https://doi.org/10.1111/bjet.13544 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to matching work; abstract confirms 'better essays, no more learning' (essay improvement but no knowledge gain) and the metacognitive laziness framing.
- gpt: exists=nuance applied=nuance [evidence_text] — The DOI, title, authors, journal, volume, issue, and pages match, though Crossref lists year 2024 while the reference uses the 2025 issue year. The abstract supports better essay-score improvement and no significant knowledge gain/transfer, but the shorthand 'no more learning' overstates a null finding.

### c66 — exists ☐ · applied ☐  (line 212)
_A short task (about 20 minutes, per press coverage **[secondary]**)._
- claude: exists=unchecked applied=unchecked [no_basis] — A secondary press-coverage detail (~20 min task) with no retrieved source; cannot verify the duration figure.
- gpt: exists=unchecked applied=unchecked [no_basis] — The item cites unspecified secondary press coverage and the lookup returned no match. No retrieved evidence supports the approximately 20-minute task-duration claim.

### c68 — exists ☐ · applied ☐  (line 225)
_The project page says "it has not yet been peer-reviewed, thus all the conclusions are to be treated with caution and as preliminary" (MIT Media Lab project page [abstract: page read]). The same page asks: "Please do not use the words like 'stupid', 'dumb', 'brain rot', 'harm', 'damage'", and to avoid "LLMs make you stop thinking"._
- claude: exists=unchecked applied=unchecked [no_basis] — Existence not-checkable and no page text retrieved; cannot verify the quoted project-page language, though it is consistent with the known MIT Media Lab 'Your Brain on ChatGPT' page.
- gpt: exists=unchecked applied=unchecked [no_basis] — The existence status is not-checkable and no page text or URL evidence was retrieved. Therefore the quoted MIT Media Lab page claims cannot be verified from the supplied evidence.

### c69 — exists ⚠️ · applied ✅  (line 229)
_Critique: Stanković, M., Hirche, E., Kollatzsch, S., & Doetsch, J. N. (2025). Comment on: Your brain on ChatGPT. arXiv:2601.00856. https://arxiv.org/abs/2601.00856 [abstract]. Concerns about "(i) study design considerations, including the limited sample size; (ii) the reproducibility of the analyses; (iii) methodological issues related to the EEG analysis; (iv) inconsistencies in the reporting of results; and (v) limited transparency". It also praises the dataset and asks for more conservative interpretation._
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to matching comment paper; abstract lists exactly the five concerns quoted and praises the dataset while urging more conservative interpretation.
- gpt: exists=nuance applied=verified [evidence_text] — The arXiv ID and URL resolve to the cited comment with matching authors and title, but the citation year 2025 is caveated by the 2601 arXiv identifier. The abstract directly lists the praised dataset/pipelines, call for more conservative interpretation, and the five categories of concern.

### c70 — exists ☐ · applied ☐  (line 235)
_Bearing: suggestive, and the press coverage outran it. Lower brain connectivity while a tool does part of the task is what you would expect whether or not anything is lost. The finding that bears on skill is the session-4 result, with 18 people. Do not lean on it. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own assessment; is_citation=false. Both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an authors' own assessment, so both axes are treated as intentionally uncited/unchecked.

### c72 — exists ☐ · applied ☐  (line 252)
_That 19 experienced endoscopists took part comes from press coverage [secondary], not the abstract._
- claude: exists=unchecked applied=unchecked [no_basis] — Secondary press figure (19 endoscopists) not in the retrieved abstract and no source retrieved; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited support is unspecified secondary press coverage and the lookup returned no match. No retrieved evidence establishes that 19 experienced endoscopists participated.

### c73 — exists ☐ · applied ☐  (line 254)
_Contested. Three letters in the December 2025 issue respond to it (Lam 2025; Levartovsky & Kopylov 2025; van de Sande et al. 2025) [record: content not read]._
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the three response letters and content was not read; cannot verify their existence or content.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is incomplete and the lookup returned no match for the alleged three letters. No retrieved record or content verifies that the December 2025 issue contained those responses.

### c74 — exists ☐ · applied ☐  (line 255)
_Secondary summaries say critics point to differences between the before and after patient groups, unreported withdrawal times, the small number of endoscopists, and secondary outcomes that did not fall [secondary]._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [secondary]; drawn from secondary summaries with no retrieved source to verify the critics' specific points.
- gpt: exists=unchecked applied=unchecked [no_basis] — The item relies on unspecified secondary summaries and the lookup returned no match. No retrieved evidence supports the stated criticisms.

### c75 — exists ☐ · applied ☐  (line 259)
_Bearing: the best real-world evidence found that AI can erode an expert's existing skill, and fast (three months). But it is one observational study of one task, it measures performance without AI rather than skill directly, and the effect could be lowered effort or attention rather than lost skill. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own assessment; is_citation=false. Both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an authors' own assessment, so both axes are treated as intentionally uncited/unchecked.

### c76 — exists ✅ · applied ✅  · ⚑ degraded  (line 264)
_Lee, H.-P. (H.), Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In _Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems_ (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778 [abstract; Microsoft Research authors]_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI, title, authors, and CHI 2025 venue confirmed via Crossref; no abstract retrieved, but the claims (319 workers, 936 examples, confidence effects, shift toward verification/stewardship) match the well-known Lee et al. study.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, venue, year, pages, and publisher metadata. No abstract or full text was retrieved, but from model knowledge the listed claims match the paper's reported survey design, 319 workers, 936 examples, confidence effects, and shift toward verification/integration/stewardship.

### c77 — exists ☐ · applied ☐  (line 276)
_Bearing: the thinking does not vanish, it moves to checking and overseeing. Whether checking is done well depends on the skill underneath (Q5.6). [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own assessment; is_citation=false. Both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an authors' own assessment, so both axes are treated as intentionally uncited/unchecked.

### c79 — exists ☐ · applied ☐  (line 285)
_A survey with interviews. It cannot tell whether AI use lowers critical thinking or whether people who think less critically use AI more. Age is tangled with both. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own assessment; is_citation=false. Both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an authors' own assessment, so both axes are treated as intentionally uncited/unchecked.

### c81 — exists ✅ · applied ⚠️  (line 295)
_Follow-up: METR (Becker, J., Rush, N., Cunningham, T., Rein, D., & Mahamud, K.) (2026, 24 February). We are changing our developer productivity experiment design. https://metr.org/blog/2026-02-24-uplift-update/ **[abstract: post read]**._
- claude: exists=verified applied=nuance [evidence_text] — Post exists and confirms the design change and participant non-participation bias. The specific -18%/-4% figures are not in the retrieved snippet, so the numeric claim is partly unverified from evidence.
- gpt: exists=verified applied=nuance [evidence_text] — The METR page resolves with matching title, authors, and date. The snippet supports the design-change rationale and nonparticipation due to not wanting to work without AI, but it does not show the exact speedup estimates or the exact 'bad proxy' wording.

### c82 — exists ☐ · applied ☐  (line 302)
_Bearing: this is about speed, not skill. It bears on skill in two ways. People's sense of how AI is affecting their work was wrong by a wide margin, so felt effects are not a safe guide. And developers declining to work without AI is itself a sign of dependence, whatever else it means. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — This is the authors' own bearing note, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is an authors' own bearing note rather than a citation, so both axes are intentionally left unchecked.

### c83 — exists ☐ · applied ✅  · ⚑ degraded  (line 307)
_Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. Harvard Business School Working Paper 24-013. **[report]** (cite-checked 2026-10-17 for brief 6; in essay 01)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Existence not checkable from evidence; this is the well-known Dell'Acqua et al. HBS working paper on the jagged frontier, and the 758 consultants and 19-point drop figures match its findings.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided, so existence cannot be verified under the evidence-only rule. Based on model knowledge only, the cited HBS working paper is commonly reported as involving 758 consultants, improved performance inside the AI frontier, and a 19 percentage-point accuracy drop outside it.

### c84 — exists ☐ · applied ☐  (line 314)
_Bearing: a skill-loss question in disguise. If you keep the skill, you can spot when the task is outside the AI's abilities; if you lose it, you cannot. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own bearing note, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is an authors' own bearing note rather than a citation, so both axes are intentionally left unchecked.

### c85 — exists ☐ · applied ☐  (line 317)
_The longest AI-specific follow-up found is Kosmyna et al.'s four months (1.6), with 18 people in the decisive session. Budzyń et al. compare three months either side (2.1). Bastani et al. (1.1) measure within a school term; Shen & Tamkin (1.2) minutes after the task. **I found no multi-year study of AI use and professional skill.** The one multi-year result in this brief is about GPS (5.3)._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited cross-reference note asserting absence of a multi-year study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and states a search limitation rather than citing a work, so both axes are intentionally left unchecked.

### c87 — exists ☐ · applied ☐  (line 336)
_Bearing: the strongest evidence *against* a simple "AI stops novices learning" story, in a setting where the AI suggested responses built from what top agents did. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own bearing note, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is an authors' own bearing note rather than a citation, so both axes are intentionally left unchecked.

### c88 — exists ✅ · applied ⚠️  (line 339)
_Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. _Science_, 381(6654), 187–192. https://doi.org/10.1126/science.adh2586 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves with matching metadata; abstract confirms 453 professionals, 40% time reduction, 18% quality gain, and decreased inequality.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref metadata matches the Science article and DOI. The abstract directly supports the 453 participants, preregistration, 40% time decrease, 18% quality increase, and reduced inequality, but the editor-summary wording about weaker-skilled participants benefiting most is not present in the retrieved abstract.

### c90 — exists ☐ · applied ☐  (line 348)
_Bearing: a single session measures output, not learning. "Substitutes for effort" is exactly the condition under which, on Q4's account, less is learned. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own bearing note, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is an authors' own bearing note rather than a citation, so both axes are intentionally left unchecked.

### c91 — exists ☐ · applied ☐  (line 351)
_Lehmann et al. 2024 (1.3): "LLMs widen the gap between students with low and high prior knowledge."_
- claude: exists=unchecked applied=unchecked [no_basis] — Cross-reference to entry 1.3 with no title or DOI; Crossref returned no match, so neither existence nor the quoted claim can be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match for an incomplete reference, which is insufficient to prove nonexistence. No source text was retrieved to assess the quoted claim.

### c92 — exists ☐ · applied ☐  (line 352)
_Shen & Tamkin 2026 (1.2) frame their study around novices "who rely heavily on AI to complete unfamiliar tasks"._
- claude: exists=unchecked applied=unchecked [no_basis] — Cross-reference to entry 1.2 with no title or DOI; Crossref returned no match, so cannot verify existence or the quoted framing.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match for an incomplete reference, which is insufficient to prove nonexistence. No source text was retrieved to assess the claim about the study framing.

### c93 — exists ☐ · applied ☐  (line 354)
_Bearing, with 3.1 and 3.2: novices gain most *in output*, while the learning evidence is mixed, and some of it points the other way. Both can be true: the novice's output looks like an expert's while the novice learns less. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own bearing note, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is an authors' own bearing note rather than a citation, so both axes are intentionally left unchecked.

### c96 — exists ☐ · applied ☐  (line 384)
_I found no study measuring how juniors who started their careers with AI develop compared with those who did not._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited note asserting an absence of research.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and reports an absence of found studies rather than citing a work, so both axes are intentionally left unchecked.

### c98 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 397)
_Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. _Journal of Experimental Psychology: Human Learning and Memory_, 4(6), 592–604. https://doi.org/10.1037/0278-7393.4.6.592 **[record]**_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves with matching metadata confirming the foundational generation-effect paper; the bearing note's read/generate analogy is apt though no abstract was retrieved to detail the generate-vs-read contrast.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref metadata verifies the article, DOI, journal, year, volume, issue, and pages. No abstract/source text was retrieved; based on model knowledge, the read-versus-generate analogy is plausible but is an application of the generation-effect paradigm to AI use rather than a directly evidenced claim.

### c101 — exists ✅ · applied ✅  · ⚑ degraded  (line 417)
_Bainbridge, L. (1983). Ironies of automation. _Automatica_, 19(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8 **[abstract; text read]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to the correct Bainbridge 1983 Automatica article. The retrieved URL text was only 'Redirecting', so the specific quotes are judged from knowledge of this well-known paper, which does contain these arguments.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article metadata and DOI. The retrieved page text did not contain the quoted passages, but the application matches the well-known content of Bainbridge's article based on model knowledge only.

### c102 — exists ☐ · applied ☐  (line 437)
_What Q4 supports. [ours]
- "The doing was the learning" has a well-tested mechanism: generating, retrieving and struggling build durable skill, and receiving the answer does not.
- It also says something the claim leaves out: the doing is often the upkeep. Retrieval depends on frequency of use (4.4), which is why already-learned skills can fade (2.1, 5.5)._
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own synthesis rather than a citation. Both axes are therefore unchecked.

### c103 — exists ✅ · applied ⚠️  (line 445)
_Plato. _Phaedrus_ 274c–275b. In _Plato in Twelve Volumes_, Vol. 9, trans. H. N. Fowler (Loeb Classical Library). Harvard University Press; London: William Heinemann, 1925. Perseus Digital Library, https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0174:text=Phaedrus:page=275 [abstract: text read at 275a–b on Perseus]_
- claude: exists=verified applied=verified [evidence_text] — Perseus page resolves to Phaedrus 275 and the fetched text contains the 'forgetfulness in the minds of those who learn' passage, supporting the Thamus/Theuth quotes.
- gpt: exists=verified applied=nuance [evidence_text] — The Perseus URL resolves to Plato's Phaedrus page 275, confirming the cited work/location. The retrieved snippet directly confirms the forgetfulness passage, but the evidence provided is truncated before fully showing the 'elixir/reminding' and 'appearance of wisdom' wording.

### c104 — exists ☐ · applied ☐  (line 452)
_Bearing: the oldest version of this essay's worry. It was partly right (people stopped memorising long texts) and largely outweighed (writing made most later knowledge possible). Its "appearance of wisdom" is the novice-output point in 3.3. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own interpretation [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own interpretation rather than a citation. Both axes are therefore unchecked.

### c105 — exists ✅ · applied ✅  · ⚑ degraded  (line 457)
_Hembree, R., & Dessart, D. J. (1986). Effects of hand-held calculators in precollege mathematics education: A meta-analysis. _Journal for Research in Mathematics Education_, 17(2), 83–99. https://doi.org/10.2307/749255 [abstract]. 79 reports._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Hembree & Dessart 1986 meta-analysis via DOI. No abstract retrieved, but the Grade 4 and basic-skills claims match this well-known meta-analysis per my knowledge.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article title, authors, journal, year, and DOI, though the page range is incomplete in the metadata. No abstract/source text was retrieved, but the stated 79-report meta-analysis and grade-specific calculator findings match the article based on model knowledge only.

### c107 — exists ☐ · applied ☐  (line 469)
_Bearing: the calculator debate's evidence lines up with Part 1. Used alongside teaching, no harm; used sustainedly at the age the skill is being formed, harm. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own synthesis rather than a citation. Both axes are therefore unchecked.

### c110 — exists ☐ · applied ☐  (line 486)
_Bearing: the clearest non-AI case of a tool taking over a skill and the skill (and the brain region that supports it) responding to use. Many people would call the trade worth it. That is Part 3's question answered for one skill. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own synthesis rather than a citation. Both axes are therefore unchecked.

### c112 — exists ✅ · applied ⚠️  (line 496)
_Camerer, C. F., Dreber, A., Holzmeister, F., Ho, T.-H., Huber, J., Johannesson, M., et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. _Nature Human Behaviour_, 2, 637–644. https://doi.org/10.1038/s41562-018-0399-z [abstract]. 21 studies replicated; 13 (62%) found a significant effect in the same direction. That Sparrow et al.'s Stroop experiment (the "computer words after hard questions" result) was among the failures is from secondary sources and from Hesselmann [secondary]._
- claude: exists=verified applied=verified [evidence_text] — DOI and EuropePMC confirm the paper, and the abstract states exactly 21 studies with 13 (62%) significant in the same direction. The Stroop-specific failure claim is flagged [secondary] and not in this abstract.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and EuropePMC verify the article, and the abstract directly supports the claim that 21 studies were replicated and 13, or 62%, showed a significant effect in the same direction. The evidence provided does not identify Sparrow et al.'s Stroop experiment as one of the failures, so that part is only indirectly/externally supported.

### c114 — exists ☐ · applied ☐  (line 507)
_Caution: the replications tested the Stroop experiment, not the memory experiments (expecting future access lowers recall). Those were not checked here. Do not say "the Google effect was debunked"; say "its best-known experiment did not replicate". [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author caution [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own caution rather than a citation. Both axes are therefore unchecked.

### c115 — exists ☐ · applied ☐  (line 510)
_Bearing: a reminder that a vivid "technology is rotting memory" finding can fail to hold. The same caution applies to 1.6. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours]; is_citation=false, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own synthesis rather than a citation. Both axes are therefore unchecked.

### c121 — exists ☐ · applied ☐  (line 542)
_Bearing: aviation is the long-running human precedent for this essay, and its response was deliberate practice of the manual skill (SAFO 13002), not abandoning automation. Casner's finding that thinking skills faded more than hand skills, and faded most when attention wandered, is the closest pre-AI match to AI's case, since AI takes over thinking. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c124 — exists ☐ · applied ☐  (line 554)
_Bearing: offloading is ordinary and mostly sensible. The question is never whether to offload, but what it costs in each case. That is Part 2's framing, and it has a research literature behind it. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own framing marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c125 — exists ☐ · applied ☐  (line 558)
_**Where the analogy holds, and where AI differs.** **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own section header marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c126 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 579)
_Bastani et al. 2025 (1.1): the "GPT Tutor" with prompts "designed to safeguard learning" largely removed the harm while still raising practice grades._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref found no match but this is a back-reference to section 1.1; Bastani et al. 2025 is a real working paper on GPT tutors whose safeguarded-tutor condition mitigated harm, consistent with the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved Crossref lookup found no match for the incomplete Bastani et al. 2025 reference, which is not decisive enough to refute existence. From model knowledge only, the claim is broadly consistent with reports of a safeguarded GPT Tutor condition, but no retrieved source text was provided here.

### c129 — exists ☐ · applied ☐  (line 591)
_Bearing: the tool is not the problem in itself. Designed to make students work, it taught well. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing note marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c130 — exists ✅ · applied ✅  · ⚑ degraded  (line 594)
_Gajos, K. Z., & Mamykina, L. (2022). Do people engage cognitively with AI? Impact of AI assistance on incidental learning. In _Proceedings of the 27th International Conference on Intelligent User Interfaces (IUI '22)_ (pp. 794–806). ACM. https://doi.org/10.1145/3490099.3511138 **[abstract]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the work by DOI; no abstract retrieved, but the described three-experiment nutrition/incidental-learning findings match my knowledge of this Gajos & Mamykina paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the ACM IUI 2022 paper metadata and DOI. No abstract or full text was retrieved, but from model knowledge only the described pattern of recommendation/explanation versus explanation-only conditions is consistent with the paper.

### c131 — exists ✅ · applied ✅  · ⚑ degraded  (line 604)
_Danry, V., Pataranutaporn, P., Mao, Y., & Maes, P. (2023). Don't just tell me, ask me: AI systems that intelligently frame explanations as questions improve human logical discernment accuracy over causal AI explanations. In _Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems_ (pp. 1–13). ACM. https://doi.org/10.1145/3544548.3580672 **[abstract]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the work by DOI; no abstract retrieved, but the AI-framed questioning finding and critical-thinking-stimulator aim match the known paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the CHI 2023 paper metadata and DOI. No application text was retrieved, but from model knowledge only the participant count and finding that AI-framed questioning improved logical discernment are consistent with the cited work.

### c133 — exists ☐ · applied ☐  (line 623)
_Bearing: what protects thinking is the thing people like least, and it helps most those who need it least. A design that keeps people thinking will not win on user preference alone. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing note marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c134 — exists ☐ · applied ☐  (line 626)
_Shen & Tamkin 2026 (1.2): six usage patterns; three "involve cognitive engagement and preserve learning outcomes even when participants receive AI assistance". In the blog, conceptual questions and asking for explanations alongside generated code scored 65% or more; delegation and progressive reliance scored under 40%. Groups of 2 to 7 people; the authors say the analysis "does not draw a causal link"._
- claude: exists=unchecked applied=unchecked [no_basis] — Back-reference to section 1.2 (a blog-based source, dated 2026); Crossref found no match and no evidence was retrieved to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match for an incomplete Shen & Tamkin 2026 reference, which is insufficient to verify or refute existence. No source text was retrieved to assess the detailed usage-pattern claims.

### c135 — exists ☐ · applied ☐  (line 630)
_Lehmann et al. 2024 (1.3): complementing beat substituting, in exploratory analyses._
- claude: exists=unchecked applied=unchecked [no_basis] — Back-reference to section 1.3; Crossref found no match and no evidence was retrieved to judge either axis.
- gpt: exists=unchecked applied=unchecked [no_basis] — The incomplete Lehmann et al. 2024 reference produced only a Crossref no-match, which is not decisive. No retrieved text supports or contradicts the claim about exploratory analyses.

### c136 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 633)
_Casner et al. 2014 (5.5): cognitive flying skills were better kept by pilots who stayed mentally engaged while the automation flew._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref found no match, but Casner et al. 2014 on retention of manual flying skills exists; the claim that cognitive skills were better retained with engagement is broadly consistent with that line of work.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref found no match for the incomplete Casner et al. 2014 reference, so existence is not verified from retrieved evidence. From model knowledge only, the claim is broadly consistent with Casner’s work on automation, engagement, and retention of flying skills, but no retrieved text was available.

### c137 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 634)
_SAFO 13002 (5.5): scheduled manual practice._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned only an irrelevant low-similarity match; however FAA SAFO 13002 is a real safety alert recommending manual flight operations practice, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The Crossref result is an unrelated low-similarity item and does not verify SAFO 13002 from retrieved evidence. From model knowledge only, FAA SAFO 13002 concerns manual flight operations and supports scheduled/manual practice.

### c138 — exists ☐ · applied ☐  (line 637)
_**What Q6 supports.** **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own section header marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c139 — exists ☐ · applied ☐  (line 641)
_The evidence is short-term and mostly from students and lab tasks. I found no study of these methods sustained over months at work._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author notes an absence of evidence, not a citable work.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is deliberately uncited and states an absence of found evidence rather than citing a specific work.

### c140 — exists ☐ · applied ☐  (line 649)
_## Q7. Testing the claim with the yardstick [ours] ... Our reading, to be argued, not a finding._
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own reading marked [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — Marked as [ours] and is_citation=false, so it is intentionally not an external citation to verify.

### c141 — exists ☐ · applied ☐  (line 651)
_*For:* the acquisition evidence is consistent and causal where it is randomised (1.1, 1.2, 1.3), and the mechanism is long established (4.1–4.3). The older-tool record shows the same: harm concentrated where the tool replaces skill formation (5.2)._
- claude: exists=unchecked applied=unchecked [no_basis] — These are internal cross-references to the document's own sections, not external works; no evidence available to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The entry contains no bibliographic work to identify, only internal cross-references, and Crossref found no match. No source text was retrieved for the claims.

### c142 — exists ☐ · applied ☐  (line 654)
_*Against "only":* skills already learned can fade when the doing was also the practice that kept them (2.1, 4.4, 5.3, 5.5). Experienced endoscopists and airline pilots were not learning; they were maintaining._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-references to document sections; no retrieved evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The entry gives no external bibliographic details and appears to point to internal sections; Crossref found no match. No evidence text was retrieved to assess the claims.

### c143 — exists ☐ · applied ☐  (line 657)
_*Also missing:* the change to thinking, not only to skill. Effort moves to checking and overseeing (2.2), and confidence in the tool goes with less critical thinking. That is not skill loss yet, but it is the condition under which skill erodes (5.5's "task-unrelated thought")._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-references to document sections; no retrieved evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — No identifiable external work is described, and the lookup produced no match. There is no retrieved source text supporting or contradicting the application.

### c144 — exists ☐ · applied ☐  (line 663)
_*For:* offloading is ordinary and mostly sensible (5.6). Each older tool cost the specific skill it replaced and little else (5.1–5.4). Panics about general decline have overreached (5.4, 1.6)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; internal cross-references, not external citations.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not an external citation and consists of internal cross-references, so both axes are unchecked.

### c145 — exists ☐ · applied ☐  (line 705)
_A successful, peer-reviewed replication of the session-4 result in Kosmyna et al. (1.6) with a larger sample._
- claude: exists=unchecked applied=unchecked [no_basis] — Kosmyna et al. refers to the known MIT 'Your Brain on ChatGPT' study, but no evidence was retrieved to confirm; (1.6) is an internal cross-reference.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only an author surname is supplied and Crossref found no match, so existence cannot be judged from the retrieved evidence. No source text was retrieved to assess the claimed session-4 result.

### c148 — exists ☐ · applied ☐  (line 732)
_A fresh challenger caught more of the producer's own material flaws than the producer reviewing its own output (figures and limits in brief 13, A.1: n = 8 problems, flaws confirmed by an AI panel, no significance test)._
- claude: exists=unchecked applied=unchecked [no_basis] — 'Brief 13, A.1' is an internal document reference; the crossref 'IN BRIEF' match is spurious and provides no basis to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved item, an unrelated “IN BRIEF” InPharma page, is a low-similarity nonmatch. No source text for “brief 13, A.1” was retrieved, so the application is unchecked.

### c149 — exists ☐ · applied ☐  (line 736)
_Bearing: only an analogy here, since the paper is about AI reviewers, not human skill. SPARRING's design asks a second party to challenge rather than to answer, the same shape as the "ask me" and "decide first" methods in Q6 (6.3, 6.4). I found no test in this repository of whether working through SPARRING keeps a *person's* own skills sharper than plain AI use. Do not imply one. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — SPARRING is the author's own system referenced internally (6.3, 6.4); the OED 'sparring' match is spurious and no relevant evidence retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved item is an Oxford English Dictionary entry for “sparring,” which is a low-similarity nonmatch to the intended SPARRING work. No relevant source text was retrieved to assess the analogy claim.

### c151 — exists ☐ · applied ☐  (line 754)
_What does years of everyday AI use do to a working professional's unaided skill? No multi-year study found on 2026-10-19._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; an open-question statement about absence of a study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and presents an open question rather than a cited work, so both axes are unchecked.

### c152 — exists ☐ · applied ☐  (line 756)
_Do juniors who start their careers with AI develop more slowly, differently, or not at all differently? No cohort study found; the evidence is one pre-AI case (3.4) and hiring data (3.5)._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question with internal cross-references.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and states an open evidence gap, so both axes are unchecked.

### c153 — exists ☐ · applied ☐  (line 758)
_Is the endoscopy result (2.1) lost skill, lowered effort, or a difference between patient groups? The correspondence (three letters) was not read._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question referencing internal section 2.1.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and identifies an unresolved question, so both axes are unchecked.

### c154 — exists ☐ · applied ☐  (line 760)
_What exactly did the Bastani et al. correction (1.1) change? Not read._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question referencing Bastani et al. via internal section 1.1; no evidence retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and says the correction was not read, so both axes are unchecked.

### c155 — exists ☐ · applied ☐  (line 761)
_Did the customer-support agents' gains (3.1) persist when the AI was unavailable? Abstract only._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question referencing internal section 3.1.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and poses an open question based only on an abstract, so both axes are unchecked.

### c156 — exists ☐ · applied ☐  (line 762)
_Do the methods that keep people thinking (Q6) survive months of real work, where speed is rewarded and the pleasant option wins? No workplace study found._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question about absence of a workplace study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and states that no workplace study was found, so both axes are unchecked.

### c157 — exists ☐ · applied ☐  (line 764)
_Does checking AI output, done regularly, maintain the underlying skill, or is checking a weaker form of practice than doing? I found no study that separates the two._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; open question about absence of a study.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and states an evidence gap rather than citing a work, so both axes are unchecked.

### c158 — exists ☐ · applied ☐  (line 769)
_**Vendor research.** Shen & Tamkin (1.2) are Anthropic authors; Lee et al. (2.2) are Microsoft Research authors. Claude, which helped draft this brief, is made by Anthropic. METR (2.4) is an independent research organisation._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; a provenance/caution note referencing internal sections.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and contains a vendor-research caution, so both axes are unchecked.

### c159 — exists ☐ · applied ☐  (line 772)
_**Preprints and unreviewed work:** Kosmyna et al. (1.6), Stanković et al. (1.6), Shen & Tamkin (1.2), Lehmann et al. (1.3), Becker et al. (2.4), Brynjolfsson, Chandar & Chen (3.5), Dell'Acqua et al. (2.5, a working paper)._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; a caution note listing works via internal cross-references.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and lists cautions about preprints and unreviewed work, so both axes are unchecked.

### c160 — exists ☐ · applied ☐  (line 775)
_**Self-report and correlation:** Lee et al. (2.2) and Gerlich (2.3) cannot show that AI caused any change._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; a methodological caution note referencing internal sections.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and gives a methodological caution, so both axes are unchecked.

### c161 — exists ☐ · applied ☐  (line 777)
_**Small samples:** Casner et al. (16 pilots), Becker et al. (16 developers), Dahmani & Bohbot's follow-up (13 people), Kosmyna et al.'s session 4 (18), Shen & Tamkin's usage patterns (2 to 7 per group)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an author's inline caution note, not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are left unchecked. No retrieved evidence or specific application claim was provided.

### c162 — exists ☐ · applied ☐  (line 782)
_**Unverified specifics flagged inline:** the Bastani correction's content (1.1); the endoscopy correspondence and the 19-endoscopist figure (2.1); how learning was measured in Brynjolfsson et al. (3.1); the Noy & Zhang working-paper sentence against the published text (3.2); the Bjork chapter's wording (4.1); Ellington 2003's own wording (5.2); whether Sparrow et al. was among Camerer et al.'s failures, from secondary sources and Hesselmann (5.4); SAFO 13002's wording (5.5); Kestin et al.'s sample and design details (6.2); the Stadler et al. task length (1.5); Beane's "ten to twenty times" (3.4); later versions of the "Canaries" figure (3.5)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an author's inline flag of unverified specifics, not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are left unchecked. No retrieved evidence or specific application claim was provided.

### c164 — exists ✅ · applied ☐  (line 796)
_Correction for Bastani et al., Generative AI without guardrails can harm learning: Evidence from high school mathematics (2025). Proceedings of the National Academy of Sciences, 122(34), e2518204122. https://doi.org/10.1073/pnas.2518204122 [record; content not read]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the correction record exists; content not read, so application axis cannot be assessed (author noted content not read).
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly verifies the correction title, journal, volume, issue, year, and DOI. No source text or specific claim was provided to assess application.

### c181 — exists ✅ · applied ☐  (line 815)
_Lee, H.-P. (H.), Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778 [abstract; Microsoft Research authors]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms exact title, authors, venue, DOI. No claims listed and no source text retrieved, so application cannot be assessed.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the title, authors, venue, year, pages, and DOI. No supported claim was provided, so application cannot be assessed.

### c182 — exists ⚠️ · applied ☐  (line 818)
_Beane, M. (2019). Shadow learning: Building robotic surgical skill when approved means fail. Administrative Science Quarterly, 64(1), 87–123. https://doi.org/10.1177/0001839217751692 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the work via DOI with matching title, author, pages. No specific claim text provided to evaluate application.
- gpt: exists=nuance applied=unchecked [no_basis] — The DOI metadata confirms the article and bibliographic details, but Crossref lists year 2018 while the reference gives 2019. No supported claim was provided, so application cannot be assessed.

### c183 — exists ⚠️ · applied ☐  (line 819)
_Brynjolfsson, E., Chandar, B., & Chen, R. (2025, August). Canaries in the coal mine? Six facts about the recent employment effects of artificial intelligence. Stanford Digital Economy Lab / SIEPR working paper. https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial [abstract: page read, via summary]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the SIEPR working paper page with matching title. Retrieved text is only site navigation, and no claim is specified to judge application.
- gpt: exists=nuance applied=unchecked [no_basis] — The Stanford SIEPR URL resolves to a page with the cited title, but the retrieved metadata does not confirm authors or date. No supported claim was provided, so application cannot be assessed.

### c184 — exists ✅ · applied ☐  (line 820)
_Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. The Quarterly Journal of Economics, 140(2), 889–942. https://doi.org/10.1093/qje/qjae044 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms title, authors, venue, DOI. No claim listed, though abstract is available for reference.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the cited QJE article, including title, authors, year, volume, issue, pages, and DOI. No supported claim was provided, so application cannot be assessed.

### c185 — exists ✅ · applied ☐  (line 821)
_Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. Science, 381(6654), 187–192. https://doi.org/10.1126/science.adh2586 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Science article exactly via DOI. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the Science article as cited. No supported claim was provided, so application cannot be assessed.

### c186 — exists ✅ · applied ☐  (line 822)
_Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence (working paper). SSRN 4375283. https://doi.org/10.2139/ssrn.4375283 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the SSRN working-paper version via DOI with matching abstract. No claim provided to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata confirms the SSRN working paper title, authors, year, and DOI. No supported claim was provided, so application cannot be assessed.

### c187 — exists ✅ · applied ☐  (line 825)
_Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. Memory & Cognition, 35(2), 201–210. https://doi.org/10.3758/BF03193441 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC both confirm this meta-analysis with matching abstract. No claim listed to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the resolved Springer URL confirm the article and DOI. No supported claim was provided, so application cannot be assessed.

### c188 — exists ☐ · applied ☐  (line 826)
_Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. P. Shimamura (Eds.), Metacognition: Knowing about knowing (pp. 185–205). MIT Press. [record; summaries only]_
- claude: exists=unchecked applied=unchecked [no_basis] — Open Library returned no match, but this is a well-known Bjork chapter in a real Metcalfe & Shimamura volume; absence from Open Library is not decisive. Existence cannot be confirmed or refuted from this evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved lookup was an Open Library no-match, which does not decisively confirm or refute the chapter's existence. No supported claim was provided, so application cannot be assessed.

### c189 — exists ✅ · applied ☐  (line 827)
_Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Roediger & Karpicke article via DOI with matching abstract. No claim provided to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the cited Psychological Science article. No supported claim was provided, so application cannot be assessed.

### c190 — exists ✅ · applied ☐  (line 828)
_Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. Journal of Experimental Psychology: Human Learning and Memory, 4(6), 592–604. https://doi.org/10.1037/0278-7393.4.6.592 [record]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Slamecka & Graf generation-effect paper via DOI. No claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata confirms the 1978 article title, authors, journal, volume, issue, pages, and DOI. No supported claim was provided, so application cannot be assessed.

### c191 — exists ✅ · applied ☐  (line 831)
_Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8 [abstract; text read]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Bainbridge's 'Ironies of automation' via DOI; URL resolves. Retrieved text was only a redirect, and no claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata confirms the Automatica article, and the DOI URL resolves to Elsevier. No supported claim was provided, so application cannot be assessed.

### c192 — exists ✅ · applied ☐  (line 832)
_Camerer, C. F., Dreber, A., Holzmeister, F., Ho, T.-H., Huber, J., Johannesson, M., et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. Nature Human Behaviour, 2, 637–644. https://doi.org/10.1038/s41562-018-0399-z [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm this replicability study with matching abstract. No claim provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and the Nature URL confirm the article and DOI. No supported claim was provided, so application cannot be assessed.

### c193 — exists ✅ · applied ☐  (line 833)
_Casner, S. M., Geven, R. W., Recker, M. P., & Schooler, J. W. (2014). The retention of manual flying skills in the automated cockpit. Human Factors, 56(8), 1506–1516. https://doi.org/10.1177/0018720814535628 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Casner et al. manual flying skills article via DOI with matching abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the cited Human Factors article. No supported claim was provided, so application cannot be assessed.

### c194 — exists ✅ · applied ☐  (line 834)
_Dahmani, L., & Bohbot, V. D. (2020). Habitual use of GPS negatively impacts spatial memory during self-guided navigation. Scientific Reports, 10, 6310. https://doi.org/10.1038/s41598-020-62877-0 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and URL resolution confirm the Dahmani & Bohbot GPS study with matching abstract. No claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata and the resolved Nature URL confirm the Scientific Reports article, with article number 6310 reflected in the reference though Crossref does not list pages. No supported claim was provided, so application cannot be assessed.

### c195 — exists ✅ · applied ☐  (line 835)
_Ebbatson, M., Harris, D., Huddlestone, J., & Sears, R. (2010). The relationship between manual handling performance and recent flying experience in air transport pilots. Ergonomics, 53(2), 268–277. https://doi.org/10.1080/00140130903342349 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm the Ebbatson et al. article with matching abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm the Ergonomics article and DOI. No supported claim was provided, so application cannot be assessed.

### c196 — exists ✅ · applied ☐  (line 836)
_Ellington, A. J. (2003). A meta-analysis of the effects of calculators on students' achievement and attitude levels in precollege mathematics classes. Journal for Research in Mathematics Education, 34(5), 433–463. https://doi.org/10.2307/30034795 [record; secondary summaries]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Ellington calculator meta-analysis via DOI. JSTOR page was blocked; no claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the JSTOR DOI record for the cited Journal for Research in Mathematics Education article, though it lists only the starting page. No supported claim was provided, so application cannot be assessed.

### c197 — exists ☐ · applied ☐  (line 837)
_Federal Aviation Administration (2013, 4 January). Safety Alert for Operators (SAFO) 13002: Manual flight operations. https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/airline_operators/airline_safety/SAFO13002.pdf [secondary]_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403 and existence_status is not-checkable; this is a known FAA SAFO but cannot be confirmed from the retrieved evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The URL fetch returned HTTP 403 and the item was marked not-checkable, leaving no decisive retrieved evidence of existence. No supported claim was provided, so application cannot be assessed.

### c198 — exists ✅ · applied ☐  (line 838)
_Hembree, R., & Dessart, D. J. (1986). Effects of hand-held calculators in precollege mathematics education: A meta-analysis. Journal for Research in Mathematics Education, 17(2), 83–99. https://doi.org/10.2307/749255 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Hembree & Dessart meta-analysis via DOI. JSTOR page blocked; no claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI record for the cited calculator meta-analysis, though it lists only the starting page. No supported claim was provided, so application cannot be assessed.

### c199 — exists ✅ · applied ☐  (line 839)
_Hesselmann, G. (2020). No conclusive evidence that difficult general knowledge questions cause a "Google Stroop effect". A replication study. PeerJ, 8, e10325. https://doi.org/10.7717/peerj.10325 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Hesselmann PeerJ replication study via DOI with matching abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the PeerJ article, including title, author, year, volume, article number, and DOI. No supported claim was provided, so application cannot be assessed.

### c200 — exists ✅ · applied ☐  (line 840)
_Maguire, E. A., Gadian, D. G., Johnsrude, I. S., Good, C. D., Ashburner, J., Frackowiak, R. S. J., & Frith, C. D. (2000). Navigation-related structural change in the hippocampi of taxi drivers. Proceedings of the National Academy of Sciences, 97(8), 4398–4403. https://doi.org/10.1073/pnas.070039597 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the Maguire et al. taxi-driver hippocampi study via DOI with matching abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the cited PNAS article, including title, authors, volume, issue, pages, and DOI. No supported claim was provided, so application cannot be assessed.

## ✅ AGREE-clean (24)
### c43 — exists ✅ · applied ✅  (line 127)
_In the coding study, three of six ways of using the AI preserved learning (Shen & Tamkin 2026; small groups, not causal)._
- claude: exists=verified applied=verified [evidence_text] — Shen & Tamkin 2026 exists (confirmed via c51 arxiv); the abstract states six AI interaction patterns, three preserving learning, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv evidence for Shen and Tamkin confirms a 2026 preprint titled “How AI Impacts Skill Formation.” Its abstract states that six AI interaction patterns were identified and that three involved cognitive engagement and preserved learning outcomes.

### c46 — exists ✅ · applied ✅  (line 142)
_Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. _Proceedings of the National Academy of Sciences_, 122(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the exact PNAS 2025 paper with matching metadata; the abstract fully supports the field experiment description.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly verifies the DOI, title, authors, journal, year, volume, and issue. The abstract supports the author note that this is the field experiment on generative AI tutors and learning in high school mathematics.

### c51 — exists ✅ · applied ✅  (line 162)
_Shen, J. H., & Tamkin, A. (2026). How AI impacts skill formation. arXiv:2601.20245. https://arxiv.org/abs/2601.20245 ; summarised in Anthropic (2026, 29 January), How AI assistance impacts the formation of coding skills, https://www.anthropic.com/research/AI-assistance-coding-skills **[abstract; blog read; Anthropic authors]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv:2601.20245 resolves to the Shen & Tamkin paper with matching title and authors; abstract content matches the described coding experiment.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves and the metadata match the cited title and authors. The abstract supports its use as a coding skill-formation experiment involving AI assistance and learning outcomes.

### c52 — exists ✅ · applied ✅  (line 163)
_summarised in Anthropic (2026, 29 January), How AI assistance impacts the formation of coding skills, https://www.anthropic.com/research/AI-assistance-coding-skills_
- claude: exists=verified applied=verified [evidence_text] — The Anthropic blog URL resolves with matching title and Jan 29, 2026 date, confirming the summary of the coding-skills study.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to the cited page title dated Jan. 29, 2026. The retrieved snippet confirms it is a blog-style research summary of a randomized controlled trial on AI assistance and coding skill formation.

### c58 — exists ✅ · applied ✅  (line 180)
_Lehmann, M., Cornelius, P. B., & Sting, F. J. (2024). AI meets the classroom: When do large language models harm learning? arXiv:2409.09047. https://arxiv.org/abs/2409.09047 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv:2409.09047 resolves to the Lehmann, Cornelius & Sting paper with matching title and authors; abstract supports the substitute/complement framing.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves and the metadata match the cited title and authors. The abstract supports the author note contrasting substitution and complementation patterns in LLM-assisted learning.

### c67 — exists ✅ · applied ✅  (line 214)
_Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., & Maes, P. (2025). Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task. arXiv:2506.08872. https://arxiv.org/abs/2506.08872 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to matching preprint; abstract confirms three groups, 54/18 participants, weakest LLM connectivity, reduced alpha/beta, quoting struggles, and four-month underperformance.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the resolved URL confirm the preprint, title, authors, and arXiv ID. The retrieved abstract directly states the group design, participant counts, weakest LLM connectivity, reduced alpha/beta connectivity in LLM-to-Brain, quotation difficulty, and underperformance across neural, linguistic, and behavioral levels.

### c71 — exists ✅ · applied ✅  (line 241)
_Budzyń, K., Romańczyk, M., Kitala, D., Kołodziej, P., Bugajski, M., Adami, H. O., Blom, J., Buszkiewicz, M., Halvorsen, N., Hassan, C., Romańczyk, T., Holme, Ø., Jarus, K., Fielding, S., Kunar, M., Pellise, M., Pilonis, N., Kamiński, M. F., et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. _The Lancet Gastroenterology & Hepatology_, 10(10), 896–903. https://doi.org/10.1016/S2468-1253(25)00133-5 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI and title confirmed; EuropePMC abstract confirms the four Poland centres, ADR decrease from 28.4% to 22.4% (-6.0%, p=0.0089), and the 'deskilling risk' title and interpretation.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the DOI, title, authors, journal, year, volume, issue, and pages, and the DOI URL resolves. The Europe PMC abstract directly supports the four-centre retrospective observational design, ADR decrease figures and p-value, interpretation, and the title phrase 'deskilling risk'.

### c78 — exists ✅ · applied ✅  (line 279)
_Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. _Societies_, 15(1), 6. https://doi.org/10.3390/soc15010006 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to matching work; abstract confirms 666 participants, negative correlation mediated by cognitive offloading, and younger participants' higher dependence/lower critical thinking.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the DOI, title, author, journal, year, volume, issue, article number, and abstract. The abstract directly states 666 participants, a significant negative correlation mediated by cognitive offloading, and younger participants' higher dependence and lower critical-thinking scores.

### c80 — exists ✅ · applied ✅  (line 288)
_Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. https://arxiv.org/abs/2507.09089 **[abstract]** (also in brief 13)_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to matching RCT; abstract confirms 16 developers, 246 tasks, forecast 24%/estimate 20% reduction, and the actual 19% increase in completion time.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the resolved URL confirm the preprint, title, authors, and arXiv ID. The abstract directly supports the RCT design, 16 developers, 246 tasks, forecasts of 24% and 20% faster completion, and the actual 19% increase in completion time.

### c86 — exists ✅ · applied ✅  (line 325)
_Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. _The Quarterly Journal of Economics_, 140(2), 889–942. https://doi.org/10.1093/qje/qjae044 (NBER working paper w31161, 2023) **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves with matching metadata; abstract directly supports the 5,172 agents, 15% productivity, skill heterogeneity, and learning/fluency claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref metadata matches the QJE article, DOI, authors, year, volume, issue, and pages. The abstract directly supports the claims about 5,172 agents, 15% productivity gains, heterogeneous gains by skill/experience, learning, and English fluency.

### c94 — exists ✅ · applied ✅  (line 358)
_Beane, M. (2019). Shadow learning: Building robotic surgical skill when approved means fail. _Administrative Science Quarterly_, 64(1), 87–123. https://doi.org/10.1177/0001839217751692 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves with matching metadata; abstract confirms the two-year five-site ethnography, 13 teaching hospitals, limited trainee role, shadow learning, undersupervised struggle, and hyperspecialization outcomes.
- gpt: exists=verified applied=verified [evidence_text] — Crossref metadata matches the article, DOI, journal, volume, issue, and pages, with the caveat that the metadata year reflects online publication in 2018 while the cited issue is 2019. The abstract directly supports the two-year five-site ethnography, interviews at 13 hospitals, limited trainee role, shadow learning, minority competence, undersupervised struggle, and hyperspecialization/decreasing expert supply.

### c99 — exists ✅ · applied ✅  (line 400)
_Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. _Memory & Cognition_, 35(2), 201–210. https://doi.org/10.3758/BF03193441 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves and EuropePMC abstract verbatim confirms the generation-vs-reading finding, 86 studies, and the .40 effect size.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the Springer URL verify the article and DOI. The Europe PMC abstract directly states that generated information is remembered better than read material and reports 445 effect sizes across 86 studies with an overall effect size of .40.

### c100 — exists ✅ · applied ✅  (line 408)
_Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. _Psychological Science_, 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves with matching metadata; abstract directly confirms that on delayed tests prior testing beat studying despite higher confidence from studying.
- gpt: exists=verified applied=verified [evidence_text] — Crossref metadata verifies the Psychological Science article and DOI. The abstract directly supports the claim that delayed prior testing produced greater retention than studying even though repeated studying increased confidence, and the bearing statement is a fair inference from that result.

### c108 — exists ✅ · applied ✅  (line 473)
_Dahmani, L., & Bohbot, V. D. (2020). Habitual use of GPS negatively impacts spatial memory during self-guided navigation. _Scientific Reports_, 10, 6310. https://doi.org/10.1038/s41598-020-62877-0 [abstract]. 50 regular drivers._
- claude: exists=verified applied=verified [evidence_text] — DOI confirms the Dahmani & Bohbot 2020 paper, and the retrieved abstract directly supports the 50 drivers, 13-participant follow-up, and causal-direction claims.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Scientific Reports article and DOI. The retrieved abstract directly supports the claims about 50 drivers, the 13-person longitudinal follow-up, worse spatial memory with greater GPS use, and the authors' interpretation regarding sense of direction.

### c109 — exists ✅ · applied ✅  (line 480)
_Maguire, E. A., Gadian, D. G., Johnsrude, I. S., Good, C. D., Ashburner, J., Frackowiak, R. S. J., & Frith, C. D. (2000). Navigation-related structural change in the hippocampi of taxi drivers. _Proceedings of the National Academy of Sciences_, 97(8), 4398–4403. https://doi.org/10.1073/pnas.070039597 [abstract]._
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Maguire et al. 2000, and the abstract contains the exact quoted statements about posterior hippocampi being larger and correlating with time as a taxi driver.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the PNAS article and DOI. The retrieved abstract directly states that posterior hippocampi were larger in taxi drivers and that hippocampal volume correlated with time spent as a taxi driver.

### c111 — exists ✅ · applied ✅  (line 491)
_Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory: Cognitive consequences of having information at our fingertips. _Science_, 333(6043), 776–778. https://doi.org/10.1126/science.1207745 [abstract]._
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Sparrow et al. 2011. The brief abstract ('encode where rather than what') supports the cited claim about lower recall and enhanced recall of where to access information.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science article and DOI. The retrieved abstract supports the claim that Internet search shifts encoding toward where information can be found rather than the information itself.

### c113 — exists ✅ · applied ✅  (line 502)
_Hesselmann, G. (2020). No conclusive evidence that difficult general knowledge questions cause a "Google Stroop effect". A replication study. _PeerJ_, 8, e10325. https://doi.org/10.7717/peerj.10325 [abstract]._
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Hesselmann 2020, and the abstract contains the quoted statements about the Google Stroop effect failing to replicate and 'no conclusive evidence' with a closer design.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the PeerJ article and DOI. The retrieved abstract directly states that the Google Stroop effect failed to replicate in two large-project attempts and that Hesselmann's closer replication found no conclusive evidence.

### c117 — exists ✅ · applied ✅  (line 515)
_Casner, S. M., Geven, R. W., Recker, M. P., & Schooler, J. W. (2014). The retention of manual flying skills in the automated cockpit. _Human Factors_, 56(8), 1506–1516. https://doi.org/10.1177/0018720814535628 **[abstract]**. 16 airline pilots in a Boeing 747-400 simulator. "We found pilots' instrument scanning and manual control skills to be mostly intact, even when pilots reported that they were infrequently practiced." But for "the cognitive tasks needed for manual flight (e.g., tracking the aircraft's position without the use of a map display, deciding which navigational steps come next, recognizing instrument system failures), we observed more frequent and significant problems", associated with "task-unrelated thought". Conclusion: the retention of cognitive skills "may depend on the degree to which pilots remain actively engaged in supervising the automation."_
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Casner et al. 2014, and the abstract supports all three claims: 16 pilots in a 747-400 sim, intact scanning/control skills, cognitive-task problems, and dependence on active supervision.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Human Factors article and DOI. The retrieved abstract directly supports the claims about 16 pilots, a Boeing 747-400 simulator, mostly intact manual/instrument skills, more problems with cognitive tasks, task-unrelated thought, and the conclusion about active supervision.

### c118 — exists ✅ · applied ✅  (line 525)
_Ebbatson, M., Harris, D., Huddlestone, J., & Sears, R. (2010). The relationship between manual handling performance and recent flying experience in air transport pilots. _Ergonomics_, 53(2), 268–277. https://doi.org/10.1080/00140130903342349 **[abstract]**. Notes "anecdotal evidence" of manual skill decay and "a paucity of objective data"; finds "significant relationships ... between pilots' very recent flying experience and their manual control strategy"._
- claude: exists=verified applied=verified [evidence_text] — DOI and EuropePMC confirm Ebbatson et al. 2010, and the abstract contains the 'anecdotal evidence', 'paucity of objective data', and 'significant relationships... recent flying experience and manual control strategy' statements.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC verify the Ergonomics article and DOI. The EuropePMC abstract directly supports the claims about anecdotal evidence, paucity of objective data, and significant relationships between very recent flying experience and manual control strategy.

### c120 — exists ✅ · applied ✅  (line 537)
_Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. _Human Factors_, 52(3), 381–410. https://doi.org/10.1177/0018720810376055 **[abstract]**. Complacency "is found in both naive and expert participants and cannot be overcome with simple practice"; automation bias "occurs in both naive and expert participants, cannot be prevented by training or instructions"._
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Parasuraman & Manzey 2010, and the abstract contains the exact quoted statements about complacency and automation bias in naive and expert participants.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Human Factors article and DOI. The retrieved abstract directly states the claims about automation complacency and automation bias occurring in both naive and expert participants and resisting simple practice, training, or instructions.

### c123 — exists ✅ · applied ✅  (line 550)
_Defined as "the use of physical action to alter the information processing requirements of a task so as to reduce cognitive demand", from tilting your head to read rotated text to a phone reminder. The review asks what triggers offloading and "what are the cognitive consequences of this behavior?"_
- claude: exists=verified applied=verified [evidence_text] — The definition and the two review questions quoted match the abstract exactly.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the bibliographic metadata for Risko and Gilbert 2016. The Europe PMC abstract contains the quoted definition and states the two review questions exactly as claimed.

### c127 — exists ✅ · applied ✅  (line 582)
_Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. _Scientific Reports_, 15, 17458. https://doi.org/10.1038/s41598-025-97652-6 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI match confirms the work; abstract explicitly supports both the learning-more claim and the shared pedagogical design claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, Europe PMC, and the DOI URL confirm the article metadata. The retrieved abstract directly states that the AI tutor used the same pedagogical best practices and that students learned significantly more in less time than in active learning.

### c132 — exists ✅ · applied ✅  (line 615)
_Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. _Proceedings of the ACM on Human-Computer Interaction_, 5(CSCW1), 1–21. https://doi.org/10.1145/3449287 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI match confirms the work; abstract explicitly supports N=199, the overreliance reduction with unfavorable subjective ratings trade-off, and the Need for Cognition moderation.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and provides the abstract. The abstract directly states N=199, reduced overreliance versus simple explainable AI approaches, less favorable subjective ratings for the strongest interventions, and greater benefit for higher Need for Cognition participants.

### c146 — exists ✅ · applied ✅  (line 717)
_Published and citable: Paper 1 (the Resolver), Zenodo concept DOI https://doi.org/10.5281/zenodo.21210264. Source read: `pilots/llm-judge-2026-05-02/v2/preprint-draft.md` (read only). It is locked. Cite its findings as published; do not paraphrase them into claims it doesn't make._
- claude: exists=verified applied=verified [evidence_text] — The Zenodo DOI resolves to the author's own 'Resolver' paper on auditable adversarial review (the crossref 'Magnetic Resolver' abstract is a spurious title collision); the citation is self-reference and consistent with the resolved record.
- gpt: exists=verified applied=verified [evidence_text] — The DOI URL resolves to a Zenodo record titled “Auditable adversarial review for AI-in-the-loop decisions…” mentioning SPARRING's Resolver, confirming the cited Zenodo work exists. The unrelated low-similarity Crossref result appears to be a false match, but the Zenodo resolution supports the claim that the work is published and citable.
