# Referee report — NONAB kill checks (phase113-NONAB-kill-checks.md)

**Date:** 2026-07-26
**Referee:** context-free adversarial agent (all arithmetic re-derived from scratch; no arithmetic error found anywhere).
**Editorial note (operator):** Preserved VERBATIM below. Verdicts: **K-NONAB-1 survival REFEREED** (level-1 formula consistency, scoped as stated); **K-FRAC-1 arithmetic CONFIRMED but the registered kill wording is vacuously satisfiable (C-Z1)** — the survival is refereed only as the index-3/ratio statement, and NONAB-FRAC must be re-registered with the singlet-unit normalization pinned. Corrections C-Z1..C-Z3 entered in the phase file's Amendment.

---

## REPORT (VERBATIM)

# Referee report — Phase 113 continuation (K-NONAB-1 / K-FRAC-1), context-free adversarial pass, 2026-07-26

All arithmetic re-derived from scratch against `phases/phase113-NONAB-kill-checks.md`, `phases/phase113-NONAB0-scoping.md`, `phases/phase104-JOIN4a-prime-derivation.md`, `phases/phase107-KNOTQ-round2-bridge-definition.md` A.6.

## Mandate A — §1 (K-NONAB-1): CONFIRMED (one wording correction, C-Z3)

**Lattice normalizations.** |α|² = 2 ⇒ current h = |α|²/2 = 1 ✓ (currents must have h = 1, so the h = q²/2 convention is internally consistent at q = √2). Root lattice √2ℤ; fundamental weight α/2, |α/2|² = 1/2 ⇒ weight lattice (1/√2)ℤ; P/Q_root ≅ ℤ₂ ✓. Coset check: −1/√2 + √2 = 1/√2, so ±1/√2 lie in one coset ✓. h(1/√2) = (1/2)/2 = 1/4; Kac: h_{j=½} = j(j+1)/(k+2) = (3/4)/3 = 1/4 ✓. So q = ±1/√2 is a genuine point of the extended arena's sector lattice (it is the generator), and the identification is consistent.

**Numbers.** D_abelian = Q²ℓ/2π = (1/2)ℓ/2π = ℓ/4π; candidate 2h_λℓ/2π = 2·(1/4)·ℓ/2π = ℓ/4π. Equal ✓.

**E1 integrality audit — independently executed on phase 104.** Q = c|I| with c ∈ ℝ throughout; the derivation distinguishes only c = 0 vs c ≠ 0. Jump-height step: a plateau of height Q smoothed at scale e^{−nℓ} has |ĝ_k|² ≈ Q²/4π²k², and 2πΣ_{k≤e^{nℓ}} k·Q²/4π²k² = (Q²/2π)nℓ + O(1) — I reproduce this ✓; Gagliardo cross-term 2Q²nℓ, ‖·‖² = G/4π ⇒ same coefficient ✓; spectral-density route (2π/ℓ)(Q²ℓ²/4π²) = Q²ℓ/2π ✓. All three are polynomial in real Q. The function-not-map claim is verbatim in phase 104 §1(a): the honest functional is well defined because ∫_{S¹}η′ = 0; η is real-valued, so no winding quantization constrains c. **The refereed E1 derivation is integrality-free — verified.**

**Kink ≡ plateau.** Shift by coset representative α/2: charge |α|/2 = 1/√2, h = 1/4 = h_{j=½} ✓.

**Convention stability (C-Z3, minor).** "Rescaling ‖·‖² by κ rescales D and (via the same convention) Q² identically" is loosely worded: Q = ∫_I η′ is coordinate-invariant and does *not* rescale; what rescales is the effective charge appearing in h = Q²/2 (the state ω(W(f)) = e^{−‖f‖²/2} changes with the norm). The invariant content — D/(2h) is convention-stable, so the agreement D = 2hℓ/2π is κ-independent — is correct; restate it that way.

**GAP-N8 fairness.** Fair and correctly deflated: abelian-side h = Q²/2 holds identically, and the candidate was defined as 2hℓ/2π, so at level 1 the check reduces to E1's own identity plus exactly the three listed verifications (integrality-freeness; arena membership of 1/√2; kink ≡ plateau). No overclaim found; the ledger's scope guard ("nothing here computes a genuinely non-abelian rate") correctly concedes that D for the SU(2)₁ net itself remains undefined (GAP-N1), so this is a formula-consistency check, as stated.

## Mandate B — §2 (K-FRAC-1): arithmetic CONFIRMED; registration wording PARTIAL (C-Z1)

**Decomposition.** v = (Q/3)(1,1,1) + w ✓; e = (1,1,1)/√3, q_b = Q/√3 ∈ (1/√3)ℤ ✓. Fermion (1,0,0): w = (2/3,−1/3,−1/3), |w|² = 6/9 = 2/3, h_su(3) = 1/3 = (4/3)/(1+3) ✓; h_u(1) = (1/3)/2 = 1/6; 1/3 + 1/6 = 1/2 ✓. Singlets: w = 0 ⟺ v = m(1,1,1) ⟺ Q ∈ 3ℤ, q_b = m√3 ✓; h(e^{i√3φ}) = 3/2 = |(1,1,1)|²/2 ✓; (1/√3)ℤ/√3ℤ ≅ ℤ₃ ✓ (index √3 ÷ 1/√3 = 3).

**Triality identity.** Both t and Q mod 3 are homomorphisms ℤ³ → ℤ₃ killing e₁−e₂, e₂−e₃ ✓; projection is linear, projected eᵢ are the weights of the 3, and wᵢ − wⱼ = eᵢ − eⱼ ∈ roots, so all three eᵢ map to the fundamental-weight coset ✓; agreement on the basis e₁,e₂,e₃ forces equality ✓. One pedantic note: the identity as an *equation* uses the isomorphism P/Q_root ≅ ℤ₃ sending [ω₁] ↦ 1 (the other choice gives t ≡ −Q mod 3); the invariant content (ker t = {Q ∈ 3ℤ}) is choice-free. Spin check (3, q_b = 1/√3): h = 1/2, fermionic ✓; ℤ₃-class of q_b matches t ✓.

**No-reassignment.** (i) Schur is airtight: the commutant of the irreducible 3 is ℂ·1, so any u(1) in u(3) commuting with su(3) is a diagonal multiple, and fermion-at-charge-1 pins it — Q = Σnᵢ forced ✓. (ii) "Fermions generate ℤ³" is exactly right: e₁,e₂,e₃ *are* the standard basis (with conjugates, the generated subgroup is all of ℤ³), so an additive δ with δ(eᵢ) = 0 vanishes identically ✓ (and even a ℤ₃-level reassignment fails: Hom(ℤ₃, ℝ) = 0). (iii) A t = 0 vector with Q ∉ 3ℤ would contradict the identity — no such lattice point ✓. Index-3 statement forced.

**C-Z1 (substantive).** The submission's own concession — "in raw fermion units every charge is an integer" — collides with K-FRAC-1's registered wording (scoping §c): "if a consistent sector assignment exists giving integer u(1) charges to triality-≠0 sectors … the conjecture is dead." Read literally, such an assignment trivially exists (fermion units), and the mechanism clause "in the normalization where N-ality-0 composites are integer-charged" fails to exclude it (3ℤ ⊂ ℤ: fermion units also make singlets integer-charged). The kill survives only under the registered clause's second half ("i.e. the branching does not force the (1/3)ℤ refinement"), read as: refinement relative to the unit *pinned to the minimal N-ality-0 singlet charge*. The submission correctly isolates this as the normalization-independent invariant — charge(fermion)/charge(minimal singlet) = 1/3, equivalently the forced index-3 of 3ℤ in ℤ — and that ratio is genuinely forced (Schur fixes Q up to overall scale; ratios are scale-free). **Correction:** NONAB-FRAC and K-FRAC-1 must be re-registered with the normalization pinned ("u(1) unit = minimal triality-0 singlet charge") or as the pure index/ratio statement; as registered, the wording is literally satisfiable and the kill vacuous. The concession does not undercut the mathematics; it exposes the registration.

## Mandate C — GAP-N7: CONFIRMED in substance (editorial correction C-Z2)

The fork is real: C-BRIDGE (phase 107 A.6, quoted exactly: "Q = ±n, D = n²ℓ(γ)/2π") has image ℤ·1, and (1/√2)ℤ ∩ ℤ = {0} (m/√2 ∈ ℤ ⇒ m = 0), so the bridge misses not just ±1/√2 but every nonzero sector of the self-dual arena. Resolution (b)'s number checks: unit = 1/√2 ⇒ D = (n/√2)²ℓ/2π = n²ℓ/4π ✓ vs original n²ℓ/2π ✓. **C-Z2:** two garbled clauses: "meets its image only in even multiples of nothing" should read "(1/√2)ℤ ∩ ℤ·1 = {0}"; and "the abelian record's D = n²ℓ/2π becomes the even-sublattice statement" is numerically loose — on the even sublattice (n = 2m in generator units) D = m²ℓ/π, which is not of the form n²ℓ/2π under any integer relabeling. The correct statement: the local (root/even-lattice) sectors are the even integers in generator units, with D = m²ℓ/π. Strike or restate; the fork's disjunction (arena-dependent unit vs bulk blindness) stands.

## Mandate D — registered wording vs tested

K-NONAB-1: no drift — the scoping's item 1 (Q² = 1/2, compare refereed D vs 2h_λℓ/2π) is exactly what was executed, and its pre-flagged normalization caveat was discharged (the audit) and honestly promoted to GAP-N7. K-FRAC-1: drift found, as in C-Z1.

## VERDICT

- **Mandate A: CONFIRMED** (C-Z3 wording). **K-NONAB-1 survival may enter the record as refereed**, scoped exactly as stated (level-1 formula consistency; GAP-N8 deflation stands; no non-abelian rate computed).
- **Mandate B: arithmetic CONFIRMED; PARTIAL as registered** (C-Z1). **K-FRAC-1 survival may enter as refereed only as the index-3/ratio statement**, with NONAB-FRAC's registration corrected accordingly; under the literal registered wording the kill is vacuously satisfiable and no survival claim is well-posed.
- **Mandate C: CONFIRMED** (C-Z2 editorial). GAP-N7 is a genuine unresolved fork; GAP-N8 correctly registered.
- **Corrections: C-Z1** (re-register NONAB-FRAC/K-FRAC-1 with the singlet-unit normalization pinned, or as the index statement); **C-Z2** (restate the two garbled GAP-N7 clauses); **C-Z3** (restate convention stability as κ-invariance of D/2h, since Q = ∫η′ itself does not rescale).

No arithmetic error found anywhere in §1 or §2; every number re-derived independently agrees.
