# Phase 118 (continuation): UNIT-1 round 1 — the unit-reconciliation round (record Q vs Sugawara q)

**Date:** 2026-07-27
**Status:** DRAFTED — awaiting referee. No verdict enters the phase-118 registration until the referee pass completes. The consultation below is preserved VERBATIM; nothing edited.
**Provenance:** Context-free derivation agent (UNIT-1 mandate, registered in phases/phase118-prize-rounds-registration.md §3; the round owed per C-AB6).

**Editorial header (operator):**
- Headline claims (UNREFEREED): reconciliation is PURE RELABELING — no refereed number changes; **K-UNIT-1 does not fire**. Primary system declared: record Q-units, with the conversion rule q → Q/√(2π) (quadratics carry exactly one 1/2π per squared charge; linear pairings conversion-free); all future formulas must carry a unit tag.
- **C-AB6 CONFIRMED STABLE:** the K-NONAB-1 SU(2)₁ agreement is unit-covariant — both comparison values are ℓ/4π under the q ≡ Q identification and ℓ/2 under the forced conversion (common rescale exactly 2π); the j = ½ defect's record charge is Q = √π, which lands exactly on the self-dual Q-lattice √π·ℤ as it must.
- **New hazard [the agent's GAP-1], the round's one substantive finding:** the circulated phase-113 formula D_λ = 2h_λℓ/2π is a q ≡ Q-frame hybrid equal to D/2π in BOTH systems — harmless inside phase-113's own intra-frame comparisons (the 1/2π cancels in agreements), but a latent 2π error in any future cross-frame use; it must be re-tagged D_λ = 2h_λℓ. Referee to verify; if confirmed, the re-tag will be entered as an amendment to phase 113's registration, not an edit of its verbatim text.
- GAP-N7 restated in R-coordinates and left open: C-BRIDGE pins R = √(2π) (record ℤ-lattice); the q ≡ Q identification pins R = 1; self-dual √2 (su(2)₁) and √3 (u(3)/ℤ₃) remain the other candidates. No choice made — the fork is a separate registration (the fine-structure locus).

---

## CONSULTATION (VERBATIM)

# UNIT-1 — Unit-Reconciliation Round: Record Charge Q vs Sugawara Charge q

## Summary

Under the forced conversion q = Q/√(2π) [BOX-1, refereed input], all five circulating formulas reconcile as pure relabeling. The rate invariant D takes the same numerical value in both systems (D = Q²ℓ/2π = q²ℓ), verified numerically. The C-AB6 stability claim is **CONFIRMED**: the K-NONAB-1 agreement in SU(2)₁ is unit-covariant — both comparison values move from ℓ/4π (under q ≡ Q) to ℓ/2 (under conversion), rescaling together by exactly 2π, so the refereed verdict (an agreement, not an absolute value) is stable. The D_spin audit resolves cleanly: D_spin = ∓2πh + 2πnh with h = Q²/4π, exactly the candidate factor. One hazard, not a contradiction: the phase-113 formula D_λ = 2h_λℓ/2π as written computes D/2π, not D, in either system — safe inside phase-113's own comparisons, unsafe in any future cross-system comparison [GAP-1]. K-UNIT-1 does **not** fire: no refereed number proves genuinely inconsistent. GAP-N7 is restated in R-coordinates and left open.

**Primary system declared: record Q-units.** The record's own conventions (σ, ω, ∫η′) and C-BRIDGE are stated there. **Conversion rule for all future formulas:** any expression imported from Sugawara/CFT conventions must substitute q → Q/√(2π); equivalently q² → Q²/2π and h_q → Q²/4π [BOX-1]. Linear zero-mode pairings (phases in charge) are conversion-free; quadratic ones (rates, energies, weights) carry exactly one factor of 1/2π per squared charge. Every future formula must carry an explicit unit tag (Q-system or q-system).

## 1. The Reconciliation Table

Throughout: q = Q/√(2π), Q = √(2π)q, Q² = 2πq², h_q = q²/2 = Q²/4π [BOX-1].

| # | Formula | Record Q-units (primary) | Sugawara q-units | Conversion factor |
|---|---|---|---|---|
| 1 | E1 rate | D = Q²ℓ/2π | D = q²ℓ = 2h_qℓ | Q² = 2πq²; the 2π cancels the explicit 1/2π. **Same number both systems** [BOX-2] |
| 2 | Mutual rate | D₁₂ = Q₁Q₂î | D₁₂ = 2πq₁q₂î | Bilinear in charge → carries one 2π; î dimensionless, unconverted |
| 3 | Spin | D_spin = ∓Q²/2 + nQ²/2 | D_spin = ∓πq² + nπq² = 2πh_q(n∓1) | Q²/2 = πq² = 2πh_q |
| 4 | BIND-2 pair | D_{γ₁} = (Q₁+îQ₂)²ℓ₁/2π | D_{γ₁} = (q₁+îq₂)²ℓ₁ | î multiplies charge linearly → survives conversion unchanged; overall square carries the 2π that cancels the 1/2π. Same number both systems |
| 5 | Phase-113 | *Correct Q-form:* D_λ = 2h_λℓ (via Q_λ² = 4πh_λ in entry 1) | *Correct q-form:* D_λ = 2h_λℓ (= q_λ²ℓ for abelian sectors) | **As circulated** (D_λ = 2h_λℓ/2π, written under q ≡ Q): equals D/2π in both systems — a hybrid, correct in neither [GAP-1] |

Note on entry 5: substituting h = q²/2 into entry 1's record form *while identifying Q = q* yields 2hℓ/2π — internally consistent with entry 1 only inside the q ≡ Q frame (the R = 1 reading of the ν-fork). Under BOX-1 the correct substitution is Q² = 4πh, giving D_λ = 2h_λℓ.

## 2. SU(2)₁ Re-derivation of C-AB6

Inputs [others': standard CFT]: SU(2)₁, j = ½ sector, h = 1/4, abelian embedding q = ±1/√2 (check: h = q²/2 = 1/4 ✓, verified numerically).

**As K-NONAB-1 was run (q ≡ Q identification):**
- Non-abelian side: D_λ = 2h_λℓ/2π = 2·(1/4)·ℓ/2π = **ℓ/4π** ≈ 0.0795775ℓ.
- Abelian defect side: D = Q²ℓ/2π with Q = q = 1/√2: D = (1/2)ℓ/2π = **ℓ/4π**.
- Agreement: ℓ/4π = ℓ/4π. PASS (as refereed).

**Under the forced conversion [BOX-1]:**
- Record charge of the j = ½ defect: Q = √(2π)·(1/√2) = √π ≈ 1.7724539 (matches √π to machine precision).
- Abelian defect side: D = Q²ℓ/2π = π·ℓ/2π = **ℓ/2**.
- Non-abelian side, correctly converted: D_λ = 2h_λℓ = 2·(1/4)·ℓ = **ℓ/2**.
- Agreement: ℓ/2 = ℓ/2. PASS.

Both sides rescale by the identical factor (ℓ/2)/(ℓ/4π) = 2π (confirmed numerically: 6.2831853… = 2π on both sides). The refereed content of K-NONAB-1 is the *agreement between two computed values* [BOX-3, per refereed input]; that agreement holds in both frames. **C-AB6 CONFIRMED: the K-NONAB-1 verdict is unit-covariant (STABLE), not an artifact of q ≡ Q.** The identification shifted both compared values coherently; it could not have manufactured a spurious agreement here, because both computations squared the same charge datum through the same (mis)labeled formula. The absolute values ℓ/4π quoted pre-conversion are frame-artifacts; the invariant value is ℓ/2.

## 3. GAP-N7 After Conversion — Restated, Not Resolved

Using the R-table (Λ_R = (1/R)ℤ in q, (1/R_Q)ℤ in Q, R_Q = R/√(2π)):

| Candidate | R (Sugawara) | q-lattice | Q-lattice | R_Q |
|---|---|---|---|---|
| Record integer lattice | **R = √(2π)** | (1/√(2π))ℤ | **ℤ** | 1 |
| Self-dual / su(2)₁ | **R = √2** | (1/√2)ℤ | √π·ℤ | 1/√π |
| u(3)/ℤ₃ decomposition | **R = √3** | (1/√3)ℤ | √(2π/3)·ℤ | √(3/2π) |

What each side pins: **C-BRIDGE** (Q = ±n·unit, unit = 1 in record units) pins the Q-lattice = ℤ, i.e. **R = √(2π)**. The **q ≡ Q identification** (phase-113's working frame) pins the q-lattice = ℤ, i.e. **R = 1** (Sugawara unit lattice). These are exactly the two prongs of BOX-1's ν-fork; the self-dual √2 and u(3) √3 points are the remaining GAP-N7 candidates. Observation (not a resolution): the j = ½ record charge Q = √π computed in §2 lies precisely on the self-dual Q-lattice √π·ℤ — consistent with su(2)₁ being the R = √2 point, as it must be. The three-way fork stands unresolved [GAP-N7, standing]; its resolution is a separate registration (where any fine-structure-constant question lives). No choice is made here.

## 4. K-UNIT-1 Audit (Pre-registered Kill)

Requirement: reconciliation must be pure relabeling; no refereed number may change.

**(a) D_spin vs spin-statistics.** Refereed: D_spin = ∓Q²/2 + nQ²/2 (record). Imported [others']: spin-statistics phase e^{2πih}, h = Q²/4π. Check the candidate resolution D_spin = 2πh up to sign: 2π·h = 2π·(Q²/4π) = Q²/2. **Exact.** So D_spin = ∓2πh + 2πnh; the phase e^{iD_spin}|_{n=0} = e^{∓2πih}, matching the spin-statistics reading with the ∓ carrying the chirality labeling and the framing term contributing e^{2πinh}. Verified numerically for Q ∈ {1, √π, 2} (Q²/2 = 2πh to machine precision). **Consistent — relabeling.**

**(b) D = 2h_qℓ vs entries 1 and 5 simultaneously.** Entry 1: D = Q²ℓ/2π = (4πh_q)ℓ/2π = 2h_qℓ. **Consistent identically** (numerically verified for Q ∈ {1, √π, 3.7}: Q²/2π = q² exactly). Entry 5 as circulated: 2h_λℓ/2π = (2h_λℓ)/2π = D/2π — off by 2π from the invariant. Is this a genuine contradiction? **No**: within the q ≡ Q frame in which entry 5 was written, entry 1 itself reads 2hℓ/2π, so the two entries agree inside that frame; and every refereed *use* of entry 5 (K-NONAB-1) compared two quantities carrying the same 1/2π, which cancels in the agreement. The discrepancy is exactly the ν-fork relabeling, already registered in BOX-1/GAP-N7. It becomes a genuine numerical error only if D_λ = 2h_λℓ/2π is ever set against an entry-1 rate computed with a true record charge — no such refereed comparison exists in the inputs. Flagged as [GAP-1]: entry 5 must be re-tagged D_λ = 2h_λℓ before any cross-frame use.

**(c) Entries 2, 3 cross-check.** Self-braiding consistency: ½·D₁₂(Q,Q; î=1) = Q²/2 = |D_spin|_{n=0} — the mutual and spin formulas share the record normalization coherently. Relabeling only.

**Kill verdict: K-UNIT-1 does NOT fire.** Every refereed number survives; the only defect found is a frame-tagging hazard (GAP-1), not an inconsistency.

## VERDICT BOX

1. **Reconciliation: PURE RELABELING** — all five formulas convert under q = Q/√(2π) with no refereed number changing; primary system = record Q-units.
2. **C-AB6: CONFIRMED STABLE** — K-NONAB-1's SU(2)₁ agreement is unit-covariant: both sides equal ℓ/4π under q ≡ Q and ℓ/2 under conversion (common factor exactly 2π); Q(j=½) = √π confirmed.
3. **D_spin audit: PASS** — D_spin = ∓2πh + 2πnh with h = Q²/4π; the candidate factor 2π·h = Q²/2 is exact.
4. **K-UNIT-1: DOES NOT FIRE** — no record-level contradiction; one hazard [GAP-1]: circulated D_λ = 2h_λℓ/2π computes D/2π and must be re-tagged as D_λ = 2h_λℓ before cross-frame use.
5. **GAP-N7: OPEN (untouched)** — three-way fork restated as R ∈ {√(2π), √2, √3}; C-BRIDGE pins R = √(2π), q ≡ Q pins R = 1; choice deferred to separate registration.

## Gaps-and-Boxes Ledger

- **[BOX-1]** (refereed input, load-bearing everywhere): forced conversion q = Q/√(2π); h_q = Q²/4π; quadratic-carries-1/2π rule.
- **[BOX-2]** (load-bearing for the audit): D is frame-invariant — Q²ℓ/2π and q²ℓ are the same number (verified numerically).
- **[BOX-3]** (load-bearing for C-AB6 verdict): the refereed content of K-NONAB-1 is the agreement between two computed values, not either absolute value (taken from the refereed brief).
- **[GAP-1]** (new): entry-5 formula D_λ = 2h_λℓ/2π is a q ≡ Q-frame hybrid equal to D/2π in both systems; harmless in intra-frame comparisons, a latent 2π error in any future cross-frame comparison; requires re-tagging to D_λ = 2h_λℓ.
- **[GAP-N7]** (standing, imported, not resolved): charge-lattice unit fork among R = √(2π) (record ℤ-lattice), R = √2 (self-dual, su(2)₁), R = √3 (u(3)/ℤ₃); the q ≡ Q reading corresponds to R = 1.
- **[others']**: Sugawara L₀ and h = q²/2; SU(2)₁ data (j = ½, h = 1/4, q = ±1/√2); spin-statistics e^{2πih}.

Numerical checks run in Python (floats, machine precision): h(q=1/√2) = 0.25; Q = √π = 1.7724539; old pair ℓ/4π = 0.0795775 both sides; new pair ℓ/2 = 0.5 both sides; rescale ratio 6.2831853 = 2π both sides; Q²/2 = 2π·(Q²/4π) for three Q values; Q²/2π = q² for three Q values. All exact to ~1e-15.

Word count: approximately 1480.

---

## Amendment section

*(Reserved. To be filled only after the adversarial referee pass. No verdict is entered in the phase-118 registration until then.)*
