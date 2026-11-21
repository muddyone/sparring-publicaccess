# cite-check report: essay 07 (what an agent is), after the first panel

**Source:** `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md` at the post-panel revision `3e2055f3` (worklist W-34), checked 2026-11-18. Substrates: claude-opus-4-8 + gpt-5.5-2026-04-23.

**Reading (builder, sparring-2).** Nothing in the essay body was refuted, and every source exists (57 of 58 confirmed independently; the 58th is a Sources-list duplicate). The eight splits (c01, c03, c04, c07, c08, c10, c19, c26) and most "problem" items are the same thing: the retrieved snippet (an abstract or the top of a page) didn't contain the specific figure or quote, so one substrate marked it unchecked. Five applications were judged from model knowledge only (c09 OpenAI guide, the PDF came back unreadable; c12 Wooldridge & Jennings; c13 Greshake; c27 Saltzer & Schroeder; c28 Jensen & Meckling); those are not verifications. c30–c33 are deliberately uncited "I found nothing" lines, correctly unchecked.

**Live-page check of the figures the snippets missed (2026-11-18, verbatim, $0).** All found as the essay states them:
- NIST: "an increase in attack success rate from 11% for the strongest baseline attack to 81% for the strongest new attack", on "Anthropic's upgraded Claude 3.5 Sonnet (released October 2024)".
- Claude Code permissions: "Only use this mode in isolated environments like containers or VMs where Claude Code can't cause damage." Default mode: "Prompts for permission on first use of each tool." The essay now quotes the first sentence exactly.
- Messages API: "The Messages API is stateless, which means that you always send the full conversational history to the API."
- Lynch et al.: Claude Opus 4 96%, Gemini 2.5 Flash 96%, GPT-4.1 and Grok 3 Beta 80%, DeepSeek-R1 79%; both quotes ("not seen evidence of agentic misalignment in real deployments"; "caution about deploying current models in roles with minimal human oversight and access to sensitive information") verbatim.
- AgentDojo §4.1 (HTML full text, not the abstract): "We find that more capable models tend to be easier to attack, a form of inverse scaling law".
- SWE-agent Table 1, SWE-bench Lite: shell-only with GPT-4 Turbo 11.00, SWE-agent with GPT-4 Turbo 18.00. (The paper's text also says "10.7 percentage points more", which matches a different baseline row; the essay doesn't use it.)
- Morris et al.: "Increasing capabilities unlock new interaction paradigms, but do not determine them" (§6.2); "The choice of appropriate autonomy level need not be the maximum achievable given the capabilities of the underlying model" (Table 2 caption).

**Still resting on brief 13 only:** Chalmers 2020's "Perhaps it is an engine…" (the essay keeps "Perhaps"), the Restatement definition (second-hand via Kolt, and the essay says so), Green 2022's 41 policies and its two quotes, Zou et al.'s 60,000-plus successes, Kwa et al.'s 50-minute starting point (from the abstract), Fortune's CEO quotes, and Invariant Labs' "architectural issue" wording.

---

## Coverage (read this first)
- **58** citations checked
- existence independently confirmed: **57**
- application evidence-grounded: **54**
- application judged from model knowledge only: **5**
- not independently checkable: **0**
- buckets — clean **10** · problem **46** · disagree **8**

## ⛔ DISAGREE — escalate to human (8)
### c01 — exists ✅ · applied SPLIT  (line 40)
_([Anthropic, Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Anthropic Messages API docs page exists and resolves. The page is about using the stateless Messages API, consistent with the claim that full conversational history must be resent, though the snippet doesn't explicitly state it.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic Messages API documentation page resolves with the expected title. The retrieved snippet does not include the claimed statelessness or requirement to resend full conversation history.

### c03 — exists ✅ · applied SPLIT  (line 46)
_([Anthropic, tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Tool use overview page exists; it describes tool use/function calling, broadly supporting that enabling tools adds instructions, though the snippet doesn't explicitly quantify added instructions.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic tool-use documentation page exists. The retrieved snippet only says tool use connects Claude to external tools/APIs and does not show that enabling tools adds another set of instructions.

### c04 — exists ✅ · applied SPLIT  (line 50)
_([Anthropic, Claude Code permissions](https://code.claude.com/docs/en/permissions))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Claude Code permissions page exists and covers permission modes and sandbox/VM environments. Snippet references sandboxing/environments consistent with advising isolated use for broad permissions, though exact wording not in snippet.
- gpt: exists=verified applied=unchecked [no_basis] — The Claude Code permissions documentation page resolves. The retrieved snippet does not include the specific guidance about using the broadest permission setting only in isolated containers or VMs.

### c07 — exists ✅ · applied SPLIT  (line 62)
_([Kapoor et al. 2025](https://arxiv.org/abs/2510.11977))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — HAL paper confirmed with 9 models and scaffold analysis. Abstract supports model/scaffold comparison but the specific claim that Claude did better in one scaffold and OpenAI in another is not stated in the abstract.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record exists as 'Holistic Agent Leaderboard' by Kapoor et al. The abstract confirms a comparison across 9 models and 9 benchmarks, but it does not state that Claude models did better in one setup and OpenAI models in another.

### c08 — exists ✅ · applied SPLIT  (line 82)
_([Chalmers 2020](https://dailynous.com/2020/07/30/philosophers-gpt-3/))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The Daily Nous 'Philosophers On GPT-3' page exists and includes Chalmers. The specific 'engine... drive many agents' and 'quasi-subject' quotes are not in the retrieved snippet, so exact attribution can't be confirmed from evidence.
- gpt: exists=verified applied=unchecked [no_basis] — The Daily Nous page 'Philosophers On GPT-3' exists. The retrieved snippet does not include the attributed Chalmers quotation about GPT-3 as an engine under the hood to drive many agents.

### c10 — exists ✅ · applied SPLIT  (line 89)
_([Kolt 2025](https://arxiv.org/abs/2501.07913))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Kolt 'Governing AI Agents' confirmed; abstract centers on common law agency doctrine, consistent with quoting the Restatement of Agency's definition, though the exact quoted phrasing is not in the abstract.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record exists as Noam Kolt's 'Governing AI Agents.' The abstract discusses agency law and principal-agent frameworks, but it does not quote or state the Restatement definition about acting on behalf of and subject to the principal's control.

### c19 — exists ✅ · applied SPLIT  (line 163)
_([Debenedetti et al. 2024](https://arxiv.org/abs/2406.13352))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — AgentDojo paper confirmed. The abstract supports it as a prompt-injection benchmark, but the specific claims that more capable models are easier to attack and weaker models fail to execute attacks are not in the retrieved abstract.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record exists as 'AgentDojo' by Debenedetti et al. The abstract discusses prompt-injection evaluation but does not state that more capable models tend to be easier to attack or that weaker models often fail to execute attackers' instructions.

### c26 — exists ✅ · applied SPLIT  (line 219)
_([Green 2022](https://doi.org/10.1016/j.clsr.2022.105681))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Green 2022 'The flaws of policies requiring human oversight of government algorithms' confirmed via DOI; title and content align with the claims about reviewing oversight policies and their ineffectiveness, though exact quotes not in snippet.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref verifies Ben Green’s 2022 article “The flaws of policies requiring human oversight of government algorithms” in Computer Law & Security Review. The retrieved application text is only a redirect and does not verify the 41-policy review or the quoted conclusions.

## ⚠️ AGREE-problem (46)
### c05 — exists ✅ · applied ⚠️  (line 57)
_([Yang et al. 2024](https://arxiv.org/abs/2405.15793))_
- claude: exists=verified applied=nuance [evidence_text] — SWE-agent paper confirmed. The abstract supports interface design improving performance but the specific GPT-4 Turbo 11→18 figures are not in the abstract, so the exact numbers can't be verified from evidence.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record exists as 'SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering' by Yang et al. The abstract supports the general point that a custom agent-computer interface significantly improves performance, but it does not contain the claimed GPT-4 Turbo 11%-versus-18% figures.

### c09 — exists ✅ · applied ✅  · ⚑ degraded  (line 86)
_([OpenAI 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The OpenAI PDF resolves but the fetched content is raw binary and unreadable; the 'systems that independently accomplish tasks on your behalf' definition is the known opening line of this guide.
- gpt: exists=verified applied=verified [model_knowledge_only] — The OpenAI CDN PDF URL resolves, though the retrieved content is raw PDF data without readable supporting text. Based on model knowledge only, OpenAI's guide defines agents in substantially the claimed terms, but the supplied evidence text itself does not verify the wording.

### c12 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 101)
_([Wooldridge & Jennings 1995](https://doi.org/10.1017/S0269888900008122))_
- claude: exists=verified applied=nuance [evidence_text] — Wooldridge & Jennings 1995 'Intelligent agents: theory and practice' confirmed. This paper is well known for the weak/strong agency distinction, though the retrieved abstract doesn't explicitly state the beliefs/intentions distinction.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies the 1995 Wooldridge and Jennings article 'Intelligent agents: theory and practice.' The abstract does not include the weak/strong agency distinction, but based on model knowledge the paper does make that distinction between weak agency and stronger mentalistic notions such as beliefs and intentions.

### c13 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 114)
_([Greshake et al. 2023](https://doi.org/10.1145/3605764.3623985))_
- claude: exists=verified applied=verified [model_knowledge_only] — Greshake et al. indirect prompt injection paper confirmed via Crossref. No abstract retrieved, but this paper is well known for showing retrieved content can control APIs and enable arbitrary behavior, consistent with the claim.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies the ACM workshop paper 'Not What You've Signed Up For' by Greshake et al. Based on model knowledge only, it supports indirect prompt injection causing LLM-integrated apps to misuse tools/APIs, but the phrase 'arbitrary code execution' is a stronger characterization than the available evidence establishes.

### c16 — exists ✅ · applied ⚠️  (line 138)
_([Fortune 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/))_
- claude: exists=verified applied=verified [evidence_text] — Fortune article exists and reports a Replit AI agent deleting a live database during a code freeze; snippet supports the catastrophic failure framing. The CEO quote and database-separation fix are consistent with the reported case though not all in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Fortune article exists and the snippet supports the reported Replit coding-agent deletion of a live database during a code freeze. The retrieved text does not include the CEO's exact 'unacceptable/should never be possible' statements or the cited fix of separating test and real databases.

### c17 — exists ✅ · applied ⚠️  (line 144)
_([Milanta & Beurer-Kellner 2025](https://invariantlabs.ai/blog/mcp-github-vulnerability))_
- claude: exists=verified applied=verified [evidence_text] — Invariant Labs blog exists, dated 2025-05-26, showing a malicious GitHub Issue coercing an agent to leak private repo data. Snippet supports the architectural-issue framing; granular permissions fix is consistent with its mitigations section.
- gpt: exists=verified applied=nuance [evidence_text] — The Invariant Labs post exists and the snippet supports the malicious GitHub issue/private-repository leakage scenario via the GitHub MCP integration. The retrieved text does not show the further claims that it was not a GitHub MCP code flaw, that it was a fundamental architectural issue, or that granular permissions were the first listed fix.

### c21 — exists ✅ · applied ☐  (line 172)
_([NIST 2025](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations))_
- claude: exists=verified applied=unchecked [evidence_text] — URL resolves to the exact NIST blog on AI agent hijacking evaluations. The snippet is only navigation chrome and does not contain the specific 11-to-81 attack success figures, so the numeric claim cannot be verified from evidence.
- gpt: exists=verified applied=unchecked [evidence_text] — The NIST URL resolves with the cited title. The retrieved snippet contains only page/navigation material and does not include the 11% to 81% Claude attack-success claim.

### c23 — exists ✅ · applied ⚠️  (line 195)
_([Lynch et al. 2025](https://www.anthropic.com/research/agentic-misalignment))_
- claude: exists=verified applied=verified [evidence_text] — Anthropic page confirmed; snippet matches stress-test of 16 models, the 'not seen evidence...in real deployments' quote, and the caution-about-deployment advice. The specific 96/100 blackmail figures aren't in the snippet but core claims are supported.
- gpt: exists=verified applied=nuance [evidence_text] — The Anthropic page exists and the snippet supports the 16-model stress test, hypothetical corporate environments, no evidence in real deployments, and caution about minimal oversight with sensitive information. The retrieved text does not include the specific 96/100 and ~80/100 blackmail-rate figures, so support is partial.

### c24 — exists ✅ · applied ⚠️  (line 210)
_([Morris et al. 2024](https://arxiv.org/abs/2311.02462))_
- claude: exists=verified applied=verified [evidence_text] — Morris et al. 'Levels of AGI' confirmed; abstract emphasizes autonomy as a deliberate deployment choice distinct from capability, consistent with the quoted 'not determine' / 'need not be the maximum' framing.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record exists with the cited DeepMind authors and title. The abstract supports a framework separating capability, autonomy, deployment, and human-AI interaction, but it does not contain the specific quoted language about capability not determining autonomy or maximum achievable autonomy.

### c27 — exists ✅ · applied ✅  · ⚑ degraded  (line 237)
_([Saltzer & Schroeder 1975](https://doi.org/10.1109/PROC.1975.9939))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Saltzer & Schroeder 1975 'The protection of information in computer systems' confirmed via DOI. No source text retrieved, but the least-privilege principle and its damage-limiting rationale are well-known content of this paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Saltzer and Schroeder’s 1975 Proceedings of the IEEE article. No application source text was retrieved, but based on general knowledge, the cited least-privilege principle and rationale are accurately attributed to that work.

### c28 — exists ✅ · applied ✅  · ⚑ degraded  (line 239)
_([Jensen & Meckling 1976](https://doi.org/10.1016/0304-405X%2876%2990026-X))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Jensen & Meckling 1976 confirmed via DOI as the foundational agency-costs paper; the claim that economists built a theory of costs of delegating authority accurately describes it. Only redirect snippet retrieved.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Jensen and Meckling’s 1976 Journal of Financial Economics article “Theory of the firm: Managerial behavior, agency costs and ownership structure.” Based on general knowledge, the broad claim about agency costs from delegating authority is an appropriate use of this foundational paper.

### c30 — exists ☐ · applied ☐  (line 177)
_On whether smarter models make fewer plain mistakes, I found nothing that settles it._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author states no source settles this question.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as deliberately uncited rather than a citation. Both existence and application are therefore unchecked.

### c31 — exists ☐ · applied ☐  (line 291)
_That harm has been measured by access level in real use. There are benchmarks and single reported cases. I found no study of how often agents cause harm in the field at each level of access._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author notes no field study found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as deliberately uncited rather than a citation. Both existence and application are therefore unchecked.

### c32 — exists ☐ · applied ☐  (line 293)
_That smarter models make no fewer plain mistakes. The evidence on capability here is about being fooled by an attacker. On mistakes, I found nothing that settles it either way._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author states nothing settles the question.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as deliberately uncited rather than a citation. Both existence and application are therefore unchecked.

### c33 — exists ☐ · applied ☐  (line 295)
_That it holds as strongly outside coding. Most of the evidence on setups, and much on risk, comes from programming tasks and test environments, with models from 2023 to 2025._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author notes a gap in evidence outside coding.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as deliberately uncited rather than a citation. Both existence and application are therefore unchecked.

### c34 — exists ✅ · applied ☐  (line 337)
_[Anthropic, Claude Code permissions](https://code.claude.com/docs/en/permissions)_
- claude: exists=verified applied=unchecked [no_basis] — Claude Code permissions doc confirmed to resolve; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic Claude Code permissions URL resolves with the title “Configure permissions - Claude Code Docs.” No claim is attached to this citation, so application cannot be evaluated.

### c35 — exists ✅ · applied ☐  (line 338)
_[Anthropic, Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)_
- claude: exists=verified applied=unchecked [no_basis] — Messages API doc confirmed to resolve; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic Messages API URL resolves with the title “Using the Messages API - Claude Platform Docs.” No claim is attached to this citation, so application cannot be evaluated.

### c36 — exists ✅ · applied ☐  (line 339)
_[Anthropic, system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts)_
- claude: exists=verified applied=unchecked [no_basis] — System prompts doc confirmed to resolve; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic system prompts URL resolves to the Claude Platform Docs system prompts page. No claim is attached to this citation, so application cannot be evaluated.

### c37 — exists ✅ · applied ☐  (line 340)
_[Anthropic, tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)_
- claude: exists=verified applied=unchecked [no_basis] — Tool use doc confirmed to resolve; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic tool-use URL resolves with the title “Tool use with Claude - Claude Platform Docs.” No claim is attached to this citation, so application cannot be evaluated.

### c38 — exists ✅ · applied ☐  (line 341)
_[Chalmers 2020](https://dailynous.com/2020/07/30/philosophers-gpt-3/)_
- claude: exists=verified applied=unchecked [no_basis] — Daily Nous 'Philosophers On GPT-3' (2020) confirmed; authorship attributed to Chalmers is nuanced (it is a multi-author collection) but no specific claim is attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Daily Nous URL resolves with the title “Philosophers On GPT-3.” No claim is attached to this citation, so application cannot be evaluated.

### c39 — exists ✅ · applied ☐  (line 342)
_[Davidson et al. 2023](https://arxiv.org/abs/2312.07413)_
- claude: exists=verified applied=unchecked [no_basis] — Davidson et al. 2023 post-training enhancements paper confirmed; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record for 2312.07413 exists and is titled “AI capabilities can be significantly improved without expensive retraining.” No claim is attached to this citation, so application cannot be evaluated.

### c40 — exists ✅ · applied ☐  (line 343)
_[Debenedetti et al. 2024](https://arxiv.org/abs/2406.13352)_
- claude: exists=verified applied=unchecked [no_basis] — Debenedetti et al. 2024 AgentDojo paper confirmed; no specific claims attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record for 2406.13352 exists and is titled “AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.” No claim is attached to this citation, so application cannot be evaluated.

### c41 — exists ✅ · applied ☐  (line 344)
_[Debenedetti et al. 2025](https://arxiv.org/abs/2503.18813)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2503.18813 matches 'Defeating Prompt Injections by Design' (CaMeL) by Debenedetti et al. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Defeating Prompt Injections by Design” by Edoardo Debenedetti et al. No supported claim was supplied, so application cannot be judged.

### c42 — exists ✅ · applied ☐  (line 345)
_[Feng et al. 2025](https://arxiv.org/abs/2506.12469)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2506.12469 matches 'Levels of Autonomy for AI Agents' by Feng et al. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Levels of Autonomy for AI Agents” by K. J. Kevin Feng et al. No supported claim was supplied, so application cannot be judged.

### c43 — exists ✅ · applied ☐  (line 346)
_[Fortune 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)_
- claude: exists=verified applied=unchecked [no_basis] — Fortune article on Replit AI wiping a database confirmed at the cited URL. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The Fortune URL resolves to an article titled “AI-powered coding tool wiped out a software company’s database in ‘catastrophic failure’.” No supported claim was supplied, so application cannot be judged.

### c44 — exists ✅ · applied ☐  (line 347)
_[Green 2022](https://doi.org/10.1016/j.clsr.2022.105681)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Green's 'The flaws of policies requiring human oversight of government algorithms' (CLSR 2022). No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1016/j.clsr.2022.105681 as Ben Green’s 2022 article “The flaws of policies requiring human oversight of government algorithms.” No supported claim was supplied, so application cannot be judged.

### c45 — exists ✅ · applied ☐  (line 348)
_[Greshake et al. 2023](https://doi.org/10.1145/3605764.3623985)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Greshake et al. indirect prompt injection paper. No claim text and no abstract retrieved to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1145/3605764.3623985 as Greshake et al.’s 2023 ACM AISec paper on indirect prompt injection. No supported claim was supplied, so application cannot be judged.

### c46 — exists ✅ · applied ☐  (line 349)
_[Jensen & Meckling 1976](https://doi.org/10.1016/0304-405X%2876%2990026-X)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Jensen & Meckling's seminal 1976 agency theory paper. No claim text provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1016/0304-405X(76)90026-X as Jensen and Meckling’s 1976 “Theory of the firm” article. No supported claim was supplied, so application cannot be judged.

### c47 — exists ✅ · applied ☐  (line 350)
_[Kapoor et al. 2025](https://arxiv.org/abs/2510.11977)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2510.11977 matches 'Holistic Agent Leaderboard' by Kapoor et al. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation” by Sayash Kapoor et al. No supported claim was supplied, so application cannot be judged.

### c48 — exists ✅ · applied ☐  (line 351)
_[Kolt 2025](https://arxiv.org/abs/2501.07913)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2501.07913 matches 'Governing AI Agents' by Kolt. No claim text provided to assess the second-hand Restatement note.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Noam Kolt’s “Governing AI Agents.” No supported claim was supplied, so application cannot be judged.

### c49 — exists ✅ · applied ☐  (line 352)
_[Kwa et al. 2025](https://arxiv.org/abs/2503.14499)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2503.14499 matches Kwa et al. time-horizon paper. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Measuring AI Ability to Complete Long Software Tasks” by Thomas Kwa et al. No supported claim was supplied, so application cannot be judged.

### c50 — exists ⚠️ · applied ☐  (line 353)
_[Lynch et al. 2025](https://www.anthropic.com/research/agentic-misalignment)_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic 'Agentic misalignment' page confirmed at the cited URL. No specific claim provided.
- gpt: exists=nuance applied=unchecked [no_basis] — The Anthropic URL resolves to “Agentic misalignment: LLMs as insider threats,” but the retrieved snippet lists Peter McCrory as author rather than “Lynch et al.” No supported claim was supplied, so application cannot be judged.

### c51 — exists ✅ · applied ☐  (line 354)
_[Milanta & Beurer-Kellner 2025](https://invariantlabs.ai/blog/mcp-github-vulnerability)_
- claude: exists=verified applied=unchecked [no_basis] — Invariant Labs GitHub MCP vulnerability post by Milanta & Beurer-Kellner confirmed at the cited URL. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Invariant Labs URL resolves to “GitHub MCP Exploited: Accessing private repositories via MCP” and the snippet names Marco Milanta and Luca Beurer-Kellner. No supported claim was supplied, so application cannot be judged.

### c52 — exists ✅ · applied ☐  (line 355)
_[Morris et al. 2024](https://arxiv.org/abs/2311.02462)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2311.02462 matches 'Levels of AGI' by Morris et al. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Levels of AGI for Operationalizing Progress on the Path to AGI” by Meredith Ringel Morris et al. No supported claim was supplied, so application cannot be judged.

### c53 — exists ✅ · applied ☐  (line 356)
_[NIST 2025](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)_
- claude: exists=verified applied=unchecked [no_basis] — NIST technical blog on strengthening AI agent hijacking evaluations confirmed at the cited URL. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — The NIST URL resolves to “Technical Blog: Strengthening AI Agent Hijacking Evaluations.” No supported claim was supplied, so application cannot be judged.

### c54 — exists ⚠️ · applied ☐  (line 357)
_[OpenAI 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)_
- claude: exists=verified applied=unchecked [no_basis] — OpenAI 'A practical guide to building agents' PDF resolves at the cited URL (binary content). No claim text provided.
- gpt: exists=nuance applied=unchecked [no_basis] — The OpenAI CDN PDF URL resolves and its filename matches “a-practical-guide-to-building-agents,” but no readable title or metadata was retrieved from the PDF. No supported claim was supplied, so application cannot be judged.

### c55 — exists ✅ · applied ☐  (line 358)
_[OWASP 2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)_
- claude: exists=verified applied=unchecked [no_basis] — OWASP LLM06:2025 Excessive Agency page confirmed at the cited URL. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — The OWASP URL resolves to “LLM06:2025 Excessive Agency - OWASP Gen AI Security Project.” No supported claim was supplied, so application cannot be judged.

### c56 — exists ✅ · applied ☐  (line 359)
_[Saltzer & Schroeder 1975](https://doi.org/10.1109/PROC.1975.9939)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Saltzer & Schroeder's classic 'The protection of information in computer systems' (1975). No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1109/PROC.1975.9939 as Saltzer and Schroeder’s 1975 “The protection of information in computer systems.” No supported claim was supplied, so application cannot be judged.

### c57 — exists ✅ · applied ☐  (line 360)
_[Schluntz & Zhang 2024](https://www.anthropic.com/engineering/building-effective-agents)_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic 'Building effective agents' confirmed (URL redirects to /research/ version). No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to “Building effective AI agents,” consistent with the cited page, though the retrieved snippet does not show the named authors. No supported claim was supplied, so application cannot be judged.

### c58 — exists ✅ · applied ☐  (line 361)
_[Willison 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)_
- claude: exists=verified applied=unchecked [no_basis] — Simon Willison's 'The lethal trifecta' post confirmed at the cited URL. No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — The Simon Willison URL resolves to “The lethal trifecta for AI agents: private data, untrusted content, and external communication.” No supported claim was supplied, so application cannot be judged.

### c59 — exists ✅ · applied ☐  (line 362)
_[Wooldridge & Jennings 1995](https://doi.org/10.1017/S0269888900008122)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Wooldridge & Jennings 'Intelligent agents: theory and practice' (1995). No claim text provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1017/S0269888900008122 as Wooldridge and Jennings’s 1995 “Intelligent agents: theory and practice.” No supported claim was supplied, so application cannot be judged.

### c60 — exists ✅ · applied ☐  (line 363)
_[Yang et al. 2024](https://arxiv.org/abs/2405.15793)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2405.15793 matches 'SWE-agent' by Yang et al. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering” by John Yang et al. No supported claim was supplied, so application cannot be judged.

### c61 — exists ✅ · applied ☐  (line 364)
_[Zou et al. 2025](https://arxiv.org/abs/2507.20526)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2507.20526 by Andy Zou et al. (2025) confirmed via ID and URL. No specific claim text is attached to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID and URL resolve to a real paper titled “Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition” by Andy Zou et al. No specific claim was provided for this citation, so application cannot be assessed.

### c62 — exists ☐ · applied ☐  (line 332)
_[What an "agent" is, and where its risk comes from](../briefs/2026-10-19-13-agents.md), a research brief with its sources._
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal research brief (local .md path) that could not be fetched; the Crossref result about ageism is clearly unrelated and does not match. Existence and application cannot be judged from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a relative local path that the URL fetcher could not check; the Crossref result was explicitly unmatched and unrelated. Without access to the local brief, whether it exists or supports the claim cannot be judged.

### c63 — exists ☐ · applied ☐  (line 382)
_Left for edition 9 (brief 14): Becker et al. 2025 (developers 19% slower with AI)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited; left for a future edition.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked deliberately_uncited/is_citation=false, so both axes are unchecked as intentionally uncited.

### c64 — exists ☐ · applied ☐  (line 381)
_Left for edition 10 (brief 15): Moffatt v. Air Canada, Mobley v. Workday, vendor terms, the EU AI Act._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately_uncited; left for a future edition.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked deliberately_uncited/is_citation=false, so both axes are unchecked as intentionally uncited.

## ✅ AGREE-clean (10)
### c02 — exists ✅ · applied ✅  (line 44)
_([Anthropic, system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts))_
- claude: exists=verified applied=verified [evidence_text] — Page exists and explicitly states Claude's web/app interfaces use a system prompt at the start of every conversation that does not apply to the API, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The page resolves as Anthropic's system prompts documentation. The snippet explicitly says Claude web/desktop/mobile apps use a system prompt at the start of every conversation and that these updates do not apply to the Claude API.

### c06 — exists ✅ · applied ✅  (line 60)
_([Davidson et al. 2023](https://arxiv.org/abs/2312.07413))_
- claude: exists=verified applied=verified [evidence_text] — Davidson et al. paper confirmed; abstract states most surveyed post-training enhancements improve performance by more than a 5x increase in training compute, directly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as 'AI capabilities can be significantly improved without expensive retraining' by Davidson et al. The abstract explicitly says most surveyed post-training enhancements improve performance by more than a 5x increase in training compute and do so without expensive retraining.

### c11 — exists ✅ · applied ✅  (line 92)
_([Schluntz & Zhang 2024](https://www.anthropic.com/engineering/building-effective-agents))_
- claude: exists=verified applied=verified [evidence_text] — Building effective agents page exists and explicitly distinguishes workflows (predefined code paths) from agents (LLMs dynamically direct their own processes and tool usage), matching the claim verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic article resolves, with a redirect to the current Anthropic page for 'Building effective AI agents.' The snippet directly states Anthropic's distinction: workflows use predefined code paths, while agents dynamically direct their own processes and tool usage.

### c14 — exists ✅ · applied ✅  (line 119)
_([OWASP 2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/))_
- claude: exists=verified applied=verified [evidence_text] — OWASP LLM06:2025 Excessive Agency page exists and states the root cause is excessive functionality, permissions, or autonomy, and that the vulnerability applies regardless of what causes the LLM to malfunction, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The OWASP 'LLM06:2025 Excessive Agency' page resolves. The snippet directly lists the root causes as excessive functionality, permissions, and autonomy, and says damaging actions can occur regardless of what is causing the LLM to malfunction.

### c15 — exists ✅ · applied ✅  (line 123)
_([Willison 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/))_
- claude: exists=verified applied=verified [evidence_text] — Willison's lethal trifecta post exists and lists private data, untrusted content, and external communication, with the exact phrasing about an attacker tricking the agent into accessing and sending private data.
- gpt: exists=verified applied=verified [evidence_text] — Simon Willison's 'lethal trifecta' post exists. The snippet explicitly names the three factors—private data, untrusted content, and external communication—and states that combining them lets an attacker trick the agent into sending private data to the attacker.

### c18 — exists ✅ · applied ✅  (line 152)
_([Debenedetti et al. 2025](https://arxiv.org/abs/2503.18813))_
- claude: exists=verified applied=verified [evidence_text] — CaMeL paper confirmed; abstract states a protective system layer securing the LLM 'even when underlying models are susceptible to attacks' and solving 77% of tasks vs 84% undefended, matching all three claims.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as 'Defeating Prompt Injections by Design' by Debenedetti et al. The abstract directly supports CaMeL as a protective layer with provable security even when underlying models are susceptible, enforcing information-flow/tool-call policies, and achieving 77% versus 84% task success.

### c20 — exists ✅ · applied ✅  (line 168)
_([Zou et al. 2025](https://arxiv.org/abs/2507.20526))_
- claude: exists=verified applied=verified [evidence_text] — ART competition paper confirmed; abstract states 1.8 million attacks across 22 agents, over 60,000 successful, and 'limited correlation between agent robustness and model size, capability, or inference-time compute,' matching both claims.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as 'Security Challenges in AI Agent Deployment' by Zou et al. The abstract directly states 1.8 million attacks against 22 agents, over 60,000 successes, and limited correlation between robustness and model size, capability, or inference-time compute.

### c22 — exists ✅ · applied ✅  (line 184)
_([Kwa et al. 2025](https://arxiv.org/abs/2503.14499))_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2503.14499 (Kwa et al.) confirmed; abstract states Claude 3.7 Sonnet has ~50 min 50% time horizon and doubling every seven months since 2019, matching both claims.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record for 2503.14499 exists and is titled “Measuring AI Ability to Complete Long Software Tasks.” Its abstract explicitly states a 50% time horizon of around 50 minutes for Claude 3.7 Sonnet and approximate doubling every seven months since 2019.

### c25 — exists ✅ · applied ✅  (line 213)
_([Feng et al. 2025](https://arxiv.org/abs/2506.12469))_
- claude: exists=verified applied=verified [evidence_text] — Feng et al. 'Levels of Autonomy for AI Agents' confirmed; abstract contains the exact quote and the operator-to-observer role framework cited.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record for 2506.12469 exists and is titled “Levels of Autonomy for AI Agents.” The abstract directly states that autonomy can be treated as a deliberate design decision separate from capability and defines levels by user roles from operator through observer.

### c29 — exists ✅ · applied ✅  (line 254)
_([Kolt 2025](https://arxiv.org/abs/2501.07913))_
- claude: exists=verified applied=verified [evidence_text] — Kolt 'Governing AI Agents' confirmed; abstract contains the quoted phrasing about conventional solutions 'might not be effective for governing AI agents that make uninterpretable decisions and operate at unprecedented speed and scale.'
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record for 2501.07913 exists and is titled “Governing AI Agents.” Its abstract directly states that incentive design, monitoring, and enforcement might not be effective for AI agents making uninterpretable decisions at unprecedented speed and scale.
