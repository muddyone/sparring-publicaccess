# When AI assistants began to remember, and why it matters for whether they learn (as of 2026-10-18)

_Cite-checked 2026-10-18 ([report](../cite-check/2026-10-18-the-when-assistants-began-to-remember-brief.md)):
nothing refuted. The three OpenAI pages blocked retrieval (HTTP 403), so their claims were judged
from model knowledge, corroborated by press coverage; two claims were narrowed to what their
sources show._

_Research brief for position piece 02 (`positions/02-it-learns.md`) and the overview (piece 00).
Gathered 2026-10-18 from web search, reading vendor announcements and press coverage through
search summaries; not yet retrieved directly. Marks: **[vendor]** the company's own announcement;
**[press]** news coverage; **[paper]** a published paper; **[inference]** my reasoning from the
sources, not a finding._

## The question under test

Bart, 2026-10-18, after a read of piece 02: the piece never says clearly what "it" is. He means
an AI system as used, an assistant such as Claude or ChatGPT or a fuller agent setup like the
ones he builds, and he means such systems *since they began to keep memory*. When did that begin
in earnest, and was there a time these systems were far less able to learn?

## Bottom line

- **A model could always learn within one conversation,** from examples placed in it. What early
  assistants lacked was keeping anything once the conversation ended.
- **Keeping things arrived in steps, and in earnest in 2024–2025:** much longer conversations
  (2023), standing instructions (ChatGPT, July 2023), memory across conversations (ChatGPT 2024,
  extended to all past chats in April 2025; Claude September–October 2025), and AI agents that
  keep their own written notes (2025).
- **So yes: before memory, the AI assistant in use was a much weaker learner.** It could learn for
  an hour and keep none of it. The line of models learned across versions throughout. [inference]

## Timeline

1. **2020: learning within a conversation.** GPT-3 showed that a large model can do a new task
   from a few examples placed in its prompt, with no change to the model ("in-context learning")
   ([Brown et al. 2020](https://arxiv.org/abs/2005.14165)). [paper]
2. **30 November 2022: ChatGPT launches** ([OpenAI 2022](https://openai.com/index/chatgpt/)).
   [vendor] It had no memory between conversations; that feature arrived in 2024 (item 5).
   [inference]
3. **11 May 2023: much longer conversations.** Anthropic expanded Claude's context window from
   about 9,000 to 100,000 tokens, around 75,000 words
   ([Anthropic 2023](https://www.anthropic.com/news/100k-context-windows)). [vendor]
4. **20 July 2023: standing instructions.** OpenAI launched custom instructions for ChatGPT, a note
   the user writes once that applies to every conversation, first as a beta for Plus subscribers
   ([OpenAI 2023](https://openai.com/index/custom-instructions-for-chatgpt/)). [vendor]
5. **13 February 2024: ChatGPT memory.** OpenAI began testing memory with a small share of free and
   Plus users; ChatGPT could remember things across conversations, and users could view and delete
   what it kept ([OpenAI 2024](https://openai.com/index/memory-and-new-controls-for-chatgpt/)).
   [vendor] On 29 April 2024 it was enabled for all Plus users outside Europe and Korea
   ([The Decoder 2024](https://the-decoder.com/openai-introduces-memory-feature-for-chatgpt-plus-users/)).
   [press]
6. **10 April 2025: memory of all past chats.** ChatGPT's memory began to draw on all past
   conversations as well as saved memories, starting with Plus and Pro users
   ([OpenAI 2024](https://openai.com/index/memory-and-new-controls-for-chatgpt/), update note;
   [TechCrunch 2025](https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/)).
   [vendor] [press]
7. **2025: agents that keep their own notes.** Anthropic released Claude Code, a command-line
   agent that reads and changes files and runs commands, as a research preview on 24 February 2025
   ([Willison 2025](https://simonwillison.net/2025/Feb/24/claude-37-sonnet-and-claude-code/)).
   [press] Anthropic's guidance for it describes CLAUDE.md files for storing instructions and
   memories that carry from one session to the next
   ([Anthropic 2025b](https://www.anthropic.com/engineering/claude-code-best-practices)). [vendor]
8. **Earlier, in research: agents with written memory.** Reflexion (2023) had language-model agents
   write reflections on feedback into an episodic memory and use them to do better on later
   attempts ([Shinn et al. 2023](https://arxiv.org/abs/2303.11366)). [paper] So written memory
   for AI agents predates the consumer features; what 2024–2025 changed is that it became a
   standard part of tools in everyday use. [inference]
9. **September–October 2025: Claude memory.** Anthropic rolled out memory to Team and Enterprise
   users in September 2025 and expanded it to Pro and Max on 23 October 2025, scoped by project and
   viewable and editable by the user ([Anthropic 2025c](https://www.anthropic.com/news/memory)).
   [vendor]

## Bearing on piece 02

- **Name the unit early.** "It" is the AI system in use, assistant or agent setup, not the bare
  model. The piece already argues this in "Which thing learns"; it should say it up front.
- **Date the claim.** The piece's claims are about systems that keep memory, which arrived in
  earnest in everyday tools in 2024–2025 (research agents had it earlier, item 8). Before that,
  the assistant in use learned within a conversation but kept nothing, so on a definition that
  asks for a lasting change, "it doesn't really learn" was close to true of it, though never of
  the line of models. [inference]
- **Gopnik's 2023 tests** ran before memory shipped, but they were single questions where memory
  of past conversations would not come into it, so the dates do not explain her results.
  [inference; raised by the 2026-10-18 panel]
- **Not all memory is equal.** A fact the user types is the "contacts app" case. Memory the system
  chooses to save is more, and notes an agent writes from its own work are the strongest case.
  [inference]

## Gaps and cautions

- **Sources were read through search summaries,** not retrieved directly; the cite-check retrieves
  them.
- **The OpenAI pages could not be retrieved by the checker** (403); their dates are corroborated
  by press coverage (The Decoder, TechCrunch) and both checking models' knowledge.
- **Claude Code's launch date comes from press coverage**; Anthropic's own launch post was not
  found in the search.
- **When CLAUDE.md files first appeared** in Claude Code is not established here; the cited
  guidance shows they existed by the time it was published.
- **Other companies' assistants** (Google's Gemini, Microsoft's Copilot) are not covered.
