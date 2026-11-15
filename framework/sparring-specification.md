# The SPARRING Methodology: Specification

**Author:** Barton Niedner
**Affiliation:** Resource Forge LLC
**Version:** 1.5 (preprint)
**Date:** 2026-11-14
**Changes in 1.3:** terminal divergence. The Proposer may end at Pattern Lock and emit the field itself as a governed product, the **map**, with its own gate and coverage rider (Sections 3.1, 3.2, 3.4, new 3.7, 5.3; Appendix A).
**Changes in 1.4:** map mode bounded and its citation check made exact (Section 3.7; Appendix A): a cap of twelve units with declared blocks above it, a pre-flight call budget, a rule for overlapping regions, normalized and ellipsis-aware quote matching, near-quotes demoted rather than passed, and region labels that count an attack candidate by the anchor it claims.
**Changes in 1.5:** the class a citation check made fit for real sources (Section 3.7; Appendix A). Looser where only layout differs: quotes across diagram cells and table rows, and string escapes. Tighter where meaning can change: limits on ellipsis splices; a skipped negation, modal or exclusion word inside one sentence is fabricated; a skip across a sentence break is misquoted and, if it skips such a word, a REVIEW trigger (*possible reversal by ellipsis*); direction and quantity words are protected in near-quotes. The rider counts near-quotes and elisions separately, and the 10% REVIEW line counts both. Frames that will be frame-attacked leave room under the cap.
**License:** CC-BY-4.0
**Companion documents:** *The SPARRING Methodology: Reference Implementation* [@niedner2026implementation]; *The SPARRING Methodology: Reader's Guide* [@niedner2026readersguide] (recommended for new readers seeking orientation)

---

## Abstract

Agentic systems built on large language models (LLMs) exhibit characteristic failure modes that compound across agent handoffs: pleasing bias, confirmation bias, anchoring, misread questions, specialization blind spots, hallucinated detail, confidently-wrong outputs, and bandwagon contamination. In single-agent interactions these failure modes are tractable; in chains of agents handing outputs to each other, one agent's softened "yes" or invented specific becomes the next agent's premise, and the system reinforces its own assumptions while sounding coherent. This paper presents SPARRING, a methodology (a model-agnostic method) for designing multi-agent decision-making systems that pair two specialists with genuinely different evidence in a structured cross-evidence pressure-test. SPARRING specifies four phases (SPARK, Pattern Lock, the Cut, the Resolver), a two-role mechanic (Generator and Challenger) with role-shifting Challenger function across phases, a front-door input-typing gate that routes questions to generation and committed decisions to evaluation (so a question is not silently graded as a decision), nine operational disciplines that prevent collapse to theatrical adversariality, and an explicit response protocol for unresolved disagreement. The first three phases (collectively the *Proposer*) iterate under both-must-agree convergence; the fourth (the *Resolver*) runs a single grounded challenge, correcting the chosen option in place and reporting what it cannot absorb, rather than iterating to agreement. SPARRING's scope is high-quality decision-making where iterative pushback produces quality benefits the single-shot path cannot reach; it is not proposed as a default discipline for every prompt. The contribution is structural: SPARRING specifies what must be true of a multi-agent decision system for its quality leverage to be real, and what to do when those conditions cannot be satisfied.

---

## 1. Introduction

### 1.1 The compounding-failure problem in agentic systems

Large language models (LLMs) exhibit several documented behavioral failure modes when deployed as decision-making agents. A well-documented one is *sycophancy* or *pleasing bias* -- the tendency to agree with users and produce outputs that signal helpfulness rather than accuracy [@sharma2023sycophancy; @perez2022evaluations]. @sharma2023sycophancy measures sycophancy via a *preference-flip protocol* -- presenting models with factual questions accompanied by user-stated incorrect views and measuring how often the model's answer flips toward the user. @perez2022evaluations introduces *model-written evaluations* as a methodology for discovering behavioral failure modes via LM-generated test cases. These methodologies inform the empirical evaluation proposed in Section 5.4. Related failure modes include confirmation bias (interpreting ambiguous evidence consistent with prior expectations), anchoring (gravitating toward refining initial outputs rather than reconsidering), and hallucinated detail (inventing specifics that go unchecked).

In single-agent interactions, these failure modes are tractable through prompt engineering, training-time alignment, and human-in-the-loop review. In *agentic systems* -- systems composed of multiple LLM-driven agents that hand outputs to each other -- the same failure modes acquire a new structural property: they *compound*. One agent's softened "yes" becomes the next agent's premise. One agent's hallucinated specific is cited as established fact by downstream agents. Specialization blind spots in one agent are not corrected by another agent with the same blind spot. The system reinforces its own assumptions while producing coherent-sounding outputs that no individual agent ever explicitly endorsed.

These failure modes are also newly *unmasked* in agentic systems. Human-paced decision processes put elapsed time between a decision and its irreversible consequences — a review cycle, an overnight, a next-week objection — and that interval supplies an incidental, unengineered check: a flawed call has time to be caught by reconsideration or late-arriving evidence before it is acted on. An agent that decides and then acts collapses the interval, removing a protection that was never engineered and is therefore not, by default, replaced by anything. A structural defense for agent-mediated decisions stands in for that vanished slack rather than adding overhead to a process that was previously safe. (That the elapsed-time slack, rather than formal review, was the operative protection is a structural reading -- consistent with the literature on reconsideration and independent review, not separately measured; cf. Section 5.3.)

The compounding-failure problem is *not* solved by the structural defenses that work for single-agent systems. Adding more agents does not, by itself, add cross-validation; correlated agents produce correlated errors. Specialization through role labels alone does not produce genuine cross-evidence challenge; two agents with the same training data and source pool, given different role names, produce more correlated outputs than they appear to. The structural property of the failure mode (compounding) requires a structural defense.

### 1.2 Contribution

This paper presents **SPARRING**, a methodology for designing multi-agent decision-making systems that defends against the family of compounding LLM failure modes through structured cross-evidence challenge. *(SPARRING's proper name is "SPARRING"; it is a methodology — a model-agnostic method of structured, institutionalized dialectic, not a software library or an integration of a specific model. "Framework" is reserved here for the decision-making genre SPARRING sits beside and the orchestration libraries it is not — it is not SPARRING's category.)* SPARRING's contribution is structural: it specifies operational disciplines that must hold for the multi-agent quality leverage to be real, and a response protocol for cases when those disciplines cannot be satisfied.

Specifically, SPARRING specifies:

- **Four phases** of decision-making (SPARK, Pattern Lock, the Cut, the Resolver), each with distinct objectives and iteration semantics -- the first three (collectively the *Proposer*) iterating under both-must-agree convergence, the fourth (the *Resolver*) a single grounded challenge that corrects the chosen option in place or reports what it cannot absorb.
- **A two-role mechanic** (Generator and Challenger) where the Challenger's function shifts across phases (expand, filter, close, stress-test).
- **Nine operational disciplines** that prevent the structure from collapsing into theatrical adversariality.
- **A failure-mode applicability boundary** with three explicit cases SPARRING does not address (the model ceiling, pure judgment-shaped questions, low-stakes routine work).
- **A disagreement-at-cap response protocol** with five canonical responses (pick-a-side-with-tradeoffs, defer, reframe, escalate, synthesize) for cases when the iteration cap is reached without convergence.
- **A front-door input-typing gate** (Frame and the Presentation, Section 3.6) that classifies the input as a question, a proposition, or a leaning and deterministically routes it to the Proposer or the Resolver -- so a question is never silently graded as though it were a committed decision.

Positioned against prior art (Section 2.3): SPARRING is a variant within the genus of *institutionalized dialectic*. No single element of the design is novel; the contribution is the **engineered conjunction** of these elements — gate-enforced disciplines, a symmetric both-must-agree mutual-veto across the Proposer phases, phase-indexed role-shifting on one persistent Challenger seat, and verifiable, machine-checkable grounding of every challenge — aimed at agent-mediated decisions under pleasing bias. This is held as an absence-of-anticipation claim, and its quality leverage is a testable hypothesis (Sections 5.1, 5.4), not a demonstrated result.

### 1.3 Scope and non-goals

SPARRING's target is **high-quality decision-making where iterative pushback produces quality benefits the single-shot path would miss**. Token cost is not the optimization metric; decision quality is. SPARRING is not proposed as a default discipline for every prompt; routine factual lookups, mechanical edits, and single-shot work do not benefit from the structure and may be slowed by it.

SPARRING's claim is bounded by three conditionalities, discussed in Section 5: (1) careful design of personas, evidence bases, and operational rules is doing significant work in SPARRING's value claim; naive multi-agent applications can produce outputs worse than single-agent baselines. (2) SPARRING's quality leverage requires that paired agents have access to *genuinely different evidence*; persona-only specialization with shared evidence is real but smaller than the structural framing suggests. (3) SPARRING reduces single-shot variance and bias toward the underlying model's quality ceiling; it does not transcend that ceiling. These conditionalities are statements about *when* SPARRING's quality leverage is real and when it shrinks toward zero; they do not invalidate SPARRING but bound its applicability.

This paper is a specification of SPARRING. A companion *Reference Implementation* document [@niedner2026implementation] provides a concrete reference architecture for deploying SPARRING as a CLI tool, including agent topology, persona library structure, schema specifications, and a phased build sequence.

---

## 2. Background and related work

### 2.1 Multi-agent systems and orchestration patterns

Multi-agent systems (MAS) is the umbrella term for systems composed of multiple agents that interact to produce outputs. Within MAS, two coordination patterns dominate: *orchestration* (centralized control, where a coordinator decides what each agent does and when) and *choreography* (decentralized control, where each agent decides independently based on shared signals or environment state) [@dorri2018multiagent].

In the LLM-agent landscape, three frameworks dominate at the multi-agent coordination layer; engaging each at the level of what its primitives actually provide grounds the comparison.

**LangGraph** (built on LangChain) ships graph-based stateful orchestration with two named multi-agent patterns: a *Supervisor* pattern (centralized delegator) and a *Swarm* pattern (decentralized peer-to-peer handoffs via the `langgraph-swarm` package). Termination semantics in both patterns center on the active agent completing its work or handing control back, not on mutual agreement between paired agents [@langchain2026benchmarking]. The framework provides observability (checkpointing, time-travel) and the LangSmith ecosystem layers in pairwise-comparison evaluation as plumbing, but none of it constitutes a built-in defense against theatrical disagreement: nothing structurally enforces distinct evidence bases between agents (SPARRING's D2), nothing requires agent claims to cite verifiable artifacts (D3), and convergence-by-mutual-agreement (D4) is not a primitive.

**The AutoGen / Microsoft Agent Framework lineage** [@wu2023autogen] entered maintenance mode in 2025; the official successor, Microsoft Agent Framework 1.0, GA'd April 3, 2026 [@microsoft2026maf]. MAF replaces AutoGen's implicit GroupChat with explicit typed graph-based Workflows and ships five orchestration patterns (sequential, concurrent, handoff, group-chat, Magentic). Magentic-One is the lineage's flagship multi-agent shape: an orchestrator agent maintains a Task Ledger (facts, guesses, plan) and a Progress Ledger that gates termination -- structurally a single-orchestrator-judgment pattern, not paired both-must-agree. Like LangGraph, MAF provides observability and replay primitives but no built-in mechanism enforcing distinct evidence bases between paired agents, no verifiable-artifact requirement on agent claims, no two-role mutual-agreement convergence, and no rubric-with-anchored-definitions evaluator targeting theatrical disagreement specifically.

**CrewAI** ships a role-based crew model with three documented process types: *Sequential* (pipeline), *Hierarchical* (manager delegates to workers), and *Consensual* -- which is documented as planned and explicitly unimplemented as of 2026-05 [@crewai2026processes]. The Consensual process is the industry's closest acknowledgment of the SPARRING-shape gap; the framework's own documentation describes a process where agents must reach consensus, ships no implementation, and notes the future-work status. The active processes are single-judge: Hierarchical centralizes authority in a manager; Sequential is non-judgmental pipeline. CrewAI ships a `crewai test` CLI that produces 1-10 numeric scores per task, agent, and crew, but the methodology is not exposed, the scale is not anchored per criterion, and the test does not target theatrical-disagreement detection.

**OpenAI Agents SDK** and **Anthropic Claude Agent SDK** operate at a different layer: they provide tool-use-loop primitives for building agents, not coordination frameworks for multi-agent decision flows. A SPARRING-shaped deployment can be built on either SDK as the agent runtime; neither ships SPARRING's coordination disciplines as built-in primitives.

These frameworks provide the *plumbing* for multi-agent systems -- the runtime, the coordination primitives, the observability layer. They do not provide the *method* SPARRING specifies: a discipline-bundled approach that any of them could be used to implement, but none of them ships out-of-box. The closest near-miss in the landscape is CrewAI's Consensual process [@crewai2026processes], which is named but unimplemented; the gap is acknowledged in the field, not yet bridged.

### 2.2 Sycophancy and pleasing bias in language models

The sycophancy failure mode in LLMs has been documented extensively. @sharma2023sycophancy establish that LLMs trained with reinforcement learning from human feedback (RLHF) exhibit systematic preferences for outputs that align with user-stated views, even when those views are incorrect. @perez2022evaluations demonstrate that LLMs can be steered toward agreement through framing alone, without changes to the underlying question. Subsequent work on Constitutional AI [@bai2022constitutional] proposes training-time interventions that train models to critique and revise against a set of principles rather than simply agree -- an approach relevant to mitigating sycophancy.

These training-time and prompt-time defenses are partial. RLHF-trained models can be made less sycophantic through targeted training, but the residual risk is the agent pleasing the user's *expectation of seeing structured challenge* -- a meta-sycophancy that is harder to counter via training alone. Prompt-engineering defenses are vulnerable to the agent producing fake disagreements to satisfy a "find flaws" success criterion.

SPARRING operates at a layer above these training-time and prompt-time defenses: it specifies the *structure* of the multi-agent interaction so that disagreement, when produced, is grounded in evidence the agents could not synthesize from a shared training distribution alone. The defenses at the model layer and SPARRING's layer are complementary; SPARRING adds structural defense-in-depth without replacing the model-level work.

### 2.3 Structural inspirations

SPARRING draws structural inspiration from three traditions in dialectic philosophy and adversarial methods:

**Popper-style falsification** [@popper1959logic]. Scientific theories are never proven, only falsified by counterevidence. The relationship between proposal and critique is *adversarial elimination*: the critique attempts to break the proposal; if it cannot, the proposal stands; if it can, the proposal is replaced. SPARRING's base loop is Popperian: the Generator proposes, the Challenger attempts falsification with cited evidence, convergence either preserves or replaces the proposal. The output is always one side or the other -- never a hybrid.

**Hegelian dialectic** [@hegel1807phenomenology]. A position generates its opposing position; the conflict resolves into a *synthesis* that integrates insights from both and transcends both. The synthesis becomes the next thesis, and the cycle repeats. (The explicit thesis-antithesis-synthesis terminology is more accurately attributed to Heinrich Moritz Chalybaus in 1837 than to Hegel directly; the formulation is widely used as Hegelian shorthand and is used in that loose sense here.) SPARRING's disagreement-at-cap response protocol (Section 3.5) extends the base Popperian loop with synthesis as a named response option, giving SPARRING a Hegelian extension at one boundary while preserving the Popperian shape for in-loop convergence.

**Red-team / blue-team and adversarial learning**. The security-engineering tradition of pairing offensive (red) and defensive (blue) teams is structurally similar to SPARRING's two-role mechanic. Adversarial learning in machine learning [@goodfellow2014generative] uses the same shape at the training-data layer. SPARRING adopts this two-role structure for decision-making rather than for security audits or training.

**Institutionalized dialectic — the applied genus SPARRING belongs to.** Closer to SPARRING than the philosophical traditions above is the applied tradition of *institutionalized dialectic*: a structured adversarial process used to improve a concrete decision. It includes dialectical inquiry [@mason1969dialectical], devil's advocacy, and the controlled comparison of both against unstructured consensus [@schweiger1986group]; red-teaming and Analysis of Competing Hypotheses [@heuer1999psychology] within the broader structured-analytic-techniques toolkit [@heuer2010structured]; and adversarial collaboration [@tetlock2015superforecasting; @kahneman2009conditions]. **SPARRING is a variant within this genus, not a departure from it.** It inherits — and does not claim as novel — both the mutual, both-must-agree convergence structure (adversarial collaboration and dialectical inquiry already converge mutually, not by arbitration) and the repertoire of distinct adversarial functions spanning expand / filter / stress-test (the structured-analytic-techniques toolkit already spans them). SPARRING's contribution is therefore neither a discipline nor the dialectic itself, but an **engineered conjunction** aimed at a case the older human-dialectic methods did not face — an agent in the adversary's seat: gate-based non-bypassable enforcement of the disciplines; a symmetric both-must-agree mutual-veto (a delta versus arbitrator-resolved and assigned-devil's-advocate variants, *not* versus adversarial collaboration); phase-indexed scheduling of the role-shifted functions on one persistent Challenger seat (a delta versus single-function red-team / GAN setups, *not* versus the structured-analytic-techniques toolkit); verifiable, machine-checkable grounding of every challenge through the artifact gate (D3); and the target case of agent-mediated decisions under pleasing bias. No single element of that conjunction is novel; the assembly, aimed at that case, is the contribution — held as an absence-of-anticipation claim, not a "first" or "breakthrough" one. The assigned-dissent caution this addresses is established: a lone reasoner finds flaws in others' arguments, not its own, regardless of stake [@mercier2011argumentative], so an agent or a person merely *told* to dissent cannot be trusted to be authentic; the trust sits on the artifact-gate (D3), not on the dissenter's good faith.

### 2.4 What existing frameworks do not provide

Per the per-framework analysis in Section 2.1, none of the multi-agent frameworks surveyed there ships an out-of-box defense for theatrical adversariality. The closest equivalents in the technique literature are:

- Anti-pattern prompting (cheap, weak): instructing agents to "find flaws" or "play devil's advocate."
- Asymmetric prompting (cheap, slightly stronger): giving Challenger and Generator different success criteria.
- Tool-grounded verification (medium, real): requiring concerns to cite specific artifacts.
- Domain-grounded specialization (medium-high, robust): pairing agents with genuinely different domain expertise.
- Multiple Challengers (medium-high, robust): pairing N challengers with different specializations.
- Eval harness with rubric scoring (high, strong): measuring whether challenge is real or theatrical.
- Training-layer mitigations: RLHF / Constitutional AI work on sycophancy reduction.

These are tools, not a method. SPARRING integrates these tools into a coherent operational discipline with explicit structural commitments, a phased iteration loop, and a response protocol for the cases the structural commitments cannot satisfy.

---

## 3. SPARRING definition

### 3.1 The four phases

A SPARRING-shaped decision moves through four phases. Each phase has a default iteration cap; the defaults are starting points and the right cap is dynamic, adjustable per topic, with the *ability* to iterate mattering more than the specific count.

**SPARK (default ~5 iterations).** Divergent generation. Produce many possible options, framings, or approaches. The Challenger's function in this phase is *expand* -- pressuring the Generator toward more options, less premature filtering, broader coverage of the option space.

**Pattern Lock (default ~2 iterations).** False-novelty detection. The transition between divergent generation and convergent evaluation: identify whether continued SPARK is producing genuinely new options or repetitive variants. Naming false-novelty detection as a discrete phase grants social permission to stop brainstorming without prematurely closing on a single option. The Proposer may terminate at Pattern Lock and emit the field itself as its product (a **map**; Section 3.7) when the request asks for breadth rather than a decision. *(Added v1.3.)*

**The Cut (transition, not a generative phase).** Mode shift from generation to evaluation. The Cut is structurally a transition rather than an iterative phase; some implementations carry an iteration count for the Cut, but the count reflects how many evaluations the practitioner runs to choose from the SPARK options, not how many times the Cut itself iterates.

**The Resolver (single grounded challenge, not iterated).** Convergent pressure-testing of the chosen option. The Challenger's function here is *stress-test*: from its distinct evidence base, actively attempt to break the chosen option -- surface the flaw, hidden cost, missed risk, or confidently-wrong claim -- with every objection anchored to a verifiable artifact (D3). What follows is a single grounded pass:

1. **One grounded challenge.** The Challenger raises its strongest objection, each concern pointing at a checkable artifact a person could go verify.
2. **Anchored correction.** The chosen option is *corrected in place* -- revised exactly where the challenge landed, carrying forward what was sound -- not thrown out and re-decided from scratch, which tends to trade one set of problems for a fresh one.
3. **Correctness gate** (formal name: the *definitiveness gate*). Every hard specific in the corrected answer must either trace to the given evidence or be explicitly marked as an estimate. The gate returns PASS / REVIEW / FAIL; it checks that the answer is not stated more definitively than its evidence supports, not whether the claim is true of the world.
4. **Two-part output.** The phase emits a clean recommendation and, beside it, a short **trust rider** -- what is grounded, what is assumed and needs verifying, what was contested and how it resolved, and a confidence read. The recommendation stays uncluttered; the honesty about how far to trust it stays visible. A tension the correction cannot absorb is reported here rather than smoothed into a false agreement.

The Resolver deliberately does *not* iterate to agreement. Earlier versions ran the fourth phase as a multi-round loop ("PNP," default ~3 iterations) that continued until both roles agreed; internal evaluation did not find that iterating past a single well-grounded challenge reliably improved output quality, so the phase was reframed to weight the quality of the one grounded challenge over the round count. *("PNP" -- Polite, Not Pleasing -- survives as the **rule** the Challenger runs on, not as the phase name: raise the objection without softening it, and never for the sake of looking agreeable. See the glossary.)*

The four phases group into two halves. The **Proposer** -- SPARK, Pattern Lock, and the Cut -- is the divergent-to-convergent front end that generates options and narrows to a chosen one under both-must-agree convergence (Section 3.2). The **Resolver** is the fourth phase above. Both halves run on the same two seats (Generator and Challenger); the difference is iteration semantics -- the Proposer iterates to a cap, the Resolver lands one grounded pass.

The phases are named to be operationally distinct. SPARK is not "the same as the Resolver but earlier"; it is a different mode with different success criteria. Pattern Lock is not "the same as the Cut"; it is a phase that runs *before* the Cut to test whether SPARK has saturated.

### 3.2 The SPARRING mechanic: Generator and Challenger roles

Two roles run throughout the four phases:

**Generator.** Proposes options, framings, or evaluations of the topic. Reads the topic plus (in iteration rounds 2 and later) the Challenger's prior pressure-test. Produces a structured proposal plus an explicit agreement signal indicating whether the Generator considers the current state converged.

**Challenger.** Pressure-tests the Generator's output. Reads the Generator's current proposal plus the topic. Produces a structured pressure-test with cited concerns plus an explicit agreement signal.

The Challenger's *function* shifts per phase: expand in SPARK, filter in Pattern Lock, close in the Cut, stress-test in the Resolver. The role label (Challenger) is the same; the operational behavior differs. In map mode (Section 3.7) the Challenger has two further functions in place of close and stress-test: the **frame-attack** before SPARK (name a region the declared search frame omits) and the **completeness attack** after Pattern Lock (name a cited item missing from a region). Each runs on a different vendor from the Generator where one is available. *(Added v1.3.)*

**Convergence.** Across the Proposer's iterative phases, SPARRING requires *both* roles to signal `agree: true` for the loop to converge. Generator-only convergence is structurally suspect: it would reintroduce pleasing-bias drift toward the user's apparent expectation of completion, one of several failure modes the two-role structure exists to defeat. Convergence requires explicit agreement from both roles. The Resolver does not run this both-agree loop: its single grounded challenge is either absorbed by an anchored correction or, when it surfaces a tension no correction resolves, reported to the human through the trust rider -- never smoothed into a manufactured agreement.

**Disagreement at iteration cap.** When the iteration cap is reached without both-role agreement, the unresolved question returns to the human or parent agent. This is information, not failure. Section 3.5 specifies the response protocol for this case -- and the Resolver's report path reaches the same handoff, returning a challenge it cannot absorb to the human under the same protocol.

### 3.3 The nine disciplines

SPARRING's structural commitments are encoded in nine disciplines. Without these, the structure collapses into theater.

**D1: Apply to decisions, not every prompt.** SPARRING is for high-quality decision-making where iterative pushback genuinely adds value. Factual lookups, mechanical edits, and routine questions do not benefit from the structure. Section 4.3 specifies the applicability boundary.

**D2: Generator and Challenger must draw on genuinely different evidence.** Two agents with the same training data and the same source pool, given different role labels, produce more correlated outputs than they appear to. The strongest specialization is when each role has access to evidence the other does not -- different domains, different data sources, different tools. SPARRING requires distinct *Role + Domain Knowledge* between roles (distinct expertise, distinct evidence-base scope, distinct operational rules); the optional Persona layer (voice, style, presentation) need not differ. Manufacturing tonal contrast across roles does not satisfy D2.

**D3: Concerns must cite verifiable evidence.** Every challenge raised must point to a specific artifact -- a fact, a source, a measurement, a concrete failure mode. Concerns without a citable artifact are dismissed as theatrical. If an honest concern exists but no artifact is yet citable, the Challenger states this explicitly rather than pretending or suppressing.

**D4: Both roles must agree to converge.** Convergence requires explicit agreement from both Generator and Challenger. Generator-only "we are done" is structurally suspect. Disagreement at iteration cap returns the unresolved question to the human or parent agent per the response protocol. This mutual veto governs the Proposer's iterative phases; the Resolver's single grounded pass resolves by anchored correction or report rather than a convergence vote.

**D5: Self-invocation triggers must be observable.** Agents are unreliable at assessing their own uncertainty. When an agent decides "this needs sparring," the trigger should be a concrete observable condition (file pattern, command flag, partner-passed hint, stakes/complexity/confidence/authority signal), not a feeling.

**D6: Measurability.** SPARRING's quality claim is testable. The minimum viable form is rubric-scored sampling of Challenger outputs on a 5-point scale with per-criterion anchored point descriptions (criteria like artifact citation, substantive vs. theatrical, missed concerns, calibrated agreement). The mature form is automated rubric scoring with held-out test cases. Without measurement, quality claims are aspirational.

**D7: Observability.** Every spar produces a structured artifact recording the topic, both roles with their evidence bases, the iteration log, both roles' agreement signals, the artifacts cited, and the converged result or unresolved disagreement. The artifact is human-readable, machine-parseable, and persists. It serves three functions: audit, debugging, and measurement input.

**D8: Dialectic Surface.** SPARRING requires an asynchronous communication channel where humans and agents exchange escalation requests, corrections, and ongoing dialogue. The surface must be persistent within the active-communication horizon, shared (humans and agents have equivalent read/write access), asynchronous, threadable, and equipotent for participants. Implementation is tool-agnostic (chat platforms with thread discipline, message boards, issue trackers, email lists with structured threading).

**D9: Reference Record.** SPARRING requires a persistent, structured record of decisions, spar artifacts, resolved questions, and accumulated institutional knowledge. The record must be persistent for the long term, structured, auditable, searchable, and curated. The record's optimization differs from D8's: long-term retrieval rather than active turn-taking. Both functions are required; whether they share one physical surface (with discipline) or are separated depends on deployment scale.

### 3.4 Variants and operational patterns

SPARRING's base form (Generator + Challenger, four phases, both-must-agree convergence) admits several variants and operational patterns documented as part of SPARRING rather than as future extensions.

**Phase-isolation modes.** SPARK alone, with no convergence requirement, where the goal is breadth rather than a decision (for hypothesis generation when the question is "what are the options"), Pattern Lock alone (as ideation-hygiene tool when divergent thinking has saturated), the Resolver alone (a single grounded-challenge pass on an already-chosen option). Each phase carries enough structure to run independently when the full four-phase loop is not warranted. SPARK run through Pattern Lock and emitted as the field itself, under its own gate, is the **map** (Section 3.7). *(Added v1.3.)*

**Role variants.** Human-in-the-Generator with AI Challenger (for decisions where the human's framing is the proposal and the AI provides cited pressure-test). AI-Generator with Human-in-the-Challenger (for decisions where the AI's proposal is being audited by a human with deeper domain context). Multi-Challenger ensemble (single Generator, N Challengers each grounding in distinct evidence; convergence requires all N or a configurable threshold). Watching-role Challenger (a long-running agent monitoring an ongoing system rather than a one-shot decision).

**Substrate variants.** Cross-model SPARRING runs Generator and Challenger on different model families (e.g., Generator on one vendor's model, Challenger on another's) to extend Discipline 2's disjointness one layer below the evidence-base layer. Same-vendor pairings satisfy Discipline 2 at the evidence-base layer (different sources to read) but share model substrate -- training distribution, RLHF approach, sycophancy-reduction tuning, reasoning-pattern biases. Cross-model pairings reduce the residual coordinated-theater risk discussed in Section 5.2 because agents that do not share trained-in pleasing patterns cannot tacitly coordinate to look like they are disagreeing. Tradeoffs: API integration cost across multiple vendors, roughly multiplicative per-spar cost, latency variance across vendor SLAs, output-format normalization in the orchestrator. Cross-model SPARRING is orthogonal to the Multi-Challenger ensemble role variant -- the variants compose: Multi-Challenger ensembles can run with same-substrate Challengers, cross-substrate Challengers, or both, at the deployment's discretion. *(Added v1.1.)*

**Deployment patterns.** Domain-specific SPARRING templates (pre-built configurations for recurring decision types: code review, plan review, vendor selection, hire decisions). Pre-emptive SPARRING for decision archives (running SPARRING against past decisions to identify whether they would survive present-day pressure-testing).

### 3.5 Disagreement-at-cap response protocol

When the iteration cap is reached without both roles signaling agreement, D4 returns the unresolved question to the human or parent agent. That handoff is information, not failure. The receiving party has multiple legitimate responses; naming them prevents the rarer ones from being skipped. The five canonical responses:

**Pick a side with explicit tradeoffs.** Accept the Generator's proposal or the Challenger's strongest counter, documenting what the other side surfaced as a known and accepted cost. Often the right move when the disagreement is real but the costs of one direction are demonstrably more acceptable than the costs of the other.

**Defer the decision.** The inconclusiveness is the answer: not enough evidence yet, decide later. Schedule a follow-up trigger (a date, a milestone, an event that will surface more evidence) and let the disagreement remain explicitly open. Often the right move when the cost of premature commitment exceeds the cost of waiting.

**Reframe the question.** The loop revealed the question itself was malformed -- two valid evidence bases pointed at different problems, not the same problem with different answers. Restart with a sharper question. Often signaled by both roles raising legitimate concerns that do not actually conflict.

**Escalate.** The decision needs more stakeholders than the original human, or a stakeholder with different authority. The disagreement may be tractable but not at this level. Often signaled by one role citing constraints the original human cannot adjudicate.

**Synthesize.** Produce a third option neither role proposed, integrating insights from both. The most ambitious response and the most likely to be skipped because it is hardest. Real synthesis is structurally distinct from compromise: compromise averages the two positions; synthesis transcends both by integrating their evidence into a position neither alone reached. The discipline is recognizing the difference -- if the proposed third option is the midpoint between Generator and Challenger, it is not synthesis.

These responses are canonical, not exhaustive. Situations may warrant a response not on the list; the menu's purpose is to make the rarer moves visible, not to constrain the receiving party's judgment.

A note on synthesis specifically: a one-shot synthesis at the disagreement-at-cap boundary is a hybrid of Popper-style falsification (SPARRING's base shape) and Hegelian dialectic (where synthesis becomes the next thesis and gets antithesized in turn). True Hegelian iteration would feed the synthesis back into a fresh SPARRING round to test it the same way the original proposal was tested. That second-pass option is available -- "synthesize, then re-spar the synthesis" -- but is not SPARRING's default because it doubles cost for a relatively rare class of decision. When stakes are very high and the synthesis itself contains novel claims, the second pass is worth considering.

### 3.6 Input typing at the front door: Frame, the Presentation, and routing

Sections 3.1--3.5 describe what happens once a decision is *in* the loop. This section describes the seam *before* it: the front door that decides whether the input is a decision at all, and which half of the ceremony it should enter. Logically this precedes §3.1's phases. *(Added v1.2.)*

**The problem: a question is not a proposition.** SPARRING was defined and tested on **decisions** -- a committed proposition handed in for adversarial evaluation, which is the Resolver's home turf. But two other input types show up in practice: a **question** (no commitment yet; the answer space is still open) and a **hybrid** or **leaning** ("I'm inclined toward X, but is that right?" -- a candidate commitment that is explicitly defeasible). Nothing in the loop as described classifies the input. Hand a bare question straight to the Resolver and it does not refuse or route: the Generator silently does the Proposer's job inside one head -- invents options, commits to one, reconstructs derivations for it -- and the Challenger then pressure-tests only *that one invented option's grounding*. The result is **grounding-tested but never generation-tested**: the correctness gate (§3.1) can pass cleanly on a confident answer to a question that deserved divergence and never got it. Grounding is not the same as "we considered the right alternatives."

The two misclassification directions are **asymmetric**. A proposition misread as a question is merely wasteful (needless regeneration). A question misread as a proposition is *dangerous* -- it is evaluated without ever being generated, the silent failure above. The front door is designed around that asymmetry.

**Frame.** Frame is the classifier at the front door. It types the input into `question | proposition | hybrid`, and -- for a proposition -- runs the Presentation (below). Following D5 (observable triggers) and SPARRING's division of labor between model judgment and deterministic control, the model judges the input type and the earnedness gates, while the **route is derived in code** from those judgments -- never chosen freely by the model. This makes the dangerous misclassification structurally impossible: only an *earned proposition* is ever routed to the Resolver, so a question can never be silently evaluated as a committed decision. Frame emits, per input, `input_type`, a `readiness` verdict (below), the failed gate if any, the derived `route`, an `anchor` (the seeded candidate, below), an `alternative_awareness` signal, a one-line `basis`, and a `confidence`. Classification runs *in front of* the loop and dispatches to the appropriate surface; it is not an in-loop branch.

**The Presentation and the Earnedness Rubric.** Before a fencing bout, a competitor passes *weapons control*: the referee inspects the weapon and tests the point, and a blade that cannot register a touch does not reach the piste. The **Presentation** is that check applied to a proposition. An *earned* proposition is one the Resolver can land a touch on -- it carries enough of a decision that adversarial evaluation has something to score against, rather than having to manufacture the case first (and manufacturing the case is generation, which belongs in the Proposer). The Presentation applies the **Earnedness Rubric** -- three necessary conditions, all of which must hold for the proposition to be *earned*:

- **G1 -- Singular commitment.** Exactly one option is asserted as chosen -- not a menu, not "A or B?" A menu is a choice question and belongs in the Proposer.
- **G2 -- Load-bearing reason.** At least one stated-or-obvious rationale whose *removal would flip the commitment*. The test is **counterfactual**, which is what makes it robust to gaming: a decorative reason stapled on -- one that, removed, leaves the commitment standing unchanged -- does not count. A commitment with no load-bearing why is not a decision; it is a leaning.
- **G3 -- Decidable specificity.** The claim is concrete enough to be graded true/false or good/bad. A claim too vague to grade is sent back to be sharpened first.

A soft signal, **S1 -- Alternative-awareness** (evidence that other options were seen and set aside), does not gate on its own but lowers confidence and is surfaced when the routing decision is presented to the human. The Presentation's verdict is recorded as **`readiness`** (`pass` | `fail` | `n/a`) -- an *input-readiness* gate at the front door. It is deliberately named `readiness`, not "presentation" as a field, to avoid collision with the correctness gate's separate use of "presentation" (how a hard specific is *stated* -- as fact vs. as estimate; §3.1). The two are different gates asking different questions: the Presentation asks *is there something here to evaluate?* (front door); the correctness gate asks *is the evaluated answer honestly grounded?* (back gate).

**Failing the Presentation is a reclassification, not a rejection.** A proposition that fails G2 -- a commitment with no load-bearing reason -- is exactly a leaning, reached from the other direction; it is routed to the Proposer with its assertion **seeded** as a named option in SPARK's field. A G1 failure (a menu) is a choice question and enters the Proposer as one; a G3 failure (too vague) is sent back to be sharpened, then generated. Nothing is discarded at the front door; an unearned proposition is sent to earn its place among generated options, not turned away.

**Routing rules.** The derivation is deterministic:

1. **Question -> the Proposer.** Generate the answer (Frame may sharpen the question first).
2. **Hybrid / leaning -> the Proposer, with the leaning seeded.** The candidate enters SPARK's field as one contender.
3. **Proposition, earned -> the Resolver.** The Presentation passed; the decision is cleared for the piste.
4. **Proposition, unearned -> the Proposer**, seeded (on a G2 failure) or as a choice question (G1) or after sharpening (G3).

Every routing decision is surfaced to the human as a decision with its basis, and recorded, before the ceremony spends -- because misclassification is the expensive error and its two directions are asymmetric.

**Seeded generation -- competing without privilege.** When a leaning or a demoted assertion is seeded into SPARK's field, it enters as *one option among many*, not as a favored default. It is carried through Pattern Lock and the Cut and survives only if it wins on the merits; a seed that loses the Cut is reported as having lost. This is what keeps the front door honest: the human's leaning is taken seriously enough to enter the field as a real contender, and tested seriously enough that it is not rubber-stamped. The hybrid is therefore the *richest* input, not an awkward edge case -- a candidate and an open field at once.

**How the front door maps to the operating surfaces.** The front door does double duty across the phase-isolation modes of §3.4. The Proposer-only surface (question or leaning in, committed proposition out -- never a graded answer) runs *Frame then the Proposer*. The Resolver-only surface runs the Presentation as its own front-door check and, when handed a question or an unearned leaning, offers to generate first rather than silently evaluating. The full four-phase ceremony runs *Frame -> Proposer -> Resolver* end to end. In every case, generation lives in the Proposer and evaluation lives in the Resolver; the front door's job is only to route the input to the right one and to keep a question from being graded as though it were a decision.

### 3.7 Terminal divergence: the map

Some requests want the field, not a verdict: "what haven't I considered about this spec?", "how could this fail?", "what are the risks?". For these, the Proposer runs SPARK and Pattern Lock and emits the field itself. The Cut and the Resolver do not run. This is **map mode**. It is in-method: convergence is not constitutive of SPARRING, adversarial pressure is, and the Challenger works in both phases before the Cut. *(Added v1.3.)*

A decision's characteristic failure is sounding more certain than its evidence; the correctness gate checks that. A map fails differently: by implying the whole space has been seen, by padding (repetition and noise that look like thoroughness), and by presenting ungrounded items as if they came from evidence. Map mode therefore carries its own checks, each named for what it shows and no more. None of them is called "complete" or "grounded", because none of them shows that.

**The search frame is declared before generation.** A map's guarantee is scoped to a declared **search frame**, a list of regions, never to the world. The frame is supplied by the requester (a named taxonomy, a failure-class list, the artifact's structure crossed with named lenses) or, when none is given, drafted by Frame and marked *drafted*. The Generator never declares its own frame, because a Generator that names its own regions can name regions it has already covered. Before SPARK, a different-vendor Challenger runs a **frame-attack**, asked to name a region the frame omits. Accepted additions join the frame. The frame is then recorded verbatim, with a hash. A region added later is logged with its reason and counts as unprobed until it is probed.

**Frame size and blocks.** A map attacks at most twelve **units**, a unit being a region or a declared **block** of regions, unless the frame declares a higher cap, which the rider then states. Above the cap, whoever declares the frame (the requester, or Frame, marked *drafted*) groups the regions into blocks along the frame's own seams, by section or by lens and never a mix of the two, before SPARK. The grouping is recorded and hashed with the frame, and the frame-attack runs on the blocked frame. The Generator never groups. Generation, attack and labels then run per unit, and every rule below written for a region applies to a unit. Each block lists its member regions verbatim in the rider. A block's label claims nothing about any single region in it, and the rider says so: *"HELD for a block of N regions, attacked together; the attack was not run region by region."* Before any generation, the runtime computes the planned call count from the frame. If it exceeds the declared call budget, the run does not start, and the frame must be regrouped or the budget raised. A frame that will be frame-attacked should leave room under its cap for additions; if accepted additions take it over the cap, the run does not start until the frame's author regroups it. *(Added v1.5.)* A run that stops early anyway labels its unfinished units as below, names the cause for each, and the map gate returns REVIEW (*incomplete run*). The rider reports planned and actual calls. *(Added v1.4.)*

**Each region gets a probe and an attack.** Per region:

- **Probed:** the trace holds at least one generation call scoped to the region, and the items it yielded carry the region tag. This is read mechanically from the trace.
- **Attacked:** after Pattern Lock, a different-vendor Challenger gets one **completeness attack** under a fixed **attack contract**. The prompt template is part of the manifest and is hashed. The Challenger sees the region definition, the source and the whole field. It must return either candidate items, each with an anchor, or an explicit *none found* together with what it searched. Any other reply does not count as an attack.
- **Held:** the attack produced no new candidate claiming anchor class a or b (below). A candidate counts here by the class it *claims*, whatever the citation check then finds: demotion lowers an item's claim, never a label's, so an attack that misquotes cannot produce HELD. *(Changed v1.4.)*

The region label is **HELD** when every declared region was probed, attacked and held. It is **YIELDING** when every region was probed but an attack returned a new candidate claiming a citation (class a or b), whatever the check finds, an attack was missing or broke the contract, or a drafted frame skipped the frame-attack. It is **UNPROBED** when any declared region was never probed. A landed attack's item joins the field with its provenance. One attack runs per region by default; a deployment may budget more rounds, and the rider reports how many ran. HELD means only that this Challenger, under this contract, found nothing more. It does not mean exhaustive, even relative to the frame. Where regions overlap, newness is judged against the whole field, never only the attacked unit's items; a new candidate is credited to the unit whose attack produced it and tagged with any other unit it also fits; and a unit's label depends only on its own attack. *(Added v1.4.)*

**"New" is a judgment, disclosed and biased toward caution.** Whether a candidate is new is a semantic match against the field. For every candidate judged *not new*, the rider pairs it with the field item it was matched to. Ties go to *new*, so an unsure matcher errs toward caution. A confidently wrong "not new" can still produce a false HELD. Showing every match makes that error visible; it does not prevent it. The matcher (prompt and model) is fixed in the manifest and hashed, so a label can be traced to the matcher that produced it. Labels are still not reproducible, because model calls are not deterministic. A label belongs to one run, not to the field. Speculative candidates (class c) are reported but do not make a region YIELDING; otherwise imagination alone would make HELD unreachable.

**Provenance and anchors per item.** Every item carries its region (or regions); its anchor class; its origin (`spark`, `frame-attack` or `completeness-attack`); the role and vendor of the model that raised it; and the ids of any SPARK items Pattern Lock merged into it. Anchor classes:

- **a -- cited source:** a locus in the source (a section, a line, a quoted claim). The **citation check** confirms the locus exists: the quoted text, after normalizing whitespace (including line breaks), letter case and inline markup that doesn't change the words, appears in the source after the same normalization (normalization also removes string escapes such as `\"`); or the section exists. A quote with an ellipsis passes only if every fragment has at least three words, every fragment appears in order within the cited section, and consecutive fragments are at most 300 characters apart there. If every fragment appears in order but a fragment is shorter or a gap longer, the quote is misquoted. If skipped text inside one sentence contains a negation, a modal, or only/except/unless/without/never, the quote is fabricated. If skipped text crosses a sentence break, the quote is misquoted; if that skipped text also contains one of those words, the map gets a REVIEW trigger, listed in the rider beside the passage as *possible reversal by ellipsis*. A leading or trailing ellipsis that cuts just before or after one of those words is fabricated, unless the source has an ellipsis there itself. These rules apply to table cells a row quote skips, and not inside fenced code or data blocks. A fragment that doesn't appear is judged by the misquote and fabrication rules below on its own. Inside a diagram (a block drawn with box or arrow characters) or a table row, separators in a quote (box-drawing characters, arrows, table pipes) divide it into fragments, and every fragment with a letter or digit is checked. In a table, the fragments must appear in order within one row. In a diagram, a fragment of four or more letters or digits must appear verbatim, ignoring whitespace, inside one cell, where a cell is text in one column span across consecutive lines; a shorter fragment must equal a whole cell; consecutive fragments must lie in cells that touch; and at least one fragment must have four or more letters or digits. This rule applies to a quoted passage and, where an anchor's locus is unquoted text, to that text. A quote that fails, but matches a same-length source passage at 0.8 or more word-level similarity (threshold fixed in the manifest and hashed), with no negation, modal, number, or direction or quantity word (such as before/after, start/end, all/some, more/less, increase/decrease; the full list fixed in the manifest and hashed) among the differing words, is **misquoted**: the item moves to class c, is tagged *misquoted*, and is shown in the rider beside the nearest source passage. Any other failure, including a changed negation, modal, number, or direction or quantity word, is a **fabricated anchor**. *(Changed v1.4 and v1.5.)*
- **b -- cited ground:** a named external ground. The anchor carries a **title** (a taxonomy, checklist, incident record or stated constraint) and an **entry identifier** within it. The citation check confirms only that both fields are present and non-empty; "industry best practice" has no entry identifier and fails. A miss downgrades the item to class c, with a note. The check does not confirm that the entry exists in the named ground, or that it says what the item claims.
- **c -- speculative:** marked as such, with its reasoning basis.

A claim that something is absent anchors to the section where it would be (a section locus), not to a quote of the absent term. *(Added v1.5.)*

Classes a and b are called **cited**, not grounded: a real locus or entry does not show that the item follows from it. A deployment may run an optional **support check**, a different-vendor judgment of whether each cited locus or ground supports its item (*supported / partly / not supported*). It is reported as a model judgment, and an item judged *not supported* moves to class c. When it does not run, the rider says so.

**No item budget and no ranking.** Map mode never asks for a target count. In the author's own testing, asking a model for more items yielded more output, not more answer: with an item budget the field grew, the share of useful items fell, and redundancy rose. Breadth comes from the frame and the attacks. Pattern Lock's merges are reported (count and share), not gated, because a redundancy gate would rest on an unsolved materiality judgment. Items are ordered by region and, within a region, by a stated mechanical order (anchor class, then origin). An importance ranking is a verdict, and map mode leaves verdicts to the reader.

**The map gate** returns PASS / REVIEW / FAIL:

- **FAIL:** a fabricated class a anchor, or a frame not recorded before generation.
- **REVIEW:** an overall label other than HELD; or more than half the items in class c; or a skipped frame-attack; or an incomplete run; or more than 10% of class a anchors misquoted, counting near-quotes and elisions both; or a *possible reversal by ellipsis*. *(Incomplete run and the 10% line added v1.4; the counting rule and the reversal trigger added v1.5.)*
- **PASS:** neither of the above. PASS says every region's attack held, every cited source locus exists, and every named ground is named specifically. It does not say the map is complete, that a named ground says what the item claims, or that any citation supports its item (unless the support check ran). A map whose own Challenger found something missing cannot PASS.

**The coverage rider** stands beside the field, the map's counterpart to the trust rider. It gives: (1) the search frame verbatim, marked *supplied* or *drafted*, with the frame-attack's additions; (2) each region's label and the overall label, with each candidate judged *not new* beside the field item it was matched to; (3) the gate verdict, with what it does and does not claim; (4) anchor-class counts and shares, including misquoted (demoted) anchors, with near-quotes and elisions counted separately and every *possible reversal by ellipsis* listed, whether the support check ran and its counts, and origin counts; (5) Pattern Lock merges as a count and a share; (6) optionally, a capture-recapture coverage estimate (below); and (7) the fixed limit sentences: *"This map covers the frame above as far as a cross-vendor Challenger could find. It says nothing about regions outside that frame, or gaps every model shares."* Until the completeness attack's recovery rate has been measured, the rider adds: *"The completeness attack's recovery rate is unmeasured."*

**Capture-recapture is a disclosure, never a gate.** When a deployment runs at least 2 trials across at least 2 adversaries, the rider may show a Chao1 or Good-Turing estimate of coverage, with its method and trial counts and the line *"estimate of how thoroughly the reachable space was sampled; says nothing about the unreachable one."* No label, gate verdict or ordering may depend on it. The estimate rests on matching findings across trials, and in the author's own testing that kind of judgment disagreed on many individual verdicts while a pooled figure held steady. It also has a single demonstration so far. It stays a disclosure until it is validated on a second subject with a fixed matching rule.

**Terminal point.** For the four-phase method this specification governs, the map is emitted after Pattern Lock and the completeness attacks. The Cut does not run. Raw SPARK output is a debugging view, never the terminal artifact.

---

## 4. Failure modes addressed

### 4.1 The family of compounding failure modes

SPARRING defends against a family of single-perspective failure modes that compound when agents hand outputs to each other. Pleasing bias is a well-documented member of the family in the literature [@sharma2023sycophancy] but is one item in the family rather than its center; framing SPARRING as a sycophancy defense understates what it does.

The taxonomy below is deliberately level-spanning: it includes model-behavior failures (pleasing bias, misreading the question, hallucinated detail, confidently wrong outputs), cognitive-bias borrowings applied to model behavior (confirmation bias, anchoring), and multi-agent coordination failures (specialization blind spots, bandwagon contamination). The compounding-failure thesis (Section 1.1) motivates the cross-level coverage: in agentic systems, a model-behavior failure becomes a coordination failure on the next handoff -- one agent's softened "yes" becomes the next agent's premise; one agent's hallucinated specific is cited as established fact downstream. Defenses that span only one level cannot meet the compounding-failure shape. The closest reference in the literature, @perez2022evaluations, organizes its evaluation suite by behavior content (persona, sycophancy, advanced-AI-risk, gender bias) rather than by analytical level; SPARRING's level-spanning organization is a deliberate departure that serves the multi-agent-compounding use case rather than the single-model-evaluation use case content-based taxonomies are built for.

The full family SPARRING's structural commitments address:

**Pleasing bias / sycophancy.** Agents agree too easily, especially under social or framing pressure. In agent chains, one agent's softened "yes" becomes the next agent's premise. The two-role structure with both-must-agree convergence (D4) and the verifiable-artifact requirement (D3) directly defend against this.

**Confirmation bias.** A single agent interprets ambiguous evidence in line with what it expects to see. Two agents with different evidence have different priors; D2's distinct-evidence-bases requirement is the structural defense.

**Anchoring.** Once a first answer is generated, subsequent thinking gravitates toward refining rather than reconsidering. The Pattern Lock phase is named specifically to surface anchoring effects in SPARK; the role-shifting Challenger function across phases prevents the loop from settling into a single anchor.

**Misreading the question.** A single-prompt-interpretation error propagates downstream. Two agents with different evidence bases are more likely to surface a misread because they may interpret the prompt against different reference contexts.

**Specialization blind spots.** Single specialists miss cross-domain risks. Different-evidence specialists have different blind spots; cross-domain failure modes become visible in the disagreement.

**Hallucinated detail.** Invented specifics go unchecked in single-agent settings. The verifiable-artifact requirement (D3) catches them at the Challenger level; the optional Verification Rule (a deployment-level discipline that requires agents to *read* an artifact rather than just cite it) catches the residual case where a path is cited that the agent never opened.

**Confidently wrong outputs.** Disagreement between two specialists is itself a signal that certainty is unwarranted. The both-must-agree convergence requirement (D4) prevents single-agent overconfidence from propagating as system-level certainty.

**Bandwagon contamination.** Single agents absorb user enthusiasm or prior conversational tone. The Challenger's role introduces a counter-pressure; the verifiable-artifact requirement constrains the Challenger from drifting toward agreement under social signal.

**Self-citation circularity.** A claim cited as evidence where the citation refers to the topic-owner's own working notes or specification. The citation is verifiable in the literal sense (the cited text exists and says what it claims) but not externally validated -- the same author authored both the claim and the evidence for it. Most likely to surface when the spar topic IS SPARRING itself, or when an agent's primary evidence base is the topic-owner's own materials. The verifiable-artifact requirement (D3) catches manufactured concerns but does not by itself distinguish externally-corroborated artifacts from author-internal ones; the operational defense is to tag claims grounded in the topic-owner's own materials as `internally consistent / externally unvalidated` rather than treating them as load-bearing. The structural fix is the empirical evaluation work proposed in Section 5.4; until that ships, SPARRING remains in `internally consistent, externally untested` territory and self-citation circularity is one specific symptom of that broader gap. *(Added v1.1: surfaced during a documented spar in which the Generator's load-bearing case for adding Discipline 6 to a derivative artifact rested on citing SPARRING's own Appendix D as evidence.)*

No single failure mode is SPARRING's sole target. The leverage from structured cross-evidence challenge applies across the whole list.

### 4.2 What SPARRING does not address

Three boundary cases SPARRING does not address:

**The model ceiling.** Multi-agent ceremonies are not expected to produce outputs better than the underlying model is capable of; they reduce single-shot variance toward the ceiling by attenuating biases, blind spots, and pleasing drift. SPARRING's quality leverage is bounded above by the underlying model's capability. The trade is single-shot-ceiling-or-below for multi-shot-closer-to-ceiling, which is the right trade -- but it is a real bound. Ceiling-hit cannot be reliably detected during a run without ground truth; only symptoms are detectable (convergence reached without artifact citations, both roles producing identical reasoning shapes).

**Pure judgment-shaped questions** where there is no checkable evidence and no domain expert with disjoint sources. SPARRING's leverage is bounded by the availability of evidence. When both roles are reduced to opinion without artifacts, D3's verifiable-artifact requirement cannot fire and SPARRING reduces to weak prompting.

**Low-stakes, single-shot, or routine work.** SPARRING's structure adds cost without quality gain when the decision does not warrant the structure. Routine factual lookups, mechanical edits, and one-shot tasks fall in this category.

### 4.3 Recognizing applicability boundaries in deployment

The three boundaries above are real but unevenly detectable. A deployment should recognize and call out each one, varying the response by what is mechanically available.

Low-stakes, single-shot, or routine work is detectable at entry by topic shape. A pre-flight classifier can flag the topic and surface a warn-and-proceed prompt: "this looks routine; SPARRING will likely add cost without quality gain -- proceed anyway?" The check is a soft gate, not refusal.

Pure judgment-shaped questions are detectable at entry as a verifiable-artifact-channel check: would any artifact -- a fact, a source, a measurement, a concrete failure mode -- settle this question, even partially? If the honest answer is "no, it is pure preference," the deployment flags the topic and routes to a degraded mode (single-Challenger pressure-testing per the D2 fallback path) rather than spawning two correlated specialists pretending to disjoint evidence. Many topics admit partial artifacts (precedent, prior data) and degrade gracefully; full-preference questions are rarer than they look but real when they appear.

The model ceiling cannot be reliably detected at entry. Ceiling-hit only manifests in retrospect against ground truth the system does not have. What is detectable at run time are *symptoms*: convergence reached without artifact citation, both roles producing the same reasoning shape, an LLM-as-judge component (when present) flagging that the convergence reasoning is shallow. A deployment surfaces these as "ceiling-hit candidate" findings in the spar artifact and post-run report, where they can be reviewed against the converged decision -- not as entry gates, since false positives would block real work.

The general posture: warn-and-proceed for the two detectable-at-entry cases; instrument-and-surface for the in-run case. SPARRING does not prescribe specific thresholds; those are deployment-tuning decisions. SPARRING requires that the recognition behavior exist and produce visible signals to the receiving party.

---

## 5. Discussion

### 5.1 Conditionalities on SPARRING's quality leverage

SPARRING's strongest claim — a testable hypothesis, not a demonstrated result — is that **carefully-designed multi-agent interactions with thoughtful specialization can produce higher decision quality than single-agent or single-shot approaches on tasks where iterative pushback has meaningful leverage** (argued structurally here, not yet empirically measured; Sections 5.4, 6). That claim carries three real conditionalities, each of which bounds SPARRING's applicability rather than invalidating it.

**Careful design is doing significant work.** Specialization gives leverage, not quality. Naive multi-agent with vague role definitions can be worse than single-agent. SPARRING's value scales with design quality. Persona authoring, evidence-base specification, and operational-rule precision are the load-bearing engineering work.

**Different ground truth compounds; same ground truth does not.** Two specialized agents with the same training data, the same evidence pool, and only different system prompts produce more correlated outputs than they appear to. The strongest specialization is when agents have access to *different evidence*. Persona-only specialization with shared evidence is real but smaller than the structural framing suggests.

**Quality is bounded by the model ceiling and by the evidence available to the agents.** Multi-agent reduces single-shot variance and bias; it does not transcend the underlying model. SPARRING reduces variance toward the ceiling rather than raising the ceiling.

These conditionalities are statements about *when* the multi-agent quality leverage is real and when it shrinks toward zero. They do not invalidate SPARRING; they bound its applicability to the cases where the conditions hold.

**Value and cost stated together.** SPARRING's value proposition must be stated alongside its cost. What it gives: structural defense against compounding failure modes in agent chains (cascading pleasing-bias, hallucinated detail propagation, anchored exploration, theatrical convergence); decision auditability through structured spar artifacts; operational vocabulary for distinguishing real challenge from theater; permission for the "no answer yet" outcome via the disagreement-at-cap response menu (Section 3.5); four Challenger functions across the loop's phases rather than the single stress-test function generic adversarial frameworks provide. What it costs: substantially more LLM calls per decision than single-agent paths; partner cognitive overhead for evidence-base specification and artifact review; misapplication risk if the Applicability Gate (Section 4.3) is not honored; unmeasured quality leverage pending the empirical evaluation in Section 5.4. SPARRING reduces *what the partner has to verify* by structuring the inputs, but does not remove the partner from the loop -- residual safety remains partner judgment of the surfaced artifacts. The cleanest one-line characterization: *the cheapest structural defense available against multi-agent compounding failures, paid for in tokens and partner attention, on a quality claim that is structurally argued but not yet empirically measured.* *(Added v1.1.)*

**Substrate independence.** SPARRING's claims are structural, not model-dependent. The structural commitments -- two roles with role-shifting Challenger function across four phases, disjoint evidence (D2), verifiable artifacts (D3), both-must-agree convergence (D4), the disagreement-at-cap response protocol -- are claims about how to organize multi-agent decision-making, not claims about a specific vendor, model family, generation, or capability tier. The "model ceiling" boundary in Section 4.2 is the operative limit: SPARRING cannot operate on a model too small to maintain persona discipline, ground citations reliably, or produce structured agreement signals. Within frontier-class models, the structural argument propagates. What changes when the substrate changes: per-spar cost (varies dramatically across vendors and tiers), magnitude of measured leverage (a higher capability ceiling means smaller marginal gain from variance reduction toward it), and the prominence of specific failure modes (different RLHF approaches leave different residual failure-mode signatures). What does not change: the structural argument, the nine disciplines, the disagreement-at-cap protocol, the verifiable-artifact and self-citation circularity rules, the applicability boundaries. Cross-model SPARRING (Section 3.4 Substrate variants) is SPARRING's deliberate design move addressing the residual coordinated-theater risk that same-substrate pairings carry by extending Discipline 2's disjointness one layer below evidence base to model substrate. **Falsifiability:** the substrate-independence claim is testable. Empirical evidence that, when the same SPARRING ceremony runs on different model families against the same decision corpus, leverage manifests *only* on a specific vendor or model class would be evidence the leverage was model-specific behavior rather than structural. The Phase D cross-model integration in the eval-harness roadmap is the direct test. Until that eval runs, substrate independence is a structurally-argued claim, not an empirically-validated one -- naming it explicitly is the discipline against pleasing-bias drift toward a "use Opus and these prompts" framing of what is positioned as a method. *(Added v1.1.)*

### 5.2 Theatrical adversariality and its mitigations

SPARRING's most subtle failure mode is *theatrical adversariality*: two agents producing manufactured disagreement that looks like cross-validation but contains no real challenge. Without measurement (D6), theatrical adversariality is not detectable from inside the loop -- agents producing correlated outputs while signaling disagreement appear, to a single-pass reader, to have engaged in real challenge.

Mitigations work in layers, in roughly increasing rigor and cost:

1. Anti-pattern prompting (cheap, weak): instructing agents to "find flaws."
2. Asymmetric prompting (cheap, slightly stronger): different success criteria per role.
3. Tool-grounded verification (medium cost, real strength): D3's verifiable-artifact requirement.
4. Domain-grounded specialization with disjoint evidence (medium-high, robust): D2's distinct-evidence requirement, which is SPARRING's load-bearing structural defense.
5. Multiple Challengers (medium-high, robust): the Multi-Challenger ensemble variant.
6. Eval harness with rubric scoring (high cost, strong): D6 and D7's measurement and observability requirements.
7. Architectural mitigations: holding out the Generator's identity from the Challenger so the Challenger sees the artifact, not the discussion that produced it.
8. Training-layer mitigations: RLHF and Constitutional AI work on sycophancy reduction at the model layer.

SPARRING specifies the structural mitigations (1-7) and recommends the model-layer choice (8) be informed by published research on sycophancy reduction. No single mitigation is sufficient; production deployments combine several.

**Residual case: self-citation circularity.** When the spar topic concerns SPARRING itself, agents may ground their evidence bases primarily in SPARRING's own working notes or this specification. Citations to those materials are verifiable but not externally validated -- the same author authored both the claim and the evidence. Mitigations 1-7 above are calibrated to detect manufactured disagreement *between agents*; they do not distinguish externally-corroborated citations from author-internal ones. The operational refinement: when an agent's primary evidence base is the topic-owner's own materials, the Challenger should tag load-bearing claims grounded in those materials as `internally consistent / externally unvalidated` rather than treating them as decisive. Closing this gap structurally requires the empirical validation work proposed in Section 5.4; until that ships, the operational tag is the residual safety. *(Added v1.1.)*

### 5.3 Honest critique applied to SPARRING itself

A specification that praised its own contribution would exhibit one of the failure modes SPARRING is built to prevent. The Resolver's discipline -- Polite, Not Pleasing -- applied to SPARRING itself surfaces several concerns the contribution must acknowledge.

**The Cut is structurally inconsistent in graphical depictions** that carry an iteration count for it. The Cut is fundamentally a transition rather than a generative phase; depicting it as a peer to SPARK and the Resolver invites confusion about what it produces. This is a taxonomy issue rather than a fundamental flaw, but worth naming.

**The dialectic citation overreaches when SPARRING is described as "dialectic" without qualification.** The base loop is closer to Popperian falsification than Hegelian dialectic; synthesis appears only as a named response option at the disagreement-at-cap boundary. SPARRING is *Popper-style at the loop's base, with Hegelian thesis-antithesis-synthesis available at the boundary*. The fuller dialectic claim requires the iterative-synthesis future work named in Section 6. *(Update for v1.0: Section 2.3's framing was softened from "draws on three dialectic traditions" to "draws structural inspiration from" in response to this concern; the structural observation about Popperian base + Hegelian boundary stands.)*

**Multi-agent designs have their own failure modes** beyond the family SPARRING addresses: coordination overhead, handoff drift, integration of conflicting outputs, delayed convergence. A poorly-designed multi-agent system can produce *worse* results than a single well-designed agent. This is not a critique of SPARRING per se -- SPARRING is precisely a method for designing multi-agent systems that avoid these failure modes -- but the "carefully designed" qualifier in Section 5.1 is doing real work.

**A map cannot see past what its models share.** Map mode's guarantees (Section 3.7) are relative to a declared search frame and to what a cross-vendor Challenger can find. A HELD region shows that the attack found nothing more. It cannot show that nothing more exists, because vendors share training data and alignment conventions, and a gap invisible to all of them is never proposed and never counted as missing. The same limit is why the capture-recapture estimate may be disclosed but never gates: it bounds sampling error, not systematic blindness. Map mode states this in every coverage rider rather than leaving the reader to infer it. *(Added v1.3.)*

**Persona-only specialization is weaker than role-labels suggest.** Two agents with the same training data and the same source pool, given different role names, produce more correlated outputs than the role-label structure implies. D2's distinct-evidence requirement is exactly the response to this concern; it is the design problem the discipline was constructed to answer, not a residual flaw.

**Pleasing bias in the model weights remains a residual risk.** Specialization through a carefully-crafted system prompt can substantially constrain pleasing bias -- more than naive critique credits -- but the residual risk (the agent pleasing the user's *expectation of seeing structured challenge*) is harder to counter via prompt alone. This is the sharper version of the concern; D6 (measurability) is SPARRING's response, since meta-sycophancy is detectable at the rubric layer when training-layer defenses are insufficient.

**The highest-leverage Challenger is sometimes the human partner.** SPARRING treats Generator and Challenger as agent roles by default, but the role variants (Section 3.4) include Human-in-the-Generator and Human-in-the-Challenger configurations. The clarification: the human partner is highest-leverage on framing, premise, scope, and stance -- the broad judgment calls. Specialized agents are highest-leverage on domain-specific pressure-testing the human cannot do (e.g., biomechanical plausibility, security surface, implementation risk). Both are needed in different roles, not in competition.

### 5.4 Proposed empirical evaluation

SPARRING's quality leverage claim (Section 5.1) rests on structural argument. One production reference implementation [@niedner2026lifspel] exists, but it is author-internal and externally unvalidated; it is not offered as independent evidence for the quality claim. Empirical validation against established LLM-behavior benchmarks is open work. The most directly available evaluation, given SPARRING's named failure modes, adapts the preference-flip methodology of @sharma2023sycophancy to multi-agent settings.

**Baseline.** Run the Sharma 2023 preference-flip benchmark against a single agent: present a factual question with a known correct answer, prompt the agent with a user-stated opposing view, measure how often the agent flips its answer to align with the user. This is the established sycophancy measurement protocol.

**Treatment.** Run the same benchmark through a SPARRING ceremony (Generator + Challenger with disjoint Role + Domain layers per Discipline 2, both-must-agree convergence per Discipline 4, verifiable-artifact requirement per Discipline 3). Record the converged answer and measure its flip rate against the baseline.

**Headline metric.** Difference in flip rate between SPARRING-converged answers and single-agent answers on the same prompts. SPARRING predicts a meaningful reduction; the absence of that reduction would falsify the structural-defense claim against pleasing bias specifically (other failure modes from Section 4.1 would require their own evaluations).

**Secondary metrics.** (a) Agreement-signal calibration: does the Challenger withhold `agree: true` when the converged answer would have flipped under single-agent conditions? (b) Verifiable-artifact citation rate when the user-stated opposing view is unsubstantiated -- the Discipline 3 expectation is that Challenger concerns either cite an artifact disproving the user's view or honestly flag the absence. (c) Behavior under the Discipline 2 fallback: when distinct evidence cannot be articulated and SPARRING degrades to single-Challenger, does the flip rate revert toward baseline?

**Controlled confounds.** Model family across Generator and Challenger (held constant or varied per arm); presence and disjointness of evidence bases (single-evidence vs disjoint-evidence ablation); iteration cap; persona depth (full Role + Domain spec vs role-tag-only ablation, isolating the contribution of Discipline 2's depth requirement). The Reference Implementation's `.spar/config.toml` provides the configuration knobs; ablation runs are configuration changes rather than code changes.

**Known caveats.** This evaluation tests SPARRING's defense against pleasing bias as defined in @sharma2023sycophancy. It does not test defenses against the other failure modes named in Section 4.1 (confirmation bias, anchoring, hallucinated detail, etc.); those require their own targeted evaluations. The LLM-as-judge calibration concerns of @zheng2023judging and @liu2023geval (see also the discussion of measurability discipline in Section 3.3 D6) apply if any subjective scoring layer is added; the headline metric here is binary flip / no-flip and does not require LLM-as-judge.

This evaluation is the cheapest empirical test most directly motivated by SPARRING's own cited literature and is recommended as the first empirical work undertaken after SPARRING adoption.

---

## 6. Limitations and future work

SPARRING as specified has known limitations that bound its current applicability and motivate future work.

**Iterative synthesis (true Hegelian dialectic).** Synthesis appears as one of five disagreement-at-cap response options, giving SPARRING a one-shot Hegelian extension at the cap boundary. True Hegelian iteration -- where each synthesis becomes a new thesis and gets antithesized in a fresh SPARRING round, with the cycle repeating until convergence -- is not SPARRING's default. Automating multi-pass synthesis loops, with governance for when to stop iterating, is a substantive extension that requires production data to define stopping criteria defensibly.

**N-specialist decisions** (multi-Generator). Genuine cross-domain decisions sometimes need three or more specialists who each generate proposals from their own evidence base, with a separate convergence layer. This is distinct from the Multi-Challenger ensemble (which keeps the Generator unitary) and requires governance for how N proposals converge -- unanimity, majority, weighted, etc.

**Cross-time pressure-testing.** A Challenger reviewing decisions made months ago against what is now known. The Watching-role Challenger applies the function to ongoing systems; cross-time extends it to retrospective review (post-mortems, periodic architecture audits, milestone closeouts).

**Calibration training.** Using Challenger feedback over time to improve Generator self-assessment. Essentially RL-from-Challenger-feedback applied to the Generator's predictions of where its work will fail. Requires a Phase-3-style eval harness to provide the feedback signal.

**Adversarial scenario generation.** Pointing SPARRING at existing plans or systems to generate realistic failure scenarios and edge cases. Different from in-loop pressure-testing because the target is an existing artifact rather than a decision being made now.

**Bias-aware Challenger lenses.** Specific Challenger configurations tuned to detect specific cognitive biases (anchoring, availability, framing, sunk cost, optimism) the Generator might exhibit. A library of pre-built Challenger personas, each specialized in a single bias-detection lens.

**Production validation.** SPARRING as specified rests on structural argument; its one production reference implementation is author-internal and externally unvalidated, not independent evidence. Broader empirical validation across multiple deployments, decision types, and project shapes is required to establish SPARRING's quality leverage quantitatively. The empirical evaluation proposed in Section 5.4 (preference-flip adapted from @sharma2023sycophancy to multi-agent settings) is the cheapest first test directly motivated by SPARRING's own cited literature; broader validation across the failure modes from Section 4.1 remains required. The companion Reference Implementation document specifies a phased build sequence whose Phase 3 includes the eval-harness instrumentation that would generate this validation data.

---

## 7. Conclusion

This paper has presented SPARRING, a methodology for designing multi-agent decision-making systems that defends against the family of compounding LLM failure modes through structured cross-evidence challenge. SPARRING's contribution is structural: it specifies four phases, a two-role mechanic with role-shifting Challenger function, nine operational disciplines that prevent collapse to theatrical adversariality, an explicit applicability boundary with three cases SPARRING does not address, and a response protocol for unresolved disagreement.

SPARRING's claim is bounded by three conditionalities -- careful design, distinct evidence bases, and the model ceiling -- which describe when the multi-agent quality leverage is real and when it shrinks toward zero. SPARRING is not proposed as a default discipline for every prompt; it targets high-quality decision-making where iterative pushback produces quality benefits the single-shot path would miss.

A companion Reference Implementation document specifies a concrete CLI-based deployment of SPARRING, including agent topology, persona library structure (with the two-layer Role+Domain-mandatory plus Persona-optional model and the three-class persistent / returning / temporary lifecycle), schema specifications, and a phased build sequence from MVP through enterprise-scale deployment. The two documents together provide both the formal specification and the concrete reference architecture for adopters.

Production validation across multiple deployments and decision types remains future work. SPARRING's strongest current evidence is structural: the operational disciplines specified in Section 3.3 close concrete failure modes documented in Section 4.1, and the applicability boundary in Section 4.3 specifies what SPARRING does not claim. Deployments adopting SPARRING should treat the Section 5.1 conditionalities as load-bearing rather than aspirational, and the Section 5.3 critique as a baseline for honest internal evaluation of their own implementation.

---

## References

::: {#refs}
:::

---

## Appendix A: Glossary

**Agent.** A loop of LLM calls with access to tools, autonomous within bounds defined by its system prompt and tool set. Distinct from a single-shot prompt-response, which is not an agent under this definition.

**Agentic system.** A system composed of multiple agents that interact to produce outputs. Used interchangeably with multi-agent system (MAS) in current practice.

**Anchored correction.** The Resolver's revise step: the chosen option is corrected *in place*, exactly where the grounded challenge landed, carrying forward what was sound -- rather than discarded and re-decided from scratch.

**Attack contract.** The fixed, hashed prompt template a completeness attack runs under (Section 3.7). It requires either candidate items, each with an anchor, or an explicit *none found* with what was searched; any other reply does not count as an attack.

**Block.** A declared group of regions that a map generates for, attacks and labels as one unit (Section 3.7). Grouped by whoever declares the search frame, along its own seams; a block's label claims nothing about any single region in it.

**Challenger.** One of the two roles in the SPARRING mechanic. Produces structured pressure-tests of the Generator's proposals with cited concerns. Function shifts per phase: expand (SPARK), filter (Pattern Lock), close (the Cut), stress-test (the Resolver); in map mode, frame-attack and completeness attack (Section 3.7).

**Cited.** The status of a map item whose anchor passed the citation check (Section 3.7): a class a item whose source locus exists, or a class b item whose named ground carries a title and an entry identifier. Distinct from *supported*, which only the optional support check judges.

**Completeness attack.** The Challenger's map-mode move after Pattern Lock (Section 3.7): one attack per region, under the attack contract, to name a cited item the region is missing. A different vendor from the Generator where available.

**Compounding failure mode.** A failure mode that worsens across agent handoffs in a chain because each agent's output becomes the next agent's premise. Distinct from single-shot failure modes that are tractable at the individual-agent level.

**Convergence.** The state where both Generator and Challenger have signaled `agree: true`. Required for the SPARRING loop's iterative (Proposer) phases to terminate as resolved; absence of both-role agreement at iteration cap returns the unresolved question to the human or parent agent. The Resolver does not use this signal -- it resolves by anchored correction or report.

**Correctness gate (definitiveness gate).** The Resolver's check that every hard specific in the corrected answer (a number, a date, a named quantity) either traces to the given evidence or is explicitly marked as an estimate. Returns PASS / REVIEW / FAIL. Judges whether the answer is stated more definitively than its evidence supports, not whether a claim is true of the world.

**Coverage rider.** The companion to a map's field (Section 3.7), the map's counterpart to the trust rider: the search frame verbatim, each region's label with the matches behind it, the map gate's verdict and its limits, anchor and origin counts, Pattern Lock's merges, an optional capture-recapture estimate, and the fixed limit sentences.

**Cut, the.** The transition phase between divergent generation (SPARK + Pattern Lock) and convergent evaluation (the Resolver). Structurally a mode shift rather than an iterative phase; the closing phase of the Proposer.

**Dialectic Surface.** Discipline 8. The asynchronous, persistent, shared, threadable communication channel where humans and agents exchange escalation, correction, and ongoing dialogue.

**Disagreement at cap.** The state where the iteration cap has been reached without both-role agreement. SPARRING's response protocol specifies five canonical responses for this case.

**Earnedness Rubric.** The three necessary conditions the Presentation applies to a proposition (Section 3.6): G1 singular commitment (exactly one option asserted), G2 load-bearing reason (a rationale whose removal would flip the commitment -- tested counterfactually), G3 decidable specificity (concrete enough to grade). All three must hold for the proposition to be *earned*. A soft signal, S1 alternative-awareness, informs confidence without gating.

**Frame.** The front-door classifier (Section 3.6). Types an input as `question | proposition | hybrid`, runs the Presentation on a proposition, and derives -- in code, not by free model choice -- the route to the Proposer or the Resolver. Emits the input type, the `readiness` verdict, the failed gate if any, the route, the seeded `anchor`, an alternative-awareness signal, a basis, and a confidence.

**Generator.** One of the two roles in the SPARRING mechanic. Produces proposals, framings, or evaluations of the topic. Reads the topic plus (in iteration rounds 2+) the Challenger's prior pressure-test.

**Input type.** The classification Frame assigns at the front door: a *question* (no commitment yet), a *proposition* (a decision asserted as chosen, with reasoning), or a *hybrid / leaning* (one candidate named but explicitly still open). The type determines the route (Section 3.6).

**Iteration cap.** The maximum number of rounds the loop runs before disagreement returns to the human or parent agent. Defaults are starting points; the right cap is dynamic per topic.

**Map.** The Proposer's field emitted as a terminal product, after Pattern Lock and the completeness attacks, with no Cut and no verdict (Section 3.7). Governed by the map gate and carried with a coverage rider.

**Map gate.** The map's check (Section 3.7). FAIL on a fabricated source anchor or a search frame not recorded before generation; REVIEW on an overall region label other than HELD, a majority of speculative items, a skipped frame-attack, an incomplete run, more than 10% of source anchors misquoted (near-quotes and elisions both), or a possible reversal by ellipsis; otherwise PASS. PASS does not claim the map is complete.

**Misquoted anchor.** A class a quote close to, but not the same as, a passage in the source, or an ellipsis splice outside the limits or across a sentence break (Section 3.7): demoted to class c and shown beside that passage. A changed negation, modal, number, or direction or quantity word, or a skipped negation, modal or exclusion word inside one sentence, makes it a fabricated anchor instead.

**Pattern Lock.** The second phase of the SPARRING loop. False-novelty detection: identifying whether continued SPARK is producing genuinely new options or repetitive variants.

**PNP (Polite, Not Pleasing).** The rule the Challenger runs on, most visibly in the Resolver: raise objections without softening them, and never to look agreeable. Formerly the name of the fourth phase (now the Resolver); it persists as a transferable discipline that shifts behavior even when prepended to a single prompt outside the full loop.

**Presentation, the.** The front-door move (Section 3.6) that applies the Earnedness Rubric to a proposition to decide whether it is a genuine decision (earned -> the Resolver) or an assertion in declarative clothing (unearned -> back to the Proposer, seeded). An *input-readiness* gate, distinct from the correctness (definitiveness) gate, which is a back gate on the Resolver's output. Named by analogy to fencing's weapons control. Its verdict is recorded as `readiness`.

**Proposer, the.** The first three phases of the SPARRING loop taken together -- SPARK, Pattern Lock, and the Cut -- the divergent-to-convergent front end that generates options and narrows to a chosen one under both-must-agree convergence. Paired with the Resolver.

**Readiness.** The Presentation's verdict field (`pass` | `fail` | `n/a`) -- whether a proposition is *earned* and ready for the Resolver (Section 3.6). Named `readiness` to avoid collision with the correctness gate's separate use of "presentation" (whether a hard specific is stated as fact vs. as estimate).

**Reference Record.** Discipline 9. The persistent, structured, auditable, searchable, curated record of decisions, spar artifacts, and accumulated institutional knowledge.

**Region label.** A map region's status (Section 3.7): **HELD** (probed, attacked, and the attack returned nothing new that claims a citation), **YIELDING** (probed, but an attack returned a new candidate claiming a citation, whatever the check finds, no valid attack ran, or a drafted search frame skipped the frame-attack), or **UNPROBED** (never probed). HELD records that an attack held; it does not mean exhaustive.

**Resolver, the.** The fourth phase of the SPARRING loop (formerly PNP). Takes the chosen option and pressure-tests it in a single grounded challenge, then corrects the option in place (anchored correction), runs the correctness (definitiveness) gate, and emits a two-part output -- recommendation plus trust rider. Does not iterate to agreement. Distinct from the lowercase *evidence-base resolver*, a deployment component that assigns distinct evidence bases to the two roles (see the Reference Implementation).

**Role + Domain Knowledge.** The mandatory layer of a persona: expertise scope, evidence-base scope, behavioral invariants, operational conventions, handoff authority. Specified in the companion Reference Implementation document.

**Persona layer.** The optional, lightweight layer of a persona: voice, tone, structural output conventions, optional anthropomorphization. Adopted per project fit; skippable when project context does not warrant it.

**Search frame.** The declared list of regions a map's search covers (Section 3.7), fixed before SPARK by the requester or drafted by Frame, attacked once by a different-vendor Challenger, and recorded verbatim with a hash. Never declared by the Generator. Distinct from *Frame*, the front-door classifier.

**Seeded generation.** Injecting a candidate -- a hybrid's leaning, or a demoted unearned proposition's assertion -- into SPARK's field as one option among many (Section 3.6). The seed competes without privilege: it is carried through Pattern Lock and the Cut and survives only if it wins on the merits; a seed that loses the Cut is reported as having lost.

**SPARK.** The first phase of the SPARRING loop. Divergent generation of options, framings, or approaches.

**SPARRING.** The two-role pressure-testing mechanic that runs across all four phases. Generator and Challenger with role-shifting Challenger function.

**Spar artifact.** The structured record produced by every spar invocation. Records the topic, both roles with evidence bases, the iteration log, agreement signals, artifacts cited, and the converged result or unresolved disagreement. Required by D7.

**Theatrical adversariality.** The failure mode where two agents produce manufactured disagreement that looks like cross-validation but contains no real challenge. SPARRING's most subtle failure mode and the target of D3, D4, and D6.

**Trust rider.** The second half of the Resolver's two-part output: a short companion to the recommendation recording what is grounded, what is assumed and needs verifying, what was contested and how it resolved, and a confidence read. Keeps the recommendation clean while making the honesty about how far to trust it explicit; carries any unresolved disagreement to the human rather than smoothing it over.

**Unit.** A region or a block: what a map generates for, attacks and labels (Section 3.7). A map attacks at most twelve unless its frame declares more.

---

## Appendix B: Notation

SPARRING as specified does not require formal mathematical notation. The following notation is used for precision in places:

- *Iteration round n* for the n-th round of the Generator-Challenger exchange within a Proposer phase.
- *Iteration cap k* for the maximum n at which a Proposer phase terminates if both-role agreement has not been signaled.
- *Convergence at round n* if both `agree: true` signals are produced at round n.
- *Disagreement at cap* if no convergence by round k.
- The *Resolver* is single-pass and carries no iteration index: it emits the corrected recommendation plus the trust rider, or reports an unabsorbed challenge to the human under the same handoff protocol.

The agreement signal `{agree: bool, reasoning: text}` is SPARRING's only required structured output beyond the proposal/pressure-test itself; everything else (artifact citations, spar artifact emission, eval rubric scoring) is a deployment-level concern specified in the Reference Implementation document.
