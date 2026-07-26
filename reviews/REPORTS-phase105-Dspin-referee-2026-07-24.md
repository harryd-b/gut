# REPORT — phase 105 D_spin referee pass (2026-07-24, verbatim)

*Context-free adversarial referee on the D_spin derivation (phases/phase105-Dspin-self-phase.md), run per standing pre-verdict policy. First referee of the session to verify numerically as well as analytically (smoothed-ramp lattice computation; finite part confirmed to ~4×10⁻⁷). Summary: A–D and F–G CORRECT with all signs and scalings verified; E (the framing counterterm) GAP as the room pre-flagged — the lone-ramp "free holonomy" is not defined, and two legitimate closures disagree by exactly the finite part (comoving compensator ⟹ D_spin = −Q²/2; uniform-background closure ⟹ D_spin = 0, both numerically confirmed) — with a real rescue: the divergence/finite split is canonical (finite part ramp-shape-independent, divergence carries all shape dependence), so MINIMAL SUBTRACTION defines D_spin = ∓Q²/2 unambiguously, provided the text adopts that definition explicitly. Overall ruling: D_spin SURVIVES as the third dictionary entry conditional on that repair. Verdicts entered in the derivation document's amendment. Report verbatim below; standing AI-referee caveat applies.*

---

Numerics confirm the analytics on every point, including the counterterm ambiguity in E. Report follows.

# Referee Report: Transport holonomy of one anchor and D_spin = ∓Q²/2

Conventions assumed as stated: σ(f,g) = ∫fg′dx, W(f)W(g) = e^{−iσ(f,g)/2}W(f+g), constants null. Write H_ε(y) = ρ(y/ε), η_θ(x) = Q[H_ε(x−m) − H_ε(x−b)], m = a+θ, understood as the periodization over 2πℤ of the rigid two-step profile. All key numbers below were verified numerically (ρ(s) = s − sin(2πs)/2π, c_ρ = 3/2, ε = 0.05, N = 8192 grid, 4000 θ-steps).

## A. Family and derivative — CORRECT (with one required clarification)

Only the moving ramp depends on θ, so ∂_θη_θ = −(Q/ε)ρ′((x−m)/ε) (periodized), a smooth bump with finite norm. This holds for all θ including through the crossing, because the rigid-superposition formula is jointly smooth — nothing singular happens when m passes b; the two ramps simply overlap transiently. Interpolation check: for m < b the profile is Q on (m+ε, b), 0 outside; for m > b the same formula gives −Q on (b+ε, m), 0 outside — which is exactly "original interval read the other way around, minus the constant Q," consistent with the endpoint bookkeeping in B. Required clarification: the verbal description "plateau Q on (m,b)" is false after the crossing; the family is defined by the formula (periodized difference of steps), not by that description. Each bracket H_ε(x−m+2πn) − H_ε(x−b+2πn) is compactly supported, so the periodization converges and η_θ is a genuine single-valued function on S¹ at every θ. With that reading, A is correct.

## B. Zero-mode bookkeeping — CORRECT

∮∂_θη dθ = −(Q/ε)∫₀^{2π}ρ′((x−a−θ)/ε)dθ = −Q∫ρ′(u)du = −Q for every x (each point is swept by the bump exactly once per period). Hence η_{2π} = η_0 − Q·1; equivalently, the telescoping periodization identity Σ_n[H_ε(x−a−2π+2πn) − H_ε(x−a+2πn)] = −1. Since constants are null (σ(c,·) = 0, ‖c‖ = 0, W(c) = 1), the loop closes in phase space modulo constants and T is a scalar. No single-valuedness problem: η_θ is a function on S¹ at each θ; the path is a loop only modulo constants, which is exactly what the vacuum representation quotients out. Consistent.

## C. Product formula — CORRECT (and the "Trotter gap" is smaller than advertised)

Induction: W(Δ_N)⋯W(Δ_1) = exp(−(i/2)Σ_k σ(Δ_k, Σ_{j<k}Δ_j))·W(ΣΔ_j). Since Σ_{j<k}Δ_j = η_{θ_{k−1}} − η_0, the stated intermediate is exact. The η_0 term: Σ_kσ(Δ_k, −η_0) = σ(η_{2π}−η_0, −η_0) = σ(−Q·1, −η_0) = 0 by constants-null. ✓. Remaining sum −(1/2)Σσ(∂_θη, η)δθ → +(1/2)∮σ(η,∂_θη)dθ by antisymmetry of σ. ✓.

Continuum limit: stronger than "plausible." For every finite partition the product is exactly (phase)·W(η_{2π}−η_0) = (phase)·1 — there is no operator-topology issue at all; only the scalar Riemann sum must converge. The integrand θ ↦ σ(η_θ,∂_θη_θ) is smooth (for fixed ε), and the error per step is O(δθ²) controlled by the uniformly bounded first and second θ-derivatives, so the sum converges at rate O(δθ). The acknowledged gap can be closed in two lines; the finiteness of ∮ of the squared norm suffices. CORRECT.

## D. Evaluation — CORRECT (all signs and scalings verified)

Integration by parts on the boundaryless circle (η_θ periodic at each θ): σ(η,∂_θη) = ∫η(∂_θη)′ = −∫η′∂_θη. ✓. With η′ = (Q/ε)[ρ′_m − ρ′_b] and ∂_θη = −(Q/ε)ρ′_m:

−∫η′∂_θη = +(Q²/ε²)∫ρ′_m² − (Q²/ε²)∫ρ′_mρ′_b.

- Self term: (Q²/ε²)·ε·c_ρ = Q²c_ρ/ε ✓ (u = (x−m)/ε, dx = ε du). Then ½∮dθ = ½·2π·Q²c_ρ/ε = πc_ρQ²/ε ✓.
- Cross term: x = b+εv gives −(Q²/ε)G(t), t = (m−b)/ε, G(t) = ∫ρ′(v)ρ′(v−t)dv ✓. Change of variables: dθ = dm = ε dt, so ½∮(−Q²/ε)G dθ = −½Q²∫G(t)dt ✓; as m loops once, t sweeps the full (compact) support of G exactly once. Fubini: ∫_ℝG = (∫ρ′)² = 1 ✓.
- Falling-ramp sign: profile Q on (m,b) requires the −QH_ε(x−b) term, hence η′ contains −(Q/ε)ρ′((x−b)/ε) ✓; combining the three signs (by-parts −, ∂_θη's −, falling ramp's −) yields cross contribution −Q²/2 — a single crossing, once per loop, not doubled ✓.

Total Φ = πc_ρQ²/ε − Q²/2. Numerical check: Φ − πc_ρQ²/ε = −0.50000038 at ε = 0.05, Q = 1. CORRECT.

## E. Framing counterterm — GAP (the finite part of Φ_free is scheme-dependent; as stated, Φ_free is not even defined)

This is indeed where the derivation breaks as written. A lone moving ramp QH_ε(x−m) is not a function on S¹ (it winds by Q), so "the same holonomy with the fixed anchor deleted" is not a loop in phase space and Φ_free has no Weyl-operator meaning without a closure prescription. Worse, legitimate closures disagree by exactly the finite part in dispute:

1. Comoving compensator (rigid dipole at fixed separation much larger than ε, take half): both ramps move, relative configuration frozen, no crossings; Φ_dipole = 2πc_ρQ²/ε exactly (numerics: 188.4955592 vs 2·div = 188.4955592), so Φ_free = πc_ρQ²/ε. This gives D_spin = −Q²/2 as claimed.
2. Uniform background closure (η_free = Q[H_ε(x−m) − x/2π], which is periodic): the θ-independent background contributes an extra cross term −(Q/2π)·Q per unit θ, and Φ_free = πc_ρQ²/ε − Q²/2 exactly (numerics: Φ_free − div = −0.4999999999996, D_spin = −3.8·10⁻⁷ ≈ 0). This gives D_spin = 0: the smeared compensating charge is itself "crossed" once per loop and reproduces the entire finite part.
3. Formal deletion (compute ½∮σ with the non-periodic step, integrand still well-defined since only η′ and the bump enter): reproduces πc_ρQ²/ε, agreeing with (1) — but this is a number, not a holonomy of Weyl operators, so it cannot be called "the holonomy of the free ramp" without argument.

The identification is not circular, but it is under-determined: the counterterm's finite part is a choice of framing/compensation scheme, and the claimed equality "divergence = Φ_free" silently selects scheme (1)/(3). Defensible repairs: (a) define D_spin by minimal subtraction of the universal divergence πc_ρQ²/ε (equivalent to (1)); this is well-defined and ρ-independent, since the finite part of Φ is ρ-independent (∫G = (∫ρ′)² = 1 for any ramp) while the divergence carries all c_ρ dependence — a genuinely canonical split by ε-scaling; or (b) declare the comoving-compensator loop the definition of "free transport" and prove scheme (2) differs precisely because its background carries charge past the mover (physically: it is not free). Either way the text must state this; as written, verdict GAP. Note the divergent piece itself is unambiguous — only the constant is scheme-dependent, and the minimal-subtraction reading rescues −Q²/2 with the stated caveat.

## F. Spin-statistics adjudication — CORRECT computation; [GAP] flag honestly placed

Rigid rotation: η_θ = η(·−θ), ∂_θη = −η′, and σ(η,−η′) = ∫η·(−η″) = +∫(η′)² by parts on the circle ✓ (the queried sign line is right). Then Φ_rigid = π∫(η′)² = 2πc_ρQ²/ε + O(e-small) for separation much larger than ε: exactly twice the one-ramp framing, zero finite part (numerics confirm to 10⁻⁹ relative). So the hierarchy — 0 crossings (rigid rotation): pure framing; 1 crossing (one anchor transported): framing − Q²/2; 2 crossings: framing − Q² — is internally consistent, and consistent with D and with the dipole computation in E. The [GAP] flag on identifying this transport phase with spin (h from L₀) is honest and correctly placed: what is computed is the holonomy of a specific adiabatic transport, and equating it with the conformal spin of the sector requires an independent rotation-generator argument (e.g., the implemented rotation one-parameter group and its ground-state eigenvalue in the charged sector), which is not given. The "1 crossing = exchange" identification additionally leans on the previously refereed two-defect crossing pairing σ = Q₁Q₂î, which supports it at the algebraic level; still, spin per se remains [GAP]-flagged, appropriately.

## G. Calibration — CORRECT

Q = q√(2π) gives D_spin = ∓πq²; |D_spin|/2π = q²/2 = h, the free-boson/U(1) vertex-operator weight ✓ (and consistent with the refereed monodromy e^{∓iQ₁Q₂} = e^{∓2πiq₁q₂} = 1 on the integer lattice, as locality demands). Lattice match: e^{∓iπq²} with q ∈ ℤ equals (−1)^{q²} = (−1)^q = e^{+iπq²}, using q² ≡ q (mod 2) ✓ — so the sign/orientation convention is invisible exactly on the lattice, and "convention-shifted in general, exact on the lattice" is an honest statement. Statistics bit (−1)^{q²} = (−1)^q ✓. Framing shift: one framing unit = one self-crossing = Q²/2, so the phase shift e^{±iQ²/2} = e^{±iπq²} = twist e^{2πih} (mod the same lattice sign) ✓, consistent with the self/cross bookkeeping in D. Arithmetic all checks.

## Summary (5 lines)

1. A–D CORRECT: the loop closes modulo constants, the product formula is exact at every partition (only a scalar Riemann sum remains), and Φ = πc_ρQ²/ε − Q²/2 with all signs verified analytically and numerically (−0.5000004 at ε = 0.05).
2. E is the real defect — GAP: a lone ramp is not a loop in phase space; the comoving-compensator closure gives Φ_free = πc_ρQ²/ε (giving D_spin = −Q²/2), but the equally legitimate uniform-background closure gives Φ_free = πc_ρQ²/ε − Q²/2 (giving D_spin = 0), both confirmed numerically.
3. The rescue is real: the divergence/finite split IS canonical (finite part ρ-independent since ∫G = 1, divergence carries all c_ρ), so minimal subtraction defines D_spin = ∓Q²/2 unambiguously — but the text must adopt that definition explicitly rather than assert the counterterm identity.
4. F CORRECT (rigid rotation = pure framing 2πc_ρQ²/ε exactly; crossing hierarchy internally consistent; the no-L₀ [GAP] flag is honestly placed), G CORRECT (h = q²/2, lattice sign identity q² ≡ q mod 2).
5. Overall ruling: D_spin = ∓Q²/2 (+ framing) SURVIVES as the third dictionary entry, conditional on replacing E's counterterm identification with the minimal-subtraction (or explicitly declared comoving-framing) definition; as currently derived, E is a GAP, not a fatal error.
