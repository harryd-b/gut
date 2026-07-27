# Phase 118 (continuation): M-FRAME2(b) — the crossing-framing pair computation at n ≠ 0

**Date:** 2026-07-27
**Status:** DRAFTED — awaiting referee. No verdict enters the D-MS registration (phase109-DMS-upgrade.md) until the referee pass completes. The consultation below is preserved VERBATIM; nothing edited.
**Provenance:** Context-free derivation agent (M-FRAME2(b) mandate, registered in phases/phase109-DMS-upgrade.md A.5; dispatch recorded in phases/phase118-prize-rounds-registration.md §1).

**Editorial header (operator):**
- Headline claim (UNREFEREED): **outcome O-B — the per-defect crossing totalization violates S4 (fusion naturality) with exact computable anomaly nQ₁Q₂; framing-deleted ELIMINATED; D-MS wins by elimination and constructively.** If refereed, this closes the spin-scheme binary — the last dictionary convention — since within zero-mode framing D-MS is already a refereed theorem (phase 117 A.1) and the crossing prescription was the sole surviving rival definition (C-S3).
- Structure of the claimed decision, which the referee must attack at every joint: (i) the gate gap of phase 105 is claimed CLOSED — every n ∈ ℤ realized by crossing moves (full yields P±, half-passages H±, windings W) with the literal gate formula; (ii) outcome O-A as literally pre-registered is claimed FALSE — a per-defect totalization exists at every n keeping M = ∓Q₁Q₂ (via a "neutrality lemma": a full lap past a neutral defect contributes zero mutual phase); (iii) the decision therefore rests entirely on S4, where the per-defect scheme shows anomaly D_fused − (D₁+D₂+M) = nQ₁Q₂, claimed unremovable by integer reassignment (n_f would need to be n(Q₁²+Q₂²)/(Q₁+Q₂)² ∉ ℤ); (iv) the unique S4-consistent crossing scheme is claimed to be cluster-scale — i.e. a global datum, collapsing into the zero-mode/D-MS definition.
- Honest hinges the agent itself flags: GAP-1 (identification of its P±/H± moves with the record's refereed offset conventions is interpretive — the referee brief supplies the phase-105 wording to adjudicate this); GAP-4 (S4 operationalized as D-additivity under fusion, derived from Φ-continuity + divergence matching, not quoted from the refereed axiom — though the agent argues any weaker "scheme-independent mutual phase" reading is also violated since e^{inQ₁Q₂} ≠ 1); GAP-5 (cluster-scale realizations exhibited for even n only; odd-n rests on an obstruction computation plus the refereed zero-mode theorem).
- Consequences IF the verdict survives refereeing (none entered yet): D-MS upgrades from adopted convention to derived scheme; M-FRAME2 closes; BIND-2's K-BIND2-3 is decided in D-MS's favor; the BIND-2(c) winding-data registration (held) unblocks with the zero-mode framing carrying the honors.

---

## CONSULTATION (VERBATIM)

# M-FRAME2(b): the crossing-framing pair computation at n ≠ 0

## 0. Summary and verdicts

1. **Gate closed.** The crossing prescription realizes every framing integer n ∈ ℤ, including |n| ≥ 2, via three elementary passage moves (full spectator yields, half-passages, re-crossings) plus windings, and reproduces Φ = πc_ρQ²/ε + (n∓1)Q²/2 literally (divergence coefficient exactly 1) for all n. Verified numerically at n = 0, 1, 2.
2. **Pair, per-defect.** A per-defect totalization of the crossing prescription EXISTS for every n and leaves the mutual term untouched: M = ∓Q₁Q₂, exactly, for n = 0, 1, 2, verified for (Q₁,Q₂) = (1,2) and (0.7,1.3). So outcome O-A as literally worded is FALSE: multiply-wound/offset passages do not *necessarily* couple mutual crossings at fixed separation — a neutrality lemma [BOX-4] cancels the contamination.
3. **But the per-defect totalization violates S4.** Fusion naturality fails with a computable anomaly: D_fused(n) − [D₁(n) + D₂(n) + M_per-def] = nQ₁Q₂, exactly the D-MS cross term. No integer reassignment of the fused framing can absorb it (it would require n_f = n(Q₁²+Q₂²)/(Q₁+Q₂)² ∉ ℤ). The unique fusion-consistent totalization is cluster-scale (the yield move must clear the *whole* pair), gives M = (n∓1)Q₁Q₂, and is manifestly a global datum — i.e., it *is* the zero-mode/winding definition.

**VERDICT: O-B. The per-defect crossing-prescription totalization violates S4; framing-deleted is eliminated; D-MS wins by elimination, and constructively: the S4-consistent crossing scheme reproduces M = (n∓1)Q₁Q₂.**

Orientation convention throughout: transport counterclockwise (ccw), upper sign, so D_spin = (n−1)Q²/2 and M-claims read M = −Q₁Q₂ (framing-deleted) vs (n−1)Q₁Q₂ (D-MS).

## 1. Crossing calculus for multi-ramp families

Configuration: N_r rigid ramps, η_t′(θ) = Σᵢ (qᵢ/ε) ρ((θ − xᵢ(t))/ε), with Σᵢ qᵢ = 0 (single-valued η, vacuum representation; the zero mode is null so its branch choice is irrelevant). With G(u) := ∫ρ(s)ρ(s+u)ds — even for *any* ρ, G(0) = c_ρ, ∫G = (∫ρ)² = 1, supp G ⊂ [−2,2] for supp ρ ⊂ [−1,1] — integration by parts (legitimate: η single-valued) gives

σ(η_t, ∂_tη_t) = −∫η′ ∂_tη dθ = (1/ε) Σᵢⱼ qᵢqⱼ ẋⱼ G((xᵢ−xⱼ)/ε).

**[BOX-1] Master formula.** For a closed family (all xᵢ return to their start mod 2π),

Φ = ½∮σ dt = (πc_ρ/ε) Σⱼ qⱼ² wⱼ + Σ_{i<j} (qᵢqⱼ/2ε) ∮(ẋᵢ+ẋⱼ) G((xᵢ−xⱼ)/ε) dt,

wⱼ = winding number of trajectory xⱼ. Exact — no O(ε) remainder — whenever crossing sweeps are complete and endpoints/co-moving separations exceed 2ε (compact support) [GAP-6].

**[BOX-2] Mover-direction crossing rule.** At a crossing event where only one of the pair (i,j) moves, with mover velocity sign s, and the relative separation sweeps the full support of G, the pair term contributes s·qᵢqⱼ/2 — *independent of which of the two is the mover, dependent only on the mover's direction*. Derivation: if i moves, ∮ẋᵢG dt = ε·sign(ẋᵢ)∫G = ε s; identically if j moves. This asymmetry (a spectator retreating cw past the mover contributes the *opposite* sign to the mover advancing ccw through it, though the relative displacement is the same) is the engine of everything below. It is not paradoxical: Φ is a symplectic area in field space, not a function of relative topology alone.

**[BOX-3] Half-passage rule.** A sweep that starts or ends at *exact coincidence* (xᵢ = xⱼ) contributes s·qᵢqⱼ/4, because ∫₋∞⁰ G = ∫₀^∞ G = ½ exactly, by evenness of G — for every ramp shape (S2-compatible).

Sanity: base family (mover +Q winding once ccw, spectator −Q static): Φ = πc_ρQ²/ε + (+1)(−Q²)/2 = πc_ρQ²/ε − Q²/2 ✓ (refereed single-defect result recovered, crossing term −Q²/2 from the crossing event, all shapes).

## 2. Single-defect gate: all n realized

Elementary passage moves (mover m = +Q ccw base transport, spectator b = −Q; contributions from [BOX-2,3]; Δn defined via D = Φ − Φ_free = (n−1)Q²/2):

| Move | Sequence | Crossing total | Δn |
|---|---|---|---|
| P0 (rigid) | m sweeps past b | −Q²/2 | 0 |
| P⁺ (full yield) | b retreats cw past m before m arrives | +Q²/2 | +2 |
| P⁻ (re-cross) | m passes b; b advances ccw back over m; m passes again | −3Q²/2 | −2 |
| H⁺ (half yield) | m advances to exact coincidence (−Q²/4); b retreats cw (+Q²/4) | 0 | +1 |
| H⁻ (chase) | m passes b (−Q²/2); b advances ccw to coincidence (−Q²/4); m escapes ccw (−Q²/4) | −Q² | −1 |
| W (windings) | extra mover lap (Δn = −1 each) or spectator lap (cw: +1, ccw: −1) | | ±1 |

All of P±, H± keep w_m = 1, w_b = 0: the divergent part is exactly πc_ρQ²/ε (coefficient 1), and composing k of the P± moves with at most one H± realizes **every n ∈ ℤ with the gate formula holding literally**:

Φ = πc_ρQ²/ε + (n−1)Q²/2, n ∈ ℤ.

The record's known gap (|n| ≥ 2 never exhibited) is closed: n = 2 is a single P⁺; n = −2 a single P⁻; n = ±3 = P± + H±; iterate for all n. Winding realizations (multiply-wound mover, w_m = w: D = −wQ²/2, n = 1−w) also give all n ≤ 1 but with divergence w·πc_ρQ²/ε, absorbed by the S1-local counterterm (free transport of the same trajectories). Identification of these moves with the record's "offset passings / same-axis dichotomy ±Q²" is interpretive [GAP-1]: the refereed offset convention is not available to me, but P⁺ vs P0 differ by exactly +Q² at the crossing, matching the quoted dichotomy magnitude, and the quantization in units of Q²/2 (with H± supplying the odd steps) reproduces the refereed formula D = ∓Q²/2 + nQ²/2 completely.

Structural fact worth recording: writing a general family's self-crossing sum via [BOX-2], one finds n = 1 − w_m + w_b + 2N_b + (half-passage terms), where N_b counts spectator-yield crossings. **Framing shifts require either winding changes or spectator participation; the moving ramp alone, winding once, is topologically locked to n = 0.**

## 3. The pair computation

Refereed base reproduced: co-moving movers m₁ = t, m₂ = t − δ (charges Q₁, Q₂), static spectators b₁ = −Q₁, b₂ = −Q₂, disjoint (δ, separations > 2ε). Crossings: m₁×b₁ (−Q₁²/2), m₂×b₂ (−Q₂²/2), m₁×b₂ and m₂×b₁ (−Q₁Q₂/2 each); m₁×m₂ co-moving at fixed separation contribute 0 (G(δ/ε) = 0). Hence M₀ = −Q₁Q₂, δ- and ε-independent ✓.

**Per-defect totalization at n ≠ 0.** Apply the framing moves of §2 to defect 1 only, localized within a window smaller than δ:

- **n₁ = 2 (P⁺, hop size h = 6ε < δ):** as m₁ approaches b₁, b₁ retreats cw by h, landing in the gap between m₂ and m₁; the train passes; m₂ later crosses the displaced b₁ rigidly (−Q₁Q₂/2, unchanged); b₁ returns after the train is gone (no crossings). Self-1 crossing: +Q₁²/2 (n₁ = 2). Mutual crossings identical to base: **M = −Q₁Q₂.**
- **n₁ = 1 (H⁺):** m₁ stops at exact coincidence with b₁; b₁ retreats cw by 5ε < δ (clear of m₂); train resumes. Self-1: 0 (n₁ = 1). **M = −Q₁Q₂.**
- **Odd/negative n via laps:** if m₁ (or b₁) executes a full extra lap, it crosses *both* of defect 2's ramps once each, with the same mover sign s: contribution (s·q/2)(+Q₂ − Q₂) = 0.

**[BOX-4] Neutrality lemma.** A full lap of any ramp past a *neutral* cluster (a complete defect: ramp + spectator) contributes zero mutual phase. Hence winding-based framing moves also leave M untouched.

**[BOX-5]** For every n ∈ ℤ there exists a gate-consistent per-defect totalization with M = ∓Q₁Q₂ exactly. **Outcome O-A, as literally pre-registered ("necessarily couple"), is false.** The decision therefore rests on the axioms.

## 4. Fusion: the S4 anomaly

Fusion Q₁, Q₂ ↦ Q = Q₁+Q₂ is the δ → 0 merge of m₁,m₂ (and b₁,b₂). Additivity of D under fusion is forced by continuity of Φ plus divergence matching: as δ → 0 the co-moving pair term supplies the contact piece (2πG(δ/ε)/ε)Q₁Q₂ → 2πc_ρQ₁Q₂/ε, exactly completing (Q₁²+Q₂²)πc_ρ/ε to the fused counterterm (Q₁+Q₂)²πc_ρ/ε. So S4 demands, for a pair framed (n, n):

D_fused(n) = D₁(n) + D₂(n) + M(n). (†)

The fused defect realizes n by the *same* gate moves (§2 with charge Q): D_fused(n) = (n−1)(Q₁+Q₂)²/2.

- **Per-defect scheme:** D₁+D₂+M = (n−1)(Q₁²+Q₂²)/2 − Q₁Q₂. **[BOX-6] Anomaly: D_fused − (D₁+D₂+M) = nQ₁Q₂ ≠ 0 for n ≠ 0.** Rescuing (†) by assigning the fused object a different integer n_f requires n_f = n(Q₁²+Q₂²)/(Q₁+Q₂)², non-integer for generic charges ((1,2), n=1: 5/9) — impossible, since the gate quantizes framing in exact units of Q²/2. This is not a removable phase: for non-integer charges e^{iΔM} = e^{inQ₁Q₂} ≠ 1, so even the physical mutual phase differs. **S4 is violated. Outcome O-B.**
- **Where the geometry enforces it:** the per-defect P⁺ requires hop size h < δ; the fusion limit destroys this (no room), and when the yield move instead clears the *whole cluster* (h > δ + margins), b₁'s retreat necessarily crosses m₂ (+Q₁Q₂/2) and replaces the later m₂×b₁ crossing (was −Q₁Q₂/2): mutual shift +Q₁Q₂ per defect's yield. With both defects framed n = 2 cluster-style: M = +Q₁Q₂ = (n−1)Q₁Q₂, and (†) holds *identically*: (Q₁+Q₂)²/2 = Q₁²/2 + Q₂²/2 + Q₁Q₂. **[BOX-7]** The fusion-consistent crossing scheme is cluster-scale: its yield prescription references the entire configuration, not one defect — it is a global (zero-mode/branch-sector) datum, i.e., the D-MS definition. The "rival" definition, once forced through S4, collapses into D-MS.
- **Odd-n obstruction, sharper:** the cluster-scale half-passage cannot frame both constituents (n,n) at δ > 0: exact coincidence can hold for only one constituent at a time (the stagger δ turns the trailing constituent's half into a full yield — I computed the attempted (1,1) family and obtained (n₁,n₂) = (1,2), M = +Q₁Q₂/2, inconsistent with any (n,n) reading). Odd-n pair framing exists only in the genuinely fused/zero-mode formulation — consistent with the refereed theorem that a compactified zero-mode section pairs linearly with total monodromy [others'].

## 5. Axiom check

| Axiom | Per-defect totalization | Cluster-scale totalization |
|---|---|---|
| S1 locality of counterterms | ✓ (counterterms = per-ramp free transports; moves sized O(ε) < δ) | ✓ (counterterms unchanged; only the *prescription* is global) |
| S2 shape-independence | ✓ (∫G = 1; halves exact by G-evenness, any ρ) | ✓ (same) |
| S3 C-equivariance | ✓ (all weights quadratic in charges; moves charge-blind) | ✓ |
| S4 fusion naturality | **✗ — anomaly nQ₁Q₂ [BOX-6]** | ✓ for even n (verified n = 2); odd n only in the fused/zero-mode formulation |

## 6. Numerics

Method: θ-grid N = 4096, ε = 0.06; ρ = normalized mollifier exp(−1/(1−u²)) (c_ρ = 0.6751168; A := πc_ρ/ε = 35.349034); η from η′ by spectral (FFT) antiderivative; Φ as the discrete symplectic polygon area ½Σ_k σ(z_k, z_{k+1}), σ(f,g) = ∫fg′dθ, ~1500 steps/radian. Convergence (F1, Q=1): error −1.03e−2 / −2.24e−3 / −5.6e−4 at 700/1500/3000 steps/rad — O(dt²) to the exact prediction. Exact Q²-scaling of singles verified at Q=2 (diff 0.0e+00).

Singles (Q = 1; predictions Φ = A + (n−1)Q²/2):

| Family | n | Φ computed | Φ predicted | diff |
|---|---|---|---|---|
| F1 rigid | 0 | 34.846795 | 34.849034 | −2.2e−3 |
| F2 full yield | 2 | 35.846795 | 35.849034 | −2.2e−3 |
| F3 half-passage | 1 | 35.346795 | 35.349034 | −2.2e−3 |

The common −2.2e−3 is pure discretization: finite parts cancel it exactly — F2−F1 = 1.000000, F3−F1 = 0.500000 (machine-exact), confirming the crossing bookkeeping n = 2 and n = 1 against n = 0.

Pairs (Φ_pair diffs from predictions: −1.1e−2 at (1,2), −4.9e−3 at (0.7,1.3), same discretization origin; M := Φ_pair − Φ₁ − Φ₂ with matching single realizations — discretization cancels in M to 1e−6):

| Family | (1,2): M | (0.7,1.3): M | Prediction |
|---|---|---|---|
| F4: n=0 base | −2.000000 | −0.910000 | −Q₁Q₂ |
| F5: n₁=2 per-defect | −2.000000 | −0.910000 | −Q₁Q₂ |
| F5h: n₁=1 per-defect | −2.000000 | −0.910000 | −Q₁Q₂ |
| F6: n=2 cluster-scale | **+2.000000** | **+0.910000** | **+(n−1)Q₁Q₂** |

S4 arithmetic from computed values (residuals are the D-values' inherited discretization, ~Q²·2e−3): at (1,2), n=2: D_fused = 4.4799 (exact 4.5); per-defect D₁+D₂+M = 0.4888 (exact 0.5); anomaly 3.991 ≈ nQ₁Q₂ = 4; cluster D₁+D₂+M = 4.4888 = D_fused ✓. n=1: anomaly 1.980 ≈ 2. At (0.7,1.3): anomalies 1.816 ≈ 1.82 (n=2), 0.901 ≈ 0.91 (n=1); cluster total 1.9951 vs fused 1.9910 ✓. S2 numerically: rerun with ρ = cos²(πu/2) (c_ρ = 0.75): F2 diff −2.7e−3, F6 diff −1.3e−2 from the same finite-part predictions — finite parts shape-independent ✓.

## 7. VERDICT BOX

> **Verdict: O-B — framing-deleted eliminated; D-MS wins.**
> Per-defect crossing-framings realizing any n exist and keep M = ∓Q₁Q₂ (O-A's "necessarily" fails, via the neutrality lemma),
> but they violate S4 with exact anomaly nQ₁Q₂ = the D-MS cross term, unremovable by integer reassignment.
> The unique S4-consistent crossing scheme is cluster-scale, gives M = (n∓1)Q₁Q₂, and is a global (zero-mode) datum — the two framing definitions merge into D-MS.
> Gate gap closed: all n ∈ ℤ realized with Φ = πc_ρQ²/ε + (n∓1)Q²/2 literal; numerics confirm every entry at n = 0, 1, 2 for (1,2) and (0.7,1.3) to 1e−6 in finite parts.

## 8. Gaps-and-boxes ledger

**Boxes (load-bearing):** [BOX-1] master multi-ramp holonomy formula. [BOX-2] mover-direction crossing rule s·qq′/2. [BOX-3] half-passage rule s·qq′/4 (G evenness). [BOX-4] neutrality lemma (full lap past a neutral defect ⇒ zero mutual phase). [BOX-5] existence of per-defect totalization with M = ∓Q₁Q₂ for all n. [BOX-6] S4 anomaly = nQ₁Q₂, integer-obstructed. [BOX-7] cluster-scale scheme satisfies S4 and equals D-MS.

**Gaps:** [GAP-1] Identification of the record's "offset passings / ±Q² same-axis dichotomy" with my P±/H± moves is interpretive; the refereed convention itself was not available. [GAP-2] Φ_free for the multivalued single-ramp counterterm imported as given [others']; numerics verify raw Φ only, D-values use the analytic counterterm. [GAP-3] Crossing calculus proved for schedules with one ramp moving per crossing and compactly supported ρ; the overlapping/co-moving regime δ ≤ 2ε enters only through the contact-term limit argument, not an independent computation. [GAP-4] S4 operationalized as D-additivity under fusion (†), derived from Φ-continuity plus divergence matching; the refereed statement's precise wording was not available, though any weaker reading ("scheme-independent mutual phase") is also violated, since e^{inQ₁Q₂} ≠ 1 for generic charges. [GAP-5] Cluster-scale realizations exhibited for even n only; odd-n fusion consistency rests on the obstruction computation plus the refereed zero-mode theorem [others']. [GAP-6] Exactness (no O(ε) remainder) uses compact support of ρ; non-compact tails would add exponentially small corrections. Imported standard results [others']: Weyl algebra/vacuum structure, nullity of constants, the refereed single-defect holonomy and M₀ = ∓Q₁Q₂, the uniqueness-theorem dichotomy, and the zero-mode pairing theorem — all taken as given per the brief.

Word count: 2,456.

---

## Amendment section

### A.1 Referee verdict (2026-07-27): KILL CONFIRMED — O-B; framing-deleted ELIMINATED; D-MS SELECTED

Report preserved verbatim in reviews/REPORTS-phase118-MFRAME2b-referee-2026-07-27.md. Independent hand re-derivations of the entire crossing calculus; fully independent numerical integrator (own discretization, schedules, constants — including the referee's own n = 4 composite family and a Q = 3 gate check); the rescue mandate executed on three routes including a split-anchor construction the round never considered. Verdicts:

- **O-B CONFIRMED.** The per-defect crossing totalization violates S4, and the elimination now stands on TWO independent legs: (1) the fusion anomaly D_fused − (D₁+D₂+M) = nQ₁Q₂ (re-derived, numerically verified, unabsorbable — see C-AC2 for the repaired proof); (2) a fusion-free kill the referee sharpened from the round's own geometry paragraph: two families with IDENTICAL per-defect data ((n₁,n₂) = (2,2)) but different M (±Q₁Q₂, measured difference 4.000000) — under the per-defect scheme M is not a function of the scheme's own labels, violating S4's scheme-independent-mutual-phase clause with no fusion limit needed. Both horns kill.
- **The rescue FAILS on all routes.** (a) Integer reassignment: the required fused value lies outside the (Q_tot²/2)ℤ gate spectrum (referee's parity theorem); declaring fused framing undefined IS the naturality violation; the anomaly phase is observable (e^{inQ₁Q₂} ≠ 1). (b) Restricting S4 to n = 0 abandons the rival's own defining formula and repeats the refereed sin that killed the uniform-background closure. (c) The referee's own strongest construction — the split-anchor fused gate — DOES defeat the round's arithmetic non-absorbability argument as literally stated (C-AC2), but fails on naturality: its framing datum is the assembly history (an elementary and an assembled charge-3 defect would carry different framing spectra), it breaks the refereed Q²/2 quantization (a third scheme, not the rival), and its global constituent bookkeeping is D-MS reconstructed from the opposite direction. No fourth route exists: S1–S3 are genuinely satisfied, Φ-continuity is a theorem.
- **Gate closure UPGRADED to a theorem:** the referee's parity theorem proves Q²/2 quantization, evens-by-full-crossings/odds-need-halves, static-spectator-locks-n=0, and all-n-realizability — the phase-105 gap is closed by proof, not enumeration.
- **GAP-1 adjudicated benign:** the P±/H± moves are a legitimate realization of the record's offset prescription, and decisively, the elimination is insensitive to the identification — it kills the most favorable completion available to the refereed rival.

### A.2 Corrections ledger

- **C-AC1.** The structural formula n = 1 − w_m + w_b + 2N_b + halves is FALSE as stated (schedule-dependence counterexample: same winding data, n = 1 vs n = −1). Correct statement: n is crossing-event data, not winding data. Non-load-bearing; ironically strengthens the round's thesis.
- **C-AC2.** The round's "no integer reassignment absorbs it" was proved only for single-anchor fused families; split-anchor configurations escape the arithmetic. Repaired by the referee via fusion-algebra naturality (history-independence of framing) plus the refereed quantization wording. Verdict unchanged; the repaired proof is the one of record.
- **C-AC3.** BOX-5 downgraded: per-defect totalization "for every n" is verified at n ∈ {1, 2}, structural for general n (composability of sub-δ moves). Immaterial to the kill (one n ≠ 0 suffices).
- **C-AC4.** Convergence-order claim integrator-specific; values independently reproduced. Cosmetic.

### A.3 Post-verdict status

**THE SPIN-SCHEME BINARY IS CLOSED. D-MS is SELECTED — no longer an adopted convention but the derived scheme:** within zero-mode framing it is a refereed theorem (phase 117 A.1, κ = ½); the sole rival definition (per-defect crossing framing, C-S3) is now refereed-eliminated by S4 on two independent legs, with the constructive complement that the S4-consistent crossing scheme reproduces M = (n∓1)Q₁Q₂ and is a global datum — the two definitions merge. S4's kill count rises to three (uniform-background closure, phase 109; per-defect crossing framing, here; with the phase-111 ℓ-linear scheme killed by fusion naturality as well). Consequences entered: phase 109's D-MS registration upgraded (A.6 there); **K-BIND2-3 does NOT fire** — M-FRAME2 selected D-MS, so BIND-2(c)'s winding component survives its gate and its registration is UNBLOCKED (with GAP-6's ordering treatment as registered); M-FRAME2 exits the open registry. Odd-n pair framing at δ > 0 remains constructively unexhibited (C-AC3/GAP-5 residue) — carried as a scope note on D-MS, not a doubt about the selection.
