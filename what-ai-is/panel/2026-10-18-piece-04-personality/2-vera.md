_Substrate: Claude (subagent as Vera Tukey). Piece 04._

I'm Vera Tukey, reporting on piece 04 ("Personality improves the relationship, not the work. Both count.").

**Verdict**

The numbers are mostly reported correctly. The trouble is the inference. The piece puts four different null or adverse results under one claim, "does personality improve output? ... it's no." The evidence supports "it hasn't been shown to, and where it was measured, it didn't". Warmth even made answers worse in one study. Two of the four nulls didn't test personality as the piece defines it: one tested job-role personas, the other humanlike robot design. The other findings are smaller: details that fell out between the report and the piece, and one unchecked number (the Kaiser subscale figures) carrying a design rule.

I didn't look at any primary data. Everything here comes from reading the report, the briefs and the cite-check records, so treat it as provisional.

**Findings, ranked**

**1. "No" claims more than the studies show. Impact 8.**
Current: "So the question "does personality improve output?" has an answer, and it's no."
- The report's high-confidence list has only "Personas don't improve factual accuracy." Its Unknown list includes "Any field study of AI co-workers at work."
- The nulls are narrow. Roesler is robots, mostly single-session studies. Zheng is factual question answering. The Bickmore exercise trials had N=24 and N=26.
- Ibrahim isn't a null at all. Warmth *hurt* accuracy.
- The piece's own human evidence points the other way, and the piece leaves it out. In Van den Broeck, relatedness correlates with task performance at ρ = .26. Friend groups outperform acquaintance groups at d = .31 (Chung, in the report).

Restate: "So does personality improve the work? Nobody has shown that it does. Where it was measured (factual answers, robot tasks, exercise), it didn't help, and in one study warmth made answers worse. No one has yet tested it on real work over months."

**2. Zheng tested job-role personas, not personality. Impact 6.**
Current: "across 162 personas and four model families, personas in system prompts didn't improve factual accuracy"
- The personas were roles such as "you are a lawyer", tested on 2,410 factual questions. The brief says the effects were "largely random."
- That shows role prompts don't help on facts. It says nothing about warmth or humour.

Restate: "Prompts that give a model a role ('You are a lawyer'), 162 of them across four model families, didn't improve its accuracy on 2,410 factual questions."

**3. The Kaiser numbers are unchecked and carry a design rule. Impact 6.**
Current: "agreement on *what we're doing and why* predicted outcomes more than the emotional bond did ([Kaiser et al. 2021]; the subscale figures come from a secondary summary)."
- The figures in question: task r = .25, goal r = .19, bond r = .12. Brief 2 says "verify against the paper."
- Both cite-check judges failed to confirm the subscale claim. GPT marked it unchecked. Claude marked it verified, but only from its own knowledge.
- There are no confidence intervals, so we don't know that .25 and .12 really differ.
- Most of the interventions had human therapists guiding them, so it isn't clear the result carries over to fully automated assistants.
- Nadia found the parenthetical meaningless.
- The report rates this "Medium." Where I land, item 4, presents it as settled.

Restate: "In online therapy programmes, most of them guided by human therapists, the overall bond went with outcomes at about r = .20. A secondary summary, which we haven't checked against the paper, reports that agreement on tasks and goals mattered more than the emotional bond."

**4. "Reliably" goes past what the one cited study shows. Impact 5.**
Current: "With machines, personality reliably improves the relationship. ... want to keep using it, and in some studies this holds over weeks and months ([Bickmore & Picard 2005])."
- Liking is reliable in short studies. The report rates trust and intention to use as "Moderate" in short studies and "Weak" past a month.
- Bickmore & Picard is one month, N=101. The "months" come from the 2010 study, N=24.
- The cite-check's GPT judge flagged this sentence as "nuance": broader than the one study.

Restate: "Social cues reliably make people like an agent more. In one month-long trial (101 people), they also felt more bonded to it and said they wanted to continue."

**5. The exercise result is understated and has no sample sizes. Impact 5.**
Current: "relational features raised logins, enjoyment and the wish to continue, but not the exercise"
- The report says the more engaging version produced *less* walking, in two small studies (N=24 crossover, N=26).
- The 2005 trial (N=101) also found no exercise gain.

Restate: "...but not the exercise. In two small trials (24 and 26 older adults), the more engaging coach led to less walking."

**6. "Matters a great deal" turns correlations into a causal claim. Impact 4.**
Current: "Between people, connection at work matters a great deal."
- The bullets below it hedge properly ("goes with", "mostly self-report correlations"), but the heading undoes that.
- The ρ = .60 behind "a great deal" is relatedness with self-reported commitment. Both come from the same survey answers, which inflates the figure.
- On Ozcelik: "six weeks later" shows which came first. It doesn't rule out poor performance or poor approachability causing the loneliness. It is one field study, with 672 employees and partial mediation.

Restate the heading: "Between people, connection at work goes with a better working life." Restate the Ozcelik bullet: "In one field study of 672 employees, those who were lonely were rated lower by their supervisors six weeks later."

**7. Ibrahim's prompt-only result is missing a qualifier. Impact 4.**
Current: "Warmth set only by prompt produced smaller but similar effects"
- Brief 2 says "smaller and less consistent." This is the setting a persona set by prompt would actually use, so the qualifier matters.
- Leaving out the size is fine. If a size goes in, use the published abstract's 10–30 points across tasks. The ~7 / ~12 point averages come from the preprint, and the report says so.

Restate: "Warmth set only by prompt produced smaller, less consistent, but similar effects."

**8. Roesler: say what was null. Impact 3.**
Current: "a meta-analysis of 78 studies found no gain in task performance from humanlike design"
- Overall, humanlike design had a medium positive effect, mainly on how people perceived the robot.
- The task-performance null is at the lowest level of the analysis, across about 6,000 participants, mostly in single sessions.

Restate: "...humanlike design made people view robots more favourably, but showed no gain in task performance (78 studies, mostly single sessions)."

**9. Fang is a preprint, and that isn't said. Impact 3.**
Current: "the one month-long randomized trial that varied a chatbot's voice"
- The trial is fair as described. It had 981 people, and the piece doesn't say that or that the paper hasn't been peer-reviewed.

Restate: "the one month-long randomized trial (981 people, not yet peer-reviewed)..."

Cheng is reported accurately. Van den Broeck's 99 studies are accurately labelled as correlational in the bullet itself.

**What this means**

The thesis holds once it is narrowed. Two edits do most of the work:
- Change "it's no" to "not shown, and in places worse" (finding 1).
- Either check the Kaiser subscale figures against the paper or hedge Where I land, item 4, in the text (finding 3).

Both are wording changes for the drafting session. No new sources are needed.
