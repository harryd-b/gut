# Referee report — MASS-1 structural tests (phase110-MASS1-structural-tests.md)

**Date:** 2026-07-26
**Referee:** context-free adversarial agent (independent verification of the Dehn-twist argument; web verification of all literature attributions; line-by-line audit of dictionary reads and kill readings).
**Editorial note (operator):** Preserved VERBATIM below. Verdicts: (a) CONFIRMED, (b) CONFIRMED with [BOX-1] → CONFIRMED WITH REPAIRS, (c) CONFIRMED (sweep exhaustive), (d) PARTIAL — the tight-knot mutual-exclusivity claim must be re-scoped. [GAP-1] CLOSED (all five attributions verified). Corrections entered as C-T1..C-T5 in the phase file's Amendment.

---

## REPORT (VERBATIM)

All checks are complete. Final referee report follows.

---

# REFEREE REPORT — phase110 MASS-1 structural tests (context-free adversarial pass, 2026-07-26)

I attempted to refute every load-bearing step. Findings below; per-mandate verdicts, literature table, and verdict box at the end.

## (A) Attack on [BOX-1] — the Dehn-twist infinitude argument (§b2)

**Result: the argument is CORRECT in substance. Two genuine gaps found, both repairable; repairs supplied. Upgrade to CONFIRMED WITH REPAIRS.**

**(i) Existence of separating d with i(c,d) > 0 — fact TRUE, note's justification INADEQUATE.** The parenthetical "e.g. the genus-splitting curve crossed twice" does not work as stated: the standard genus-splitting curve can be isotoped disjoint from a given nonseparating c whenever c lies in one of the two pieces, and the note gives no argument that a crossing arrangement exists. The fact is nevertheless true for every nonseparating simple closed curve c on closed orientable X of genus g ≥ 2. Repair (two steps): (1) By the change-of-coordinates principle, the mapping class group acts transitively on nonseparating simple closed curves and homeomorphisms preserve both "separating" and i(·,·); so it suffices to treat one standard c. (2) Take c = γ₂ in the standard chain γ₁,…,γ₂g₊₁ (i(γⱼ,γⱼ₊₁) = 1, else 0). Let s = ∂N(γ₄ ∪ γ₅): a separating essential curve (bounds a one-holed torus; essential since g ≥ 2), with i(s, γ₂) = 0 but i(s, γ₃) ≥ 2 (γ₃ cannot be isotoped into either complementary piece: inside would force i(γ₃,γ₂) = 0, outside would force i(γ₃,γ₄) = 0). Now d := T_{γ₃}(s) is separating (homeomorphic image of a separating curve) and, by the same FLP inequality the note uses, i(d, γ₂) ≥ i(s,γ₃)·i(γ₃,γ₂) − i(s,γ₂) ≥ 2 > 0. Note g ≥ 2 is genuinely needed (a torus has no essential separating curves); the note correctly restricts to g ≥ 2.

**(ii) Twist–intersection inequality — CORRECTLY STATED AND APPLIED.** The FLP form (Exposé 4 appendix; restated as Farb–Margalit, *Primer*, Prop. 3.4) is the two-sided estimate |i(T_d^k(a), b) − |k|·i(d,a)·i(d,b)| ≤ i(a,b); the note's one-sided i(T_d^k(a),b) ≥ |k|·i(a,d)·i(b,d) − i(a,b) is the weaker half — fine. Specialization a = b = c: i(c,c) = 0 is correct (geometric intersection of an isotopy class with itself is defined via distinct representatives in minimal position; a simple class has disjoint representatives). So i(T_d^k(c), c) ≥ |k|·i(c,d)² > 0 for k ≠ 0. In fact FLP gives *equality* here: i(T_d^k(c), c) = |k|·i(c,d)² — the note's claim is strictly weaker than what the source provides. No error.

**(iii) Pairwise non-isotopy — GAP, trivially repaired.** The displayed inequality only shows T_d^k(c) ≄ c for k ≠ 0. Pairwise distinctness needs one more line: i is a mapping-class invariant, so for j ≠ k, i(T_d^k(c), T_d^j(c)) = i(T_d^{−j}T_d^k(c), c) = i(T_d^{k−j}(c), c) = |k−j|·i(c,d)² > 0, hence non-isotopic. The note's "pairwise non-isotopic by the standard intersection-growth inequality" asserts the right conclusion but the written derivation covers only the j = 0 case. Repair adopted.

**(iv) Simplicity and homology class — CORRECT.** T_d^k is a homeomorphism, so T_d^k(c) is simple and essential. T_d acts on H₁ by the transvection x ↦ x + ⟨x,[d]⟩[d]; since d is separating, [d] = 0, so the action is the identity and [T_d^k(c)] = h exactly as claimed.

**(v) Geodesic representatives and unboundedness — CORRECT.** Distinct isotopy classes of essential simple closed curves are distinct free homotopy classes (isotopy ⟺ free homotopy for essential simple closed curves on surfaces — Epstein's theorem; *Primer* Prop. 1.10); each free homotopy class on a closed hyperbolic surface has a unique geodesic representative; and the geodesic representative of a simple class is itself simple (standard: geodesic representatives realize minimal self-intersection; *Primer* §1.2.4). Since i(T_d^k(c), T_d^j(c)) > 0, the geodesics are distinct even as point-sets. Infinitely many distinct closed geodesics plus properness of the length function (only finitely many closed geodesics below any length bound on a closed hyperbolic surface) forces unbounded lengths. All steps verified; simple ⇒ primitive also holds (a proper power traverses its curve multiply; its parametrization is non-injective), so the family consists of admissible primitive carriers under clause (s).

**Verdict A: [BOX-1] → CONFIRMED WITH REPAIRS** (repairs (i) and (iii) above must be entered in the amendment; nothing load-bearing fails).

## (B) Literature verification ([GAP-1]) — all web-checked

| # | Attribution | Verdict |
|---|---|---|
| 1 | Phillips–Sarnak, "Geodesics in homology classes," Duke Math. J. 55 (1987) 287–297 | **VERIFIED.** Exists; proves N(t;m) ~ C·e^{ht}/t^{r/2+1}-type asymptotics per fixed homology class m on constant-negative-curvature manifolds (r = rank H₁). Infinitude + unboundedness per class follows. Note's "~c·e^L/L^{g+1}" is the right shape for surfaces. |
| 2 | Katsuda–Sunada, Amer. J. Math. 110 (1988) | **VERIFIED with page correction:** "Homology and closed geodesics in a compact Riemann surface," Amer. J. Math. 110 (1988) 145–156. Same subject, ✓. |
| 3 | FLP, *Travaux de Thurston sur les surfaces*, Astérisque 66–67 (1979), Exposé 4, for the twist–intersection inequality | **VERIFIED.** The two-sided inequality \|i(t_α^k(β),γ) − \|k\|·i(α,β)i(α,γ)\| ≤ i(β,γ) and the equality i(t_α^k(β),β) = \|k\|·i(α,β)² are FLP results (Exposé 4, appendix); restated as *Primer* Prop. 3.2/3.4 with FLP attribution. The note's one-sided form follows. |
| 4 | Mirzakhani, polynomial growth ~L^{6g−6} of simple closed geodesics | **VERIFIED:** "Growth of the number of simple closed geodesics on hyperbolic surfaces," Ann. of Math. 168 (2008) 97–125; s_X(L) asymptotic to a degree-(6g−6) polynomial. The note should cite this paper explicitly. |
| 5 | "Simple closed curve ⇒ nonseparating with primitive class, or separating with zero class"; "simple closed geodesic ⇒ primitive" | **VERIFIED (standard).** Separating ⟺ null-homologous (*Primer* §1.3.1); a nonseparating scc admits a dual curve meeting it once, so its class pairs to ±1 with something and is primitive (*Primer* Prop. 6.2 / change of coordinates). Simple ⇒ primitive: a proper power's parametrization is m-to-1, not injective. |

One unverified-in-passing item the note leans on at §(d)(ii): length-spectrum multiplicities exist — this is Horowitz/Randol (multiplicity is in fact unbounded on every hyperbolic surface); recommend adding the citation when the amendment is written.

## (C) Dictionary reads — CONFIRMED

- **E3:** synthesis row E3 reads "D_spin = ∓Q²/2 + nQ²/2 (D-MS); parity (−1)^q" — no ℓ anywhere. Note's read correct.
- **E7:** Box 4 of phase105-entry7 reads verbatim "D̄₁₂ = ⟨Q₁[c₁], Q₂[c₂]⟩" and "the entry is *homologically blind* — homologous classes are indistinguishable"; Amendment A.1 confirms descent ("The homological descent … is CONFIRMED"). Quotes accurate, including the C-L4 caveat (unsigned self-intersection accessible as crossing-cosets/2) — and the note is right that unsigned counts are not class-blind, an honest limitation of the theorem's "indistinguishable" claim which the note itself flags.
- **E2:** phase105-D12 line: "the diagonal entry is **metric** (carries the length ℓ) while the off-diagonal entry is **topological** (no length) … not one quadratic form." Note's read correct.
- **E4:** synthesis row "ΔD = Q₁Q₂ℓ/π"; interlock "E4's binding is the polarization of E1's quadratic form on a single axis." Arithmetic checks: ((Q₁+Q₂)²−Q₁²−Q₂²)ℓ/2π = Q₁Q₂ℓ/π ✓. Single-axis read correct.
- **Exhaustiveness of the §(c) sweep:** the note names E2, E4, E6, E7. E1 and E3 are single-carrier; E5 is refereed as "same axis, reflected side" (no second length) and its L-MIRROR law acts on E2's topological entries. Amendments checked: entry7 A.3 (C-L4 — length-free), phase107 A.6 (C-BRIDGE — single carrier, D = n²ℓ/2π), phase108 (E1's state-level status — single carrier). **No length-carrying cross-axis term exists anywhere in the refereed record.** The no-go's search is exhaustive; the sweep should say explicitly that E3/E5 were inspected and are single-axis, but nothing is missed.

## (D) Logic of §(d)

**(i) M ≠ f(D) — CONFIRMED.** (n=1, ℓ): D = ℓ/2π. (n=2, ℓ/4): D = 4·(ℓ/4)/2π = ℓ/2π. Equal D, unequal ℓ, so any strictly monotone M(ℓ) separates what f(D) cannot; and f(Q²ℓ/2π) at fixed ℓ varies with Q, contradicting MASS-1(a)'s registered "independence from the charge data." Both horns correct. Corollary correct: Q = 0 ⇒ D = 0 (and by phase-108, Q = 0 profiles are in the erasure orbit), so no state-level ℓ exists for neutral defects; consistent with C-BRIDGE's n ≥ 1.

**(ii) Tight-knot mutual exclusivity — PARTIAL: honest conditionality present, but the headline is overstated in one respect.** The note does conditionalize ("if a future refereed dynamical entry made carriers energy-minimizing ('tight'), ℓ would become a function of the charge/topology data and K-MASS-1 would fire") before the bolded "mutually exclusive" sentence — no slide into asserting present incompatibility; the registration's §5 verification of V–K/Buniy–Kephart is correctly reused. The overstatement: K-MASS-1 as registered fires only if ℓ becomes a function of *charge/homology* data. Tightness locks ℓ to the full topological type of the carrier; under KNOT-Q many knot types share a genus/charge, so a general tight-knot mechanism does *not* by itself force ℓ = f(Q,h) — generations could survive as distinct knot types of equal charge with distinct tight lengths. The claim is correct *within this program's registered state space* (where carrier data is (D, Q, class, framing) and minimization at fixed registered data selects a unique length), and that is the sense in which the note argues it; but the amendment should scope the exclusivity claim to "energy minimization over the registered invariants," not to V–K-type mechanisms in general. The quadratic-vs-|Q|^{3/4} scaling contrast is arithmetically correct and fairly used.

**(iii) δ^m conflation — CONFIRMED.** Synthesis §1 indexes the arena by hyperbolic elements γ with translation length ℓ, with no primitivity restriction on E1; δ^m is hyperbolic with translation length mℓ₀, so D(Q,δ^m) = Q²·mℓ₀/2π as recorded — numerically identical to a primitive carrier of length mℓ₀. E3 sees (Q,n); E7 sees m[c_δ], and non-primitive classes do contain primitive geodesics (Phillips–Sarnak counts per class are dominated by primitives), so class data cannot certify primitivity. "Simple ⇒ no wound configurations" is right: a simple closed geodesic is primitive, so under C-BRIDGE + (s) no admissible carrier is a proper power. [GAP-4] and both repairs are stated accurately; the observation that this genuinely favors clause (s) is fair.

Minor wording flag (Test 3, §b): "mostowesque rigidity" is a misnomer — dimension 2 has no Mostow rigidity; the correct (and sufficient) statement is simply that a *fixed* hyperbolic structure has a fixed length spectrum, functions of the 6g−6 moduli. The GAP-6 content survives; the word should go.

## (E) Kill readings

**K-MASS-1:** note's restatement ("MASS-1 dies if ℓ is forced to be a function of the charge/homology data on admissible carriers") matches the registered wording verbatim. The test performed — exhibiting infinitely many admissible lengths at fixed (Q,h), with and without clause (s) — is the correct way to show no such forcing is consistent with the record. No drift. **K-MASS-2:** registered wording "inconsistent with any monotone M(ℓ) assignment" is ambiguous in English; the note reads it as "inconsistent with *every* monotone M," which is the only reading under which the kill is nonvacuous (some inconsistent M always exists). Reading endorsed, but the amendment should record the disambiguation. The three-futures analysis is faithful and exhaustive (derived-and-consistent / derived-and-inconsistent / never-derived), and future (iii)'s zero-mass-defect prediction is correctly framed as a named blank pending calibration, not a present refutation. The note also correctly quotes registration §3's binding-energy exposure sentence.

---

## VERDICT BOX

| Claim | Verdict |
|---|---|
| (a) Generations toy theorem | **CONFIRMED** as scoped (items 1–4 are correct reads of refereed formulas; caveats i–iv honest; infinitude now literature-verified) |
| (b) K-MASS-1 does not fire | **CONFIRMED**, with [BOX-1] upgraded to CONFIRMED WITH REPAIRS (repairs A(i), A(iii)); (b1) class censorship and (b3) sterile zero-class both correct |
| (c) Binding-energy no-go | **CONFIRMED**; the sweep is exhaustive over E1–E7 and all amendments |
| (d) M(ℓ) constraints | **PARTIAL**: (i), (iv), (v) confirmed; (ii) fine; (iii) mutual-exclusivity must be re-scoped to energy-minimization over the registered invariants (correct program-internally, overstated as a claim about tight-knot mechanisms generally) |

**May enter the MASS-1 registration as refereed:** the toy theorem (a); the K-MASS-1 non-firing verdict (b) including the clause-(s) analysis; the additivity no-go (c) with its three-futures K-MASS-2 analysis; (d)(i) and (d)(iv). **[BOX-1]: CONFIRMED WITH REPAIRS** — no longer boxed once repairs A(i) (existence of d via change of coordinates + twisted separating curve) and A(iii) (pairwise distinctness via MCG-invariance of i) are entered. **[GAP-1]: CLOSED** — all five attributions verified (Katsuda–Sunada pages 145–156; Mirzakhani = Ann. of Math. 168 (2008) 97–125; add Horowitz/Randol for length-spectrum multiplicity). **Stays boxed/flagged:** the (d)(iii) exclusivity claim until re-scoped; the "mostowesque" wording in Test 3; [GAP-3] (overshoot), [GAP-5]–[GAP-7] stand as recorded and are honestly labeled.

Sources: [Phillips–Sarnak, Project Euclid](https://projecteuclid.org/euclid.dmj/1077306021) · [Katsuda–Sunada context, Lalley Duke 58](https://galton.uchicago.edu/~lalley/Papers/homology.pdf) · [FLP, Thurston's Work on Surfaces (Kim–Margalit translation)](https://books.google.com/books/about/Thurston_s_Work_on_Surfaces_MN_48.html?id=qHZ2BQAAQBAJ) · [Mirzakhani, Ann. of Math. 168 (2008)](https://annals.math.princeton.edu/2008/168-1/p03) · [Farb–Margalit, A Primer on Mapping Class Groups](https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf)
