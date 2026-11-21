# cite-check report: essay 07, the approval-fatigue line (2026-11-20)

**Source:** `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`, the paragraph beginning "The usual way to keep a person involved". Hughes 2026 is new (not in brief 13). Green 2022 came along in the excerpt; its degraded flag here is a retrieval limit (DOI redirect only) and it passed with evidence in the 11-18 check.


_(Run on an excerpt of the approval-fatigue paragraph, taken from the essay draft.)_

## Coverage (read this first)
- **2** citations checked
- existence independently confirmed: **2**
- application evidence-grounded: **2**
- application judged from model knowledge only: **1**
- not independently checkable: **0**
- buckets — clean **1** · problem **1** · disagree **0**

## ⚠️ AGREE-problem (1)
### c01 — exists ✅ · applied ✅  · ⚑ degraded  (line 7)
_Ben Green reviewed 41 government policies that require people to oversee automated decisions. He wrote that "evidence suggests that people are unable to perform the desired oversight functions", and that the requirement can give "a false sense of security" ([Green 2022](https://doi.org/10.1016/j.clsr.2022.105681))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the Green 2022 article on flaws of policies requiring human oversight of government algorithms. The retrieved snippet was only 'Redirecting', so the specific quotes and 41-policy figure rely on model knowledge, which aligns with the paper's known content.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms DOI 10.1016/j.clsr.2022.105681 as Ben Green’s 2022 article, “The flaws of policies requiring human oversight of government algorithms,” in Computer Law & Security Review. The retrieved text did not include substantive source content beyond redirect/title metadata, but from model knowledge the cited claims match the article’s findings; confidence is capped accordingly.

## ✅ AGREE-clean (1)
### c02 — exists ✅ · applied ✅  (line 11)
_Anthropic says that people using its coding tool accept 93 in every 100 of those prompts, and it warns of "approval fatigue, where people stop paying close attention to what they're approving" ([Hughes 2026](https://www.anthropic.com/engineering/claude-code-auto-mode))_
- claude: exists=verified applied=verified [evidence_text] — The fetched Anthropic page explicitly states users accept 93% of prompts and warns of 'approval fatigue, where people stop paying close attention to what they're approving', matching both claims verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to “How we built Claude Code auto mode,” published Mar. 25, 2026. The retrieved page text explicitly says approval prompts lead to “approval fatigue,” defines it as people stopping paying close attention, and states users accept 93% of prompts.
