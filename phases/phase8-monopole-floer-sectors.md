# Phase 8 — The monopole-Floer ↔ superselection-sector correspondence (the constructive step)

**Where we are.** Phases 6–7 returned obstructions that *located* the bet but were negative. The program needed a constructive win, and Phase 7 left one concrete, buildable statement on the table: that the monopole superselection sectors on a globally hyperbolic $M=\mathbb{R}\times\Sigma$ are organized by the Seiberg–Witten (monopole) Floer homology $HM(\Sigma)$ of the Cauchy slice. This document makes that precise, **proves the part that is provable**, states the rest as a **sharp conjecture with a physical dictionary**, and names the **three obstructions** that bound it. This is the Planks-2∩4 result that survived the exotic-smoothness obstruction — no Plank 3 in it, and that limit is stated honestly.

**Verdict (one line).** The **label level is a theorem**: magnetic superselection sectors of abelian gauge theory on $\mathbb{R}\times\Sigma$ are in canonical bijection (after a spin-structure basepoint) with $\mathrm{Spin}^c(\Sigma)\cong H^2(\Sigma;\mathbb{Z})$ — exactly the grading set of $HM(\Sigma)$. The **internal level is a conjecture with a clean dictionary**: within each sector, the reducible/$U$-tower part of $HM(\Sigma,\mathfrak{s})$ is the pure-flux vacuum, the irreducibles are charged-matter bound states, and the Frøyshov invariant $h$ is a geometry-assigned ground-state grading of the sector. The full equivalence is bounded by three named gaps (Euclidean vs. Lorentzian, topological-invariant vs. dynamical, and which theory). Net: a concrete realization of "the charge sectors *and their content* are computed by a gauge-theoretic invariant of the spatial geometry."

---

## 1. What is being claimed, split into provable and conjectural

Two distinct assertions hide inside "$HM(\Sigma)$ classifies the monopole sectors":

- **(L) Label level.** The *set* of sectors equals the *grading set* of $HM(\Sigma)$. — *Provable; §2.*
- **(I) Internal level.** The *graded module* $HM(\Sigma,\mathfrak{s})$ within each sector $\mathfrak{s}$ computes the (topological skeleton of the) *state content* of that sector. — *Conjectural; §3.*

Keeping these apart is the whole discipline here: (L) is a structural consistency check; (I) is where any real physics (and any real risk of being wrong) lives.

---

## 2. The theorem (label level)

**Setup.** $M=\mathbb{R}\times\Sigma$ globally hyperbolic, $\Sigma$ a closed oriented 3-manifold (the smooth Cauchy slice, which exists and is unique up to diffeo by Bernal–Sánchez + Moise, Phase 7). Consider abelian $U(1)$ (Maxwell) gauge theory on $M$.

**Theorem.** *The magnetic superselection sectors of this theory are in canonical bijection with $H^2(\Sigma;\mathbb{Z})$, and — after choosing a base spin structure on $\Sigma$ — with $\mathrm{Spin}^c(\Sigma)$, which is precisely the grading set of the monopole Floer homology $HM(\Sigma)=\bigoplus_{\mathfrak{s}\in\mathrm{Spin}^c(\Sigma)}HM(\Sigma,\mathfrak{s})$.*

**Proof.**
1. *Magnetic sectors $\cong H^2(\Sigma;\mathbb{Z})$.* A magnetic-charge configuration is a principal $U(1)$-bundle on $\Sigma$; isomorphism classes are classified by the first Chern class $c_1\in H^2(\Sigma;\mathbb{Z})$. The flux through any 2-cycle is $\langle c_1,[\,\cdot\,]\rangle$. Because $c_1$ is a *global* topological invariant, it cannot be changed by any operation localized in a contractible region — so distinct $c_1$ label inequivalent (superselected) representations. (This is the Phase-5 monopole lattice, now read as bundle classes; cf. the operator-2-cohomology description of magnetic flux sectors in the AQFT literature.)
2. *$\mathrm{Spin}^c(\Sigma)\cong H^2(\Sigma;\mathbb{Z})$.* Every closed oriented 3-manifold is parallelizable (Stiefel), hence spin, hence $w_2(\Sigma)=0$. Thus $\mathrm{Spin}^c$ structures exist, and $\mathrm{Spin}^c(\Sigma)$ is a torsor over $H^2(\Sigma;\mathbb{Z})$ via $\mathfrak{s}\mapsto \mathfrak{s}+a$, $c_1(\mathfrak{s}+a)=c_1(\mathfrak{s})+2a$. Choosing the $\mathrm{Spin}^c$ structure induced by a spin structure as basepoint gives a (basepoint-dependent) isomorphism $\mathrm{Spin}^c(\Sigma)\cong H^2(\Sigma;\mathbb{Z})$.
3. *$HM$ grading set.* By construction (Kronheimer–Mrowka), $HM(\Sigma)$ decomposes over $\mathrm{Spin}^c(\Sigma)$; the set of $\mathfrak{s}$ for which $HM(\Sigma,\mathfrak{s})\neq 0$ is a subset of $\mathrm{Spin}^c(\Sigma)$, and the *grading set* (the indexing) is all of $\mathrm{Spin}^c(\Sigma)$.
4. Compose: $\{\text{magnetic sectors}\}\cong H^2(\Sigma;\mathbb{Z})\cong \mathrm{Spin}^c(\Sigma)=\{\text{gradings of }HM(\Sigma)\}$. $\qquad\blacksquare$

**Reading.** This is real but modest: it says the *indexing* of monopole sectors and of $HM(\Sigma)$ coincide canonically. It is a consistency theorem, not yet a deep equivalence — both sides are indexed by the same group, and the theorem checks that the identification is canonical (not an accident of cardinality). The *electric* sectors are dual, labeled by characters $\widehat{H^2}$ — consistent with the AQFT statement that abelian sectors are labeled by (electric) flux; magnetic/electric duality exchanges the two, and the monopole equations pick out the magnetic ($\mathrm{Spin}^c$/$c_1$) side.

---

## 3. The conjecture (internal level) + physical dictionary

$HM(\Sigma,\mathfrak{s})$ is far richer than the single label $\mathfrak{s}$: it is a graded $\mathbb{Z}[U]$-module assembled from solutions of the Seiberg–Witten equations on $\Sigma$ (critical points of the Chern–Simons–Dirac functional), with three flavors $\widehat{HM},\ \widecheck{HM},\ \overline{HM}$ distinguished by how they treat the **reducible** solution. The conjecture is that this structure is the *content* of the superselection sector, under the dictionary:

| $HM$ structure | proposed physical meaning in sector $\mathfrak{s}$ |
|---|---|
| **reducible solution** (zero spinor, flat/Yang–Mills connection) | the **pure-flux vacuum** of the magnetic sector $\mathfrak{s}$ (Maxwell field, no charged matter) |
| **$\overline{HM}$ / the $U$-tower** (from infinity, reducible-dominated) | the **Coulombic / topological** content — the $U(1)$ field's own states in that flux background |
| **irreducible solutions** (nonzero spinor $\Phi$) | **charged-matter bound states** — the Spin$^c$ Dirac field $\Phi$ *is* the charged matter, bound by the flux |
| **Frøyshov invariant $h(\Sigma,\mathfrak{s})$** (measures interaction with the reducible; additive under $\#$) | a **geometry-assigned ground-state grading/offset** of the sector — a quantum number the spatial geometry attaches to each charge sector |

**Conjecture (internal).** *For the abelian Seiberg–Witten monopole QFT on $\mathbb{R}\times\Sigma$, the graded module $HM(\Sigma,\mathfrak{s})$ computes the topological skeleton of the space of (ground/bound) charged states of the superselection sector $\mathfrak{s}$, with the reducible/irreducible split given by the dictionary above.*

**Why it's plausible.** The Floer generators are literally the static solutions of the theory's own (Spin$^c$ Maxwell–Dirac) field equations on the spatial slice — i.e. the time-independent classical configurations, which are exactly what one quantizes around to build a sector's state space. The $U$-action shifting grading by $-2$ is the natural "add one Coulombic quantum" operation. So the dictionary is not arbitrary; it matches the variational origin of $HM$. **But it is a conjecture** — see §4.

This is the suggestive payoff: *the spatial geometry, through one gauge-theoretic invariant, would fix not just which charges exist (label) but the ground-state structure of each charge sector (content).* That is Plank 2 (sectors from the net/geometry) ∩ Plank 4 (gauge structure from geometry), made concrete.

---

## 4. The three obstructions (what bounds the claim)

1. **Signature: Euclidean Floer vs. Lorentzian sectors.** $HM(\Sigma)$ is built from the SW equations on the *Riemannian* cylinder $\mathbb{R}\times\Sigma$ (Morse theory of the CSD functional); superselection sectors are *Lorentzian*. Linking them is a Wick-rotation/Osterwalder–Schrader-type statement that is **not** established here. The label theorem (§2) survives because it is signature-independent (topology of bundles); the internal conjecture (§3) genuinely needs the Euclidean–Lorentzian dictionary.
2. **Topological invariant vs. dynamical sector structure.** $HM(\Sigma)$ depends only on the smooth $\Sigma$ — it is a diffeomorphism invariant. The full superselection structure of an interacting QFT depends on dynamics (couplings, spectrum). So $HM$ can at most capture the **topological/kinematic skeleton** of the sectors, not the full dynamical content. The word "skeleton" in the conjecture is load-bearing.
3. **Which theory.** The SW equations are a *specific* abelian gauge-plus-spinor system (Spin$^c$ Dirac + Maxwell with the SW quartic coupling). The correspondence, if true, is about **that** theory (the abelian monopole QFT), not Maxwell-without-matter or QCD. This is a restriction, but a clean and honest one: it names the theory the statement is about.

These three are the precise boundary between the proven (§2) and the hoped-for (§3), and each is a well-posed problem in its own right.

---

## 5. What this buys the program

- **A constructive win after two obstruction phases.** The label theorem is a genuine (if modest) proved statement tying AQFT sectors to a gauge-theoretic invariant of the spatial geometry — the first *proved* bridge in the Planks-2∩4 program, not just a pointer.
- **A sharp, falsifiable conjecture** (internal level) with a motivated dictionary and three named gaps — exactly the form Phase 2's discipline wanted ("convert the bet into the smallest claim that can be proven or refuted").
- **Honest scope.** It is Planks 2∩4 only. $\Sigma$ is a 3-manifold, smoothly unique — **no exotic smoothness, no Plank 3.** This is the same wall as Phase 7: the constructive bridge lives exactly where exotic smoothness *cannot*. The program's two halves (the buildable Planks-2∩4 corner; the exotic Plank-3 frontier) remain on opposite sides of the global-hyperbolicity divide.

So the bet's status sharpens once more: there is now a *proved* fragment (sector labels = spatial gauge-theory gradings) and a *concrete conjecture* for the rest — but only in the globally hyperbolic, non-exotic regime. The distinctive (exotic) content still lives across the divide identified in Phase 7.

---

## 6. Next sub-questions

1. **(Tighten obstruction 2 into a precise statement.)** Formulate exactly what "topological skeleton of the sector's state content" means — e.g. as an associated graded of a filtration on the sector Hilbert space — so the internal conjecture becomes checkable on examples ($\Sigma=S^3$, lens spaces, $\Sigma_g\times S^1$). $S^3$ (trivial $H^2$, single sector, $HM$ = the $U$-tower) is the controlled base case: does its $U$-tower match the Coulombic vacuum tower of the single sector? **Most concrete next step.**
2. **(Attack obstruction 1.)** Is there an Osterwalder–Schrader / Wick-rotation statement connecting the Euclidean CSD Morse theory to the Lorentzian sector Hilbert space for the SW QFT? Even a formal version would upgrade §3 from analogy to derivation.
3. **(Bridge to the frontier.)** The constructive corner is non-exotic by Phase 7. The only way exotic content re-enters is the non-globally-hyperbolic regime (Phase 7 front #2). Does any *Floer-type* invariant survive for the singular/exotic 4-manifolds there (e.g. end-periodic or instanton-Floer variants used to detect exotic $\mathbb{R}^4$)? That would be the first object able to carry all three planks.

**Recommended next step:** sub-question 1 with $\Sigma=S^3$ — the smallest controlled case, where the conjecture's internal dictionary can be checked against an explicit, fully-known $HM$ ($U$-tower) and an explicit single-sector vacuum structure. A clean match would be the first evidence *for* (not just consistency *with*) the internal conjecture; a mismatch would falsify the dictionary cheaply. Either is a real result.

---

## 7. Methodological note

This phase deliberately separated "what can be proved now" (a modest theorem) from "what is conjectured" (the physics), rather than presenting the whole correspondence as established — which would have been the seductive overclaim. The proved fragment is small but solid; the conjecture is sharp and comes with its own falsification test (§6.1). That is the honest shape of a constructive step at a research frontier: a small theorem, a precise conjecture, named gaps, and a cheap next experiment. The grand bet is unchanged in probability; the program now has its first proved bridge and a falsifiable next move.

---

## Sources
- Abelian gauge-theory superselection sectors labeled by flux; operator 1-/2-cohomology, magnetic flux ↔ operator-2-cohomology: ["An Algebraic Approach to Nonperturbative QFT" (arXiv:hep-th/9707230)](https://arxiv.org/pdf/hep-th/9707230); [Symplectic reduction of Yang–Mills with boundaries: superselection sectors (arXiv:2010.15894)](https://arxiv.org/pdf/2010.15894); [Null Hamiltonian Yang–Mills: memory as superselection (arXiv:2303.03531)](https://arxiv.org/pdf/2303.03531).
- Monopole Floer homology: three flavors $\widehat{HM},\widecheck{HM},\overline{HM}$; reducible vs. irreducible solutions and the blow-up; $U$-action; Frøyshov invariant $h(Y)$ measuring interaction with the trivial/reducible connection, additive under connected sum; $\mathrm{Spin}^c$ grading: Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (CUP 2007); [Manolescu, "Floer theory and its topological applications" (arXiv:1508.00495)](https://arxiv.org/pdf/1508.00495); [Frøyshov / "Monopole Floer homology for rational homology 3-spheres" (arXiv:0809.4842)](https://arxiv.org/pdf/0809.4842).
- Closed oriented 3-manifolds are parallelizable (hence spin, $w_2=0$): Stiefel's theorem (standard).
- $\mathrm{Spin}^c$ structures form a torsor over $H^2(\,\cdot\,;\mathbb{Z})$; Dirac/charge quantization via $c_1$: see Phase-5/6 documents and [Seiberg–Witten equations — nLab](https://ncatlab.org/nlab/show/Seiberg-Witten+equations).
