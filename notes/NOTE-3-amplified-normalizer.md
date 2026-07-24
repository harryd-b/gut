# NOTE-3 — The amplified normalizer lemma (JOIN-4c)

*Standalone mathematics note; drafted 2026-07-24 in the phase-104 working session. **Status: [derived, refereed — verdict: LEMMA TRUE, PROOF CORRECT AFTER ONE REPAIR; repair applied in the text below, all referee contributions credited in §4].** Report preserved verbatim in `reviews/REPORTS-phase104-JOIN4c-referee-2026-07-24.md`. Purpose: close correction item C2 of phase 104 §7.3 — phase 103's [R_Γ] step cited Feldman–Moore for a normalizer statement in an ambient algebra where the base is not Cartan; this note proves the statement actually needed. Method disclosure: drafted with substantial AI assistance; the proof is printed in full so that any reader can check it without trusting anyone.*

---

## 1. Statement

**Setting.** (X, μ) a standard probability space; Γ a countable group acting on X by nonsingular transformations; N = L∞(X) ⋊ Γ the crossed-product von Neumann algebra (any type; no trace assumed); A₀ = L∞(X) ⊂ N. Let P be any von Neumann algebra with separable predual (the case of interest: P = B(H)), and set

> M := P ⊗̄ N = (P ⊗̄ L∞(X)) ⋊ Γ,  A := 1 ⊗ A₀,

where Γ acts diagonally with **trivial action on P** (this identification is exact — no untwisting is involved, because the P-leg action is trivial by construction; contrast the inner-action untwisting of the arena 𝒞, which is how M of this form arises there). R_Γ ⊂ X × X denotes the orbit equivalence relation, [R_Γ] its full group: the nonsingular invertible transformations T of X with (x, Tx) ∈ R_Γ for a.e. x.

**Lemma (amplified normalizer lemma).** *Let u ∈ M be a unitary with uAu\* = A, and let β ∈ Aut(A₀) be the induced automorphism, u(1⊗a)u\* = 1⊗β(a). Then β is implemented by an element of the full group: there is T ∈ [R_Γ], unique mod null, with β(a) = a∘T⁻¹.*

Note what is *not* assumed: no trace, no ergodicity, no essential freeness, no factoriality; A is not maximal abelian in M (its relative commutant is P ⊗̄ A₀), so the Feldman–Moore normalizer theorem does not apply verbatim — that inapplicability is exactly the gap (phase 104 §7.3 C2) this note closes.

## 2. Proof

**Step 0 (canonical expectation and Fourier coefficients).** Write Q := P ⊗̄ L∞(X) ≅ L∞(X, P), so M = Q ⋊ Γ with canonical unitaries λ_γ and the canonical faithful normal conditional expectation E : M → Q determined by E(q λ_γ) = δ_{γ,e} q. For x ∈ M define the Fourier coefficients x_γ := E(x λ_γ\*) ∈ Q. Standard crossed-product facts used (discrete group, canonical E; see e.g. Takesaki vol. II or any crossed-product reference): (i) E is Q-bimodular; (ii) the coefficients determine the element — if x_γ = 0 for all γ ∈ Γ then x = 0 (via the decomposition of the standard form into the λ_γ-translates of L²(Q), or the dual coaction). We write γ_\*a := a∘γ⁻¹ for the action on L∞(X), so that λ_γ (1⊗a) λ_γ\* = 1⊗γ_\*a; scalars L∞(X)·1 are central in Q.

**Step 1 (point realization of β).** β is a normal automorphism of A₀ = L∞(X) with X standard; by the classical point-realization theorem (von Neumann) there is a nonsingular invertible transformation T of X, unique up to null sets, with β(a) = a∘T⁻¹. It remains to show (x, Tx) ∈ R_Γ a.e.

**Step 2 (the coefficient equation).** The normalization relation reads u(1⊗a) = (1⊗β(a))u for all a ∈ A₀. Take γ-th Fourier coefficients of both sides. Right side, by left Q-modularity: [(1⊗β(a))u]_γ = (1⊗β(a))·u_γ. Left side: (1⊗a)λ_γ\* = λ_γ\*(1⊗γ_\*a), so [u(1⊗a)]_γ = E(u λ_γ\* (1⊗γ_\*a)) = u_γ·(1⊗γ_\*a) by right Q-modularity. Hence, in L∞(X, P), for every γ ∈ Γ and a ∈ A₀:

> u_γ · (γ_\*a) = (β(a)) · u_γ,  i.e.  (a∘γ⁻¹ − a∘T⁻¹) · u_γ = 0,

where a∘γ⁻¹, a∘T⁻¹ act as central (scalar-valued) functions.

**Step 3 (pointwise identification on supports).** Fix γ and set S_γ := {x ∈ X : u_γ(x) ≠ 0} (measurable, defined mod null after choosing a representative of u_γ ∈ L∞(X,P)). Choose a countable **point-separating** algebra 𝒜 of Borel sets — available since X is standard Borel (pull back the dyadic clopen algebra under a Borel isomorphism of X into {0,1}^ℕ); point-separation, not mod-null generation, is what the argument needs [repair R1, §4 — the referee exhibited a counterexample scheme showing a merely mod-null-generating algebra can fail to separate a positive-measure family of pairs]. Apply the Step-2 identity to the countably many indicators a = χ_Z, Z ∈ 𝒜, choosing Borel representatives once and for all. For each Z the identity gives a conull set on which χ_Z(γ⁻¹x) = χ_Z(T⁻¹x) whenever x ∈ S_γ; intersecting over the countable family, there is a conull set on which, for all x ∈ S_γ, the points γ⁻¹x and T⁻¹x are not separated by any Z ∈ 𝒜 — hence, 𝒜 being point-separating, γ⁻¹x = T⁻¹x for a.e. x ∈ S_γ. Thus:

> T⁻¹ = γ⁻¹ a.e. on S_γ, for every γ ∈ Γ.

**Step 4 (the supports cover X).** Claim: ⋃_γ S_γ is conull. Suppose not; let Y := X ∖ ⋃_γ S_γ have μ(Y) > 0. Then u_γ = 0 a.e. on Y for *every* γ, so the element (1⊗χ_Y)u has Fourier coefficients [(1⊗χ_Y)u]_γ = χ_Y·u_γ = 0 for all γ, whence (1⊗χ_Y)u = 0 by coefficient determination (Step 0(ii)). Multiplying by u\* on the right: 1⊗χ_Y = 0, contradicting μ(Y) > 0. (No Parseval-type identity and no trace is needed; faithfulness of coefficient determination suffices.)

**Step 5 (conclusion).** By Steps 3–4, for a.e. x ∈ X there is γ ∈ Γ with T⁻¹x = γ⁻¹x ∈ Γx. Hence graph(T⁻¹) ⊂ R_Γ mod null, and since R_Γ is symmetric, T ∈ [R_Γ]. Uniqueness mod null is Step 1. ∎

## 3. Remarks

1. **Generality.** The proof uses only that the P-leg carries the trivial A₀-action; P is arbitrary. In particular the statement holds for the arena 𝒞 ≅ B(H) ⊗̄ (L∞(S¹)⋊Γ) with A = 1⊗L∞(S¹): *every unitary of 𝒞 normalizing the base acts on it by an element of [R_Γ]* — the (P1) premise of phase 104 §3/§7, now with its own proof.
2. **Relation to Feldman–Moore.** For P = ℂ this recovers (one direction of) the Feldman–Moore normalizer picture for the Cartan pair L∞(X) ⊂ L∞(X)⋊Γ; the content of the amplification is that a large fiber with trivial action cannot enlarge the normalizer's action on the base — the A₀-bimodule support of M stays concentrated on R_Γ because the fiber contributes only the diagonal.
3. **With essential freeness** (which holds for torsion-free cocompact Fuchsian boundary actions — nontrivial elements are hyperbolic with two fixed points, a null set; the torsion caveat of phase 100 stands), the γ realizing T on S_γ is a.e. unique, and the S_γ induce mod null the familiar countable partition of X on which T agrees with single group elements.
4. **What this repairs, and what it does not.** This closes phase 104 §7.3 **C2**: phase 103's step "unitaries of 𝒞 normalizing the base implement [R_Γ]" now rests on a printed proof rather than an inapplicable citation, and — combined with the [R_Γ] one-parameter-group triviality (phase 103 §2) — the fired kill's printed pedigree is whole for its stated scope. It does **not** touch the Referee-1 residue (phase 104 §7.1): one-sided and skew motion of the base by modular flows of general normal states remain open exactly as recorded; this lemma concerns honest normalizers only.

## 4. Amendment (2026-07-24, same session) — the referee pass: verdict and contributions

**Verdict: LEMMA TRUE; PROOF CORRECT AFTER ONE REPAIR** (context-free adversarial referee; report verbatim in `reviews/REPORTS-phase104-JOIN4c-referee-2026-07-24.md`). Per-step: Steps 0, 1, 2, 4, 5 CORRECT (Step 2's γ-vs-γ⁻¹ audit passed, cross-checked on u = λ_g; the referee further notes such an error could anyway only relabel the realizing element, never move graph(T⁻¹) out of R_Γ). Step 3: GAP, repaired.

- **R1 (the one repair, applied above in Step 3):** "countable algebra generating the Borel σ-algebra mod null" does not imply point separation — the referee's counterexample scheme saturates a generating algebra along an injective Borel map into a null set, leaving a positive-measure family of unseparated pairs. Repair: take 𝒜 point-separating (standard Borel supplies one); mod-null generation is then not needed at all.
- **[Referee-contributed] Proof of coefficient determination (Step 0(ii)), previously asserted:** if E(xλ_γ\*) = 0 for all γ, then for finite sums y = Σλ_{γ_i}q_i bimodularity gives E(xy) = 0; Kaplansky density supplies a bounded net y_i → x\* σ-strongly; σ-weak continuity of left multiplication and normality of E give E(xx\*) = 0; faithfulness gives x = 0. Valid in all types; no trace.
- **[Referee-contributed] Strengthening — the separable-predual hypothesis on P can be dropped:** replace the pointwise Step-3 apparatus by the central support z_γ ∈ L∞(X) of u_γ over ℂ⊗L∞(X): from f·u_γ = 0 (f central scalar) one gets χ_{|f|>ε}·u_γ = 0 for every ε > 0, so f vanishes on supp z_γ =: S_γ; Step 4 becomes 1 − ⋁_γ z_γ = 0. No point evaluation anywhere; **P arbitrary**. The hypotheses genuinely consumed are exactly: Γ countable (Step 4) and (X, μ) standard (Steps 1, 3).
- **Strongest version (referee's formulation, adopted):** *X standard, Γ countable acting nonsingularly, N = L∞(X)⋊Γ any type, P any von Neumann algebra, M = P⊗̄N, A = 1⊗L∞(X). If u ∈ U(M) normalizes A, the induced β is a∘T⁻¹ for T ∈ [R_Γ], unique mod null; moreover the central supports S_γ of the Fourier coefficients cover X mod null and T⁻¹ = γ⁻¹ a.e. on S_γ.*
- **Remarks confirmed:** Remark 2 with the precise reading — this is the *automorphism direction* of the Feldman–Moore normalizer picture only (the decomposition u = a·u_T needs the Cartan/free setting, deliberately not assumed; the lemma is slightly more general than the FM context since freeness is dropped). Remark 3 confirmed: under essential freeness the S_γ are a.e. pairwise disjoint and the realizing γ is a.e. unique; without freeness uniqueness fails badly (trivial action), which is why only existence is asserted.

**Consequence entered:** phase 104 §7.3 **C2 is closed** — phase 103's [R_Γ] step now rests on this refereed lemma in place of the inapplicable Feldman–Moore citation; combined with the [R_Γ] one-parameter-group triviality (phase 103 §2), the fired kill's printed pedigree is whole for its stated scope. The Referee-1 residue (skew/one-sided motion) remains open exactly as recorded.

---

*Signature and responsibility statement: [SIGNATURE BLOCK — see template; a named human signatory completes this before circulation. The lemma and proof are elementary given standard crossed-product theory and are printed in full above; the referee verdict and all referee contributions are recorded in §4 and the report is preserved verbatim in the reviews folder.]*
