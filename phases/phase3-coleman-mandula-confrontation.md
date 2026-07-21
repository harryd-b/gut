# Phase 3 — Confronting the no-go theorems

**Where we are.** Document 1 showed the smallest test of Plank 4 ("EM is intrinsic 4D torsion") fails: torsion is a covariant tensor, its only gauge freedom is local Lorentz $\mathfrak{so}(1,3)$, and the frame bundle has no internal $U(1)$ factor. That last sentence is the local-algebra shadow of **Coleman–Mandula**. The only surviving door was (a) *enlarge the structure group, not the dimension* — which walks straight into the no-go theorems. This document does that confrontation honestly: it (1) confirms the obstruction is not a $U(1)$ accident, (2) states Coleman–Mandula precisely and finds the one escape coherent with the bet, (3) brings in the sharper companion theorem (Weinberg–Witten), and (4) states what the bet must become to survive — a much narrower, more defensible flag than where it started.

**Verdict (one line).** The bet survives Coleman–Mandula and Weinberg–Witten only by (i) giving up the global S-matrix — justified by background independence + cosmology + confinement — and (ii) treating the unified gauge fields as *co-fundamental data inside one connection*, **not** as composites emergent from a geometric substructure. Crucially, the escape door this forces is the **same algebraic-QFT framework Plank 2 already needs** — so the planks cohere on which assumption to drop. The cost is real: no S-matrix means rebuilding the particle concept itself, and no one has constructed a realistic gauge theory in that framework.

---

## 1. The obstruction is general: $U(1)\to SU(2)$ changes nothing (and adds a trap)

For $U(1)$ we needed a torsion projection that shifts inhomogeneously by $\partial_\mu\lambda$ (one scalar). For $SU(2)$ the gauge field $A_\mu = A_\mu^i\,\tau^i$ is $\mathfrak{su}(2)$-valued and transforms as

$$A_\mu \;\to\; U A_\mu U^{-1} + U\,\partial_\mu U^{-1}, \qquad U(x)\in SU(2),$$

so the required inhomogeneous (Maurer–Cartan) term $U\partial_\mu U^{-1}$ is $\mathfrak{su}(2)$-valued. Same structural demand as before — torsion would have to carry an inhomogeneous shift valued in an *internal* $\mathfrak{su}(2)$. It does not: torsion transforms homogeneously, and the frame bundle's structure group is $SO(1,3)$ (or affine $\mathbb{R}^4\rtimes GL(4)$), with no internal $\mathfrak{su}(2)$ factor. **Same failure, non-abelian.**

### The self-dual $\mathfrak{su}(2)$ trap (worth disarming once)

There is a seductive objection: the complexified Lorentz algebra splits,
$$\mathfrak{so}(1,3)_{\mathbb C}\;\cong\;\mathfrak{su}(2)_L \oplus \mathfrak{su}(2)_R$$
(the self-dual / anti-self-dual, or left/right, halves — exactly the Ashtekar self-dual-connection structure). So doesn't $\mathfrak{so}(1,3)$ *already contain* an $\mathfrak{su}(2)$ to be the weak group?

**No — and seeing why is instructive.** Those two $\mathfrak{su}(2)$'s act on *spacetime spinor/frame indices*; they **are** the Lorentz rotations and boosts. Identifying weak isospin with the self-dual half $\mathfrak{su}(2)_L$ would make weak isospin a **spacetime** symmetry that fails to commute with Lorentz boosts. Concrete contradiction: the members of a weak doublet $(\nu_e, e)^T$ would have to be related by a (chiral) Lorentz transformation — but they are *both* spin-$\tfrac12$, carry *different* electric charge and mass, and are distinct particles. Weak isospin is an internal quantum number that commutes with spin; the Lorentz $\mathfrak{su}(2)$ does not. So the "free" $\mathfrak{su}(2)$ inside $\mathfrak{so}(1,3)$ is exactly the wrong kind — it is spacetime, chiral, and non-commuting with boosts. This *is* Coleman–Mandula speaking in the small.

**Take-away:** the gauge content of the Standard Model must sit in the **internal** factor, which the frame bundle simply does not contain. Routing it through geometry therefore requires enlarging the structure group — and now we owe the theorems an answer.

---

## 2. Coleman–Mandula, stated precisely, and its escapes

**Theorem (Coleman–Mandula, 1967).** Under the assumptions below, the connected symmetry group of the S-matrix of a 4D QFT is *locally isomorphic to a direct product*
$$G \;=\; \text{Poincaré} \times G_{\text{internal}},\qquad G_{\text{internal}}\ \text{compact},$$
and the internal generators are Lorentz scalars. Spacetime and internal symmetries cannot mix nontrivially.

**The five assumptions (this is where all the action is):**

1. **Poincaré invariance** — $G$ contains the Poincaré group.
2. **Discrete spectrum / mass gap** — for any $M$, only finitely many one-particle types with mass $\le M$.
3. **Nontrivial scattering** — the S-matrix is not the identity; particles interact.
4. **Analyticity** — the S-matrix is analytic in $s,t$ (away from physical poles/cuts), i.e. **an S-matrix exists** with the usual properties.
5. **Technical** — generators act with distributional kernels in momentum space.

**The known escapes (each = violating one assumption):**

- **Graded algebra (SUSY).** Replace the Lie algebra with a Lie *super*algebra; the supercharges are spinors, not scalars. Haag–Łopuszański–Sohnius proved this is the **unique** loophole *within* assumptions 1–5. But SUSY is not "geometry-first" in your sense, and the LHC has not found it. *Not your door.*
- **No mass gap → conformal symmetry** (violate 2). A massless/conformal theory enlarges the spacetime side from Poincaré to the conformal group. *Discussed below — doesn't deliver the merger.*
- **No S-matrix** (violate 3/4). If asymptotic scattering states don't exist, the theorem's object of study is gone. *This is your door — see §3.*
- **Non-Poincaré spacetime symmetry** (violate 1): de Sitter, Galilean, Lorentz-violating theories. *Available but ideologically self-defeating for this bet — see §3.*
- **$D\le 2$**: no scattering angle. *Irrelevant in 4D.*

---

## 3. Which assumption must *this* bet drop? Going one by one.

The discipline here: not "which escape exists" but "which escape is *coherent with the bet's own commitments*" — 4D, Lorentzian, spacetime fundamental.

**Assumption 1 (Poincaré/Lorentz) — reject the door.** Breaking Lorentz invariance (Hořava–Lifshitz, analog/emergent-gravity models) does evade CM. But the whole content of Plank 1 is that the *Lorentzian* tetrad $e^a{}_\mu$ is ontologically primitive. Throwing away Lorentz invariance discards the very object you are making fundamental. *Available to others, incoherent for you.* Reject.

**Assumption 2 (mass gap) — partial, doesn't help.** Going massless/conformal evades CM, but (i) the real world *has* massive particles, so a strictly conformal theory isn't the world; conformal symmetry must break in the IR, and CM reasserts itself on the IR S-matrix. (ii) More fatally for Plank 4: even when it applies, the conformal escape still produces a **direct product** $\text{Conformal}\times G_{\text{internal}}$ — it *enlarges the spacetime factor* but still forbids putting gauge charge *into* it. So masslessness buys conformal spacetime symmetry, not the spacetime⊕gauge merger you want. *Doesn't deliver.*

**Assumption 3/4 (existence of an S-matrix) — this is the honest door.** Two independent physical reasons the S-matrix may not exist, both already true of the real world or forced by the bet:

- **(i) Confinement.** Colored states (quarks, gluons) are *not* asymptotic states; there is no S-matrix element with external quarks. CM's hypotheses literally fail for the confined sector. This is a standard, legitimate escape.
- **(ii) Cosmology / background independence.** An S-matrix needs asymptotic in/out regions (flat asymptotia or a well-defined asymptotic Hilbert space). A closed or de Sitter universe has **no global S-matrix** — horizons obstruct it; de Sitter famously lacks one. A genuinely background-independent, geometry-first gravitational theory on a cosmological $M^4$ plausibly has **no S-matrix at all.** This matches the framing in your synthesis exactly ("evading Coleman–Mandula through no asymptotic S-matrix — true in a confined or cosmological setting").

**This is the door.** And here is the payoff that makes it more than a dodge: dropping the global S-matrix forces you into **algebraic QFT in curved spacetime** — local von Neumann algebras $\mathcal{O}\mapsto\mathfrak A(\mathcal{O})$, no global particle number, the particle concept reconstructed locally. **That is precisely the framework Plank 2 already committed you to** (Reeh–Schlieder, the AQFT net as the source of the entanglement structure). So Planks 2 and 4 *want the same escape hatch.* The bet's pieces are not independent dodges; they cohere on dropping the same assumption. That is a genuine structural result, and a point in the bet's favor for internal consistency (not for truth — see costs).

**The honest cost.** Removing the S-matrix removes the *prohibition* but also your main *tool*. Essentially everything rigorous in particle physics — the particle concept, cross sections, and *the Wigner classification itself* (particles = Poincaré irreps, the first no-go from your setup) — is built on asymptotic states. Drop them and you must rebuild the particle notion from the local net up. The door is real, but it relocates the entire problem into a framework (cosmological AQFT) where **no one has constructed a realistic gauge unification.** You trade a theorem you'd violate for a research program no one has completed.

**Assumption 5 (technical/analyticity in the strong sense) — not a physical door.** Weakening it tends to pathology, not physics. Reject.

**Section verdict:** the unique CM escape consistent with the bet's commitments is *"there is no global S-matrix,"* grounded in background independence + cosmology + confinement, landing you in cosmological AQFT — the same place Plank 2 lives.

---

## 4. The sharper wall: Weinberg–Witten

Coleman–Mandula forbids the *symmetry merger*. **Weinberg–Witten (1980)** is more directly dangerous to your *slogan* ("everything is the curvature/torsion of one connection"), because it targets **emergent** massless gauge bosons and gravitons specifically:

**Theorem (Weinberg–Witten).**
1. A theory with a Lorentz-covariant conserved 4-current $J^\mu$ admits **no massless particle of spin $>\tfrac12$** carrying nonzero charge under it.
2. A theory with a Lorentz-covariant conserved stress-energy tensor $\theta^{\mu\nu}$ admits **no massless particle of spin $>1$.**

So an emergent (composite) charged photon (spin 1) or an emergent graviton (spin 2) is forbidden **if** the theory has the relevant Lorentz-covariant current / stress tensor. The slogan "the graviton and the gauge bosons are all just pieces of one geometric connection" is exactly the kind of claim WW exists to test.

**Why it does *not* kill the standard objects (the loopholes), and what that forces on you:**

- **The fundamental graviton is safe** because GR's energy is *non-localizable*: there is only a stress-energy **pseudotensor**, not a Lorentz-covariant $\theta^{\mu\nu}$. WW's hypothesis fails, so a *fundamental* spin-2 is fine. **But notice the direction:** this loophole protects the graviton *as fundamental*, i.e. it supports **Plank 1**, and it works *against* any reading in which the graviton is a bound state emergent from a deeper substrate. WW is telling you: keep the graviton fundamental.
- **Gluons/gauge bosons are safe** because the conserved charge current that is Lorentz-covariant is not gauge-invariant (and the gauge-invariant one isn't covariant in the required sense). Standard.
- **Emergence loopholes** (for people who *want* composite gravitons): broken Lorentz, nonlocality, "no spin-2 below the gravity scale," or the graviton living in a *different* spacetime (holography). All of these cost something you don't want to pay (Lorentz, locality, or 4D-intrinsicness).

**What WW forces the bet to become.** The dangerous reading of "unification" is *gauge boson = composite/bound-state emergent from geometric substructure*. WW (plus the loophole structure) says: don't do that in 4D with Lorentz invariance and locality intact. The safe reading is **co-fundamental**: the gauge connection is *part of the same single fundamental connection as the spin connection* — one object, not a composite of more-fundamental geometric stuff. "Everything is the curvature of one connection" must mean **"co-fundamental, same geometric object,"** not **"gauge boson is a bound state of the metric."** WW is the theorem that forces that precision, and it happens to push you back toward Plank 1 (geometry fundamental) rather than toward "emergence."

---

## 5. What the bet must become (the sharpened flag)

Putting Documents 1 and this together, the position that *survives* both no-go theorems is narrower and more defensible than the opening slogan:

1. **Gauge fields are not torsion-as-potential.** (Doc 1: wrong rep / wrong gauge group / Weyl's rock.) They require an enlarged structure group.
2. **The enlargement evades Coleman–Mandula by dropping the global S-matrix**, justified by background independence + cosmology + confinement — landing in **cosmological algebraic QFT**, the *same* framework Plank 2 needs. The planks cohere on this.
3. **Weinberg–Witten forces the graviton to stay fundamental** (= Plank 1) and forces "unification" to mean *co-fundamental data in one connection*, **not** gauge-bosons-as-composites.
4. **Net flag:** *A background-independent, S-matrix-free 4D theory in which the spin connection and an internal gauge connection are co-fundamental components of a single connection on an enlarged frame bundle, with the particle/entanglement structure read off the local algebra net (AQFT) rather than from asymptotic states.*

This is a real position with named obstructions answered: it says *which* CM assumption it drops (the S-matrix) and *why* (background independence/confinement), and it states its relationship to WW (graviton fundamental, gauge fields co-fundamental not composite). A skeptic must now argue against *that*, not against a slogan.

**The honest probability statement, unchanged.** Removing the S-matrix removes your tools as well as the prohibition; nobody has built realistic gauge unification in cosmological AQFT; and the Wigner/particle concept itself has to be rebuilt there. The bet is still a long shot. But it is now a *precisely located* long shot, and — genuinely interesting — its escape doors for Planks 2 and 4 turned out to be the same door. Coherence is not truth, but it is the first thing a real program needs.

---

## 6. The natural Phase-4 direction (where this points next)

The single most promising lead falls straight out of §3–§4: in algebraic QFT there is a **rigorous theorem that reconstructs the internal gauge group from the local-algebra structure** — the **Doplicher–Roberts (DR) reconstruction theorem** (built on Doplicher–Haag–Roberts superselection theory). Given the net of observable algebras $\mathcal{O}\mapsto\mathfrak A(\mathcal{O})$ and its superselection sectors, DR canonically reconstructs a **compact gauge group $G$** and a field algebra carrying its action. In other words, there is an existing, rigorous sense in which:

$$\text{geometry / causal net of local algebras} \;\Longrightarrow\; \text{compact internal gauge group } G.$$

This is *literally* "the internal gauge symmetry is a shadow of the algebra of local (geometric) regions" — the exact bridge where **Plank 2 (AQFT) and Plank 4 (gauge from geometry) meet.** It does not by itself pick out $SU(3)\times SU(2)\times U(1)$, and it lives (so far) in Minkowski AQFT, not cosmological — but it is the rigorous home for the bet's central claim, and extending DHR/DR superselection theory to AQFT **on a fixed cosmological 4-manifold** is a concrete, citable, genuinely under-explored research target.

**Concrete next sub-questions:**
- State the DR reconstruction precisely and identify exactly what input data fixes $G$ (the statistics of superselection sectors / the symmetric tensor category). Then ask: *what geometric feature of $M^4$ could fix that categorical data?* — this is the rigorous version of "forces from geometry."
- Does DHR/DR survive on a globally hyperbolic curved/cosmological spacetime with no S-matrix? (Partial results exist in algebraic QFT on curved spacetime — map them.)
- Independently quantify Document 1's "door (c)": compute the effective pseudoscalar from axial torsion (an axion-like field) and assess whether it is phenomenologically live *regardless* of the grand bet — a sub-result that stands on its own.

---

## Sources (verification)
- Coleman–Mandula statement and the five assumptions (mass gap, nontrivial analytic S-matrix, Poincaré, technical): [Coleman–Mandula theorem — Wikipedia](https://en.wikipedia.org/wiki/Coleman%E2%80%93Mandula_theorem); [Scholarpedia: Coleman–Mandula](http://www.scholarpedia.org/article/Coleman-Mandula_theorem). Loopholes (no mass gap → conformal; no S-matrix; de Sitter): [scientificlib summary](https://www.scientificlib.com/en/Physics/LX/ColemanMandulaTheorem.html).
- Haag–Łopuszański–Sohnius (graded algebra is the unique loophole within the assumptions): noted in the Wikipedia and Scholarpedia entries above.
- Weinberg–Witten theorem (spin $>\tfrac12$ no covariant current; spin $>1$ no covariant stress tensor) and loopholes (broken Lorentz, nonlocality, no low-energy spin-2, holography; gravitational stress-energy is a pseudotensor): [Weinberg–Witten theorem — Wikipedia](https://en.wikipedia.org/wiki/Weinberg%E2%80%93Witten_theorem); [Jenkins, "Topics in Particle Physics and Cosmology Beyond the Standard Model" / WW essay](https://pure.mpg.de/rest/items/item_33005/component/file_33006/content); [Challenges for Emergent Gravity (arXiv:1207.2504)](https://arxiv.org/pdf/1207.2504).
- Self-dual decomposition $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ (Ashtekar variables context): standard; see e.g. Ashtekar self-dual connection literature.
- Doplicher–Roberts reconstruction / DHR superselection (compact gauge group reconstructed from the observable net): S. Doplicher & J. E. Roberts, "Why there is a field algebra with a compact gauge group describing the superselection structure in particle physics," *Commun. Math. Phys.* 131 (1990) 51.
