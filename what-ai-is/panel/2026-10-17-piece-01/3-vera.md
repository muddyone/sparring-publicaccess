_Substrate: Claude (subagent as Vera Tukey), with Rhea Castellan's review in hand._

I'm writing this as Vera Tukey. I read the persona, memory and project context first, then checked the piece against the primary records. I edited no files.

**Bottom line.** Every number in the piece matches its source. The problem is the probe 2c headline: it measures something other than what a general reader will think it measures. Without notes, Claude already named "needs two" correctly on 8 of its 10 final machines. What notes fixed was finding the right pair of blocks within four tests. So the result shows that a carried rule makes exploring more efficient. It does not show a "needs two" bias being overcome. That is still a real finding, and arguably a better one, but the piece currently tells the other story.

**What I checked myself, and what I took on trust**
- I recounted probe 2c from the per-machine counts and records, and read all 20 notes written just before the final machine (10 Claude, 10 GPT).
- I compared how each model opened its tests on the final machine, with and without notes.
- I confirmed the with-notes and without-notes runs used the same machines (10 of 10 sequences match), so the right test is a paired one.
- I re-ran `budget_sim.py`, which makes no API calls. I also wrote a variant that allows a third rule, "exactly one". It was a working file outside the repository.
- I checked the Gjerde figures against Table 3 of the paper's PDF.
- I checked Yiu's 85% and 76% only through Gjerde's restatement (85.2% and 75.9%), not against Yiu's own text.
- I did not check Samiei, GX-Chen or Lucas; those belong to `/cite-check`.

## 1. Are the numbers right?

All the figures match:
- **85% and 76%** match Yiu's 85.2% for children and 75.9% for GPT-4, as Gjerde reports them.
- **81.3% and 88.2%** match Gjerde Table 3, Experiment 2, standard condition. With step-by-step reasoning GPT-4o scored 86.0%. The test against humans gave p = 1.00 after a Bonferroni correction.
- **53% and 93%** reproduce exactly (53.3% and 93.3%).
- **10/10 vs 2/10** and **8 vs 6** match `runs/probe4c/probe4.json`.

Three statements are a little off:
- **"got every one right, 240 machines in all."** Over all 240 machines, the rule was right 240 times, but both rule and pair were right 239 times: GPT named the wrong pair once (`result.md`). The pre-registered measure was the 60 final machines, all correct.
- **"humans' 88.2%."** Those humans are 300 UK adults, not children. The piece's earlier comparison was with children aged 3 to 7, so readers will compare unlike groups.
- **The 53% figure is placed in front of probe 2c, where it doesn't hold.** It assumes the explorer knows there are only two possible rules. In 2c the rules aren't named, and Claude's notes keep "exactly one" in play as well. With three possible rules, an ideal explorer who doesn't know the rule gets about 36% in four tests. Claude's no-notes rate in 2c was 12 of 40 (30%), close to that.

## 2. Is probe 2c sized right? (prioritised changes)

**Impact 9. Say what "right" means.**
- Current text: *"Claude with notes got the final 'needs two' machine right 10 times out of 10, against 2 out of 10 without notes."* Its setup line also asks whether notes help the assistant *"overcome that bias."*
- Why it matters: "right" means both blocks and the rule. Without notes, Claude got the rule right on 8 of 10 final machines and on 30 of 40 machines overall. Its misses were mostly the wrong pair.
- The behaviour shows how the notes helped. With notes, all 10 runs opened with a four-block test, which is the best first move if you expect "needs two". Without notes, all 10 opened with three blocks, and most later spent tests on single blocks, which only help under "any one".
- Suggested text: "Without notes, Claude usually guessed the rule (8 of 10) but found the right pair only 2 times in 10, since four tests aren't enough to settle both. With notes it assumed 'needs two' from the start, planned its tests around it, and got both right 10 times out of 10."
- Then point the setup question at carrying the rule over, not at overcoming the bias.

**Impact 7. Say how many versions were tried, and how 2c was chosen.**
- The order was: three calibration variants, then probe 2, probe 2b and probe 2c. Each was designed after seeing the previous result, and 2c is the only cell that came out positive.
- The piece does show that the named-rules version found nothing ("the first framing shows how easily the result goes away"). It does not say that 2c was the third version tried, devised after two nulls.
- The README's p ≈ 0.0004 uses a Fisher test, which treats the two groups as independent. The machines were matched, so the right test is McNemar: 8 machines went from wrong to right and none the other way, p = 0.008 two-sided.
- That result is still small. But against roughly six comparable final-machine comparisons (three versions × two models), a strict correction leaves it borderline.
- Suggested addition: "This was the third version of the task I tried; the first two showed nothing."
- Separately, the README's p-value should be corrected.

**Impact 7. "Do what a rule kept in the learner does" claims more than was tested.**
- Current text: *"a rule kept in writing can do what a rule kept in the learner does"* and *"Claude formed the expectation Gopnik's children form."*
- Nothing was compared with a rule kept inside a learner: no humans, and no model that updates itself.
- A real expectation also has to give way when the pattern changes. That test (three "needs two" machines, then an "any one" machine) was dropped from the pre-registered pilot.
- The notes suggest the expectation may be rigid. Two of Claude's notes tell it to answer the closing question by the rule rather than by the evidence, for example: "If asked whether a single object lights the machine, answer as AND predicts: it never does."
- Suggested text: "...it suggests, short of proving it, that a rule kept in writing can form from a few examples and carry over to the next task, for at least one model. Whether it gives way when a machine breaks the pattern, as a learner's expectation should, wasn't tested."

**Impact 6. Make the disclosure specific.**
- The header says only "the drafting model is an interested party."
- The specifics: the one model that showed the effect is Claude. The analysis was done by a Claude session, and the notes were read by that same session, unblinded.
- The locked pilot had planned blind coding of the notes by two coders from different vendors.
- Suggested addition to the 2c paragraph: "The model that showed the effect is made by the same company as the model that helped me draft and analyse this; the notes were read by one Claude session, not blind. The replication will use blind coding by other vendors' models."

**Impact 5. Use the fairer comparison and the stronger evidence.**
- 2 of 10 is a low draw. Without notes, Claude got about 3 in 10 machines fully right across the whole sequence (12 of 40). "About 3 in 10" is the honest comparison.
- *"Every one of its notes stated the expectation"*: 9 of 10 state it as an expectation for the next machine. The tenth records "third machine in a row" but only advises confirming the rule.
- Better to cite the behaviour, which every run shows: all 10 opened with four blocks with notes, none did without.

**Impact 4. GPT's notes weren't neutral.**
- Current text: *"GPT's notes stayed neutral."*
- Several say outright "Do not assume the next machine uses AND", so they actively refused to carry the rule.
- One GPT note is malformed: it is just an ANSWER line, not a note.
- Suggested text: "GPT's notes deliberately treated each machine as new ('Do not assume the next machine uses AND')."

**Impact 4. "Neither model carried the rule" claims an absence ten runs can't show.**
- Pooled over both wordings, notes gave 27 of 40 against 22 of 40 without, which is within chance.
- Suggested text: "notes made no clear difference (27 of 40 against 22 of 40), and the notes kept both rules open."

## 3. Rhea's alternative explanations, against the real design and notes

- **The rule might not give way when the pattern changes: live, and the most important.** Nothing was tested with a changed rule, and the "answer as AND predicts" notes are a warning sign. On "any one" sequences Claude did answer "any one" (rule right 5 of 5 with notes), so it isn't simply always saying "needs two". But that doesn't show it would update partway through a sequence.
- **Notes as useful strategy rather than a carried rule: partly answered.** In probes 2 and 2b the notes carried detailed strategy and gave no gain. In 2c, the four-block opening is the best move only if you expect "needs two", so the change tracks the rule. A control would still settle it.
- **The framing changes the problem, not just the wording: live.** Leaving the rules unnamed adds "exactly one" to what the model considers. That drags the no-notes baseline down (an ideal explorer drops from 53% to about 36%) and gives notes more room. Part of what notes do in 2c is remove a difficulty the unnamed framing created. The README says so. The piece doesn't.
- **Notes condition also got told the answer: by design, and fine.** After each machine, the with-notes condition was told which blocks were the right ones; the no-notes condition was told nothing. Since each machine was a fresh conversation, that feedback could only reach the final machine through the notes. It should still be said, because "notes" in the piece means feedback plus notes.
- **Any long preamble, rather than its content, helping: unlikely, but cheap to rule out.** The model's own reasoning on the final machine quotes the rule from its notes.
- **Rhea's point 7 (not significant isn't the same as equal): correct.** It is easy to remove, as in the first item of section 4.

**A minimal locked replication.**
- Setup: the 2c framing, 4 tests, fresh seeds, and prompts, parser, scoring and analysis script all frozen at a tag before any run.
- Cells per model:
  1. "Needs two" sequences, no notes.
  2. "Needs two" sequences, with notes. Comparing 1 and 2 on the same machines (McNemar) is the primary result.
  3. Three "needs two" machines, then an "any one" final machine, with notes. This tests whether the rule gives way.
  4. "Needs two" sequences with feedback kept, but each note swapped for an irrelevant note of the same length.
  5. "Any one" sequences without and with notes, as the mirror case. With no memory, machines are independent, so the no-notes "any one" cell also serves as the baseline for cell 3.
  6. Optional: notes kept but mixed histories, and a positive control told the rule outright (the ceiling is 93%).
- Pre-registered secondaries: whether the first test uses four blocks, and the rate of fully correct machines over the whole sequence. Notes coded blind by two coders from different vendors.
- Sample size: 30 to 40 sequences per cell. The 10/10 is probably inflated by being the one positive of several tries, so plan for a 30- to 40-point effect, not 70.

## 4. Other claims that go beyond their evidence

**Impact 6. "Newer ones have closed most of that gap."**
- In 2023, GPT-4 trailed children by 9 points (and adults by 20).
- In 2025, GPT-4o trailed adults by 7 points, on different, harder items with four options each.
- A reader comparing the piece's own figures (85 − 76 = 9 against 88.2 − 81.3 = 6.9) will see about a quarter of the gap closed, not most.
- Suggested text: "On a newer test against adults, GPT-4o came within 7 points of them, and within 2 with step-by-step reasoning."

**Impact 5. "Not significantly different from humans."**
- Replace with the numbers: "scored 86%, against the adults' 88%."
- The paper ran no equivalence test, and it treats repeated model runs as separate participants, which the authors themselves say is "not strictly accurate."

**Impact 5. The two open readings of the stopped pilot.**
- The follow-up bears on them. With the rules unnamed, the models still named "needs two" about 3 times in 4 without notes (Claude 30 of 40, GPT 29 of 40).
- That leans toward "the bias has mostly closed." Naming the rules wasn't the whole explanation.
- Some imbalance remains: Claude got the "any one" rule right on 18 of 20 machines, against 30 of 40 for "needs two". Both counts are small.

**Impact 4. "How the task was framed decided the result."**
- "Decided" is a causal claim, resting on three probes of 10 runs each where the baseline itself shifts.
- Suggested text: "How the task was framed changed the result."

**Impact 3.** Write "240 machines" as "got the rule right on all 240 machines", or "solved every final machine, 60 of 60".

## What to do next

The Impact 9 and 7 items should be fixed before the piece goes out:
- what "right" means (and the setup question that follows from it),
- that 2c was the third version tried,
- narrowing "does what a rule kept in the learner does", and saying the reversal test wasn't run.

The specific disclosure (Impact 6) costs one sentence. The README's Fisher p-value should also be corrected to the paired McNemar value (p = 0.008).

The finding that survives is good and well suited to general readers: with a rule carried in its own notes, Claude spent its few tests the way a learner who knows the rule would. That is the efficiency gap Gopnik's group found, closed for one model on one task.

I made no memory write because the brief said not to edit files. The entry worth adding later: 2c's "correct" means pair plus rule, and its no-notes deficit is the pair, not the rule.
