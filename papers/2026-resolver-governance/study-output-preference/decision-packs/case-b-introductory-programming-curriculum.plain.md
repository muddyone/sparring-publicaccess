<!--
Plain-language rater-facing pack for V2 Case B (WORKING DRAFT, pending the
plain-pack pre-reg amendment + condition re-run). Rebuilt from the locked
case-b-introductory-programming-curriculum.md: every fact, citation, number, and
replication caveat preserved; academic register dropped per the 2026-06-04
readability decision; jargon glossed once on first use; no facts added; the
"what this is testing" meta (which names C3/C5b targets) deliberately excluded so
it never reaches the rater. This is the text fed to the regenerated conditions
only. The rater does NOT read this full pack — the rater sees the condensed
`rd_eval_cases` fields (`question` + `evidence_summary`, rendered by
blind-rating.php), which are maintained separately and were given their own
stakes-legibility clarity pass in the 2026-06-14 amendment.
-->

## The situation

Northern Coastal Community College (NCCC) is a public two-year college in the Pacific Northwest serving about 6,400 students a year, of whom roughly 1,100 take at least one computer-science course. The CS department is redesigning its long-running **CS101: Introduction to Programming** for the 2026-27 school year. The redesign has been in committee for 14 months and must reach a decision on how the course is built by June 30, 2026, to leave time for syllabus, materials, and instructor prep before enrollment opens August 1, 2026.

**About the course:**
- 16-week semester, 3 hours/week of lecture plus a required 2 hours/week of lab.
- About 8 sections in fall, 6 in spring, ~28 students each — roughly 390 students a year.
- About 62% take CS101 as a general-education elective, not as the start of a CS major. Of the 38% who continue, about half eventually transfer to a four-year CS program.
- Python has been the teaching language since 2018 (before that, Java).
- The department has 4 full-time CS faculty plus 6–8 adjuncts each semester.

**Who the students are:**
- ~57% are adult learners (age 22+, with prior work experience).
- ~31% are first-generation college students.
- ~20% speak English as a second language.
- Over the last three years: about 73% finish the course (the department treats anything under 75% as a concern). Of those who finish, the average final-exam score is 78% and the median is 82%.

**The two ways to build the course:**

- **Path A — "Concepts first."** The first 5 weeks teach the thinking behind programming — how to break a problem into steps, basic ways to organize data (like lists and dictionaries), how the order of steps is controlled, and rough reasoning about how much work a solution takes — all using plain-English-style step sketches (pseudocode) and diagrams, with no actual code yet. Python is introduced in week 6 as the tool to implement those ideas; the remaining 10 weeks mix concepts with Python practice. Programming projects start in week 8.
- **Path B — "Language first."** The first 5 weeks teach Python itself — variables, types, expressions, loops, functions, and the basics of lists and dictionaries — with small programs students can run and tinker with right away. The deeper thinking (breaking down problems, organizing data) emerges from coding practice in weeks 6–12. Larger programming projects run in weeks 10–16.

**The decision:** Which path better serves the course's goals — especially the stated goal that "students will understand programming as a discipline, not just one language" — and what are the trade-offs in how many students finish, how well they're prepared if they transfer to a four-year program, and how accessible the course is to the 57% adult-learner / 31% first-generation / 20% second-language student body?

## What we know (the evidence)

Six things the decision can draw on:

1. **How much mental load learners can carry at once.** Sweller, van Merriënboer & Paas (1998, "Cognitive Architecture and Instructional Design," *Educational Psychology Review* 10(3), 251–296) showed that hitting learners with two hard new things at the same time — a new way of thinking *and* a new notation to write it in — produces measurably worse learning than teaching them one at a time. Applied to CS101: teaching the ideas first in plain sketches and diagrams, before adding Python's syntax, should lower the total load while students are first forming the concepts. This is the theory-based case for Path A.

2. **What actually drives whether students finish.** Bennedsen & Caspersen (2007, "Failure rates in introductory programming," *ACM SIGCSE Bulletin* 39(2), 32–36) reviewed 63 intro-programming courses across many schools and design choices. Their key finding: how many students finished depended far more on *student preparation* and *which language* was taught than on *concepts-first vs. language-first ordering*. Completion rates ranged 65–78% across course designs, but 58–85% across language choices. Ordering by itself did not predict differences in completion.

3. **How adults learn best.** Knowles (1980, *The Modern Practice of Adult Education*) and the later research on adult learners (e.g., Cercone 2008) find that adults are motivated by early, concrete competence — "I can already do something useful." Path B's "by week 3 you've written a working program" milestone fits that. Path A's "weeks 1–5 are sketches and diagrams, you haven't run code yet" may cause adult learners specifically to lose motivation earlier — even though the mental-load research (point 1) favors Path A for actually remembering the concepts.

4. **First-generation and second-language students.** Hatfield, Williams, et al. (2019, "First-Generation Students in Introductory Computer Science," *Computer Science Education* 29(4), 412–431) found that first-generation and second-language students did about as well as their peers on concept exams, but consistently about 12 percentage points lower on open-ended tasks where they had to write code from scratch. The authors' proposed reason: those tasks demand three things at once — the concept, the syntax, and an unspoken sense of what a "good" solution is expected to look like. The implication: Path B's earlier focus on syntax fluency may narrow that gap for these students, while Path A's later start on coding may leave it in place. **Note on how solid this finding is:** it held up in two of three later studies but failed to replicate in Lewis et al. (2022).

5. **How students do after transferring to a four-year program.** Two large studies of community-college-to-four-year CS transfers — Smith & Garcia (2021, *Journal of College Student Transfer*) and Park et al. (2023, *Computer Science Education*) — both found that students who came from a concepts-first community-college intro course did slightly better in their four-year data-structures-and-algorithms course (a small effect: Cohen's d ≈ 0.18 in Smith & Garcia, ≈ 0.22 in Park et al. — about 3–4 percentage points on course finals). But this edge showed up only for students who took data structures within their first 18 months at the four-year school; for those who took it later, there was no measurable difference tied to how their intro course was built.

6. **NCCC's own history.** The 2018 switch from Java to Python was a *language* change, not a path change (the course was language-first both before and after). Completion jumped from 64% to 71% in the first year and settled at about 73% by year three. The faculty's after-the-fact review credited this partly to Python being easier to write correctly (especially for adult learners) and partly to it being familiar from the media ("I've heard of Python"). There is no internal data on what a switch to Path A would have done, because NCCC has never run Path A.

## The question to answer

Which path — Path A (concepts first) or Path B (language first) — should NCCC adopt for the 2026-27 CS101 redesign, and why? What trade-offs does the chosen path NOT solve? Are there hybrid versions of either path that would better serve NCCC's specific students and goals?

Your answer should include:

- A specific choice (Path A, Path B, or a justified hybrid).
- Clear reasoning grounded in the evidence above (and any other evidence you can cite).
- An honest statement of the trade-offs your choice does NOT solve.
- A specific look at the 57% adult-learner / 31% first-generation / 20% second-language students, and how your chosen path serves (or fails) each group.
- A specific look at the 38% who continue past the course (where preparation for transfer matters most) and the 62% who don't (where finishing the course and its general value matter most).

Keep in mind the June 30, 2026 deadline, the 4-full-time / 6–8-adjunct staffing, and the existing commitment to Python as the teaching language.
