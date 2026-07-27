# Referee report — UNIT-1 unit-reconciliation round (phase 118)

**Date:** 2026-07-27
**Reviewed document:** phases/phase118-UNIT1-reconciliation.md (consultation section)
**Referee:** context-free adversarial agent (independent re-derivations + 200 randomized numeric trials; mandate: make K-UNIT-1 fire if any genuine inconsistency exists). Report preserved VERBATIM below; nothing edited.

---

# ADVERSARIAL REFEREE REPORT — Unit-Reconciliation Audit (K-UNIT-1)

## Verdict summary

I attacked the submission on every mandated front: re-derived BOX-1 from the commutators, re-derived all five formula conversions by hand and confirmed each with independent randomized numerics (200 trials, all pass), expanded the BIND-2 square hunting for a genuine D₁₂ conflict, stress-tested the SU(2)₁ stability logic for a masked disagreement, and audited the R-table arithmetic. **The "pure relabeling" verdict survives. K-UNIT-1 DOES NOT FIRE.** The submission's arithmetic is correct throughout. I found no genuine inconsistency between refereed numbers. Two refinements are required (ledger below): the GAP-1 hazard characterization "correct in neither system" needs sharpening — the formula is *form-identical* to entry 1 under the q≡Q reading, which is precisely why it circulated, but as an absolute rate it is off by 2π in every genuine frame because h, ℓ, and D are frame-invariant; and the report must state explicitly that entry 5 vs entry 1 is the *closest near-fire pair*, rescued only by the record's own stipulation that entry 5 was written under the q≡Q identification.

## Per-claim analysis

**BOX-1 re-derivation (independent).** With [j_m,j_n] = ±2πm δ_{m+n}, setting a_m = j_m/√(2π) gives [a_m,a_n] = ±m δ_{m+n}, the standard U(1) current algebra. Q = ∫η′-type zero mode is j₀; hence q = a₀ = Q/√(2π), h_q = q²/2 = Q²/4π. Linear pairings pick up one factor √(2π) per charge symbol (conversion-free only when written as pairings of the same-type object); quadratics pick up 2π, so record-frame quadratic rates carry the compensating 1/2π. BOX-1 confirmed as forced.

**Claim 1 — table conversions.** All verified by hand and numerically:
- **E1 invariance:** D = Q²ℓ/2π = (2πq²)ℓ/2π = q²ℓ = 2h_qℓ. Exact; the number is frame-invariant. PASS.
- **D₁₂:** Q₁Q₂î = √(2π)q₁·√(2π)q₂·î = 2πq₁q₂î. The î is an intersection datum (integer-valued topological count), not a charge; it carries no conversion. PASS.
- **D_spin:** ∓Q²/2 + nQ²/2 = (∓1+n)·πq² since Q²/2 = πq²; and with h = Q²/4π, 2πh = Q²/2 exactly, so D_spin = ∓2πh + 2πnh. PASS.
- **BIND-2 invariance:** (Q₁+îQ₂)² = (√(2π)q₁ + î√(2π)q₂)² = 2π(q₁+îq₂)² — exact, because î multiplies a charge *linearly inside* the square, so √(2π) factors out of the binomial before squaring. Hence D_γ₁ = (Q₁+îQ₂)²ℓ₁/2π = (q₁+îq₂)²ℓ₁, same number both frames. The submission's answer to "why does î not convert?" is correct and I verified it is not an approximation: the identity holds term-by-term in the binomial expansion. PASS.
- **SU(2)₁ arithmetic:** h = j(j+1)/(k+2) = (3/4)/3 = 1/4; q = ±1/√2 satisfies h = q²/2; Q = √(2π)/√2 = √π; abelian D = πℓ/2π = ℓ/2; re-tagged non-abelian D = 2·(1/4)·ℓ = ℓ/2. Both equal ℓ/2; both equal ℓ/4π in the q≡Q frame; rescale factor exactly 2π. PASS.

**Claim 2 — C-AB6 stability.** Attack attempted: could the q≡Q identification have masked a real disagreement? The masking scenario requires the two sides to rescale *differently* under the frame correction. The abelian side is q²ℓ/2π (purely quadratic in the charge datum); the non-abelian side is 2hℓ/2π with h = q²/2 (purely quadratic in the same datum). A common mislabeling multiplies both by the identical factor 2π; the *ratio* of the two computed values is frame-independent. Masking would require a term linear in charge (rescaling by √(2π)) or a charge-independent additive term on one side only; neither formula has one. The refereed content — the agreement — is unit-covariant. One caveat the submission understates: this argument leans on h being computed as q²/2 of the *same* charge datum. Here h = 1/4 was independently sourced from Sugawara (j(j+1)/(k+2)), and it happens to equal q²/2 exactly — so the agreement is a real two-route check, not a tautology, and it still rescales covariantly because both routes are quadratic. Stability CONFIRMED; the check is slightly stronger than the submission's "same datum through the same formula" phrasing suggests.

**Claim 3 — D_spin audit.** Verified above. PASS.

**Claim 4 — K-UNIT-1: the attack (mandate 2).** I expanded BIND-2: (Q₁+îQ₂)²ℓ₁/2π = Q₁²ℓ₁/2π + î²Q₂²ℓ₁/2π + **îQ₁Q₂ℓ₁/π**. If the cross term were the same quantity as entry 2's D₁₂ = Q₁Q₂î, K-UNIT-1 would fire spectacularly: equating them forces ℓ₁/π = 1 for all ℓ₁, absurd. They are **different quantities**, and the record's own typing says so precisely: entry 2 carries no length and is labeled by an intersection datum — it is the intensive/topological mutual statistic between two *distinct* curves, ℓ-independent, one contribution per intersection. The BIND-2 cross term is extensive in ℓ₁ — it is part of the *self*-rate of the composite charge (Q₁+îQ₂) propagating along γ₁, where î counts units of Q₂ dragged onto γ₁; it has the ℓ/2π structure of entry 1, i.e., it is a per-curve energetic rate, not a braiding pairing. A rate proportional to length and a topological phase per intersection cannot be forced equal by any unit conversion, and no refereed statement in the record equates them. Self-braiding cross-check stressed likewise: ½D₁₂(Q,Q;î=1) = Q²/2 and |D_spin|_{n=0} = Q²/2 — both ℓ-free topological quantities of the same type, both carrying the Q²/2 (no 1/2π) normalization; internally coherent, and coherent with the standard spin–statistics shape. The record thus splits cleanly into two type-families — ℓ-carrying rates with 1/2π per squared charge (entries 1, 4) and ℓ-free topological pairings with Q²/2 normalization (entries 2, 3) — each internally consistent and consistently related. **No refereed pair of numbers for the same quantity disagrees. K-UNIT-1 does not fire.**

The genuine near-fire is **entry 5 vs entry 1**: for an abelian-embeddable λ, D_λ = 2h_λℓ/2π and D = 2h_qℓ differ by exactly 2π as absolute numbers. Had entry 5 been written as a record-frame formula, this would be a firing inconsistency. It does not fire *only* because the record itself declares entry 5 "written under the IDENTIFICATION q ≡ Q" — the discrepancy is fully repaired by re-tagging its symbols and applying BOX-1, which is by K-UNIT-1's own wording a relabeling, not a genuine inconsistency. The submission reached the right verdict but did not flag this as the decisive boundary case; it should.

**Mandate 3 — GAP-1 adjudication.** Is "correct in neither system" right? The counter-reading: in the q≡Q frame, entry 1 instantiated with q reads D = q²ℓ/2π = 2hℓ/2π, so the circulated formula *is* entry 1 within that frame. But the q≡Q "frame" is not a valid unit system — it is a mislabeling. The physical rate D is frame-invariant (Q²ℓ/2π = q²ℓ, verified), h_λ is the conformal weight (invariant; h = 1/4 is convention-free), and ℓ is invariant. Therefore D = 2h_λℓ is an identity among invariants, and D_λ = 2h_λℓ/2π yields a number wrong by 2π *in every frame* — the mandate's proposed "correct in the R=1 frame" reading fails because it would require h to be a frame-dependent symbol, which a conformal weight is not. So the submission's "correct in neither" is **upheld**, with the refinement (C-UNIT-R1) that the formula is form-identical to entry 1 under the mis-instantiation Q→q — explaining both its origin and its harmlessness in intra-frame agreements (the common 2π cancels in ratios, exactly as K-NONAB-1 exhibited). The re-tag recommendation **D_λ = 2h_λℓ** stands and is the unique invariant-correct form; the distinction does not change the recommendation, only its justification.

**Mandate 4 — fork restatement audit.** Λ_Q = (√(2π)/R)ℤ, R_Q = R/√(2π). Verified: R = √(2π) → Λ_Q = ℤ (record, matches C-BRIDGE), R_Q = 1. R = 1 → Λ_q = ℤ (Sugawara unit lattice), R_Q = 1/√(2π) ≈ 0.3989. R = √2 → Λ_Q = √π·ℤ ≈ 1.7725·ℤ, and Q(j=½) = √π lies on it (it is the generator), R_Q = 1/√π. R = √3 → Λ_Q = √(2π/3)·ℤ ≈ 1.4472·ℤ, R_Q = √(3/2π). All submission lattice arithmetic exact. No resolution smuggled: the submission lists all four candidate frames with their implied R without electing one; GAP-N7 remains open. Note the fork options are mutually exclusive as Q-lattices (ℤ, √π·ℤ, √(2π/3)·ℤ pairwise incommensurable), so the fork is genuine and the unit audit correctly does not adjudicate it.

## Corrections ledger

- **C-UNIT-R1 (refinement, verdict-preserving):** GAP-1's "correct in neither system" should read: *form-identical to entry 1 under the mis-instantiation Q→q; wrong by 2π as an absolute rate in every genuine frame, since h_λ, ℓ, D are all frame-invariant.* Re-tag D_λ = 2h_λℓ unchanged.
- **C-UNIT-R2 (omission):** The submission must record entry 5 vs entry 1 as the decisive near-fire for K-UNIT-1, non-firing solely because entry 5's q≡Q provenance is part of the refereed record, making the repair a relabel. If any future circulation drops that provenance tag, the pair becomes a firing inconsistency.
- **C-UNIT-R3 (strengthening, no error):** C-AB6 stability argument should note h = 1/4 was independently Sugawara-sourced, so K-NONAB-1 is a genuine two-route agreement, covariant because both routes are purely quadratic in the charge datum.
- **C-UNIT-R4 (bookkeeping):** The record's two type-families (ℓ-carrying rates with 1/2π vs ℓ-free topological pairings with Q²/2) should be tagged explicitly in the ledger to pre-empt future cross-type "inconsistency" claims like the BIND-2 cross-term trap.

## VERDICT BOX

```
K-UNIT-1: DOES NOT FIRE — reconciliation is pure relabeling; all conversions exact.
Submission arithmetic: ALL VERIFIED (hand + 200 randomized numeric trials, all pass).
C-AB6 stability: CONFIRMED unit-covariant; agreement frame-independent (ratio test).
GAP-1 hazard: UPHELD with refinement C-UNIT-R1; re-tag D_λ = 2h_λℓ mandatory.
GAP-N7: restated, not resolved; R-table arithmetic exact; no smuggled resolution.
```

Word count: approximately 1560.
