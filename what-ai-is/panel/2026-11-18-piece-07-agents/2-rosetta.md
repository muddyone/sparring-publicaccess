# Rosetta: plain-language review, essay 07 (first panel read), 2026-11-18

Reviewer: Rosetta (communications / plain language). Reader held throughout: an everyday AI user who
keeps hearing that "agents" will soon book, email, code and pay for them, and who will act on the
six-step list and on one rule.

What I read: the brief (`brief.md` in this folder); the draft (`drafts/2026-11-18-07-agents.md`, body
only, Draft notes only where the brief points); `positions/03-someone-there.md` in full for flag 2, and
`positions/02-it-learns.md` for the car image; brief 13 (only to keep every rewrite inside what it says a
source says, lines named where it mattered); my persona and memory (the entries that bore on this: the
whole-artifact pass in my charter, the 2026-10-28 "hear it through the narration builder" lesson, and the
essay 06 lesson that a rule the reader acts on must have one name). I ran
`newsletter-what-ai-is/narration/build-scripts.py`'s `speakable()` on the draft; quotes marked
**aloud** are its output. No new source is proposed anywhere below.

Each finding: impact (1-10), the passage, the reader's problem, the fix. The drafter rewrites every adopted
fix; my wording is a target, not copy. The cap limits packaging, never the message: nothing below cuts a
concept, and every additive fix says what it buys the reader.

---

## Findings, ranked

### 1. The correction of essay 03 misquotes essay 03, and calls our own work muddled (impact 9; flag 2)

> "Here I have to clear up something this series itself muddied. In essay 03 I said there really is an
> agent on the other end of the conversation."

Essay 03 never says that. Its position says "there really is **something** on the other end"
(`positions/03-someone-there.md`, line 7), and its word for what is there is a "quasi-subject". The only
place essay 03 uses "agent" about the assistant is the opposite of this claim: Chalmers's list of what
would raise the odds of consciousness includes "a unified agent", and essay 03 reports him calling the
lack of one "maybe the deepest" obstacle (lines 105-108). So a reader who goes back to essay 03 to check
will find the series saying the reverse of what essay 07 says it said. (The wording comes from brief 13,
lines 67, 337 and 408, which put "agent" in essay 03's mouth; the brief is where the error started.)

"Muddied" then confesses to a muddle that didn't happen. That breaks the register target in the
self-deprecating direction, about a published essay.

The *need* the section answers is real and brief 13 states it well (line 411): a reader fresh from essay
03 will hear "agent" as "the someone from essay 03, now with tools". So keep the section, and change what
it says essay 03 did.

Fix: say what essay 03 said, and that this essay uses a nearby word in another sense. Target:

> "Essay 03 said there really is something on the other end of the conversation: something you can
> accurately describe as having beliefs and aims, rich enough to argue with. Philosophers call that
> kind of thing an agent. The industry uses the same word for something else, and this essay is about
> the industry's kind."

Then the Chalmers "engine… to drive many agents" line follows naturally, and "On that view even a chat
assistant that can't touch anything is an agent" can stay. Drop "muddied" and "clear up".

### 2. The one rule the reader acts on has four names, and they don't mean the same thing (impact 8; flag 8)

> Title: "What you let it do is what counts."
> Position: "not 'how smart is it?' but 'what am I letting it do?'"
> Step 1: "Ask what it can touch, not how smart it is."
> Landing: "It's 'what did we let it do, and who was looking?'"

The brief names the rule the reader carries away: "ask what it can touch, not how smart it is". It
appears in that form once, at step 1. Everywhere else the reader meets a different wording, and they are
not synonyms: "touch" is access only, "let it do" is access plus how far it goes alone, and the landing
adds a third thing, "who was looking". A reader taking one rule home has to decide which of four it is.

Fix: one wording wherever the reader is told what to ask. Use the brief's, "ask what it can touch, not
how smart it is", in the position's last sentence, step 1 and the landing. The second dial already has
its own step (3) and its own section, so the rule doesn't need to carry it; the landing can say "and
then, how far it goes before anyone looks" as a second, separate question. Title: see flag 8 below.

### 3. "The limit on the harm", reached "for good or ill", doesn't parse; and the limit is set by one thing in one place, two in another (impact 7)

> Position: "What it's allowed to touch, and how far it goes before anyone looks, set the limit on the
> harm it can do. How capable it is decides how much of that limit it reaches, for good or ill."
> Line 158: "What an agent is allowed to touch sets the **ceiling** on the harm it can do."
> Line 237: "It decides how much of the limit an agent reaches, in both directions."

Read literally: if the limit is a limit on *harm*, an agent can't reach more of it "for good". The reader
has to stop and repair the image. Then the key sentence at line 158 drops the second dial (how far it
goes before anyone looks) that the position put into the same sentence, and calls the limit a
"ceiling", a word used once. Three small differences in the sentence the whole essay rests on.

Fix: make the limit a limit on *what it can do*, with harm inside it, and use one word ("limit")
throughout. Target for the position, repeated in the same shape at line 158:

> "What it's allowed to touch, and how far it goes before anyone looks, set the limit on what it can
> do, harm included. How capable it is decides how much of that it actually does, good and bad."

If the drafter wants line 158 to be about access only (the evidence in that section is about access),
say so: "Of the two dials, what it can touch is the one the security research is about."

### 4. "Your assistant" means a person in one sentence and an AI everywhere else (impact 7)

> "A sentence hidden in an email won't usually turn your assistant against you; it can turn an agent."

The essay uses "assistant" for the AI from its opening ("an AI assistant you work with turn by turn",
line 24) to its landing ("An AI agent isn't a smarter assistant. It's an assistant you've let act for
you"). Here, two paragraphs after "an assistant with your email password", it means a human employee.
A reader who has spent 2,500 words with "assistant" = ChatGPT reads this sentence as "a hidden sentence
won't turn ChatGPT against you", which is the opposite of the essay's prompt-injection section.

Fix: "won't usually turn a human assistant against you; it can turn an agent." Same in line 188 if the
drafter wants it fully safe: "a human assistant with your email password".

### 5. Step 4's advice points two opposite ways (impact 6; the reader acts on this)

> "If you find yourself clicking 'allow' without reading, that's a sign it's asking about too much, or
> should be allowed less."

"Asking about too much" suggests letting it ask less (give it more room); "should be allowed less"
suggests giving it less room. The reader can't tell which to do, and these are the instructions they act
on.

Fix: say what each half means, so it is one instruction with two parts. Target: "that's a sign the
setup is wrong: let it do the harmless things without asking, and take away the risky ones it keeps
asking about." (Our advice, not a source's claim; the essay already says it found no study of approval
prompts, line 178.)

### 6. Step 2 and step 3 each have a phrase the reader can't act on as written (impact 6)

> Step 2: "If it can see your private data, read things from outside, and send messages out… Remove one
> of the three."
> Step 3: "More steps alone is fine for work you can undo."

"Read things from outside": outside of what? Willison's words are "exposure to untrusted content"; the
plain meaning is text anyone could have written. And "Remove one of the three" gives no picture of how.

"More steps alone" first parses as "only more steps", then as "more steps on its own".

Fix, step 2: "read things anyone could have written (web pages, incoming email)… Remove one of the three:
for example, an agent that reads your inbox shouldn't also be able to send email." (Adds one example; the
example is ours, and it applies the test as Willison states it, brief 13 §5.3.)
Fix, step 3: "Letting it take many steps on its own is fine for work you can undo."

### 7. The prompt-injection quote is security jargon, and the label comes before the plain idea (impact 6)

> "The main problem is called *prompt injection*. … text an agent retrieves can 'act as arbitrary code
> execution' and 'control how and if other APIs are called', meaning other tools and services"

"Arbitrary code execution" is a term of art the reader can't weigh; "meaning other tools and services"
glosses only "APIs". The label "prompt injection" comes first and its meaning second (my plain-language-
first rule; mild, because the meaning follows at once).

Fix: plain idea first, label after, and carry the quote's meaning in words: "An agent reads things as it
works… Any of that text can carry instructions, and the agent may follow them. Security people call this
*prompt injection*. Researchers showed early on that text an agent reads can work like a command typed
into it, deciding whether and how it uses its other tools." Keep the Greshake quote only if the drafter
glosses "arbitrary code execution" in the same sentence.

### 8. The NIST sentence switches subject without saying so, and "11 tries in 100" counts the wrong thing (impact 6)

> "And when US government testers built stronger attacks against one leading model, their success rate
> rose from 11 tries in 100 to 81."

The section is "A smarter model isn't a safer one", and the two sentences before it are about whether
better *models* resist. This one is about better *attacks*. "And" tells the reader it is more of the
same, so they look for the capability link and don't find it. "11 tries in 100" also reads as a count of
tries; the source counts attacks that worked (brief 13 line 557: "from 11% … to 81%").

Fix: signal the switch and say what it means for the reader: "The attacks are getting better, too. When
US government testers built stronger ones against one leading model, the share that worked rose from 11
in every 100 to 81. A defence that looks fine today has been tested against yesterday's attacks." (The
last sentence restates what the NIST page is about, strengthening evaluations; if Vera thinks it goes
further than brief 13 supports, drop it and keep the first two.)

### 9. The Lynch paragraph carries three ideas, and the blackmail example arrives without its link (impact 6)

> "That doesn't make capability irrelevant. It cuts both ways… In stress tests that its authors
> deliberately set up to leave no other way out, leading models… sometimes chose harmful actions, such as
> blackmail… And what an agent can get done on its own keeps growing. One measure of the length of task
> agents can complete has been doubling about every seven months"

Idea one: a capable agent does more of the good and the bad job. Idea two: capable models can *choose*
harm, not only be fooled. Idea three: their reach keeps growing. The reader gets idea two straight after
idea one with no bridge, and "agentic misalignment" in the quote is a research term. Then "the length of
task" has no unit the reader knows: length in what?

Fix: split into two paragraphs. Open the Lynch sentence with its link: "Capable models can also choose
badly, not just be fooled." Carry "agentic misalignment" as "they have not seen this happen in real use".
For Kwa, give the scale brief 13 has (§2.8): "the length of software task agents can finish about half
the time, around 50 minutes of work in early 2025, has been doubling about every seven months." That also
restores "software", which the draft drops; the brief says the measure is software tasks only.

### 10. The developer's "you" reads as the reader (impact 5)

> "the model remembers nothing from one request to the next: 'you always send the full conversational
> history'"

The "you" in Anthropic's docs is a developer. The reader has never sent a conversation history and will
wonder when they did. Fix: "a developer has to 'always send the full conversational history'".

### 11. "A fivefold increase in the computing power" is a scale the reader doesn't have (impact 5; flag 3)

> "most were worth more than a fivefold increase in the computing power spent training the model"

The reader has no feel for training compute. They don't act on this number; it is a reason to believe
that setups matter a lot. So say what it means and keep the claim.

Fix: "most were worth as much as training the model with more than five times the computing power,
without retraining it at all." (Brief 13 §2.5: "significantly improved without expensive retraining";
"more than a 5x increase in training compute".)

### 12. "There's no neutral setup in which to measure 'the model itself'" is a researcher's sentence (impact 4; flag 3)

Fix: say the consequence for the reader: "So a score for a model in one setup doesn't tell you how it will
do in another: in one large comparison across nine models, which setup worked best depended on which model
was in it." (Brief 13 §2.6's "bearing".)

### 13. "It made the agent safe" is stronger than "stopped the attacks they tested" (impact 5; honest claim)

> "It stopped the attacks they tested 'even when underlying models are susceptible'… It made the agent
> safe without making the model any harder to fool."

"Safe" is absolute; the sentence before is about the attacks tested. Also "susceptible" is plain enough
but the 77-vs-84 cost has no felt meaning.

Fix: "It protected the agent without making the model any harder to fool", and give the cost in words:
"at a price: about 7 fewer tasks done in every 100."

### 14. "Zou: limited correlation between agent robustness and … inference-time compute" (impact 5)

Three research words in one quote ("correlation", "robustness", "inference-time compute"). Fix: carry it
in words, quote less: "found that bigger or more capable models, or ones given more time to think, were
not much harder to hijack." (The abstract's "limited correlation", brief 13 §6.2; "not much harder" keeps
"limited", it doesn't say "no".)

### 15. "Today" will be wrong on Friday (impact 4)

> "Today one of them fixed broken links on a page of mine"

The fix was 2026-11-18; the edition goes out 2026-11-20. Fix: "This week". (The Draft notes already flag
that the held push may resolve before publication; that's the drafter's to watch.)

### 16. "Part one's advice: calibrate trust to the job, as it's actually done" sends the reader off-page (impact 4)

A new subscriber hasn't read Part one, and "calibrate" is a register word. Fix: say the advice itself:
"That's the advice Part one kept returning to: trust it as far as its record in that job has earned, and
no further."

### 17. Aloud: two citations are read out, one garbled (impact 4)

**aloud:** "…subject to the principal's control" (the Restatement of Agency, as quoted in Kolt 2025)"
**aloud:** "…whoever they are (Jensen & Meckling 197690026-X))"

The Jensen & Meckling DOI contains parentheses, so the narration builder's link pattern stops early and
the listener hears "nineteen seventy-six ninety thousand twenty-six X". The Restatement parenthesis is
prose, so it is kept and read mid-sentence.

Fix: for Jensen & Meckling, escape or encode the parentheses in the URL (`%28` / `%29`) so the link is one
unit; for the Restatement, move the attribution into the sentence ("…as the standard legal reference
puts it, quoted by Kolt") or accept it being read. Also note that the six steps lose their numbers aloud
and run together ("…don't let it write. Run Willison's test."); the builder does the same to every essay,
so this is a builder issue, not this draft's.

### 18. In the position, "In the working sense" presupposes a sense the reader hasn't met (impact 3)

> "In the working sense, an 'agent' is an AI you've let act for you."

The other sense arrives forty lines later. Fix: "In everyday use" in the position, and let "working sense"
be introduced in the "Two meanings" section, where it is defined.

---

## Whole-artifact pass (read last, cold, start to finish, as the reader)

1. **Kinds of number the reader must hold: three, and well handled.** Almost every figure is on one scale,
   "x out of 100" (11 vs 18, 77 vs 84, 11 to 81). That consistency is a real strength and worth keeping.
   The others are counts (nine models, 22 agents, 1.8 million attempts, 41 policies), which need no
   re-orientation, and two odd ones out: "fivefold … computing power" (finding 11) and "doubling about every
   seven months" with no unit (finding 9). Neither is acted on; both should carry their meaning in words.
2. **Off-page sends:** essay 02 (car and engine, restated, fine), essay 03 (finding 1: restated wrongly),
   "Part one kept asking" (restated at once, fine), "Part one's advice" (finding 16), "the last essay in
   this part" (fine, a forward pointer).
3. **Research terms near-meaningless to this reader:** harness (introduced and then replaced by "setup",
   good), prompt injection, arbitrary code execution, APIs, robustness, inference-time compute, agentic
   misalignment, uninterpretable, least set of privileges. All but the last two are addressed above;
   "uninterpretable" and "least set of privileges" sit inside quotes that the surrounding sentence already
   explains, and can stay.

The spine is easy to follow. The reader comes away knowing what an agent is in this essay, why access
matters more than cleverness, and what to do. What they can't do as written is carry one rule home with
one name (findings 2, 3).

## Counts

Body (title to "Where I land", via `speakable()`): 193 sentences, about 2,910 words.

- **Under eight words:** 48 of 193, 25%. Below the 30% target, but flow outranks the ratio and the essay's
  flow is good: paragraphs open from where the last ended, and the short sentences land deliberately ("The
  report said 'done'. The work wasn't there."). Don't chop to reach 30%.
- **30 words or more:** 17. The longest are 46 words: the "By 'it' I mean" paragraph's first sentence and
  the Saltzer & Schroeder sentence. Both read aloud cleanly enough; the Saltzer one would be easier split
  before "because".
- **Explainer connectives:** "Put plainly" (1), "meaning" (2), "That's why" (1), "So here's how I'd put
  it" (1), "Notice what kind of warning that is" (1), plus nine uses of "So" opening a consequence. The
  three-connective target is met.

## Verdicts on my flags

**Flag 2, "Two meanings of 'agent'": the need is right, the placement is right, the correction is not
fair to essay 03.** It says essay 03 said something it didn't, and calls the series muddled for it. Keep
the section where it is (before the first section that relies on the working sense), restate essay 03
accurately ("something on the other end", a quasi-subject), and drop "muddied" (finding 1). Also change
"In the working sense" in the position (finding 18) so the reader isn't handed the term before the
section that explains it.

**Flag 3, the harness numbers: two of three usable as written.** "11 out of 100 … 18 out of 100, an
improvement of more than half" is exactly right for this reader. "Nine models" is fine as a count, but
the sentence around it needs its consequence in plain words (finding 12). "Fivefold increase in the
computing power" is not usable; say what it is worth (finding 11).

**Flag 5, the incident list: fair to the companies, and hedged about right.** The database case names no
company in the text, quotes its chief executive taking it seriously, and says "reportedly"; the GitHub
case quotes the researchers saying it is "not a flaw in the… server code itself". "These are single
reported cases, not rates" is the right hedge in the right place. One small tighten: "In each case the
agent held access the job didn't need" states as fact what the first case only reports; "In both cases,
as reported, …" costs three words.

**Flag 8, the title: keep the first sentence; align the second with the rule.** "A smarter AI isn't a
safer one" is short, true to the evidence (it says "isn't safer", not "is less safe"), and in the series
pattern. "What you let it do is what counts" is a fifth wording of the rule (finding 2). If the rule is
"ask what it can touch", the title could be "A smarter AI isn't a safer one. Ask what it can touch." If
the drafter prefers "let it do" because it covers both dials, then use "let it do" in the rule
everywhere instead. Either is fine; the same words in title, position, step 1 and landing is what matters.

**On the position choice (brief §0):** option 3 serves this reader well. It gives them something to do,
and the reader is someone about to hand an agent a job. I have no finding against it.

---

**Verdict: ready after fixes.** The argument is clear and the steps are usable; findings 1-5 are the ones
a reader would stall on or misread, and finding 1 is an accuracy fix about our own published essay.
