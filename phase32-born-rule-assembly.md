# Phase 32 — M0b/M0c executed: the Born rule and statisticality as outputs of the folded geometry

*Working session, 2026-07-11. Executes scorecard milestones M0b (Born rule forced) and M0c (statisticality forced) from phase 31, class V. Method: theorem assembly with every imported result attributed, every hypothesis audited against the framework's geometric algebra, and an explicit expert-audit list (§8) for the operator-algebraic facts that must be confirmed before this is shown to a referee. Nothing below is claimed as new mathematics; the claimed contribution is the assembly and its geometric reading — per the phase-29 sweep, the chain "GV foliation ⇒ Gleason-forced Born rule" appears in no prior literature.*

---

## 0. Aim and framing

**Claim to be established.** Let M be the observable algebra that the framework's geometry produces — the von Neumann algebra of a codimension-1 foliation (Σ,F) with GV ≠ 0, restricted to its type III factor component (§1). Then:

- **(M0b — Born rule forced):** every consistent probability assignment on the yes/no events of M *is* a quantum state; the Born rule is not a postulate but the unique probability calculus on the folded geometry's event lattice.
- **(M0c — statisticality forced):** M admits **no dispersion-free states at all** and **no pure normal states**; every physical state is intrinsically mixed and thermal (KMS) with respect to its own modular flow. Determinism is not merely false in this world — it is *structurally impossible*, and the impossibility is caused by the same geometric datum (the fold, GV ≠ 0) that generates the clock (§4.1 of the core document).

**What "derived" means here.** Derived from: (i) the geometric primitives (Σ, F, GV ≠ 0) via theorem links V.1–V.2; (ii) the premise that physical events are the projections of the geometric algebra (the "event premise," audited in §6); (iii) standard operator-algebraic theorems (attributed below). NOT derived: the identification of M with the algebra of *our* laboratory observables — that is the V.7/T1 join, the program's standing bottleneck, and it is flagged wherever it matters.

## 1. The object: the geometric event lattice

By V.1 (Connes): the holonomy groupoid G of (Σ,F) yields the C*-algebra C*_r(Σ,F) and, in the GNS representation of a suitable transverse weight, the **foliation von Neumann algebra** M₀ = W*(Σ,F). Noncommutativity is geometric: it is the holonomy of the leaves.

By V.2 (Hurder–Katok): GV ≠ 0 ⟹ M₀ has a nontrivial **type III component**. Write M for that component; for the Thurston-type foliations of S³ used by the program (and by AMK, who assert the factor property with subtype III₁), M is a factor — we carry the audit item **[A1]**: *factoriality (ergodicity of the transverse flow) and the subtype for the specific foliations must be confirmed; the assembly below needs only "type III von Neumann algebra, no type I₂ direct summand," which the type III component satisfies by construction.*

**The event lattice** is P(M) = {p ∈ M : p = p* = p²}, the orthomodular lattice of projections — the geometry's yes/no questions (in the foliation reading: holonomy-localized measurable propositions about the transverse structure). A **probability assignment** is a map μ: P(M) → [0,1] with μ(1) = 1 and μ(p+q) = μ(p) + μ(q) whenever pq = 0 (finite additivity on orthogonal events); **complete additivity** (over arbitrary orthogonal families) is the physically natural strengthening for normal-state physics.

## 2. The imported theorem (generalized Gleason)

**Theorem (Gleason 1957; extended to von Neumann algebras by Christensen, Yeadon, Paszkiewicz et al.; finitely-additive case completed by Bunce–Wright 1992; monograph treatment: Hamhalter, *Quantum Measure Theory*, 2003).** Let N be a von Neumann algebra **with no direct summand of type I₂**. Then every finitely additive probability measure on P(N) extends to a **unique state** on N; completely additive measures correspond exactly to **normal states**. **[A2: exact statement and hypotheses to be spot-checked against Bunce–Wright, Bull. AMS 26 (1992) 288, and Hamhalter 2003, in the expert audit.]**

Remarks. (i) The I₂ exclusion is essential and sharp (the original dim-2 Gleason counterexamples). (ii) The content is that **additivity on orthogonal events forces linearity**: the measure, defined only on the non-linear lattice P(N), is revealed to be the restriction of a linear functional — this is precisely the Born rule's mathematical content.

## 3. Hypothesis audit for the geometric algebra

- **(H1) M is a von Neumann algebra.** ✓ — V.1 (Connes construction). [Theorem]
- **(H2) No type I₂ direct summand.** ✓ — M is the type III component (type-decomposition summands are unique; a type III algebra has, by definition, no type I part). If one prefers the full M₀: a type I₂ summand would be a two-dimensional atomic representation of the foliation algebra, which the audit item **[A3]** asks an expert to exclude for the relevant foliations (expected trivially; the factor route makes it moot).
- **(H3) Additivity class.** Both versions available: finite additivity suffices for the Born-rule conclusion (Bunce–Wright — the *strongest* form: even a finitely-additive assigner of probabilities cannot escape quantumness); complete additivity delivers normal states — the physically accessible class, in which the GNS standard form represents every probability as a vector/density-matrix expectation.

## 4. Theorem M0b (assembled): the Born rule as geometry's probability calculus

> **Let (Σ,F) be a codimension-1 foliated 3-manifold with GV(F) ≠ 0 and M the type III component of W*(Σ,F). Then every finitely additive probability assignment on the event lattice P(M) is the restriction of a unique state ω on M, and every completely additive assignment is a unique normal state. In the GNS representation, probabilities take the standard quantum form μ(p) = ω(p) = ⟨ξ_ω, π_ω(p) ξ_ω⟩. There is no other probability calculus on the folded geometry's events.**

*Proof:* assembly of §2 under the audit of §3. ∎ *(modulo [A1]–[A3])*

**Geometric reading.** The two hypotheses that carry all the weight — noncommutativity and the I₂ exclusion — are both *outputs of the geometry*: holonomy makes the algebra noncommutative (V.1), and the fold makes it type III (V.2), which excludes I₂ with room to spare. In this framework the correct answer to "why the Born rule?" is: *because the event lattice of a folded geometry admits no other additive probability theory.* The question "why is the world quantum?" is converted into "why is the event lattice P(M) for this M?" — which is the V.7 join, i.e., the framework's one bottleneck, not a new one.

## 5. Theorem M0c (assembled): statisticality and thermality forced

Under the same hypotheses (M a type III factor — [A1]):

1. **No dispersion-free states, at all.** A dispersion-free state (ω(a²) = ω(a)² for all self-adjoint a) is a character. A character's kernel is a norm-closed two-sided ideal of codimension 1; but **a type III factor is a simple C*-algebra** (every nonzero projection is equivalent to 1; norm-closed ideals of a von Neumann algebra are generated by their projections — audit item **[A4]** for the precise simplicity citation), so no such ideal exists. *Hidden-variable determinism is not false-in-practice; it is unavailable on this event lattice even through finitely-additive or singular states.* (For the {0,1}-valued-measure formulation, the generalized Kochen–Specker theorem — two-valued measures on P(N) exist iff N has an abelian direct summand; Hamhalter 2003 — gives the same conclusion from the lattice side. **[A5]**)
2. **No pure normal states.** Pure normal states exist only on type I factors (a pure normal state generates an irreducible GNS representation with minimal projections; type III has none). Every physical (normal) state of the folded geometry is **mixed**. [Standard; audit [A6] for the cleanest citation.]
3. **Intrinsic thermality.** By Tomita–Takesaki, every faithful normal state ω is KMS at β = −1 with respect to its own modular flow σ^ω — on a type III algebra this flow is *outer* (nontrivial as dynamics), so every accessible state of the folded geometry behaves as an equilibrium state of an intrinsic dynamics. This is the precise sense in which **the same fold produces the chance and the clock**: GV ≠ 0 ⇒ type III ⇒ (this section) statisticality *and* (§4.1 of the core) the modular time whose GV-pinning is Plank IV.
4. **Homogeneity (III₁ only — carries the [A1] subtype caveat).** If the factor is III₁, the Connes–Størmer transitivity theorem makes the normal state space *homogeneous*: any two normal states are approximately unitarily equivalent. Physics: no absolute "rest states"; every preparation is reachable from every other by an approximate symmetry — a strikingly egalitarian state space, unique to the III₁ world.

## 6. Scope, stated honestly (what these theorems do and do not establish)

- **The event premise.** Gleason-type theorems force the Born rule *given* that events are the projections of a von Neumann algebra and probabilities add on orthogonal events. A contextual hidden-variable theory evades the conclusion by rejecting the premise (this is Bell's old point about Gleason and the content of Kochen–Specker). The framework's position is that the premise is *supplied by the geometry* — the event lattice is handed to us by the foliation algebra, not chosen — but that defense is only as strong as the V.7 join.
- **The V.7 join (the bottleneck, unchanged).** Everything above concerns the foliation algebra. That the laboratory's observables *are* (a subnet of) this algebra is the program's central conjectural identification — the same join gating the gravity track (T1). M0b/M0c sharpen what rides on it: if V.7 holds, quantum probability and statistical physics are geometric necessities; if it fails, they remain theorems about an algebra nature doesn't use.
- **Not addressed here:** tensor/composite structure, complex-vs-real (the foliation algebra is canonically complex, but uniqueness is not argued), the emergence of specific observables and dynamics (Plank IV's job), and measurement-as-process (AMK's Casson-tower decoherence remains the adjacent candidate).

## 7. Scorecard effect

- **V.4 (Born rule): THEOREM (assembly to be written) → DERIVED (assembled; pending audit items A1–A5).** The program's **first fully in-house derived benchmark**, and it lands on the quantum track.
- **V.3 (statisticality): THEOREM → DERIVED (assembled; same caveats),** now with the sharper package: no dispersion-free states at all (not merely no normal ones), no pure normal states, intrinsic KMS thermality, and (III₁) state-space homogeneity.
- Class II unchanged; M1 (Unruh) is the natural next target and will reuse §5.3's modular machinery.

## 8. Expert-audit list (operator algebraist; est. one afternoon)

| # | Fact used | Where used | Confidence | Ask |
|---|---|---|---|---|
| A1 | Factoriality + subtype of W*(S³,F) for Thurston-type GV≠0 foliations | §1, §5.4 | medium (AMK assert III₁; §4.1 carries the component-vs-factor caveat) | confirm ergodicity/factoriality; subtype only needed for §5.4 |
| A2 | Generalized Gleason, finitely-additive form (Bunce–Wright 1992; Hamhalter 2003) | §2, §4 | high | spot-check statement/hypotheses |
| A3 | No I₂ summand of full W*(Σ,F) (moot on the factor route) | §3 | high | confirm or discard via factor route |
| A4 | Type III factors are simple C*-algebras | §5.1 | high | precise citation (Takesaki vol. II?) |
| A5 | Generalized Kochen–Specker: two-valued measures ⇔ abelian summand (Hamhalter) | §5.1 | medium | confirm exact statement |
| A6 | Pure normal states exist only on type I | §5.2 | high | cleanest citation |

*Status line: M0b and M0c are executed as theorem assemblies at mathematics level modulo the audit table — the first two class-V links to reach DERIVED. The claimed novelty is the assembly and geometric reading only; every component theorem is decades old, which is exactly what makes the assembly robust.*
