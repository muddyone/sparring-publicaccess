# Outside review: Rhea Castellan (the developmental scientist)

_Substrate: openai/gpt-6.1-sol. Finish: stop._

## VERDICT

The minimal argument survives: a model-plus-memory system can learn in a defensible functional sense, without changing its weights. The larger argument does not yet survive: Gopnik’s central contrasts are already functional, and the exploratory study does not establish that written memory closes the relevant gap in causal learning.

## OBJECTIONS

### 1. The main opponent is misidentified

“Both of us overreached, and in the same way: we each leaned on form.”

“Her contrasts mostly dissolve when you look at children closely.”

The objection is that Gopnik’s published argument is not principally about biological substrate, childhood, or resemblance to human learning. It concerns capabilities: generating informative evidence, discovering causal structure, and extending knowledge beyond the examples supplied. Your later acknowledgment that her distinction “was never learning versus not learning” undercuts this earlier accusation.

The strongest version of her position is this: two systems may both learn statistically while differing substantially in what they learn, from which evidence, through whose experimental choices, and with what capacity to generalize. Calling both “pattern learners” does not dissolve any of those differences. Bayesian inference is a framework within which those differences can be specified, not evidence against their importance.

Published basis: Yiu, Kosoy and Gopnik, 2023, *Perspectives on Psychological Science*; Gopnik and colleagues, 2004, *Psychological Review*, “A theory of causal learning in children: Causal maps and Bayes nets.”

Change: **Concede** that Gopnik’s central contrast is already functional. **Cut** the claim that her contrasts mostly dissolve. If you retain a criticism of substrate-based objections, identify advocates who actually make them rather than treating Gopnik as their representative.

### 2. The pilot supports useful persistence, but does not yet identify the claimed learning process

“Claude formed the expectation Gopnik’s children form, and its notes held it, like the rats’ map, until the next machine called for it.”

The reported result is compatible with learning an abstract expectation about causal structure. But the evidence supplied does not distinguish that interpretation from several narrower possibilities: preserving an effective instruction, retaining otherwise unavailable task history, or exploiting a regularity specific to this task generator.

The strongest objection is not that a textual rule cannot be an overhypothesis. It can. The question is whether the system learns an expectation about new cases from the distribution of earlier cases, and revises that expectation appropriately when the distribution changes. A successful final “needs two” trial after exclusively “needs two” training does not establish that whole functional profile.

Published basis: Kemp, Perfors and Tenenbaum, 2007, *Developmental Science*, “Learning overhypotheses with hierarchical Bayesian models”; Lucas and colleagues, 2014, *Cognition*. The pilot itself is not independently assessable from the linked material supplied here.

Change: **Qualify** the interpretation. **Add** matched histories dominated by each rule, mixed histories, and tests of appropriate reversal. Compare abstract notes with retained transcripts and equally long task-irrelevant notes. Lock prompts, scoring, generators and analysis—not merely fresh seeds. A failed replication would count against this implementation, not establish a general limitation of written memory.

### 3. Active exploration is treated as a possible later complication when it belongs at the centre

“If acting on the world, rather than learning continuously, turns out to be the real edge, Gopnik’s emphasis on exploration is the deeper point, and my functional framing undersells it.”

This makes an established distinction sound like an unresolved alternative that might eventually become relevant. The developmental literature already distinguishes receiving observations from selecting interventions that resolve uncertainty.

The strongest objection is that final accuracy can conceal the capability under dispute. A learner may eventually answer correctly while choosing redundant tests, failing to separate competing explanations, or needing much more evidence. Your own summary reports poorer exploration efficiency, then gives greater interpretive weight to closing accuracy gaps.

This does not require a body, biological needs or personal stakes. Choosing interventions in a simulated blicket world can count as active causal exploration. Conversely, manipulating physical objects does not by itself establish good experimental reasoning.

Published basis: Gopnik and colleagues, 2004, *Psychological Review*; Schulz and Bonawitz, 2007, *Developmental Psychology*, “Serious fun: Preschoolers engage in more exploratory play when evidence is confounded.”

Change: **Add** intervention quality, evidence efficiency and transfer as primary outcomes. **Concede** that these are functional differences already central to Gopnik’s account, not exceptions to your framing.

### 4. The framing manipulation changes the inference problem; it does not straightforwardly reveal or remove a bias

“With both rules named on every machine, neither model carried the rule.”

“My task removed it, since the prompt named both possible rules up front.”

Neither conclusion follows simply from naming the alternatives. Knowing that two hypotheses exist does not eliminate a prior preference between them. Conversely, treating successive machines independently may be appropriate if the instructions imply independent rule assignments.

The strongest objection is that you have not separated uncertainty about an individual machine from uncertainty about what machines in this environment usually do. That distinction is precisely what an overhypothesis addresses. Repeatedly presenting both rules might suggest that each new machine resets the problem; leaving them unnamed might encourage a shared explanation across machines. Those are different assumptions about the environment, not merely different packaging of identical evidence.

Lucas et al.’s important result concerns how experience with causal form changes subsequent generalization. “Adults struggle with conjunction; children do better” is an incomplete account of that result.

Published basis: Lucas, Bridgers, Griffiths and Gopnik, 2014, *Cognition*; Kemp, Perfors and Tenenbaum, 2007, *Developmental Science*.

Change: **Add** the exact instructions and clarify how rules were generated across machines. **Qualify** “neither model carried the rule” unless the evidence warranted expecting transfer. **Cut** the implication that naming both hypotheses by itself removes the relevant bias.

### 5. The system boundary expands whenever necessary, weakening attribution

“It is the whole system: the model, its memory and notes, and the upgrades it receives.”

“That is like watching a second grader and concluding children don’t learn, since a second grader never knows more than a second grader.”

External memory and externally supplied upgrades should not be bundled together without argument. A system that writes and retrieves its own records presents one attribution problem. A product replaced or modified by engineers using additional training data presents another.

The strongest objection is that a sufficiently expansive boundary can make almost any improved artefact a learner. That does not render system-level learning illegitimate, but it requires identifying whose experience causes which change, and which component performs the adaptation. Otherwise, the argument slides between a conversational agent learning and a development organisation improving its product.

The second-grader analogy also misses its target. A frozen checkpoint is not merely an age category containing an individual who continues changing internally. Nevertheless, frozen weights do not rule out learning through context or external memory.

Published basis: Clark and Chalmers, 1998, *Analysis*; Brown and colleagues, 2020, *NeurIPS*, “Language Models are Few-Shot Learners.”

Change: **Separate** pretraining, within-context adaptation, persistent external memory and developer-led retraining. **Cut** the second-grader analogy. Defend the memory-equipped agent as the learner without automatically annexing its entire development pipeline.

### 6. The learning-profile comparison understates functional differences and contradicts its own definition

“Most of these differences are form: the same function, reached another way.”

“For knowledge work, where nearly everything can be written, that gap is small.”

The table includes differences in automaticity, retention, retrieval dependence and acquisition of skills. Those are differences in learning function, not simply differences in storage material.

The strongest objection is that expressibility is not sufficient for effective learning. A procedure can be fully described yet remain difficult to execute reliably, retrieve at the right moment, combine with other procedures, or apply under distraction. Writing down a rule does not establish that these problems are small. Knowledge work includes tacit discrimination and practical judgment, not just facts that can be recorded.

There is also an internal tension: if learning is defined functionally, an assistant that reliably improves a skill through stored instructions has learned something procedural in the relevant functional sense. You cannot simultaneously insist that storage location is immaterial and declare that such improvement must remain merely factual.

Published basis: Anderson, 1982, *Psychological Review*, “Acquisition of cognitive skill.”

Change: **Qualify** the table as a description of particular assistant architectures, not a general learning taxonomy. **Cut or support** the claim that the gap is small for knowledge work. Distinguish successful execution from storing a description of successful execution.

### 7. The benchmark comparisons cannot bear the historical conclusion placed on them

“Those were 2022–23 models, and newer ones have closed most of that gap.”

“with step-by-step reasoning was not significantly different from humans”

Failure to detect a difference is not evidence of equivalence. Nor does improvement on newly written tool-choice questions establish that the original functional contrast has mostly disappeared.

The strongest objection is that comparable percentages can conceal differences in participants’ ages, item difficulty, prompting, exposure and scoring. Selecting a plausible tool from verbal alternatives is also narrower than discovering a useful tool through exploration. The piece needs to specify which gap has narrowed: performance on this item format, not innovation generally.

Published basis: Altman and Bland, 1995, *BMJ*, “Absence of evidence is not evidence of absence.” I cannot independently verify the cited 2025–26 papers, interview or pilot files from the supplied text; assessments of their findings here are conditional on your summaries.

Change: **Qualify** the historical conclusion, report uncertainty and matching conditions, and distinguish preprints from journal publications. **Add** an equivalence analysis if equivalence is the intended claim.

## MISREPRESENTATIONS

### Bayesian learning is not a concession that the differences dissolve

“Her own theory of children is statistical: Bayesian learners weighing evidence, which is pattern learning over interventions rather than over text.”

This compresses away the explanatory substance of the theory: structured hypotheses, interventions, distinctions between observation and action, and learning about how evidence was generated. These are not cosmetic qualifications to generic pattern recognition. Gopnik and colleagues, 2004, *Psychological Review*, makes those distinctions central.

### Cultural learning is not simply imitation

“Most human learning is imitation too.”

No measure or evidence supports “most,” and imitation is not interchangeable with social learning. Learning from testimony, selectively trusting an informant, and inferring what a teacher intends are not simply copying. Nor does substantial human dependence on culture rebut a claim about distinctive capacities for causal discovery. Relevant published work includes Harris, 2012, *Trusting What You’re Told*, Harvard University Press.

### Tolman’s rats are made to establish more than they establish

“And a note that sits unused until it’s needed is what Tolman’s rats had: knowledge waiting for its moment.”

Tolman’s work supports distinguishing acquisition from immediate performance. It does not establish equivalence between a stored note and a cognitive map. Clark and Chalmers provide an argument for counting suitably integrated external resources as memory; they do not experimentally establish equivalent learning capabilities. The analogy should be identified as an analogy, not treated as corroboration.

### H.M.’s impairment is overstated and the “opposite profile” is misleading

“H.M., could form no new memories of facts or events”

“A memory-equipped assistant has roughly the opposite profile.”

H.M. had profound, selective memory impairments, not an absolute inability to acquire any new factual information. More importantly, the assistant comparison contrasts an experimentally characterised human memory disorder with an architectural description of a software system. It does not demonstrate a reverse dissociation between independently tested learning systems. Qualify both claims. Relevant sources are Squire, 2009, *Neuron*, and Corkin, 2002, *Nature Reviews Neuroscience*.

## WHAT THE PIECE GETS RIGHT THAT YOUR SIDE SHOULD CONCEDE

Persistent, usable external memory can support genuine learning; neither neurons nor weight updates are necessary. A textual rule can also carry an abstract expectation across tasks—the unresolved question is how reliably, efficiently and appropriately it does so.
