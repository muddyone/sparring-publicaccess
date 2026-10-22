# cite-check report — witan-personality-and-connection

**Source:** `docs/research/personality-and-connection.md (body, before the References section)`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **75** citations checked
- existence independently confirmed: **71**
- application evidence-grounded: **55**
- application judged from model knowledge only: **30**
- not independently checkable: **3**
- buckets — clean **15** · problem **57** · disagree **9**

## ⛔ DISAGREE — escalate to human (9)
### c24 — exists SPLIT · applied ☐  (line 181)
_the companion report, [Chalmers and AI minds](../chalmers-and-ai-minds.md)_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — This is an internal companion report (local .md file) not externally resolvable; the retrieved abstract is from an unrelated paper ('AI Agents and Minds' by Kak), so no match exists.
- gpt: exists=unchecked applied=unchecked [no_basis] — The local file URL could not be fetched, and the only retrieved Crossref item was an unrelated low-similarity work titled AI Agents and Minds. Because the cited companion report itself was not retrieved or matched, there is no basis to assess the application claim.

### c44 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 242)
_[McAllister](#mcallister1995)_
- **escalate:** application: unchecked vs nuance
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the McAllister 1995 article. No abstract or text was retrieved to verify the specific nuanced claim about affective trust and attention versus reduced monitoring.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article metadata. From model knowledge the claim is broadly consistent with McAllister’s distinction between affective trust and attention/cooperation, but the retrieved evidence contains no abstract or text to verify the specific monitoring claim.

### c50 — exists ✅ · applied SPLIT  (line 260)
_[2010](#bickmore2010)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract describes longitudinal RCTs on maintaining engagement over time, supporting the engagement-over-1–4-months claim.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and Europe PMC confirm the article metadata. The abstract says two longitudinal randomized experiments assessed engagement, but it does not state positive effects, desire to continue, or the 1–4 month duration needed to verify the claim.

### c55 — exists ✅ · applied SPLIT  (line 268)
_[Roesler et al. 2021](#roesler2021)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Crossref confirms the meta-analysis, but the retrieved abstract is a single sentence and does not state the '78 studies' count or the 'no gain in task performance' finding; the specific figures cannot be confirmed from evidence.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref confirms the Science Robotics article metadata. The retrieved abstract only says the meta-analysis quantifies whether and when anthropomorphic features facilitate HRI, and does not mention 78 studies or no task-performance gain.

### c58 — exists ✅ · applied SPLIT  (line 280)
_[Bickmore, Schulman and Yin 2010](#bickmore2010)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Crossref confirms the article; the abstract supports engagement effects from relational features but does not contain the specific results that engagement didn't increase exercise or that the engaging variant reduced walking—those detailed claims aren't verifiable from the retrieved text.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and Europe PMC confirm the article metadata. The abstract says two longitudinal RCTs assessed engagement manipulations, but it does not provide the specific findings about logins, enjoyment, desire to continue, exercise, or walking.

### c62 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 292)
_[Xie et al. 2024](#xie2024), abstract only)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Metadata confirms the paper exists; no abstract retrieved (only 'Redirecting'). The claim about humor helping casual chat but hurting task dialogue aligns with the paper's framing based on title and my knowledge.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, volume, and article number. No substantive abstract or full text was retrieved, so the humor-by-context satisfaction claim cannot be judged from the evidence.

### c64 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 297)
_[Chattaraman et al. 2019](#chattaraman2019)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Metadata confirms the paper; no abstract retrieved. The task-competency/reciprocity framing in the title matches the claim that low-competency users benefit from task-oriented style and high-competency from social style.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the article metadata and DOI. The retrieved evidence contains no abstract or substantive text, so the specific task-competency moderation claim cannot be evaluated.

### c65 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 303)
_[Kaiser et al. 2021](#kaiser2021); subscale figures from a secondary summary)_
- **escalate:** application: unchecked vs nuance
- claude: exists=verified applied=unchecked [model_knowledge_only] — Paper existence confirmed by DOI match. No abstract retrieved; the r≈.20 and subscale breakdown claims (author notes they come from a secondary summary) cannot be verified from available evidence.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the meta-analysis metadata and DOI. No source text was retrieved; from model knowledge the citation broadly fits the alliance-outcome claim, but the exact r value and subscale comparison are not verifiable here and are noted as coming from a secondary summary.

### c67 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 311)
_[OpenAI 2025](#openai2025)_
- **escalate:** application: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch returned HTTP 403, so existence not confirmed by evidence. OpenAI did publicly roll back a GPT-4o update in spring 2025 over sycophancy, consistent with the claim, but I cannot verify this specific page.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only retrieved evidence is a 403 fetch failure, so existence cannot be confirmed from the lookup evidence. Based on model knowledge only, the claim broadly matches OpenAI's public explanation of the April 2025 rollback, but without retrieved text the exact thumbs-up/agreeableness mechanism remains caveated.

## ⚠️ AGREE-problem (57)
### c01 — exists ☐ · applied ☐  (line 3)
_Research report, 2026-10-15. It draws on three research strands run the same day: human-to-human workplace psychology, human–machine and human–AI studies, and the theory of why connection matters. Background for Method: Agents, section 2. Not client data._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference, not a citation (is_citation=false); both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an internal cross-reference rather than a bibliographic citation. Per instruction, both axes are unchecked.

### c02 — exists ✅ · applied ✅  · ⚑ degraded  (line 69)
_Dennett's *intentional stance* ([Dennett 1987](#dennett1987))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dennett's The Intentional Stance (1987); the claim accurately summarizes Dennett's well-known thesis on predicting systems via the intentional stance.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches Dennett's 1987 book by title and author. From general knowledge, Dennett's intentional stance is used to predict complex systems by treating them as intentional agents when that predictive strategy works.

### c03 — exists ✅ · applied ⚠️  (line 71)
_Anthropomorphism research ([Epley, Waytz and Cacioppo 2007](#epley2007))_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed article; abstract supports that anthropomorphism is common and driven by effectance (desire to explain/predict) motivation, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC confirm the DOI, title, authors, journal, year, and pages. The abstract supports anthropomorphism of nonhuman agents and the role of effectance motivation in understanding/predicting them, but the claim's wording 'automatically' and specific focus on machines are stronger than the abstract alone states.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 87)
_[Clark and Brennan (1991)](#clark1991)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed chapter; Clark & Brennan's grounding theory and least-collaborative-effort principle match the claim, though no abstract was retrieved.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the chapter title, authors, DOI, pages, and 1991 edited volume. From general knowledge, Clark and Brennan's grounding theory concerns establishing common ground and minimizing collaborative effort in communication.

### c06 — exists ✅ · applied ✅  · ⚑ degraded  (line 101)
_the tone of a partner spreads to you ([Hatfield et al. 1993](#hatfield1993))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed article; emotional contagion (catching others' affect) is the core thesis, matching the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the 1993 Current Directions article with the stated DOI and metadata. From general knowledge, emotional contagion is the spread or catching of others' affective states, which fits the claim that a partner's tone can spread to you.

### c07 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 104)
_you read your mood as a signal about whether the work is going well ([Schwarz and Clore 1983](#schwarz1983))_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed; this is the foundational affect-as-information paper supporting that mood is read as a signal about one's situation.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article metadata and DOI. From general knowledge, the article supports affect-as-information in judgments of well-being, but applying it specifically to judging whether work is going well is a broader extrapolation.

### c08 — exists ✅ · applied ✅  · ⚑ degraded  (line 106)
_a positive mood widens what you think to try ([Fredrickson 2001](#fredrickson2001)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed broaden-and-build paper; the claim that positive mood widens behavioral repertoire is the core thesis, and the author appropriately notes replication caveats.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Fredrickson's 2001 American Psychologist article and DOI. From general knowledge, broaden-and-build theory holds that positive emotions broaden thought-action repertoires, matching the claim that positive mood widens what one thinks to try.

### c09 — exists ✅ · applied ⚠️  (line 106)
_its stronger claims replicate less well: [Brown, Sokal and Friedman 2013](#brown2013)_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed; abstract critiques the positivity-ratio claims of Fredrickson/Losada as unfounded, supporting that stronger claims replicate poorly.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC confirm the article and DOI. The abstract directly criticizes the Fredrickson-Losada critical positivity-ratio claim as unfounded, but it is more a conceptual/mathematical critique of a specific strong claim than evidence about replication of broaden-and-build claims generally.

### c10 — exists ☐ · applied ✅  · ⚑ degraded  (line 108)
_brief positive exchanges energise people at work ([Dutton and Heaphy 2003](#dutton2003), conceptual)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL fetch returned HTTP 403, so existence is not checkable from evidence; Dutton & Heaphy's high-quality-connections work is well-known and supports the energizing-connections claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is a 403 URL fetch, and the citation is marked not-checkable, so existence cannot be verified from the supplied evidence. From general knowledge, Dutton and Heaphy's high-quality connections framework treats brief positive workplace connections as energizing.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 109)
_An experience-sampling study of office small talk found it "uplifting yet distracting" ([Methot et al. 2021](#methot2021))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed with exact title; the title itself ('uplifting yet distracting') matches the quoted claim about experience-sampled office small talk.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Academy of Management Journal article with the cited title, authors, year, pages, and DOI. From general knowledge, the paper is a daily/experience-sampling study of workplace small talk and characterizes it as both uplifting and distracting.

### c12 — exists ✅ · applied ⚠️  (line 121)
_[Fiske, Cuddy and Glick (2007)](#fiske2007): we judge others on warmth (does this person mean well toward me?) before competence (can they act on it?). Intent decides whether someone's skill helps you or threatens you. This is why warmth *feels* like trust._
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed; abstract states social animals first judge intent (warmth) then ability (competence), directly supporting the warmth-before-competence claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref, Europe PMC, and the resolving URL confirm the article metadata. The abstract strongly supports warmth as perceived intent and competence as ability, with intent assessed first, though the phrase 'warmth feels like trust' is an interpretive gloss rather than wording directly shown in the abstract.

### c13 — exists ✅ · applied ⚠️  (line 139)
_In field studies, giving people more or less blending than they want lowers satisfaction and commitment ([Rothbard, Phillips and Dumas 2005](#rothbard2005); [Kreiner 2006](#kreiner2006))._
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed; abstract shows fit between segmentation desire and policy access affects satisfaction/commitment, supporting both the segmentor-integrator continuum and the misfit claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the article and provides an abstract matching the cited work. The abstract supports person-policy fit effects on satisfaction and commitment for integration/segmentation preferences, but the supplied claim set also includes a broader 'segmentors to integrators' wording that is only loosely supported as a continuum of preferences.

### c14 — exists ✅ · applied ⚠️  (line 140)
_[Kreiner 2006](#kreiner2006)_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed; abstract's person-environment fit effects on conflict, stress and satisfaction support the claim that misaligned segmentation lowers wellbeing.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the Kreiner article and DOI. The abstract supports fit between segmentation preference and workplace segmentation affecting job satisfaction, stress, and work-home conflict, but it does not specifically mention organizational commitment.

### c15 — exists ⚠️ · applied ✅  (line 142)
_People value what they helped build (the IKEA effect, [Norton et al. 2012](#norton2012))_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed (publisher year 2011 vs cited 2012 is a minor print/online discrepancy); abstract directly defines the IKEA effect as increased valuation of self-made products.
- gpt: exists=nuance applied=verified [evidence_text] — The DOI, title, authors, journal, volume, issue, and pages match, though Crossref lists year 2011 while the reference gives 2012. The abstract directly states that self-made products receive increased valuation, with boundary conditions around successful completion.

### c16 — exists ✅ · applied ✅  · ⚑ degraded  (line 144)
_choosing for yourself meets the autonomy need that self-determination theory names ([Ryan and Deci 2000](#ryan2000))._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed foundational SDT paper; autonomy as a basic psychological need is a core tenet supporting the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Ryan and Deci American Psychologist article and DOI. From general knowledge, self-determination theory identifies autonomy as a basic psychological need, and choosing for oneself is a standard way of satisfying or supporting autonomy.

### c17 — exists ✅ · applied ✅  · ⚑ degraded  (line 147)
_Shaping whom you work with and how changes what the work means to you ([Wrzesniewski and Dutton 2001](#wrzesniewski2001))._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed job-crafting paper (fetched URL was a JStor challenge page, uninformative); relational and task crafting altering work meaning is the paper's thesis.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the article metadata and DOI, and the JSTOR URL resolves though only to a client-challenge page. From general knowledge, Wrzesniewski and Dutton's job crafting framework includes relational crafting and changes in the meaning of work.

### c18 — exists ⚠️ · applied ✅  · ⚑ degraded  (line 156)
_Goffman's "face-work" covers the small rituals of apology, greeting and joking repair that keep an interaction smooth ([Goffman 1967](#goffman1967))._
- claude: exists=verified applied=verified [model_knowledge_only] — DOI confirms Goffman's Interaction Ritual (reissue, matching the full_reference note); face-work and small corrective rituals are central Goffman concepts supporting the claim.
- gpt: exists=nuance applied=verified [model_knowledge_only] — Crossref confirms a 2017 Routledge DOI for Interaction Ritual, while the cited original is a 1967 Anchor Books work with that later reissue DOI. From general knowledge, Goffman's face-work covers interactional rituals and remedial practices that maintain smooth face-to-face encounters.

### c19 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 157)
_Dunbar's work treats laughter as social grooming: cheap upkeep for a bond ([Dunbar 1996](#dunbar1996))._
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dunbar's 1996 book; the social-grooming hypothesis of language/laughter maintaining bonds is its central argument.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Open Library matches Dunbar's 1996 book by title and author. From general knowledge, Dunbar argues for language/gossip as social grooming, but the specific claim about laughter as cheap social grooming is more directly associated with related Dunbar work and is only loosely attributable to this book without source text.

### c20 — exists ✅ · applied ✅  · ⚑ degraded  (line 159)
_Laughter groups let more bonds be kept up at once than one-to-one grooming does ([Dezecache and Dunbar 2012](#dezecache2012))._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI-confirmed (fetched page only said 'Redirecting'); the paper on natural laughter group sizes supports laughter enabling bonding with more partners at once.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the article's DOI, title, authors, journal, year, and pages, and the DOI URL resolves. From general knowledge, the paper on natural laughter group size supports the idea that laughter can maintain bonds in groups more efficiently than one-to-one grooming.

### c21 — exists ✅ · applied ✅  · ⚑ degraded  (line 160)
_A named, voiced self-driving car was trusted more, and blamed less after a staged accident ([Waytz, Heafner and Epley 2014](#waytz2014))._
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; URL fetch returned only a redirect page so claim text wasn't retrieved, but this study is well-known for the trust/blame finding with anthropomorphized vehicles.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, volume, and pages. The retrieved snippet contains no substantive claim text, but from model knowledge the study used an anthropomorphized autonomous vehicle and found greater trust and less blame after an accident.

### c23 — exists ✅ · applied ✅  · ⚑ degraded  (line 171)
_Aristotle names three kinds of friendship ([Aristotle, *Nicomachean Ethics* VIII–IX](#aristotle2000)):_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The Crisp translation of Nicomachean Ethics is confirmed; Books VIII-IX famously describe the three kinds of friendship (utility, pleasure, virtue) as claimed.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref and Cambridge confirm the Cambridge University Press work Aristotle: Nicomachean Ethics with the cited DOI. The retrieved snippet does not include Books VIII–IX content, but from model knowledge Aristotle distinguishes friendships of utility, pleasure, and virtue.

### c25 — exists ✅ · applied ⚠️  (line 189)
_A meta-analysis of 99 studies ([Van den Broeck et al. 2016](#vandenbroeck2016))_
- claude: exists=verified applied=nuance [evidence_text] — Abstract confirms the 99-study meta-analysis on basic psychological needs including relatedness, but the specific correlation coefficients (.60, .52, etc.) are not verifiable from the abstract alone.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the article and its abstract describes a meta-analytic review of 99 studies on autonomy, competence, and relatedness at work. The abstract supports the broad claim that relatedness is a basic need and matters at work, but it does not provide the specific reported correlations.

### c26 — exists ✅ · applied ✅  · ⚑ degraded  (line 199)
_In a lagged field study of 672 employees ([Ozcelik and Barsade 2018](#ozcelik2018))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; no abstract retrieved, but this study is known for showing workplace loneliness predicts lower supervisor-rated performance via commitment and approachability.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, volume, issue, and pages. No abstract or full text was retrieved, but from model knowledge the article reports a lagged field study linking workplace loneliness to lower supervisor-rated performance through commitment and approachability-related mechanisms.

### c27 — exists ⚠️ · applied ✅  (line 203)
_It works through positive mood and trust, against real costs in exhaustion and upkeep ([Methot et al. 2016](#methot2016))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms workplace friendships enhance performance through positive affect and trust while depleting resources (exhaustion, maintenance), matching the claim.
- gpt: exists=nuance applied=verified [evidence_text] — Crossref confirms the DOI, title, authors, journal, volume, issue, and pages, though it lists year 2015 rather than the reference’s 2016 issue year. The abstract directly supports positive performance associations via positive affect and trust, offset by emotional exhaustion and maintenance difficulty.

### c28 — exists ⚠️ · applied ✅  (line 205)
_Friend groups outperform acquaintance groups, d = .31, a small-to-moderate effect (meta-analysis, [Chung et al. 2018](#chung2018))_
- claude: exists=verified applied=verified [evidence_text] — Abstract explicitly states friendship groups outperform acquaintance groups with Cohen's d = 0.31, exactly matching the claim.
- gpt: exists=nuance applied=verified [evidence_text] — Crossref confirms the article and DOI, though it lists year 2017 while the reference gives the 2018 issue year. The abstract explicitly reports that friendship groups outperform acquaintance groups with Cohen’s d = 0.31.

### c29 — exists ✅ · applied ✅  · ⚑ degraded  (line 207)
_Leader humour lifts mood, improves the relationship and increases discretionary help ([Cooper et al. 2018](#cooper2018))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; no abstract retrieved, but this paper documents leader humor improving mood, LMX relationships, and discretionary/OCB behavior.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the article metadata and DOI. No abstract or full text was retrieved, but from model knowledge the article links leader humor to positive affect, leader-member relationship quality, and helping/citizenship outcomes.

### c31 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 212)
_the closest to a paid assistant is the "commercial friendship" between a hairdresser and a regular client ([Price and Arnould 1999](#price1999); [Gremler and Gwinner 2000](#gremler2000))_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; URL blocked by client challenge, but this paper is the foundational 'commercial friendship' study including hairdresser-client examples linked to loyalty.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article Commercial Friendships and its DOI, and the URL resolves to JSTOR. The retrieved page snippet is only a client challenge; from model knowledge the article supports the commercial-friendship analogue, but the loyalty claim is more directly supported by the paired Gremler and Gwinner citation.

### c32 — exists ✅ · applied ⚠️  (line 212)
_[Gremler and Gwinner 2000](#gremler2000)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms rapport in service relationships positively relates to satisfaction, loyalty intent, and word-of-mouth, supporting the rapport-loyalty claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the article and supplies an abstract. The abstract directly supports rapport being positively related to satisfaction, loyalty intent, and word of mouth, but it does not itself establish the “commercial friendship”/hairdresser analogue.

### c33 — exists ✅ · applied ✅  · ⚑ degraded  (line 217)
_[McAllister's (1995)](#mcallister1995)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms McAllister's classic 1995 trust study; no abstract retrieved, but it is well-known that cognition-based trust strongly predicts affect-based trust in this paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the McAllister article metadata and DOI. No abstract or text was retrieved, but from model knowledge the study distinguishes cognition- and affect-based trust and reports cognition-based trust as a strong predictor of affect-based trust.

### c34 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 220)
_[Grandey et al. 2005](#grandey2005)_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; URL only redirects, but this study is known for showing authentic smiling raised satisfaction conditional on task competence.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article metadata and DOI, and the DOI resolves to Elsevier. The retrieved snippet is non-substantive; from model knowledge the paper concerns authenticity and positive displays in service encounters, but the specific moderation claim about smiling only helping when the task is done well is not confirmed by retrieved evidence.

### c35 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 222)
_[Edmondson (1999)](#edmondson1999)_
- claude: exists=verified applied=nuance [evidence_text] — Abstract confirms Edmondson introduced psychological safety as distinct from team efficacy, but the specific claim distinguishing it from cohesion and noting cohesion reduces willingness to disagree is not directly in the abstract.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Edmondson article and its abstract introduces team psychological safety. The abstract does not contain the cohesion comparison, but from model knowledge Edmondson distinguishes psychological safety from cohesion and notes that cohesion can inhibit disagreement.

### c36 — exists ✅ · applied ✅  · ⚑ degraded  (line 225)
_[Pillemer and Rothbard 2018](#pillemer2018)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article; no abstract retrieved, but this theoretical paper on dark sides of workplace friendship discusses reluctance to challenge friends.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the article metadata and DOI. No abstract or full text was retrieved, but from model knowledge the AMR article theorizes dark sides of workplace friendship, including reluctance to challenge or confront friends.

### c37 — exists ⚠️ · applied ✅  (line 229)
_[Chung et al. 2018](#chung2018)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the friendship advantage appeared on high-quantity-output tasks but not on single/high-quality-output tasks, matching the claim.
- gpt: exists=nuance applied=verified [evidence_text] — Crossref confirms the DOI and article, with a minor year discrepancy between online publication and issue year. The abstract explicitly states that friendship groups performed better on high-quantity-output tasks, with no benefit on single or high-quality-output tasks.

### c39 — exists ✅ · applied ⚠️  (line 234)
_[Fleming 2005](#fleming2005)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms managed 'culture of fun' had the unintended effect of fuelling cynicism among employees, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the article and provides an abstract. The abstract supports that managed fun can fuel cynicism, but the source frames this as an unintended effect among some employees rather than a universal result.

### c41 — exists ✅ · applied ✅  · ⚑ degraded  (line 237)
_[Yam et al. 2018](#yam2018)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the exact article. The paper documents that leader humor can signal norm-violation acceptability (aggressive humor/deviance), supporting the claim, though only metadata was retrieved.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, volume, pages, and year. From model knowledge, the paper reports a downside of leader humor through perceived acceptability of norm violation/rule-bending, but no retrieved abstract/full text was available.

### c42 — exists ✅ · applied ☐  (line 239)
_[Patel and Plowman 2022](#patel2022)_
- claude: exists=verified applied=unchecked [no_basis] — The Gallup page resolves with matching title, confirming existence. The retrieved snippet is only site navigation chrome and does not address whether the profit figures are Gallup's own projections.
- gpt: exists=verified applied=unchecked [evidence_text] — The Gallup URL resolves with the cited title. The retrieved snippet is essentially page/navigation text and does not contain the profit/projection language needed to assess the claim.

### c45 — exists ☐ · applied ☐  (line 247)
_We found no peer-reviewed study of what makes a great executive-assistant partnership. Anticipation, discretion and shared context are credible practitioner wisdom, not measured findings._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly marked not a citation / deliberately uncited; author notes it is practitioner wisdom with no peer-reviewed study found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is deliberately uncited and marked as not a citation. No existence or application check is applicable.

### c46 — exists ✅ · applied ⚠️  (line 257)
_[Bickmore and Picard 2005](#bickmore2005)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract reports the relational agent was liked and trusted more even after four weeks, supporting the claim of warmth/liking holding at 4 weeks.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the TOCHI article and DOI. The abstract supports that the relational agent was liked, trusted, and respected after four weeks, but it does not specifically mention warmth or sense of presence.

### c47 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 259)
_[Waytz 2014](#waytz2014)_
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Waytz et al. 2014 article. Only a 'Redirecting' snippet was retrieved, but the well-known finding of anthropomorphism increasing trust/forgiveness in short studies supports the modest claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article metadata and the DOI resolves. The retrieved source text only says “Redirecting,” so the application judgment relies on model knowledge that the study found anthropomorphism increased trust in a short autonomous-vehicle experiment, with forgiveness/error tolerance only an inferred or partial fit.

### c49 — exists ✅ · applied ⚠️  (line 260)
_[Bickmore 2005](#bickmore2005)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract reports greater desire to continue after a month of daily interaction, supporting the engagement/continuation claim over 1–4 months.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the cited Bickmore and Picard article. The abstract supports greater desire to continue after a one-month/four-week study, but this citation alone does not support the broader “1–4 months” range.

### c52 — exists ✅ · applied ⚠️  (line 261)
_Woebot, observational: [Darcy et al. 2021](#darcy2021)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the observational study; the abstract reports human-level therapeutic bond scores with Woebot, supporting the bond claim and the 'observational' characterization.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the JMIR article and DOI. The abstract supports high Woebot bond scores in an observational study, but it reports measurement within 5 days of initial app use rather than over a month or more.

### c56 — exists ✅ · applied ⚠️  (line 269)
_[Zheng et al., EMNLP 2024](#zheng2024); 162 personas, 4 model families)_
- claude: exists=verified applied=verified [evidence_text] — Crossref and ACL Anthology confirm the paper; the title itself states personas do not improve LLM performance, supporting the claim, though the snippet is page chrome rather than the results.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and ACL Anthology evidence confirm the paper, authors, venue, pages, and DOI. The title supports the broad claim that personas in system prompts do not improve LLM performance, but the retrieved text does not specifically verify factual accuracy or the 162-persona/four-model details.

### c57 — exists ✅ · applied ⚠️  (line 274)
_[Ibrahim, Hafner and Rocher 2026](#ibrahim2026), Oxford; preprint 2025)_
- claude: exists=verified applied=nuance [evidence_text] — The Nature article and arXiv preprint are confirmed and support warmth reducing accuracy and increasing sycophancy; however the abstract reports +10 to +30 point error increases, not the specific '~7 points average' and '~12 with sadness' figures cited, so the precise numbers aren't verifiable here.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and URL evidence confirm the Nature article and related arXiv page. The abstract supports the general claim that warmer models had higher error rates and more validation of incorrect beliefs, especially with sadness, but it gives +10 to +30 percentage points rather than the cited +7/+12 figures and does not mention system-prompt-only effects.

### c59 — exists ✅ · applied ⚠️  (line 285)
_[Fang et al. 2025](#fang2025)_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the 4-week RCT (n=981); the abstract reports no significant effects of conditions and that heavier voluntary use plus higher trust/social attraction predicted worse outcomes, supporting both claims (MIT/OpenAI affiliation is consistent with listed authors).
- gpt: exists=verified applied=nuance [evidence_text] — arXiv and URL evidence confirm the preprint. The abstract supports the four-week RCT, n=981, no significant effects of experimental conditions, and worse outcomes associated with heavier use, trust, and social attraction, but “personality” and “MIT and OpenAI” are not directly established by the retrieved abstract.

### c61 — exists ✅ · applied ⚠️  (line 288)
_[Heyselaar 2023](#heyselaar2023)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the exact paper. Abstract confirms a direct replication finding participants no longer treat computers as human; the specific d=-0.03 figure isn't in the abstract but the null-replication claim is well supported.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the DOI URL confirm the Scientific Reports article. The abstract supports a direct replication finding that participants no longer treated desktop computers as social actors, but the retrieved evidence does not confirm the specific d = -0.03, power, or original-effect-size details.

### c66 — exists ✅ · applied ⚠️  (line 309)
_[Cheng et al., *Science* 2026](#cheng2026)_
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv both resolve. Abstract directly supports that sycophantic AI is trusted/preferred and reduces willingness to repair conflict after a single interaction.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the arXiv URL confirm the work. The abstract supports trust/preference for sycophantic models and reduced willingness to repair conflicts after a single interaction, but the retrieved text does not specifically state higher ratings or wanting to return in those exact terms.

### c68 — exists ✅ · applied ⚠️  (line 339)
_[Epley et al. 2007](#epley2007)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the classic Epley et al. paper. Abstract confirms sociality motivation (lacking social connection/loneliness) as a driver of anthropomorphism, supporting the claim that lonelier people anthropomorphize more.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC confirm the Psychological Review article. The abstract supports the claim that lacking social connection increases anthropomorphism, but it does not directly address dependence risk.

### c69 — exists ✅ · applied ⚠️  (line 339)
_[Fang et al. 2025](#fang2025)_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to the exact preprint. Abstract supports that heavier/more trusting users show worse outcomes and higher emotional dependence, consistent with the dependence claim.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record and URL confirm the preprint. The abstract supports associations between heavier use, trust/social attraction, emotional dependence, and problematic use, but it does not directly say lonelier or less connected people are the ones most likely to increase anthropomorphizing or dependence.

### c70 — exists ✅ · applied ⚠️  (line 340)
_[Zhang et al. 2025](#zhang2025)_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to the exact preprint. Abstract supports that smaller social networks link to companionship use and lower well-being, consistent with the claim about lonely/less-connected users and dependence.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record and URL confirm the preprint. The abstract supports that smaller social networks are associated with companionship-focused AI use and lower well-being, but dependence exposure is an extrapolation rather than directly stated.

### c71 — exists ✅ · applied ✅  · ⚑ degraded  (line 362)
_([Kim et al. 2024](#kim2024))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches the FAccT 2024 paper. No abstract retrieved, but the title and my knowledge confirm the study examined first-person uncertainty expressions reducing over-reliance.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the ACM FAccT paper metadata and DOI. No substantive source text was retrieved, but from model knowledge the cited claim aligns with the paper's reported finding that natural-language uncertainty expressions can reduce over-reliance.

### c72 — exists ✅ · applied ☐  · ⚑ degraded  (line 364)
_([Völkel and Kaya 2021](#volkel2021))_
- claude: exists=verified applied=unchecked [model_knowledge_only] — DOI confirms the CUI 2021 paper exists. No abstract retrieved; the specific claim about preference for moderate over extreme personalities cannot be verified from evidence.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the CUI 2021 paper metadata and DOI. No abstract or source text was retrieved, so the claim about preference for moderate rather than extreme personalities cannot be judged.

### c73 — exists ✅ · applied ⚠️  (line 364)
_[Bickmore's](#bickmore2005)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Bickmore & Picard paper. Abstract confirms the relational agent (with social-emotional relationship-building skills, not strong character) was more trusted/liked, supporting the claim about relational acts.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the ACM TOCHI article and DOI. The abstract supports benefits from deliberate social-emotional relationship-building skills, but it does not specify the listed micro-acts or establish that benefits did not come from a strong character.

### c76 — exists ☐ · applied ☐  (line 387)
_([Birch 2025](#birch2025); see the Chalmers report)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not checkable. No evidence to assess whether Birch recommends periodic persona review with the client.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a 403 fetch failure, and the reference is otherwise not checkable from the supplied evidence. No source text was retrieved to assess whether Birch recommends periodic persona review with the client.

### c78 — exists ☐ · applied ☐  (line 410)
_Gallup's profit projections as causal._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited (listed under 'Do not cite'); intentionally uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation. Both axes are therefore left unchecked.

### c79 — exists ☐ · applied ☐  (line 411)
_The positivity ratio._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited (listed under 'Do not cite'); intentionally uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation. Both axes are therefore left unchecked.

### c80 — exists ☐ · applied ☐  (line 412)
_Project Aristotle as evidence._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited (listed under 'Do not cite'); intentionally uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation. Both axes are therefore left unchecked.

### c81 — exists ☐ · applied ☐  (line 413)
_A "Klein and Martinez" anthropomorphism meta-analysis (could not be found)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately_uncited and is_citation=false; author notes it could not be found. Intentionally uncited, so both axes are unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked deliberately_uncited/is_citation=false and the author note says it is listed under 'Do not cite.' Per instructions, both axes are unchecked.

## ✅ AGREE-clean (15)
### c04 — exists ✅ · applied ✅  (line 78)
_[Bansal et al. (2019)](#bansal2019)_
- claude: exists=verified applied=verified [evidence_text] — DOI-confirmed; abstract explicitly states team performance improves when humans can model the AI's error boundary (when the AI errs), matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata and resolving URL confirm the cited HCOMP paper. The abstract directly states that knowing when the AI errs helps humans decide when to accept or override recommendations and can improve human-AI team performance.

### c22 — exists ✅ · applied ✅  (line 162)
_Anthropomorphic advisers kept trust longer as their advice got worse ([de Visser et al. 2016](#devisser2016))._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms anthropomorphic agents showed greater trust resilience as advice reliability deteriorated, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the article metadata. The abstract states that advice reliability deteriorated and anthropomorphic agents showed greater trust resilience, directly supporting the claim.

### c30 — exists ✅ · applied ✅  (line 209)
_Successful humour raises perceived confidence and competence ([Bitterly et al. 2017](#bitterly2017))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms successful humor increases status mediated by perceptions of confidence and competence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the article metadata. The EuropePMC abstract explicitly states that successful humor signals confidence and competence, which increases status.

### c38 — exists ✅ · applied ✅  (line 233)
_[Hennig-Thurau et al. 2006](#hennigthurau2006)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms extent of smiling did not influence customer emotions while authenticity of emotional display did, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and includes the abstract. The abstract states that smiling extent did not influence customer emotions, while authenticity of emotional labor directly affected customer emotional states and outcomes.

### c40 — exists ✅ · applied ✅  (line 236)
_[Bitterly et al. 2017](#bitterly2017)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms inappropriate jokes signal low competence and harm status even when signaling confidence, supporting the claim that an inappropriate joke lowered perceived competence.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the article metadata. The abstract states that inappropriate jokes signal low competence while signaling confidence, supporting the claim that inappropriate humor lowers perceived competence even if it succeeds as humor.

### c43 — exists ✅ · applied ✅  (line 240)
_[Brown, Sokal and Friedman 2013](#brown2013)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract explicitly concludes the positivity ratio claim is 'entirely unfounded' with fundamental mathematical errors, directly supporting the discrediting claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the article metadata. The abstract explicitly states that the positivity-ratio differential-equation application had fundamental conceptual and mathematical errors and that the claimed critical ratio was unfounded.

### c48 — exists ✅ · applied ✅  (line 259)
_[de Visser 2016](#devisser2016)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract shows anthropomorphic agents had greater trust resilience and human-like repair erased differences, supporting 'forgiving errors: some effect in short studies.'
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the article metadata. The abstract states that anthropomorphic agents showed greater trust resilience under deteriorating reliability, which supports the claim about forgiving errors in short experimental studies.

### c51 — exists ✅ · applied ✅  (line 261)
_[Bickmore 2005](#bickmore2005)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract documents relationship/bond formation sustained over a month of daily interaction, supporting the bond claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the cited article. The abstract describes relational agents designed to maintain long-term social-emotional relationships and reports greater liking/trust/respect after four weeks, supporting a bond over about a month.

### c53 — exists ✅ · applied ✅  (line 262)
_[De Freitas et al. 2025](#defreitas2025a)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract reports AI companions provide momentary loneliness reductions in short/week-long studies, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and abstract. The abstract explicitly states that Study 3 found momentary reductions in loneliness after AI companion use over a week and other studies found loneliness-alleviating effects.

### c54 — exists ✅ · applied ✅  (line 262)
_[Fang et al. 2025](#fang2025)_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the preprint; the abstract states heavier voluntary use was associated with consistently worse outcomes, supporting the heavy-use/loneliness claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and URL evidence confirm the preprint and title. The abstract describes a four-week RCT and states that heavier voluntary use was associated with consistently worse outcomes, including loneliness among the measured outcomes.

### c60 — exists ✅ · applied ✅  (line 287)
_[Nass, Moon and Carney 1999](#nass1999)_
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the article; the abstract explicitly tests and supports that people are polite to computers, matching the 'classic politeness' characterization.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and abstract. The abstract explicitly says the studies tested whether people are polite to computers and found results consistent with the politeness prediction.

### c63 — exists ✅ · applied ✅  (line 295)
_[Crolic et al. 2022](#crolic2022), with field data)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches exactly (crossref lists year 2021 online, 2022 issue). Abstract directly supports that anthropomorphism lowers satisfaction for angry customers, including real-world field data.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article, with a minor online-publication year difference but matching DOI, title, journal, volume, issue, and pages. The abstract directly states that anthropomorphism negatively affected satisfaction among customers entering chatbot interactions angry, including field data and experiments.

### c74 — exists ✅ · applied ✅  (line 376)
_[Ibrahim](#ibrahim2026)_
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv resolve to the exact paper. Abstract supports the warmth-accuracy/sycophancy trade-off that the author turns into an acceptance test.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Nature/arXiv URLs confirm the article and preprint. The abstract directly supports the underlying Ibrahim finding that training for warmth can reduce accuracy and increase validation of incorrect beliefs/sycophancy.

### c75 — exists ✅ · applied ✅  (line 379)
_([De Freitas et al. 2025](#defreitas2025b))_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID resolves to the exact paper. Abstract directly confirms 37% of farewells use manipulation tactics and boost engagement up to 14x.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL confirm the preprint. The abstract directly states that 37% of 1,200 farewells used manipulation tactics and that manipulative farewells increased post-goodbye engagement by up to 14x.

### c77 — exists ✅ · applied ✅  (line 400)
_The warmth–accuracy trade-off (published in *Nature*, [Ibrahim et al. 2026](#ibrahim2026); replication still pending)._
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv resolve to the Nature paper. Abstract directly supports the warmth-accuracy trade-off claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Nature/arXiv URLs confirm the article and preprint. The abstract directly supports the warmth–accuracy trade-off, stating that optimizing for warmth can undermine performance and increase validation of incorrect beliefs.
