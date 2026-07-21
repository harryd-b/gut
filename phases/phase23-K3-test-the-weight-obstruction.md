# Phase 23 — The K3 test: a decisive Hodge-weight obstruction

**The test (Phase 22).** Does a prepotential-like functional — the object that turns "curves" into "dynamics" — emerge from the **K3 period map** alone (classical Hodge theory of the 4-manifold), *without* invoking an $\mathcal N=2$ gauge theory? A yes revives the original non-SUSY bet; a no means the period→dynamics step is SUSY/auxiliary-bound.

**Verdict (one line).** **Decisive no — for a clean structural reason.** A nontrivial **prepotential** (special Kähler geometry) is a **weight-3** variation of Hodge structure (Calabi–Yau threefold); the Seiberg–Witten prepotential is **weight-1** (a curve). The physical 4-manifold's own period geometry is **weight-2** (K3 = type-IV Hermitian symmetric = the **N=4**, *degenerate*-prepotential case). So a 4-manifold **cannot source its dynamics from its own periods** — weight 2 is structurally the wrong weight, sitting *between* the two prepotential-carrying weights and carrying neither. To get a prepotential the theory must borrow an **auxiliary weight-1 curve** (the SW curve — which arrives with the SUSY gauge-theory interpretation) or **extra dimensions** (a weight-3 Calabi–Yau). **Both moves are exactly what the original bet refused.** The bet does not revive: *4D self-sufficiency is in structural tension with the very mechanism (special geometry) that makes geometry fix dynamics.*

---

## 1. Where the prepotential lives, by Hodge weight

The prepotential $F$ (with the metric $=\mathrm{Im}\,\partial^2 F$) is not generic — it is a specific variation-of-Hodge-structure (VHS) phenomenon, and the weight is fixed:

| Hodge weight | geometric object | period structure | prepotential? |
|---|---|---|---|
| **1** | a curve / Riemann surface ($H^1$) | rigid special geometry; periods of $\lambda$ over the curve | **yes** — the **SW prepotential** (over the moduli of curves) |
| **2** | a **surface / 4-manifold** ($H^2$; K3) | **type-IV Hermitian symmetric** domain $SO(2,n)/\!\big(SO(2)\times SO(n)\big)$ | **no** — this is the **N=4** case; the "prepotential" degenerates to $F=-iX^0X^1$ (quadratic, trivial) |
| **3** | a **Calabi–Yau threefold** ($H^3$, $h^{3,0}=1$) | projective special Kähler; VHS of "Calabi–Yau type" | **yes** — the **N=2 supergravity prepotential** |

The middle row is the killer. *"A projective special Kähler structure is a variation of polarized Hodge structures of weight 3 with $h^{3,0}=1$"* — weight 3, not 2. And K3's period domain is type IV / Hermitian symmetric, the maximally-symmetric N=4 geometry, whose prepotential is the degenerate $F=-iX^0X^1$ — **no nontrivial dynamics encoded.**

## 2. The 4-manifold is at the wrong weight

A physical 4-manifold $X$ carries its primitive Hodge data in $H^2(X)$ — **weight 2**. By the Torelli theorem the K3 *is* its weight-2 period point, so "the K3 period map" is exactly the weight-2 data. By §1 that data is N=4-degenerate: it has a Kähler metric (the Bergman/Hodge metric on the type-IV domain) but **no nontrivial prepotential** — nothing that plays the role $F$ plays in fixing $\mathcal N=2$/SW dynamics.

So the answer to the test is **no**: the K3 period map yields a symmetric-space geometry, not a dynamics-fixing prepotential. The "curves → dynamics" step does **not** come for free from the 4-manifold's own periods.

## 3. Why the curves don't rescue it (closing the Phase-22 hope precisely)

Phase 22's hope was that Taubes' $J$-holomorphic curves (SUSY-free) would supply the spectral curve. They supply *curves* — but the **period → prepotential** map needs those curves organized as a **weight-1 VHS over a moduli space of vacua**. Two honest mismatches:

1. **Wrong base.** The 4-manifold's elliptic/Lefschetz fibration gives a weight-1 fiber variation over its **base surface $C$** (Kodaira's functional invariant) — the right *weight* but the wrong *base*: the SW prepotential lives over the **Coulomb branch of vacua**, not over a geometric base curve. A fixed 4-manifold has no intrinsic moduli-of-vacua to vary over.
2. **Wrong weight for the manifold itself.** The 4-manifold's *own* variation (deforming $X$) is weight-2 (§2) — N=4-degenerate. So neither the fibration's base nor the manifold's moduli supplies the weight-1-over-vacua structure the prepotential requires.

To manufacture it you must **add** either (i) an auxiliary weight-1 curve fibered over an auxiliary moduli space — which is precisely the SW curve, and that object's *meaning* (the $a_D=\partial F/\partial a$ relation) comes from the $\mathcal N=2$ gauge-theory interpretation, i.e. **SUSY re-enters**; or (ii) a weight-3 Calabi–Yau — i.e. **extra (6 real) dimensions**.

## 4. The tie-back: the bet's core commitment forbids its own mechanism

This is the deep point, and it connects straight to Plank I (exactly 4D, no extra dimensions, no auxiliary scaffolding):

> The dynamics-fixing prepotential lives at **weight 1** (an auxiliary curve) or **weight 3** (a Calabi–Yau threefold = extra dimensions). The physical 4-manifold sits at **weight 2**, which carries no nontrivial prepotential. **The original bet's insistence on pure 4D self-sufficiency — no auxiliary curve, no extra dimensions — is exactly the condition that excludes the prepotential.** The commitment and the mechanism are in structural tension.

So the program's earliest plank (exactly 4D) and its deepest mechanism (special geometry = how geometry fixes dynamics) are incompatible *as stated*: geometry fixes dynamics via a prepotential, the prepotential is a weight-1-or-3 object, and 4D-self-contained geometry is weight-2. The bet asked the one weight that can't self-source.

## 5. What survives (precise, not a blanket negation)

- **Taubes still holds:** the SUSY-free $J$-holomorphic curves of a symplectic 4-manifold = SW data. The *geometric content* is real and SUSY-free.
- **Protected topology/sectors still geometric:** Planks II–III on the protected stratum (sectors, charge quantization, universal entanglement) are weight-independent and stand.
- **Special geometry still fixes dynamics where it applies** (weight 1 SW curve; weight 3 CY) — just not from the 4-manifold's own (weight-2) periods.

What **fails** is exactly and only the **4-manifold-self-sourcing of dynamics** — and it fails decisively, by Hodge weight.

## 6. Verdict on the original (anti-SUSY, pure-4D) bet

**Closed, negatively, with a structural reason.** The non-SUSY revival required the 4-manifold's geometry to supply the period→prepotential map. It cannot: weight-2 is the N=4-degenerate case. The dynamics-fixing structure is available only by importing a weight-1 auxiliary curve (SUSY interpretation) or weight-3 extra dimensions — the two things the bet forbade. So:

- the **honest descendant** remains the SUSY-protected (or weight-1-curve / weight-3-CY) geometry-first picture of Phase 19;
- the **original anti-SUSY pure-4D bet** is now not just "disfavored" but **structurally obstructed** — by the Hodge weight of 4-manifolds.

That is the decisive result the $K3$ test was run to find. It is, fittingly, the same shape as every prior decisive finding: the geometry-first instinct is right *on the protected stratum* and provably blocked off it — and here the block is that 4D is the wrong Hodge weight to be its own dynamical source.

## 6b. Coda — the exotic-smoothness exception (scope correction)

The verdict above obstructs **one channel**: "geometry → dynamics *via the period map*." It does **not** obstruct the **exotic-smoothness / Seiberg–Witten channel**, because SW invariants and the Godbillon–Vey class are **not period data** — the weight argument (a statement about the Hodge structure on $H^2$) says nothing about them. So the precise scope is:

- **Period channel: closed** (weight-2, symmetric, no prepotential — all smooth structures, since weight is homotopy-level).
- **Exotic-smoothness channel: open.** The small exotic $\mathbb R^4$'s form a **radial family parametrized by $\mathrm{GV}\in\mathbb R$**, so exotic data is **function-valued over that modulus**; AMK compute physical functions of it (Higgs potential, confinement, cosmological constant). This *escapes* the weight obstruction and reaches the parameter/potential level of dynamics — non-SUSY, intrinsically 4D.

So §6's "structurally obstructed" should read **"the period route is structurally obstructed; the exotic-smoothness route is the surviving exception."** Honest limits on the exception: AMK identifications are matched-not-forced (Phase 21); the exotic moduli is wild (no special-geometry rigidity known); the refined invariant (SW–Floer) may still be skeletal (Phase 18). **Net: the exotic-smoothness channel is the single open route by which 4D geometry might source its own dynamics — real and partial (it fixes parameters/potentials), not established as a full derived law. It is where the original bet remains alive.**

## 7. The one remaining sliver (stated for completeness)
The argument assumes the dynamics-fixing structure *must* be a special-geometry prepotential. If there were a genuinely *non-special-geometry* "geometry → dynamics" mechanism — one not of VHS/prepotential type at all — the weight obstruction wouldn't apply. No such mechanism is known (every rigorous case is special geometry / integrability / holomorphy, all VHS-type), and Phase 21 already found tt\*/non-abelian-Hodge needs $(2,2)$. So the sliver is real but empty as far as current mathematics reaches: **there is no known weight-2 (4-manifold-intrinsic) mechanism by which geometry fixes dynamics.**

---

## Sources
- K3 period domain = type IV Hermitian symmetric $SO(2,n)/(SO(2)\times SO(n))$, weight-2 Hodge structure, Torelli: [K3 surface — Wikipedia](https://en.wikipedia.org/wiki/K3_surface); [Huybrechts, *Lectures on K3 Surfaces*](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf).
- Special Kähler / prepotential = **weight-3** VHS of Calabi–Yau type ($h^{3,0}=1$); consequence of $\mathcal N=2$: [String Theory on Calabi–Yau Manifolds (arXiv:hep-th/9702155)](https://arxiv.org/pdf/hep-th/9702155); ["Special Kähler Geometry: Does there Exist a Prepotential?" (arXiv:hep-th/9712092)](https://arxiv.org/pdf/hep-th/9712092).
- N=4 degenerate prepotential $F=-iX^0X^1$ (the weight-2 / K3 case): noted in N=2/N=4 supergravity literature (e.g. [arXiv:2004.11433](https://arxiv.org/pdf/2004.11433)).
- SW prepotential = weight-1 periods of the SW curve (rigid special geometry): Seiberg–Witten 1994; Donagi–Witten (Phase 22).
- Kodaira functional/homological invariant of elliptic surfaces (the fiber period over the base): standard theory of elliptic surfaces.
