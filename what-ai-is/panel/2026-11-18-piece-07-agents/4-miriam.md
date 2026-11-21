# Miriam Vale: argument review, essay 07 (first panel read), 2026-11-18

Lane: argument. Does the essay earn its position or only assert it? Is any sentence stronger than its evidence,
as brief 13 records that evidence? Are the counter-arguments handled fairly?

**What I read:** my persona and my memory (standing positions,
especially "citing a paper imports its other results", "both directions of inaccuracy about a third party are
failures", "a disclosure gesture raises the standard for everything it does not mention", and "check the
comparator"); the panel brief; the draft `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md` (body and
notes; Draft notes only where the brief points); brief 13 in full
(`docs/research/what-ai-is/briefs/2026-10-19-13-agents.md`); the options page
(`docs/research/what-ai-is/positions-drafts/13-agents-options.md`); essay 03
(`docs/research/what-ai-is/positions/03-someone-there.md`); essay 00's summary line for essay 03 and essay 02's
engine-and-car line, to check what the series actually said. Format from the essay 06 review. I added no new
sources, and every narrowed wording below stays inside what brief 13 says its source says. I did not update my
memory file, per this run's instruction to edit no other file.

## Overall diagnosis

The essay's core argument is sound and it is the right argument for this reader: an agent's access is the
ceiling on the harm it can do, so "what am I letting it do?" is the better question than "how smart is it?".
The evidence for that ceiling (Greshake, OWASP, Willison, the two incidents, CaMeL, least privilege) is real
and well used. The honesty apparatus is good: "single reported cases, not rates", CaMeL's cost reported, Lynch's
own caveats kept, the Green stretch disclosed, a real "What this doesn't claim" list.

**But the essay asserts two things more firmly than it shows.** First, it misquotes its own essay 03 in the very
paragraph that corrects essay 03. Second, its headline claim, "a smarter model isn't a safer one", is evidenced
only for one kind of harm (being fooled by planted instructions), while the title and position apply it to
safety in general. A third, quieter problem: the "working sense" of agent, as defined, contradicts the Anthropic
definition quoted two sentences earlier. And twice a source's hedge is hardened on the way in (Green, Kolt).
All of this is fixable without changing the position; most fixes add a clause, not a section.

**Strongest objection a fair critic would raise.** *"Every study behind your title measures how easily an agent is
fooled by an attacker. Your lead incident, the deleted database, had no attacker: it was a mistake made with
access the agent held. On plain mistakes you cite nothing about capability, and your own line that a capable
agent 'does more of the good job' suggests a smarter one might make fewer of them. So for the most common
everyday harm, smarter might well be safer, and your title says otherwise without evidence."* As drafted, the
essay doesn't answer this. With finding 3 adopted it does, and the ceiling argument loses nothing, because the
ceiling holds whichever way the mistake rate goes.

---

## Ranked findings

### 1. Impact 8: the correction misquotes essay 03 (flag 2)

> "Here I have to clear up something this series itself muddied. In essay 03 I said there really is an agent on
> the other end of the conversation."

**The problem.** Essay 03 never says that. Its position is "there really is something on the other end", and its
term for that something is Chalmers's "quasi-subject", with "quasi-beliefs and quasi-desires". The phrase "an
agent on the other end" comes from essay 00's one-line summary of essay 03 (and from brief 13, which repeated
it). A reader who goes back to check, which a correction invites, finds the essay misquoting itself in the
sentence that claims to set the record straight. That is the one kind of sentence that costs more when wrong
than when absent.

The real muddle is a different one, and a better case for the correction: essay 03 used "agent" both ways
without saying so. Its roadmap's "a unified agent" is the philosopher's sense, and its "Where this gets harder"
paragraph says "several AI agents ... all drawing on a shared project record", which is the working sense. Its
"it" also already took in "a fuller setup that works on its own with files and tools". So the series did blur
the word; it just didn't do it in the sentence quoted.

The same paragraph then says "On that view even a chat assistant that can't touch anything is an agent." In
Chalmers's terms (as brief 13, 3.4 records them) it is a quasi-subject. Saying "agent" here restates the
overview's gloss, not his word.

**Fix.** Quote essay 03 accurately ("there really is something on the other end", what Chalmers calls a
"quasi-subject"), say the overview summed that up as "an agent on the other end", and note that essay 03 also
used "agents" for the working kind. Replace "muddied" with a neutral statement that the series has used the word
two ways: "muddied" is mildly self-deprecating about our own work (brief §3), and the accurate version is also
the more generous one. Use "quasi-subject" (or "agent in the philosopher's sense, what Chalmers calls a
quasi-subject") in the next sentence.

**Placement:** right where it is. The position paragraph already says "in the working sense", which presupposes
another sense, so add one clause to the "By 'it' I mean" paragraph pointing ahead ("and by 'agent' the working
sense, which I separate below from the sense essay 03 used"). That costs ten words and stops a reader from
essay 03 hearing "the someone, now with tools" for four paragraphs.

### 2. Impact 8: the opening asserts a frequency the essay later says it doesn't have

> "But when an AI agent does real damage, the story is nearly always about what it was allowed to do, not how
> intelligent it was."

**The problem.** "Nearly always" is a rate. The essay later says, correctly, "These are single reported cases,
not rates" and "I found no study of how often agents cause harm in the field at each level of access." The
opening claims exactly what the disclaimer disowns, and it is the sentence that frames the whole essay. The
reader is pushed to the conclusion before the argument starts.

**Fix.** Scope it to what was looked at: in the cases I found (or: in the reported cases), the story was about
what it was allowed to do. That is nearly as strong, and it matches the essay's own later honesty.

### 3. Impact 7: "a smarter model isn't a safer one" is evidenced for manipulation only (flag 4)

> "So a smarter model isn't a safer one" (position) · "The natural hope is that better models will grow out of
> this. The evidence so far says no."

**The problem.** Debenedetti 2024, Zou 2025 and NIST 2025 all measure one thing: how often an attacker's planted
instructions succeed. On that, the claim holds: one benchmark found "more capable models tend to be easier to
attack", a large competition found "limited correlation" with capability, and none of the essay's sources shows
robustness rising with capability. The section body is correctly scoped to "this" (prompt injection). But the
title and the position drop the scope and say "safer" in general, and the essay's lead incident (the deleted
database) involved no attacker at all. Brief 13 offers nothing on whether more capable models make fewer plain
mistakes with the access they hold; ToolEmu and Agent-SafetyBench (5.5) report failure rates but not sorted by
capability. The essay's own "A more capable agent does more of the good job" hints the other way for mistakes,
which is the fair critic's opening.

"The evidence so far says no" is also firmer than the brief's own reading. Its Open questions call the
capability–robustness link "Unsettled", resting on two studies with 2024–2025 models, one a single benchmark.

**Does "ceiling" vs "how much of it it reaches" hold up?** Yes, and it is the essay's best idea. It survives the
objection above intact: whatever the mistake rate, the access limit bounds the worst case. It also absorbs Lynch
correctly (capability finds harmful routes, but only inside what the agent can touch). It needs one condition
stated: see finding 6.

**Is the claim stronger than the evidence?** In the title and position, yes, modestly. In the section body, only
in "says no".

**Fix.** (a) Change "The evidence so far says no" to something like "The evidence so far doesn't support it",
and say it rests on two large tests. (b) Add one or two sentences, after the Zou or NIST line, saying these
studies measure being fooled by an attacker; on whether smarter models make fewer plain mistakes, I found
nothing that settles it, and even if they do, the access limit is what bounds the worst case. (c) That sentence
lets the title stand, read as "isn't safer by being smarter". If the drafter prefers, the position can say
"isn't, so far, any harder to fool", but with (b) in place I would keep the title.

### 4. Impact 7: the working definition contradicts the Anthropic line just quoted

> "In a *workflow*, the steps are fixed in advance by the people who built it. In an *agent*, the model
> 'dynamically direct[s] [its] own processes and tool usage'" ... "and a rigid script that books your flights is
> the reverse."

**The problem.** The essay's working sense is "something you have let act for you": delegation. Anthropic's line
is about who decides the next step: autonomy. On Anthropic's own definition, a rigid flight-booking script is a
*workflow*, not an agent, yet two sentences later the essay calls it an agent in the working sense. The two ideas
the essay later separates as two dials (what it may touch; how far it goes before anyone looks) are fused into
one definition here. A careful reader notices the contradiction; a casual one absorbs a definition the essay's
own sources don't share. The Wooldridge & Jennings "weak notion" is also autonomy ("operate without the direct
intervention of humans"), not delegation.

**Fix.** Say the working definitions agree on acting for someone, and differ on how much the thing decides for
itself, which is why agency comes in degrees (brief 13 Q8 Part 2: "how much it is allowed to do for you, and how
many steps it takes before you look"). Then either drop the rigid-script example or say what it shows: a script
acts for you, but on Anthropic's line it is a workflow, not an agent. This sets up the "how far it goes" section
instead of undercutting it.

### 5. Impact 7: Green's hedge is hardened, and the sentence's logic is off (flag 6)

> "A review of 41 government policies that require people to oversee automated decisions found that 'people are
> unable to perform the desired oversight functions'"

**The problem.** Brief 13 records Green's words as "evidence suggests that people are unable to perform the
desired oversight functions". The essay drops "evidence suggests" and adds "found". It also makes the policy
review the source of the finding, but reading 41 policies can't show that people are unable to oversee anything;
Green surveys the policies and draws on the evidence about people. The source's hedge is the honest part, and
removing it makes Green say more than he did.

**Is the stretch honest and clear?** Yes. "That was about government systems, not AI agents, and I found no study
of whether people really read the approval prompts agents show them" is exactly the right disclosure, and "I
wouldn't lean on it too hard" is well calibrated. The closing "Anyone who has clicked 'allow' for the twentieth
time in an hour can guess" is an appeal to the reader's experience immediately after admitting there's no
evidence; it is labelled as a guess, so it is acceptable voice, but it is the one place the essay pushes rather
than shows (impact 2, keep if Bart likes it).

**Fix.** Restore the hedge and fix the structure: a review of 41 such policies argued that they rest on a weak
footing, because "evidence suggests that people are unable to perform the desired oversight functions", and that
they can give "a false sense of security". Keep the disclosure sentence as it is.

### 6. Impact 7: the ceiling needs "allowed" to mean enforced, and the worked example must show that

> "What it's allowed to touch ... set the limit on the harm it can do." · "Neither could publish it. Changing
> what the public sees waits for me. The agents are capable enough to publish it. They aren't allowed to."

**The problem.** The ceiling argument holds only if "allowed" means what the setup actually lets it do, not what
it has been told. Brief 13 (1.3) makes the point itself: the model only requests actions, and the software that
carries them out "is where permission lives". The essay never says this, and the reader needs it more than any
other single idea here, because the commonest everyday "limit" is an instruction ("don't send anything without
asking me"). The essay's own lead incident shows why: the database was deleted during a code freeze, and the fix
the source records was a separation the setup enforces ("automatic separation between development and
production databases"). The brief doesn't say whether the agent had been told about the freeze, so don't claim
that; the fix alone carries the point.

The worked example then has to be an enforced limit to land. If the agents can't publish because they don't
hold the credentials or the push needs Bart's approval in the tool, the example is perfect and should say so in
a clause ("they don't hold the key"). If the hold is a rule in the agents' instructions that they follow, the
example illustrates obedience, which is the weaker kind of limit the Replit case warns about. I have no evidence
either way about how this hold is enforced; the drafter or Bart should check before publication.

**Fix.** Add two or three sentences in "What it's allowed to touch" saying a limit is what the setup enforces,
not what the agent is told, with the database fix as the example. Make the worked example say which kind of limit
it is. Step 1 of the list could carry four words of this ("set it in the tool, don't just tell it").

### 7. Impact 6: Kolt is hardened and given reasons he didn't give

> "A legal scholar who applied agency law to AI agents found its usual remedies strained for exactly these
> reasons: agents 'that make uninterpretable decisions and operate at unprecedented speed and scale'"

**The problem.** Brief 13 records Kolt as saying conventional fixes "might not be effective". "Found ... strained"
upgrades an argument to a finding. And "exactly these reasons" claims Kolt names the essay's two differences, but
his are opacity ("uninterpretable decisions") and speed and scale. He doesn't mention text that redirects the
agent. Only one of the two matches.

**Fix.** "Argued its usual remedies might not work for agents 'that make uninterpretable decisions and operate at
unprecedented speed and scale'." Either drop "exactly these reasons", or adopt opacity as a third difference (the
quote already supports it, and it bears on step 5, checking the work).

### 8. Impact 6: "the company's chief executive" reads as the victim's CEO (flag 5)

> "a coding agent reportedly deleted a company's live database during a code freeze. The company's chief
> executive called it 'unacceptable'"

**The problem.** "The company" points back to the company whose database was lost. Per brief 13, the speaker is
the chief executive of Replit, the company that makes the agent ("Replit agent in development deleted data from
the production database"). As written, the reader misattributes the quote, and loses the fact that is most fair
to the company: its own CEO called it unacceptable and the company shipped a fix.

**Fix.** "The chief executive of the company that makes the agent called it ..." Naming Replit is fine, since the
source URL names it; not naming it is also fine.

**Flag 5 verdict.** Fair to both companies, and the hedging is right: "reportedly" on a secondary source, and
"single reported cases, not rates" up front. Two smaller fixes: in the GitHub quote, the ellipsis removes
"GitHub MCP" from "not a flaw in the GitHub MCP server code itself", which is the clause that clears GitHub, so
restore it; and brief 13 says "a user's agent", not "coding agent". "In each case the agent held access the job
didn't need, or that no one was checking" is brief 13's own reading, marked [ours]; frame it as the essay's
reading ("in each case, as I read them") rather than as a finding (impact 3, all three together).

### 9. Impact 6: step 6 ("raise its limits as it earns them") ignores the essay's own first section

> "We do raise people's limits as they earn trust, and an agent's limits can grow the same way, as its track
> record in that job builds up." · "6. Raise its limits as it earns them, in that job, as you would with a
> person."

**The problem.** The essay's first argument is that a different setup or model is a different worker. It follows
that a track record belongs to one model in one setup, and starts again when either changes, which for products
that update often is frequently. Second, the essay's first difference (any text it reads can redirect it) means a
good record doesn't protect against the next planted instruction: an attacker doesn't care how well the agent has
behaved. As written, step 6 invites the reader to relax exactly the limit that Willison's test says to keep.

**Fix (additive).** One sentence each: the record belongs to that model in that setup, so it starts again when
either changes; and earned trust can widen what the agent does, but shouldn't hand it all three parts of
Willison's test. Both come from the essay's own argument, so no new source.

### 10. Impact 5: the position says autonomy sets the limit; the ceiling paragraph says only access does

> Position: "What it's allowed to touch, and how far it goes before anyone looks, set the limit on the harm it can
> do." · Later: "What an agent is allowed to touch sets the ceiling on the harm it can do."

**The problem.** The two statements disagree, and the later one is the correct one. How far it goes before anyone
looks doesn't cap the worst harm; one unreviewed irreversible step can reach the ceiling. What it changes is how
much damage lands before someone can stop it, which the essay itself says ("the damage can arrive before anyone
reviews it"). The position follows brief 13's candidate restatement, but the brief elsewhere (6.5) treats autonomy
as "a third dial", not part of the ceiling.

**Fix.** In the position: what it can touch sets the limit; how far it goes before anyone looks decides how much
goes wrong before you can stop it; how capable it is decides how much of the limit it reaches. Three dials, each
named for what it does, which also matches the section headings.

### 11. Impact 5: the NIST figure is placed as evidence for something it doesn't show

> "And when US government testers built stronger attacks against one leading model, their success rate rose from
> 11 tries in 100 to 81"

**The problem.** It sits third in a list arguing that more capable models aren't more robust. It compares
attacks, not models: it shows that a leading model's apparent robustness depended on how hard it was attacked.
That is a real and useful point (a benchmark's low attack rate can understate the risk), but the reader is
invited to take it as a third capability result.

**Fix.** Say what it shows: even a leading model, against stronger attacks than the benchmark's, was fooled 81
times in 100. That supports "don't rely on the model" directly. (The numbers' presentation is Vera's.)

### 12. Impact 5: CaMeL "made the agent safe", and one defence becomes "the defences that work"

> "The defences that work run the same way. One research team built ..." · "It made the agent safe without making
> the model any harder to fool."

**The problem.** One study is introduced as a class ("the defences that work"). And "safe" generalises beyond
what brief 13 records: a layer securing it against prompt injection "even when underlying models are susceptible",
on the tasks tested, at a cost.

**Fix.** "One defence that works runs the same way." And "It protected the agent against those attacks without
making the model any harder to fool." The second half of that sentence is the essay's best line in the section;
keep it.

### 13. Impact 5: two counter-arguments the brief supplies are left out

**The problem.** Brief 13 hands the essay two fair objections and how to answer them, and the essay uses neither:

- **The vendors key their own safety rules to capability** (6.4: Anthropic's RSP, OpenAI's Preparedness
  Framework). A reader who knows this will think the essay contradicts the companies. The brief's answer is
  ready: those frameworks address catastrophic misuse, a different risk from an agent misusing *your* access.
- **Some researchers count capability inside the definition of an agent** (3.14: Kasirzadeh & Gabriel's four
  dimensions include "efficacy" alongside autonomy). The essay's "None of these working definitions mentions
  intelligence" is true of the definitions chosen, and a critic will say they were chosen for that.

Both concessions strengthen the essay: they show the author saw the objection and that the answer fits the
ceiling argument ("capability is a dial, not the definition").

**Fix.** One sentence each, in "A smarter model isn't a safer one" and "Two meanings", within what the brief says
(abstract-level for 3.14; page-read for 6.4).

### 14. Impact 5: a paraphrase in quotation marks

> "one setting runs the same model anywhere from 'asks before each new kind of action' to 'asks about nothing'"

**The problem.** These read as the vendor's words. They aren't: brief 13 records the page's mode as "Prompts for
permission on first use of each tool". In an essay whose authority rests on quoting sources exactly, a made-up
quotation (even a fair paraphrase) is a trust risk if any reader opens the link. The drafter flagged it for the
cite-check; I'd fix it before.

**Fix.** Drop the quotation marks, or use the page's words for the first end ("prompts for permission on first
use of each tool").

### 15. Impact 4: "the companies'" generalises from one company

> "Through the companies' developer access, the model remembers nothing from one request to the next" · "The chat
> app adds standing instructions of its own"

**The problem.** Every source in this paragraph is Anthropic's documentation of Anthropic's products. The
paragraph opens with "Claude" or "ChatGPT", then says "the companies'" plural. The brief supports this for
Anthropic only.

**Fix.** "Through Anthropic's developer access ..." and "Claude's chat app ...". The point (the product, not the
model, supplies memory and standing instructions) survives intact on one well-documented example.

### 16. Impact 4: Lynch: "sometimes" undersells, the link to capability is implicit, and the vendor is unnamed

> "leading models from several companies sometimes chose harmful actions, such as blackmail"

**The problem.** Three small things, in both directions. (a) Brief 13 records 96% of runs in one scenario for two
models; "sometimes" will be read as rare. "In one scenario, most of the time" is accurate, and the essay already
carries the contrived-setting caveat that keeps it fair. (b) The essay uses Lynch as its evidence that capability
matters but doesn't say why: the brief's reading is that this kind of scheming takes some sophistication. Without
that clause the reader can't see why blackmail is a capability point. (c) The reassuring caveat ("not seen
evidence ... in real deployments") is from Anthropic, whose models were among those tested and whose model helped
write the essay. The notes disclose company research in general; this is the one place where the body should say
whose research it is.

**Fix.** One clause each.

### 17. Impact 4: from tools that misreported to "an agent saying it finished"

> "I've had tools tell me a job succeeded when it hadn't happened at all. ... An agent saying it finished a step
> is not evidence the step happened."

**The problem.** The experience is of tools; the conclusion is about agents. The bridge is good, and it is
stronger stated: if plain tools can report "done" falsely, an agent's "done" deserves the same check. "Not
evidence" also overstates: a report is weak evidence, not none. (No figure asked for, per brief §4.)

**Fix.** "is not proof the step happened", and one bridging clause from tools to agents.

### 18. Impact 4: "your assistant" collapses the contrast it draws

> "A sentence hidden in an email won't usually turn your assistant against you; it can turn an agent."

**The problem.** In this essay "assistant" means the AI assistant (the "By 'it'" paragraph). Here it means a
human assistant, so the sentence can be read as contrasting an AI with itself.

**Fix.** "your human assistant" or "a person working for you".

### 19. Impact 3: Jensen & Meckling paraphrases the unconfirmed sentence

> "Economists built a whole theory on the fact that someone acting for you won't always act in your interests,
> whoever they are"

**The problem.** The drafter paraphrased rather than quoted because brief 13 says the second sentence of the
definition is unconfirmed. A paraphrase still relies on it, and "whoever they are" is the brief's own reading
([ours]). This is for the cite-check, but the argument doesn't need the unconfirmed half: the confirmed
definition ("delegating some decision making authority to the agent") already makes the delegation point.

**Fix.** Ground the sentence on the confirmed definition, or confirm the second sentence against the page before
publication.

### 20. Impact 3: "the security field has built its thinking about agents on it"

**The problem.** A broad statement about a whole field, supported by OWASP, Willison and Greshake.

**Fix.** "much of the security thinking about agents starts from it".

---

## Verdicts on my §6 flags

- **Flag 2 (two meanings of "agent"): needs a fix before it ships.** The distinction is the right one, and
  placing it as the second section is right. The correction misquotes essay 03 and blames essay 03 for the
  overview's phrase (finding 1); the working definition then contradicts its own source (finding 4). Fair to
  essay 03 once it quotes essay 03's actual words, and fairer still if it says the series used the word two
  ways, which essay 03 really did.
- **Flag 4 ("a smarter model isn't a safer one"): slightly stronger than the evidence in the title and
  position; sound in the section body except "says no".** The evidence covers being fooled by an attacker, not
  plain mistakes (finding 3). The Lynch concession is handled fairly, though it needs its capability link stated
  (finding 16). "Ceiling" versus "how much of it it reaches" holds, and is the essay's strongest idea, provided
  the ceiling is what the setup enforces (finding 6) and autonomy is kept as a separate dial, not part of the
  ceiling (finding 10). NIST is misplaced as a capability result (finding 11).
- **Flag 5 (the incident list): fair, hedged about right.** Fix the CEO misattribution (finding 8), restore
  "GitHub MCP" in the quote, drop "coding" from the GitHub agent, and frame "in each case" as the essay's reading.
  Not too much hedging: the "single reported cases, not rates" line is what earns the right to use them.
- **Flag 6 (the ask-first section and Green 2022): the stretch is honest and clear, but the quote is hardened.**
  Restore "evidence suggests" and stop the policy review "finding" something about people (finding 5).

## Is option 3 the right lead?

**Yes.** The reader's one rule ("ask what it can touch, not how smart it is") and steps 1 to 3 come straight out
of option 3, and the brief's security evidence backs it most. Options 1 and 2 are the right ground: 1 makes
"change the setup, change the worker" concrete, and 2 is needed in any version (the options page says so too).
Option 5 works as a section, as drafted. I would not move option 4 to the opening: "Compared to what?" sits well
where it is, after the reader knows what the risk is, and it is where step 6's earned-trust caveat (finding 9)
belongs. The one thing the lead costs is that the body takes about 700 words to reach the ceiling argument; the
opening paragraph's promise carries the reader through that, provided it no longer asserts "nearly always"
(finding 2).

## Strongest element

"It made the agent safe without making the model any harder to fool", together with the ceiling paragraph. That
is the essay's argument in two sentences, and with "safe" narrowed (finding 12) it is the line a reader will
remember and act on.

## Verdict

**Needs another round:** the position is right and earned in its core, but the self-misquote of essay 03, the
"nearly always" opening and the unscoped "safer" are load-bearing, and findings 4 to 6 change what the reader
takes away. All are fixable in clauses, not rewrites.
