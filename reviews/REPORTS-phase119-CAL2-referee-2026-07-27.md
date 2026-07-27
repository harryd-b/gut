# Referee report — CAL-2 moduli/extremality round (phase 119)

**Date:** 2026-07-27
**Reviewed document:** phases/phase119-CAL2-moduli-round1.md (consultation section)
**Referee:** context-free adversarial agent (independent from-scratch exact-arithmetic re-implementation of the Bolza group and spectrum to depth 7 plus the full depth-8 shell on positive-trace levels; homology-invariant audit certifying no over-merge; literature-anchor audit; kill-ruling and honesty-finding audit). Report preserved VERBATIM below; nothing edited.

**Editorial note (operator):** the referee's pre-report reconciliation note (transmitted with the report) is retained at top — it documents a replication trap (signed-trace collection) that the referee fell into, caught via its own homology audit, and converted into correction C-AF6.

---

Complete reconciliation. With both trace signs included, my independent depth-7 enumeration gives exactly the submission's multiplicities — 12, 12, 24 unoriented at the three lowest levels — and at 10+8√2 all 552 elements are literal squares of systolic elements (zero primitives), in 12 unoriented classes. My earlier discrepancy was my own single-sign collection bug, caught by the homology audit; it also revealed that the submission's table silently reports |trace|, worth a replication warning. All mandated computations are now done: sanity checks passed (relation exact, homology-certified no over-merge, all ratios reproduced). Delivering the final report.

# ADVERSARIAL REFEREE REPORT

## Verdict summary

I re-implemented the Bolza group from scratch in exact arithmetic (my own code; ring ℤ[ζ₈] ⊕ ℤ[ζ₈]·s with z⁴ = −1, s² = 2+2√2) and re-derived the low-lying primitive spectrum by reduced-word enumeration to word length 7, plus the full length-8 shell (6,588,344 words) on positive-trace levels, with union-find conjugacy merging over ~3,200 conjugators and an independent homology-invariant audit certifying no over-merge. Every computational anchor I was mandated to check is CONFIRMED. The interpretive layer draws corrections: reading (A)'s kill is empirically assisted, not internal; the honesty finding misses real falsifiable content; reading-(C) survival is a loophole; plus labeling defects. K-CAL2-1 DOES NOT FIRE (narrowly). K-CAL2-2 RESPECTED.

## Per-claim analysis

### 1. Independent recomputation

**Group verification (exact).** Generators in the stated Aurich–Steiner form: det = 1, SU(1,1) form, and the octagon relation b₀b₁⁻¹b₂b₃⁻¹b₀⁻¹b₁b₂⁻¹b₃ = +I hold exactly in my ring. Across all 1,098,057 reduced words of length ≤ 7: zero elliptic/parabolic elements, all traces in ℤ[√2] with p ≡ 2 mod 4 and q even (both signs). Bookkeeping cross-check: the submission's "6,588,344 words" equals exactly 8·7⁷, the reduced words of length exactly 8; cumulative to length 8 is 7,686,401 (C-AF7).

**Trace-to-length conversion.** cosh(ℓ/2) = |tr|/2 is correct (the "/4" variant floated in my brief is wrong and inconsistent with every row). All eleven rows reproduce to all printed decimals: 3.05714, 4.89690, 5.82807, [6.11428 = 2ℓ₁ exactly, since tr(γ²) = tr²−2 gives (2+2√2)²−2 = 10+8√2], 6.67201, 7.10738, 7.26316, 7.59569, 7.88069, 8.13008, 8.22490. Ratios confirmed: 1.60179, 1.90638, and all others match (2.18243, 2.32484, 2.37580, 2.48457, 2.57780, 2.65937, 2.69039).

**Multiplicities (exact at my depth).** A replication trap I fell into and escaped: in the +I lift, conjugacy preserves the *signed* trace, and systolic classes occur at both ±(2+2√2). Collecting only positive traces gives 16 oriented / 8 unoriented classes — homology-certified exact (16 components, 16 distinct H₁ = ℤ⁴ vectors, zero mixed components) — and the missing classes sit at trace −(2+2√2): 8 oriented / 4 unoriented. Totals at depth 7:
- ℓ₁ = 3.05714: 24 oriented / **12 unoriented** — matches submission and kissing number 12.
- ℓ₂ = 4.89690 (±(6+4√2)): 24 / **12** — matches.
- ℓ₃ = 5.82807 (±(10+6√2)): 48 / **24** — matches.
- ℓ = 6.11428 (10+8√2; the level (−10,−8) is empty): all 552 enumerated elements are *literally* squares of enumerated systolic elements — zero non-squares, zero components lacking a square member. **ZERO primitives confirmed.** The class count is 24 oriented = **12 unoriented**; the submission's "24 squares" is an oriented count inside an unoriented table (C-AF1).

Counts were stable from depth 5 through 8 (positive part checked through the full depth-8 shell). Scope limits, stated honestly: my conjugacy counts are certified upper bounds with a homology-certified lower bound at the systole level; rows at ℓ ≥ 6.67 (48, 24, 24, 4, 48, 24, 96, and the unconverged 136) and the "122,968 hyperbolic elements with ℓ ≤ 9" figure I did not verify. The stabilizer arithmetic of the claimed rows is internally consistent (96/mult ∈ ℤ throughout: 8,8,4,2,4,4,24,2,4,1), and 136 > 96 forcing beyond-symmetry degeneracy is sound — Bolza is arithmetic (quaternion order over ℚ(√2)), where unbounded multiplicity is expected.

### 2. Literature anchors (from my own knowledge)

Confirmed: systole 2 arccosh(1+√2); Jenni (1984) — Bolza uniquely maximizes the systole in genus 2, with Schmutz Schaller's later work; kissing number 12 in genus 2 attained by Bolza; |Aut⁺| = 48 (GL(2,3)), full isometry group 96, the genus-2 maximum; Buser–Sarnak — maximal systole grows ~log g, so genus-wide systole-maximization diverges; Klein quartic — genus 3, Hurwitz, |Aut⁺| = 168 = PSL(2,7); genus-3 systole-maximality genuinely open. The generator form matches my memory of Aurich–Steiner's regular-octagon model — and my exact verification makes the attribution moot. λ₁-maximality of Bolza in genus 2 by Fortier Bourque–Petri: consistent with my knowledge (rigorous, computer-assisted), moderate confidence; the submission properly brackets it as an import. No mismatches found. Published low-lying Bolza spectrum values agree with the table as far as I recall them (multiplicities usually quoted oriented — exactly double the submission's unoriented column, as my computation confirms).

### 3. BOX-1 and the readings

The injectivity argument is sound: strictly monotone ⟹ injective ⟹ a length class is exactly a mass-degeneracy class. But "reading (A) dead by *internal* contradiction" overstates. The record's registered definition — generations = distinct primitive geodesics with same charge data — is perfectly satisfied by mass-degenerate distinct geodesics. The contradiction needs the *external* qualitative fact that observed generation masses differ. That import is ordinal, not numerical, so no tripwire violation — but the kill is empirically assisted (C-AF2). Liabilities of (B) are fairly, indeed damningly, stated: forced exact ≥4-fold degeneracy with no splitting mechanism, and the 12/12/24 mismatch. (C)'s liability is understated if anything: without an occupancy rule it is contentless. Two readings were missed (C-AF4): (D) generations as iterates ℓ, 2ℓ, 3ℓ of one primitive — automatically mass-distinct under monotone M, excluded *only* by the record's own primitivity clause, which deserves explicit notice since the record's registered wording is doing real work there; (E) reinterpreting exact multiplicity as internal quantum numbers (12 = 3 generations × 4 internal states would convert (B)'s worst liability into structure — requires new record machinery, but its absence from the analysis is a gap). Also, "minimum multiplicity anywhere = 4" extrapolates from ten converged rows to an infinite spectrum (C-AF5). The prime-geodesic-theorem infinite-tower point (GAP-3) is correct: ~e^L/L growth, no internal truncation, nothing marks "three."

### 4. Kill rulings

**K-CAL2-1.** Arm 1 (no internal principle selecting a unique moduli point at test genus): does not fire. Systole-maximality is expressible in the record's own vocabulary (lengths), selects Bolza uniquely at g = 2 (Jenni), and the confluence with kissing number and automorphism maximality (λ₁ honestly bracketed as an import) discharges the tuning concern *at g = 2*. The unselected genus is correctly quarantined in GAP-4 and does not trigger the registered wording. Arm 2 ("cannot host the generation structure"): under (B), hosting is strained but not impossible under the registered wording — and the submission's refusal to sharpen the kill post hoc is procedurally correct (retroactively mandating singlet levels to make the kill fire would be as illegitimate as retroactively weakening it). Under (C), hosting is vacuous: any spectrum with ≥3 slots "hosts" three generations. **Explicit ruling: survival-via-(C) is a loophole, not substantive.** A reading with no occupancy rule cannot host anything in a falsifiable sense; if (C) is retained, the record must register an occupancy rule next round or strike it. The submission's own grade — DOES NOT FIRE, ALIVE-WOUNDED conditional on GAP-2/3/4 — is honest, not generous; I concur with the ruling while insisting the load-bearing survival case is (B)-marginal, not (C).

**K-CAL2-2.** RESPECTED. I searched the submission for measured-mass comparisons, fits of M, or tuning: none. Ratios are stated as structure (explicitly permitted); the extremality principles are standard, pre-existing criteria, not reverse-engineered toward a target spectrum — the ratios fall out of a surface selected on independent grounds. Two near-misses, both properly self-flagged: "three lowest classes" imports the number three from phenomenology (GAP-3 candidly concedes nothing internal marks three), and reading (A)'s kill uses qualitative mass-distinctness (C-AF2). Neither breaches the registered wording.

### 5. Honesty finding

The core claim is correct: with M an unknown strictly-monotone function, any increasing triple maps to any increasing triple, so single-sector ratio spectra have zero falsifiable content; genuine content is ordinal/counting/multiplicity/cross-sector interleaving (one M for all sectors is real rigidity). But it is incomplete (C-AF3). The three regimes:

(i) **M unknown:** only level order and count, multiplicity pattern (every low level ≥4-fold exactly degenerate — currently a *disconfirming* structural prediction), gap structure as ordinal fact, and cross-sector interleaving. Ratios: no content. Submission correct.

(ii) **M pinned at two points** (two measured masses — outside this round's tripwire, but the honest statement of future content): the ratios do *not* become predictive — monotonicity does not interpolate, so 1 : 1.60179 : 1.90638 stays uninformative about the third mass beyond ordering. What *does* appear is falsifiable exclusion content the submission missed: Bolza has no levels strictly between ℓ₁ and ℓ₂ (or ℓ₂ and ℓ₃), so no states may exist in the open mass window between the two pinned masses in that sector, and level-counting in any mass window becomes a hard prediction. The brief's suggestion that pinning makes "the ratios predict all others" is wrong unless M's functional form is also fixed.

(iii) **M derived:** full quantitative spectrum mₖ = M(ℓₖ); the ratio table becomes sharp mass predictions, and the exact-degeneracy pattern becomes an immediate confrontation.

## Corrections ledger

- **C-AF1.** "Exactly the 24 squares of systole classes" at level 10+8√2: oriented count in an unoriented-multiplicity table. Correct unoriented count is 12 (verified exactly; all 552 depth-7 elements are literal squares; 24 oriented / 12 unoriented classes). Labeling, not substance.
- **C-AF2.** Reading (A) is not killed "by internal contradiction": the kill requires the external qualitative fact that generation masses are distinct. Reclassify as BOX-1 + minimal empirical input. No tripwire violation.
- **C-AF3.** Honesty finding incomplete: (a) two-point pinning of M yields falsifiable exclusion windows and window-counting predictions (missed); (b) pinning does *not* make the ratio spectrum predictive (monotone M does not interpolate) — guard against future overclaim.
- **C-AF4.** Two unexamined readings: iterates-as-generations (blocked solely by the record's primitivity clause — should be surfaced) and multiplicity-as-internal-quantum-numbers (potential rescue of (B)).
- **C-AF5.** "Minimum multiplicity anywhere = 4" is an extrapolation from ten converged rows, not a theorem; quantifier overclaims.
- **C-AF6.** Trace table silently reports |trace|: in the +I lift both signs occur (e.g. 8 of 24 oriented systole classes carry trace −(2+2√2)). Unstated, this halves-or-worse a replicator's multiplicities (it initially bit this referee). State the convention.
- **C-AF7.** "6,588,344 words" is the length-exactly-8 shell (8·7⁷), not the cumulative enumeration (7,686,401). Trivial.

## VERDICT BOX

1. Computational anchors: CONFIRMED by independent exact recomputation (systole 3.05714/trace ±(2+2√2)/mult 12; levels 2–3 mult 12/24; 10+8√2 zero primitives; all lengths and ratios exact to printed digits).
2. Literature anchors: CONFIRMED within my knowledge; no mismatches; λ₁ import correctly bracketed.
3. K-CAL2-1: DOES NOT FIRE — but survival-via-reading-(C) is ruled a loophole; substantive status is ALIVE-WOUNDED on (B)-marginal, conditional on GAP-2/3/4.
4. K-CAL2-2: RESPECTED — no measured-mass comparison, no fit, no tuning; two properly self-flagged qualitative near-misses.
5. Seven corrections (C-AF1–C-AF7), all labeling/interpretive; no computational error found in the submission.

Word count: ~1,950.
