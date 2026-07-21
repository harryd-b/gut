# Phase 11 — The Euclidean–Lorentzian bridge (the last gate)

**Where we are.** Phases 8–10 reduced the whole internal monopole-Floer ↔ sector correspondence to **one** remaining gate: linking the Euclidean Chern–Simons–Dirac (CSD) Morse theory that computes $HM(\Sigma)$ to the Lorentzian sector Hilbert space of the Seiberg–Witten QFT on $\mathbb{R}\times\Sigma$. Naively this is "analytically continue everything," which is hopeless. The right move is to use the **supersymmetric** structure that $HM$ already carries. This document does that.

**Verdict (one line).** The gate is **substantially closed, not fully**. Via Witten's supersymmetric Morse theory, $HM(\Sigma)$ **is** the space of supersymmetric (BPS) ground states of a quantum mechanics whose superpotential is the CSD functional — i.e. the Hilbert space the topologically-twisted SW theory assigns to $\Sigma$. Osterwalder–Schrader reflection positivity on the cylinder $\mathbb{R}\times\Sigma$ then reconstructs a Lorentzian Hilbert space in which $HM(\Sigma)$ sits **as the BPS/protected sector**, with positive norm. This **derives** all three dictionary clauses (vacuum tower, offset, bound states) **for the BPS sector** — upgrading them from "structurally confirmed" to "derived." The residual gap shrinks from "Euclidean vs. Lorentzian for everything" to two named, smaller items: **(a) BPS sector vs. full sector**, and **(b) rigorous OS positivity for the interacting (untwisted) theory**. And there is a real reason to think (a) is *small*: superselection charges are precisely the *locally-unmovable, protected* quantities — the same kind of thing BPS states are.

---

## 1. Why not brute-force analytic continuation

The full Lorentzian sector Hilbert space contains all excited states; reconstructing it from Euclidean data requires the full OS machinery (reflection positivity for all correlators of the interacting theory), which is not available for the SW QFT on a general curved $\mathbb{R}\times\Sigma$. But $HM(\Sigma)$ is not the full Hilbert space — it is a finite/graded, highly structured object. The strategy is to identify *what subspace* of the Lorentzian theory $HM$ is, and bridge only that. The answer is the **protected (BPS/ground-state) sector**, where everything is controlled.

---

## 2. Step 1 — $HM(\Sigma)$ = supersymmetric ground states (Witten–Morse)

**Witten (1982), "Supersymmetry and Morse theory":** for a superparticle on a Riemannian manifold with a Morse function $f$ used to deform the supercharge, the **supersymmetric ground states** are in bijection with the Morse complex of $f$ — topology (Betti numbers) appears as the *number of SUSY ground states*, and instanton (tunneling) corrections to the supercharge reproduce the Morse differential.

Floer's 3-manifold theory is exactly the infinite-dimensional version: take the configuration space of $U(1)$-connection–spinor pairs on $\Sigma$ mod gauge, with the **Chern–Simons–Dirac functional** as $f$. Then:
- critical points of CSD = solutions of the **3D Seiberg–Witten equations** on $\Sigma$ (the Floer generators);
- gradient flow lines = solutions of the **4D SW equations on $\mathbb{R}\times\Sigma$** (the cylinder!) = instanton tunneling;
- the resulting Morse homology = **monopole Floer homology $HM(\Sigma)$**.

**Therefore $HM(\Sigma)$ is, by construction, the space of supersymmetric ground states of a quantum mechanics whose "time" is the $\mathbb{R}$ direction of the spacetime and whose configuration space is the SW field space on $\Sigma$.** It is already a *space of quantum states*, not merely an abstract homology group — and the Euclidean "time" of the Floer/Morse picture is literally the spacetime $\mathbb{R}$ direction. This is the conceptual heart of the bridge.

The grading: the homological/Maslov grading is the **fermion number / charge** of the SUSY QM; the $U$-action (degree $-2$) is the standard descendant/charge operation. So the structures the dictionary needed (charge ladder, offset, generators) are already present as quantum-mechanical data.

---

## 3. Step 2 — this SUSY QM is the twisted SW theory on $\mathbb{R}\times\Sigma$ (TQFT)

Seiberg–Witten theory on a 4-manifold is the **topological (Donaldson–Witten) twist** of the abelian monopole sector of an $\mathcal{N}=2$ theory; twisting is precisely the device that **preserves part of the supersymmetry on a curved Euclidean background**, making the path integral metric-independent and localizing it onto SW solutions. In this language:
- the twisted SW theory is a TQFT that assigns to a closed 4-manifold $X$ its **SW invariant** (partition function) and to a 3-manifold $\Sigma$ a **Hilbert space — exactly $HM(\Sigma)$** (states on the spatial slice);
- the cylinder $\mathbb{R}\times\Sigma$ is the "time evolution," and its BPS/ground states are the Floer generators (localization: the path integral is saturated by SW solutions).

So $HM(\Sigma)$ is the **TQFT Hilbert space on $\Sigma$** for the twisted theory. The twist is what makes the Euclidean Floer computation well-defined and metric-independent on a curved $\Sigma$ — it is a feature, not a bug, and it is *why* the correspondence to topology works at all.

---

## 4. Step 3 — Osterwalder–Schrader on the cylinder, restricted to BPS

**Osterwalder–Schrader reconstruction:** Euclidean correlators satisfying **reflection positivity** (positivity under reflection in the Euclidean time axis) analytically continue to a **unitary Lorentzian QFT**; reflection positivity ⟺ Lorentzian unitarity, and the OS inner product's quotient-completion **is** the physical Hilbert space.

On the cylinder $\mathbb{R}\times\Sigma$ with $\mathbb{R}$ as Euclidean time, reflection is in that axis. The key point: **on the supersymmetric/BPS sector, reflection positivity holds and is essentially the statement that BPS states have positive norm.** The SUSY inner product restricted to ground states (harmonic representatives of the Floer/Morse cohomology) is positive-definite — this is the same positivity that makes Hodge-theoretic harmonic representatives a genuine Hilbert space. Hence OS reconstruction applied to the protected sector yields:

$$
\boxed{\ HM(\Sigma)\ \hookrightarrow\ \mathcal{H}^{\text{Lor}}_{\text{sector}} \quad\text{as the BPS (protected) subspace, with positive norm.}\ }
$$

The Euclidean Floer generators become honest Lorentzian states; the Floer grading becomes the conserved charge/fermion number; the $U$-tower becomes the Lorentzian charge ladder. This is the bridge — for the protected sector.

---

## 5. What is now derived (and what the gate has shrunk to)

**Derived (for the BPS/protected sector):** all three dictionary clauses, previously only "structurally confirmed," now follow from Steps 1–3:

| clause | status before | status now |
|---|---|---|
| vacuum tower = global-$U(1)$ charge ladder | confirmed structurally ($S^3$) | **derived**: the $U$-tower is the BPS charge ladder in $\mathcal H^{\text{Lor}}$ |
| Frøyshov $h$ = sector ground-state grading | confirmed ($\Sigma(2,3,5)$) | **derived**: $h$ is the BPS vacuum's charge/fermion grading offset |
| irreducibles = charged-matter bound states | classical ($\Sigma(2,3,7)$), quantum gated | **derived for BPS**: irreducible SW solutions = BPS charged bound states in $\mathcal H^{\text{Lor}}$; rank $HM_{red}$ = their number |

**The residual gap, now two smaller named items:**

1. **BPS sector vs. full sector.** $HM(\Sigma)$ is the *protected* part of $\mathcal H^{\text{Lor}}_{\text{sector}}$, not all of it. The full sector has non-BPS excited states $HM$ does not see. So the correspondence derives the *protected content* of each superselection sector, not its entire Hilbert space.
2. **Rigor for the interacting, untwisted theory.** OS reflection positivity is rigorous for free theories and controlled (via SUSY/localization) on the BPS sector; full OS positivity for the *interacting, untwisted* SW QFT on a general curved $\mathbb{R}\times\Sigma$ is **not** rigorously established. So Step 3 is rigorous on the protected sector and formal beyond it.

This is a genuine reduction: from "the entire Euclidean–Lorentzian link is open" (Phase 8) to "the link is established on the protected sector; what remains is (a) whether protected = all that matters for superselection, and (b) constructive-QFT rigor for the full interacting theory."

---

## 6. Why gap (a) may be small — superselection is itself "protection"

A real argument, offered as suggestive not proven. **Superselection charges are exactly the quantities that cannot be changed by any local operation** — DHR charges, fluxes, the $c_1\in H^2$ labels of Phase 5. They are *topologically/algebraically protected*. **BPS states are exactly the states protected by the SUSY algebra** (saturating the energy bound, robust under continuous deformation). These two notions of "protected" are not obviously the same, but they are deeply aligned: both are the data that survives coarse-graining, deformation, and local disturbance. So the protected (BPS) sector that $HM(\Sigma)$ captures is plausibly *precisely* the superselection-relevant content — the non-BPS excitations are the local, createable, non-superselected states that superselection theory deliberately quotients out. If this alignment is exact, **gap (a) closes**, and $HM(\Sigma)$ is not a fragment of the sector data but the whole of the superselection-relevant data. Making this precise — "superselection content = BPS content for the SW QFT" — is the sharp next question.

---

## 7. What this means for the bet

- **Plank II ∩ Plank III** (the corner that survived the exotic-smoothness divide) now has: a **proved label theorem** (Phase 8), **clause-by-clause confirmation** (Phases 9–10), and now a **derivation of the internal correspondence on the protected sector** (this phase), with the residual gap reduced to two named, plausibly-small items. This is a real, layered result — the most developed part of the entire program.
- **Honest scope, unchanged:** still globally hyperbolic and non-exotic (no Plank I content — the exotic frontier remains across the Phase-7 divide), still specific to the SW abelian-monopole QFT.
- **A structural bonus for the whole bet:** the bridge works *because* the theory is supersymmetric/topological. This quietly says the geometry-first correspondence is most natural in a **protected/topological** sector — consistent with the recurring Phase-3/7 finding that the bet lives where ordinary dynamics is suppressed (no S-matrix, no global hyperbolicity, and now: the protected sector). The three "sacrifices" (S-matrix, global hyperbolicity, non-protected states) keep pointing the same way: the bet's natural home is the topological/protected stratum of physics.

---

## 8. Verdict and next sub-questions

The last gate is mostly through. The internal correspondence is derived on the protected sector; what remains is sharp and bounded.

1. **[The crux now] Superselection content = BPS content?** Make §6 precise for the SW QFT: is the superselection-relevant data of a sector exactly its BPS content? A "yes" closes gap (a) and turns the whole internal correspondence into a theorem (modulo constructive rigor). **Highest leverage.**
2. **[Constructive rigor] OS positivity for the interacting SW QFT** on $\mathbb{R}\times\Sigma$, at least perturbatively or on special $\Sigma$ — gap (b).
3. **[Multi-sector] $\Sigma_g\times S^1$**: test the derived correspondence with several sectors at once (carried over from Phase 10).
4. **[Cross to the frontier] Protected invariants in the non-globally-hyperbolic regime.** The bet's recurring lesson is that its home is the protected stratum; end-periodic / instanton-Floer invariants (which detect exotic ends) are protected invariants that *do* extend past global hyperbolicity. This is the one route by which Plank I (exotic smoothness) could re-enter the now-derived Plank II∩III machinery. Scope whether a "protected-sector AQFT" survives where the full theory doesn't.

**Recommended next step:** sub-question 1 — it is now the single statement standing between the internal correspondence and a theorem, and §6 already sketches why it should hold.

---

## 9. Methodological note

The bridge looked like a wall in Phase 8 ("Euclidean vs. Lorentzian") and turned out to be mostly passable once approached through the *supersymmetric* structure $HM$ already had — Witten–Morse + topological twist + OS-on-BPS. The honest gain is precise: not "the bridge is built" but "the bridge is built on the protected sector, and here are the two smaller things left." The recurring meta-lesson sharpened again: the geometry-first correspondence is natural exactly in the **protected/topological** stratum — the same address (suppress ordinary dynamics) the bet has been driven toward at every junction. That convergence remains the most interesting structural fact the program has produced.

---

## Sources
- Witten, "Supersymmetry and Morse theory," *J. Diff. Geom.* 17 (1982) 661 — SUSY ground states = Morse complex; instantons = tunneling = gradient flow; Floer's 3-manifold generalization: [supersymmetric quantum mechanics — nLab](https://ncatlab.org/nlab/show/supersymmetric+quantum+mechanics); [Topology and physics — a historical essay (arXiv:hep-th/9709135)](https://arxiv.org/pdf/hep-th/9709135).
- SW theory as topological (Donaldson–Witten) twist of $\mathcal N=2$; twisting preserves SUSY on curved Euclidean space; localization (saddle point exact); coupling to $\mathrm{Spin}^c$: [Vergouwen–De Haro, "Supersymmetry in the Seiberg–Witten Theory" (arXiv:2409.04811)](https://arxiv.org/pdf/2409.04811); Witten, "Monopoles and Four-Manifolds," *Math. Res. Lett.* 1 (1994).
- BPS states from the SUSY algebra; protected, geometry-dependent; topological solitons: [Vergouwen–De Haro (arXiv:2409.04811)](https://arxiv.org/pdf/2409.04811).
- Osterwalder–Schrader reconstruction: reflection positivity ⟺ Lorentzian unitarity; Hilbert space + Hamiltonian reconstructed from Euclidean correlators: [Schwinger function / OS reconstruction overview](https://grokipedia.com/page/Schwinger_function); [Jaffe, "Reflection Positivity" lectures (arXiv:1802.09037)](https://arxiv.org/pdf/1802.09037).
- Monopole Floer as TQFT Hilbert space on $\Sigma$ / cobordism maps: Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (CUP 2007); [Manolescu (arXiv:1508.00495)](https://arxiv.org/pdf/1508.00495).
