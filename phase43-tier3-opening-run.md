# Phase 43 — Tier 3 opening run: the carrier switch, the skein-ħ check, the V.7 checklist, and the uniqueness argument

*Working session, 2026-07-17. Executes TIER-3-PLAN §6 steps 1–4 (B3, C1, A1, D). Headline result, stated up front because it is the program's largest single advance since the audit began: **there exists a foliation class for which every operator-algebra property the framework needs is already proven — and for it, the fold's algebra and the laboratory's local algebra are literally the same object** (the unique hyperfinite type III₁ factor). The program's reference carrier is switched accordingly. The phase-39 open question is thereby resolved by substitution; B3 passes with a bonus structural corollary (the one scale may be discrete); V.7 is reduced to a net-arrangement problem; and the "fold as THE activator" argument is written.*

---

## 1. C1 — the carrier switch [verified against primary sources]

**The finding.** For the **weak-stable (Anosov) foliation F_ws of Σ = T¹Σ_g** — the unit tangent bundle of a compact hyperbolic surface, itself a closed 3-manifold — every property the framework's spine needs is established in the literature:

1. **GV ≠ 0** — this is the *original* nonvanishing Godbillon–Vey example (Roussarie, reported in Godbillon–Vey, C. R. Acad. Sci. 273 (1971) 92; Ghys, Sém. Bourbaki 706, verbatim: the first nonzero example).
2. **Factor** — the leafwise relation is orbit-equivalent to the boundary action of π₁(Σ_g) on S¹ with the Lebesgue class, which is ergodic.
3. **Type III₁** — Connes, *NCG* (1994), Ch. I p. 9–10, verbatim: Anosov foliations of unit sphere bundles of genus > 1 surfaces "give a factor of type III₁"; independently proven by the ratio-set argument (geodesic-flow scaling ⇒ ratio set = ℝ₊): Spatzier, ETDS 7 (1987) 289.
4. **Hyperfinite/injective** — Spatzier's amenability + Connes–Feldman–Weiss, ETDS 1 (1981) 431. ~~*(Correction logged: there is no "Bowen, Anosov foliations are hyperfinite" paper — that citation, if it appears anywhere in our notes, conflates Bowen–Marcus 1977 on horocycle unique ergodicity.)*~~ **[ERRATUM TO THE ERRATUM, 2026-07-18, fresh red team FR-3: the struck "correction" was itself wrong. R. Bowen, "Anosov foliations are hyperfinite," Ann. of Math. 106 (1977) 549–565, EXISTS — confirmed via Tondeur's foliation bibliography; Spatzier 1987 (item 3) itself cites it. Bowen 1977 is restored as the primary hyperfiniteness source, with Spatzier + CFW as the route used above. The meta-lesson is logged in phase 74: the ledger's failure mode is not only fabricating citations but fabricating absences — both are now checked against sources, not memory.]**
5. **Uniqueness** — Haagerup, Acta Math. 158 (1987) 95: there is exactly one injective III₁ factor.
6. **The QFT side** — Buchholz–D'Antoni–Fredenhagen, CMP 111 (1987) 123: the local algebras of physically reasonable quantum field theories are that same unique hyperfinite III₁ factor (survey: Yngvason, math-ph/0411058).

**The consequence (the headline).** Combining 1–6:

> **W*(T¹Σ_g, F_ws) ≅ R_∞ ≅ every local algebra of quantum field theory.**
>
> The folded geometry's algebra and the laboratory's local algebra are abstractly the *same object* — not analogous, not similar in type: isomorphic, by a uniqueness theorem. [theorem-level, assembled from the six cited results]

**The switch, and why it is now free.** The program had fixed on Thurston-type foliations of S³ (for the arbitrary-GV realization), whose type is established nowhere (confirmed: no literature; such foliations may not even be factors). But phase 42 retired the AMK numerology — the only part of the program that ever *used* the GV magnitude. Everything that survives needs only GV ≠ 0. **Therefore the framework adopts Σ = T¹Σ_g with F_ws as its canonical carrier**, on which the entire spine — V.1–V.5 (M0b/M0c), L1/L2, M1, the Connes pairing — now runs on proven ground with the III₁-conditional caveats of phase 39 *discharged* (the Connes–Størmer homogeneity of phase 32 §5.4 and the "outer at every t ≠ 0" statement are unconditional on this carrier). The exotic-R⁴/S³ chapter is re-graded: a historical motivation and an open mathematical flank, no longer load-bearing. One correction inherited from the hunt: for the III₁ carrier the **flow of weights is trivial** (that is what III₁ means), consistent with Connes' GV theorem trivially; the geometric content of "GV meters the clock" lives entirely in the Connes *pairing* (phase 36 Layer 2) — which is exactly the formulation phase 36 chose, now vindicated as the only survivable one.

## 2. B3 — the skein-ħ consistency check [passes; one new corollary]

The check: the deformation parameter of the quantization map (phase 34: Goldman Poisson algebra → Kauffman skein algebra, t = e^{h/4}) and the ħ of the clock relation R1 (k_B T·𝒯 = ħ, phase 41) must be the same constant.

**Setup.** The skein h is dimensionless; the physical identification must read h = ħ/S₀, where S₀ is the natural action scale of the Goldman symplectic form on the character variety. R1's ħ is fixed by (T, 𝒯). Consistency requires only that one action scale S₀ exists making both true simultaneously — and since S₀ is exactly the undetermined "one scale" in its symplectic guise, **no obstruction exists: B3 passes.** [derived at structural level] The check is non-vacuous in one direction: had the skein side *forced* a particular dimensionful h independently of the modular side, the two could have clashed; it does not — it forces something better:

**The corollary (new, conjecture-level).** The Goldman/Atiyah–Bott form on the character variety is *integral*; finite-dimensional (TQFT) quantizations exist only at discrete levels, i.e., t at roots of unity. The framework's sector census is *finite* (Bradlow truncation, phases 28/40). **If** the finite census is implemented by the finite-level quantization — the natural reading — **then h is pinned to a discrete series, and with it the single scale of phase 41: the framework's one free scale would be quantized, not tunable,** with the classical limit as level → ∞. [conjecture, conditional on the finite-census ⇒ finite-level identification; flagged: at roots of unity the skein algebra develops a large center — whether that structure matches the superselection story is a sharp follow-up question, logged as **B3b**.] A one-parameter theory whose one parameter is discrete is the strongest "predict, don't fit" structure the program has ever had on the table; B3b is now on the critical path.

## 3. A1 — the V.7 checklist, with condition (1) discharged

V.7 as a scorable list, updated for the carrier switch:

| # | Condition the join needs | Status |
|---|---|---|
| 1 | Local building blocks match: foliation algebra ≅ hyperfinite III₁ = QFT local algebra | **PASSED — theorem level** (§1; the C1 assembly) |
| 2 | Net structure: a coherent assignment O ↦ A(O) of subalgebras of W*(Σ,F_ws) to regions of ℝ×Σ with isotony and locality | **OPEN — this is now the entire content of V.7** |
| 3 | Split property / nuclearity of the inclusions | open; checkable once (2) has a candidate |
| 4 | Haag-duality pattern, including its violations on topologically nontrivial regions (a *positive* requirement — the sector story needs the violations) | open; desk-checkable per candidate |
| 5 | Covariance: the GV-metered flow acts geometrically on the net (ties to B2's tick–fold computation) | open |

The reduction is real: before today, V.7 was "is the geometry's algebra the right kind of object *and* arranged the right way"; condition (1)'s discharge removes the first half by theorem. What remains is an *arrangement* problem — build one candidate net inside the Anosov foliation algebra (the A2 free-field embedding is the natural first attempt, now with a concrete target space). Honest boundary: abstract isomorphism of building blocks carries **no physics by itself** — every pair of reasonable QFTs shares the same local factor without being the same theory. The physics is all in rows 2–5. Stated plainly so the headline of §1 cannot be oversold.

## 4. D — the uniqueness argument (fold as THE activator), written

E1 established that intrinsic time does not need the fold: type III — indeed the same hyperfinite III₁ factor — arises from GV = 0 structures too. The framework's defensible claim, now stated as the record's official position [interpretation, tagged]:

> **Time exists without the fold; a geometric clock does not.** Any type III structure has a canonical outer dynamics (L2), but it is *anonymous* — no geometric datum meters it, nothing ties its parametrization to the underlying space. A GV ≠ 0 fold is precisely the structure for which the clock acquires a geometric meter: the Connes pairing GV = i_H[Ẋ] (audited verbatim, phase 39) makes the invariant *the coupling between the intrinsic dynamics and the transverse geometry*. Without the fold there is a clock but no dial; with it, geometry reads the clock — and only then can "geometry fixes physics" be a falsifiable claim rather than a slogan. The fold is not necessary for time; it is necessary for *time that geometry can measure* — and a framework whose emergent time had no geometric handle would be unfalsifiable by construction.

This also absorbs C1's correction gracefully: on the III₁ carrier the flow of weights (the old, retired "which flow" answer) is trivial, so the pairing is not merely the *better* formulation of Plank IV — it is the *only* nonvacuous one.

## 5. Ledger effects

- Phase 39's open question (factoriality/III₁): **resolved by substitution** for the adopted carrier; remains open for S³ foliations, no longer load-bearing.
- Phase 32 §5.4 homogeneity and the III₁-refinements of L2/B3: **unconditional on the new carrier**.
- New critical-path items: **A2** (free-field net inside W*(T¹Σ_g, F_ws)) and **B3b** (roots-of-unity center vs. superselection structure), joining B2/B1.
- Outreach note: the §1 assembly is six citations and one paragraph — the single most communicable result the program owns, and the natural opening of any expert letter.

*Status line: Tier 3's cheap moves all paid. One theorem-level identification gained (the carrier's algebra IS the lab's algebra), one conditional discreteness structure surfaced (the quantized scale), V.7 halved, and the activator argument written. The critical path is now: B2/B1 (the scale computations) and A2 (one candidate net), with B3b as the wildcard that could make the framework parameter-discrete.*
