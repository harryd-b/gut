# Referee report — M-FRAME deciding computation (phase109-MFRAME-decider.md)

**Date:** 2026-07-26
**Referee:** context-free adversarial agent (independent re-derivation + independent FFT numerics).
**Editorial note (operator):** Preserved VERBATIM below. Verdict: CONFIRMED-WITHIN-SCHEME — the oscillator sector is fully verified, but the framing mechanism decides only the global-framing scheme; the D-MS/framing-deleted binary is NOT closed. Corrections entered as C-S1..C-S5 in the phase file's Amendment.

---

## REPORT (VERBATIM)

# Referee report: M-FRAME deciding computation (phases/phase109-MFRAME-decider.md)

**Independent verification performed:** full re-derivation of the oscillator/Berry sector from the stated one-particle structure; independent FFT numerics (N = 2¹⁸, my own script, since deleted); line-by-line audit of the zero-mode mechanism against the refereed conventions in `phases/phase105-Dspin-self-phase.md` and the registration `phases/phase109-DMS-upgrade.md`.

## (C) Oscillator part — VERIFIED, independently and exactly

**Berry formula.** For the coherent family p̂ₖ(t) = p̂ₖe^{−ikt} in ⟨f,g⟩ = 2πΣ_{k≥1}k f̂ₖ*ĝₖ: ⟨p_t,ṗ_t⟩ = −2πiΣk²|p̂ₖ|², so ∫₀^{2π}Im⟨p_t,ṗ_t⟩dt = −4π²Σk²|p̂ₖ|²; with the orientation sign this is Φ_osc = 4π²Σ_{k≥1}k²|p̂ₖ|² = 4π²Σ|η̂′ₖ|². Cross-check against the refereed product formula (phase105-Dspin line 27, Φ = ½∮σ(η_t,∂_tη_t)dt with σ = −2Im⟨·,·⟩): identical. Every 2π checks.

**Parseval.** E = 2πΣ_{k∈ℤ}|η̂′ₖ|², η̂′₀ = Q/2π ⟹ 4π²Σ_{k≥1}|η̂′ₖ|² = πE − Q²/2 **exactly** (zero o(1) for smooth scaling shapes, since E = c_ρQ²/ε exactly). Verified.

**Pair cross term.** Disjoint supports ⟹ Σ_{k∈ℤ}η̂′₁ₖ*η̂′₂ₖ = 0 ⟹ chiral cross = −(k=0 cross) = −Q₁Q₂ exactly, δ- and ε-independent. Verified.

**My numerics** (independent script, FFT mode sums):
- Gate finite part Φ − πc_ρQ²/ε: quad (c_ρ=1.2) and quart (c_ρ=10/7), ε ∈ {0.025, 0.05, 0.1, 0.4}, Q ∈ {1, 1.7}: **−0.5000000 / −1.4450000** at every setting (6–7 digits). Box shape: −0.5045 at ε=0.025, −0.4998 at ε=0.4 — resolution artifact growing as ε↓, consistent with [GAP-3].
- M₀ = Φ_pair − Φ₁ − Φ₂, mixed shapes, (Q₁,Q₂) ∈ {(1,2),(0.7,1.3)}, ε ∈ {0.05,0.1}, δ ∈ {0.5,1.0,2.5}: **−2.0000000 and −0.9100000 in all 12 cases** (7 digits).
- Discrete Pancharatnam vs mode sum (Q=1, ε=0.1): 37.1752 at 3200 steps, 37.1976 at 12800, exact 37.1991 — matches the submission's 37.175 / 37.199.

All of the submission's Section 3 numbers reproduce. The n-table (lines 84–91) is arithmetic given Φ_zm, as the submission itself concedes (line 82).

**One error found in the oscillator sector (line 37):** "The antichiral projection gives πE + Q²/2." False as a projection statement: for real η′, Σ_{k≤−1}|η̂′ₖ|² = Σ_{k≥1}|η̂′ₖ|², so the antichiral sum gives the **same** πE − Q²/2; no orientation choice produces πE + Q²/2 while keeping the divergence positive. The claimed value requires assigning the k=0 mode to the antichiral sum (k≤0 vs k≥1) — a zero-mode ownership **convention**, not a derivation. So "the ∓ chirality branch is derived, not inserted" is overstated: in the refereed record the ∓ is transport orientation (phase105-Dspin line 39); here it is a zero-mode assignment matched to the gate. Not fatal (the gate's ∓ is refereed input either way), but it adds to the calibration ledger below.

## (A) The zero-mode/framing mechanism — NOT a consequence of the stated Weyl calculus

1. **σ(c,η) sign.** The stated form σ(f,g) = ∫fg′dθ gives σ(c,η) = c∫η′dθ = **+cQ**, not −cQ (line 41). The value −cQ is the by-parts form of σ(η,c). On multivalued profiles antisymmetry fails by exactly the monodromy boundary term cQ: ∫cη′ = +cQ but ∫ηc′ = 0. The pairing is genuinely undefined on (constants × winding profiles) without an extension choice. [GAP-1] correctly flags the sign, but the problem is deeper than a sign.

2. **The pairing is identically zero in the refereed representation.** Phase105-Dspin line 11 (the conventions under which the gate formula was refereed): "Constants are **null**: σ(c,f) = 0 and ‖c‖ = 0, so W(c) is represented trivially in the vacuum GNS representation." Consequently W(η_t + a(t)) = W(η_t) in the vacuum representation: the n ≠ 0 family is **unitarily identical** to the n = 0 family, and Φ_zm ≡ 0. "n extra deck loops of the branch section" corresponds to **no family of unitaries** in the stated calculus — it is a metaphor there. The mechanism requires the compactified/dynamical zero mode explicitly flagged in phase105-Dspin §5: "In a compactified model where the zero mode is dynamical, W(−Q·**1**) is a nontrivial zero-mode translation... flagged, not analyzed." That extension is not constructed here.

3. **What is calibrated vs structural.** In any zero-mode extension, the coefficient in Φ_zm = κ·Δa·Q_tot (sign, the ½, equivalently the compactification-radius/pairing normalization) is free; the gate fixes κ·Q = Q/2 per unit deck loop. So **sign, factor ½, and (per the antichiral finding) the ∓ assignment are all matched to the gate** — [GAP-1] understates. The single structural invariant is: *a spatially constant section pairs linearly with the total monodromy* ∫η′_tot = Q_tot. That linearity is robust, and it is the load-bearing feature: given gate calibration Φ_zm(single) = nQ²/2, substituting Q → Q_tot yields n(Q₁+Q₂)²/2 and the cross term nQ₁Q₂. **Conditional on framing being a zero-mode/constant-section winding, the D-MS cross term is forced.** The condition is the whole question — see (B).

4. The rejected candidate (line 47, fixed-period circle → linear-in-Q frame phase, fails quadratic gate) is a correct selection **among zero-mode realizations**. It does not select between zero-mode and non-zero-mode realizations.

## (B) The globality argument — Steps 1–3 hold; Step 4 is contradicted by the refereed record

**Step 1** (deck lattice (Q₁+Q₂)ℤ): correct for branches of η_tot, but the branch data of the *pair* (η₁,η₂) is a Q₁ℤ×Q₂ℤ torsor surjecting onto it; "one multivalued function" presupposes the global reading it is meant to establish.

**Step 2** (fallback): verified at common n: Σᵢ½nQᵢQ_tot = ½nQ_tot². At independent windings n₁ ≠ n₂: ½(n₁Q₁+n₂Q₂)Q_tot = ½n₁Q₁² + ½n₂Q₂² + **½(n₁+n₂)Q₁Q₂** — for n₁+n₂ odd, a half-integer multiple of Q₁Q₂, outside *both* rival forms. So the per-defect-deck assignment is not a coherent framing; this construction has **no per-particle framing at all**. The registration is posed at common n (phase109-DMS-upgrade line 90: "fixed ℓ, n, branch... one transport frame"; A.2: "a framing sector n ≠ 0"), so the submission answers the registered question — but only that question.

**Step 3** (localized constants not gauge): correct; σ(cχᵢ,f) = c∫χᵢf′ ≠ 0 changes the automorphism family.

**Step 4 — the decisive failure.** The claim "the only per-defect alternative... has no finite-ε Weyl realization" omits the third option, which is **the refereed record's own origin of n**. Phase105-Dspin line 45: offset passings at the crossing "shift the crossing contribution by integer multiples of Q²/2" — finite at finite ε, no divergence, no renormalization, localized at the defect's own crossing; refereed as part of the D_spin entry (Amendment, line 111), with its own gap only for |n| > 1 (multiply-wound passages). The Amendment to phase105 further *identifies* the C-D5 same-axis prescription ambiguity with framing. So a per-defect, finite-ε framing realization **exists in the refereed transport construction**: in the E3 single-anchor family, offset prescriptions at each defect's self-crossing with rigid mutual crossings give S(Qᵢ) = πc_ρQᵢ²/ε + (n∓1)Qᵢ²/2 — gate-passing per defect — and M = ∓Q₁Q₂, the framing-deleted answer.

The submission's step 4 attacks only a *renormalized local L₀ twist* (correctly: divergent core energy would spoil the gate's divergence coefficient). It never confronts the crossing-prescription realization, because its own transport family — rigid co-rotation of the total profile — **has no crossings** (phase105-Dspin §2(a) computed exactly this family and found "pure framing, no universal phase"; here the finite parts arise instead from chiral k=0 bookkeeping). The mechanism that produced n in the refereed gate formula is structurally invisible in the family chosen to decide n's pair behavior. Therefore "the finite-ε Weyl calculus as specified realizes only the global reading" (line 72) is family-relative, and the VERDICT BOX overrides the correct concession already present in [GAP-2].

## (D) The gate — genuine, correctly quoted

Phase109-DMS-upgrade line 21 states Φ_ε = πc_ρQ²/ε + (n∓1)Q²/2 + o(1) as refereed E3 input, c_ρ shape-dependent, finite part exactly shape-independent. The submission's conventions match (its density ρ = E3's step ρ′; c_ρ = ∫ρ²du = ∫ρ′²ds; finite part sign and (n∓1) grouping identical). The calibration is not spurious. One note: the E3 family (single-anchor loop, single-valued two-ramp profile, finite part from a crossing event) and the M-FRAME family (rigid rotation of a multivalued one-ramp profile, finite part from the chiral zero-mode subtraction) are **different families that produce the same Φ_ε** — the gate is passed by a different mechanism than the one that refereed it.

## (E) Scope — what is and is not decided

Fully correct as mathematics, the submission establishes: *in the rigid-rotation transport family, with framing defined as deck winding of the global branch section, in a zero-mode-extended representation calibrated to the gate, M = (n∓1)Q₁Q₂; and any zero-mode realization of framing forces the cross term nQ₁Q₂.* Still unresolved even then: (i) whether the registration's "transport construction" (A.2) denotes this family or the refereed E3 family, in which n≠0 pair transport is underdetermined — self- and mutual-crossing prescriptions are independent choices, and per-defect self-offsets yield M = ∓Q₁Q₂ at finite ε; (ii) per-particle framing n₁ ≠ n₂ (no realization in this construction; naive assignment gives the non-scheme value ½(n₁+n₂)Q₁Q₂); (iii) the zero-mode extension itself (unconstructed; sign, ½, and ∓ assignment all gate-matched); (iv) which definition of framing the genuine charged sectors (L₀-eigenvalue spin) realize — the standing sector-gap of phase105.

**Minimal repair** (exists, and is a re-scoping, not a fit): replace the verdict with the conditional above, and register the actual remaining decider: either (a) construct the compactified zero-mode representation and *derive* the pairing normalization now calibrated, or (b) compute the E3 crossing family at n ≠ 0 and show gate-consistent multiply-wound passages necessarily couple the mutual crossings (tying the self- and mutual-prescriptions), or show the per-defect offset totalization violates one of S1–S4. Absent that, both schemes possess finite-ε realizations of refereed pedigree, and A.2's binary stands.

---

## VERDICT BOX

**CONFIRMED-WITHIN-SCHEME.** The computation is correct where it computes: oscillator sector verified analytically and numerically to 6–7 digits (gate finite part −Q²/2 exact; M₀ = −Q₁Q₂ exact, δ/ε-independent; my numbers match the submission's throughout), and the deck arithmetic n(Q₁+Q₂)²/2 is exact bookkeeping *given* its premises. But it decides only the global-framing scheme, for three reasons established above: (1) Φ_zm is not a consequence of the stated Weyl calculus — in the refereed vacuum representation (constants null, phase105-Dspin line 11) the n≠0 family is unitarily identical to n=0 and Φ_zm ≡ 0; the mechanism lives in an unconstructed zero-mode extension whose sign, ½, and chirality assignment are all calibrated to the gate (only Q_tot-linearity is structural); (2) Step 4's exclusion of per-defect framing is contradicted by the refereed record: E3's own n originates as finite-ε, per-defect crossing prescriptions (phase105-Dspin line 45), which in the E3 pair family yield M = ∓Q₁Q₂ — the rival scheme has a finite-ε realization the submission's crossing-free family cannot see; (3) the "antichiral gives πE + Q²/2" derivation of ∓ is a zero-mode ownership convention, not a projection theorem. What remains is precisely the [GAP-2] dichotomy, now sharpened: **framing = global branch-section/zero-mode winding (⟹ M = (n∓1)Q₁Q₂) versus framing = per-defect crossing prescription (⟹ M = ∓Q₁Q₂); both are finite-ε-realizable, the gate is degenerate between them, and the registration's binary is not closed by this computation.** The registered D-MS identification should remain a convention pending repair (a) or (b) above.
