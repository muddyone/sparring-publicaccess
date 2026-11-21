# Cold read: essay 07, "A smarter AI isn't a safer one" (Nadia Okonkwo), 2026-11-18

Read once, straight through, as an everyday AI user on a phone. I have not read the series, brief 13, the
options file or any other background. Where I say "I stalled", I mean I stopped and went back.

## What I took away

An "agent" is just an AI I've let do things for me: send the email, touch the files, spend the money. What
decides how much damage it can do is what I've let it reach and how long it runs before I look, not how
clever it is. Cleverer models aren't harder to trick; in one test they were easier, because a weak model that
gets fooled bungles the attacker's instructions and a strong one carries them out. So before I hand one a job:
give it only what the job needs, don't let it see my private stuff, read outside content and send things out
all at once, make it stop before anything I can't undo, actually read what it asks me to approve, and check the
work rather than trusting "done". Raise its limits as it earns them, the way I would with a new hire.

That's a clear message and I'd act on it. The title told me what I was getting and the essay delivered it.
Three things worked on me: "more capable models tend to be easier to attack" (the line I'd repeat to someone),
Willison's three-part test (the one thing I could actually apply tonight), and "Nobody calls a spending limit an
insult to the new hire." I also liked that it credits a 1975 security principle instead of acting like it just
discovered least privilege. I'm tired of people who just discovered a problem; this one didn't do that.

Where I drifted: the middle of "Same model, different worker" (the developer-access paragraph) and most of
"Two meanings of 'agent'". On a phone, the second one is where I'd have started skimming. It opens by
correcting an essay I never read, then stacks five definitions from five authorities. I came back at "What
it's allowed to touch sets the limit", which is where the essay really starts for me.

**Would I comment?** Yes, with a question: "Step 2 says remove one of the three. But if I connect ChatGPT to my
email, it gets all three at once: my private mail, outside mail coming in, and the ability to send. Which one
am I supposed to remove, and how, when the product bundles them?" The essay doesn't answer that, and it's the
step I most want to take.

## Findings, ranked

### 1. Step 2 tells me to "remove one of the three" but not how a normal person does that

> "2. **Run Willison's test.** If it can see your private data, read things from outside, and send messages
> out, all three at once, someone else can make it send your data to them. Remove one of the three."

**What went wrong.** This is the most useful step and the least usable. I understand the test. I don't know
what "remove one" looks like in an app I'd actually use. Email is the obvious case, and an email-connected
assistant has all three by nature. I finished the list knowing the danger and not the move.

**Impact: 8.**

**Fix.** Add one or two concrete examples right in the step: what removing each leg looks like (don't connect
it to the account with private data; keep it off outside web pages and mail for that job; let it draft but not
send). If email genuinely can't be made safe this way, say that plainly; it's a finding a reader would want.
This adds words, and it's the step the brief says readers will act on.

### 2. "Two meanings of 'agent'" is where I'd stop on a phone, and its payoff is at the bottom

> "Here I have to clear up something this series itself muddied. In essay 03 I said there really is an agent on
> the other end of the conversation."

**What went wrong.** Second section in, and I'm being asked to care about a correction to an essay I never
read. Then come Chalmers, OpenAI, Anthropic, the Restatement of Agency and a 1995 paper, one after another. It
read like borrowing authority to define a word. The sentence that actually helped me is the last one:

> "The first is a description it earns. The second is a role you hand it."

That's good, and I only got it because I read on out of duty.

**Impact: 7.**

**Fix.** Lead the section with the plain split (one meaning is "something you can talk to as having aims",
the other is "something you've let act for you"; this essay means the second). Then do the essay 03 correction
in a sentence or two, as an honest aside. Then give the sources as support. Don't cut the correction, because
owning it is to the essay's credit. Just don't make it the doorway.

### 3. The "rigid script" line contradicts the Anthropic definition two paragraphs earlier

> "In a *workflow*, the steps are fixed in advance by the people who built it. In an *agent*, the model
> 'dynamically direct[s] [its] own processes and tool usage'"

> "a rigid script that books your flights is the reverse"

**What went wrong.** I'd just been told that fixed steps make a *workflow, not an agent*. Then a rigid script
is offered as an agent in the working sense. I stalled and went back. Either the essay's working sense is
"acts for you" (OpenAI's and the law's) and Anthropic draws a narrower line, or the example is wrong. As
written, it looks like the essay didn't notice.

**Impact: 6.**

**Fix.** Say that the definitions differ on this point. For example: "acting for you" is what they share;
Anthropic draws a further line between fixed workflows and agents that choose their own next step; by the broad
sense a flight-booking script counts, by Anthropic's it doesn't. Or pick an example that is an agent by every
definition given.

### 4. The NIST number doesn't show what its paragraph claims

> "And when US government testers built stronger attacks against one leading model, their success rate rose
> from 11 tries in 100 to 81"

**What went wrong.** The paragraph is arguing that smarter *models* aren't safer. This sentence is about
smarter *attacks* against one model. It's a real and alarming number, but it's evidence that the attackers get
better, not that capability fails to protect. I read it twice looking for the connection. (Also: it's the
second "11 out of 100" in the essay, after the programming one. I briefly thought it was the same study.)

**Impact: 6.**

**Fix.** Either say what it shows in its own words ("and the attacks improve too: ...", which supports
"don't wait for the models to grow out of it"), or move it to the prompt-injection section, where it shows how
real the threat is.

### 5. The blackmail stress test is the biggest jolt in the essay and it's buried mid-sentence

> "In stress tests that its authors deliberately set up to leave no other way out, leading models from several
> companies sometimes chose harmful actions, such as blackmail, to avoid being replaced or to reach their
> goals."

**What went wrong.** Two things. First, "its authors": the tests are plural and nothing owns "its", so I
tripped on the grammar. Second, "AI models chose blackmail" is the thing a reader will remember and repeat, and
it lands in the middle of a paragraph about capability cutting both ways. It also seems, at first read, to cut
*against* the essay: if models choose harm on their own, isn't the model the problem? The essay's answer (the
authors' own advice is about access and oversight) comes a sentence later and I nearly missed it.

**Impact: 6.**

**Fix.** Give it its own short paragraph. Say what the setup was in a plain sentence, say the authors found no
sign of it in real use, then say why it supports the essay: even here, the advice was to limit access and keep
a person watching. That's additive, and it's worth it, because readers will take this sentence away whatever
you do with it.

### 6. "your assistant" switches meaning without warning

> "A sentence hidden in an email won't usually turn your assistant against you; it can turn an agent."

**What went wrong.** The whole essay has used "assistant" to mean the AI ("an AI assistant you work with",
"An AI agent isn't a smarter assistant"). Here it means a human assistant. I read it as ChatGPT first, and then
the sentence made no sense.

**Impact: 5.**

**Fix.** "your human assistant", or "a person you've hired".

### 7. "The company's chief executive": which company?

> "a coding agent reportedly deleted a company's live database during a code freeze. The company's chief
> executive called it 'unacceptable'"

**What went wrong.** I took "the company" to be the one whose database got deleted. Then it didn't make sense
that their CEO was announcing fixes to the tool. I think it's the tool maker's CEO, but the text gives me two
companies and one "the company".

**Impact: 5.**

**Fix.** Name the tool maker, or say "the chief executive of the company that makes the tool". Naming it is
also fairer to them: it shows their CEO said it should never be possible and fixed it.

### 8. "a fivefold increase in the computing power spent training the model" means nothing to me

> "A survey of such improvements estimated that most were worth more than a fivefold increase in the computing
> power spent training the model"

**What went wrong.** The 11 vs 18 sentence just before it worked; I could see "more than half better". This one
I can't picture. I don't know what training compute is worth or how big a fivefold increase is. It passes
straight through me.

**Impact: 4.**

**Fix.** Say it on a scale I know, in plain words: something like "the setup gained as much as making the model
itself several times bigger would have", if the source supports that reading. Or say what it means for me (a
better setup can matter more than a newer model) and leave the multiplier as backup.

### 9. The developer-access paragraph lost me

> "Through the companies' developer access, the model remembers nothing from one request to the next"

> "The chat app adds standing instructions of its own at the start of every conversation, which developers'
> access doesn't get"

**What went wrong.** I use the chat app. I've never used "developer access" and don't know what it is. Three
Anthropic documentation links in a row, about a product layer I'll never see, before the payoff. The payoff is
good ("It isn't about how smart the model is. It's about what it can reach."), and the coding-tool permission
setting is the part that earns it.

**Impact: 4.**

**Fix.** Say "developer access" in plain words once (the version programmers build products on). Then put it
in terms of what I see: the memory and the instructions in my chat app were added by the app, not the model.
Keep the permission-setting example; it's the strongest thing in the section.

### 10. "Length of task" in what?

> "One measure of the length of task agents can complete has been doubling about every seven months"

**What went wrong.** Length in steps? In hours? Of the agent's time or a person's? "Doubling" means nothing
until I know what's doubling.

**Impact: 3.**

**Fix.** Say what the length is measured in, in the words the brief gives for the source.

### 11. "It made the agent safe" claims more than the sentence before it

> "It stopped the attacks they tested 'even when underlying models are susceptible' ... It made the agent safe
> without making the model any harder to fool."

**What went wrong.** The study stopped the attacks they tested. "Safe" is a much bigger word, and I'm skeptical
of it in a security context.

**Impact: 3.**

**Fix.** "safe against those attacks", or "It protected the agent without making the model any harder to
fool."

### 12. Small stalls

- **"the… server code itself"** (the GitHub incident). What server? It's the first and only time a server
  appears. "the tool's own code", or one clause saying what it was.
- **"More steps alone is fine for work you can undo."** I read "alone" as "only" first. "Letting it take more
  steps on its own is fine..."
- **"that's a sign it's asking about too much, or should be allowed less."** I couldn't tell if "allowed less"
  was the fix or the diagnosis. If I'm clicking "allow" without reading, my instinct is the reverse: let it do
  the safe things without asking, so the questions that remain are the ones worth reading. Say which you mean.
- **"for good or ill"** in the bold position. The limit is on *harm*; capability can't reach more of a harm
  limit "for good". The later "ceiling" paragraph says this better.
- **"from operator to observer"**. I wasn't sure who was the operator: the person or the AI. A few words
  ("from the person running each step to the person only watching") fix it.
- **"Part one's advice"**, **"essay 02"**, **"essay 03"**. Fine for series readers, and each is mostly
  explained in place. But together with the essay 03 correction, I felt I'd walked into the middle of something.

## Verdicts on the drafter's flags

**Flag 1, length (mine).** I didn't feel the length on the strong sections; access, smarter-isn't-safer,
compared-to-what and the list all moved. I felt it on "Two meanings" and the developer-access paragraph, and
that's an ordering problem, not a word-count problem (findings 2 and 9). Nothing should be cut. If anything,
the essay is *under*-explained in three places a reader will act on or repeat: step 2's "remove one" (finding
1), the blackmail study (finding 5), and the NIST number (finding 4). Net, it gets slightly longer, and should.

**Flag 7, the worked example (mine).** It lands, and the last three lines are the best landing in the essay:
"The agents are capable enough to publish it. They aren't allowed to. That's the point." It's concrete enough
in outline (one builds, one checks, one plans; a public page; neither can publish). Three things would make it
land harder:

- **"Today"** will be false on the day I read it. Give it a day, or "this week". And if the fix is *still*
  waiting on you when the essay goes out, say so. It's honest, and it shows the rule costs something, the same
  way the 77-vs-84 trade-off did. A skeptical reader is already thinking "so a link fix waits on you?"; answer it
  before she does.
- **"a page of mine that anyone can read"** is a roundabout way of saying a public page or your website.
- **What could have gone wrong** if they could publish. One sentence (a bad fix live in front of everyone,
  with nobody having looked) turns a story about restraint into a story about a harm that didn't happen.

**Flag 8, the title (a view).** Works. I knew what I was getting and it's the claim I'd repeat. It's a sentence
and a half, but both halves earn it.

**Flag 2, "Two meanings" (a view).** The correction is fair and owning it is to the essay's credit. Placement is
the problem: it's the doorway to the second section, for a reader who never saw essay 03. See finding 2.

**Flag 5, the incidents (a view).** Hedging felt right ("reportedly", "single reported cases, not rates").
Nothing felt unfair to the companies. Naming the tool maker in the first one (finding 7) would be fairer, not
less fair, because their CEO's response is on the record and reflects well.

**Flag 6, Green 2022 (a view).** Honest and clear. The essay says plainly it's about government systems and
that no study of agent prompts was found. The "twentieth time in an hour" line does the rest, and I believed it.

## Verdict

Ready after fixes: the argument is clear and I'd act on it, but fix step 2's "remove one", restructure "Two
meanings" so its payoff leads, and repair the rigid-script, NIST and blackmail passages before it goes out.
