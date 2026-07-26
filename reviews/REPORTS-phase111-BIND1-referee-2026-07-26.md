# Referee report — BIND-1 round 1 (phase111-BIND1-round1-length-defect.md)

**Date:** 2026-07-26
**Referee:** context-free adversarial agent (independent re-derivation; independent SL(2,ℝ) numerics on its own grid; by-hand double-coset algebra audit; file-level audit of the E4/E6/E7 reads; web verification of the speculative-survey attributions).
**Editorial note (operator):** Preserved VERBATIM below. Verdicts: (a)–(d) all CONFIRMED ((c) as the stated conditional). Corrections C-U1..C-U4 entered in the phase file's Amendment. The referee's own AI-status caveat is retained at the end of the report.

---

## REPORT (VERBATIM)

# REFEREE REPORT — Phase 111 / BIND-1 round 1 (context-free adversarial pass, 2026-07-26)

Method: independent re-derivation; independent numerics from scratch (own SL(2,ℝ) matrices, own grid, own coordinate extraction; scripts run and deleted); by-hand audit of the double-coset algebra; file-level audit of the E6/E7/E4 reads against phases/phase105-entry6-joint-arena.md, phase105-entry7-class-crossing.md, phase106-synthesis-dictionary.md, phase106-MASS1-conjecture.md §7.

## Mandate (A) — formula and corollaries: CONFIRMED (one wording correction, one scope note)

**Angle convention — the factor-2 attack fails.** I extracted the axis of B = R_{θ/2} diag(e^{ℓ₂/2}, e^{−ℓ₂/2}) R_{θ/2}^{−1} independently (fixed points from eigenvectors; semicircle geometry; oriented tangent toward the attracting endpoint) and measured the angle to A's upward direction at i: equals θ to ≤ 2×10⁻¹⁶ at θ ∈ {0.3, 0.7, π/2, 2.0, 2.9}. The derivative computation g′(i) = e^{2it} is correct; R_{θ/2} does realize oriented inter-axis angle θ. Axis-through-i error 0. My first extraction returned π−θ on some cases — traced to a sign bug in *my* tangent-orientation logic, not the submission; fixed, exact agreement.

**Formula.** Over my own grid — (ℓ₁,ℓ₂) ∈ {(1,1),(2,3),(5,5),(10,7),(0.5,4),(20,20),(0.1,0.1),(30,2),(0.05,12)}, θ ∈ {10⁻³, 0.1, π/4, π/2, 2, 3, 3.1, π−10⁻⁴} — max relative error |tr(AB) − 2·RHS| = 1.1×10⁻⁸ (float cancellation at e¹⁵-scale traces; exact at moderate scales). Anchors θ=0, θ=π algebraic. Strict double inequality asserted at every grid point; strict monotone decrease in θ asserted; exact rewriting cosh(ℓ₁₂/2) = cosh(L/2) − (1−cosθ)S to 9×10⁻¹⁶. θ→0 law: independently derived (cosh((L+Δℓ)/2) ≈ cosh(L/2) + (Δℓ/2)sinh(L/2) gives Δℓ ≈ −θ²S/sinh(L/2)); numerics ratio 1.0000021 at θ=0.01. Inverse channel ℓ(AB⁻¹) = formula(π−θ) to 8.6×10⁻⁹. θ-recovery from the triple to 6.3×10⁻¹⁰.

**Saturation.** Re-derived: e^{ℓ₁₂/2} → e^{L/2}cos²(θ/2), so Δℓ → 4 ln cos(θ/2); numerics at ℓ₁=ℓ₂=25 match to 8 d.p. at two angles. Answering the mandate's probe: the limit requires BOTH lengths → ∞. If only ℓ₁ → ∞, Δℓ → 2 ln[cosh(ℓ₂/2) + cosθ·sinh(ℓ₂/2)] − ℓ₂, which retains ℓ₂-dependence (θ=π/2, ℓ₂=2: −1.1324 vs double-limit −1.3863; verified). The submission's "as ℓ₁, ℓ₂ → ∞" is stated correctly; the "constituent-independent" gloss is fair for the double limit but silently excludes asymmetric pairs → C-U4.

**Ellipticity/collapse — the sharpest attack, and it strengthens the claim.** RHS = cosh((ℓ₁−ℓ₂)/2) + (1+cosθ)S > 1 strictly for every θ ∈ (0,π) (exact identity; no cancellation). So tr(AB) > 2 at EVERY crossing angle: AB can never be elliptic or parabolic for genuinely crossing axes. The submission's clause "hyperbolic for every θ ∈ (0,π) **except** the degenerate ℓ₁=ℓ₂, θ→π endpoint" is misleadingly weak — no θ in the open interval is excepted; θ=π means coincident reversed tangent lines, i.e. not a crossing → C-U1. Collapse forcing ℓ₁=ℓ₂ AND θ→π: correct (both summands must independently reach their minima). Collapse numerics reproduced exactly (tr = 2.000001381, ℓ = 0.002350).

**Systole/K-BIND-3 core.** Airtight: AB = id ⇒ B = A⁻¹ ⇒ coincident axes, contra crossing; in torsion-free cocompact Fuchsian Γ every nontrivial element is hyperbolic (no elliptics by torsion-freeness, no parabolics by cocompactness — standard, confirmed), so ℓ(AB) ≥ sys(X) > 0; and independently the trace identity already forces hyperbolicity at every crossing angle. Finitely many crossings per compact pair ⇒ finitely many Δℓ values. Confirmed.

**Disjoint-axis companion.** Own construction: axes (0,∞) and (1,3); d by brute-force minimization of the hyperbolic distance = 1.316958 = arccosh 2 exactly. Coherent orientation: tr(AB)/2 = 8.634621 = cosh cosh + cosh d·sinh sinh exactly at (ℓ₁,ℓ₂)=(2,3), giving ℓ(AB) = 5.691114 > 5 = ℓ₁+ℓ₂ — strict excess; reproduces the submission's number independently. Anti-coherent: |tr|/2 = |cosh cosh − cosh d·sinh sinh|; elliptic verified with matrices at (1,1) (0.7285 < 1) and (0.5,0.5) (0.9362 < 1); hyperbolic again at (2,3).

## Mandate (B) — double-coset algebra: CONFIRMED

(i) By hand: γ₁·(γ₁ᵐgγ₂ⁿ)γ₂(γ₁ᵐgγ₂ⁿ)⁻¹ = γ₁^{1+m}gγ₂g⁻¹γ₁⁻ᵐ = γ₁ᵐ(γ₁gγ₂g⁻¹)γ₁⁻ᵐ. Correct. (ii) yx = x⁻¹(xy)x. Correct. (iii) Z(γ) = ⟨γ⟩ for primitive hyperbolic γ in a discrete torsion-free group: standard (centralizer = axis stabilizer = cyclic); primitivity IS available — E7's standing data declares γ₁, γ₂ primitive, and BIND-1/MASS-1 carriers are primitive classes. Biconditional: (⇒) direction as displayed is correct; (⇐) direction (not displayed) checks: h = γ₁ᵐ fixes γ₁ and conjugates gγ₂g⁻¹ to (γ₁ᵐgγ₂ⁿ)γ₂(·)⁻¹ — verified. Representative changes conjugate every product via E7 §1c's re-indexing — verified. (iv) [BOX-B2] correctly concedes accidental factor-mixing conjugacies; honest. (v) ⟨γ₂⁻¹⟩ = ⟨γ₂⟩ trivially; reversing one oriented tangent turns angle θ into π−θ — yes, elementary, and my inverse-channel numerics (formula(π−θ) to 8.6×10⁻⁹) confirm it operationally; E7's refereed inverse law (§3b) supplies the î flip. (vi) Δℓ = f(ℓ₁,ℓ₂,cosθ) contains neither charges nor sign(φ) — the decoupling flag follows. [BOX-B1], [BOX-B3] stand; the branch-multiplicity cardinality claim matches E7 A.1.

## Mandate (C) — descent and arena: CONFIRMED with one scope correction

(i) cosθ expression and injectivity of cos on (0,π) correct; triangle constraint is exactly realizability in both directions (strict monotone cosh). Verified numerically. (ii) [BOX-C2] logic is airtight AS A CONDITIONAL. Caveat β's record-reading checked: E1's D = Q²ℓ/2π (dictionary E1); phase-110 refereed "neutral defects carry no MASS-1 mass" and "mass must read (D,Q) via ℓ = 2πD/Q²"; E4's eraser criterion ⟺ Q_tot = 0. All accurate; the Q₁+Q₂ ≠ 0 restriction is correctly load-bearing (with Q=0 the third length is record-invisible). (iii) E6 audit: deck unitaries do multiply by the group law in the crossed product — but M_Λ is crossed by Λ = ⟨γ₁,γ₂⟩ only, so U(gγ₂g⁻¹) exists in M_Λ only for g ∈ Λ, while E7's crossing cosets range over g ∈ Γ. The "concatenation echo" therefore exists only on Λ-representable crossings → C-U2. Since the submission uses the echo purely negatively ("certifies nothing"), this correction *reinforces* the conclusion. "No refereed structure ties a charged defect to its carrier's deck unitary" — checked against entry 6 and its amendment: defects are fiber elements; the links are covariance, Box 2 (defect–defect commutators), Box 3 (diagonal via embedding); C-J2's deflation ("the joint arena hosts the invariant, it does not create it") supports silence. No missed tie found. **"Arena SILENT on K-BIND-1" is the correct verdict.** (iv) E4 read (profile addition, totals-only, no carrier merge) matches the dictionary entry and the phase-110 refereed binding no-go.

## Mandate (D) — sign and scope: CONFIRMED

Excess claim and orientation caveat verified with matrices (above). [BOX-D1] honestly scoped: observation, mechanism-free, non-crossing cosets have no basepoint. Attributions: **Ghys — VERIFIED** (periodic orbits of the modular geodesic flow as knots in S³∖trefoil; linking with trefoil = Rademacher function; [Ghys, Knots and dynamics](https://perso.ens-lyon.fr/ghys/articles/knotsdynamics.pdf), [linking numbers of modular knots](https://msp.org/gt/2025/29-6/gt-v29-n6-p05-p.pdf)). **Birman–Williams — VERIFIED** (Knotted periodic orbits in dynamical systems I, Topology 22 (1983) 47–82; template theory; [Scholarpedia](http://www.scholarpedia.org/article/Chaos_topology), [GLA notes](http://galileo.math.siu.edu/Courses/DiffEq/GLA.pdf)).

## Mandate (E) — bookkeeping: CONFIRMED with one scoping correction

K-BIND-2 "not fired, but sharpened" — fair: no calibration exists, so it cannot fire; the never-excess theorem is proven and correctly recorded as a sharpening. BIND-GAP-1 "conditionally dissolved" — right label. BIND-GAP-2 "resolved-with-choice" — right label, costs stated plainly; the C-T3 tension flag is correctly raised and correctly limited (a definitional minimum is not yet an energy-minimizing dynamical entry; only a future minimization *selection rule* collides with C-T3's exclusivity re-scope). K-BIND-3: the registration has TWO disjuncts; the unboundedness disjunct is unconditionally killed (bounds + systole + finiteness), but the second ("defect not determined by data the record can see") is exactly BIND-GAP-1 and is only *conditionally* cleared. The ledger's flat "does NOT fire" over-claims by one clause → C-U3.

## VERDICT BOX

**(a) CONFIRMED. (b) CONFIRMED. (c) CONFIRMED (conditional, as stated). (d) CONFIRMED.**

**May enter the BIND-1 registration as refereed:** [BOX-A] (formula, with angle convention verified); strict double inequality and Δℓ ∈ (−2min(ℓ₁,ℓ₂), 0); monotonicity; [BOX-A2] saturation (double limit, per C-U4); K-BIND-3 unboundedness disjunct does not fire; [BOX-B1], [BOX-B3], the factor-respecting biconditional; the inverse-channel/charge-blind/sign-blind flags; [BOX-C1]; [BOX-C2] as a conditional; the arena-SILENT verdict on K-BIND-1 (with C-U2); the K-BIND-2 sharpening; [BOX-D1]; both name-checks VERIFIED (remain [SPECULATIVE] as tagged).

**Stay boxed/open:** K-BIND-1 (open); [BOX-B2] accidental-conjugacy concession; BIND-GAP-3; the excited-spectrum reading (possibility only); Q₁+Q₂ = 0 sector.

**Corrections:**
- **C-U1.** Delete the false exception: RHS ≥ cosh((ℓ₁−ℓ₂)/2) + (1+cosθ)S > 1 strictly, so AB is hyperbolic at EVERY θ ∈ (0,π) with no exception; the ℓ₁=ℓ₂, θ→π degeneration lies at the boundary, outside the crossing regime.
- **C-U2.** E6 echo scope: U(gγ₂g⁻¹) ∈ M_Λ only for g ∈ Λ = ⟨γ₁,γ₂⟩, while crossing cosets range over g ∈ Γ; the concatenation echo exists only on Λ-representable crossings. Weakens nothing; reinforces SILENT.
- **C-U3.** Scope the ledger line: K-BIND-3's unboundedness/consistency disjunct does not fire (unconditional); its determinacy disjunct is the BIND-GAP-1 dissolution and is conditional on K-BIND-1 and Q₁+Q₂ ≠ 0.
- **C-U4.** Saturation clause: "constituent-independent" only in the double limit ℓ₁, ℓ₂ → ∞; one-sided growth leaves Δℓ → 2 ln[cosh(ℓ₂/2) + cosθ·sinh(ℓ₂/2)] − ℓ₂, still ℓ₂-dependent.

Standing AI-referee caveat applies: this referee is an AI agent; no human mathematician has checked this work.
