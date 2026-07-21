# Phase 21 — Clearing the remaining open fronts (consolidated)

The scholarship/outreach step (front #1) is set aside as human-only. This phase clears the rest of what can be done in-room: the two consequential fronts (#2 non-SUSY geometry→dynamics; #3 derive the gauge connection), the AMK audit (#5), and the tractable small items. Several connect, and the result is a genuinely unifying closing picture — **the two faces of geometry-first (protected/SUSY vs. exotic/non-SUSY) are separated by the global-hyperbolicity divide, and each gives a different partial answer to "forces from geometry."**

---

## Front #2 — Is there a non-SUSY "geometry → dynamics" principle? **Closes: no (cleanly).**

The candidate from Phase 20 was **tt\* geometry**. Doing the check:

- **The mathematics is SUSY-free.** tt\* geometry *is* **non-abelian Hodge theory / harmonic bundles** (Cecotti–Vafa ↔ Simpson): a 1–1 correspondence between representations of $\pi_1$ and polystable Higgs bundles, a purely mathematical structure (a harmonic metric on a flat bundle) needing no supersymmetry.
- **But the *dynamics-fixing power* needs protection.** The statement "this geometry **fixes the effective action**" relies on the metric being the *protected* ground-state metric — i.e. on the $(2,2)$/holomorphic (chiral-ring) structure that makes it rigid and corrections-free. Strip the $(2,2)$ structure and the harmonic-bundle geometry still *exists*, but it no longer **determines** the dynamics: the ground-state metric receives uncontrolled corrections.

**Verdict.** No fully unprotected "geometry → dynamics" principle. The geometric principle's reach is **exactly coextensive with a protecting structure** — and that protection can be called *spacetime SUSY*, *worldsheet $(2,2)$*, or *holomorphy*, but it cannot be removed. This is the **same** answer as the whole program (geometry-first = the protected stratum), now confirmed for the deepest physics question. **The original fully-non-SUSY bet, in the "geometry fixes unprotected dynamics" form, is dead.** What survives is "needs a protecting structure" — which is the Phase-19 descendant. *(Sharpened open remnant: does harmonic-bundle geometry fix dynamics with a protecting structure weaker than $(2,2)$ — e.g. a single holomorphic structure, no full SUSY? That is the last crack of light, and it is a real math-physics question.)*

---

## Fronts #3 + #5 — Can the gauge connection be derived from geometry? **Closes: regime-dependent — and this is where the original bet still lives.**

Two regimes, two answers — split exactly by the **global-hyperbolicity divide** (Phase 7):

**(a) Protected / globally hyperbolic regime (our rigorous corner).** The gauge connection is **independent data**. Assembled verdict: it is not torsion (Doc 1: wrong rep/gauge group), cannot be merged into the frame-bundle structure group without SUSY (Phase 3: Coleman–Mandula), and even in the SW/special-geometry picture the field $A$ is a degree of freedom, not a functional of $(e,\omega,T)$. Geometry fixes the gauge **group** (topology: $\widehat G$ = Pontryagin dual of $H^2(\Sigma)$, Phase 14) and the **protected dynamics** (special geometry, Phase 19) — **but not the connection itself.** So strong-form Plank III ("the SM gauge field is a functional of the 4-geometry") is **false** in this regime.

**(b) Exotic / non-globally-hyperbolic regime — the Asselmeyer-Maluga–Król program.** Here the *smooth structure itself* generates gauge structure, and this is the **original anti-SUSY bet's only living embodiment.** The chain is concrete:
$$\text{small exotic }\mathbb R^4 \;\leftrightarrow\; \text{codim-1 foliations of }S^3 \;\xrightarrow{\text{Godbillon–Vey}\in H^3(S^3,\mathbb R)}\; \text{SU(2) WZW} + \text{twisted K-theory} \;\xrightarrow{\text{claimed}}\; U(1)\times SU(2)\times SU(3).$$
**Honest audit:** the chain is serious, genuinely geometric, **SUSY-free**, and lives **exactly in the exotic, non-globally-hyperbolic regime our Phase-7 analysis said the exotic content must inhabit** — a real consistency with the whole program. It gets **SU(2) naturally** (Godbillon–Vey / WZW). **But:** the step to the *full* $SU(3)\times SU(2)\times U(1)$ goes through specific WZW-level / twisted-K-theory identifications that are **matched, not forced**; and it produces gauge-*group*/WZW data, not manifestly a dynamical SM *connection* with the right matter couplings. So: **partial, geometric, non-SUSY, unconfirmed.**

**Combined verdict on "forces from geometry."** In the protected regime, forces are *not* derived (group + protected dynamics are; the connection isn't). In the exotic regime, the smooth structure *does* generate gauge structure (AMK), partially and unconfirmedly. **The original bet survives only as the AMK exotic-smoothness program** — which is exactly where Phases 6–7 located the exotic content, and exactly the non-SUSY route front #2 left a crack open for. The whole program's pieces snap together here: **two faces of geometry-first, protected/SUSY and exotic/non-SUSY, on the two sides of the global-hyperbolicity divide.**

---

## Plank II worked example ($S^2\times S^1$) — concrete numbers for the universal/bulk split

$H^2(S^2\times S^1;\mathbb Z)=\mathbb Z\Rightarrow \widehat G=U(1)$. The 3+1D free $U(1)$ entanglement entropy is
$$S = \alpha L^2 - \gamma\log L + \cdots,\qquad \gamma = \underbrace{1}_{\text{topological}} + \underbrace{\tfrac{1}{45}}_{\text{local (anomaly)}} = \tfrac{46}{45}.$$
This **realizes Phase 17's split with actual numbers**: the **topological coefficient $-1$** is the universal, sector/geometry-derived piece (survives even as the charge mass $\to\infty$) — *geometric, Plank II ✓*; the **$-1/45$** is local conformal-anomaly physics — *not* sector-geometric (the non-protected bulk piece). So on $S^2\times S^1$: geometry (via $\widehat G=U(1)$) fixes the topological $-1$; the $-1/45$ is independent local dynamics. Clean confirmation that Plank II holds **exactly on the universal/topological part and not the local part** — the program's pattern, now with a number.

---

## Non-abelian topological charge — exists, concretely

Non-abelian Aharonov–Bohm sectors require non-abelian $\pi_1(\Sigma)$ (Phase 5). Concrete realization: take $\Sigma$ a flat or Seifert 3-manifold with $\pi_1$ a non-abelian finite group (e.g. the quaternion group $Q_8$, giving a quaternionic space form). Then the topological sector category is $\mathrm{Rep}(\pi_1)$ — a genuinely **non-abelian** sector structure from pure topology, with the DR-reconstructed gauge group $=\pi_1$ (a finite non-abelian group). This is the topological route to non-abelian charge structure — modest but concrete, and it shows the sector-from-topology mechanism is not limited to abelian groups.

---

## Side results (compact)

- **Axial-torsion pseudoscalar.** The axial part $S^\mu$ of torsion couples to the fermion axial current $j_5^\mu$; in minimal Einstein–Cartan, integrating out the non-propagating torsion yields the standard repulsive **4-fermion axial–axial contact term** $\sim (G\,)\,(j_5)^2$; if torsion is given a kinetic term it propagates as an **axion-like pseudoscalar** with gravitational-strength coupling to $j_5$. Standard EC result; a phenomenologically real (if tiny) ALP, independent of the grand bet.
- **Brans source of a Fintushel–Stern pair.** Two exotic structures $X_K$, $X_{K'}$ (differing by knot surgery) act as *different* effective gravitational sources (Brans/Asselmeyer); they are distinguished by their SW invariants $=$ Alexander polynomials $\Delta_K\neq\Delta_{K'}$. So the effective "exotic matter" content differs in a way indexed by the knot — qualitatively a real, computable-in-principle difference; a clean stress-energy number needs the Asselmeyer machinery.

---

## Closing synthesis: the open-items list is now exhausted of in-room work

After this pass, every open front is either **resolved in-room** (here), **awaiting a human step** (#1 scholarship/expert), or **a genuinely hard research problem** (constructive OS; AMK completeness to the full SM; harmonic-bundle dynamics with sub-$(2,2)$ protection). The unifying picture the closing pass crystallized:

> **Geometry-first has two faces, separated by the global-hyperbolicity divide:**
> - **Protected / globally hyperbolic / SUSY face** — rigorous, far-reaching (topology → sectors/entanglement; special geometry → low-energy dynamics), but gauge connection is independent data and exotic 4D content is *excluded*.
> - **Exotic / non-globally-hyperbolic / non-SUSY face** — the original bet's home; the smooth structure *generates* gauge structure (AMK: Godbillon–Vey → SU(2) WZW → claimed SM), but rigour is absent and completeness to the full SM is unconfirmed.
> 
> The deepest structural fact of the entire program is that these two faces are **the same divide** seen in every plank — and "geometry → dynamics" works on each only to the extent a **protecting structure** (SUSY, $(2,2)$, holomorphy, or — conjecturally — exotic-smoothness rigidity) is present.

That is the honest terminus. The bet is neither vindicated nor dead: it is **resolved into two partial, regime-separated faces**, with its rigorous successes, its single remaining physics crack (sub-$(2,2)$ protection / AMK completeness), and its human-step prerequisite (novelty check) all named.

---

## Sources
- tt\* geometry = non-abelian Hodge / harmonic bundles (SUSY-free mathematics): [Non-Abelian Hodge Theory notes](https://link.springer.com/chapter/10.1007/978-1-4939-2830-9_5); [tt\* in 3 and 4 dimensions (arXiv:1312.1008)](https://arxiv.org/pdf/1312.1008); non-SUSY application still using residual $(2,2)$: [tt\* and closed-string tachyons (arXiv:hep-th/0111155)](https://arxiv.org/pdf/hep-th/0111155).
- AMK: exotic $\mathbb R^4$ ↔ codim-1 foliations of $S^3$, Godbillon–Vey $\in H^3(S^3,\mathbb R)$, SU(2) WZW + twisted K-theory, claimed $U(1)\times SU(2)\times SU(3)$: [Asselmeyer-Maluga–Król, "Abelian gerbes, generalized geometries and exotic $\mathbb R^4$"]( https://arxiv.org/abs/1105.1557); [Exotic $\mathbb R^4$ and QFT (IOP)](https://iopscience.iop.org/article/10.1088/1742-6596/343/1/012011/pdf); [Higgs potential and confinement on exotic $\mathbb R^4$ (arXiv:1303.1632)](https://arxiv.org/pdf/1303.1632).
- $U(1)$ 3+1D entanglement: topological $-1$ (survives infinite charge mass) + local $-1/45$ = $-46/45$: [On the Entanglement Entropy of Maxwell Theory (arXiv:1801.01158)](https://arxiv.org/abs/1801.01158); [Entanglement entropy in (3+1)d free U(1) gauge theory, JHEP02(2017)101](https://link.springer.com/article/10.1007/JHEP02(2017)101).
- Non-abelian AB sectors require non-abelian $\pi_1$: [Aharonov–Bohm superselection sectors (arXiv:1912.05297)](https://arxiv.org/abs/1912.05297).
- Axial torsion → 4-fermion / axion-like: standard Einstein–Cartan (Hehl et al., RMP 48, 393). Brans/exotic source distinguished by SW = Alexander polynomial: [Fintushel–Stern; Asselmeyer-Maluga (arXiv:1101.3168)](https://arxiv.org/pdf/1101.3168).
