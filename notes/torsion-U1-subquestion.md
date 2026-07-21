# Can 4D torsion carry a U(1) gauge potential intrinsically?

**Sub-question (Phase 2, Plank 4).** In Einstein–Cartan / metric-affine geometry on a fixed 4-manifold, the torsion $T^a{}_{\mu\nu}$ has 24 components. Do any of them — in particular the "tensor" (non-trace) part — have the right *count* and the right *transformation properties* to encode a $U(1)$ electromagnetic potential $A_\mu$ intrinsically in 4D, with no extra dimensions and no enlarged structure group? And if not, exactly what breaks?

**Verdict (one line).** No. The count works for two of the three pieces, but the transformation law fails for all three: torsion is a *covariant tensor* (a field-strength–like object), not an *inhomogeneously-transforming connection* (a potential), and the only gauge freedom available to it is local Lorentz $\mathfrak{so}(1,3)$, never an internal $U(1)$. The identification dies at the transformation law, which is the thing that actually *defines* a gauge potential. This reproduces, in modern language, the precise rock that Weyl's 1918 geometrization of EM split on.

---

## 1. The setup and the decomposition

Torsion is $T^a = de^a + \omega^a{}_b \wedge e^b$, a vector-valued 2-form; in components $T^\lambda{}_{\mu\nu} = -T^\lambda{}_{\nu\mu}$. The free index runs over 4 values, the antisymmetric pair $[\mu\nu]$ over $\binom{4}{2}=6$, so

$$\#\,\text{components} = 4 \times 6 = 24.$$

Under the Lorentz group $SO(1,3)$ this 24-dimensional space splits into **three irreducible pieces**:

$$
T_{\lambda\mu\nu} \;=\; \underbrace{\tfrac{1}{3}\big(g_{\lambda\mu}V_\nu - g_{\lambda\nu}V_\mu\big)}_{\text{trace vector } V}\;+\;\underbrace{\tfrac{1}{3}\,\epsilon_{\lambda\mu\nu\rho}\,A^\rho}_{\text{axial vector } A}\;+\;\underbrace{q_{\lambda\mu\nu}}_{\text{pure tensor}}
$$

with

| piece | definition | Lorentz character | components |
|---|---|---|---|
| **trace vector** | $V_\mu = T^\lambda{}_{\lambda\mu}$ | true 4-vector $(\tfrac12,\tfrac12)$ | **4** |
| **axial vector** | $A^\mu \propto \epsilon^{\mu\nu\rho\sigma}T_{\nu\rho\sigma}$ | pseudovector | **4** |
| **pure tensor** | $q_{\lambda\mu\nu}$, traceless + $q_{[\lambda\mu\nu]}=0$ | mixed-symmetry, **no vector subrep** | **16** |

$4 + 4 + 16 = 24$. ✓ (Hehl et al. 1976; this is the standard textbook decomposition — confirmed against the literature below.)

This already settles the headline form of the question.

---

## 2. What a $U(1)$ potential actually requires

To *be* a Maxwell potential, an object $A_\mu$ must satisfy three things — not one:

1. **(Count / Lorentz rep.)** It is a Lorentz 4-vector: one copy of the $(\tfrac12,\tfrac12)$ irrep, 4 real components.
2. **(Inhomogeneous gauge law.)** Under the *internal* $U(1)$ it shifts by a gradient:
   $$A_\mu \;\longrightarrow\; A_\mu + \partial_\mu \lambda(x), \qquad \lambda:\,M\to \mathbb{R}\ \ (\text{one scalar}).$$
   This is what makes it a *connection* rather than just a covector field.
3. **(Integrability of $F$.)** Its field strength $F=dA$ is automatically closed, $dF=0$ — the homogeneous Maxwell equations / Bianchi identity. This is what guarantees a global $A$ exists and that charge is the *only* source.

A candidate that passes (1) but fails (2) or (3) is not a gauge potential; it is at best a matter covector. Keep all three in view — most "geometrization of EM" attempts quietly satisfy only (1).

---

## 3. Testing each piece

### 3a. The pure tensor part (16) — fails at step 1

The 16-component $q_{\lambda\mu\nu}$ is, by construction, the part with **both** traces removed. As a Lorentz representation it contains **no $(\tfrac12,\tfrac12)$ vector**. So it cannot supply a 4-vector $A_\mu$ at all: wrong irrep, fails requirement (1) before we even reach the gauge law.

This is the direct answer to the question as posed ("the non-trace tensor part"): **the 16 are the wrong shape.** The only vector-transforming material in torsion is the two *traces* — which is why any serious attempt must use $V$ or $A$, not $q$. So the rest of the work is about them.

### 3b. The trace vector (4) — right rep, wrong gauge group (this is Weyl's rock)

$V_\mu$ is a genuine 4-vector, so it passes (1). Now (2): we need a transformation under which $V_\mu \to V_\mu + \partial_\mu\lambda$. **There isn't one in Riemann–Cartan geometry.** The reason is structural:

- Torsion $T^a$ is a *tensorial* 2-form. Under a local Lorentz (frame) transformation $\Lambda^a{}_b(x)$ it transforms **homogeneously**, $T^a \to \Lambda^a{}_b\,T^b$. No inhomogeneous shift. Hence $V_\mu$ transforms homogeneously too — it never picks up a $\partial_\mu(\cdot)$ term.
- The object in the geometry that *does* transform inhomogeneously is the **spin connection** $\omega^a{}_b \to \Lambda\,\omega\,\Lambda^{-1} + \Lambda\,d\Lambda^{-1}$. But that inhomogeneous term is valued in $\mathfrak{so}(1,3)$: it is parameterized by an *antisymmetric* $\Lambda^{ab}(x)$ — **6** parameters acting on the *frame* indices — not by a single scalar $\lambda(x)$ acting on an internal phase. Wrong group ($\mathfrak{so}(1,3)$, dim 6), wrong indices (frame, not internal).

So the "gauge freedom" living in the connection is local Lorentz, full stop. You cannot project a scalar $U(1)$ orbit out of a 6-parameter Lorentz orbit acting on spacetime indices without a choice that is itself not Lorentz-covariant (it would pin EM to a preferred plane/boost).

**This is not a new failure — it is *the* failure.** Weyl (1918) identified the trace of his non-metric connection (the "Weyl vector") with $A_\mu$ precisely because it carried an inhomogeneous shift under local *scale* transformations $g\to e^{2\lambda}g$. The shift is real — but its gauge group is **dilatations** $(\mathbb{R}_+)$, not the compact internal $U(1)$ of EM. Einstein's objection (second clocks / atomic line spacing would depend on worldline history, contradicting the sharpness of spectral lines) is exactly the statement that a *non-compact, non-integrable scale* connection is physically not the electromagnetic potential. The trace vector's natural home is the dilatation current, not charge. **Right rep, wrong group — and history already knows it.**

### 3c. The axial vector (4) — gives an axion, not a photon

$A^\mu$ is a *pseudo*vector, dual to the totally antisymmetric part $T_{[\lambda\mu\nu]}$, which is a **3-form**. A 3-form $H = dB$ is the field strength of a *2-form* Kalb–Ramond potential $B_{\mu\nu}$, not of a 1-form. Equivalently, when axial torsion is made to propagate it couples to the fermion axial current and its quantum is a **pseudoscalar (axion-like) field** — spin 0, parity-odd — not a spin-1 vector boson. Wrong spin/parity for the photon. (This is a robust and well-trodden result; it's why "torsion ⇒ dark-matter axion" is a live idea while "torsion ⇒ photon" is not.)

### 3d. Even if you forced (1)–(2): step 3 and the dynamics also break

Two further obstructions, for completeness:

- **Bianchi / integrability.** Torsion's own integrability condition in Einstein–Cartan is the *first Bianchi identity* $DT^a = R^a{}_b \wedge e^b$ — **not** $dT^a=0$. Any $F$ built from torsion would therefore *not* automatically satisfy $dF=0$; its "magnetic" source would be curvature. That destroys the homogeneous Maxwell equations and with them the meaning of charge as the sole source. Fails requirement (3).
- **Propagation.** In minimal Einstein–Cartan, torsion is *non-dynamical*: the Cartan equation makes it an algebraic function of spin density ($T\sim$ spin current), with no kinetic term — it doesn't propagate, so it cannot be a radiative photon. Giving it a kinetic term means leaving minimal EC for quadratic Poincaré-gauge / metric-affine actions, where propagating torsion modes are generically plagued by **ghosts and tachyons**; only narrow parameter windows are healthy (Lin–Hobson–Lasenby find a few hundred critical no-ghost cases, of which a handful are power-counting renormalizable). The photon, by contrast, is healthy for free. So even the dynamical route buys instability you must then fight.

---

## 4. The clean statement of why it fails

The deepest way to say it uses the bundle language from your own setup. All of this geometry — coframe $e^a$, spin connection $\omega^a{}_b$, torsion $T^a$ — lives on the **frame bundle**, whose structure group is at most $GL(4,\mathbb{R})$ (or, for the orthonormal frame bundle, the Lorentz group $SO(1,3)$, possibly extended to the affine group $\mathbb{R}^4\rtimes GL(4)$ when you gauge translations too). **This group contains no internal $U(1)$ factor that commutes with Lorentz and acts trivially on spacetime indices.** Electromagnetism's $U(1)$ must act on a *separate* fiber — the phase of charged matter — commuting with spacetime transformations. You cannot manufacture that internal factor out of the frame bundle's own structure group.

This is the local-algebra shadow of **Coleman–Mandula**: spacetime and internal symmetries combine only as a direct product $\text{Poincaré}\times G_{\text{internal}}$. Torsion's gauge orbit is the *spacetime* (Lorentz) factor; EM's $U(1)$ is the *internal* factor; the theorem forbids the merger you'd need to read one off the other. **The obstruction Plank 4 has to evade is sitting right here, in the smallest possible test case — and the test case loses.**

---

## 5. What this result is worth (and the narrow doors left open)

This is a genuine **negative result**, and it does three useful things for the program:

1. **It kills the naive form of Plank 4 cleanly.** "EM is intrinsic 4D torsion" fails not by taste but by representation theory + the transformation law. That sharpens the bet: Plank 4 cannot route EM through Riemann–Cartan torsion *as a potential*.
2. **It re-derives the historical fork from scratch.** The trace vector lands you exactly on Weyl 1918 and Einstein's objection. That's not a coincidence to be embarrassed by — it's confirmation that the calculation is tracking something real, and it tells you the fork is about *compact internal vs. non-compact spacetime* gauge groups.
3. **It maps the boundary**, i.e. the only doors that remain even in principle:
   - **(a) Enlarge the structure group, not the dimension.** Gauge more than Poincaré (metric-affine with a bigger $G$, or a $GL$/conformal extension) so an internal factor genuinely exists. This is *not* "intrinsic 4D Riemann–Cartan" anymore, and it walks straight into Coleman–Mandula — which is the honest cost, and the next thing to confront (Phase 3).
   - **(b) Field-strength, not potential.** Give up making torsion the *potential* and ask only whether a torsion 2-form can reproduce $F_{\mu\nu}$ on-shell (a constitutive/"premetric" identification). Then you must manufacture $dF=0$ by hand and explain why charge is quantized — both currently unmet.
   - **(c) Accept what torsion actually gives.** Trace vector → dilatation/Weyl gauge; axial vector → axion-like pseudoscalar. These are real, healthy, and *not* electromagnetism. If the program wants to keep them, it should claim *these* fields, not the photon.

**Net:** the smallest calculable version of Plank 4 returns a definite "no, and here is the exact rock." The bet now knows it must either enlarge the structure group (and face Coleman–Mandula head-on) or abandon "EM from torsion" for "scalar/pseudoscalar sectors from torsion." That is exactly the kind of constraint a research program is supposed to extract from itself.

---

## Next sub-questions this opens
- **Phase 3 hand-off:** if you take door (a), *which* Coleman–Mandula assumption are you dropping — asymptotic S-matrix (confinement/cosmology) or mass gap? Write the construction whose structure group $\supset SO(1,3)\times U(1)$ and show where the no-go's hypotheses fail.
- Repeat this exact test for $SU(2)$ (does any torsion piece carry an $\mathfrak{su}(2)$ triplet with an inhomogeneous law?) — the answer is structurally the same but worth doing once, in full, to nail the pattern.
- Quantify door (c): compute the effective pseudoscalar from axial torsion and ask whether *that* field is phenomenologically interesting (it may be — independent of the grand bet).

---

## Sources (verification of the standard results used)
- Torsion irreducible decomposition $24 = 4 + 4 + 16$ (trace vector / axial vector / tensor): [Torsion tensor — HandWiki](https://handwiki.org/wiki/Torsion_tensor); foundational ref. F. W. Hehl et al., "General relativity with spin and torsion," *Rev. Mod. Phys.* 48, 393 (1976). See also [Hehl & Obukhov, gr-qc/0001010 context](https://arxiv.org/pdf/gr-qc/0412034).
- Weyl 1918 trace-connection ↔ $A_\mu$ identification and its failure (Einstein's objection; gauge group is scale, not $U(1)$): [W. O. Straub, "On the Failure of Weyl's 1918 Theory"](http://www.weylmann.com/weyl_theory.pdf); [Scholz, "Weyl geometry in late 20th century physics"](https://www.academia.edu/58398416/Weyl_geometry_in_late_20th_century_physics).
- Propagating torsion ghost/tachyon constraints (minimal EC torsion is non-dynamical; quadratic PG generically unhealthy, narrow no-ghost windows): [Lin, Hobson, Lasenby, "Ghost and tachyon free Poincaré gauge theories: a systematic approach," PRD 99, 064001 (2019)](https://arxiv.org/abs/1812.02675); [Lin, Hobson, Lasenby, "Power-counting renormalizable, ghost-and-tachyon-free Poincaré gauge theories"](https://arxiv.org/pdf/1910.14197).
