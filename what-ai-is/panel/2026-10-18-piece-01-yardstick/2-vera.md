_Substrate: Claude (subagent as Vera Tukey), with the stage-1 reviews in hand. Piece 01 (the yardstick)._

**Vera Tukey: numbers and fair comparisons in piece 01 (the yardstick)**

**Verdict.** Most figures match their brief entries and verification marks: Grove, Dietvorst, Liu (499 people), Manoli, Logg, Rieger, Dell'Acqua (758 consultants, 19 points), Krishnamurthy, Samiei, Burda (54 environments) and the Probe 2c counts. Two passages are not fair comparisons. The *Noise* underwriter figure is a between-person quantity set against a within-system demand, and it is still marked secondary. The clinical-versus-mechanical evidence is set against generative AI, when the mechanical side of that evidence is the calculator. The algorithm-aversion section calls one finding an error. Probe 2c is mostly consistent with the settled account but leaves out what "fully right" was missing without notes.

**1. Impact 8: the underwriter figure is secondary-sourced and compares the wrong kind of inconsistency.**
- Current words: "two underwriters pricing the same case differed by a median of 55%, about five times what the company's executives expected (Kahneman, Sibony & Sunstein, _Noise_, 2021; figure from secondary summaries, to check against the book before publishing). Inconsistency is the normal condition of expert judgment."
- The brief (2.1) is marked **[secondary]** and says "check the book before quoting numbers." Both cite-check passes judged it from model knowledge only. No retrieved text confirms 55% or "five times."
- From memory (not verified), the book defines the gap as the difference between two quotes divided by their average, takes the median across pairs, and puts the executives' typical expectation at about 10%. So "five times" is plausible, but it is unchecked.
- The bigger problem is the kind of variation. The figure measures disagreement **between two people** (what the book calls level plus pattern noise). The calculator demand it answers is "the same input always giving the same output," which is the **same** system asked twice. In people, that matches occasion noise. In models, it matches sampling variability. Disagreement between underwriters would match disagreement between different models or deployments. The piece answers one kind of variation with evidence about another.
- The leftover note must come out either way.
- Honest restatement (after checking the book): "At one insurer, when two underwriters priced the same case, their quotes typically differed by 55% of the average of the two, about five times what executives expected (_Noise_, ch. 2). That is disagreement between people. The same expert also varies from one day to the next, and that is the closer comparison to a model giving different answers to the same question." If the book can't be checked, cut the number and keep the claim qualitative.

**2. Impact 8: Grove is evidence for fixed formulas, not for generative AI.**
- Current words: "mechanical prediction rules were about 10% more accurate than expert clinical judgment on average… Expert judgment is valuable, and it is not the gold standard we imagine."
- The mechanical rules in Grove's meta-analysis are fixed, consistent formulas: the calculator in the piece's own terms. Part of their edge over experts comes from that consistency. The evidence shows expert judgment is beatable, which is fair. It says nothing about open-ended generative systems, and it partly supports the calculator standard the piece argues against.
- The abstract's "about 10%" has no stated unit; it is not percentage points. The piece also leaves out that in many studies neither side was clearly ahead.
- Honest restatement: "Across studies of health and behaviour, fixed statistical formulas matched or beat expert clinical judgment, and experts were clearly better in only a few (Grove et al. 2000). That shows expert judgment is no gold standard. It doesn't show how generative AI compares, because those formulas are the opposite of generative AI: fixed and perfectly consistent."

**3. Impact 6: the piece asks for consistency and relies on it at the same time.**
- Current words: "We don't expect an intern to be perfectly consistent." Later: "An error a model makes again and again can be found, measured and designed against."
- The first excuses variation in a model's answers. The second depends on the model being consistent. Both can be true, but only if the piece names which consistency it means.
- Honest restatement (added after the scale point): "Models vary in their wording from run to run but often repeat the same kinds of error. The second is what makes their errors testable."

**4. Impact 6: aversion findings are presented as proof of irrationality.**
- Current words: "Machines get a harsher, more binary verdict." Also: "That last finding is the binary error in its purest form."
- None of these studies measured whether verdicts were "binary." That is the author's reading.
- **Dietvorst:** the authors show a costly mistake. Participants were paid for accuracy and still abandoned the better forecaster.
- **Liu:** a stated acceptance threshold from one convenience sample.
- **Manoli:** attitude spillover. Generalizing from one AI to all AI can be reasonable when systems share models or training data, the piece's own Bommasani point (Rhea, objection 5).
- Honest restatement: "These studies show that people judge machine errors more harshly than human ones. In one (Dietvorst), that cost them accuracy. In the others, a stricter standard may be partly justified, for example when one model's flaw is shared by many systems. Whether it is justified depends on what the systems share."

**5. Impact 5: Probe 2c needs two facts added and its claim narrowed.**
- Present and correct: exploratory, rules unnamed, third version tried, GPT did not show it, 10/10 against 2/10 fully right.
- Missing:
  - Without notes, Claude got the **rule** right on 8 of 10 final machines. Its shortfall was finding the right pair in four tests. "Spent its few tests accordingly" hints at this but doesn't say it.
  - One model, ten runs per condition, no replication.
- Current words: "That is learning from its own experiments." And in the curiosity summary: "given experiments to run, a model can learn from them and carry the lesson to the next task."
- Honest restatement, first part: "Without notes, Claude usually guessed the rule (8 of 10) but found the right pair only twice in four tests. With notes, it assumed 'needs two' from the start and got both right every time: the lesson made its exploring more efficient. One model, ten runs, not yet replicated."
- Honest restatement, curiosity summary: "...for one model on one task, a model keeping notes learned from experiments it was given and carried the lesson to the next."

**6. Impact 2: "solved every machine" in the locked pilot is slightly loose.**
- Current words: "three current models solved every machine they were given."
- The rule was right on all 240 machines, but rule and pair together on 239. Honest restatement: "...named the rule correctly on all 240 machines they were given."

**What to do.** Fix items 1 and 2 before the piece goes out: check the 55% against the book or cut it, name which kind of inconsistency each piece of evidence measures, and stop presenting Grove as evidence about generative AI. Items 3 to 5 are sentence-level fixes. I edited no files.
