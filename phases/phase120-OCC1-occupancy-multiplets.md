# Phase 120 (continuation): OCC-1 round 1 — occupancy rules and the multiplet structure

**Date:** 2026-07-27
**Status:** DRAFTED — **REFEREE DEFERRED (budget)**. NOTHING below is refereed; no verdict enters the phase-120 registration until the adversarial referee pass runs. The consultation below is preserved VERBATIM; nothing edited.
**Provenance:** Context-free derivation agent (OCC-1 mandate, phases/phase120-OCC-SU23-FORK-registration.md §1). K-OCC-3 (numerology tripwire) reported respected.

**Editorial header (operator):**
- **BOTH KILLS CLAIMED FIRED (unrefereed):** K-OCC-1 fires — no candidate occupancy rule is simultaneously record-internal and selective; reading (C) is STRUCK per the standing CAL-2 referee ruling. K-OCC-2 fires — reading (E) (multiplets as generation × internal quantum numbers) is dead: the computed symmetry contains NO order-3 element and acts intransitively; the 12-multiplet decomposes as 4+4+4 into structurally INEQUIVALENT homology-graded sectors, not three copies of anything. **Reading (B) is the sole survivor** for the generation question.
- **GAP-7 claimed REFUTED (unrefereed):** the isometry group computable from the registered octagon realization is D₈ of order 16 (quotient signature (2,8,8), Riemann–Hurwitz closing exactly), NOT 96; no length class among ℓ₁–ℓ₆ is a single orbit; multiplicity ≠ symmetry from the systole row onward; the prior "stabilizer 96/mult" arithmetic has no realized orbit meaning (its ℓ₇ entry would need stabilizer order 24 > 16 — impossible).
- **MAJOR NEW ANOMALY — QUARANTINED, UNADJUDICATED (GAP-8):** this refutes the imported [others'] identification |Isom(Bolza)| = 96 / GL(2,3) FOR THE REGISTERED REALIZATION — despite that realization exactly reproducing the Bolza systole, kissing number, and low spectrum (twice-refereed). This is in DIRECT TENSION with: (i) standard literature (Bolza's automorphism group of order 48/96 is textbook); (ii) the CAL-2 referee's literature confirmation; (iii) systole-maximizer uniqueness. The operator notes the a-priori likeliest resolution is an INCOMPLETE isometry census in this round (the literature's order-3 element must live somewhere the four hunt strategies did not reach), but that is exactly what the deferred referee must adjudicate — with a mandate to explicitly construct or exclude the order-3 isometry on this realization. UNTIL THEN: all symmetry-based claims from both this round AND the prior CAL-2 stabilizer discussion are quarantined; the orbit tables below are conditional on the census's completeness (the round's own GAP-9 concedes negatives depend on closure completeness).
- What survives regardless of the anomaly (positives are exact): the spectrum re-audit (V1 — third independent exact confirmation of the multiplicities); the existence of the 16 verified isometries and their orbit refinements (orbits can only merge, never split, if more isometries exist); the homology grading of classes (conjugation-invariant, exactly computed); the hyperelliptic behavior table; BOX-1's degeneracy argument.
- **Numbers-mandate impact (notes/PLAN-2026-07-27-numbers-mandate.md, step 2):** the occupancy-rule branch of the critical path FAILED honestly — no record-internal selective rule exists. The GOLD/SILVER chain now runs exclusively through reading (B): generations = lowest length classes, with the matching rule (step 4, MATCH-1) carrying the burden the occupancy rule cannot. The window-count (SILVER) targets survive — they need M pinned at two points plus the class list, not an occupancy rule. "Nothing marks three" is SHARPENED: even the symmetry offers no canonical 3 (the recurring three-orbit pattern is reported with its own counterexamples, not promoted).

---

## CONSULTATION (VERBATIM)

# OCC-1 — Occupancy/Multiplet Round: Derivation Record

## Summary and verdicts

**V1 (spectrum audit: PASS).** Exact recomputation of the record's realization (ring ℤ[z]⊕ℤ[z]s, z⁴=−1, s²=2+2√2; word-ball to length 6, 155,577 distinct elements; octagon relation closes to +I) reproduces every registered spectral fact: unoriented multiplicities 12/12/24/48/24/24 at ℓ₁–ℓ₆ and 4 at ℓ₇; oriented counts exactly double (no self-inverse classes); both trace signs occur, and sign is a class invariant; spectral floor exactly at trace 2+2√2; the 2ℓ₁ row is purely squared systoles (12 classes, zero primitives).

**V2 (GAP-7, orbit-transitivity: REFUTED — the round's central empirical result).** The isometry group computable from the record's registered realization has order 16 (dihedral D₈ = ⟨R,σ⟩; orientation-preserving part ℤ₈), not 96. No length class among ℓ₁–ℓ₆ is a single isometry orbit; only ℓ₇ (mult 4) is transitive. The record's "stabilizer arithmetic 96/mult" has no realized orbit meaning; its ℓ₇ entry (stabilizer 24) is impossible in a group of order 16. Arithmetic (non-symmetry) degeneracy begins at ℓ₁, not at the mult-136 row.

**V3 (new anomaly, flagged for the record).** The imported claim [others': Bolza |Isom|=96, GL(2,3)] is contradicted by exhaustive record-internal computation on this realization. Either the realization is not the Bolza surface (despite reproducing the registered systole value 2·arccosh(1+√2), 12 systoles, and full low spectrum — which would put it in tension with [others': systole-maximizer uniqueness at genus 2]), or the literature attachment to this octagon realization is wrong. This must be externally re-refereed ([GAP-8] below).

**V4 (K-OCC-1: FIRES — reading (C) STRUCK).** No candidate occupancy rule is simultaneously record-internal and selective of a definite finite set.

**V5 (K-OCC-2: FIRES — reading (E) dead).** No order-3 element exists in the realizable symmetry, so the isometry group supplies no 3-fold index of any kind. The 12-multiplet does decompose canonically as three blocks of four — but as an *intransitive* orbit decomposition into structurally inequivalent sectors (distinct homology types), not a (generation index)×(internal index) factorization; no group acts on the 3-element block set. Reading (E) as registered is dead; the fine structure is logged as sharpened GAP-5 content.

**V6.** Reading (B) is the sole survivor; readings (A), (D) remain dead as ruled.

## 1. Orbit/stabilizer computation

**Method [BOX-2].** All arithmetic exact over ℤ[z]⊕ℤ[z]s. Conjugacy classes by norm-bounded conjugation closure with union-find (unions only on verified exact conjugations, so class counts are exact once they match the registered multiplicities — they all do). Isometries: R (b₀→b₁→b₂→b₃→b₀⁻¹; exact ring operation: top-right ×z) and σ (b₀→b₀, b₁→b₃⁻¹, b₂→b₂⁻¹, b₃→b₁⁻¹; entrywise conjugation) verified to preserve the relation exactly; ⟨R,σ⟩ ≅ D₈, order 16, closed as a permutation group on all class rows.

**Isometry census [BOX-3, load-bearing].** Any additional isometry was hunted four independent ways: (i) geometric grid of elliptic rotations at all candidate (2,3,8)-tiling vertices around both order-8 fixed points (octagon center and corner); (ii) general conjugator pair-solves (SVD nullspaces) over all systole-trace image pairs to word length 5; (iii) exhaustive algebraic solve: for *every* possible image g₀ of b₀ (all 1112 trace-(+2+2√2) elements of the exact conjugation-closure slice to norm 650), the full 2-dimensional solution space of ρb₀ρ⁻¹=g₀ was intersected with det ρ=1 and tr ρ = 2cos(kπ/n) for every elliptic order realizable on genus 2 (n = 2,3,4,5,6,8,10; all k), images verified against the complete exact trace-slice (53,048 elements, norm ≤ 20000 — a 32× margin over the provable image bound e^{2·2.4485}·‖b‖ ≈ 618 for any elliptic lift with fixed point in the closed fundamental octagon; such a lift must exist for every finite-order orientation-preserving isometry since all have fixed points on genus 2 by Riemann–Hurwitz parity); (iv) class-quadruple identification of all 508 elliptic normalizers found. Result: normalizing elliptics exist at orders 2, 4, 8 only, and every one induces one of the 16 known ⟨R,σ⟩ outer classes. Orders 3, 5, 6, 10: zero. The method's positive controls: it recovers R, R-powers, the hyperelliptic π-rotations at all six Weierstrass points (center, corner, four edge-midpoint classes — count 6 ✓), and all 8 reflections.

**Consistency [BOX-4].** Quotient orbifold from the fixed-point census: signature (2,8,8); Riemann–Hurwitz closes exactly for |Isom⁺|=8 (2 = −16+4+7+7). A 32-element holomorphic action on genus 2 admits no valid signature, and any group of order 24/48/96 contains order 3 (refuted); with the order-16 case excluded by the (2,4,8)-generation obstruction for the computed order profile, Isom = D₈(16) is forced. Lagrange then bars transitivity on any 12- or 24-fold multiplet (12 ∤ 16, 24 ∤ 16).

**Orbit table** (unoriented classes; full D₈(16); stabilizer order = 16/orbit):

| row | mult | orbit sizes | stabilizers | grading of orbits (computed invariants) |
|---|---|---|---|---|
| ℓ₁ | 12 | 4+4+4 | 4, 4, 4 | H₁ support 1 (±e_k, tr +) / support 2 (tr +) / support 3 (tr −) |
| ℓ₂ | 12 | 4+4+4 | 4, 4, 4 | supp 2 (tr +) / supp 3 with a ±2 (tr +) / supp 4 (tr −) |
| ℓ₃ | 24 | 4+4+8+8 | 4,4,2,2 | supp-2 adjacent (+) / supp-4 double-2 (+) / supp-2 with 2 (+) / supp-4 (−) |
| ℓ₄ | 48 | 16+16+16 | 1, 1, 1 | free orbits; hyperelliptic *moves* unoriented classes (chiral pairs) |
| ℓ₅ | 24 | 8+8+8 | 2, 2, 2 | hyperelliptic moves classes |
| ℓ₆ | 24 | 8+8+8 | 2, 2, 2 | hyperelliptic fixes classes |
| ℓ₇ | 4 | 4 (transitive) | 4 | all H₁ = 0 (commutator/null-homologous), tr − |

The ℓ₁ generator-orbit stabilizer is verified Klein-four {1, σ, R⁴, σR⁴} (contains the hyperelliptic); remaining order-4 stabilizers are reflection+hyperelliptic type by exclusion of rotations (ℤ₈ acts freely on oriented classes) [GAP-10: iso-types beyond ℓ₁ inferred, not element-listed]. Homology grades every orbit at ℓ₁–ℓ₃ completely: within each row, (H₁ support pattern, trace sign) separates exactly the orbits — the record thus *does* own an internal quantum number: it is the orbit label itself, jointly carried by homology class and trace sign. Hyperelliptic behavior is row-dependent: it fixes all unoriented classes at ℓ₁,ℓ₂,ℓ₃,ℓ₆,ℓ₇ but pairs distinct classes at ℓ₄,ℓ₅.

**Answer to the reading-(E) question.** The 12-multiplet carries no transitive action at all, hence no block system of a transitive action and no (3-block)×(4-block) product. What exists is an intransitive canonical partition 12 = 4+4+4 whose three parts are *inequivalent* (different homology support, different trace sign) — three sectors, not three copies. Under K-OCC-3 discipline: the recurrence of "three orbits" at ℓ₁, ℓ₂, ℓ₄, ℓ₅, ℓ₆ is reported together with its counterexamples (ℓ₃: four orbits; ℓ₇: one) and is *not* promoted to a generation count; it was found, not engineered.

## 2. Occupancy rules (reading (C) survival test)

(a) **One defect per isometry orbit.** Statable and now fully record-internal (the group is computed). Selects a definite set *per row* (3,3,4,3,3,3,1,… slots) but the length cutoff is unfixed: infinitely many orbits in total. Not selective. Also under-determined within an orbit unless the defect is read as delocalized over the orbit. Fails.
(b) **Homology-graded occupancy.** Statable record-internally (H₁ computed per class; conjugation-invariant). Two sharp variants: "occupy H₁-primitive support-1 classes" — at ℓ₁ this selects exactly the 4 central-axis systoles, and no ±e_k class recurs through ℓ₇ (checked; unbounded beyond that [GAP-11]); "occupy null-homologous classes" — first selects ℓ₇'s symmetric quadruplet. Each grades but does not bound: infinitely many classes of any homology type expected at large length. Selective only with an unfixed cutoff. Fails as sole rule.
(c) **k lowest classes.** Nothing in the record fixes k. Fails (as anticipated by the task).
(d) **Charge-lattice compatibility.** The record's charge enters only through D = Q²ℓ/2π; no registered structure couples the charge lattice to trace field or homology. Not statable record-internally. Fails.
(e) **Exclusion principle.** A constraint (≤1 per slot), not a selection. Fails as sole rule.

**K-OCC-1 ruling: FIRES.** No candidate is both record-internal and selective. Per the standing referee ruling, reading (C) is **STRUCK**.

## 3. K-OCC-2 ruling

"Naturally" was pre-specified as: group-theoretic factorization, invariant grading, or nothing. Computed answer: no factorization (intransitive action; no order-3 exists in the realizable symmetry group, so no 3-index is acted on by anything); there *is* an invariant grading (orbit = homology-support × trace-sign sectors, 4+4+4). This grading cannot host generations: by BOX-1 all 12 states are exactly mass-degenerate, and the registered qualitative fact is that generation masses differ. **K-OCC-2 FIRES: reading (E) is dead.** GAP-5 stands with sharpened content: the ≥4-fold multiplets are unions of symmetry orbits carrying a computable two-part label (orbit sector; homology class), awaiting physical interpretation that respects exact intra-row degeneracy.

## 4. Synthesis — what calibration step 2 inherits

- **Live:** reading (B) only — generations = distinct low length classes (mass ordering from monotone M [BOX-1]); each class an exact degeneracy multiplet with the computed fine structure.
- **Registered structural predictions:** any dynamics respecting the record's symmetry must be constant on orbits; the systole multiplet must behave as 3 inequivalent sub-multiplets of 4 (homology-graded), never as 12 equivalent states; ℓ₄ and ℓ₅ states occur in hyperelliptic-chiral pairs; ℓ₇ is the first fully symmetric null-homologous quadruplet. Exclusion windows: no realizable symmetry can merge classes across rows (M injective) or across orbit sectors within a row.
- **Not done (per task):** no derivation of "three" (GAP-3 stands, sharpened: even the symmetry offers no canonical 3); no genus derivation (GAP-4 stands); no interpretation of multiplets beyond the computed sector structure.
- **Urgent for the record:** re-referee the Bolza attachment ([GAP-8]); every downstream use of "96", "GL(2,3)", or "stabilizer 96/mult" is unsupported for the registered realization.

## VERDICT BOX

1. GAP-7: **REFUTED** — computable isometry group is D₈ (order 16, quotient (2,8,8)); no ℓ₁–ℓ₆ row is one orbit; multiplicity ≠ symmetry orbit from ℓ₁ onward.
2. K-OCC-1: **FIRED** — reading (C) STRUCK (no record-internal selective occupancy rule).
3. K-OCC-2: **FIRED** — reading (E) dead (no order-3, no transitive factorization; 12 = 4+4+4 intransitive homology-graded sectors, not generations).
4. Reading (B) sole survivor; BOX-1 and MASS-1 untouched; K-OCC-3 respected (no mass comparisons, no tuning; "three orbits" reported with counterexample ℓ₃).
5. NEW ANOMALY [GAP-8]: imported |Isom|=96 [others'] fails for the registered realization — identification with Bolza must be re-refereed before any symmetry-based claim is reused.

## Gaps-and-boxes ledger

- [BOX-1] (inherited, used): monotone M ⟹ exact intra-class degeneracy ⟹ no generations within a class.
- [BOX-2] exact class/orbit machinery (validated against all registered multiplicities).
- [BOX-3] exhaustive elliptic-normalizer census (validated on 508 positive controls; zero at orders 3,5,6,10).
- [BOX-4] Riemann–Hurwitz/Lagrange closure forcing |Isom|=16.
- [GAP-8] (new, major): Bolza-attachment anomaly (realization vs [others'] 96/GL(2,3); tension with [others'] systole-maximizer uniqueness).
- [GAP-9] residual numeric epsilon: conjugation-closure reachability (32× norm margin) and 10⁻³-rounding lookups; all *positives* exactly verified; negatives depend on closure completeness.
- [GAP-10] stabilizer iso-types beyond ℓ₁ inferred (order exact, structure argued).
- [GAP-11] audit depth ends at ℓ₇; ℓ₈–ℓ₁₀ and mult-136 not orbit-decomposed (ℓ₁₀'s mult 96 now implies ≥6 orbits).
- [others'] imports used: genus-2 maximal automorphism facts, realizable automorphism orders {2,…,6,8,10}, Riemann–Hurwitz, triangle-group areas; Bolza attributions now quarantined under [GAP-8].

Word count: ~1990.

---

## Amendment section

*(Reserved. REFEREE DEFERRED for budget — to be dispatched next usage cycle with these pre-committed mandates: (1) ADJUDICATE GAP-8 by explicitly constructing or excluding the order-3 isometry on this exact realization — the literature's 48/96 automorphism group is textbook-solid, so an incomplete census is the a-priori likeliest resolution; the census's negative results (BOX-3, GAP-9) are the attack surface; (2) verify the D₈ orbit tables and homology gradings (positives, exactly checkable); (3) audit both kill rulings against the registered wordings; (4) rule what survives if the census IS incomplete — orbits merge but never split, so which claims are census-robust. No verdict enters any registration until then.)*
