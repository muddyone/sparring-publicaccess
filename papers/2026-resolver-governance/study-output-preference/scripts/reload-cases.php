<?php
/**
 * Plain-pack re-run loader. Updates rd_eval_cases (resourceforge sparring DB)
 * with the plain rater-facing question/evidence_summary + the regenerated
 * answers, under a fresh X/Y assignment. Backs up the prior rows first.
 *
 * Run ON the VPS from the resourceforge clone context. Answer files expected in
 * /tmp/v2reload/. Pre-rater-data only (refuses if any rating exists).
 */
require '/home/[redacted-user]/public_html/resourceforge.com/sparring/vendor/autoload.php';
\Lifspel\Services\EnvLoader::load();
$config = require '/home/[redacted-user]/public_html/resourceforge.com/sparring/src/config/config.php';
$db = \Lifspel\Services\Database::getConnection($config);

// Safety: refuse if any rating exists (must stay pre-rater-data).
$n = (int)$db->query("SELECT COUNT(*) FROM rd_eval_ratings")->fetchColumn();
if ($n > 0) { fwrite(STDERR, "ABORT: $n ratings exist; not reloading.\n"); exit(1); }

$dir = '/tmp/v2reload';
$a_baseline = file_get_contents("$dir/case-a-output.plain.md");
$a_spar     = file_get_contents("$dir/case-a-recommendation.plain.md");
$b_baseline = file_get_contents("$dir/case-b-output.plain.md");
$b_spar     = file_get_contents("$dir/case-b-recommendation.plain.md");
foreach (['a_baseline'=>$a_baseline,'a_spar'=>$a_spar,'b_baseline'=>$b_baseline,'b_spar'=>$b_spar] as $k=>$v) {
    if ($v === false || trim($v) === '') { fwrite(STDERR, "ABORT: missing/empty answer file: $k\n"); exit(1); }
}

$a_question = <<<'EOT'
TerraClarity Consulting is a 50-person environmental-consulting firm with a flat structure (four founding partners, ~46 staff). It's finishing its first employee handbook (~28,000 words), going to all staff on July 1, 2026; the decision is due June 15, 2026. The question: throughout the handbook, what single word should it use for the people who work there? Three options: "Employees" (the word in the firm's legal documents — offer letters, payroll — and the industry standard); "Team members" (what the firm has used in its outward-facing materials for 7 years); or "Colleagues" (proposed by the partner who chairs the pay committee, to signal a flat, peer relationship). The draft currently uses "Employees," but the pay-committee chair says that clashes with the firm's outward voice and its pay philosophy. Recommend a word (or a justified hybrid), with reasoning grounded in the evidence, the trade-offs it does not solve, and how to handle the legal-document consistency issue.
EOT;

$a_evidence = <<<'EOT'
Six pieces of evidence: (1) Pfeffer (2007) — word choices in company documents shape how staff and outsiders see the firm; effects are small (1–3 points) but consistent. "Team members" vs "employees" lowered felt hierarchy but changed no actual authority or reporting lines. (2) Legal consistency — the word doesn't change at-will status (the Toussaint v. Blue Cross line), but if the handbook and offer letters use different words, the mismatch can be cited in a wrongful-termination dispute; fix it with a clause linking the handbook term to the official legal term. (3) Peer firms (SHRM 2024, 217 firms): 71% "employees," 22% "team members," 4% "colleagues," 3% mixed on purpose. (4) The firm has used "team members" in outward materials for 7 years; new hires meet it before "employees." (5) The firm uses published pay ranges with performance-based progression; the pay committee's 2025 notes say "colleagues" fits that philosophy. (6) A non-anonymous staff survey (43 of 46 staff): 12% preferred "employees," 67% "team members," 21% "colleagues."
EOT;

$b_question = <<<'EOT'
Northern Coastal Community College (a public two-year college, ~6,400 students a year, ~1,100 in computer science) is redesigning its CS101: Introduction to Programming for 2026-27, with a decision due June 30, 2026. Its students: ~57% adult learners (age 22+), ~31% first-generation, ~20% second-language; about 73% finish (the department worries about anything under 75%). Python is the teaching language. Two ways to build the course: Path A "concepts first" — weeks 1–5 teach the thinking (breaking problems down, organizing data, controlling the order of steps) in plain sketches and diagrams, with no code yet; Python starts week 6. Path B "language first" — weeks 1–5 teach Python itself with small runnable programs; the deeper thinking emerges from coding later. Which path better serves the course's goals (especially "understand programming as a discipline, not just one language")? Recommend a path (or a justified hybrid), with reasoning, the trade-offs it does not solve, attention to that student body, and the split between the 38% who continue (transfer prep) and the 62% who don't (finishing + general value). Staffing: 4 full-time faculty + 6–8 adjuncts across ~8 sections.
EOT;

$b_evidence = <<<'EOT'
Six pieces of evidence: (1) Cognitive-load research (Sweller 1998) — teaching a new way of thinking AND a new notation at once hurts learning versus one at a time; this favors concepts-first sequencing. (2) Bennedsen & Caspersen (2007), 63 intro courses — how many students finish depends far more on student preparation and language than on concepts-vs-language ordering (65–78% across course designs; 58–85% across languages). (3) Knowles (1980) — adults are motivated by early concrete competence, which favors language-first's "working program by week 3." (4) Hatfield et al. (2019) — first-generation and second-language students trail ~12 points on write-from-scratch tasks; early syntax may help, but the finding failed to replicate in Lewis 2022. (5) Smith & Garcia (2021) and Park et al. (2023) — concepts-first students did slightly better after transferring (d ≈ 0.18–0.22, ~3–4 points), but only if they took data structures within 18 months. (6) NCCC's 2018 Java→Python switch (a language change, not a path change) raised completion from 64% to 73%; there's no data on what a Path A switch would have done.
EOT;

// Back up current rows before overwriting (reversibility).
$rows = $db->query("SELECT * FROM rd_eval_cases ORDER BY id")->fetchAll(PDO::FETCH_ASSOC);
file_put_contents("$dir/backup-rd_eval_cases.json", json_encode($rows, JSON_PRETTY_PRINT));
echo "backed up ".count($rows)." rows to $dir/backup-rd_eval_cases.json\n";

$upd = $db->prepare("UPDATE rd_eval_cases SET question=:q, evidence_summary=:e, answer_x_text=:x, answer_y_text=:y, answer_x_condition=:xc, answer_y_condition=:yc WHERE id=:id");

// Fresh X/Y assignment (flipped from the original): A -> X=baseline, Y=sparring ; B -> X=sparring, Y=baseline.
$upd->execute([':q'=>$a_question, ':e'=>$a_evidence, ':x'=>$a_baseline, ':y'=>$a_spar, ':xc'=>'baseline', ':yc'=>'sparring', ':id'=>1]);
$upd->execute([':q'=>$b_question, ':e'=>$b_evidence, ':x'=>$b_spar, ':y'=>$b_baseline, ':xc'=>'sparring', ':yc'=>'baseline', ':id'=>2]);
echo "updated case A (id=1: X=baseline, Y=sparring) and case B (id=2: X=sparring, Y=baseline)\n";

echo "VERIFY:\n";
foreach ($db->query("SELECT id, answer_x_condition xc, answer_y_condition yc, CHAR_LENGTH(question) q, CHAR_LENGTH(evidence_summary) e, CHAR_LENGTH(answer_x_text) ax, CHAR_LENGTH(answer_y_text) ay FROM rd_eval_cases ORDER BY id")->fetchAll(PDO::FETCH_ASSOC) as $r) echo "  ".json_encode($r)."\n";
