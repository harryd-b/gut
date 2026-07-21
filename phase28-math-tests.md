# Phase 28 — Running the Class C tests: Brieskorn parity, the statistics clause, and Σ_g×S¹

*Working session, 2026-07-11. This session executes the three desk-decidable tests of phase 27 §6 (P6). Conventions: "Seifert orientation" = −Y(G) for the standard negative-definite star-shaped plumbing G; the bridge object throughout is HM ≅ HF⁺ (Kutluhan–Lee–Taubes / Colin–Ghiggini–Honda / Taubes), stated explicitly here because the review flagged silent theory-switching. Every imported result is cited; every derivation performed here is marked [derived here] with its cross-checks.*

---

## 1. Test 3 — the Brieskorn no-cancellation guard: **PASS, upgraded to a theorem**

**The structural result.** Ozsváth–Szabó, *On the Floer homology of plumbed three-manifolds* (arXiv:math/0203265), Corollary 1.4: *if G is a negative-definite graph with at most one bad vertex, then all elements of HF⁺(−Y(G), 𝔱) have even ℤ/2 grading.* Every Seifert integral homology sphere Σ(α₁,…,αₙ) — in particular every Brieskorn sphere Σ(p,q,r) — is the boundary of a star-shaped negative-definite plumbing whose only possible bad vertex is the central one. So the hypothesis holds for the **entire family**, and:

> **HF⁺(Σ) is parity-pure for every Seifert integral homology sphere Σ** — all even in one orientation; by the duality χ_red(−Y) = −χ_red(Y) with d(−Y) = −d(Y), all odd in the other. In either orientation there are no mixed-parity reduced generators.

**Consequence for the guard.** Phase 16's no-cancellation guard 3(b) asked that no even/odd cross-cancellation can occur between protected generators. With parity purity this is automatic: *there is nothing of the other parity to cancel against.* The guard holds for all Brieskorn spheres — indeed all Seifert ℤHS³ — **by theorem, not case-by-case verification**. The phase-16 correction note (which demanded per-manifold parity checks) is hereby superseded in the positive direction: the check has been done once and for all, at the right level of generality.

**The phase-10 ĤF worry, dissolved.** The review observed that ĤF(Σ(2,3,7)) = 𝔽²₍₀₎ ⊕ 𝔽₍₋₁₎ contains both parities on the flagship example. Resolution: the odd generator arises in the passage HF⁺ → ĤF (the U-map exact sequence shifts a copy into odd degree); it is an artifact of the hat flavor. The object the bridge compares is HM ≅ HF⁺, which is parity-pure. The guard fails for ĤF and holds for HM — and HM is what the dictionary uses.

**The explicit deciders.** In the Seifert orientation and OS conventions:

| Σ | HF⁺ | d | rank HF_red | parity | source |
|---|---|---|---|---|---|
| Σ(2,3,5) | 𝒯⁺₍₋₂₎ | −2 | 0 | — | OS math/0203265, verbatim |
| Σ(2,3,7) | 𝒯⁺₍₀₎ ⊕ ℤ₍₀₎ | 0 | 1 | even | OS math/0203265, verbatim |
| Σ(2,3,11) | 𝒯⁺₍₋₂₎ ⊕ ℤ (even degree) | −2 | 1 | even | [derived here] |
| Σ(2,3,13) | 𝒯⁺₍₀₎ ⊕ ℤ² (even degrees) | 0 | 2 | even | [derived here] |

**Derivation for Σ(2,3,11), Σ(2,3,13)** [derived here; three independent inputs, mutually cross-checked]:
1. *Surgery presentations:* Σ(2,3,11) and Σ(2,3,13) are the ±1/2-surgeries on the trefoil completing the family whose n = 1 members are Σ(2,3,5) and Σ(2,3,7).
2. *d-invariants:* for 1/n-surgeries, d(S³₁/ₙ(K)) = −2V₀(K), independent of n. Anchoring V₀ on the n = 1 members (d(Σ(2,3,5)) = −2 ⇒ V₀ = 1 on that side; d(Σ(2,3,7)) = 0 ⇒ V₀ = 0 on the mirror side) gives **d(Σ(2,3,11)) = −2, d(Σ(2,3,13)) = 0** — each family keeps its n = 1 d-invariant.
3. *Casson invariant:* the surgery formula λ(S³₁/ₙ(K)) = n·(½)Δ″_K(1) with Δ_trefoil(t) = t − 1 + t⁻¹ (Δ″(1) = 2) gives |λ| = n: so **|λ(Σ(2,3,11))| = |λ(Σ(2,3,13))| = 2**. Independent cross-check: the Fintushel–Stern instanton Floer homologies of Σ(2,3,11) and Σ(2,3,13) have rank 4 = 2|λ| ✓ (and rank 2 = 2|λ| for the n = 1 members ✓).
4. *Ranks:* Ozsváth–Szabó's λ = χ(HF⁺_red) − d/2, with parity purity forcing |χ_red| = rank(HF_red) (no cancellation in the Euler characteristic), gives: Σ(2,3,11): rank = |λ| − |d/2| = 2 − 1 = **1**; Σ(2,3,13): rank = |λ| − 0 = **2**. Consistency of the whole table: within each family Σ(2,3,6n∓1), d is constant and rank(HF_red) grows by one per step of n — the expected staircase.

*(Caveat register: step 4's sign resolution uses parity purity + the anchors; a graded-roots recomputation would pin the absolute degrees of the reduced generators, which are not needed for this test. The parities — the test's content — are theorem-backed regardless.)*

**Verdict: Test 3 PASSES.** Better: the corrected CORE §5 scope note (ii) — "the guard must be verified case-by-case" — can now be **deleted and replaced by the OS Cor 1.4 citation**. The bridge for Brieskorn spheres remains "modulo standard local analysis" (the analytic half stands), but the parity half is closed for the entire Seifert class.

---

## 2. Test 2 — the statistics clause (Floer ℤ/2-grading = bose/fermi): **consistent; discriminating power located**

On Brieskorn (and all Seifert) homology spheres, parity purity means the dictionary predicts **uniform statistics across all protected states of a given universe** — no bose/fermi mixing in any Σ(p,q,r) protected sector. This is: (a) internally consistent (no spin-statistics tension in the abelian sector); (b) *unfalsifiable on this family* — there is no parity diversity to test against; and (c) now a **theorem-backed prediction of the correspondence**: if anyone exhibits a Seifert ℤHS³ with mixed-parity HM_red, the correspondence is refuted — and OS Cor 1.4 says the framework is safe on this axis for the whole family.

The first *discriminating* arena is b₁ > 0, where mixed parity genuinely occurs (§3(b)): there the clause makes a sharp, countable prediction — **fermionic protected-state multiplicity in flux sector k = b_odd(Sym^{g−1−|k|}(Σ_g))**, the odd Betti numbers of the symmetric product (via Macdonald's generating function Σ_d P_t(Sym^d)q^d = (1+tq)^{2g}/((1−q)(1−t²q))). Concretely for g = 2: sector |k| = 1 (Sym⁰ = pt): purely bosonic, one state; sector k = 0 (Sym¹ = Σ₂): 4 fermionic classes (H¹(Σ₂) = ℤ⁴) against 2 bosonic. Physical reading: the odd classes are H¹(Σ)-valued — fermion zero modes dressing the vortex moduli — exactly where a physicist would put the fermionic protected states. **Verdict: PASS as consistency; upgraded from "untested conjecture" to "quantitative prediction with a specified arena."**

---

## 3. Test 1 — Σ_g×S¹, the first multi-sector contact: **label level EXTENDS; two new structures; the b₁>0 bridge gap is now *principled***

Sector labels: Spin^c(S¹×Σ_g), organized by the flux k = ½⟨c₁(𝔰),[Σ_g]⟩ plus torsion data. Three regimes, all from the literature:

**(a) |k| ≥ g — adjunction truncation.** HF⁺(S¹×Σ_g, 𝔰) = 0 whenever |⟨c₁(𝔰),[Σ]⟩| > 2g − 2 (Ozsváth–Szabó adjunction). So of the infinitely many flux sectors, **only finitely many (|k| ≤ g−1) carry protected content**. This is not a pathology but the **Bradlow bound**: the abelian vortex equations on Σ admit no solutions when the flux exceeds the stability bound. Dictionary consequence: "sector exists, protected content empty" — the label clause is untouched (labels are Spin^c structures, all present), and the internal dictionary survives *with a physical explanation* for the truncation. Logged as new structure: **the protected flux ladder is finite when b₁ > 0.** (This also harmonizes with the Gauss-law correction of phase 9: the tower is flux-sector grading, not a physical charge ladder — and the grading is now seen to be bounded.)

**(b) 0 < |k| ≤ g−1 — symmetric-product sectors.** HM(S¹×Σ_g, 𝔰_k) ≅ H*(Sym^{g−1−|k|}(Σ_g)) (Muñoz–Wang on the SW side, transported through HM ≅ HF⁺). Distinct sectors carry distinct, nonzero protected content: **the label correspondence extends to its first genuine multi-sector example — PASS.** Mixed parity appears (odd cohomology of symmetric products), which has two consequences: it activates the statistics test of §2, and it proves that the Brieskorn no-cancellation mechanism is **unavailable in principle** for b₁ > 0 — not merely unverified, as the corrected CORE §5 had it, but structurally absent (the parity purity that powers §1 fails here by computation). The b₁ > 0 bridge needs a genuinely new argument; that gap is now *principled*, which is what a good obstruction looks like.

**(c) k = 0 — the torsion sector.** Jabuka–Mark (arXiv:math/0502328) compute this sector completely: HF^∞ is the cohomology of a circle bundle over the **Jacobian torus** of Σ_g, and HF⁺ contains nontrivial **2-torsion for every g > 2**. Dictionary consequences: the U-tower is *dressed by the Jacobian* — the moduli of flat U(1) connections, precisely the reducible torus T^{2g} the corrected phase 18 pointed to — and the integral 2-torsion is structure that no naive "charge ladder" reading accommodates. Logged as the second new structure: **the k = 0 clause of the dictionary must be rebuilt around (Jacobian dressing + torsion), not a bare tower.** For g = 1 (T³) the sector is the only one (g − 1 = 0 truncates all k ≠ 0), consistent with the trivial-group observation of CORE §2.1 read at the protected level.

**Verdict: Test 1 — label level PASSES (first multi-sector confirmation in the program); internal dictionary partially extends, acquiring two sharp new requirements (Bradlow truncation, Jacobian/torsion dressing); the OS-positivity bridge for b₁ > 0 remains open and is now known to require a new mechanism rather than a longer computation.**

---

## 4. Ledger and document updates

1. **CORE §5, bridge scope note (ii):** replace "the guard must be verified case-by-case in the monopole normalization" with "the parity half of the guard holds for all Seifert ℤHS³ by OS Cor 1.4 (phase 28 §1); 'modulo standard local analysis' refers to the analytic half only."
2. **phase 27, P6 statuses:** Test 3 → **PASSED (theorem)**; Test 2 → **consistent, quantitative prediction issued for b₁ > 0**; Test 1 → **label level PASSED; dictionary constraints logged; bridge gap principled**.
3. **New falsification handles gained:** any Seifert ℤHS³ with mixed-parity HM_red refutes the correspondence (theorem says none exists — safe axis); for S¹×Σ_g, the fermionic multiplicity must equal b_odd(Sym^{g−1−|k|}Σ_g) — a finite computation per sector that any Floer theorist can audit.
4. **What did NOT survive contact:** the naive "infinite charge ladder in every sector" picture (dead twice over: Gauss law + Bradlow truncation); the hope that the Brieskorn no-cancellation argument would extend to b₁ > 0 (dead in principle, not just in practice).
5. **Forward:** the single most valuable next computation is the g = 2 torsion sector against the dictionary's rebuilt k = 0 clause (Jabuka–Mark give the full answer; the physics side needs to say what the 2-torsion *is* — a genuinely new question the program did not know to ask before today).

*Sources: Ozsváth–Szabó, arXiv:math/0203265 (Cor 1.4; Σ(2,3,5), Σ(2,3,7) verbatim); Jabuka–Mark, arXiv:math/0502328 (k = 0 sector, 2-torsion); Muñoz–Wang (SW of S¹×Σ_g); Fintushel–Stern (instanton ranks used as cross-checks); Casson surgery formula and OS λ = χ_red − d/2 for the derived entries.*
