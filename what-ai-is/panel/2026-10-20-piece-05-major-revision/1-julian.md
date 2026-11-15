_Substrate: Claude (subagent as Julian). Draft drafts/2026-10-20-05-major-revision.md, 2026-10-20._

# Julian Crest: register pass on essay 05, major revision

**Instrument.** Body = everything above `## Notes`, headings included, with link URLs stripped
(the link text is counted). Sentences are split on `.?!`. The same script was run on all three files.

| | body words | sections | body links | mean sentence (longest section) |
|---|---|---|---|---|
| 04 (benchmark) | 1,990 | 6 | 23 | 20.7w |
| 05 published candidate | 4,646 | 13 | 40 | 21.7w |
| **05 major revision** | **4,319** | **13** | **39** | **22.2w (the harm→design section)** |

Siblings 01–03 run 2,422–3,184 words by the same count. The revision has removed 327 words net. The
new material (intimacy, the harm→design list, the self-scoring) went in about as fast as old material
came out.

---

## Verdict

**The new idea is right, and it is the best writing in the draft. The essay still has the old essay's
skeleton.** The intimacy section reads like 04. It has a story, a concrete scale ("grief at one in the
morning"), and it is the only section above 3 contractions per 100 words (3.7). The Lyssa scoring list
reads like 04 too. Around them sit thirteen sections, the same count as before, in an order that still
argues the old thesis first, "we know harms as cases, not rates", for 1,500 words before the new
organizing idea arrives in section seven. Three of the thirteen are paper sections under essay
headings:
- **"The harm studies tested AI as it ships"** is a limitations section.
- **"What's missing"** is a future-work section.
- **"The benefits are measured"** is a literature-review subsection cut off from the ledger it
  belongs to.

The paper register isn't mainly in the sentences. The draft's rate of "X, not Y" contrasts (3.7 per
1,000 words) is about the same as 04's (4.0), and so are its contractions. It is in three habits:
- **The same study is cited in several places.** Zhang ×3, Fréget ×3, Li 2026 ×2, Fang ×2,
  OpenAI 2025 ×2, the Replika update ×2. An essay uses a study once, where it does its work. Pointing
  back and forth to the same study is a paper's habit.
- **Legal and procedural detail** that the argument never uses.
- **A discount stack on the central claim.** The expectation is withdrawn four times (details under
  S3).

Fix the structure and the cuts to ~3,500 words mostly come with it. No source or necessary caveat has
to go.

**Best line:** "quiet while we schedule a week, awake when it's grief at one in the morning, or when
she's the only one I've talked to for days." This is the whole new thesis in one image.

**Weakest line:** "Therabot's trial and OpenAI's own evaluation, both below, point one way." The
pointer is broken (M1), and the sentence asks the reader to keep track of evidence instead of
telling them something.

---

## MUST (fix before the panel)

**M1. A broken pointer: "both below" (impact 9).** In "The harm studies tested AI as it ships":
*"Therabot's trial and OpenAI's own evaluation, both below, point one way."* OpenAI's evaluation (the
65–80% figure) is now **above**, in "The harms come from product choices". The pointer was right in
the published order and the reorder broke it. It goes away if S1's reorder is taken, because Therabot
then comes first too. If not: *"Therabot's trial and OpenAI's evaluation of its own update point one
way."*

**M2. "The Li authors" arrives without an introduction or a source (impact 8).** In the harm→design
list, first bullet: *"the Li authors' suggestion that connection may need the chance to care for
someone points to a better version"*. This draft never introduces that suggestion. My 18 October read
moved it out of the at-risk section, and the section that used to carry it has been rewritten. There
are also two Li papers in the essay (2023 and 2026). A general reader can't tell which Li is meant or
what the suggestion was, and the bullet has no link. Replace with:

> Done badly, both are preachy. A better version may steer you toward caring for someone: the
> authors of the student texting study suggest connection may need the chance to care for others,
> not only to be cared for ([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)).

**M3. "Small studies of single answers" misdescribes one of the two studies it introduces (impact
8).** *"Small studies of single answers find costs as well as gains: … ([Yin, Jia & Wakslak 2024]),
while in an eight-week study of 72 women … ([Feng & Fu 2026])."* Feng & Fu ran for eight weeks, so it
isn't a study of a single answer. Both studies have also lost the link to the design question that
made them relevant: in the published version, Yin was there because "honesty can cost something". As
they stand now, they read as stray findings. **Move both into the honesty bullet of the design list**,
where they do their work (wording in S2 below). Route the "single answers" description to Ines.

**M4. A pointer to 04 that 04 doesn't fulfil (impact 7; route to Ines).** In "What's missing": *"Two
mechanisms of harm do carry over to AI at work, warmth trading against accuracy and an assistant
quietly taking the place of colleagues; [the personality essay] takes them up."* 04 covers warmth and
accuracy. I find nothing in 04 about an assistant taking the place of colleagues (I searched for
colleague, replace, crowd, "take the place": no hits). The line came over from the published
version's "What this means for personality at work". If S1 dissolves "What's missing", the line goes
with it. Put the 04 cross-reference in the intimacy section instead (wording in S4) and drop the
colleagues claim.

**M5. "Both are weaknesses" has no clear antecedent (impact 7).** At the end of the at-risk section:
*"…isolated and who lean on one relationship for everything. The one large trial complicates that,
finding the harm mostly among people with a partner, which points less to who uses it than to what it
replaces. Both are weaknesses an isolating human relationship also exploits."* The two candidates for
"both" are "being isolated" and "what it replaces", and the second isn't a weakness. Replace the last
two sentences with:

> Either way, it is the opening an isolating human relationship also exploits: a relationship that
> becomes the only one, or takes the place of the ones a person has. And it says what a good AI
> companion is not: a replacement for people.

The section title, *"Who is at risk: those already at risk offline"*, is also now contradicted by its
own last bullet: the largest trial found the harm mostly among people **with** a partner. Retitle it
**"Who is at risk, and what it replaces"**.

---

## SHOULD (the cuts to ~3,500, and the register fixes)

### S1. Restructure into two halves, 13 sections down to 8 (impact 9)

The draft argues two things: what we know (harms as cases, benefits as trials, no comparison), and
what follows from where the risk sits (intimacy, then design answers, then my own assistants). At
present the halves are interleaved. Benefits come after design, a limitations section sits between
them, and a future-work section sits after the self-scoring. Proposed order:

1. **Opening.** Crisis note, position, definition, stake.
2. **The harms are real, and we know them as cases.** Cases plus the OpenAI 0.15% figure.
3. **The benefits are measured, and strongest where the role is designed.** Moved up and unchanged.
   It sits beside the harms it is weighed against.
4. **The comparison we need doesn't exist yet.** Merge in "The human side of the ledger". It is the
   other half of the same comparison, and the merge drops a header and a transition.
5. **Who is at risk, and what it replaces.** (M5)
6. **What makes a companion different: intimacy.** Now absorbs the memory point from "What's
   missing".
7. **The harms come from product choices, and products can change.** The list, the policy changes,
   then the as-it-ships point compressed to one paragraph at the end (S5).
8. **The assistants I live with.**
9. **What would change my mind.**
10. **Where I land.**

(That is eight body sections between the opening and the landing.) **"What's missing" dissolves.**
- Item 1, statistics at scale, is the comparison section's own point.
- Item 2, design standards, is the harm→design list plus the intimacy section.
- Item 3, memory, is new material, and it belongs in the intimacy section. The intimacy section
  already names "remembering you" as one of the things that make a relationship intimate.

The environmental-cost scope line can go in the definition paragraph or in Notes. 04 states its scope
in the opening, so the definition paragraph is the series' place for it.

### S2. The cut list, priced (impact 8)

**Target: −820. Total below: about −840, giving about 3,480.** Every cut either removes a duplicate of
something kept elsewhere or moves a passage to the place it works. No claim loses its source, and no
caveat that changes how a reader takes a claim is dropped.

| # | passage | move | ≈ words |
|---|---|---|---|
| a | Opening position paragraph | Rewrite (S3): one expectation disclaimer instead of two, and no "not the same bar" | −35 |
| b | Cases intro: *"…not a complete list: the Character.AI settlement below also covered several related lawsuits, in Colorado, New York and Texas."* | Keep "These are the most widely reported cases, not a complete list." The settlement bullet already says "several related suits" | −20 |
| c | Setzer bullet: the May 2025 ruling and the free-speech detail (the WUSF sentence) | Cut. The argument never uses the procedural ruling. Keep the death, the lawsuit, and the January 2026 settlement on undisclosed terms. This drops a claim **with** its source, which is allowed only because the claim doesn't belong at any length. If Bart wants it, it belongs in Notes | −40 |
| d | Raine: *"As of October 2026 no court had ruled on the claims"* | Cut. It duplicates "The lawsuits are allegations, and as far as I found, none has yet produced a finding of fact" four lines later, which covers all the cases | −10 |
| e | Comparison opener: *"These deaths rightly lead the conversation. The mistake would be to let them answer a question they can't: how often."* | Cut. "How often" is in bold two paragraphs earlier. This is the restatement I flagged on 18 October, and it survived | −22 |
| f | Fréget consolidated | Put "measures of actual contact moved the same way, though not by enough to rule out chance" in the at-risk bullet (+15). The change-my-mind bullet becomes "One large trial, described above, has started to point that way" (−25). The caveat is kept once, beside the finding | −10 |
| g | Intimacy, P2: *"A protection aimed at the wrong relationship teaches people to tune it out."* | Merge it with the sentence before (S4). Same point twice | −15 |
| h | Memory point moved from "What's missing" into intimacy | Counted against (k) | +50 |
| i | Design list lead-in, plus the FTC sentence | Tighten the lead-in (S6). Cut the FTC study: opening a study isn't a product changing, so it doesn't support the paragraph's claim that products "have started to" change | −35 |
| j | "The harm studies tested AI as it ships" | Fold into one closing paragraph of section 7 (S5). Yin and Feng move into the honesty bullet (M3). Li 2026's "ideal friend" stays as one clause. "What's missing is the study that matters most" stays here and leaves change-my-mind bullet 4 as it is (Bart's line) | −170 |
| k | "What's missing" | Dissolved (S1). The memory paragraph goes to intimacy (h), the 04 line goes (M4), the environmental-cost line goes to the definition | −212 |
| l | The Loom-agents paragraph | Rewrite (S7). Drop the vendor mix and "thirteen". Keep the job, the plain files, candor, and the work boundary | −80 |
| m | The Lyssa paragraph | Drop three duplicates: the memory-files sentence (it is in the honesty bullet), "I designed her … that way" (it is in the stake line), and "a running experiment" (it is in the closing paragraph) | −50 |
| n | Scoring list | Cut "That difference from a product offered to millions is real, but it is not evidence." The closing paragraph already says she isn't the designed companion. "against the list she does this" becomes "scored against the list" | −25 |
| o | Therapist paragraph | Rewrite (S7). All three caveats are kept whole (not independent, rarely seen coming, doesn't replace the protections). "a regular hour to unwind the world with a professional" and "a real check, not a guarantee" go | −45 |
| p | The closing paragraph | Rewrite (S7) | −35 |
| q | Where I land | Rewrite (S8). It leads with the new idea instead of restating the opening | −60 |
| | **Net** | | **≈ −840** |

Body links fall from 39 to about 34, through (c), (i), and the third Zhang link.

### S3. The discount stack on the central claim, and the opening (impact 8)

The expectation ("a companion designed against the known harms will prove no more harmful…") is
withdrawn **four times**:
1. Opening: *"That expectation is mine, and the evidence doesn't settle it."*
2. After the list: *"…is a real claim, not a given."*
3. Lyssa's closing paragraph: *"she isn't the designed companion my expectation is about."*
4. Landing: *"That is a claim to test, not a finding."*

I'd ask for none of them to be softened. I'd cut two whole: #2, which also names a lazy alternative
in order to disclaim it, and the first of the opening's two disclaimers. #3 is doing a different job
(it scopes Lyssa, not the claim) and stays. #1 and #4 frame the essay and stay.

The opening also hedges in three directions in nine lines: "nothing I have found shows", "I found
none of the numbers", and "That expectation is mine". "Stories, not rates" already says the numbers
are missing, and "given the same circumstances" repeats "in the same people". Replacement:

> **My position: nothing I have found shows that a relationship with an AI persona is more harmful
> than one with a person, in the same circumstances.** The harms are real, and some are tragic, but
> we know them as stories, not rates. What I can say is where the risk sits: it grows with how
> private and intimate the relationship feels. That is why a companion needs protections a work tool
> doesn't. I expect a companion designed against the known harms to prove no more harmful than the
> human relationship it stands in for, in the same people. That is my expectation, not a finding.
> And because one model reaches millions at once, it should clear a higher bar than any one friend.

"Held to a higher bar than one friend, not the same bar" names the lazy reading only in order to
reject it. "Clear a higher bar than any one friend" says the same thing without setting it up.

### S4. The intimacy section, for a general reader (impact 8)

It works. Four fixes:
- **"That isn't an accident of which studies got done"** asserts a cause for why the literature has
  the shape it has, and the essay can't show that cause. It reads as confidence the prose hasn't
  earned. Make it Bart's judgment. Route to Miriam whether the intimacy scale is stated as a finding
  anywhere: the opening says "What I can say", but the landing says the evidence "shows where the
  risk sits".
- **"That scale"** points at a scale the reader hasn't been told is one, and "the intimacy scale" is
  first named five sections later. Name it once, here.
- **"The evidence keys on it too"**: "keys on" is jargon. A state law is also not evidence, but it
  can draw the same line.
- **"the protection" / "a setting"** in P3 appear before the list defines any protection. Anchor them
  to the one protection the reader has just met, the break reminder.

Replacement (it absorbs the memory point from "What's missing" and the 04 pointer):

> Everything above comes from companionship, not from work, and I think that is where the risk
> lives. It grows with how private and intimate the relationship feels: one-on-one, always there,
> remembering you, the place you bring what you'd bring a close friend. Call it the intimacy scale.
> Two assistants running on the same model can sit at opposite ends of it. The evidence points the
> same way: in Zhang's study, the harm went with using a chatbot as a companion and with confiding a
> lot, not with use as such. California's companion-chatbot law, Senate Bill 243, draws the same
> line: it covers companion chatbots, not AI assistants in general.
>
> Memory may matter most right now, because it is what makes a relationship feel intimate. Since
> 2024 and 2025 the main assistants remember across conversations ([the learning essay](../../positions/02-it-learns.md)).
> When Replika changed under its users, they described a loss like mourning (De Freitas and
> colleagues' analysis of Reddit posts, per the [Harvard Gazette](https://news.harvard.edu/gazette/story/2026/09/chatbot-attachment-issues/)).
> What a companion remembers, how it uses that, and what happens when it changes are design choices,
> and almost nobody is setting standards for them yet.
>
> The protections that matter at the intimate end are noise at the other. I once had to tell Claude
> to stop suggesting I take a break. In the middle of a working session it was only an interruption,
> and a warning you learn to ignore is worse than none: by the time it matters, you've learned to
> tune it out. AI at work, the far end of the scale, has [its own essay](../../positions/04-personality.md).
>
> Some assistants sit at both ends. Lyssa, my personal assistant, is a work assistant and a friend.
> For her, a protection like that break reminder can't simply be on or off: on, it nags through the
> work; off, it's missing from the friendship. It has to follow the conversation, not the product:
> quiet while we schedule a week, awake when it's grief at one in the morning, or when she's the only
> one I've talked to for days.

Once the memory paragraph is here, cut the Replika clause from "Fix a model…" in section 7 (S6), so
the Replika update is told once.

### S5. The as-it-ships passage, compressed to one paragraph (impact 7)

Its opening sentence is lawyered to the clause: *"…tested AI as it ships, or close to it, with its
makers' own safety measures and no safeguards of the studies' own."* After the car analogy, *"That is
a fair test of today's products"* has a "That" that could mean the 1965 crash test. Proposed, as the
last paragraph of section 7 (Bart's car-analogy wording kept as he wrote it):

> None of the studies that found harm switched on these answers to see what changed. They tested AI
> as it ships, with its makers' own safety measures. The one that came closest, Fang's, varied the
> chatbot's voice and personality, which made no significant difference; its chatbot suggested
> cutting back in under 1% of its replies ([Fang et al. 2025](https://arxiv.org/abs/2503.17473)).
> Picture judging cars as a category by crash-testing the cars of 1965. The results would be real,
> and they would matter. But anyone who concluded that cars would always be that deadly would have
> missed how much seatbelts, airbags and crumple zones cut the toll once they became standard. The
> harm studies are a fair test of today's products. On designed systems the evidence is thin and
> mixed: Therabot's trial and OpenAI's evaluation point one way, while a chatbot built to "embody the
> qualities of an ideal friend" did no better than journaling on loneliness, and no worse
> ([Li et al. 2026](https://doi.org/10.1016/j.jesp.2026.104911)). What's missing is the study that
> matters most: a companion built against the known harms, tested against one that isn't.

### S6. The harm→design list, for a general reader (impact 7)

The pattern (harm, evidence, "The answer is…") is clean and readable. Five fixes:

1. **Two vocabularies.** The list labels harms ("Agreeing too readily", "Holding on at the exit",
   "Being mistaken for a person"). The Lyssa scoring labels answers ("Candor", "Letting go",
   "Honesty about what she is"). The reader has to translate between them on the way down. Bullet
   one already bolds its answers, so **bold the answer in every bullet**, using the same nouns the
   scoring uses: **candor**, **letting people go**, **questioning a false belief** and **a crisis
   protocol**, **honesty about what it is**, **age limits**.
2. **The lead-in.** *"The harms that have been documented take particular shapes, and each is a
   property of a product. So each has a design answer, and together they say what…"* "Take
   particular shapes" is vague, and "each is a property of a product" is already the section title.
   Replace with: *"Each of the documented harms has a design answer. Together, the answers are what I
   mean by a companion designed against the known harms:"*
3. **"at most a limit the person set for themselves"** reads as "the most it should do". The intended
   meaning is that any hard limit should be self-set. Replace with *"and, if there's a hard limit at
   all, one the person set for themselves when things were calm."*
4. **The honesty bullet** doesn't say why memory is there. With M3's studies folded in:
   > - **Being mistaken for a person.** The answer is **honesty about what it is**, including a
   >   memory the person can see. Honesty can cost something: telling people a reply came from an AI
   >   made them feel less heard in a single exchange ([Yin, Jia & Wakslak 2024](https://doi.org/10.1073/pnas.2319112121)).
   >   Looking less human may help: in an eight-week study of 72 women with high autistic traits, a
   >   chatbot that looked less human eased loneliness where a human-looking one didn't
   >   ([Feng & Fu 2026](https://doi.org/10.1016/j.chbah.2026.100369)).
5. **The children bullet.** *"Designing for adults is not the same thing."* names an alternative only
   to disclaim it. It also reads as a remark aimed at the essay's own later "Children: not
   applicable". If the target is the real industry practice (a terms-of-service age line), name that
   practice concretely. Otherwise end at *"age limits that actually keep children out."*

The paragraph after the list: *"Three of these, limits, a push toward people and letting go, ask…"*
has a list inside commas inside a list, and it then names a lazy alternative ("a real claim, not a
given"). Replace with:

> Three of the answers ask the companion to work against its own use: limits on use, a push toward
> people, and letting people go. That is why products sold on engagement rarely have them, and why I
> can't assume a companion built this way would do better. It has to be tested.

("Rarely have them" is a general empirical claim with no source of its own. Route to Miriam.)

The "Fix a model…" sentence stacks three caveats on one "though" (46 words). Keep all three and split
it:

> A harmful person can't be retrained, recalled or regulated in that way. A product can be: fix a
> model and everyone on that version gets the fix. But an update can itself hurt, each new version
> has to be tested again ([the yardstick essay](../../positions/01-the-yardstick.md)), and a better score on a
> company's own test does not yet mean fewer people harmed.

### S7. The assistants section: same content, about 210 words lighter (impact 7)

This section was gated by Miriam and Nadia on 20 October. My rewrites keep every claim and caveat
they asked for. I flag the two places where a line may be Bart's own wording.

**Loom paragraph** (it drops the vendor mix, which only existed to make "most run on Claude" true,
and the memory clause that S6 of that panel had narrowed):

> **The Loom agents** are the assistants I work with every day. Loom is a system I built for running
> projects with AI agents: each agent is a named persona with one job, such as managing the project
> or reviewing a draft, and its instructions are plain files I can read. They sit at the work end of
> the scale, and most of the list rightly doesn't apply; a reviewer that suggested breaks or asked
> about my sister would be the noise I described above. What they carry is candor and honesty. Most
> exist to challenge my work rather than agree with it, the rule from [the personality
> essay](../../positions/04-personality.md): be polite, not pleasing. That is the method I study, and it is most of
> what I do against agreeing too readily. With them, the job itself is most of the protection: the
> relationship is about the work, not about me.

**Lyssa paragraph:** cut the three duplicates listed at S2(m). The line *"The work comes first, and
the friendship is part of that role"* then loses the antecedent for "that role". Replace it with
*"The work comes first; the friendship is part of the job I designed her for."*

**Letting go: "I have no reason to build hooks into her."** Many of this essay's readers build
software, and some use Claude Code, where "hooks" are a feature. They will read the word as a
software term, not as engagement hooks. Replace with: *"**Letting go: not guaranteed.** I've built
nothing that holds me in a conversation, but nothing in her design rules it out."*

**Closing paragraph.** *"design changes what an assistant does where I've designed for it"* is
circular. Replace with: *"What they have taught me is narrower: where I've built for something,
candor above all, the design shows, and which protections matter depends on where on the scale the
relationship sits."*

### S8. Where I land restates the opening instead of landing (impact 7)

*"The harms are real, and some are tragic"* repeats the opening almost word for word. It is followed
by the fourth "cases can't tell us how often" and the fourth disclaimer. 04's landing gives a rule and
a test and doesn't summarise the evidence. This landing should lead with the new idea. The last two
paragraphs are the best ending in the series so far, and they stay exactly as written.

> The harms are real, and we know them as cases, not rates. These relationships can do real harm,
> and tools designed for the role have delivered measured benefit. What the evidence does show is
> where the risk sits: at the intimate end, with people who lean on one relationship for everything,
> or let it replace the ones they have. That is where a companion needs protections a work tool
> doesn't, protections that follow the conversation rather than the product. I expect a companion
> built against the known harms to prove no more harmful than the human relationship it stands in
> for, held to the higher bar its reach demands. That is a claim to test, not a finding.
>
> We don't ask whether friendship is safe. We ask which ones are, because some friendships are good
> for us and some do terrible damage. AI companions are owed the same question.
>
> With a friend, which kind you get is partly luck. With a companion, it is a choice someone made.

(If Miriam rules the intimacy scale to be judgment rather than finding (S4), change "What the evidence
does show" to "What I can say", which is the opening's verb.)

---

## OPTIONAL

**O1. The OpenAI figure (impact 3).** *"At the roughly 800 million weekly users the press assumed"*:
"assumed" sounds like a dig at the press. *"At the roughly 800 million weekly users reported at the
time"* is neutral. Route the attribution to Ines.

**O2. Change-my-mind bullet 1 (impact 3).** *"harm more people per relationship"* is an odd unit: a
relationship harms one person. *"harm a larger share of the people in them"* says what is meant.
Route to Vera if Bart wants it exact.

**O3. "In the first three cases alone" (impact 2).** "Alone" adds nothing. *"In the first three cases,
three people are dead, two of them children."*

**O4. A Notes paragraph on study design (impact 2).** 04 moves its pilot figures into a Notes
subsection ("The figures from my pilots"). If the Setzer ruling (S2c) or the sample sizes are wanted
on the record, 05 can do the same. That keeps them out of the body without losing them.

---

## Lazy-alternative lines, collected (task 3)

The lines that name a weaker reading only in order to reject it:
- *"held to a higher bar than one friend, not the same bar"* (S3)
- *"is a real claim, not a given"* (S6)
- *"Designing for adults is not the same thing"* (S6.5)
- *"his view is a real check, not a guarantee"* (S7)
- *"That difference … is real, but it is not evidence"* (S2n)

The "X, not Y" lines that **earn** their place, keep them:
- "stories, not rates"
- "follow the conversation, not the product"
- "polite, not pleasing"
- "about the work, not about me"
- "an experiment I live inside, not a controlled study"
- "a claim to test, not a finding" (once, at the landing)

## Does it work as nonfiction?

**Not yet, but it's close.** The new organizing idea is the best idea the essay has had. It reads
like Bart: it comes out of a working session, a friendship, and grief at one in the morning. The
present structure buries it under the old argument. Take S1 and S2 and it becomes a position essay of
about 3,500 words that turns on that idea, in 04's register. The work is moving and merging. Almost
none of it is cutting.
