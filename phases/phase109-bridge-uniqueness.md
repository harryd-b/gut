# Phase 109 — convention upgrades, part 2: C-BRIDGE uniqueness and the quadratic bulk invariant (REFEREED 2026-07-26; rigidity + e-odd CONFIRMED; W ruled reverse-engineered; |e| = 1 stays a postulate — see Amendment)

*Working session, 2026-07-26, executing the operator's instruction to reduce the postulate content of C-BRIDGE. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered; C-BRIDGE stands as adopted until a referee rules].***

*Headline claims (pre-verdict): (1) RIGIDITY THEOREM (unconditional): any bridge satisfying monoidality + locality + MCG-equivariance is multiplication by one integer PER MCG-ORBIT of simple closed geodesics — 1 + ⌊g/2⌋ constants (non-separating orbit + one per separating type), NOT one global e; equivariance forces orbit-constancy and nothing across orbits. (2) The braiding route is CLOSED: the intersection fibers of two torsion walls are Legendrian, the four ξ-tangency marked points alternate rigidly (carrying only î), and the continuous crossing-angle datum is an unquantized modulus — no canonical bulk U(1) phase exists; any postulated one is circular. (3) The session's hoped-for claim "mod-1 spin matching forces e² = 1" is CORRECTED: it forces only e ODD (e = 3 passes: 4n² ∈ ℤ) — equivalent to the unconditional parity axiom P′ (winding parity ↦ statistics parity), which already gives e odd hence nonzero (bridge injectivity for free). (4) Every naive single-pass rotation quantity along the wall is 0 or LINEAR in n (relative rotation 0; parabolic shear −2πnℓ; helicity ∝ n) — but a genuine QUADRATIC self-pairing exists: the endpoint-half-weighted orbit-tower framing sum S(n) = ½·0 + Σ₁^{n−1}k + ½·n = n²/2 exactly, over the tower of σ-Reeb tori at t = k/n, with the ½-endpoint convention identified as the BULK TWIN of boundary minimal subtraction. (5) CONDITIONAL THEOREM: under hypothesis H-QUAD (S(n) is canonical — presentation-independent, ½-convention justified) and axiom W (the bridge matches real-valued lowest weights, not just spin phases), |e| = 1 per orbit — postulate (N) becomes a theorem. Net postulate content after this work: faithfulness + P′ (structural, unit-free) + H-QUAD/W, replacing the bare numerical (N). Goes to a context-free referee before any verdict; the adversarial crux is whether S(n) is canonical or reverse-engineered.*

---

## The derivation, verbatim

# SPAN-2: Reducing the postulate content of C-BRIDGE

**Status of inputs.** All round-2 facts, the locality theorem, the boundary dictionary (braiding q₁q₂î, spin ∓q²/2 + n_fr q²/2, parity (−1)^q, conjugation), and the forced parts of C-BRIDGE (anchors, homomorphism k ↦ e·k) are taken as given [others']. The target is the bare postulate (N): |e| = 1.

## 1. The uniqueness scaffold (Task 1)

**Definition 1 (geometric side G).** Objects: finite formal decorations D = {(γ₁,n₁),…,(γ_k,n_k)}, the γᵢ distinct *oriented* essential simple closed geodesics on Σ_g (g ≥ 2), nᵢ ∈ ℤ. Crossings are *allowed and carried as structure*, not excluded: each unordered pair carries the canonical integer î_ij (signed crossing number of axes; homologically ⟨[γᵢ],[γⱼ]⟩), and the object carries the pairing matrix (nᵢnⱼî_ij). Monoidal structure: union of decorations, adding nᵢ on a repeated geodesic; unit = ∅. Involution ρ: orientation reversal of a geodesic. Symmetries: Γ = MCG(Σ_g), acting through unique geodesic representatives of essential isotopy classes [others': hyperbolic-surface standard].

**[GAP-1]** A multi-wall object with crossings is *formal bookkeeping only*: two torsion collars over crossing geodesics overlap along fiber circles, and the simultaneous insertion is not a defined contact operation. This does not affect the rigidity theorem, whose axioms constrain F on single-geodesic objects; it does block one route in §2.

**Definition 2 (sector side S).** ℤ-graded sectors of the compactified chiral U(1) lattice net, with anchoring data (pair of boundary points); fusion q ⊗ q′ = q + q′; braiding phase e^{iπqq′î}; lowest conformal weight h_q = q²/2 ∈ ℝ (spin = h_q mod 1); conjugation q ↦ −q; statistics parity (−1)^q.

**Axioms on a bridge F: G → S.** (i) Monoidality per geodesic; (ii) locality: F(γ,n) is anchored at fix(γ); (iii) equivariance: for φ ∈ Γ, F(φγ,n) is the same abstract sector as F(γ,n), and F ∘ ρ = (charge conjugation) ∘ F.

**Theorem 1 (rigidity).** Any F satisfying (i)–(iii) has F(γ,n) = (charge e_{[γ]}·n anchored at fix(γ)), with e_{[γ]} ∈ ℤ depending only on the Γ-orbit [γ], well defined up to global sign per orbit.

*Proof.* (i): by fusion-additivity of charge, n ↦ charge(F(γ,n)) is a homomorphism ℤ → ℤ, hence = e_γ·n. (ii) fixes the anchor as fix(γ). (iii): "same abstract sector" means equal image under a grading-preserving identification of sector categories; the grading automorphisms of ℤ compatible with fusion are q ↦ ±q **[GAP-2:** I use that any automorphism of the sector category preserving fusion is ±id on the grading group; for ℤ this follows from Aut(ℤ) = {±1}, both of which preserve spin q²/2 and braiding up to overall conjugation — but a referee should confirm the boundary Γ-action is implemented by such automorphisms**]**. Hence |e_γ| is Γ-orbit-constant; ρ-equivariance is automatic for every e (torsion −n on γ̄ ↦ charge −en, consistent) and absorbs the sign. ∎

**Orbit count, honestly.** Γ acts transitively on non-separating simple closed curves, and on separating curves of each splitting type h ∈ {1,…,⌊g/2⌋} [others': change-of-coordinates principle, Farb–Margalit]. Transitivity gives *nothing across orbits*: G as defined has no relation identifying a separating decoration with non-separating ones (separating classes are null-homologous; no monoidal relation merges orbits). So a priori e does differ between orbits.

**[BOX 1] Space of admissible bridges = ℕ^{1+⌊g/2⌋}:** one non-negative integer |e₀| (non-separating orbit) plus one |e_h| per separating type h = 1,…,⌊g/2⌋, signs being pure orientation convention. Equivariance forces a single constant *per orbit*, not one global e; the honest count of independent constants is 1 + ⌊g/2⌋. (N) asserts |e₀| = 1 (and per-orbit analogues). **[GAP-3:** if the program's tightness class only realizes torsion on non-separating γ, only e₀ is operative; unverified here.**]**

## 2. The braiding route is closed (Task 2)

The bulk crossing datum n₁n₂î is a unit-free integer; the boundary braiding of images is the *phase* e^{iπ(e₁n₁)(e₂n₂)î}. A matching axiom needs a canonical bulk phase at a crossing. I looked for one in the contact data of T_{γ₁} ∩ T_{γ₂} = the fiber circles T¹_pΣ over crossing points p.

Computation (Fermi/flat model α = cosθ cosh t dσ + sinθ dt; fiber tangent ∂_θ ∈ ker α): the fiber is *Legendrian*. Wall T_{γᵢ} is ξ-tangent exactly along its two circles of unit normals (θ = φᵢ ± π/2); on the fiber over p these cut four marked points which *alternate cyclically for every crossing angle* — the configuration is combinatorially rigid and carries only the crossing sign already encoded in î. The continuous datum, the ξ-framing comparison of the two walls along the fiber, is the crossing angle φ₂ − φ₁ ∈ (0,π): a modulus of the pair of geodesics, *not quantized by ξ*, hence not canonical. Finally, no glued contact structure exists whose holonomy could be measured [GAP-1].

**Verdict: route closed.** There is no canonical bulk U(1) phase at a crossing; positing one of the form e^{iπc·n₁n₂î} imports the unit c and is circular. **Salvage (parity):** both sides carry canonical mod-2 data — bulk winding parity n mod 2 (the refereed canonical integer, reduced), boundary statistics parity (−1)^q. The structural axiom **(P′)**: *F sends winding parity to statistics parity* is non-circular (no unit appears) and forces (−1)^{e_h n} = (−1)^n for all n, i.e. **each e_h is odd** — in particular e_h ≠ 0. Crossing-parity matching adds nothing beyond this (and reaches only e₀, since separating classes pair to î = 0).

## 3. The spin route (Task 3): computations

Coordinates: Fermi collar of γ, metric cosh²t dσ² + dt², θ = angle from ∂_σ; tautological contact form α = cosθ cosh t dσ + sinθ dt; on T_γ = {t=0}, α| = cosθ dσ (the round-2 form). Reeb = geodesic flow; wall orbit R_γ = {t=0, θ=0}, length ℓ. All formulas below verified symbolically (sympy).

**(3a) Rotation of ξ relative to TT_γ along R_γ.** At orbit points α = dσ, dα = −dt∧dθ, so ξ = span(∂_t, ∂_θ) while TT_γ = span(∂_σ, ∂_θ). The line ξ ∩ TT_γ = ℝ∂_θ is *constant* along the orbit: **relative rotation = 0**. The linearized flow on ξ in the frame (∂_t, ∂_θ) is the Jacobi system j″ = j (K = −1): hyperbolic, constant eigendirections (1,±1), no rotation.

**(3b) What n units of torsion do along the wall.** Layer model (T² × [0,1], α_n = cos(2πnt)dσ − sin(2πnt)dθ); computed Reeb field R = cos(2πnt)∂_σ − sin(2πnt)∂_θ, with t invariant. Along the wall (fixed t) the plane field is σ-independent: torsion is a purely transverse phenomenon, and the rotation datum of (3a) remains **0 for every n**. The new linearized datum along the wall orbit is a parabolic shear δθ ↦ δθ − 2πnℓ·δt per period: **linear in n**. Other canonical single-pass quantities: layer helicity ∫α∧dα = −2πn·Area (linear); the swept flux-area of [α|_{T_t}] in H¹(T²;ℝ) (linear). **Honest interim verdict (b): every single-pass contact quantity of the wall is linear or zero in n; no rotation-number candidate is quadratic.**

**(3c) The quadratic candidate: the orbit-tower self-weight.** Quadratic n² can only arise by pairing the decoration with the winding — a *self*-pairing. The layer supplies a canonical one. The Reeb direction rotates through n full turns across the layer; the tori on which Reeb is σ-directed (parallel copies of the wall-orbit torus) occur at t = k/n, k = 0,…,n, boundaries included. By the localized form of the refereed winding fact **[GAP-4:** the refinement "ξ-winding across the sub-layer [0, k/n] equals k" of the refereed total winding n; needs one-line referee check**]**, the ξ-framing of the k-th torus relative to the wall is exactly k. Define the wall's self-weight as the endpoint-half-weighted total relative framing:

  **S(n) := ½·0 + Σ_{k=1}^{n−1} k + ½·n = n²/2**  (exactly; verified).

The ½-endpoint weight is the standard interval-boundary (Maslov endpoint) convention [others'], with a structural justification here: the two boundary tori are shared interfaces with the ambient tight side, so each belongs half to the layer. **[GAP-5:** presentation-independence of S(n) and a first-principles derivation of the ½-convention are the residual checks; note this ambiguity is the exact bulk twin of the boundary framing term n_fr·q²/2 removed by minimal subtraction — an unweighted count gives n(n±1)/2 = n²/2 ± n/2, i.e. shifts by "half-integer framing", and the symmetric convention is the bulk minimal subtraction.**]**

**(3d) The matching equation — with a correction to the task's phrasing.** Two inequivalent versions:

- *Mod-1 spin matching*: (en)²/2 ≡ n²/2 (mod 1) for all n forces only **e odd**, *not* e² = 1. Explicitly e = 3 passes: (9−1)n²/2 = 4n² ∈ ℤ. The claim "spin matching mod 1 forces e² = 1" is **false**; I flag this plainly. Mod-1 spin matching reproduces exactly the parity constraint of §2.
- *Real-valued weight matching (axiom W)*: the charge-q sector's lowest conformal weight is the real number q²/2, not merely a phase. The axiom *F matches the bulk self-weight to the lowest weight*: (en)²/2 = S(n) = n²/2 in ℝ for all n. This forces **e² = 1**. The chirality sign ∓q²/2 in D_spin pairs with the torsion orientation sign **[GAP-6:** the sign convention matching (left/right mover vs. torsion sign) is bookkeeping I have not re-derived**]**.

**[BOX 3] Conditional theorem.** *Let F satisfy (i)–(iii). IF (H-QUAD): the endpoint-half-weighted orbit-tower framing sum is a well-defined canonical invariant of the torsion wall equal to n²/2 (checks: [GAP-4], [GAP-5]); and IF the bridge satisfies the weight axiom (W); THEN |e_{[γ]}| = 1 on every orbit — (N) becomes a theorem.* Independently, the parity axiom (P′) alone yields unconditionally: every e_{[γ]} is odd, hence nonzero (injectivity of the bridge for free). Deliverable class: **(a)**, with the canonical bulk quantity computed, not guessed — but conditional on the framing-convention check, exactly as honesty requires.

## 4. Verdict (Task 4)

**[BOX 4] Postulate content of C-BRIDGE after this work.**
- *Removed:* (N) as a bare numerical postulate.
- *Unconditional (Theorem 1):* the bridge is one integer per MCG-orbit of decorated geodesics: 1 + ⌊g/2⌋ constants, signs conventional.
- *Nearly free (axiom P′ — structural, imports no unit):* each constant is odd; in particular nonzero.
- *Remaining single geometric hypothesis:* **H-QUAD** — the orbit-tower self-weight S(n) = n²/2 is canonical (presentation-independent; ½-endpoint convention = bulk minimal subtraction) — plus the weight axiom W (match real weights, not spin phases). Together: |e| = 1 per orbit.
- *Honest negatives:* the braiding-phase route is closed (no canonical bulk U(1) crossing phase exists; any postulated one is circular); mod-1 spin matching can never do better than "e odd"; separating-orbit constants are invisible to crossing constraints (î = 0) and are reached only orbit-wise via P′/W; multi-wall crossing objects are formal, not contact insertions.
- *Referee checklist:* [GAP-2] boundary Γ-action is by grading-±1 automorphisms; [GAP-4] sub-layer winding localization; [GAP-5] presentation-independence and the ½-endpoint convention for S(n); [GAP-6] chirality/orientation sign pairing; [GAP-3] whether separating-orbit decorations occur in the tightness class at all.

## 5. Five-line summary

1. Rigidity is unconditional: axioms (i)–(iii) force the bridge to be one integer per MCG-orbit — 1 + ⌊g/2⌋ constants, not one global e.
2. The braiding route is closed: a crossing of torsion walls carries no canonical bulk phase, only the known integer î; a phase axiom would be circular.
3. Along the wall, every rotation-type quantity is zero or linear in n (shear −2πnℓ; helicity ∝ n): naive spin candidates fail, and mod-1 spin matching provably forces only *e odd* (e = 3 survives), correcting the hoped-for claim.
4. The quadratic datum exists as a self-pairing: the endpoint-half-weighted sum of ξ-framings over the layer's tower of σ-Reeb tori equals exactly n²/2; matching it to the real-valued lowest weight (en)²/2 forces e² = 1.
5. Net result: (N) is replaced by parity-preservation (giving e odd, unconditionally) plus one checkable geometric hypothesis — H-QUAD, canonicity of the n²/2 orbit-tower invariant under the symmetric endpoint convention — with faithfulness intact; the sole residual referee burden is [GAP-4]/[GAP-5].

---

## AMENDMENT — referee verdicts entered (2026-07-26)

*Context-free adversarial referee pass completed 2026-07-26; report verbatim in `reviews/REPORTS-phase109-bridge-referee-2026-07-26.md`. The referee verified all differential geometry symbolically and ran the tower arithmetic in every convention — including the trap set in the brief, which fired. Standing AI-referee caveat applies.*

### A.1 Confirmed [refereed]

- **Theorem 1 (rigidity) with repair C-Q1**: the equivariance axiom must include "+id on oriented-curve stabilizers" (otherwise a −id implementation on a curve-preserving mapping class would force e = 0); with it, the bridge is one integer per MCG-orbit, **1 + ⌊g/2⌋ independent constants** [refereed].
- **Braiding closure** [refereed]: no canonical bulk crossing phase exists; a phase axiom would be circular. Deflation adopted: **P′ ≡ mod-1 spin matching** — one constraint, not two independent corroborations.
- **All B3 computations** verified symbolically (rotation 0; shear −2πnℓ; helicity ∝ n).
- **Unconditional refereed gain: each e_orbit is ODD, hence nonzero — the bridge is injective.** This survives everything.

### A.2 Correction C-Q2 — the tower was misstated; the arithmetic is stronger than claimed

The true Reeb-parallel tower has **2n+1 tori at t = k/(2n)** (the trap in the brief, confirmed). The restriction to the +∂_σ sub-tower is orientation-canonical, and — the referee's strengthening — **both** oriented sub-towers independently give n²/2, the −tower with *no endpoint convention at all*. The claimed reflection-symmetry justification of the ½-convention is WRONG (both symmetric conventions are already reflection-invariant); the genuine selector, verified by the referee, is **concatenation additivity** (only the trapezoid weighting satisfies S(n)+S(m) = (n+m)² /2 under layer stacking). Adopted with these repairs: the oriented Reeb-tower trapezoid sum = n²/2 is genuine geometry.

### A.3 Correction C-Q3 (decisive) — axiom W is reverse-engineered; |e| = 1 remains a postulate

The referee's killing test: the equally-canonical FULL tower gives S = n², under which W forces e² = 2 — no integer solution. That an unresolved normalization choice decides between "|e| = 1" and "inconsistency" proves W's entire content is the normalization, i.e. the conclusion. **H-QUAD-as-normalized-invariant: UNPROVEN. The conditional theorem is formally valid but epistemically empty beyond the e-odd part.**

### A.4 C-BRIDGE status after this phase

Postulate content, final refereed form: **faithfulness + P′ (theorem-grade consequence: e odd per orbit, nonzero, injective) + the residual normalization |e| = 1 per orbit** — which is now understood as a pure choice of charge unit (equivalently: which lattice extension the bulk selects), the mildest kind of postulate, but a postulate. The adopted C-BRIDGE convention stands unchanged in force, with its disclosure updated to this sharper decomposition. [Interpretation, tagged: an odd e ≠ ±1 would mean the bulk generates only a sublattice of charges — the normalization postulate asserts the bulk sees the full lattice.]
