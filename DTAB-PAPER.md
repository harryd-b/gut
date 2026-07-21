# The Heegaard Floer d-invariants of circle bundles over surfaces (draft 1)

*Standalone mathematics paper, drafted 2026-07-19. No external framework content appears or is load-bearing. Proofs are printed in full or reduced to verified citations; every computation is reproducible from the committed scripts (`dtab1_calc.py` … `dtab4b_calc.py`, the sweep engine) and the data file (`DTAB-DATA-2026-07-19.md`). Coefficients 𝔽 = ℤ/2ℤ except where stated. Signature block to be completed by the human signatory before circulation.*

---

## Abstract

Let Y(g,n) be the circle bundle of Euler number n > 0 over a closed oriented surface of genus g ≥ 2. We determine the graded 𝔽[U]-module structure of HF⁺(Y(g,n), 𝔰) for every torsion spin^c structure — the tower-bottom profile (generalized d-invariants) together with the reduced part — in closed form where the surgery cone retracts to a single truncation, and by an exact finite cone computation otherwise. Three structural results organize the answer. (1) The integral triple cup product of Y(g,n) vanishes, so HF^∞ is standard in every torsion class (over 𝔽 by Lidman, over ℤ by Levine–Ruberman) despite b₁ = 2g; among circle bundles over Σ_g the *trivial* bundle is the pathological one. (2) On every class whose non-minimal representatives lie outside the Alexander window, the tower bottoms follow a single closed formula, d_m = d(n,i) + (m−g) + 2 min(0, g+j−m) − 2 min(0, j), a tent-shaped binomial profile anchored by the lens-space correction terms; the truncation is exact because the eliminated zig-zag maps are isomorphisms. (3) At the extremal Euler number n = 2g−2 — the unit tangent bundle — the unique doubly-hit self-conjugate class exhibits a *displaced-tower* phenomenon: the profile is binomial except that the top exterior-power tower sits two below its expected grading, degenerate with the rank-one reduced class at (4g−9)/4; we prove this via an exact three-term cone (a no-corrections lemma plus Jabuka–Mark's identification of the filtration flip as the exact duality star) and verify it by direct computation at g = 2, 3, 4. Complete tables for g ≤ 4 accompany the paper; the methods extend verbatim to any (g,n).

## 1. Introduction and statements

Fix g ≥ 2 and n > 0; Y(g,n) denotes the Euler-number-n circle bundle over Σ_g, realized as n-surgery on the genus-g Borromean knot B ⊂ #^{2g}(S¹×S²) [OS08 §5]. Torsion spin^c structures form a ℤ/n-torsor; by adjunction over the vertical tori, all Floer homology is supported there. We write j = j(n,i) for a minimal-|·|-representative of the class [i], X(g,d) for the Ozsváth–Szabó module ⊕_{k=0}^{d} Λ^{2g−k}H¹(Σ) ⊗ ℤ[U]/U^{d−k+1}, and d(n,i) for the lens-space correction terms.

**Theorem A (standardness).** *The integral triple cup product form of Y(g,n) vanishes identically; hence HF^∞(Y(g,n), 𝔰) is standard — Λ*(H¹(Y;ℤ)⊗𝔽) ⊗ 𝔽[U,U⁻¹] over 𝔽, and integrally — for every torsion 𝔰.* (Proof: one line via the Gysin sequence, §3; the standardness is Lidman's theorem over 𝔽 and Levine–Ruberman's Theorem 3.2 over ℤ. Contrast: Σ_g×S¹ has nonstandard HF^∞ with integral 2-torsion, Jabuka–Mark.)

**Theorem B (the closed form).** *Let [i] be a torsion class all of whose non-minimal representatives s satisfy |s| ≥ g. Then HF⁺(Y(g,n),[i]) is the direct sum, over m = 0,…,2g with multiplicity C(2g,m), of towers 𝒯⁺ with bottom gradings*
d_m(Y(g,n),[i]) = d(n,i) + (m−g) + 2·min(0, g+j−m) − 2·min(0, j),
*plus the reduced module ⊕_{s≡i, s≠j} X_{c(i,s)}(g, g−1−|s|) of [OS08, Thm 5.6]. The hypothesis holds for every class when n ≥ 2g−2, and for the stated classes at every n.* (§5. The absolute normalization is fixed by the g = 0 specialization, which must return HF⁺(L(n,1),i) = 𝒯⁺_{d(n,i)}; the shift is knot-independent because it lives on the surgery cobordism. The formula passes the conjugation test d_m([i]) = d_{2g−m}([−i]) at every applicable class, with no tuning.)

**Theorem C (tied classes; the displaced tower).** *Let n = 2k and consider the tied class [k].*
*(i) If k ≥ g, the profile is exactly binomial — C(2g,m) bottoms at d(n,k)-anchored gradings m−g — palindromic, with vanishing reduced part.*
*(ii) If k = g−1 (the extremal bundle n = 2g−2, i.e. the unit tangent bundle up to orientation), the profile is binomial except that the Λ^{2g} tower's bottom is displaced two below its binomial position, into the grading (4g−9)/4 of the rank-one reduced class.*
(§6. The computation reduces to an exact three-term cone A_{−k} ⊕ A_k → B: a *no-corrections lemma* — the Gaussian-elimination zig-zags of the bi-infinite cone propagate strictly outward, so the truncation acquires no induced terms — together with the identification of the filtration flip as Jabuka–Mark's B⁺, which is the duality star with sign −1 and forced U-reindexing, *with no lower-order terms* [JM, Lemmas 3.1, 3.2, 3.5]. Verified by independent machine computation at g = 2, 3, 4.)

**Corollary D (extremality; from [OS08, Thm 5.6] by a window argument).** *HF⁺_red(Y(g,n)) = 0 for n ≥ 2g−1 (recorded for completeness; stated and used in [MT]), while at n = 2g−2 the total reduced rank is 1, in the unique doubly-hit self-conjugate class, forced there by conjugation invariance. The unit tangent bundle is thus extremal: the largest Euler number with any reduced Floer homology, carrying exactly one class — at the Milnor–Wood line, where horizontal foliations end and Fuchsian rigidity begins (§7, Question 3).*

Complete tables (all torsion classes, g ≤ 4, n ≤ 2g+2; 70 rows; every row's reduced part matching [OS08, Thm 5.6] with a constant anchoring shift) accompany the paper as a data section.

## 2. Background and conventions

We use the integer-surgeries mapping cone of [OS08]: X⁺(n) = ⊕_s A_s⁺ → ⊕ B_s⁺ over representatives s ≡ i (mod n), with A_s⁺ = C{max(i, j−s) ≥ 0} for the Borromean complex C ≅ Λ*H¹(Σ_g) ⊗ ℤ[U,U⁻¹] (all differentials vanish; C{i,j} = U^{−i}Λ^{g−i+j}, supported in grading i+j), v_s the i-projection, h_s the j-projection composed with the flip. Over 𝔽 the flip exchanges C{i,j} and C{j,i} [OS08, Prop 5.2]; over ℤ it is B⁺(α₁∧…∧α_k ⊗ U^ℓ) = −ι_{α₁}⋯ι_{α_k}ω ⊗ U^{g−k+ℓ}, ω the volume form [JM]. Gradings on X(g,d) follow [OS08]'s centered convention (the summand Λ^{2g−d} in degree zero) — a convention our computations confirm empirically against Theorem 5.5 (§7).

## 3. Theorem A

H¹(Y;ℤ) = π*H¹(Σ;ℤ) by Gysin (n ≠ 0), so any triple product of one-classes is π* of a class in H³(Σ;ℤ) = 0. Lidman's theorem (HF^∞ at torsion 𝔰 is the homology of Λ*(free H¹) ⊗ 𝔽[U,U⁻¹] with differential the contraction by the integral triple cup form) gives 𝔽-standardness; Levine–Ruberman Thm 3.2 gives it integrally. ∎ *Caution: "standard" refers to Λ* of the free part H¹(Y;ℤ)⊗𝔽 ≅ 𝔽^{2g}; for even n the group H¹(Y;𝔽) is 2g+1-dimensional and would overstate the rank by a factor of two.*

## 4. Corollary D's window argument

X(g, g−1−|s|) = 0 unless |s| ≤ g−1; the window [−(g−1), g−1] holds 2g−1 integers. For n ≥ 2g−1 each residue class meets it at most once, necessarily at j — the [OS08, Thm 5.6] sum is empty. For n = 2g−2 exactly one class meets it twice, at s = ±(g−1) (tying for j); the survivor contributes X(g,0) ≅ 𝔽. Conjugation invariance plus total rank one forces self-conjugacy of the supporting class. ∎

## 5. Theorem B: bookkeeping and calibration

For ω ∈ Λ^m, the A_s⁺ tower has U-floor min(0, g+s−m), hence relative bottom 2min(0, g+s−m) + (m−g) — the tent profile. Exactness of the single-A truncation: eliminating (A_s, B_s) via v_s (s > j side) and (A_s, B_{s+n}) via h_s (s < j side) uses isomorphisms precisely when the kernels X(g, g−1−|s|) vanish, i.e. |s| ≥ g — the hypothesis; induced corrections compose strictly outward (see §6) and never return. The absolute shift attached to A_j⁺ is a property of the surgery cobordism, independent of the knot; setting g = 0 (the unknot; Y(0,n) = L(n,1)) forces shift = d(n,i) − 2min(0,j). Both closure properties — the g = 0 anchor and the conjugation symmetry across all applicable (g,n,i) — were verified by machine with no free parameters. ∎

## 6. Theorem C: the exact three-term cone

*(No-corrections lemma.)* In the bi-infinite cone for [k], every out-map of an eliminated A_s points away from the center (v_s leftward maps into B_s on the left tail; h_s rightward into B_{s+n} on the right tail), so Gaussian elimination induces terms only further outward: the surviving A_{−k} ⊕ A_k → B acquires nothing. *(The flip.)* By [JM] the flip is the exact star (sign −1); the cone is thus completely explicit. For k ≥ g both projections are injective on the relevant ranges and the binomial profile is immediate; for k = g−1 the kernels K_{±(g−1)} ≅ X(g,0) interfere: an explicit 𝔽-linear computation (per exterior-line pair, all differentials zero) yields the displaced-tower profile and the rank-one reduced class at the displaced grading. Machine verification at g = 2, 3, 4 (tower plateaus 2^{2g}; red parts matching Thm 5.6; anchoring constant) accompanies the scripts. A remark on extraction: reduced classes whose top grading coincides with a tower bottom are invisible to dimension-counting alone; our extraction tracks the U-module structure (an early dimension-only pass undercounted one such class, caught by the acceptance suite — we flag the pitfall for others computing from cones). ∎

## 7. Data, verification chain, and questions

**Verification chain (summary).** g = 0 calibration exact by construction; conjugation symmetry across all applicable classes; Theorem 5.5 reproduced through three-A and five-A cones at g = 2 and 3 *at full graded resolution* (red totals 2 and 18; distributions {2} and {2,12,2}+{2} with constant anchor shifts); tower plateaus 2^{2g} throughout; the tied-class computations reproduce the general engine; 70/70 rows anchored.

**Questions.** (1) *Integral lifts:* Theorem A holds over ℤ; our cone computations are over 𝔽 — the integral tied-class profile (where [JM]'s sign −1 lives) is open. (2) *Naturality:* the mapping-class group acts on Y(g,n) covering Σ_g; the d-invariant profile is MCG-invariant by construction, but the finer equivariance of the tower decomposition (the Λ^m-family structure under Sp(2g,ℤ)) and any projective phenomena in refined settings seem unexamined. (3) *The extremal geometry:* n = 2g−2 is the Milnor–Wood/Giroux line; at equality the horizontal foliation is rigid (Goldman; Matsumoto–Ghys). Is the surviving reduced class the (twisted) contact/Eliashberg–Thurston invariant of the perturbed Fuchsian foliation — "maximal = rigid" as a Floer statement? (4) *q-series checkpoints:* extensions of homological-block/Ẑ-type invariants to genus-decorated plumbings do not yet exist; these tables provide the complete target data for the first such extension on its simplest nontrivial family.

## References

Ozsváth–Szabó, *Knot Floer homology and integer surgeries*, AGT 8 (2008) 101–154 [OS08]. Jabuka–Mark, *On the Heegaard Floer homology of a surface times a circle*, Adv. Math. 218 (2008) [JM]. Lidman, arXiv:1011.4277. Levine–Ruberman, arXiv:1403.2464. Mark–Tosun, arXiv:2512.04278 [MT]. Ozsváth–Szabó, *Absolutely graded Floer homologies…*, Adv. Math. 173 (2003). Mrowka–Ozsváth–Yu, Comm. Anal. Geom. 5 (1997). Milnor–Wood/Giroux/Goldman/Matsumoto–Ghys as cited in §7. (Venue format at typesetting.)

---

*Method disclosure and signature: drafted with substantial AI assistance; all cited theorems verified against primary sources during the work; the two early computational errors this project made (a convention-mixing in a related spin-sum computation, and the dimension-only extraction pitfall of §6) were caught by external review and by the acceptance suite respectively, and both instruments are described so the reader may distrust us efficiently. [SIGNATURE BLOCK — human signatory; graded verification statement.]*
