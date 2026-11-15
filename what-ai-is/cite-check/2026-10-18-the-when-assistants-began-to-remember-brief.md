# cite-check report — brief10

**Source:** `briefs/2026-10-18-10-when-assistants-began-to-remember.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **11** citations checked
- existence independently confirmed: **7**
- application evidence-grounded: **7**
- application judged from model knowledge only: **4**
- not independently checkable: **4**
- buckets — clean **4** · problem **13** · disagree **0**

## ⚠️ AGREE-problem (13)
### c01 — exists ☐ · applied ☐  (line 18)
_**A model could always learn within one conversation,** from examples placed in it. What early assistants lacked was keeping anything once the conversation ended._
- claude: exists=unchecked applied=unchecked [no_basis] — Narrative statement, not a citation (is_citation=false); no evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are left unchecked as uncited source text.

### c02 — exists ☐ · applied ☐  (line 20)
_**Keeping things arrived in steps, and in earnest in 2024–2025:** much longer conversations (2023), standing instructions (ChatGPT, July 2023), memory across conversations (ChatGPT 2024, extended to all past chats in April 2025; Claude September–October 2025), and AI agents that keep their own written notes (2025)._
- claude: exists=unchecked applied=unchecked [no_basis] — Narrative statement, not a citation; no evidence provided to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are left unchecked as uncited source text.

### c03 — exists ☐ · applied ☐  (line 24)
_**So yes: before memory, the AI assistant in use was a much weaker learner.** It could learn for an hour and keep none of it. The line of models learned across versions throughout. [inference]_
- claude: exists=unchecked applied=unchecked [no_basis] — Author-flagged inference, not a citation; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and as an inference, so both axes are left unchecked.

### c05 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 32)
_([OpenAI 2022](https://openai.com/index/chatgpt/)). [vendor]_
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL returned HTTP 403, so existence not confirmed from evidence; ChatGPT launched 30 Nov 2022 without cross-conversation memory is well established from general knowledge.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The only retrieved evidence is an HTTP 403, so existence cannot be verified from the lookup. From model knowledge, ChatGPT launched on 30 November 2022 and lacked persistent cross-chat memory, but the cited page's actual support for the memory part is not confirmed.

### c07 — exists ☐ · applied ✅  · ⚑ degraded  (line 37)
_([OpenAI 2023](https://openai.com/index/custom-instructions-for-chatgpt/)). [vendor]_
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL blocked (403), existence not confirmed from evidence; OpenAI launched custom instructions in beta for Plus users on 20 July 2023 per general knowledge.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved lookup was blocked with HTTP 403, so existence is unchecked under the provided evidence. From model knowledge, OpenAI announced custom instructions for ChatGPT on July 20, 2023 as a Plus beta applying across conversations.

### c08 — exists ☐ · applied ✅  · ⚑ degraded  (line 40)
_([OpenAI 2024](https://openai.com/index/memory-and-new-controls-for-chatgpt/)). [vendor]_
- claude: exists=unchecked applied=verified [model_knowledge_only] — URL returned 403; OpenAI began testing memory with a small share of users on 13 Feb 2024 is corroborated by general knowledge and the Decoder snippet (c09).
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The URL fetch returned HTTP 403, so the work's existence is unchecked from retrieved evidence. From model knowledge, OpenAI's February 13, 2024 memory announcement tested cross-chat memory with a small set of Free and Plus users and included user controls.

### c10 — exists ☐ · applied ✅  · ⚑ degraded  (line 48)
_([OpenAI 2024](https://openai.com/index/memory-and-new-controls-for-chatgpt/), update note; [TechCrunch 2025](https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/)). [vendor] [press]_
- claude: exists=unchecked applied=verified [evidence_text] — The OpenAI update note URL returned 403, but the companion TechCrunch source (c11) confirms the 10 April 2025 rollout drawing on past chats for Plus/Pro.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The OpenAI page fetch returned HTTP 403, so existence is unchecked from the retrieved evidence. From model knowledge, the April 10, 2025 update began rolling out expanded memory/reference to past chats for paid users, but this is not verified by retrieved text here.

### c11 — exists ✅ · applied ⚠️  (line 49)
_[TechCrunch 2025](https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/)). [vendor] [press]_
- claude: exists=verified applied=verified [evidence_text] — TechCrunch article dated April 10, 2025 confirms memory referencing past conversations rolling out first to Pro and Plus subscribers.
- gpt: exists=verified applied=nuance [evidence_text] — The TechCrunch URL resolves to the cited article dated April 10, 2025. The snippet supports rollout to Pro and Plus users and use of previous conversations, but it is less explicit on 'all past conversations as well as saved memories'.

### c12 — exists ✅ · applied ⚠️  (line 51)
_([Willison 2025](https://simonwillison.net/2025/Feb/24/claude-37-sonnet-and-claude-code/)). [press]_
- claude: exists=verified applied=verified [evidence_text] — Willison's 24 Feb 2025 post confirms Claude Code release; snippet mentions Claude Code but doesn't fully quote file/command/research-preview details, though these are well known.
- gpt: exists=verified applied=nuance [evidence_text] — The Simon Willison page resolves and is dated 24 February 2025 with the title 'Claude 3.7 Sonnet and Claude Code'. The provided snippet only partially supports the claim, since it does not show the details that Claude Code was a command-line research preview that reads/changes files and runs commands.

### c13 — exists ✅ · applied ⚠️  (line 54)
_([Anthropic 2025b](https://www.anthropic.com/engineering/claude-code-best-practices)). [vendor]_
- claude: exists=verified applied=verified [evidence_text] — Anthropic Claude Code best-practices page confirmed and references writing an effective CLAUDE.md, supporting the claim about CLAUDE.md files.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Claude Code documentation titled 'Best practices for Claude Code'. The snippet includes relevant headings such as 'Write an effective CLAUDE.md' and 'Store instructions and memories', but it does not fully display the asserted details about reading at session start and updating as work goes on.

### c15 — exists ☐ · applied ☐  (line 66)
_Before that, "it doesn't really learn" was close to true of the assistant in use, though never of in-conversation learning or of the line of models. [inference]_
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited author inference; no evidence to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and marked as an inference, so both axes are unchecked.

### c16 — exists ☐ · applied ☐  (line 69)
_**Gopnik's 2023 tests** used models tested without any memory, before memory shipped. [inference, from the dates above and Yiu, Kosoy & Gopnik 2023]_
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited inference referencing Yiu, Kosoy & Gopnik 2023; no evidence retrieved to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and marked as an inference, so both axes are unchecked.

### c17 — exists ☐ · applied ☐  (line 71)
_**Not all memory is equal.** A fact the user types is the "contacts app" case. Memory the system chooses to save is more, and notes an agent writes from its own work are the strongest case. [inference]_
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited author inference; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and marked as an inference, so both axes are unchecked.

## ✅ AGREE-clean (4)
### c04 — exists ✅ · applied ✅  (line 29)
_([Brown et al. 2020](https://arxiv.org/abs/2005.14165)). [paper]_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2005.14165 'Language Models are Few-Shot Learners' by Brown et al. confirmed; abstract directly supports GPT-3 few-shot/in-context learning without gradient updates.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Brown et al.'s 'Language Models are Few-Shot Learners'. The abstract explicitly says GPT-3 was tested few-shot with demonstrations specified in text and without gradient updates or fine-tuning.

### c06 — exists ✅ · applied ✅  (line 34)
_([Anthropic 2023](https://www.anthropic.com/news/100k-context-windows)). [vendor]_
- claude: exists=verified applied=verified [evidence_text] — Page resolves and text confirms May 11, 2023 expansion of Claude's context from 9K to 100K tokens (~75,000 words).
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to Anthropic's 'Introducing 100K context windows' page dated May 11, 2023. The snippet states Claude's context window expanded from 9K to 100K tokens, corresponding to around 75,000 words.

### c09 — exists ✅ · applied ✅  (line 43)
_([The Decoder 2024](https://the-decoder.com/openai-introduces-memory-feature-for-chatgpt-plus-users/)). [press]_
- claude: exists=verified applied=verified [evidence_text] — The Decoder article confirms memory enabled for all ChatGPT Plus users on 29 April 2024, not available in Europe and Korea.
- gpt: exists=verified applied=verified [evidence_text] — The Decoder page resolves and is titled 'OpenAI introduces "Memory" feature for ChatGPT Plus users'. The snippet says that on April 29, 2024 OpenAI enabled Memory for all ChatGPT Plus users and that it was not currently available in Europe and Korea.

### c14 — exists ✅ · applied ✅  (line 57)
_([Anthropic 2025c](https://www.anthropic.com/news/memory)). [vendor]_
- claude: exists=verified applied=verified [evidence_text] — Anthropic memory page confirms Sept 11, 2025 Team/Enterprise rollout and Oct 23, 2025 expansion to Pro/Max with project-scoped, viewable/editable memory.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic/Claude memory page resolves and is dated September 11, 2025. The snippet states the update expanding memory to Pro and Max on Oct. 23, 2025 and describes project-scoped memory plus user ability to view and edit what Claude remembers.
