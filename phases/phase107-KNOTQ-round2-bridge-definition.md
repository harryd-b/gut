# Phase 107 — KNOT-Q campaign, round 2: the bridge at one torsion insertion (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-26, executing the operator's instruction to complete the remaining KNOT-Q work. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered; KNOT-Q v2 registration unchanged until referee].***

*Headline claims (pre-verdict): (1) Route 2 (homotopy/holonomy pairing) is computed rigorously and yields ZERO — one unit of Giroux torsion changes no homotopy invariant of the plane field (relative Euler class vanishes via the ∂_t section; primary obstruction vanishes; full class imported), and any pairing through the fiber class lands in ℤ/(2g−2), incompatible with Q ∈ ℤ — so e cannot be a homotopy-level pairing; (2) Route 1 (leaf-space transport) forces the ANCHORS onto fix(γ) canonically (the ideal boundary trace of the lifted wall cylinders is exactly {ξ±} — derived from the geometry, not fitted to the locality theorem) and yields a canonical integer winding n per wall crossing, but the post-insertion Reeb flow has no canonical weak-stable foliation, so winding ↦ charge is a postulated homomorphism k ↦ e·k; (3) THE BRIDGE IS UNDERDETERMINED AND THE DETERMINING CHOICE IS NAMED: a homotopy-factoring bridge forces e = 0 (kill would fire); faithfulness + sector-surjectivity (axiom N) forces e = ±1 (Q = ±n, D = n²ℓ/2π); additivity alone leaves e ∈ ℤ. There is a principled PRE-KILL argument against homotopy-factoring (it would annihilate the entire refereed bulk datum — torsion is precisely the homotopy-invisible contact invariant), but it is a definitional stance, not a theorem; (4) kill verdict INCONCLUSIVE, honestly; (5) the simplicity prediction (s) stands nonvacuous — within the proven operation class, quantized bulk data attaches only over simple closed geodesics while the boundary admits all hyperbolic classes. Consistency checks pass (anchors, additivity, inverse sign, finite D); the layer contact volume (linear in n) is noted NOT to match D's n² scaling, with no coincidence claimed. Referee to check the local geometry computations, the transversality claims, the Euler-class argument, and the honesty of the underdetermination framing.*

---

## The derivation, verbatim

# The Bridge at One Torsion Insertion: Boundary-Net Action of Giroux Torsion Along a Vertical Torus

## 0. Object and conventions

Fixed data: X = T¹Σ_g = Γ\PSL(2,ℝ), contact form α_can, Reeb = geodesic flow; boundary circle S¹ = ∂ℍ = leaf space of the lifted weak-stable foliation; chiral U(1) current net A(I) with defect automorphisms α_ρ(W(f)) = e^{i∫ρf}W(f), Q = ∫ρ; refereed locality theorem (anchors on fix(γ), D = Q²ℓ/2π); round-1 results (i)–(v) as given. γ ⊂ Σ_g a **simple** essential closed geodesic, length ℓ = ℓ(γ), axis endpoints ξ± ∈ S¹; T_γ = π⁻¹(c_γ) the embedded vertical torus. The F-GAP object: the boundary-net action of one unit (n = 1) of Giroux torsion inserted along T_γ; extract e in Q = e·n.

Coordinates on T_γ: (s, θ), s ∈ ℝ/ℓℤ arclength on c_γ, θ the fiber angle from c_γ′(s), frame (c′, n) parallel along the geodesic.

## 1. Local geometry at T_γ (computed)

α_can(u) = ⟨v, dπ(u)⟩ gives α_can|_{T_γ} = cos θ ds. Consequences (all verified pointwise):

- **Tangency circles.** ξ_can = T T_γ exactly on the two circles {θ = ±π/2} (unit normals to c_γ). So T_γ is *not* pre-Lagrangian or convex for α_can as it sits; the insertion operation requires first isotoping T_γ (or its collar) to a normal-form position. [GAP-1] The insertion uses Colin's normal form [others'; Colin 2001, as in round-1 (i)]; well-definedness of the result up to contact isotopy, independent of the normalizing isotopy, is imported [others', partially; flagged].
- **Foliation transversality (needed for Route 1).** The weak-stable leaves are everywhere transverse to T_γ. Checked at the three suspect loci: (a) generic points — leaf plane (flow, stable) vs torus plane (∂_s, ∂_θ) sum to 3 dimensions; (b) the two closed Reeb orbits γ± ⊂ T_γ (θ = 0, π) — intersection is exactly the flow line, and stable ∉ T T_γ (the stable Jacobi direction is a nontrivial vertical/horizontal-normal mix), so the sum is still 3-dimensional; (c) the tangency circles θ = ±π/2 — there T T_γ = ξ but flow ∉ ξ, so leaf + torus = everything. **Transversality holds without exception.**
- **Layer data.** For the layer (T²×[0,1], α_n = cos(2πnt)dx − sin(2πnt)dy), with x-circle of length ℓ and y-circle (fiber) of length 2π: α_n ∧ dα_n = 2πn dt∧dx∧dy, so the layer's contact volume is 4π²nℓ (linear in n; recorded for §9). Every plane ξ_n(t) contains ∂_t; the plane's trace line in T² winds exactly n full turns (restates round-1 (ii)).

**[BOX 1]** *T_γ is tangent to ξ_can along two circles (insertion needs a normal-form choice, [GAP-1]), but the weak-stable foliation is everywhere transverse to T_γ. Route 1's transport question is well-posed at the level of germs.*

## 2. Route 2 — homotopy/holonomy pairing: the answer is zero

**Relative Euler class (rigorous).** The section ∂_t of ξ_n over the layer is nowhere zero and matches the boundary plane fields at t = 0, 1. Hence the relative Euler class of the inserted layer vanishes and e(ξ_new) = e(ξ_can) in H²(X;ℤ). One unit of torsion does **not** change e(ξ) by PD[T_γ] or by any multiple of any class: the change is exactly 0.

**Full homotopy class.** The primary difference obstruction (in H²(layer, ∂; π₂(S²)) ≅ ℤ², generated by the annuli S¹_x×I, S¹_y×I) also vanishes: the Gauss map ν_n(t) = cos(2πnt)∂_x − sin(2πnt)∂_y depends only on t, so both annulus degrees are 0. The secondary (Hopf-type, H³ rel ∂) obstruction: on T³ the structures ξ_n are classically all homotopic as plane fields though pairwise non-contactomorphic [others'; Giroux, Kanda], and torsion insertion is known not to change the homotopy class of the plane field in the toroidal settings of the Heegaard Floer literature [others'; Ghiggini–Honda–Van Horn-Morris]. [GAP-2] The rel-boundary secondary obstruction for this specific X is imported from these statements, not recomputed here.

Additional internal check: any pairing through H₁(X) = ℤ^{2g} ⊕ ℤ/(2g−2) against the fiber class would be valued in ℤ/(2g−2) (the fiber generates the torsion summand, round-1 (v)), incompatible with Q ∈ ℤ. No homotopy-level pairing can carry the bridge.

**[BOX 2]** *Route 2 yields e = 0 identically: Giroux torsion is invisible to every homotopy invariant of the plane field (Euler class rigorously; full class [others'], [GAP-2]). Therefore either the bridge factors through homotopy data and e = 0 (kill fires), or the bridge must be defined on finer contact/dynamical data. Route 2 cannot itself supply a nonzero e.*

This is the plainly-stated meaning requested: e is **not** a homotopy-class pairing; consistency with Route 1 is the whole question.

## 3. Route 1 — leaf-space transport

**No canonical post-insertion foliation.** The layer Reeb field is R_n ∝ cos(2πnt)∂_x − sin(2πnt)∂_y: each torus {t} carries a linear flow whose slope rotates through all values n times, so the new Reeb flow contains n circles' worth of pre-Lagrangian tori of closed orbits (including fiber-class orbits). The post-insertion Reeb flow is not Anosov and has **no canonical weak-stable foliation**. [GAP-3] Any "re-glued leaf space" requires a choice of Reeb deformation/interpolating foliation through the layer; the transport is *not* canonically a circle map.

**The canonical germ datum.** What *is* canonical: the contact structure is unchanged outside the collar, the old foliation persists there (transversally to the wall, §1), and along any arc crossing the layer, the plane field — every plane containing ∂_t — traces a loop of lines in the (x,y)-torus winding **exactly n full turns rel endpoints**. This relative winding is a well-defined integer (endpoint-fixed loop in the circle of co-oriented lines), independent of all choices in [GAP-1]/[GAP-3]. It is precisely the datum that distinguishes ξ_n contact-topologically while being homotopy-invisible (consistent with Box 2).

**Where the anchors land (derived, not fitted).** In the universal cover the preimage of T_γ is the Γ-orbit of cylinders over the lifts of the axis of γ. The cylinder over the axis A(ξ₋, ξ₊) has ideal boundary trace exactly {ξ₋, ξ₊} = fix(γ). Every weak-stable leaf W_ξ, ξ ∉ {ξ±}, crosses the cylinder transversally in a single arc; the accumulated U(1) winding per crossing is n. Read on the leaf space, the wall is a defect line whose endpoints on S¹ are ξ±: **the anchors land on fix(γ)**, exactly as the locality theorem requires — this came out of the geometry (the wall's location), independently of any choice of e.

**The bridge postulate.** [GAP-4] The identification "n full turns of ξ-winding across the wall ↦ charge e·n at the anchors, ρ supported at {ξ₊, ξ₋} with signs fixed by the orientation of γ" is a postulate, not a derivation. Additivity (n layers = n-fold winding) forces the map ℤ → ℤ, k ↦ e·k, to be a homomorphism; nothing in Routes 1–2 computes the generator value e beyond excluding the homotopy definition.

**[BOX 3]** *Route 1 produces: a canonical anchor set fix(γ), a canonical integer winding n per crossing, and a bridge that is a homomorphism ℤ → ℤ, k ↦ e·k. The integer |e| is fixed only by a normalization axiom: (N) sector-surjectivity — every quantized boundary charge in the arena M_γ is realized by some torsion datum. Under (N), |e| = 1 (Q = ±n); without (N), e ∈ ℤ is undetermined (any faithful choice e ≠ 0 passes all consistency checks).*

## 4. Route 3 — domain-wall sector transport (brief)

Treating the layer as a wall between two tight copies: its boundary data on the leaf space concentrate at fix(γ) (same cylinder-trace argument), and the locality theorem then *permits* exactly the defect classes α_ρ with ρ anchored at ξ± — it constrains the support and quantization but not the value of e. Route 3 confirms Route 1's anchor structure and adds no normalization. [GAP-5] No independent bulk quantity computed here (e.g. the layer volume 4π²nℓ, linear in n) reproduces the quadratic D = Q²ℓ/2π; no matching was attempted or claimed.

## 5. [BOX 4] The bridge definition (choices itemized)

*One unit of Giroux torsion along T_γ acts on the boundary net as the defect-automorphism class α_{ρ_γ,e} with ρ_γ,e = e·(δ⁺_{ξ₊} − δ⁻_{ξ₋})-type anchored density, charge Q = e·n at the fix(γ) anchors, where:*

- *anchor set = fix(γ): **forced** (cylinder trace, §3);*
- *homomorphism structure Q = e·n: **forced** by additivity;*
- *sign under γ → γ⁻¹: **conventional** (orientation of c_γ);*
- *e ≠ 0: **forced** only if the bridge is required to be faithful on torsion data and NOT required to factor through plane-field homotopy — the latter exclusion is argued (§2, §6) but is itself a definitional stance [GAP-6];*
- *|e| = 1: **not forced**; follows only from normalization axiom (N) of Box 3 (named choice).*

*Extracted value: e = ±1 under (N) + faithfulness; e = 0 under a homotopy-factoring definition; e ∈ ℤ∖{0} in between.*

## 6. Kill evaluation (v2, armed)

Honest verdict: **INCONCLUSIVE — the bridge is underdetermined, and the determining choice is named.** Precisely:

- e = 0 is *not forced*: it follows only if one demands the bridge factor through homotopy invariants. There is a principled, pre-kill reason to reject that demand: round-1 established the quantized twist data (torsion n) as the bulk object, and torsion is homotopy-invisible (Box 2); a homotopy-factoring bridge annihilates the *entire* refereed bulk datum, making the correspondence empty by construction rather than falsified. This reason was available before the kill clauses were evaluated and does not depend on e. [GAP-6] Still, "the bridge must see contact—not homotopy—data" is a definitional commitment, not a theorem.
- e ≠ 0 is *not forced* either: no computation here pins the generator. Clauses (a)/(b′) are verified only **conditionally**, at the strength: "anchors and quantization forced; nonvanishing and unit normalization by named axioms (faithfulness, (N))."
- The contractible-projection clause is safe unconditionally: the construction attaches charge only along vertical tori over essential geodesics; there is no mechanism assigning charge to contractible-projection classes (knot-Lutz is excluded by round-1 (i)).

## 7. Simplicity prediction (s)

Bulk side, within the operation class {knot-Lutz, torus-torsion}: torsion insertion requires an **embedded** incompressible torus; all such in X are vertical over *simple* closed geodesics (round-1 (i)). For c non-simple, π⁻¹(c) is an immersed torus; there is no torsion-insertion operation along immersed tori in the literature known to me, and cut-and-reglue is undefined without embeddedness. Higher-genus "generalized torsion" along convex surfaces exists as a notion [others', partially — Colin–Honda-circle literature] but is not known to preserve (universal) tightness and does not canonically attach to a non-simple geodesic class. [GAP-7] I cannot *prove* no exotic tightness-compatible mechanism exists, but within the declared operation class, realizability over non-simple classes fails. Boundary side: the locality theorem admits defects at fix(γ) for *every* hyperbolic γ, simple or not. **The discriminating tension stands: prediction (s) is nonvacuous.**

## 8. Consistency checks

1. **Locality/anchors:** ρ supported on fix(γ) — derived (§3), ✔.
2. **Additivity:** n stacked unit layers = winding n ⟹ Q = e·n = n·(e·1), ✔ (built in via the homomorphism axiom, [GAP-4]).
3. **γ → γ⁻¹:** swaps ξ±, reverses crossing co-orientation ⟹ ρ ↦ −ρ, Q ↦ −Q, ✔ per convention.
4. **D-value:** D = Q²ℓ/2π = e²n²ℓ(γ)/2π — finite and computable; under (N), D = n²ℓ(γ)/2π. Noted honestly: the layer's contact volume 4π²nℓ is linear in n and does not match D's n²-scaling; no coincidence is claimed (§4).

## 9. Five-line summary

1. Route 2 is rigorous and yields zero: torsion changes no homotopy invariant of ξ (relative Euler class computed = 0; full class [others']), so e cannot be a homotopy pairing.
2. Route 1 yields canonical anchors fix(γ) (cylinder ideal trace — derived, matching the locality theorem unforced) and a canonical integer winding n per wall-crossing; but post-insertion there is no canonical weak-stable foliation ([GAP-3]), and winding ↦ charge is a postulated homomorphism k ↦ e·k ([GAP-4]).
3. **The bridge is underdetermined; the determining choice is named:** homotopy-factoring ⟹ e = 0 (kill fires); faithfulness + sector-surjectivity (N) ⟹ e = ±1, Q = ±n, D = n²ℓ/2π; additivity alone leaves e ∈ ℤ.
4. Kill verdict: **INCONCLUSIVE**, with a principled pre-kill argument (torsion is the refereed bulk datum and is homotopy-invisible) against the e = 0 route, but that argument is definitional, not a theorem ([GAP-6]).
5. Prediction (s) stands: within {knot-Lutz, torus-torsion}, quantized bulk data attaches only over simple closed geodesics (embedded incompressible tori are vertical-over-simple), while the boundary admits defects for all hyperbolic γ — the discriminating tension is real.
