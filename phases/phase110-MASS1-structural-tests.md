# Phase 110: MASS-1 structural tests — generations theorem, K-MASS-1, binding no-go, M(ℓ) constraints

**Date:** 2026-07-26
**Status:** DRAFTED — awaiting referee. No verdict entered in the MASS-1 registration (phases/phase106-MASS1-conjecture.md) until the referee pass completes.
**Provenance:** Context-free derivation agent executing the four registered MASS-1 test mandates. The consultation below is preserved VERBATIM per house rules. Nothing has been edited.

**Editorial header (operator):**
- Mandates, from the registration: (a) generations toy theorem; (b) K-MASS-1 independence test (including the KNOT-Q clause-(s) interaction); (c) binding-energy carrier search with honest no-go permitted; (d) constraints on the functional form M(ℓ).
- Headline claims (UNREFEREED until the referee verdict is entered as an amendment): toy theorem PROVED at intended level; K-MASS-1 does NOT fire (subject to [BOX-1], the Dehn-twist infinitude argument — the note's only load-bearing new geometry); binding-energy no-go CONFIRMED (composite masses exactly additive within E1–E7; feeds K-MASS-2); mass cannot be a function of D alone — it needs the pair (D, Q); MASS-1 and the tight-knot mass mechanism (Vakulenko–Kapitanskii / Buniy–Kephart) are argued mutually exclusive; winding multiplicity is invisible to state-level invariants unless clause (s) is adopted ([GAP-4] — a genuine point in favor of the simplicity restriction).
- [GAP-1] is a cluster of confident-but-unverified external attributions (Phillips–Sarnak, Katsuda–Sunada, FLP, Mirzakhani, simple⇒primitive-or-zero). The referee is instructed to verify these against the literature; the record requires verified citations before adoption.
- The referee is instructed to attack [BOX-1] hardest: it is the only new mathematics in the note.

---

## CONSULTATION (VERBATIM)

# MASS-1 structural derivation note: generations toy theorem, K-MASS-1 test, binding-energy no-go, and constraints on M(ℓ)

*Context-free derivation agent, 2026-07-26. Status: [derived; NOT refereed; no verdict entered]. Inputs: the refereed dictionary E1–E7 (phases/phase106-synthesis-dictionary.md), E7 with Amendment (phases/phase105-entry7-class-crossing.md), E2 (phases/phase105-D12-cross-invariant.md), C-BRIDGE and clause (s) (phases/phase107-KNOTQ-round2-bridge-definition.md), the MASS-1 registration (phases/phase106-MASS1-conjecture.md).*

**Summary of verdicts.** **(a)** The generations toy theorem is PROVED at the intended level: distinct primitive closed geodesics in a common homology class carry identical charge, spin/statistics, and class-pairing data (by E7's refereed homological blindness) while E1's D = Q²ℓ/2π separates them through ℓ; infinitude of the family is standard geometry [others']. Two honest caveats: the unsigned crossing counts made accessible by C-L4 are NOT class-blind, and the theorem overshoots — it predicts infinitely many generations with no truncation [GAP-3]. **(b)** K-MASS-1 DOES NOT FIRE: on a fixed closed hyperbolic surface a fixed (homology class, charge) pair realizes an infinite, unbounded set of lengths, and this survives the KNOT-Q simplicity clause (s) for primitive nonzero classes — but (s) empties every non-primitive nonzero class of carriers, and rigidity means lengths are selected from a fixed countable menu, never tuned; both restrictions are recorded, not papered over. **(c)** The binding-energy no-go is CONFIRMED: no refereed structure couples the lengths of different geodesics; within the dictionary, MASS-1 composite masses are exactly additive; K-MASS-2's demand is spelled out. **(d)** M cannot be a function of D alone (mass–charge degeneracy); M(ℓ) is equivalent to M(2πD/Q²) on charged carriers, so mass needs the invariant PAIR (D,Q); monotonicity and normalization are unforced by anything recorded; the Vakulenko–Kapitanskii/tight-knot analogy is identified as precisely the K-MASS-1-violating scenario; and E1's numbers conflate an m-fold traversal with a primitive geodesic of length mℓ — repaired only if clause (s) (or an explicit primitivity restriction) is adopted [GAP-4].

---

## §(a) Generations toy theorem

**Setting.** X = Γ\ℍ a closed hyperbolic surface, genus g ≥ 2, Γ ⊂ PSL(2,ℝ) cocompact torsion-free. Carriers: primitive closed geodesics c with charge Q ∈ ℤ∖{0} (C-BRIDGE normalization Q = ±n; the theorem below does not need C-BRIDGE, only a fixed charge assignment).

**Theorem (toy).** Let c, c′ be distinct primitive closed geodesics on X with [c] = [c′] = h ∈ H₁(X;ℤ), carrying equal charge Q and equal framing datum n. Then:

1. **(Charge)** equal by hypothesis; charge is a label of the defect profile (E1), containing no ℓ.
2. **(Spin/statistics)** equal: E3's refereed entry D_spin = ∓Q²/2 + nQ²/2 and parity (−1)^q are functions of (Q, n, chirality branch) only — ℓ does not appear in the formula (dictionary row E3, phases/phase106-synthesis-dictionary.md §2). So equal (Q, n) forces equal spin, statistics, and parity.
3. **(Class pairing)** equal against everything: for any third carrier (Q₃, [c₃]), the refereed E7 entry gives D̄ = Q Q₃⟨[c],[c₃]⟩ = Q Q₃⟨[c′],[c₃]⟩ since [c] = [c′]. The exact refereed clause: "**D̄₁₂ = ⟨Q₁[c₁], Q₂[c₂]⟩** … the entry is *homologically blind* — homologous classes are indistinguishable" (phase105-entry7-class-crossing.md, Box 4 and §7 Honest limits (2); descent CONFIRMED in Amendment A.1).
4. **(Separation)** E1's refereed invariant D = Q²ℓ/2π satisfies D(c) ≠ D(c′) whenever ℓ(c) ≠ ℓ(c′) (automatic for distinct primitive geodesics of distinct lengths; geodesics of equal length are separated by nothing in the record — see caveat (ii) below). By the phase-108 JOIN-4a″ theorem, D is a state-level, locally un-erasable invariant (synthesis §4, B1), so the separation is physical, not bookkeeping. ∎

Proof content: items 1–3 are direct reads of refereed formulas; item 4 is E1 plus injectivity of ℓ ↦ Q²ℓ/2π at fixed Q ≠ 0. No new mathematics.

**Infinitude of the family.** Each nonzero class h ∈ H₁(X;ℤ) contains infinitely many primitive closed geodesics with lengths → ∞. [others': this follows from the counting asymptotics for closed geodesics in a fixed homology class — Phillips–Sarnak, "Geodesics in homology classes," Duke Math. J. 55 (1987), and Katsuda–Sunada, Amer. J. Math. 110 (1988), which give ~ c·e^L/L^{g+1}-type growth per class on a closed hyperbolic surface. I am confident of these attributions but they have NOT been run through the record's literature-verification protocol; flagged as GAP-1 rather than asserted as verified.] Lengths → ∞ then follows because only finitely many closed geodesics exist below any length bound (discreteness of the length spectrum [others', standard]).

**What the theorem does NOT establish.** (i) Nothing about mass: the mass column is empty; MASS-1 is an unrefereed registration. The theorem says the refereed formalism *contains* families with identical registered quantum numbers and distinct ℓ — it does not say ℓ is mass. (ii) "Identical interaction data" holds exactly at the level of the REGISTERED entries (the signed homological pairing). The referee's C-L4 addendum makes the UNSIGNED self-intersection count accessible as (crossing cosets)/2 (entry7 Amendment A.3), and unsigned counts generally differ between homologous geodesics. So c and c′ are indistinguishable relative to the signed dictionary, not relative to everything the formalism could measure. This is a real soft spot of MASS-1(b)'s "identical quantum numbers" phrasing and is recorded. (iii) No dynamics: generations here are a label family; no mixing, decay, or transition exists anywhere in the record (blocked by the phase-103/104 kills). (iv) **Overshoot:** the same infinitude that supplies generations supplies infinitely many of them, masses unbounded under any monotone M with M(ℓ) → sup. Nothing recorded truncates the family to three. [GAP-3] This is a standing tension of MASS-1(b), not currently a kill (the registration conjectures a mechanism, not a count).

---

## §(b) K-MASS-1 independence test

**The kill:** MASS-1 dies if ℓ is forced to be a function of the charge/homology data on admissible carriers.

**Test 1 — fixed class, fixed charge, unrestricted primitive carriers.** By §(a)'s infinitude, the set {ℓ(c) : c primitive, [c] = h} is infinite and unbounded for every h ≠ 0 [others', GAP-1]. So ℓ is not a function of (Q, h): the same data pair sits over infinitely many lengths. **Kill does not fire.**

**Test 2 — under KNOT-Q clause (s) (charge only over SIMPLE closed geodesics; phase107 §7, refereed as nonvacuous; C-BRIDGE A.6).** Simplicity is a genuine constraint and changes the carrier census in two ways:

*(b1) Class censorship.* A simple closed curve on a closed orientable surface is either nonseparating, representing a PRIMITIVE class of H₁(X;ℤ), or separating, representing 0 [others', standard surface topology]. Hence under (s), **every non-primitive nonzero class (e.g. 2h) contains NO admissible carrier at all.** The carrier lattice over homology is censored to {primitive classes} ∪ {0}. This is a real structural restriction MASS-1 inherits from C-BRIDGE and must carry; recorded, not papered over.

*(b2) Infinitude survives for primitive classes.* Claim: for h primitive and g ≥ 2, the set of SIMPLE closed geodesics on the fixed surface X in class h is infinite with unbounded lengths. Argument shape [BOX-1]: pick a simple nonseparating curve c with [c] = h [others': every primitive class is so represented]; pick a separating simple closed curve d with geometric intersection i(c,d) > 0 (exists for g ≥ 2, e.g. the genus-splitting curve crossed twice). The Dehn twist T_d acts trivially on H₁ (since [d] = 0), so [T_d^k(c)] = h for all k; the curves T_d^k(c) are simple; and they are pairwise non-isotopic by the standard intersection-growth inequality i(T_d^k(c), c) ≥ |k|·i(c,d)² − i(c,c) = |k|·i(c,d)² > 0 for k ≠ 0 [others': Fathi–Laudenbach–Poénaru, Travaux de Thurston, Exposé 4 — attribution confident but unverified, folded into GAP-1]. Distinct isotopy classes have distinct geodesic representatives (uniqueness of the geodesic in a free homotopy class), all simple, all in class h; lengths are unbounded because only finitely many closed geodesics lie under any length bound. [BOX-1: the inequality use and the existence of d are standard but not formalized here; a referee should check the i(c,d) > 0 arrangement.] Note simplicity fails to KILL the mechanism, contrary to the worry that simple geodesics per class can be finite on a fixed surface — the twist family shows infinitude; what IS true is that simple geodesics are far sparser (polynomial ~L^{6g−6} overall growth [others': Mirzakhani; unverified, GAP-1]) and class-censored per (b1). Honest residue: this claim is the load-bearing new geometry input of this note and gets [BOX-1] status until checked.

*(b3) The zero class.* Separating simple geodesics carry charge under (s) but lie in class 0: E7 pairs them to zero against EVERYTHING (Box 4). A generations family in class 0 would be interaction-invisible at class level. Whether such "sterile" carriers are physical or artifacts is undetermined [GAP-7].

**Test 3 — cross-class correlation.** Can two distinct classes force correlated lengths? No refereed structure relates ℓ(c₁) to ℓ(c₂): E2 and E7 (the only cross-axis entries) are length-free; E4 lives on one axis. So no recorded correlation exists. But one honest structural fact: on a FIXED surface, mostowesque rigidity of the hyperbolic structure means ALL lengths in ALL classes are simultaneously determined by the point in moduli space. Lengths are selected from a rigid countable menu, never independently tuned. Consequence: if MASS-1 ever reaches calibration, every generation mass ratio in every family is a fixed function of (6g−6) moduli — massively over-constrained relative to observed spectra unless the surface is chosen to fit, which would be numerology. Recorded as GAP-6 (a future exposure, not a present kill).

**Verdict (b): K-MASS-1 does not fire.** ℓ varies over an infinite unbounded set at fixed (Q, h), with or without clause (s) — subject to [BOX-1] — but (s) censors non-primitive classes (b1), creates a sterile zero-class sector (b3), and rigidity converts "independent dial" into "independent menu selection" (Test 3).

---

## §(c) Binding-energy carrier gap

**Search of the record for a length-carrying cross-axis coupling.**

- **E2** (phase105-D12-cross-invariant.md, Task 3): D₁₂ = Q₁Q₂·î(γ₁,γ₂) with î ∈ {0,±1}. The file states it explicitly: the off-diagonal entry is "**topological** (no length)" — the sanity-check note contrasts it with the metric diagonal and rules that the two are "not one quadratic form." **î carries no length.**
- **E7**: D̄₁₂ = Q₁Q₂⟨[c₁],[c₂]⟩ — homological only (Box 4); by construction blind even to geometry within a class, a fortiori to length.
- **E6** (joint arena): the cross-term recovered internally is the central-extension class of the implementer lines, equal to D₁₂ — topological again (synthesis §2 interlocks).
- **E4** (fusion): ΔD = Q₁Q₂ℓ/π carries a length — but ONE length: it is the polarization of E1's quadratic form on a SINGLE axis (synthesis interlocks; both charges ride the same geodesic). It couples charges, not lengths of different carriers. Fusion in E1/E4 is totals-only.

No other entry exists (the dictionary is complete as planned, entry7 Amendment A.5). **No refereed structure couples ℓ₁ to ℓ₂.**

**No-go (stated as the finding):** *Within the refereed dictionary, any mass assignment M(ℓ) per carrier yields exactly additive composite masses M(ℓ₁) + M(ℓ₂) for two-carrier systems; binding energy (composite mass defect) has no carrier.* This sharpens the exposure already named in the registration §3 ("binding energy … has no carrier in the current dictionary") from an observation into a checked no-go: the search above is exhaustive over E1–E7.

**What K-MASS-2 now demands.** K-MASS-2 (registration §4) fires only if a refereed length-carrying cross-axis coupling IS someday derived AND its induced composite-mass correction is inconsistent with every monotone M(ℓ). The present no-go therefore leaves exactly three futures: (i) a new refereed entry — a length-carrying analogue of D₁₂ — is derived and is consistent with some monotone M: MASS-1 survives and gains binding; (ii) such an entry is derived and is inconsistent: K-MASS-2 fires, MASS-1 dies; (iii) no such entry ever exists: MASS-1 survives K-MASS-2 vacuously but then PREDICTS zero mass defect for all composites — a statement that contradicts basic phenomenology the moment any calibration column exists. Since the calibration column is currently empty (synthesis §4), (iii) is today a named blank, not a refutation — but it must be listed as MASS-1's sharpest falsifiable consequence. **No coupling is invented here; the gap is the deliverable.** [GAP-5]

---

## §(d) Constraints on the functional form M(ℓ)

**(i) M is not a function of D alone.** Suppose mass is a function of refereed state-level invariants. For a charged carrier the state-level data are (D, Q) (plus framing and class, which carry no length). Since ℓ = 2πD/Q² for Q ≠ 0, the registered M(ℓ) IS a function of refereed invariants — but of the PAIR (D, Q), through the ratio D/Q², never of D alone. If one demanded M = f(D), then under C-BRIDGE (Q = ±n, D = n²ℓ/2π) the carriers (n = 1, ℓ) and (n = 2, ℓ/4) would be exactly degenerate in mass while differing in charge — and, worse, within a fixed generation family (fixed Q, varying ℓ) f(D) works, but across charges mass would be forced to depend on Q, contradicting MASS-1(a)'s registered charge-independence. **Flagged tension: "mass = function of the existence cost D" is inconsistent with MASS-1 as registered; MASS-1 requires mass to read ℓ = 2πD/Q², discarding the Q² factor.** Corollary: neutral defects (Q = 0, D = 0) have no state-level ℓ and hence no MASS-1 mass — carriers must be charged, consistent with C-BRIDGE's Q = ±n, n ≥ 1.

**(ii) Monotonicity.** Nothing recorded forces it; nothing forbids it. What the record does force: DISCRETENESS of the mass spectrum (countable rigid length spectrum [others', standard]) and, under any strictly monotone M, injectivity of mass on each generation family up to length-spectrum multiplicity (geodesics of equal length — which exist, the length spectrum has multiplicities [others'] — get equal mass; nothing in the record separates them; minor conflation, recorded). Monotonicity remains pure registration, killable only by K-MASS-3.

**(iii) Vakulenko–Kapitanskii caution (registration §5, verified there).** In knot-soliton models E ≳ c|Q|^{3/4}: energy grows SUBLINEARLY in charge because the minimizer's geometry adjusts to the charge. Two consequences here. First, D = Q²ℓ/2π grows QUADRATICALLY in charge at fixed carrier — if anyone reads D as an energy/mass, the scaling is maximally unlike the knot-energy benchmark; a further strike against M = f(D), independent of (i). Second and sharper: the V–K/Buniy–Kephart mechanism works precisely because carrier length is DETERMINED by charge topology (tight-knot ropelength ℓ_min = ℓ_min(knot type)). Translated into this program, that is exactly the correlation K-MASS-1 forbids: if a future refereed dynamical entry made carriers energy-minimizing ("tight"), ℓ would become a function of the charge/topology data and **K-MASS-1 would fire**. Recorded: the nearest successful prior art for "mass from knotted-carrier length" lives in the regime where MASS-1 is dead. MASS-1's survival requires carriers whose lengths are NOT selected by charge — i.e., the generations mechanism and the tight-knot mass mechanism are mutually exclusive. This is the note's sharpest structural finding for (d).

**(iv) Iterated traversal vs primitive length.** Let δ be primitive with length ℓ₀ and consider γ = δ^m (translation length mℓ₀). E1 is indexed by hyperbolic elements (synthesis §1) and assigns D(Q, δ^m) = Q²·mℓ₀/2π — numerically IDENTICAL to a primitive carrier of length mℓ₀ with the same Q. E3 sees (Q, n) only. E7 sees the class m[c_δ]; but non-primitive classes also contain primitive geodesics [others', per the class-counting results, GAP-1], so class data cannot certify primitivity either. **Conclusion: no refereed state-level invariant distinguishes an m-fold-wound carrier from a primitive carrier of the same total length, same charge, same class.** M(ℓ) therefore conflates "heavier generation" with "multiply wound same particle" [GAP-4]. Two recorded repairs, neither free: (1) MASS-1(a) already says "primitive closed geodesic" — but primitivity is then carrier bookkeeping imposed by fiat, not read from the state; (2) clause (s) repairs it structurally: a simple closed geodesic is automatically primitive (a proper power traverses its curve multiply and is not simple), so under C-BRIDGE + (s) the admissible carrier set contains no wound configurations at all. This is a genuine point IN FAVOR of the simplicity restriction, counterweighing (b1)'s censorship — recorded as the trade-off it is.

**(v) Normalization.** No recorded structure fixes units, an additive constant, or the value of any M(ℓ); the calibration column is empty (synthesis §4). Any specific functional form would be numerology and none is proposed.

---

## Gaps and boxes ledger

- **[GAP-1]** External attributions asserted with confidence but NOT run through the record's literature-verification protocol: Phillips–Sarnak (Duke 55, 1987) and Katsuda–Sunada (Amer. J. Math. 110, 1988) for infinitude/counting of primitive closed geodesics per homology class; FLP (Travaux de Thurston) for the twist–intersection inequality; Mirzakhani for polynomial simple-geodesic growth; standard surface topology for "simple ⇒ primitive-or-zero class." If any attribution is wrong the FACTS remain standard folklore, but the record requires verified citations before adoption.
- **[BOX-1]** §(b2): infinitude and unboundedness of simple closed geodesics in a fixed primitive class on a fixed surface via separating-curve Dehn twists — argument shape supplied, not formalized; the load-bearing new input of this note; needs referee.
- **[GAP-3]** Generations overshoot: the mechanism yields infinitely many generations per class; no truncation to three exists anywhere in the record.
- **[GAP-4]** Primitivity is not a state-level invariant: (D, Q, class, framing) cannot separate δ^m from a primitive carrier of length mℓ₀; repaired only by fiat restriction or by adopting clause (s).
- **[GAP-5]** Binding-energy carrier absent (the §(c) no-go): within E1–E7, composite masses under MASS-1 are exactly additive; feeds K-MASS-2 as spelled out.
- **[GAP-6]** Mass-ratio rigidity: on a fixed surface all lengths (hence all mass ratios under any M) are determined by the moduli point; future calibration is over-constrained or fitted.
- **[GAP-7]** Zero-class (separating, simple) carriers under (s): charged but E7-invisible against everything; physical status undetermined.
- **[others']** imports beyond GAP-1: countability/rigidity/multiplicity of the length spectrum; unique geodesic per free homotopy class; existence of separating curves meeting a given nonseparating curve (g ≥ 2).
- Refereed inputs used as ground truth (cited in place, not re-derived): E1 (D = Q²ℓ/2π; state-level by phase-108), E2 (î length-free), E3 (no ℓ in D_spin), E4 (same-axis polarization only), E6 (topological cross-term recovery), E7 Box 4 + Amendment (homological descent and blindness; C-L4 unsigned-count accessibility), C-BRIDGE + clause (s) (phase107 §7, A.6 with its mandatory C-M2 disclosure).

**One-line close.** The refereed dictionary genuinely contains the generations pattern (a) and passes its independence kill (b) — subject to [BOX-1] — but it forces exactly additive composite masses (c), forbids mass from being a function of the existence cost D alone, places MASS-1 in structural opposition to the only successful prior mass-from-length mechanism, and cannot see winding multiplicity without the simplicity clause (d): four honest tensions recorded, none fitted away.

---

## Amendment section

Note on the ledger numbering: the agent's [GAP-7] (zero-class sterile carriers) is local to this note and distinct from the program-level GAP-7 in the open registry; disambiguate as MASS-GAP-7 if cross-referenced.

### A.1 Referee verdict (2026-07-26)

Adversarial referee report preserved verbatim in reviews/REPORTS-phase110-MASS1-referee-2026-07-26.md (independent verification of the geometry; web verification of all attributions). Per-mandate verdicts:

- **(a) Generations toy theorem: CONFIRMED** as scoped. All four items are correct reads of refereed formulas; the four honesty caveats stand.
- **(b) K-MASS-1 does not fire: CONFIRMED.** [BOX-1] upgraded to **CONFIRMED WITH REPAIRS** (see A.2). Class censorship (b1) and the sterile zero-class sector (b3) both correct.
- **(c) Binding-energy no-go: CONFIRMED.** The sweep is exhaustive over E1–E7 and all amendments (E3/E5 inspected by the referee and confirmed single-axis). Within the refereed record, composite masses under any M(ℓ) are exactly additive; the three-futures K-MASS-2 analysis is faithful.
- **(d) M(ℓ) constraints: PARTIAL.** (i) M ≠ f(D) CONFIRMED (both horns, plus the neutral-carrier corollary). (iv) δ^m conflation CONFIRMED (E1 is indexed by hyperbolic elements with no primitivity restriction; simple ⇒ primitive so clause (s) repairs it structurally). (v) stands. (iii) re-scoped per C-T3 below.

### A.2 Corrections ledger

- **C-T1 ([BOX-1] repair i).** The "genus-splitting curve crossed twice" justification was inadequate (that curve can be isotoped off c). Repaired: by change of coordinates take c = γ₂ in the standard chain; s = ∂N(γ₄∪γ₅) is separating with i(s,γ₃) ≥ 2; d := T_{γ₃}(s) is separating with i(d,γ₂) ≥ 2 > 0 by the FLP inequality. g ≥ 2 genuinely needed.
- **C-T2 ([BOX-1] repair iii).** Pairwise non-isotopy needs MCG-invariance of i: i(T_d^k(c), T_d^j(c)) = i(T_d^{k−j}(c), c) = |k−j|·i(c,d)² > 0 for j ≠ k (FLP in fact gives equality). The note's displayed inequality covered only j = 0.
- **C-T3 (re-scope of the exclusivity claim, §d iii).** The mutual-exclusivity statement holds for *energy minimization over the registered invariants* (where minimization at fixed (Q, class, framing) selects a unique length, making ℓ a function of registered data — K-MASS-1 fires). It does NOT extend to tight-knot mechanisms in general: tightness locks ℓ to full topological type, and many knot types share a charge, so generations could survive in a general V–K-type model as distinct knot types of equal charge. Corrected statement: **MASS-1 is incompatible with any future dynamical entry that minimizes energy over the program's registered state space; it is not incompatible with tight-knot mechanisms per se.**
- **C-T4 (wording).** "Mostowesque rigidity" struck — dimension 2 has no Mostow rigidity. Correct statement: a fixed hyperbolic structure has a fixed length spectrum, a function of the 6g−6 moduli. GAP-6 content unchanged.
- **C-T5 (kill disambiguation).** K-MASS-2's registered "inconsistent with any monotone M(ℓ)" is read as "inconsistent with EVERY monotone M" — the only nonvacuous reading. Recorded as the binding interpretation.

### A.3 Literature ledger — [GAP-1] CLOSED

All five attributions verified by the referee (web-checked): Phillips–Sarnak, Duke Math. J. 55 (1987) 287–297; Katsuda–Sunada, "Homology and closed geodesics in a compact Riemann surface," Amer. J. Math. 110 (1988) 145–156; FLP, Travaux de Thurston, Astérisque 66–67 (1979), Exposé 4 appendix (also Farb–Margalit, Primer, Prop. 3.2/3.4); Mirzakhani, Ann. of Math. 168 (2008) 97–125; the surface-topology facts standard (Primer §1.3.1, Prop. 6.2). Added: Horowitz/Randol for length-spectrum multiplicity (unbounded on every hyperbolic surface) — supports §(d)(ii)'s multiplicity caveat.

### A.4 Post-verdict status

Refereed and eligible to enter the MASS-1 registration: the generations toy theorem (a); the K-MASS-1 non-firing verdict (b) with the clause-(s) census (censorship to primitive classes ∪ {0}; sterile zero-class sector; infinitude via the repaired Dehn-twist family); the exact-additivity no-go (c) with the three-futures K-MASS-2 analysis; (d)(i) M ≠ f(D); (d)(iv) the δ^m conflation and its clause-(s) repair. Still open/flagged: MASS-GAP-3 (generations overshoot — nothing selects three), MASS-GAP-5 (binding carrier absent — MASS-1's sharpest falsifiable consequence), MASS-GAP-6 (moduli rigidity of mass ratios), MASS-GAP-7 (sterile zero-class carriers).
