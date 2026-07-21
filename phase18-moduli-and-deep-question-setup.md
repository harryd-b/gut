# Phase 18 — The moduli case ($\Sigma_g\times S^1$), as the laboratory for the deep question

**Why this phase, and its role.** The deep question — *is the protected/topological stratum **foundational** (it determines the full dynamics) or merely **skeletal** (it's the rigid bones; the dynamical physics is independent information)?* — is **invisible** in the isolated/nondegenerate cases (PSC, Brieskorn): there the protected and dynamical strata are gap-separated, decoupled by fiat, so the question has no content. The **moduli case is the minimal arena where flat directions couple the two strata**, turning the deep question into a sharp finite-dimensional one. This phase does the moduli case *as that laboratory*, and extracts a concrete preliminary answer.

**Verdict (one line).** Two findings. **(Technical)** On $\Sigma_g\times S^1$ the SW critical set is the **Jacobian torus** (Morse–Bott moduli); positivity *survives* (Hodge theory: harmonic forms on the moduli space have positive norm), but the **no-cancellation guard fails** (the torus has cohomology in both parities, so boson–fermion cancellation is now possible) — the bridge here needs the *full moduli-space structure*, not isolated-point data. **(Deep question)** In this laboratory the protected data is $H^*(\text{moduli})$ and the dynamical data is the *geometry/effective action on the moduli space*, and **cohomology manifestly under-determines geometry** — so, in the first setting where the question has content, the protected stratum is **skeletal, not foundational.** This converges with the categorical fact that **modular data does not even determine the category, and the category does not determine the CFT** (Frobenius/non-chiral data needed). Two independent lines, same answer: *skeletal*.

---

## 1. The moduli setup

Take $\Sigma=\Sigma_g\times S^1$, $\Sigma_g$ a genus-$g$ surface ($g\ge 1$). Then:
- $b_1(\Sigma)=2g+1>0$, $H^2(\Sigma;\mathbb{Z})=\mathbb{Z}\oplus\mathbb{Z}^{2g}$ — **multiple magnetic sectors** (first multi-sector test, also wanted since Phase 10).
- For non-torsion $\mathrm{Spin}^c$ structures the SW–Floer homology was computed (Muñoz–Wang); the relevant **moduli space of SW solutions is the Jacobian / Picard torus** $\mathrm{Jac}(\Sigma_g)=T^{2g}$ (a reducible component homeomorphic to the Jacobian torus, in the Seifert/product computations). So the critical "set" is a **torus**, not isolated points: genuine **Morse–Bott** moduli with flat directions.

This is exactly the regime the Brieskorn argument (Phase 16) excluded.

## 2. Technical status of the no-cancellation lemma here

**Positivity — survives.** Over a Morse–Bott moduli space $\mathcal M$, the protected states are not Gaussians at isolated points but **$L^2$/harmonic cohomology classes of $\mathcal M$**. By Hodge theory the harmonic representatives have **positive norm** (the Hodge inner product is positive-definite). So OS positivity is *not* lost in the moduli case — it upgrades from "Gaussian at a point" to "Hodge inner product on $\mathcal M$." Good news for the bridge.

**No-cancellation — fails as a free guard.** The Brieskorn argument used grading concentration (no opposite-parity partners). The Jacobian torus $T^{2g}$ has cohomology $H^*(T^{2g})=\Lambda^*\mathbb{R}^{2g}$ — nonzero in **every** degree, both parities. So opposite-parity partners *exist*, and boson–fermion cancellation is now possible in principle. Whether $HM(\Sigma)=\mathcal H^{\text{phys}}_{\text{BPS}}$ now depends on the **detailed structure of $\mathcal M$ and the Floer/physical differential on $H^*(\mathcal M)$** — not settled by a parity slogan.

**Net technical reading.** The moduli case is exactly where the lemma stops being automatic: positivity is fine (Hodge), but the identification $HM=\mathcal H^{\text{phys}}_{\text{BPS}}$ requires controlling the full moduli geometry. This is the honest boundary of the Phases 15–16 results — and, as anticipated, the kernel lives here.

## 3. The deep question, made finite-dimensional

Now the payoff for which we did this. In the moduli case the two strata are concrete objects on the *same* space $\mathcal M=\mathrm{Jac}(\Sigma_g)$:

| stratum | what it is on $\mathcal M$ |
|---|---|
| **protected / topological** | the cohomology $H^*(\mathcal M)$ (= $HM(\Sigma)$ in the Morse–Bott computation), the sector category, $\gamma=\log\mathcal D$ |
| **dynamical / non-protected** | the **geometry** of $\mathcal M$: the metric (from the kinetic term), the effective potential lifting flat directions, the full spectrum of fluctuations |

The deep question becomes: **does $H^*(\mathcal M)$ determine the geometry/dynamics on $\mathcal M$?** And the answer is an unambiguous **no**:
- the cohomology of a torus is $\Lambda^*\mathbb{R}^{2g}$ for *every* flat or curved metric, *every* choice of potential — cohomology is a homotopy invariant, blind to the metric, the potential, the spectrum;
- infinitely many distinct dynamical theories on $\mathcal M$ (different effective actions, different liftings of the flat directions, different excited spectra) share the *same* $H^*(\mathcal M)$.

So **in the first setting where the deep question has content, the protected data provably does not determine the dynamical data.** The protected stratum is **skeletal**: it fixes the topological bones (which sectors, the universal entropy, the BPS count) and leaves the dynamical flesh (metric on moduli, lifting, spectrum) as independent information.

## 4. The same answer from the categorical side (independent line)

This is not a quirk of the torus. The general, categorical version of the deep question has a known answer in the same direction:
- **Modular categories are not determined by their modular data** ($S,T$ matrices) — even the protected category isn't fixed by its protected numerical invariants.
- **The modular tensor category does not determine the CFT** — a full (non-chiral) conformal field theory needs *extra* data, a symmetric special Frobenius algebra (Fuchs–Runkel–Schweigert); different CFTs share one MTC.

So at the **local/geometric** level (cohomology ↛ geometry of moduli) and the **global/categorical** level (category ↛ full theory), the protected data under-determines the dynamics. Two independent lines converge: **skeletal.**

## 5. What "skeletal" precisely means for the bet (stated carefully)

- It does **not** say geometry-first is wrong or that the protected results (Planks II–III on the protected stratum) are diminished — those stand.
- It **does** say: the protected/topological data **alone** does not reconstruct the full dynamical physics. "Everything protected is geometry" is secure; "**everything** is geometry" would additionally require a *principle* that supplies the missing dynamical data (metric on moduli, Frobenius/non-chiral data, the full spectrum) from geometry — and the protected data by itself does not contain it.
- So the bet's strongest defensible form after Phase 18: **geometry-first is true on, and only on, the protected stratum; extending it to the full theory requires new, non-protected input that the program has not produced and that the under-determination results suggest is genuinely independent.**

This is the honest preliminary answer the moduli laboratory delivers — and it is exactly the kind of finite-dimensional, checkable model the deep question needed.

## 6. The deep question, now sharply re-posed for the next phase

Phase 18 answers the *easy direction* (protected alone ↛ dynamics: skeletal). The next phase should ask the *hard, interesting* direction, now precisely formulable:

> **Is there a geometry-first *principle* that supplies the missing dynamical data?** Concretely: does the requirement that the dynamical data itself be *geometric* (e.g. the moduli-space metric = the natural $L^2$/Weil–Petersson metric induced by the geometry; the lifting potential = a geometric functional; the Frobenius/non-chiral data = fixed by orientation/Poincaré-duality of $\Sigma$) **uniquely fix** the dynamics from the geometry — even though the *protected data* alone does not?

If **yes**, the bet is rescued in a stronger form: not "protected determines dynamics," but "geometry determines dynamics, with the protected data as its topological shadow and the geometric metric/structure as the rest." If **no**, the bet is fundamentally skeletal. This is the real fork, and Phase 18 has cleared the ground to state it exactly.

## 7. Verdict
- **Moduli technical result:** positivity survives (Hodge on $\mathcal M$); no-cancellation is no longer automatic (both-parity cohomology) and needs the full moduli geometry — the kernel lives exactly here.
- **Deep question, easy direction — answered:** protected data alone does **not** determine dynamics (cohomology ↛ geometry; modular data ↛ category ↛ CFT). The protected stratum is **skeletal**.
- **Deep question, hard direction — sharply posed:** does a *geometry-first principle* (geometric metric + geometric non-chiral data) fix the dynamics that the protected data alone cannot? This is the next phase, and it is the genuine fork for the whole bet.

---

## Sources
- SW–Floer of $\Sigma_g\times S^1$ for non-torsion $\mathrm{Spin}^c$; moduli space = Jacobian/Picard torus: [Muñoz–Wang, "Seiberg–Witten–Floer homology of a surface times a circle for non-torsion spin-c structures" (arXiv:math/9905050)](https://arxiv.org/abs/math/9905050); [Mrowka–Ozsváth–Yu, "Seiberg–Witten monopoles on Seifert fibered spaces" (arXiv:math/9612221)](https://arxiv.org/pdf/math/9612221).
- Morse–Bott / Hodge positivity (harmonic representatives positive-norm): standard Hodge theory; Floer Morse–Bott framework (Kronheimer–Mrowka).
- Modular categories not determined by modular data: [Mignard–Schauenburg / "Modular categories are not determined by their modular data," Lett. Math. Phys. (2021)](https://link.springer.com/article/10.1007/s11005-021-01395-0). MTC does not determine the CFT (need Frobenius algebra / non-chiral data): [Fuchs–Runkel–Schweigert program; "Twenty-five years of 2d RCFT" (arXiv:0910.3145)](https://arxiv.org/pdf/0910.3145).
