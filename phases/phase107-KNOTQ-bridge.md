# Phase 107 — KNOT-Q campaign, round 1: the bridge construction and kill adjudication (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-26, executing the operator's instruction "Kick off KNOT-Q." **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered; the KNOT-Q registration in phases/phase105-SPAN1-knot-charge.md §4 is UNCHANGED until a referee pass].***

*Headline claims (pre-verdict): (1) the registered decoration is broken twice over — Lutz twists along a knot are UNRESTRICTED (no Bennequin constraint exists on twist admissibility: clause (a)'s stated mechanism is a category error) and always produce an OVERTWISTED structure (incompatible with the tight carrier); (2) the repair is forced by tightness itself: the admissible quantized twist data on tight T¹Σ_g is exactly Giroux torsion n ∈ ℤ₊ on vertical tori over essential SIMPLE closed geodesics — the bridge sends this to charge Q = e·n anchored at fix(γ), and the bulk thereby selects the ℤ-quantized lattice boundary net (a pleasing consistency); (3) clause (a)'s CONCLUSION survives under the repaired bridge with a replaced, forced mechanism (locality + tightness, not Bennequin) — the genus-0 kill cannot legitimately fire; (4) the trefoil-minimality clause is adjudicated numerology (likely a leak from Ghys's modular-surface/trefoil correspondence, which lives on the WRONG carrier), and the Arf clause is ill-typed (the statistics parity is torsion parity, not a knot invariant; Arf is undefined for most charged classes); (5) an UNREGISTERED prediction emerges: charge is supported only over SIMPLE closed geodesics; (6) VERDICT: kill INCONCLUSIVE — it fires iff the single missing object resolves to e = 0: whether one unit of Giroux torsion along T_γ acts nontrivially on the boundary net. All of this goes to a context-free referee (with literature access) before any verdict or any amendment to the KNOT-Q registration.*

---

## The derivation, verbatim

# KNOT-Q Bridge Construction and Kill-Condition Adjudication

**Derivation document. Context-free brief; codomain = refereed boundary defect theory (locality theorem, D = Q²ℓ/2π); domain = canonical contact structure ξ on T¹Σ_g, Reeb flow = geodesic flow.**

---

## 1. Preliminary: the naive bridge is vacuous, and clause (a)'s stated mechanism is a category error

The registered conjecture decorates a transverse knot K with "n units of Lutz twist along K" and invokes the Bennequin budget sl(K) ≤ 2g_S(K) − 1 to forbid positive twist at genus 0. Two contact-topology facts, both standard [others'], destroy this reading before any bridge is built:

**(F1)** [others' — Lutz; see Geiges, *Introduction to Contact Topology*, §4.3] Every transverse knot K in any contact 3-manifold has a standard tubular neighborhood, and a (half or full) Lutz twist can be performed in that neighborhood **for every K, with no restriction whatsoever** — no dependence on sl(K), g_S(K), or knot class. The Bennequin inequality constrains the self-linking number of transverse knots *in a tight structure*; it is not, and cannot be converted into, an admissibility condition on Lutz twists. I checked this claim deliberately, as instructed: there is no theorem of the form "positive Lutz twist along K requires sl(K) ≥ bound." Clause (a)'s stated mechanism is a **category error**.

**(F2)** [others'] Any Lutz twist (along any transverse knot, any genus) produces an **overtwisted** contact structure — the Lutz tube contains an overtwisted disk. So the decoration named in KNOT-Q destroys the tightness hypothesis of the carrier *uniformly*, for every knot class.

> **[BOX 1] (Naive bridge no-go.)** Under the literal KNOT-Q decoration (Lutz twist along K), either the carrier's tightness hypothesis is dropped — and then twists are unrestricted at every genus, contradicting (a)'s mechanism — or tightness is retained, and then **no** knot admits **any** positive twist, so the decoration set is empty. The Bennequin budget plays no role in either branch.

This does not yet fire the kill: the second disjunct of the kill ("zero charge to every knot class") presupposes a constructed quantization *assigning* zero, whereas here the literal decoration has empty domain — the quantization is undefined, not zero-valued. The kill **hangs** on the literal reading.

---

## 2. Task 1 — The minimal canonical bridge (repaired decoration)

The repair is dictated by asking: *what quantized twist deformations does the tight carrier actually support?*

**(F3)** [others' — Giroux; Colin, *Une infinité de structures de contact tendues sur les variétés toroïdales* (2001)] Inserting n units of Giroux torsion (layer T² × [0,1], α_n = cos(2πnt)dx − sin(2πnt)dy) along an **incompressible** pre-Lagrangian torus in a universally tight structure yields a universally tight structure; the unit is quantized in ℤ. On T¹Σ_g specifically this produces the known infinite family of universally tight structures. [GAP-1: I import the precise scope of Colin's theorem — incompressible + pre-Lagrangian suffices — from memory of the literature; the application to the specific tori below should be checked against Colin/Massot.]

**(F4)** [others' — Seifert-fibered 3-manifold topology] T¹Σ_g is Seifert fibered over the hyperbolic base Σ_g; every incompressible torus in it is isotopic to a **vertical** torus π⁻¹(c), c an essential *simple* closed curve on Σ_g, uniquely represented by a simple closed geodesic. [GAP-2: standard, but imported.]

**(F5)** Torsion inserted along a *compressible* torus (π⁻¹(c) for c contractible bounds π⁻¹(disk) ≅ D²×S¹) is a Lutz-type twist in a solid torus and yields an overtwisted structure [others'; GAP-3: I believe "positive torsion along a compressible torus ⇒ overtwisted" is standard, but I flag the exact citation as unverified].

So tightness itself classifies the admissible quantized twist data:

> **[BOX 2] (Forced twist locus.)** In the tight carrier (T¹Σ_g, ξ), the admissible quantized twist decorations are exactly Giroux-torsion assignments **n: {essential simple closed geodesics c} → ℤ₊**, localized on the vertical tori T_c = π⁻¹(c). Twists attached to a *knot* K per se are never tightness-compatible (F2). This locus is forced by (F3)–(F5), not chosen.

**The bridge map B.** Given a transverse knot K with free homotopy class of projection [π(K)]:

- If [π(K)] is trivial: no hyperbolic γ, no anchor (refereed locality theorem); B(K, —) = trivial (inner, chargeless) defect.
- If [π(K)] is nontrivial with geodesic representative γ: the tightness-compatible decoration is torsion n along T_γ (defined when γ is simple; see §5 for non-simple classes). B assigns the boundary defect with **anchor fix(γ)** and charge

  **Q = e · n, e ∈ ℤ the charge unit,**

  by the **holonomy principle**: the characteristic foliation of the torsion layer rotates exactly n full turns across the layer (verified symbolically: α_n ∧ dα_n = 2πn·dV, contact iff n ≠ 0; foliation angle = π/2 + 2πnt, net rotation n·2π), and the principle identifies this integer winding with the winding ∫ρ = Q of the U(1) defect automorphism α_ρ.

**Forced/convention ledger** (determines whether the kill can legitimately fire):

- *Forced:* the twist locus (BOX 2); the anchor at fix(γ) (refereed locality theorem); the quantization Q ∈ ℤ **if** the holonomy principle holds — note the satisfying consistency check that the bulk then selects the lattice/compactified boundary extension (Q ∈ ℤ) [others'], not the plain net (Q ∈ ℝ): a continuous charge would have no bulk preimage.
- **[GAP-4] Not forced:** the holonomy principle itself. It is the canonical candidate (integer winding ↦ integer winding, both localized on the same conjugacy class γ), but it is a *postulate*, not derived from a quantization functor. In particular **e ≠ 0 is unproven**: nothing yet shows the torsion insertion acts nontrivially on the boundary net. If e = 0, every charge vanishes.
- *Convention:* overall sign of Q (see §4); normalization e = 1.

---

## 3. Task 2 — The genus-0 clause, honestly

Does a genus-0 transverse knot map to Q ≠ 0 under B? **No — and by two independent forced mechanisms, neither of which is Bennequin:**

1. **Locality.** g_S(K) = 0 means K bounds an embedded disk, hence K is null-homotopic in T¹Σ_g, hence π(K) is contractible in Σ_g. By the refereed locality theorem there is no hyperbolic γ, no fixed-point anchor, and the coupling-visible charge is zero. (Note: no closed Reeb orbit is ever genus-0 — closed geodesics on hyperbolic surfaces are essential — so genus-0 transverse knots are never orbits; they are "spectator" knots.)
2. **Overtwisting.** Any attempt to place twist near a contractible class uses a compressible torus (or a Lutz twist along K itself), which destroys tightness (F2/F5) and with it the carrier hypothesis — there is no tight configuration whose quantization could carry the charge.

> **[BOX 3] (Clause (a): conclusion survives, mechanism replaced.)** Genus-0 ⇒ Q_visible = 0 is **forced** in the bridge B — but by locality + tightness, **not** by the Bennequin budget. The registered mechanism ("the budget −1 admits no positive twist") is refuted (F1): Bennequin constrains sl, never twist admissibility. KNOT-Q's clause (a) is true-as-stated with a false proof attached.

The kill's first disjunct (nonzero charge at genus 0) therefore **cannot fire** against B — and this immunity is legitimate, not fitted: the two mechanisms above ((refereed) locality; (F4)-forced twist locus) were fixed before any charge was assigned.

---

## 4. Task 3 — Clauses (b) and (c)

**(b) Q ≠ 0 at genus ≥ 1: supported (conditionally).** Torsion n = 1 along T_γ for any essential simple closed geodesic is tight-admissible (F3) and B assigns Q = e·1 ≠ 0 *provided e ≠ 0* [GAP-4]. The Reeb orbit over γ is essential, hence (where null-homologous — see below) has g_S ≥ 1, consistent with (b). The induced invariant is bulk-computable: **D = Q²ℓ/2π = e²n²·(Reeb period of the orbit over γ)/2π.**

**(b) Trefoil minimal quantum: numerology.** The minimal quantum n = 1 is realized along *every* essential simple closed geodesic; no knot-theoretic minimality distinguishes any "trefoil class." Moreover "trefoil" is not even canonically defined in T¹Σ_g (it is not S³). The likely origin of this clause is Ghys's modular correspondence (geodesic flow on the *modular* surface ↔ trefoil complement, Lorenz knots) [others'], which concerns the noncompact PSL(2,ℤ)\PSL(2,ℝ), not the compact carrier here. **Unsupported as registered.** [GAP-5: whether a trefoil statement survives in a cusped/orbifold version of the framework is open, not tested here.]

**(c) Chirality ↦ sign(Q): not forced.** Giroux torsion is intrinsically unsigned/nonnegative as an invariant of the unoriented torus T_γ, and T_γ = T_{γ⁻¹} carries *both* Reeb orbits (over γ and γ⁻¹) as positively transverse knots — nothing in the contact data selects one, while fix(γ) = fix(γ⁻¹) as a set with attracting/repelling roles swapped. The layer form α_n is contact for either sign of n (verified: α_n ∧ dα_n = 2πn·dV), but insertion with reversed co-orientation is related by an orientation convention. Conclusion: **|Q| is bridge-defined; sign(Q) requires a convention** (an orientation of Σ_g plus a choice of attracting-vs-repelling anchor labeling). Relative signs of two charges are then meaningful; the map "left-handed ↦ Q < 0" is a convention, not a theorem. Partially structural, not forced. [GAP-6]

**(c) Arf ↦ statistics parity: numerology, and partly ill-typed.** The refereed statistics grading is (−1)^Q = (−1)^{en} — the **parity of the torsion**, an invariant of the twist data, not of the knot. Arf(K) is (i) only defined for null-homologous K, whereas charged Reeb orbits over γ are null-homologous only under a homological condition ([γ] = 0 in H₁(Σ_g) plus a fiber-class condition in H₁(T¹Σ_g), whose fiber summand is ℤ/(2g−2)) — so for most charged classes Arf is not even defined; and (ii) where defined, n is freely choosable independently of K's knot type, so no identity Arf(K) ≡ n (mod 2) can be forced. There is a conceivable bulk ℤ/2 shadow (torsion parity interacts with the homotopy class of the plane field — half-vs-full Lutz twisting [others']), but it attaches to the twist, not to Arf. **Blunt verdict: the Arf clause is numerology at present.** [GAP-7]

---

## 5. An unregistered prediction of the bridge

BOX 2 forces charge to be supported only on **simple** closed geodesics (non-simple classes have no embedded vertical torus, only immersed ones). KNOT-Q says nothing about simplicity. This is a falsifiable divergence between the bridge and the conjecture: either non-simple hyperbolic classes carry charge by some other mechanism (immersed-torus torsion is not a tight-preserving operation in the literature I can invoke), or the boundary theory must show charge is realizable only over simple classes. [GAP-8: genuinely open; a sharp test for the next iteration.]

---

## 6. Task 4 — Verdict on the kill

> **[BOX 4] VERDICT: TEST INCONCLUSIVE — with sharp conditional content.**
>
> - The kill **does not fire and cannot legitimately fire yet**, because the charge assignment Q = e·n rests on the holonomy postulate [GAP-4], which is a canonical *candidate*, not a forced consequence of a quantization. The registration's admission stands: the bridge functor still does not exist.
> - **Sharpened F-GAP (the object that must exist):** a computation of the boundary-net action induced by a single Giroux-torsion insertion along T_γ — i.e., a proof that the torsion-deformed carrier defines a defect sector with e ≠ 0 (equivalently, that the layer's foliation winding is implemented by a noninner automorphism anchored at fix(γ)). **If e ≠ 0: kill dodged and clauses (a) + (b-first-half) verified** (with (a)'s mechanism replaced per BOX 3). **If e = 0 is forced: the kill's second disjunct fires** (zero charge to every knot class).
> - Independently of e, the *registered mechanisms* of (a) (Bennequin budget: category error, BOX 1/3), (b) (trefoil minimality: modular-surface numerology), and (c) (Arf: ill-typed + unforced) are refuted or unsupported; the conjecture's *conclusions* (a) and (b-realizability) survive under the repaired bridge. The repair itself (knot-attached Lutz → torus-attached torsion) is disclosed as such; it is motivated by the forced classification (F3)–(F5), not fitted to the kill — indeed it *adds* an unregistered constraint (simplicity, §5) the conjecture never asked for.

---

**Five-line summary.**
1. Lutz twists along knots are unrestricted and always overtwist: KNOT-Q's Bennequin-budget mechanism for (a) is a category error, and the literal decoration is incompatible with the tight carrier.
2. The tight carrier forces the twist data to be Giroux torsion n ∈ ℤ₊ on vertical tori over essential *simple* closed geodesics; the canonical bridge sends this to charge Q = e·n anchored at fix(γ), matching the ℤ-quantized (lattice) boundary net.
3. Genus-0 knots get Q = 0 by locality + tightness — clause (a)'s conclusion survives with a replaced, forced mechanism; the genus-0 kill cannot fire.
4. Trefoil-minimality and Arf↦statistics are numerology (the parity is torsion parity, not Arf; sign(Q) is convention up to orientation data).
5. VERDICT: INCONCLUSIVE — the kill fires iff the torsion insertion acts trivially on the boundary net (e = 0); proving e ≠ 0 (or = 0) for one torsion unit along one T_γ is the single missing object.
