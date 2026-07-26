# Phase 112 (continuation): BIND-2 round 1 — the two-arc line-frame computation (K-BIND2-1 attacked head-on)

**Date:** 2026-07-26
**Status:** DRAFTED — awaiting referee. No verdict entered in the BIND-2 registration (phases/phase112-BIND2-SPACE1-registration.md) until the referee pass completes.
**Provenance:** Context-free derivation agent executing the K-BIND2-1 mandate (the two-arc computation demanded by the phase-111 kill referee's C-V4). The consultation below is preserved VERBATIM per house rules. Nothing has been edited.

**Editorial header (operator):**
- Headline claim (UNREFEREED): **K-BIND2-1 does NOT fire — B2-b survives with coefficient (Q₁+îQ₂)²ℓ₁/2π in both crossing channels.** The referee-identified O(n) cross-pairing disease is confirmed real pre-truncation (and exhibited numerically: slope −0.318 in the global opposite-side pairing) but is annihilated identically, for every n, by E1's own I-local truncation χ_Ī₁ — because γ₁ preserves both arcs, complementary-side structures never enter the observation interval. The round argues this is provably the same mechanism that makes refereed E1 equal Q²ℓ/2π rather than 2Q²ℓ/2π, and that the truncation is FORCED (trivializer uniqueness extends verbatim to the pair profile), not chosen.
- Numerics: twelve configurations, growth exactly linear (increments constant to 5 decimals by n ≈ 20), coefficients matching (Q₁+îQ₂)²ℓ₁/2π to 4 decimals, including the exact zero at Q₂ = −îQ₁, the asymmetric cases, the î-flip, and explicit exhibits of both excluded diseases (the global D = 0 and the incoherent-sum 2×).
- One genuine bookkeeping discovery flagged: **[BOX-B] representative pinning** — the rate factors through the swept charge, which depends on where the carrier's OWN ramps sit relative to its own leg; calibration against refereed E1 forces the canonical placement (full charge inside the leg). The record nowhere states this convention explicitly; the referee is asked to ratify it as the E2-class → rate bookkeeping rule.
- §(d) contains a [SKETCH]-tagged preliminary on K-BIND2-2 (erasability): the difference profile has swept charge îQ₂ ≠ 0, which by the phase-108 C-N1 criterion is an infrared zero-mode obstruction — suggesting the shift is state-level. Full orbit analysis deferred to a K-BIND2-2 round.

---

## CONSULTATION (VERBATIM)

# Phase 112 — BIND-2 round 1: the two-arc line-frame computation of D_{γ₁}(pair) — K-BIND2-1 attacked head-on

**Summary with verdict.** K-BIND2-1 does **NOT** fire; **B2-b SURVIVES with coefficient (Q₁+îQ₂)²ℓ₁/2π** [derived + numerics, unrefereed]. The two-arc line-frame computation was carried out with E1's own truncation bookkeeping and no ad hoc regulator, and the referee's O(n) cross-pairing disease resolves cleanly: (1) the complementary-arc structures (the partner's second ramp AND carrier 1's own compensating ramp) are annihilated **identically, for every n**, by E1's I-local truncation χ_Ī₁ — because γ₁ preserves both arcs, complementary-side ramps never enter Ī₁; this is provably *the same mechanism* that makes refereed E1 equal Q²ℓ/2π rather than 2Q²ℓ/2π. (2) The truncation is not a choice: the trivializer-uniqueness argument of the refereed E1 derivation extends verbatim to the pair profile, so ζ^{(n)}_in is the *unique* coherent trivializer in H(I₁) — the functional is forced. (3) The surviving same-side cross term is log-coherent over the full range nℓ₁ and contributes exactly 2îQ₁Q₂, squaring the refereed swept charge. (4) Numerics: twelve configurations, all linear (not superlinear), all matching (Q₁+îQ₂)²ℓ₁/2π to 4 decimals; the pre-truncation O(n) opposite-side pairing is exhibited explicitly (it is real, and it cancels globally to a bounded quantity — never entering the I-local rate). One genuine bookkeeping discovery is flagged: the rate depends on the E2-class *representative* through the profile's values at the carrier's own fixed points; calibration against refereed E1 pins the representative uniquely [BOX-B]. All computations below are mine unless tagged [others'].

## §(a) E1's single-carrier mechanism, reconstructed (calibration gate)

From phases/phase104-JOIN4a-prime-derivation.md [others', refereed]: the functional is the **squared Ḣ^{1/2}-norm growth of the truncated telescoped trivializer**. Conventions: ‖f‖² = 2πΣ_{k≥1}k|f̂_k|² = G/4π with G the Möbius-invariant Gagliardo integral; ζ^{(n)} := η − η∘γⁿ; truncation g_in := g·χ_Ī, *defined only for g vanishing at the fixed points ξ±* (kinks only, so g_in ∈ H(I)); D := lim ‖ζ^{(n)}_in‖²/n = Q²ℓ/2π with Q = ∫_I η′.

Three load-bearing facts extracted from the record:

1. **The truncation is definitional, not a regulator.** The refereed Task-3 uniqueness argument: any coherent trivializer g ∈ H(I) of the n-step I-local cocycle satisfies σ(g − ζ^{(n)}, f) = 0 for all f ∈ C_c^∞(I), forcing g = ζ^{(n)} + const on I with supp g ⊂ Ī; nonzero constants create endpoint jumps ∉ H^{1/2}. So ζ^{(n)}_in is the *unique* trivializer — I-locality is built into the in-algebra formulation (the cocycle c′_t(γⁿ) lives on A(I)).

2. **The single-near-jump structure.** ζ^{(n)} on Ī has exactly one log-divergent structure: a smeared jump of height Q at scale e^{−nℓ} at the *repelling* endpoint (the referee of phase 104 confirmed "a two-edge model would have doubled it" [others']).

3. **The 2Q²→Q² mechanism, made explicit.** For the compensated single-valued profile (plateau class: down-ramp on the complementary arc), the compensating ramp's γ⁻ⁿ-pullback accumulates at the repelling point *from the outside* — a second same-scale near-jump of height Q on the wrong side. Globally the two near-jumps cancel in Ḣ^{1/2} (opposite circle-oriented heights at separation ~e^{−nℓ}): D_global = 0, exactly the dictionary's refereed line "globally compensated single-valued profiles have D = 0" [others', phase106 §1]. Adding the two sides *without* their cross-pairing gives 2Q²ℓ/2π. The I-local truncation keeps exactly one: Q²ℓ/2π.

**Lemma A (I-local rate; hypotheses exact).** Let η be bounded, smooth except finitely many C-D5 ramps, **none located at a₁ or b₁** (so η is continuous at the fixed points), with γ₁ hyperbolic, leg I₁ = (a₁,b₁), repelling a₁. Then (i) ζ^{(n)} vanishes at a₁,b₁ for all n, so ζ^{(n)}_in ∈ H(I₁) and is the unique coherent trivializer; (ii) ramps in I₁ pull back toward a₁ (log-linearly, speed ℓ₁), ramps in I₁′ pull back toward a₁ *within I₁′* and are annihilated by χ_Ī₁ identically for all n; (iii) D = (∫_{Ī₁}η′)²·ℓ₁/2π — the square of the **leg-swept charge** η(b₁⁻) − η(a₁⁺). Proof of (iii) is §(b); (i)–(ii) are immediate from γ₁ fixing a₁,b₁ and preserving both arcs.

**[BOX-B] The representative-pinning finding (genuine, previously unstated).** D is *not* a function of the E2 class alone: it factors through the swept charge η(b₁⁻)−η(a₁⁺), which depends on where the carrier's **own** anchor ramps sit relative to its own leg. Refereed E1's profile (η′ = c across I) puts all of Q inside: swept = Q ✓. A representative with C-D5 ramps *straddling* its own anchors symmetrically would have swept charge Q/2 − Q/2 = 0 and D = 0 — contradicting refereed E1. So calibration **forces** the canonical representative with the carrier's full charge inside its leg (up-ramp inside a₁, down-ramp outside b₁) — precisely the convention the refereed combinatorial core already used when it certified ∫_{I₁}(η₁+η₂)′ = Q₁+îQ₂ [others', phase111 A.3]. C-D5's midpoint convention governs *shared* anchors of two profiles (σ-regularization), not own-anchor placement; the record nowhere states the latter explicitly — flagged for the referee. The partner's ramps are at interior points of the arcs (anchor-interlacing, theorem-grade [others']), so no such ambiguity touches the partner terms.

## §(b) The two-arc line-frame computation

**Frame.** Conjugate γ₁ to x ↦ e^{ℓ₁}x on ℝ: a₁ = 0 (repelling), b₁ = ∞ (attracting), I₁ = (0,∞), I₁′ = (−∞,0). Log coordinates u = log x, v = log(−x); pullback η∘γ₁ⁿ is translation by nℓ₁ in u and in v. In these coordinates the Gagliardo kernel becomes translation-invariant: du du′/4sinh²((u−u′)/2) (same-side), du dv/4cosh²((u−v)/2) (opposite-side); the truncated function's cross-boundary term is exactly 2∫f(u)²du. (Line frame per the phase-104 erratum: the log-frame *spectral* heuristic is invalid; the Gagliardo line-frame computation is the refereed one [others'].)

**Profiles (î = +1; ccw order a₁,a₂,b₁,b₂).** η₁: up-edge at fixed position x ~ O(1) on the positive axis (charge Q₁ inside I₁ per [BOX-B]), down-edge on the negative axis. η₂: up-edge (+Q₂) at x_a > 0 (a₂ ∈ I₁, refereed), down-edge (−Q₂) at x_b < 0 (b₂ ∈ I₁′). For î = −1 the partner plateau covers a₁: η₂ ≡ Q₂ near 0 on both sides (continuous at a₁ — Lemma A hypotheses hold), in-leg ramp −Q₂ at x_B > 0 (b₂ ∈ I₁).

**Edge inventory under γ₁ⁿ (î = +1), with s := e^{−nℓ₁}.** ζ^{(n)} = η_pair − η_pair∘γ₁ⁿ is a superposition of "boxes": each ramp at fixed position p produces the box (charge)·χ_(ps, p) — fixed outer edge, translating inner edge at scale ~ps.

- Positive axis (kept by χ): −Q₁ box on (x_ε s, x_ε); −Q₂ box on (x_a s, x_a).
- Negative axis (complementary): −Q₁ box and −Q₂ box hugging 0⁻ at the same scale s.

**The dangerous terms, pre-truncation.** The opposite-side near-jump clusters at ±O(s) pair through the cosh-kernel with log(1/s) = nℓ₁ coefficients — the referee's O(n) cross-pairings, confirmed (and measured: §(c)). Their signed total: circle-oriented near-a₁ edge heights sum to zero (the pair profile is globally compensated), so the *global* norm is bounded — D_global = 0, the pair reproducing exactly the refereed compensated-profile statement. The O(n) terms are real individually and cancel only in the global sum; neither the disease nor its cancellation enters the I-local functional, because:

**Truncation, applied exactly as the record does.** ζ^{(n)}_pair vanishes at a₁,b₁ (fixed points; η_pair continuous there), so ζ^{(n)}_in := ζ^{(n)}χ_Ī₁ ∈ H(I₁) with kinks only — the truncation is exactly as benign as in refereed E1, and by Lemma A(i) it is the unique coherent trivializer: **no enumeration of readings is needed at the truncation step; the record forces iterate-then-truncate.** The complementary-side boxes are killed identically for all n (their supports never meet Ī₁).

**The surviving computation.** On the positive axis, with x_ε < x_a (both O(1)):

ζ^{(n)}_in = −Q₁ on (x_ε s, x_a s), −(Q₁+Q₂) on (x_a s, x_ε), −Q₂ on (x_ε, x_a), 0 elsewhere.

Four smoothed edges: j = −Q₁ at x_ε s, −Q₂ at x_a s, +Q₁ at x_ε, +Q₂ at x_a. Using the standard piecewise-edge asymptotic ‖f‖² ≈ (1/2π)[Σᵢjᵢ²log(1/wᵢ) + Σ_{i≠j}jᵢjⱼlog(1/|pᵢ−pⱼ|)] + O(1) (normalization checked against refereed E1): own-edge terms give (Q₁²+Q₂²)nℓ₁; the *same-side* inner-edge pair at separation ~s gives 2(−Q₁)(−Q₂)log(1/s) = **+2Q₁Q₂nℓ₁** — log-coherent over the full range because both structures translate together at speed ℓ₁ with O(1) offset; all other pairs are O(1). Equivalently and more transparently: in log coordinates the sinh-kernel is exponentially local, so the entire growth sits in the cross-boundary term (1/2π)∫f²du — and on the overlap of the two log-plateaus (length nℓ₁ − O(1)) the *heights add*: ∫f²du = (Q₁+Q₂)²nℓ₁ + O(1). This matches refereed E1's confirmation A structure exactly ("cross-region pairs carry the growth; all other regions O(1)" [others']).

**Result:** D_{γ₁}(pair) = (Q₁+Q₂)²ℓ₁/2π. For î = −1 the in-leg partner structure has charge −Q₂ (down-ramp at b₂), flipping the cross term: (Q₁−Q₂)². **Both channels: D = (Q₁+îQ₂)²ℓ₁/2π** — the square of the refereed swept charge. When Q₂ = −îQ₁ the norm is *bounded* (rate exists and equals 0), not ill-defined.

**Readings enumeration (calibration gate does the work).** R1 iterate-then-truncate: forced by trivializer uniqueness → (Q₁+îQ₂)². R2 global (no truncation): D = 0 for every compensated profile including the single carrier — contradicts refereed E1; excluded. R3 two-sided incoherent sum: 2(Q₁+îQ₂)² — the "2Q²" reading the record already excludes for the single carrier. R4 own-anchor-straddling representative: changes the single-carrier baseline (midpoint: D = 0 ≠ refereed) — excluded [BOX-B]. Exactly one reading survives calibration, and it is the one the record forces.

## §(c) Numerics (raw numbers)

Implementation: line frame, log-coordinate grids u ∈ [−(40ℓ₁+25), 25], du = 0.025; translation-invariant Möbius kernels 1/4sinh²(Δ/2) (same-side), 1/4cosh²(Δ/2) (opposite-side); truncated cross-boundary term 2∫f²du exact; ‖·‖² = G/4π; tanh edges (log-width 0.5); slopes fit on n ∈ [15,35]; ℓ₁ = 0.5 unless stated (ℓ₁/2π = 0.07958). Scripts run and deleted.

| configuration | measured slope | (Q₁+îQ₂)²ℓ₁/2π | Q₁²ℓ₁/2π | (Q₁²+Q₂²)ℓ₁/2π |
|---|---|---|---|---|
| single Q=1 (calibration) | **0.07958** | 0.07958 | — | — |
| single Q=1.5, ℓ=0.8 | **0.28648** | 0.28648 | — | — |
| single, compensated class, truncated | **0.07958** | 0.07958 | — | — |
| single, compensated, GLOBAL | 0.00007 | (D_global = 0 ✓) | | |
| î=+1 (1,1) | **0.31835** | 0.31831 | 0.07958 | 0.15915 |
| î=+1 (1,−1) | **−0.00002** | 0 | 0.07958 | 0.15915 |
| î=+1 (2,−1) | **0.07955** | 0.07958 | 0.31831 | 0.39789 |
| î=+1 (1,1) GLOBAL | 0.00018 | (bounded; opposite-side pairing slope −0.31821 — the O(n) disease, individually real, cancelling) | | |
| î=−1 (1,1) | **−0.00002** | 0 | 0.07958 | 0.15915 |
| î=−1 (1,−1) | **0.31835** | 0.31831 | 0.07958 | 0.15915 |
| î=−1 (2,−1) | **0.71628** | 0.71620 | 0.31831 | 0.47746 |
| î=+1 (1,1), ramp moved/narrowed (C-D5 reshape) | **0.31863** | 0.31831 | | |
| two sides summed without cross-pairing | 0.63669 | (= 2×0.31831: the "2Q²" disease, exhibited) | | |

Raw series (‖ζ^{(n)}_in‖² at n = 5,10,…,40): single (1): 0.7126, 1.1434, 1.5437, 1.9418, 2.3397, 2.7376, 3.1355, 3.5334 — per-step increments 0.08614, 0.08007, 0.07962, 0.07958, 0.07958, 0.07958, 0.07958. Pair (1,1) î=+1: 1.7579, 3.6160, 5.2243, 6.8172, 8.4088, 10.0004, 11.5919, 13.1835 — increments 0.37162, 0.32165, 0.31858, 0.31833, 0.31831, 0.31831, 0.31831. **Growth is exactly linear** (increments constant to 5 decimals by n ≈ 20); no superlinearity anywhere; the like-charge/unlike-charge and î-flip sign structure of B2-b is reproduced in full, including the asymmetric case and the exact zero at Q₂ = −îQ₁.

## §(d) State-level status [SKETCH — K-BIND2-2 preliminary only]

On A(I₁), the pair state ω∘Ad W(η₁+η₂) and the unshifted reference ω∘Ad W(η₁) differ exactly by Ad W(η₂), and η₂'s I₁-relevant datum is a step of swept charge îQ₂ across I₁ with only one ramp inside: its I₁-truncation carries an endpoint jump of height îQ₂ (η₂(b₁) − η₂(a₁) = îQ₂ ≠ 0), the log-divergent class of phase 104 §1(b). The phase-108 machinery applies to this **difference profile** directly: the infrared criterion ĥ ∉ L² is equivalent to nonzero swept charge (Q_diff = îQ₂ ≠ 0 ⇔ sup_t‖k_t^{diff}‖ = ∞, per C-N1's repaired form [others']), which is the named obstruction functional: **the swept-charge difference îQ₂ as an infrared zero-mode**. So the candidate answer to K-BIND2-2 is that the shift is *not* in the local-unitary erasure orbit whenever îQ₂ ≠ 0 — but this sketch establishes only the coherent-operation obstruction plus the criterion's applicability; the full JOIN-4a″ orbit analysis (general inner operations, and the correct choice of reference state on the joint algebra rather than A(I₁) alone) is the open work of a K-BIND2-2 round. [SKETCH]

## Gaps-and-boxes ledger

- **[BOX-A]** Model profiles are tanh edges in log coordinate, not the record's exact Möbius model; C-D5 reshaping is O(1) at fixed n (checked numerically: reshape run moves the slope by 0.001, within fit error). O(1) uniformity in n is estimated, not proved — the same status as E1's own GAP-5, inherited not worsened.
- **[BOX-B]** Representative pinning (§a): D factors through the swept charge η(b₁⁻)−η(a₁⁺); the canonical placement (carrier's full charge inside its own leg) is forced by calibration against refereed E1 and matches the refereed swept-charge count, but the record nowhere states own-anchor ramp placement explicitly. Referee should ratify this as the E2-class → rate bookkeeping convention.
- **[BOX-C]** Partner anchors are interior points of the two arcs — theorem-grade via anchor-interlacing [others']; the degenerate coincidence (partner anchor at a₁ or b₁) is excluded by anchor distinctness of a genuine crossing.
- **[BOX-D]** The piecewise-edge log-pairing asymptotic is verified against refereed E1 and numerically, with leading term forced by the overlap identity ∫f²du; uniform constants not proved.
- **[GAP-1]** Physical (energy/entropy) reading of the pair rate inherits E1's GAP-6: asserted-plausible, not derived.
- **[others']** Imports: full E1 machinery and conventions (phase104-JOIN4a-prime, refereed); anchor-interlacing lemma + swept-charge core Q₁+îQ₂ (theorem-grade/refereed, phase 111); dictionary I-locality line (phase 106); C-D5 (phase 105); ĥ ∉ L² criterion (phase 108).
- No new postulates; no regulator beyond the record's own χ_Ī₁, which is forced by trivializer uniqueness. Temporary scripts deleted.

**VERDICT BOX. K-BIND2-1: DOES NOT FIRE.** The two-arc line-frame computation, executed with E1's own I-local truncation, yields a well-defined linear rate with coefficient **(Q₁+îQ₂)²ℓ₁/2π** in both crossing channels — partner-sensitive, not partner-blind, not divergent. The referee's O(n) cross-pairing obstruction is real pre-truncation and is removed by the identical mechanism that fixes refereed E1's coefficient (complementary-side annihilation under χ_Ī₁, here exact for all n by γ₁-invariance of the arcs). B2-b's analytic coefficient is hereby earned pending adversarial referee; conditional on ratification of [BOX-B], the rate-shift binding claim stands with its registered sign structure (like charges: excess ×(1+Q₂/Q₁)²; opposite: defect to exactly zero at Q₂ = −îQ₁).

---

## Amendment section

### A.1 Referee verdict (2026-07-26): K-BIND2-1 CONFIRMED-DOES-NOT-FIRE; [BOX-B] RATIFIED

Adversarial referee report preserved verbatim in reviews/REPORTS-phase112-BIND2-referee-2026-07-26.md. Every E1 attribution audited line-by-line against phase104-JOIN4a-prime-derivation.md and found correct (functional, normalization, truncation definition with the kink precondition, Task-3 uniqueness, iterate-then-truncate as the forced order, the line-frame erratum, the compensated-profile D = 0 line, C-D5 midpoint scope). The C-V4 demand ruled MET, not dodged. The referee's main assault — a truncation-boundary divergence where the inner edges accumulate at the cut point — was repelled analytically (exact cross-boundary identity 2∫f²du; independent re-derivation of the overlap identity) and numerically (the same-side sinh kernel carries zero growth: fitted slope 0.000000). Independent numerics at different modulus (ℓ₁ = 0.7), grid, edge model, and fit window reproduce every coefficient to 5 decimals with increments constant to 6 decimals; the superlinear-drift hunt was negative.

**Refereed and entered:** Lemma A (stated hypotheses); the forced iterate-then-truncate reading; **D_{γ₁}(pair) = (Q₁+îQ₂)²ℓ₁/2π in both channels**, including the exact zero at Q₂ = −îQ₁ (bounded norm, rate 0 — not ill-defined); the pre-truncation O(n) disease as real-but-globally-cancelling and never entering the I-local functional; the [BOX-B] canonical-representative convention — RATIFIED, with the referee's strengthening that it is DERIVABLE from the record's refereed charge reading Q = ∫_I η′ (phase 104 §0), so the ambiguity does not infect E1.

**Not refereed (stay as tagged):** §(d)'s K-BIND2-2 sketch; [BOX-A]/[BOX-D] uniformity (inherit E1's GAP-5, unchanged); [GAP-1] physical reading.

### A.2 Corrections ledger

- **C-W1.** The Task-3 quote is σ(g − ζ^{(n)}_in, f) per phase 104 §3 (equivalent for supp f ⊂ I by the record's ζ_out-pairs-trivially check; quotes must be exact).
- **C-W2.** The §(d) criterion citation conflated two statements: C-N1 proper gives sup_t‖k_t‖ = ∞ ⟹ ĥ ∉ L² NEAR 0 (one implication); the full Q = 0 ⟺ orbit-membership equivalence is phase 108's mechanism line. Split accordingly; "near 0" restored.
- **C-W3.** The global-run opposite-side pairing slope −0.31821 is single-quadrant normalized; the full opposite-side contribution is 2× (referee measurement: −0.891268 = −2(Q₁+Q₂)²ℓ₁/2π at ℓ₁ = 0.7). Quadrant convention now stated.
- **C-W4.** The [BOX-B] ratification records the derivability note (refereed charge reading + calibration, not calibration alone).

### A.3 Post-verdict status

**B2-b's analytic coefficient is REFEREED. The dictionary's first length-carrying cross-axis coupling stands:** a carrier's I-local rate in the presence of a crossing partner is (Q₁+îQ₂)²ℓ₁/2π — partner-sensitive, sign-structured (like charges excess, opposite charges defect to exactly zero at Q₂ = −îQ₁), linear, and produced by the record's own forced machinery. Next registered work: K-BIND2-2 (full erasability/orbit round, building on the [SKETCH]); the queued BIND2-GAP-1 stiffness round; K-BIND2-3 rides on M-FRAME2.
