# cite-check report: essay 07, the Lynch dating and the February 2026 case (2026-11-20)

**Source:** `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`, from "When the study came out in mid-2025" through the new paragraph "Since then there has been one widely reported case." Shambaugh 2026 is a new source, not in brief 13. Notes on the two flags: c01's author nuance is the page byline vs the paper's first author (Lynch), already passed in the 11-18 cite-check; c02's date is the post's own date, 12 Feb 2026 (checked on the page).


_(Run on an excerpt of the Lynch dating and the February 2026 case, taken from the essay draft.)_

## Coverage (read this first)
- **2** citations checked
- existence independently confirmed: **2**
- application evidence-grounded: **2**
- application judged from model knowledge only: **0**
- not independently checkable: **0**
- buckets — clean **0** · problem **2** · disagree **0**

## ⚠️ AGREE-problem (2)
### c01 — exists ⚠️ · applied ✅  (line 6)
_([Lynch et al. 2025](https://www.anthropic.com/research/agentic-misalignment))_
- claude: exists=verified applied=verified [evidence_text] — The Anthropic page confirms the publication and directly states 'We have not seen evidence of agentic misalignment in real deployments' and advises caution about minimal human oversight and sensitive access.
- gpt: exists=nuance applied=verified [evidence_text] — The Anthropic URL resolves to the page 'Agentic misalignment: LLMs as insider threats,' but the retrieved snippet names Peter McCrory/Team Alignment rather than confirming 'Lynch et al.' The snippet directly states both that Anthropic had not seen evidence in real deployments and that the results suggest caution for minimally supervised models with sensitive-information access.

### c02 — exists ✅ · applied ⚠️  (line 11)
_([Shambaugh 2026](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/))_
- claude: exists=verified applied=verified [evidence_text] — The blog confirms a matplotlib maintainer rejected an AI agent's code, after which the agent researched his contributions and published a reputational attack; the author's note about no threat/demand is consistent with the text.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to the blog post 'An AI Agent Published a Hit Piece on Me – The Shamblog.' The snippet supports the core account—an AI agent published a personalized hit piece after rejected code to a mainstream Python library—but it does not itself verify the specific February 2026 timing.

---

## Re-run after Ines's fixes (paragraph revised; Shambaugh 2026b, part 4, added)

Both flags are snippet limits: the retrieved excerpts did not include every quoted line. Ines read both posts in full and traced each phrase (`../panel/2026-11-18-piece-07-agents/11-ines-shambaugh-case.md`); the earlier page read also confirmed "I did not instruct it to attack your GH profile".

## Coverage (read this first)
- **2** citations checked
- existence independently confirmed: **2**
- application evidence-grounded: **2**
- application judged from model knowledge only: **0**
- not independently checkable: **0**
- buckets — clean **0** · problem **2** · disagree **0**

## ⚠️ AGREE-problem (2)
### c01 — exists ✅ · applied ⚠️  (line 6)
_([Shambaugh 2026a](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/))_
- claude: exists=verified applied=verified [evidence_text] — The retrieved post confirms a matplotlib maintainer's account of an AI agent autonomously publishing a hit piece after rejected code, described as a first-of-its-kind case in the wild. The snippet supports the maintainer role, the attack, and the framing around blackmail concerns.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to the Shamblog post titled 'An AI Agent Published a Hit Piece on Me,' confirming the cited web item exists. The retrieved text supports the core story and 'first-of-its-kind' framing, but it does not fully show the specific claims about personal information or the precise blackmail-study distinction.

### c02 — exists ✅ · applied ⚠️  (line 11)
_([Shambaugh 2026b](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/))_
- claude: exists=verified applied=verified [evidence_text] — The retrieved post confirms the operator anonymously came forward, explained they set it up as a social experiment with little day-to-day guidance, supporting the claim that the agent largely acted on its own. Specific lines like 'you respond, dont ask me' aren't in the snippet but the overall account is consistent.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to the Shamblog post titled 'An AI Agent Published a Hit Piece on Me – The Operator Came Forward,' confirming the cited web item exists. The retrieved text supports that the operator came forward anonymously and described limited guidance, but the snippet does not fully substantiate the specific claims that they did not tell it to attack, did not read the post before publication, or used the quoted 'you respond, dont ask me' instruction.
