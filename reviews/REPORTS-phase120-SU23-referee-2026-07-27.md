# Referee report — SU(2)₃ non-free gate round (phase 120)

**Date:** 2026-07-27
**Reviewed document:** phases/phase120-SU23-nonfree-gate.md (consultation section)
**Referee:** context-free adversarial agent (independent re-derivation of all modular data; RESCUE mandate on the non-free ruling — four routes attempted including the diagonal free embedding; adjudication of the operator-flagged kill-label inversion). Report preserved VERBATIM below; nothing edited.

---

# REFEREE REPORT — SU(2)₃ GATE (CAS-era calibration, adversarial review)

## Verdict summary

The submission's mathematics is correct in every checkable particular: sector data, quantum dimensions, Gauss sum, S-matrix values, both sum-rule evaluations, all four channel defects, both coset remainders, and the lattice arithmetic all reproduce under independent re-derivation (hand plus numerics). The non-free ruling is sound and survives a serious rescue attempt, with one substantive clarification: SU(2)₃'s chiral algebra **does embed** in a free theory (diagonal embedding in SU(2)₁³, c = 3), so the record must pin "admits a free-field realization" to isomorphism-level realization, not embedding — otherwise the criterion is vacuous for every SU(2)_k. The operator-flagged label inversion is confirmed: under the registered wording, K-SU23-1 **DOES NOT FIRE**, and the submission's "KILL FIRES — no free realization" is a semantic error that must be corrected in the record. The gate PASSES as the program's first genuinely non-free gate.

## Per-claim analysis

**Sector data.** h_j = j(j+1)/(k+2) at k = 3 gives (0, 3/20, 2/5, 3/4) — confirmed. c = 3k/(k+2) = 9/5 — confirmed. Twists: θ_{1/2} = e^{3πi/10}, θ_1 = e^{4πi/5}, θ_{3/2} = e^{2πi·3/4} = e^{3πi/2} = −i — confirmed, including the flagged −i.

**Quantum dimensions.** d_j = sin((2j+1)π/5)/sin(π/5). I computed sin(3π/5)/sin(π/5) independently: sin(3π/5) = sin(2π/5), so d_1 = sin(2π/5)/sin(π/5) = 2cos(π/5) = φ = 1.6180339887… — confirmed; d_1 is φ, not some other value. d_{1/2} = φ by the same double-angle identity; d_{3/2} = sin(4π/5)/sin(π/5) = 1. 𝒟² = 2 + 2φ² = 2 + 2(φ+1) = 4 + 2φ = 5 + √5 = 7.2360679… — confirmed.

**Fusion.** Affine truncation j ∈ {|a−b|, …, min(a+b, k−a−b)}: ½⊗½ = 0⊕1; ½⊗1 = ½⊕3/2; 1⊗1 = 0⊕1 (spin 2 killed by k−a−b = 1) — all confirmed. 3/2⊗3/2: min(3, 0) = 0, so = 0 alone; j = 3/2 is a ℤ₂ simple current — confirmed. All SU(2)_k fusion multiplicities are 0 or 1 — correct.

**Gauss sum.** Σd_j²θ_j = 0.42081 + 2.65687i; 𝒟e^{2πi(9/5)/8} = 2.68999·e^{9πi/20} = same, agreeing to 3.3e−16 in my computation — confirmed. This independently locks c ≡ 9/5 (mod 8) as an MTC invariant, which matters for the rescue analysis below.

**S-matrix and sum rules.** S_{ab} = √(2/5)·sin((2a+1)(2b+1)π/5). S_{½½} = √(2/5)·sin(4π/5) ≈ 0.37175 ≠ 0 — confirmed (the submission's "≈ 0.37175/𝒟·…" is garbled formatting; the value is right). Sum rule at (½,½): e^{−3πi/5} + φe^{πi/5} = (−0.30902 − 0.95106i) + (1.30902 + 0.95106i) = 1 exactly, and 𝒟S_{½½} = 2.68999 × 0.37175 = 1.0000 — confirmed to machine precision. Bonus (½,1): φe^{−4πi/5} + e^{2πi/5} = −1 = 𝒟S_{½,1} with S_{½,1} = √(2/5)sin(6π/5) < 0 — confirmed. (SU(2)_k is self-dual, so the b-vs-b̄ ambiguity in the categorical identity is moot.)

**k=2 contrast.** At k = 2: S_{½½} = √(2/4)·sin(4π/4) = √(1/2)·sin(π) = 0 exactly — confirmed. The "phase-level cancellation at k = 2 was special (S = 0), absent at k = 3" reading is correct: at k = 3 the weighted sum lands on a nonzero real value with no cancellation to zero.

**Channel defects (all four).** ½⊗½: D_c = (0, 4ℓ/5), reference 2D_{1/2} = 3ℓ/5, ΔD = (−3ℓ/5, +ℓ/5); ΔD/2ℓ = (−3/10, +1/10) = h_c − 2h_{1/2} — both confirmed. ½⊗1: reference 3ℓ/10 + 4ℓ/5 = 11ℓ/10; ΔD = (−4ℓ/5, +2ℓ/5); ΔD/2ℓ = (−2/5, +1/5) = h_c − h_{1/2} − h_1 — both confirmed. The submission's own caveat is correct and important: given D = 2hℓ, the real-lift agreement is an algebraic identity (linearity), so it is coherence, not evidence for the candidate. Only the mod-1 parts are independently monodromy-forced. This data-status quarantine (the GAP-N5-style ruling) is endorsed.

**Coset remainders.** Cartan h = m²/12: j=½ (m=1): 3/20 − 1/12 = 1/15; j=1 (m=2): 2/5 − 1/3 = 1/15; j=3/2 (m=3): 3/4 − 9/12 = 0 exactly — all confirmed. Parafermion identification: SU(2)₃/U(1) = ℤ₃ parafermions, c = 2(k−1)/(k+2) = 4/5 — confirmed. Spin field σ_ℓ has h = ℓ(k−ℓ)/(2k(k+2)); for k=3, ℓ=1: 2/30 = 1/15 — confirmed. The "non-free residue localizes in the parafermion coset" reading is arithmetically exact and a genuinely nice structural observation; note c = 4/5 is the (5,6) minimal model (3-state Potts), also φ-bearing and non-free, so the localization is consistent.

**Lattice observations.** Reading A: q = m/√6 from h = q²/2 = m²/12 — confirmed; ratios 1/√3 and √(2/3) to the k=1 (1/√2 spacing) and k=2 (1/2 spacing) lattices, both irrational — confirmed, no convention slip; the two readings are properly level-tagged and not mixed. Reading B: denominators 4→8→12 = 4k — confirmed. {m²/12} ∩ {n²/4} = {0}: m² = 3n² forces 3 | m, then 3 | n, infinite descent; insoluble in nonzero integers — confirmed.

**Fib ⊠ anti-semion.** Product weights: (τ,1) → 2/5 = h_1; (1,s̄) → 3/4 = h_{3/2}; (τ,s̄) → 23/20 ≡ 3/20 = h_{1/2} (mod 1); c: 14/5 + 7 ≡ 9/5 (mod 8) — all confirmed. Scoping to mod-1 spins and mod-8 central charge, with VOA isomorphism explicitly disclaimed, is exactly the right discipline; as an MTC-level factorization this is standard and correct. Adequate.

## The rescue attempt (mandated)

I attempted seriously to construct a free realization of SU(2)₃ or break the obstructions.

**(a) Is the classification "free ⇒ d ∈ {2^{m/2}}" correct and complete?** Under the pinned sense of "free" (stacks of free Majoranas and free compact lattice bosons), yes. n Majoranas yield Ising-type sectors with d ∈ {1, √2, 2, …} ⊂ ℤ[√2]; lattice bosons yield pointed categories, all d = 1; Deligne products stay in ℤ[√2], so d² ∈ ℤ throughout. φ ∉ ℤ[√2] (φ lives in ℚ(√5), and φ² = φ + 1 ∉ ℤ). Since quantum dimension is an invariant of the braided category and inherited by any fusion subcategory, no free-stack MTC can contain a φ-dimensional object, let alone equal SU(2)₃. "Free parafermions" (Baxter–Fendley clock chains) are integrable, generically non-Hermitian spectral constructions — not free-field CFTs in the pinned sense; they do not produce a unitary chiral algebra with ½ℤ central charge. Higher-dimensional lattice fermions reduce, at the level of the induced 2d chiral data, to Majorana stacks. W-algebra constructions (e.g., via cosets) are not free by definition. **Route fails.**

**(b) Embeddings and cosets — the real pressure point.** SU(2)₃ **can** be embedded in a free theory: the diagonal embedding SU(2) ↪ SU(2)₁ × SU(2)₁ × SU(2)₁ carries level 1+1+1 = 3, and SU(2)₁³ is free (three lattice bosons at the self-dual radius; equivalently realizable from free fields, c = 3). So the level-3 currents are honestly constructible from free fields. Does this fire the registered kill ("admits a free-field realization")? I rule **no**, on two grounds. First, precedent: the k = 2 gate was ruled FREE because SU(2)₂ **is** three Majoranas — central charges match (3/2 = 3 × 1/2), zero coset remainder; realization there meant isomorphism. Second, vacuousness: the diagonal-in-SU(2)₁^k construction embeds **every** SU(2)_k in a free theory, so the embedding reading would make the free/non-free distinction empty — including retroactively at k = 1, 2. The discriminating invariant is the commutant: for k = 3 the coset (SU(2)₁³)/SU(2)₃ has c = 3 − 9/5 = 6/5 ≠ 0, so the embedding has a nontrivial commutant and the free theory's sectors decompose into SU(2)₃ ⊗ coset modules rather than restricting to SU(2)₃'s MTC. A conformal embedding (c-preserving) into a free theory would require a free theory with c = 9/5 ∉ ½ℤ — impossible. **Ruling: "admits a free-field realization" = isomorphism of chiral data (equivalently, MTC equivalence with matching c mod 8), not embedding. Route fails as a rescue but forces a wording clarification (C-AH2).**

**(c) c mod 8 escape via E₈ stacking.** Stacking with (E₈)₁ (c = 8, free, trivial MTC) shifts c by 8 and leaves the MTC unchanged — that is exactly why c mod 8 is the right invariant. 9/5 mod 8 remains outside ½ℤ + 8ℤ, and stacking cannot alter the φ quantum dimensions. **Route fails.**

**(d) Non-chiral escape.** The full SU(2)₃ WZW (c_L = c_R = 9/5) has c_− = 0, and the doubled category Fib ⊠ Fib̄ (inside the double of SU(2)₃) is realizable as a string-net/Levin-Wen lattice model — but a lattice string-net is not a free-field theory, and more decisively, the record's gated object is the **chiral** MTC with its chiral central charge; non-chiral doubling destroys precisely the invariants under test. **Irrelevant to the chiral record; route fails.**

**Rescue conclusion: no free realization exists.** The two obstructions (d² ∉ ℤ; c mod 8 ∉ ½ℤ) are independent, categorical invariants, and both are fatal. The substance of the submission's non-free ruling is CONFIRMED.

## Adjudication of the kill-label inversion

Registered wording: **K-SU23-1 fires IF SU(2)₃ admits a free-field realization.** The submission's finding — no free realization, which I independently confirm — is the negation of the firing condition. Therefore **K-SU23-1 DOES NOT FIRE**. The submission's verdict box ("K-SU23-1: KILL FIRES — no free realization") asserts the correct substance under an inverted label; this is a pure semantic error, presumably from conflating "the free-realization hypothesis is killed" with "the registered kill fires." The record must enter: K-SU23-1 DOES NOT FIRE; the "first non-free gate" claim survives; the gate PASSES and the SU(2)₂-era gap ("non-abelian ≠ non-free") is closed at k = 3. Kill wording asymmetry noted for the ledger: this kill was registered so that firing = gate escalation, not gate success — future verdict boxes must quote the registered conditional verbatim before ruling.

**K-SU23-2** (channel rates finite, distinct where claimed, well-defined, pure data): D_j = (0, 3ℓ/10, 4ℓ/5, 3ℓ/2) are finite, pairwise distinct, and determined by (h, ℓ) alone; channel labels are superselection data; outcome selection is properly quarantined. **DOES NOT FIRE.** Caveat carried forward unchanged: the candidate D_λ = 2h_λℓ itself remains underived (GAP-N1); K-SU23-2 gates the candidate's internal well-formedness, not its truth.

## Corrections ledger

- **C-AH1 (substantive, record-critical):** Verdict-box label inverted. "K-SU23-1: KILL FIRES — no free realization" must read "K-SU23-1: DOES NOT FIRE — no free realization exists; gate passes as first non-free gate." Substance unchanged.
- **C-AH2 (clarification, binding going forward):** The non-free ruling must pin "admits a free-field realization" to isomorphism/MTC-equivalence level. SU(2)₃ embeds in the free theory SU(2)₁³ (diagonal, commutant c = 6/5); the embedding reading would vacuously "free" every SU(2)_k. The subcategory-inheritance argument in the submission is unaffected (a VOA embedding with nontrivial commutant does not make SU(2)₃'s MTC a fusion subcategory of the free MTC), but the wording should say so explicitly.
- **C-AH3 (minor):** "Free quantum dimensions lie in {2^{m/2}} ∪ {1}" — the airtight invariant statement is d ∈ ℤ[√2] (hence d² ∈ ℤ) for the pinned free class; the union-with-{1} phrasing is redundant/imprecise but the conclusion is unaffected.
- **C-AH4 (typographical):** "S_{½½} = √(2/5)sin(4π/5) ≈ 0.37175/𝒟·…" is garbled; the value 0.37175 is correct as stated elsewhere and 𝒟S_{½½} = 1 exactly.

## VERDICT BOX

1. All modular data, sum rules, channel defects, coset remainders (1/15 twice; σ₁ at c = 4/5 correct), and lattice arithmetic: VERIFIED independently.
2. Non-free ruling: CONFIRMED — rescue attempted and failed on all four routes; obstructions (φ² ∉ ℤ, c = 9/5 mod 8 ∉ ½ℤ) are categorical invariants; "realization" pinned to isomorphism (C-AH2).
3. K-SU23-1: **DOES NOT FIRE** under registered wording; submission's "KILL FIRES" label is a semantic inversion (C-AH1) — substance correct, label must be corrected in the record.
4. K-SU23-2: DOES NOT FIRE — channel rates finite, distinct, pure data (candidate still underived per GAP-N1).
5. Gate ruling: SU(2)₃ **PASSES** as the program's first genuinely non-free non-abelian gate.

Word count: approximately 1,960.
