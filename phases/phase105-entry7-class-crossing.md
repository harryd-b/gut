# Phase 105 — entry 7 candidate: the conjugacy-class crossing invariant D̄₁₂ (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-26, continuing per the adopted plan (notes/PLAN-2026-07-26-dictionary-completion.md). **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** Editorial note on labels: the derivation agent self-titled its document "SPAN-2", colliding with the record's existing SPAN-2 label (phases/phase105-D12-cross-invariant.md); text preserved verbatim including that title; registered in the record as **entry 7 / CLASS-1**.*

*Headline claims (pre-verdict): (1) D̄₁₂ = Q₁Q₂·Î([γ₁],[γ₂]), the sum of refereed E2 pair entries over double cosets ⟨γ₁⟩\Γ/⟨γ₂⟩, is well-defined, FINITE (crossing cosets ↔ transverse intersection points of the closed geodesics), and representative-independent; (2) it equals Q₁Q₂ × the ALGEBRAIC intersection number of the closed geodesics, with |Î| ≤ i(c₁,c₂) and Î ≡ i mod 2; (3) — the structural prize, if it survives refereeing — **HOMOLOGICAL DESCENT**: D̄₁₂ = ⟨Q₁[c₁], Q₂[c₂]⟩, the intersection pairing of charge-weighted classes in H₁(X;ℝ) — the dictionary's cross-invariant is a homological pairing, and is correspondingly homologically BLIND (separating geodesics pair to zero with everything); (4) multiplicity law m₁m₂ on powers (entry registered for primitive classes); inverse law; antisymmetry; summand-wise mirror law; (5) the diagonal off-identity signed sum vanishes IDENTICALLY (double cosets count each self-crossing twice with cancelling signs — the writhe-like single-count is not defined by this formalism); (6) the flagged "surface-level defect" divergence concern is resolved by DISSOLUTION: the profile sum diverges absolutely AND boundary ergodicity (Hopf) shows no nonzero Γ-invariant profile class exists — the entry is DATA (a pairing of charge-decorated H₁ classes), not a state, exactly per the adopted thesis. Numerics on an explicit punctured-torus group verify finiteness plateaus, antisymmetry, inverse and multiplicity laws, the homology formula on six pairs, and the diagonal cancellation. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# SPAN-2: The class-level crossing invariant D̄₁₂ — derivation

**Standing data (refereed, imported):** E2: on the distinguished plateau class, σ(η₁,η₂) = Q₁Q₂·î(γ₁,γ₂) exactly, î ∈ {0,±1} the signed crossing number of the oriented axes, î = +1 for ccw cyclic order (a₁,a₂,b₁,b₂); C-D5 at shared anchors; σ kills constants. Entry 6: one-sided modular mirror flips D₁₂. E1: diagonal metric entry D = Q²ℓ/2π. Γ ⊂ PSL(2,ℝ) discrete, torsion-free; γ₁, γ₂ ∈ Γ primitive hyperbolic, [γ₁] ≠ [γ₂^{±1}] except in §3c; cᵢ ⊂ X = Γ\ℍ the closed geodesic of [γᵢ].

## 1. Definition, finiteness, representative independence

**Definition.** For a double coset ⟨γ₁⟩g⟨γ₂⟩ set î_g := î(axis γ₁, g·axis γ₂), and

**[BOX 1]** D̄₁₂ := Q₁Q₂·Î([γ₁],[γ₂]), Î := Σ_{⟨γ₁⟩g⟨γ₂⟩ ∈ ⟨γ₁⟩\Γ/⟨γ₂⟩} î_g — a well-defined, **finite** sum of refereed E2 pair entries, independent of the chosen representatives γᵢ.

**(a) Well-defined on double cosets.** î is PSL(2,ℝ)-invariant: Möbius maps preserve the ccw cyclic order on ∂ℍ, hence î(hα,hβ) = î(α,β). The oriented axis(γ₂) is ⟨γ₂⟩-invariant, so gγ₂ⁿ·axis γ₂ = g·axis γ₂; and î(axis γ₁, γ₁^m g·axis γ₂) = î(γ₁^{−m}axis γ₁, g·axis γ₂) = î_g since γ₁^{−m} preserves axis γ₁ with orientation. So î_g depends only on ⟨γ₁⟩g⟨γ₂⟩. Moreover every summand falls under refereed E2: g·axis γ₂ = axis γ₁ would force gγ₂g⁻¹ = γ₁^{±1} (torsion-free, both primitive), excluded by [γ₁] ≠ [γ₂^{±1}]; all axes in the sum are distinct from axis γ₁.

**(b) Finiteness.** Lemma (standard [others']; argument shape): *crossing double cosets are in bijection with ordered pairs (branch of c₁, branch of c₂) meeting transversally at a point of X* — i.e. with transverse intersection points counted with branch multiplicity. If î_g ≠ 0 the two axes cross in a unique point p̃_g (distinct complete geodesics in ℍ meet at most once); π(p̃_g) ∈ c₁ ∩ c₂, and moving g within its double coset moves p̃_g by ⟨γ₁⟩ along axis γ₁ — the same point of X. Conversely, given a transverse crossing p with chosen branches: the c₁-branch lifts to a Γ-translate of axis γ₁; adjust by a deck element so the lift p̃ lies on axis γ₁ (residual ambiguity: ⟨γ₁⟩, the oriented-axis stabilizer, using primitivity); the c₂-branch through p̃ lifts to g·axis γ₂ for some g (all lifts of c₂ are translates of axis γ₂; ambiguity ⟨γ₂⟩ on the right). The two ambiguities are exactly the double-coset relation. Since c₁, c₂ are **compact** and distinct geodesics cross transversally in isolated points, there are finitely many such crossings. Note cocompactness of Γ is *not* needed — only that the γᵢ are hyperbolic in a discrete group, making cᵢ compact. [GAP-1: the bijection is cited as standard; the lift/ambiguity bookkeeping above is the argument shape, not a formalized proof.]

**(c) Representative independence.** γ₁ → hγ₁h⁻¹ gives axis(hγ₁h⁻¹) = h·axis γ₁ and the bijection ⟨hγ₁h⁻¹⟩g⟨γ₂⟩ ↦ ⟨γ₁⟩h⁻¹g⟨γ₂⟩ with î(h·axis γ₁, g·axis γ₂) = î(axis γ₁, h⁻¹g·axis γ₂): the multiset of summands is unchanged. Symmetrically on the right. ∎

## 2. Geometric identification

**Sign lemma.** At a transverse crossing of oriented geodesics α (a₁→b₁), β (a₂→b₂) in ℍ, define the local sign ε := sign det(t_α, t_β). Then ε = î. *Model computation:* disk model, α the horizontal diameter oriented rightward (a₁ at angle π, b₁ at 0). The î = +1 configuration, ccw order (a₁,a₂,b₁,b₂), puts a₂ in the lower semicircle and b₂ in the upper, so β crosses upward: det(t_α,t_β) > 0. Both ε and î are invariant under orientation-preserving Möbius maps, so the model case is general. [others': endpoint linking = crossing sign is standard.] Since π: ℍ → X is a local orientation-preserving isometry, ε at p̃_g equals the local frame sign of the two branches at the image point.

**[BOX 2]** Î([γ₁],[γ₂]) = Σ_{transverse crossings p ∈ c₁∩c₂} ε(p) = the **algebraic intersection number** ĉ₁·ĉ₂ of the oriented closed geodesics on the oriented surface X.

**Bounds and parity.** |Î| ≤ (number of transverse crossings of the geodesic representatives) = i(c₁,c₂), the geometric intersection number, because closed geodesics realize the minimal transverse intersection in their free homotopy classes [others'; GAP-2: minimality imported]. Equality iff all crossings carry one sign. Parity: each crossing contributes ±1, so **Î ≡ i(c₁,c₂) mod 2**. Worked example: §6, punctured torus, Î([A],[B]) = −1 = ±i.

## 3. Well-definedness details

**(a) Powers/multiplicity.** Let γᵢ = δᵢ^{mᵢ}, δᵢ primitive, mᵢ ≥ 1. Axes and orientations are unchanged, so each summand is unchanged; only the coset space refines. Inside a coarse coset ⟨δ₁⟩g⟨δ₂⟩ with distinct axes (all crossing cosets qualify), the map (i mod m₁, j mod m₂) ↦ ⟨δ₁^{m₁}⟩δ₁^i g δ₂^j⟨δ₂^{m₂}⟩ is a bijection onto the fine cosets it contains: a coincidence δ₁^i g δ₂^j = δ₁^{i′}g δ₂^{j′} with (i,j) ≠ (i′,j′) would give g⁻¹δ₁^k g = δ₂^{−l}, (k,l) ≠ 0, forcing shared axes — excluded. Hence each crossing coarse coset splits into exactly m₁m₂ fine cosets with equal î:

**Î([δ₁^{m₁}],[δ₂^{m₂}]) = m₁m₂·Î([δ₁],[δ₂]).** The dictionary entry is registered for **primitive** classes; powers via this multiplicity law. (Numerically verified.)

**(b) Inverses and the mirror.** ⟨γ₁⁻¹⟩ = ⟨γ₁⟩, so the coset space is identical; axis(γ₁⁻¹) is axis(γ₁) reversed, and swapping a₁↔b₁ flips the linking class: every î_g flips. Thus Î([γ₁⁻¹],[γ₂]) = −Î. Consistency with Entry 6: r₁γ₁r₁ = γ₁⁻¹, and the refereed mirror flips each pair entry; since the mirror fixes each double coset (as a set) and negates each summand, the class-level law D̄₁₂ → −D̄₁₂ is the coset-wise aggregate. [GAP-3: Entry 6 was refereed for a single element pair; the class-level mirror is *defined* summand-wise here, not re-derived in a joint arena.] Antisymmetry: g ↦ g⁻¹ bijects ⟨γ₁⟩\Γ/⟨γ₂⟩ with ⟨γ₂⟩\Γ/⟨γ₁⟩, and î(axis₁, g·axis₂) = î(g⁻¹axis₁, axis₂) = −î(axis₂, g⁻¹axis₁), so Î([γ₂],[γ₁]) = −Î([γ₁],[γ₂]).

**(c) Diagonal.** Take [γ₁] = [γ₂] = [γ], γ primitive. The identity coset has coincident axes: outside E2's distinct-axes hypothesis; it carries the metric entry E1 (D = Q²ℓ/2π), not a crossing sign, and is excluded from Î (C-D5 assigns no crossing value there). Same-axis translates occur only for g ∈ ⟨γ⟩ (torsion-free), i.e. only the identity coset.

**[BOX 3]** Î_off([γ],[γ]) := Σ_{⟨γ⟩g⟨γ⟩ ≠ ⟨γ⟩} î_g = 0, **identically** — even for non-simple c. *Proof.* ι: ⟨γ⟩g⟨γ⟩ ↦ ⟨γ⟩g⁻¹⟨γ⟩ is a well-defined involution, and î_{g⁻¹} = î(g·axis, axis) = −î_g. A ι-fixed coset (g⁻¹ = γ^a g γ^b) satisfies î_g = î_{g⁻¹} = −î_g = 0, so crossing cosets pair off with opposite signs. ∎

*Adjudication of what this computes:* each **unordered** geometric self-crossing of c corresponds (via §1b with c₁ = c₂ = c) to the two ordered branch pairs, i.e. exactly the pair {coset(g), coset(g⁻¹)}. The double-coset sum therefore counts every self-crossing **twice, with cancelling signs**. The writhe-like single-count signed sum is *not* defined by this formalism — it would require a canonical ordering of branches, which double cosets do not supply. The well-defined class quantity is 0, consistent with x·x = 0 for the antisymmetric homological form; the sum does **not** compute the (generally nonzero) unsigned self-intersection count. (Numerically confirmed: [A²B²] below.)

## 4. Homological descent

**[BOX 4]** Î([γ₁],[γ₂]) = ⟨[c₁],[c₂]⟩, the homological intersection pairing on H₁(X;ℤ). Hence **D̄₁₂ = ⟨Q₁[c₁], Q₂[c₂]⟩** on H₁(X;ℝ): the dictionary's cross-invariant is a homological pairing of charge-weighted cycle classes.

*Proof.* By Box 2, Î = ĉ₁·ĉ₂. The algebraic intersection number of transverse loops on an oriented surface depends only on the homology classes [others': if c₁ ∼ c₁′ in H₁ then their difference bounds a 2-chain S, and the signed intersection of ∂S with the compact loop c₂ vanishes; for closed X this is Poincaré duality]. [GAP-4: the open-surface (non-cocompact) case is routine — both loops compact — but imported, not re-proved.] Structural consequence: the entry is *homologically blind* — homologous classes are indistinguishable; any class with separating (null-homologous) geodesic pairs to 0 with everything, however large its geometric intersections.

## 5. What carries the invariant (divergence question adjudicated)

**Data reading — adopted.** D̄₁₂ is a **finite signed sum of refereed pairwise E2 invariants**, a pairing of labels: precisely, a function of the pair of charge-decorated classes, and by Box 4 a function of (Q₁[c₁], Q₂[c₂]) ∈ H₁(X;ℝ)⊕H₁(X;ℝ). No joint state, no dynamics — consistent with the standing thesis "geometry is data."

**State reading — fails, twice over.**
(i) *No absolute convergence.* A Γ-covariant "surface defect profile" would be η̄ = Σ_{g⟨γ₂⟩} η∘g⁻¹ over the infinite coset space. Möbius transformations act unitarily on the one-particle space (vacuum-preserving, quasi-free), so every term has the same H^{1/2}-norm: the sum of norms diverges linearly in the number of orbit terms (exponentially in word length — Γ nonelementary). [GAP-5: only absolute divergence is proven; conditional cancellation is not ruled out by this argument alone.]
(ii) *No invariant target exists.* Stronger: any Fuchsian group of the first kind (cocompact included) acts **ergodically** on ∂ℍ = S¹ [others': Hopf]. A Γ-invariant profile class would admit an a.e.-Γ-invariant measurable representative modulo constants, hence be a.e. constant, hence **zero** in the symplectic one-particle space (σ kills constants). There is nothing for the sum to converge to. [GAP-6: identification of H^{1/2}-classes with measurable boundary functions and the a.e.-invariance bookkeeping — routine but not spelled out; for Γ of the second kind (not our case) ergodicity fails and the argument doesn't apply.]

The flagged "surface-level defect" concern is thereby resolved by *dissolution*: reading (a) is what the entry means; reading (b) is empty.

## 6. Numerics (evidence, not proof [GAP-7])

Punctured-torus group Γ = ⟨A,B⟩, A = [[1,1],[1,2]], B = [[1,−1],[−1,2]], tr[A,B] = −2 (discrete, free, non-cocompact; closed geodesics compact so §1 applies). Method: reduced words to length 7 (4372 elements); canonical double-coset representative by minimizing reduced γ₁^m g γ₂^n; axis endpoints via eigenvectors, Cayley-mapped to S¹; î from cyclic order. All sums **plateau by word length ≤ 5** (finiteness visible). Results:

- Î([A],[B]) = −1; Î([B],[A]) = +1; Î([A⁻¹],[B]) = +1; Î([A],[B⁻¹]) = +1 (antisymmetry, inverse law).
- Representative independence: conjugated representatives (e.g. BABA⁻¹B⁻¹·... reps of [B], [A]) give identical values.
- Multiplicity: Î([A²],[B]) = −2; Î([A²],[B²]) = −4.
- Class consistency: Î([AB],[A]) = Î([BA],[A]) = +1.
- Homology (H₁ exponent vectors (p,q)): Î = −(p₁q₂ − q₁p₂) exactly, on six pairs including ([A²B],[AB⁻¹]) → 3, ([A²B⁻¹],[B]) → −2, ([A²B²],[A]) → 2 (overall sign is the orientation convention). Box 4 verified.
- Diagonal: [A²B²] is non-simple (homology 2·(1,1)): exactly two crossing cosets, signs +1 and −1, paired under g↔g⁻¹; total 0. [A²B], [AB] simple: no crossing cosets. Box 3 verified.

## 7. Dictionary entry and honest limits

**[BOX 5] — SPAN-2 entry (class-level crossing invariant).** For distinct primitive hyperbolic classes [γ₁], [γ₂] ([γ₁] ≠ [γ₂^{±1}]) with charges Q₁, Q₂:

  **D̄₁₂ = Q₁Q₂·Î([γ₁],[γ₂]) = Q₁Q₂·⟨[c₁],[c₂]⟩ ∈ (Q₁Q₂)·ℤ**

finite; antisymmetric under 1↔2; bilinear in charges; **multiplicity law** m₁m₂ on powers (registered for primitive classes); **inverse law** −D̄ under [γ₁]→[γ₁⁻¹]; **mirror law** D̄₁₂ → −D̄₁₂ (summand-wise Entry 6, coset space fixed); diagonal: identity coset carries E1, off-identity signed sum ≡ 0. Status: **data** — a pairing of charge-decorated homology classes Qᵢ[cᵢ] ∈ H₁(X;ℝ); no state, no dynamics.

**Honest limits.** (1) No dynamics claimed; D̄₁₂ aggregates pairwise plateau invariants — no joint infinite-defect state exists (§5(ii)) and none is used. (2) Homological blindness: D̄₁₂ sees strictly less than geometry; |Î| ≤ i(c₁,c₂) with Î ≡ i mod 2, and homologous classes are indistinguishable. (3) The class-level mirror is definitional aggregation of Entry 6 [GAP-3]. (4) Imports [others']: crossing↔double-coset bijection, endpoint-linking = crossing sign, geodesic intersection minimality, homology invariance of algebraic intersection, boundary ergodicity. (5) Numerics: one non-cocompact example, finite word length; a plateau is *guaranteed* by §1 but its attainment at L = 5 for these words is empirical.

---

**Summary (5 lines).**
1. D̄₁₂ = Q₁Q₂ Σ_{double cosets} î is well-defined, finite, representative-independent — a finite sum of refereed E2 entries (Box 1).
2. It equals Q₁Q₂ times the algebraic intersection number of the closed geodesics, hence the **homological pairing** Q₁Q₂⟨[c₁],[c₂]⟩ (Boxes 2, 4; numerically verified on a punctured-torus group).
3. Multiplicity m₁m₂ on powers, inverse law, antisymmetry, and summand-wise mirror all hold; the diagonal off-identity sum vanishes identically because double cosets count each self-crossing twice with opposite signs (Box 3).
4. The "surface defect" divergence concern dissolves: the profile sum diverges absolutely and, by boundary ergodicity, no nonzero Γ-invariant profile exists — the entry is **data** (a pairing of charge-decorated H₁-classes), not a state.
5. Gaps flagged: standard-fact imports [others'], summand-wise mirror as definition, open-surface homology invariance, and numerics as finite-length evidence.
