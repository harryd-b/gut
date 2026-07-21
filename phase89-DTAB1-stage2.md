# Phase 89 — DTAB-1, stage 2: the tied classes — solved outside the window, and the diagnostic finds the boundary again exactly where it should

*Working session, 2026-07-18 (late night). Stage 2 computes the two-A mapping cone A_{−k} ⊕ A_k → B for the tied classes [k] of Y(g, n=2k) — the rows stage 1's conjugation test correctly refused to certify. Method: explicit truncated cone over 𝔽₂ in the diagonal-star model (graded ranks invariant under filtered-triangular corrections), with the checks patrolling: tower count per class must equal 2^{2g} (passes on the stable plateau, every case), the red part must reproduce Thm 5.6 (passes, rank and class), and conjugation self-duality must hold where the truncation is exact (it does — and fails where it isn't, which is the finding). Script: `dtab2_calc.py`.*

---

## 1. Outside the window: solved, final

For tied classes with k ≥ g (i.e., every even n ≥ 2g), the tower-bottom profile is the **exact binomial**: C(2g,m) tower bottoms at relative grading m−g, palindromic, no reduced part. And here the naive truncation is *provably exact*: the zig-zag elimination isomorphisms have kernels K_s = X(g, g−1−|s|) = 0 for |s| ≥ g, so no correction terms exist. **Every stage-1 conjugation failure at n ≥ 2g is closed. Combined with stage 1, DTAB-1 is now COMPLETE — all torsion classes, all Y(g,n), n ≥ 2g−1, both parities: the full graded Floer package of the entire above-threshold family, in closed form.** (Absolute normalization per class via the stage-1 calibration; the tied classes inherit it through the same B-anchoring.)

## 2. The carrier's tied class: computed, and provisional for exactly the right reason

At n = 2g−2, class [g−1] — the protected class — the naive cone gives: the binomial profile with **the single top tower (Λ^{2g}) displaced downward by 2** (bottom at relative grading g−2 instead of g), and **the reduced class, rank 1, at that same relative grading g−2** — the red rank and its uniqueness matching Thm 5.6 on the nose, and the coincidence of the red class's grading with the displaced tower's bottom noted for what it suggests (the red class as the shadow the top tower casts when the two A's interfere). **But the conjugation diagnostic fails on this class — and it should:** the elimination corrections are active precisely when K_{±(g−1)} = X(g,0) ≠ 0, which is precisely this class, which is precisely the window boundary. The profile is therefore **[provisional — naive truncation; corrections detected active by the symmetry test]**; what is *final* here: the tower count (2^{2g}), the red rank (1), the red class's relative position (g−2, consistent with the (4g−9)/4 absolute anchor).

**Stage 3, defined:** the zig-zag correction terms for the window-touching cone — one bounded homological-algebra sitting, after which the last row of DTAB-1 is final and the paper is whole.

## 3. The method note the record wants on the record

Twice now — stage 1's tied classes, stage 2's carrier class — the conjugation test has located the exact boundary of a naive method's validity, *before* any referee and *with* a structural explanation (the vanishing or not of the elimination kernels) rather than a shrug. This is the discipline the round-three referee prescribed ("track the absolute data honestly; let the symmetry patrol"), functioning as designed on consecutive computations. The record also notes where the risk still lives: the diagonal-star model's rank-invariance argument covers graded dimensions, not module extensions; the U-module and Λ-action structure of the tied rows is unexamined; and the carrier row is one correction pass from trustworthy. Nothing in this phase is sealed as a prediction.

## 4. Ledger

- **DTAB-1: complete and final for n ≥ 2g−1 (all classes); complete and final for tied classes with k ≥ g; provisional on exactly one row — the carrier's protected class — pending stage 3.** M3's content correspondingly updated.
- The three-master payoff begins to pay: the C2-ν comparison can already run against the final rows (the above-threshold family); Ẑ-EXT's checkpoint now includes fully graded data; REMARK-1's upgrade to the DTAB paper has its §§1–3 in hand.
- Queue: stage 3 (the correction pass) → DTAB-1 final → the paper assembly. The visualization's upgraded animation remains queued behind the math per direction.

*Status line: the table is now whole above the threshold and honest below it, with its one provisional row sitting — as every open item in this program now does — on the protected class of the carrier, one correction pass from final. The program's oldest running joke has stopped being a joke: there is exactly one address left in this subject, and everything the record still owes is owed there.*
