# Outside review: Rhea Castellan

_Substrate: openai/gpt-6.1-sol. Piece: 04-personality-for-outside.md. Finish: stop._

## VERDICT

The recommendation to test pleasantness against candour survives, but the central division—personality improves the relationship, not the work—does not. The piece turns heterogeneous and sometimes null findings into a categorical conclusion, then treats benefits to use, trust and collaboration as separate from work even though they can improve or damage its results.

## OBJECTIONS

### 1. The main conclusion is stronger than the evidence permits

“So the question ‘does personality improve output?’ has an answer, and it's no.”

This does not follow from “It does not reliably improve the work.” Failure to establish a general benefit is not evidence that there is no benefit. More fundamentally, the studies described concern different interventions and outcomes: robot appearance, role instructions to a language model, relational dialogue and exercise adherence. They do not isolate one common variable called “personality.”

The strongest objection is that the piece changes both the intervention and the outcome while presenting a single verdict. A persona prompt could leave model accuracy unchanged while a conversational manner helps a person disclose missing information, notice an error or finish a task. Conversely, a more engaging assistant could make an unchanged answer more damaging by encouraging reliance.

Bickmore and Picard (2005, *ACM Transactions on Computer-Human Interaction*) study relational interaction; Zheng et al. (2024, *Findings of EMNLP*) study persona prompting. Those are not interchangeable tests.

The developmental perspective makes another missing outcome visible: discovering which question to ask or intervention to try. Lucas et al. (2014, *Cognition*) examine learning unfamiliar causal relationships, not merely retrieving correct answers. Yiu, Kosoy and Gopnik’s paper, initially published in 2023 and appearing in the 2024 volume of *Perspectives on Psychological Science*, distinguishes cultural transmission from innovation. Neither supplies evidence for workplace personality; both caution against treating factual-answer accuracy as the whole of cognitive work.

**Change:** Qualify the conclusion to the interventions and outcomes actually studied. Separate answer accuracy, individual task performance, collaborative discovery and longer-term workplace results. Concede that the evidence presented does not establish the title’s general division.

### 2. The proposed separation between warmth and judgement is a requirement, not an established capability

“Personality belongs in phrasing, small talk, humour and name. It never touches candour, accuracy or the willingness to disagree. Those stay fixed at every setting.”

Your own account of the warmth study suggests precisely that these dimensions do not automatically stay separate. Presenting their separation as an available setting understates the engineering and evaluation problem.

The strongest version of this objection is that politeness, agreement, confidence, qualification and disagreement are partly expressed through the same language choices. The boundary between manner and epistemic content is not clean. A softened warning can communicate less urgency even when its factual propositions remain unchanged.

Sharma et al. (2024, *International Conference on Learning Representations*, “Towards Understanding Sycophancy in Language Models”) provide relevant evidence that preference-based training can favour agreement with users over truthfulness. That does not establish an inevitable warmth penalty, but it undermines any presumption that the dimensions are independently controllable.

Also clarify “with the content held constant.” Was content matched in the training examples, or held constant in the evaluated answers? Those are different claims. I cannot independently verify the 2026 article here; this objection assesses your summary conditionally.

**Change:** Label fixed candour and accuracy as acceptance criteria, not demonstrated properties. Add checks for omitted corrections, weakened warnings, misleading confidence and appropriate disagreement—not just factual correctness.

### 3. Engagement and trust are not unqualified benefits

“The working day is an outcome in its own right: how it feels, whether you come back, whether you trust and use what you have.”

Feeling better is a legitimate outcome. Returning, trusting and using are not automatically beneficial outcomes. Later, the piece correctly identifies those same measures as signals that can reward harmful sycophancy.

The strongest objection is an identification problem: increased use could mean that a useful tool became easier to access, or that an unreliable tool became harder to resist. Increased trust could mean better calibration or worse calibration. Without distinguishing these, the positive and negative sections count the same behaviour differently according to the surrounding story.

Lee and See (2004, *Human Factors*, “Trust in Automation: Designing for Appropriate Reliance”) distinguish appropriate reliance from simply increasing trust. Parasuraman and Riley (1997, *Human Factors*) distinguish use, misuse and disuse.

**Change:** Separate enjoyment from engagement, and engagement from beneficial reliance. Add measures of when people accept, challenge, verify or reject the assistant’s advice. Concede that greater use can improve or worsen the work even without changing answer accuracy.

### 4. User control is presented as better supported than it is

“This is the best-supported part: let the person set how much personality they want.”

The cited research concerns preferences about boundaries between work and nonwork life. It does not directly establish the effects of user-selected AI personalities.

The strongest objection is that preference matching is not necessarily welfare matching. A person may prefer precisely the reassuring, agreeable setting that makes them less likely to scrutinise advice. Your later discussion of sycophancy supplies a reason not to assume that user choice solves this problem.

Rothbard, Phillips and Dumas (2005, *Organization Science*) and Kreiner (2006, *Journal of Organizational Behavior*) support claims about work–nonwork boundary preferences and fit. They do not, by themselves, establish the benefits or safety of adjustable AI warmth.

**Change:** Qualify this as a design inference rather than the best-established empirical conclusion. Distinguish control over humour, verbosity and greetings from control over reassurance, agreement and relational intensity.

### 5. The workplace displacement risk is named, not covered

“Two of its mechanisms do carry over to work, warmth trading against accuracy and an AI assistant quietly taking the place of colleagues, and both are covered above.”

The second mechanism has not been covered above. The piece establishes that relationships between colleagues matter, but does not examine whether an appealing assistant strengthens those relationships, substitutes for them or changes access to help and informal learning.

The strongest objection is that an intervention could improve the user’s immediate experience while weakening their human support network. For a novice, asking an assistant instead of a colleague may also remove occasions for correction, mentoring and learning how the workplace actually operates. The direction of the effect is an empirical question.

“No citation”: the piece supplies no evidence establishing the displacement mechanism or its consequences. Nor does it supply comparative evidence for “most of the documented harm sits there,” which would require specifying what counts as harm and what literature was searched.

**Change:** Cut the claim that displacement is already covered. Add it as an unresolved workplace outcome, and qualify the assertion that harm is concentrated in companionship contexts.

### 6. The stated verification process does not support the strongest literature claims

“None exists yet.”

“Nobody has tested a known persona over months.”

“the subscale figures come from a secondary summary”

A process that checks whether cited sources support sentences cannot establish that relevant uncited studies do not exist. Restricting this piece to the sources in one earlier document makes the universal absence claims especially vulnerable.

The “known persona” claim also needs a definition. Knowing that an agent is artificial, knowing that its manner was deliberately designed, and being explicitly told how that manner is intended to influence you are different conditions. Existing relational-agent research cannot be excluded merely because it uses different terminology.

The comparison between shared goals and emotional bonds needs the original analysis. Different coefficient sizes—or one significant result and one nonsignificant result—do not alone establish a reliable difference between predictors. Gelman and Stern (2006, *The American Statistician*) explain this general statistical error. That does not show your comparison is wrong; it shows why the secondary summary is insufficient.

Two AI judgements also do not constitute two independent replications of source verification.

**Change:** Qualify absence claims to the literature searched. Define the disclosure condition you mean. Check the original subscale analysis and report its domain and uncertainty. Describe the AI checking process as assistance with verification, not a substitute for inspecting pivotal sources.

## MISREPRESENTATIONS

### Developmental science

The piece does not actually state Gopnik’s developmental position, so there is no direct misrepresentation of it to identify. It would be equally mistaken to recruit the “little scientist” literature as evidence that personable AI improves workplace results. Its relevant challenge is narrower: learning includes exploration, intervention and revision of causal hypotheses, which your treatment of “the work” largely leaves out.

### Common ground is not simply memory

“In an assistant, that comes from memory, not personality.”

Clark and Brennan (1991, “Grounding in Communication,” in *Perspectives on Socially Shared Cognition*) describe an interactive achievement: establishing sufficient mutual understanding through acknowledgements, clarification, repair and other coordination processes. Stored information can help, but memory is neither sufficient nor the whole mechanism. Conversational manner may affect whether people expose misunderstandings or request clarification; that possibility needs testing, not exclusion by definition.

### Psychological safety is not an argument against warmth

“Edmondson, who named psychological safety”

Edmondson did not originate the term; Kahn (1990, *Academy of Management Journal*) used it before her 1999 paper. More substantively, Edmondson’s distinction between psychological safety and cohesion does not make warmth the opposite of candour. Her account concerns whether interpersonal risks such as admitting mistakes and challenging assumptions are safe. The relevant contrast is supportive interaction versus pressure to maintain agreement, not friendliness versus truth.

### Authenticity in human service work does not settle disclosed AI design

“The human research says authenticity, not amount, is what lands”

Hennig-Thurau et al. (2006, *Journal of Marketing*, “Are All Smiles Created Equal?”) study emotional displays and service relationships. That does not justify the general contrast “authenticity, not amount,” still less establish what happens when users knowingly interact with a designed AI persona. Identify the particular finding and preserve the difference between perceived human sincerity and disclosed artificial presentation.

### Aristotle does not reserve friendship exclusively for virtue

“Calling it a friend is where the claim stops holding.”

Your preceding sentences acknowledge Aristotle’s friendships of utility and pleasure. His taxonomy therefore cannot, by itself, establish that only virtue friendship warrants the word. You may argue that AI friendship language is misleading for other reasons, but the conclusion needs that argument rather than an unexplained shift to the most demanding category.

## WHAT THE PIECE GETS RIGHT THAT YOUR SIDE SHOULD CONCEDE

Pleasant interaction can have value without increasing factual accuracy. Neither users’ liking nor their willingness to return establishes that an assistant is helping them judge or act better.
