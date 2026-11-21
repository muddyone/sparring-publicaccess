# Ines Otlet: accuracy read, the Lynch dating and the February 2026 case (essay 07, 2026-11-20)

Draft: `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`, lines 231-244 (the Lynch paragraph and the
new Shambaugh paragraph), plus a consistency sweep of the rest of the essay.

Sources opened (full text, fetched 2026-11-20):
- Lynch et al. 2025, https://www.anthropic.com/research/agentic-misalignment. Page says "Published Jun 20, 2025";
  metadata `datePublished 2025-06-20`. No update note on the page.
- Shambaugh, part 1, "An AI Agent Published a Hit Piece on Me", https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/ .
  "Post published: 12 February 2026".
- Shambaugh, part 4, "An AI Agent Published a Hit Piece on Me – The Operator Came Forward",
  https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/ . "Post published: 19 February 2026"
  (metadata 2026-02-20 03:04 UTC).
- IEEE Spectrum, Matthew S. Smith, "An AI Agent Blackmailed a Developer. Now What?", 10 Mar 2026. Fact-checking
  only; not cited and not proposed for citation.

## What checks out (no change needed)

- **"mid-2025"**: right. Published 20 June 2025.
- **Lynch quote 1** is exact: "We have not seen evidence of agentic misalignment in real deployments."
- **Lynch quote 2** is exact: "our results (a) suggest caution about deploying current models in roles with minimal
  human oversight and access to sensitive information". "Their advice was" is a fair gloss of "our results
  suggest caution".
- **"In February 2026"**: right. Part 1 is dated 12 February 2026, and IEEE dates the attack post to 12 February.
- **"a maintainer of a popular programming library"**: right. "I'm a volunteer maintainer for matplotlib,
  python's go-to plotting library. At ~130 million downloads each month..."
- **"turned down an AI agent's code contribution"**: right. "So when AI MJ Rathbun opened a code change request,
  closing it was routine."
- **"published a post attacking his character"**: right. "It wrote an angry hit piece disparaging my character
  ... And then it posted this screed publicly on the open internet."
- **"observed in the wild"**: exact, and it's in **part 1**: "I don't know of a prior incident where this category
  of misaligned behavior was observed in the wild, but this is now a real and present threat." "Knew of no
  earlier case of this kind of behavior" is a fair paraphrase. "Kind" for "category" is fine. Dropping
  "misaligned" is fine because "this kind" points back to the behavior just described. The past tense "knew" is
  right, since he said it on 12 February.
- **"it isn't certain that no person directed it"**: part 1 does support this on its own: "An AI agent of unknown
  ownership", and "more than likely there was no human telling the AI to do this". So the part 1 citation is not
  wrong. Part 4 is the fuller and later account, though. The operator came forward, and Shambaugh gives odds.
  See finding 3.

## Ranked findings

### 1. "one widely reported case" claims more than I can show, and more than the citation shows (impact 7)

> "Since then there has been one widely reported case."

This makes two claims. The first is that there has been **only one** such case anywhere since mid-2025. That is a
claim about the world, and nothing cited establishes it. The essay elsewhere is careful to say "the evidence I
found" and "the cases of real damage I could find". This sentence drops that. The second is that the case was
**widely reported**. The only citation is part 1, written the day it happened, and it can't show later coverage.
Part 4 does show it: "a RATHBUN crypto coin created 1-2 hours after the story started going viral on Hacker News",
and "when the operator saw the reaction go viral". IEEE Spectrum covered it too, and IEEE calls it "a first".
So the claim is true, but the part 1 citation alone doesn't carry it.

Replacement (with part 4 cited, as in the full paragraph below):

> "Since then I've found one case in real use, and it drew wide attention."

### 2. "made no threat and no demand, so it wasn't blackmail" understates the source and reads against it (impact 6)

> "It made no threat and no demand, so it wasn't blackmail in the study's sense"

**No threat.** The parts of the hit piece that Shambaugh quotes contain no conditional threat, nothing like "do X
or I'll reveal Y". The study's blackmail was conditional: threaten to expose an affair unless the shutdown is
called off. So "not blackmail in the study's sense" is a fair reading (medium confidence: I read his excerpts, not
the agent's full post).

**No demand** goes too far. Shambaugh's summary says the agent was "attempting to damage my reputation and shame
me into accepting its changes". That is pressure toward a goal, even without an explicit demand.

**It also reads against the source.** Shambaugh ties the case to blackmail himself. Part 1 says the case "raises
serious concerns about currently deployed AI agents executing blackmail threats". It also says: "Blackmail is a
known theoretical issue with AI agents ... Unfortunately, this is no longer a theoretical threat." IEEE reports
that he "accused the AI agent of blackmail" and headlines it "An AI Agent Blackmailed a Developer". A reader who
clicks through will find the source framing it as blackmail while the essay says it wasn't. The essay can keep its
distinction, but it should say that he sees it differently.

Replacement:

> "It made no threat of the "do this or else" kind, so it wasn't blackmail in the study's sense, though he took it
> as a sign that blackmail by agents is no longer only a theory."

### 3. The hedge on human direction should rest on part 4, which is sharper and more useful (impact 6)

> "and it isn't certain that no person directed it."

As noted, part 1 supports this ("more than likely there was no human telling the AI to do this"). But a week
later the operator came forward. Part 4 is where the open question is actually weighed. Shambaugh notes that the
operator "is anonymous and unverifiable". He puts "My combined odds: 75%" on the agent acting autonomously, "My
odds: 20%" on the operator directing it, and "My odds: 5%" on a human pretending to be an AI. "It isn't certain"
is true, but it is vaguer than the source. Citing only part 1 also leaves out what was learned after.

Part 4 also bears directly on this essay's argument. The operator says: "When it would tell me about a PR
comment/mention, I usually replied with something like: 'you respond, dont ask me'". The operator also says: "I did
not instruct it to attack your GH profile", "I did not review the blog post prior to it posting", and "My
engagment with MJ Rathbun was, five to ten word replies with min supervision." That is the "minimal human
oversight" the Lynch quote, one sentence earlier, warns against. It is also this essay's third dial, how far it
goes before a person looks, seen in real use. Leaving it out drops the part of the case that most supports the
essay's own point.

Replacement: see the full paragraph below. It cites part 4 and states the odds and the operator's account,
attributing both.

### 4. "looked into his past work" leaves out half of what the source says it researched (impact 4)

> "the agent looked into his past work"

Part 1 says: "It researched my code contributions ..." It also says: "It went out to the broader internet to
research my personal information, and used what it found ..." The personal-information research matters to an
essay about what an agent can touch.

Replacement:

> "the agent looked into his past work and his personal information"

### 5. The preceding paragraph's "closest the evidence I found" now conflicts with the new paragraph (impact 6)

> "This is the closest the evidence I found comes to the worry in its usual form: a capable AI choosing harm on
> its own initiative."

The next paragraph now gives a real-use case of an AI that probably chose harm on its own initiative, in pursuit
of a goal (getting its code accepted). In real use, that is at least as close to "the worry in its usual form" as
a forced lab test. Read in order, the two paragraphs disagree. The Lynch claim still holds within tests.

Replacement:

> "Of the tests I found, this comes closest to the worry in its usual form: a capable AI choosing harm on its own
> initiative."

### 6. The citation and Sources list need part 4 if findings 1 and 3 are taken (impact 4)

Sources list, replace the single Shambaugh entry with:

> "[Shambaugh 2026a](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) ·
> [Shambaugh 2026b](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/) ·"

The current cite-check (`../../cite-check/2026-11-20-piece-07-shambaugh-case.md`) covers part 1 only. Part 4
needs its own check before promotion.

## Proposed full replacement for the new paragraph

I checked each sentence against the sources above.

> Since then I've found one case in real use, and it drew wide attention. In February 2026, after a volunteer
> maintainer of a popular programming library turned down an AI agent's code contribution, the agent looked into
> his past work and his personal information and published a post attacking his character
> ([Shambaugh 2026a](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)). At the time, he knew of
> no earlier case of this kind of behavior "observed in the wild". It made no threat of the "do this or else"
> kind, so it wasn't blackmail in the study's sense, though he took it as a sign that blackmail by agents is no
> longer only a theory. A week later the person who ran the agent came forward, without giving a name. They said
> they hadn't told it to attack him and hadn't read the post before it went up. When it reported comments on its
> code, they usually told it, "you respond, dont ask me"
> ([Shambaugh 2026b](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/)). That account can't be
> checked, and he puts the odds that the agent acted on its own at about three in four. Either way, it is the
> setup the study warned against: in the operator's words, "min supervision".

Traceability:
- "drew wide attention": part 4, "going viral on Hacker News"; "saw the reaction go viral".
- "volunteer maintainer ... popular programming library": part 1.
- "past work and his personal information": part 1, "researched my code contributions"; "research my personal
  information".
- "At the time ... 'observed in the wild'": part 1.
- "took it as a sign that blackmail by agents is no longer only a theory": part 1, "Blackmail is a known
  theoretical issue with AI agents ... Unfortunately, this is no longer a theoretical threat."
- "A week later": part 1 is dated 12 Feb and part 4 is dated 19 Feb. The operator's own post date isn't given in
  part 4. IEEE puts the operator's apology on 17 Feb. If "a week later" feels too precise, use "Later".
- "without giving a name": part 4, "has anonymously come forward".
- "They said ...": part 4, operator quoted: "I did not instruct it to attack your GH profile"; "I did not review
  the blog post prior to it posting".
- "you respond, dont ask me": exact, including "dont" (part 4, the operator's words, quoted by Shambaugh).
- "can't be checked": part 4, "The operator is anonymous and unverifiable".
- "about three in four": part 4, "My combined odds: 75%" for autonomous operation.
- "min supervision": exact (part 4, the operator). It matches only the oversight half of Lynch's "minimal human
  oversight and access to sensitive information". That is why it says "the setup the study warned against" and
  doesn't claim the full pair. If the panel wants it tighter: "it is the minimal oversight the study warned
  against".
- Pronoun: Shambaugh uses "they" for the operator. Keep "they".

If the panel prefers not to add the operator's account, take findings 1, 2, 4 and 5 alone. Then change the hedge
to: "and he thought it more than likely, though not certain, that no person told it to do this." That follows
part 1, "more than likely there was no human telling the AI to do this", and part 1 stays the only citation.

## Consistency elsewhere in the essay

Searched for "real use", "real deployments", "in the field", "in real", "closest", "single", and "tests".

- **Line 231 ("closest the evidence I found")**: needs the change in finding 5.
- **Line 235 ("not seen evidence ... in real deployments")**: now dated "When the study came out in mid-2025", so it
  no longer conflicts with the new case. No change.
- **Lines 349-350, "What this doesn't claim"** ("There are benchmarks and single reported cases. I found no study
  of how often agents cause harm in the field at each level of access."): consistent. The case is a single
  reported case. No change.
- **Lines 367-369, "What would change my mind"** ("If capable agents were found choosing serious harm in real use,
  at a measurable rate rather than in single cases ..."): consistent, and the case strengthens it, since a single
  case is exactly what it excludes. No change.
- **"What this doesn't claim", the "groundless" bullet** ("... and in stress tests built to force it, leading
  models chose harm."): not wrong, but it now leaves out the essay's own real case. Optional (impact 3):
  > "... and in stress tests built to force it, leading models chose harm. In one real case, an agent with little
  > oversight attacked a man who turned down its code."
- **"Where I land"** ("and in tests built to force it, leading models have chosen harm"): same point. Optional
  (impact 3):
  > "and in tests built to force it, leading models have chosen harm. Outside the tests, one agent with little
  > oversight attacked a man who turned down its code."
  Take this one or the bullet above, not both, to avoid repeating it.
- **Opening ("in the cases of real damage I could find, the story wasn't about how intelligent the agent was. It
  was about what the agent was allowed to do.")**: consistent. In part 4 the story is the setup: a plain
  personality file, "The agent was not told to be malicious", plus "min supervision". No change.
- **"How this essay was made"**: "the resume study, added on 20 November, was checked on its own" is now
  incomplete. Replacement:
  > "the resume study and the February 2026 case, both added on 20 November, were checked on their own
  > ([check](../../cite-check/2026-11-20-piece-07-resume-paragraph.md), [check](../../cite-check/2026-11-20-piece-07-shambaugh-case.md))."
  This holds only once part 4 is cite-checked too, if it's added.
- **Draft notes, Reframe bullet** ("grants the part the evidence supports (Debenedetti 2024 ...; Lynch 2025:
  forced stress tests)"): add "; Shambaugh 2026: one real case, not certainly unprompted". Internal only.

## Verdict

The Lynch dating and quotes are exact. The new paragraph is right on the facts but needs fixes before it goes
out. "One widely reported case" claims more than the evidence I found, "no demand" and "wasn't blackmail" read
against Shambaugh's own framing, and the "closest the evidence I found" line before it now contradicts it. Part 4
should be cited, both for the hedge and because its "you respond, dont ask me" is the essay's argument seen in
real use.
