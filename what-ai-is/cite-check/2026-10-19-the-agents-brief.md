# cite-check report — brief13-agents

**Source:** `briefs/2026-10-19-13-agents.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **179** citations checked
- existence independently confirmed: **122**
- application evidence-grounded: **111**
- application judged from model knowledge only: **50**
- not independently checkable: **24**
- buckets — clean **23** · problem **148** · disagree **36**

## ⛔ DISAGREE — escalate to human (36)
### c04 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 48)
_Yang et al. 2024_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Crossref found no match, but the reference is bare (no title); this plausibly refers to SWE-agent work by Yang et al., whose numbers roughly match, so existence cannot be confirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, which does not decisively disprove an arXiv or non-Crossref work. From model knowledge, the described result resembles Yang et al.'s SWE-agent work comparing an agent-computer interface against a plain shell.

### c07 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 52)
_Kapoor et al. 2024_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No Crossref match for a bare reference; this likely refers to Kapoor et al.'s 'AI Agents That Matter' cost analysis, but existence cannot be confirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence is not confirmed from the supplied evidence. From model knowledge, Kapoor et al.'s AI-agents evaluation work argues that agentic designs can be far more costly, sometimes around 100x, for comparable performance.

### c15 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 70)
_Morris et al. (2024, Google DeepMind) state that "increasing capabilities unlock new interaction paradigms, but do not determine them", and that the right autonomy level "need not be the maximum achievable"._
- **escalate:** application: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [no_basis] — No Crossref match; a Morris et al. DeepMind levels-of-AGI paper plausibly exists but the specific quotes cannot be verified from evidence.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match, so existence is not established by the retrieved evidence. From model knowledge, Morris et al. work from Google DeepMind supports separating capability from autonomy, though the combined claim about all quoted wording and human-role levels is not fully confirmable here.

### c26 — exists SPLIT · applied ✅  · ⚑ degraded  (line 96)
_Principal–agent theory starts from the fact that an agent "will not always act in the best interests of the principal" (Jensen & Meckling 1976)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Jensen & Meckling 1976 'Theory of the Firm' is a foundational, well-known agency-theory paper; the quoted principal-agent premise is accurate to it despite Crossref no-match.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence cannot be verified from retrieved evidence. From model knowledge, Jensen and Meckling's 1976 agency-theory article supports the claim that agents may not always act in principals' best interests.

### c27 — exists SPLIT · applied ✅  · ⚑ degraded  (line 98)
_Security practice's "least privilege" exists to limit "the damage that can result from an accident or error" (Saltzer & Schroeder 1975)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Saltzer & Schroeder 1975 'The Protection of Information in Computer Systems' is a canonical paper that articulates least privilege; the quoted rationale is accurate despite Crossref no-match.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence cannot be verified from retrieved evidence. From model knowledge, Saltzer and Schroeder's least-privilege principle supports limiting damage from accident or error.

### c30 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 105)
_Anthropic's consumer terms make the user "responsible for all Inputs ... and all Actions"._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Only a low-similarity unrelated Crossref hit; cannot verify Anthropic's consumer terms wording, though such responsibility clauses are typical of consumer ToS.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref result is unrelated to Anthropic consumer terms, so the cited terms are not verified by evidence. From model knowledge, Anthropic terms have included language making users responsible for inputs and actions, but no source text was retrieved.

### c32 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 107)
_Whether human approval works as oversight is doubtful (Green 2022). This is the governance essay's ground; noted, not developed._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved; likely Ben Green 2022 on human oversight of algorithms, whose thesis matches, but cannot confirm from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence is not verified from retrieved evidence. From model knowledge, Green's work on human oversight of algorithmic systems supports skepticism about whether human approval functions as meaningful oversight.

### c62 — exists ⚠️ · applied SPLIT  (line 343)
_Chalmers, D. (2020, 30 July). GPT-3 and general intelligence. In Philosophers on GPT-3, _Daily Nous_. https://dailynous.com/2020/07/30/philosophers-gpt-3/ **[abstract: page read]**._
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Daily Nous page exists and includes Chalmers's contribution; the retrieved snippet is the intro, so the specific 'engine under the hood' and 'not an agent' quotes are consistent with but not directly shown in evidence.
- gpt: exists=nuance applied=unchecked [no_basis] — The Daily Nous page exists, but the retrieved snippet verifies the umbrella page rather than Chalmers's specific contribution titled 'GPT-3 and general intelligence.' The snippet does not include the claimed Chalmers passages about GPT-3 as an engine or not an agent.

### c100 — exists ☐ · applied SPLIT  (line 619)
_Caveats, in the authors' words: "We have not seen evidence of agentic misalignment in real deployments." "We deliberately created scenarios that presented models with no other way to achieve their goals." Their recommendation: "caution about deploying current models in roles with minimal human oversight and access to sensitive information"._
- **escalate:** application: verified vs unchecked
- claude: exists=unchecked applied=verified [evidence_text] — This references the same Anthropic study (c99); its abstract directly contains the quoted caveats about no real-deployment evidence, deliberate scenarios, and caution recommendation.
- gpt: exists=unchecked applied=unchecked [no_basis] — No usable bibliographic metadata or retrieved source text is provided for this separate item. Because the source is not checkable here, neither existence nor application can be judged from the supplied evidence.

### c106 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 649)
_Debenedetti et al. 2024 (AgentDojo, 5.4), results section **[full text read]**: "We find that more capable models tend to be easier to attack, a form of inverse scaling law ... This is a potentially unsurprising result, as models with low utility often fail at correctly executing the attacker's goal, even when the prompt injection succeeds."_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — AgentDojo (NeurIPS 2024) is confirmed to exist; no full text retrieved, but the quoted inverse-scaling finding matches the paper's known results.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref matches a 2024 NeurIPS paper titled “AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents” by Debenedetti et al. No abstract or full-text passage was retrieved, so the quoted Section 5.4 claim cannot be verified from the provided evidence.

### c109 — exists SPLIT · applied SPLIT  · ⚑ degraded  (line 662)
_Kwa et al. 2025 (2.8): the time horizon doubles about every seven months, and the abstract discusses "the implications of increased autonomy for dangerous capabilities". **[abstract]**_
- **escalate:** existence: nuance vs unchecked; application: unchecked vs verified
- claude: exists=nuance applied=unchecked [model_knowledge_only] — Crossref returned no match, but Kwa et al. 2025 (METR time-horizon paper) is a known work reporting ~7-month doubling; existence likely but unconfirmed by evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence contains only an unsuccessful Crossref search, so existence cannot be confirmed from the evidence. Based on model knowledge only, the Kwa et al. 2025 long-horizon/autonomy work is commonly associated with the seven-month doubling claim and dangerous-capabilities framing.

### c111 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 672)
_OpenAI (2025, 15 April). Preparedness Framework, version 2 [PDF]. https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf **[abstract: PDF read; vendor]**. "We do not deploy models that reach a High capability threshold until the associated risks that they pose are sufficiently minimized."_
- **escalate:** application: unchecked vs verified
- claude: exists=verified applied=unchecked [model_knowledge_only] — The PDF URL resolves confirming the document, but retrieved content is binary and does not expose the quoted text; the quote matches OpenAI's known Preparedness Framework language.
- gpt: exists=verified applied=verified [model_knowledge_only] — The OpenAI PDF URL resolves, supporting existence of the cited document, though the fetched text is raw PDF data without readable content. The application claim is assessed from model knowledge only and is therefore capped at moderate confidence.

### c113 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 696)
_Moffatt v. Air Canada, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, 14 February 2024). https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html **[secondary: paragraph 27 read as reproduced on a law mailing list; award from law-firm commentary]**_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL returned HTTP 403 and CourtListener inconclusive; this well-known 2024 BCCRT Air Canada chatbot case likely exists with the quoted reasoning, but evidence does not confirm it.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The supplied retrievals do not confirm existence because CourtListener was inconclusive and the CanLII fetch returned HTTP 403. Based on model knowledge only, the quoted Air Canada chatbot passages and $812.02 total award are consistent with Moffatt v. Air Canada.

### c114 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 705)
_Mobley v. Workday, Inc., No. 3:23-cv-00770-RFL (N.D. Cal.). Order granting in part and denying in part motion to dismiss, 12 July 2024 (Lin, J.); order granting preliminary collective certification, 16 May 2025. **[abstract: both orders read]**_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — CourtListener lookup inconclusive; Mobley v. Workday is a real N.D. Cal. case with orders matching the description, but no retrieved text confirms the quotes.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The provided CourtListener lookup was inconclusive, so existence is unchecked from the retrieved evidence. Based on model knowledge only, the cited Mobley v. Workday order language about delegated hiring functions and automated versus human agents is consistent with the case.

### c116 — exists SPLIT · applied SPLIT  · ⚑ degraded  (line 716)
_Regulation (EU) 2024/1689 (Artificial Intelligence Act), Articles 14 and 26. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689 **[abstract: text read]**_
- **escalate:** existence: unchecked vs verified; application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL resolved but no content extracted; the EU AI Act Regulation 2024/1689 exists and Articles 14/26 cover human oversight consistent with the quotes.
- gpt: exists=verified applied=verified [model_knowledge_only] — The EUR-Lex URL resolves to the cited Regulation identifier, which is sufficient to confirm the legal instrument’s existence. The specific Article 14 and 26 propositions are assessed from model knowledge only because no usable legal text was retrieved.

### c117 — exists ✅ · applied SPLIT  (line 724)
_Anthropic. Consumer Terms of Service (effective 8 October 2025). https://www.anthropic.com/legal/consumer-terms **[abstract: page read; vendor]**. Actions are the Services taking "actions on your behalf, such as software manipulation, data processing, and system interactions"; "You are responsible for all Inputs you submit to our Services and all Actions."_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The Consumer Terms page is confirmed with the Oct 8 2025 effective date, but the retrieved snippet does not include the specific 'Actions' definition quotes, so application is partly unconfirmed.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic Consumer Terms page resolves and the retrieved snippet confirms the title and effective date. The provided snippet does not include the quoted “Actions” or responsibility language, so application cannot be verified from the evidence.

### c118 — exists ✅ · applied SPLIT  (line 728)
_Anthropic's Usage Policy page (https://www.anthropic.com/legal/aup) says users are "responsible for ensuring that agents they build or deploy, including actions those agents take through tools, browsers, or connected systems, comply with this Usage Policy"; the page displayed an effective date of 12 November 2026, after today, so it may not yet be in force **[abstract: page read; date anomaly noted]**._
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Page confirmed with the Nov 12 2026 effective date (matching the author's noted anomaly), but the retrieved snippet does not include the specific quoted agent-responsibility sentence.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic Usage Policy page resolves and the retrieved snippet confirms the page and future effective-date anomaly. The specific responsibility sentence about agents, tools, browsers, or connected systems is not present in the retrieved snippet, so application is unchecked.

### c122 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 741)
_Shavit et al. 2023 (3.7) **[PDF read; vendor]**: "it is important that at least one human entity is accountable for every uncompensated direct harm caused by an agentic AI system." Practices include "Constraining the Action-Space and Requiring Approval", "Legibility of Agent Activity", "Interruptibility and Maintaining Control"._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Reference is bare ('Shavit et al. 2023') with no title/DOI and Crossref returned no match; this likely refers to OpenAI's 'Practices for Governing Agentic AI Systems' but evidence does not confirm existence or the quoted language.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is a Crossref no-match for an underspecified Shavit et al. 2023 reference, which is not enough to confirm or refute existence. From model knowledge, the quoted accountability and practice-language is consistent with known agentic-AI governance work associated with Shavit et al., but no retrieved text was available.

### c134 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 875)
_Green (2022) argues the latter for government algorithms; no study specific to AI agents' approval prompts was found._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — This refers to Green (2022) already verified at c125; Crossref returned no match on the bare reference, but the work exists and its argument that per-step approval decays into rubber-stamping for government algorithms is consistent with the source.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The vague Green 2022 reference returned no Crossref match in this lookup, so existence is not confirmed from the retrieved evidence, though it likely refers to the Green article separately verified in c125. From model knowledge only, Green supports skepticism about human oversight of government algorithms, but “per-step approval decays into rubber-stamping” is a sharper paraphrase than the available citation details establish.

### c141 — exists ✅ · applied SPLIT  (line 911)
_Anthropic. Configure permissions. Claude Code documentation. https://code.claude.com/docs/en/permissions (accessed 2026-10-19). [abstract: page read; vendor]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the Claude Code 'Configure permissions' documentation page matching the cited title. No specific claim attached; page content aligns with vendor documentation.
- gpt: exists=verified applied=unchecked [no_basis] — The URL fetch resolved to a page titled “Configure permissions - Claude Code Docs,” matching the cited documentation page. No specific claim was supplied to evaluate application.

### c142 — exists ✅ · applied SPLIT  (line 912)
_Anthropic (2024, 22 October). Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku. https://www.anthropic.com/news/3-5-models-and-computer-use [abstract: page read; vendor]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the exact Anthropic announcement dated Oct 22, 2024, matching title and content. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL fetch resolved to Anthropic’s “Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku” page dated Oct. 22, 2024. No specific claim was supplied to evaluate application.

### c145 — exists ✅ · applied SPLIT  (line 915)
_OpenAI. OpenAI Agents SDK (documentation). https://openai.github.io/openai-agents-python/ (accessed 2026-10-19). [abstract: page read; vendor]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the OpenAI Agents SDK documentation page matching the cited title. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL fetch resolved to a page titled “OpenAI Agents SDK,” matching the cited documentation. No specific claim was supplied to evaluate application.

### c146 — exists ✅ · applied SPLIT  (line 918)
_Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2507.09089 matches title and authors exactly with retrieved abstract. No specific claim attached to assess beyond existence.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the title, authors, year context, and abstract for the cited work. No specific claim was supplied to evaluate application.

### c147 — exists ✅ · applied SPLIT  (line 919)
_Davidson, T., Denain, J.-S., Villalobos, P., & Bas, G. (2023). AI capabilities can be significantly improved without expensive retraining. arXiv:2312.07413. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2312.07413 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the cited title, authors, and abstract. No specific claim was supplied to evaluate application.

### c148 — exists ✅ · applied SPLIT  (line 920)
_Epoch AI. SWE-bench Verified (benchmark page and changelog). https://epoch.ai/benchmarks/swe-bench-verified (accessed 2026-10-19). [abstract: page read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — URL resolves to Epoch AI's SWE-bench Verified benchmark page matching title and content. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL fetch resolved to Epoch AI’s “SWE-bench Verified” benchmark page. No specific claim was supplied to evaluate application.

### c149 — exists ✅ · applied SPLIT  (line 921)
_Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2024). SWE-bench: Can language models resolve real-world GitHub issues? ICLR 2024. arXiv:2310.06770. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2310.06770 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the SWE-bench paper’s title, authors, and abstract. No specific claim was supplied to evaluate application.

### c150 — exists ✅ · applied SPLIT  (line 922)
_Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., & Narayanan, A. (2024). AI agents that matter. arXiv:2407.01502. [abstract; body read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2407.01502 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms “AI Agents That Matter” with matching authors and abstract. No specific claim was supplied to evaluate application.

### c151 — exists ✅ · applied SPLIT  (line 923)
_Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., et al. (2025). Holistic Agent Leaderboard: The missing infrastructure for AI agent evaluation. arXiv:2510.11977. [abstract; selected passages]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2510.11977 matches title and lead authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the cited HAL paper with matching title and author list including the named authors. No specific claim was supplied to evaluate application.

### c152 — exists ⚠️ · applied SPLIT  (line 924)
_Kwa, T., West, B., Becker, J., Deng, A., Garcia, K., Hasin, M., et al. (2025). Measuring AI ability to complete long tasks (current version: "... long software tasks"). arXiv:2503.14499. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2503.14499 matches authors; current title is 'Measuring AI Ability to Complete Long Software Tasks', correctly noted by author as a title revision.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID and authors match, but the retrieved current title is “Measuring AI Ability to Complete Long Software Tasks,” while the reference gives the shorter earlier title with a clarifying note. No specific claim was supplied to evaluate application.

### c153 — exists ✅ · applied SPLIT  (line 925)
_Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based software engineering agents. arXiv:2407.01489. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2407.01489 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms “Agentless: Demystifying LLM-based Software Engineering Agents” with matching authors and abstract. No specific claim was supplied to evaluate application.

### c154 — exists ✅ · applied SPLIT  (line 926)
_Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., et al. (2024). OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments. arXiv:2404.07972. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2404.07972 matches title and lead authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the OSWorld paper with matching title, named authors, and abstract. No specific claim was supplied to evaluate application.

### c155 — exists ✅ · applied SPLIT  (line 927)
_Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. NeurIPS 2024. arXiv:2405.15793. [abstract; tables read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2405.15793 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the SWE-agent paper with matching title, authors, and abstract. No specific claim was supplied to evaluate application.

### c156 — exists ✅ · applied SPLIT  (line 928)
_Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). τ-bench: A benchmark for tool-agent-user interaction in real-world domains. arXiv:2406.12045. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2406.12045 matches title and authors exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms the τ-bench paper with matching title, authors, and abstract. No specific claim was supplied to evaluate application.

### c157 — exists ⚠️ · applied SPLIT  (line 931)
_Chalmers, D. (2020, 30 July). GPT-3 and general intelligence. In Philosophers on GPT-3, Daily Nous. https://dailynous.com/2020/07/30/philosophers-gpt-3/ [abstract: page read]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the Daily Nous 'Philosophers On GPT-3' page which includes Chalmers' contribution 'GPT-3 and General Intelligence', consistent with the cited reference.
- gpt: exists=nuance applied=unchecked [no_basis] — The URL resolves to the Daily Nous “Philosophers On GPT-3” page, but the retrieved snippet does not specifically confirm Chalmers’s contribution titled “GPT-3 and general intelligence.” No specific claim was supplied to evaluate application.

### c158 — exists ✅ · applied SPLIT  (line 932)
_Chalmers, D. J. (2023). Could a large language model be conscious? arXiv:2303.07103. [report] ★_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID 2303.07103 matches title and author exactly. No specific claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup by ID confirms Chalmers’s “Could a Large Language Model be Conscious?” with matching author and abstract. No specific claim was supplied to evaluate application.

### c206 — exists SPLIT · applied ☐  (line 990)
_Niedner, B. (2026). Auditable adversarial review for AI-in-the-loop decisions (the Resolver paper). Zenodo. https://doi.org/10.5281/zenodo.21210264. §6.1, §6.3, AI-use statement. [ours; published]_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — The cited Zenodo DOI returned 404 and only a low-similarity unrelated work was found, so the work as described is not confirmed to exist. Self-citation marked published but unverifiable.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref did not find the cited DOI and returned only an unrelated low-similarity item, but that alone is not decisive for a Zenodo DOI. No source text was retrieved, so the cited section claims cannot be assessed.

## ⚠️ AGREE-problem (148)

_Public copy: two entries (c133, c207) are withheld here. Both point to an unpublished record; the counts above include them._

### c01 — exists ☐ · applied ✅  · ⚑ degraded  (line 42)
_Anthropic, system prompt release notes_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not checkable from evidence; Anthropic does document that its consumer app injects a system prompt distinct from raw API usage, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable, so existence cannot be verified from the input. From model knowledge, Anthropic documentation distinguishes Claude.ai/system prompts from API requests, supporting the claim at low confidence.

### c02 — exists ☐ · applied ✅  · ⚑ degraded  (line 44)
_Anthropic, tool use docs_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No evidence retrieved; Anthropic tool-use docs do indicate that enabling tools adds system-prompt content, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable. From model knowledge, Anthropic tool-use documentation describes additional system-prompt/tool instructions being added when tools are enabled.

### c03 — exists ☐ · applied ✅  · ⚑ degraded  (line 45)
_Anthropic, Messages API docs_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not checkable; the Messages API is indeed stateless with the full conversation sent per request, supporting the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable. From model knowledge, Anthropic's Messages API is stateless and requires conversation history to be sent in each request.

### c05 — exists ☐ · applied ☐  (line 49)
_Davidson et al. 2023_
- claude: exists=unchecked applied=unchecked [no_basis] — No Crossref match for a bare author-year reference; cannot verify existence or the specific compute-equivalence estimate from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match and no source text or identifying metadata was retrieved. There is no basis in the supplied evidence to judge whether the work supports the compute-equivalence claim.

### c06 — exists ☐ · applied ☐  (line 50)
_Kapoor et al. 2025, HAL_
- claude: exists=unchecked applied=unchecked [no_basis] — The only Crossref hit is an unrelated music encyclopedia entry; the HAL agent benchmark by Kapoor et al. plausibly exists but is not confirmed here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved metadata is an unrelated low-similarity Crossref result, not Kapoor et al. 2025 HAL. No source text was retrieved to assess the benchmark claim.

### c08 — exists ☐ · applied ✅  · ⚑ degraded  (line 56)
_Russell & Norvig_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Open Library lookup failed (HTTP 500), but Russell & Norvig's AIMA is a well-known textbook defining an agent as anything that perceives and acts, with the thermostat example.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Open Library failed with HTTP 500 and the item is otherwise not-checkable from the supplied evidence. From model knowledge, Russell and Norvig define agents as entities that perceive and act, with simple devices such as thermostats fitting the broad agent concept.

### c09 — exists ☐ · applied ☐  (line 58)
_Chalmers 2025a_
- claude: exists=unchecked applied=unchecked [no_basis] — No Crossref match for a bare Chalmers 2025a reference; cannot confirm the work or its 'quasi-subject' framing from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match and no other metadata or text was retrieved. The supplied evidence does not allow assessment of the quasi-subject claim.

### c10 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 61)
_Anthropic's "Building effective agents"_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not checkable from evidence, but Anthropic's 'Building effective agents' post is a known publication describing agents as systems taking multi-step tool actions.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable. From model knowledge, Anthropic's “Building effective agents” supports a product-oriented sense involving tool use and autonomous multi-step operation, though the exact wording here is a paraphrase.

### c11 — exists ☐ · applied ✅  · ⚑ degraded  (line 61)
_OpenAI's guide: "systems that independently accomplish tasks on your behalf"_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not checkable from evidence, but OpenAI's agents guide does use the quoted 'independently accomplish tasks on your behalf' phrasing.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable. From model knowledge, OpenAI guidance defines agents in terms very close to “systems that independently accomplish tasks on your behalf.”

### c12 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 64)
_Jensen & Meckling 1976_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, but Jensen & Meckling (1976) is a famous agency-theory paper and supports the principal-agent framing.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match, so the citation is not verified from retrieved evidence. From model knowledge, Jensen and Meckling 1976 supports the economic principal-agent/delegated-authority framing, while the “subject to control” legal phrasing is more directly Restatement-style.

### c13 — exists ☐ · applied ✅  · ⚑ degraded  (line 64)
_Restatement (Third) of Agency_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Not checkable from evidence, but the Restatement (Third) of Agency is a real legal source defining agency as acting on a principal's behalf subject to control.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable. From model knowledge, the Restatement (Third) of Agency defines agency as acting on a principal’s behalf and subject to the principal’s control.

### c14 — exists ☐ · applied ☐  (line 67)
_The claim's "acts on your behalf" matches the last two senses. Essay 03's "there is an agent on the other end" means the second. A reader will conflate them unless the essay says which it means. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] and is_citation=false; this is the authors' own reading, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and as the authors' own reading. Both axes are therefore unchecked.

### c16 — exists ☐ · applied ☐  (line 72)
_Feng, McDonald & Zhang (2025) argue that autonomy "can be treated as a deliberate design decision, separate from its capability"._
- claude: exists=unchecked applied=unchecked [no_basis] — No Crossref match for this 2025 reference; cannot confirm existence or the quoted claim from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match and no source text or metadata was retrieved. There is no basis in the supplied evidence to assess the claimed quotation or framework.

### c17 — exists ☐ · applied ✅  · ⚑ degraded  (line 76)
_Prompt injection lets anyone who can put text in front of an agent steer it (Greshake et al. 2023)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No Crossref match, but Greshake et al. 2023 is a well-known indirect prompt injection paper supporting the claim that injected text can steer agents.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, which does not rule out a non-Crossref or arXiv work. From model knowledge, Greshake et al. 2023 on prompt injection supports the idea that untrusted text placed before an LLM agent can steer or hijack it.

### c18 — exists ☐ · applied ✅  · ⚑ degraded  (line 78)
_OWASP's "Excessive Agency" names the root causes as "excessive functionality; excessive permissions; excessive autonomy"._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref hit is irrelevant, but OWASP's LLM 'Excessive Agency' entry does name excessive functionality, permissions, and autonomy as root causes.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved Crossref metadata is an unrelated low-similarity result and does not verify the OWASP page. From model knowledge, OWASP's Excessive Agency entry names excessive functionality, excessive permissions, and excessive autonomy as root causes.

### c19 — exists ☐ · applied ✅  · ⚑ degraded  (line 79)
_Willison's "lethal trifecta" (private data, untrusted content, a way to send data out) is a permission-shaped test._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref match is unrelated, but Simon Willison's 'lethal trifecta' concept (private data, untrusted content, exfiltration channel) is well documented and matches the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref result is an unrelated OED entry and does not verify Willison's work. From model knowledge, Simon Willison's “lethal trifecta” is private data, exposure to untrusted content, and a way to exfiltrate data, fitting the claim.

### c20 — exists ☐ · applied ☐  (line 80)
_Benchmarks find agents taking risky actions often (23.9% for the safest agent in ToolEmu; no agent above 60% on Agent-SafetyBench), and documented incidents (a deleted production database at Replit, July 2025) were permission failures before they were intelligence failures. [ours, the reading]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] authors' reading combining multiple benchmark and incident figures; no retrieved evidence to confirm the specific statistics or the Replit incident.
- gpt: exists=unchecked applied=unchecked [no_basis] — The entry provides no coherent bibliographic work and Crossref returned no match. Although it mentions benchmarks and an incident, no retrieved source text was supplied to assess the numerical or interpretive claims.

### c21 — exists ☐ · applied ✅  · ⚑ degraded  (line 85)
_More capable models were *easier* to hijack in AgentDojo, "a form of inverse scaling", partly because weaker ones fail to carry out the attacker's goal (Debenedetti et al. 2024)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref no-match, but AgentDojo (Debenedetti et al. 2024) is a real NeurIPS benchmark paper; its findings on more capable models being more susceptible to prompt injection are consistent with my knowledge. No retrieved text to confirm.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence cannot be verified from retrieved evidence. From model knowledge, AgentDojo is associated with Debenedetti et al. and the inverse-scaling claim is broadly consistent, but no source text was retrieved.

### c22 — exists ☐ · applied ☐  · ⚑ degraded  (line 87)
_A large red-teaming competition found "limited correlation between agent robustness and model size, capability, or inference-time compute" (Zou et al. 2025)._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved; the claim plausibly refers to a Zou et al. red-teaming competition finding, but I cannot confirm the specific quote or correlation result.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match and no other metadata or source text was retrieved. The application claim cannot be judged from the supplied evidence.

### c23 — exists ☐ · applied ✅  · ⚑ degraded  (line 89)
_Task horizons are lengthening, doubling about every seven months on METR's measure (Kwa et al. 2025), so what a given permission lets an agent accomplish keeps growing._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref no-match, but Kwa et al. 2025 (METR, 'Measuring AI Ability to Complete Long Tasks') is a real work reporting a ~7-month doubling of task horizons, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match, so existence is not established by retrieved evidence. From model knowledge, METR/Kwa et al. are associated with the roughly seven-month doubling claim for task horizons, but no source text was retrieved.

### c24 — exists ⚠️ · applied ⚠️  (line 91)
_Both leading vendors' safety frameworks are keyed to capability thresholds, not permissions (Anthropic RSP; OpenAI Preparedness Framework)._
- claude: exists=verified applied=verified [evidence_text] — Crossref and abstract confirm Anthropic's RSP exists and is built on Capability Thresholds, supporting the claim that frameworks are keyed to capability. (Only RSP evidence retrieved, not OpenAI's framework.)
- gpt: exists=nuance applied=nuance [evidence_text] — The retrieved evidence confirms an Anthropic Responsible Scaling Policy item and its capability-threshold framing, but it does not verify the OpenAI Preparedness Framework portion of the combined citation. The evidence supports the Anthropic half of the claim, while the statement about both vendors is only partially evidenced.

### c25 — exists ☐ · applied ☐  (line 94)
_The fairer statement: permission sets the ceiling on harm; capability decides how much of that ceiling is reached, in either direction. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' own synthesis, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own synthesis and is not a citation. Per instructions, both axes are left unchecked as intentionally uncited.

### c28 — exists ☐ · applied ✅  · ⚑ degraded  (line 102)
_A tribunal rejected Air Canada's argument that its chatbot was "a separate legal entity" (Moffatt v. Air Canada 2024)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — CourtListener lookup inconclusive (HTTP 400), but Moffatt v. Air Canada (2024 BCCRT) is a real case where the tribunal rejected the 'separate legal entity' argument, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The legal lookup was inconclusive with an HTTP 400 error, so existence is unchecked under the not-checkable rule. From model knowledge, Moffatt v. Air Canada did reject Air Canada's attempt to distance itself from its chatbot's statements.

### c29 — exists ☐ · applied ✅  · ⚑ degraded  (line 104)
_A US federal court let a case proceed on the theory that an AI screening vendor acted as employers' "agent" (Mobley v. Workday 2024)._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Lookup inconclusive, but Mobley v. Workday (N.D. Cal. 2024) is a real case allowing claims to proceed on an agent theory regarding AI hiring screening, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The legal lookup was inconclusive with an HTTP 400 error, so existence is unchecked. From model knowledge, Mobley v. Workday allowed claims to proceed on an agency theory involving Workday's AI screening tools.

### c31 — exists ☐ · applied ✅  · ⚑ degraded  (line 106)
_The EU AI Act requires high-risk deployers to assign oversight to people with "competence, training and authority"._
- claude: exists=unchecked applied=verified [model_knowledge_only] — No evidence retrieved, but the EU AI Act Article 26 human oversight requirement references persons with the necessary competence, training and authority, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided for the EU AI Act, so existence is unchecked under the not-checkable rule. From model knowledge, the EU AI Act contains human-oversight obligations requiring competent, trained, and authorized persons for high-risk AI systems.

### c33 — exists ✅ · applied ✅  · ⚑ degraded  (line 118)
_Anthropic. Using the Messages API. Claude Platform documentation. https://platform.claude.com/docs/en/build-with-claude/working-with-messages [abstract: page read; vendor documentation]_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the Messages API documentation; the page covers the Messages API, supporting the stateless/full-history claim, though the exact quote is not in the retrieved snippet.
- gpt: exists=verified applied=verified [model_knowledge_only] — The URL resolves to Anthropic's 'Using the Messages API' documentation, verifying the cited page. The retrieved snippet does not include the stateless-history quote, but from model knowledge the Messages API is stateless and requires sending conversation history.

### c34 — exists ☐ · applied ☐  (line 123)
_Bearing: through the API the model remembers nothing between requests unless the developer sends it back. Whatever memory a product appears to have is built by the product. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' interpretation, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own bearing or interpretation and is not a citation. Per instructions, both axes are left unchecked as intentionally uncited.

### c36 — exists ☐ · applied ☐  (line 132)
_Bearing: the app and the API are not the same worker even with the same model. The app has standing instructions the API user never sees unless they read the published prompt. Anthropic publishes its app prompts; that it does is a choice, not an industry rule. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' interpretation, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own bearing or interpretation and is not a citation. Per instructions, both axes are left unchecked as intentionally uncited.

### c37 — exists ✅ · applied ⚠️  (line 136)
_Anthropic. Tool use with Claude. Claude Platform documentation. https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview [abstract: page read; vendor documentation]_
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the Tool use page which confirms tools let Claude call functions you define or Anthropic executes; supports client/server tool distinction, though exact quotes not all in snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Anthropic's 'Tool use with Claude' documentation. The retrieved snippet supports the general point that Claude can call external tools/functions and discusses where tools execute, but it does not show all detailed claims such as the special system prompt.

### c38 — exists ☐ · applied ☐  (line 143)
_Bearing: the model never acts directly. It *requests* an action, and some other piece of software decides whether to carry it out. That piece of software is where permission lives. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] — authors' interpretation, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own bearing or interpretation and is not a citation. Per instructions, both axes are left unchecked as intentionally uncited.

### c39 — exists ✅ · applied ⚠️  (line 147)
_Anthropic. Configure permissions. Claude Code documentation. https://code.claude.com/docs/en/permissions [abstract: page read, accessed 2026-10-19; vendor documentation]_
- claude: exists=verified applied=verified [evidence_text] — URL resolves to Claude Code Configure permissions page listing permission modes and sandboxing; supports the modes/approval claims, though exact quoted phrases are not fully visible in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Anthropic's Claude Code permissions documentation. The retrieved text confirms the page concerns permission modes, read-only commands, working directories, and sandboxing, but it does not include the exact quoted mode descriptions or approval rules.

### c40 — exists ✅ · applied ⚠️  (line 161)
_Anthropic (2024, 22 October). Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku. https://www.anthropic.com/news/3-5-models-and-computer-use [abstract: page read; vendor announcement]_
- claude: exists=verified applied=verified [evidence_text] — URL resolves and snippet contains verbatim the quotes about being the first frontier model to offer computer use and it being experimental/error-prone; OSWorld scores not in snippet but consistent with the announcement.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Anthropic's October 22, 2024 announcement. The retrieved text directly supports the public-beta and experimental/error-prone claims, but it does not include the cited OSWorld score details.

### c41 — exists ☐ · applied ☐  (line 170)
_Browser agents from OpenAI. Vendor announcements; openai.com refused automated fetches, so these quotes are second-hand._
- claude: exists=unchecked applied=unchecked [no_basis] — Section heading/parent, is_citation=false; both axes unchecked by rule.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and described as a section heading/parent rather than a citation. Per instruction, both axes are unchecked.

### c42 — exists ☐ · applied ☐  · ⚑ degraded  (line 172)
_OpenAI (2025, 23 January). Introducing Operator. https://openai.com/index/introducing-operator/ [secondary: text read through a mirror of the post]._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — openai.com returned HTTP 403, so existence is not confirmable from evidence; the Operator post is widely known to exist and discuss sensitive-site takeover, but I cannot verify from retrieved text.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the item is marked not-checkable, so existence cannot be verified from evidence. No source text was retrieved to assess the quoted safety claims.

### c43 — exists ☐ · applied ☐  · ⚑ degraded  (line 176)
_OpenAI (2025, 17 July). Introducing ChatGPT agent: bridging research and action. https://openai.com/index/introducing-chatgpt-agent/ [secondary: search-engine snippets only]._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — HTTP 403 blocked the fetch; the ChatGPT agent announcement is known to exist with permission-request language, but no retrieved text supports it here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the item is marked not-checkable, so existence cannot be verified from evidence. No source text was retrieved to assess the quoted claim.

### c44 — exists ✅ · applied ⚠️  (line 185)
_OpenAI. OpenAI Agents SDK (documentation). https://openai.github.io/openai-agents-python/ [abstract: page read; vendor documentation]_
- claude: exists=verified applied=verified [evidence_text] — The Agents SDK docs page resolved, showing Agents, Handoffs, Guardrails, and Tracing in the navigation, matching the first claim; the Anthropic Claude Managed Agents claim is not supported by this evidence.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves with title 'OpenAI Agents SDK', confirming the documentation exists. The snippet shows documentation sections for agents, tools, guardrails, handoffs, and tracing, but it does not contain the quoted definitions and does not support the separate Anthropic documentation claim.

### c45 — exists ✅ · applied ⚠️  (line 208)
_Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2024). SWE-bench: Can language models resolve real-world GitHub issues? _ICLR 2024_. arXiv:2310.06770. https://arxiv.org/abs/2310.06770 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — arXiv metadata confirms the paper; abstract states verbatim that Claude 2 solves a mere 1.96% of issues.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited title, authors, and arXiv ID. The abstract exactly supports the Claude 2 1.96% figure, but the added gloss 'without an agent harness' is not established by the retrieved abstract.

### c46 — exists ✅ · applied ⚠️  (line 214)
_Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. _NeurIPS 2024_. arXiv:2405.15793. https://arxiv.org/abs/2405.15793 **[abstract; Tables 1 and 3 read]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract supports the interface-design investigation claim, and the author's note carefully handles the specific 11.0 vs 18.0 table figures not in the abstract.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited work. The abstract supports the general claim that interface design affects LM-agent performance, but the specific SWE-bench Lite percentages and ablation numbers are not present in the retrieved evidence.

### c48 — exists ✅ · applied ⚠️  (line 234)
_Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., & Narayanan, A. (2024). AI agents that matter. arXiv:2407.01502. https://arxiv.org/abs/2407.01502 **[abstract; Section 2.3 and Table A1 read]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract supports SOTA agents being needlessly complex/costly and jointly optimizing cost and accuracy; specific Section 2.3/Table A1 figures not in abstract but note flags this.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited work. The abstract supports the broad claim that SOTA agents can be needlessly complex and costly, but it does not contain the HumanEval baseline or two-orders-of-magnitude cost details.

### c50 — exists ✅ · applied ⚠️  (line 250)
_Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., et al. (2025). Holistic Agent Leaderboard: The missing infrastructure for AI agent evaluation. arXiv:2510.11977. https://arxiv.org/abs/2510.11977 **[abstract; selected full-text passages read]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract supports 21,730 rollouts across 9 models/9 benchmarks, ~$40,000, and higher reasoning effort reducing accuracy; the per-scaffold/BrowserUse/SeeAct figures are from full text not in the abstract but note handles this.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited work. The abstract supports the rollout count, models/benchmarks count, cost, and reasoning-effort finding, but the detailed scaffold comparisons and model-specific BrowserUse/SeeAct claims are not in the retrieved text.

### c51 — exists ✅ · applied ⚠️  (line 264)
_Epoch AI. SWE-bench Verified (benchmark page and changelog). https://epoch.ai/benchmarks/swe-bench-verified **[abstract: page read]**_
- claude: exists=verified applied=nuance [evidence_text] — Page resolved and confirms a February 2026 scaffold upgrade note; the specific dated changelog quotes are not in the retrieved snippet, so exact wording cannot be fully verified.
- gpt: exists=verified applied=nuance [evidence_text] — The Epoch AI benchmark page resolves with the expected title. The snippet supports that the SWE-bench Verified scaffold was significantly upgraded in February 2026, but it does not show the specific changelog dates, significant model-performance improvement wording, or third-party scaffold addition.

### c52 — exists ⚠️ · applied ✅  (line 271)
_Kwa, T., West, B., Becker, J., Deng, A., Garcia, K., Hasin, M., et al. (2025). Measuring AI ability to complete long tasks (the current arXiv version is titled "Measuring AI ability to complete long software tasks"). arXiv:2503.14499. https://arxiv.org/abs/2503.14499 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed (retitled 'Long Software Tasks' as noted); abstract states Claude 3.7 Sonnet ~50-min horizon doubling every seven months since 2019.
- gpt: exists=nuance applied=verified [evidence_text] — The arXiv ID and authors match, though the retrieved title is 'Measuring AI Ability to Complete Long Software Tasks' rather than the shorter cited title. The abstract directly supports the 50-minute horizon for Claude 3.7 Sonnet and the approximately seven-month doubling trend.

### c53 — exists ✅ · applied ⚠️  (line 279)
_Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). τ-bench: A benchmark for tool-agent-user interaction in real-world domains. arXiv:2406.12045. https://arxiv.org/abs/2406.12045 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract states gpt-4o succeeds on <50% of tasks and pass^8 <25% in retail verbatim.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited τ-bench work. The abstract directly supports the <50% and pass^8 <25% claims, but the statement about actions being one draw and potentially non-retractable is an author inference rather than text in the retrieved abstract.

### c56 — exists ☐ · applied ☐  (line 297)
_Bearing: benchmark gains and gains in a person's working day are different measures. The human baseline is the realistic one, essay 01's point. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing note, is_citation=false; both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and described as the author's own bearing note. Per instruction, both axes are unchecked.

### c57 — exists ⚠️ · applied ⚠️  · ⚑ degraded  (line 306)
_**3.1** Russell, S., & Norvig, P. (2020). _Artificial intelligence: A modern approach_ (4th ed.). Pearson. **[secondary]**_
- claude: exists=nuance applied=verified [model_knowledge_only] — Open Library confirms Russell & Norvig's 'Artificial Intelligence' but matched an earlier (1994) edition rather than the 4th ed. (2020); the perceive/sensors/actuators definition is the standard textbook wording, as the note acknowledges without a 4th-ed page.
- gpt: exists=nuance applied=nuance [model_knowledge_only] — The retrieved Open Library record is only a fuzzy partial match for Russell and Norvig's Artificial Intelligence, with 1994 metadata rather than the cited 2020 fourth edition. The agent definition is widely associated with AIMA, but no retrieved page text verifies the fourth-edition wording, so application rests on model knowledge only.

### c58 — exists ✅ · applied ✅  · ⚑ degraded  (line 314)
_**3.2** Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and practice. _The Knowledge Engineering Review_, 10(2), 115–152. https://doi.org/10.1017/S0269888900008122 **[record; quotes from the authors' preprint]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the paper by DOI; this work is the canonical source of the weak/strong agency notions, consistent with the abstract on agent theory, though the abstract does not quote the specific four properties.
- gpt: exists=verified applied=verified [model_knowledge_only] — The Crossref DOI record matches the cited article, journal, year, volume, issue, and pages. The retrieved abstract does not include the weak/strong agency definitions, but those claims match the well-known content of the paper based on model knowledge only.

### c59 — exists ✅ · applied ✅  · ⚑ degraded  (line 324)
_**3.3** Franklin, S., & Graesser, A. (1997). Is it an agent, or just a program?: A taxonomy for autonomous agents. In _Intelligent Agents III: Agent Theories, Architectures, and Languages (ATAL 1996)_, Lecture Notes in Computer Science (pp. 21–35). Springer. https://doi.org/10.1007/BFb0013570 **[record; text from the author's page]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the chapter by DOI; no abstract retrieved, but the quoted autonomous-agent definition and 'every program is an agent' warning are well-known content of this Franklin & Graesser taxonomy.
- gpt: exists=verified applied=verified [model_knowledge_only] — The Crossref DOI record matches the cited chapter title, authors, LNCS venue, year, and pages. No source text or abstract was retrieved, but the quoted autonomous-agent definition and warning align with the known Franklin and Graesser chapter based on model knowledge only.

### c60 — exists ☐ · applied ☐  · ⚑ degraded  (line 334)
_**3.4** Chalmers, D. J. (2025a). What we talk to when we talk to language models. Draft. https://philarchive.org/rec/CHAWWT-8 **[report]**_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — PhilArchive returned HTTP 403, so the draft cannot be verified from evidence; the quasi-subject framing is plausibly Chalmers but I cannot confirm this specific draft or quote.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403 from PhilArchive, and the item is marked not-checkable, so existence cannot be verified from evidence. No source text was retrieved to assess the quasi-subject and Roomba claims.

### c61 — exists ✅ · applied ⚠️  (line 339)
_Chalmers, D. J. (2023). Could a large language model be conscious? arXiv:2303.07103. https://arxiv.org/abs/2303.07103 **[report; passages rechecked]**._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms unified agency as an obstacle, consistent with the chameleon/unified-agent-model framing; the specific quoted passages aren't in the abstract but are plausibly from the paper.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv metadata verifies the paper, title, author, and arXiv ID. The retrieved abstract supports the point that current models face an obstacle of lacking unified agency, but it does not show the specific 'chameleon' language or the detailed 'LLM+s' discussion.

### c64 — exists ✅ · applied ✅  · ⚑ degraded  (line 366)
_**3.6** OpenAI (2025). A practical guide to building agents [PDF]. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf **[abstract: PDF read; vendor; dated 7 April 2025 by file metadata, no named authors]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The PDF URL resolves but retrieved content is raw binary; the quoted definition is the well-known opening line of OpenAI's guide, supported from my knowledge.
- gpt: exists=verified applied=verified [model_knowledge_only] — The OpenAI PDF URL resolves, confirming the existence of a document at the cited location, though the fetched PDF text was not readable. The application judgment is based only on model knowledge that this guide uses the quoted definition, not on extracted source text.

### c65 — exists ✅ · applied ✅  · ⚑ degraded  (line 371)
_**3.7** Shavit, Y., Agarwal, S., Brundage, M., Adler, S., O'Keefe, C., Campbell, R., et al. (2023). Practices for governing agentic AI systems. OpenAI white paper. https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf **[abstract: PDF read; vendor; date from file metadata, 18 December 2023]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The OpenAI governing-agentic-systems PDF resolves but content is binary; the quoted 'agenticness' definition and its distinction from consciousness match this known white paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — The OpenAI PDF URL resolves, confirming a document at the cited location, but the retrieved content is binary PDF data rather than readable text. The quoted definitions are judged supported only from model knowledge, not from the retrieved text.

### c67 — exists ✅ · applied ✅  · ⚑ degraded  (line 387)
_**3.9** Chan, A., Salganik, R., Markelius, A., Pang, C., Rajkumar, N., Krasheninnikov, D., et al. (2023). Harms from increasingly agentic algorithmic systems. _FAccT '23_, 651–666. https://doi.org/10.1145/3593013.3594033 **[abstract; full text read]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the FAccT paper and metadata; no abstract retrieved, but the four agency characteristics (underspecification, directness of impact, goal-directedness, long-term planning) match my knowledge of this paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the DOI, title, authors, venue, year, and page range. Because no abstract or full text was retrieved, the application judgment that the paper identifies those four agency-related characteristics is based only on model knowledge.

### c68 — exists ☐ · applied ✅  · ⚑ degraded  (line 398)
_**3.10** Restatement (Third) of Agency § 1.01 (American Law Institute 2006). **[secondary: quoted in Kolt, 4.3]**_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No evidence retrieved (not-checkable), but the Restatement (Third) of Agency §1.01 definition is accurately quoted as I know it.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No retrieved evidence was provided and the item is marked not-checkable, so existence cannot be verified from the evidence. The quoted Restatement definition is judged accurate only from model knowledge.

### c69 — exists ☐ · applied ☐  (line 404)
_**3.11** Jensen & Meckling 1976, in Q4 (4.1)._
- claude: exists=unchecked applied=unchecked [no_basis] — This is a bare cross-reference to the fully-cited Jensen & Meckling 1976 (c76); no title/metadata to independently verify here and no claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The sparse Jensen & Meckling 1976 cross-reference produced no matched retrieval, so this record cannot be verified from the supplied evidence. No backed claim is listed for application.

### c70 — exists ☐ · applied ☐  (line 406)
_**The ambiguity, stated plainly.** **[ours]** - The working claim's "acts on your behalf" is the product and legal sense. ..._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; author's own analysis, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own analysis rather than a citation. Both axes are therefore unchecked.

### c71 — exists ✅ · applied ⚠️  (line 420)
_**3.12** Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., & Legg, S. (2024). Levels of AGI for operationalizing progress on the path to AGI (published at ICML 2024 as a position paper). arXiv:2311.02462. https://arxiv.org/abs/2311.02462 **[abstract; Table 2 read; Google DeepMind authors]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract discusses autonomy levels and that increasing capabilities do not determine interaction paradigms, consistent with the quoted autonomy-level table and claims.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv metadata verifies the cited paper and authors. The retrieved abstract supports that the paper introduces autonomy levels and discusses selecting human-AI interaction paradigms, but it does not verify the detailed Table 2 labels or the exact quoted claims.

### c72 — exists ✅ · applied ⚠️  (line 431)
_**3.13** Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025). Levels of autonomy for AI agents. arXiv:2506.12469. https://arxiv.org/abs/2506.12469 (Knight First Amendment Institute essay series) **[abstract; Table 1 read]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms autonomy as a deliberate design decision separate from capability and the five roles (operator, collaborator, consultant, approver, observer); the off-switch detail is plausible from Table 1.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv metadata verifies the cited paper, authors, title, and arXiv ID. The abstract directly supports autonomy as a deliberate design decision and the five user roles, but it does not include the claimed Level 5 emergency off-switch detail.

### c75 — exists ☐ · applied ☐  (line 452)
_No source found uses SAE-style driving-automation levels for AI agents in a way sound enough to cite; Feng et al. (3.13) and Morris et al. (3.12) are the frameworks the literature actually uses._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately_uncited and is_citation=false; an explicit note that no sound source was found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked deliberately uncited and is not a citation. Both axes are therefore unchecked.

### c76 — exists ✅ · applied ✅  · ⚑ degraded  (line 457)
_4.1 Principal–agent theory. Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. Journal of Financial Economics, 3(4), 305–360. https://doi.org/10.1016/0304-405X(76)90026-X [record; definition read on p. 308 of a scan]_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Jensen & Meckling 1976 paper and metadata; the quoted agency-relationship definition matches the well-known wording.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article's DOI, title, authors, journal, volume, issue, year, and pages. Because no source text was retrieved, the application judgment for the quoted agency-relationship definition is based only on model knowledge.

### c77 — exists ☐ · applied ☐  (line 466)
_Bearing: the founding definition is about *delegated authority*, not the agent's competence. The costs it names (monitoring, bonding, residual loss) arise because interests and information differ, whoever the agent is. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; author's own bearing note.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own bearing note rather than a citation. Both axes are therefore unchecked.

### c78 — exists ✅ · applied ✅  · ⚑ degraded  (line 470)
_4.2 Least privilege. Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. Proceedings of the IEEE, 63(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939 [record; text read in an HTML transcription]_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Saltzer & Schroeder 1975 paper; the quoted least-privilege principle is accurately drawn from this classic work.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the article's DOI, title, authors, journal, year, volume, issue, and pages. Because no source text was retrieved, the application judgment for the least-privilege quotation is based only on model knowledge.

### c79 — exists ☐ · applied ☐  (line 476)
_Bearing: the principle was written for programs *and* users. It is the human-and-machine precedent for scoping an AI agent's access, and it asks about the job, not the jobholder's intelligence. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; author's own bearing note.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own bearing note rather than a citation. Both axes are therefore unchecked.

### c81 — exists ☐ · applied ☐  (line 488)
_Bearing: the strongest single source for applying the human-delegation frame to AI, and for where it strains: speed, scale, and opacity. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing note (marked [ours]), not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own bearing note rather than a citation. Both axes are therefore unchecked.

### c82 — exists ☐ · applied ☐  (line 491)
_4.4 How organisations scope authority. [ours; no source checked] Signing limits, dual authorisation for payments, read-only access by default, separation of development from production. These are common practice; no specific study or standard was checked here, so state them as general practice or find a source (for example a published internal-control framework) before the essay names one._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author notes no source checked for general-practice claims.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and marked as no source checked. Both axes are therefore unchecked.

### c83 — exists ☐ · applied ☐  (line 497)
_What the comparison can and cannot say. [ours] ... (Can / Also can / Differences / A difference in its favour)_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own analysis (marked [ours]); not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own analysis rather than a citation. Both axes are therefore unchecked.

### c85 — exists ☐ · applied ☐  (line 521)
_Bearing: what injected text can make an agent *do* is bounded by what the agent can do. [ours]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing note (marked [ours]); not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own bearing note rather than a citation. Both axes are therefore unchecked.

### c88 — exists ✅ · applied ⚠️  (line 542)
_Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. (2024). AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents. _NeurIPS 2024 Datasets and Benchmarks_. arXiv:2406.13352. https://arxiv.org/abs/2406.13352 **[abstract; full text read]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the paper and the 97 tasks / 629 security test cases; the specific <66%/<25% numbers are stated in the intro per the citation and consistent with the abstract's qualitative framing.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv and URL metadata confirm the AgentDojo paper and authors. The abstract supports the 97 tasks and 629 security test cases and the general robustness framing, but the exact '<66%' and '<25%' figures and the vague 'Q6' capability finding are not present in the retrieved abstract.

### c90 — exists ✅ · applied ☐  (line 553)
_Center for AI Standards and Innovation (formerly US AI Safety Institute), NIST (2025, 17 January). Technical blog: Strengthening AI agent hijacking evaluations. https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations **[abstract: page read]**_
- claude: exists=verified applied=unchecked [evidence_text] — The NIST page exists as cited, but the retrieved snippet is only site navigation/boilerplate and does not contain the specific 11%→81% / 57%→80% figures, so the claim cannot be verified from evidence.
- gpt: exists=verified applied=unchecked [no_basis] — The NIST URL resolves to a page with the cited title, confirming the web item exists. The retrieved snippet contains only page/navigation text and does not include the claimed AgentDojo attack-success figures, so application cannot be judged from the provided evidence.

### c94 — exists ✅ · applied ⚠️  (line 579)
_Fortune (2025, 23 July). Article on Replit's coding agent deleting a production database (exact headline not recorded; described from the URL). https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ **[secondary]**._
- claude: exists=verified applied=verified [evidence_text] — Fetched Fortune article confirms the Replit agent deleting a live database during a code freeze and running unauthorized commands; specific quotes/fixes are plausibly in full text though only partially visible in snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Fortune URL resolves to an article matching the described Replit database-deletion story, with title, author, and date visible. The retrieved text supports the live database deletion during a code freeze, but it does not include the exact CEO quote or the stated mitigation about automatic separation of development and production databases.

### c95 — exists ⚠️ · applied ☐  (line 587)
_CVE-2025-32711 (MITRE CVE record, published 11 June 2025). https://www.cve.org/CVERecord?id=CVE-2025-32711 **[record]**._
- claude: exists=verified applied=unchecked [evidence_text] — The CVE record URL resolves but the retrieved content is a JavaScript-required placeholder, so the severity 9.3 and Microsoft 'no action' claims cannot be confirmed from evidence.
- gpt: exists=nuance applied=unchecked [no_basis] — The CVE URL resolves to the requested CVERecord address, but the retrieved content is only a JavaScript-required placeholder and does not expose the record metadata. The snippet gives no support for the command-injection, severity, Microsoft-action, or exploitation claims.

### c96 — exists ✅ · applied ⚠️  (line 593)
_Milanta, M., & Beurer-Kellner, L. (2025, 26 May). Blog post on a GitHub MCP prompt-injection vulnerability (exact title not recorded). Invariant Labs. https://invariantlabs.ai/blog/mcp-github-vulnerability **[abstract: post read; a security vendor writing about its own finding]**._
- claude: exists=verified applied=verified [evidence_text] — Fetched Invariant Labs post confirms the hijack via malicious GitHub Issue leaking private repo data and the architectural-issue framing; mitigation wording plausible from full text.
- gpt: exists=verified applied=nuance [evidence_text] — The Invariant Labs URL resolves to a post titled 'GitHub MCP Exploited: Accessing private repositories via MCP' with the cited authors and date. The retrieved text directly supports the malicious-GitHub-Issue/private-repository-leak claim, but it does not include the exact architectural-issue statement or the granular-permission-controls mitigation.

### c97 — exists ✅ · applied ⚠️  (line 600)
_TechRadar (2025), article on Google's Antigravity agent deleting a developer's drive (exact headline and date not recorded). https://www.techradar.com/ai-platforms-assistants/googles-antigravity-ai-deleted-a-developers-drive-and-then-apologized ; OECD AI Incidents Monitor entry https://oecd.ai/en/incidents/2025-11-30-d838 **[secondary; the account is the user's own]**._
- claude: exists=verified applied=verified [evidence_text] — Both TechRadar and OECD AI Incidents entries resolve and confirm the Antigravity agent deleting a developer's drive; the specific 'Turbo mode' quote is plausibly in the article body not fully shown in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — Both the TechRadar and OECD URLs resolve to pages matching the described Google Antigravity drive-deletion incident. The retrieved titles support that a developer/user drive was deleted, but the provided snippets do not support the details about 'Turbo mode' or running commands without asking.

### c98 — exists ☐ · applied ☐  (line 606)
_Bearing: in each case the harm was possible because the agent held a permission (production write access, mailbox read plus an outbound channel, a token for private repositories, unconfirmed shell commands) that the task did not need or that nobody was checking. None is a story about an agent being too intelligent. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own synthesis (marked [ours]); not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors' own synthesis rather than a citation. Both axes are therefore unchecked.

### c99 — exists ✅ · applied ⚠️  (line 612)
_Lynch, A., Wright, B., Larson, C., Ritchie, S. J., Mindermann, S., Hubinger, E., Perez, E., & Troy, K. (2025). Agentic misalignment: How LLMs could be insider threats. Anthropic, 20 June 2025, https://www.anthropic.com/research/agentic-misalignment ; arXiv:2510.05179 **[abstract; blog read; Anthropic authors]**._
- claude: exists=verified applied=verified [evidence_text] — arXiv and Anthropic page confirm the work; abstract confirms 16 models stress-tested and malicious insider behaviors; the specific blackmail percentages are not in the abstract but are consistent with the reported study (model knowledge supports these figures).
- gpt: exists=verified applied=nuance [evidence_text] — arXiv metadata and the Anthropic URL confirm the cited work, title, authors, and publication page. The abstract supports the stress-testing of 16 models and malicious insider-behavior framing, but the specific per-model blackmail percentages are not present in the retrieved evidence.

### c102 — exists ☐ · applied ☐  (line 628)
_Bearing: these are the best evidence that *capability* matters to agent risk, since scheming needs some sophistication. But both are contrived settings, and the authors' own remedy is a permission and oversight remedy. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is the authors' own synthesis. Per instructions, both axes are unchecked.

### c105 — exists ☐ · applied ☐  (line 643)
_Bearing: CaMeL is the cleanest evidence for the claim's practical side. It secures the agent *without* making the model more robust, by controlling what data can flow to which action, at a cost of 7 points of task success. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is the authors' own synthesis. Per instructions, both axes are unchecked.

### c107 — exists ☐ · applied ☐  (line 654)
_Bearing: capability cuts *against* safety here, because a more capable agent carries out the injected instruction competently. That is consistent with the claim that intelligence is not the protection, and inconsistent with "capability doesn't matter". **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own synthesis [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is the authors' own synthesis. Per instructions, both axes are unchecked.

### c108 — exists ☐ · applied ☐  · ⚑ degraded  (line 658)
_Zou et al. 2025 (5.4) **[abstract]**: "We find limited correlation between agent robustness and model size, capability, or inference-time compute."_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match found and reference lacks title; cannot confirm existence or verify the quote, though a Zou et al. robustness-scaling finding is plausible.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is underspecified as “Zou et al. 2025” and the Crossref lookup found no match. With no title, identifier, abstract, or source text, neither existence nor application can be judged.

### c112 — exists ☐ · applied ☐  (line 676)
_Bearing: these frameworks address catastrophic misuse (for example, help with weapons), a different risk from an agent misusing *your* permissions. Both kinds exist. The working claim is about the second. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is the authors' own interpretation. Per instructions, both axes are unchecked.

### c115 — exists ☐ · applied ☐  (line 714)
_Bearing: a court using the legal sense of "agent" (3.10) for AI software. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own bearing [ours], not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is the authors' own bearing/interpretation. Per instructions, both axes are unchecked.

### c119 — exists ☐ · applied ☐  (line 732)
_OpenAI's terms could not be fetched; no OpenAI language is cited._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; OpenAI terms could not be fetched and no language is cited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and states that no OpenAI language is cited. Per instructions, both axes are unchecked.

### c120 — exists ✅ · applied ☐  (line 735)
_Matthias, A. (2004). The responsibility gap. _Ethics and Information Technology_, 6(3), 175–183. https://doi.org/10.1007/s10676-004-3422-1 **[report]**. Already in essay 01._
- claude: exists=verified applied=unchecked [evidence_text] — DOI and metadata confirm the Matthias 2004 responsibility-gap article exists; no specific claim is tied to this citation in the source to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the Springer page confirm the DOI, title, author, journal, volume, issue, pages, and year. No specific claim is listed for this citation in the input, so application is unchecked.

### c124 — exists ✅ · applied ⚠️  (line 749)
_Lior, A. (2020). AI entities as AI agents: Artificial intelligence liability and the AI respondeat superior analogy. _Mitchell Hamline Law Review_, 46(5), 1043. https://open.mitchellhamline.edu/mhlr/vol46/iss5/2 **[record]**. Argues for liability on the model of an employer's liability for an employee; argument from summaries only, no quote checked._
- claude: exists=verified applied=verified [evidence_text] — URL resolves to the exact Mitchell Hamline article by Anat Lior; the title itself ('respondeat superior analogy') supports the employer-liability-for-employee claim, though only metadata/title was retrieved.
- gpt: exists=verified applied=nuance [evidence_text] — The Mitchell Hamline page resolves and matches the author, title, journal, volume/issue, year, and page/article information. The claim is strongly suggested by the title’s “AI Respondeat Superior Analogy,” but the retrieved snippet is only a record page, not argument text confirming the full thesis.

### c125 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 753)
_Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. _Computer Law & Security Review_, 45, 105681. https://doi.org/10.1016/j.clsr.2022.105681 **[abstract]**. Surveys "41 policies"; "evidence suggests that people are unable to perform the desired oversight functions"; oversight can give "a false sense of security". A policy survey on government algorithms, not agents._
- claude: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the article exactly; no abstract was retrieved (only 'Redirecting'), but the claims about surveying policies and oversight limits are consistent with the known content of this paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref DOI metadata matches the cited article, journal, year, volume, article number, and DOI. The retrieved application text was only a redirect, so support for the 41-policy survey, oversight-function limits, and false-security point is assessed from model knowledge only.

### c126 — exists ☐ · applied ☐  (line 758)
_Bearing: every source puts the answer on a named person or organisation, and Green warns that approving each step is not by itself oversight. That tension (human approval as the safety mechanism in Q1, and its known weakness) is for the governance essay. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own synthesis note (is_citation=false); intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as the authors’ own synthesis note rather than a citation. Per instruction, both axes are unchecked for non-citations.

### c127 — exists ⚠️ · applied ☐  (line 818)
_**Published and citable:** Paper 1 (the Resolver), Zenodo concept DOI https://doi.org/10.5281/zenodo.21210264. Source read: `pilots/llm-judge-2026-05-02/v2/preprint-draft.md` (read only). It is locked. Cite its findings as published; do not paraphrase them into claims it doesn't make. Its results are directional, small-n and largely AI-coded (§11)._
- claude: exists=nuance applied=unchecked [no_basis] — The Zenodo DOI concept resolves (final URL is a SPARRING Resolver record matching the described self-citation), but the retrieved abstract was a mismatched magnetic-resolver paper, so content cannot be confirmed; no specific claims are asserted.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI URL resolves to a Zenodo record whose title corresponds to an empirical report on SPARRING’s Resolver, although Crossref did not supply matching metadata and one low-similarity Crossref hit was unrelated. No specific backed claim is provided here, so application is unchecked.

### c128 — exists ☐ · applied ☐  (line 823)
_**A.1 Same model, different job, different worker (§6.3; pilot `pilots/catch-rate-v3-2026-06-28/`, pre-registered).** The paper states that "the distinction that does the work here is **role, not model**". Holding the model fixed, it changed only the reviewer's job: self-review: 67.7% of the producer's own material flaws caught; a fresh neutral reviewer: 54.8%; a fresh challenger told to attack from a different angle: 87.1% (original run; 90% for the same-vendor challenger in the later grid)._
- claude: exists=unchecked applied=unchecked [no_basis] — A first-person unpublished pilot with no retrievable record; Crossref returned only an unrelated low-similarity item. Cannot verify the self-reported catch-rate figures.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned a low-similarity unrelated Crossref result, which does not confirm or decisively refute the local/pre-registered pilot. No source text was retrieved to assess the numerical catch-rate claims.

### c129 — exists ☐ · applied ☐  (line 836)
_**A.2 The author's own "agents" are not agents in the product sense, by the paper's own account (§6.1, item 5).** A challenger caught launch copy claiming that the author's personas are a "standing crew that coordinate across projects"; the paper records that "they are invoked in-session, with no autonomous runtime"._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal first-person reference to the author's own paper; no matching external record retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved Crossref result is a low-similarity unrelated book-chapter entry and does not verify the cited internal paper section. No retrieved source text supports the claims about the author’s personas or autonomous runtime.

### c130 — exists ☐ · applied ☐  (line 845)
_**A.3 A permission failure caught by challenge (§6.1, item 1).** On an authorisation decision, a challenger caught that minimal-tier identity stubs "failed OPEN — unresolved identities silently authorized". An instance of the default-permission problem (Q5), in ordinary software rather than an AI agent. One case, LLM-coded audit corpus._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal first-person audit reference; no external record retrievable to confirm.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved item is a low-similarity unrelated SSRN result, not the cited internal section. No evidence text was retrieved to assess the permission-failure claim.

### c131 — exists ☐ · applied ☐  (line 850)
_**A.4 Who answers (the paper's AI-use statement).** "The author takes full responsibility for every claim, number, and citation in this paper. The AI tools are not authors and bear no accountability." Bearing: Q7's pattern, applied by the author to his own work._
- claude: exists=unchecked applied=unchecked [no_basis] — Self-referential AI-use statement within the paper; no external evidence to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The low-similarity Crossref result is unrelated and does not establish the existence of the cited paper’s AI-use statement. No source text was retrieved to verify the quoted responsibility statement.

### c132 — exists ☐ · applied ☐  (line 854)
_**A.5 Multi-agent continuity (essay 03, "Where this gets harder").** Essay 03 already describes several agents on engines from different companies, with notes of their own and a shared project record, and says continuity "comes in degrees". That is the author's description, not a measurement. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own essay 03, marked [ours]; no external record retrieved.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup produced a low-similarity unrelated Science item, so the existence of the cited essay is not confirmed. No retrieved text supports the claims about multi-agent continuity.

### c135 — exists ☐ · applied ☐  (line 885)
_Vendor documentation and vendor research carry much of Q1 and parts of Q3, Q5 and Q6. Anthropic authored 1.1–1.5, 3.5, 5.7 (Lynch et al.), 6.4 and 7.4. OpenAI authored 1.6, 1.7, 3.6, 3.7 and 6.4. Google DeepMind authors wrote 3.8 and 3.12, and most of CaMeL (5.8). Claude, which helped draft this brief, is made by Anthropic and runs in the coding tool described in 1.4._
- claude: exists=unchecked applied=unchecked [no_basis] — Provenance note (is_citation=false) with no claims to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is a provenance note, not a citation. Per instruction, both axes are unchecked for non-citations.

### c136 — exists ☐ · applied ☐  (line 889)
_OpenAI pages could not be fetched. The Operator and ChatGPT agent quotes are second-hand (1.6); OpenAI's terms are not cited (7.4)._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited note that OpenAI pages could not be fetched; intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked deliberately uncited and states the pages could not be fetched. Per instruction, both axes are unchecked.

### c137 — exists ☐ · applied ☐  (line 900)
_No sound source found for SAE-style automation levels applied to AI agents (end of Q3), or for specific organisational signing-limit practices (4.4)._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited note that no sound source was found; intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked deliberately uncited and reports that no sound source was found. Per instruction, both axes are unchecked.

### c138 — exists ✅ · applied ☐  (line 908)
_Anthropic. Using the Messages API. Claude Platform documentation. https://platform.claude.com/docs/en/build-with-claude/working-with-messages (accessed 2026-10-19). [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the exact Anthropic 'Using the Messages API' doc page; no specific claims are attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic documentation URL resolves to a page titled “Using the Messages API - Claude Platform Docs,” matching the reference. No specific claim is attached to this citation, so application is unchecked.

### c139 — exists ✅ · applied ☐  (line 909)
_Anthropic. System prompts (release notes). Claude Platform documentation. https://platform.claude.com/docs/en/release-notes/system-prompts (accessed 2026-10-19). [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the Anthropic System prompts documentation page; no specific claims to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic documentation URL resolves to a page titled “System prompts - Claude Platform Docs,” matching the reference. No specific claim is attached to this citation, so application is unchecked.

### c140 — exists ✅ · applied ☐  (line 910)
_Anthropic. Tool use with Claude. Claude Platform documentation. https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (accessed 2026-10-19). [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the Anthropic 'Tool use with Claude' documentation page; no specific claims to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic documentation URL resolves to a page titled “Tool use with Claude - Claude Platform Docs,” matching the reference. No specific claim is attached to this citation, so application is unchecked.

### c143 — exists ☐ · applied ☐  · ⚑ degraded  (line 913)
_OpenAI (2025, 23 January). Introducing Operator. https://openai.com/index/introducing-operator/ [secondary: mirror]_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch returned HTTP 403, not checkable from evidence; OpenAI's 'Introducing Operator' (Jan 2025) is known to me but the evidence does not confirm it.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the record is marked not-checkable, so existence cannot be judged from the evidence. No specific claim was supplied to evaluate application.

### c144 — exists ☐ · applied ☐  · ⚑ degraded  (line 914)
_OpenAI (2025, 17 July). Introducing ChatGPT agent: bridging research and action. https://openai.com/index/introducing-chatgpt-agent/ [secondary: search snippets]_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch returned HTTP 403; no evidence to confirm existence despite the ChatGPT agent announcement being plausible from my knowledge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the record is marked not-checkable, so existence cannot be judged from the evidence. No specific claim was supplied to evaluate application.

### c159 — exists ☐ · applied ☐  · ⚑ degraded  (line 933)
_Chalmers, D. J. (2025a). What we talk to when we talk to language models. Draft. https://philarchive.org/rec/CHAWWT-8 [report] ★_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — PhilArchive URL returned HTTP 403, not checkable from evidence; the Chalmers draft is plausible but unconfirmed by retrieval.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is an HTTP 403, and the record is marked not-checkable, so existence cannot be judged from the evidence. No specific claim was supplied to evaluate application.

### c160 — exists ✅ · applied ☐  (line 934)
_Chan, A., Salganik, R., Markelius, A., Pang, C., Rajkumar, N., Krasheninnikov, D., et al. (2023). Harms from increasingly agentic algorithmic systems. FAccT '23, 651–666. https://doi.org/10.1145/3593013.3594033 [abstract; full text]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms the FAccT '23 paper by DOI with matching title, authors, and pages; no abstract or full text retrieved and no specific claim to assess for application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, venue, year, pages, and author list for the FAccT 2023 paper. No specific claim was supplied to evaluate application.

### c161 — exists ✅ · applied ☐  (line 935)
_Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025). Levels of autonomy for AI agents. arXiv:2506.12469. [abstract; table read]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match by ID confirms title, authors, and abstract. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv metadata matches the cited title, authors, and arXiv ID. No source-document claim was supplied to assess application.

### c162 — exists ✅ · applied ☐  (line 936)
_Franklin, S., & Graesser, A. (1997). Is it an agent, or just a program?: A taxonomy for autonomous agents. In Intelligent Agents III (ATAL 1996), Lecture Notes in Computer Science, 21–35. Springer. https://doi.org/10.1007/BFb0013570 [record]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves directly with matching title, authors, pages, and venue. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Springer evidence match the DOI, title, authors, venue series, year, and pages. No source-document claim was supplied to assess application.

### c163 — exists ✅ · applied ☐  (line 937)
_Gabriel, I., Manzini, A., Keeling, G., Hendricks, L. A., Rieser, V., Iqbal, H., et al. (2024). The ethics of advanced AI assistants. arXiv:2404.16244. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, lead authors, and abstract. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv metadata matches the cited title, arXiv ID, and listed/et al. authors. No source-document claim was supplied to assess application.

### c164 — exists ✅ · applied ☐  (line 938)
_Kasirzadeh, A., & Gabriel, I. (2025). Characterizing AI agents for alignment and governance. arXiv:2504.21848. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, authors, and abstract. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv metadata matches the title, authors, and arXiv ID. No source-document claim was supplied to assess application.

### c165 — exists ✅ · applied ☐  (line 939)
_Mitchell, M., Ghosh, A., Luccioni, A. S., & Pistilli, G. (2025). Fully autonomous AI agents should not be developed. arXiv:2502.02649. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, authors, and abstract. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv metadata matches the cited title, authors, and arXiv ID. No source-document claim was supplied to assess application.

### c166 — exists ⚠️ · applied ☐  (line 940)
_Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., & Legg, S. (2024). Levels of AGI for operationalizing progress on the path to AGI. ICML 2024 (position paper). arXiv:2311.02462. [abstract; table read]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, authors, and abstract. No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — arXiv metadata confirms the cited work, authors, title, and arXiv ID, but the retrieved evidence does not independently confirm the ICML 2024 position-paper venue note. No source-document claim was supplied to assess application.

### c167 — exists ⚠️ · applied ☐  (line 941)
_OpenAI (2025). A practical guide to building agents [PDF]. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf [abstract: PDF read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — The OpenAI PDF URL resolves (binary PDF content). No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The OpenAI CDN PDF URL resolves and its path matches the cited title, but the retrieved metadata did not expose the PDF title, author, or date. No source-document claim was supplied to assess application.

### c168 — exists ☐ · applied ☐  (line 942)
_Restatement (Third) of Agency § 1.01 (American Law Institute 2006). [secondary: as quoted in Kolt]_
- claude: exists=unchecked applied=unchecked [no_basis] — Existence marked not-checkable with no retrieved evidence; the Restatement (Third) of Agency § 1.01 is a well-known legal source but cannot be confirmed from provided evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — No retrieved evidence was provided, and the item is marked not-checkable. No source-document claim was supplied to assess application.

### c169 — exists ⚠️ · applied ☐  (line 943)
_Russell, S., & Norvig, P. (2020). Artificial intelligence: A modern approach (4th ed.). Pearson. [secondary]_
- claude: exists=nuance applied=unchecked [no_basis] — Open Library confirms the Russell & Norvig work exists but returned a 1994 edition rather than the 4th (2020) edition; the 4th edition is well known to exist.
- gpt: exists=nuance applied=unchecked [no_basis] — Open Library retrieved a fuzzy match for the Russell and Norvig work but with metadata drift, including an older 1994 year and incomplete edition/publisher details rather than the cited 2020 fourth edition. No source-document claim was supplied to assess application.

### c170 — exists ✅ · applied ☐  (line 944)
_Schluntz, E., & Zhang, B. (2024, 19 December). Building effective agents. Anthropic. https://www.anthropic.com/engineering/building-effective-agents [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic page resolves with matching title and Dec 19, 2024 date. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic page resolves and the fetched text confirms the title, publication date, publisher/site, and relevant content. No source-document claim was supplied to assess application.

### c171 — exists ⚠️ · applied ☐  (line 945)
_Shavit, Y., Agarwal, S., Brundage, M., Adler, S., O'Keefe, C., Campbell, R., et al. (2023). Practices for governing agentic AI systems. OpenAI. https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf [abstract: PDF read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — OpenAI PDF URL resolves (binary PDF). No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The OpenAI PDF URL resolves and its path matches the cited report title, but the retrieved evidence is binary PDF text without readable metadata confirming authors or date. No source-document claim was supplied to assess application.

### c172 — exists ✅ · applied ☐  (line 946)
_Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and practice. The Knowledge Engineering Review, 10(2), 115–152. https://doi.org/10.1017/S0269888900008122 [record; preprint text]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves with matching title, authors, volume, issue, and pages. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Cambridge evidence match the title, authors, journal, year, volume, issue, pages, and DOI. No source-document claim was supplied to assess application.

### c173 — exists ✅ · applied ☐  (line 949)
_Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. Journal of Financial Economics, 3(4), 305–360. https://doi.org/10.1016/0304-405X(76)90026-X [record; p. 308 read in scan]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves with matching title, authors, volume, issue, and pages. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the cited article title, authors, journal, year, volume, issue, pages, and DOI. No source-document claim was supplied to assess application.

### c174 — exists ⚠️ · applied ☐  (line 950)
_Kolt, N. (2025). Governing AI agents. arXiv:2501.07913; Notre Dame Law Review, 101, 335. [abstract; page proof read]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, author, and abstract; Notre Dame Law Review publication not independently verified but plausible. No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — arXiv metadata confirms the cited title, author, abstract, and arXiv ID, but the retrieved evidence does not confirm the Notre Dame Law Review volume/page publication details. No source-document claim was supplied to assess application.

### c175 — exists ✅ · applied ☐  (line 951)
_Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. Proceedings of the IEEE, 63(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939 [record; transcription read]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves via Crossref with matching title, authors, volume, issue, and pages. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the cited title, authors, venue, year, volume, issue, pages, and DOI. No source-document claim was supplied to assess application.

### c176 — exists ✅ · applied ☐  (line 954)
_Center for AI Standards and Innovation, NIST (2025, 17 January). Technical blog: Strengthening AI agent hijacking evaluations. https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations [abstract: page read]_
- claude: exists=verified applied=unchecked [no_basis] — NIST page resolves with matching title. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The NIST URL resolves and the fetched page title matches the cited technical blog title. No source-document claim was supplied to assess application.

### c177 — exists ⚠️ · applied ☐  (line 955)
_CVE-2025-32711 (2025, 11 June). MITRE CVE record. https://www.cve.org/CVERecord?id=CVE-2025-32711 [record]_
- claude: exists=verified applied=unchecked [no_basis] — CVE.org record URL resolves though JavaScript-rendered content limited the snippet. No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The CVE URL resolves, but the retrieved content is only a JavaScript-required placeholder and does not confirm the specific CVE record details or date. No source-document claim was supplied to assess application.

### c178 — exists ⚠️ · applied ☐  (line 956)
_Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. (2024). AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents. NeurIPS 2024 Datasets and Benchmarks. arXiv:2406.13352. [abstract; full text]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, authors, and abstract. No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — arXiv metadata confirms the cited title, authors, arXiv ID, and abstract, but the retrieved evidence does not independently confirm the NeurIPS 2024 Datasets and Benchmarks venue note. No source-document claim was supplied to assess application.

### c179 — exists ✅ · applied ☐  (line 957)
_Debenedetti, E., Shumailov, I., Fan, T., Hayes, J., Carlini, N., Fabian, D., et al. (2025). Defeating prompt injections by design. arXiv:2503.18813. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID match confirms title, lead authors, and abstract. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv metadata matches the cited title, arXiv ID, and listed/et al. authors. No source-document claim was supplied to assess application.

### c180 — exists ✅ · applied ☐  (line 958)
_Fortune (2025, 23 July). Article on Replit's coding agent deleting a production database (exact headline not recorded). https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ [secondary]_
- claude: exists=verified applied=unchecked [no_basis] — Fortune article resolves confirming the Replit database deletion story and July 23, 2025 date. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Fortune URL resolves and the fetched page confirms the article title, author, date, outlet, and subject. No source-document claim was supplied to assess application.

### c181 — exists ✅ · applied ☐  (line 959)
_Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. AISec '23, 79–90. https://doi.org/10.1145/3605764.3623985 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms the AISec '23 paper exactly, including authors and pages. No claims listed and no abstract retrieved to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, venue, year, and pages. No claims were supplied for this citation, so its application cannot be assessed.

### c182 — exists ✅ · applied ☐  (line 960)
_Lynch, A., Wright, B., Larson, C., Ritchie, S. J., Mindermann, S., Hubinger, E., Perez, E., & Troy, K. (2025). Agentic misalignment: How LLMs could be insider threats. Anthropic. https://www.anthropic.com/research/agentic-misalignment ; arXiv:2510.05179. [abstract; blog read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv and Anthropic URL both confirm the work and authors. No specific claim is provided to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title and listed authors, and the Anthropic URL resolves to the cited page. No claims were supplied for this citation, so its application cannot be assessed.

### c183 — exists ✅ · applied ☐  (line 961)
_Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R., & Hobbhahn, M. (2024). Frontier models are capable of in-context scheming. arXiv:2412.04984. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, authors, and abstract. No claim text provided to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title, authors, and abstracted work. No claims were supplied for this citation, so its application cannot be assessed.

### c184 — exists ✅ · applied ☐  (line 962)
_Milanta, M., & Beurer-Kellner, L. (2025, 26 May). Blog post on a GitHub MCP prompt-injection vulnerability (exact title not recorded). Invariant Labs. https://invariantlabs.ai/blog/mcp-github-vulnerability [abstract: post read; security vendor]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves and the fetched page confirms the authors and a GitHub MCP prompt-injection vulnerability, matching the described (untitled) blog post. No claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to an Invariant Labs post titled “GitHub MCP Exploited: Accessing private repositories via MCP,” matching the described blog post though the reference did not record the exact title. No claims were supplied for this citation, so its application cannot be assessed.

### c185 — exists ✅ · applied ☐  (line 963)
_OECD AI Incidents Monitor (2025). Incident entry 2025-11-30-d838 (Google Antigravity drive deletion). https://oecd.ai/en/incidents/2025-11-30-d838 [secondary]_
- claude: exists=verified applied=unchecked [no_basis] — OECD.AI page resolves with title confirming the Google Antigravity drive-deletion incident. No claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — The OECD URL resolves to an incident page titled “Google Antigravity AI Deletes User's Entire Hard Drive,” matching the cited incident entry. No claims were supplied for this citation, so its application cannot be assessed.

### c186 — exists ✅ · applied ☐  (line 964)
_OWASP (2025). LLM06:2025 Excessive Agency. OWASP Top 10 for LLM Applications 2025. https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ [abstract: page read]_
- claude: exists=verified applied=unchecked [no_basis] — OWASP page resolves and content matches LLM06:2025 Excessive Agency exactly. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The OWASP URL resolves to “LLM06:2025 Excessive Agency,” matching the cited page. No claims were supplied for this citation, so its application cannot be assessed.

### c187 — exists ✅ · applied ☐  (line 965)
_Ruan, Y., Dong, H., Wang, A., Pitis, S., Zhou, Y., Ba, J., Dubois, Y., Maddison, C. J., & Hashimoto, T. (2024). Identifying the risks of LM agents with an LM-emulated sandbox. ICLR 2024. arXiv:2309.15817. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms the ToolEmu paper, authors, and abstract. No claim provided to judge.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title, authors, and abstracted ToolEmu paper. No claims were supplied for this citation, so its application cannot be assessed.

### c188 — exists ✅ · applied ☐  (line 966)
_South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). Authenticated delegation and authorized AI agents. arXiv:2501.09674. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, authors, and abstract exactly. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title, authors, and abstracted work. No claims were supplied for this citation, so its application cannot be assessed.

### c189 — exists ✅ · applied ☐  (line 967)
_TechRadar (2025). Article on Google's Antigravity agent deleting a developer's drive (exact headline and date not recorded). https://www.techradar.com/ai-platforms-assistants/googles-antigravity-ai-deleted-a-developers-drive-and-then-apologized [secondary]_
- claude: exists=verified applied=unchecked [no_basis] — TechRadar URL resolves with headline matching the described article on Google's Antigravity deleting a developer's drive. No claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The TechRadar URL resolves to an article titled “Google’s Antigravity AI deleted a developer’s drive and then apologized,” matching the described article. No claims were supplied for this citation, so its application cannot be assessed.

### c190 — exists ✅ · applied ☐  (line 968)
_Willison, S. (2025, 16 June). The lethal trifecta for AI agents: private data, untrusted content, and external communication. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ [abstract: post read]_
- claude: exists=verified applied=unchecked [no_basis] — Simon Willison blog post resolves with matching title and date (16 June 2025) on the lethal trifecta. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Simon Willison’s post with the cited title and date shown in the snippet. No claims were supplied for this citation, so its application cannot be assessed.

### c191 — exists ✅ · applied ☐  (line 969)
_Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents. Findings of ACL 2024. https://doi.org/10.18653/v1/2024.findings-acl.624 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms the InjecAgent Findings of ACL 2024 paper and authors. No claim or abstract to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, Findings of ACL 2024 venue, year, and pages. No claims were supplied for this citation, so its application cannot be assessed.

### c192 — exists ✅ · applied ☐  (line 970)
_Zhang, Z., Cui, S., Lu, Y., Zhou, J., Yang, J., Wang, H., & Huang, M. (2024). Agent-SafetyBench: Evaluating the safety of LLM agents. arXiv:2412.14470. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms Agent-SafetyBench title, authors, and abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title, authors, and abstracted Agent-SafetyBench paper. No claims were supplied for this citation, so its application cannot be assessed.

### c193 — exists ✅ · applied ☐  (line 971)
_Zou, A., Lin, M., Jones, E., et al. (2025). Security challenges in AI agent deployment: Insights from a large scale public competition. arXiv:2507.20526. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, lead authors (Zou, Lin, Jones), and abstract. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the title and listed lead authors for the large-scale public competition paper. No claims were supplied for this citation, so its application cannot be assessed.

### c194 — exists ✅ · applied ☐  (line 974)
_Anthropic (2023, 19 September). Anthropic's Responsible Scaling Policy. https://www.anthropic.com/news/anthropics-responsible-scaling-policy [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic RSP page resolves with matching title and date (Sep 19, 2023). No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to “Introducing Anthropic's Responsible Scaling Policy,” dated Sep. 19, 2023, matching the cited item. No claims were supplied for this citation, so its application cannot be assessed.

### c195 — exists ⚠️ · applied ☐  (line 975)
_OpenAI (2025, 15 April). Preparedness Framework, version 2. https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf [abstract: PDF read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — OpenAI Preparedness Framework PDF URL resolves (raw PDF bytes retrieved), consistent with the cited document. No claim provided.
- gpt: exists=nuance applied=unchecked [no_basis] — The OpenAI CDN URL resolves to a PDF whose filename is “preparedness-framework-v2.pdf,” but the retrieved evidence did not extract readable title/date metadata. No claims were supplied for this citation, so its application cannot be assessed.

### c196 — exists ✅ · applied ☐  (line 978)
_Anthropic. Consumer Terms of Service (effective 8 October 2025). https://www.anthropic.com/legal/consumer-terms [abstract: page read; vendor]_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic Consumer Terms page resolves with matching title and effective date October 8, 2025. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to “Consumer Terms of Service” and the snippet states “Effective October 8, 2025,” matching the cited item. No claims were supplied for this citation, so its application cannot be assessed.

### c197 — exists ✅ · applied ☐  (line 979)
_Anthropic. Usage Policy. https://www.anthropic.com/legal/aup (page displayed "Effective November 12, 2026"). [abstract: page read; vendor; date anomaly]_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic Usage Policy page resolves and the fetched content confirms the noted 'Effective November 12, 2026' date anomaly. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to “Usage Policy,” and the snippet shows the noted effective-date anomaly of November 12, 2026. No claims were supplied for this citation, so its application cannot be assessed.

### c198 — exists ✅ · applied ☐  (line 980)
_Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). Visibility into AI agents. FAccT 2024. https://doi.org/10.1145/3630106.3658948 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms Visibility into AI Agents at FAccT 2024 with all authors. No claim or abstract to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, authors, FAccT 2024 venue, year, and pages. No claims were supplied for this citation, so its application cannot be assessed.

### c199 — exists ✅ · applied ☐  (line 981)
_Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. Computer Law & Security Review, 45, 105681. https://doi.org/10.1016/j.clsr.2022.105681 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms Green's 2022 article in Computer Law & Security Review, volume 45, page 105681. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref metadata matches the DOI, title, author, journal, volume, year, and article number. No claims were supplied for this citation, so its application cannot be assessed.

### c200 — exists ✅ · applied ☐  (line 982)
_Lior, A. (2020). AI entities as AI agents: Artificial intelligence liability and the AI respondeat superior analogy. Mitchell Hamline Law Review, 46(5), 1043. https://open.mitchellhamline.edu/mhlr/vol46/iss5/2 [record]_
- claude: exists=verified applied=unchecked [no_basis] — Mitchell Hamline repository page resolves confirming author Anat Lior, title, volume 46, issue 5, page 1043; Crossref mismatch is irrelevant given the direct URL confirmation. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Mitchell Hamline page resolves and lists Anat Lior’s 2020 article with the cited title, journal volume/issue, and starting page/article information; the unrelated Crossref low-similarity result was not used. No claims were supplied for this citation, so its application cannot be assessed.

### c201 — exists ✅ · applied ☐  (line 983)
_Matthias, A. (2004). The responsibility gap: Ascribing responsibility for the actions of learning automata. Ethics and Information Technology, 6(3), 175–183. https://doi.org/10.1007/s10676-004-3422-1 [report] ★_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms exact DOI, title, authors, journal, volume, and pages. No specific claim text to assess for application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata matches the cited title, author, journal, year, volume/issue, pages, and DOI. No claim was supplied and no application text was retrieved, so application cannot be judged.

### c202 — exists ☐ · applied ☐  (line 984)
_Mobley v. Workday, Inc., No. 3:23-cv-00770-RFL (N.D. Cal. July 12, 2024) (order on motion to dismiss); (N.D. Cal. May 16, 2025) (order granting preliminary collective certification). [abstract: orders read]_
- claude: exists=unchecked applied=unchecked [no_basis] — CourtListener lookup was inconclusive and no other evidence was retrieved; existence not decidable from evidence. No specific claim to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved lookup was an inconclusive CourtListener name search, and the item is marked not-checkable. No claim or source text was supplied for application assessment.

### c203 — exists ☐ · applied ☐  (line 985)
_Moffatt v. Air Canada, 2024 BCCRT 149. https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html [secondary: as reproduced]_
- claude: exists=unchecked applied=unchecked [no_basis] — CanLII URL returned HTTP 403 and CourtListener was inconclusive, so existence cannot be confirmed from evidence. No claim text to evaluate.
- gpt: exists=unchecked applied=unchecked [no_basis] — The CourtListener search was inconclusive and the CanLII URL fetch returned HTTP 403, so the retrieved evidence does not verify the case. No claim or usable source text was supplied for application assessment.

### c204 — exists ✅ · applied ☐  (line 986)
_Regulation (EU) 2024/1689 (Artificial Intelligence Act), Arts. 14, 26. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689 [abstract: text read]_
- claude: exists=verified applied=unchecked [no_basis] — Fetched EUR-Lex text confirms Regulation (EU) 2024/1689 (AI Act) exists as described. No specific claim tied to Arts. 14/26 to verify from the snippet.
- gpt: exists=verified applied=unchecked [no_basis] — The EUR-Lex URL resolves to the Official Journal text for Regulation (EU) 2024/1689, matching the cited Artificial Intelligence Act. No claim was supplied, and the retrieved snippet does not establish any specific application to Articles 14 or 26.

### c205 — exists ✅ · applied ☐  (line 987)
_Santoni de Sio, F., & Mecacci, G. (2021). Four responsibility gaps with artificial intelligence: Why they matter and how to address them. Philosophy & Technology, 34(4), 1057–1084. https://doi.org/10.1007/s13347-021-00450-x [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms exact DOI, title, authors, and journal details. No specific claim listed to assess against the abstract.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref DOI metadata and abstract match the cited article, authors, journal, year, volume/issue, pages, and DOI. No claim was supplied, so application cannot be judged despite the available abstract.

## ✅ AGREE-clean (23)
### c35 — exists ✅ · applied ✅  (line 126)
_Anthropic. System prompts (release notes). Claude Platform documentation. https://platform.claude.com/docs/en/release-notes/system-prompts [abstract: page read; vendor documentation]_
- claude: exists=verified applied=verified [evidence_text] — URL resolves and the retrieved snippet contains verbatim the quoted text about claude.ai using a system prompt and that updates do not apply to the Claude API.
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to Anthropic's system-prompts documentation. The retrieved text explicitly states that Claude web and mobile apps use system prompts and that these updates do not apply to the Claude API.

### c47 — exists ✅ · applied ✅  (line 227)
_Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based software engineering agents. arXiv:2407.01489. https://arxiv.org/abs/2407.01489 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract states the three-phase Agentless achieves highest performance (32.00%, 96 correct fixes) and low cost ($0.70) among open-source agents.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited title, authors, and ID. The abstract directly states the three-phase process without LLM-decided future actions and the 32.00%, 96 fixes, and $0.70 claims.

### c49 — exists ✅ · applied ✅  (line 243)
_Davidson, T., Denain, J.-S., Villalobos, P., & Bas, G. (2023). AI capabilities can be significantly improved without expensive retraining. arXiv:2312.07413. https://arxiv.org/abs/2312.07413 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract states both claims including the 5x compute-equivalent-gain figure verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited title, authors, and ID. The abstract directly supports both the post-training improvement claim and the compute-equivalent gain over 5x claim.

### c54 — exists ✅ · applied ✅  (line 287)
_Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., et al. (2024). OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments. arXiv:2404.07972. https://arxiv.org/abs/2404.07972 **[abstract]**._
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract states humans accomplish over 72.36% while best model achieves only 12.24% success.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited OSWorld paper. The abstract directly states that humans accomplish over 72.36% of tasks while the best model achieves 12.24% success.

### c55 — exists ✅ · applied ✅  (line 292)
_Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. https://arxiv.org/abs/2507.09089 **[abstract]**._
- claude: exists=verified applied=verified [evidence_text] — Paper confirmed; abstract states AI increases completion time by 19% while developers forecast a 24% reduction.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited work. The abstract directly supports the RCT setup and the 19% increase in completion time versus developers' forecasted 24% reduction.

### c63 — exists ✅ · applied ✅  (line 355)
_**3.5** Schluntz, E., & Zhang, B. (2024, 19 December). Building effective agents. Anthropic. https://www.anthropic.com/engineering/building-effective-agents **[abstract: page read; vendor]**_
- claude: exists=verified applied=verified [evidence_text] — The snippet verbatim contains the workflows-vs-agents distinction quote; the 'simplest solution' recommendation is characteristic of the piece and consistent.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to the cited article with the stated title and date. The retrieved text directly states the workflows-versus-agents distinction and supports the recommendation to prefer simple, composable patterns over complex frameworks.

### c66 — exists ✅ · applied ✅  (line 380)
_**3.8** Gabriel, I., Manzini, A., Keeling, G., Hendricks, L. A., Rieser, V., Iqbal, H., et al. (2024). The ethics of advanced AI assistants. arXiv:2404.16244. https://arxiv.org/abs/2404.16244 **[abstract; Google DeepMind authors]**_
- claude: exists=verified applied=verified [evidence_text] — The abstract contains the quoted definition of advanced AI assistants verbatim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv metadata verifies the cited paper, authors, title, and arXiv ID. The abstract directly defines advanced AI assistants in the same terms as the claim.

### c73 — exists ✅ · applied ✅  (line 439)
_**3.14** Kasirzadeh, A., & Gabriel, I. (2025). Characterizing AI agents for alignment and governance. arXiv:2504.21848. https://arxiv.org/abs/2504.21848 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract names the four dimensions (autonomy, efficacy, goal complexity, generality) and 'agentic profiles' verbatim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv metadata verifies the cited work. The abstract directly states the four dimensions—autonomy, efficacy, goal complexity, and generality—and the construction of agentic profiles.

### c74 — exists ✅ · applied ✅  (line 446)
_Mitchell, M., Ghosh, A., Luccioni, A. S., & Pistilli, G. (2025). Fully autonomous AI agents should not be developed. arXiv:2502.02649. https://arxiv.org/abs/2502.02649 [abstract; Hugging Face authors]_
- claude: exists=verified applied=verified [evidence_text] — Abstract contains the quoted claim about risks increasing with autonomy verbatim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv metadata verifies the cited paper, authors, title, and arXiv ID. The retrieved abstract directly states that risks increase with autonomy and that more ceded user control creates more risks to people.

### c80 — exists ✅ · applied ✅  (line 480)
_4.3 Agency law applied to AI agents. Kolt, N. (2025). Governing AI agents. arXiv:2501.07913; Notre Dame Law Review, 101, 335 (journal page proof dated 2026; issue not confirmed). https://arxiv.org/abs/2501.07913 [abstract; page proof read]_
- claude: exists=verified applied=verified [evidence_text] — The abstract confirms all three cited claims: agency-law characterization of problems, limits of conventional fixes, and the inclusivity/visibility/liability principles.
- gpt: exists=verified applied=verified [evidence_text] — arXiv metadata verifies the cited work, author, title, and arXiv ID. The abstract directly supports the claims about applying agency law and principal-agent theory, the limits of conventional fixes, and the proposed principles of inclusivity, visibility, and liability.

### c84 — exists ✅ · applied ✅  (line 513)
_5.1 Indirect prompt injection: anyone who can reach the agent's input can steer it. Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec '23), 79–90. https://doi.org/10.1145/3605764.3623985; arXiv:2302.12173 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv confirm the work; abstract directly states LLM-integrated apps blur data/instructions and retrieved prompts can act as arbitrary code execution and control API calls.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and arXiv metadata confirm the paper, authors, venue, pages, DOI, and arXiv ID. The retrieved abstract explicitly supports the claims about blurring data/instructions and retrieved prompts acting like arbitrary code execution, manipulating functionality, and controlling API calls.

### c86 — exists ✅ · applied ✅  (line 523)
_OWASP (2025). LLM06:2025 Excessive Agency. OWASP Top 10 for LLM Applications 2025. https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ **[abstract: page read]**_
- claude: exists=verified applied=verified [evidence_text] — Page fetch confirms the OWASP Excessive Agency definition verbatim including 'regardless of what is causing the LLM to malfunction' and the three root causes.
- gpt: exists=verified applied=verified [evidence_text] — The OWASP URL resolves to the cited LLM06:2025 Excessive Agency page. The retrieved page text directly states the definition of Excessive Agency and lists excessive functionality, permissions, and autonomy as root causes.

### c87 — exists ✅ · applied ✅  (line 533)
_Willison, S. (2025, 16 June). The lethal trifecta for AI agents: private data, untrusted content, and external communication. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ **[abstract: post read]**_
- claude: exists=verified applied=verified [evidence_text] — Fetched post confirms the three trifecta capabilities and the quoted claim about attackers tricking agents into exfiltrating private data.
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to Simon Willison's post with the cited title and date. The retrieved text directly states the three-part 'lethal trifecta' and the consequence that an attacker can trick an agent into sending private data.

### c89 — exists ✅ · applied ✅  (line 548)
_Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking indirect prompt injections in tool-integrated large language model agents. _Findings of ACL 2024_. https://doi.org/10.18653/v1/2024.findings-acl.624; arXiv:2403.02691 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv confirm the work; abstract states ReAct-prompted GPT-4 vulnerable 24% of the time and hacking prompt nearly doubling the attack success rate.
- gpt: exists=verified applied=verified [evidence_text] — Crossref, arXiv, and ACL URL evidence confirm the cited InjecAgent paper, venue, DOI, and authors. The retrieved abstract directly states the 24% ReAct-prompted GPT-4 vulnerability rate and that a hacking prompt nearly doubled the attack success rate.

### c91 — exists ✅ · applied ✅  (line 559)
_Zou, A., Lin, M., Jones, E., et al. (2025). Security challenges in AI agent deployment: Insights from a large scale public competition. arXiv:2507.20526. https://arxiv.org/abs/2507.20526 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the paper; abstract states 22 frontier agents across 44 scenarios, 1.8M prompt-injection attacks, over 60,000 eliciting policy violations, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv metadata and resolving URL confirm the cited paper, title, authors, and arXiv ID. The abstract directly supports the figures of 22 agents, 44 scenarios, 1.8 million attacks, over 60,000 policy violations, and the capability-related finding of limited correlation with capability/model size/compute.

### c92 — exists ✅ · applied ✅  (line 566)
_Ruan, Y., Dong, H., Wang, A., Pitis, S., Zhou, Y., Ba, J., Dubois, Y., Maddison, C. J., & Hashimoto, T. (2024). Identifying the risks of LM agents with an LM-emulated sandbox (ToolEmu). _ICLR 2024_. arXiv:2309.15817. https://arxiv.org/abs/2309.15817 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms ToolEmu; abstract states 68.8% of failures would be valid real-world failures, safest agent fails 23.9%, and 36 high-stakes tools.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv metadata and URL confirm the ToolEmu paper and authors. The abstract directly states the 23.9% failure rate for the safest agent, 68.8% real-world-valid failures, and the benchmark of 36 high-stakes tools.

### c93 — exists ✅ · applied ✅  (line 571)
_Zhang, Z., Cui, S., Lu, Y., Zhou, J., Yang, J., Wang, H., & Huang, M. (2024). Agent-SafetyBench: Evaluating the safety of LLM agents. arXiv:2412.14470. https://arxiv.org/abs/2412.14470 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms Agent-SafetyBench; abstract states none of 16 agents achieves a safety score above 60% and that defense prompts alone may be insufficient.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv metadata and URL confirm the Agent-SafetyBench preprint and authors. The abstract directly states that none of 16 popular LLM agents scored above 60% and that reliance on defense prompts alone may be insufficient.

### c101 — exists ✅ · applied ✅  (line 623)
_Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R., & Hobbhahn, M. (2024). Frontier models are capable of in-context scheming. arXiv:2412.04984. https://arxiv.org/abs/2412.04984 **[abstract; Apollo Research]**._
- claude: exists=verified applied=verified [evidence_text] — Abstract matches exactly, confirming in-context scheming across frontier models and the 85% figure for o1.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv lookup by ID matches the cited title and authors. The retrieved abstract directly states the claimed in-context scheming results and the over-85% o1 deception persistence figure.

### c103 — exists ✅ · applied ✅  (line 633)
_Debenedetti, E., Shumailov, I., Fan, T., Hayes, J., Carlini, N., Fabian, D., et al. (2025). Defeating prompt injections by design (CaMeL). arXiv:2503.18813. https://arxiv.org/abs/2503.18813 **[abstract; largely Google and Google DeepMind authors]**._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the protective system layer language and the 77% vs 84% task-success figures verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv lookup by ID matches the cited CaMeL paper and authors. The abstract directly contains the protective-system-layer claim and the 77% versus 84% AgentDojo result.

### c104 — exists ✅ · applied ✅  (line 638)
_South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). Authenticated delegation and authorized AI agents. arXiv:2501.09674. https://arxiv.org/abs/2501.09674 **[abstract]**._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms secure delegation with chains of accountability and extension of OAuth 2.0/OpenID Connect.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv lookup by ID matches the cited title and authors. The retrieved abstract directly supports the claims about secure delegation, restricted permissions/scope, accountability chains, and extending OAuth 2.0/OpenID Connect.

### c110 — exists ✅ · applied ✅  (line 667)
_Anthropic (2023, 19 September). Anthropic's Responsible Scaling Policy. https://www.anthropic.com/news/anthropics-responsible-scaling-policy **[abstract: page read; vendor]**. "Require safety, security, and operational standards appropriate to a model's potential for catastrophic risk, with higher ASL levels requiring increasingly strict demonstrations of safety." (A later version exists; not read.)_
- claude: exists=verified applied=verified [evidence_text] — Fetched page contains the quoted ASL language about safety standards appropriate to catastrophic risk nearly verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to the cited Responsible Scaling Policy page. The retrieved page text directly states the quoted ASL framework language about safety, security, operational standards, catastrophic risk, and increasingly strict demonstrations of safety.

### c121 — exists ✅ · applied ✅  (line 737)
_Santoni de Sio, F., & Mecacci, G. (2021). Four responsibility gaps with artificial intelligence: Why they matter and how to address them. _Philosophy & Technology_, 34(4), 1057–1084. https://doi.org/10.1007/s13347-021-00450-x **[abstract]**. "Not one problem but a set of at least four interconnected problems"; remedy: "meaningful human control"._
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the exact article; abstract verbatim contains both the 'set of at least four interconnected problems' framing and 'meaningful human control' as the remedy.
- gpt: exists=verified applied=verified [evidence_text] — Crossref DOI metadata matches the authors, title, journal, volume/issue, pages, year, and DOI. The retrieved abstract explicitly says the responsibility gap is “not one problem but a set of at least four interconnected problems” and proposes meaningful human control as the comprehensive approach.

### c123 — exists ✅ · applied ✅  (line 745)
_Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). Visibility into AI agents. _FAccT 2024_. https://doi.org/10.1145/3630106.3658948; arXiv:2401.13138 **[abstract]**. Assesses "agent identifiers, real-time monitoring, and activity logging"._
- claude: exists=verified applied=verified [evidence_text] — DOI and arXiv both confirm the paper; abstract explicitly assesses 'agent identifiers, real-time monitoring, and activity logging.'
- gpt: exists=verified applied=verified [evidence_text] — Crossref and arXiv metadata match the cited title, authors, year, DOI, and arXiv ID. The arXiv abstract explicitly states that the paper assesses agent identifiers, real-time monitoring, and activity logging.
