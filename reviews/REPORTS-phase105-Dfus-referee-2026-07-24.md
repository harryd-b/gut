# REPORT — phase 105 D_fus referee pass (2026-07-24, verbatim)

*Context-free adversarial referee on the D_fus derivation (phases/phase105-Dfus-fusion-binding.md), run per standing pre-verdict policy; verified numerically (2²¹-point FFT, Möbius invariance of the discrete norm to 15 digits). Summary: fusion/split-independence CORRECT with the flagged remainder gap CLOSED BY THE REFEREE (Möbius-invariance argument, uniform bound, error improved to O(1)); binding = polarization CORRECT; annihilation core fact CORRECT but formulation repaired — the collar loophole makes the "slightly larger algebra" notion vacuous, and the sharp dichotomy is: local Weyl implementer in A(I) itself ⟺ total charge zero; the quadratic-refinement identity CORRECT at zero framing with the framing constraint now mandatory and the branch–crossing sign correlation recorded as genuinely open; and one substantive scope finding (item 5): every single-valued globally-compensated profile has D = 0 identically — E1's rate Q²ℓ/2π is the I-LOCAL (truncated-cocycle) erasure rate, not a global-difference rate — the dictionary's first entry measures the cost of LOCAL erasure. Verdicts entered in the derivation document's amendment. Report verbatim below; standing AI-referee caveat applies.*

---

All checks complete. Numerics: winding profiles (density purely in I) reproduce the predicted increment 0.17905 for both charge splits with remainder plateauing at 1.490 ≤ 2‖ψ‖; single-valued compensated profiles saturate (rate 0). Report follows.

---

# Referee Report: Fusion / Binding / Annihilation / Refinement (D_fus)

**Numerical setup used.** Disk automorphism γ_a(z)=(z+a)/(1+az), a=tanh(ℓ/2), ℓ=0.5; fixed points z=±1; norm 2πΣ_{k≥1}k|f̂_k|² on 2²¹-point FFT grid. Möbius invariance of the discrete norm verified to 15 digits.

## 1. FUSION / SPLIT-INDEPENDENCE — CORRECT (flagged gap is real but closable exactly as hinted; I close it)

- **Central phase:** Ad(cU)=Ad(U) for |c|=1; composite state = state of η₁+η₂, Q_tot = Q₁+Q₂. CORRECT.
- **Accumulation formula:** ζ⁽ⁿ⁾(x) = η(x)−η(e^{nℓ}x) = ∫_{e^{nℓ}x}^x (η₁+η₂)′ is exact; the near-jump height is the total charge crossed, ∫_I(η₁+η₂)′ = Q₁+Q₂, independent of the split. CORRECT.
- **Remainder bound (the gap):** closable, and uniformly. Set ψ := (η₁+η₂) − Q_tot·s₀ (s₀ the unit reference profile). ψ has zero total charge with density in I, hence is (mod constant) a fixed single-valued H^{1/2} function, and r⁽ⁿ⁾ = ψ − ψ∘γⁿ. Since γⁿ is Möbius and the homogeneous norm is Möbius-invariant, ‖ψ∘γⁿ‖ = ‖ψ‖, so **‖r⁽ⁿ⁾‖ ≤ 2‖ψ‖ uniformly in n** — the "fixed function composed with the flow" mechanism works verbatim. Widely separated bumps only enlarge the constant ‖ψ‖ (it degrades as bumps approach ∂I), never the n-dependence. Numerics: ‖r⁽ⁿ⁾‖ plateaus at 1.4902 ≤ 2‖ψ‖ = 2.1074 by n=6.
- **Cross term:** Cauchy–Schwarz gives 2Q_tot|⟨s⁽ⁿ⁾,r⁽ⁿ⁾⟩| ≤ C√n. CORRECT, but not sharp: η₁+η₂ satisfies E1's hypotheses directly, so O(1) is already available. State O(1).
- **Numerics:** increments of ‖ζ⁽ⁿ⁾‖² for split (1.0, 0.5) and for a single bump of charge 1.5 both converge to 0.1801 → predicted Q_tot²ℓ/2π = 0.17905 (residual ~0.5% still decreasing at n=12). Split-independence confirmed.

## 2. BINDING = POLARIZATION — CORRECT

ΔD = [(Q₁+Q₂)²−Q₁²−Q₂²]ℓ/2π = 2Q₁Q₂ℓ/2π = **Q₁Q₂ℓ/π**. Arithmetic correct. Signs: like charges give rate surplus, opposite charges deficit, exactly zero total at Q₂=−Q₁. One nit: ΔD is *twice* the polarization bilinear form B(Q₁,Q₂)=Q₁Q₂ℓ/2π under the convention B(x,y)=½[D(x+y)−D(x)−D(y)]; state which normalization "polarization" means. The structural contrast — same-axis binding is the polarization of one quadratic form on a single axis's charge lattice, cross-geodesic D₁₂=Q₁Q₂î is a pairing between distinct axes — is sound. The honesty flag (growth rate, not energy; "binding" is metaphor absent dynamics) is adequate and necessary.

## 3. ANNIHILATION — core fact CORRECT; formulation WRONG as stated on (a) and (b)

**(a) Existence-iff: WRONG as literally stated.** With ĥ′ prescribed only on I and merely required ≡0 *outside* I_ε, single-valuedness demands ∮ĥ′=0, which the collar I_ε∖I can absorb for **any** ∫_Iρ: existence is unconditional. The iff is true only if ĥ′ is required to vanish outside Ī (collar used solely for smoothing, no net collar charge): then a smooth single-valued ĥ exists ⟺ ∫_Iρ = 0.

**(b) Which algebra: the A(I)-restricted formulation is vacuous.** Any single-valued profile gives a vector state W(f)*Ω in the vacuum representation, so "normal/vacuum-class" per se has no content; worse, the collar trick of (a) plus locality implements the *restriction to A(I)* of **every** charge-Q defect by a Weyl unitary in A(I_ε) ⊋ A(Ī). So "vacuum on A(I) via a unitary in a slightly larger algebra" cannot detect Q=0. The right notion is implementation by a (Weyl) unitary **in A(I) itself** — equivalently, a *global* identity of states with a strictly I-supported implementer.

**(c) Corrected boxed statement.**
> **Annihilation.** Suppose supp(η₁+η₂)′ ⋐ I and Q₁+Q₂ = 0. Then the primitive P of (η₁+η₂)′ is smooth, single-valued, compactly supported in I, and the pair state equals ω∘AdW(P) *as a global state*, with W(P) ∈ A(I): it is inner in the strongest local sense, and D = 0. Conversely, if Q₁+Q₂ ≠ 0, any single-valued k with k′ = (η₁+η₂)′ on Ī must carry charge −Q in the open complement (∮k′=0), so supp k′ ⊄ Ī and no Weyl unitary in A(I) reproduces the I-data; implementation from A(I_ε), I_ε ⊋ Ī, is possible for every Q (collar compensation) and detects nothing. Sharp dichotomy: **the defect's I-data are those of a charge-zero local Weyl unitary in A(I) ⟺ Q₁+Q₂ = 0.** (If the densities are only concentrated near I, run the statement on a slightly larger arc J ⊃ Ī.)

The two flagged caveats point at the right neighborhood, but the collar loophole (b) is the actual issue; the prompt's proposed "extends to A(I_ε) vacuum-equivalent" cleaner statement is exactly the vacuous one and should be rejected. Numerics: annihilation cocycle norm² bounded (1.82–1.96, all n).

## 4. QUADRATIC REFINEMENT — arithmetic CORRECT at n=0; framing constraint is a GAP unless stated; descent CORRECT; sign-correlation is a real open check

- n=0: ∓[(Q₁+Q₂)²−Q₁²−Q₂²]/2 = ∓Q₁Q₂. CORRECT.
- **Framing:** excess = ∓Q₁Q₂ + ½[n_pair(Q₁+Q₂)² − n₁Q₁² − n₂Q₂²]. As an identity in (Q₁,Q₂) this forces n₁=n₂=n_pair=0. Common framing n₁=n₂=n_pair=n gives excess (n∓1)Q₁Q₂ — i.e., D_spin(·;n) refines the *shifted* pairing. The naive additive rule n_pair=n₁+n₂ yields excess ∓Q₁Q₂ + n₁Q₂²/2 + n₂Q₁²/2 + (n₁+n₂)Q₁Q₂ — not the claimed identity. The derivation must state the constraint (all framings 0, or fixed common framing with shifted pairing). GAP if unstated.
- **Mod-2 descent:** for Q∈ℤ, 2·D_spin = (n∓1)Q² and Q² ≡ Q (mod 2), so (−1)^{2D_spin} = (−1)^{(n∓1)Q} is a well-defined character; the parity's failure to be additive is governed by the even quantity 2Q₁Q₂ ≡ 0 (mod 2). Algebra CORRECT; caveat: (−1)^{D_spin} itself is ill-defined for odd Q at n=0 (half-integers) — use (−1)^{2q}.
- **Sign correlation:** REAL outstanding check. C-D5 only zeroes same-axis σ; D-MS only fixes the subtraction. Neither orients the crossing î relative to the ∓ branch; that linkage is an independent convention/datum, not derivable from the stated ones.

## 5. LIMITS — honesty flags fine EXCEPT the zero-mode caveat, which hides a genuine failure mode (adjudicated: WRONG under the naive reading; rate stands only in the winding/I-local formulation)

No-dynamics and no-anchoring flags: honest. **Zero-mode: one-line theorem —** if η is single-valued (so η ∈ Ḣ^{1/2}(S¹)), Möbius invariance gives ‖η−η∘γⁿ‖ ≤ ‖η‖+‖η∘γⁿ‖ = 2‖η‖ = O(1). **Every compensated single-valued profile has D = 0**, regardless of where the −Q sits. Numerically confirmed: with a smooth −Q_tot compensator in the open complementary arc, increments decay geometrically (ratio ≈ e^{−ℓ}) and ‖ζ⁽ⁿ⁾‖² saturates at 2‖η‖² ≈ 3.93. Mechanism: γ⁻ⁿ drives every compact piece of the complement to the *repelling* point too, building a canceling near-jump on the far side of ξ₋ — not a second jump at the attracting point, and not an O(1) correction. Consequently E1's Q is necessarily the charge of a **winding** profile (density in I only; η lives on the cover; only the differences ζ⁽ⁿ⁾ are in H^{1/2}, their wrap-jump canceling because γ fixes the endpoints). The refereed "smooth O(1) return at the attracting end" is the line-frame approach to the constant at x→∞ — the winding closure *through* the attracting fixed point — and is genuinely O(1); it is *not* the same object as a smooth compensating density in the open complementary arc. With this reading the rate Q²ℓ/2π stands (numerics: 0.180 → 0.17905), and locality is preserved provided D is defined via the I-supported cocycle rather than the global difference of a compensated profile. The derivation must say this explicitly; any statement implying a single-valued globally-compensated profile carries D = Q²ℓ/2π is false.

## Summary

1. Fusion/split-independence CORRECT; remainder gap closed rigorously by Möbius invariance (‖r⁽ⁿ⁾‖ ≤ 2‖ψ‖, uniform in n); error is in fact O(1), not just O(√n); rate 0.17905 confirmed numerically for both splits.
2. Binding = polarization CORRECT (ΔD = Q₁Q₂ℓ/π; factor-2 convention should be named); honesty flag adequate.
3. Annihilation: fact CORRECT, formulation WRONG as stated — collar loophole makes the A(I_ε) notion vacuous; corrected dichotomy: local Weyl implementer in A(I) itself ⟺ Q_tot = 0.
4. **Overall ruling on D_fus: CONFIRMED as a quadratic form in total charge on a fixed axis, D_fus(Q₁+Q₂) = (Q₁+Q₂)²ℓ/2π with split-independence — but only in the winding/I-local cocycle formulation; the spin refinement holds verbatim only at zero framing, and the branch–crossing sign correlation remains unproven.**
5. Zero-mode caveat is the one substantive danger: single-valued compensated profiles have D = 0 identically (proved and numerically verified); E1's rate survives only for winding profiles / the I-local cocycle — the derivation must be rewritten to say so.
