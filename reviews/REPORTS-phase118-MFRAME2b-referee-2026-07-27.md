# Referee report — M-FRAME2(b) crossing-framing pair computation (phase 118)

**Date:** 2026-07-27
**Reviewed document:** phases/phase118-MFRAME2b-crossing-pair.md (consultation section)
**Referee:** context-free adversarial agent with explicit RESCUE mandate for the framing-deleted scheme (independent hand re-derivations; fully independent numerical integrator — own discretization, schedules, and constants; rescue routes including one the submission did not consider). Report preserved VERBATIM below; nothing edited (HTML entity escapes from transport decoded).

---

# ADVERSARIAL REFEREE REPORT — elimination of the "framing-deleted" (per-defect crossing) scheme

## Verdict summary

Elimination CONFIRMED: outcome O-B, on axiom S4, matching the precedent. I re-derived every load-bearing formula by hand, built a fully independent numerical integrator (own discretization of the symplectic form, own schedules, own profile normalization — no reuse of the submission's code, schedules, or constants), and confirmed all key families to discretization accuracy, with the exact rational differences machine-verified. I mounted the strongest rescue I could construct — including a split-anchor fusion route the submission never considers, which defeats the submission's arithmetic non-absorbability argument as literally stated (C-AC2) — and the rescue still fails, on naturality grounds. Two genuine errors found; neither is load-bearing. The kill in fact stands on two independent legs, one of which needs no fusion limit at all.

## Independent re-derivation of the crossing calculus (mandate 1)

**BOX-1 (master formula).** From σ(f,g)=∫fg′ and η_t′(θ)=Σᵢ(qᵢ/ε)ρ((θ−xᵢ)/ε): ∂_tη = −Σⱼ(qⱼẋⱼ/ε)ρ((θ−xⱼ)/ε), integration by parts (legitimate: Σqᵢ=0 makes η single-valued; constants null), and ∫ρ((θ−xᵢ)/ε)ρ((θ−xⱼ)/ε)dθ = εG((xᵢ−xⱼ)/ε) give σ(η,∂_tη) = (1/ε)Σᵢⱼqᵢqⱼẋⱼ G((xᵢ−xⱼ)/ε). Diagonal: (πc_ρ/ε)Σqⱼ²wⱼ. Off-diagonal, using G even: (qᵢqⱼ/2ε)∮(ẋᵢ+ẋⱼ)G dt. **Confirmed exactly.**

**BOX-2 (mover-direction rule).** The pair term carries ẋᵢ+ẋⱼ — the center-of-motion, not the relative velocity. A full sweep with a single mover of velocity sign s gives (qᵢqⱼ/2ε)·sε∫G = s·qᵢqⱼ/2 regardless of which ramp moves. **Confirmed**, and this genuinely is the engine: a spectator retreating cw past the mover (+Q²/2) and the mover advancing ccw through the spectator (−Q²/2) are topologically identical relative crossings with opposite phases. Checked against the refereed base case: mover +Q ccw (s=+1), anchor −Q, one crossing, −Q²/2, total Φ = πc_ρQ²/ε − Q²/2 ✓. Checked against the refereed pair: four crossings (−Q₁²/2, −Q₂²/2, two × −Q₁Q₂/2), co-moving m₁×m₂ term ∝ G(δ/ε)=0 at δ>2ε ⟹ M₀ = −Q₁Q₂ exactly, δ- and ε-independent ✓.

**BOX-3.** ∫₀^∞G = ½ from evenness plus ∫G=1 alone; quarter-rule shape-independent ✓. **BOX-4.** A full lap crosses every ramp of a static neutral cluster once with the same mover sign: (s·q_m/2)Σq_k = 0 ✓.

**My own parity theorem** (not in the submission; independently proves three of its claims). For a single defect with w_m=1, w_b=0: each full crossing contributes −(Q²/2)s, each half −(Q²/4)s, s = mover's sign; relative winding forces Σs(m-moved) − Σs(b-moved) = 1; halves occur only in coincidence entry/exit pairs with pair-sums ∈ {0, ±Q²/2}. Corollaries: (i) **D is quantized exactly in Q²/2 steps** for single-anchor families — the gate formula's quantization is a theorem, not an observation; (ii) full crossings alone reach exactly the even n; every odd n requires half-passages — precisely the gate table's structure; (iii) **a static spectator locks n=0** (Σs(m)=1 forced), confirming "the moving ramp alone, winding once, is locked to n=0"; (iv) all n ∈ ℤ are realized at w_m=1, w_b=0, divergence coefficient exactly 1 — explicit constructions at n = −2,−1,0,1,2 (submission's) and my own composite n=4 (three cw fulls: b-yield, m-backup, b-yield, then rigid completion), extending by iteration.

## Independent numerics (mandates 1–2)

Own implementation: θ-grid N=4096, ε=0.06, direct field-space Φ = ½Σₖσ(η_k,η_{k+1}) with an antisymmetrized discrete symplectic form (my first, naive discretization exhibited a linearly accumulating bias — a useful reminder that this quantity punishes sloppy integrators; the antisymmetrized form is clean and converges, error halving 800→1600 steps/rad). My c_ρ(bump) = 0.6751168 and A = πc_ρ/ε = 35.349034 reproduce the submission's constants independently.

Results (Φ vs exact prediction; residuals are common-mode discretization ~1.4e−2 per unit Q², cancelling in differences):

| family | Φ (mine) | exact | check |
|---|---|---|---|
| F1 rigid Q=1 | 34.835254 | A−0.5 | F2−F1 = **+1.0000031** |
| F2 yield (n=2) | 35.835257 | A+0.5 | F3−F1 = **+0.5000031** |
| F3 half (n=1) | 35.335257 | A | F3b−F1 = **−0.4999969** |
| F3b chase (n=−1) | 34.335257 | A−1 | F9−F1 = **+2.0000000** |
| F9 my composite (n=4) | 36.835254 | A+1.5 | ✓ |
| F8/F7 rigid/yield Q=3 | 313.517 / 322.517 | 9A∓4.5 | F7−F8 = **+9.0000279** |
| F1c/F3c cos² shape | 38.7535 / 39.2535 | A_c−0.5 / A_c | shape-independence ✓ |
| F4 pair base (1,2) | 172.176268 | 5A−4.5 | M = −2 ✓ |
| F5 per-defect (2,2) | 177.176268 | 5A+0.5 | F5−F4 = **+5.000000** (D-shifts only; M = −2) |
| F6 cluster (2,2) | 181.176268 | 5A+4.5 | F6−F5 = **+4.000000** = 2Q₁Q₂ (M = +2) |

At (0.7,1.3): F5b−F4b = **2.180000** = Q₁²+Q₂² (M unchanged at −0.91), F6b−F5b = **1.820000** = 2Q₁Q₂ (M = +0.91). S4 arithmetic: D_fused(n=2,Q=3) = +4.376, per-defect sum = +0.431, anomaly = **+3.945 ≈ 4 = nQ₁Q₂**; cluster sum = +4.431 = D_fused within common-mode error — additivity holds cluster-side, fails per-defect-side. All of the submission's numerical claims replicate under a fully independent implementation.

## Per-claim analysis

**Claim 1 (gate closed, all n).** CONFIRMED, and upgraded: my parity theorem makes "all n, divergence coefficient exactly 1, quantization Q²/2" a proof rather than an enumeration. One error: the structural formula n = 1 − w_m + w_b + 2N_b + halves is **false as stated** (C-AC1). Counterexample: w_m=1, spectator ccw lap (w_b=+1): a co-rotating schedule gives zero crossings ⟹ n=1, while a sequential schedule (b laps while m parks, then m laps) gives two ccw crossings ⟹ n=−1. Same winding data, different n: framing is crossing-event data, not winding data. This ironically *strengthens* the paper's thesis, and nothing downstream uses the formula. The winding rows (W) of the gate table are similarly schedule-specific.

**Claim 2 (per-defect totalization exists; M untouched; O-A false).** CONFIRMED at n=2 by my F5 (both defects framed via h<δ hops; M = −Q₁Q₂ exactly at two charge pairs); n=1 confirmed by the submission; general n follows by composing local moves, each excursion < δ, with BOX-4 protecting laps. O-A as pre-registered is falsified in its premise: general n requires no multiply-wound passages at all, so the anticipated coupling mechanism never engages. D-MS wins by a different route (O-B), which the pre-registration anticipated disjunctively.

**Claim 3 (S4 anomaly).** The identity D_fused(n) − [D₁+D₂+M] = nQ₁Q₂ re-derived by hand and verified numerically. The reassignment formula n_f = n(Q₁²+Q₂²)/(Q₁+Q₂)² verified algebraically (it equals 1 + [(n−1)(Q₁²+Q₂²)−2Q₁Q₂]/(Q₁+Q₂)²); non-integer for generic charges, and even at special charges no single map works identically ((1,1),n=1 ⟹ ½; (1,3),n=2 ⟹ 5/4). The derivation of (†) from Φ-continuity + divergence matching is sound: I verified the co-moving contact term 2πQ₁Q₂G(δ/ε)/ε → 2πc_ρQ₁Q₂/ε exactly completes πc_ρ(Q₁+Q₂)²/ε, and Φ-continuity is a property of the phase functional, not a scheme convention.

**A second, fusion-free kill the submission only gestures at (its §4 geometry paragraph), which I state sharply:** the per-defect scheme's complete data for my F5 and F6 families is *identical* — (n₁,n₂) = (2,2), each b_i yielding before m_i arrives — yet M = −Q₁Q₂ in one and +Q₁Q₂ in the other (measured difference 4.000000). The datum separating them is whether the yield excursion crossed the *other* defect's mover, i.e., h vs δ — information a per-defect prescription cannot possess. So under the per-defect scheme, M is not a function of the scheme's own labels: the "scheme-independent mutual phase" clause of S4 is violated with no fusion limit needed. The only escape — restricting offsets to h < δ — cannot be *stated* per-defect (it references other defects' positions), conceding that framing data is global. Both horns kill.

## GAP-1 adjudication (mandate 3)

The phase-105 prescription: offset passings = "resolving the shared-anchor moment by displaced smoothings," shifting the crossing contribution by integer multiples of Q²/2, same-axis dichotomy ±Q², only n ∈ {0,±1} exhibited. Ruling: **the P±/H± moves are a legitimate realization of this prescription, not a smuggled substitute.** A displaced smoothing at the shared-anchor moment, embedded in a *continuous closed* transport family (as it must be for Φ = ½∮ to be defined), is precisely a spectator excursion; the submission reproduces the record's checkpoints exactly — quantization in Q²/2 steps (now a theorem, my parity result), P⁺ vs rigid differing by exactly Q² (the same-axis dichotomy), and H± supplying the record's exhibited n = ±1. Decisively: **the elimination is insensitive to this identification.** The kill uses only the rival's refereed defining data — D = ∓Q²/2 + nQ²/2 quantized in Q²/2, M framing-independent — so even if P±/H± were a different totalization, it is the *most favorable* completion available to the refereed rival (it exists for all n and preserves M, more than the record established). Killing the best completion kills the scheme. GAP-1: benign; scope of elimination correct.

## THE RESCUE (mandate 4)

**(a) Deny (†) / decouple fused framing.** (a1) Integer reassignment n_f: dead — the fused single-anchor gate spectrum is −(Q₁+Q₂)²/2 + ((Q₁+Q₂)²/2)ℤ by my parity theorem; the required value (n−1)(Q₁²+Q₂²)/2 − Q₁Q₂ (e.g. −2 at (1,2), n=1, against steps of 9/2) is outside it, and no charge-independent integer map exists. (a2) Declare fused framing UNDEFINED ("framing lost under fusion"): inadmissible — S4 makes fusion part of the theory's structure; the δ→0 limit family concretely exists (Φ is continuous; the merged configuration *is* a single (Q₁+Q₂)-ramp), and its finite part sits outside every framed class the scheme recognizes. A scheme whose sector decomposition is not closed under fusion is the definition of non-naturality; refusing to assign the datum is the violation, not an exemption from it. (a3) "The anomaly is a re-parameterization": no — e^{inQ₁Q₂} ≠ 1 for generic charges, and the phase is observable relative to the refereed n=0 sector.

**(b) Restrict S4 to n=0 / declare fusion singular for framed defects.** Fails. The axioms enter a refereed uniqueness theorem unconditionally; the rival's defining formula D = ∓Q²/2 + nQ²/2 ranges over n, and the record exhibits n = ±1 — a scheme retreating to n=0 no longer defines framing and is no longer the rival. Partial fusion is exactly what S4 forbids, and S4 has killed for this before (uniform-background closure). Admitting "fusion works only in the unframed sector" is a *confession* of the anomaly, not a defense.

**(c) My strongest construction — the split-anchor fused gate (not considered by the submission).** Frame the fused charge-(Q₁+Q₂) defect against *split* spectators (−Q₁ at b₁, −Q₂ at b₂). The crossing quanta then include (Q₁+Q₂)Qᵢ/2 and /4, plus spectator–spectator crossings ±Q₁Q₂/2, ±Q₁Q₂/4 — generating a lattice (¼ℤ at (1,2)) that **does contain −2**. So the fused object *can* arithmetically realize D = D₁+D₂+M_framing-deleted, satisfying additivity, refuting the submission's "impossible (gate quantizes in Q²/2)" as literally stated (C-AC2). Why the rescue still fails, on three independent grounds: (i) the fused framing datum is now the anchor partition plus per-anchor offsets — the constituent decomposition. Under iterated fusion this becomes the full assembly history. A framing that is a function of assembly history is precisely *not* natural with respect to the fusion algebra, whose objects are charges: an elementary charge-3 defect and an assembled one would carry different framing spectra ((9/4)ℤ vs ¼ℤ), so "the framing of a charge-3 defect" is ill-defined. (ii) The refereed record fixes the crossing prescription's residual freedom at integer multiples of Q²/2 for a charge-Q defect; the split-anchor enlargement breaks that refereed quantization, so the rescued object is a *third* scheme, not the refereed rival — and its global constituent bookkeeping is functionally the branch-sector/zero-mode datum, i.e., D-MS reconstructed (the submission's BOX-7 point, reached from the opposite direction). (iii) The fusion-free kill (label degeneracy at δ>0, above) is untouched by any fused-object maneuver. **Rescue fails. I could not construct a fourth route: S1–S3 are genuinely satisfied by the per-defect scheme (verified), so no lesser axiom can be traded, and Φ-continuity is a theorem of the phase functional, not an assumption one may drop.**

## Odd-n obstruction and GAP-5 (mandate 5)

The (1,1)→(1,2) obstruction is geometrically sound as argued (a cluster-scale half-passage is anchored at coincidence with one mover; the retreat through a staggered train necessarily *fully* crosses the trailing mover), though I did not independently simulate the (1,1) attempt. It does not weaken the elimination: it limits only the δ>0 *constructive* exhibit of D-MS to even n. The kill of per-defect is unconditional across all n ≠ 0 — odd n included (n_f = 5/9 arises at n=1) — and D-MS at odd n rests on the separately refereed zero-mode theorem. O-B, as pre-registered, requires exactly the elimination, which is total.

## Theorem vs interpretation

THEOREM (re-derived and/or numerically confirmed here): BOX-1–BOX-4; gate realization of all n at unit winding with divergence coefficient exactly 1; Q²/2 quantization for single-anchor families; existence of the per-defect (n,n) totalization with M = ∓Q₁Q₂ (n=2 verified independently, n=1 by submission, general n by composition); cluster (2,2) family with M = ±Q₁Q₂ and exact additivity; contact-term completion of the fused counterterm; the anomaly identity nQ₁Q₂; label degeneracy of per-defect data. INTERPRETATION (adjudicated, all resolved in the submission's favor or repaired here): GAP-1 identification (ruled legitimate and immaterial); S4 operationalization (violation obtains under both the additivity reading and the scheme-independent-mutual-phase reading); non-absorbability against split-anchor enlargements (repaired via naturality + the refereed quantization wording, C-AC2).

## Corrections ledger

- **C-AC1.** §2 structural formula n = 1 − w_m + w_b + 2N_b + halves is not a function of winding data (co-rotating vs sequential spectator ccw lap: same windings, n = 1 vs n = −1); the spectator-lap W rows are schedule-specific and the w_b sign convention is internally inconsistent. Non-load-bearing; the correct statement is that n is crossing-event data.
- **C-AC2.** §4 "no integer reassignment absorbs it (gate quantizes in Q²/2)" is proved only for single-anchor fused families; split-anchor fused configurations realize D values (e.g. −2 at Q_tot=3) outside the (Q_tot²/4)-lattice, so the arithmetic argument alone has a hole. Closed in this report via fusion-algebra naturality (history-independence) and the refereed quantization wording. Verdict unchanged.
- **C-AC3.** §3's "for every n there exists a per-defect totalization" is verified at n ∈ {1,2} only; general n rests on composability of sub-δ moves (structurally sound via the parity decomposition, but not exhibited for arbitrary interleavings). Downgrade BOX-5 from "exact" to "verified n ≤ 2, structural for general n". Immaterial to the kill (the anomaly needs only one n ≠ 0).
- **C-AC4.** The submission's "convergence O(dt²)" is integrator-specific and unverifiable from outside; its reported values are nonetheless independently reproduced. Cosmetic.

## VERDICT BOX

> **VERDICT: KILL CONFIRMED — outcome O-B.** The framing-deleted (per-defect crossing) scheme violates S4 and is eliminated; the crossing calculus, gate closure (all n ∈ ℤ), pair computations, and anomaly nQ₁Q₂ all survive independent re-derivation and independent numerics; the rescue fails on all routes, including a split-anchor route the submission missed (C-AC2 repaired).
> Framing survives only as a global zero-mode/branch-sector datum: **D-MS selected** (even n constructively at δ>0; odd n via the refereed zero-mode theorem).
> Two errors found (C-AC1 structural formula; C-AC2 incomplete non-absorbability proof); neither load-bearing.
> The elimination stands on two independent legs: fusion anomaly nQ₁Q₂ and fusion-free label degeneracy of per-defect data.
> S4 kills again — same axiom, same precedent, third scheme eliminated.

Word count: ~2,530.
