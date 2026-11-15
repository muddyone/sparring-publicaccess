# Vera Tukey: numbers review, essay 06 (first panel read), 2026-11-14

Lane: every figure in `drafts/2026-11-14-06-different-answers.md`. Checked against brief 12
(`briefs/2026-10-19-12-different-answers.md`) and, for Bart's two studies, Paper 1
(`pilots/llm-judge-2026-05-02/v2/preprint-draft.md` §6.3, §6.4, read only). I also checked the
published 2026-09-14 correction to the catch-rate post, which uses the same §6.4 data
(`docs/research/post-catch-rate-2026-09-02/public-bundle-2026-09-14/README.md` and
`denoise-new-counts.json`).

**What shaped this, disclosed.** No web. Every outside figure is checked only as far as the brief's
abstract-level entry goes. Every outside source behind a number here is marked **[abstract]** in the
brief, so no outside figure has been read in a full text. I did look at one distribution, the
per-problem new-flaw counts in `denoise-new-counts.json`. Everything else is summary figures.
Impact is on a 1 to 10 scale.

---

## 1. Every figure

| # | Essay text (quoted) | Source | Matches? | Label OK? | Fix |
|---|---|---|---|---|---|
| 1 | "five models set to be deterministic were given the same eight tasks ten times each" | brief 1.2, Atil [abstract] | yes | yes | none |
| 2 | "accuracy still varied by up to 15% from run to run" | brief 1.2: "up to 15% across naturally occurring runs" | yes in figure | **no**: the unit isn't settled (15 percentage points, or 15% of the score?), and "from run to run" reads as consecutive runs, not the spread across ten | "across the ten runs". Cite-check to confirm the unit, then write "percentage points" if it is (F7) |
| 3 | "the same prompt run 1,000 times … gave 80 different completions" | brief 1.4, He [checked against the post] | yes | **no**: misreadable as "80 of the 1,000 came out different" | "came out in 80 distinct versions" (F5) |
| 4 | "17.9 percentage points" on grade-school maths | brief 4.1, Wang [abstract]: "+17.9% on GSM8K" | **figure yes, unit unsupported** | **no**: the unit goes beyond the brief, and there's no model, no starting score, and no number of samples | see flag 5 verdict (F4) |
| 5 | "more than 350 models" | brief 4.6, Kim [abstract] | yes | yes | none |
| 6 | "the same wrong answer about 60% of the time on one benchmark" | brief 4.6: "On one leaderboard dataset, models agree 60% of the time when both models err" | yes | partly: "one benchmark" is good, but nothing tells the reader what chance would give | add a chance yardstick once the cite-check confirms the dataset's answer format (F6) |
| 7 | "about seven months later, repeated about nine in ten … changed about one in ten" | brief 2.1, Ulery [abstract]: 89.1% identifications, 90.1% exclusions; "most changes went to 'inconclusive'" | yes | partly: "changed" hides that most changes were to "inconclusive" | "mostly to 'can't tell'" (F10) |
| 8 | "ten radiologists … ranged from 11% to 65%" | brief 2.3, Elmore 1994 [abstract] | yes | partly: this is *different* experts disagreeing, set next to a *same* expert retest with no label | label it (F9) |
| 9 | "changed their answer 46% of the time" (first use, l.100–101) | brief 5.7, Laban [abstract] | yes | **no**: no citation and no scope at first use | cite and scope it at first use (F8) |
| 10 | "those examiners changed about one in ten on a plain retest" | brief 2.1 | yes | the comparison drawn is the problem | flag 2 verdict (F3) |
| 11 | "moved one open model's accuracy by as much as 76 points" | brief 5.1, Sclar [abstract]: "up to 76 accuracy points" (LLaMA-2-13B, few-shot) | yes | partly: "points" of what? | "76 percentage points (on a 0–100 scale)" (F7) |
| 12 | "models changed their answer 46% of the time on average, and accuracy dropped" (l.125) | brief 5.7 | yes | partly: ten 2023 models on seven classification tasks, not stated | add the scope (F8) |
| 13 | "8 problems, with the flaws judged by AI" (§6.4) | Paper 1 §6.4: n = 8 | yes | yes | none |
| 14 | "The final answers had about the same number of flaws as after one challenge and one fix" | Paper 1 §6.4: R2 against R1, +0.000 same-vendor, −0.125 cross-vendor | yes | yes | keep. But see F1 on what sits around it |
| 15 | "revising under that pressure added new ones" | Paper 1 §6.4 "~2.0–2.6 new per output … read the levels as upper bounds"; **public correction 2026-09-14**: the same grader finds 1.95 "new" flaws in drafts nobody revised | **no, as an absolute claim** | — | F1 |
| 16 | "Legal research tools … 17–33% of the time" | brief 6.3, Magesh [abstract]: "each hallucinate between 17% and 33% of the time" | yes | OK. A plainer scale would help | optional (F11) |
| 17 | "(8 problems, with the flaws judged by AI)" (§6.3) | Paper 1 §6.3 | yes | missing: hard problems built to contain flaws; no significance test | F2 |
| 18 | "caught 87% of the serious flaws … 68% … 55%" | Paper 1 §6.3 table: 87.1 / 67.7 / 54.8; brief A.3 the same | **yes** (correct rounding: 27, 21 and 17 of 31) | **no**: "the serious flaws" reads as all the flaws there were. It is the 31 an AI panel confirmed | F2 |
| 19 | "On GPT's work the self-review gap nearly vanished" | Paper 1 §6.3 grid; brief A.3 | yes | partly: a follow-up run, not the pre-registered one | optional label (F16) |
| 20 | "On 31 forecasting questions, the pooled forecasts of twelve models … 925 human forecasters" | brief 4.5, Schoenegger [abstract] | yes | yes | F14 (what it supports) |
| 21 | "you can ask it ten times, independently, for almost nothing" | rhetorical, no source | n/a | fine | none |
| 22 | "It costs a minute" (step 1) | no source; it's advice | n/a | fine | none |
| 23 | "Several studies here used 2023 models" | Laban, Sharma, Smit, Manakul, Wang | yes | yes | none |

Paper 1 checks asked for in my brief: **the A.3 figures 87 / 68 / 55 match §6.3 exactly** (87.1, 67.7, 54.8,
rounded correctly). They are the pre-registered single-vendor cell, all Claude, 31 flaws, which is the
right cell to quote. **The A.4 sentence "about the same number of flaws" matches §6.4's R2-against-R1 null.**
The sentence next to it does not hold up against the published correction (F1).

---

## 2. Ranked findings

### F1 (Impact 8). §6.4: "revising under that pressure added new ones" repeats a figure we have publicly corrected, and the paragraph leaves out the comparison that cuts our way less

> "The argument removed old flaws, but revising under that pressure added new ones. The final answers had
> about the same number of flaws as after one challenge and one fix"

- **What's wrong.** The paper's new-flaw counts (about 2.0 to 2.6 per answer) are the grader's reading. The
  paper itself says to read them as upper bounds. On 2026-09-14 we published a correction on the same data:
  the grader, run on the original drafts that **nobody revised**, finds an average of **1.95 "new" flaws**
  per draft. One challenge-and-fix came to 2.125, which is **0.175 above an untouched draft**. So "added new
  ones", as a plain statement, is mostly the grader's baseline. What survives is a **comparison**: the
  challenged rewrite ended with more new flaws than the model rewriting on its own (about 0.9 more per
  draft same-model, about 1.4 more cross-model; 5 problems higher, 1 lower, 2 tied). Our own correction says
  "a size doesn't cancel the baseline". An essay is the wrong place to bring the uncorrected size back.
- **The left-out comparison.** §6.4's own effort-matched control, in which the model quietly revised its
  own work twice with no challenger, **came out cleanest of all**. That is 2.25 flaws per answer, against
  2.625 and 3.125 after one challenge-and-fix, and the arguing condition was worse again (+0.375 and +0.750,
  Paper 1). Brief 12 §A says to report each pilot "and keep the unfavourable numbers". Here the unfavourable
  number cuts against the essay's next sentence ("models asked to correct themselves with no new
  information often fail", Huang) and against the §6.3 bullet's suggestion that a challenger is a check
  that "works". It doesn't cut against the position. It **sharpens** it: the challenge *finds* problems,
  and its rewrite is a new answer that needs checking in turn.
- **Fix (plain words, for the drafter to rewrite).** Something like: *"The challenge found more of the old
  flaws. But the rewrite made under that pressure brought in more new ones than the model's own quiet
  rewrite did. In the end, arguing to agreement left about as many flaws as one challenge and one fix, and
  neither came out cleaner than the model simply revising its own work twice."* Then keep "8 problems,
  flaws judged by AI, a small result". Add "one run each, no statistical test" if there's room in the
  rhythm. The lesson for the reader, which belongs in "What does": *use the challenger to find what's
  wrong, then check the fix too.* That adds two sentences. It makes the routine's step 4 honest about
  what a reviewer gives you.
- Ceiling for any wording: "no cleaner", in both directions. The R1-against-R1′ net gap is noise-sized
  (same-vendor +0.375, SD 2.07, 3 better, 2 worse, 3 tied). Don't write "self-revision did better". Write
  "did as well or better", or "neither came out cleaner".

### F2 (Impact 7). §6.3: the 87 / 68 / 55 have the right figures but no stated denominator, and they measure *finding* flaws, not a better final answer

> "A reviewer told to attack it caught 87% of the serious flaws. Claude checking its own work caught 68%,
> and a neutral fresh reviewer caught 55%"

- **The denominator.** "the serious flaws" reads as *all* of them. It is the 31 flaws that at least two of
  three AI auditors agreed on, across 8 hard problems built to contain flaws. Each percentage is a count
  over 31, so one flaw is about 3 points. For this reader, counts read on sight: **27, 21 and 17 of 31**.
  That also removes any false sense of precision.
- **Who the reviewers were.** All three were Claude. The attacker and the neutral reviewer were fresh
  copies, the self-reviewer was the author. So the 87-against-55 gap is the **instructions alone**, with
  the same model and the same fresh eyes. That is exactly the essay's "the job you give the check matters".
  But the reader can't see it, and a reader who has just been told "you don't make an answer reliable by
  asking the same model again" will be puzzled that the winning check was the same model. Say it: *"a fresh
  copy of Claude, told to attack it"*.
- **What it measures.** These are flaws *flagged* on a fixed draft. Paper 1 §6.4 calls this measure one
  that "cannot see" the revision. It is good evidence that a reviewer with a job *finds* more, but not that
  the answer ends up better (F1). The bullet sits under "the checks that do work". Scope it to *finding*.
- **Fix.** *"In a study of mine (8 hard problems built to contain flaws, with the flaws judged by AI), I
  looked at work Claude had produced. An AI panel agreed on 31 serious flaws. A fresh copy of Claude told
  to attack the work found 27 of them. Claude re-checking its own work found 21, and a fresh copy asked
  for a neutral review found 17."* Keep "The job you give the check matters", and the GPT sentence. Adds
  about 25 words, each one a denominator or a label.

### F3 (Impact 7). Flag 2: the 46% against "about one in ten" is a pairing of two numbers that measure different things

> "it appears easier to talk out of a correct answer: models asked "are you sure?" changed their answer
> 46% of the time, while those examiners changed about one in ten on a plain retest, with nobody pushing
> back and on a different task. So the comparison is loose."

Verdict in §3. In short, the disclosure is honest, but the sentence still sets 46 beside 10 as evidence for
a claim neither number measures.

### F4 (Impact 6). Flag 5: "17.9 percentage points" goes beyond its source, and the reader can't use it as written

Verdict in §3.

### F5 (Impact 5). "80 different completions" reads as "80 of 1,000 came out different"

> "the same prompt run 1,000 times at the "no randomness" setting gave 80 different completions"

- **What's wrong.** The source says **80 unique** completions: 1,000 runs produced 80 distinct versions.
  An everyday reader can easily take "80 different" as 8% of runs differing from the rest, which is a
  smaller and different finding.
- **Fix.** *"came out in 80 distinct versions."* Optionally add the brief's detail, which makes it
  concrete: *"all identical for the first hundred or so tokens (word pieces), then splitting."*

### F6 (Impact 5). Kim's 60% has no yardstick, so the reader can't tell whether it is high

> "when two of them both got a question wrong, they gave the same wrong answer about 60% of the time on
> one benchmark"

- **What's wrong.** "Helps less than you'd hope" needs the number to be judged against something. If two
  models erred independently on a four-option multiple-choice question, they would pick the same wrong
  option about a third of the time by chance. That is arithmetic, not a source. Whether the benchmark *is*
  multiple choice, and with how many options, is **not in the brief** (the abstract says only "one
  leaderboard dataset"). So I can't hand the drafter the yardstick.
- **Fix.** The cite-check should record the dataset and its answer format. If it is multiple choice, add
  one clause, e.g. *"where chance alone would give about one in three"*, with the right figure for the
  format. If that can't be confirmed, leave the number as it is. Do not supply a baseline from memory.

### F7 (Impact 4). The same kind of number appears in three units

- "up to 15%" (Atil), "17.9 percentage points" (Wang), "76 points" (Sclar). All three are probably changes
  in an accuracy score out of 100, but the essay gives the reader three labels for them.
- **Atil.** "up to 15%" is the abstract's wording. Whether it means 15 points or 15% of the score isn't
  settled at abstract level. **The cite-check must confirm the unit.** If it is points, write "up to 15
  percentage points". If not, write "up to 15% of its score".
- **Sclar.** "76 points" means nothing to this reader without a scale. Write *"76 percentage points, on a
  scale where 100 is every answer right"*, or *"from X to Y correct"* if the cite-check finds the ends.
  (The abstract says "accuracy points". Percentage points of accuracy is the plain reading, so this one
  does not go beyond the abstract.)
- After that, one rule throughout: a change in a percentage score is "percentage points" at first use,
  and "points" after that.

### F8 (Impact 4). The 46% first appears in "Compared to what?" with no citation and no scope

- Line 100–101 uses the 46% two sections before Laban is cited (l.125). A reader arriving at "Compared to
  what?" gets a precise figure with no source.
- It also needs its scope wherever it travels: **ten 2023 models, seven classification tasks** (brief
  5.7). The "What this doesn't claim" bullet about 2023 models is too far away to bound it.
- **Fix.** Cite Laban at the first use, and give the scope once: *"in a 2023 test of ten models on
  sorting-type questions"* (or "classification tasks", Rosetta's call).

### F9 (Impact 3). The radiologist range is *different* experts. The examiners are the *same* expert. The essay doesn't say which is which

- Brief 12 Q2 makes this distinction carefully: the fair analogue to "the same AI gave two answers" is
  the *same* expert asked twice. Elmore's 11% to 65% is ten radiologists disagreeing with each other. Its
  AI counterpart is Kim's different models, not one model asked twice.
- **Fix, additive.** *"And different experts disagree with each other even more: when ten radiologists
  read …"* That one clause keeps the comparison honest, and it strengthens the paragraph.

### F10 (Impact 3). "changed about one in ten" hides that most changes were to "inconclusive"

- Brief 2.1: "most changes went to 'inconclusive'". An examiner moving from "match" to "can't tell" is a
  hedge, not a reversal. The reader will picture reversals, like the AI's flips.
- **Fix.** *"changed about one in ten, mostly to 'can't tell'"*. This also feeds the flag-2 fix.

### F11 (Impact 2). Magesh: a plainer scale is available

- "17–33% of the time" is right, and it is a range **across tools** (brief: "each hallucinate between 17%
  and 33%"). The reader could take it as one tool's variation.
- **Optional.** *"between about one answer in six and one in three, depending on the tool."*

### F12 (Impact 2). "Nobody has yet run the study" is stronger than the search supports

- Brief 12 Q2: "No head-to-head study was **found** (search 2026-10-19)".
- **Fix.** *"I haven't found the study that would settle the comparison …"*. Also in "What would change my
  mind", which already assumes the study doesn't exist.

### F13 (Impact 2). "Its tone tells you nothing about whether it's right" is stronger than its evidence

- Xiong (brief 3.5) says stated confidence tends to be **over**confident, and that calibration improves
  with capability. Brief 3.6 (Tian) finds stated confidence "typically better-calibrated" for chat-tuned
  models. Neither supports "nothing".
- **Fix.** *"Its tone is a poor guide to whether it's right."* Miriam may want this too. It's here because
  "nothing" is a quantity the evidence doesn't reach.

### F14 (Impact 2). Schoenegger supports a crowd of twelve, and "indistinguishable" on 31 questions is weak equivalence

- The bullet is headed "A different model, or a crowd of them". The only number under it is a pool of
  **twelve**, and it measures the accuracy of an average, not a check. It doesn't speak to asking *one*
  other model. Step 4 of the routine ("Ask a different model") rests on the brief's own reading (6.12
  **[ours]**) and on Kim's limit, not on this figure.
- "Statistically indistinguishable" on 31 questions means no difference was detected at a small n. It
  does not show the two crowds were equal. "About as accurate as" is fair. Don't strengthen it.
- **Fix.** Optional: *"pooled forecasts of twelve models were about as accurate as …"*, and leave the
  single-second-model claim to the "Because models share errors" sentence, which is already worded as a
  condition.

### F15 (Impact 1). Two dropped qualifiers

- Basil: no improvement "except one model, Gemini 2.0 Flash". Meincke 2025c: "**generally** has no
  significant effect". The essay drops both. Neither changes the argument. "Generally" costs one word.

### F16 (Impact 1). The GPT sentence is follow-up work

- The 87 / 68 / 55 are the pre-registered cell. "On GPT's work the self-review gap nearly vanished" comes
  from the later grid, which is added work. *"In a follow-up run, on GPT's work …"* keeps the two apart.

---

## 3. Verdicts on the drafter's flags

### Flag 2: 46% under "are you sure?" against about one in ten on a retest

**Not fair as written, though it is honestly hedged.** The hedge ("So the comparison is loose") is
true. But the sentence still offers the two numbers as evidence for *"easier to talk out of a correct
answer"*, and neither measures that. There are four mismatches. The draft discloses two of them, the
missing pushback and the different task.

1. **Condition.** Pushback for the AI, none for the people. The human figure can't tell you how a person
   behaves under pushback, which is the claim. (Disclosed.)
2. **Task.** Classification questions against fingerprint comparisons. (Disclosed.)
3. **What counts as a change.** The examiners' changes were mostly to "inconclusive" (F10). Laban's are
   answer flips. A hedge and a reversal are being counted as the same thing. (Not disclosed.)
4. **"Correct".** The 46% counts every flip, including wrong answers flipped to right ones. The evidence
   that correct answers were given up is the **accuracy drop** (17% on average, brief 5.7), not the 46%.
   (Not disclosed, and the word "correct" leans on the wrong number.)

A ratio reader will do the sum "about five times as often". That sum is meaningless here, because the
two numbers have different numerators and different conditions.

**Fix.** Make the claim about the AI alone, with its own evidence, and move the examiners to the
"nearest human figure" role:

> *"And it appears easier to push off an answer. In a 2023 test of ten models, simply asking "are you
> sure?" made them change their answer 46% of the time, and they got less accurate overall
> ([Laban et al. 2023]). I know of no study that puts experts under the same pressure. The examiners'
> one in ten, mostly moves to "can't tell", came from a quiet retest months later, with nobody pushing."*

This keeps "Compared to what?" honest. It keeps the 46%, and it adds what the reader needs to see why
the comparison is loose, rather than just being told that it is.

### Flag 5: Wang et al. "17.9"

- **The brief supports only "+17.9%"**, from the abstract, on GSM8K. The draft's "**percentage points**"
  is a conversion the brief doesn't make. Panel brief §5 forbids going beyond an abstract's claim. So the
  current wording is unsupported until checked, even if it turns out right.
- **Absolute or relative?** I suspect absolute. My recollection of the paper's results table is one
  model going from about 57% to about 74% correct, a 17.9-point gain. That is memory, not checked here.
  **Do not paste it.** The **cite-check must confirm** from the full text: (a) absolute points or a
  relative gain, (b) which model the 17.9 belongs to, (c) its starting and ending accuracy, and (d) how
  many answers were sampled for each vote.
- **Can the reader use it as written?** Not yet, for three reasons.
  1. The figure has no starting score. "Rose 17.9 points" from 10% and from 80% are different worlds.
  2. "17.9" is false precision for this reader. Use "about 18".
  3. **The comparison it invites isn't the routine's.** A majority vote needs several answers, and the
     paper sampled many. The very next paragraph tells the reader to "ask the question again", which is
     two answers. Two answers give a disagreement signal but no majority. Placed where it is, the 17.9
     reads as the payoff of asking twice.
- **Fix, after the cite-check.** *"On one benchmark of grade-school maths word problems, taking the most
  common of many sampled answers raised one model's score by about 18 percentage points, from about X% to
  about Y% correct."* Fill in X and Y only from the confirmed table. Then open the next paragraph so it
  doesn't inherit the gain: *"You don't need many answers to use the warning half of this. Ask the
  question again …"*. If the cite-check shows a relative gain, write *"improved its score by about 18%"*,
  with the base.

---

## 4. One-line verdict

**Ready after fixes.** The figures are transcribed accurately, and 87 / 68 / 55 and "about the same number
of flaws" match Paper 1. But F1 has to land before this goes out: it brings back a size that our
2026-09-14 correction withdrew, and it leaves out our own unfavourable control. F2, F3 and F4 come next,
with F4 gated on the cite-check. None of these needs another full round. F1 to F4 need a check of the
rewritten sentences against this report.
