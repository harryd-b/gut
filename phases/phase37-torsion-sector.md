# Phase 37 — The k = 0 sector decoded: prequantization of the Aharonov–Bohm torus, and what the torsion is

*Working session, 2026-07-11. Executes the phase-28 forward item ("what IS the 2-torsion, physically?") using a full extraction of Jabuka–Mark (arXiv:math/0502328, Adv. Math. 2008) with exact theorem statements. Outcome: the g = 2 dictionary check passes; the earlier Spin-vs-Spin^c guess for the torsion is REPLACED by a sharper reading the data actually supports; and the k = 0 clause of the internal dictionary is rewritten around it.*

---

## 1. The mathematics (Jabuka–Mark, exact)

- **Structure theorem (their Thm 1.1, all g ≥ 1, ℂ-coefficients):** HF⁺(Σ_g×S¹, 𝔰₀) = reduced part ⊕ towers indexed by *primitive and coprimitive* forms in Λ*H¹(Σ_g); over ℤ the reduced part is X₀(g, g−3)[5/2] ≅ H*(Sym^{g−3}Σ_g;ℤ) (shifted) **as graded groups** — the integral U-module structure is an open extension problem, and the Λ*H₁-action at k = 0 is explicitly beyond their methods.
- **The circle bundle (their §1.2):** HF^∞(Σ_g×S¹, 𝔰₀; ℂ) ≅ H*(E_g; ℂ) ⊗ ℤ[U,U⁻¹], where **E_g → T^{2g} is the circle bundle over the Jacobian torus with Euler class ω = the intersection-form class** in H²(T^{2g};ℤ) ≅ Λ²H¹(Σ_g;ℤ).
- **The torsion (their Thm 1.2, Cor 1.3 + Lee–Packer):** dim_{ℤ₂} HF^∞_d = 2^{2g−1} + 2^{g−1} exceeds dim_ℂ = C(2g+1, g) exactly when g ≥ 3 ⇒ **2-torsion in every degree of HF^∞(ℤ) for all g ≥ 3** — "the first example known to the authors of torsion in ℤ-coefficient Heegaard Floer homology." Via Lee–Packer's computation of H*(E_g;ℤ): **cyclic summands of every order ≤ n occur for g ≥ 2n−1** (ℤ/3 at g ≥ 5, ℤ/4 at g ≥ 7, …). The torsion lives in the **tower/stable range**; the reduced part is torsion-free.

## 2. The g = 2 dictionary check: PASS

At g = 2: X(2, −1) = 0 ⇒ HF⁺_red(Σ₂×S¹, 𝔰₀) = 0, and the ℤ₂/ℂ dimensions agree (10 = 10) — no torsion. Dictionary reading: the flux-neutral sector of the g = 2 universe carries **no protected irreducible content** (no neutral-sector gravisolitons — consistent with phase 30, since Sym^{g−3} is empty), and its tower is the primitive/coprimitive structure exactly. Clean, complete, and matching the Ozsváth–Szabó g ≤ 2 computations the theorem extends. First fully-decoded multi-sector universe: **all sectors of Σ₂×S¹ are now dictionary-checked** (k = ±1 from phase 28; k = 0 here).

## 3. What the torsion is: the hypothesis replaced

The phase-28-era guess (torsion = Spin-vs-Spin^c ℤ/2 shadow) is **refuted by the data**: Lee–Packer's pattern produces torsion of *every* order n (at g ≥ 2n−1), not a single ℤ/2 — no torsor-doubling story survives that. What the data does support:

**E_g is the prequantum circle bundle of the Aharonov–Bohm moduli space.** The Jacobian T^{2g} = H¹(Σ;ℝ/ℤ) *is* the moduli of flat U(1) connections — precisely the continuous Aharonov–Bohm moduli of CORE §2.3 — and ω (the intersection form) is its natural symplectic form. A circle bundle with Euler class = the symplectic class is, by definition, the **prequantization bundle** of geometric quantization; equivalently E_g is the **Heisenberg nilmanifold** — the compact quotient of the Heisenberg central extension of H¹(Σ;ℤ) by the intersection pairing. Physically that extension is exactly the **algebra of holonomy (Wilson) operators around the a- and b-cycles, whose commutators are fixed by intersection numbers** — the large-gauge clock-and-shift algebra of the flux-neutral sector. (Note the resonance with Casini–Magán's flat-space result that knot-operator commutators are determined by linking numbers — the same structure, appearing here on the cycles of Σ; and with phase 34's O3, where the skein/quantum-torus embedding carries the identical Heisenberg data into the foliation algebra.)

**Proposed reading (the rewritten k = 0 clause) [conjecture, this program]:**

> *The flux-neutral sector's protected content is not a bare charge ladder and not a bare Jacobian-dressed tower: it is the cohomology of the **geometric quantization** of the Aharonov–Bohm moduli — the U-tower fibered over the prequantum bundle E_g. The integral torsion is the **discrete fingerprint of the quantized holonomy (Heisenberg) algebra**: the finite clock-shift subalgebras that survive at each level, with Lee–Packer's "order ≤ n at g ≥ 2n−1" tracking the integral divisibility of powers of ω (theta-level structure). In words: the protected sector of the neutral flux class KNOWS that the AB moduli are quantized, and the torsion is how it says so over ℤ.*

Three consistency checks this reading passes immediately: (i) torsion sits in the *tower* (the reducible/abelian part — where large gauge transformations act), not the reduced part — so the **dark-sector census of phase 30 is untouched** (gravisoliton counting is torsion-free); (ii) the deficiency of HF^∞ from the "standard" answer is cut out exactly by ω — the sector remembers the polarization, as geometric quantization requires; (iii) it explains why the torsion is invisible over ℂ and ℚ (quantization integrality is an integral phenomenon), i.e., why every field-coefficient computation missed it.

## 4. New questions this sharpens (Floer-letter material)

1. **Λ*-action on torsion classes** — Jabuka–Mark explicitly cannot determine the H₁-action at k = 0; the prequantization reading predicts the torsion classes transform as **theta-characteristic-like data** under the H₁(Σ;ℤ)-translations of the Jacobian. A computable discriminator, and an open question a Floer expert would recognize as interesting independent of the physics.
2. **The U-extension problem** — their integral module structure is an open extension problem; the reading predicts the extension is the one induced by the prequantum U(1) (Gysin) structure. Also stated as a check.
3. **Coefficient transfer [audit F1]:** the bridge object is HM ≅ HF⁺ (KLT/CGH/Taubes); confirm the isomorphism's coefficient generality (ℤ vs field coefficients) before asserting the torsion statement verbatim on the monopole side.
4. **Higher torsion physics:** ℤ/3 at g ≥ 5, ℤ/4 at g ≥ 7 — the reading ties these to level structures; a mismatch in the pattern's arithmetic (elementary divisors of ∧ω^k vs Lee–Packer's orders) would falsify the interpretation cheaply. **[audit F2: compare Lee–Packer's divisor pattern with the theta-level arithmetic]**

## 5. Record updates

- **CORE §5, k = 0/tower clause:** rewritten per §3 (applied in this consolidation round) — replacing both the naive ladder (dead since phase 9/28) and the bare "Jacobian dressing" placeholder of phase 28 with the prequantization reading, tagged [conjecture].
- **Phase-28 forward item closed** ("what is the 2-torsion") — answered at conjecture level with named checks; the g = 2 universe fully decoded.
- **Falsifiability note:** unlike most interpretive moves, this one has *four* cheap kill-switches (§4 items 1, 2, 4 and the F1 transfer) — all desk work for a Floer theorist.

*Sources: Jabuka–Mark arXiv:math/0502328 (Thms 1.1, 1.2, Cor 1.3, Rmk 4.8; §1.2 circle-bundle statement, exact quotes in the extraction record); Lee–Packer for H*(E_g;ℤ); Ozsváth–Szabó for k ≠ 0 and g ≤ 2 baselines. The prequantization/Heisenberg reading and its checks are this program's [conjecture].*
