# Phase 105 — entry 6 candidate: the joint two-geodesic arena (JOINT-1) and the mirror lemma L-MIRROR (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-26, continuing the phase-105 successor program per the adopted plan (notes/PLAN-2026-07-26-dictionary-completion.md). **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** Editorial note on labels: the derivation agent self-titled its document "SPAN-2", which collides with the record's existing SPAN-2 label (the D₁₂ cross-invariant, phases/phase105-D12-cross-invariant.md); the derivation text is preserved verbatim below including that title, and this entry is registered in the record as **entry 6 / JOINT-1**.*

*Headline claims (pre-verdict): (1) a **precise partial no-go** — for a crossing pair no joint arena can keep an interval-local fiber: the requirements (fiber preserved by Λ = ⟨γ₁,γ₂⟩, both leg algebras contained) force the local slot to collapse to B(H), with crossing used essentially (Lemma A2); (2) the **ledger survives the collapse** — 1⊗L∞(S¹) is still exactly the center of the collapsed fiber, and the minimal honest joint arena is M_Λ = (B(H)⊗̄L∞(S¹))⋊Λ; internally the visibility trichotomy trivializes (everything visible); (3) **the internal consistency test PASSES at derivation level** — D₁₂ = Q₁Q₂·î reappears inside M_Λ as the central-extension class of the two defect-implementer lines (the full real σ, not just its exponential mod 2π), equivalently the obstruction to jointly ledgering both defects, reproducing the refereed triple equivalence internally; (4) the diagonal rates Dᵢ = Qᵢ²ℓᵢ/2π survive via canonical embeddings M_{γᵢ} ↪ M_Λ (with a flagged Tomiyama obstruction: no normal expectation onto the single arena exists); (5) **L-MIRROR is claimed PROVED in the E2 plateau class** — the mirrored sharp profile is s₁∘r₁ = Q₁ − s₁, a constant σ kills, so D₁₂ → −D₁₂ exactly in every configuration, sharp and smooth alike, with the prior winding-profile counterexamples adjudicated out-of-domain (winding profiles belong to E1, not E2). All of this goes to a context-free referee before any verdict; the referee's mandates include Lemma A2's arc-convergence argument, the internality of the central-extension class, and the legitimacy of the out-of-domain adjudication.*

---

## The derivation, verbatim

# SPAN-2 — The joint two-geodesic arena, and the mirror lemma L-MIRROR

## 0. Conventions

All notation as in the established setting: Weyl relations W(f)W(g) = e^{−iσ(f,g)/2}W(f+g), σ(f,g) = ∫_{S¹} f g′ dθ; single arenas M_γ = (A(I)⊗̄L∞(S¹)) ⋊_γ ℤ; entries E1–E5, C-D5, the locality trichotomy, and the triple equivalence are taken as given [others' = previously refereed]. γ₁, γ₂ are hyperbolic with anchors aᵢ = ξᵢ₋, bᵢ = ξᵢ₊, legs Iᵢ = Pᵢ = (aᵢ,bᵢ) (ccw), crossing with î = +1 (cyclic order a₁,a₂,b₁,b₂). Λ = ⟨γ₁,γ₂⟩ ≤ PSL(2,ℝ). [GAP-1: "generically Λ is free of rank 2" is assumed as a genericity label only; nothing below uses freeness except the inertness remark in §1.4.]

---

## 1. Task A — the joint arena

### 1.1 What a joint arena must be

The single arena's defining structure is: a crossed product N ⋊ G over the acting group, whose fiber N = F ⊗̄ L∞(S¹) contains the full leg algebra (needed to host arbitrary defects AND their E1 truncated-cocycle/erasure data, which live in A(I)), with the base 1⊗L∞(S¹) = Z(N) (the ledger), and G acting jointly (covariantly on F, boundary action on L∞). A joint arena for (γ₁,γ₂) must therefore be M = (F ⊗̄ L∞(S¹)) ⋊ Λ with (R1) Ad U(g)F = F for all g ∈ Λ (else the crossed product is undefined), (R2) F ⊇ A(I₁) and F ⊇ A(I₂) (both defects internal with E1 data), (R3) 1⊗L∞ ⊆ Z(fiber).

### 1.2 Lemma A1 (no common leg)

*No interval I is preserved by both γ₁ and γ₂.* Proof: a Möbius γ with γ(I) = I preserves ∂I = {x,y} setwise. If γ swapped x,y, then γ² fixes both; γ² is hyperbolic with the same fixed points ξ±, so {x,y} = {ξ₋,ξ₊} and γ swaps ξ₋,ξ₊ — impossible, γ fixes each. So γ fixes x,y individually, forcing {x,y} = {ξ₋,ξ₊}. A common leg needs ∂I ⊆ {ξ₁±} ∩ {ξ₂±} = ∅ (anchors pairwise distinct). ∎

So the single-arena template (interval fiber preserved by the group) is unavailable; the question is what fiber (R1)–(R2) force.

### 1.3 Lemma A2 (fiber collapse — crossing forces F = B(H))

*Any von Neumann algebra F ⊆ B(H) satisfying (R1)–(R2) for a crossing pair equals B(H).* Proof: By (R1)–(R2) and Möbius covariance, F ⊇ A(γ₂ⁿ I₁) for all n. Because the axes cross, a₁ and b₁ lie in different components of S¹∖{a₂,b₂}; under γ₂ⁿ every point ≠ a₂ flows to b₂, with γ₂ⁿa₁ → b₂ from the ccw-after side and γ₂ⁿb₁ → b₂ from the ccw-before side. Hence the ccw arcs γ₂ⁿI₁ = (γ₂ⁿa₁, γ₂ⁿb₁) increase to S¹∖{b₂}. By isotony F ⊇ A(J) for every interval J with closure in S¹∖{b₂}. The commutant of ∨_J A(J) is, by Haag duality, ∩ A(J′) over intervals J′ shrinking to {b₂}, which is ℂ1 [GAP-2, others': point-triviality ∩_{I∋p}A(I) = ℂ1, standard for irreducible Möbius-covariant nets]. So F = B(H). ∎

Remark (crossing is essential): the proof uses precisely that a₁, b₁ straddle the γ₂-anchors, i.e. î ≠ 0. For nested/disjoint pairs the images γ₂ⁿI₁ shrink, and whether a proper local joint fiber exists is left open [GAP-7].

Candidate (b) — the algebra generated by the two single arenas in the vacuum representation — contains A(I₁), A(I₂), U₁, U₂ and hence equals B(H) by the same argument: it is degenerate and loses the ledger entirely (L∞(S¹) does not act on H). Candidate (c) is candidate (b) plus external bookkeeping — not an algebra with an internal ledger. Candidate (a) with the forced fiber is therefore the honest choice:

**[BOX 1] (Partial no-go + construction.)** *No joint arena for a crossing pair retains an interval-local fiber: (R1)+(R2) force the first tensor slot to collapse to B(H) (Lemma A2). The minimal honest joint arena is*

M_Λ = (B(H) ⊗̄ L∞(S¹)) ⋊ Λ, g·(x⊗f) = U(g)xU(g)* ⊗ f∘g⁻¹.

*The joint ledger survives: 1⊗L∞(S¹) = Z(B(H)⊗̄L∞(S¹)) is still exactly the center of the fiber ((R3) holds). What is destroyed is locality of the fiber, not centrality of the ledger: internally, the visible/invisible/inadmissible trichotomy trivializes — every defect is visible to M_Λ.*

### 1.4 Status of the ledger structure

The Λ-action on the base is essentially free (each g ≠ e is Möbius, fixing ≤ 2 points — Lebesgue-null), so the crossed product over the base is of the standard essentially-free type and the refereed countable-orbit rigidity (fact (ii)) applies verbatim to R_Λ (Λ countable). Base-inertness (fact (i)) was proved for *leg-aligned* states; "leg-aligned" is undefined in M_Λ (no leg), and no analog is claimed [GAP-4]. The canonical expectation E₀ onto the fiber persists (Fourier restriction on ℓ²(Λ)). One structural novelty: Z(M_Λ) = L∞(S¹)^Λ ⊗ 1; if Λ is discrete of the second kind (Schottky), this is L∞(Ω(Λ)/Λ) ≠ ℂ — the joint arena has nontrivial center supported on the ordinary set [GAP-5, others': Fuchsian non-ergodicity on S¹ for second-kind groups]; for Λ dense in PSL(2,ℝ) the center is trivial.

### 1.5 Internal recovery of the cross-invariant D₁₂

Take E2-class representatives ηᵢ (plateau on Pᵢ, ramps of width < δ/2 at the anchors, all four ramps pairwise disjoint, C-D5). Both W(tη₁), W(sη₂) (t,s ∈ ℝ) lie in the fiber of M_Λ. From the Weyl relation and antisymmetry of σ:

W(tη₁) W(sη₂) W(tη₁)⁻¹ W(sη₂)⁻¹ = e^{−i t s σ(η₁,η₂)} · 1.

So the group generated by the two implementer lines (mod phases ℝ²) is a central extension of ℝ² by 𝕋 whose class, under H²(ℝ²,𝕋) ≅ ∧²ℝ² ≅ ℝ [others': standard], is the antisymmetric form (t,s)∧(t′,s′) ↦ (ts′−st′)σ(η₁,η₂). The full real number σ(η₁,η₂) — not merely its exponential mod 2π — is thus an internal invariant of M_Λ (the single-commutator phase alone gives it only mod 2π; the one-parameter families remove the ambiguity).

It remains to *compute* σ in the class. η₂′ is supported on two ramps; since all ramps are pairwise disjoint, η₁ is constant on each η₂-ramp, equal to its plateau value there. Hence, exactly,

σ(η₁,η₂) = ∫ η₁ η₂′ dθ = Q₂[η₁(a₂) − η₁(b₂)].

For crossing with î = +1: a₂ ∈ P₁ (η₁ = Q₁), b₂ ∉ P₁ (η₁ = 0), so σ = Q₁Q₂. For î = −1: σ = −Q₁Q₂. Nested or disjoint: both or neither anchor in P₁, σ = 0. So σ = Q₁Q₂î exactly, with no extra terms and no normalization discrepancy.

**[BOX 2] (Internal consistency.)** *Inside M_Λ, the cross-invariant reappears as the class of the central extension of ℝ² generated by the two defect-implementer lines: D₁₂ = σ(η₁,η₂) = Q₁Q₂·î, exactly. Equivalently, it is the obstruction to a joint abelian ledgering of both implementers: they generate an abelian (extendable-to-ledger) group iff σ = 0 iff the axes do not cross — the refereed triple equivalence is reproduced internally, not assumed.*

### 1.6 Diagonal survival

Each single arena embeds canonically: A(Iᵢ)⊗̄L∞ ⊆ B(H)⊗̄L∞ (subfiber; the γᵢ-action restricts to the single-arena action) and ⟨γᵢ⟩ ≤ Λ (subgroup), giving normal inclusions M_{γᵢ} = (A(Iᵢ)⊗̄L∞) ⋊_{γᵢ} ℤ ↪ M_Λ. The E1 quantity D = Qᵢ²ℓᵢ/2π is defined from Iᵢ-local truncated Connes-cocycle data under iteration of γᵢ — objects living entirely in the embedded copy and computed from the same Hilbert-space data; the embedding changes nothing.

**[BOX 3] (Diagonal survival.)** *D_i = Qᵢ²ℓᵢ/2π is recovered inside M_Λ by restriction to the embedded single arena M_{γᵢ} ⊂ M_Λ, unchanged.* Caveat: recovery is via *embedding*, not expectation. The group direction is fine (canonical expectation M_Λ → fiber⋊⟨γᵢ⟩ by Fourier restriction), but there is **no** normal conditional expectation B(H) → A(Iᵢ): the range of a normal expectation on B(H) is atomic (type I) [GAP-6, others': Tomiyama], while A(Iᵢ) is type III₁. So "restriction/expectation onto each single arena" holds in the weaker (embedding) sense only — flagged.

---

## 2. Task B — L-MIRROR in the E2 class

### 2.1 Theorem and proof (sharp representatives)

Let r₁ be the reflection fixing ∂I₁ = {a₁,b₁} (boundary action of the modular conjugation J₁ of (A(I₁),Ω), per E5). r₁ fixes a₁, b₁ and maps P₁ = (a₁,b₁) onto P₁′ = (b₁,a₁). Hence for the sharp E2 representative s₁ = Q₁·1_{P₁}:

s₁∘r₁ = Q₁·1_{r₁⁻¹P₁} = Q₁·1_{P₁′} = Q₁ − s₁.

σ is insensitive to additive constants in either argument [given, E2], so for every configuration of the second defect,

σ(s₁∘r₁, s₂) = σ(Q₁ − s₁, s₂) = −σ(s₁, s₂).

The candidate route is correct and complete at sharp level; note it uses **no** Möbius structure — any orientation-reversing homeomorphism fixing both anchors gives the same result, since only the plateau structure enters.

### 2.2 (i) Smooth C-D5 representatives

Let η₁ be a smooth representative (ramps in ε-neighborhoods of a₁, b₁, ε < δ/2). r₁ fixes both anchors with r₁′ = −1 there, so η₁∘r₁ has its ramps again at a₁, b₁ (distorted in shape by the Möbius reflection, and contained in slightly different neighborhoods — shrink ε so the reflected ramps remain disjoint from the η₂-ramps). The distortion is irrelevant: off the η₁-ramps, η₁∘r₁ + η₁ ≡ Q₁ identically (plateau values Q₁+0 or 0+Q₁), and η₂′ vanishes *on* the η₁-ramps (disjointness). Hence exactly

σ(η₁∘r₁ + η₁, η₂) = Q₁∫η₂′ dθ = 0, i.e. σ(η₁∘r₁, η₂) = −σ(η₁, η₂),

ramp shapes notwithstanding. Midpoint regularization at shared anchors: since r₁′(anchor) = −1, a ramp chosen r₁-symmetric about the anchor is mapped to itself reversed, preserving the midpoint convention; choosing C-D5 representatives r₁-equivariantly is a convention refinement available within the class [GAP-8: needed only in shared-anchor configurations; in the generic all-distinct case σ is ramp-independent anyway].

### 2.3 (ii) Is s₁∘r₁ the right mirror representative?

Yes. Across the a₁-ramp (ccw), η₁ transports +Q₁; η₁∘r₁ goes from value Q₁ (just before a₁, image lands past a₁ inside P₁) to 0 (just after), i.e. transports **−Q₁** across the a₁-ramp and +Q₁ across b₁. So s₁∘r₁ is precisely the E2-class plateau representative of a charge-(−Q₁) defect on the reflected side — matching the refereed conjugation entry (J flips charge, reflects support to I₁′). The E2 mirror of defect 1 is s₁∘r₁; no other candidate is consistent with the anchor-transport bookkeeping.

### 2.4 (iii) Reconciliation with the winding counterexamples

The winding computation fails for two stacked reasons. (α) A winding profile has a non-periodic part ∝ Q₁θ; composing with r₁ produces −Q₁·(linear) *plus a non-constant Möbius-distortion term* (r₁(θ) + θ is not constant), whose derivative is supported on all of S¹ and therefore pairs with η₂ globally — the "kill the constant" step is unavailable. (β) The branch-cut/branch-charge convention at the anchors injects convention-dependent boundary terms (hence the observed 0 → 0 and −1/4 → +3/4: neither a flip nor any fixed law). But the dictionary's D₁₂ is *defined* on the distinguished single-valued plateau class (E2 verbatim: "the distinguished profile class for the cross-invariant is the single-valued plateau class"); winding profiles belong to the diagonal/metric entry E1. So the counterexamples live outside the invariant's domain: they refute the winding-class law, not L-MIRROR. Consistency with the exact identities: anti-symplecticity gives σ(s₁∘r₁, s₂) = −σ(s₁, s₂∘r₁); combined with the flip this yields the corollary σ(s₁, s₂∘r₁) = +σ(s₁,s₂) — directly checkable, since σ(s₁,h) = Q₁[h(b₁) − h(a₁)] and r₁ fixes a₁, b₁. Verified numerically below.

### 2.5 (iv) Numerics

Smooth cos²-bump ramps (width 0.05), Q₁ = 2, Q₂ = 3, r₁ implemented as the exact Möbius circle map z ↦ φ⁻¹(−φ(z)), φ(z) = (z−z_{a₁})/(z−z_{b₁}) (involution error ≤ 10⁻¹⁵; fixes both anchors). Grid 4·10⁵ points; all values exact to ≤ 10⁻⁶:

| configuration | σ(η₁,η₂) | σ(η₁∘r₁,η₂) | σ(η₁,η₂∘r₁) | σ(η₁∘r₁,η₂∘r₁) |
|---|---|---|---|---|
| crossing î=+1 (a₁,a₂,b₁,b₂) | +6.000000 | −6.000000 | +6.000000 | −6.000000 |
| crossing î=−1 (a₁,b₂,b₁,a₂) | −6.000000 | +6.000000 | −6.000000 | +6.000000 |
| nested (P₂⊂P₁) | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| disjoint | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

Single-mirror flip, the mixed identity σ(η₁∘r₁,η₂) = −σ(η₁,η₂∘r₁), the corollary σ(η₁,η₂∘r₁) = +σ(η₁,η₂), and the both-mirrored flip all confirmed in every configuration.

**[BOX 4] (L-MIRROR: PROVED in the E2 class.)** *In the distinguished plateau class (E2, C-D5), the mirror of defect 1 under the modular reflection r₁ is the E2 representative s₁∘r₁ = Q₁ − s₁ of the charge-(−Q₁) defect on P₁′, and for every configuration of defect 2 — both crossings, nested, disjoint —*

D₁₂(mirror-1, 2) = σ(s₁∘r₁, s₂) = −σ(s₁,s₂) = −D₁₂,

*exactly, for sharp and for smooth C-D5 representatives alike. The prior winding-profile counterexamples concern profiles outside the invariant's domain of definition and leave this statement untouched. Bonus corollary: mirroring defect 2 across the* other *defect's reflection r₁ leaves σ unchanged.*

---

## 3. Five-line summary

1. **No-go, precise form:** a joint arena for a crossing pair cannot keep an interval-local fiber — crossing forces the fiber's local slot to collapse to B(H) (Lemma A2, crossing used essentially); the ledger 1⊗L∞(S¹) nevertheless survives as the exact center of the collapsed fiber.
2. **Construction:** M_Λ = (B(H)⊗̄L∞(S¹)) ⋊ Λ is the minimal honest joint arena; candidates (b),(c) lose the ledger.
3. **Consistency:** the cross-invariant reappears internally as the central-extension class of the two implementer lines, D₁₂ = Q₁Q₂î exactly — equivalently the obstruction to jointly ledgering both defects, reproducing the triple equivalence.
4. **Diagonals:** each Dᵢ = Qᵢ²ℓᵢ/2π survives via canonical embedding M_{γᵢ} ↪ M_Λ (no normal expectation exists onto the single arena — Tomiyama obstruction, flagged).
5. **L-MIRROR: PROVED in the E2 class** — s₁∘r₁ = Q₁ − s₁ up to a constant σ kills, so the flip D₁₂ ↦ −D₁₂ holds exactly in all configurations (verified numerically to 10⁻⁶); the winding counterexamples lie outside E2's domain.
