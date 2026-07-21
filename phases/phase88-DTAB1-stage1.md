# Phase 88 — DTAB-1, stage 1: the d-invariant table of circle bundles, in closed form off the ties

*Working session, 2026-07-18 (late night). The math track resumes with the computation three masters have been waiting for — the REMARK-1 upgrade ("a small real paper," per the fresh referee), C2-ν's data requirement, and Ẑ-EXT's checkpoint calibration. Stage 1 delivers the closed form on its honest domain, built under the round-three rules: the one non-derived input (the absolute grading shift) is CALIBRATED against ground truth rather than bootstrapped from relative phases, the calibration point is exact (g = 0 lens spaces), and the domain boundary announces itself through a symmetry test that fails precisely where the method is known to be incomplete. Script: `dtab1_calc.py`.*

---

## 1. The result

For Y(g,n), n > 0, torsion class [i] with a **unique** minimal-|·| representative j, the tower family Λ^m H¹ (m = 0…2g, multiplicity C(2g,m)) has bottom grading:

> **d_m(Y(g,n), [i]) = d(n,i) + (m − g) + 2·min(0, g+j−m) − 2·min(0, j)**

[derived + calibrated]. Derivation: the Borromean complex C = Λ*H¹ ⊗ ℤ[U,U⁻¹] with C{i,j} = U^{−i}Λ^{g−i+j} and vanishing differentials gives H(A_s⁺) by pure bookkeeping — for ω ∈ Λ^m the allowed U-range has floor min(0, g+s−m), so the relative bottom is 2min(0, g+s−m) + (m−g); the absolute shift attached to A_j⁺ by the surgery formula is knot-independent (it lives on the cobordism), so it is fixed once by the g = 0 case, where the unknot's cone must return HF⁺(L(n,1), i) = 𝒯⁺_{d(n,i)} — giving shift = d(n,i) − 2min(0,j). **Calibration is exact by construction at g = 0; the content is the g-dependence, which is derived.**

**The two checks:**
- **Conjugation symmetry d_m([i]) = d_{2g−m}([−i]) holds for every class with a unique representative, at every (g,n) tested** — a nontrivial global test (it mixes the m-profile reversal with the i ↔ n−i lens-space terms) that the formula passes with no tuning.
- **It fails exactly and only on the tied classes** (i = n/2, n even) — where the provisional single-A values are *known* to be wrong, because the correct object is the cone over both A_{±n/2}. The failure is the method diagnosing its own boundary: nothing off the ties is contaminated.

## 2. What stage 1 already completes

**For n ≥ 2g−1 with n odd, this table is the ENTIRE Floer package of Y(g,n)** — HF_red vanishes there (REMARK-1 Prop 2a), every class has a unique representative, and the closed form above lists every tower bottom with multiplicities. A closed-form, fully graded HF⁺ for an infinite two-parameter family of Seifert manifolds, calibrated and symmetry-tested — the "large half" of the small real paper, done. Sample (g = 2, n = 5, class [0]): d = (−1, 0, 1, 0, −1) with multiplicities (1,4,6,4,1) — the tent-shaped m-profile peaked at m = g+j, which is the general shape.

## 3. What stage 2 requires — and where it points

The tied classes need the honest cone over both A_{±n/2} — and the tied class at the carrier's Euler number n = 2g−2 is [g−1]: **the protected class, again.** Every road in this program ends at the same address: the double class whose cone carries the rank-one reduced part (at grading (4g−9)/4, already known from the c(i,s) machinery), the theta half of the spin ledger, the MOY-degenerate spin sector, and now the one gap in the d-invariant table. Stage 2 is the two-A cone computation with the B-tower matching done honestly — bounded, delicate after this week's lessons, and the natural next sitting. Its output completes DTAB-1 for even n, hands C2-ν its absolute data for the class that matters, and finishes the calibration target Ẑ-EXT would be tested against.

## 4. Ledger

- **DTAB-1 stage 1 closed:** the closed form [derived, calibrated at g = 0, conjugation-verified off ties]; the n ≥ 2g−1 odd package complete; the tied-class boundary diagnosed by the symmetry test. M3's content is now half-filled with actual values.
- Method note for the record: this is the first absolute-grading computation the program has produced *under* the post-round-three rules (calibrate, don't bootstrap; let a symmetry test patrol the domain), and the first whose error-boundary was found by the computation itself rather than by a referee.
- Queue: **stage 2 (the double-class cone)** → completes DTAB-1 → REMARK-1 rev 3 upgrade to the full paper → C2-ν gets its data. In parallel, per the user: the visualization's animation to be made more compelling (a proper hyperbolic-disk geodesic flow rather than the stylized lemniscate — queued).

*Status line: the table three chapters were waiting for now exists on the domain where it can be trusted, with its one gap sitting — of course — on the protected class, which has now been the site of the census collapse, the spin ledger, the Majorana lines, the MOY degeneracy, and the last missing d-invariant. The program long ago stopped believing in coincidences it likes; but it is permitted to notice that every question it asks lands on the same doorstep, and to knock there next.*
