# Outside review: Rhea Castellan

_Substrate: openai/gpt-6.1-sol. Piece: 01y-for-outside.md. Finish: stop._

## VERDICT

The modest argument survives: AI should be compared with realistic alternatives in the role where it will actually be used. The stronger argument—that critics commonly demand calculator-like perfection, and that comparison with colleagues answers their concerns—is not established. The developmental discussion also makes the disagreement too easy to resolve by reducing causal exploration and discovery largely to whether a system starts investigating without instructions.

## OBJECTIONS

### 1. The central opponent is not established

“You know how to evaluate a calculator, and most software. It must be:
- **correct or incorrect,** with nothing in between;
- **perfectly consistent,** the same input always giving the same output;
- **fully trustworthy and explainable** before it counts as safe or valuable.”

The piece needs to establish that these are the standards its opponents actually apply. They are not a satisfactory description of software evaluation generally: software can be probabilistic, reliability can be graded, and acceptable failure rates depend on consequences. Nor do users ordinarily require a calculator’s implementation to be fully explainable.

The strongest objection is that the piece substitutes an implausible position for substantive criticism. Influential critics discuss concentrated power, discrimination, misleading linguistic fluency, environmental costs and deployment conditions—not simply failures to achieve deterministic perfection. Showing that people sometimes distrust algorithms does not show that academic criticism rests on this supposed yardstick.

Published basis: Bender, Gebru, McMillan-Major and Shmitchell, 2021, ACM FAccT, “On the Dangers of Stochastic Parrots,” supplies an identifiable critical position against which this characterization could be tested. It is not representative evidence about all critics, either.

Change: qualify the claim to particular, accurately quoted criticisms, or add the content analysis needed to support its stated prevalence. Cut the characterization of “most software.” The admission that the prevalence claim is currently an impression does not supply the missing foundation.

### 2. Gopnik’s position is reduced to a weaker contrast

“In Alison Gopnik's account they are truth-seekers who experiment on the world, while models trained on text pass on what others have written”

The contrast is not simply between children who initiate inquiry and models that need prompting. It concerns how learners generate hypotheses, choose informative interventions, discover causal structure and produce innovations that go beyond reproducing accumulated cultural material.

Yiu, Kosoy and Gopnik also treat cultural transmission as an important achievement. Children themselves learn extensively through testimony and imitation. The question is how transmission and discovery interact, not which class of entity exclusively possesses each.

The strongest objection is that the piece subsequently treats initiating experiments as the remaining gap, although the developmental position concerns the quality, flexibility and generalization of investigation as well. A system could initiate many experiments while learning very little; another could investigate competently after an invitation.

Published basis: Yiu, Kosoy and Gopnik, 2023 online publication, *Perspectives on Psychological Science*, “Transmission Versus Truth, Imitation Versus Innovation”; Gopnik et al., 2004, *Psychological Review*, “A Theory of Causal Learning in Children.”

Change: add the distinction between initiating inquiry and conducting causally informative inquiry. Qualify the transmission/truth contrast as a proposed difference in learning functions, not an exhaustive division between children and models. A model selecting interventions in a simulated world could satisfy the relevant functional tests; biological embodiment need not be made a requirement.

### 3. The pilot does not yet establish the developmental comparison

“over a run of machines it wrote down the expectation that they ‘need two’”

“That is learning from its own experiments.”

The second statement could be justified at the level of the model-plus-notes system. But it does not, by itself, establish the analogy to children’s overhypothesis learning.

An overhypothesis is a higher-order expectation about how causal relationships are organized across cases. Writing down a recurring rule is evidence worth investigating, but the decisive question is whether the learner uses evidence to form, transfer and revise that expectation. Lucas and colleagues investigated learning about the forms of causal relationships, including developmental differences in responsiveness to evidence supporting less familiar forms—not merely whether learners could retain a successful rule.

The strongest alternative explanation is that notes preserve a useful task-specific heuristic within a repeatedly sampled problem family. That can improve performance without establishing the broader causal flexibility invoked by the comparison. Selecting the third task version and obtaining the effect in one model also makes the result exploratory rather than a clean test of a prior prediction.

Published basis: Lucas, Bridgers, Griffiths and Gopnik, 2014, *Cognition*, “When Children Are Better (or at Least More Open-Minded) Learners Than Adults.”

Change: qualify the conclusion as preliminary system-level learning. Add public task specifications, complete transcripts, all attempted conditions, fresh held-out problems, matched-history controls, and tests in which the causal rule changes. Distinguish retaining information from learning a transferable expectation. The linked local files are not supplied here, so this is an assessment of the reported design, not a reanalysis.

### 4. “Without being asked” is not a sufficient definition of curiosity

“By that test, curiosity counts if a system seeks information without being asked to.”

“The same functional test that credits these systems with learning finds no natural curiosity in them.”

The first sentence introduces an additional criterion that does not follow simply from defining curiosity as motivation to seek information. Information seeking can be prompted yet internally directed; unprompted information seeking can instead serve an externally specified task.

Children’s curiosity is also sensitive to demonstrations, instructions, uncertainty and social context. Much developmental evidence comes from situations deliberately arranged by researchers. Being invited to explore does not determine which intervention a child chooses or what the child learns.

The strongest objection is architectural: a conversational model that runs only when called has no ordinary opportunity to initiate anything. Its silence between calls cannot distinguish absence of an information-seeking policy from absence of an execution loop. Conversely, giving a model a timer and instructions to generate questions would not establish curiosity merely because no user supplied that particular question.

Published basis: Kidd and Hayden, 2015, *Neuron*; Schulz and Bonawitz, 2007, *Developmental Psychology*, “Serious Fun”; Bonawitz et al., 2011, *Cognition*, “The Double-Edged Sword of Pedagogy.”

Change: qualify “no natural curiosity.” Separate opportunities to act, initiation, preference for information, intervention quality and subsequent learning. If the intended claim concerns current assistant products rather than underlying learning capacities, say so.

### 5. Human comparison does not make a higher machine threshold irrational

“The better question isn't ‘is it reliable software?’ It's ‘how does it compare with whoever would otherwise fill this role, and what checks do its real differences call for?’”

“That last finding is the binary error in its purest form.”

The first quotation presents questions that should usually be asked together. The second treats broader generalization from an AI failure as necessarily an error, without examining whether the systems share relevant causes of failure.

The strongest objection is that apparently unequal standards can reflect unequal consequences. A shared model may create correlated failures across institutions; a deployment may remove alternatives or impose risks on people who did not choose it. Equal average accuracy need not imply equal acceptability. Whether generalizing from one model to others is warranted depends on what they share, not simply on whether people generalize similarly about humanity.

The correct comparison is also often between complete workflows, not between an isolated model and an isolated intern. Review time, detection difficulty, deskilling, escalation and residual errors all count. Better model performance does not guarantee better human–AI performance.

Published basis: Bainbridge, 1983, *Automatica*, “Ironies of Automation”; Vaccaro, Almaatouq and Malone, 2024, *Nature Human Behaviour*, “When Combinations of Humans and AI Are Useful.”

Change: concede that higher thresholds can be justified. Add workflow-level outcomes and distribution of harms to the yardstick. Qualify the aversion studies as evidence about judgments, not proof that those judgments are unreasonable.

### 6. Correction and a named person do not close most accountability gaps

“Fix it once and it's fixed for everyone.”

“Correct a model and every user gets the fix, and later versions inherit it.”

“Two things close most of it:”

These are much stronger claims than the argument supports. A correction can be specific to a prompt, deployment, memory store or model version. Retraining can introduce regressions. Later versions do not automatically inherit a reliable behavioral correction.

Accountability is also not merely the availability of an update and the identification of a person. It includes authority to intervene, evidence preservation, independent scrutiny, remedies for affected people and enforceable responsibility. A named professional may lack the information or control needed to answer meaningfully for a provider’s system.

The strongest objection is that the piece offers operational maintenance as a substantial solution to an institutional problem. Some harms remain even after a model has been corrected.

Published basis: Matthias, 2004, *Ethics and Information Technology*, identifies the responsibility problem; Sculley et al., 2015, *Advances in Neural Information Processing Systems*, “Hidden Technical Debt in Machine Learning Systems,” documents maintenance complications; Raji et al., 2020, ACM FAT*, “Closing the AI Accountability Gap,” develops a broader auditing framework.

Change: cut the universal inheritance claim and “most.” Add versioned regression testing, limits of user control, institutional duties and remedies. Keep correctability distinct from accountability.

### 7. Evidence of human fallibility is being asked to establish too much

“The demands made of AI are demands human experts don't meet.”

“Inconsistency is the normal condition of expert judgment.”

The cited evidence establishes reasons not to idealize human performance. It does not establish that standards imposed on generative AI are inappropriate.

The insurance example concerns disagreement between underwriters. That is not the same phenomenon as one system returning different answers to repeated identical inputs. Both may matter, but their causes and remedies differ. Similarly, evidence that mechanical prediction rules outperform clinical judgment does not establish the performance of open-ended generative systems. Indeed, that literature demonstrates the value of some precisely specified, comparatively constrained methods.

The strongest objection is inferential: failures of the human baseline help specify a comparison, but do not determine its outcome or identify the right safeguards.

Published basis: Grove et al., 2000, *Psychological Assessment*; Kahneman, Sibony and Sunstein, 2021, *Noise*, Little, Brown Spark.

Change: qualify the generalizations and distinguish between-person disagreement, within-person variability and model sampling variability. Add task-matched evidence wherever a claim concerns generative AI rather than mechanical prediction generally. Verify the insurance statistic directly before publication.

### 8. The intentional stance supplies predictions, not a general management prescription

“On the ground, an apparent aim should be responded to the way we'd respond to a colleague's.”

“The human one does, and it brings the remedy with it: make candour a requirement instead of hoping it survives closeness.”

Dennett’s intentional stance does not entail either prescription. A system can usefully be described as pursuing an aim without sharing the mechanisms, incentives or capacities that make an intervention work with a colleague.

The strongest objection is precisely developmental: superficially similar behavior can arise from different learning processes and generalize differently. Human reluctance to contradict a friend and model sycophancy might warrant a common behavioral label while requiring different interventions. A requirement for candour is an objective, not evidence that the objective can be reliably implemented.

The piece acknowledges that differences matter, but these passages infer practical remedies from resemblance before establishing that those remedies transfer.

Published basis: Dennett, 1987, *The Intentional Stance*, MIT Press, supports the predictive strategy, not an unrestricted inference to colleague-like treatment. No citation establishes the proposed transfer of remedies.

Change: qualify the colleague comparison and separate behavioral description from causal explanation. Add evidence that the proposed safeguard changes behavior reliably, including under pressure and outside its training examples.

## MISREPRESENTATIONS

**The developmental position.** “they are truth-seekers” invites readers to hear a categorical contrast between truth-oriented children and merely reproductive machines. Yiu, Kosoy and Gopnik’s distinction concerns complementary functions of innovation and cultural transmission. Children are neither invariably accurate nor independent of cultural learning.

**The remaining developmental gap.** “What it lacks is the urge to start them” presents initiation as the residual difference after experimentally grounded learning has been established. The reported pilot does not settle intervention quality, causal abstraction, robustness to changed rules or broad transfer. Those are central parts of the developmental comparison, not incidental qualifications.

**The curiosity criterion.** “By that test” attributes more to Kidd and Hayden than their behavioral approach establishes. “Without being asked to” is the author’s proposed operational condition and should be identified as such.

**The critics.** “fully trustworthy and explainable before it counts as safe or valuable” needs an identifiable holder. Without one, readers are being invited to reject an opponent whose actual commitments have not been shown.

**The status of the evidence.** The local pilots, working papers, preprints and published studies do not have interchangeable evidential status. Automated source checks cannot establish that a study’s design warrants the inference drawn from it. I cannot independently verify the supplied 2026 references here; their summaries should not be treated as independently confirmed by this review.

## WHAT THE PIECE GETS RIGHT THAT YOUR SIDE SHOULD CONCEDE

Human fallibility and opacity belong in the comparison. Prompting and external memory do not, by themselves, disqualify a system from genuinely learning or conducting informative experiments.
