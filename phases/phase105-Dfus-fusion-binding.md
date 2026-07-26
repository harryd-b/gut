# Phase 105 — fourth entry candidate: D_fus — fusion, binding, annihilation (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** The proposed fourth entry: the composition law of same-axis defects. Headline claims (pre-verdict): fusion is profile addition with D(pair) = (Q₁+Q₂)²ℓ/2π depending only on total charge (split-independent); the binding term ΔD = Q₁Q₂ℓ/π is exactly the POLARIZATION of the per-geodesic quadratic form (like charges super-additive — repulsion-as-data; opposite sub-additive), while the cross-geodesic entry D₁₂ remains a separate topological object — the two do not mix; charge–anticharge pairs are INNER — vacuum class, finite erasure cost, genuinely vacuum fluctuations (stronger than rate-zero, via a compact-support representative licensed by the refereed locality theorem, with the hypothesis-transfer caveats flagged); and the QUADRATIC-REFINEMENT IDENTITY holds: D_spin(Q₁+Q₂) − D_spin(Q₁) − D_spin(Q₂) = ∓Q₁Q₂ — the spin form is the quadratic refinement of the mutual-statistics pairing, descending mod 2 on the lattice to spin parity (−1)^q — exactly the algebraic setting of Arf invariants (census connection flagged conjecture-only). All "binding/annihilation" language is rate-arithmetic on static states: no dynamics, no potential, no winding sectors. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# Dictionary Entry: Fusion, Binding, Annihilation (same-axis)

Standing conventions: hyperbolic γ with axis arc I = (ξ₋, ξ₊), translation length ℓ; ‖f‖² = 2πΣ_{k≥1} k|f̂_k|² (homogeneous H^{1/2}, hence Möbius/scale covariant); refereed entries E1–E3, C-D5, D-MS, S1-i as cited.

---

## 1. Fusion additivity and split-independence

**Fusion rule.** For same-axis profiles η₁, η₂ with densities on I, the composite defect is implemented by W(η₁)W(η₂) = e^{−iσ(η₁,η₂)/2} W(η₁+η₂). Two remarks: (a) under C-D5 the same-axis pairing is assigned σ = 0; (b) even without C-D5, the scalar phase cancels in Ad W(·), so the composite *state* is the state of the single profile η₁+η₂ unconditionally. Charge additivity is immediate:

**Q_tot = ∫_I (η₁+η₂)′ = Q₁ + Q₂.**

**Split-independence of the existence entry.** Run E1 on η := η₁+η₂, which lies in the same profile class (smooth, density concentrated near/on I). In the line frame conjugate γ to x ↦ e^{ℓ}x on ℝ, repelling point 0, attracting ∞. Then

ζ^{(n)}(x) = η(x) − η(e^{nℓ}x) = ∫_{e^{nℓ}x}^{x} (η₁+η₂)′.

For fixed x in the axis region, e^{nℓ}x runs past the entire combined support as n → ∞, so ζ^{(n)}(x) → −(total accumulated charge ahead of x) and, across the repelling point, ζ^{(n)} develops a near-jump whose height is the *total* accumulated charge Q₁+Q₂ — regardless of how the density is split between η₁′ and η₂′, because only the integral ∫(η₁+η₂)′ over the swept region enters. Structurally: ζ^{(n)} = (Q₁+Q₂)·s^{(n)} + r^{(n)}, where s^{(n)} is the unit near-jump of E1 (inner scale e^{−nℓ}, outer scale O(1)) and r^{(n)} carries the internal two-bump structure, rescaled conformally. Since the homogeneous H^{1/2} norm is scale invariant, ‖r^{(n)}‖ = O(1) uniformly in n; hence

‖ζ^{(n)}‖² = (Q₁+Q₂)² ‖s^{(n)}‖² + O(‖s^{(n)}‖) = (Q₁+Q₂)² · nℓ/2π + O(√n),

by Cauchy–Schwarz on the cross term. Therefore

**▣ D(pair) = (Q₁+Q₂)² ℓ / 2π — dependent only on the total charge, not on the split of density over I.**

This is the same accumulation/line-frame argument as refereed E1 ("only total accumulated charge enters the near-jump height"), applied to η₁+η₂, which satisfies E1's hypotheses. [GAP — minor] The uniform O(1) bound on ‖r^{(n)}‖ uses smoothness/bounded variation of the combined density; this matches E1's smearing hypothesis but I have not re-verified E1's remainder estimate is stated with the uniformity needed when the density has widely separated bumps inside I (self-similarity of H^{1/2} makes this plausible at E1's rigor level, not beyond it).

## 2. Binding = polarization

Define ΔD := D(pair) − D(Q₁) − D(Q₂). From Task 1 and E1:

**▣ ΔD = 2Q₁Q₂ · ℓ/2π = Q₁Q₂ ℓ/π.**

Sign reading: like charges give ΔD > 0 — the pair's record is strictly super-additive, costlier to erase together than separately ("repulsion-as-data"); opposite charges give ΔD < 0 (sub-additive, "attraction-as-data"). Algebraically, ΔD is exactly the polarization of the quadratic form D(Q) = (ℓ/2π)Q²: ΔD(Q₁,Q₂) = D(Q₁+Q₂) − D(Q₁) − D(Q₂) = 2B(Q₁,Q₂) with B the associated bilinear form.

Contrast with the refereed structural note: the *cross-geodesic* entry D₁₂ = Q₁Q₂·î is **not** the polarization of D — it is topological (integer crossing number, no ℓ), a different kind of object. The *same-geodesic* binding **is** the polarization.

**▣ Structure: per geodesic, the dictionary carries a metric quadratic form D_γ(Q) = Q²ℓ(γ)/2π whose polarization is the binding term; across distinct geodesics it carries an independent topological pairing Q₁Q₂·î. The two do not mix.**

**Honesty flag (mandatory).** D is an erasure-cost *rate* (growth rate of a one-particle H^{1/2} norm under iterated γ), not an energy. "Binding" and "repulsion" here are analogical labels for super-/sub-additivity of that rate. No Hamiltonian, force, or potential is defined or implied.

## 3. Annihilation (Q₂ = −Q₁)

The combined profile η₁+η₂ is smooth with ∫_I (η₁+η₂)′ = 0.

**Hypothesis transfer to S1-i.** S1-i requires: smooth defect, total charge 0, density compactly supported (in a proper open interval J ⊂ S¹, so that W ∈ A(J) and locality applies). Adjudication: since the refereed locality result says the defect state on A(I) depends only on η′|_I, we may pass to any global representative with the same density on I. Choose ĥ with ĥ′ = (η₁+η₂)′ on I and ĥ′ ≡ 0 outside a small neighborhood I_ε; a smooth single-valued such ĥ exists **iff** ∫_I (η₁+η₂)′ = 0 — which is exactly the present case. (For Q_tot ≠ 0 no such compact representative exists; ∫_{S¹}η′ = 0 forces a compensating charge −Q_tot elsewhere.) With ε small enough that J = I_ε is a proper arc, S1-i applies verbatim: the pair state is implemented by the local Weyl unitary W(ĥ) ∈ A(J) and is **inner** — unitarily in the vacuum class.

**▣ Charge–anticharge pairs on one geodesic are erasable: the pair state is inner, vacuum class; D(pair) = 0 exactly — a fixed local unitary at finite cost erases it, not merely a vanishing rate.**

Distinction, carefully: *rate zero* would only mean ‖ζ^{(n)}‖² = o(n) (cost may still diverge); *inner* means finite total cost and membership in the vacuum folium. The argument via S1-i establishes the stronger statement, **inner**, provided the compact-support representative exists. [GAP] Two caveats on the transfer: (i) if the individual densities have non-compact tails ("concentrated near I" but not supported in I ∪ small closed neighborhoods), the compact-support hypothesis of S1-i fails for the literal profile, and only the representative-swap argument above rescues it — this swap changes the state only on A(J), which is exactly what the refereed locality theorem licenses, but I flag that S1-i's referee report should be checked for whether "vacuum class" was proved for the state on A(J) or for a global state; (ii) if ∫_I η₂′ = −∫_I η₁′ holds only for the charges *in I* while the compensating return densities of η₁, η₂ sit in different far regions, the global combined density is chargeless but possibly not single-interval-supported; the representative swap handles this too, same caveat.

## 4. The quadratic-refinement identity

From E3 at framing n = 0: D_spin(Q) = ∓Q²/2. Direct computation:

**▣ D_spin(Q₁+Q₂) − D_spin(Q₁) − D_spin(Q₂) = ∓Q₁Q₂.**

The right side is the mutual-statistics exponent at one crossing: the refereed cross-geodesic pairing is D₁₂ = Q₁Q₂·î with commutator phase e^{−iσ}, so at î = 1 the braiding exponent is (up to the orientation sign fixed jointly with D-MS) ∓Q₁Q₂. Hence **the spin form is the quadratic refinement of the mutual-statistics pairing**: q(x+y) − q(x) − q(y) = b(x,y) with q = D_spin, b = ∓Q₁Q₂.

Precision about configurations: this is an identity of *forms*, i.e., of the functions Q ↦ D_spin(Q) and (Q₁,Q₂) ↦ b(Q₁,Q₂), not of any single configuration's phase. The left side is evaluated using the same-axis fusion rule Q₁+Q₂ of Task 1 (where σ = 0 under C-D5 — that vanishing does **not** enter and does not conflict: b on the right is the value the pairing *takes* at one crossing, realized by a configuration of two defects on distinct geodesics crossing once, î = 1). Sign consistency: the ∓ branch in D_spin and the sign of the braiding exponent are correlated through the same orientation convention fixed by D-MS; the identity holds branch-by-branch. [GAP] I have not independently re-derived this sign correlation from first principles; it is taken from the joint refereed conventions — if D-MS and the crossing orientation were fixed independently, a relative sign check is outstanding.

**Lattice case** (Q = q√(2π), q ∈ ℤ): D_spin = ∓πq², so the spin phase is e^{∓iπq²} = (−1)^{q²} = (−1)^q:

**▣ Spin parity = (−1)^q; the refinement identity descends mod 2 to q̄: Λ/2Λ → ℤ/2 refining the even pairing — exactly the algebraic setting of quadratic refinements and their Arf invariants.**

[GAP — flagged as conjecture-level gloss] The connection to an Arf-invariant census of defect sectors (e.g., counting spin structures / classifying the mod-2 refinements realized by the dictionary) is *not derived here*; only the algebraic identity above is established.

## 5. Honest limits

- **No dynamics.** Nothing here describes an annihilation *process*; Task 3 is a statement of class membership (vacuum class) of a static pair state. No time evolution, no scattering.
- **Binding is rate-arithmetic.** ΔD is super/sub-additivity of an erasure-cost rate; no energy, force, or thermodynamic quantity is claimed.
- **No distance, no potential.** On a single geodesic the refereed anchoring/locality theorem places the visible charge at the shared fixed points ξ±; there is no notion of "separating" the two same-axis defects, hence no distance variable and no distance-dependent potential exists or is claimed. ΔD is a single number per (Q₁,Q₂,ℓ).
- **Zero-mode / compactification caveats.** All profiles here are smooth single-valued functions on S¹, so ∫_{S¹}η′ = 0: every "charge Q in I" carries a compensating −Q elsewhere, and the constant mode (k = 0) is absent from both σ and ‖·‖. Genuinely charged (winding) sectors of the compactified boson — multivalued η, lattice Q = q√(2π) as global charge — are outside the derivation except where explicitly invoked in Task 4's lattice gloss. [GAP] The Task 3 innerness argument uses single-valuedness essentially (existence of the compact representative ĥ); its extension to winding sectors is not addressed.

## Summary (5 lines)

1. Fusion: same-axis defects fuse by profile addition; D(pair) = (Q₁+Q₂)²ℓ/2π depends only on total charge (split-independent, E1-level rigor).
2. Binding ΔD = Q₁Q₂ℓ/π is exactly the polarization of the per-geodesic quadratic form D; the cross-geodesic pairing is a separate topological object.
3. Charge–anticharge pairs are inner (vacuum class, finite erasure cost), via a compact-support representative licensed by locality — stronger than rate-zero, modulo the flagged S1-i hypothesis-transfer caveat.
4. D_spin is the quadratic refinement of the one-crossing mutual pairing, ∓Q₁Q₂; on the lattice, spin parity (−1)^q; Arf census is conjecture-level only.
5. All "binding/annihilation" language is arithmetic of erasure-cost rates on static states; no dynamics, no potential, no winding sectors.
