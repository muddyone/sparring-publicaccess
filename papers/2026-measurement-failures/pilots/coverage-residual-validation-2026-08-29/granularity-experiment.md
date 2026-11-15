# Controlled test: granularity drives yield, but does NOT explain the recall collapse

**Status: exploratory. A controlled manipulation that CONFIRMED half of my explanation and
REFUTED the other half. The refuted half is the one I had put in the previous write-up.**
Tests the claim in [`taxonomy-granularity-finding.md`](./taxonomy-granularity-finding.md).
Raw: `runs/july-2020-secured-transactions.granularity-arms.json`.

---

## The claim under test

Across three fact patterns the structured walk scored recall 1.00 / 0.35 / 1.00, and I
attributed the 0.35 to the NCBE taxonomy being drawn at coarse granularity for Decedents'
Estates and Conflict of Laws. That was **observational** — three subjects that differ in
many ways — so this makes it an intervention: same fact pattern, same key, same model, same
walk mechanism, **only the map changes.**

| arm | nodes | distinct labels | median words | what it degrades |
|---|---|---|---|---|
| **control** | 350 | 341 | 4 | — |
| **collapse** | 86 | 85 | 3 | count **and** words |
| **relabel** | 350 | **85** | 3 | **words only** — count held at the control's |

The relabel arm is the load-bearing one. Collapsing a hierarchy necessarily cuts node
count, so a drop there could be "fewer things to tick" rather than "vaguer things to tick".
Relabelling keeps 350 candidates and degrades only the wording.

## Result

```
arm          items  recall  yield  noise  redun  offkey  ctrl
control          9    1.00   0.89   0.02   0.00    0.49  1.00
collapse         5    1.00   0.76   0.00   0.00    0.36  1.00
relabel          5    1.00   0.70   0.07   0.00    0.31  1.00
```

## 1. Confirmed: specificity drives yield and off-key discovery, and it is not a count effect

Yield falls monotonically **0.89 → 0.76 → 0.70**, and off-key discovery falls **0.49 → 0.36
→ 0.31**. The walk finds less material per item emitted, and much less ungraded-but-material
content, as its map gets vaguer.

**Crucially the relabel arm degrades *more* than collapse** (0.70 vs 0.76) despite having
350 candidates to the collapse arm's 86. Handing the walk the same number of boxes with
vaguer words hurt it *more* than handing it fewer boxes with the same words. That is the
specificity-over-count separation the design was built to make, and it comes out clean.

## 2. Refuted: granularity does NOT explain the recall collapse

**Recall stayed at 1.00 in every arm.** Coarsening the map — by either route — did not cost
the walk a single weighted point.

That is a problem for my explanation. If coarse labels caused the 0.35 recall on Decedents'
/ Conflict of Laws, then coarsening the Secured Transactions map should have pushed its
recall down. It did not move at all.

So **the observational finding conflated two effects**:

- *Granularity → yield and off-key.* Supported, by a controlled manipulation.
- *Granularity → recall.* **Not supported.** The Decedents'/Conflict recall collapse needs a
  different explanation.

I stated the opposite in [`taxonomy-granularity-finding.md`](./taxonomy-granularity-finding.md),
where the headline was framed around recall. That framing is wrong and this document
supersedes it on that point.

### What might actually explain the recall collapse

Three candidates, none tested:

1. **The key, not the map.** Secured Transactions' key is two parallel three-part problems
   (attachment, attachment, priority × two collateral items) — mechanical enough that even
   a coarse map suffices. Decedents'/Conflict asks whether a will was contingent on
   surviving a trip and which of two women a bequest meant. I flagged this confound when
   choosing the case; this result promotes it from caveat to leading candidate.
2. **Contentless is not the same as coarse.** My degraded labels stayed *contentful* —
   "Validity of security agreements and rights of parties". Conflict of Laws ships **"Basic
   concepts"** and **"Application in specific areas"**, which carry no doctrinal content at
   all. Coarse-but-meaningful may be survivable where contentless is not.
3. **Cross-subject dilution.** Decedents'/Conflict is the only two-subject pattern tested.

Candidate 2 is directly testable with a fourth arm that replaces labels with genuinely
contentless headings, and candidate 1 by running the degraded arms on a non-mechanical key.
Neither has been run.

## 3. Recall is at ceiling here, which bounds what this test could have shown

Every rung scored recall 1.00 on this fact pattern — `g1`, `g3` and all three walk arms. So
recall had **no headroom to fall**, and a null on recall is weaker evidence than it looks:
the manipulation could not have demonstrated a recall effect on this pattern even if one
exists.

**This is the honest limit of the experiment.** It establishes the yield effect, and it
fails to reproduce the recall effect *on a pattern where recall cannot move*. The clean
version runs the same three arms on a fact pattern where recall discriminates —
Decedents'/Conflict is the only one of three that does, and its map is already coarse, so
the arms would have to run in the other direction (enriching a map rather than degrading
one), which is not something this design can do.

## What stands after this

- The structured walk's **quality** (yield, off-key) is inherited from its taxonomy's
  wording. Controlled, and separated from count.
- The structured walk's **coverage** (recall) is not explained by taxonomy wording. Open.
- The practical recommendation survives in weakened form: measuring a map's granularity
  predicts how *clean* a structured enumerator's output will be, not whether it will find
  the answer.
