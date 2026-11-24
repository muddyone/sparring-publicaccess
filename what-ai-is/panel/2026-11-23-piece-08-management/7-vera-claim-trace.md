# Vera Tukey: claim trace, essay 08 after revision, 2026-11-24

Lane: accuracy only. Bart approved the content on 2026-11-24, so this report does not touch style or argument.
I traced every sentence that changed between `f0bbef18` and HEAD (`e141f6f9`), and re-checked every number and
quote in the essay, against brief 14, brief 14b, and the three-source check with its addenda. Then I checked
the essay's references back to essays 02, 06 and 07.

**What shaped this, disclosed.** I added no sources. I read one cited source again at its own URL (Becker et
al., arXiv 2507.09089 v2 HTML, Table 1 and Appendix C.2.7) because the 11-24 addendum didn't cover a new claim
about quality. I also tried to open the FAA SAFO PDF, but it returned 403, so the FAA finding rests on the
three-source check's quotes. One finding (F9) relies on what I know of the paper's author list, not on the
briefs, and it is marked for confirmation. Impact is on a 1 to 10 scale.

**The cap limits packaging, never the message.** Cut only what shouldn't be said at any length. If something
needs more room, add a numbered part.

---

## Findings

### F1 (Impact 5). Becker: the source did look at quality, and saw no difference

> "The study measured time, not the quality of the finished work, so the extra time may have bought something;
> it doesn't say."

- **Problem.** The paper addresses this directly. Table 1 lists the factor "Low quality initial pull requests"
  with the evidence "Qualitatively similar PR quality between conditions". Appendix C.2.7 found no sign that the
  AI-allowed PRs were lower quality. Post-review fix time was 9 minutes without AI and 15 with it, a difference
  that was not significant. The check was qualitative and partly self-reported, so "measured time, not quality"
  is fair as far as formal measurement goes. But "it doesn't say" is wrong, because the authors do say, and what
  they say cuts against "the extra time may have bought something".
- **Corrected wording (keeps the "no claim about value" intent of 8805eccd).** "The study measured time and
  didn't formally grade the finished work, though the researchers saw no sign that its quality differed either
  way."
- **Same paragraph, minor.** "smaller or unfamiliar projects". The source says "small greenfield projects or
  development in unfamiliar codebases". Use "small new projects or unfamiliar code".

### F2 (Impact 5). FAA: an advisory has become an order

> "Aviation didn't leave hand-flying to pilots' good intentions; the regulator told airlines to schedule it."

- **Problem.** A SAFO is a safety *alert*, not a rule. The source wording is "This SAFO **encourages** operators
  to promote manual flight operations **when appropriate**." The essay's own earlier sentence gets it right
  ("urged airlines … 'when appropriate'"). This new sentence turns that into "told … to schedule it".
- **Corrected wording.** "Aviation didn't leave hand-flying to pilots' good intentions; the regulator urged
  airlines to build it into their operations."

### F3 (Impact 4). Hembree & Dessart: "cost children the skill" is stronger than the source

> "Leaned on heavily at the age the skill was being formed, it cost children the skill."

- **Problem.** The source wording (14b 6.4) is "Sustained calculator use in Grade 4 **appears to hinder the
  development** of basic skills in average students." That describes a hedged slowing, not a loss. The essay's
  earlier sentence ("held them back") is accurate. This new one is not.
- **Corrected wording.** "Leaned on heavily at the age the skill was being formed, it held children back in that
  skill."

### F4 (Impact 4). Canaries: the essay names a comparison group the source doesn't give

> "employment for 22-to-25-year-olds in the jobs most exposed to AI falling 13% relative to more experienced
> workers in the same jobs"

- **Problem.** Brief 14 3.5 has a "13 percent relative decline in employment" and, as a separate point, says
  more experienced workers in the same occupations "were stable or growing". It doesn't say the 13% is measured
  against them. As I understand the paper, the comparison is with the least-exposed jobs, after controlling for
  firm-level shocks. In round 1 I said "don't invent [a group]". The fix that went in named one.
- **Corrected wording.** "…shows employment for 22-to-25-year-olds in the jobs most exposed to AI falling 13% in
  relative terms, while more experienced workers in the same jobs held steady or grew."

### F5 (Impact 3). Wiles: "check less" and "trust" are the essay's gloss, and the subgroup drops out

> "One study suggests that picture makes people check less."
> "thinking of the AI as a colleague seems to bring a colleague's trust with it"

- **Problem.** What was measured is errors caught, and only among managers whose organisations put AI on the
  org chart. Average effects were "small". Trust was not measured. What the authors report is that the label
  "shifts perceived accountability toward the AI system". The paragraph that follows supplies the subgroup, so
  the first sentence only needs to stop claiming the general case. "Seems" and "In this essay's terms" already
  flag the trust line as Bart's reading. It would be accurate to point to what the study actually found.
- **Corrected wording.** "One study suggests that picture can make people catch fewer errors." Optionally: "…seems
  to bring a colleague's trust with it (the study found responsibility shifting toward the AI), and trust is
  what lets you check less."

### F6 (Impact 3). Shen & Tamkin: "learning on the job" describes a lab task as workplace learning

> "A smaller study found the same in adults learning on the job: software developers learning a new code
> library"

- **Problem.** The participants were working developers, but they learned the library in a short study task,
  not in their jobs. Brief 14 1.2 says they were measured "shortly after the coding task".
- **Corrected wording.** "A smaller study found the same in working adults: software developers learning a new
  code library…"

### F7 (Impact 2). Shen & Tamkin: two small overstatements

- > "the time saved was too small to count"

  The source says about two minutes faster, "not statistically significant". The time saved wasn't too small to
  count. It was too small to tell apart from chance. **Corrected wording:** "the time saved was too small to be
  sure it was real."
- > "the same study found that how they used the AI mattered: those who asked it to explain … kept most of their
  > learning."

  The usage groups had 2 to 7 people each, and the authors say the analysis "does not draw a causal link". The
  essay states this caveat later (l.365) but not here. **Corrected wording:** "…the same study suggested that how
  they used the AI mattered…"

### F8 (Impact 2). METR: "many developers"

> "many developers no longer wanted to do half their work without AI, so they wouldn't sign up"

- **Source wording.** "an increased share of developers say they would not want to do 50% of their work without
  AI". That supports a rising share, not "many". **Corrected wording:** "more and more developers no longer wanted
  to…"

### F9 (Impact 3, confirm before changing). Notes: the vendor count may still be one short

> "Three of the studies I rely on come from AI companies or AI consultants"

- **Problem.** The essay also relies on Dell'Acqua et al. 2023 (the 758 consultants). To my knowledge, that
  study was run with BCG, and its author list (Candelon, Krayer) includes BCG people. The briefs don't record
  affiliations for it, so check the paper's author notes first.
- **Corrected wording, if confirmed.** "Four of the studies I rely on come from AI companies or AI consultants:
  the coding study (Anthropic), the survey of knowledge workers (Microsoft), and the 'AI employee' and consultants
  studies (authors at BCG)."

### F10 (Impact 2). Artz and Goodall: "look at records" doesn't fit a survey

> "Both studies look at records rather than running tests"

- **Problem.** Artz et al. use worker surveys (NLSY, Working in Britain), and Goodall & Pogrebna use team
  records.
- **Corrected wording.** "Both studies observe rather than test…", or "Both studies look at surveys and records
  rather than running tests…"

### F11 (Impact 2). Essay 07 consistency: "agent"

> "As AI starts carrying out whole jobs on its own, the kind the last essay called an agent"

- **Problem.** Essay 07 defines an agent as "an AI you've let act for you" (l.7, l.82). Its examples are single
  actions: send the email, pay the bill. "Whole jobs" isn't wrong, but it isn't the definition the essay points
  back to.
- **Corrected wording.** "As AI starts acting for you, carrying out whole jobs on its own, what the last essay
  called an agent, the move gets bigger…"

### F12 (Impact 1). Notes: the date

> "Drafted and reviewed on 23 November 2026."

- **Problem.** The revisions and the Becker addendum are dated 24 November.
- **Corrected wording.** "Drafted and reviewed on 23 and 24 November 2026."

---

## Traced and clean

These match their sources or their marks, and need no change:

- **Calculator and history.** The calculator bridge ("more than two thousand years later"). "So both sides had a
  point…". "Used alongside ordinary teaching … a fair trade" (Hembree: "improved").
- **Kosmyna block.** 18 people, unreviewed, the authors' word list verbatim against the project page, Stanković
  "posted a comment".
- **Specialists and Bastani.** The specialists' checks (Bart's). "AI fits the first half". Bastani's 48% "higher
  than those of students without it" and 17% (abstract, verified). "Those were children" (high-school students;
  acceptable).
- **Coding study.** Shen & Tamkin "finished faster" (abstract: "some productivity improvements") and "paid for
  the speed in learning" ("at the cost of learning the library"). The quote is verbatim. 50% and 67%. The skills
  missed (code reading, debugging).
- **Lehmann.** Null overall, exploratory status stated, "seemed to matter".
- **Budzyń.** "about 28" and "about 22", "compared records from before and after", "three letters in response".
- **Bainbridge and decay.** "People who study automation saw this coming". Arthur (cognitive tasks "more
  susceptible"). Casner.
- **First trap.** The "done" report (Bart's). "Points the same way, though it measures something nearby". Artz's
  proxy. Benson "not always the best". Watkins verbatim against IMD. Dell'Acqua "19 fewer correct answers in every
  100". Leyden & Scur "are worth checking" and the checking skill.
- **Becker numbers.** 24%, about 20%, 19% longer, all now on the time scale. The causes (§3.3, §4.1: familiarity,
  large repositories of more than 1.1 million lines and about 10 years, under 44% of suggestions accepted, major
  clean-ups). "Don't name one cause".
- **Becker meaning.** "Misjudged … in the wrong direction" fits the brief's "wrong by a wide margin". METR "harder
  to trust" fits "likely a bad proxy".
- **Lee, Brynjolfsson, Beane.** Lee et al. "stewardship" (source: "task stewardship"). Brynjolfsson, Li &
  Raymond: "three months", "rare and not necessarily random", "noisy". Beane: "fewer of them become experts" fits
  "a decreasing supply of experts relative to demand", and "that shows it can happen" stays inside the brief's
  "the mechanism exists".
- **Care section.** Köbis verbatim, "far less likely".
- **Advice and close.** Step 4 quotes Bainbridge verbatim. "Most of us won't…" and the exercise line are Bart's
  analogy and assert no researched figure. Bastani "without asking students for discipline" is a fair reading
  of a tutor built with safeguards. Niedner "future review". Limits ("four months"). The close: "Nothing I found
  shows a general decline", "far more of it stays with you".
- **Bart's first-hand passages.** Lettering, structural engineering, reading glasses, "I know I won't", the
  "done" report and the Resolver paper are his. None asserts a researched fact. "CAD hadn't yet taken over" is
  period memory, and that's acceptable.
- **Essay 06.** "Sounds just as sure when it's wrong as when it's right" matches 06 l.93 ("sounds the same").
- **Essay 02.** The care section ("they grow into the job … An AI gives you less of that") no longer contradicts
  02's claim that an AI with memory learns. The conflicting line was removed in 60bd009f.

## Verdict

**Fix then publish.** F1 to F4 are real accuracy problems: one claim the source contradicts, one advisory
turned into an order, one hedge dropped, and one comparison group invented. Each is a one-sentence swap. F5 to
F12 are small. F9 needs the Dell'Acqua author notes checked before the line is changed. No figure in the essay
is wrong.
