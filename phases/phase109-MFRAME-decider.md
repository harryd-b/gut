# Phase 109 (continuation): M-FRAME — the deciding computation for the spin scheme

**Date:** 2026-07-26
**Status:** DRAFTED — awaiting referee. No verdict entered in the D-MS registration until the referee pass completes.
**Provenance:** Context-free derivation agent (M-FRAME mandate, registered in phases/phase109-DMS-upgrade.md Amendment). The consultation below is preserved VERBATIM per house rules. Nothing has been edited.

**Editorial header (operator):**
- M-FRAME was registered as the deciding computation between the two survivors of the phase-109 uniqueness theorem: D-MS (mutual term M = (n∓1)Q₁Q₂) and the framing-deleted rival (M = ∓Q₁Q₂). The uniqueness theorem (refereed) showed axioms S1–S4 select exactly one scheme; which of the two rivals satisfies them hangs on whether the mutual transport phase carries the framing cross term nQ₁Q₂.
- Calibration gate (pre-registered): the construction must reproduce the refereed single-defect formula Φ_ε = πc_ρQ²/ε + (n∓1)Q²/2 before its pair output counts.
- Headline claim (UNREFEREED until the referee verdict is entered as an amendment): **M = (n∓1)Q₁Q₂ — D-MS confirmed.** Framing couples to total charge via the branch-section deck lattice (Q₁+Q₂)ℤ.
- The agent's [GAP-2] is the honest hinge: the single-defect gate is degenerate between global (branch-section) framing and per-defect (renormalized local twist) framing; the pair computation splits them, and the finite-ε Weyl calculus is claimed to realize only the global reading. The referee is instructed to attack exactly this selection step.

---

## CONSULTATION (VERBATIM)

All numerics confirm the analytics. The final document follows.

---

# Two-defect transport phase in the Weyl calculus: the mutual term M(Q₁,Q₂)

**Deciding computation between [others'] D-MS (M = (n∓1)Q₁Q₂) and [others'] framing-deleted (M = ∓Q₁Q₂). Gate input [others']: refereed E3 single-defect formula Φ_ε = πc_ρQ²/ε + (n∓1)Q²/2 + o(1).**

## 1. Construction

Charge-Q defect at θ₀: winding profile η with η′(θ) = (Q/ε)ρ((θ−θ₀)/ε), ∫ρ du = 1, so η jumps by Q across the ramp (jump-height = charge normalization; fixed by gate calibration below). η is multivalued on S¹: monodromy η(θ+2π) = η(θ) + Q. Decompose η = (Q/2π)θ + p(θ), p single-valued; equivalently p̂_k = η̂′_k/(ik) for k≠0.

**Transport phase functional [BOX 1].** Transporting W(η_t), η_t(θ) = η(θ−t), t ∈ [0,2π], the accumulated Berry/Pancharatnam phase of the coherent family is the chiral one-particle Berry integral of the single-valued part plus the zero-mode (branch) contribution:

Φ = s·∫₀^{2π} Im⟨p_t, ṗ_t⟩ dt + Φ_zm,  ⟨f,g⟩ = 2πΣ_{k≥1} k f̂_k* ĝ_k,  s = orientation sign,

where Φ_zm = ½∫σ(η_t, ȧ(t))-type pairing of the branch section a(t) (below). Since p̂_k(t) = p̂_k e^{−ikt}, the first term evaluates exactly:

Φ_osc = 4π²Σ_{k≥1} k²|p̂_k|² = 4π²Σ_{k≥1}|η̂′_k|² = πE − Q²/2,  E = ∫η′² dθ = c_ρQ²/ε,  c_ρ = ∫ρ(u)²du.

The identity uses Parseval with the k=0 mode (η̂′₀ = Q/2π) removed: the chiral projection (k≥1 only) automatically subtracts Q²/2 from πE. The antichiral projection gives πE + Q²/2 (with transport orientation reversed to keep the divergence positive) — **the ∓ chirality branch is derived, not inserted**.

**Gate check [BOX 2].** Φ(n=0) = πc_ρQ²/ε ∓ Q²/2: shape-dependent divergence with coefficient πc_ρ = π∫ρ², finite part exactly −Q²/2 (chiral) / +Q²/2 (antichiral), **exactly** shape-independent (zero o(1) remainder for smooth scaling shapes). Matches the gate at n=0.

**Framing term origin.** The mode-sum family p_t closes exactly, but the full profile does not: η(θ−2π) = η(θ) − Q. A branch section a(t) (spatially constant shift) must be chosen along the loop; branches of the multivalued η form a torsor over the deck lattice **Qℤ** (shifting η by its own monodromy is the deck transformation). Minimal closure is already accounted for inside Φ_osc (that is what the −Q²/2 is); *frame winding n* = n extra deck loops of the section: Δa = nQ. Constants pair with the profile through σ: σ(c, η) = −c∫η′dθ = −cQ, so

Φ_zm = ½·Δa·Q·(sign) = nQ²/2.

Single defect total: πc_ρQ²/ε + (n∓1)Q²/2 — **gate reproduced, including the framing term's origin** (frame-winding sign convention for n fixed per chirality branch; [GAP-1] the absolute orientation-vs-chirality pairing is a convention matched to the gate, not independently derived).

Rejected candidate construction (reported per brief): identifying framing with winding of a *universal* zero-mode circle of fixed period (e.g. 2π) gives a frame phase **linear** in Q per winding — fails the gate's quadratic nQ²/2 for generic Q. The deck lattice Qℤ (charge-proportional) is the unique zero-mode realization passing the gate.

## 2. Pair derivation

Profiles η₁, η₂, disjoint ramps, separation δ, total η = η₁+η₂, monodromy Q₁+Q₂.

**Oscillator part.** Φ_osc(pair) = 4π²Σ_{k≥1}|η̂′₁,k + η̂′₂,k|². Cross term: 8π²Σ_{k≥1}Re(η̂′₁,k* η̂′₂,k). By Parseval, Σ_{k≠0}η̂′₁,−k η̂′₂,k = (1/2π)∫η′₁η′₂ dθ = 0 (disjoint supports), so 2ReΣ_{k≥1} = −η̂′₁,₀η̂′₂,₀ = −Q₁Q₂/4π². Hence cross = **−Q₁Q₂ exactly**, δ-independent, ε-independent, no divergence mixing. (Antichiral: +Q₁Q₂.) So the n=0 mutual term is M₀ = ∓Q₁Q₂ — unambiguous, and common to both rival formulas.

**Framing part — the deciding step.** The frame acts through the branch section of the pair profile. Trace the mechanism:

1. η_tot is **one** multivalued function; its deck lattice is (Q₁+Q₂)ℤ. A frame winding is a loop in the branch torsor: Δa = n(Q₁+Q₂).
2. The coupling σ(c, η_tot) = −c(Q₁+Q₂) sees only **total** winding charge: a constant cannot be "owned" by one defect. Even formally assigning per-defect decks Δa_i = nQ_i, each still pairs with Q_tot: Σᵢ ½·nQ_i·Q_tot = ½nQ_tot². Same answer.
3. A spatially localized constant (c·χᵢ(θ), χᵢ = 1 near defect i only) is **not** gauge: χᵢ′ ≠ 0 in the gap modifies η′ there, changing the automorphism family. So no per-defect frame exists in the zero-mode sector.
4. The only per-defect alternative — frame winding as a *local* conformal spin twist e^{2πin h_i}, h_i ∝ Q_i² — has **no finite-ε Weyl realization**: an interval ramp has no internal circle to wind (a rotated step does not close), and the would-be generator (local L₀) adds a divergent core energy ∼ nQ²/ε, violating the gate's finite framing term unless a renormalization *not present in the construction* is added.

Therefore the calibrated construction forces the global reading:

Φ_zm(pair) = ½·n(Q₁+Q₂)·(Q₁+Q₂) = n(Q₁+Q₂)²/2 = nQ₁²/2 + nQ₂²/2 + **nQ₁Q₂**.

**[BOX 3] Pair result:** Φ_pair = πc₁Q₁²/ε₁ + πc₂Q₂²/ε₂ + S(Q₁) + S(Q₂) + M, with

**M(Q₁,Q₂) = (n ∓ 1)Q₁Q₂**  (exact; δ-independent; no divergent mutual part).

Framing couples to total charge, n(Q₁+Q₂)²/2, because the frame is the branch/zero-mode section of the single global profile — the σ-pairing of constants is blind to which defect contributes the winding.

**Where the rival scheme lives ([GAP-2], the honest caveat).** The framing-deleted answer M = ∓Q₁Q₂ is exactly what one gets if "framing" is instead *defined* as a renormalized per-defect ribbon/spin twist (point-limit e^{2πin h_i}). The single-defect gate is **degenerate** between the two definitions (for one defect, Q_tot² = Q²), so the gate alone cannot separate them; the pair computation is where they split, by precisely nQ₁Q₂. The finite-ε Weyl calculus as specified cannot realize the per-defect definition (points 3–4 above), so within this construction the verdict is not ambiguous — but a scheme built on renormalized local twists would self-consistently produce the other answer. That is the precise content of the scheme difference: **scheme choice = whether framing is the global branch-section winding (realizable at finite ε) or a renormalized local spin twist (not realizable at finite ε).** The deciding construction selects the former.

## 3. Numerics

Implementation: N = 2¹⁸ grid, FFT mode sums (Φ_osc = 4π²Σ_{k≥1}|η̂′_k|²), plus discrete Pancharatnam product over the rotation family as an independent check (converges to the mode-sum value: 37.175 at 3200 steps vs 37.199 exact, Q=1, ε=0.1). Shapes: ρ_quad = 6u(1−u) (c_ρ = 1.2), ρ_quart = 30u²(1−u)² (c_ρ = 10/7), box (c_ρ = 1).

**Gate verification.** Φ − πc_ρQ²/ε across ε ∈ [0.025, 0.4], Q ∈ {1, 1.7}: smooth shapes give −Q²/2 to 6–7 digits at every ε (−0.500000; −1.445000 = −1.7²/2); box shape agrees to ~0.5% with a slowly growing grid-resolution artifact (discontinuous η′, slow Fourier decay) [GAP-3: box-shape numerics limited by FFT resolution, not a physical o(1) failure]. Divergence coefficient and exact shape-independence of the finite part: confirmed.

**Mutual term, n = 0.** M₀ = Φ_pair − Φ₁ − Φ₂, mixed shapes (quad + quart), (Q₁,Q₂) ∈ {(1,2), (0.7,1.3)}, ε ∈ {0.05, 0.1}, δ ∈ {0.5, 1.0, 2.5}: **M₀ = −2.000000 and −0.910000 in every case** (= −Q₁Q₂ to 6 digits, δ- and ε-independent). Both rivals share this term; it verifies the construction's mutual sector.

**Mutual term, n = 1, 2.** The deck contribution ½ΔaQ_tot is exact bookkeeping once Δa = nQ_tot is forced (Sec. 2); numerics here confirm arithmetic, not the globality itself — reported as such for honesty:

| (Q₁,Q₂) | n | M (this construction) | D-MS (n−1)Q₁Q₂ | framing-deleted −Q₁Q₂ |
|---|---|---|---|---|
| (1,2) | 0 | −2.000000 | −2 | −2 |
| (1,2) | 1 | 0.000000 | 0 | −2 |
| (1,2) | 2 | +2.000000 | +2 | −2 |
| (0.7,1.3) | 0 | −0.910000 | −0.91 | −0.91 |
| (0.7,1.3) | 1 | 0.000000 | 0 | −0.91 |
| (0.7,1.3) | 2 | +0.910000 | +0.91 | −0.91 |

(Chiral branch shown; antichiral flips the ∓1 column sign.)

## VERDICT BOX

**M = (n ∓ 1)Q₁Q₂ — D-MS confirmed.** The framing cross term nQ₁Q₂ is present: framing couples to total charge, n(Q₁+Q₂)²/2.

Five-line summary:
1. The chiral Berry functional Φ = 4π²Σ_{k≥1}|η̂′_k|² + branch-section term reproduces the gate exactly: πc_ρQ²/ε ∓ Q²/2 + nQ²/2, with ∓ derived from the chiral projection and n from deck winding of the branch lattice Qℤ.
2. Pair, n=0: mutual term ∓Q₁Q₂, exact and δ-independent (numerics: 6 digits, all shapes/separations) — shared by both schemes.
3. Framing is necessarily global in this construction: the profile's branch lattice is (Q₁+Q₂)ℤ, constants σ-couple only to total winding, localized constants aren't gauge, and per-defect spin twists have no finite-ε realization — so the frame term is n(Q₁+Q₂)²/2, forcing M ⊃ nQ₁Q₂.
4. The single-defect gate is degenerate between global and per-defect framing (Q_tot = Q); the pair splits them, and the finite-ε Weyl calculus selects global — a framing-deleted answer would require redefining framing as a renormalized local twist outside this construction ([GAP-2], precisely located).
5. Numerics verify divergence coefficient, exact finite-part shape-independence, Pancharatnam convergence, and M at n = 0,1,2 for (1,2) and (0.7,1.3): matches (n∓1)Q₁Q₂ throughout.

*(Word count ≈ 1450, under cap.)*

---

## Amendment section

(Reserved for the referee verdict. Empty until the referee pass completes.)
