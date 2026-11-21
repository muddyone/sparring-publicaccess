# Miriam Vale: argument read, the "What if no one can press send?" paragraph (essay 07, 2026-11-21)

Essay: `docs/research/what-ai-is/positions/07-agents.md`, the paragraph after the six-step list (lines 351-359),
beginning "What if no one can press send?". Read the whole essay first. No new sources consulted or proposed.
Consulted: my persona and memory file (standing anti-overclaim positions); prior panel reports 12 (Ines, approval
fatigue) for the Hughes 2026 wording. Not consulted: the brief or cite-check files, since no claim here turns on a
source.

Lens: does the paragraph follow from the essay's own argument (Willison's three-part test, least privilege, the
three dials, the key-versus-rule distinction, the protective-layer finding) without overreaching?

## Overall diagnosis

The paragraph answers a real question the essay invites, and its first move is right: if sending can't be removed,
take away the private data. But it reads as a recipe that closes the problem, and the essay's own argument says it
can't. The essay's claim is that access caps harm, not that limits prevent mistakes or attacks. The paragraph never
says what harm is left after the cap, and the thing it relies on to cover that gap ("a promise goes to a person") is
a rule, not a key: the exact weaker kind of limit the essay spends three sections warning about. The chat-assistant
half then says the opposite of the essay's evidence on oversight. Both are fixable without new sources, and the
fixed version is stronger, because it shows the essay's framework working on a hard case instead of waving it
through.

Strongest element: "so take away the third part" applied to a job where sending is the job. That's the essay's
test doing real work, and it should stay.

## Ranked findings

### F1. The promise guard is a rule, not a key, and the paragraph doesn't say so. Impact 9

Passage: "anything that can't be undone, such as a refund or a promise, goes to a person."

What's wrong: a refund can be keyed (give the agent no refund tool). A promise can't. A promise is just words in a
reply, and writing replies is the job. Nothing in the settings can stop an auto-responder from writing "we'll
refund you in full"; only its instructions can, and the essay has just said instructions are "just text the model
reads, and as we've just seen, other text can override it." The customer's email is that other text. So the
paragraph puts a rule and a key side by side as if they were the same kind of limit, a page after "Where you can,
take the key." A careful reader will catch it, and it's the one place a critic can turn the essay's central
distinction against it.

Replacement: separate the two. "…and it has no way to issue a refund or change an account. Even then, one thing is
left that no setting takes away: what it says, in your name, to whoever wrote. A planted line, or a plain mistake,
can still make it promise something you didn't offer. Telling it to hand promises to a person is a rule, not a key."

### F2. It implies the setup is safe, when the essay only claims access caps harm. Impact 8

Passage: the paragraph as a whole, ending the auto-responder half on "And have someone read a sample of what it
sent, so mistakes surface early."

What's wrong: the essay's position is that access "sets the limit on the harm", and that the third dial decides
"how much goes wrong before anyone can stop it." Applied honestly here: access has been narrowed, so the leak is
capped, but the third dial is now set to "after it's sent", because every reply goes out before anyone looks.
Sampling doesn't stop anything; it finds it afterwards. "Surface early" overstates that. The paragraph also never
names the residual harm (F1), so a reader comes away thinking the four moves make the auto-responder fine. That is
the overreach the essay's own "What this doesn't claim" list is built to prevent.

Replacement: "And have someone read a sample of what it sent. That finds problems, but only after they've gone
out. So this setup limits the harm; it doesn't make it safe."

### F3. The private-data move dodges the common case: answering needs the sender's own records. Impact 8

Passage: "take away the third part: it shouldn't be able to see your private data. Give it only what it needs to
answer, such as your hours, your prices, and your common questions."

What's wrong: the examples are all public information, which makes the step look easy. Many auto-responders exist
to answer "where's my order?" or "when does my plan renew?", and that needs the customer's own records. Those are
the business's private data. The paragraph doesn't say what to do then, so the reader who most needs it either
concludes the advice doesn't fit their job or connects the whole customer database. The essay's argument has a
clean answer: least privilege. Let it see only the records of the person writing, and let the system decide who
that is, not the email (anyone can write "I'm customer 4417"). Then the third part isn't gone, it's shrunk: the most
a planted line can get out of it is what the sender could already see. Saying "shrunk, not gone" is the honest
version, and it fits Willison's test better than pretending the leg was removed.

Also note, without adding it to the essay: "reply only to the person who wrote in" does not close the leak on its
own, because the person who wrote in is the very person who may have planted the instruction. It limits who else
gets hit, which is worth having, but the data rule is what does the work. The replacement keeps the two in that
order for that reason.

Replacement: "If it has to look up a customer's own order, let it see only that customer's records, matched by the
system, not by what the email claims. That doesn't remove the third part, but it shrinks it: the most a planted
line can get out of it is what the sender could already see."

### F4. "There's already a reviewer" contradicts the essay's oversight evidence and step 5. Impact 8

Passage: "A chat assistant that answers you directly is a different case. The person who asked reads the answer,
so there's already a reviewer."

What's wrong: this is the reader's case Bart named: a chat answer used without review. The sentence answers it by
asserting the review happens. The essay's own evidence says being in the reviewer's seat isn't reviewing: Green
2022 ("people are unable to perform the desired oversight functions"; "a false sense of security") and Hughes
2026 (93 in 100 approval prompts accepted; "approval fatigue"). Step 5, ten lines up, says "'Done' is a claim, not a
result." A chat answer is a claim. And the first five essays' advice, restated here, is to trust it only as far as
its record in that job has earned. So the sentence contradicts three things the essay stands on, and the reader it
was written for is exactly the one it misleads.

What is true, and follows from the essay: a chat assistant with nothing connected isn't acting for you (the Notes
already say it isn't an agent "in the working sense"). Its answer goes nowhere until you use it, so the person who
acts is you, and the question becomes whether you check it, which is the earlier essays' question, not this one's.

Replacement: "A chat assistant that answers you, with nothing connected, isn't acting for you; you are. Its answer
goes nowhere until you use it. But don't count your reading it as a check. Seeing an answer isn't checking it, any
more than seeing an approval prompt is reading it, and step 5 applies here too: an answer is a claim, not a result.
If you'll act on it in a way you can't undo, check it first."

### F5. "Answers you directly" is not the same as "safe", once the chat is connected. Impact 6

Passage: "The risk comes back when the answer goes somewhere on its own, such as into a tool that acts on it."

What's wrong: this names one way the risk returns and implies it's the only one. Most chat apps now let the
assistant search the web and connect to email or files. A chat that can read your files and read web pages has two
of Willison's three parts before any answer "goes somewhere", and it may have the third by fetching a page or link.
I suspect a critic who knows the security literature will raise chat-app data leaks here; I'm not proposing a source
for it, and the essay doesn't need one, because it follows from the essay's own test. The fix is to make the test the
trigger, not the destination of the answer.

Replacement: "And once the chat can see your files or email, or browse the web, or its answer goes straight into
something that acts on it, it's acting for you, and the same questions apply, starting with Willison's test."

### F6. Unacknowledged tension with step 3. Impact 5

Passage: "Some jobs need an agent to write and send on its own".

What's wrong: step 3 lists sending among the things you can't undo and says "set it to stop and ask." The
auto-responder breaks that by design. That's a legitimate trade, but unannounced it reads as the essay quietly
dropping its own rule when the rule is inconvenient. Naming the exception is one clause and it pays off later: it
is why sampling (F2) and the residual-harm line (F1) are needed. "Need" is also a little strong; the job could have
a person. "Built to" is accurate.

Replacement: "Some jobs are built to have an agent write and send on its own, such as an auto-responder that answers
customer email. That's a deliberate exception to step 3, because every reply it sends is one you can't take back."

### F7. Mark the keys as keys. Impact 4

Passage: "Then keep the sending small: it can reply only to the person who wrote in, with no attachments".

What's wrong: these can be real keys, but the paragraph doesn't say where they're set. Every step in the list says
"in the tool's settings, not only in what you tell it"; this paragraph is the one place a reader most needs that and
doesn't get it. Without it, "reply only to the sender" reads like an instruction to the agent.

Replacement: "Then narrow the sending in the tool's settings: it can reply only to the person who wrote in, with no
attachments, and it has no way to issue a refund or change an account."

## Refutation check (anything a careful reader could use against the essay)

- F1 is the sharpest: the essay's own key-versus-rule distinction, applied to its own advice. Fix before publishing.
- F4 is the second: the essay's own oversight evidence, applied to its own reassurance.
- A reader who knows of real cases where a company was held to a promise its customer-service chatbot made will
  read the current text as naive. The fix (F1, F2) answers that without citing anything.
- Nothing in the fixed version needs a new source. Every claim in it follows from Willison's test, least privilege,
  the three dials, or the key/rule distinction already argued in the essay.

## Proposed replacement (two paragraphs; the second is the chat case)

The current paragraph carries two different cases. Splitting it keeps each one honest; nothing is cut.

> What if no one can press send? Some jobs are built to have an agent write and send on its own, such as an
> auto-responder that answers customer email. That's a deliberate exception to step 3, because every reply it sends
> is one you can't take back. Willison's test still applies. The agent has to read things anyone could have
> written, and it has to send, so the part to take away is the private data. Give it only what it needs to answer,
> such as your hours, your prices, and your common questions. If it has to look up a customer's own order, let it
> see only that customer's records, matched by the system, not by what the email claims. That doesn't remove the
> third part, but it shrinks it: the most a planted line can get out of it is what the sender could already see.
> Then narrow the sending in the tool's settings: it can reply only to the person who wrote in, with no attachments,
> and it has no way to issue a refund or change an account. Even then, one thing is left that no setting takes away:
> what it says, in your name, to whoever wrote. A planted line, or a plain mistake, can still make it promise
> something you didn't offer. Telling it to hand promises to a person is a rule, not a key. So have someone read a
> sample of what it sent. That finds problems, but only after they've gone out. This setup limits the harm; it
> doesn't make it safe.
>
> A chat assistant that answers you, with nothing connected, isn't acting for you; you are. Its answer goes nowhere
> until you use it. But don't count your reading it as a check. Seeing an answer isn't checking it, any more than
> seeing an approval prompt is reading it, and step 5 applies here too: an answer is a claim, not a result. If
> you'll act on it in a way you can't undo, check it first. And once the chat can see your files or email, or browse
> the web, or its answer goes straight into something that acts on it, it's acting for you, and the same questions
> apply, starting with Willison's test.

Accuracy note for whoever merges: "matched by the system" is only as good as how the system knows who wrote in. If
Ines or Vera want it tighter, "checked against a sign-in, not taken from what the email claims" is the stricter
version; I kept the plainer one.

## Verdict

Right instinct, wrong ending: as written it reassures where the essay's own argument says it can't, twice; with
the replacement it becomes the essay's best worked example of limiting harm without pretending to prevent it.
