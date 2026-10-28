# Rosetta: voice-and-flow review of the Hinton passage in essay 03

_Reviewer 2 of the panel, run independently. 2026-10-28._
_Passage: from "Others put it far higher." to "So on this question, I weigh Chalmers more." in
`docs/research/what-ai-is/positions/03-someone-there.md`._
_Read: the whole essay, cold, start to finish; the Hinton brief
(`docs/research/what-ai-is/briefs/2026-10-28-16-hinton-on-ai-consciousness.md`); Bart's voice notes (private, not in this record);
the narration script builder (`docs/research/newsletter-what-ai-is/narration/build-scripts.py`).
I ran the builder's own `speakable()` function on the passage to hear exactly what the narrator
will say. I did not read the other panelists' reviews._

## Verdict

The passage belongs where it is, and its way in works. "Others put it far higher" mirrors Seth's
"lower still" right before it, so the reader moves from one end of the range to the other without
a bump. Three things stop it from reading as if it had always been there. **The way out breaks:**
the next paragraph's "anyway" now points at the wrong sentence. **It reads worse aloud than on the
page:** the narrator speaks two citations mid-sentence, and Hinton's "not working 'properly'"
loses its scare quotes and, without his example, sounds like nonsense. **The first paragraph is in
the wrong order:** the quote arrives before we know who he is, his credentials then come between
the quote and his reason for it, and the paragraph runs to nine sentences. All three can be fixed
without dropping anything. The fix splits the passage into three paragraphs and adds one sentence:
Hinton's own example.

The hook lands. Details in finding 7.

## Findings, ranked by impact

### 1. The next paragraph's "anyway" now points at Hinton, not at Chalmers's estimate. Impact 9

**Text (opening of the paragraph after the passage):**
> Chalmers draws a practical lesson anyway.

Before the insertion, "anyway" followed Chalmers's own judgment that today's models are probably
not conscious: *he thinks they probably aren't, and draws a lesson anyway.* Now it follows "So on
this question, I weigh Chalmers more," and a listener hears *I weigh Chalmers more, and Chalmers
draws a lesson anyway*, which makes no sense. Of everything in the passage, this is what most shows
that something was inserted. One edit to the next paragraph's first sentence fixes it, and nothing
else in that paragraph has to change.

**Replace with:**
> Low as his own estimate is, Chalmers still draws a practical lesson.

### 2. The narrator reads two citations aloud, mid-sentence. Impact 8

`build-scripts.py` drops a parenthesis only when it holds a single link and nothing else. Two in
this passage don't qualify, so the narrator reads them out. This is the builder's output for the
passage, verbatim:

> "AI has just as much subjective experience as we do," he said in October 2026 **(Futurism 2026,
> reporting a Telegraph interview)**. … He shared the 2018 Turing Award and the 2024 Nobel Prize in
> Physics for it **(The Verge 2019; Nobel Prize 2024)**, and in 2023 …

On the page these are clutter. Aloud, they are worse: the narrator stops in the middle of
Hinton's first quote to say "Futurism 2026, reporting a Telegraph interview". The other four
citations in the passage are dropped, as they should be.

**Fix:** put the Telegraph in the sentence and keep Futurism as a single-link citation. The Notes
already explain why Futurism is the source, and the source list labels it secondary, so the
written version loses no honesty. Give each award its own single-link parenthesis.

> In October 2026 he told The Telegraph, "AI has just as much subjective experience as we do"
> (Futurism 2026).
>
> That work earned him a share of the 2018 Turing Award (The Verge 2019) and of the 2024 Nobel
> Prize in Physics (Nobel Prize 2024) …

(The existing "from a talk transcript" citation in the next paragraph, Chalmers 2026, is also read
aloud. It predates this passage and is outside my brief, but the same fix applies if Bart wants
it.)

### 3. Quote marks around words Hinton didn't say. Impact 7

**Text:**
> Hinton's "already, as much as we do" does not.

This is our summary of his view, not something he said. In print, quote marks tell the reader
these are his exact words. The brief has "already, as much as we do" as our interpretation, marked
**[ours]**. A passage this careful about secondary sourcing shouldn't put a paraphrase in quote
marks. Aloud the marks vanish, so this one matters on the page.

**Replace with:**
> Hinton's view, that AI's experience is here already and as full as ours, does not.

### 4. The first paragraph is in the wrong order and runs too long. Impact 7

The order now is hook, name, quote, then "Hinton is the computer scientist…", two credential
sentences, and then "His case rests on…". The quote and its reason are split by the résumé, and
"Hinton is" restarts a subject the listener was just given. At nine sentences and about 190 words,
it is the longest paragraph in the section. That is where a listener loses track.

**Fix:** give his credentials in the same sentence as his name, then the quote, and start a new
paragraph for his reason. The reason then comes straight after the claim it explains, and each
paragraph does one job: who he is and what he says, why he says it, where that leaves him.

### 5. Without his example, "not working 'properly'" sounds absurd aloud. Impact 6

**Text:**
> subjective experience "is just a way of talking about what your perceptual system's telling you
> when it's not working 'properly'"

The narrator can't speak the scare quotes. Without them, and without the case he was describing,
a listener hears *experience is what your senses report when they break*. That makes a Nobel
laureate sound foolish one sentence before we call his view disputed. Hinton gives an example in
the same Globe and Mail interview, and the brief checked it against the page **[text]**: a chatbot
with a camera, fooled by a prism, says the prism gave it "the subjective experience" that an
object was off to one side. One sentence of it makes his argument make sense, and that is the
generous way to present him.

**Add, after the quote:**
> His example is a chatbot with a camera that a prism has fooled: it says the prism gave it "the
> subjective experience" that an object was off to one side (Globe and Mail 2024).

_Accuracy gate:_ this sentence is new to the essay, though it comes from the same source as the
quote. It needs a `/cite-check` pass before the essay ships.

### 6. The verdict on Hinton's view is stricter than the one on Chalmers's, and the weighing rests on credentials alone. Impact 5

**Text:**
> That view of experience is disputed, and it is an argument, not a finding.
> …
> But whether anyone is experiencing anything is a question about consciousness, and that is
> Chalmers's field, not Hinton's. So on this question, I weigh Chalmers more.

Each sentence is accurate. Read together, they hold Hinton to a standard the essay doesn't apply
to Chalmers. Chalmers's fading-neurons argument is also an argument, not a finding, and the essay
already says his estimates are "a judgment, his and mine, not a measurement". Saying so here costs
nothing and keeps the passage generous: the claim stays at full strength, and the reader sees that
the essay applies the same standard to both men. The close then weighs on field alone, which reads
as "trust the right credential". The passage has already given the better reason: Hinton's answer
depends on that disputed view of experience. Name it, and the weighing rests on the argument as
well as the field.

**Replace with:**
> Like Chalmers's view, Hinton's is an argument rather than a finding, and it is disputed.
> …
> But whether anyone is experiencing anything is a question about consciousness, which is
> Chalmers's field rather than Hinton's, and Hinton's answer rests on that disputed view of what
> experience is. So on this question, I weigh Chalmers more.

The landing line stays as it was. It is the right ending.

### 7. The hook lands, but its verb tense slips. Impact 4

**Text:**
> If you have seen a clip of "the godfather of AI" saying AI is already conscious, that is probably
> Geoffrey Hinton.

It is a hook, not a stumble. The essay already speaks to the reader as "you" ("when you talk with
an AI assistant", "Imagine your neurons"). A clip is concrete and recent, and the sentence admits
the reason the passage exists without making a fuss of it. Aloud, the narrator says "the godfather
of AI" without the quote marks, which is fine: it is his common nickname, and the passage then
gives his real credentials. Two small problems. "have seen … that **is**" changes tense in the
middle; it should be "was". And "probably" sounds as if we are guessing at who it is. "Most
likely" carries the same honest doubt, since other people get called godfathers of AI too, and
reads less like a shrug.

**Replace with:**
> If you have seen a clip of "the godfather of AI" saying AI is already conscious, it was most
> likely Geoffrey Hinton, the computer scientist whose work on neural networks underlies today's
> AI.

### 8. Two numbers run together aloud, and "by 2024" sounds wrong for a 2024 survey. Impact 3

**Text:**
> In 2024, 582 researchers … would exist by 2024, 2034 and 2100.

The narrator will say "twenty twenty-four, five hundred eighty-two" with only a comma between
them. Asking someone in 2024 whether something will exist "by 2024" sounds like an error. The
brief notes that the paper calls 2024 "today".

**Replace with:**
> In 2024, a survey asked 582 researchers who publish at leading AI venues how likely it was that
> an AI system with subjective experience exists today, and that one will by 2034 and by 2100.

### 9. "For it" and "field" both point the wrong way. Impact 3

- "He shared the 2018 Turing Award and the 2024 Nobel Prize in Physics **for it**": the nearest
  noun is "today's AI", not his work. Fixed by "That work earned him…" in finding 2.
- "It also sits far from most of his **own field**" and, three sentences later, "Chalmers's
  **field**, not Hinton's" use the same word for two different things: AI research, and the study
  of consciousness. Heard close together, the second seems to contradict the first. **Replace**
  the first with "most of his own colleagues".

### 10. Smuggled virtue and other AI tells: none found. Impact 1, for the record

No sentence names a dishonest alternative in order to disclaim it. "It is an argument, not a
finding" is a real distinction the reader needs, not a pose. "So he could speak freely about AI's
dangers" is a fact from the Guardian source that shows him speaking against his own interest, and
it is generous. Keep it. No hedge filler, no announced candor, and no punchy fragments. Apart
from finding 4, the passage moves in medium-length sentences, which suits where the series has
gone.

## Full proposed revised passage

Three paragraphs instead of two. Every fact and source in the current version is kept, and one
sentence is added (Hinton's prism example, finding 5, which needs a cite-check). URLs are the same
as in the current file.

> Others put it far higher. If you have seen a clip of "the godfather of AI" saying AI is already
> conscious, it was most likely Geoffrey Hinton, the computer scientist whose work on neural
> networks underlies today's AI. That work earned him a share of the 2018 Turing Award
> ([The Verge 2019](https://www.theverge.com/2019/3/27/18280665/ai-godfathers-turing-award-2018-yoshua-bengio-geoffrey-hinton-yann-lecun))
> and of the 2024 Nobel Prize in Physics
> ([Nobel Prize 2024](https://www.nobelprize.org/prizes/physics/2024/press-release/)), and in 2023
> he left Google so he could speak freely about AI's dangers
> ([The Guardian 2023](https://www.theguardian.com/technology/2023/may/02/geoffrey-hinton-godfather-of-ai-quits-google-warns-dangers-of-machine-learning)).
> In October 2026 he told The Telegraph, "AI has just as much subjective experience as we do"
> ([Futurism 2026](https://futurism.com/artificial-intelligence/nobel-scientist-geoffrey-hinton-ai-conscious-toast)).
>
> His case rests on a view of what experience is. The idea that we have an "inner theatre" setting
> us apart from machines is, he says, "just rubbish": subjective experience "is just a way of
> talking about what your perceptual system's telling you when it's not working 'properly'". His
> example is a chatbot with a camera that a prism has fooled: it says the prism gave it "the
> subjective experience" that an object was off to one side
> ([Globe and Mail 2024](https://www.theglobeandmail.com/business/article-geoffrey-hinton-artificial-intelligence-machines-feelings)).
> Like Chalmers's view, Hinton's is an argument rather than a finding, and it is disputed.
>
> It also sits far from most of his own colleagues. In 2024, a survey asked 582 researchers who
> publish at leading AI venues how likely it was that an AI system with subjective experience
> exists today, and that one will by 2034 and by 2100. Their median answers were 1%, 25% and 70%
> ([Dreksler et al. 2025](https://arxiv.org/abs/2506.11945)). Chalmers's figures sit near those;
> Hinton's view, that AI's experience is here already and as full as ours, does not. On how these
> systems learn, Hinton's word carries great weight. But whether anyone is experiencing anything
> is a question about consciousness, which is Chalmers's field rather than Hinton's, and Hinton's
> answer rests on that disputed view of what experience is. So on this question, I weigh Chalmers
> more.
>
> Low as his own estimate is, Chalmers still draws a practical lesson. He treats today's models as
> tools, but says … _(rest of the paragraph unchanged)_

**What the narrator will say** (the builder applied to the revision, with citations dropped as
they should be): "…it was most likely Geoffrey Hinton, the computer scientist whose work on neural
networks underlies today's AI. That work earned him a share of the 2018 Turing Award and of the
2024 Nobel Prize in Physics, and in 2023 he left Google so he could speak freely about AI's
dangers. In October 2026 he told The Telegraph, "AI has just as much subjective experience as we
do."" No citation is spoken.

**Knock-on:** the Notes say "His Telegraph interview is quoted as Futurism reported it". That
still holds, and it now matters more, because the text names The Telegraph directly. Keep it.
