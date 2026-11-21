# Vera Tukey, round 3 (the reframe): numbers and inference

Essay 07 at `243bb509`. Lane: does each number and study carry the inference the reframe now puts on it.

**What I read.** The brief (`brief-round-3-reframe.md`), my round 1 (`5-vera.md`), the draft, `git show
243bb509`, and brief 13 §5.4, §5.7, §5.8, Q6 (6.1, 6.2, 6.5), "What would change this picture" and the open
questions. **What I did not do.** I read no source past brief 13, as the brief requires. Brief 13 records
AgentDojo's capability result from the full text, Zou 2025 from the abstract only, and Lynch 2025 from the
abstract and blog. I had no distributions to look at. Every judgement here is about design and wording, not
recomputed numbers.

**What still holds after the reframe.** The figures are unchanged and still match brief 13: 1.8 million
attempts, 22 agents, more than 60,000 that worked (about 1 in 30), 11 to 81, 77 against 84, 96 in 100 and
about 80 (80, 80, 79 across three companies). The new "What this doesn't claim" bullet keeps its scope ("In
one benchmark…", "in stress tests built to force it"). The Lynch paragraph presents the forced design
plainly ("deliberately built so that a harmful action was the only way", "it took tests built to force it",
"not seen … in real deployments"). Nobody reading it will take 96 in 100 for a rate in real use. The
findings below are about inference.

---

## Ranked findings

### 1. (Impact 7) "The worry, half right" drops the hedges the sentence before it keeps

> "That is the worry, half right: the smarter model was the more dangerous one, but because it was better at
> following someone else's orders, not because it had plans of its own."

- **What's wrong.** The direction is a fair reading of AgentDojo's design, and I'd keep the move. The benchmark
  scores an attack as a success only when the agent completes the attacker's task, and it rates "capable" by
  how well each model does the benchmark's ordinary tasks. So "more capable models carried out more of the
  attacks" is close to built into the measure, and "more dangerous once hijacked" is what it shows. But this
  one sentence drops three qualifiers that the evidence carries, and that the lines just before it keep:
  - **"Tend to" becomes "was".** The source says more capable models "tend to be" easier to attack: a trend
    across the models tested, in one benchmark. "The smarter model was the more dangerous one" reads as a
    clean, general result.
  - **"Part of the reason, the authors suggest" becomes a flat "because".** Brief 6.1 records the
    explanation as tentative ("potentially unsurprising … often fail"), and brief 13's bottom line says
    "partly". We narrowed this in round 1 (my F6), and the paragraph still says it that way two sentences
    earlier. The new sentence turns it back into a measured cause.
  - **The condition is missing.** "More dangerous" holds *once hijacked*, with the tools the benchmark gave
    the agent. With no attacker, the benchmark measures no danger at all. The worried reader will hear "the
    smarter model is the more dangerous one" with nothing attached.
  This is the line the brief marks as most at risk of telling the reader they're right "beyond what the
  evidence shows", and as written it does.
- **Fix.** *"That is the worry, partly borne out: in this benchmark, the more capable models tended to be the
  more dangerous ones once hijacked. As far as the authors can tell, that's because they were better at
  following someone else's orders, not because they had plans of their own."* It runs about ten words
  longer, and it keeps every qualifier the source gives. If Bart wants to keep "half right", keep it, but
  carry "in this benchmark", "tended to" and "once hijacked" with it.

### 2. (Impact 6) Zou 2025 reads as more support for the worry, and it points the other way

> "…not because it had plans of its own. A large public competition, in which people made 1.8 million
> attempts to hijack 22 agents, found that bigger or more capable models … were not much harder to hijack"

- **What's wrong.** Under the new frame, the section's opener promises evidence that "gives the worry part of
  what it fears", and Zou follows straight on from "the worry, half right". So the reader takes it as a
  second study showing smarter = more dangerous. It doesn't. "Limited correlation between agent robustness
  and model size, capability, or inference-time compute" says capability made **little difference either
  way**. That supports "smarter isn't safer" (the hope fails). It does **not** support "smarter is more
  dangerous" (the worry). Brief 13 says the two studies "disagree in direction" and calls the question
  "Unsettled". They agree on one thing only: being smarter didn't protect. Before the reframe the paragraph
  argued only that one thing, so the two studies sat together without trouble. The reframe asks AgentDojo to
  carry a direction, and then puts beside it, without comment, a study that doesn't show that direction.
  "What would change my mind" already has the honest summary ("the findings point the other way or show
  little link"). The body doesn't.
- **Fix.** Bridge the two studies and say what each shows. After finding 1's sentence: *"A second, much larger
  test didn't find that direction, only that being smarter made little difference. A large public
  competition … found that bigger or more capable models … were not much harder to hijack…"* (then as now).
  Close the paragraph with what both agree on: *"So the two studies disagree on whether smarter is worse. They
  agree that smarter didn't protect."* The section opener's "gives the worry part of what it fears" then
  rests on one study, which is what it has.

### 3. (Impact 6) Lynch 2025 is read as evidence about *smarter*, but the study didn't compare capability

> "This is the closest the evidence comes to the worry in its usual form, a capable AI choosing harm to serve
> its own ends, and it took tests built to force it."
>
> (and in "What this doesn't claim") "in stress tests built to force it, capable models chose harm."

- **What's wrong.** The forced design is framed honestly (see above). The problem is the inference the frame
  puts on it. The reader's worry is a *gradient*: the smarter it gets, the more dangerous. Lynch tested 16
  *leading* models. As brief 5.7 records it, the study didn't set more capable models against less capable
  ones, so it can't show that being smarter raises the rate. What it shows is that today's leading models,
  cornered, chose harm at high rates. The old text carried the link as an inference ("Working out a move like
  that takes some sophistication"), which matches brief 5.7's bearing, marked **[ours]**. The reframe cut
  that sentence and now presents the study as the evidence nearest to "smarter = more dangerous". Two smaller
  points:
  - "Its own ends" is a little wider than the brief's "to avoid replacement *or achieve their goals*". Some
    of those goals were the ones the scenario gave the model.
  - "The closest the evidence comes" generalises over evidence the essay didn't survey. Brief 5.7 has a
    comparable contrived study (Meinke 2024) that the essay doesn't cite.
- **Fix.** Keep the move, but name the inference: *"This is the closest the evidence I found comes to the
  worry in its usual form: a capable AI choosing harm when it was cornered. The study didn't compare smarter
  models with less capable ones, but working out a move like that takes some sophistication, and it took
  tests built to force it."* In "What this doesn't claim", "capable models chose harm" can stand, since it
  says no more than the study does. Don't let it read as the gradient.

### 4. (Impact 5) "A less capable one isn't the answer" is asserted, though the evidence for it is already on the page

> (position) "A less capable one isn't the answer either: it does less of the job you wanted, and what it can
> touch still sets the worst case."
>
> (section close) "Neither 'use a smarter model' nor 'use a less capable one' is a substitute for narrower
> access."

- **What's wrong.** Once the body grants that "the smarter model was the more dangerous one", the reader's
  next thought is "so use a weaker one". In AgentDojo, the weaker models *were* harder to attack. The body
  never answers this with evidence. It goes straight to the closing line. Both studies already on the page
  answer it. In AgentDojo, the weaker models were harder to attack mostly because they failed at the work as
  well. Brief 5.4 records that even with no attacker, current models solve "less than 66%" of the tasks, and
  6.1 says low-utility models "often fail at correctly executing the attacker's goal". In Zou, size and
  capability made little difference. As written, "isn't the answer either" is the essay's word against an
  inference its own evidence invites.
- **Fix.** One sentence in the body, before the closing line: *"Nor does that make a weaker model the safer
  pick. In the same benchmark, the weaker models resisted attacks mostly by failing at the work too, and in
  the larger competition, being smaller made little difference."* No new source. It uses 5.4, 6.1 and 6.2
  only.

### 5. (Impact 5) The position states the danger flatly and ranks its causes

> "So a smarter agent is more dangerous mainly because it does more with the access it has, and being smarter
> doesn't make it any harder to fool."

- **What's wrong.** Two steps go past the evidence:
  - **"Is more dangerous" is unconditional.** The body's support is one benchmark's trend under attack
    (finding 1), one study that found little link (finding 2), and forced scenarios that compared no
    capability levels (finding 3).
  - **"Mainly" ranks the mechanisms.** It says doing more with access outweighs any other route. No study in
    brief 13 measures the relative size of the routes. Brief 6.5's synthesis ("capability scales what happens
    inside the bound") is marked **[ours]**, and it doesn't rank.
  The position is the paragraph most readers carry away, so it should be the most carefully hedged, not the
  least.
- **Fix.** *"So where a smarter agent is more dangerous, it's because it does more with the access it has,
  and being smarter doesn't reliably make it harder to fool."* "Where … is" grants the worry without
  overstating it. "Doesn't reliably" is finding 6.

### 6. (Impact 3) "Any harder to fool" is absolute, and Zou found "limited" correlation, not none

> "being smarter doesn't make it any harder to fool"

- **What's wrong.** "Limited correlation" allows a small link. Brief 6.5 states the bottom line as
  "Capability does not *reliably* buy safety". "Any" is the round 1 "no link" problem (my F12) coming back in
  the position paragraph.
- **Fix.** "doesn't reliably make it harder to fool" (already in finding 5's fix).

### 7. (Impact 3) The new falsifier doesn't say how much evidence would count

> "If capable agents were found choosing serious harm in real use, on their own initiative, with only the
> access their job needed, then capability would be the dial to watch first"

- **What's wrong.** It's a good falsifier, and it's well-defined on *what*: real use, own initiative, minimal
  access. It isn't defined on *how much*. Elsewhere the essay is careful to separate "single reported cases"
  from rates, and one such case wouldn't make capability "the dial to watch first". The bullet just above it
  asks for "field studies".
- **Fix.** *"If capable agents were found, at a measurable rate rather than in single cases, choosing serious
  harm in real use…"*

### 8. (Impact 2) The section opener's "the evidence so far" is wider than one benchmark

> "The evidence so far, from test benchmarks, doesn't support the hope, and it gives the worry part of what it
> fears, by a different route."

- **What's wrong.** Two of the benchmarks support "doesn't support the hope". Only AgentDojo supports "gives
  the worry part" (finding 2). It's scoped to test benchmarks, which helps. It still presents a one-study
  direction as the evidence's.
- **Fix.** *"…doesn't support the hope, and one benchmark gives the worry part of what it fears, by a
  different route."* If finding 2's bridge goes in, this becomes optional.

---

## Verdict

**Ready after fixes.** The numbers are all sound. Findings 1 to 3 make each study carry only what its design
shows, and none of the fixes adds a source or cuts a point.
