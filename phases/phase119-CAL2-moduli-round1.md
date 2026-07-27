# Phase 119 (continuation): CAL-2 round 1 — extremality selection and the Bolza length spectrum

**Date:** 2026-07-27
**Status:** DRAFTED — awaiting referee. No verdict enters the phase-119 registration until the referee pass completes. The consultation below is preserved VERBATIM; nothing edited. (The agent's own header line styling is preserved as delivered.)
**Provenance:** Context-free derivation agent (CAL-2 route (a) mandate, registered in phases/phase119-CAL2-SU22-registration.md §1). The K-CAL2-2 numerology tripwire was binding; the agent reports compliance (no comparison to measured masses anywhere).

**Editorial header (operator):**
- Headline claims (UNREFEREED): **K-CAL2-1 does not fire** — at genus 2 a record-internal principle (systole-maximality) selects a unique point (the Bolza surface, [others']), the selection is ROBUST (at least three record-internal principles coincide there — systole-maximality, maximal automorphisms, maximal kissing number, reportedly also λ₁), and the spectrum can host three generations under the occupancy reading. Route (a) ALIVE-WOUNDED, conditional on three named gaps: no occupancy rule (GAP-2), no truncation of the infinite level tower — nothing marks "three" (GAP-3), and the genus blank underived (GAP-4).
- **Both refereed anchors CONFIRMED by exact computation:** systole = 2·arccosh(1+√2) = 3.05714 (trace 2+2√2), unoriented primitive multiplicity 12 (= the known kissing number). Method: exact integer arithmetic in the ring {a + b·s : a,b ∈ ℤ[z]}, z⁴ = −1, s² = 2+2√2; octagon relation verified to close exactly; 6,588,344 words enumerated to length 8; 122,968 distinct hyperbolic elements retained; conjugacy via union-find (counts are a priori upper bounds, BOX-2); primitivity by exact power-marking. Ten depth-converged primitive classes through ℓ ≈ 8.22; three deeper rows honestly reported as unconverged lower bounds (GAP-1 — with the cautionary finding that depth-stability was shown fallible).
- **The parameter-free ordinal output of the Bolza point:** length ratios 1 : 1.60179 : 1.90638 : 2.18243 : … with multiplicities 12, 12, 24, 48, 24, 24, 4, 48, 24, 96; the ℓ = 2ℓ₁ level is PURELY imprimitive (squared systoles — zero primitives).
- **The load-bearing derivation (BOX-1):** MASS-1's monotone M is injective ⟹ a length class is an exact-degeneracy multiplet ⟹ generations CANNOT be symmetry-related geodesics of one class; a generation ladder climbs ACROSS length classes. This resolves the degeneracy dilemma by derivation, killing reading (A) on the record's own terms. Reading (B) (generations = the three lowest classes) survives at the cost of uninterpreted ≥4-fold multiplets (GAP-5: no level of multiplicity < 4 exists ANYWHERE in the computed range); reading (C) (occupancy/slots) is cleanest but needs the missing occupancy rule.
- **The honesty finding (structural, important):** because M is an unknown strictly monotone function, the single-sector ratio spectrum has NO falsifiable content by itself — any increasing length triple maps to any increasing mass triple under some monotone M. The genuine parameter-free content is (a) level order and count, (b) the multiplicity pattern, (c) cross-sector rigidity: ONE M serves every charge sector via ℓ = 2πD/Q², so the INTERLEAVING of levels across different-Q sectors is a rigid ordinal prediction once occupancy is fixed. This finding sharpens the calibration plan: step 2's real deliverable is ordinal/cross-sector structure, not ratios.
- K-CAL2-2 compliance claimed (referee to audit): ratios stated as structure; no measured-mass comparison anywhere; the agent explicitly declined to sharpen the kill condition post hoc when it noticed that a singlet-mandating record WOULD have fired arm 2.

---

## CONSULTATION (VERBATIM)

CAL-2 (route a): EXTREMALITY SELECTION — DERIVATION RECORD

SUMMARY AND VERDICTS

1. Both refereed anchors are CONFIRMED by independent exact computation: the Bolza systole is exactly 2 arccosh(1+sqrt2) = 3.05714 (trace 2+2sqrt2), with unoriented primitive multiplicity 12.
2. The primitive length spectrum of the Bolza surface was computed by exact integer arithmetic to length ~8.9; the first 10 primitive classes (through l = 8.22) are stable under the deepest enumeration step (word-length 7 -> 8); three deeper rows are still growing and are reported as lower bounds [GAP-1].
3. K-CAL2-1 ruling: DOES NOT FIRE. At genus 2 a record-internal principle (systole-maximality) selects a unique point (Bolza) [others'], and the selected spectrum contains three distinct low-lying length classes whose multiplicities are workable under one of the two admissible readings (the occupancy reading). Route (a) survives, wounded by three named gaps: the genus blank [GAP-4], the absence of an occupancy/truncation rule [GAP-2, GAP-3], and the uninterpreted internal multiplicities [GAP-5].
4. Honesty finding (structural): because MASS-1's M is an unknown strictly monotone function, the single-sector ratio spectrum has by itself NO falsifiable content — any increasing length triple maps to any increasing mass triple under some monotone M. The parameter-free content of the Bolza point is ordinal and cross-sector (orderings, multiplicities, interleavings under l = 2*pi*D/Q^2), not single-sector ratios. K-CAL2-2 was respected throughout: no comparison to measured masses was made.

1. CANDIDATE EXTREMALITY PRINCIPLES

(i) Systole-maximality at fixed genus. Statable using only lengths of closed geodesics: record-internal. At genus 2 it selects the Bolza surface, uniquely [others': Jenni 1984; Schmutz Schaller 1993 — imported, not verified here; the Bolza systole VALUE and multiplicity are verified below, its extremality is not].
(ii) Maximal automorphism group. Statable using only isometries of the record's own metric: record-internal. At genus 2 the maximum is |Aut+| = 48, attained by Bolza (unverified [others']).
(iii) Extremal first Laplace eigenvalue. Requires a Laplacian, i.e., a field/wave structure the record does not currently contain (it has geodesics, lengths, charged defects); admissible only as an extension — flagged as an import. Reported to be maximized at genus 2 by Bolza via linear-programming bounds [others': Fortier Bourque–Petri — unverified].
(iv) Maximal kissing number (number of systoles) at fixed genus. Record-internal (pure length data). Reported maximum 12 at genus 2, attained by Bolza [others': Schmutz Schaller — unverified; the value 12 for Bolza is verified below].
(v) Other natural candidates: extremal Selberg zeta / determinant of the Laplacian (import, same caveat as (iii); status unverified), minimal diameter (record-internal; extremizer unknown to me), arithmeticity/maximal quaternion order (record-internal-adjacent; selects a finite class, not obviously a unique point — Bolza is arithmetic, derived from a quaternion order over Q(sqrt2) [others']).

Coincidence structure at genus 2: candidates (i), (ii), (iv) — and reportedly (iii) — all select the SAME point, the Bolza surface. This confluence is route (a)'s strongest evidence: the selection is robust to the choice among record-internal principles at genus 2, so no tuning of the principle toward a desired spectrum occurs there (K-CAL2-2 concern discharged at g=2).

2. THE BOLZA PRIMITIVE LENGTH SPECTRUM (exact computation)

Method [BOX-3]. The Bolza fundamental group was taken in its standard regular-octagon SU(1,1) form: generators b_k = [[1+sqrt2, s*z^k],[s*z^(-k), 1+sqrt2]], k = 0..3, z = exp(i*pi/4), s = sqrt(2+2*sqrt2) [others': Aurich–Steiner form]. Before use, verified EXACTLY (integer arithmetic in the ring {a + b*s : a,b in Z[z]}, z^4 = -1, s^2 = 2+2*sqrt2; 32 integers per matrix): det = 1; SU(1,1) structure; the octagon relation b0 b1^-1 b2 b3^-1 b0^-1 b1 b2^-1 b3 = identity holds exactly; no elliptic or parabolic traces occur; all traces lie in Z[sqrt2] (as required for this arithmetic group). Enumeration: all reduced words to length 8 (6,588,344 at the top level), exact PSU sign canonicalization and deduplication, retaining the 122,968 distinct hyperbolic elements with l = 2 arccosh(|tr|/2) <= 9. Conjugacy classes (= oriented geodesics): union-find under conjugation by all 64 words of length <= 2, with lookups inside the retained set — class counts are therefore a priori UPPER bounds [BOX-2]; the method validates exactly on the systole (24 oriented = 12 unoriented = the known kissing number). Primitivity: exact marking of k-th powers. Inverse classes were matched exactly (0 failures), giving unoriented counts. Completeness: NO rigorous guarantee that every geodesic with l <= 8.9 is represented by a word of length <= 8 [GAP-1]; evidence is stability of rows under the deepest enumeration step 7 -> 8, plus the exact systole/kissing validation. Cautionary finding: two rows (k = 11, 13 below) that were stable under 6 -> 7 nevertheless grew at depth 8 — depth-stability is evidence, not proof, and the ledger treats it as such [GAP-1].

Primitive spectrum (unoriented multiplicities; cosh(l_k/2) = (p + q*sqrt2)/2):

```
 k   l_k       trace p+q*sqrt2   mult   l_k/l_1    status (depth 7 -> 8)
 1   3.05714    2 +  2 sqrt2      12    1.00000    converged (anchor: = 2 arccosh(1+sqrt2), mult 12 — both anchors CONFIRMED)
 2   4.89690    6 +  4 sqrt2      12    1.60179    converged
 3   5.82807   10 +  6 sqrt2      24    1.90638    converged
 -   6.11428   10 +  8 sqrt2       0    2.00000    converged; NO primitives: this level consists exactly of the 24 squares of systole classes
 4   6.67201   14 + 10 sqrt2      48    2.18243    converged
 5   7.10738   18 + 12 sqrt2      24    2.32484    converged
 6   7.26316   18 + 14 sqrt2      24    2.37580    converged
 7   7.59569   22 + 16 sqrt2       4    2.48457    converged
 8   7.88069   26 + 18 sqrt2      48    2.57780    converged (was 32 at depth 6)
 9   8.13008   30 + 20 sqrt2      24    2.65937    converged
10   8.22490   30 + 22 sqrt2      96    2.69039    converged (was 88 at depth 6)
11   8.43685   34 + 24 sqrt2      24    2.75972    NOT converged (20 -> 24; lower bound)
12   8.62846   38 + 26 sqrt2      48    2.82240    converged
13   8.70275   38 + 28 sqrt2      24    2.84670    NOT converged (16 -> 24; lower bound)
14   8.87148   42 + 30 sqrt2     136    2.90189    NOT converged (128 -> 136; lower bound)
```

Structural observations: every observed trace has p = 2 mod 4 and q even; the smallest multiplicity anywhere is 4 (class k=7) — NO singlet, doublet, or triplet levels occur in the computed range; multiplicities of the converged classes are consistent with orbits of the order-96 isometry group [others': |Isom(Bolza)| = 96, unverified], with stabilizers of order 8, 8, 4, 2, 4, 4, 24, 2, 4, 1 (orbit-transitivity per class unverified [GAP-7]); the k=14 class (>= 136 > 96) cannot be a single isometry orbit — a degeneracy beyond symmetry, as expected on an arithmetic surface [others'].

3. STRUCTURAL CONFRONTATION WITH MASS-1

[BOX-1] MASS-1's registered monotone-increasing M is injective; at fixed Q, mass is a strictly increasing function of l. Therefore: distinct generation masses <=> distinct lengths. This immediately DERIVES (not assumes) the resolution of the degeneracy dilemma: generations CANNOT be symmetry-related geodesics of one length class — those carry exactly equal mass. A length class is an exact-degeneracy multiplet; a generation ladder must climb ACROSS length classes.

Reading (A) — generations within one degenerate class: excluded by [BOX-1] as an internal contradiction (equal masses, but generations are defined by distinct masses). Dead on the record's own terms; no measured data invoked.

Reading (B) — generations = the distinct low-lying length classes, multiplicities = internal multiplet structure. Then the record predicts, parameter-free: three lowest generation levels in ratio 1 : 1.60179 : 1.90638 (in LENGTH; masses follow under unknown monotone M — these ratios are the record's raw predictions-in-waiting and were NOT compared to any measured spectrum, per K-CAL2-2), with internal multiplets of sizes 12, 12, 24. Liabilities: no level in the entire computed range has multiplicity < 4, so every particle would sit in a >= 4-fold exactly degenerate multiplet for which the record supplies no quantum number, no interpretation, and no splitting mechanism [GAP-5]; and the third class's multiplet (24) differs from the first two (12), so the third "generation" would differ from the others in an attribute besides mass, straining the registered definition of a generation.

Reading (C) — occupancy: geodesics are available slots; a physical defect occupies one geodesic; three generations = three occupied slots in the three lowest classes. No degeneracy contradiction arises, and multiplicities become slot counts, not particle degeneracies. Liability: the record contains NO occupancy rule — nothing says which slots are filled, why one per class, or why only three classes [GAP-2].

Accumulation. Primitive geodesics proliferate exponentially, pi(L) ~ e^L / L [others': prime geodesic theorem]; the level tower is infinite and unbounded in l. Under monotone M this predicts infinitely many generations of increasing mass (or masses accumulating at sup M if M is bounded — still infinitely many states) unless something truncates. NO record-internal truncation candidate was found: the record's only internal scales are the systole, the genus, and Q; none marks "three" [GAP-3]. This is a standing structural liability of route (a), not resolved here. A related unstated point: the level at exactly 2*l_1 is purely imprimitive (doubly traversed systoles); the record does not say whether iterates carry defects [GAP-6].

Falsifiability structure (ordinal, K-CAL2-2-compliant). Because M is an unknown monotone function, ANY three increasing masses are compatible with the three lowest length classes: the single-sector ratio spectrum, though parameter-free, is not yet a prediction. Genuine parameter-free content: (a) the ORDER and COUNT of levels; (b) the multiplicity pattern (12, 12, 24, 48, 24, 24, 4, ...); (c) cross-sector rigidity — one and the same M serves every charge sector, and l = 2*pi*D/Q^2 ties sectors together, so the interleaving of mass levels across different-Q sectors is a rigid ordinal prediction once occupancy is fixed.

4. THE SELECTION QUESTION AND THE KILL RULING

Genus 2: systole-maximality selects a unique point, the Bolza surface [others': Jenni; Schmutz Schaller — uniqueness imported, unverified here], and (i), (ii), (iv) — reportedly (iii) — coincide there. Genus 3: maximal symmetry selects the Klein quartic (Hurwitz bound 84(g-1) = 168 attained) [others']; lambda_1-maximality is reported for the Klein quartic by the same linear-programming method [others': Fortier Bourque–Petri — unverified]; systole-maximality in genus 3 is, to my knowledge, OPEN (Klein quartic is a candidate; neither extremality nor uniqueness verified) (unverified). General genus: no candidate principle is known to select uniquely at every genus, and nothing internal selects the genus itself; "maximize systole over all g" diverges, since the genus-g systole maximum grows without bound like a multiple of log g [others': Buser–Sarnak — unverified]. The genus remains the record's named blank [GAP-4].

K-CAL2-1 ruling. Arm 1 (no unique selection): does NOT fire at fixed genus 2 — unique selection exists and is robust across at least three record-internal principles. Arm 2 (spectrum cannot host generation structure): does NOT fire — three distinct low-lying length classes exist (ratios 1 : 1.60179 : 1.90638) with multiplicities that are workable under reading (C), and marginally under reading (B) at the cost of [GAP-5]. VERDICT: K-CAL2-1 DOES NOT FIRE. Route (a) is alive at fixed genus 2 — wounded, with its survival conditional on closing [GAP-2]/[GAP-3] (occupancy/truncation) and on either fixing the genus externally or finding an internal genus selector [GAP-4]. Had the record mandated singlet generation levels, arm 2 would fire (minimum observed multiplicity is 4); the registered record does not mandate this, and the referee declines to sharpen the kill condition post hoc.

5. ROUTE (b) — REGISTERED ALTERNATIVE (statement only)

If K-CAL2-1 had fired (or should route (a)'s gaps prove unclosable), the fallback is: the 6g-6 moduli of X are environmental parameters, fixed by no principle — the length spectrum is then measured, not derived. The first few independent lengths (up to 6g-6 of them) calibrate the moduli; every FURTHER length, multiplicity, and cross-sector interleaving becomes an overdetermined consistency check of the record. Route (b) sacrifices parameter-freeness but retains falsifiability through that overdetermination; it is registered here as the standing alternative and requires no computation now.

VERDICT BOX
1. K-CAL2-1: DOES NOT FIRE — unique record-internal selection exists at genus 2 (Bolza, via systole-maximality [others']); spectrum can host three generations under the occupancy reading.
2. Anchors CONFIRMED exactly: systole 2 arccosh(1+sqrt2) = 3.05714, trace 2+2 sqrt2, unoriented multiplicity 12.
3. Parameter-free ordinal output at the Bolza point (10 depth-converged primitive classes): ratios 1 : 1.60179 : 1.90638 : 2.18243 : 2.32484 : 2.37580 : 2.48457 : 2.57780 : 2.65937 : 2.69039; multiplicities 12, 12, 24, 48, 24, 24, 4, 48, 24, 96.
4. Structural liabilities: no level of multiplicity < 4 anywhere computed; unequal multiplets across the lowest classes; infinite untruncated level tower; genus underived.
5. Route (a): ALIVE-WOUNDED at fixed g=2; falsifiable content is ordinal and cross-sector (monotone-M gauge freedom voids single-sector ratio predictions); route (b) remains registered.

GAPS-AND-BOXES LEDGER
[BOX-1] Injectivity of monotone M forces generations onto distinct length classes; length classes are exact-degeneracy multiplets. (Load-bearing derivation; depends only on MASS-1 as registered.)
[BOX-2] Class counts are union-find upper bounds within a word-length-8 ball; validated exactly against the systole/kissing anchor.
[BOX-3] Identification of the stated SU(1,1) generators with the Bolza group: octagon relation, determinants, trace integrality all verified exactly; the identification itself is imported [others'].
[GAP-1] No rigorous completeness of the enumerated spectrum: word-length-8 truncation; rows k = 11, 13, 14 unconverged (multiplicity lower bounds); depth-stability shown fallible (two rows stable at 6 -> 7 grew at depth 8).
[GAP-2] No occupancy rule: which geodesic slots carry physical defects is unspecified.
[GAP-3] No record-internal truncation of the infinite level tower; nothing marks "three".
[GAP-4] Genus not derived; all genus-2 selection results are conditional on g=2.
[GAP-5] No interpretation, quantum number, or splitting mechanism for the >= 4-fold internal multiplets.
[GAP-6] Status of imprimitive (iterated) geodesics as defect carriers unstated.
[GAP-7] Transitivity of the isometry group on each length class assumed plausible, not verified; several extremality facts imported [others'] without verification, as tagged inline.

Word count: 2282

---

## Amendment section

*(Reserved. To be filled only after the adversarial referee pass. No verdict is entered in the phase-119 registration until then.)*
