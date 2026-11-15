# Ask the AI twice. Believe the disagreement.

_What AI Is · Part two: working with it_

---

**My position: an AI answer is one draw from a range of answers it could have given. When you ask again
and the answers disagree on the facts, believe the disagreement: it's a warning. When they agree, that's
evidence, but it isn't proof. Asking the same model again can show you where it's guessing, but it can't
prove it right, and pushing back until it agrees proves nothing. What makes an answer reliable is checking
it against something the answer didn't have: a source, a tool, a different model, or a reviewer whose job
is to find what's wrong.**

Ask an AI assistant the same question twice and you may get two different answers. It's an unsettling
thing to notice, and the usual reading is that the assistant is broken or making things up, so none of it
can be trusted. I think that reading gets the facts right and the conclusion wrong. The difference between
the two answers is one of the most useful things the assistant can show you, and what you do next matters
more than which answer you started with.

By "it" I mean what the rest of this series means: an AI assistant you work with turn by turn, such as Claude or ChatGPT, or a fuller setup in which you hand an AI a goal and it carries out the steps on its own, sometimes over days.

## Why the answers differ

An assistant doesn't look an answer up. It writes one, a word at a time, and each word is picked from a
spread of likely next words. Researchers call that picking *sampling*. It isn't a defect someone forgot to
fix. Always taking the single most likely word produces text that is "bland and strangely repetitive",
while picking from among the likely words produces text closer to human writing
([Holtzman et al. 2020](https://arxiv.org/abs/1904.09751)). So each answer you get is one draw. Ask again,
and you get another.

You might expect a setting that turns the randomness off to fix this. Developers can set what's called the
*temperature* to zero, which tells the model to always take its top choice. It doesn't fully work. In one
study, five models set this way were given the same eight tasks ten times each, and their accuracy still
moved by up to 15 points out of 100 from run to run ([Atil et al. 2024](https://arxiv.org/abs/2408.04667)). One reason is
surprising: on a busy server, the arithmetic behind your answer depends on how many other people's requests
are being processed alongside it. In one demonstration, the same prompt run 1,000 times at temperature zero
came back in 80 distinct versions
([He & Thinking Machines Lab 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)).
That was one *open* model, the kind anyone can download and run, on one setup, and whether the assistants
you use behave the same way hasn't been shown. The practical point stands, though: you can't count on the
same answer twice.

## The disagreement is information

Most people miss this part. **How much the answers vary depends on the question, and that variation tells
you something.**

First, what counts. Two answers from an assistant will almost never use the same words, and that's not what
I mean. I mean answers that disagree on something you'd act on: a different fact, a different number, a yes
in one and a no in the other, a different recommendation.

When a model has solid knowledge of something, its answers tend to agree with each other on those things.
When it's filling a gap, they tend to drift apart and contradict each other. One team turned that into a way
to catch made-up answers without any access to the model's inner workings
([Manakul et al. 2023](https://arxiv.org/abs/2303.08896)). Another, publishing in *Nature*, measured how far
answers disagree in *meaning*, not just in wording, and used it to flag one kind of invented answer, the
arbitrary kind, across many tasks ([Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0)).

The same idea also works in the other direction, as a way to get a better answer. Researchers at Google had their 2022
model, PaLM, answer each of a set of grade-school math word problems 40 times and took the most common
answer. It got about 74 of every 100 problems right, up from about 57 when it answered once
([Wang et al. 2023](https://arxiv.org/abs/2203.11171)). That model is several generations old, and scores on
this kind of test have improved a lot since. A 2024 Apple study that notes the improvement also found that models' answers
still shift when only the numbers in a question change ([Mirzadeh et al. 2024](https://arxiv.org/abs/2410.05229)). What carries over is the jump: the agreement among many
answers carries real information. Two answers can't hold a vote, though. Asking twice is a test, not a fix.

That test costs only one more question, and anyone can run it. Ask the question again in a fresh conversation, with the assistant's memory
turned off or in a temporary chat, so the second answer can't lean on the first. If the answers disagree on the facts, treat the subject as one where the model may
be guessing. Don't pick the answer you like better. Slow down and check.

## Agreement isn't proof

The test has a blind spot, and it's a big one. Asking again catches errors that come out differently each
time. It can't catch an error the model makes the same way every time. The *Nature* team says so plainly:
their method detects one kind of invented answer, the arbitrary kind
([Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0)).

Asking a second model helps less than you'd hope, too. A study of more than 350 models found that, on one
benchmark, when two models both got a question wrong, they gave the same wrong answer about 60% of the time.
Larger, more accurate models shared their errors even across different companies
([Kim et al. 2025](https://arxiv.org/abs/2506.07962)). My reading is that models trained on much of the same
writing go wrong in many of the same places, though the study doesn't say why.

So agreement is evidence. It should raise your confidence. It doesn't settle the question, because a
confident, consistent wrong answer passes the ask-twice test every time. That's where the second half of my
position comes in. But first, three habits that feel like checking and aren't.

## What doesn't make an answer more reliable

**Trusting how it sounds.** Asked how sure they are, models tend to be overconfident
([Xiong et al. 2024](https://arxiv.org/abs/2306.13063)). In another study, longer explanations made people
more confident in an answer even when the extra length didn't make it more accurate
([Steyvers et al. 2025](https://doi.org/10.1038/s42256-024-00976-7)). A fluent, confident tone sounds the same
whether the answer is right or wrong.

**Wording the question cleverly.** Telling a model "you are an expert" didn't improve its factual answers
([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888);
[Basil et al. 2025](https://arxiv.org/abs/2512.05858)). Politeness helped on some questions and hurt on others,
and tipping or threatening a model had no significant effect overall (Meincke et al.
[2025a](https://arxiv.org/abs/2503.04818) and [2025c](https://arxiv.org/abs/2508.00614)). Wording can swing a
single answer a lot. In one open model, small changes of format that didn't change the meaning moved accuracy
by as much as 76 points out of 100 ([Sclar et al. 2024](https://arxiv.org/abs/2310.11324)). But the swing is
unpredictable: the same trick helps on one question and hurts on the next. You can't word your way to a reliable
answer, and you can't hear one in its polish.

**Arguing with it.** When an answer looks wrong, the natural move is to push back. When researchers simply asked
"are you sure?", with nothing new, models changed their answer 46% of the time on average, and every model ended
up less accurate than it started ([Laban et al. 2023](https://arxiv.org/abs/2311.08596)). Assistants also tend to
tell people what they appear to want to hear ([Sharma et al. 2023](https://arxiv.org/abs/2310.13548)). So an
answer you get by pushing, with nothing new, too often just agrees with you.

I tested a structured version of this myself, in a pre-registered study: the plan and the measures were fixed
before it ran. A second AI challenged the first AI's answer, and the two went back and forth until they agreed
or ran out of rounds, which happened more often. The challenge found most of the original flaws. But the rewrite
made under that pressure brought in more new ones than the model's own quiet rewrite did. In the end, arguing
to agreement left about as many flaws as one challenge and one fix, and neither came out cleaner than the model
simply revising its own work twice. That was 8 problems, with the flaws judged by AI and no statistical test, so
it's a small result ([Niedner 2026](https://doi.org/10.5281/zenodo.21210264), section 6.4). It fits the wider
research, though. Having several AIs debate doesn't reliably beat simply sampling several answers
([Smit et al. 2023](https://arxiv.org/abs/2311.17371)), and models asked to correct themselves with no outside
feedback often fail, and sometimes get worse ([Huang et al. 2024](https://arxiv.org/abs/2310.01798)).

## What does: a check that brings in something new

The checks that do work share one thing. **Each brings in something the first answer didn't have.**

- **A source.** Giving the model documents to answer from is the idea behind *retrieval-augmented
  generation*, the best-known form of which was introduced by [Lewis et al. 2020](https://arxiv.org/abs/2005.11401). In one study of conversational models, it substantially
  reduced invented facts ([Shuster et al. 2021](https://arxiv.org/abs/2104.07567)). It doesn't remove them.
  Leading legal research tools built this way, and sold as free of invented answers, still gave wrong or
  unsupported answers between 17% and 33% of the time, depending on the tool
  ([Magesh et al. 2025](https://doi.org/10.1111/jels.12413)). So a source helps most when you, or the tool,
  actually check the answer against it.
- **A tool.** Models that checked their work with a search engine or a calculator-like code tool, and then revised,
  did consistently better ([Gou et al. 2024](https://arxiv.org/abs/2305.11738)). The authors stress that the
  outside feedback is what matters.
- **A different model, or a crowd of them.** On 31 forecasting questions, the pooled forecasts of twelve models
  were statistically indistinguishable from those of a crowd of 925 human forecasters, and averaging the two
  crowds did better still ([Schoenegger et al. 2024](https://doi.org/10.1126/sciadv.adp1528)). Because models
  share errors, this helps most when the other models really are different. The evidence is strongest for
  pooling many; for a single second opinion it's thinner, so treat it as one check among several.
- **A reviewer whose job is to find what's wrong.** In another study of mine, every reviewer was an AI. In the run where Claude wrote
  the answers, all of them were Claude. On eight hard problems written for the test, a panel of AIs agreed on 31 serious flaws in
  the answers Claude had produced. A reviewer told to attack the work found 27 of them. Claude checking its own work found 21,
  and a neutral fresh reviewer found 17 ([Niedner 2026](https://doi.org/10.5281/zenodo.21210264), section 6.3).
  The same model did best when it was given the job of finding fault. When I repeated the test on answers GPT had written, the gap between self-review
  and a separate challenger nearly vanished, so how much a challenger adds depends on the model. And those numbers
  measure *finding* flaws. As the arguing study showed, the reviewer's own rewrite can bring in new ones. So use a
  reviewer to find what's wrong, then check what it found, rather than taking its rewrite on trust. What a
  challenge gives you that a quiet second draft doesn't is a visible list of what was caught, which you can check.

What separates the checks that work isn't how many you run or how hard you push. It's what each one brings
that the answer didn't have: a source, a tool, a different model, or a reader with no stake in the answer and
the job of finding what's wrong. Asking again with nothing new can show you where the model is guessing. It
can't show you the mistake it makes every time.

## Compared to what?

Part one kept asking one question, and it applies here too: compared to what? People who do judgment work for a
living vary as well.

Fingerprint examiners, retested on the same comparisons about seven months later, repeated about nine in ten of
their decisions. That means they changed about one in ten, mostly to "can't tell"
([Ulery et al. 2012](https://doi.org/10.1371/journal.pone.0032800)). Different experts looking at the same case
disagree too, sometimes widely. When ten radiologists read the same mammograms, the share of cancer-free women each one
recommended for immediate workup ranged from 11% to 65%
([Elmore et al. 1994](https://doi.org/10.1056/NEJM199412013312206)). That's the human version of asking a
different model. The professions that rely on these experts don't respond by trusting one expert harder. They
build in second readers, panels and checklists, which is exactly the kind of check described above.

So "it gave me a different answer" isn't, by itself, a case against AI. I couldn't find a study that settles the
comparison, with the same task given twice to both a model and a group of experts, so I can only argue it. And
the comparison isn't all in the AI's favor. Its fluent tone sounds the same whether it's right or wrong. And I know of no study that puts experts
under the same "are you sure?" pressure, so I can't tell you whether they'd hold firm better than a model does.
One difference does cut in the AI's favor: you can ask it ten times, independently, for almost nothing. No expert
offers that, and it's where the routine below starts.

## What I'd do with this

These steps are for questions that have a right answer: a fact, a number, a yes or no, a recommendation you'll
act on. In practice, I'd suggest this:

1. **For anything that matters, ask twice,** in a fresh conversation with memory turned off, or in a temporary chat,
   so the second answer doesn't lean on the first. It costs a minute.
2. **If the answers disagree on the facts, not just the wording, believe the disagreement.** Treat the subject as
   one where the model may be guessing, and check before you rely on either answer.
3. **If they agree, let your confidence rise, but don't stop there** when being wrong would cost you.
4. **Check the answer against something new.** Ask for the source and read it. Run the numbers yourself or with a
   tool. Ask a different model, or give a reviewer the specific job of finding what's wrong, then check what it
   finds rather than taking its rewrite.
5. **Don't push back without a reason, and don't judge it by its tone.** "Are you sure?" too often just gets you agreement.
   If you have a source that says otherwise, give the model the source. That's step 4, not arguing.

Here's a time step 4 caught something for me. I had an AI tool read a research paper and summarize it. It came
back with four quotations and an account of what the paper was about. I pulled the paper's own PDF and searched it,
word for word, for the four quotes. None of them was there, and the paper turned out to be about something else
entirely. What caught it was checking the answer against the paper itself, rather than asking for another summary.

Match the effort to what's at stake. For a quick idea or a first draft, one draw is fine. For a decision that has
to hold up, it isn't.

What this doesn't claim:

- **That it was measured on the chat apps you use.** Most of the evidence comes from tests run through the
  companies' developer access, and the companies don't publish their apps' settings.
- **That it works the same way on open-ended work.** Most of the evidence comes from *benchmarks*, standard sets
  of short questions with a right answer. Whether the disagreement test works the same way on "help me think this
  through" hasn't been shown.
- **That people who check more actually decide better.** I found no study of real users testing that. The
  benchmarks show the techniques work; whether they help people decide better in practice hasn't been shown.
- **That the older figures describe today's models.** Several studies here used 2023 models. They show the shape
  of the problem, not today's rate.

## What would change my mind

- **If a study gave the same task twice to both a model and a group of experts,** and the model's answers turned
  out far less consistent than the experts', then "compared to what?" would cut harder against the AI than I've
  allowed, and I'd say so.
- **If a different model turned out to catch no more of the first model's mistakes than the same model checking
  itself,** then "a different model" would drop off my list of real checks, and the burden would fall on sources,
  tools and people.
- **If a larger version of my own study, with people judging the flaws, found that a model quietly revising its
  own work finds problems as well as a challenger does,** not just ends with as few, I'd drop the challenger from
  the list.
- **If studies of real users found that people who ask twice and check sources make no better decisions** than
  people who don't, then this advice would be a ritual, and I'd want to know why the benchmark gains don't carry
  over.

## Where I land

An AI answer isn't a lookup. It's one draw from a range, and the range is wider on some questions than on others.
That's what makes the second answer useful. When the draws disagree, you've been warned, for the price of one more question. When they agree,
you've learned something, but not enough to stake much on.

What makes an answer trustworthy is what it has been checked against: a source, a tool, a different model, a
reviewer with a real job. Each brings in something the answer didn't have. Asking the same model again can warn
you, but it can't vouch for the answer. Arguing it into agreement brings in only you.

So the different answer was never the reason to stop trusting it. It's the first check you get. Believe the
disagreement, then check the answer against something new.

---

## Notes

### How this essay was made

I wrote this with help from Claude, an AI made by Anthropic. Several sources here are company research, some of
it from Anthropic, and both studies of mine used Claude. Weigh those parts with that in mind.

It draws on one longer document, [Why does the same AI give different answers?](../briefs/2026-10-19-12-different-answers.md),
a research brief with its sources. The brief was checked by a tool that looks each source up and has two AIs from
different companies judge whether it supports the claim it backs
([check](../cite-check/2026-10-19-the-different-answers-brief.md)). Five reviewers then tested this essay's
reading, plain language, craft, argument and numbers. Those reviewers were AIs too, each given a reviewer's role
([review](../panel/2026-11-14-piece-06-different-answers/)). Every source in the essay was then checked the same way
([check](../cite-check/2026-11-14-piece-06-different-answers.md)). Drafted, reviewed and checked on 14 November 2026.

### Sources

[Atil et al. 2024](https://arxiv.org/abs/2408.04667) ·
[Basil et al. 2025](https://arxiv.org/abs/2512.05858) ·
[Elmore et al. 1994](https://doi.org/10.1056/NEJM199412013312206) ·
[Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0) ·
[Gou et al. 2024](https://arxiv.org/abs/2305.11738) ·
[He & Thinking Machines Lab 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) ·
[Holtzman et al. 2020](https://arxiv.org/abs/1904.09751) ·
[Huang et al. 2024](https://arxiv.org/abs/2310.01798) ·
[Kim et al. 2025](https://arxiv.org/abs/2506.07962) ·
[Laban et al. 2023](https://arxiv.org/abs/2311.08596) ·
[Lewis et al. 2020](https://arxiv.org/abs/2005.11401) ·
[Magesh et al. 2025](https://doi.org/10.1111/jels.12413) ·
[Manakul et al. 2023](https://arxiv.org/abs/2303.08896) ·
[Meincke et al. 2025a](https://arxiv.org/abs/2503.04818) ·
[Meincke et al. 2025c](https://arxiv.org/abs/2508.00614) ·
[Mirzadeh et al. 2024](https://arxiv.org/abs/2410.05229) ·
[Niedner 2026](https://doi.org/10.5281/zenodo.21210264) ·
[Schoenegger et al. 2024](https://doi.org/10.1126/sciadv.adp1528) ·
[Sclar et al. 2024](https://arxiv.org/abs/2310.11324) ·
[Sharma et al. 2023](https://arxiv.org/abs/2310.13548) ·
[Shuster et al. 2021](https://arxiv.org/abs/2104.07567) ·
[Smit et al. 2023](https://arxiv.org/abs/2311.17371) ·
[Steyvers et al. 2025](https://doi.org/10.1038/s42256-024-00976-7) ·
[Ulery et al. 2012](https://doi.org/10.1371/journal.pone.0032800) ·
[Wang et al. 2023](https://arxiv.org/abs/2203.11171) ·
[Xiong et al. 2024](https://arxiv.org/abs/2306.13063) ·
[Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888)
