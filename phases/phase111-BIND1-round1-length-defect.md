# Phase 111 (continuation): BIND-1 round 1 — length-defect formula, well-definedness, descent, sign

**Date:** 2026-07-26
**Status:** DRAFTED — awaiting referee. No verdict entered in the BIND-1 registration (phases/phase111-BIND1-conjecture.md) until the referee pass completes.
**Provenance:** Context-free derivation agent executing the four registered BIND-1 round-1 mandates. The consultation below is preserved VERBATIM per house rules. Nothing has been edited.

**Editorial header (operator):**
- Headline claims (UNREFEREED until the referee verdict is entered as an amendment): (a) exact defect formula cosh(ℓ₁₂/2) = cosh(ℓ₁/2)cosh(ℓ₂/2) + cos θ·sinh(ℓ₁/2)sinh(ℓ₂/2); strict binding at every crossing angle; Δℓ bounded in (−2min(ℓ₁,ℓ₂), 0); saturation Δℓ → 4 ln cos(θ/2) for long constituents; K-BIND-3 does not fire (systole floor). (b) BIND-GAP-2 resolved-with-choice: one well-defined product class per crossing double coset; ℓ_min over the finite canonical set is a pair invariant; multiplicity possibly an excited spectrum. (c) MAIN RESULT: the trace identity is invertible — the crossing angle is a function of the length triple, so conditional on carrier status (= K-BIND-1, on which the arena is SILENT) and Q₁+Q₂ ≠ 0, the defect closes over three E1-type invariants and BIND-GAP-1 dissolves. (d) Both orientation channels bind; the crossing mechanism can NEVER deliver QCD-style excess (sharpening K-BIND-2); excess exists in the trace algebra only over non-crossing cosets, mechanism-free; 3D linking survey tagged SPECULATIVE (unit tangent bundle; Ghys knots-and-dynamics name-checked, unverified).
- New flags for the record: Δℓ is charge-blind and crossing-sign-blind — binding sign and interaction sign (D₁₂) are decoupled; neutral composites are E1-invisible, consistent with E4 annihilation.
- The referee is instructed to independently verify the trace identity and numerics, audit the double-coset algebra (including the centralizer and primitivity hypotheses), and check the E6 deck-unitary "concatenation echo" read against the entry-6 file.

---

## CONSULTATION (VERBATIM)

# BIND-1 derivation round — the length-defect formula, well-definedness, descent, and sign

**Summary with per-mandate verdicts.** (a) DERIVED and numerically verified: for crossing axes, cosh(ℓ(AB)/2) = cosh(ℓ₁/2)cosh(ℓ₂/2) + cos θ·sinh(ℓ₁/2)sinh(ℓ₂/2); the defect Δℓ is strictly negative at every crossing angle, strictly monotone in θ, bounded below by −2 min(ℓ₁,ℓ₂), with large-length saturation Δℓ → 4 ln cos(θ/2); total collapse ℓ₁₂ → 0 occurs only in the degenerate annihilation limit and is forbidden inside Γ by the systole — K-BIND-3 does not fire on either count. (b) The product class depends on a crossing only through its double coset; the canonical object is a finite set of ≤ i(c₁,c₂) product classes; the minimal length over it is a well-defined pair invariant — BIND-1 survives in amended form, with the multiplicity recorded as a possible excited spectrum. (c) POSITIVE (the round's main result): the identity is invertible, so θ is a function of the length triple; conditional on carrier status for c₁₂ (exactly K-BIND-1, on which the arena is SILENT) and on Q₁+Q₂ ≠ 0, BIND-GAP-1 dissolves — the defect closes over three E1-type data, no new datum needed. (d) Both orientation channels bind (defect only); length excess exists in the record's own trace algebra but only over NON-crossing cosets, where there is no concatenation point; 3D linking survey given [SPECULATIVE].

---

## §(a) The length-defect formula

**Derivation (self-contained).** Traces, lengths, and the crossing angle are conjugation invariants, so normalize in SL(2,ℝ): put the crossing point at i, axis(A) = the imaginary axis oriented upward, A = diag(e^{ℓ₁/2}, e^{−ℓ₁/2}). The rotation matrix R_t = [[cos t, sin t], [−sin t, cos t]] fixes i with derivative g′(i) = (cos t − i sin t)^{−2} = e^{2it}: it rotates the tangent space at i by 2t. So a hyperbolic B of length ℓ₂ whose oriented axis makes angle θ ∈ (0,π) with axis(A) at i is B = R_{θ/2} diag(e^{ℓ₂/2}, e^{−ℓ₂/2}) R_{θ/2}^{−1}. Direct multiplication gives

tr(AB) = 2[cosh(ℓ₁/2)cosh(ℓ₂/2) + cos θ·sinh(ℓ₁/2)sinh(ℓ₂/2)],

and since |tr| = 2 cosh(ℓ/2) for hyperbolic elements:

**[BOX-A] cosh(ℓ(AB)/2) = cosh(ℓ₁/2)cosh(ℓ₂/2) + cos θ·sinh(ℓ₁/2)sinh(ℓ₂/2),** θ = angle between the oriented translation directions.

This is the classical product trace identity for intersecting axes — Fenchel's cosine rule for line-matrices (*Elementary Geometry in Hyperbolic Space*); cf. Buser's trace relations (*Geometry and Spectra*, Ch. 2) [others' for attribution; the derivation above is self-contained, so no import is load-bearing]. Sanity anchors: θ = 0 gives cosh((ℓ₁+ℓ₂)/2) (same-axis composition, E4's regime); θ = π gives cosh((ℓ₁−ℓ₂)/2).

**(i) Strictness.** For θ ∈ (0,π): cos θ < 1 gives RHS < cosh((ℓ₁+ℓ₂)/2); cos θ > −1 gives RHS > cosh(|ℓ₁−ℓ₂|/2). cosh is strictly increasing, so

**|ℓ₁ − ℓ₂| < ℓ(AB) < ℓ₁ + ℓ₂, both strict, for ALL crossing angles.** Δℓ < 0 always, and ∂(RHS)/∂θ = −sin θ·sinh(ℓ₁/2)sinh(ℓ₂/2) < 0, so Δℓ is strictly decreasing in θ. AB is hyperbolic for every θ ∈ (0,π) except the degenerate ℓ₁ = ℓ₂, θ → π endpoint (below).

**(ii) Regimes.** Write L = ℓ₁+ℓ₂, S = sinh(ℓ₁/2)sinh(ℓ₂/2). Exactly: cosh(ℓ₁₂/2) = cosh(L/2) − (1−cos θ)S.

- **θ → 0:** Δℓ = −θ²·S/sinh(L/2)·(1 + O(θ²)). Grazing crossings bind quadratically weakly. (Numerics: ratio exact/leading = 1.000003 at θ = 0.01.)
- **θ = π/2:** the hyperbolic Pythagoras cosh(ℓ₁₂/2) = cosh(ℓ₁/2)cosh(ℓ₂/2); nothing singular — the defect is smooth and monotone through π/2.
- **Large lengths, fixed θ:** cosh, sinh → e^{x/2}/2, so cosh(ℓ₁₂/2) → (e^{L/2}/4)(1+cos θ) = (e^{L/2}/2)cos²(θ/2), hence

  **[BOX-A2] Δℓ → 4 ln cos(θ/2) as ℓ₁, ℓ₂ → ∞,** exponentially fast. Binding SATURATES: for long constituents the defect depends on the angle alone — a UV-insensitive, constituent-independent binding energy (at θ = π/2: Δℓ∞ = −2 ln 2 ≈ −1.386).
- **θ → π, fixed lengths:** ℓ₁₂ → |ℓ₁−ℓ₂|, Δℓ → −2 min(ℓ₁,ℓ₂) (open infimum).

**(iii) Bounds / K-BIND-3.** At fixed (ℓ₁,ℓ₂), Δℓ ranges over the bounded open interval (−2 min(ℓ₁,ℓ₂), 0): **bounded below — the unboundedness concern does not fire.** Collapse Δℓ → −(ℓ₁+ℓ₂), i.e. ℓ₁₂ → 0, requires cosh(ℓ₁₂/2) → 1, forcing ℓ₁ = ℓ₂ AND θ → π simultaneously: B degenerates to A⁻¹ (coincident reversed axis — no longer a crossing), and the composite class tends to the trivial class. That limit is the annihilation configuration, not a bound state. Inside cocompact torsion-free Γ it is forbidden outright: AB = id would force B = A⁻¹ (same axis, contradicting crossing), every nontrivial element is hyperbolic, and discreteness/cocompactness gives the systole floor **ℓ(AB) ≥ sys(X) > 0**, so Δℓ ≥ sys(X) − ℓ₁ − ℓ₂ strictly above −(ℓ₁+ℓ₂). Moreover a fixed pair of closed geodesics has finitely many crossings, hence finitely many angles: Δℓ takes finitely many values per pair — no infimum pathology.

**Numerics (mandatory; script run and deleted per house rules).** Explicit 2×2 matrices over the grid (ℓ₁,ℓ₂) ∈ {(1,1),(2,3),(5,5),(10,7),(0.5,4),(20,20)}, θ ∈ {0.1, π/4, π/2, 2, 3, 3.1}: max |matrix − formula| = 4.0×10⁻¹³; strictness and the −2 min floor asserted at every point; θ recovered from the length triple to 10⁻⁹; inverse channel ℓ(AB⁻¹) matches formula(π−θ) (10⁻⁷ relative; float cancellation at e²⁰-scale traces); saturation: ℓ₁=ℓ₂=20, θ=π/2 gives Δℓ = −1.38629435 vs limit −1.38629436; collapse: ℓ₁=ℓ₂=2, θ=π−10⁻³ gives tr(AB) = 2.00000138, ℓ(AB) = 0.00235. Disjoint-axis check for §(d): d(axes (0,∞),(1,3)) = 1.316958 by direct minimization = arccosh 2 (exact cross-ratio value), and the cosh d formula reproduces ℓ(AB) = 5.691114 to 10⁻⁶.

## §(b) BIND-GAP-2 — well-definedness

Fix primitive γ₁, γ₂ representing c₁, c₂ and use E7's refereed bijection {crossing double cosets ⟨γ₁⟩g⟨γ₂⟩} ↔ {transverse crossings of c₁, c₂}. Concatenating at the crossing of coset g gives the class P_g := [γ₁·gγ₂g⁻¹].

**Per-crossing well-definedness.** Replacing g by γ₁ᵐgγ₂ⁿ: γ₁·(γ₁ᵐgγ₂ⁿ)γ₂(γ₁ᵐgγ₂ⁿ)⁻¹ = γ₁ᵐ(γ₁·gγ₂g⁻¹)γ₁⁻ᵐ — conjugate. **[BOX-B1] P_g depends only on the double coset: each crossing carries one well-defined product class.** Order is immaterial: [xy] = [yx] (conjugate by x), so joining c₂-then-c₁ at the same crossing gives the same class.

**Across crossings.** For cosets g, g′, a conjugator h respecting the factorization (hγ₁h⁻¹ = γ₁, h(gγ₂g⁻¹)h⁻¹ = g′γ₂g′⁻¹) forces h ∈ Z(γ₁) = ⟨γ₁⟩ (primitive, torsion-free) and g′⁻¹hg ∈ Z(γ₂) = ⟨γ₂⟩, i.e. g′ ∈ ⟨γ₁⟩g⟨γ₂⟩. **Exact statement: factor-respecting conjugacy of products ⟺ same double coset.** [BOX-B2: for distinct cosets the products are generically non-conjugate, but ACCIDENTAL conjugacies via factor-mixing conjugators are excluded by nothing in the record — generic statement, not a universal theorem.]

**What IS canonical.** The finite multiset S⁺(c₁,c₂) = {P_g : crossing cosets}, of cardinality i(c₁,c₂) (branch multiplicity per E7 A.1; ≤ i(c₁,c₂) as a set). Representative changes γᵢ → hγᵢh⁻¹ re-index cosets (E7 §1c) and conjugate every product: S⁺ is an invariant of the pair. Every P_g is nontrivial (triviality forces coincident axes, contra crossing), hence hyperbolic, ℓ(P_g) ≥ sys(X). Therefore:

**[BOX-B3] ℓ_min(c₁,c₂) := min over S⁺ of ℓ is a well-defined, positive invariant of the pair** (defined whenever i(c₁,c₂) ≥ 1) — a minimum of a class function over a finite nonempty canonical set.

**Honest assessment.** BIND-1 survives BIND-GAP-2 in the amended form "composite carrier = minimal-length product class." Two costs, stated plainly: (1) nothing in the record selects the minimum — the selection is definitional, and any future minimization-flavored selection rule must be checked against the C-T3 exclusivity re-scope (MASS-1 vs energy-minimizing dynamical entries); (2) alternatively the multiplicity is itself physical — one bound class per crossing, a spectrum of up to i(c₁,c₂) composites (ground + excited) [recorded as a possibility, not asserted].

**Inverse-orientation channel.** S⁻(c₁,c₂) = {[γ₁·gγ₂⁻¹g⁻¹]} lives over the SAME coset space (⟨γ₂⁻¹⟩ = ⟨γ₂⟩, same axes, same crossings). At a crossing of oriented angle θ the reversed factor crosses at π−θ, and by E7's inverse law the sign flips: the two channels at one crossing carry (î_g, θ) and (−î_g, π−θ). By §(a), **both channels bind** (Δℓ < 0 at every θ ∈ (0,π)); the obtuse-angle channel binds more (monotonicity). Since Δℓ depends only on cos θ = cos|φ| while î = sign φ (φ the signed angle), **the crossing sign never enters the defect: E2's î and BIND-1's Δℓ are independent data at each crossing** — there is no anti-binding channel in 2D, and binding cannot be aligned with crossing sign. Further flag: Δℓ contains no charge at all — like-sign and opposite-sign pairs bind identically while D₁₂ = Q₁Q₂î flips. Interaction sign and binding sign are decoupled in the registered structure [flagged as a physical oddity, not a kill].

## §(c) BIND-GAP-1 — descent to registered data

**(i) Invertibility.** From [BOX-A]: cos θ = [cosh(ℓ₁₂/2) − cosh(ℓ₁/2)cosh(ℓ₂/2)] / [sinh(ℓ₁/2)sinh(ℓ₂/2)]; the denominator is positive and cos is injective on (0,π). **[BOX-C1] θ is a function of the length triple (ℓ₁, ℓ₂, ℓ₁₂)**, and conversely realizable triples are exactly those with |ℓ₁−ℓ₂| < ℓ₁₂ < ℓ₁+ℓ₂ (a strict "triangle" constraint). Verified numerically to 10⁻⁹. With k ≥ 2 crossings, the multiset of product-class lengths determines the multiset of crossing angles — angles become DERIVED data.

**(ii) Closure over E1 data.** Consequently:

**[BOX-C2 — main positive result] Δℓ = ℓ(c₁₂) − ℓ₁ − ℓ₂ is a function of three lengths of closed geodesics — three E1-type invariants — PROVIDED the product class is granted carrier status. Under that grant BIND-GAP-1 dissolves: no new registered datum (no angle column) is needed; the angle is output, not input.**

Caveats, carefully: (α) carrier status for c₁₂ is precisely K-BIND-1's open question — the dissolution is conditional; (β) E1 registers ℓ only through D = Q²ℓ/2π, so the composite's length is record-visible only if nonzero charge rides c₁₂; if Q₁+Q₂ = 0 the composite is E1-invisible (refereed: neutral defects carry no MASS-1 mass) — consistently, E4 makes Q_tot = 0 composites exactly the locally erasable (annihilating) ones, so the dissolution holds on the physical sector Q₁+Q₂ ≠ 0; (γ) which product class is "the" composite is §(b)'s question, upstream of this one.

**(iii) Arena certification — K-BIND-1 status.** Survey of refereed structures: E4's fusion composes defects by profile addition (Ad W(η₁)W(η₂) = Ad W(η₁+η₂)) — totals-only, and η₁+η₂ is no plateau profile of any single geodesic: the defect calculus's native composition is additive, the exact root of the phase-110 no-go; it does not concatenate carriers. E6's M_Λ contains one structure whose composition IS concatenation: deck unitaries multiply, U(γ₁)U(gγ₂g⁻¹) = U(γ₁gγ₂g⁻¹) — group multiplication in the crossed product literally realizes concatenation of classes. But no refereed structure ties a charged defect to its carrier's deck unitary (defects are fiber elements, U's are group elements; the only refereed link is covariance), so the echo carries no charge data and certifies nothing. E6's central-extension class recovers σ = crossing, not merger. **Verdict: the arena is SILENT. K-BIND-1 remains fully open.**

## §(d) Sign and scope (BIND-GAP-3, K-BIND-2)

From §(a): products over actual crossings give **strictly negative Δℓ — mass defect, attractive binding — in both orientation channels, at every angle, independent of charges and crossing signs.** The 2D record cannot deliver length excess at a crossing; K-BIND-2's excess demand is undeliverable by this mechanism, exactly as the registration feared.

One sharpening the record should have: the same trace algebra DOES contain an excess channel — for **disjoint** axes at distance d, the companion identity replaces cos θ by cosh d: cosh(ℓ(AB)/2) = cosh(ℓ₁/2)cosh(ℓ₂/2) + cosh d·sinh(ℓ₁/2)sinh(ℓ₂/2) in the coherent orientation [others': Fenchel's unified cosine rule — angle and distance are one complexified invariant; verified numerically above], giving strict EXCESS ℓ(AB) > ℓ₁+ℓ₂ (the anti-coherent orientation has |tr|/2 = |cosh cosh − cosh d·sinh sinh| and can even be elliptic at small lengths). E7's coset enumeration includes exactly these non-crossing cosets. But they correspond to no intersection point of c₁, c₂ — no concatenation basepoint, no BIND-1 mechanism; joining would need an arbitrary connecting arc. **[BOX-D1] Excess exists in the record's algebra only over non-crossing cosets, mechanism-free — recorded as data for BIND-GAP-3, nothing claimed.**

[SPECULATIVE — feeds BIND-GAP-3, ≤300 words] The operator's linked-knot excess needs constituents that obstruct each other's tightening — impossible for two curves in a surface, plausible for linked closed curves in a 3-manifold. The natural in-record 3-manifold is the unit tangent bundle UT(X) = Γ\PSL(2,ℝ): periodic orbits of the geodesic flow are canonically embedded closed curves, one per oriented closed geodesic, pairwise DISJOINT (distinct orbits never meet) — every pair acquires a well-defined linking datum where the surface had only crossing signs. Attributions [others', unverified here — name-checked, not relied on]: Ghys's knots-and-dynamics program (modular surface, periodic orbits as knots, linking with the trefoil, linking numbers of geodesic-flow orbits); Birman–Williams template theory. A 3D BIND would need: (1) a lift of the carrier dictionary to UT(X) — E3's framing entry already whispers in that direction, framing being UT-type data; (2) a ropelength-type functional on pairs obstructed by linking (Buniy–Kephart is the verified prior art); (3) a derivation that excess = f(linking). None exists in the record. [end SPECULATIVE]

## Gaps-and-boxes ledger

- **[BOX-A]** trace identity: derived self-contained; classical attribution (Fenchel; Buser) [others', not load-bearing].
- **[BOX-B2]** non-conjugacy of products across distinct crossings is generic; accidental conjugacies unexcluded.
- **[BOX-C2]** BIND-GAP-1 dissolution is conditional: on carrier status (= K-BIND-1) and on Q₁+Q₂ ≠ 0.
- **[BOX-D1]** excess ↔ non-crossing cosets: observation only, no mechanism.
- **BIND-GAP-1:** conditionally dissolved — defect = function of three E1 lengths; angle derived, not registered.
- **BIND-GAP-2:** resolved-with-choice — ℓ_min well-defined; multiplicity possibly physical (excited states); selection rule undelivered; tension-flag vs C-T3.
- **BIND-GAP-3:** open; 2D strictly defect-signed at crossings; 3D linking speculative.
- **K-BIND-1:** OPEN — arena silent (E4 additive; M_Λ's concatenation echo carries no charge data).
- **K-BIND-2:** not fired, but sharpened: the crossing mechanism can never deliver excess.
- **K-BIND-3:** does NOT fire — Δℓ ∈ (−2 min(ℓ₁,ℓ₂), 0), finitely many values per pair, systole floor in Γ.
- **New flags for the record:** Δℓ is charge-blind and crossing-sign-blind (decoupled from D₁₂); neutral composites are E1-invisible, consistently with E4 annihilation; binding saturates at 4 ln cos(θ/2) for long constituents.

---

## Amendment section

### A.1 Referee verdict (2026-07-26): all four mandates CONFIRMED

Adversarial referee report preserved verbatim in reviews/REPORTS-phase111-BIND1-referee-2026-07-26.md (independent re-derivation; independent numerics on the referee's own grid; by-hand coset algebra; file-level arena audits; web verification of the speculative attributions). Verdicts: **(a) CONFIRMED** (formula, angle convention verified against the factor-2 attack, strictness, monotonicity, bounds, saturation, systole argument); **(b) CONFIRMED** (double-coset algebra, both directions of the biconditional, primitivity hypothesis available); **(c) CONFIRMED as the stated conditional** (invertibility; [BOX-C2] airtight given caveats α, β, γ; arena-SILENT verdict on K-BIND-1 correct and reinforced by C-U2); **(d) CONFIRMED** (excess only over non-crossing cosets; anti-coherent ellipticity matrix-verified; Ghys and Birman–Williams attributions both web-VERIFIED, retained as [SPECULATIVE] as tagged).

The referee's sharpest attack strengthened the result: tr(AB) > 2 at EVERY crossing angle — the composite can never be elliptic or parabolic, with no exceptions in the open interval.

### A.2 Corrections ledger

- **C-U1.** The clause "hyperbolic for every θ ∈ (0,π) except the degenerate ℓ₁ = ℓ₂, θ → π endpoint" is deleted as misleadingly weak: RHS = cosh((ℓ₁−ℓ₂)/2) + (1+cos θ)S > 1 strictly, so AB is hyperbolic at every crossing angle with NO exception; the degeneration lies on the boundary θ = π, outside the crossing regime.
- **C-U2.** E6 echo scope: U(gγ₂g⁻¹) ∈ M_Λ only for g ∈ Λ = ⟨γ₁,γ₂⟩, while E7's crossing cosets range over g ∈ Γ — the concatenation echo exists only on Λ-representable crossings. Weakens nothing (the echo was used negatively); reinforces the arena-SILENT verdict.
- **C-U3.** K-BIND-3 scoping: the kill has two disjuncts. The unboundedness/consistency disjunct does NOT fire, unconditionally (bounds + systole + finiteness). The determinacy disjunct ("defect not determined by data the record can see") is the BIND-GAP-1 dissolution and is cleared only CONDITIONALLY (on K-BIND-1 and Q₁+Q₂ ≠ 0). The round's flat "does not fire" over-claimed by one clause.
- **C-U4.** Saturation: "constituent-independent" holds only in the double limit ℓ₁, ℓ₂ → ∞. One-sided growth gives Δℓ → 2 ln[cosh(ℓ₂/2) + cos θ·sinh(ℓ₂/2)] − ℓ₂, which retains ℓ₂-dependence.

### A.3 Post-verdict status

Refereed and entered in the BIND-1 registration: the exact defect formula [BOX-A] and its corollaries (strict binding at every crossing; Δℓ ∈ (−2min(ℓ₁,ℓ₂), 0); saturation per C-U4; hyperbolicity with no exceptions per C-U1); per-crossing well-definedness and the ℓ_min pair invariant ([BOX-B1], [BOX-B3]); the conditional closure over three E1 lengths ([BOX-C1], [BOX-C2]); the never-excess sharpening of K-BIND-2; the charge-blind/sign-blind decoupling flags; the non-crossing-coset excess observation [BOX-D1]. Open: **K-BIND-1 (the arena is silent on cross-axis fusion — now the single load-bearing open question of BIND-1)**; BIND-GAP-3 (3D excess; UT(X)/linking route speculative but attributions verified); [BOX-B2]; the excited-spectrum reading; the neutral-composite sector. Standing AI-referee caveat applies throughout.
