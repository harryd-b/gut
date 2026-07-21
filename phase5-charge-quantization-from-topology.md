# Phase 5 — Charge quantization from the topology of $M^4$ (the controlled calculation)

**Where we are.** Phase 4 identified the live lead (Doplicher–Roberts: gauge group from the local net) and named the first calculable sub-question: take a concrete spacetime topology and compute the charge sectors it induces — "charge quantization from geometry" in a controlled case, the rigorous descendant of the Kaluza–Klein fact $p_5 = n/R$ **without** the extra dimension. This document does that calculation, in two complementary controlled examples, and is explicit about what each does and does not show.

**Verdict (one line).** In 4D, **(A)** spacetime topology with $\pi_1\neq 0$ provably generates *new* charge quantum numbers (Aharonov–Bohm sectors, labeled by unitary representations of $\pi_1(M)$), and **(B)** genuine *integer* charge quantization is the integrality of a degree-2 cohomology class, $g = c_1 \in H^2(\Sigma;\mathbb{Z}) = \mathbb{Z}$ — Dirac quantization as topology. Together they realize the bet's "KK charge quantization without the $S^1$": the quantizing integer is a **Chern number of a bundle over the 4-manifold**, not a momentum on a fifth dimension. **Honest limits:** this is abelian only; non-abelian AB needs non-abelian $\pi_1$ and is hard; and crucially the gauge bundle/net is still *presupposed*, not derived from $(M^4, e^a, \omega, T)$ — Phase-4 gap 3 persists.

---

## 0. The two distinct mechanisms (don't conflate them)

"Charge from geometry" splits into two genuinely different statements, and clarity requires separating them:

1. **New charges from $\pi_1$ (Aharonov–Bohm).** Nontrivial $\pi_1(M)$ creates *new sector labels* — a flat background holonomy charges feel when transported around non-contractible loops. This label is generically **continuous** (a flux modulus). Mechanism: representations of the fundamental group.
2. **Quantization from $H^2$ (Dirac/monopole).** Magnetic charge is forced to be an **integer** because it is a first Chern class, an element of *integer* cohomology $H^2(\Sigma;\mathbb{Z})$. Mechanism: integrality of characteristic classes.

(1) answers "where do extra charge-like quantum numbers come from?"; (2) answers "why are charges quantized?". The bet's headline ("charge quantization is geometric, as in KK") is carried by (2); (1) is the bonus that topology manufactures charge labels at all.

---

## 1. Example A — Aharonov–Bohm sectors on a cosmic-string spacetime

**Geometry.** Take $M = \mathbb{R}_t \times \Sigma$ globally hyperbolic with Cauchy surface
$$\Sigma = \mathbb{R}^3 \setminus \{\text{line}\} \;\simeq\; S^1 \quad(\text{homotopy equivalence}),$$
i.e. Minkowski with an idealized straight cosmic string / solenoid removed. Then
$$\pi_1(\Sigma) = \mathbb{Z}, \qquad H^1(\Sigma;\mathbb{Z}) = \mathbb{Z}.$$

**Sector calculation (DHR/CRV topological sectors).** In AQFT on a curved spacetime, beyond the ordinary DHR charges the charged superselection sectors carry an extra quantum number: a flat potential whose holonomy is an **irreducible unitary representation of $\pi_1(M)$** (Brunetti–Ruzzi; Ciolli–Ruzzi–Vasselli; Dappiaggi et al.). So the topological labels are
$$\widehat{\pi_1(\Sigma)} \;=\; \mathrm{Hom}\big(\mathbb{Z}, U(1)\big) \;\cong\; U(1), \qquad \text{generator}\ \mapsto e^{i\alpha},\ \alpha\in[0,2\pi).$$

**Reading.** The topology produces a **new, continuous** quantum number $\alpha$ — the Aharonov–Bohm flux phase — that does not exist on Minkowski space. A charge $q$ transported around the string picks up $e^{iq\alpha}$. This is "a charge quantum number from pure geometry," rigorously, but note it is a **modulus, not a quantized integer**: the flux $\alpha$ ranges over all of $U(1)$.

**Two honest riders.**
- *What's quantized here is the detector, not the flux.* If the matter is a charge-$1$ Dirac field, the observable charges are $n\in\mathbb{Z}$ ($n$-particle states) — but that $\mathbb{Z}$ comes from the *field content* (unit charge), not from $\Sigma$'s topology. Example A alone does not quantize charge.
- *Non-abelian bonus/limit:* a **non-abelian** Aharonov–Bohm effect — sectors labeled by irreps of a non-abelian group — exists **iff $\pi_1(M)$ is non-abelian** (Ruzzi et al.). So *non-abelian* internal charge structure from topology requires a *non-abelian fundamental group* of the 4-manifold. That is a sharp, citable target connecting Plank 4's non-abelian gauge groups to 4-manifold topology — and it is exactly the kind of structure that 4-manifolds (unlike, say, surfaces) can have in abundance.

**Example A result:** $\boxed{\ \pi_1(\Sigma)=\mathbb{Z} \ \Rightarrow\ \text{topological sectors} = \mathrm{Hom}(\mathbb{Z},U(1)) = U(1)\ (\text{continuous AB flux})\ }$ — new charge label from geometry, not yet quantization.

---

## 2. Example B — magnetic charge quantization as $H^2(\Sigma;\mathbb{Z})$ integrality

**Geometry.** Take $\Sigma$ containing a non-contractible 2-sphere, e.g. $\Sigma \simeq \mathbb{R}^3\setminus\{\text{point}\} \simeq S^2$, so
$$H^2(\Sigma;\mathbb{Z}) = \mathbb{Z}.$$

**Bundle calculation.** A Maxwell field with a monopole is a connection on a **principal $U(1)$-bundle** $L\to\Sigma$. Such bundles are classified by their **first Chern class**
$$c_1(L) \in H^2(\Sigma;\mathbb{Z}) = \mathbb{Z}.$$
The magnetic charge is the flux of the curvature $F = dA$ through the $S^2$:
$$g \;=\; \frac{1}{2\pi}\int_{S^2} F \;=\; c_1(L) \;\in\; \mathbb{Z}.$$
The integral is forced to be an integer because $[F/2\pi]$ is the *integral* class $c_1$ — there is no continuous freedom. This is **Dirac's quantization condition, recast as the integrality of a characteristic class.** No Dirac string, no choice of gauge — the integer is a topological invariant of how the internal $U(1)$ twists over the 4-manifold's spatial slice.

**Closing the loop to electric charge.** The same fact quantizes *electric* charge, via compactness:
$$\text{$\exists$ one monopole } \Longleftrightarrow \text{gauge group is compact } U(1)\ (\text{not } \mathbb{R}) \Longrightarrow \text{electric charges} \in \widehat{U(1)} = \mathbb{Z}.$$
And in the Doplicher–Roberts language of Phase 4: a **compact** reconstructed gauge group is exactly what forces the superselection charges (the irreps) to be a *discrete* set with integer statistical dimensions. So $H^2$-integrality $\to$ monopole $\to$ compact $U(1)$ $\to$ discrete (integer) charge sectors. Everything coheres: **the integrality of charge and the compactness of the gauge group are the same topological fact seen from two sides.**

**Example B result:** $\boxed{\ H^2(\Sigma;\mathbb{Z})=\mathbb{Z}\ \Rightarrow\ g = c_1 \in \mathbb{Z}\ \Rightarrow\ \text{electric charge}\in\mathbb{Z}\ }$ — genuine quantization from 4-manifold topology.

---

## 3. The payoff: KK charge quantization, without the extra dimension

Side-by-side with the precedent the bet wanted to replace:

| | Kaluza–Klein (5D) | This calculation (4D) |
|---|---|---|
| source of the integer | momentum on the fiber $S^1$: $p_5 = n/R$, $n\in\mathbb{Z}$ from Fourier modes | Chern class $c_1 \in H^2(\Sigma;\mathbb{Z}) = \mathbb{Z}$ |
| where the $\mathbb{Z}$ lives | compactness of a *physical extra spacetime dimension* | compactness/topology of the **internal $U(1)$ bundle over $M^4$** |
| spacetime dimension | 5 | **4** |
| charge is… | KK momentum | a topological invariant of the 4-manifold + bundle |

**This is the bet's claim, realized in a controlled case:** charge quantization is geometric, and the geometry can be the topology of the *four* dimensions we have (plus an internal bundle), not a fifth spacetime dimension. The integer $n$ is a winding number on $M^4$, not a momentum along $S^1$.

---

## 4. The honest limits (what this does *not* show)

1. **The internal $U(1)$ bundle is presupposed, not derived.** Example B uses the principal $U(1)$-bundle as given. It proves quantization is topological *once you have* the bundle; it does **not** derive that bundle (the gauge field itself) from $(M^4, e^a, \omega, T)$. This is exactly **Phase-4 gap 3** and **Document 1's result** (gauge fields aren't intrinsic torsion) reappearing: the geometry quantizes the charge but does not yet *produce* the gauge connection. The bet's Plank 4 still owes that derivation.
   - *Caveat on "without the extra dimension":* a $U(1)$ principal bundle has a circle fiber, so a skeptic will say the $S^1$ snuck back in. The honest distinction: the KK $S^1$ is a *spacetime* dimension (you carry momentum along it); the bundle $U(1)$ is an *internal* fiber (no propagation, charge = how it twists). Spacetime is genuinely 4D. But this is the *standard fiber-bundle picture of gauge theory* — which Plank 4 wanted to *derive*, not *assume*. So the win is "quantization is 4D-topological"; the unfinished business is "derive the bundle."
2. **Abelian only.** Both examples are $U(1)$. The non-abelian case (the SM's $SU(3)\times SU(2)$) needs non-abelian $\pi_1(M)$ (Example A's rider) or non-abelian bundle data, and the clean $H^2$-integrality story is replaced by harder characteristic-class data ($c_2$, etc.). Not done here.
3. **Doesn't select the Standard Model.** Nothing picks $H^2(\Sigma;\mathbb{Z})$ or $\pi_1$ to give the SM charge spectrum; the topology is *chosen by hand*. Selecting it is the deep open problem (and where Plank 3 / exotic smoothness would have to enter — see below).

---

## 5. What this buys the program, and the next sub-questions

**Net:** a real, self-contained result — *charge quantization is the integrality of a degree-2 cohomology class of the 4-manifold's spatial slice; topology with nontrivial $\pi_1$ additionally manufactures new (Aharonov–Bohm) charge labels.* This stands on its own (it's just rigorous math/physics) **regardless of whether the grand bet ever closes**, which was the Phase-2 discipline: produce sub-results that survive the failure of the big claim. It also tightens the bet's flag: the charge-quantization plank of Plank 4 is **secured**; the gauge-field-existence plank is **still open** (gaps 1 above).

**Next sub-questions, in order of leverage:**

1. **(The real fusion of Plank 3 + Plank 4.)** Does the *smooth* structure (not just the topology) of $M^4$ influence $H^2$ / the bundle data? Exotic $\mathbb{R}^4$'s and exotic 4-manifolds can differ in Seiberg–Witten invariants while sharing topology — and SW invariants *are* built from $U(1)$ (Spin$^c$) bundle/monopole data. **Sharp question:** can two homeomorphic-but-not-diffeomorphic 4-manifolds carry *different* charge-sector structure? If yes, that is "charge content from the exotic smooth structure" — the single most distinctive prediction the bet could make. This is the genuine, citable, open frontier.
2. **(Non-abelian.)** Construct a spacetime with non-abelian $\pi_1$ (e.g. $\Sigma$ with $\pi_1$ a non-abelian discrete group) and compute the non-abelian AB sectors explicitly — the topological route to $SU(2)$-type charge structure.
3. **(Close gap 3, even negatively.)** State precisely what extra data beyond $(M^4, g)$ is needed to fix the principal bundle, and whether any of it can come from torsion/affine structure rather than being independent. A clean no-go here would itself sharpen Plank 4.

**Recommended next step:** sub-question 1. It is the point where the three live planks (3: dimension/smoothness, 4: gauge charge, via 2: AQFT sectors) would actually fuse, it connects to a real and active invariant (Seiberg–Witten), and even a partial answer would be a distinctive result. It is the natural successor and the most "the math isn't good enough yet" question in the whole program — which is precisely where the bet claimed its edge.

---

## Sources
- Topological/Aharonov–Bohm superselection sectors labeled by unitary reps of $\pi_1(M)$; non-abelian AB iff $\pi_1$ non-abelian: [Diaz-Marin, Ruzzi et al., "Aharonov–Bohm superselection sectors," Lett. Math. Phys. 110 (2020); arXiv:1912.05297](https://arxiv.org/abs/1912.05297); [Brunetti–Ruzzi, "Superselection Sectors and General Covariance. I" (arXiv:gr-qc/0511118)](https://arxiv.org/pdf/gr-qc/0511118); [Ciolli–Ruzzi–Vasselli, "Presheaves of Superselection Structures in Curved Spacetimes," CMP (2015)](https://link.springer.com/article/10.1007/s00220-014-2251-2); ["Background potentials and superselection sectors" (arXiv:1811.12121)](https://arxiv.org/pdf/1811.12121).
- Dirac charge quantization as $c_1 \in H^2(\Sigma;\mathbb{Z})=\mathbb{Z}$ (monopole = $U(1)$ bundle over $S^2$, charge = Chern number): [Dirac charge quantization — nLab](https://ncatlab.org/nlab/show/Dirac+charge+quantization); [Dirac monopole — Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Dirac_monopole).
- Compactness of $U(1)$ ⟺ electric charge quantization; DR discrete-sector connection: see Phase-4 document and [Doplicher–Roberts, CMP 131 (1990) 51](https://link.springer.com/article/10.1007/BF02097680).
- (Forward pointer) Seiberg–Witten invariants as Spin$^c$/$U(1)$-monopole data distinguishing smooth structures: standard; to be developed in the next sub-question.
