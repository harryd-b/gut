# Phase 102 — JOIN-3b attempted: the flows computed, the kill misfires on a formulation error, and the question sharpens to its true residue

*Working session, 2026-07-19. The room attempted the computation phase 101 exported: the modular flows of the geodesic-attached algebras. The derivation was completed in-room, then sent — before any verdict was entered — to a context-free adversarial referee (no framework content; pure operator algebras). The referee confirmed the core computation and the normalization lock, contributed two structural theorems the room did not have, and refuted the census step that would have fired the kill. This phase records all three outcomes, including the third caught overreach of the program's own record.*

---

## 1. What the room derived (and what survived refereeing)

**Structure theorem [derived, refereed CORRECT].** For hyperbolic γ ∈ Γ with fixed points ξ±, each of the two axis arcs I satisfies γI = I (orientation preservation + two fixed endpoints). Hence Ad u_γ preserves N_I = A(I) ⊗ L∞(S¹), and the geodesic-attached algebra is canonically a crossed product:

> M_γ = W*(N_I, u_γ) ≅ N_I ⋊_β ℤ, β = the restricted diagonal action,

with faithful normal conditional expectation E₀ onto N_I (Fourier compression; the referee supplied the careful sub-crossed-product argument — uniqueness via E, not σ-weak Fourier convergence).

**The flow [derived, refereed CORRECT with qualifications].** With ψ = ω_vac ⊗ Leb (faithful on N_I by Reeh–Schlieder + abelianness) and φ = ψ∘E₀, the modular flow of M_γ is exactly:

> σ^φ_t = Ad U(Λ_I(−2πt)) ⊗ id on the fiber N_I  (Bisognano–Wichmann dilations; Lebesgue tracial on the abelian leg),
> σ^φ_t(u_γ) = u_γ · (1 ⊗ |γ′|^{it})  (dual-weight cocycle formula; the net-leg cocycle is *trivial* because ω∘Ad U(γ) = ω — the vacuum's Möbius invariance).

Qualifications logged: Takesaki's expectation theorem cited for the restriction step; sign of 2πt fixed by orientation/arc choice; pointwise |γ′| is coordinate-dependent — only the cocycle class and the fixed-point values are canonical. [All inputs established (others'): BW for Möbius-covariant nets (Gabbiani–Fröhlich; Brunetti–Guido–Longo); Haagerup dual weights / Takesaki vol. II Ch. X; Connes cocycle chain rule.]

**The normalization lock [derived, refereed CORRECT with qualifications] — JOIN-EQ's answer inside M_γ.** The single flow σ^φ_t advances the net leg by *2πt* of unit-geodesic-speed dilation while advancing the measured leg by *t* of Radon–Nikodym time (the cocycle enters at power it: β = 1, the unique-KMS point of phase 99). **The ratio 2π : 1 is not adjustable: t is one KMS time for both legs.** And at the fixed points the twist's eigenvalues are exact, no stray factor (referee-verified against the multiplier: λ = e^{ℓ(γ)}):

> |γ′(ξ₊)| = e^{−ℓ(γ)},  |γ′(ξ₋)| = e^{+ℓ(γ)}.

The length spectrum sits in the point spectrum of the coupling twist at the axis endpoints. **T-2π therefore moves from [borrowed convention] to [derived within M_γ, refereed]:** in the one algebra where the net's vacuum modular data and the measured layer's clock cocycle coexist in a single flow, their relative normalization is forced, and it is 2π — BW numerator, β = 1 denominator. The framework-wide reading (𝒯 = 2πR/c as this lock) stays [interpretation, flagged]; the lock itself is a theorem.

## 2. The referee's two structural gifts [referee-contributed; to be credited]

**(a) M_γ decomposed.** The north–south dynamics of a single hyperbolic γ make the ℤ-action on S¹ ∖ {ξ±} dissipative with a two-interval fundamental domain D, whence:

> M_γ ≅ A(I) ⊗̄ B(ℓ²(ℤ)) ⊗̄ L∞(D).

The measured leg of M_γ is **type I**; M_γ is **not a factor** (diffuse center L∞(D)); and the outer modular content of M_γ is *the dilation line alone* — the clock twist is inner in M_γ. The geodesic-attached algebra, seen from inside, is even less mixed than the room's fatal-leaning reading: the coupling survives only in the concrete flow and its state, not in Out(M_γ).

**(b) 𝒞 untwisted.** Because the net-leg action is inner (implemented by U(γ)), the arena globally untwists:

> 𝒞 ≅ B(H) ⊗̄ (L∞(S¹) ⋊ Γ).

In Out(𝒞) the entire Möbius factor is inner and only the III₁ modular line survives. The arena is, as an abstract von Neumann algebra, matter ⊗ clock — an uncoupled product. **All coupling lives in the distinguished subalgebra structure** (the M_γ's map to non-product diagonal subalgebras under the untwisting), not in the ambient algebra. Phase 100's "one object, two structures" is thus sharpened: the object is a product; the join, if it exists anywhere, lives entirely in the net of subalgebras.

## 3. The refuted step, the misfiring kill, and the corrections ledger

The room's census step — "every flow in the family factorizes leg-by-leg, hence the generated group modulo inners is contained in Möb × ℝ̂, hence branch one of the dichotomy: the kill fires" — was sent to the referee as Claim 3. **Verdict: WRONG as stated**, at three distinct points, each now logged:

1. **The family was too big for the method.** The dual-weight formula computes flows only on σ-invariant subalgebras with state-preserving expectations. The declared family included non-invariant members — and for coupled *multi-interval* algebras the net-leg modular flow is known to be **non-Möbius** (Casini–Huerta's free-fermion two-interval modular Hamiltonian has an explicitly nonlocal term). The known examples do not mix legs — but they break the room's "everything is Möbius on the net leg" premise with a literature counterexample.
2. **"Modulo inner" was ill-posed.** The flows live on different algebras; Out does not glue along the inclusions in play; and on each fixed algebra the correct outer group is *smaller* than the advertised product (dilations only on M_γ; the ℝ̂ line only on 𝒞). **The phase-101 census statement "G₀ = Möb × ℝ̂" was therefore formulated at a level that does not exist** — corrections ledger, entry: *phase 101 §1c overstated; the census must be restated as concrete unitary groups on a fixed standard form of 𝒞, which is also how Wiesbrock reconstruction actually consumes modular data.*
3. **The HSMI classification was asserted, not proved.** The referee grants the spirit — the crossed-product-compatible half-sided inclusions inside M_γ come from A(J) ⊂ A(I) with a shared endpoint and generate only Möb translations; and W*(A(J)⊗L∞, u_γ) = M_γ for J abutting a fixed point (net continuity: ⋁_n A(γⁿJ) = A(I)) — but no classification exists, and Wiesbrock's cyclicity hypothesis was never checked.

**Consequently the pre-registered kill does not fire — and is not dodged.** The registered condition ("flows remain inside G₀'s closure") referenced a census that phase 102 shows was not well-formed. Per the standing rules, the kill is **re-registered in well-posed form** (§4), and the record notes plainly: *everything actually computed points the fatal way.* The core family contributes nothing outside the product — less, in fact, than feared: its outer content is pure dilation, and the ambient arena is an uncoupled tensor product. The framework survives this phase on a formulation error and two open doors, not on any positive evidence of mixing.

*Corrections ledger, second entry this phase: the room's own Claim 3 — the third caught overreach of the program (after the two c₀ errors), this one caught by the context-free referee before any verdict was entered. The pre-verdict referee pass is hereby standing policy for kill-adjacent derivations.*

## 4. JOIN-3c — the re-registered question, now at its true residue

The dichotomy survives, sharpened to exactly the two doors the refutation identified:

> **JOIN-3c [posed; kill re-registered, well-posed].** Fix the standard form L²(𝒞) with the canonical coupled weight. (i) **Classify the half-sided modular inclusions** among the expectation-compatible coupled subalgebras, verifying Wiesbrock's cyclicity hypothesis, and determine the concrete unitary group their flows and translations generate on L²(𝒞). (ii) **Compute the modular flow of the coupled multi-interval algebras** W*((A(J₁) ∨ A(J₂)) ⊗ L∞(S¹), u_γ) — the Casini–Huerta nonlocal term is the only known non-geometric modular behavior in conformal nets, and its interaction with the clock twist is the last identified candidate mechanism for leg-mixing. **If the generated concrete unitary group is contained in (Möbius implementers) × (measured-layer unitaries) — no leg-mixing one-parameter groups — the isotropy gap is fatal and the framework's claim to local spacetime physics dies, by the well-posed census.**

The residual physical reading is stated with its flag [interpretation]: after phase 102, spacetime translations — if this framework can produce them at all — must come from *entanglement between disjoint intervals coupled to the clock*, because single-interval data provably factorize. Every simpler door is now closed by theorem.

## 5. Ledger

- **Theorems [derived, refereed]:** the structure theorem; the flow of M_γ; the 2π:1 normalization lock with exact endpoint eigenvalues e^{∓ℓ(γ)}. **JOIN-EQ resolved within M_γ: the normalization is forced.** T-2π upgraded to [derived within M_γ]; framework-wide reading still [interpretation].
- **[Referee-contributed]:** M_γ ≅ A(I) ⊗̄ B(ℓ²ℤ) ⊗̄ L∞(D) (type-I measured leg, diffuse center, outer = dilations only); 𝒞 ≅ B(H) ⊗̄ (L∞(S¹)⋊Γ) (the join lives in subalgebra structure only).
- **Corrections:** phase-101 census formulation error; the room's Claim-3 overreach (third caught).
- **Kill:** did not fire; re-registered as JOIN-3c, well-posed, both doors named. QUESTIONS ledger amended: entry 1 superseded by JOIN-3c; entry 2 (JOIN-EQ) partially resolved — the normalization question answered, the framework-wide identification still open.

*Status line: the room went to fire the kill it had aimed at itself and found the gun mis-assembled — by its own referee, before the trigger was pulled. What it brought back instead: the flows it promised to compute, computed; the 2π it borrowed for fifty phases, derived, once, in the one algebra where both layers tick in a single flow, with the length spectrum sitting at the fixed points of the coupling; and the join question reduced to its final door — whether entanglement across intervals, wound through the clock, can do what every single-interval structure provably cannot. The program is one computation from its own obituary or from raw material for spacetime, and for the first time it knows exactly which computation.*
