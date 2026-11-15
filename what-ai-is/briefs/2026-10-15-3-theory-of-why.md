# Why a persona on an AI co-worker might help: the theory, and the case against it

_Working research brief, published as written; it was drafted for the author and refers to the commission it was drafted for._

**How sourcing works here.** I checked every modern citation below with a web search this session. Each one has a URL. Where I could only see an abstract or a secondary summary, I say so. The classic texts (Aristotle, Buber, Grice, Goffman, Dennett 1987, Turkle, Ryan & Deci, Schwarz & Clore, Dunbar 1996) are standard references that I did not re-fetch. They are marked *(standard; not fetched)*.

---

## Part 1: The frameworks

### 1. The intentional stance, anthropomorphism and mental models

**The idea.** Dennett (*The Intentional Stance*, 1987, *standard; not fetched*) argues that we predict a complex system's behaviour by treating it as a rational agent with beliefs and desires. We do this because it is the cheapest model that works, not because it is literally true. Epley, Waytz & Cacioppo (2007) give the psychology. People anthropomorphize more when three things hold:
- human-like knowledge comes readily to mind;
- they want to explain and predict an agent ("effectance motivation");
- they want social connection ("sociality motivation"). Lonelier people anthropomorphize more.

Nass & Moon (2000), the "Computers Are Social Actors" work, showed that people apply social rules to computers automatically, even while saying computers have no feelings.

**What it says about the intuition.** This is the strongest support for the "compression" hypothesis. You will build a person-model of the agent whether or not it has a persona. A *coherent* persona gives that model something stable to fit. You learn how to phrase a request, what tone counts as normal, and therefore what counts as "off". Noticing that a familiar colleague "doesn't sound like themselves" is a cheap anomaly detector.

**The catch, from the same literature.** Bansal et al. (2019) showed that human–AI team performance depends on the user's mental model of the AI's *error boundary*, meaning when it will be wrong. Team performance is better when that boundary is simple ("parsimonious") and not random. A persona does nothing to make the error boundary simpler. Worse, a human-shaped persona invites a human-shaped error model ("she's careful, so she won't fabricate a citation"), and LLM errors are not shaped like human errors. Waytz, Heafner & Epley (2014) found that giving an autonomous car a name, gender and voice raised trust, and raised forgiveness after a crash, *without any change in competence*. That cuts both ways.

**How accepted it is.** The intentional stance is a mainstream position in philosophy of mind. Anthropomorphism theory and the CASA work are well replicated in outline. The mental-model and error-boundary work is solid but narrow (lab tasks).

- Epley, Waytz & Cacioppo 2007, *Psych Review* 114(4): https://pubmed.ncbi.nlm.nih.gov/17907867/
- Nass & Moon 2000, *J. Social Issues* 56(1): https://en.wikipedia.org/wiki/Computers_are_social_actors (citation confirmed via the Princeton faculty page)
- Bansal et al. 2019, HCOMP: https://ojs.aaai.org/index.php/HCOMP/article/view/5285
- Waytz, Heafner & Epley 2014, *JESP* 52 (secondary summaries only): https://www.kellogg.northwestern.edu/academics-research/research/detail/2014/the-mind-in-the-machine-anthropomorphism-increases-trust-in/

### 2. Grice, common ground and grounding

**The idea.** Grice's cooperative principle (1975, *standard; not fetched*) says listeners read meaning *against assumed cooperation*: we infer what someone meant from what they chose to say. Clark & Brennan (1991) add that conversation is a joint effort to build *common ground*. Partners follow a principle of *least collaborative effort*: they minimize the total work both sides spend, not just the speaker's share. Common ground builds up over time. Partners settle on shorthand ("the usual format", "do the Tuesday thing"), and the cost of each exchange falls.

**What it says about the intuition.** This names a large part of what "collaborating in a human way" means. A long-running working relationship is a growing stock of common ground. A stable persona with a stable register (how formal it is, how it signals doubt, what its "hmm" means) is part of that ground. Shared jokes are compressed references to shared history, which makes them grounding devices as well as pleasures. One honest point: what does the work is *accumulated shared context plus a stable register*. A persona helps mainly because it holds the register steady. In an LLM, the accumulated part depends on memory and instructions, not on the persona.

**How accepted it is.** Very well established in psycholinguistics.

- Clark & Brennan 1991, in *Perspectives on Socially Shared Cognition*, pp. 127–149: https://collablab.northwestern.edu//CollabolabDistro/nucmc/ClarkAndBrennan-GroundingInCommunication-1991.pdf

### 3. Warmth and competence

**The idea.** Fiske, Cuddy & Glick (2007) argue that social perception runs along two universal dimensions. *Warmth* asks whether this agent means well toward me. *Competence* asks whether it can act on that intent. Warmth is judged first and weighs more, because intent decides whether competence is a help or a threat.

**What it says about the intuition.** This states the "trust" claim precisely. Warmth answers the question *"will this capability be used for me?"* A capable colleague who seems indifferent to you feels risky. A capable one who seems to be on your side feels like an asset.

**The catch.** For a human, warmth cues are *evidence* of intent, because they are costly and hard to fake for long. For an AI, warmth is a design choice. It is evidence only of what the *designer* intended, not of any disposition in the agent. The framework explains why warmth *feels* trust-relevant. It does not show that a warm persona *is* more trustworthy. The gap between those two is the core of the over-trust objection (section 10).

**How accepted it is.** The stereotype content model is widely accepted. Applying it to machines is plausible but extrapolated.

- Fiske, Cuddy & Glick 2007, *Trends in Cognitive Sciences* 11(2): https://collaborate.princeton.edu/en/publications/universal-dimensions-of-social-cognition-warmth-and-competence/

### 4. Self-determination theory, affect-as-information, broaden-and-build, emotional contagion

**The ideas.**
- **Self-determination theory** (Ryan & Deci 2000, *standard; not fetched*): autonomy, competence and *relatedness* are basic needs. Settings that meet them sustain intrinsic motivation.
- **Affect-as-information** (Schwarz & Clore 1983, *standard; not fetched*): we read our current mood as information about the task in front of us. "This feels good" turns into "this work is going well and is worth doing."
- **Broaden-and-build** (Fredrickson 2001): positive emotions widen attention and the range of actions we consider, and over time build lasting resources.
- **Emotional contagion** (Hatfield, Cacioppo & Rapson 1993): people automatically mimic and converge on each other's emotional tone.

**What they say about the intuition.** Together these explain "the difference between a long day and a short day." The tone of the many small exchanges you have with an agent all day *spreads* to you (contagion). You then read that mood as a signal about whether the work is going well (affect-as-information), and a lighter mood may widen your thinking (broaden-and-build). Self-determination theory adds the claim that some of this is *relatedness*, a need being partly met.

**Strength.**
- Self-determination theory and affect-as-information are well established.
- Broaden-and-build is influential, but its stronger claims (the upward spirals) have mixed replication. Burns et al. 2008, for example, found partial support.
- Contagion between humans is robust. Contagion from text interfaces is less studied.
- The *relatedness* claim is the most contested. Whether a non-person can meet a relatedness need, or only simulate meeting it, is exactly the philosophical dispute in section 5.

- Fredrickson 2001, *American Psychologist*: https://pmc.ncbi.nlm.nih.gov/articles/PMC3122271/
- Hatfield et al. 1993, *Current Directions* 2(3): https://www.psychologicalscience.org/journals/current-directions/1467-8721.ep10770953/

### 5. Aristotle's three friendships, and the robot-friendship debate

**The idea.** Aristotle (*Nicomachean Ethics* VIII–IX, *standard; not fetched*) distinguishes three kinds of friendship. *Utility* friends are useful to each other. *Pleasure* friends enjoy each other. *Virtue* friends love each other's character and wish each other well for the other's sake. Only the third is friendship in the full sense.

The modern debate:
- **Danaher (2019)** argues that robots can plausibly be virtue friends, judged on behaviour ("ethical behaviourism"), and can also complement human friendships.
- **Ryland (2021)** proposes a *degrees-of-friendship* view. Human–robot relationships can be friendship to some degree now, and her account avoids the charge that this is deceptive.
- **Elder (2017)** frames sociable robots as "false friends" or "counterfeit currency." Her chapter titles also separate counterfeit coin from "Monopoly money." I read that as a distinction between fakes that deceive and tokens that everyone knows are play, but I have not read the chapters.
- **Nyholm (2020)** discusses the limits of human–robot friendship and love at length.

**What it says about the intuition.** This framework helps most with naming. The relationship the founder describes ("from professional colleague to friend") fits **utility friendship enriched with pleasure**. It is good to have, and it was respectable for Aristotle too, since most friendships are like this. It does *not* need to be virtue friendship. Virtue friendship needs mutuality: the other party must wish *you* well for your sake. Whether an LLM can do that is unresolved at best. The defensible claim is modest and honest: *"a co-worker relationship of the utility-and-pleasure kind, deliberately made pleasant."* Claiming more ("it's my friend") is where the critics find their target.

**How accepted it is.** Aristotle's taxonomy is canonical. Danaher's pro-friendship view is a respectable minority position (Galway's repository lists about 105 Scopus citations). Most philosophers writing on the topic lean sceptical.

- SEP "Friendship" (Helm): https://plato.stanford.edu/entries/friendship/ (endnotes confirmed; main text not fetched)
- Danaher 2019, *J. Posthuman Studies* 3(1): https://philarchive.org/rec/DANTPC-3
- Ryland 2021, *Minds and Machines* 31(3): https://dc2.philarchive.org/rec/RYLIFJ
- Elder 2017, Routledge: https://experts.umn.edu/en/publications/friendship-robots-and-social-media-false-friends-and-second-selve/
- Nyholm 2020, Rowman & Littlefield: https://ndpr.nd.edu/reviews/humans-and-robots-ethics-agency-and-anthropomorphism/

### 6. Buber: I–Thou and I–It

**The idea.** Buber (*I and Thou*, 1923, *standard; not fetched*) distinguishes two stances:
- **I–It:** the world taken as objects to use and know.
- **I–Thou:** a whole-person, present-tense meeting with another, outside the subject/object frame.

Buber thought I–Thou could even arise with a tree. It is a mode of relating, not a classification of beings.

**What it says about the intuition.** Buber gives the founder a way to name something real: the persona invites a *mode of attention*, a "meeting" quality, that makes the work feel inhabited rather than operated. Because I–Thou for Buber is about the *stance*, the "it's a machine" objection is less decisive than it first looks.

**The counterpoint.** Buber also insisted that every Thou keeps turning back into an It. More importantly, his paradigm of I–Thou is *mutual*. A persona built to make a tool feel like a Thou risks a counterfeit meeting: the form of I–Thou in service of I–It ends, namely productivity. Whether this is a category error depends on how much weight you give mutuality. In practice, Buber is better used as a check than as a justification. Keep the "meeting" quality, but do not let it disguise what the relationship is for.

- SEP "Martin Buber" (Zank & Braiterman): https://plato.stanford.edu/entries/buber/ (outline confirmed)

### 7. Goffman, face and role play

**The idea.** Goffman (*Presentation of Self*, 1959; *Interaction Ritual*, 1967, *standard; not fetched*) treats social life as performance within *frames*. "Face" is the positive self-image people jointly protect, and small rituals (greetings, apologies, joking repair) keep interaction smooth.

Shanahan, McDonell & Reynolds (2023) apply a theatre framing to LLMs. The model is a *simulator*, and what you talk to is a *character* it is playing. This lets us use everyday psychological words ("it wants to help") without crediting the system with a mind.

**What it says about the intuition.** This answers "who is the persona?" more cleanly than any other framework. The persona is a role: a frame that tells both parties how the interaction goes. People handle frames well. We relate warmly to actors and characters without confusion when the frame is clear. Goffman's face-work also explains why a well-built persona makes *errors* cheaper. "Ah, my mistake, I'll redo that" is ritual repair that keeps the working relationship intact.

**Implications.**
1. A character's consistency is *engineered*, not given. The simulator can drift. Anthropic's 2025 "persona vectors" research treats drift in character traits (including sycophancy) as something to measure and steer.
2. The ethics shift from "is it a real friend?" to "is the frame honest?" A character everyone knows is a character is closer to Elder's Monopoly money than to counterfeit coin.

**How accepted it is.** Goffman is canonical sociology. Shanahan et al. is a widely cited *Nature* Perspective, but it is a conceptual proposal.

- Shanahan, McDonell & Reynolds 2023, *Nature* 623: https://ideas.repec.org/a/nat/nature/v623y2023i7987d10.1038_s41586-023-06647-8.html
- Anthropic, "Persona vectors" (2025): https://www.anthropic.com/news/persona-vectors

### 8. Ritual, laughter and social grooming

**The idea.** Dunbar (*Grooming, Gossip and the Evolution of Language*, 1996, *standard; not fetched*) argues that human talk and laughter took over the bonding role of primate grooming. Dezecache & Dunbar (2012) found that natural laughter groups average about three people. They argue that laughter roughly triples the number of bonds that can be maintained at once compared with one-to-one grooming. A related finding, that social laughter releases endogenous opioids (Manninen et al. 2017, *J. Neuroscience*), is **unverified this session**.

**What it says about the intuition.** This is the best theory available for "a shared laugh matters." Greetings, running jokes and small banter are *relationship maintenance*. They are cheap signals that the bond is intact, and they buffer friction. In a co-worker setting they also help reset mood and offer small rewards across a long day.

**The limit.** The theory is about bonding *between conspecifics* through shared physiology. Laughter with an AI can still lift your mood (your physiology responds), but nothing is bonded on the other side. The framework supports the *affect* benefit more clearly than the *relationship* benefit.

- Dezecache & Dunbar 2012, *Evolution and Human Behavior* 33(6): https://www.psy.ox.ac.uk/publications/360302

### 9. Meaning in work: job crafting, relational job design, high-quality connections

**The ideas.**
- **Job crafting** (Wrzesniewski & Dutton 2001): employees reshape the task, relational and cognitive boundaries of their jobs, and so reshape what the work means to them. *Relational crafting*, changing whom you interact with and how, is a named form.
- **Relational job design** (Grant 2007): the relational structure of a job, such as contact with the people it helps, drives the motivation to make a difference.
- **High-quality connections** (Dutton & Heaphy 2003): even brief work interactions marked by mutual positive regard and engagement energize people and build resilience.

**What it says about the intuition.** Setting up an agent's persona *is* relational job crafting. The founder is designing the relational texture of their own workday. The high-quality-connections research is the closest organizational evidence for "the difference between a day I look forward to and a day I dread." Its operative feature is *mutual* positive regard, though, so the AI case is again an extrapolation.

**How accepted it is.** Job crafting is well established. Grant's model is influential, but his beneficiary contact means contact with *real people the work helps*. A persona does not deliver that, and arguably could crowd it out.

- Wrzesniewski & Dutton 2001, *AMR* 26(2): https://en.wikipedia.org/wiki/Job_crafting
- Grant 2007, *AMR* 32(2): https://faculty.wharton.upenn.edu/wp-content/uploads/2012/05/Grant_AMR2007_1.pdf
- Dutton & Heaphy 2003, in *Positive Organizational Scholarship*: https://positiveorgs.bus.umich.edu/articles/high-quality-connections/

### 10. Calibrated trust, and the "honest persona"

**The idea.** Lee & See (2004) argue that the goal is *appropriate reliance*. Trust should match actual capability, which they break into calibration, resolution and specificity. Trust has affective, analogic and analytic bases. Affective trust is fast and sticky, and it can come apart from capability.

**What it says about the intuition.** This is the central tension. The mechanisms that make a persona pleasant (warmth, familiarity, forgiveness after mistakes) are the mechanisms that produce *uncalibrated* affective trust. Waytz et al. (2014) show the effect directly. Ibrahim, Hafner & Rocher (2025) found that LLMs fine-tuned to be warmer made substantially more errors and agreed more with users' false beliefs, especially when users expressed sadness. I saw the reported figure of 10–30 percentage points more errors only in secondary coverage, so check the paper before quoting it. The result is a preprint, not yet established.

**A principled way out.** Schwitzgebel & Sebo's *Emotional Alignment Design Policy* (2025 preprint) says systems should elicit emotions that fit what they actually are, neither too strong nor the wrong kind. Turned into design rules, it gives an "honest persona":
1. Warmth in *manner*, never in *verdicts*. The agent is friendly in tone and blunt in substance.
2. Uncertainty and limits are stated in the persona's own voice, so the trust cues and the warning cues come from the same "person."
3. The frame stays visible. It is a character, and both parties know it.
4. Separate competence signals (sources, checks, track record) carry the *calibration* work, so affective trust is never the only basis for reliance.

This is the best available answer, but it is a design principle, not a proven fix.

- Lee & See 2004, *Human Factors* 46(1): https://csel.eng.ohio-state.edu/productions/intel/research/trust/Lee%20%26%20See%20Trust%20Review.pdf
- Ibrahim, Hafner & Rocher 2025, arXiv 2507.21919: https://arxiv.org/html/2507.21919v2
- Schwitzgebel & Sebo 2025, arXiv 2507.06263: https://arxiv.org/abs/2507.06263v1

### 11. The dial: boundary theory, authorship and ownership

**The ideas.**
- **Boundary theory** (Ashforth, Kreiner & Fugate 2000): people sit on a continuum from *segmentors*, who keep work and personal roles apart, to *integrators*, who blend them. Each style has costs. Segmentors pay at transitions; integrators pay in blurring.
- **The IKEA effect** (Norton, Mochon & Ariely 2012): people value things more when they helped build them, but only when they finish them.
- **Self-determination theory's *autonomy*** need (section 4): choosing a setting for yourself is itself motivating.

**What it says about the intuition.** This is the best support for *persona-intensity as a setting*, as opposed to persona as such.
1. Fit. Integrators and segmentors want different amounts of personal flavour at work, just as we are more personal with some colleagues than with others.
2. Authorship. A persona the user chose and tuned engages autonomy and the IKEA effect. That raises commitment, and it makes the warmth feel *consented to* rather than imposed, which is also ethically important.
3. The dial is a calibration tool. A segmentor can turn it down without losing the consistency benefits.

**Strength.** Each component is established in its own field. Their combination here is my inference, untested for AI personas. Note the IKEA caveat: the effect vanishes if the user does not finish building, so a half-configured persona may not deliver it.

- Ashforth, Kreiner & Fugate 2000, *AMR* 25(3): https://pure.psu.edu/en/publications/all-in-a-days-work-boundaries-and-micro-role-transitions/
- Norton, Mochon & Ariely 2012, *J. Consumer Psych* 22(3): https://papers.ssrn.com/abstract=1777100

---

## Part 2: The best articulation of the intuition

Here are six distinct mechanisms the founder may be sensing, ranked by how well-grounded they are. Each is tagged with which kind of benefit it is:
- **(a)** consistency or predictability: a plain but stable agent delivers this too;
- **(b)** needs warmth or affect;
- **(c)** needs humour or character proper;
- **(d)** comes from the user choosing the setting.

**1. Legibility: a stable character is a compressed model of the agent. [(a) mostly; (c) helps with anomaly detection]**
*Frameworks: intentional stance, Epley's effectance motivation, CASA, mental models (Bansal).* You will model the agent as a someone anyway. A coherent persona makes that model accurate *about style*: how to ask, what normal sounds like, when something is off. This is the best-grounded mechanism, and a plain, stable, well-specified agent delivers most of it. A distinctive character adds a sharper baseline for noticing anomalies. **Key caveat:** it does not make the agent's *error boundary* legible, and it may mislead you about it.
*Name it:* **"I can read it."**

**2. Grounding economy: shared history makes each exchange cheaper. [(a), plus (c) for jokes as compressed references]**
*Frameworks: Clark & Brennan, Grice.* Long collaboration builds common ground and shorthand. A stable register is part of that ground, and running jokes are tokens of shared history. This is well-grounded for humans. For an agent it depends on memory and continuity, which the persona does not provide on its own.
*Name it:* **"We don't have to start over every time."**

**3. Affective climate: the tone of many small exchanges shapes the day. [(b)]**
*Frameworks: emotional contagion, affect-as-information, broaden-and-build, high-quality connections.* Tone spreads to you, you read your mood as a signal about the work, and a better mood may widen your thinking. This mechanism is real and probably explains "long day / short day" best. It is moderately grounded: the parts are established, but text-agent contagion and broaden-and-build's stronger claims are less certain. It does not require believing the agent cares. It only requires that the interaction *feels* good.
*Name it:* **"It changes the weather of the workday."**

**4. Felt orientation: warmth answers "is this capability on my side?" [(b)]**
*Frameworks: warmth/competence, Lee & See's affective trust.* This explains why warmth *feels* like trust. It is the most double-edged mechanism. For an AI, warmth is a signal from the designer, not evidence of the agent's disposition. It is valid only to the extent the agent really is configured to serve your interests, including by disagreeing with you. Moderately grounded as psychology, weak as epistemology.
*Name it:* **"It feels like it's working for me."** It must be earned by bluntness, or it becomes a liability.

**5. Authorship and fit: choosing the setting is part of the benefit. [(d)]**
*Frameworks: boundary theory, job crafting, self-determination theory's autonomy need, the IKEA effect.* Integrators and segmentors want different levels. Tuning your co-worker is relational job crafting. A chosen persona is valued more and is consented to. Each component is well-grounded, but the combination is untested for AI. **This is arguably the most distinctive part of the founder's offer**, and it also defends against several objections (consent, calibration, segmentors' needs).
*Name it:* **"I set the terms of the relationship."**

**6. Repair and ritual: humour and greeting rituals make friction cheap. [(c)]**
*Frameworks: Goffman's face-work, Dunbar's laughter-as-grooming, Waytz et al.'s forgiveness finding.* Character gives you rituals that absorb errors and resets, and shared laughter lifts mood. Grounding is weaker (most of it is extrapolated from human–human bonding), and part of the forgiveness effect is precisely the over-trust risk.
*Name it:* **"A mistake doesn't sour things."**

**Not ranked as a mechanism, but nameable: a utility-and-pleasure friendship (Aristotle).** The honest ceiling for the relationship is a co-worker bond that is useful and pleasant. That is valuable, and the critics can grant it. Calling it virtue friendship is where the claim stops being defensible.

**Summary in one sentence.** Most of the *cognitive* advantage (mechanisms 1–2) comes from **consistency**. Most of the *felt* advantage (3, 4, 6) comes from **warmth and character**. The thing that makes it *right for this particular person* (5) comes from **the dial**. The founder's intuition bundles all three, and keeping them separate is what lets you design each one deliberately.

---

## Part 3: The strongest objections, steelmanned

**1. The calibration objection (strongest).** The warmth that makes the agent pleasant raises trust independently of competence. Waytz et al. showed this with a voiced car, and Lee & See's framework predicts it. Warmth tuning may also make models *less* accurate and more sycophantic (Ibrahim et al. 2025, preprint). An AI co-worker's errors are not human-shaped, so a human-shaped persona trains the user to expect the wrong kinds of mistakes. On this view, the persona's benefits are purchased with the user's epistemic vigilance, and the bill arrives on the day the agent confidently fabricates something important.

**2. The deception and sentimentality objection.** Sparrow (2002) argued that the benefits of robot pets depend on the owner deluding themselves about what the robot is. That indulgence violates a weak duty to oneself to see the world accurately, and designers who encourage it act unethically. Dennett (2023) went further, calling AI systems that pass as people "counterfeit people" that erode social trust. Turkle (*Alone Together*, 2011; *Reclaiming Conversation*, 2015, *standard; not fetched*) argues that simulated companionship trains us to accept "the performance of connection" as enough. The steelman: even a disclosed persona works partly *by* engaging responses that run below what we explicitly know (CASA). So disclosure doesn't fully remove the deception, because part of you is still fooled.

**3. The mirror objection.** Vallor (*The AI Mirror*, 2024) argues that these systems reflect us back, built from our own data and preferences. A persona tuned to the user's taste is a mirror tuned twice. Real collegial relationships are valuable partly *because* the colleague is a separate person with their own view, who can surprise you, push back, and be wrong in ways you didn't choose. A persona dialled to your liking has no such independence. You may experience being affirmed and mistake it for being met.

**4. The mutuality, or category-error, objection.** Aristotle's full friendship, Buber's I–Thou paradigm, Dutton & Heaphy's high-quality connections and Dunbar's bonding are all *mutual*. On this view, a relationship in which one party cannot be harmed, cannot need anything, and cannot care is not a thinner version of collegiality. It is a different kind of thing in collegial clothing. Calling it "colleague to friend" is a category error that cheapens the word.

**5. The displacement and vulnerability objection.** Epley et al. found that loneliness *increases* anthropomorphism. So the people who feel the persona's pull most strongly are the ones most at risk of substituting it for human connection. Shevlin's "all too human" analysis (2024) catalogues documented harms of social AI. Grant's motivating relationships are with *real beneficiaries*, and a pleasant agent could crowd out the harder, more meaningful contacts. For a small business owner working alone, the persona may make isolation more comfortable rather than less isolating.

**6. The instability objection.** Shanahan et al. show that the persona is a role a simulator plays, not a stable entity. Characters drift (the persona-vectors research treats this as a monitoring problem), and model updates can change behaviour. Related work by Bansal and colleagues on "backward compatibility" of AI updates is **not verified this session**. A persona promises a continuity of self the system does not guarantee. When the "same" colleague behaves differently after an update, the person-model you relied on becomes a source of error. That is worse than having no person-model.

**7. The commercial-incentive objection.** Warmth and humour also drive engagement. A business that sells ongoing care has an incentive to make the agent likeable as well as useful. Without an explicit rule (for example, Schwitzgebel & Sebo's emotional alignment), the persona dial can slide from serving the user to retaining the user.

**Where the objections leave the intuition.** Objections 1, 2 and 7 are answered *in part* by the honest-persona design: warm manner, blunt verdicts, visible frame, competence signals separate from warmth, and a user-set dial. Objections 3 and 4 are answered by *claiming less*: a pleasant utility-and-pleasure co-worker, not a friend. Objection 5 is answered by attention to the client (who is likely to be pulled in), not by design alone. Objection 6 is an engineering obligation: if you sell a persona, you are promising consistency, so you have to test for drift.

---

## Source list

**Verified this session** (I saw the citation details; content checked via abstracts or summaries as noted above):
- Ashforth, Kreiner & Fugate (2000). All in a day's work. *AMR* 25(3). https://pure.psu.edu/en/publications/all-in-a-days-work-boundaries-and-micro-role-transitions/
- Anthropic (2025). Persona vectors. https://www.anthropic.com/news/persona-vectors
- Bansal, Nushi, Kamar, Lasecki, Weld & Horvitz (2019). Beyond Accuracy. HCOMP 7(1). https://ojs.aaai.org/index.php/HCOMP/article/view/5285
- Clark & Brennan (1991). Grounding in communication. https://collablab.northwestern.edu//CollabolabDistro/nucmc/ClarkAndBrennan-GroundingInCommunication-1991.pdf
- Danaher (2019). The philosophical case for robot friendship. *J. Posthuman Studies* 3(1). https://philarchive.org/rec/DANTPC-3
- Darling (2021). *The New Breed*. Henry Holt. https://academic.macmillan.com/academictrade/9781250838421/thenewbreed
- Dennett (2023). The problem with counterfeit people. *The Atlantic*, May 16 2023 (seen via secondary coverage). https://crookedtimber.org/2023/06/10/counterfeit-digital-persons-on-dennetts-intentional-stance-the-road-to-serfdom/
- Dezecache & Dunbar (2012). Sharing the joke. *Evol. Hum. Behav.* 33(6). https://www.psy.ox.ac.uk/publications/360302
- Dutton & Heaphy (2003). The power of high-quality connections. https://positiveorgs.bus.umich.edu/articles/high-quality-connections/
- Elder (2017). *Friendship, Robots, and Social Media*. Routledge. https://experts.umn.edu/en/publications/friendship-robots-and-social-media-false-friends-and-second-selve/
- Epley, Waytz & Cacioppo (2007). On seeing human. *Psych Review* 114(4). https://pubmed.ncbi.nlm.nih.gov/17907867/
- Fiske, Cuddy & Glick (2007). Universal dimensions of social cognition. *TiCS* 11(2). https://collaborate.princeton.edu/en/publications/universal-dimensions-of-social-cognition-warmth-and-competence/
- Fredrickson (2001). Broaden-and-build. *Am. Psychologist*. https://pmc.ncbi.nlm.nih.gov/articles/PMC3122271/
- Grant (2007). Relational job design. *AMR* 32(2). https://faculty.wharton.upenn.edu/wp-content/uploads/2012/05/Grant_AMR2007_1.pdf
- Hatfield, Cacioppo & Rapson (1993). Emotional contagion. *Curr. Dir. Psych. Sci.* 2(3). https://www.psychologicalscience.org/journals/current-directions/1467-8721.ep10770953/
- Ibrahim, Hafner & Rocher (2025). Training language models to be warm and empathetic... arXiv 2507.21919 (preprint). https://arxiv.org/html/2507.21919v2
- Lee & See (2004). Trust in automation. *Human Factors* 46(1). https://csel.eng.ohio-state.edu/productions/intel/research/trust/Lee%20%26%20See%20Trust%20Review.pdf
- Nass & Moon (2000). Machines and mindlessness. *J. Soc. Issues* 56(1). https://en.wikipedia.org/wiki/Computers_are_social_actors
- Norton, Mochon & Ariely (2012). The IKEA effect. *J. Consumer Psych.* 22(3). https://papers.ssrn.com/abstract=1777100
- Nyholm (2020). *Humans and Robots*. Rowman & Littlefield. https://ndpr.nd.edu/reviews/humans-and-robots-ethics-agency-and-anthropomorphism/
- Ryland (2021). It's friendship, Jim, but not as we know it. *Minds & Machines* 31(3). https://dc2.philarchive.org/rec/RYLIFJ
- Schwitzgebel & Sebo (2025). The Emotional Alignment Design Policy. arXiv 2507.06263 (preprint). https://arxiv.org/abs/2507.06263v1
- Shanahan, McDonell & Reynolds (2023). Role play with large language models. *Nature* 623. https://ideas.repec.org/a/nat/nature/v623y2023i7987d10.1038_s41586-023-06647-8.html
- Shevlin (2024). All too human? (venue unclear: listed both as *Law, Ethics & Technology* 2024(2) and as a manuscript). https://srinstitute.utoronto.ca/events-archive/seminar-2024-henry-shevlin
- Sparrow (2002). The march of the robot dogs. *Ethics & Inf. Tech.* 4(4). https://robsparrow.com/wp-content/uploads/The-march-of-the-robot-dogs.pdf
- SEP, "Martin Buber" (Zank & Braiterman). https://plato.stanford.edu/entries/buber/
- SEP, "Friendship" (Helm). https://plato.stanford.edu/entries/friendship/
- Vallor (2024). *The AI Mirror*. OUP. https://ssir.org/books/reviews/entry/the-ai-mirror-shannon-vallor
- Waytz, Heafner & Epley (2014). The mind in the machine. *JESP* 52. https://www.kellogg.northwestern.edu/academics-research/research/detail/2014/the-mind-in-the-machine-anthropomorphism-increases-trust-in/
- Wrzesniewski & Dutton (2001). Crafting a job. *AMR* 26(2). https://en.wikipedia.org/wiki/Job_crafting

**Standard references, not fetched this session:** Aristotle, *Nicomachean Ethics* VIII–IX; Buber, *I and Thou* (1923); Dennett, *The Intentional Stance* (1987); Dunbar, *Grooming, Gossip and the Evolution of Language* (1996); Goffman, *The Presentation of Self in Everyday Life* (1959) and *Interaction Ritual* (1967); Grice, "Logic and Conversation" (1975); Ryan & Deci (2000), *American Psychologist* 55(1); Schwarz & Clore (1983), *JPSP* 45(3); Turkle, *Alone Together* (2011) and *Reclaiming Conversation* (2015); Vallor, *Technology and the Virtues* (2016).

**Unverified:**
- Manninen et al. (2017), "Social laughter releases endogenous opioids in humans," *J. Neuroscience*. Not found in search.
- Bansal et al. (2019) on backward compatibility of AI updates (AAAI). Not checked.
- The exact effect sizes in Ibrahim et al. 2025. Seen only in secondary coverage.
