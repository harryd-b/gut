# Phase 4 — The Doplicher–Roberts lead: gauge group from the geometry of the local net

**Where we are.** Document 2 forced the bet into algebraic QFT (drop the global S-matrix) and showed Planks 2 and 4 want that *same* framework. The obvious question: is there, inside AQFT, a rigorous statement that the *internal gauge group* is determined by the *local-algebra (geometric) structure*? There is. This document states it, shows it is genuinely the meeting point of Planks 2 and 4, reports a striking dimensional fact that resonates with Plank 3, reports the existing curved-spacetime extension that already makes "charges from topology" rigorous — and then is honest about the three gaps that keep this a lead rather than a result.

**Verdict (one line).** The Doplicher–Roberts theorem proves that a *compact gauge group is reconstructed canonically from the superselection structure of the net of local observable algebras* — i.e. from the algebra-of-regions data that the bet calls geometric. On curved spacetime this already shows **spacetime topology induces charge sectors** and the gauge group appears as a **Tannaka dual of a group bundle**. This is the rigorous home of "forces from geometry." But: (i) the category is *input*, not derived from pure geometry; (ii) DR gives *a* compact group, not *the* Standard-Model group; (iii) the observable *net itself* is presupposed, not built from $(M^4, e^a, \omega, T)$. The lead is real and under-explored; the bet's job is to close those three gaps.

---

## 1. The theorem, stated precisely

**DHR setup (Doplicher–Haag–Roberts).** Start from the net of observable algebras $\mathcal{O}\mapsto \mathfrak{A}(\mathcal{O})$ on spacetime (the same object Plank 2 makes primary). A *superselection sector* (a charge type) is described by a **localized, transportable endomorphism** $\rho$ of the global observable algebra:
- *localized*: $\rho$ acts as the identity on $\mathfrak{A}(\mathcal{O}')$ for any region causally disjoint from a chosen double cone;
- *transportable*: an equivalent $\rho$ exists in any other double cone.

These endomorphisms compose ($\rho\otimes\sigma := \rho\sigma$), have conjugates (anticharges), direct sums and subobjects, and an exchange symmetry $\varepsilon(\rho,\sigma)$ from moving one charge past another. So the charge sectors form a **rigid (symmetric, in $\geq 4$D) tensor $C^*$-category** $\mathcal{T}$, with a **statistical dimension** $d(\rho)$ and a **statistics phase** attached to each sector.

**Doplicher–Roberts reconstruction (1989–1990).** Every such symmetric tensor $*$-category with conjugates, direct sums, subobjects and $\mathrm{End}(\mathbf{1})=\mathbb{C}$ is **equivalent to the category of finite-dimensional unitary representations of a compact group** (more precisely a compact *supergroup*, the super-part encoding fermionic sectors), **unique up to isomorphism**. Concretely: from the observable net alone, DR construct *simultaneously*
$$\boxed{\ \text{observable net } \mathfrak{A}\ \xrightarrow{\ \text{DR}\ }\ \big(\text{field algebra } \mathfrak{F},\ \text{compact gauge group } G\big)\ }$$
such that $\mathfrak{A} = \mathfrak{F}^{G}$ (the observables are exactly the gauge-invariant part of the field algebra), and the superselection sectors are exactly the irreducible representations of $G$.

This is **Tannaka–Krein duality** (Tannaka 1939) in its modern (Deligne 1990) form: a symmetric tensor category *is* the representation category of a unique compact (super)group, and the group is recovered as the automorphisms of the forgetful/embedding functor.

**One-line meaning:** *the internal gauge group is not extra data — it is the Tannaka dual of the category of localized charges of the net.*

---

## 2. Why this is exactly the Plank 2 ∩ Plank 4 meeting point

- **Plank 2** says: take the net of local algebras (geometry → algebra) as primary; entanglement/Hilbert structure is its shadow (Reeh–Schlieder).
- **Plank 4** says: the internal gauge structure should come *from* the geometry, not be independent data.

DR delivers precisely the bridge between them: **the gauge group $G$ of Plank 4 is reconstructed from the very net of local algebras that Plank 2 takes as fundamental.** The arrow the bet wants — geometry $\to$ algebra of regions $\to$ internal gauge symmetry — is, in this corner, a *theorem*, not a hope. Both planks are served by the same object; this is the strongest formal foothold the program has found, and it is the natural place to plant the flag from Document 2's §6.

Note also: DHR gave the **first first-principles proof of spin–statistics** from this structure, and the statistical dimension is tied to particle spin. So the Wigner obstruction (particles = irreps; spin labels) and the gauge structure live in *one* categorical object here — which is the kind of unification of "the two no-go theorems' subject matter" the bet is after.

---

## 3. The 4D fact (a real, if partial, Plank-3 resonance)

The exchange symmetry $\varepsilon(\rho,\sigma)$ behaves differently by spacetime dimension, and the difference is sharp:

| spacetime dim | category type | statistics | gauge object |
|---|---|---|---|
| $1{+}1$, $2{+}1$ | **braided** | anyons; statistics phase any value, dimension can be non-integer | quantum-group / braided, *not* an ordinary group |
| $\geq 3{+}1$ (so **4D**) | **symmetric** (permutation) | statistics phase $\pm 1$; dimension $\in \mathbb{N}$ → **bosons & fermions only** | an **ordinary compact (super)group** |

So **$3{+}1$ is the threshold dimension at which DHR charges have honest permutation statistics and the reconstructed object is a genuine compact gauge group** (with Bose/Fermi alternative and integer multiplicities), rather than the braided/anyonic structures of lower dimensions.

*Honest caveat:* this makes 4 the **threshold/minimal** dimension for ordinary gauge structure, not the *unique* one (it holds for all $\geq 4$). It is therefore a *resonance* with Plank 3, not a proof of it — the uniqueness leg of Plank 3 still has to come from exotic smoothness (Donaldson/Seiberg–Witten), which is a different argument. But it is a second, independent sense in which 4D is exactly where the structure the Standard Model needs first appears cleanly. Worth recording; not worth overclaiming.

---

## 4. The curved-spacetime extension already makes "charges from topology" rigorous

This is the part that most directly advances the bet, and it already exists in the literature (Brunetti–Ruzzi; Ciolli–Ruzzi–Vasselli; "Superselection sectors and general covariance"; "Quantum charges and spacetime topology"). On a globally hyperbolic curved spacetime:

- Superselection structures become **categories of sections of presheaves of symmetric tensor categories** over the spacetime.
- Given an embedding functor, the superselection structure is a **Tannaka-type dual of a *locally constant group bundle*** — and that bundle "becomes a natural candidate for the role of the gauge group." *(So $G$ is promoted from a group to a group bundle over $M$ — gauge structure literally fibered over the geometry.)*
- **The nontrivial topology of spacetime induces new superselection sectors.** The charges factorize into a **DHR (charge) part** and a **topological part** that governs how the charge behaves when transported along paths — an **Aharonov–Bohm-type** effect read purely from geometry/topology.

Translated into the bet's language: *the topology of the 4-manifold contributes charge sectors and fibers the gauge group over spacetime.* That is "forces from geometry," partially and rigorously, today. It is exactly the kind of statement Plank 4 needs and the kind of mechanism (topology carrying physical DOF) Plank 3 gestures at. This is the live edge to push on.

---

## 5. The three honest gaps (why this is a lead, not a result)

1. **The category is input, not derived from pure geometry.** DR/Tannaka takes the symmetric tensor category $\mathcal{T}$ as *given* (it comes from the QFT's charge content) and returns $G$. It does **not** derive $\mathcal{T}$ from the bare smooth/metric structure of $M^4$. The curved-spacetime work shows topology contributes a *factor* (the AB part), but the *charge* part still comes from the matter content you put in. **The bet's real task:** show that the smooth/differential-topological structure of $M^4$ (this is where exotic smoothness / Seiberg–Witten could enter) *fixes, or constrains,* the category — not just contributes a topological twist.

2. **DR gives *a* compact group, not *the* Standard-Model group.** Reconstruction is an existence/uniqueness theorem: whatever symmetric tensor category you have *is* $\mathrm{Rep}(G)$ for a unique $G$. Getting $G = SU(3)\times SU(2)\times U(1)$ requires the category to already have that representation structure. Nothing here selects the SM. **Task:** find geometric/topological data on $M^4$ whose Tannaka dual is (or contains) the SM group — or honestly report that nothing generic does.

3. **The observable net itself is presupposed.** DHR/DR start from a net $\mathfrak{A}(\mathcal{O})$ — i.e. a quantum field theory already exists on the spacetime. The bet's Plank 1 wants the *net* to be a shadow of the geometry $(M^4, e^a,\omega, T)$. Constructing the net *from* the geometry (rather than assuming it) is unsolved and is where Planks 1–2 must do work this corner does not do for free.

These three gaps are the precise statement of *how far the rigorous bridge actually reaches* and *what the bet must add*. Naming them is the deliverable.

---

## 6. The sharp sub-questions this defines (Phase-5 candidates)

In increasing ambition:

1. **(Toy, doable.)** Take a concrete spacetime topology (e.g. $M^4$ with $\pi_1\neq 0$, or a chosen 2-cycle structure) and compute the *topological* superselection sectors it induces (the AB part), following Ciolli–Ruzzi–Vasselli. Deliverable: an explicit map *topology of $M^4$* $\to$ *abelian charge sectors*. This is "charge quantization from geometry" in a controlled case — and it is the rigorous descendant of the Kaluza–Klein charge-quantization fact the bet wanted *without* the extra dimension.
2. **(Core, hard.)** Formulate precisely: *which* feature of the smooth structure of $M^4$ could fix the non-topological (DHR charge) part of the category? Is there any handle by which exotic smoothness / Seiberg–Witten invariants enter the symmetric tensor category? This is the genuine fusion of Plank 3 and Plank 4, and appears genuinely open.
3. **(Foundational.)** State what it would take to *construct the observable net from the geometry* (gap 3). Even a no-go ("nets are underdetermined by $(M^4,g)$ alone, here's the missing data") would be a real result that sharpens Plank 1.
4. **(Frontier check.)** The *braided* Doplicher–Roberts program is active as of 2026 (arXiv:2602.08348). Check whether anything there changes the 4D symmetric-vs-braided story in a way relevant to the bet.

**Recommended immediate next step:** sub-question 1 — it is concrete, calculable with the curved-spacetime AQFT machinery, yields an explicit "topology → quantized charge" statement, and directly tests whether the bet's charge-from-geometry claim survives contact with a real calculation. It is the natural successor to Document 1's "smallest calculable claim" discipline.

---

## 7. Honest verdict

This is the best foothold the program has. The arrow "geometry/net → compact gauge group" is a theorem (DR/Tannaka), the 4D case is exactly the one giving ordinary gauge groups, and the curved-spacetime extension already turns *topology* into *charge sectors* with the gauge group fibered over spacetime. Planks 2 and 4 genuinely meet here, rigorously.

But the bridge reaches *from the net's charge category to the group*, not *from bare geometry to the charge category*, and not *to the specific SM group*. The three gaps in §5 are where the bet still has to do the work, and none is known to be closeable. So: a real lead, an under-explored and citable one, with a concrete first calculation (§6.1) that could produce a standalone result regardless of whether the grand bet ever closes. Probability of the grand bet is unchanged — low — but the program now has a *constructive* next step with a defined deliverable, which is exactly what Phase 2's discipline demanded.

---

## Sources
- DR reconstruction (compact gauge group + field algebra from the observable net): S. Doplicher & J. E. Roberts, "Why there is a field algebra with a compact gauge group describing the superselection structure in particle physics," *Commun. Math. Phys.* 131 (1990) 51 — [Springer](https://link.springer.com/article/10.1007/BF02097680); [Doplicher–Roberts reconstruction theorem — nLab](https://ncatlab.org/nlab/show/Doplicher-Roberts+reconstruction+theorem).
- DHR superselection, symmetric tensor categories, statistics dimension, 4D permutation vs low-D braided, Tannaka–Krein/Deligne: [Algebraic Quantum Field Theory — an introduction (arXiv:1904.04051)](https://arxiv.org/pdf/1904.04051); [On Superselection Theory of Quantum Fields in Low Dimensions](https://www.researchgate.net/publication/45872486_On_Superselection_Theory_of_Quantum_Fields_in_Low_Dimensions).
- Curved-spacetime / topology → superselection sectors, group bundle as gauge group, AB-type topological charges: [Brunetti–Ruzzi, "Superselection Sectors and General Covariance. I" (arXiv:gr-qc/0511118)](https://arxiv.org/pdf/gr-qc/0511118); [Ciolli–Ruzzi–Vasselli, "Presheaves of Superselection Structures in Curved Spacetimes," Commun. Math. Phys. (2015)](https://link.springer.com/article/10.1007/s00220-014-2251-2); ["Quantum charges and spacetime topology" (arXiv:0801.3365)](https://arxiv.org/pdf/0801.3365).
- Active braided DR program (2026): [The braided Doplicher–Roberts program (arXiv:2602.08348)](https://arxiv.org/pdf/2602.08348).
- AQFT in curved spacetime (background): [Fewster–Verch / Hollands–Wald reviews (arXiv:1504.00586)](https://arxiv.org/pdf/1504.00586).
