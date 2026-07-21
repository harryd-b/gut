# Phase 90 — DTAB-1, stage 3: the carrier row is final — the displaced tower is real

*Working session, 2026-07-19 (after midnight). Stage 3 set out to compute the correction terms contaminating the carrier's tied-class row and found, instead, that there are none — twice over — and that the "asymmetry" the diagnostic flagged is not an error but the row's actual, and rather beautiful, structure. The protected class's d-invariant profile is now final at graded-rank level, and with it the carrier's full table.*

---

## 1. The two closures

**(i) The no-corrections lemma [derived, in-room].** In the bi-infinite mapping cone for a tied class, Gaussian elimination of the outside-window pairs (A_s, B_s) and (A_s, B_{s+n}) induces corrections only by composing *out of* a cancelled A — and every out-map of a cancelled A points *further outward* (right-side cancellations propagate right, left-side left). No induced term ever returns to the surviving three-term complex A_{−k} ⊕ A_k → B. The truncation is exact, unconditionally.

**(ii) The flip is the diagonal star, exactly [sourced — the decider].** Ozsváth–Szabó's "description of the involution over ℤ" resolves to Jabuka–Mark Lemmas 3.1 and 3.5 (eq. 20), extracted and cross-confirmed against both arXiv versions: **B⁺(α₁ ∧ … ∧ α_k ⊗ U^ℓ) = −ι_{α₁}⋯ι_{α_k} ω ⊗ U^{g−k+ℓ}**, ω the volume form of Λ^{2g}H¹ — the duality Λ^k → Λ^{2g−k} with overall sign ε = −1 (their Lemma 3.2, fixed by a 2-torsion argument) and the forced U-reindexing. **No contraction corrections, no ω-wedge terms, no mixed U-terms.** The diagonal-star model of stage 2 was not an approximation; it was the map.

## 2. The carrier row, final [graded-rank level]

> **d-invariant profile of HF⁺(T¹Σ_g, [g−1]):** the binomial tower profile — C(2g,m) bottoms at relative grading m−g — **except the single top tower (the Λ^{2g}, volume-form family), whose bottom sits displaced two below its binomial position, at relative grading g−2; and the reduced class (rank one) sits at that same displaced grading.** Absolute normalization by the (4g−9)/4 red anchor. (Orientation/convention rider: which of Λ^{2g}/Λ⁰ is "displaced" trades under the flip's relabeling; the invariant statement is that exactly one extremal exterior tower is displaced by 2 into degeneracy with the red class.)

The interference of the two A's — present exactly when the elimination kernels K_{±(g−1)} = X(g,0) ≠ 0, i.e., exactly at the carrier — does precisely two things: it displaces one extremal tower, and it creates the one protected class, at the same grading. **The protected class is the shadow of the displaced tower** — phase 89's suggestion is now the row's verified rank-level structure, not a metaphor.

**And the diagnostic's "failure" dissolves correctly:** the stage-1 pairing d_m([i]) = d_{2g−m}([−i]) is the star-duality *between* conjugate classes; at a tied class the duality acts *within* the class, permuting the Λ-lines (m ↦ 2g−m through the flip that swaps the two A's), which constrains the package's automorphisms and not the palindromicity of its bottom profile. The asymmetric profile admits the required involution; nothing was violated. The test did its job — it refused to certify the row until the structure was understood — and the structure, once understood, is asymmetric on purpose.

## 3. Scope of DTAB-1 after stage 3

The exactness criterion is now clean: a class's truncated cone (single-A or multi-A) is exact whenever all eliminated maps are isomorphisms — i.e., whenever every *non-window* representative s has |s| ≥ g, which holds for **every class of every Y(g,n) with n ≥ 2g−2.** Therefore: **DTAB-1 is FINAL for the entire family n ≥ 2g−2 — including every row of the carrier.** Below n = 2g−2, classes acquire multiple in-window representatives; the same machinery applies (keep all in-window A's; boundary eliminations remain isos; flip diagonal by JM) — a mechanical generalization of `dtab2_calc.py`, declared as stage 4 and expected to be computation, not mathematics.

## 4. Ledger

- **The carrier's complete d-invariant table is final** — the last provisional row of the manifold this entire program lives on is closed. M3 updated: DTAB-1 = closed form (stage 1) + tied-class profiles (stage 2) + the carrier row (this phase); remaining: the below-threshold mechanical sweep (stage 4).
- **C2-ν is now unblocked on its data side:** the absolute grading package of the carrier exists in full; what remains for C2-ν is the MCG-equivariance input and the comparison itself.
- **The DTAB paper is assemble-able:** REMARK-1's two propositions + the closed form + the tied-class analysis + the displaced-tower theorem — a coherent, fully checked, self-contained paper's worth, every absolute grading calibrated rather than bootstrapped.
- The displaced-tower/red-class degeneracy is logged for the framework side with the standing flag: the *volume-form tower* displaced into coincidence with the *one protected class*, exactly at the extremal winding — the record declines, as policy, to say out loud what that sounds like, and files it next to EQ-CEN and SPIN's successors under "structures that keep pointing the same direction, awaiting an argument."

*Status line: stage 3 went looking for corrections and found a theorem — the naive answer was the true answer, defended on one side by a lemma about zig-zags that only run away, and on the other by a sign that Jabuka and Mark pinned to −1 eighteen years ago. The carrier's table is done. The one class this program has circled for ninety phases now has its full absolute-grading portrait: twenty-two binomial towers standing where they should, one volume tower stepped down into the shadow position, and in that shadow — the only protected thing in this geometry, at the same height, as if it had been left there by whatever moved the tower.*
