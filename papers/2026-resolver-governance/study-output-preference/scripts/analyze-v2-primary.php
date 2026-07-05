<?php
/**
 * SPARRING V2 -- PRIMARY analysis (§8a-§8f + §8c two-tier gate + §8h/§8j cuts).
 *
 * Companion to analyze-v2.php (which implements the SECONDARY §8k/§8i covariate
 * machinery). This script implements the confirmatory analysis plan locked in
 * the V2 pre-registration §8, with the operational definitions inherited from
 * the V1 analyzer (pilots/.../v1/scripts/analyze.php), as the pre-reg requires
 * ("inherited from V1 §x"):
 *
 *   §8a  Cross-rater statistics, WITHIN rating-condition (per-criterion mean
 *        pairwise Spearman across raters + per-(criterion,condition) mean/stdev).
 *        Primary subset = unaided completers; ai_assisted reported as exploratory
 *        standalone (pre-reg §8a). H4 cross-condition Spearman also reported.
 *   §8b  Per-judge / cross-vendor consensus alignment vs the human reference
 *        (per-criterion Spearman over the 4 (case x condition) cells; per-judge;
 *        headline over all 24 cells). Canonical (case,condition,criterion) table
 *        with judge = mean of the two position passes, consensus = mean of 3.
 *   §8c  Two-tier per-criterion gate on the §8b per-criterion consensus rho:
 *          high-tier  (C1,C2,C5a,C5b): >=0.7 PASS, 0.4-0.7 BORDERLINE, <0.4 FAIL
 *          lower-tier (C3,C4):         >=0.5 PASS, 0.2-0.5 BORDERLINE, <0.2 FAIL
 *        Aggregate: PASS = >=5/6 PASS AND no FAIL; BORDERLINE = >=4/6 PASS AND
 *        <=1 FAIL; else FAIL. (H2.)
 *   §8d  Paired-comparison: per-criterion sparring/baseline/tied vote counts
 *        across raters x cases; sign-agreement vs the §8e absolute delta
 *        direction; two-sided exact binomial vs 50/50, ties excluded. (H3.)
 *   §8e  Per-criterion delta (sparring - baseline), human + per-judge + consensus.
 *   §8f  Direction-of-preference unanimity: fraction preferring SPARRING across
 *        raters x criteria x cases (paired) and judges x criteria x cases. (H1.)
 *   §8g  Claim-scaling tier label for the achieved completer n.
 *   §8h  Familiarity-stratified cut: re-run the gate/§8f on the low-exposure
 *        (F0-F2) human reference, and excluding fingerprint-capable (F4) raters.
 *   §8j  Modality cut: re-run the gate/§8f on the human reference excluding
 *        audio_only raters (per case).
 *
 * ----------------------------------------------------------------------------
 * HUMAN REFERENCE (§8b) -- A DISCLOSED INTERPRETATION UNDER THE OPENED POOL.
 *
 * The locked §8b text names the "unaided RF-partner subset (Bart, External rater E3,
 * External rater E4)" as the primary human reference. The 2026-05-27 amendment opened the
 * pool to an open convenience sample but did not re-define §8b. In the realized
 * pool the named RF partners who completed are External rater E3 (ai_assisted) and External rater E4
 * (unaided); Bart (the author) did not complete. The literal "unaided RF-partner"
 * reference therefore collapses to n=1 (External rater E4) -- too small to anchor a
 * judge-alignment correlation.
 *
 * This analyzer therefore reports the gate against THREE human references, with
 * the choice made explicit so it can be disclosed as a pre-registration
 * deviation in the Ch 7 writeup (transparency, not a silent pick):
 *   PRIMARY      = unaided completers (the largest comparable-condition subset,
 *                  which is the §8a rule for cross-rater statistics, and the
 *                  CONSORT-default "blind == unaided" comparable condition).
 *   SENSITIVITY  = full completer pool.
 *   LITERAL-RF   = unaided ∩ RF_PARTNER_UIDS (reported to SHOW the degeneracy).
 * RF_PARTNER_UIDS defaults to the named partners present (External rater E3=19, External rater E4=20)
 * and is overridable with --rf-partners=19,20,...
 * ----------------------------------------------------------------------------
 *
 * USAGE:
 *   php analyze-v2-primary.php --self-test
 *   php analyze-v2-primary.php --from-json=<ratings-export.json> \
 *       [--judges=<judge-results-plain.json>] [--rf-partners=19,20] [--json-out=<file>]
 *
 * The ratings export must be the AUGMENTED export (carries rater_condition,
 * familiarity, modality) produced by sparring-web scripts/export-ratings-for-analysis.php.
 */

declare(strict_types=1);
ini_set('display_errors', '1');
error_reporting(E_ALL);

const CRITERIA      = ['c1', 'c2', 'c3', 'c4', 'c5a', 'c5b'];
const CRIT_TO_JUDGE = ['c1' => '1', 'c2' => '2', 'c3' => '3', 'c4' => '4', 'c5a' => '5a', 'c5b' => '5b'];
const HIGH_TIER     = ['c1', 'c2', 'c5a', 'c5b'];
const LOW_TIER      = ['c3', 'c4'];
const CONDITIONS    = ['baseline', 'sparring'];   // delta = sparring - baseline
const JUDGES        = ['anthropic', 'openai', 'xai'];

// ============================================================================
// Stats primitives (Spearman inherited from the V1 analyzer).
// ============================================================================

function rankWithTies(array $values): array
{
    $n = count($values);
    $indexed = [];
    foreach ($values as $i => $v) $indexed[] = ['i' => $i, 'v' => $v];
    usort($indexed, fn($a, $b) => $a['v'] <=> $b['v']);
    $ranks = array_fill(0, $n, 0.0);
    $i = 0;
    while ($i < $n) {
        $j = $i;
        while ($j + 1 < $n && $indexed[$j + 1]['v'] === $indexed[$i]['v']) $j++;
        $avgRank = (($i + 1) + ($j + 1)) / 2.0;
        for ($k = $i; $k <= $j; $k++) $ranks[$indexed[$k]['i']] = $avgRank;
        $i = $j + 1;
    }
    return $ranks;
}

function pearson(array $x, array $y): ?float
{
    $n = count($x);
    if ($n < 2 || $n !== count($y)) return null;
    $mx = array_sum($x) / $n;
    $my = array_sum($y) / $n;
    $num = 0.0; $sxx = 0.0; $syy = 0.0;
    for ($i = 0; $i < $n; $i++) {
        $dx = $x[$i] - $mx; $dy = $y[$i] - $my;
        $num += $dx * $dy; $sxx += $dx * $dx; $syy += $dy * $dy;
    }
    $d = sqrt($sxx * $syy);
    return $d == 0.0 ? null : $num / $d;   // null => a constant vector
}

function spearman(array $a, array $b): ?float
{
    if (count($a) !== count($b) || count($a) < 2) return null;
    return pearson(rankWithTies($a), rankWithTies($b));
}

function mean(array $v): ?float { return count($v) ? array_sum($v) / count($v) : null; }

function stdev(array $v): ?float
{
    $n = count($v);
    if ($n < 2) return null;
    $m = array_sum($v) / $n;
    $s = 0.0;
    foreach ($v as $x) $s += ($x - $m) ** 2;
    return sqrt($s / ($n - 1));   // sample stdev
}

/** Mean pairwise Spearman across a set of equal-length vectors (null pairs skipped). */
function mean_pairwise_spearman(array $vectors): array
{
    $rhos = [];
    $vals = array_values($vectors);
    $m = count($vals);
    for ($i = 0; $i < $m; $i++) {
        for ($j = $i + 1; $j < $m; $j++) {
            $r = spearman($vals[$i], $vals[$j]);
            if ($r !== null) $rhos[] = $r;
        }
    }
    return ['mean_rho' => mean($rhos), 'n_pairs' => count($rhos)];
}

/** C(n,k) as exact float (n<=~30 safe in double). */
function nCk(int $n, int $k): float
{
    if ($k < 0 || $k > $n) return 0.0;
    $k = min($k, $n - $k);
    $r = 1.0;
    for ($i = 1; $i <= $k; $i++) $r = $r * ($n - $k + $i) / $i;
    return $r;
}

/** Two-sided exact binomial p-value vs p=0.5 (symmetric tail doubling). */
function binom_two_sided(int $k, int $n): ?float
{
    if ($n <= 0) return null;
    $cum = function (int $lo, int $hi) use ($n): float {
        $s = 0.0;
        for ($i = $lo; $i <= $hi; $i++) $s += nCk($n, $i);
        return $s * (0.5 ** $n);
    };
    $kk = min($k, $n - $k);
    $p = 2.0 * $cum(0, $kk);
    return min(1.0, $p);
}

// ============================================================================
// Data shaping.
// ============================================================================

/** completers = raters who submitted EVERY open case. */
function completers(array $data): array
{
    $caseIds = array_map(fn($c) => (int) $c['id'], $data['cases']);
    $byUser = [];
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;
        $byUser[(int) $r['rater_user_id']][(int) $r['case_id']] = true;
    }
    $out = [];
    foreach ($byUser as $uid => $cs) {
        $all = true;
        foreach ($caseIds as $cid) if (empty($cs[$cid])) { $all = false; break; }
        if ($all) $out[] = $uid;
    }
    sort($out);
    return $out;
}

/** Per-rater rating condition (consistent across cases in V2; first non-null wins, else 'unknown'). */
function rater_conditions(array $data): array
{
    $out = [];
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;
        $uid = (int) $r['rater_user_id'];
        $c = $r['rater_condition'] ?? null;
        if ($c !== null && !isset($out[$uid])) $out[$uid] = $c;
    }
    return $out;
}

/** case_id -> {label, x_condition, y_condition} */
function case_index(array $data): array
{
    $idx = [];
    foreach ($data['cases'] as $c) $idx[(int) $c['id']] = $c;
    return $idx;
}

/**
 * Human cell scores for a rater subset:
 *   cells[caseLabel][condition][crit] = mean over subset raters of that
 *   rater's score for (condition, crit) on that case (X/Y mapped to condition).
 * Also returns raw per-rater vectors for §8a.
 */
function human_cells(array $data, array $subsetUids): array
{
    $caseIdx = case_index($data);
    $sub = array_flip($subsetUids);
    $acc = [];          // label -> cond -> crit -> [scores]
    $perRater = [];     // uid -> crit -> [A.baseline,A.sparring,B.baseline,B.sparring]
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;
        $uid = (int) $r['rater_user_id'];
        if (!isset($sub[$uid])) continue;
        $case = $caseIdx[(int) $r['case_id']] ?? null;
        if (!$case) continue;
        $label = $case['label'];
        foreach (CRITERIA as $crit) {
            $xs = $r['x'][$crit] ?? null;
            $ys = $r['y'][$crit] ?? null;
            if ($xs === null || $ys === null) continue;
            $byCond = [
                $case['x_condition'] => (float) $xs,
                $case['y_condition'] => (float) $ys,
            ];
            foreach (CONDITIONS as $cond) {
                if (!isset($byCond[$cond])) continue;
                $acc[$label][$cond][$crit][] = $byCond[$cond];
                $perRater[$uid][$crit][$label . '.' . $cond] = $byCond[$cond];
            }
        }
    }
    $cells = [];
    foreach ($acc as $label => $byCond) {
        foreach ($byCond as $cond => $byCrit) {
            foreach ($byCrit as $crit => $vals) {
                $cells[$label][$cond][$crit] = mean($vals);
            }
        }
    }
    return ['cells' => $cells, 'per_rater' => $perRater];
}

/**
 * Judge cells from the judge JSON:
 *   perJudge[judge][caseLabel][condition][crit] = mean of the two position passes
 *   consensus[caseLabel][condition][crit]       = mean across the 3 judges
 */
function judge_cells(array $judgeData): array
{
    $caseLabel = fn(string $s) => stripos($s, 'case-a') !== false ? 'A' : (stripos($s, 'case-b') !== false ? 'B' : $s);
    $byPass = []; // judge -> label -> cond -> crit -> [passScores]
    foreach ($judgeData['results'] as $row) {
        if (empty($row['scores'])) continue;
        $judge = $row['judge'];
        $label = $caseLabel($row['case']);
        $sideCond = ['X' => $row['x_condition'], 'Y' => $row['y_condition']];
        foreach ($sideCond as $side => $cond) {
            foreach (CRITERIA as $crit) {
                $jk = CRIT_TO_JUDGE[$crit];
                $sc = $row['scores'][$side][$jk] ?? null;
                if ($sc === null) continue;
                $byPass[$judge][$label][$cond][$crit][] = (float) $sc;
            }
        }
    }
    $perJudge = [];
    foreach ($byPass as $judge => $byLabel)
        foreach ($byLabel as $label => $byCond)
            foreach ($byCond as $cond => $byCrit)
                foreach ($byCrit as $crit => $passes)
                    $perJudge[$judge][$label][$cond][$crit] = mean($passes);
    $consensus = [];
    foreach (['A', 'B'] as $label)
        foreach (CONDITIONS as $cond)
            foreach (CRITERIA as $crit) {
                $vals = [];
                foreach (JUDGES as $j) {
                    $v = $perJudge[$j][$label][$cond][$crit] ?? null;
                    if ($v !== null) $vals[] = $v;
                }
                $consensus[$label][$cond][$crit] = mean($vals);
            }
    return ['per_judge' => $perJudge, 'consensus' => $consensus];
}

// ============================================================================
// §8b + §8c: judge-vs-human alignment and the two-tier gate.
// ============================================================================

/** Per-criterion Spearman of judge-side vs human-side over the 4 (case x condition) cells. */
function per_criterion_rho(array $humanCells, array $judgeSide): array
{
    $out = [];
    foreach (CRITERIA as $crit) {
        $h = []; $j = [];
        foreach (['A', 'B'] as $label) {
            foreach (CONDITIONS as $cond) {
                $hv = $humanCells[$label][$cond][$crit] ?? null;
                $jv = $judgeSide[$label][$cond][$crit] ?? null;
                if ($hv === null || $jv === null) continue;
                $h[] = $hv; $j[] = $jv;
            }
        }
        $out[$crit] = ['rho' => spearman($h, $j), 'n' => count($h), 'human' => $h, 'judge' => $j];
    }
    return $out;
}

function classify_criterion(string $crit, ?float $rho): array
{
    if ($rho === null) return ['class' => 'INDETERMINATE', 'reason' => 'rho undefined (constant vector on one side)'];
    if (in_array($crit, HIGH_TIER, true)) {
        $pass = 0.7; $bord = 0.4;
    } else {
        $pass = 0.5; $bord = 0.2;
    }
    if ($rho >= $pass) return ['class' => 'PASS', 'reason' => sprintf('rho=%.3f >= %.2f', $rho, $pass)];
    if ($rho >= $bord) return ['class' => 'BORDERLINE', 'reason' => sprintf('%.2f <= rho=%.3f < %.2f', $bord, $rho, $pass)];
    return ['class' => 'FAIL', 'reason' => sprintf('rho=%.3f < %.2f', $rho, $bord)];
}

function aggregate_gate(array $perCritClass): array
{
    $pass = 0; $fail = 0; $indet = 0;
    foreach ($perCritClass as $c) {
        if ($c['class'] === 'PASS') $pass++;
        elseif ($c['class'] === 'FAIL') $fail++;
        elseif ($c['class'] === 'INDETERMINATE') $indet++;
    }
    if ($pass >= 5 && $fail === 0)       $agg = 'PASS';
    elseif ($pass >= 4 && $fail <= 1)    $agg = 'BORDERLINE';
    else                                 $agg = 'FAIL';
    return ['aggregate' => $agg, 'n_pass' => $pass, 'n_fail' => $fail, 'n_indeterminate' => $indet];
}

/** Full §8b/§8c gate against one human reference (its consensus rho path). */
function gate_for_reference(array $data, array $judge, array $subsetUids): array
{
    $hc = human_cells($data, $subsetUids)['cells'];
    $perCritConsensus = per_criterion_rho($hc, $judge['consensus']);
    $cls = [];
    foreach (CRITERIA as $crit) $cls[$crit] = classify_criterion($crit, $perCritConsensus[$crit]['rho']);
    $agg = aggregate_gate($cls);

    // headline rho over all 24 cells (consensus vs human)
    $hv = []; $jv = [];
    foreach (CRITERIA as $crit)
        foreach (['A', 'B'] as $label)
            foreach (CONDITIONS as $cond) {
                $h = $hc[$label][$cond][$crit] ?? null;
                $j = $judge['consensus'][$label][$cond][$crit] ?? null;
                if ($h === null || $j === null) continue;
                $hv[] = $h; $jv[] = $j;
            }
    $perJudgeRho = [];
    foreach (JUDGES as $jname) {
        $pc = per_criterion_rho($hc, $judge['per_judge'][$jname] ?? []);
        $jhv = []; $jjv = [];
        foreach (CRITERIA as $crit)
            foreach (['A', 'B'] as $label)
                foreach (CONDITIONS as $cond) {
                    $h = $hc[$label][$cond][$crit] ?? null;
                    $j = $judge['per_judge'][$jname][$label][$cond][$crit] ?? null;
                    if ($h === null || $j === null) continue;
                    $jhv[] = $h; $jjv[] = $j;
                }
        $perJudgeRho[$jname] = ['headline_rho' => spearman($jhv, $jjv), 'per_criterion' => array_map(fn($x) => $x['rho'], $pc)];
    }

    return [
        'n_raters'           => count($subsetUids),
        'headline_rho'       => spearman($hv, $jv),
        'per_criterion_rho'  => array_map(fn($x) => ['rho' => $x['rho'], 'n' => $x['n']], $perCritConsensus),
        'per_criterion_class' => $cls,
        'gate'               => $agg,
        'per_judge'          => $perJudgeRho,
    ];
}

// ============================================================================
// §8e: per-criterion delta (sparring - baseline).
// ============================================================================

function deltas(array $humanCells, array $judge): array
{
    $celldelta = function (array $side, string $crit): ?float {
        $sp = []; $bl = [];
        foreach (['A', 'B'] as $label) {
            $s = $side[$label]['sparring'][$crit] ?? null;
            $b = $side[$label]['baseline'][$crit] ?? null;
            if ($s !== null) $sp[] = $s;
            if ($b !== null) $bl[] = $b;
        }
        $ms = mean($sp); $mb = mean($bl);
        return ($ms === null || $mb === null) ? null : $ms - $mb;
    };
    $out = ['per_criterion' => [], 'aggregate' => []];
    $humanAgg = []; $consAgg = []; $judgeAgg = ['anthropic' => [], 'openai' => [], 'xai' => []];
    foreach (CRITERIA as $crit) {
        $h = $celldelta($humanCells, $crit);
        $c = $celldelta($judge['consensus'], $crit);
        $pj = [];
        foreach (JUDGES as $j) $pj[$j] = $celldelta($judge['per_judge'][$j] ?? [], $crit);
        $out['per_criterion'][$crit] = ['human' => $h, 'consensus' => $c, 'per_judge' => $pj];
        if ($h !== null) $humanAgg[] = $h;
        if ($c !== null) $consAgg[] = $c;
        foreach (JUDGES as $j) if ($pj[$j] !== null) $judgeAgg[$j][] = $pj[$j];
    }
    $out['aggregate'] = [
        'human' => mean($humanAgg), 'consensus' => mean($consAgg),
        'per_judge' => ['anthropic' => mean($judgeAgg['anthropic']), 'openai' => mean($judgeAgg['openai']), 'xai' => mean($judgeAgg['xai'])],
    ];
    return $out;
}

// ============================================================================
// §8d: paired-comparison votes + binomial.
// ============================================================================

function paired_analysis(array $data, array $subsetUids, array $humanDeltas): array
{
    $caseIdx = case_index($data);
    $sub = array_flip($subsetUids);
    $out = [];
    foreach (CRITERIA as $crit) {
        $sparring = 0; $baseline = 0; $tied = 0;
        foreach ($data['ratings'] as $r) {
            if (empty($r['submitted'])) continue;
            $uid = (int) $r['rater_user_id'];
            if (!isset($sub[$uid])) continue;
            $case = $caseIdx[(int) $r['case_id']] ?? null;
            if (!$case) continue;
            $pref = $r['paired'][$crit] ?? null;
            if ($pref === 'x_better') $winner = $case['x_condition'];
            elseif ($pref === 'y_better') $winner = $case['y_condition'];
            elseif ($pref === 'tied') { $tied++; continue; }
            else continue; // missing
            if ($winner === 'sparring') $sparring++;
            elseif ($winner === 'baseline') $baseline++;
        }
        $nDecisive = $sparring + $baseline;
        $p = $nDecisive > 0 ? binom_two_sided($sparring, $nDecisive) : null;
        // sign-agreement vs the absolute (§8e) delta direction for this criterion
        $absDelta = $humanDeltas['per_criterion'][$crit]['human'] ?? null;
        $pairedDir = $sparring <=> $baseline;            // +1 sparring / -1 baseline / 0
        $absDir = $absDelta === null ? null : ($absDelta <=> 0);
        $signAgree = ($absDir === null || $pairedDir === 0) ? null : ($pairedDir === $absDir);
        $out[$crit] = [
            'sparring' => $sparring, 'baseline' => $baseline, 'tied' => $tied,
            'n_decisive' => $nDecisive,
            'prop_sparring' => $nDecisive ? $sparring / $nDecisive : null,
            'binom_p_two_sided' => $p,
            'sig_05' => ($p !== null && $p < 0.05),
            'sign_agreement_with_abs_delta' => $signAgree,
        ];
    }
    return $out;
}

// ============================================================================
// §8f: direction-of-preference unanimity (descriptive).
// ============================================================================

function unanimity(array $data, array $subsetUids, array $judge): array
{
    $caseIdx = case_index($data);
    $sub = array_flip($subsetUids);
    // raters: paired prefs across raters x criteria x cases
    $rS = 0; $rB = 0; $rT = 0;
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;
        $uid = (int) $r['rater_user_id'];
        if (!isset($sub[$uid])) continue;
        $case = $caseIdx[(int) $r['case_id']] ?? null;
        if (!$case) continue;
        foreach (CRITERIA as $crit) {
            $pref = $r['paired'][$crit] ?? null;
            if ($pref === 'x_better') $w = $case['x_condition'];
            elseif ($pref === 'y_better') $w = $case['y_condition'];
            elseif ($pref === 'tied') { $rT++; continue; }
            else continue;
            if ($w === 'sparring') $rS++; elseif ($w === 'baseline') $rB++;
        }
    }
    // judges: per judge x criteria x cases, sparring score > baseline score?
    $jS = 0; $jB = 0; $jT = 0;
    foreach (JUDGES as $jn) {
        foreach (['A', 'B'] as $label) {
            foreach (CRITERIA as $crit) {
                $s = $judge['per_judge'][$jn][$label]['sparring'][$crit] ?? null;
                $b = $judge['per_judge'][$jn][$label]['baseline'][$crit] ?? null;
                if ($s === null || $b === null) continue;
                if ($s > $b) $jS++; elseif ($s < $b) $jB++; else $jT++;
            }
        }
    }
    $frac = fn($s, $t, $b) => ($s + $t + $b) > 0 ? $s / ($s + $t + $b) : null;
    return [
        'raters' => ['sparring' => $rS, 'tied' => $rT, 'baseline' => $rB, 'frac_sparring' => $frac($rS, $rT, $rB)],
        'judges' => ['sparring' => $jS, 'tied' => $jT, 'baseline' => $jB, 'frac_sparring' => $frac($jS, $jT, $jB)],
        'combined_frac_sparring' => $frac($rS + $jS, $rT + $jT, $rB + $jB),
    ];
}

// ============================================================================
// §8a: within-condition cross-rater statistics.
// ============================================================================

function section_8a(array $data, array $subsetUids): array
{
    $hc = human_cells($data, $subsetUids);
    $perRater = $hc['per_rater'];
    $out = ['per_criterion' => []];
    foreach (CRITERIA as $crit) {
        // vectors over the 4 (case.cond) keys, in a fixed order
        $keys = ['A.baseline', 'A.sparring', 'B.baseline', 'B.sparring'];
        $vectors = [];
        foreach ($subsetUids as $uid) {
            $vec = [];
            $ok = true;
            foreach ($keys as $k) {
                $v = $perRater[$uid][$crit][$k] ?? null;
                if ($v === null) { $ok = false; break; }
                $vec[] = $v;
            }
            if ($ok) $vectors[$uid] = $vec;
        }
        $mp = mean_pairwise_spearman($vectors);
        // mean/stdev per (condition) across raters, pooling cases
        $perCond = [];
        foreach (CONDITIONS as $cond) {
            $vals = [];
            foreach ($subsetUids as $uid) {
                foreach (['A', 'B'] as $label) {
                    $v = $perRater[$uid][$crit][$label . '.' . $cond] ?? null;
                    if ($v !== null) $vals[] = $v;
                }
            }
            $perCond[$cond] = ['mean' => mean($vals), 'stdev' => stdev($vals), 'n' => count($vals)];
        }
        $out['per_criterion'][$crit] = [
            'mean_pairwise_rho' => $mp['mean_rho'], 'n_pairs' => $mp['n_pairs'],
            'by_condition' => $perCond,
        ];
    }
    return $out;
}

// ============================================================================
// Runner.
// ============================================================================

function fnum($v, int $d = 3): string { return $v === null ? '  n/a' : sprintf('%+.' . $d . 'f', $v); }
function fr($v): string { return $v === null ? 'n/a' : sprintf('%.3f', $v); }

function run_analysis(array $data, array $judgeData, array $rfPartners): array
{
    $allCompleters = completers($data);
    $cond = rater_conditions($data);
    $unaided     = array_values(array_filter($allCompleters, fn($u) => ($cond[$u] ?? '') === 'unaided'));
    $aiAssisted  = array_values(array_filter($allCompleters, fn($u) => ($cond[$u] ?? '') === 'ai_assisted'));
    $unaidedRF   = array_values(array_filter($unaided, fn($u) => in_array($u, $rfPartners, true)));

    // familiarity / modality subsets
    $fam = (array) ($data['familiarity'] ?? []);
    $lowExposure = array_values(array_filter($allCompleters, function ($u) use ($fam) {
        $f = $fam[(string) $u] ?? null; return $f !== null && in_array($f, ['f0', 'f1', 'f2'], true);
    }));
    $fingerprintExcl = array_values(array_filter($allCompleters, function ($u) use ($fam) {
        return ($fam[(string) $u] ?? null) !== 'f4';   // drop F4 (none expected)
    }));
    $modality = (array) ($data['modality'] ?? []);
    $audioOnlyUsers = [];
    foreach ($modality as $uid => $byCase)
        foreach ((array) $byCase as $cid => $m)
            if ($m === 'audio_only') $audioOnlyUsers[(int) $uid] = true;
    $noAudioOnly = array_values(array_filter($allCompleters, fn($u) => !isset($audioOnlyUsers[$u])));

    $judge = judge_cells($judgeData);

    // PRIMARY human reference = unaided completers
    $primaryGate = gate_for_reference($data, $judge, $unaided);
    $primaryHuman = human_cells($data, $unaided)['cells'];
    $primaryDeltas = deltas($primaryHuman, $judge);
    $primaryPaired = paired_analysis($data, $unaided, $primaryDeltas);
    $primaryUnanimity = unanimity($data, $unaided, $judge);
    $a8a_unaided = section_8a($data, $unaided);
    $a8a_ai = section_8a($data, $aiAssisted);

    // H4: cross-condition Spearman on the per-(case,cond,crit) human means, unaided vs ai_assisted
    $hcU = human_cells($data, $unaided)['cells'];
    $hcA = human_cells($data, $aiAssisted)['cells'];
    $h4 = [];
    foreach (CRITERIA as $crit) {
        $u = []; $a = [];
        foreach (['A', 'B'] as $label)
            foreach (CONDITIONS as $c) {
                $uv = $hcU[$label][$c][$crit] ?? null; $av = $hcA[$label][$c][$crit] ?? null;
                if ($uv === null || $av === null) continue;
                $u[] = $uv; $a[] = $av;
            }
        $h4[$crit] = spearman($u, $a);
    }

    return [
        'subsets' => [
            'all_completers' => $allCompleters,
            'unaided' => $unaided, 'ai_assisted' => $aiAssisted, 'unaided_rf_partner' => $unaidedRF,
            'low_exposure_f0_f2' => $lowExposure, 'fingerprint_excluded' => $fingerprintExcl,
            'no_audio_only' => $noAudioOnly, 'audio_only_users' => array_keys($audioOnlyUsers),
            'rf_partner_uids' => $rfPartners,
        ],
        'tier' => completers_tier(count($allCompleters)),
        'gate_primary_unaided' => $primaryGate,
        'gate_sensitivity' => [
            'full_pool'         => gate_for_reference($data, $judge, $allCompleters),
            'low_exposure_8h'   => gate_for_reference($data, $judge, $lowExposure),
            'fingerprint_excl_8h' => gate_for_reference($data, $judge, $fingerprintExcl),
            'no_audio_only_8j'  => gate_for_reference($data, $judge, $noAudioOnly),
            'literal_unaided_rf' => count($unaidedRF) >= 2 ? gate_for_reference($data, $judge, $unaidedRF)
                                    : ['n_raters' => count($unaidedRF), 'note' => 'degenerate (<2 raters) -- see header; reported to show the locked §8b reference is not usable under the realized pool'],
        ],
        'deltas_8e_unaided' => $primaryDeltas,
        'paired_8d_unaided' => $primaryPaired,
        'unanimity_8f_unaided' => $primaryUnanimity,
        'unanimity_8f_full' => unanimity($data, $allCompleters, $judge),
        'cross_rater_8a' => ['unaided' => $a8a_unaided, 'ai_assisted' => $a8a_ai],
        'h4_cross_condition_rho' => $h4,
    ];
}

function completers_tier(int $n): string
{
    if ($n < 4)  return 'below-floor';
    if ($n === 4) return 'descriptive-only';
    if ($n <= 6) return 'descriptive+sign-test';
    if ($n <= 9) return 'descriptive+bootstrap-CI';
    return 'full-inferential (n>=10)';
}

function print_report(array $R): void
{
    $S = $R['subsets'];
    echo "================= SPARRING V2 PRIMARY ANALYSIS (§8a-§8f, §8c gate) =================\n";
    echo "Completers (both cases): " . count($S['all_completers']) . "  -> claim tier: " . $R['tier'] . "\n";
    echo "  unaided=" . count($S['unaided']) . "  ai_assisted=" . count($S['ai_assisted'])
       . "  low-exposure(F0-F2)=" . count($S['low_exposure_f0_f2'])
       . "  audio-only=" . count($S['audio_only_users']) . "\n";
    echo "  RF partners present (uids " . implode(',', $S['rf_partner_uids']) . ") unaided=" . count($S['unaided_rf_partner']) . "\n\n";

    $g = $R['gate_primary_unaided'];
    echo "----- §8b/§8c GATE  [PRIMARY human reference = unaided completers, n=" . $g['n_raters'] . "] -----\n";
    echo "Headline Spearman (consensus vs human, 24 cells): " . fr($g['headline_rho']) . "\n";
    echo "Per-criterion (judge-consensus vs human) rho + two-tier class:\n";
    foreach (CRITERIA as $crit) {
        $rho = $g['per_criterion_rho'][$crit]['rho'];
        $cl  = $g['per_criterion_class'][$crit];
        $tier = in_array($crit, HIGH_TIER, true) ? 'high' : 'low ';
        printf("  %-4s (%s)  rho=%-7s  -> %-13s  %s\n", strtoupper($crit), $tier, fr($rho), $cl['class'], $cl['reason']);
    }
    printf("AGGREGATE GATE (H2): %s   [%d PASS / %d FAIL / %d INDET of 6]\n\n",
        $g['gate']['aggregate'], $g['gate']['n_pass'], $g['gate']['n_fail'], $g['gate']['n_indeterminate']);

    echo "Per-judge headline rho vs human: ";
    foreach (JUDGES as $j) echo $j . "=" . fr($g['per_judge'][$j]['headline_rho']) . "  ";
    echo "\n\n";

    echo "----- §8e PER-CRITERION DELTA (sparring - baseline) -----\n";
    foreach (CRITERIA as $crit) {
        $d = $R['deltas_8e_unaided']['per_criterion'][$crit];
        printf("  %-4s  human=%s  consensus=%s\n", strtoupper($crit), fnum($d['human'], 2), fnum($d['consensus'], 2));
    }
    $ad = $R['deltas_8e_unaided']['aggregate'];
    printf("  AGGREGATE  human=%s  consensus=%s\n\n", fnum($ad['human'], 3), fnum($ad['consensus'], 3));

    echo "----- §8d PAIRED COMPARISON (across raters x cases; two-sided exact binomial vs 50/50) -----\n";
    $nSig = 0;
    foreach (CRITERIA as $crit) {
        $p = $R['paired_8d_unaided'][$crit];
        if ($p['sig_05']) $nSig++;
        printf("  %-4s  sparring=%-2d baseline=%-2d tied=%-2d | p=%-7s %s | sign-agrees-abs=%s\n",
            strtoupper($crit), $p['sparring'], $p['baseline'], $p['tied'],
            fr($p['binom_p_two_sided']), $p['sig_05'] ? 'SIG' : '   ',
            $p['sign_agreement_with_abs_delta'] === null ? 'n/a' : ($p['sign_agreement_with_abs_delta'] ? 'yes' : 'NO'));
    }
    printf("  H3: %d/6 criteria significant at p<0.05 (pre-reg H3 target: >=4/6)\n\n", $nSig);

    echo "----- §8f DIRECTION-OF-PREFERENCE UNANIMITY (descriptive, H1) -----\n";
    $u = $R['unanimity_8f_unaided'];
    printf("  raters (unaided): sparring=%d tied=%d baseline=%d  frac_sparring=%s\n",
        $u['raters']['sparring'], $u['raters']['tied'], $u['raters']['baseline'], fr($u['raters']['frac_sparring']));
    printf("  judges:           sparring=%d tied=%d baseline=%d  frac_sparring=%s\n",
        $u['judges']['sparring'], $u['judges']['tied'], $u['judges']['baseline'], fr($u['judges']['frac_sparring']));
    printf("  combined frac preferring SPARRING: %s\n", fr($u['combined_frac_sparring']));
    $uf = $R['unanimity_8f_full']['raters'];
    printf("  (full pool raters: sparring=%d tied=%d baseline=%d frac=%s)\n\n",
        $uf['sparring'], $uf['tied'], $uf['baseline'], fr($uf['frac_sparring']));

    echo "----- §8a CROSS-RATER (within condition) mean pairwise Spearman -----\n";
    foreach (['unaided', 'ai_assisted'] as $grp) {
        echo "  [$grp]";
        foreach (CRITERIA as $crit) {
            $r = $R['cross_rater_8a'][$grp]['per_criterion'][$crit]['mean_pairwise_rho'];
            echo "  " . strtoupper($crit) . "=" . fr($r);
        }
        echo "\n";
    }
    echo "\n----- §8h / §8j SENSITIVITY GATES (aggregate only) -----\n";
    foreach ($R['gate_sensitivity'] as $name => $gs) {
        if (isset($gs['note'])) { printf("  %-22s n=%d  %s\n", $name, $gs['n_raters'], $gs['note']); continue; }
        printf("  %-22s n=%-2d  headline_rho=%-6s  AGG=%s [%dP/%dF/%dI]\n",
            $name, $gs['n_raters'], fr($gs['headline_rho']),
            $gs['gate']['aggregate'], $gs['gate']['n_pass'], $gs['gate']['n_fail'], $gs['gate']['n_indeterminate']);
    }
    echo "\n----- H4 cross-condition (unaided vs ai_assisted) per-criterion Spearman -----\n  ";
    foreach (CRITERIA as $crit) echo strtoupper($crit) . "=" . fr($R['h4_cross_condition_rho'][$crit]) . "  ";
    echo "\n";
}

// ----------------------------------------------------------------------------
// Self-test.
// ----------------------------------------------------------------------------

function approx(?float $a, ?float $b, float $eps = 1e-6): bool
{
    if ($a === null || $b === null) return $a === $b;
    return abs($a - $b) <= $eps;
}

function run_self_test(): int
{
    $ok = true;
    $say = function (string $label, bool $pass, string $extra = '') use (&$ok) {
        echo '  [' . ($pass ? 'PASS' : 'FAIL') . "] $label" . ($extra ? "  $extra" : '') . "\n";
        if (!$pass) $ok = false;
    };

    // Spearman: perfect monotone -> 1.0 ; perfect inverse -> -1.0
    $say('spearman monotone = 1', approx(spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0));
    $say('spearman inverse  = -1', approx(spearman([1, 2, 3, 4], [40, 30, 20, 10]), -1.0));
    // Known Spearman: rho = 1 - 6*sum(d^2)/(n(n^2-1)) = 1 - 6*4/(5*24) = 0.8
    $r = spearman([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]);
    $say('spearman known (0.8)', approx($r, 0.8, 1e-9), 'got=' . fr($r));
    $say('spearman constant -> null', spearman([3, 3, 3], [1, 2, 3]) === null);

    // Exact two-sided binomial vs 0.5
    $say('binom 5/5 = 0.0625', approx(binom_two_sided(5, 5), 0.0625, 1e-9));
    $say('binom 6/6 = 0.03125', approx(binom_two_sided(6, 6), 0.03125, 1e-9));
    $say('binom 8/10 = 0.109375', approx(binom_two_sided(8, 10), 0.109375, 1e-9));
    $say('binom 9/10 = 0.0214844', approx(binom_two_sided(9, 10), 0.021484375, 1e-9));
    $say('binom 5/10 = 1.0', approx(binom_two_sided(5, 10), 1.0, 1e-9));

    // Criterion classification thresholds (high vs low tier)
    $say('high-tier 0.7 -> PASS', classify_criterion('c1', 0.70)['class'] === 'PASS');
    $say('high-tier 0.5 -> BORDERLINE', classify_criterion('c1', 0.50)['class'] === 'BORDERLINE');
    $say('high-tier 0.39 -> FAIL', classify_criterion('c1', 0.39)['class'] === 'FAIL');
    $say('low-tier 0.5 -> PASS', classify_criterion('c3', 0.50)['class'] === 'PASS');
    $say('low-tier 0.2 -> BORDERLINE', classify_criterion('c3', 0.20)['class'] === 'BORDERLINE');
    $say('low-tier 0.19 -> FAIL', classify_criterion('c3', 0.19)['class'] === 'FAIL');
    $say('null rho -> INDETERMINATE', classify_criterion('c3', null)['class'] === 'INDETERMINATE');

    // Aggregate gate rule
    $mk = fn(array $classes) => aggregate_gate(array_map(fn($c) => ['class' => $c], $classes));
    $say('agg 6 PASS -> PASS', $mk(['PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'PASS'])['aggregate'] === 'PASS');
    $say('agg 5 PASS 1 BORD -> PASS', $mk(['PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'BORDERLINE'])['aggregate'] === 'PASS');
    $say('agg 5 PASS 1 FAIL -> BORDERLINE', $mk(['PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'FAIL'])['aggregate'] === 'BORDERLINE');
    $say('agg 4 PASS 2 BORD -> BORDERLINE', $mk(['PASS', 'PASS', 'PASS', 'PASS', 'BORDERLINE', 'BORDERLINE'])['aggregate'] === 'BORDERLINE');
    $say('agg 4 PASS 2 FAIL -> FAIL', $mk(['PASS', 'PASS', 'PASS', 'PASS', 'FAIL', 'FAIL'])['aggregate'] === 'FAIL');
    $say('agg 3 PASS -> FAIL', $mk(['PASS', 'PASS', 'PASS', 'BORDERLINE', 'BORDERLINE', 'BORDERLINE'])['aggregate'] === 'FAIL');

    // End-to-end on a tiny synthetic fixture: 2 cases, 2 raters, sparring strictly
    // dominates by +2 on every criterion/side; judges echo it. Expect unanimous
    // sparring direction and positive deltas.
    $synthCases = [
        ['id' => 1, 'label' => 'A', 'x_condition' => 'baseline', 'y_condition' => 'sparring'],
        ['id' => 2, 'label' => 'B', 'x_condition' => 'sparring', 'y_condition' => 'baseline'],
    ];
    $mkScores = fn($base, $bump) => array_combine(CRITERIA, array_map(fn($i) => $base + $bump, range(0, 5)));
    $synthRatings = [];
    foreach ([101, 102] as $uid) {
        // case A: X=baseline(4), Y=sparring(6); case B: X=sparring(6), Y=baseline(4)
        $synthRatings[] = ['rater_user_id' => $uid, 'case_id' => 1, 'submitted' => true, 'rater_condition' => 'unaided',
            'x' => $mkScores(4, 0), 'y' => $mkScores(6, 0),
            'paired' => array_combine(CRITERIA, array_fill(0, 6, 'y_better'))];
        $synthRatings[] = ['rater_user_id' => $uid, 'case_id' => 2, 'submitted' => true, 'rater_condition' => 'unaided',
            'x' => $mkScores(6, 0), 'y' => $mkScores(4, 0),
            'paired' => array_combine(CRITERIA, array_fill(0, 6, 'x_better'))];
    }
    $synthData = ['cases' => $synthCases, 'ratings' => $synthRatings,
        'case_order' => [], 'familiarity' => ['101' => 'f0', '102' => 'f0'], 'modality' => []];
    $synthJudge = ['results' => []];
    foreach (['anthropic', 'openai', 'xai'] as $j) {
        foreach (['case-a' => ['baseline', 'sparring'], 'case-b' => ['sparring', 'baseline']] as $case => $cc) {
            foreach (['pass1', 'pass2'] as $pass) {
                [$xc, $yc] = $cc;
                $sc = fn($cond) => array_combine(['1', '2', '3', '4', '5a', '5b'], array_fill(0, 6, $cond === 'sparring' ? 6 : 4));
                $synthJudge['results'][] = ['judge' => $j, 'case' => $case, 'pass' => $pass,
                    'x_condition' => $xc, 'y_condition' => $yc,
                    'scores' => ['X' => $sc($xc), 'Y' => $sc($yc)]];
            }
        }
    }
    $R = run_analysis($synthData, $synthJudge, [101, 102]);
    $say('synth: 2 completers', count($R['subsets']['all_completers']) === 2);
    $say('synth: unanimous sparring (raters frac=1.0)', approx($R['unanimity_8f_unaided']['raters']['frac_sparring'], 1.0));
    $say('synth: unanimous sparring (judges frac=1.0)', approx($R['unanimity_8f_unaided']['judges']['frac_sparring'], 1.0));
    $say('synth: human aggregate delta = +2', approx($R['deltas_8e_unaided']['aggregate']['human'], 2.0));
    $say('synth: consensus aggregate delta = +2', approx($R['deltas_8e_unaided']['aggregate']['consensus'], 2.0));
    // every criterion: 2 raters x 2 cases = 4 decisive sparring votes -> binom_two_sided(4,4)=0.125
    $say('synth: paired c1 all-sparring p=0.125', approx($R['paired_8d_unaided']['c1']['binom_p_two_sided'], 0.125, 1e-9));

    echo $ok ? "\nALL SELF-TESTS PASSED\n" : "\nSELF-TESTS FAILED\n";
    return $ok ? 0 : 1;
}

// ----------------------------------------------------------------------------
// Main.
// ----------------------------------------------------------------------------

$args = $argv ?? [];
if (in_array('--self-test', $args, true)) exit(run_self_test());

$fromJson = null; $judgesPath = null; $jsonOut = null; $rfPartners = [19, 20];
foreach ($args as $a) {
    if (str_starts_with($a, '--from-json=')) $fromJson = substr($a, 12);
    elseif (str_starts_with($a, '--judges=')) $judgesPath = substr($a, 9);
    elseif (str_starts_with($a, '--json-out=')) $jsonOut = substr($a, 11);
    elseif (str_starts_with($a, '--rf-partners=')) $rfPartners = array_map('intval', array_filter(explode(',', substr($a, 14))));
}

if ($fromJson === null) {
    fwrite(STDOUT, "usage: php analyze-v2-primary.php --self-test | --from-json=<file> [--judges=<file>] [--rf-partners=19,20] [--json-out=<file>]\n");
    exit(0);
}
if (!is_readable($fromJson)) { fwrite(STDERR, "cannot read $fromJson\n"); exit(1); }
if ($judgesPath === null) $judgesPath = __DIR__ . '/../judging/judge-results-plain.json';
if (!is_readable($judgesPath)) { fwrite(STDERR, "cannot read judges file $judgesPath\n"); exit(1); }

$data = json_decode(file_get_contents($fromJson), true);
$judgeData = json_decode(file_get_contents($judgesPath), true);
if (!is_array($data) || !isset($data['ratings'])) { fwrite(STDERR, "bad ratings export\n"); exit(1); }
if (!is_array($judgeData) || !isset($judgeData['results'])) { fwrite(STDERR, "bad judge file\n"); exit(1); }

$R = run_analysis($data, $judgeData, $rfPartners);
print_report($R);

if ($jsonOut === null) $jsonOut = __DIR__ . '/../analysis/primary-results.json';
@mkdir(dirname($jsonOut), 0755, true);
file_put_contents($jsonOut, json_encode($R, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
echo "\nWrote: $jsonOut\n";
exit(0);
