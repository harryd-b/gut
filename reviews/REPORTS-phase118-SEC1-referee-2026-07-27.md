# Referee report — SEC-1 sector-energy column round (phase 118)

**Date:** 2026-07-27
**Reviewed document:** phases/phase118-SEC1-energy-column.md (consultation section)
**Referee:** context-free adversarial agent (independent re-derivations + independent truncated-Fock numerics; RESCUE mandate on the O3 ruling, including the modular-Hamiltonian route). Report preserved VERBATIM below; nothing edited.

**Editorial note (operator):** the referee's pre-report working notes (transmitted with the report) are included at the top for completeness, as they contain the independent-findings summary.

---

Numerics complete. Key independent findings before drafting the report:

- Degeneracy claim p(N)=1,1,2,3,5 confirmed mathematically — but the submission's own stated truncation (4 modes, occupation ≤3) yields 1,1,2,3,**4** at N=4 (the partition 1+1+1+1 needs n₁=4). Their verification as described could not have produced their reported numbers.
- K-SEC-1 identity 2πh_q = Q²/2 exact — but the pass requires an unregistered third conversion (weight→phase factor 2π) beyond BOX-1 and the branch convention.
- Cylinder monotonicity: with the standard c=1 Casimir, E_ℓ is decreasing only for Q² > π/6 ≈ 0.72 — it fails at the submission's own test point Q=0.7. GAP-6 is overstated.
- Positivity audit: the record's literal commutator sign with the standard annihilation convention gives negative norms; the submission silently relabeled.
- Modular rescue attempted: Bisognano–Wichmann/Hislop–Longo interval flows give canonical clocks for free, so the O3 diagnosis "missing a clock" is wrong — but modular time is dimensionless and interval choice is a frame choice, so O3 itself survives.

Writing the referee report.

# REFEREE REPORT — SEC-1 SUBMISSION

## Verdict summary

The submission is **substantially confirmed with corrections**. All load-bearing algebra checks out under independent re-derivation and independent numerics: the L₀ spectrum, the p(N) degeneracy law, the K-SEC-1 factor identity, and the pair-sector floor identity are all exact. However: (1) the submission's *reported verification* of the degeneracies is internally impossible as described (its stated truncation cannot produce its stated numbers); (2) the K-SEC-1 pass silently uses a third, unregistered conversion (weight→phase, factor 2π) beyond the two the kill licenses; (3) K-SEC-2, read strictly, **fires on the column as posed** — the object survives, but only under the name "sector weight," not "sector energy"; (4) the cylinder-frame tension (GAP-6) is overstated and fails at one of the submission's own test points; (5) the mandated rescue of O3 via modular theory fails to overturn O3 but refutes the submission's closing diagnosis: canonical clocks exist for free in the record's modular structure; what is missing is a canonical subalgebra choice and a *scale*, not a clock. COLLIDE-2 = O3 stands. K-MASS-3 does not fire.

## Per-claim analysis

### §1–§2: Definition, spectrum, degeneracies (Mandate 1)

Hand re-derivation: with a₀|q⟩ = q|q⟩ and L₀ = ½a₀² + Σ_{k≥1}a_{−k}a_k, lowest weight is h_q = q²/2 and excited eigenvalues are q²/2 + Σk·n_k; degeneracy at level N is the partition count p(N). Confirmed.

Independent numerics (my own script, truncated Fock matrices, commutator residuals ≤ 3.6e−15):

- modes 1–4, occupation ≤ 4: degeneracies 1, 1, 2, 3, 5 at N = 0..4 — matches p(N). Adding mode 5, occ ≤ 5: 1, 1, 2, 3, 5, 7 through N = 5. **Claim confirmed.**
- modes 1–4, occupation ≤ 3 (the submission's stated truncation): degeneracies 1, 1, 2, 3, **4** at N = 0..4. The state (a₋₁)⁴|0⟩ requires n₁ = 4 and is cut off. The submission's reported "1,1,2,3,5 at occupation ≤ 3" is impossible as described. The mathematical claim survives (I verified it independently); the submission's verification record is defective (C-SEC-R1).
- Spectrum shifts rigidly by q²/2 with degeneracies unchanged. Confirmed.

Sign audit: the record's literal [j_m, j_n] = −2πmδ_{m+n} gives [a_k, a_{−k}] = −k for k > 0; combined with a_{k>0} annihilating the vacuum this yields negative norms (⟨0|a_k a_{−k}|0⟩ = −k), contradicting positivity of ω(W(f)) = e^{−π Σk|f̂_k|²}. Positivity of the refereed state forces the effective +k convention (equivalently, the opposite mode-labeling under the chirality flag). The submission's numerics silently used +k. Forced, hence harmless — but it is an unstated step and the chirality bookkeeping should be recorded (C-SEC-R5).

"Only gap ratios fully frame-invariant" (§2, Mandate 5): correct *as scoped*. The frame moves actually in play (circle ↔ ℓ-cylinder) act affinely on the spectrum (scale 2π/ℓ, shift by Casimir); differences are shift-invariant but scale-covariant, ratios invariant under both. Under general Schwarzian reparametrizations even this fails, but no such frame is a candidate here. The honest-deficit paragraph (calling k a "frequency" presupposes a clock) is correct and consistent with §4.

### §3: K-SEC-1 (Mandate 2)

Algebra: q = Q/√(2π) ⇒ h_q = Q²/4π ⇒ 2πh_q = Q²/2, so D_spin = ∓Q²/2 + nQ²/2 = 2πh_q(n∓1). Exact by hand; my numerics confirm to ≤ 1.4e−14 at Q ∈ {0.7, 1.0, 3.2, 11.0}, both branches, multiple n.

Attack on the pass. The registered kill demands the column's Q²-part reproduce D_spin's Q²-part "under the forced conversion plus the chirality-branch convention." Those two licensed inputs supply q ↔ Q and the ∓ sign — **neither supplies a 2π**. The column's Q²-part is Q²/4π; D_spin's is Q²/2. On the strict literal reading the kill FIRES: the coefficients differ by 2π, and the submission closes the gap with a third conversion (weight→phase via e^{2πih}) that was never registered.

Can the strict reading be sustained? I rule no, for two reasons. First, e^{2πiL₀} is the full rotation of the record's own circle — a purely spectral, kinematic operation requiring no zero-mode evolution; the phase 2πh_q it assigns is internal record data, not imported dynamics. Second, and decisively: the refereed D_spin's own framing unit is Q²/2 = 2πh_q — D_spin's n-ambiguity quantum *already* equals 2π × weight, so D_spin is dimensionally a phase. Demanding a weight equal a phase without the 2π is a category error under which every conceivable column fails, making the kill vacuous rather than strict. The natural reading — Q²-structure must match after the standard phase identification — is the registered intent, and it passes with the nontrivial bonus that branch unit and framing unit coincide (both 2πh_q).

**Ruling: K-SEC-1 DOES NOT FIRE**, conditional on the weight→phase conversion being explicitly registered (C-SEC-R2). GAP-4 (single shared assumption BOX-1) is honest and stands; note additionally that the 2π is shared with D_spin's phase character, so the test is one identity, not three.

### §4: K-SEC-2 scoping and COLLIDE-2 (Mandate 3)

The registered wording: "if defining or evaluating the column requires zero-mode evolution, the column dies AS POSED." Defining and evaluating A = (L₀ eigenvalue) + (declared constant) requires no evolution — pure spectral data. So the *object* survives the literal antecedent.

But the column was posed as sector-**ENERGY**. The submission itself proves (BOX-4, correctly) that attaching energy semantics — any frame in which A or its rescaling is "the energy" — is exactly the blocked dynamical declaration. An "energy column" that cannot, in principle within scope, be an energy is not honestly registrable under that name: evaluating the column *as posed* (as an energy) requires the blocked step, so the kill's antecedent is met on the name.

**Ruling: K-SEC-2 FIRES on the registration as posed.** What survives, precisely: the identical mathematical object re-registered as the **sector weight column** (L₀/scaling-dimension column) — dimensionless; frame-robust data = differences (shift-invariant) and ratios (fully invariant); degeneracy grading p(N); floor values h_q = q²/2. A conditional clause may be attached: it upgrades to an energy column upon exactly one refereed dynamical input. This is a rename plus honesty repair, not a demolition — the submission's own §4 diagnosis concedes the substance (C-SEC-R3).

Cylinder tension audit: the submission asserts frame (2) gives E_ℓ = (2π/ℓ)(h_q + C_frame) "DECREASING in ℓ." With C_frame declared-not-computed, the monotonicity direction is *undetermined* (sign of h_q + C_frame). With the standard c = 1 Casimir −1/24, E_ℓ decreases iff h_q > 1/24, i.e. Q² > π/6 ≈ 0.724 — this **fails at the submission's own test point Q = 0.7** (h = 0.0390 < 1/24 = 0.0417), where E_ℓ is increasing in ℓ, i.e. no tension with MASS-1 at all. GAP-6 must be scoped: the dormant tension exists only for h_q + C_frame > 0 (C-SEC-R4). The rate D = 2h_qℓ is increasing always (h_q > 0); confirmed.

### Mandate 4: RESCUE attempt on O3

Attempted rescue via structure already in the record. (a) *Modular route.* The record is built on modular data; by Bisognano–Wichmann/Hislop–Longo, the vacuum modular flow of any interval algebra of the chiral U(1) net is the Möbius flow preserving the interval — a canonical one-parameter group with **zero** new dynamical input, with modular Hamiltonian K_I a local weighted integral of T. This defeats the submission's *diagnosis*: canonical clocks exist for free; "the missing ingredient is a Hamiltonian/clock" is wrong as stated. But the rescue fails to produce a canonical *energy*: (i) modular time is dimensionless — matching the flow parameter to a physical unit is precisely the blocked scale declaration; (ii) there is no canonical interval — choosing I is choosing a frame — and the global pure vacuum has trivial modular flow, so no interval-free option exists. Modular data yields more dimensionless invariants (e.g., relative entropies of sector states, functions of h_q), i.e. more members of the same class as A, never a scale. (b) *Rate route.* E := πD/ℓ² = (2π/ℓ)h_q is *computable* from refereed data (D, ℓ) with no evolution — but the claim that this combination is "the energy" is the cylinder-frame declaration itself; D's refereed status is as an E1 rate, and arithmetic availability of a number is not energy semantics. Rescue fails on interpretation, not computability.

**Ruling: O3 CONFIRMED** — mass = sector energy fails structurally within the data-only extension — with the diagnosis amended: what is missing is a canonical subalgebra/frame choice plus a scale (unit), not a clock (C-SEC-R6). K-MASS-3 correctly does not fire: no *derived* decreasing M(ℓ) exists (and per C-SEC-R4, even the conditional decrease is Q-dependent). MASS-1 stands as M(D,Q).

### §5: Pair sector (Mandate 5)

Hand check: gap(q) := A_lw(q) − A(0) = q²/2 is C_frame-free; gap(q₁+q₂) − gap(q₁) − gap(q₂) = q₁q₂ exactly. Numerics: max error 2.8e−14 over 1000 random draws. Negative for opposite charges. Confirmed. The caveats are correct and load-bearing: two localized defects at finite separation are excited states of F_{q₁+q₂} (spectrum h_{q₁+q₂} + ℤ≥0, so the lowest weight is genuinely the infimum/floor — verified structure); any separation-dependent potential reading requires the blocked dynamics; and calling q₁q₂ a binding *energy* imports the unresolved scale, consistent with the K-SEC-2 ruling above (it is a binding-shaped *weight* datum).

## Corrections ledger

- **C-SEC-R1** (verification defect): The stated truncation (4 modes, occupation ≤ 3) yields degeneracies 1,1,2,3,**4** at N = 0..4, not the reported 1,1,2,3,5 — the level-4 state (a₋₁)⁴|0⟩ is cut off. The p(N) law itself is correct (independently verified at occupation ≥ 4). The submission's numerical record is misreported and must be re-run or restated.
- **C-SEC-R2** (K-SEC-1): The pass requires a third conversion — weight→phase, factor 2π via e^{2πiL₀} — beyond BOX-1 and the branch convention. Register it explicitly; it is kinematic (spectral, no zero-mode evolution) and independently forced by D_spin's framing unit already equaling 2πh_q. Unregistered, a literalist referee could fire the kill.
- **C-SEC-R3** (K-SEC-2): Fires on the name. "Sector energy" is not honestly registrable; the column registers as the **sector weight column**, energy semantics conditional on one refereed dynamical input.
- **C-SEC-R4** (GAP-6 scope): "Cylinder frame ⟹ energy decreasing in ℓ" holds only for h_q + C_frame > 0; with the standard −1/24 it fails for Q² < π/6 ≈ 0.724, including the submission's own test point Q = 0.7. The dormant tension is Q-dependent and C_frame-dependent.
- **C-SEC-R5** (sign bookkeeping): The record's literal [a_m, a_n] = −mδ_{m+n} with standard annihilators gives negative norms; positivity of ω forces the +k relabeling silently used. State it (chirality-label bookkeeping), else the numerics verify a different algebra than the record literally declares.
- **C-SEC-R6** (O3 diagnosis): Modular theory (interval modular flows, already within the record's modular data) supplies canonical dimensionless clocks at zero cost. The missing ingredient for an energy is a canonical subalgebra choice plus a scale/unit — amend §4's closing diagnosis accordingly.

## VERDICT BOX

1. **K-SEC-1: DOES NOT FIRE** (pass valid once the 2π weight→phase conversion is registered; C-SEC-R2).
2. **K-SEC-2: FIRES AS POSED** on the name "sector energy"; column survives re-registered as sector **weight** column (C-SEC-R3).
3. **COLLIDE-2: outcome O3 CONFIRMED**; modular and rate-route rescues fail to yield a canonical scale; diagnosis amended (C-SEC-R6). **K-MASS-3: DOES NOT FIRE**; MASS-1 stands as M(D,Q).
4. All core identities independently verified (spectrum, p(N), 2πh_q = Q²/2, pair floor q₁q₂); one verification misreport (C-SEC-R1), one overstated tension (C-SEC-R4), one silent sign relabeling (C-SEC-R5).
5. **Overall: CONFIRMED WITH CORRECTIONS — registration granted under amended name.**

Word count: ≈ 1,960.
