<?php
/**
 * SPARRING V2 -- §8k / §8i analysis (cross-case comprehension-load covariate).
 *
 * Implements the analysis code pre-registered in the 2026-06-14 amendments:
 *
 *   §8k (cross-case comprehension-load covariate, secondary):
 *     - PRIMARY detector: per-case Krippendorff's alpha on the load-sensitive
 *       criteria C3 (missed real concerns) and C4 (calibrated confidence),
 *       compared between Case A and Case B. A *material* between-case divergence
 *       -- pre-specified as a per-case alpha gap >= 0.20 on either C3 or C4, OR a
 *       between-case sign flip in the §8f direction-of-preference on C3 or C4 --
 *       is reported as a comprehension-load confound on the pooled gate, NOT
 *       silently folded in. Each per-case alpha is reported WITH its per-case n.
 *     - CORROBORATING signal: per-case completion time (optional; see note).
 *     - Subject to the §8g claim-scaling floors (descriptive at small n).
 *
 *   §8i (per-case secondary, extended):
 *     - per-case overall Krippendorff's alpha over all available ratings on the
 *       case (the existing §8i), reported with per-case n; AND
 *     - a per-case dropout-by-position tally: how many raters completed that case
 *       only vs. both cases, split by presentation position (first-seen vs.
 *       second-seen, per rd_eval_rater_case_order). A Case-B-heavy single-case
 *       asymmetry concentrated in the second-seen position is flagged as
 *       candidate comprehension-driven attrition.
 *
 * Krippendorff's alpha is ORDINAL here (the 1-7 rubric is ordinal) and tolerates
 * the incomplete rating matrix by construction (Hayes & Krippendorff 2007) --
 * which is exactly why §8i uses it for partial completers.
 *
 * ----------------------------------------------------------------------------
 * COMPLETION TIME (WITHDRAWN, per the 2026-06-14 amendment addendum): rd_eval_ratings
 * has no server-side start timestamp, and the save-and-return instrument makes an
 * open->submit wall-clock dominated by away-time (an uninformative reading-effort
 * proxy). The per-case completion-time component of §8k was dropped rather than
 * shipped as a misleading metric; §8k relies on the alpha-divergence PRIMARY
 * detector. The optional `active_seconds` input below is retained as a harmless
 * no-op hook: if active on-page time is ever captured it is reported, otherwise
 * §8k stands without it.
 * ----------------------------------------------------------------------------
 *
 * USAGE:
 *   php analyze-v2.php --self-test            # validate the engine (no data needed)
 *   php analyze-v2.php --from-json=<file>     # run on exported ratings
 *
 * INPUT JSON SHAPE (--from-json), produced by the read-only prod export
 * (see export-ratings-for-analysis.php):
 *   {
 *     "cases": [
 *       {"id":3,"label":"A","slug":"...","x_condition":"baseline","y_condition":"sparring"},
 *       {"id":4,"label":"B","slug":"...","x_condition":"sparring","y_condition":"baseline"}
 *     ],
 *     "ratings": [
 *       {"rater_user_id":12,"case_id":3,"submitted":true,
 *        "x":{"c1":6,"c2":5,"c3":4,"c4":5,"c5a":6,"c5b":5},
 *        "y":{"c1":4,"c2":4,"c3":3,"c4":4,"c5a":5,"c5b":4},
 *        "paired":{"c1":"x_better","c3":"y_better", ...},
 *        "active_seconds":540 }                      // active_seconds optional
 *     ],
 *     "case_order": {"12":3,"15":4}                  // user_id -> first-seen case_id
 *   }
 *
 * Output: console summary + (for --from-json) v2/analysis/8k-8i-results.json.
 */

declare(strict_types=1);

ini_set('display_errors', '1');
error_reporting(E_ALL);

const CRITERIA      = ['c1', 'c2', 'c3', 'c4', 'c5a', 'c5b'];
const LOAD_CRITERIA = ['c3', 'c4'];           // §8c lower-tier / counterfactual-inference
const SIDES         = ['x', 'y'];
const ALPHA_GAP_FLAG = 0.20;                   // pre-registered §8k threshold

// ============================================================================
// Krippendorff's alpha (nominal / interval / ordinal), missing data tolerated.
// ============================================================================

/**
 * @param array $units  array of units; each unit is a list of numeric values
 *                      (one per coder that rated it). Units with < 2 values are
 *                      ignored (unpairable).
 * @param string $metric 'nominal' | 'interval' | 'ordinal'
 * @return array{alpha: ?float, n_units: int, n_values: float, note?: string}
 */
function krippendorff_alpha(array $units, string $metric = 'ordinal'): array
{
    $usable = array_values(array_filter($units, fn($u) => count($u) >= 2));
    if (count($usable) === 0) {
        return ['alpha' => null, 'n_units' => 0, 'n_values' => 0.0, 'note' => 'no pairable units'];
    }

    // Ordered category set (numeric sort -- ordinal/interval need the order).
    $catset = [];
    foreach ($usable as $u) {
        foreach ($u as $v) {
            $catset[(string) $v] = (float) $v;
        }
    }
    $cats = array_values($catset);
    sort($cats, SORT_NUMERIC);
    $pos = [];
    foreach ($cats as $i => $c) {
        $pos[(string) $c] = $i;
    }
    $K = count($cats);

    // Coincidence matrix: each unit of m values contributes 1/(m-1) per ordered
    // pair of distinct value-slots.
    $o = array_fill(0, $K, array_fill(0, $K, 0.0));
    foreach ($usable as $u) {
        $m = count($u);
        $w = 1.0 / ($m - 1);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($i === $j) continue;
                $o[$pos[(string) $u[$i]]][$pos[(string) $u[$j]]] += $w;
            }
        }
    }

    $nc = array_fill(0, $K, 0.0);
    for ($c = 0; $c < $K; $c++) {
        for ($k = 0; $k < $K; $k++) {
            $nc[$c] += $o[$c][$k];
        }
    }
    $n = array_sum($nc);
    if ($n < 2) {
        return ['alpha' => null, 'n_units' => count($usable), 'n_values' => $n, 'note' => 'fewer than 2 paired values'];
    }

    // Squared difference function delta^2(a,b) over category POSITIONS a,b.
    $delta2 = function (int $a, int $b) use ($metric, $cats, $nc): float {
        if ($a === $b) return 0.0;
        if ($metric === 'nominal') return 1.0;
        if ($metric === 'interval') {
            $d = $cats[$a] - $cats[$b];
            return $d * $d;
        }
        // ordinal: (sum of marginal counts spanning a..b, minus half the endpoints)^2
        $lo = min($a, $b);
        $hi = max($a, $b);
        $s = 0.0;
        for ($g = $lo; $g <= $hi; $g++) $s += $nc[$g];
        $s -= ($nc[$a] + $nc[$b]) / 2.0;
        return $s * $s;
    };

    $num = 0.0; // observed disagreement (x n)
    $den = 0.0; // expected disagreement (x n(n-1))
    for ($c = 0; $c < $K; $c++) {
        for ($k = 0; $k < $K; $k++) {
            $d2 = $delta2($c, $k);
            if ($d2 === 0.0) continue;
            $num += $o[$c][$k] * $d2;
            $den += $nc[$c] * $nc[$k] * $d2;
        }
    }
    if ($den == 0.0) {
        // No expected disagreement: every value identical -> perfect by convention.
        return ['alpha' => 1.0, 'n_units' => count($usable), 'n_values' => $n, 'note' => 'all values identical'];
    }

    $alpha = 1.0 - ($n - 1) * $num / $den;
    return ['alpha' => $alpha, 'n_units' => count($usable), 'n_values' => $n];
}

// ============================================================================
// §8g claim-scaling tier label (per achieved n).
// ============================================================================

function reporting_tier(int $n): string
{
    if ($n < 4)  return 'below-floor';
    if ($n === 4) return 'descriptive-only';
    if ($n <= 6) return 'descriptive+sign-test';
    if ($n <= 9) return 'descriptive+bootstrap-CI';
    return 'full-inferential';
}

// ============================================================================
// Data shaping from the export JSON.
// ============================================================================

/** Index submitted ratings by case_id -> list of rating rows. */
function ratings_by_case(array $data): array
{
    $byCase = [];
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;            // completers of THIS case
        $byCase[(int) $r['case_id']][] = $r;
    }
    return $byCase;
}

/** §8i overall per-case alpha: units = 12 cells (6 criteria x {x,y}). */
function case_overall_alpha(array $caseRatings): array
{
    $units = [];
    foreach (CRITERIA as $crit) {
        foreach (SIDES as $side) {
            $vals = [];
            foreach ($caseRatings as $r) {
                $v = $r[$side][$crit] ?? null;
                if ($v !== null) $vals[] = (float) $v;
            }
            $units[] = $vals;
        }
    }
    $a = krippendorff_alpha($units, 'ordinal');
    $a['n_raters'] = count($caseRatings);
    return $a;
}

/** §8k per-case per-criterion alpha: units = {x_<crit>, y_<crit>} (2 units). */
function case_criterion_alpha(array $caseRatings, string $crit): array
{
    $units = [];
    foreach (SIDES as $side) {
        $vals = [];
        foreach ($caseRatings as $r) {
            $v = $r[$side][$crit] ?? null;
            if ($v !== null) $vals[] = (float) $v;
        }
        $units[] = $vals;
    }
    $a = krippendorff_alpha($units, 'ordinal');
    $a['n_raters'] = count($caseRatings);
    return $a;
}

/**
 * §8f-style net direction for a (case, criterion): net preference for the
 * SPARRING condition over baseline, mapped through the case's X/Y assignment.
 * Returns -1 / 0 / +1 (sign of #prefer-sparring - #prefer-baseline).
 */
function case_criterion_direction(array $caseRatings, string $crit, array $case): int
{
    $xCond = $case['x_condition'] ?? '';
    $yCond = $case['y_condition'] ?? '';
    $net = 0;
    foreach ($caseRatings as $r) {
        $pref = $r['paired'][$crit] ?? null;
        if ($pref === 'x_better') $winner = $xCond;
        elseif ($pref === 'y_better') $winner = $yCond;
        else continue; // tied / missing
        if ($winner === 'sparring') $net++;
        elseif ($winner === 'baseline') $net--;
    }
    return $net <=> 0;
}

// ============================================================================
// §8k: cross-case comprehension-load covariate.
// ============================================================================

function section_8k(array $data, array $byCase): array
{
    // Resolve the two cases by label (A, B); fall back to first two by id order.
    $cases = $data['cases'];
    usort($cases, fn($a, $b) => (string) ($a['label'] ?? $a['id']) <=> (string) ($b['label'] ?? $b['id']));
    $A = $cases[0] ?? null;
    $B = $cases[1] ?? null;

    $out = ['criteria' => [], 'flag' => false, 'reasons' => []];
    if (!$A || !$B) {
        $out['note'] = 'need exactly two cases to compare';
        return $out;
    }

    $ra = $byCase[(int) $A['id']] ?? [];
    $rb = $byCase[(int) $B['id']] ?? [];

    foreach (LOAD_CRITERIA as $crit) {
        $aAlpha = case_criterion_alpha($ra, $crit);
        $bAlpha = case_criterion_alpha($rb, $crit);

        $gap = ($aAlpha['alpha'] !== null && $bAlpha['alpha'] !== null)
            ? abs($aAlpha['alpha'] - $bAlpha['alpha'])
            : null;
        $gapFlag = ($gap !== null && $gap >= ALPHA_GAP_FLAG);

        $dirA = case_criterion_direction($ra, $crit, $A);
        $dirB = case_criterion_direction($rb, $crit, $B);
        $signFlip = ($dirA !== 0 && $dirB !== 0 && $dirA !== $dirB);

        if ($gapFlag) {
            $out['flag'] = true;
            $out['reasons'][] = sprintf(
                '%s: between-case alpha gap %.3f >= %.2f (A=%.3f n=%d, B=%.3f n=%d)',
                strtoupper($crit), $gap, ALPHA_GAP_FLAG,
                $aAlpha['alpha'], $aAlpha['n_raters'], $bAlpha['alpha'], $bAlpha['n_raters']
            );
        }
        if ($signFlip) {
            $out['flag'] = true;
            $out['reasons'][] = sprintf('%s: §8f direction sign flip between cases (A=%+d, B=%+d)', strtoupper($crit), $dirA, $dirB);
        }

        $out['criteria'][$crit] = [
            'case_a' => ['alpha' => $aAlpha['alpha'], 'n_raters' => $aAlpha['n_raters'], 'tier' => reporting_tier($aAlpha['n_raters']), 'direction' => $dirA],
            'case_b' => ['alpha' => $bAlpha['alpha'], 'n_raters' => $bAlpha['n_raters'], 'tier' => reporting_tier($bAlpha['n_raters']), 'direction' => $dirB],
            'alpha_gap' => $gap,
            'gap_flag' => $gapFlag,
            'sign_flip' => $signFlip,
        ];
    }

    // Corroborating: per-case completion time (only if active_seconds present).
    $out['completion_time'] = completion_time_stats($data, [$A, $B], $byCase);

    return $out;
}

function completion_time_stats(array $data, array $cases, array $byCase): array
{
    $any = false;
    $perCase = [];
    foreach ($cases as $c) {
        $secs = [];
        foreach (($byCase[(int) $c['id']] ?? []) as $r) {
            if (isset($r['active_seconds']) && $r['active_seconds'] !== null) {
                $secs[] = (float) $r['active_seconds'];
                $any = true;
            }
        }
        sort($secs);
        $perCase[$c['label'] ?? $c['id']] = $secs
            ? ['n' => count($secs), 'median_s' => $secs[intdiv(count($secs), 2)], 'mean_s' => array_sum($secs) / count($secs)]
            : ['n' => 0];
    }
    return $any
        ? ['captured' => true, 'note' => 'corroborating-only; confounded by reading length', 'per_case' => $perCase]
        : ['captured' => false, 'note' => 'completion time withdrawn (2026-06-14 amendment addendum); §8k relies on the alpha-divergence primary detector'];
}

// ============================================================================
// §8i: per-case overall alpha + dropout-by-position tally.
// ============================================================================

function section_8i(array $data, array $byCase): array
{
    $out = ['per_case_alpha' => [], 'dropout' => []];

    $caseById = [];
    foreach ($data['cases'] as $c) $caseById[(int) $c['id']] = $c;

    foreach ($data['cases'] as $c) {
        $cr = $byCase[(int) $c['id']] ?? [];
        $a = case_overall_alpha($cr);
        $out['per_case_alpha'][$c['label'] ?? $c['id']] = [
            'alpha' => $a['alpha'], 'n_raters' => $a['n_raters'],
            'tier' => reporting_tier($a['n_raters']), 'note' => $a['note'] ?? null,
        ];
    }

    // Who submitted which case.
    $submittedByUser = []; // user_id -> set of case_id
    foreach ($data['ratings'] as $r) {
        if (empty($r['submitted'])) continue;
        $submittedByUser[(int) $r['rater_user_id']][(int) $r['case_id']] = true;
    }
    $order = [];
    foreach (($data['case_order'] ?? []) as $uid => $cid) $order[(int) $uid] = (int) $cid;

    // Per case: completed-this-only vs both, split by first-seen / second-seen.
    foreach ($data['cases'] as $c) {
        $cid = (int) $c['id'];
        $tally = [
            'first_seen'  => ['only_this' => 0, 'both' => 0],
            'second_seen' => ['only_this' => 0, 'both' => 0],
            'position_unknown' => ['only_this' => 0, 'both' => 0],
        ];
        foreach ($submittedByUser as $uid => $cases) {
            if (empty($cases[$cid])) continue; // didn't complete this case
            $did = count($cases);
            $bucket = $did >= 2 ? 'both' : 'only_this';
            if (!isset($order[$uid])) $posKey = 'position_unknown';
            else $posKey = ($order[$uid] === $cid) ? 'first_seen' : 'second_seen';
            $tally[$posKey][$bucket]++;
        }
        $out['dropout'][$c['label'] ?? $c['id']] = $tally;
    }

    // Flag: a Case-B-heavy single-case asymmetry concentrated in second-seen.
    $byLabel = $out['dropout'];
    $bOnlySecond = $byLabel['B']['second_seen']['only_this'] ?? 0;
    $aOnlySecond = $byLabel['A']['second_seen']['only_this'] ?? 0;
    $out['attrition_flag'] = ($bOnlySecond > $aOnlySecond && $bOnlySecond > 0);
    $out['attrition_note'] = $out['attrition_flag']
        ? "Case B has more second-seen single-case completers ($bOnlySecond) than Case A ($aOnlySecond): candidate comprehension-driven attrition."
        : 'no Case-B-heavy second-seen single-case asymmetry detected';

    return $out;
}

// ============================================================================
// Runner.
// ============================================================================

$args = $argv ?? [];
$fromJson = null;
$selfTest = in_array('--self-test', $args, true);
foreach ($args as $a) {
    if (str_starts_with($a, '--from-json=')) $fromJson = substr($a, 12);
}

if ($selfTest) {
    exit(run_self_test());
}

if ($fromJson === null) {
    fwrite(STDOUT, "usage: php analyze-v2.php --self-test | --from-json=<file>\n");
    exit(0);
}

if (!is_readable($fromJson)) {
    fwrite(STDERR, "cannot read $fromJson\n");
    exit(1);
}
$data = json_decode((string) file_get_contents($fromJson), true);
if (!is_array($data) || !isset($data['cases'], $data['ratings'])) {
    fwrite(STDERR, "input JSON missing 'cases' or 'ratings'\n");
    exit(1);
}

$byCase = ratings_by_case($data);
$results = ['section_8k' => section_8k($data, $byCase), 'section_8i' => section_8i($data, $byCase)];

$outDir = dirname(__DIR__) . '/analysis';
@mkdir($outDir, 0755, true);
file_put_contents($outDir . '/8k-8i-results.json', json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));

print_report($results);
echo "\nWrote: $outDir/8k-8i-results.json\n";
exit(0);

function print_report(array $r): void
{
    echo "===== §8k cross-case comprehension-load covariate =====\n";
    foreach ($r['section_8k']['criteria'] as $crit => $c) {
        echo sprintf(
            "  %s  A: alpha=%s n=%d (%s) dir=%+d | B: alpha=%s n=%d (%s) dir=%+d | gap=%s%s%s\n",
            strtoupper($crit),
            fmt($c['case_a']['alpha']), $c['case_a']['n_raters'], $c['case_a']['tier'], $c['case_a']['direction'],
            fmt($c['case_b']['alpha']), $c['case_b']['n_raters'], $c['case_b']['tier'], $c['case_b']['direction'],
            fmt($c['alpha_gap']),
            $c['gap_flag'] ? '  [GAP-FLAG]' : '',
            $c['sign_flip'] ? '  [SIGN-FLIP]' : ''
        );
    }
    $k = $r['section_8k'];
    echo '  LOAD-CONFOUND FLAG: ' . ($k['flag'] ? 'YES' : 'no') . "\n";
    foreach ($k['reasons'] as $reason) echo "    - $reason\n";
    echo '  completion time: ' . ($k['completion_time']['captured'] ? 'captured' : 'not captured') . " (" . $k['completion_time']['note'] . ")\n";

    echo "\n===== §8i per-case alpha + dropout-by-position =====\n";
    foreach ($r['section_8i']['per_case_alpha'] as $label => $a) {
        echo sprintf("  Case %s: overall alpha=%s n=%d (%s)\n", $label, fmt($a['alpha']), $a['n_raters'], $a['tier']);
    }
    foreach ($r['section_8i']['dropout'] as $label => $t) {
        echo sprintf("  Case %s dropout: first-seen[only=%d both=%d] second-seen[only=%d both=%d] unknown[only=%d both=%d]\n",
            $label, $t['first_seen']['only_this'], $t['first_seen']['both'],
            $t['second_seen']['only_this'], $t['second_seen']['both'],
            $t['position_unknown']['only_this'], $t['position_unknown']['both']);
    }
    echo '  ATTRITION FLAG: ' . ($r['section_8i']['attrition_flag'] ? 'YES' : 'no') . ' -- ' . $r['section_8i']['attrition_note'] . "\n";
}

function fmt($v): string
{
    return $v === null ? 'n/a' : sprintf('%.3f', $v);
}

// ============================================================================
// Self-test: validate the engine and the detectors. No data/DB required.
// ============================================================================

function run_self_test(): int
{
    $fail = 0;
    $approx = function (string $name, ?float $got, float $want, float $tol = 0.005) use (&$fail) {
        $ok = $got !== null && abs($got - $want) <= $tol;
        printf("  [%s] %-34s got=%s want=%.3f\n", $ok ? 'PASS' : 'FAIL', $name, $got === null ? 'null' : sprintf('%.3f', $got), $want);
        if (!$ok) $fail++;
    };
    $assert = function (string $name, bool $cond) use (&$fail) {
        printf("  [%s] %s\n", $cond ? 'PASS' : 'FAIL', $name);
        if (!$cond) $fail++;
    };

    // (1) Krippendorff's canonical 4-observer / 12-unit example.
    // Published values: nominal 0.743, interval 0.849 (Hayes & Krippendorff 2007;
    // Krippendorff 2011). Validating the engine against these firmly-established
    // numbers; ordinal is then checked for plausibility (between the two, ~0.8).
    $units = [
        [1, 1, 1],          // u1  (C missing)
        [2, 2, 3, 2],       // u2
        [3, 3, 3, 3],       // u3
        [3, 3, 3, 3],       // u4
        [2, 2, 2, 2],       // u5
        [1, 2, 3, 4],       // u6
        [4, 4, 4, 4],       // u7
        [1, 1, 2, 1],       // u8
        [2, 2, 2, 2],       // u9
        [5, 5, 5],          // u10 (A missing)
        [1, 1],             // u11 (A,B missing)
        [3],                // u12 single value -> ignored
    ];
    echo "Krippendorff canonical example:\n";
    $approx('alpha nominal', krippendorff_alpha($units, 'nominal')['alpha'], 0.743);
    $approx('alpha interval', krippendorff_alpha($units, 'interval')['alpha'], 0.849);
    $ord = krippendorff_alpha($units, 'ordinal');
    $nom = krippendorff_alpha($units, 'nominal')['alpha'];
    $intv = krippendorff_alpha($units, 'interval')['alpha'];
    printf("  [INFO] alpha ordinal = %.3f (expect between nominal and interval, ~0.8)\n", $ord['alpha']);
    $assert('ordinal between nominal and interval', $ord['alpha'] >= $nom - 0.02 && $ord['alpha'] <= $intv + 0.02);

    // Degenerate cases.
    $assert('all-identical -> alpha 1.0', krippendorff_alpha([[5, 5, 5], [3, 3]], 'ordinal')['alpha'] === 1.0);
    $assert('no pairable units -> null', krippendorff_alpha([[5], [3]], 'ordinal')['alpha'] === null);

    // (2) §8k detector: construct Case A high agreement on C3, Case B low -> gap flag.
    $mk = function (int $uid, int $cid, array $x, array $y, array $paired = [], $secs = null): array {
        return ['rater_user_id' => $uid, 'case_id' => $cid, 'submitted' => true, 'x' => $x, 'y' => $y, 'paired' => $paired, 'active_seconds' => $secs];
    };
    $full = fn($c3, $c4) => ['c1' => 5, 'c2' => 5, 'c3' => $c3, 'c4' => $c4, 'c5a' => 5, 'c5b' => 5];

    $data = [
        'cases' => [
            ['id' => 1, 'label' => 'A', 'x_condition' => 'baseline', 'y_condition' => 'sparring'],
            ['id' => 2, 'label' => 'B', 'x_condition' => 'sparring', 'y_condition' => 'baseline'],
        ],
        'ratings' => [],
        'case_order' => [],
    ];
    // Case A (id 1): 6 raters, tight C3 agreement (x=5,y=2 for all) -> high alpha.
    // Paired C3: all prefer Y (=sparring in A) -> direction +1.
    for ($u = 1; $u <= 6; $u++) {
        $data['ratings'][] = $mk($u, 1, $full(5, 5), $full(2, 4), ['c3' => 'y_better', 'c4' => 'y_better']);
        $data['case_order'][(string) $u] = 1; // A first-seen
    }
    // Case B (id 2): 6 raters, scattered C3 (no agreement) -> low/negative alpha.
    // Paired C3: all prefer X (=sparring in B) -> direction +1 (same sign, no flip on C3).
    // Paired C4: all prefer Y (=baseline in B) -> direction -1; Case A C4 dir +1 -> SIGN FLIP on C4.
    $c3x = [2, 6, 3, 7, 1, 5];
    $c3y = [6, 1, 7, 2, 5, 1];
    for ($i = 0; $i < 6; $i++) {
        $u = 10 + $i;
        $data['ratings'][] = $mk($u, 2, $full($c3x[$i], 5), $full($c3y[$i], 4), ['c3' => 'x_better', 'c4' => 'y_better']);
        $data['case_order'][(string) $u] = 2; // B first-seen
    }

    $byCase = ratings_by_case($data);
    $k = section_8k($data, $byCase);
    echo "\n§8k synthetic scenario:\n";
    $assert('C3 gap flag fires (A tight vs B scattered)', $k['criteria']['c3']['gap_flag'] === true);
    $assert('C4 sign-flip fires (A:+ vs B:-)', $k['criteria']['c4']['sign_flip'] === true);
    $assert('overall load-confound flag = YES', $k['flag'] === true);
    $assert('completion time reported not-captured', $k['completion_time']['captured'] === false);

    // (3) §8i dropout-by-position tally.
    // Build: r1 A-first both; r2 A-first A-only; r3 B-first B-only; r4 B-first both.
    $d = [
        'cases' => $data['cases'],
        'ratings' => [
            $mk(101, 1, $full(5, 5), $full(2, 4)), $mk(101, 2, $full(5, 5), $full(2, 4)), // both
            $mk(102, 1, $full(5, 5), $full(2, 4)),                                          // A only
            $mk(103, 2, $full(5, 5), $full(2, 4)),                                          // B only
            $mk(104, 1, $full(5, 5), $full(2, 4)), $mk(104, 2, $full(5, 5), $full(2, 4)), // both
        ],
        'case_order' => ['101' => 1, '102' => 1, '103' => 2, '104' => 2],
    ];
    $bc = ratings_by_case($d);
    $i8 = section_8i($d, $bc);
    echo "\n§8i synthetic dropout:\n";
    // Case A: first-seen = r101(both), r102(only). second-seen = r104(both). r103 didn't do A.
    $assert('A first-seen only=1', $i8['dropout']['A']['first_seen']['only_this'] === 1);
    $assert('A first-seen both=1', $i8['dropout']['A']['first_seen']['both'] === 1);
    $assert('A second-seen both=1', $i8['dropout']['A']['second_seen']['both'] === 1);
    // Case B: first-seen = r103(only), r104(both). second-seen = r101(both). r102 didn't do B.
    $assert('B first-seen only=1', $i8['dropout']['B']['first_seen']['only_this'] === 1);
    $assert('B second-seen both=1', $i8['dropout']['B']['second_seen']['both'] === 1);

    echo "\n" . ($fail === 0 ? "ALL SELF-TESTS PASSED\n" : "$fail SELF-TEST(S) FAILED\n");
    return $fail === 0 ? 0 : 1;
}
