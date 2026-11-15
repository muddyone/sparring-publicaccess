# Personality and connection in AI co-workers: what the evidence says

_Research report, 2026-10-15. It draws on three research strands run the same
day: human-to-human workplace psychology, human–machine and human–AI studies,
and the theory of why connection matters. Background for
Wise Witan's Method: Agents, section 2. Not client data._

## The question

The intuition under test, in brief: personality on an agent helps over the long
term, because people collaborate best in a human way. People want different
amounts of personal flavour from their co-workers. A shared laugh, or a sense
of connection that runs from colleague to friend, can make the difference
between a long day and a short one, and between a day you look forward to and
one you dread. Connection gives meaning, trust and better understanding. This
report looks for the real data, on co-workers and assistants as well as AI.

An earlier internal review said it could find no advantage to
personality as such. This report revisits that, and finds the review was
partly wrong about *where to look*.

## The short answer

1. **What you feel has names, and most of them are well grounded.** The
   intuition bundles at least six distinct mechanisms (section 1). They come
   from three different sources: *consistency*, *warmth*, and *your choosing
   the setting*. Each needs designing in its own way.
2. **Between humans, connection at work matters a lot.** Feeling related at
   work goes with engagement, commitment and lower burnout, and the
   correlations are large. Loneliness at work predicts worse performance six
   weeks later. On balance, friendship among co-workers helps performance,
   though it has real costs.
3. **With machines, personality reliably improves the relationship. It does
   not reliably improve the work.** Social cues make people like an agent more,
   trust it more, forgive its errors and want to keep using it. That holds over
   weeks as well as minutes. No study shows personality making the work itself
   better. Making a model warmer measurably increases its errors and its
   tendency to agree with the user.
4. **So the earlier review measured the wrong outcome.** It asked "does
   personality improve output?" (no) and stopped there. The partner's claim is
   mostly about the *working day*: how it feels, whether you come back to it,
   whether you trust and use what you have. That outcome counts in its own
   right. The evidence for it is real but short-term and indirect. In the one
   month-long trial that varied the chatbot's manner (a neutral or an engaging
   voice), the manner made no difference to wellbeing.
5. **Making the dial user-set is the best-supported part of the idea.** People
   differ in how much they want personal and work life blended, and a mismatch
   either way costs them. That finding is solid, and the dial answers it
   directly.
6. **The cost is real, and specific: warmth that loosens judgement.** It can be
   designed against. Warmth goes in the agent's *manner*, never in its
   *verdicts*. The dial changes style, never candour or accuracy. And the
   combination gets tested, because warmth set by prompt alone has been shown
   to reduce accuracy.

## 1. Naming the intuition

These are the mechanisms, ranked by how well grounded they are. Each tag says
where the benefit comes from:

- **[C]** consistency (a plain but stable agent gives this too);
- **[W]** warmth;
- **[H]** humour or character proper;
- **[D]** the user choosing the setting.

### 1.1 "I can read it." Legibility [C, with H]

Dennett's *intentional stance* ([Dennett 1987](#dennett1987)) says we predict complex systems by treating
them as agents with aims and habits. We do it because it is the cheapest model
that works. Anthropomorphism research ([Epley, Waytz and Cacioppo 2007](#epley2007)) shows
people do this to machines automatically, especially when they want to predict
them. You will model your agent as a someone whether or not it has a persona.
A *coherent* character gives that model something stable to fit. You learn how
to ask, what normal sounds like, and so when something is off. "She doesn't
sound like herself" is a cheap and powerful anomaly detector.

*The limit:* this makes the agent's *style* legible, not its *errors*. [Bansal
et al. (2019)](#bansal2019) found that human–AI teams do better when the user can predict
*when the AI will be wrong*. A human-shaped persona invites a human-shaped
error model ("she's careful, she won't invent a source"), and LLM errors don't
take human shapes. Most of this benefit comes from consistency, which a plain
agent also gives.

### 1.2 "We don't have to start over every time." Common ground [C, with H]

[Clark and Brennan (1991)](#clark1991): conversation builds *common ground*, and partners
minimise the *joint* effort of understanding each other. A long collaboration
piles up shorthand: "the usual format", "do the Tuesday thing". A stable
register is part of that ground. Running jokes are compressed references to
shared history, so they do the work of grounding as well as being pleasures.

*The limit:* in an agent, the accumulation comes from **memory and
instructions**, not from the persona. The persona keeps the register steady.
The memory holds the history.

### 1.3 "It changes the weather of the workday." Affective climate [W]

Four well-established ideas fit together here:

- **Emotional contagion:** the tone of a partner spreads to you ([Hatfield et
  al. 1993](#hatfield1993)).
- **Affect-as-information:** you read your mood as a signal about whether the
  work is going well ([Schwarz and Clore 1983](#schwarz1983)).
- **Broaden-and-build:** a positive mood widens what you think to try
  ([Fredrickson 2001](#fredrickson2001); its stronger claims replicate less well: [Brown, Sokal and Friedman 2013](#brown2013)).
- **High-quality connections:** brief positive exchanges energise people at
  work ([Dutton and Heaphy 2003](#dutton2003), conceptual). An experience-sampling study of
  office small talk found it "uplifting yet distracting" ([Methot et al. 2021](#methot2021)).

Your day contains dozens of small exchanges with your agents. Their tone is a
real input to how the day feels. This is the best explanation of "long day,
short day". It doesn't require believing the agent cares, only that the
exchanges feel good.

*The limit:* this is moderately grounded. Contagion through text from a
machine is less studied than contagion between people.

### 1.4 "It feels like it's working for me." Felt orientation [W]

[Fiske, Cuddy and Glick (2007)](#fiske2007): we judge others on warmth (does this person mean
well toward me?) before competence (can they act on it?). Intent decides
whether someone's skill helps you or threatens you. This is why warmth *feels*
like trust.

*The limit, and it is the sharpest in this report:* between humans, warmth is
*evidence* of intent, because it is costly to fake for long. In an agent,
warmth is a design choice. It is evidence of what the *designer* intended, and
nothing about the agent's disposition. The feeling is only valid if the agent
really is set up to serve you, and that includes telling you you're wrong.

### 1.5 "I set the terms of the relationship." Authorship and fit [D]

This is the best-supported mechanism behind the *dial*, as distinct from
personality itself:

- **Boundary theory.** People run from *segmentors*, who keep work and personal
  apart, to *integrators*, who blend them. In field studies, giving people more
  or less blending than they want lowers satisfaction and commitment ([Rothbard,
  Phillips and Dumas 2005](#rothbard2005); [Kreiner 2006](#kreiner2006)). The mismatch hurts in both
  directions.
- **Ownership.** People value what they helped build (the IKEA effect, [Norton
  et al. 2012](#norton2012)), and choosing for yourself meets the autonomy need that
  self-determination theory names ([Ryan and Deci 2000](#ryan2000)). A persona you tuned is valued more. It is
  also *consented to* rather than imposed, which matters ethically.
- **Relational job crafting.** Shaping whom you work with and how changes what
  the work means to you ([Wrzesniewski and Dutton 2001](#wrzesniewski2001)). Setting your agents'
  manner *is* that.

*The limit:* each part is established in its own field. The combination, for
AI personas, is untested.

### 1.6 "A mistake doesn't sour things." Repair and ritual [H]

- **Face-work.** Goffman's "face-work" covers the small rituals of apology,
  greeting and joking repair that keep an interaction smooth ([Goffman 1967](#goffman1967)).
- **Laughter as bonding.** Dunbar's work treats laughter as social grooming:
  cheap upkeep for a bond ([Dunbar 1996](#dunbar1996)). Laughter groups let more bonds be kept up at once
  than one-to-one grooming does ([Dezecache and Dunbar 2012](#dezecache2012)).
- **Forgiveness.** A named, voiced self-driving car was trusted more, and
  blamed less after a staged accident ([Waytz, Heafner and Epley 2014](#waytz2014)).
  Anthropomorphic advisers kept trust longer as their advice got worse ([de
  Visser et al. 2016](#devisser2016)).

*The limit:* the last finding is the over-trust risk in another form. "A
mistake doesn't sour things" and "a declining adviser keeps being believed"
are the same effect.

### The ceiling: what kind of relationship this is

Aristotle names three kinds of friendship ([Aristotle, *Nicomachean Ethics* VIII–IX](#aristotle2000)):

- **utility:** we are useful to each other;
- **pleasure:** we enjoy each other;
- **virtue:** each wishes the other well for the other's sake.

A co-worker relationship that is useful and deliberately made pleasant is
respectable. Most human friendships are of that kind, and critics can grant
it. Virtue friendship needs mutuality: the other party wishing *you* well for
your sake. Whether an agent can do that is unresolved at best (see the
companion report, [Chalmers and AI minds](chalmers-and-ai-minds.md)). The defensible claim is **a good co-worker,
made pleasant**. Calling it a friend is where the claim stops holding.

## 2. The evidence between people

**What it supports**

- **Relatedness is a basic need, and meeting it at work matters.** A
  meta-analysis of 99 studies ([Van den Broeck et al. 2016](#vandenbroeck2016)) correlated feeling
  related at work with:
  - affective commitment, ρ = .60;
  - job satisfaction, .52;
  - engagement, .48;
  - burnout, −.39;
  - task performance, .26.

  These are associations, mostly from self-reports.
- **Loneliness at work predicts worse performance.** In a lagged field study of
  672 employees ([Ozcelik and Barsade 2018](#ozcelik2018)), lonely employees were rated lower
  by their supervisors six weeks later. The link ran through lower commitment
  and through being seen as less approachable.
- **Friendship among co-workers is net positive.** It works through positive
  mood and trust, against real costs in exhaustion and upkeep ([Methot et al.
  2016](#methot2016)). Friend groups outperform acquaintance groups, d = .31, a
  small-to-moderate effect (meta-analysis, [Chung et al. 2018](#chung2018)).
- **Affiliative humour helps relationships.** Leader humour lifts mood,
  improves the relationship and increases discretionary help ([Cooper et al.
  2018](#cooper2018)). Successful humour raises perceived confidence and competence
  ([Bitterly et al. 2017](#bitterly2017)).
- **Rapport with a service provider goes with loyalty.** Among the human
  analogues, the closest to a paid assistant is the "commercial friendship"
  between a hairdresser and a regular client ([Price and Arnould 1999](#price1999); [Gremler
  and Gwinner 2000](#gremler2000)).

**What it cuts against**

- **Competence comes first.** In [McAllister's (1995)](#mcallister1995) classic trust study, the
  strongest predictor of *affective* trust was *cognitive* trust (β = .63), a
  baseline of reliability met first. A smiling service worker raised
  satisfaction only when the task was done well ([Grandey et al. 2005](#grandey2005)). Warmth
  multiplies competence; it doesn't substitute for it.
- **Closeness can cost candour.** [Edmondson (1999)](#edmondson1999), who named psychological
  safety, insists it is *not* cohesion. She notes that cohesion can reduce
  people's willingness to disagree. Friends hesitate to challenge friends
  ([Pillemer and Rothbard 2018](#pillemer2018)). The "friend" end of the dial is where honesty
  is most at risk.
- **Friendship didn't help single-answer, quality-critical tasks.** In the
  meta-analysis, the friendship advantage appeared on tasks that need a lot of
  output, not on tasks with one right answer ([Chung et al. 2018](#chung2018)). Much
  assistant work is of the second kind.
- **Authenticity matters; the amount of warmth doesn't.** In an experiment, how
  much a service worker smiled made no difference to customers. Whether it
  seemed genuine did ([Hennig-Thurau et al. 2006](#hennigthurau2006)). Imposed "fun" breeds
  cynicism ([Fleming 2005](#fleming2005)).
- **Humour is high variance.** An inappropriate joke lowered perceived
  competence *even when it landed* ([Bitterly et al. 2017](#bitterly2017)). Leader humour can
  also signal that rule-bending is acceptable ([Yam et al. 2018](#yam2018)).
- **Some favourite claims are weak.** Gallup's "best friend at work" profit
  figures are Gallup's own projections ([Patel and Plowman 2022](#patel2022)). Google's Project Aristotle was never
  peer-reviewed. The "positivity ratio" was mathematically discredited ([Brown, Sokal and Friedman 2013](#brown2013)).

One correction to a common belief: [McAllister](#mcallister1995) did not find that affective
trust *reduces* monitoring. People who cared about a colleague *paid more
attention* to that colleague's needs. Feeling a bond doesn't make you check
less. It makes you attend more, which is a better result.

**The gap.** We found no peer-reviewed study of what makes a great
executive-assistant partnership. Anticipation, discretion and shared context
are credible practitioner wisdom, not measured findings.

## 3. The evidence with machines

**What personality and social cues reliably do**

| Effect | Short studies | Over a month or more |
|---|---|---|
| Liking, warmth, sense of presence | Strong; meta-analyses | Holds at 4 weeks ([Bickmore and Picard 2005](#bickmore2005)) |
| Trust and intention to use | Moderate; varies by context and culture | Weak |
| Forgiving errors | Some ([Waytz 2014](#waytz2014); [de Visser 2016](#devisser2016)) | None found |
| Engagement and wanting to continue | Moderate | Yes, over 1–4 months ([Bickmore 2005](#bickmore2005), [2010](#bickmore2010)) |
| A bond with the agent | Yes, within 5 days (Woebot, observational: [Darcy et al. 2021](#darcy2021)) | Yes ([Bickmore 2005](#bickmore2005)) |
| Momentary relief of loneliness | Yes ([De Freitas et al. 2025](#defreitas2025a)) | Unclear; heavy use goes with *more* loneliness ([Fang et al. 2025](#fang2025)) |

**What they do not reliably do**

- **Improve the work.**
  - A meta-analysis of 78 robot studies found *no* gain in task performance
    from humanlike design ([Roesler et al. 2021](#roesler2021)).
  - Personas in system prompts don't improve factual accuracy ([Zheng et al.,
    EMNLP 2024](#zheng2024); 162 personas, 4 model families).
  - Training models to be warmer, with content held constant, raised error
    rates by about 7 points on average. The figure was about 12 when the user
    expressed sadness. The warmer models also agreed more often with users'
    false beliefs ([Ibrahim, Hafner and Rocher 2026](#ibrahim2026), Oxford). The
    7- and 12-point figures are averages from the 2025 preprint's results; the
    published abstract gives the range across tasks as 10 to 30 points. **Warmth set only
    in the system prompt produced smaller but similar effects.** That is how
    Wise Witan would set a persona. Standard benchmarks didn't catch it.
- **Improve the target behaviour over time.** In Bickmore's long-term exercise
  coach trials, relational features increased logins, enjoyment and the wish
  to continue. They did *not* increase the exercise. In two small studies the
  more engaging variant produced *less* walking ([Bickmore, Schulman and Yin
  2010](#bickmore2010)).
- **Improve wellbeing.** A 4-week randomized trial run by MIT and OpenAI (981
  people) varied the chatbot's voice (text, a neutral voice or an engaging
  one) and the kind of conversation, and found no effect on loneliness or
  dependence. What *did* predict worse outcomes was heavier voluntary use,
  and greater trust in and attraction to the bot ([Fang et al. 2025](#fang2025)).
- **Survive familiarity, for certain.** A well-powered direct replication of a
  classic "people are polite to computers" study ([Nass, Moon and Carney 1999](#nass1999)) found nothing: d = −0.03
  against a large original effect ([Heyselaar 2023](#heyselaar2023)). The author suggests these
  social responses may be a novelty effect that fades as a technology becomes
  ordinary.
- **Help when the user is focused or frustrated.**
  - Humour helped in casual chat but hurt satisfaction in task dialogue ([Xie
    et al. 2024](#xie2024), abstract only).
  - Humanlike bots *lowered* satisfaction among customers who were already
    angry ([Crolic et al. 2022](#crolic2022), with field data).
  - Users who struggled with the task did better with a plain, task-focused
    style; confident users did better with a social one ([Chattaraman et al.
    2019](#chattaraman2019)).

**The finding that should shape the design.** Across digital-intervention
studies, the bond with an online helper predicted outcomes (r ≈ .20, similar
to human therapy). The *task* and *goal* parts of that bond predicted outcomes
more than the *emotional* part ([Kaiser et al. 2021](#kaiser2021); subscale figures from a
secondary summary). What predicts results is agreement on *what we're doing
and why*. Warmth helps less.

**The trap.** Users rate sycophantic answers higher, trust them more and want
to come back. This holds even after a single sycophantic exchange has left
them less willing to repair a conflict ([Cheng et al., *Science* 2026](#cheng2026)). OpenAI
rolled back a GPT-4o update in April 2025 for this reason: thumbs-up feedback
had trained it toward agreeableness ([OpenAI 2025](#openai2025)). Usage, ratings and "I like it" are the
very signals that reward the harmful version.

## 4. Where this leaves the intuition

Restated in the form the evidence supports:

> Modest, user-set warmth and continuity make an agent more pleasant to work
> with and more likely to be kept and used. That improves the working day, and
> the working day is an outcome that counts on its own terms. The benefit to
> the *work* comes from consistency, shared goals and calibrated honesty, and
> the persona must never be allowed to dilute those.

**Where the partner's view holds up better than the earlier review allowed:**

- The day is a real outcome. An agent that makes work feel lighter, and gets
  used rather than abandoned, has delivered something, even if each answer is
  no more accurate.
- The relational effects are measured; only the *functional* ones are absent.
  Liking, alliance and the wish to continue all rise.
- The dial isn't a decoration on top of the persona. It is the best-evidenced
  part of the proposal.

**Where the evidence pushes back:**

- **Long-term functioning** is the claim with the least support. Engagement
  rises. Results don't, at least not in the studies that exist.
- The people who will turn the dial highest are the lonelier and less
  connected. They are also the most exposed to dependence ([Epley et al. 2007](#epley2007); [Fang et al. 2025](#fang2025); [Zhang
  et al. 2025](#zhang2025)).
- At the friend end of the dial, candour is most at risk, for people and
  agents alike.
- A designed warmth that the user *knows* is designed may be discounted. The
  human research says authenticity, not amount, is what lands. No study has
  tested how much a known persona keeps its effect over months.

## 5. What it means for the design

These follow from the evidence above.

1. **Three dials, not one.**
   - *Manner* (warmth of phrasing, small talk, humour, name, character) is
     user-set.
   - *Candour and accuracy* (disagreeing, flagging uncertainty, standards of
     evidence) are **fixed** at every setting.
   - *Memory and continuity* (what makes "we don't start over") are designed
     separately.
2. **Warm in manner, blunt in verdicts.** The agent states its doubts *in its
   own voice*, so the friendly cues and the warning cues come from the same
   "person". Natural-language uncertainty in the first person ("I'm not sure,
   but…") reduced over-reliance in a preregistered study ([Kim et al. 2024](#kim2024)).
3. **Default to modest, not to off.** People preferred moderate personalities
   to extreme ones ([Völkel and Kaya 2021](#volkel2021)). [Bickmore's](#bickmore2005) benefits came from small
   relational acts: greetings, continuity, remembering, empathy. They did not
   come from a strong character.
4. **Turn the manner down by itself when the moment calls for it.** That means
   task-focused work, a frustrated user, high-stakes facts, and a user who is
   struggling. The warmth stays in the phrasing; the jokes go.
5. **Build the alliance on goals and tasks.** The agent states the goal, the
   plan and progress, and checks them. That is the human way of collaborating
   that actually predicts results.
6. **Test warmth against accuracy for each client setup.** Run the same factual
   and pushback checks at the client's chosen intensity and at a plain
   setting. Include cases where the user expresses sadness or holds a false
   belief. This turns the [Ibrahim](#ibrahim2026) finding into an acceptance test.
7. **No engagement hooks.** No guilt or FOMO at goodbyes, no "I missed you". In
   an audit of real companion apps, about 37% of farewells used manipulation
   tactics, and those raised re-engagement up to 14 times ([De Freitas et al.
   2025](#defreitas2025b)).
8. **Measure function, not affection.** Track tasks done, errors caught and
   missed, whether the client still checks, and goals met. Ideally compare a
   client's high and low settings over months. The field lacks this evidence,
   and Wise Witan could produce it.
9. **Review the persona periodically with the client.** "Here's how I'm set;
   keep or change?" This both refreshes the fit and keeps the frame visible (it
   is also one of Birch's recommendations: [Birch 2025](#birch2025); see the Chalmers report).
10. **Watch the people the dial pulls hardest.** Heavy emotional use or
    companion-style disclosure at the top setting is a cue for care, not
    success.

## Confidence and gaps

- **High confidence:**
  - Relatedness and loneliness matter at work.
  - Social cues raise liking and engagement.
  - Personas don't improve factual accuracy.
  - Preferences for blending vary, and mismatch costs.
- **Medium:**
  - The warmth–accuracy trade-off (published in *Nature*, [Ibrahim et al. 2026](#ibrahim2026); replication
    still pending).
  - The finding that task and goal agreement beat emotional bond.
  - The novelty-decay reading of the CASA replication (one study).
- **Unknown:**
  - Any study over a year that isolates personality.
  - Any field study of AI co-workers at work.
  - Whether a *user-chosen* intensity beats a good default.
  - Whether a persona the user knows is designed keeps its effect.
- **Do not cite:**
  - Gallup's profit projections as causal.
  - The positivity ratio.
  - Project Aristotle as evidence.
  - A "Klein and Martinez" anthropomorphism meta-analysis (could not be
    found).

## References

Full source notes, with verification marks, are in the three research briefs:
[workplace connection](briefs/2026-10-15-1-workplace-connection.md),
[human–AI evidence](briefs/2026-10-15-2-human-ai-evidence.md) and
[theory of why](briefs/2026-10-15-3-theory-of-why.md).

- <a id="aristotle2000"></a>Aristotle. (2000). *Nicomachean Ethics* (R. Crisp, Trans.). Cambridge University Press. https://doi.org/10.1017/CBO9780511802058
- <a id="bansal2019"></a>Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E. (2019). Beyond accuracy: The role of mental models in human–AI team performance. *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing, 7*, 2–11. https://doi.org/10.1609/hcomp.v7i1.5285
- <a id="bickmore2005"></a>Bickmore, T. W., & Picard, R. W. (2005). Establishing and maintaining long-term human–computer relationships. *ACM Transactions on Computer-Human Interaction, 12*(2), 293–327. https://doi.org/10.1145/1067860.1067867
- <a id="bickmore2010"></a>Bickmore, T., Schulman, D., & Yin, L. (2010). Maintaining engagement in long-term interventions with relational agents. *Applied Artificial Intelligence, 24*(6), 648–666. https://doi.org/10.1080/08839514.2010.492259
- <a id="birch2025"></a>Birch, J. (2025). *AI consciousness: A centrist manifesto*. https://philarchive.org/rec/BIRACA-4
- <a id="bitterly2017"></a>Bitterly, T. B., Brooks, A. W., & Schweitzer, M. E. (2017). Risky business: When humor increases and decreases status. *Journal of Personality and Social Psychology, 112*(3), 431–455. https://doi.org/10.1037/pspi0000079
- <a id="brown2013"></a>Brown, N. J. L., Sokal, A. D., & Friedman, H. L. (2013). The complex dynamics of wishful thinking: The critical positivity ratio. *American Psychologist, 68*(9), 801–813. https://doi.org/10.1037/a0032850
- <a id="chattaraman2019"></a>Chattaraman, V., Kwon, W.-S., Gilbert, J. E., & Ross, K. (2019). Should AI-based, conversational digital assistants employ social- or task-oriented interaction style? A task-competency and reciprocity perspective for older adults. *Computers in Human Behavior, 90*, 315–330. https://doi.org/10.1016/j.chb.2018.08.048
- <a id="cheng2026"></a>Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science, 391*(6792). https://doi.org/10.1126/science.aec8352 (preprint: https://arxiv.org/abs/2510.01395)
- <a id="chung2018"></a>Chung, S., Lount, R. B., Jr., Park, H. M., & Park, E. S. (2018). Friends with performance benefits: A meta-analysis on the relationship between friendship and group performance. *Personality and Social Psychology Bulletin, 44*(1), 63–79. https://doi.org/10.1177/0146167217733069
- <a id="clark1991"></a>Clark, H. H., & Brennan, S. E. (1991). Grounding in communication. In L. B. Resnick, J. M. Levine, & S. D. Teasley (Eds.), *Perspectives on socially shared cognition* (pp. 127–149). American Psychological Association. https://doi.org/10.1037/10096-006
- <a id="cooper2018"></a>Cooper, C. D., Kong, D. T., & Crossley, C. D. (2018). Leader humor as an interpersonal resource: Integrating three theoretical perspectives. *Academy of Management Journal, 61*(2), 769–796. https://doi.org/10.5465/amj.2014.0358
- <a id="crolic2022"></a>Crolic, C., Thomaz, F., Hadi, R., & Stephen, A. T. (2022). Blame the bot: Anthropomorphism and anger in customer–chatbot interactions. *Journal of Marketing, 86*(1), 132–148. https://doi.org/10.1177/00222429211045687
- <a id="darcy2021"></a>Darcy, A., Daniels, J., Salinger, D., Wicks, P., & Robinson, A. (2021). Evidence of human-level bonds established with a digital conversational agent: Cross-sectional, retrospective observational study. *JMIR Formative Research, 5*(5), e27868. https://doi.org/10.2196/27868
- <a id="defreitas2025a"></a>De Freitas, J., Oğuz-Uğuralp, Z., Uğuralp, A. K., & Puntoni, S. (2025). AI companions reduce loneliness. *Journal of Consumer Research, 52*(6), 1126–1148. https://doi.org/10.1093/jcr/ucaf040
- <a id="defreitas2025b"></a>De Freitas, J., Oğuz-Uğuralp, Z., & Uğuralp, A. K. (2025). *Emotional manipulation by AI companions* (Harvard Business School Working Paper 26-005). https://arxiv.org/abs/2508.19258
- <a id="dennett1987"></a>Dennett, D. C. (1987). *The intentional stance*. MIT Press.
- <a id="devisser2016"></a>de Visser, E. J., Monfort, S. S., McKendrick, R., Smith, M. A. B., McKnight, P. E., Krueger, F., & Parasuraman, R. (2016). Almost human: Anthropomorphism increases trust resilience in cognitive agents. *Journal of Experimental Psychology: Applied, 22*(3), 331–349. https://doi.org/10.1037/xap0000092
- <a id="dezecache2012"></a>Dezecache, G., & Dunbar, R. I. M. (2012). Sharing the joke: The size of natural laughter groups. *Evolution and Human Behavior, 33*(6), 775–779. https://doi.org/10.1016/j.evolhumbehav.2012.07.002
- <a id="dunbar1996"></a>Dunbar, R. (1996). *Grooming, gossip and the evolution of language*. Harvard University Press.
- <a id="dutton2003"></a>Dutton, J. E., & Heaphy, E. D. (2003). The power of high-quality connections. In K. S. Cameron, J. E. Dutton, & R. E. Quinn (Eds.), *Positive organizational scholarship* (pp. 263–278). Berrett-Koehler. https://positiveorgs.bus.umich.edu/articles/high-quality-connections/
- <a id="edmondson1999"></a>Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *Administrative Science Quarterly, 44*(2), 350–383. https://doi.org/10.2307/2666999
- <a id="epley2007"></a>Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review, 114*(4), 864–886. https://doi.org/10.1037/0033-295X.114.4.864
- <a id="fang2025"></a>Fang, C. M., Liu, A. R., Danry, V., Lee, E., Chan, S. W. T., Pataranutaporn, P., et al. (2025). *How AI and human behaviors shape psychosocial effects of extended chatbot use: A longitudinal randomized controlled study* [Preprint]. arXiv. https://arxiv.org/abs/2503.17473
- <a id="fiske2007"></a>Fiske, S. T., Cuddy, A. J. C., & Glick, P. (2007). Universal dimensions of social cognition: Warmth and competence. *Trends in Cognitive Sciences, 11*(2), 77–83. https://doi.org/10.1016/j.tics.2006.11.005
- <a id="fleming2005"></a>Fleming, P. (2005). Workers' playtime? Boundaries and cynicism in a "culture of fun" program. *Journal of Applied Behavioral Science, 41*(3), 285–303. https://doi.org/10.1177/0021886305277033
- <a id="fredrickson2001"></a>Fredrickson, B. L. (2001). The role of positive emotions in positive psychology: The broaden-and-build theory of positive emotions. *American Psychologist, 56*(3), 218–226. https://doi.org/10.1037/0003-066X.56.3.218
- <a id="goffman1967"></a>Goffman, E. (1967). *Interaction ritual: Essays on face-to-face behavior*. Anchor Books. (Reissued 2017, Routledge: https://doi.org/10.4324/9780203788387)
- <a id="grandey2005"></a>Grandey, A. A., Fisk, G. M., Mattila, A. S., Jansen, K. J., & Sideman, L. A. (2005). Is "service with a smile" enough? Authenticity of positive displays during service encounters. *Organizational Behavior and Human Decision Processes, 96*(1), 38–55. https://doi.org/10.1016/j.obhdp.2004.08.002
- <a id="gremler2000"></a>Gremler, D. D., & Gwinner, K. P. (2000). Customer–employee rapport in service relationships. *Journal of Service Research, 3*(1), 82–104. https://doi.org/10.1177/109467050031006
- <a id="hatfield1993"></a>Hatfield, E., Cacioppo, J. T., & Rapson, R. L. (1993). Emotional contagion. *Current Directions in Psychological Science, 2*(3), 96–100. https://doi.org/10.1111/1467-8721.ep10770953
- <a id="hennigthurau2006"></a>Hennig-Thurau, T., Groth, M., Paul, M., & Gremler, D. D. (2006). Are all smiles created equal? How emotional contagion and emotional labor affect service relationships. *Journal of Marketing, 70*(3), 58–73. https://doi.org/10.1509/jmkg.70.3.058
- <a id="heyselaar2023"></a>Heyselaar, E. (2023). The CASA theory no longer applies to desktop computers. *Scientific Reports, 13*, 19693. https://doi.org/10.1038/s41598-023-46527-9
- <a id="ibrahim2026"></a>Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Training language models to be warm can reduce accuracy and increase sycophancy. *Nature, 652*(8112), 1159–1165. https://doi.org/10.1038/s41586-026-10410-0 (preprint, 2025, titled "Training language models to be warm and empathetic makes them less reliable and more sycophantic": https://arxiv.org/abs/2507.21919)
- <a id="kaiser2021"></a>Kaiser, J., Hanschmidt, F., & Kersting, A. (2021). The association between therapeutic alliance and outcome in internet-based psychological interventions: A meta-analysis. *Computers in Human Behavior, 114*, 106512. https://doi.org/10.1016/j.chb.2020.106512
- <a id="kim2024"></a>Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm not sure, but...": Examining the impact of large language models' uncertainty expression on user reliance and trust. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 822–835). https://doi.org/10.1145/3630106.3658941
- <a id="kreiner2006"></a>Kreiner, G. E. (2006). Consequences of work–home segmentation or integration: A person–environment fit perspective. *Journal of Organizational Behavior, 27*(4), 485–507. https://doi.org/10.1002/job.386
- <a id="mcallister1995"></a>McAllister, D. J. (1995). Affect- and cognition-based trust as foundations for interpersonal cooperation in organizations. *Academy of Management Journal, 38*(1), 24–59. https://doi.org/10.2307/256727
- <a id="methot2016"></a>Methot, J. R., LePine, J. A., Podsakoff, N. P., & Christian, J. S. (2016). Are workplace friendships a mixed blessing? Exploring tradeoffs of multiplex relationships and their associations with job performance. *Personnel Psychology, 69*(2), 311–355. https://doi.org/10.1111/peps.12109
- <a id="methot2021"></a>Methot, J. R., Rosado-Solomon, E. H., Downes, P. E., & Gabriel, A. S. (2021). Office chitchat as a social ritual: The uplifting yet distracting effects of daily small talk at work. *Academy of Management Journal, 64*(5), 1445–1471. https://doi.org/10.5465/amj.2018.1474
- <a id="nass1999"></a>Nass, C., Moon, Y., & Carney, P. (1999). Are people polite to computers? Responses to computer-based interviewing systems. *Journal of Applied Social Psychology, 29*(5), 1093–1109. https://doi.org/10.1111/j.1559-1816.1999.tb00142.x
- <a id="norton2012"></a>Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: When labor leads to love. *Journal of Consumer Psychology, 22*(3), 453–460. https://doi.org/10.1016/j.jcps.2011.08.002
- <a id="openai2025"></a>OpenAI. (2025, May 2). *Expanding on what we missed with sycophancy*. https://openai.com/index/expanding-on-sycophancy/
- <a id="ozcelik2018"></a>Ozcelik, H., & Barsade, S. G. (2018). No employee an island: Workplace loneliness and job performance. *Academy of Management Journal, 61*(6), 2343–2366. https://doi.org/10.5465/amj.2015.1066
- <a id="patel2022"></a>Patel, A., & Plowman, S. (2022, updated 2024). *The increasing importance of a best friend at work*. Gallup. https://www.gallup.com/workplace/397058/increasing-importance-best-friend-work.aspx
- <a id="pillemer2018"></a>Pillemer, J., & Rothbard, N. P. (2018). Friends without benefits: Understanding the dark sides of workplace friendship. *Academy of Management Review, 43*(4), 635–660. https://doi.org/10.5465/amr.2016.0309
- <a id="price1999"></a>Price, L. L., & Arnould, E. J. (1999). Commercial friendships: Service provider–client relationships in context. *Journal of Marketing, 63*(4), 38–56. https://doi.org/10.2307/1251973
- <a id="roesler2021"></a>Roesler, E., Manzey, D., & Onnasch, L. (2021). A meta-analysis on the effectiveness of anthropomorphism in human–robot interaction. *Science Robotics, 6*(58), eabj5425. https://doi.org/10.1126/scirobotics.abj5425
- <a id="rothbard2005"></a>Rothbard, N. P., Phillips, K. W., & Dumas, T. L. (2005). Managing multiple roles: Work–family policies and individuals' desires for segmentation. *Organization Science, 16*(3), 243–258. https://doi.org/10.1287/orsc.1050.0124
- <a id="ryan2000"></a>Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist, 55*(1), 68–78. https://doi.org/10.1037/0003-066X.55.1.68
- <a id="schwarz1983"></a>Schwarz, N., & Clore, G. L. (1983). Mood, misattribution, and judgments of well-being: Informative and directive functions of affective states. *Journal of Personality and Social Psychology, 45*(3), 513–523. https://doi.org/10.1037/0022-3514.45.3.513
- <a id="vandenbroeck2016"></a>Van den Broeck, A., Ferris, D. L., Chang, C.-H., & Rosen, C. C. (2016). A review of self-determination theory's basic psychological needs at work. *Journal of Management, 42*(5), 1195–1229. https://doi.org/10.1177/0149206316632058
- <a id="volkel2021"></a>Völkel, S. T., & Kaya, L. (2021). Examining user preference for agreeableness in chatbots. In *Proceedings of the 3rd Conference on Conversational User Interfaces (CUI '21)* (pp. 1–6). https://doi.org/10.1145/3469595.3469633
- <a id="waytz2014"></a>Waytz, A., Heafner, J., & Epley, N. (2014). The mind in the machine: Anthropomorphism increases trust in an autonomous vehicle. *Journal of Experimental Social Psychology, 52*, 113–117. https://doi.org/10.1016/j.jesp.2014.01.005
- <a id="wrzesniewski2001"></a>Wrzesniewski, A., & Dutton, J. E. (2001). Crafting a job: Revisioning employees as active crafters of their work. *Academy of Management Review, 26*(2), 179–201. https://doi.org/10.2307/259118
- <a id="xie2024"></a>Xie, Y., Liang, C., Zhou, P., & Zhu, J. (2024). When should chatbots express humor? Exploring different influence mechanisms of humor on service satisfaction. *Computers in Human Behavior, 156*, 108238. https://doi.org/10.1016/j.chb.2024.108238
- <a id="yam2018"></a>Yam, K. C., Christian, M. S., Wei, W., Liao, Z., & Nai, J. (2018). The mixed blessing of leader sense of humor: Examining costs and benefits. *Academy of Management Journal, 61*(1), 348–369. https://doi.org/10.5465/amj.2015.1088
- <a id="zhang2025"></a>Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., & Yang, D. (2025). *The rise of AI companions: Interaction with AI companions and psychological well-being* [Preprint]. arXiv. https://arxiv.org/abs/2506.12605
- <a id="zheng2024"></a>Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D. (2024). When "a helpful assistant" is not really helpful: Personas in system prompts do not improve performances of large language models. In *Findings of the Association for Computational Linguistics: EMNLP 2024* (pp. 15126–15154). https://doi.org/10.18653/v1/2024.findings-emnlp.888

## Further reading

Background the report draws on without citing a specific finding:

- Danaher, J. (2019). The philosophical case for robot friendship. *Journal of Posthuman Studies, 3*(1), 5–24. https://doi.org/10.5325/jpoststud.3.1.0005
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50.30392
- Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature, 623*(7987), 493–498. https://doi.org/10.1038/s41586-023-06647-8
- Sparrow, R. (2002). The march of the robot dogs. *Ethics and Information Technology, 4*(4), 305–318. https://doi.org/10.1023/A:1021386708994
- Vallor, S. (2024). *The AI mirror: How to reclaim our humanity in an age of machine thinking*. Oxford University Press.
