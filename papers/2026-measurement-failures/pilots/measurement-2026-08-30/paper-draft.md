<!-- ============================================================================
     📄 PAPER 2 (THE MEASUREMENT PAPER) — OPEN DRAFT. Not published, not locked.
     ============================================================================

     Status  : first full draft 2026-08-30; round-1 panel (Ada, Vera Tukey, Miriam,
               Minard) assembled 2026-09-16 — see panel-assembly-2026-09-16.md;
               round-2 re-review (Rosetta, Vera Tukey, Ines Otlet) assembled the
               same day; round-3 narrow re-review by the same panel assembled the
               same day.
               Nothing here is pre-registered; this is a case series, not a
               hypothesis test (see §3).
     Spine   : docs/findings/instrument-failure-catalogue.md
     Evidence: pilots/coverage-residual-validation-2026-08-29/
               pilots/seeded-miss-2026-08-29/

     SEQUENCING: this paper publishes FIRST, and its DOI must be verified
     resolving, before the Proposer paper (Paper 3) — whose coverage secondary
     is validated by citing it. See ./README.md.

     STRUCTURAL TEST, applied at every revision: a reader who skips both case
     studies must still get the paper's claim. If §6 and §7 start carrying the
     argument instead of illustrating it, the spine has slipped.
============================================================================ -->

# Twenty-four results that didn't mean what their labels said: measurement failures from a project testing whether AI systems can be trusted to report on their own reliability

**Barton Niedner**
Resource Forge LLC · bart.niedner@resourceforge.com

**Status: open draft, 2026-08-30; round-1, round-2 and round-3 reviews assembled 2026-09-16.** This is a
**case series**, not a pre-registered study — its analysis choices were not fixed in writing before
the data was seen (§3.2). Its entries are drawn from one project, one team, and a non-random sample
of the failures that were *caught*. That selection constraint is structural, not incidental; it is
stated here, before any of the material below, and at length in §10.1. The two case studies in
§6 and §7 are exploratory results from that project's own pilots; their numbers are reported
with the intervals and instabilities the underlying work established.

**© 2026 Barton Niedner.** Text licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Accompanying code: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). The author
retains copyright.

---

## Abstract

> **In plain terms (reader's summary).** We were building ways to measure whether AI systems
> miss things. Twenty-four times, a tool we had built gave us a confident result that did not mean
> what its label said. Our write-up of one of them put it in a line: *"The number was real; the
> label on it was not."* A "how much new did it find" score was really counting where two
> vocabularies failed to match. A "lift" from adding a second AI vendor was really two different
> quantities averaged together. A safety check reported "passing" while the tool it guarded was
> broken, because it could only detect problems in one direction. This paper is the record of all
> twenty-four.
>
> The part worth carrying away is not any individual mistake. It is two things about the set.
> **First: a number looking plausible was no evidence that it was right.** For twenty-three of the
> twenty-four, our records say what showed the number was wrong, and it was never the number looking
> wrong. Each time it was a second check, a comparison against something else, or someone sitting
> down and looking at what the number was actually counting. For the remaining one, the records show
> the safeguard we built once the problem was known, but not what found the problem. Several of
> the wrong numbers read as perfectly reasonable at the time; one was written up as the strongest
> evidence we had that one of our tools was measuring something real.
>
> **Second: evidence like this is easy to lose.** When a measuring tool is repaired, the repair
> can replace the broken version in the same change, and the record of *how it broke* goes with
> it, so the next person meets the failure fresh. We kept ours. The failures fall into seven
> recurring shapes that a reader can reuse, but what carried forward in our own work was the written
> record of each failure, not the individual fix. Keeping the
> record has already changed our later work. Notes written at the time credit one later safeguard
> to a specific failure we had written down, and another to the written record as a whole, and
> that second safeguard went on to catch a later failure. A third safeguard was recorded at the time with a reason of its own, and no
> record ties it to any failure we had written down. And once, the written record did the catching
> itself: a rule set in advance for a later study, deciding whether that study should reconsider its main
> measure, was read against a failure already on the list before the rule was ever used, and it was
> blind to exactly that failure.

Evaluating AI systems increasingly means building bespoke instruments — an LLM judging
another model's output, a matcher deciding whether two phrasings are the same idea, a control
meant to catch a generous grader. In our experience these instruments are constructed quickly and
trusted immediately, and they are hard to validate for a structural reason: the thing they measure is
usually the thing no gold standard exists for. This paper reports **twenty-four documented cases**, from a single
project explicitly working on this failure mode, in which such an instrument produced a
confident result whose label (a recall, a lift, a clean control) did not match what it actually
measured.

Two properties of the collection carry the paper. **A number looking plausible was no evidence
that it was right.** Twenty-three of the twenty-four entries record the check that established the
error, and each was an internal check, a cross-comparison, or an inspection of what was actually being
counted, never the number looking wrong; the remaining one records the guard built in response to its
error, not what found it. One of the wrong numbers had been written up at the time as the strongest
available evidence that the audit behind it worked. And the entries cluster into **seven recurring
shapes** — a check that measures something else; direction averaged away; identity mismatch; a judge
that over-credits; real-at-small-n-only; stale or raced state; instability read as signal — which
are transferable in a way the individual fixes are not.

Two case studies supply the paper's evidence without carrying its argument. In the first, an
instrument proved **ill-posed** rather than merely noisy: three mechanisms for deciding whether two
generators raised "the same" consideration failed in three different directions, and the pattern in
the failures is the finding — when two generators speak at different granularities, the question has
no determinate answer, and every mechanism that computes one is reporting how it resolved that
ambiguity. In the second, an instrument **worked and was read wrong**: generators raised a
consideration a real appellate court held a tribunal had missed **0.90** of the time, and raised it
and cleared the study's quality bar **0.85** of the time, while the measure reported **0.50** (95%
interval 0.33 to 0.67, covering case sampling only) — most of the shortfall being a matching rule that
discarded evidence for being dual-purpose.

The paper closes with what did the catching, what did not, and what we would do differently —
including one negative worth its own line: **a pooled figure can agree while the verdicts under
it do not.** On an earlier, 33-case version of the second case study's corpus, a scoring at k=2
(each judgement made twice and majority-voted) and a scoring at k=4 of the same 132 runs agreed
within **0.01** on the figure pooled over all runs, while disagreeing on **19%** of run-level
verdicts, and only keeping both scorings showed it. The figure for the cases that give least away,
the kind the study headlines, moved further: from 0.64 to 0.58. The two scorings also differed in their
tie threshold (the majority rule counts a tie as yes, so k=2 means at least 1 of 2 and k=4 at least
2 of 4) and in which decoys each run was judged against (missed points taken from other cases and
mixed in to catch a generous judge), so how much of that disagreement doubling k would remove was not
measured.

> **Honest-claim tag (house rule).** Every load-bearing claim in this paper is grounded in one
> project's own documents: internally consistent, externally unvalidated. This paper is a
> **case series**: it establishes that these twenty-four failures occurred and, for twenty-three of them, how
> each was caught. It does **not** establish a base rate, a frequency ranking among the shapes, or that
> the shapes are exhaustive. §10.1 states why it structurally cannot.

**Keywords:** LLM-as-judge · evaluation methodology · measurement validity · construct
validity · negative results · AI evaluation

---

## 1. Introduction

### 1.1 The instruments are new, and the ones that most need checking are the hardest to check

A large and growing share of AI evaluation runs on instruments built for the occasion. An LLM
scores another model's answer. A matcher decides whether *"premarital contracts"* and
*"division of property"* are the same issue or two. A membership judge decides whether a broad
heading covers a specific candidate. A control is written to catch a grader that says yes too
easily.

In our experience these instruments share three properties that together make them dangerous:

1. **They are built fast**, usually as a means to some other end — the real question is the
   experiment, and the instrument is plumbing.
2. **They are trusted immediately**, because they return numbers in the expected range.
3. **They are hard to validate**, because the quantity they measure is typically the one for
   which no gold standard exists. If a gold standard existed, the instrument would be
   unnecessary.

The third point is not a complaint about rigour. It is structural. The measures that most need
validation are exactly the measures that cannot be validated in the ordinary way, because they
are pointed at the region where human judgment has not been recorded.

### 1.2 What can happen to the evidence

When such an instrument is found to be broken, the fix and the deletion can arrive in the same
commit. The instrument is repaired, the wrong number is replaced by a corrected one, and the
record of *how a careful person came to believe the wrong number* disappears with it. Whoever
builds the next such instrument meets the failure fresh.

That is a rational local choice and a poor collective one. The fix is specific to one
instrument; the **shape of the failure** is not.

### 1.3 What this paper is

A project studying whether AI systems can be trusted to report on their own reliability kept a
record of its own instruments failing. The record began as a table in one pilot's write-up and
became a standing catalogue, with a rule to append every case — including, especially, those
found in work that otherwise succeeded (§3.2 gives its dates). The record, as this paper reports
it, holds **twenty-four entries**.

This paper is that record, organised by the shapes the failures recur in, with two of the
project's pilots supplied as worked cases. It is written for people building evaluation
instruments, not for readers of the project's own subject matter; no claim about the method
under study in those pilots is made or needed here.

**A reader who wants only the transferable part can read §4.2 (the seven shapes), §8 (what
caught them) and §11 (what we would do differently), and stop.** §10.1 states what none of it
can tell you. §6 and §7 are the worked cases behind them.

§2 places the work against the construct-validity, benchmark-critique, LLM-as-judge, and
forking-paths literatures, and states the gap it addresses: we did not find a first-person,
in-flight record of instruments failing **with the catching mechanism recorded**, which is what
makes §8 possible.

### 1.4 The two findings

**Finding 1 — a plausible-looking number was no evidence that it was right.** Twenty-three of the
twenty-four entries record the check that established the error, and in none of them was it the number
looking wrong: each was an internal check, a cross-comparison, or an inspection of what the number
counted. The remaining one, entry 6, records the guard built in response to its error, not what found
it (§5). Several of the wrong numbers read better than what replaced them. A cross-vendor lift of
**+0.130** read as a modest effect of the expected sign; taking only what the second vendor added,
against the same-vendor floor, gave **−0.114**, and an exploratory re-run on the same exam question
with output volume matched gave **+0.008**, a null. A gradient in how often generators recovered a
missed point, rising with how strongly each case's text gave that point away — **0.38 / 0.65 /
0.94** — was written up as the strongest available evidence that the audit rating the cases worked.
On a larger corpus, with that audit run five times instead of twice, it read **0.64 / 0.64 / 0.68**,
and no reading since has told the three levels apart.

**Finding 2 — the written record is the reusable asset.** The twenty-four cluster into seven recurring
shapes (§4.2), and the written record changed later work. The design note of the study in §7 says
its two-sided decoy control exists because of the failure recorded as entry 9, a sanity test that
could see error in one direction only. A recount of the §6 study's results built its falsification pass
in from the start on the strength of the catalogue as it then stood; that write-up credits the catalogue, not any one
entry. A third safeguard, a verbatim-quote requirement, was recorded at the time as a guard added
while the study rebuilt its case extraction, and no record traces it to any entry (§8.3). The falsification
pass went on to catch a later entry outright. The decoy control was found by a later entry to have a
hole — which is a better argument for keeping the record than a clean success would have been. And
once the record did the catching with no safeguard in between: entry 21, a gate written in advance
into a later study's design to decide whether its primary measure is reconsidered, was caught before
it ever ran by reading it against the catalogue, where entry 18, already written down, was the
counter-example to its reproducibility bar (§4.3). The fixes did not transfer; the written-down failures did.

---

## 2. Related work

> **Citation status.** Every reference below was checked on two separate questions — does it
> exist, and does it support the claim it is cited for — and the two are reported separately.
> **16 of 18** are confirmed to exist by DOI or arXiv id against a live index, and **16 of 18**
> were checked against the source's own retrieved text for the claim they back, ten of them against
> an abstract. The exceptions are named: **Hadamard (1902)** is not machine-resolvable and we found
> no retrievable text of it, and **Krippendorff** is a book whose claim was checked against secondary
> descriptions. The full record of what the checks found and changed is the note at the end of §2.7.

This paper draws on four literatures, and what it adds is a record we did not find in any of
them (§2.7).

### 2.1 Construct validity: an early statement of the problem

That a measure's *name* is not its *meaning* is not a new observation. Construct validity is a
discipline built around one of the failures this paper catalogues, and it long predates machine
learning. Cronbach and Meehl frame its question as *"What constructs account for variance in test
performance?"*, to be investigated whenever no criterion or universe of content is accepted as
entirely adequate to define the quality to be measured [@cronbach1955construct]. The term was the
chief innovation of the report of the American Psychological Association's Committee on
Psychological Tests, published in 1954 as the *Technical Recommendations* with the agreement of
committees of two other associations. Cronbach and Meehl, both members of that committee, record
that the idea was first formulated by a subcommittee of Meehl and R. C. Challman. They describe
their 1955 interpretation as not "official", and the paper as their attempt to explain the
concept and elaborate its implications [@cronbach1955construct].

Both they and Messick locate validity in the interpretation of scores. For Cronbach and Meehl,
construct validation *"is involved whenever a test is to be interpreted as a measure of some
attribute or quality which is not 'operationally defined'"*, and they write: *"In one sense, it is
naive to inquire 'Is this test valid?' One does not validate a test, but only a principle for making
inferences."* Elsewhere they still speak of a test's validity [@cronbach1955construct]. Messick
builds on their account and widens it into a **unified** concept, with construct validity as the
unifying force: validity is *"not a property of the test or assessment as such, but rather of the
meaning of the test scores"* — an overall evaluative judgement of how far empirical evidence and
theoretical rationales support the adequacy and appropriateness of the interpretations and actions
based on those scores [@messick1995validity]. Jacobs and Wallach [@jacobs2021measurement] carried the
framework into computational systems, which often involve *unobservable* theoretical constructs: such
constructs are operationalised through a measurement model, and the operationalisation can come apart
from the construct it is meant to measure. Many of this paper's entries sit where these accounts
point: a failure **built** into an instrument — a matcher, a control, a threshold — that **surfaced**
as a score meaning something other than its label said.

**Not all of them sit there, and mapping this catalogue onto construct validity is our framing,
not the field's name for it.** Entries 3, 5 and 8 fit in the plain sense: a score tracked a
different attribute than its label named. Entry 14 fits in another of Cronbach and Meehl's senses:
its gradient was offered as validation evidence of the kind they call group differences, a difference
the construct leads one to expect between groups [@cronbach1955construct], and the difference did not
hold. Ten more fit under Jacobs and Wallach's extension, where the operationalisation that came
apart is a matcher, a clustering, a metric, a projection, a judge, a guard or an estimate of the
judge's variance: entries 1, 2, 4, 6, 7, 9, 12, 15, 23 and 24. Entry 21 fits there too, though it
never ran: a gate whose precision bar, by its record, took one instrument's interval as the
precision of another.
**Eight do not fit in Cronbach and Meehl's sense.** Four are not about what a score meant: a small-n
effect and a refuted prediction (10, 11), and two stale or raced inputs (13, 19). Four are checks on
tooling rather than measurements: a completion signal that measured the loop rather than the work
(16), a parse check standing in for whether an edit landed (17), a silent process and an empty log
standing in for whether a run did any work (20), and a citation check that read one identifier
field and reported the identifiers absent (22). Each of those four reported something other than
its label said, but none produced a score whose interpretation a validity account addresses. That
leaves entry 18, verdicts disagreeing between two scorings of the
same runs: a reliability failure, whose place depends on the account. Cronbach and Meehl count
studies of *"differences associated with the examiner"* among those that have indicated *"upper
limits to test validity"* [@cronbach1955construct], so entry 18 arguably fits their account.
Messick's unified concept brings generalizability across occasions and raters inside validity
[@messick1995validity], and Jacobs and Wallach pair construct reliability with construct validity
[@jacobs2021measurement]; under Messick's formulation entry 18 fits, and arguably the instability
across scorings in entry 10 with it. The count depends on the formulation, which is part of why the
mapping is ours.

Where our entries fit that vocabulary, they are **operationalisation failures**: ways an
operational definition and its construct silently come apart in practice.
What the construct-validity literature supplies is the principled account; what it does not
supply, and what §5 reports for this record, is the empirical observation that, wherever the record
says how a failure was established, **it did not announce itself at the level of the number.**

### 2.2 Benchmark and evaluation critique in machine learning

A substantial body of work argues that ML benchmarks measure less than they claim. Raji and
colleagues [@raji2021everything] challenge whether general-capability benchmarks can support
the broad claims made of them — a construct-validity concern in substance, though that is our
framing of their argument rather than their vocabulary; Bowman and Dahl [@bowman2021benchmarking] set out what would be required
to fix benchmarking in language understanding; Blodgett and colleagues [@blodgett2021salmon]
audit bias benchmarks and find ambiguities and construct problems severe enough to undermine
their reported measurements.

The difference in posture is the point. That literature is largely **external and
retrospective** — an analysis of an artifact someone else published and the community has
adopted. This paper is **internal and in-flight**: the instruments are our own, the failures
were caught before publication rather than after adoption, and for all but one the record includes
*what caught them*.

### 2.3 LLM-as-judge and its known biases

Using a language model to evaluate another model's output is now standard practice, and its
characteristic distortions are documented: position bias, verbosity bias, and self-enhancement
bias [@zheng2023judging], along with evidence that evaluators score **their own generations**
higher than human annotators do [@panickssery2024selfpreference].

Those are biases **of the judge**. Most of what this paper reports is not: entries 1, 5 and 7
(shape C) are matching, clustering and projection failures in which the judge was working
correctly and the *comparison layer around it* was not, and entry 3 is a control that tested
deduplication while appearing to test the judge. The distinction matters practically, because a
pipeline hardened against known judge biases can still deliver a confidently wrong number through
the machinery that decides what the judge is asked about. Shape D — a judge over-crediting
something adjacent, entries 6, 12 and 15 — is the family here closest to that literature's
subject: a failure of the judge itself rather than of the machinery around it.

### 2.4 Researcher degrees of freedom, forking paths, and the multiverse

The finding in §6.3 — that three mechanisms for the same quantity produced three different
answers, each reporting its own resolution of an underdetermined question as a result — is a
**measurement-layer instance of a well-described analysis-layer problem**. Simmons, Nelson and
Simonsohn [@simmons2011falsepositive] showed how undisclosed flexibility in analysis choices
manufactures apparent findings; Gelman and Loken [@gelman2014forking] generalised it to
*"the garden of forking paths,"* where no p-hacking is required because a single defensible
path is chosen after seeing the data.

The response our §6 arrived at independently is close to **multiverse analysis**
[@steegen2016multiverse]: rather than defending one specification, run the plausible ones and
report the spread. We got there by failure rather than by design — three mechanisms were built
because each previous one broke — and the outcome is consistent with that literature's
rationale for reporting a spread rather than a specification: **no single mechanism was
diagnosable alone, and the disagreement was the finding.**

Two things we would offer as additions rather than instances. First, the forking paths here
are in the **measurement** layer rather than the analysis layer, which is earlier and less
visible: the choice is made when the instrument is written, not when the data is analysed.
Second, the spread across mechanisms diagnosed the **question** rather than the answer.
Well-posedness is Hadamard's notion [@hadamard1902problemes]; as a current lecture note states it, a
problem is well-posed when its solution exists, is unique, and is stable [@machida2024lecture]. What fails
in §6 is specifically **uniqueness** — more than one defensible resolution exists and nothing in
the problem selects between them. That is a stronger verdict than "this estimate is fragile," and a
multiverse over specifications is how we detected it.

### 2.5 Reliability, replicates, and the limits of majority voting

Inter-annotator agreement is the standard reliability instrument in content analysis
[@krippendorff2013content] and in computational linguistics [@artstein2008intercoder]. Sampling
a model several times and aggregating by majority was introduced as **self-consistency**
[@wang2023selfconsistency]; that the practice is now widespread is our own characterisation of
the field, not a claim of that paper's.

Our §9.1 bears on that practice. On the earlier, 33-case corpus of §7, a scoring at k=2 and a
scoring at k=4 of the same 132 runs **agreed within 0.01 on the pooled figure while disagreeing on
19% of run-level verdicts.** The two scorings also differed in their tie threshold — the majority
rule counts a tie as yes, so k=2 means at least 1 of 2 and k=4 at least 2 of 4 — and in their decoy
draws, so how much of that disagreement doubling k would remove was not measured. What the
comparison does show is the **empirical trap**: the pooled figure agreed across scorings (0.66 and
0.67) and would have been filed as confirmation. Beneath it, the clean-stratum figure, the stratum §7
headlines, moved from 0.64 to 0.58, and the disagreement in the verdicts was visible **only because
both scorings were kept**. Reliability reported at the aggregate can conceal disagreement that a run-level comparison
exposes immediately.

### 2.6 Negative results, and the genre this paper belongs to

Publication bias against negative and null results is long documented, and the specific
casualty here is narrower than a failed hypothesis: a **failed instrument** can be deleted in the
commit that fixes it (§1.2), so the evidence never enters the record at all. Software engineering
has a genre for first-hand accounts of this kind, the *experience report*; we name it as the
nearest genre we know of and cite no methods source for it. Medicine has the **case series**, a
collection of individual cases reported without a comparison group, and §3.2 adopts that label
and cites the methods literature behind it.

### 2.7 The gap this paper fills

The literatures above are, respectively: the principled account of the problem
(§2.1), external audits of finished artifacts (§2.2), characterised biases of one component
(§2.3), the analysis-layer version of our §6 (§2.4), and the reliability practice our §9.1 bears
on (§2.5).

What we did not find in them is a **first-person, in-flight record of evaluation instruments
failing, with the catching mechanism recorded for each.** We did not run a systematic prior-art
search, so that is a statement about what we found, not a claim that no such record exists —
reports in the experience-report genre §2.6 names are the likeliest place for one. That record is
what makes §8 possible — §8 names what did the catching wherever the record names it, and in
none of the twenty-three entries whose record says what established the error was it someone finding
the number implausible — and it is not recoverable from an external audit, because by the time an
artifact is public the catching mechanisms that were tried and failed have left no trace. The
contribution is not a new theory of validity. It is the observation, from twenty-four documented
instances in one project, that **a wrong number looking plausible was no evidence that it was
right**: wherever the record names what established an error, it was never the number looking wrong.
With that come the shapes the failures recur in and the mechanisms that actually surfaced them.

> **What the citation checks found and changed.**
>
> **Where the two axes stand.** *Existence* was resolved against a live index (Crossref, arXiv,
> Open Library), not supplied from model knowledge: **16 of 18** references are confirmed by DOI
> or arXiv id. One shows edition drift (Krippendorff — Open Library returns 1980 and 2013
> editions, and the citation reads 2013). One is not machine-resolvable in any index we queried:
> **Hadamard (1902)**, cited only for the origin of the notion of well-posedness. *Application* —
> does the work support the claim it is cited for — is the weaker axis. **16 of 18** were checked
> against the source's own retrieved text: **5 by the automated retriever**, and **11 by hand on
> 2026-09-16**, because the retriever's coverage is bounded by which publishers deposit abstracts to
> Crossref — a gap in the tool, not a property of the sources. All five automated checks, and five of
> the hand checks (Jacobs and Wallach, Bowman and Dahl, Zheng et al., Panickssery et al., and Dekkers
> et al.), were made against an abstract, so ten of the sixteen rest on an abstract. Two hand checks
> read another version of the cited work: Messick against the 1994 ETS research report that carries
> the cited article's title, and Gelman and Loken against their 2013 working paper, with the cited 2014
> article's subtitle for the phrase §2.4 quotes. We found no retrievable text of Hadamard (1902) in any
> index we queried; the criteria §2.4 uses rest on Machida, whose text we retrieved. Krippendorff is a
> book: the claim it backs was checked against secondary descriptions of its reliability chapter,
> **not against the book's own text**, and that is a weaker footing than every other entry here.
>
> *(A note on the counts below: they are citations as the verification tool extracted them from
> the draft in each pass, which is not the bibliography's entry count. The bibliography held 15
> entries through 2026-09-05, 16 once a modern companion to Hadamard was added on 2026-09-16, and
> 18 once the two case-series methods sources §3.2 cites were added the same day.)*
>
> **First pass, 2026-08-30.** The first draft of this section was written from model knowledge
> and its bibliography carried no DOIs, so a first verification pass confirmed **2 of 17**
> citations and fell back to memory for the rest — a coverage failure invisible in the prose,
> which read identically before and after. Resolving every entry against a live index raised
> confirmed existence to **13**. Three claims did not survive the *application* axis and were
> rewritten: Raji et al. are now credited with challenging what general-capability benchmarks can
> support, with "construct validity" marked as our framing of their argument rather than their
> vocabulary; Krippendorff and Artstein are now paired with the fields each actually covers
> rather than cited jointly for both; and the claim that majority-sampling is "routine practice"
> is now marked as our characterisation of the field rather than something the self-consistency
> paper establishes. Krippendorff's edition was corrected from a 4th/2018 claim to 2013. A
> reference recruited for a claim it does not support is **shape D** of §4.2 — a judge
> over-crediting something adjacent — and it would have been entirely invisible to a reader.
>
> **Second and third passes, 2026-09-05 and 2026-09-16 — and the first pass's own coverage was
> the thing that needed checking.** The 2026-08-30 pass reported both axes together. The
> 2026-09-05 pass found that its headline figure was scoped to **existence**, while for **11 of
> 16 citations the application judgement had come from model memory**, because the automated retriever can only reach
> abstracts that a publisher deposits to Crossref. That is not a wrong number; it is a right
> number standing where a reader will take it for a broader one — **shape A** of §4.2, in this
> paper's own verification. The status at the head of §2 now reports the two axes separately and
> names every entry that rests on weaker footing.
>
> The 2026-09-16 pass also found the verification tool itself misreporting. The 2026-09-05 report had
> marked two citations, Raji et al. and Wang et al., as carrying no identifier at all, and recommended
> adding identifiers. Both had carried a correct arXiv id since 2026-08-30. The tool's bibliography
> join read an entry's `doi` field and not its arXiv fields, and then reported the identifiers absent.
> That is **entry 22** of the catalogue (Appendix A), caught by reading the bibliography itself rather
> than the tool's summary of it.
>
> On 2026-09-16 the remaining applications were grounded by hand against retrieved source text,
> and **two more claims did not survive**:
>
> - **Panickssery et al. were credited with too wide a finding.** We had written that evaluators
>   *"favour text from their own model family."* The paper's claim is narrower and about the
>   model itself: an evaluator *"scores its own outputs higher than others' while human
>   annotators consider them of equal quality."* Family-level transfer is our extrapolation, not
>   their result, and §2.3 now states what they found.
> - **Messick was cited for a framing he explicitly rejects.** He had been paired with Cronbach
>   and Meehl for validity as a property of the instrument. Messick's own text says validity is
>   *"not a property of the test or assessment as such, but rather of the meaning of the test
>   scores."*
>
> Both are shape D again, and neither was visible in the prose. **Across the three passes, five
> claims, touching six of the sixteen citations, were recruited for more than their sources
> support** — in a paper whose subject is instruments whose results did not mean what their labels
> said, written by people watching for exactly that.
>
> **A review against the retrieved texts, 2026-09-16.** An independent review of this section,
> reading Cronbach and Meehl in full and Messick in the 1994 report version, found that the Messick
> repair had overshot. It had cast Cronbach and Meehl as holding the instrument view Messick rejects,
> and their text does not rest on that view either: *"In one sense, it is naive to inquire 'Is this
> test valid?' One does not validate a test, but only a principle for making inferences."* §2.1 now
> cites both for locating validity in the interpretation of scores, with Messick widening that into a
> unified concept. The same review corrected six smaller characterisations: the name of the APA
> committee and Meehl's part in formulating the term; "the oldest" statement of the problem, when
> Cronbach and Meehl call construct validity the chief innovation of the 1954 report; reliability as
> something Cronbach and Meehl "keep separate", when they allow score stability as evidence; the
> subject of Messick's definition, which is evidence and theory supporting an interpretation, not a
> score; a hedge dropped from Cronbach and Meehl's condition (*"accepted as entirely adequate"*); and
> Jacobs and Wallach's *unobservable*, which had been quoted as *unobserved*. It narrowed two
> attributions — the three well-posedness criteria now rest on Machida rather than on Hadamard's 1902
> paper, and judge-bias work is now described as closest to shape D's subject rather than as having
> predicted it — and it supplied the case-series methods sources §3.2 now cites.
>
> **A second pass over the same texts, the same day,** found that repair a step too strong in turn.
> §2.1 had said both works locate validity "not in the instrument", which is Messick's position;
> Cronbach and Meehl's denial carries the qualifier *"In one sense"*, and elsewhere they still speak
> of a test's validity, so §2.1 now quotes the qualifier. The pass moved two entries in §2.1's count:
> entry 14 fits Cronbach and Meehl's account, because its gradient was offered as the group-difference
> evidence they describe, and entry 18 now rests on their counting examiner differences against a
> test's validity, where §2.1 had cited a sentence about stability over occasions. It also found that
> this note had named one hand check made against an abstract when there were five.
>
> **The two references not checked against their own text** should be weighed against that rate:
> six of sixteen, a little over one in three. Krippendorff is one of those six — its
> claim was narrowed on 2026-08-30, and the narrowed claim rests on secondary descriptions of the
> book. Hadamard (1902) now carries only the attribution of the notion of well-posedness; the
> criteria §2.4 uses rest on Machida, whose text was retrieved. Both remain on weaker footing than
> every other reference here, and neither is load-bearing for any finding in this paper.

---

## 3. Scope, genre, and what this paper does not claim

### 3.1 The subject is instruments, not the project

The two pilots in §6 and §7 belong to a research programme testing whether AI systems can be
trusted to report on their own reliability, through structured AI deliberation. That
programme's claims are reported elsewhere and are **out of scope here**. The pilots appear
because they are where the instruments were built and where they failed — a reader who knows
nothing about the method under study loses nothing.

### 3.2 This is a case series

The appropriate genre label is **case series**. In the medical literature it names a
publication that aggregates individual cases, uncontrolled and non-comparative
[@murad2018methodological], and the label is used inconsistently enough that it is worth stating
what we mean by it [@dekkers2012distinguishing]. Here it is a documented, non-random collection
of instances with a common structure, reported for the transferability of the pattern rather
than for a rate; that purpose is our framing, not a definition either source gives. It is not a
survey, not a randomised comparison, and not pre-registered. *(Of the two pilots it draws on, the
one in §7 pre-registered its analysis decisions in a design note that, by its own record, was
written before any data was pulled. The one in §6 was declared exploratory and not a
pre-registration, though it wrote down what it expected before the data arrived. Both records are
deposited with this paper, and §12 says what anchors their timing.)* What a case series can establish is that
these failures occur, what form they take, and what caught them. What it cannot establish is how
often they occur — a case series selects its cases by their outcome and, unlike a cohort study,
supports no calculation of a rate for that outcome [@dekkers2012distinguishing] — nor which shape dominates, nor whether the seven shapes
are exhaustive.

In Murad and colleagues' framework for the methodological quality of case series, the first
domain is **selection**: a series that describes every case in its authors' experience over a
period meets it, and one whose selection method is unclear leaves open that similar cases went
unreported [@murad2018methodological]. Selection is also what we take to separate this collection
from a pile of anecdotes. Its rule is §4.1's: append every case, **including those
found in work that succeeded**; never remove an entry because it was later fixed; record the
mechanism that caught it. The rule was written down on 2026-08-29, in the commit that consolidated
the first fifteen entries from the project's working records, and entries 16–24 were admitted
under it. The fifteen gathered before the rule meet that standard only as far as the working
records they came from were complete. No entry has been removed since, and this paper reports the
catalogue as it stood on 2026-09-16, at twenty-four entries (§4.1). The same selection names
what the collection lacks: an entry is admitted only by **being caught**, so there is no
denominator of failures that occurred — the limit §10.1 states in full.

§10.1 comes before the practitioner guidance in §11 so that the guidance is read against the
limits it states.

### 3.3 What is *not* claimed

- **No base rate.** The catalogue counts failures found, not failures occurred.
- **No frequency ranking.** That seven shapes recur says nothing about their relative
  prevalence in the wild, or even in this project. The same holds for the five catching
  mechanisms in §8.1: their order is an order of appearance in this record, not of efficacy.
- **No exhaustiveness.** Seven shapes describe twenty-four entries from one team's habits and
  tooling. A different stack would likely surface shapes we do not have.
- **No claim that our catching methods are sufficient.** §10.2 names a class of failure that
  none of them can detect, and we believe it to be the important one.

---

## 4. The catalogue

### 4.1 What is recorded, and the rules

Each entry records four things: **what the number said**, **what closer checking found**,
**which shape it took**, and — the field that does the work — **how it was caught**. The rules
were written down on 2026-08-29, in the same change that consolidated the first fifteen entries
from the project's working records; entries 16–24 were added under them. They are:

- Append every new case, including ones found in work that succeeded.
- Never remove an entry because it was later fixed. **The fix is part of the record.**
- Record the catching mechanism, not just the diagnosis.

That third rule is what makes §8 possible. The earliest collected list, of entries 1–8, already
had a column for how each was caught; the rule made that field required for every entry since.

**This paper reports the catalogue as it stood on 2026-09-16, at n = 24.** The catalogue is a
standing, append-only artifact of an ongoing project, and it will keep growing after publication —
the study whose design this project is currently pre-registering will very likely add to it. Entries
added after that date extend the artifact, not this paper. Without a stated date, a catalogue paper
would either have to stop the catalogue or quietly fall out of step with it.

### 4.2 The seven shapes

| shape | what happens | one instance | entries |
|---|---|---|---|
| **A. The check measures something else** | A check or a measure reports on something other than its target — a validation that tests deduplication rather than the judge, a completion signal that tests the loop rather than the work. | a control "failed" at 0.50; the judge was right, and the control was measuring deduplication | 2, 3, 8, 9, 16, 20, 21, 22, 23, 24 |
| **B. Direction averaged away** | Two different quantities are averaged into one number that describes neither. | a cross-vendor lift printed as +0.130, "SUBSTANTIAL": the measure averaged what one vendor's runs added over the other's with what they lacked, and printed the result as a lift | 4 |
| **C. Identity mismatch** | Two names or filings for the same thing fail to match, so the measure counts a difference that is in the naming, not the substance — orthographic, lexical, or the same doctrine filed under two headings. | weighted recall 0.00, because `1(a)` and `(1)(a)` did not round-trip | 1, 5, 7 |
| **D. The judge over-credits** | A matching or membership pass says yes to something adjacent, and the yes is invisible because nothing tests near-misses. | a 10-item list judged to cover 261 of 281 candidates | 6, 12, 15 |
| **E. Real at small n only** | A large, mechanistically plausible effect that dissolves as data is added. | the missed point recovered far more often in cases from first-instance tribunals than from reviewing ones (0.90 against 0.50), with a ready mechanism; as cases were added and the design was scored again, the gap shrank and then changed sign | 10, 11 |
| **F. Stale or raced state** | The number is computed from inputs that have since changed, silently. | two scorers raced on a shared file, and 8 rows kept a label written by the other scorer | 13, 17, 19 |
| **G. Instability read as signal** | A gradient or ordering that is a property of the estimator's variance, not the world. | recovery reading 0.38 / 0.65 / 0.94 across three levels of how plainly a case's facts give away the missed point, a 0.56-point spread; once the pass assigning those levels (the leakage audit) was run with five replicates instead of two, the spread in every later reading was between 0.04 and 0.21, and none has separated it from zero | 10, 14, 18 |

The letters are labels, not an ordering; §3.3 disclaims any ranking among the shapes. Entry 10
carries two shapes. Each instance's figures are that entry's own; where one matches a figure
reported elsewhere in the paper, such as the abstract's 0.90 and 0.50, it measures something
different. The full twenty-four-entry table is **Appendix A**. The body below discusses the entries that
carry the argument; the appendix is the record.

### 4.3 The five entries that changed how the work was done

Most entries are instructive. Five changed how the work was done. Three of the project's later
safeguards appear in the record, credited at three different strengths (§8.3). Records written at
the time credit a two-sided decoy control specifically to the failure recorded as entry 9, and a
falsification pass to the list of failures already written down, which held that failure. The
falsification pass went on to catch entry 12, and entry 15 found a hole in the decoy control. No
record traces the third safeguard, a verbatim-quote requirement, to any entry. Entry 18 changed a
practice rather than producing a safeguard. In entry 21 the written record did the catching itself,
with no safeguard in between, and the catch changed a later study's design.

**Entry 9 (shape A) — a guard that passes because it cannot see the failure it was built for.**
A sanity test reported *passing* while the instrument it guarded was broken. The test could
detect error in only one direction: it checked for false novelty and was blind to everything
reading as identical. It is the direct ancestor of the two-sided decoy control in §7.

**Entry 12 (shape D) — the falsification pass that saved a triumphant conclusion.** A recount
of the **parent study** — the coverage study §6 draws on — ran a "material beyond the key" pass
that claimed 18.4 items per run. A second, different-vendor pass, blind to which item each phrase
came from, **struck 88% of them**. Stopping at the first pass would have moved one generator
configuration's reported off-key rate from 0.03 to roughly 0.36 and looked like a clean
confirmation of a prediction the project had already made in print. The recount's own write-up says why the falsification pass was there: it was built in from the
start, "on the strength of" the list of failures already written down.

**Entry 15 (shape D) — the control that could not see a near-miss.** A case showed raw recovery
of **1.00** on a seed that was **not raisable from the case file at all** — the seed turns on
calendar-date discrepancies the file never mentions. The judge had been crediting a topically
adjacent item. The study's own best control — clean on the current corpus, well under the 0.10 rate its
scorer allows for a clean verdict (§7.1) — could not see this. It draws each decoy from another case in the corpus, on
the assumption that such a decoy has nothing to do with these facts, so it was built to test
far-off generosity.

**Entry 18 (shape G) — an aggregate that agreed while a fifth of its verdicts did not.** A scoring
of the same 132 runs with two judge calls per verdict (k=2) and another with four (k=4) agreed
within 0.01 on the pooled figure while disagreeing on 19% of run-level verdicts, and only keeping
both scorings showed it. The clean-stratum figure, the one §7 headlines, moved more: from 0.64 to
0.58. The two scorings also differed in their tie threshold (a tie counts as yes, so k=2 needs one
of two and k=4 two of four) and in their decoy draws, so how much of the disagreement doubling k
would remove was not measured. It produced no new safeguard. It changed a practice: two scorings of
the same runs are now compared run by run, never by their pooled figures (§9.1).

Entry 15 generalises entry 9 into a sentence worth keeping: **a control tests the failure it was
shaped to test.** A clean far-off control says nothing about near-misses, and reporting it as
"the judge is not generous" overstates what it establishes.

**Entry 21 (shape A) — a gate caught by the catalogue before it ran.** A later study in the same
programme wrote into its design, in advance, the condition under which its primary measure would be
reconsidered: two bars, named precision and reproducibility, each with a number attached. Neither
measured what its name said. The precision bar, by the catalogue's record, was set on the interval
of the seeded-miss study's headline, which asks whether a generator recovered one planted missed
point. The hypothesis the gate governs asks how much off-key material a generator emits across its
whole output. Both run through the same matching rule, which is why §7 calls that headline off-key,
but the project's own register of its instruments lists them as two measures with different
precision, so the bar certified one measure for a claim carried by the other. The reproducibility bar was stated on a pooled
figure, and entry 18, already in the catalogue when the gate was written, is a pooled figure that
agreed within 0.01 while a fifth of the verdicts beneath it did not. A gate written that way passes
in the situation it exists to catch. By the record made when the gate was amended, both defects were
found by reading it against the catalogue, before the check had run and before any of that study's
factorial data existed. The gate was
amended, with the reproducibility bar now on run-level verdict agreement and the superseded text
kept beside it. Nothing had been misreported to anyone; the entry is in the catalogue because its
shape is the shape of entries that were.

---

## 5. Finding 1 — a plausible-looking number was no evidence that it was right

The claim is narrow and checkable against Appendix A. Twenty-three of the twenty-four entries record the
check that established the error, and in none of the twenty-three was that check a person looking at
the number and finding it implausible. The remaining one, entry 6, records the safeguard built in response to
its error, not the check that found it.

**Entry 6.** Appendix A lists a *"plausibility guard"* beside it: a mechanical bound that flags any run
judged to cover more than three times as many candidate issues as the run itself raised, and that
fires without anyone's judgment. The guard came after the error was understood. Its code comment
already names the failure, *"membership over-merging"*, in a first build of the membership judge that
credited a list of 10 broad headings with covering 275 of 281 specific candidates (the deviation
record gives 261 of 281 for the same failure), and the commit that
added it records that a tightened prompt, tried first, *"barely moved it"*. So the guard was the response to entry 6, not the check that established it, and what did establish it is not on file.
Entry 9 belongs to the same event: the sanity test that passed was the one guarding this membership
judge. It is counted among the twenty-three by what established its own error, that the test could detect
failure in one direction only; that the instrument it guarded was broken is entry 6's error, and what
established that is not on file either.
Entries 3 and 8 are different: in each, a control's number fell outside a threshold set in advance,
someone then looked, and the record names what that look found. That is the distinction §8.1 draws
between a mechanical bound and a person's reaction to a number.

**One bound on that claim.** The catalogue's catching field records the check that **established**
each error. It does not record whatever prompted someone to run that check, so the claim is about
what established each error, not about what first drew attention to it. Where the record does show
what set a check running, it was something disagreeing with something else, or a check already in
place — never the number looking wrong on its own. Entry 13's 0.58, below, is the clearest case. Its
deviation record, the pilot's dated log of departures from its plan, traces the catch to a table
reporting 24 runs over 6 cases rated as not giving the answer away, while the file of record listed
seven, and says in as many words that it was *"not the number looking wrong."* The deviation records
for entries 4 and 5 say the same of theirs. So does the catalogue's record of entry 19, written the
night it was caught: the variance tool's off-key 0.639 over 9 cases was a perfectly reasonable
figure, and what showed it wrong was knowing that the clean stratum now held 15 cases while the
tool's header said 9. The practical consequence below does not depend on what
prompted any check.

The obvious reading is that we were unusually diligent, and it is the wrong one. **Several of the
wrong numbers looked entirely reasonable.** Consider three:

| the number | why it reads fine | what it was |
|---|---|---|
| cross-vendor lift **+0.130, "SUBSTANTIAL"** | a modest positive effect, the expected sign | two different quantities averaged into one number that describes neither (shape B). The tool's first version averaged the two directions of the comparison, what the second vendor added and what it lacked, into 0.304, which cleared the same-vendor floor, and printed a lift of +0.130. That run's clustering was not saved, so none of its figures can be re-checked. The only saved clustering is from the corrected run: there the second vendor added 0.038 and lacked 0.553, and the added direction alone against the 0.151 floor is **−0.114**; an exploratory re-run on the same exam question, with output volume matched, gave **+0.008**, a null |
| the headline figure in a scorer's report, **0.58** | the report's table was internally consistent: 24 runs over 6 cases | **0.50**. Two copies of the scorer, run at the same time, each wrote the file that records how strongly each case gives its missed point away, and 8 rows kept the label computed by the other copy (shape F) |
| a gradient in recovery across three levels of how strongly each case's text gave the missed point away: **0.38 / 0.65 / 0.94** | cases that give more away should be recovered more often; the study's first write-up called it *"the strongest available evidence"* that the audit rating the cases measured something real | a 0.56-point spread that did not hold. On a larger corpus, with that audit run five times instead of twice, it read **0.64 / 0.64 / 0.68**; two later scorings read 0.58 / 0.61 / 0.75 and 0.50 / 0.65 / 0.71. The spread fell to between 0.04 and 0.21, and no reading since has told the three levels apart (shape G). The five-run audit also fired a gate that removed one case whose missed point could not be raised from its file |

The third is the instructive one. The gradient was not merely unsuspected; it was welcomed. It
matched what the audit was expected to produce, so it was written up as validation, and a number
that matches its expectation reads as confirmation rather than as something to check. A number
only looks implausible relative to an expectation, and in exploratory measurement the expectation
is either weak enough to accommodate whatever arrives or, as here, specific enough for an artifact
to satisfy it.

Entry 1's weighted recall of **0.00** is not in the table, although its own deviation record calls
it plausible-looking. It was the scorer's first result, on a generator output whose coverage the
project had already recorded: a note surveying the corpus, committed before the scorer existed, lists
that output's 57 issues as covering every one of the answer key's five points, recall 5 of 5. So the
0.00 contradicted a fact already on file. The record does not say what prompted the check; if that
contradiction did, it was a cross-comparison against a known value, not a sense that the number
looked wrong.

The practical consequence is the one sentence we would keep if we kept only one:

> **On this record, a number looking plausible was no evidence that it was right.** Wherever the
> record names what established an error, it was a check, never how the number looked.

---

## 6. Case A — an instrument that was ill-posed, not merely noisy

*The pilot behind this case supplied entries 1–9, which span §4.2 shapes A, B, C and D. The
sections below work through three of them: entries 5 and 7 (shape C) and entry 6 (shape D). A
reader who skips it loses examples, not the argument.*

### 6.1 What was being built

The goal was a coverage measure that did not depend on a contested answer-quality judgment:
run a second, independent generator and count what it surfaces that the first one missed. Every
number in that design requires one operation — deciding whether something raised by
**generator B**, a structured enumerator, is **the same issue** as something raised by
**generator A**, running free.

Three mechanisms were built for that operation. All three failed, in three different
directions.

### 6.2 Three mechanisms, three failures

**Attempt 1 — pooled clustering.** Failed by **under-merging**. It marked *"Premarital
contracts"* and *"Division of property"* — the human examiners' 30%- and 35%-weighted key
points — as issues generator A never found, when A had covered them under 45 distinct
labels. Clustering on label *plus* rationale, to bridge the vocabularies, moved
measured novelty **the wrong way** (+0.274 → +0.305): the richer text made nearly every item
unique, pooled distinct strings rose from 281 to 377, and the clusterer received a harder task
rather than a better-informed one.

**Attempt 2 — directed membership.** *"Is candidate X present in this list?"* — the same shape
that scores 1.00 unanimity when matching against a human answer key. Failed by **over-merging**,
the exact mirror image: a 10-item walk of broad taxonomy headings was judged to cover **261 of
281** specific candidates. Tightening the prompt with explicit anti-inflation instructions moved
it barely at all.

**Attempt 3 — project both sides onto a fixed taxonomy, then do set arithmetic.** Give both
generators one externally-fixed coordinate system (350 nodes), so no cross-vocabulary matching
happens at comparison time. This one **produced plausible numbers and a wrong answer**: node
counts were sane, the floor landed in line with earlier estimates, and it reported a lift of
**+0.207** for generator B.

It was a **filing artifact**. Nine "B-only" nodes included *Defenses > Duress and undue
influence* and *Fraud, misrepresentation, and nondisclosure* — while generator A had
explicitly produced *"Defenses: duress/undue influence"* and *"Defenses: fraud/
misrepresentation."* Both sides raised the doctrine. The projection filed one under *Family Law
> Premarital contracts* and the other under *Contracts > Defenses*, and set difference reported
a gap that does not exist. **The taxonomy carries the same doctrine in more than one place, so
the coordinate system is not unique and the projection is not well-defined.**

### 6.3 The finding is the pattern, not any one failure

> When two generators speak at different granularities, *"did B raise something A didn't"* has
> **no determinate answer**, and every mechanism that computes it is really reporting how it
> resolved that ambiguity.

This is a different and more serious verdict than "the instrument was noisy." A noisy
instrument can be improved by more data or more replicates. An **ill-posed** one cannot, because
the quantity it estimates is not defined independently of the estimator. It can only be improved
by deciding the question the design left open — fixing the matching granularity, say — and
reporting that decision as a convention rather than as a result. The three mechanisms did not disagree because one was better built; they disagreed
because each silently supplied a different answer to a question the design left open.

**How this was caught matters as much as the result.** Not by any one mechanism's number. Each
failure, taken alone, read as a defect in that mechanism and prompted a replacement, and the third
mechanism produced entirely plausible numbers. What showed that the question itself was ill-posed
was **running three and comparing them**. A single mechanism, competently built, would have shipped
a number.

### 6.4 Expansion produces more output, not more answer

Every mechanism this case built for comparing the two generators was ill-posed, and one result
that did not depend on comparing them still stood. That is §9.3's rule — *a broken rule does not
make every number computed with it wrong* — in its cleanest instance, and it answers the question
a reader should be asking by now: if the comparison was that broken, why believe anything from
this pilot?

Pushed from 22 items to 56 on instruction, a model **lost 30 points of yield**, doubled its noise
and more than doubled its redundancy:

| | items | recall | yield | noise | redundancy |
|---|---|---|---|---|---|
| natural | 22 | 1.00 | **0.79** | **0.06** | **0.14** |
| ~55-item budget | 56 | 1.00 | 0.49 | 0.13 | 0.34 |

*recall* = share of the human examiners' weighted key points the run found · *yield* = share of
emitted items that were sound, raised, material and non-duplicate · *noise* = share that were not
a real issue correctly stated, or not actually put in play by these facts · *redundancy* = share
that restated an earlier item. These are not a partition of the output — an item that is sound and
on-point but immaterial counts toward none of them — so the rows need not sum to one.

**Recall was 1.00 in every configuration, including a 13-item walk.** So this design could not
have detected a coverage gain in either direction, and the result is about cost, not coverage:
redundancy tracks volume almost linearly across every configuration measured (13 items → 0.09;
22 → 0.14; 56 → 0.33 and 0.34, one figure per vendor; 63 → 0.35), in both vendors tested.

§7.4 points the same way on cost, in a different design and a different corpus: of two generator
vendors, paired over 47 cases, the one emitting about two and a half times as many items per run
had the lower yield, 0.518 against 0.634. **This result is also the baseline a companion paper on
the same project's method has to beat.**

---

## 7. Case B — an instrument that worked and was read wrong

*This case illustrates shapes A, D, E, F and G. It supplies entries 10–15 and 18, two more from the
run that grew its corpus (19, 20), and two from this paper's own review of its variance budget (23,
24). A reader who
skips it loses the worked numbers behind §8, not the argument; the two general points it makes
(§7.3, §7.6) are restated in §11.*

### 7.1 The design

The measure under validation — call it **off-key discovery** — counts items that clear a blind
judge's quality bar (defined below) and match **no** point in a human-authored key. It is the one
measure in the family that looks at ungraded material, and therefore the one number nothing
could check.

To check it, the project needed a **seed**: a consideration a real decision-maker actually
failed to weigh. It took them from appellate opinions in which a court held that the tribunal
below erred by failing to consider something, filed **after both vendors' training cutoffs**.
The generator sees only the situation as it stood before the lower court, and is asked to list
every issue the court must address. It is never told anything was missed.

**Three terms the rest of this case depends on.**

- **Leakage stratum.** The situation is written from the appellate court's own statement of
  facts, and that court already knew what was missed — so it may foreground exactly those facts,
  which inflates recovery. An independent blind pass, the **leakage audit**, rates each case for how strongly its
  situation *telegraphs* the seed: **explicit**, **hinted**, or **neutral**. The **clean
  stratum** is the neutral one. Every headline figure below is the clean stratum, because
  leakage can only push recovery up, so it is the only stratum where a high number is not
  confounded.
- **Stimulus-validity gate.** A case is dropped before scoring if its seed is **impossible** to
  raise from the file the generator sees — not merely hard. It removes cases, and so it sets the
  corpus size.
- **The quality bar.** An item counts as **signal** if the blind judge rates it sound (a real
  issue, correctly stated), raised (put in play by these facts), material (could change the
  outcome) and non-duplicate. The positive control below applies the first three only. Off-key discovery and partial
  credit (§7.2) apply all four. Raw recovery applies none: it asks only whether any item
  addressed the seed.

**The corpora.** Every §7 figure rests on one of two corpora:

| corpus | cases extracted | removed by the gate | cases scored | clean-stratum cases | runs scored |
|---|---|---|---|---|---|
| earlier | 34 | 1 | 33 | 9 | 132 |
| **current** | **49** | **2** | **47** | **15** | **188** |

The gate has removed two cases in all, and the leakage audit rated both neutral, so each would
otherwise have sat in the clean stratum. *Eqbal v. Blanche* was scored in the study's first three
passes and removed when the audit was re-run at five replicates (§7.6; entry 15). *People v.
Occhipinti* entered with the current corpus and was removed at its first audit, before any of its
runs was scored. The table counts cases after removal: *Eqbal* is out of both rows, *Occhipinti*
out of the current one.

Four runs per case throughout: two generator vendors, two runs each. Each run is judged k times and
the verdicts are majority-voted; k is the number of **scoring replicates** (also called judging
replicates), and the leakage audit is replicated separately. Both corpora are reported at four
scoring replicates, with the audit at five, except in §7.6's history of earlier passes and §9.1's
comparison. Earlier, smaller passes appear only in §7.6's reading history.

Two controls, and the second is the one that licenses everything else:

| control | result | reading |
|---|---|---|
| **positive** — over key points a run covered, does the blind judge rate ≥1 covering item sound + raised + material? | **0.97** (pre-set floor 0.90) | PASS |
| **negative** — decoy seeds from other cases, scored in the *same shuffled call* as the real seed, among decoys the judge rules not applicable to these facts | **0.01** (n=557) | CLEAN |

The negative control can be reported two ways, and an earlier version of the underlying pilot did
report it both ways, on different lines, without saying why. **They are not a discrepancy; they
are two denominators.** Over all 564 decoys the "recovered" rate is 0.02. Over the 557 the judge
ruled not applicable to these facts, it is 0.01 — and that is the false-positive floor, because a
decoy that does not apply should never be credited. The remaining **7 decoys the judge ruled
applicable were credited at 0.86** (6 of 7). A number that reads as an unresolved conflict and turns
out to be a denominator is §5's point in miniature.

**Those seven are not generic considerations.** The scorer's report labels applicable decoys
"generic considerations that really do apply", meaning requirements such as making findings and
stating reasons, which apply to any case. All seven were written for another case, and most carry
its specifics. Read against the case files, they sort three ways. Two apply in substance: whether a
lesser sanction would have served, and concurrent rather than consecutive sentences. Their credit is
sound. Two name another jurisdiction's rule or test (Idaho's Rule 16(e), Nevada's *Young* factors)
in a case whose file carries its own state's counterpart, so the question plausibly applies and the
credit is defensible. Two name facts from another case that are absent from this one (another
couple's 55/45 property split and capital-gains allocation; another party's social-media contacts)
and were credited on an item that addressed only the general topic. The seventh was not credited. So
the false-positive floor depends on how many of those applicability rulings stand: **0.014 if all of
them do, rising to 0.021 if the four decoys that carry another case's rule or facts are counted as
not applicable.** Every version is far under the control's own threshold of 0.10, and its verdict
stands.

It also says what this control is. It was built to test **far-off generosity**, with decoys drawn
from other cases, and on that it is **clean**. It was not built to test **near-misses**. Entry 15
showed that gap. The two fact-bound credits above are the same generosity turning up inside the
control by accident, and they show only when the decoys are read against the case files. The control
exists **because of entry 9**.

### 7.2 The result: the loss is the matching rule, not blindness

In the cleanest leakage stratum (60 runs over 15 cases), the numbers decompose:

```
raw recovery              0.90     some item addressed the missed consideration
  reported as off-key     0.50     the measure counted it
  absorbed into the key   0.40     the measure discarded it
never raised at all       0.10
```

**Off-key reported 0.50 where the generators raised the seed 0.90 of the time.** Raw recovery has
no quality condition; the figure that also requires the quality bar is **0.85**, partial credit
(defined below). Most of the
shortfall — **0.35 of the 0.40** — is an **exclusive-match rule**: the matcher credits the same
item against a key point, the item is stripped from the off-key set, and a hit is recorded as a
miss.

The 0.50 is a mean over a flat distribution, not a typical case. The 15 per-case values are
**0.00, 0.00, 0.00, 0.25, 0.25, 0.50, 0.50, 0.50, 0.50, 0.75, 0.75, 0.75, 0.75, 1.00, 1.00** —
spread across all five values four runs allow.

Per case, this is not an averaging artifact. **Three cases recovered 0.00** under the exclusive
rule while their generators had plainly found the consideration. The table's *partial credit*
column counts an item for the seed whether or not the matcher also credited it to a key point,
with the quality bar unchanged:

| case | raw | off-key | partial credit | absorbed |
|---|---|---|---|---|
| *Needham* | 0.75 | **0.00** | 0.75 | 0.75 |
| *Thaete* | 0.75 | **0.00** | 0.75 | 0.75 |
| *Sheffield* | **1.00** | **0.00** | 0.75 | 1.00 |

The first two are the clean form of the defect: every run that raised the seed had its citing
item absorbed, so the measure reported zero while the generator had in fact found the
consideration **three times in four**, and partial credit returns exactly that.

**The third case, *Sheffield*, entered with the current corpus and shows that the two failure modes
are separable.** Its generators raised the seed in **all four** runs, yet partial credit returns
0.75, not 1.00: in one run, neither of the two items addressing the seed cleared the blind judge's
quality bar (sound, raised, material, non-duplicate). That is not the matching rule discarding
evidence; it is evidence that did not clear the bar. The scoring does not record which criterion
failed, so it cannot say whether those items were unsound or duplicates. Both failures report 0.00
through the exclusive rule, and they are not the same thing.

Dropping the exclusive rule — an item counts for the seed whether or not the matcher also
credits it to a key point, with the quality bar unchanged — recovers nearly all of it:

| rule | clean stratum |
|---|---|
| exclusive match (as reported) | 0.50 |
| **partial credit** | **0.85** |
| raw (upper bound) | 0.90 |

**The five-point residual is a quality-bar effect, not a matching-rule one, and it corrects how this
was first reported.** On the earlier corpus's 9-case clean stratum, partial credit equalled raw
exactly, and the study's write-up said nothing is lost between the generator addressing the seed and
the corrected measure counting it. On the current corpus that is no longer exactly true: in **3 runs
of 60**, every item addressing the seed failed the blind judge's quality bar (one item in two of
those runs, two in *Sheffield*'s), so raw counts the run and partial credit does not. The claim that
the exclusive-match rule is responsible for the *bulk* of the shortfall is untouched: it accounts
for 0.35 of the 0.40 gap. What changes is that "exactly" was a property of nine cases, and it did
not survive six more.

### 7.3 And the corrected rule cannot be used for comparison

Partial credit lands at **0.85 / 0.92 / 0.99** across the three leakage strata, at or near ceiling
in all three, leaving 0.15 of headroom in the clean stratum, the only one a comparison would be run
in. Its own 95% interval there is **[0.77, 0.92]**.

That is too little room to compare two generator setups at this corpus size. *This is a model
estimate, not a measurement:* setting each clean-stratum case's recovery rate to its observed
partial credit, drawing four fresh runs per case for each setup, and testing the paired difference
over the 15 cases at the 5% level, with the gain spread across cases in proportion to each case's
room below 1.00, a second setup that used the whole 0.15 of headroom would be detected about **85%**
of the time, a ten-point gain about **a third** of the time, and a five-point gain about **10%**. Only a gain close to the full headroom is reliably visible. A rise is easier to see than an
equal fall (a fifteen-point fall would be detected about half the time), because a setup at 1.00 has
no run-to-run variation. *(On the earlier corpus's 9-case clean stratum the strata read 0.92 / 0.92
/ 1.00, flat at the ceiling. The conclusion is unchanged; its reason is now too little room rather
than none.)*

That gives the two rules different jobs, and **neither replaces the other**:

- **Partial credit is a validation measure**: "did the generator find it?" It is the honest answer
  to that question, and near its ceiling it has too little room to compare setups reliably.
- **Exclusive match is the candidate comparison measure.** Being lossy, it sits mid-scale, where a
  difference has room to show, but its **level is not a coverage rate and must never be read as
  one.** It does keep a monotonic ordering across the leakage strata (0.50 / 0.65 / 0.71). We do not
  report that as an established separation. Bootstrapping cases within each stratum, the difference
  between the explicit and clean strata runs from −0.02 to +0.44, and between the hinted and clean
  strata from −0.08 to +0.37; both intervals include zero. **Entries 10 and 14** are two orderings
  in this project that looked like this and did not hold.

Reporting partial credit as a coverage improvement would be its own confident wrong number: a
ceiling effect dressed as a result. This is the paper's cleanest example of a general point: **a
repaired instrument can acquire a new failure mode in the repair.**

### 7.4 A between-vendor observation that converges with §6.4 on cost

Two vendors were scored on the same cases, one emitting about **two and a half times** the items of the
other (57 against 22 per run). The less verbose vendor is the model §6.4 manipulated, which also
emitted about 22 items per run at natural verbosity there.

**On raw recovery, the comparison sits against the ceiling.** Across all 47 cases, not only the
clean stratum, the more verbose vendor raised the seed in 92 of 94 runs and the other in 88 of 94
(0.98 against 0.94). Paired by case, the difference is 1.4 standard errors, and its 95% interval
runs from −0.02 to +0.10. That pooled figure is mostly ceiling: both vendors raised the seed in
every run of all 20 explicit-stratum cases, and all five cases where the vendors differed are in the
clean stratum. There the verbose vendor leads, 29 of 30 runs against 25 of 30 (0.97 against 0.83), a
difference whose interval runs from −0.06 to +0.33. So the more verbose vendor did not recover the
seed detectably better, on a measure with little room above it. Nor are the two shown to be
equivalent: where recovery is hardest, the interval allows the verbose vendor to be up to a third of
the scale better.

**On cost, the comparison is clear.** Yield (the share of a run's items that cleared the full
quality bar, as in §6.4) was **0.52 for the verbose vendor against 0.63**, paired over all 47 cases:
12 points lower, 8.2 standard errors from zero, with a 95% interval from −0.15 to −0.09. It was
lower in every leakage stratum, including the clean one, by 0.11.

This does not replicate §6.4. §6.4 manipulated one model, pushing it from 22 items to 56 on
instruction; this observes two different models at their natural verbosity, so volume is confounded
with everything else that differs between them. What it offers is convergence on cost: in both
designs, more items came with a smaller share worth keeping, here on a different corpus with a
human-authored seed. It offers no convergence on coverage, because neither design can detect a
coverage gain: §6.4's recall was at ceiling in every configuration, and raw recovery here is at
ceiling outside the clean stratum.

### 7.5 What this case does not establish

Three limits belong to the case itself:

- **The headline rests on the 15 clean-stratum cases of the 47 scored**, with a 95% interval of
  roughly **[0.33, 0.67]**, a third of the scale. The point estimate should not be quoted without
  it. **That interval covers case sampling only.** The scoring itself also varies: two scorings of
  the same runs disagree on individual verdicts (§9.1). No judge term for a single scoring
  configuration has been measured (§9.2), so no interval combining the two is reported, and [0.33,
  0.67] is narrower than the measure's full uncertainty by an amount that is not known.
- **Selection is inflationary.** A miss reaches an appellate holding because it was arguable,
  preserved, briefed and consequential. Seeds skew findable.
- **Nothing here detects a blind spot shared by the generator and every judge.** The appellate
  courts validate the *seed*; they never validate the judges.

### 7.6 What a larger corpus did to these numbers

Every figure in this case was re-derived when the corpus grew from the earlier corpus to the current
one (§7.1): 33 scored cases to 47, and the clean stratum from 9 cases to 15, with the same replicate
counts, models and settings, so the two are comparable. Four things came out of it, and they point
in different directions.

The run that grew the corpus also added two entries to the catalogue, both found in work that
otherwise succeeded. A screening run vanished, leaving no process and an empty log, which is what a
run that never started looks like. Checking the corpus files rather than the process showed that it
had done work (entry 20). By the commit message that recorded the run, it had screened 7 opinions and
extracted 2 before it died; the files were not committed in that state. And the study's own variance
tool reported on a corpus that no longer existed (entry 19, under the second point below).

**First, the headline moved, and its history shows how many things move a number that looks like one
measurement repeated.** The table gives the headline each pass of the study reported and committed,
one row per pass:

| pass | headline | cases scored (clean stratum) | scoring replicates | leakage-audit replicates | what changed from the pass before |
|---|---|---|---|---|---|
| 1 | 0.38 | 13 (4) | 2 | 2 | first pass |
| 2 | 0.55 | 25 (5) | 2 | 2 | the corpus grew, and the clean-stratum runs were scored a second time; the second scoring is the one reported |
| 3 | 0.50 | 34 (7) | 2 | 2 | the corpus grew; every earlier run's scoring carried over unchanged |
| 4 | 0.58 | 33 (9) | 4 | 5 | three changes at once: the leakage audit was re-run (10 of 34 cases changed stratum), the stimulus-validity gate then removed one case, and scoring replicates doubled |
| 5 | 0.50 | 47 (15) | 4 | 5 | the corpus grew by 15 cases, and the stimulus-validity gate removed one of them, *Occhipinti*, before any of its runs was scored; every earlier run's scoring carried over unchanged |

Five different things moved this number: corpus growth, a second scoring of the same runs, a re-run
leakage audit, the stimulus-validity gate §7.1 defines, and a change in scoring replicates.

Three rows need a note.

- **Pass 4 bundles three changes, and they pull in different directions.** Re-stratifying pass 3's
  scoring under the re-run audit and removing the gated case, *Eqbal*, together lift the figure from
  0.50 to 0.64. The gate supplies 0.06 to 0.08 of that, about half, depending on which change is
  applied first. Re-scoring at four replicates then brings it to 0.58. The 0.64 was never a pass's
  committed headline; the study's write-up gives it as the two-replicate side of §9.1's comparison.
- **Pass 3's 0.50 is entry 13's corrected value.** Inside that pass, two scorers raced on a shared
  file and the scorer's report first read 0.58; the race was caught, and the report regenerated at
  0.50, before the pass was committed. Pass 4's 0.58 is a different figure: the legitimate headline at four replicates, on a
  corpus without *Eqbal*.
- **Pass 2's 0.55 is that pass's second scoring of the same runs.** The first scoring read 0.50.
  Re-scoring the 20 clean-stratum runs at the same replicate count, with freshly drawn decoys
  (§9.1 explains why every re-scoring here draws new ones), agreed on 17 of 20 off-key verdicts.
  That is a direct reading of how much this number moves
  when the scoring is repeated. Both scorings are committed.

**The first three passes include a case the study later ruled invalid.** *Eqbal* sat in the clean
stratum in passes 1 to 3 and scored 0.00 off-key in every run; pass 4's re-run audit found that its
seed could not be raised from its case file at all (entry 15). Without it, those three passes would
read 0.50, 0.69 and 0.58. The last equals the raced 0.58 above for a reason: each drops, from the
same seven clean-stratum cases, a different case that scored 0.00 in all four runs. The exclusion
drops *Eqbal*; the race had mislabelled *Needham* out of the stratum.

The study pre-registered a floor: below 20 usable cases (cases scored, after screening and the
gate), a pass reports as underpowered. The study's write-ups from pass 2 on apply it to every scored case;
pass 1's applied it to the clean stratum, and pass 1, at 13 cases scored, is below the floor on
either reading. The pre-registration set no separate floor for the clean stratum, which has held
fewer than 20 cases in every pass, and 15 now; that is why §7.5 never gives the headline without its
interval. **Above the floor, four headlines span 0.08**, from 0.50 to 0.58; including the first pass,
whose headline was 0.375 before rounding, the spread is 0.21. Without *Eqbal*, the four above the floor span 0.19. On any of these readings, **the
level is not a quantity this instrument can report to two decimals**, and that is what this history
establishes.

It does not establish that the interval was reliable. All five readings do fall inside the current
interval, [0.33, 0.67]. That is a weak test, for four reasons. The readings come from nested
corpora, so they are not independent of one another. The current interval was computed from a corpus
that contains the data behind the earlier readings. It is a bootstrap over cases, so it models the
sampling of cases, which corpus growth changes, and none of the other things that moved them: the
second scoring, the re-run audit, the gate and the change in replicates.
And the containment depends on keeping *Eqbal*: without it, pass 2 would read 0.69, above the
interval. An unstable instrument would pass the same test. What the history does support is narrower
and still worth acting on: **quote the interval, never the level alone.** A project that reported only the
point estimate would have published four different values for one quantity across five passes.

**Second, the interval narrowed**, from roughly half the scale, [0.33, 0.81] on the earlier corpus's
clean stratum, to a third of it, [0.33, 0.67] on the current one. A bootstrap over cases has to
narrow when cases are added: at this growth it would have narrowed by about this much whatever the
scoring contributes. So the narrowing is not, by itself, evidence about where the variance lives.
§9.2 names what would be, and why it has not been run. Taken at face value, the variance tool first
showed no narrowing at all. Run after the new scoring, it read an archived scoring of the earlier
corpus by default, without naming the file, and reported that scoring's 9 cases, off-key 0.639 and
interval [0.39, 0.86], in the correct format and without complaint. Knowing that the clean stratum
now held 15 cases, against the 9 in the tool's header, caught it (entry 19). The tool now prints the
path of every input it reads.

**Third, the values across leakage strata moved, though not their order.** The earlier corpus's
0.58 / 0.61 / 0.75 became 0.50 / 0.65 / 0.71: the clean stratum fell eight points, the top stratum
four, and the spread widened from 0.17 to 0.21. That movement is part of why §7.3 does not report
the ordering as a separation. It is also where entry 14's gradient now stands. Pass 1 read 0.38 /
0.65 / 0.94, a spread of 0.56. Every reading under the re-run audit has been far shallower: 0.64 /
0.64 / 0.68 on the earlier corpus's k=2 scoring, and the two k=4 readings above. On none of the
three does the gap between the explicit and clean strata exclude zero.

**Fourth, one claim did not survive, and §7.2 corrects it.** Partial credit no longer recovers the
raw upper bound exactly. The correction came from re-running a number already in the study's own
write-up, after a run that had **succeeded**, and a successful run is the kind nobody re-reads.

---

## 8. What actually caught them

Alongside §4.2's seven shapes, this is the section a practitioner needs. In the twenty-three entries whose record says what
established the error, five mechanisms did most of the catching. Four entries (10, 11, 14 and 18) were caught by collecting
more — more cases, more scorings, or running the prediction — and are described where they appear
(§7.6, §9). Entry 21 was caught by reading it against the catalogue itself, which §8.3 describes.
Entry 6's record does not say what found it (§5).

### 8.1 The five mechanisms

*The order below is not a ranking of efficacy; §3.3 and §10.1 explain why this record cannot
supply one.*

**1. A second, differently-shaped pass over the same data.** Entry 12's falsification pass — different vendor, blind to provenance — struck 88% of what the first
pass claimed. The requirement is that the second pass be *differently shaped*, not merely
repeated: a second run of the same procedure is a replicate, which can expose wobble in a pass's verdicts
but not what that pass was shaped to miss.

**2. Comparing independent mechanisms for the same quantity.** How §6 was caught. Three
mechanisms agreeing would have been weak evidence; three mechanisms **disagreeing in three
directions** was decisive, and no single one of them was diagnosable alone.

**3. Inspecting what the number counted.** Unglamorous and repeatedly decisive. Entry 3's
control "failed" at 0.50; reading the four failures showed the judge was correct and the control
was measuring deduplication. Entry 7's lift dissolved on reading which taxonomy nodes had been counted as raised by generator B
alone (§6.2). Entry 19's variance figures were shown to be stale by reading the tool's header, which
said 9 cases, against a clean stratum known to hold 15 (§7.6). Entry 22's missing citation identifiers
were there once someone read the bibliography instead of the tool's summary of it (§2.7). Entry 23's
judge term turned out to count runs that had been scored only once when the two scorings behind it
were compared row by row, instead of through the flip rate the tool printed (§9.2). Entry 24 was found by
working out by hand what quantity the tool's judge-term conversion computes: √(p(1−p)/n) is not the standard deviation of one scoring's mean, which is √(p/2n). A case with a
known answer then confirmed the derivation. On 36 runs, 12 of them coin flips and 24 settled, that
standard deviation is 0.048 by direct calculation and in 40,000 simulated pairs of scorings, √(p/2n)
gives 0.048, and the tool's conversion gives 0.062. The same flip rate over the same number of runs
is the earlier corpus's k=4 budget, and there the right figure reverses the tool's verdict (§9.2).
Entry 20 is the
same move applied to a silence rather than a number: the corpus files, not the process table or the
empty log, showed that a run had done work (§7.6).

**4. A guard with a stated threshold.** Entry 15 was established by the seeded-miss study's
stimulus-validity gate, written into the design before any generator ran: a case is dropped when
most of the leakage audit's replicates judge its missed point impossible to raise from the case
file, and a tie keeps the case. Once the audit ran five replicates instead of two, the gate fired on
a case whose missed point could not be raised from its file at all, though the judge had credited it
as raised in every run (raw recovery 1.00): the judge had been crediting a near-miss (§4.3). The
rating behind the gate is a model's, but the gate applies its rule the same way every time, with no
one's reaction to a number involved, and that is what separates it from a person finding a number
implausible. Entry 6 has the same kind of guard, written after the fact: a **mechanical bound** that
flags any run covering more than 3× its own item count, added once the membership judge had credited
a 10-item list with 275 of 281 candidates by the guard's code comment (261 of 281 in the deviation
record; §6.2). From then on it shows that failure the same way
every time. It is not what established entry 6, and the record does not say what did (§5).

**5. Behaviour downstream failing to appear.** Entry 17's silent no-op edit was caught because
the change it should have produced never showed up later. It is slow, and it is the only one of
the five that caught entry 17.

### 8.2 What never caught anything on this record

- **Human plausibility judgment** — none of the twenty-three entries whose record says what
  established the error. Entry 6's record does not say what found it (§5).
- **Exit codes and success messages** — entry 16 is shape A one level down: the check measured
  *"the loop finished"*, not *"the work happened."* A broad `except`, added so one malformed
  input could not kill a long run, also swallowed quota exhaustion; the success message printed
  regardless of whether anything was fetched. Entry 20 is the same signal failing the other way: no
  process and an empty log read as a run that never started, when it had done work before it died.
- **"Does it parse?" as a proxy for "did it land?"** — entry 17. The fix was `assert old in s`
  on every string-replacing edit, which is the whole lesson.
- **A pooled figure compared across two scorings** — §9.1. Scorings of the same 132 runs at k=2
  and k=4 agreed within 0.01 on the pooled figure while disagreeing on 19% of run-level verdicts,
  and the clean-stratum figure §7 headlines moved from 0.64 to 0.58; compared at the pooled level,
  they would have looked interchangeable. Extra passes did help catch
  entries 14 and 18, but through comparisons finer than the pooled figure: across the leakage
  audit's levels for 14, verdict by verdict for 18.

### 8.3 What keeping the entries bought

Three of the project's later safeguards appear in the record, credited at three different
strengths. Records written at the time credit a two-sided decoy control specifically to the failure
recorded as entry 9, and a falsification pass to the list of failures already written down, which
held that failure. No record traces the third, a verbatim-quote requirement, to any entry. Laid out:

| what the record credits | safeguard | what that safeguard later did |
|---|---|---|
| entry 9 — a sanity test that could see error in one direction only | a two-sided decoy control | **had a hole found in it by entry 15** — clean on far-off decoys, blind to a near-miss |
| the list of failures already written down, entry 9's among them | a falsification pass, run by a different vendor blind to provenance | **caught entry 12** |
| no entry | a verbatim-quote requirement: the leakage audit — the pass that rates how plainly a case's facts give away the missed point — may rate a case *explicit*, giving it away outright, only by quoting at least eight words found in the case file; otherwise the rating is downgraded to *hinted* | no later catch recorded |

Of the two safeguards credited to failures written down, one caught a later entry and a later
entry found a hole in the other. Entry 12 is the clearest case: the pass that caught it was built
into the recount from the start, on the strength of the failures already written down. Entry 15 is
arguably the more useful one, because a safeguard the record then proved incomplete is exactly what
keeping the record is for.

The record has also done the catching directly, with no safeguard between it and the error. Entry 21
is a gate written in advance into a later study's design, deciding whether that study's primary
measure is reconsidered. Its record says both of the gate's defects were found by reading it against
the catalogue rather than against itself. For its reproducibility bar the counter-example was entry
18, already written down when the gate was written: the bar was stated on a pooled figure, and entry
18 is a pooled figure that agreed while the verdicts beneath it did not (§4.3). The amendment that
repaired the gate, written before the check ran, cites entry 18 by number, so this credit stands at
the same strength as the decoy control's: a record made at the time names the failure it rests on.

This is the argument for keeping a catalogue rather than only the fixes: **the entries are
reusable; the fixes are not.**

---

## 9. Three negatives worth their own statement

### 9.1 The pooled figure agreed while a fifth of the verdicts disagreed

The earlier corpus (33 cases scored, 132 runs) was scored twice, once at k=2 and once at k=4 scoring
replicates, to find out whether more replicates stabilise the measure. It is reported as a record of
that comparison and has not been re-run on the current corpus.

**The two scorings agreed on the pooled figure and disagreed on the verdicts.** The pooled figure,
over all 132 runs, moved by 0.01, from 0.66 to 0.67. That agreement was itself an average of
movements in opposite directions: the clean stratum, which carries §7's headline, fell from 0.64 to
0.58, the hinted stratum from 0.64 to 0.61, and the explicit stratum rose from 0.68 to 0.75. Run-level agreement on off-key was **0.81**: 25 of 132 individual
verdicts differed. Seventeen of 33 cases moved, two of them by 0.50, one in each direction.

**The trap is that the pooled figure looked reassuring.** Read at the pooled level, the two scorings
agreed and would have been filed as *"k=2 was fine all along."* The run-level comparison shows about
a fifth of the verdicts changing from one scoring to the next, **and the two readings are only
distinguishable because both scorings were kept.**

**What the comparison cannot say is how much of that disagreement doubling k would remove**, because
k was not the only thing that changed between the two scorings:

- **The tie threshold moved with k.** The scorer's majority vote counts a tie as yes, so at k=2 a
  verdict needs 1 vote of 2 and at k=4 it needs 2 of 4. The shift shows most plainly in raw
  recovery, which rests on one such vote: all three raw-recovery verdicts that differed went from
  yes at k=2 to no at k=4. Off-key rests on several, and they pull opposite ways. Whether items are
  rated sound, raised and material, and whether they cite the seed, count toward it; whether items
  are matched to the key or marked duplicate count against it. Its 25 differing verdicts split 12
  from yes to no and 13 from no to yes.
- **The decoys were redrawn.** The seed is judged in the same shuffled call as its decoys, and the
  two scorings used the same decoy draw in only 2 of 132 runs, so in the other 130 the seed judge
  saw a different set of considerations. That difference is not special to this pair. The scorer
  draws decoys from one seeded sequence that advances with each run it scores, over whatever cases
  the corpus holds at the time, so every re-scoring in this study redraws them: pass 2's re-scoring
  in §7.6 kept the draw in 0 of its 20 runs. Decoy context is part of what any repeat here measures,
  and what sets this pair apart from pass 2's repeat is k and its tie threshold.

So the 19% is the disagreement between two scoring configurations, not the instability of either
one. Separating them needs a second scoring at k=4, which was not run. The one repeat at a fixed k
on record is pass 2's re-scoring in §7.6, at k=2: 17 of 20 off-key verdicts agreed, too few runs to
tell apart from the 107 of 132 that agreed here. The familiar arithmetic, that majority-voting more
samples of a borderline call converges on a coin flip rather than on the truth, assumes a voter whose
threshold stays fixed as k grows. This scorer's threshold moves with k, so that arithmetic does not
describe it, and nothing here measured how this scorer's verdicts settle as k grows.

**Where the disagreement sits is still informative**, because all three measures were scored under
the same pair of configurations. Agreement was 0.98 on raw recovery (129 of 132 runs), 0.96 on
partial credit (50 of the 52 runs for which the k=2 scoring stored it), and 0.81 on off-key. Off-key
is the only one of the three that also depends on the matcher's decision to absorb an item into the
key, so the disagreement concentrates in the comparison layer around the seed judge. That is §2.3's
point, that a pipeline can fail in the machinery around a judge rather than in the judge, in this
paper's own data.

### 9.2 The variance in the sample was measured; the variance in the judge was not

**The study chose to add cases rather than scoring replicates on the strength of a judge term that did
not measure the judge** (catalogue entry 23). No judge term for a single scoring configuration has been measured, before
that choice or since.

The study's variance tool splits the headline's uncertainty into two terms. The **case term** is the
standard deviation of the stratum mean when cases are resampled (a bootstrap over cases). The
**judge term** is built from how often two scorings of the same runs disagree. The tool converts a
disagreement rate p over n runs into a standard deviation as √(p(1−p)/n). The quantity the case term
has to be set against is the standard deviation of one scoring's mean, which is √(p/2n): the chance
that two independent scorings of a run disagree is twice the variance of either scoring's verdict on
it. At the disagreement rates below, the tool's conversion is 30 to 35% too large (catalogue entry 24).
The budgets for
the clean stratum give both:

```
earlier corpus, 9 clean cases, k=4 scoring:
    case sampling                      sd 0.118    95% interval [0.33, 0.81]
    k=2 against k=4 disagreement       6 of 36 clean-stratum runs (rate 0.167)
                                       sd 0.062 as the tool converts it, 0.048 as √(p/2n)

earlier corpus, 9 clean cases, k=2 scoring (the budget the study acted on):
    case sampling                      sd 0.119    95% interval [0.39, 0.86]
    k=2 against pass 2's first scoring 3 of 28 runs (rate 0.107); 12 of the 28 scored once
                                       sd 0.058 as the tool converts it, 0.044 as √(p/2n)

current corpus, 15 clean cases, k=4 scoring:
    case sampling                      sd 0.085    95% interval [0.33, 0.67]
    judge sampling                     not computed -- see below
```

**The case term is sound, and it is large.** On the current corpus its interval spans a third of the
scale.

**Neither judge figure the tool has produced is a judge term for one configuration:**

- **The k=4 figure** pairs the k=2 and k=4 scorings §9.1 compares. Those differed in replicate count
  and tie threshold, so the figure measures the disagreement between two configurations, not the
  variation of either.
- **The k=2 figure** pairs the earlier corpus's k=2 scoring with pass 2's first scoring (§7.6), read
  under the re-run leakage audit, whose clean stratum holds 28 of pass 2's runs. Sixteen of them are
  runs pass 2 scored a second time: four of the five cases §7.6's re-scoring covered, with *Eqbal*
  gated out. Those are the right kind of pair, and 3 of the 16 flipped, the same three §7.6 counts.
  The other 12 come from three cases the earlier audit had placed outside the clean stratum, so pass
  2 scored them once and both files carry that one scoring. They agreed by construction and pulled
  the rate down to 3 of 28.

That matters because the k=2 budget directed the study's next step. The tool's rule for calling one
term dominant is that one standard deviation be at least twice the other; it read 0.119 against
0.058 as case sampling dominating, and the study's resume plan gave that budget as its reason for
adding cases rather than replicates. The budget could not show that. The conversion is not what
undermines it: converted as √(p/2n), both pairings clear the rule, 0.119 against 0.044 and 0.118
against 0.048 (the tool's own conversion had put the k=4 pairing below it). What undermines it is
that one judge figure is between two configurations and the other counts 12 runs agreeing with
themselves. Adding cases did narrow the case term, as it had to; which lever was the bigger one has
not been measured.

The expansion to 15 cases does not test the split either, though it is tempting to read it as one. A
bootstrap over cases narrows when cases are added, whatever the judge contributes, and it narrowed
by about as much as that arithmetic predicts. The test is a second, independent scoring of the
current corpus's runs under the same configuration as the first, with its disagreement converted as
√(p/2n). Like every re-scoring in this study, it would draw fresh decoys unless the harness is
changed to hold the draw fixed (§9.1).

**That is why no judge term is computed at 15 cases.** No such second scoring exists. The archived
scorings that do exist were produced under other configurations, and pairing one with the current
scoring would repeat the k=4 figure's problem. The tool no longer supplies a second scoring by
default, and without one it skips the judge term. So **every interval quoted for this measure,
§7.5's and §7.6's included, is the case term alone.**

A profiling pass asked whether anything predicts *which* cases recover, so that expansion could be
targeted. It ran on the earlier corpus's k=2 scoring and found nothing it read as a difference: the study's
write-up reported high- and low-recovery cases matched on items emitted, off-key pool, key size,
recall and seed length, and on raw recovery (1.00 against 0.97). The profile also printed situation
length, which already differed by about a fifth, and the write-up did not list it. **That reading
belonged to one scoring, not to the corpus.** On the k=4 scoring of the same corpus the groups
already differ on raw recovery (1.00 against 0.86), and on the current corpus they still do: 0.99 in
the 25 high-recovery cases (off-key 0.75 or above) against 0.86 in the 11 low ones (0.25 or below).
Cases at exactly 0.50 fall in neither group. Part of that gap is built in, because a run cannot
count off-key a seed it never raised, so no case in the high group can sit below 0.75 raw. The
off-key pool now differs by about a fifth as well (it differed by an eighth on the k=2 scoring),
situation length still does, and the low group holds proportionally almost twice as many clean-stratum cases (5 of 11 against 6 of 25). With 25 cases
against 11, the comparison no longer supports "matched" and is too small to establish a difference.

The absorption account still explains most of the low group. Seven of its 11 cases raised the seed
in every run, and 85% of its shortfall below full off-key recovery is seeds raised and not counted.
What no longer holds is that the low group raised the seed *just as reliably*. The study itself never
re-ran the profile on the k=4 scoring or the current corpus, because its profiling tool read the k=2
scoring by default. The figures above come from re-running the full profile for this paper, after
that default was corrected.

### 9.3 A refuted prediction, and why it is in the paper

The project predicted, in writing, that the **parent study's** numbers — the coverage study §6
draws on — were **substantially understated** by the same exclusive-match defect described in §7.2. The recount was run: the
correction is **+0.00 to +0.08, median +0.04** across the recount's eleven generator arms (+0.03
if the two arms that ran the structured walk on a deliberately degraded taxonomy are counted too).
The prediction was **refuted** and the parent
study's published numbers stand.

The transferable part is *why* the same defect is severe in one place and negligible in the
other. §7's measure is **targeted** — "does any item address this one seed?" — so a single
absorbed item destroys a binary signal. The parent measure is a **rate over the 9–56 items a run
typically emitted**, where absorbing a handful moves it by a few points.

> **The damage a broken rule does scales with how concentrated the measure is. A broken rule
> does not make every number computed with it wrong.**

This entry is in the catalogue because a project that only records the failures it *finds in
others'* work, or only the predictions that came true, is running the same selection bias the
catalogue exists to document.

---

## 10. Limitations

### 10.1 The survivorship problem

**This catalogue records instrument failures that were caught. It cannot say anything about the
rate of failures that were not caught, and by construction it never will.**

**§5 and §8 must both be read through that**, and they are affected differently.

For §5, the selection is less damaging than it first looks. A failure caught by someone finding a
number implausible would be **in** this collection, because catching is how an entry gets in and the
catching mechanism is a recorded field. So the population plausibility would have caught is not
invisible here; it is the one population the collection could see, and in none of the twenty-three
entries whose record says what established the error did it do so. The blind spot is narrower and
sharper than survivorship usually implies: failures caught by **nothing**, which §10.2 names. Two
real limits apply. The catching field records the check that *established* an error, not what
prompted someone to run it. And for entry 6 the record names neither: the guard it lists was written
after the error had been diagnosed, so what established the error is not recorded, and it could have
been a person finding a number too high (§5).

For §8, the same selection cuts the other way. A mechanism that catches more will appear more often
partly because catching is the inclusion rule, so **the order of §8.1 says nothing about which
mechanism works best.**

The sharper version of the worry is the one we cannot answer: **failures caught by nothing at
all leave no trace**, and the catalogue's most likely systematic gap is exactly the class of
error our five catching mechanisms are shaped to miss. §10.2 names the one we know of.

### 10.2 Shared blind spots are undetectable by everything here

Where the generator and every judge are blind together, all of these instruments read clean —
and clean reads as good coverage. Every judging, matching and auditing pass in this paper is a model
checking a model. The human-authored elements in the material are the examiners' answer key behind
§6 and the appellate courts behind §7. Both fix what the instruments look for: the **key points**
and the **seed**. Both also check a judge, but only on what they name. The key served as a positive
control on §6's blind judge, which had to rate at least one covering item sound, raised and material
for at least 90% of key points; seeds drawn from other cases are the decoys in §7's control on the
seed judge. Nothing human-authored checks a judge on anything it does not name, and that is where a
shared blind spot sits.

We regard this as the important open problem, and none of the seven shapes addresses it.

### 10.3 One project, one team, twenty-four entries

The sample is not random, not independent, and not large. The entries share a stack, a set of
habits, and in most cases the same author. A different team would likely surface shapes we do not
have — and would likely be blind to different ones. **Seven shapes describing twenty-four entries
is a starting taxonomy offered for reuse, not a validated classification.**

### 10.4 The project constraint that shaped the material

The programme these pilots come from operates under a standing constraint of **no live human
evaluation**. That is a real limitation on the underlying work and it propagates here: it is
why §10.2 has no remedy on offer, and why the appellate-opinion corpus in §7 — human-authored,
post-cutoff, and independent of the model ecosystem — was worth the considerable cost of
building.

---

## 11. What we would do differently

Offered as practice, at the confidence level §10 supports.

1. **Never let a single mechanism answer an ambiguous question.** If a measurement requires
   deciding whether two things are "the same," build two mechanisms of different shape and
   compare them. If they disagree, the quantity may be ill-posed rather than hard — and then the
   remedy is to decide the question the design left open and report that as a convention, not a
   result (§6.3).
2. **Make every control two-sided.** A control that can only detect error in one direction will
   pass while the instrument it guards is broken (entry 9). State, in writing, which direction
   of failure the control cannot see.
3. **Ask what your control's decoys are near.** Far-off decoys test far-off generosity and
   nothing else. A clean far-off control does not license "the judge is not generous"
   (entry 15).
4. **Write mechanical bounds, not intuitions.** A written bound, such as "flag any run covering more
   than 3× its own item count", fires the same way on every run, whoever reads the output. This
   project wrote that one in response to a judge crediting a 10-item run with covering 275 of 281
   candidates, so that the next reading like it is flagged rather than left for someone to notice. Of
   the 23 entries whose record says what established the error, none was established by someone
   finding the number implausible (§5).
5. **Compare run-level, not pooled, when comparing two scorings.** Two scoring configurations whose
   pooled figures agreed within 0.01 disagreed on nearly a fifth of individual verdicts, and moved
   the clean-stratum headline from 0.64 to 0.58 (§9.1). Only keeping both scorings showed it.
6. **Assert that your edits landed.** `assert old in s`. A tool that reports success because nothing
   threw is measuring the wrong thing (entries 16, 17).
7. **Budget your variance, and check what each term was computed from and how it was converted.**
   The budget that sent this study to add cases rather than replicates read a case sd of 0.119
   against a judge figure of 0.058, on the earlier corpus's clean stratum under its k=2 scoring. That
   judge figure counted 12 runs that had been scored only once as agreeing with themselves, and the
   tool turned its disagreement rate into a standard deviation about a third larger than the one the
   case term is compared with. No judge term for a single scoring configuration has been measured
   since (§9.2; entries 23, 24).
8. **Keep the failures.** Write down what the number said, what it turned out to be, and how that
   was caught. The third field is what makes the record reusable, and it is the easiest one to leave
   out.
9. **Re-validate after a repair.** A fixed instrument is a new instrument. §7.3's corrected rule
   answered the validation question and, sitting near its ceiling, lost most of its room to
   compare two generator setups. That was invisible until it was checked.
10. **Quote the interval, never the level alone, and say what the interval leaves out.** §7's headline read
   four different values across five passes of one study (§7.6), each computed correctly on the
   corpus it had, three of them on a corpus that still held a case the study's own gate later
   removed. The level is not reportable to two decimals. And the interval quoted beside it covers
   only the sampling of cases, one of the five things that moved it (§7.6, §9.2).
11. **Make every analysis tool name what it read, and tell "absent" from "not read".** A variance
   tool that defaulted to an archived scoring reported a corpus that no longer existed, in the right
   format and without complaint (entry 19); had its header printed the path it read, the error would
   have shown at once, and it now does. A citation tool that read an entry's DOI field but not its
   arXiv fields reported two arXiv identifiers absent, and its report turned that into an action item for work already
   done (entry 22). A record whose fields a tool did not read should be reported differently from a
   record that has none.

---

## 12. Data and code availability

<!-- DEPOSIT GATE (pre-deposit-checks-2026-09-16.md): every item this section names must be
     present in the public archive before this paper is deposited. On 2026-09-16 none of it was:
     the public repository held only the Resolver paper's materials. -->

The work reported here was done in the author's working repository, which is private. The
materials below are deposited with this paper in the public archive named at the end of this
section. Paths are the working repository's, and the archive keeps the same layout. In the archive's copies
only, ten scripts read API keys from environment variables instead of a machine-specific key file;
the archive's provenance list names each change, and no analysis logic differs.

**The catalogue.** The standing, append-only catalogue (`docs/findings/instrument-failure-catalogue.md`)
is condensed as Appendix A and deposited in full, as it stood at twenty-four entries. It continues
to be appended in the working repository; the deposited copy is the one this paper reports.

**The seeded-miss study (§7)**, `pilots/seeded-miss-2026-08-29/`: its design note, which fixed the
analysis decisions in advance; its deviation ledger; its write-ups; the scripts that fetch,
screen, generate and score, and the variance and profiling tools §9.2 discusses; the corpus exactly
as handed to the generators, with the screening and leakage-audit records beside it; all 196
generator run outputs, including the eight belonging to the two cases the stimulus-validity gate
removed; and the current scoring. The cached opinion text is not included, for size; US judicial
opinions are public domain, and the fetch script rebuilds the cache from CourtListener. The design
note states that it was written before any data was pulled. It was first committed together with
the initial corpus, so that ordering rests on the note's own record, and on the deviation ledger,
which dates each departure and says what data existed when it was made, rather than on a separate
timestamp.

**Every scoring this paper draws on, including the superseded ones.** The working repository holds
the scorings behind passes 1 to 4 of §7.6, including the k=2 scoring behind §9.1's replicate
comparison, only in its version history. They are deposited as files, each with the leakage audit it
was read under. So are the three archived scorings kept in the study's `attic/` folder: the k=2
scoring again, with its rows re-labelled under the re-run leakage audit; the pre-correction state
behind entry 13; and the first scoring behind pass 2's 0.50 → 0.55 re-scoring. A provenance list
gives the commit and date each deposited file comes from, since the files themselves carry neither.

**The coverage study (§6)**, `pilots/coverage-residual-validation-2026-08-29/`: its design note,
which records what the study expected before its data (it was declared exploratory, and is not a
pre-registration); its deviation ledger; its write-ups; its scripts; and its run outputs, including
the recount's behind §9.3. Its exam questions and model analyses are the National Conference of Bar
Examiners' copyright and are not redistributed: every run output carries a placeholder where the
fact pattern was, and the scripts rebuild the corpus from NCBE's published materials. What was
derived from those materials, including the structured answer key that each run output also
carries, is deposited only as far as NCBE's terms allow, and anything withheld is listed in the
archive's README.

**Shared code.** The scripts of both studies import one model-calling helper from an earlier study
in the same project. It is already public, unchanged, in the Resolver paper's archive, and a copy is
deposited here. Re-running any model pass needs the reader's own vendor API keys; re-deriving a
figure from the deposited scorings calls no model.

**What re-derives, and from what.** The measured figures in §7 and §9 re-derive from the deposited
data: §7 and §9.1–9.2 from the seeded-miss study's scorings, and §9.3 from the recount's outputs under
`pilots/coverage-residual-validation-2026-08-29/runs/`. Some figures were computed for this paper in
review rather than by the studies' own scripts, among them §7.3's between-stratum intervals and power
estimate, §7.4's paired vendor comparisons, and the simulation behind entry 24. The code for those is
not part of the deposit; each passage states its method, and the data it was applied to are
deposited. One figure rests on part of a scoring: §9.1's partial-credit agreement, 50 of 52 runs
(0.96), is taken over the 52 of the 132 runs for which the k=2 scoring stored partial credit.

*(Archive DOI and public repository URL to be inserted at deposit. This paper must be
published, and its DOI verified resolving, before the companion Proposer paper cites it.)*

---

## 13. Generative-AI use and author responsibility

This paper reports work in which AI systems are both the subject and the instrument, so the
disclosure matters more than usual.

Every instrument described was implemented with AI assistance, and the judging, matching and
auditing passes in both case studies were performed by large language models across two
vendors. **Several of the twenty-four entries are failures in AI-authored analysis code, and at
least two (entries 16, 17) are failures in the AI-assisted tooling used to conduct the work
itself.** The drafting of this paper was AI-assisted.

The author reviewed and is responsible for all claims. Numbers in the body were taken from
committed run outputs and write-ups, not restated from memory. Independent review of the draft
then re-derived the figures in §7, §9.1 and §9.2 from committed run outputs, including earlier
scorings recovered from the working repository's history and the archived scorings kept beside the
study, all of them deposited (§12), and §9.3's recount figures were re-derived from that study's committed outputs during
revision. Figures that did not reproduce were corrected to what the committed data give. One figure
rests on part of a scoring: §9.1's 0.96 agreement on partial credit covers the 52 of 132 runs for
which the k=2 scoring stored partial credit (§12).

---

## Appendix A — the twenty-four entries

*Condensed from the standing catalogue, which is the record. `shape` refers to §4.2.*

### From the coverage study (1–9)

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 1 | C | weighted recall **0.00** | recall was 1.00 | key ids did not round-trip (`1(a)` vs `(1)(a)`) |
| 2 | A | a **consensus** clustering | one clustering; threshold 0.5 returns it unchanged | replicate-count check |
| 3 | A | control **FAIL at 0.50** | judge was correct; the control measured deduplication | inspecting the four "failures" |
| 4 | B | cross-vendor lift **+0.130, SUBSTANTIAL** | two different quantities averaged into one number: the tool's first version averaged what the second vendor added with what it lacked, into 0.304, and printed the result as a lift of +0.130. That run's clustering was not saved, so its figures cannot be re-checked. On the saved, corrected run the two directions read 0.038 and 0.553, and the added direction against the floor is −0.114, itself partly a volume artifact; an exploratory re-run on the same exam question with output volume matched gave **+0.008**, a null | the pool shape: B-only clusters a small fraction of A-only. The saved clustering reads 5 against 37; the study's narrative gives 4 against 40 for the first run, whose clustering was not saved |
| 5 | C | structured novelty **+0.305** | vocabulary mismatch, not novelty | the "novel" set contained the 30%- and 35%-weighted key points |
| 6 | D | a 10-item list covering **261 of 281** | membership judge over-merging | not recorded. The plausibility guard on covers/own ratio was written in response, after the over-merge (275 of 281 by the guard's code comment) had been named and a tightened prompt had barely moved it (§5) |
| 7 | C | projection lift **+0.207** | a filing artifact: both sides raised the doctrine, and the taxonomy filed it under two headings | inspecting which nodes were "B-only" |
| 8 | A | positive control **0.43** | the control was confounded with recall | control tracked recall to ±0.08 |
| 9 | A | a sanity test **passing** | the instrument it guarded was broken | it could only detect failure in one direction |

### From the seeded-miss study and the recount (10–15)

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 10 | E + G | first-instance tribunals recover far better, **0.90 vs 0.50**, with a ready mechanism | the **sign does not hold**. Four scorings of the same design: 0.90/0.50, 0.66/0.61, **0.62/0.73** — reversed — then 0.61/0.66 | more data, then more scorings. Labelled exploratory *when it looked strongest*, which is the only reason it is a footnote |
| 11 | E | (a prediction) the parent study's off-key rates are **understated** | correction is **+0.00 to +0.08**, median +0.04 | running it (§9.3) |
| 12 | D | a "material beyond the key" pass claimed **18.4 items/run** | **88% struck** by a blind, different-vendor pass | the falsification pass, built in from the start because of the catalogue as it then stood |
| 13 | F | headline off-key **0.58** | **0.50** | two scorers raced on a shared file; 8 rows kept a label from the other scorer's audit. Caught by cross-checking each row's stamp against the file of record |
| 14 | G | a monotonic leakage gradient **0.38 / 0.65 / 0.94**, cited as the audit self-validating | **0.64 / 0.64 / 0.68** on the grown corpus with the audit at k=5; later scorings read 0.58 / 0.61 / 0.75 and 0.50 / 0.65 / 0.71, and none has told the levels apart | raising the audit from k=2 to k=5, on the grown corpus; 10 of 34 cases changed stratum, and the stimulus-validity gate it fired removed one case |
| 15 | D | raw recovery **1.00** on one case | the seed was **not raisable from that case file at all** | the stimulus-validity gate, once the audit was reliable enough to fire it |

### From the tooling (16–17), and the replicate comparison (18)

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 16 | A | a corpus pull **completing** — count printed, exit 0 | the daily API quota was exhausted on the first request; every candidate failed in turn | reading the output. A broad `except` swallowed quota exhaustion and the success message printed regardless |
| 17 | F | an edit **applied** — file parsed, no error | a string-replace silently matched nothing | the behaviour it should have produced never appeared. `assert old in s` was the fix |
| 18 | G | doubling replicates (k=2 → k=4) would **stabilise** the measure — the premise the rescore was launched on | the two scorings of the same 132 runs agreed within 0.01 on the pooled figure and **disagreed on 19% of run-level verdicts** (25 of 132), while the clean-stratum headline moved from 0.64 to 0.58. They also differed in tie threshold and decoy draws, so how much doubling k itself would remove was not measured | scoring the same runs twice and comparing run by run, rather than comparing pooled figures — which agreed |

### From the corpus-expansion run (19–20), 2026-08-30

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 19 | F | the variance budget after a new scoring: **9 cases, 36 runs, off-key 0.639, 95% interval [0.39, 0.86]** — correctly formatted and internally consistent | the clean stratum had just grown to **15 cases / 60 runs at 0.500**, interval **[0.33, 0.67]**. The tool's default input was an archived scoring, and it did not name the file it read. Taken at face value, the interval had not narrowed from 0.47 wide, when it was 0.33 wide | knowing the clean stratum held 15 cases and seeing the header say 9: a mismatch against a known fact, **not** the number looking implausible. The tool now prints every input path |
| 20 | A | a screening run that had **vanished** — no process, a **0-byte log**, no error — observationally identical to "never started" | it had screened **7 opinions and extracted 2** before dying. Python buffers output when it is not writing to a terminal, and the buffer died with the process | checking the corpus files rather than the process: `screen.json` had moved 102 → 109 and `cases.json` 34 → 36. No file state in between was committed: the files are committed only before the run (102, 34) and after the relaunch completed (163, 49). The 7 and 2 rest on the commit message that recorded the run, and 109 and 36 on the catalogue entry written the same night |

### From the programme's own governance (21), 2026-09-16

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 21 | A | a **reopening condition** for a later study's primary measure: two bars, "precision" and "reproducibility", each with a number attached | **neither bar measured what its name said.** By the record, the precision bar was the interval of the seeded-miss *recovery* headline, whether one planted missed point was recovered, while the hypothesis it gates is about how much *off-key material* a generator emits; the project's instrument register lists those as two measures. The reproducibility bar was stated on a **pooled** figure, and entry 18 had shown a pooled figure agreeing within 0.01 while 19% of run-level verdicts disagreed. The gate had not yet run | reading the gate against the catalogue rather than against itself; entry 18, already written down, was the counter-example to the reproducibility bar. Amended before the check ran, with the superseded text kept |

### From this paper's own citation gate (22), 2026-09-16

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 22 | A | two citations carrying **no identifier at all** (`not-checkable`), with adding identifiers as the recommended action | **both carried a correct arXiv id**, and had since 2026-08-30, six days before that report. The tool's bibliography join read `doi` but not `eprint` / `archivePrefix`, then reported the ids absent | reading `refs.bib` directly instead of the tool's summary of it |

### From this paper's own review of its variance figures (23–24), 2026-09-16

| # | shape | it reported | it was | how it was caught |
|---|---|---|---|---|
| 23 | A | a **judge term** at k=2, case sd 0.119 against judge sd **0.058**, read as "case selection dominates about 2:1" and used to redirect effort to adding cases | not two independent scorings of the same runs. Of the 28 clean-stratum runs the two files shared, **12 were the same scoring** (identical but for a restamped stratum label), and all 3 flips fell among the other 16. The k=4 judge term paired two different configurations. **No judge term for a single configuration was ever measured** | diffing the two archived scorings row by row, rather than reading the flip rate the tool printed (§9.2) |
| 24 | A | the tool's judge term, "implied sd of the stratum mean", **0.062** at k=4, and its verdict **COMPARABLE** (case 0.118 < 2 × 0.062) | the tool converts a disagreement rate p as √(p(1−p)/n), but the sd of one scoring's mean it implies is √(p/2n): **0.048**. Against that, 0.118 **clears** the tool's own 2× rule, so the verdict reverses. The tool's figure is about 30% too large | deriving the conversion by hand and checking it against a case with a known answer — 36 runs, 12 coin flips and 24 settled: 0.048 directly and in 40,000 simulated pairs, 0.062 by the tool's formula — in this paper's own review (§9.2) |

---

## Appendix B — what entries 14 and 15 cost

**Entry 14 removed an argument, not just a number.** The monotonic gradient, 0.38 / 0.65 / 0.94, was
the evidence cited for the leakage audit measuring something real. With a more reliable audit that
0.56-point spread shrank to between 0.04 and 0.21: 0.64 / 0.64 / 0.68 on the earlier corpus's k=2
scoring, 0.58 / 0.61 / 0.75 on its k=4 scoring, and 0.50 / 0.65 / 0.71 on the current corpus. On
none of those readings does the gap between the explicit and clean strata exclude zero, so that
self-validation is **withdrawn**. When this entry was recorded, the pre-registered decision to
headline the clean stratum bought little: 0.64 clean against 0.66 pooled, at two scoring replicates
on the earlier corpus. **On the current corpus the two sit thirteen points apart, 0.50 against
0.63.** So the choice of stratum now moves the headline materially, on a stratification whose
self-validation this entry withdrew. That is a worse position for the methodology than the one first
recorded.

**Entry 15 exposed a hole in the study's own best control**, described in §4.3 and §7.1. The
stimulus-validity gate has now removed two cases (§7.1); this is the one in which the judge was observed
crediting a near-miss, and it was invisible to the control that exists to catch exactly that
failure. The other, *People v. Occhipinti*, was removed at its first audit, before any of its runs
was scored, so whether the judge would have credited a near-miss there is not known. Its missed
point is the defendant's age and medical conditions as mitigating factors, which its case file never
mentions. Each of its four runs does carry a general item on considering mitigating factors, and
one lists age and medical issues among its examples: the kind of adjacent item the judge credited on
*Eqbal*. That is a reading of the runs, not a judge's verdict. The control's own applicable-decoy cell, read case by case against the case files, holds
two more credits of the same kind (§7.1). They were found by reading the decoys, not by the
control's verdict, which stayed clean.
