# Phase 14 — The space/time accounting, and the completeness step (worked out)

Two deliverables: **Part A**, a clarifying note on the role of the $\mathbb{R}$ axis (space vs. time across the program); **Part B**, the completeness step from Phase 12, actually worked out in the abelian case — with an explicit ledger of what is proved vs. what remains. The honest punchline of Part B: doing the work *confirms* the Phase-13 assessment — the abelian completeness is a packaging of standard theorems (Doplicher–Roberts + Pontryagin duality), and **all** the genuinely-hard, potentially-original content funnels into a **single** constructive-QFT item.

---

# Part A — What the $\mathbb{R}$ axis is, and the space/time accounting

**The question.** Going from the proven 2+1D topological-order superselection template to our setting, is the extra dimension time?

**Two comparisons, two answers.**

1. **Versus the 2+1D template: the extra dimension is *space*.** Both settings have one time. Anyonic topological order lives on a **2D spatial slice**; ours lives on a **3D spatial slice $\Sigma^3$**. The added dimension is spatial — and it is *exactly* what changes the category from **braided/modular** (anyons; braiding needs 2 spatial dimensions) to **symmetric** (ordinary Doplicher–Roberts compact gauge group; Result C — worldlines can't be braided in 3 spatial dimensions). So the space dimension is responsible for the modular→symmetric shift that put us in the DR (not the anyon) regime.

2. **Versus the bare Floer invariant: the added dimension is *time* — and that was Phase 11.** $HM(\Sigma)$ as mathematics is **timeless**: a static invariant of a 3-manifold, no dynamics, no evolving Hilbert space. Promoting it to a statement about a *quantum field theory's* superselection sectors required giving $\Sigma$ a time axis. That is the whole content of Phase 11.

**The $\mathbb{R}$ in $\mathbb{R}\times\Sigma$ wears three hats:**
- **Morse-flow parameter** — pure mathematics; gradient flow of the Chern–Simons–Dirac functional defining $HM(\Sigma)$.
- **Euclidean time** — the flow lines *are* instantons (tunneling), interpolating between time-independent solutions "at infinity in the time direction."
- **Lorentzian physical time** — after Wick rotation / Osterwalder–Schrader reflection in that axis.

Phase 11 was precisely the theorem-shaped identification of these three. So the instinct "the additional dimension is time" is **physically correct in the sense that matters**: the dimension that converts a timeless 3-manifold invariant into a live superselection structure is time, entering through the *flow = Euclidean time = (Wick) Lorentzian time* chain.

**The asymmetry, and its honest cost to the grand bet.** This makes the setup *not* space–time symmetric. All the geometry-first content — smooth structure, the $\mathrm{Spin}^c$/charge lattice, topology — lives in the **spatial** 3-manifold $\Sigma$; **time is what the OS bridge manufactures.** And this sharpens a tension already seen in Phase 7: a globally hyperbolic spacetime is *smoothly* $\mathbb{R}\times\Sigma$ (Bernal–Sánchez), so the 4-manifold here is a **standard product** with **no exotic smoothness**. The rich 4D smooth structure that Plank I makes fundamental is therefore *absent* exactly in the corner where the time-reconstruction works. Restated bluntly: **the part of the program that became rigorous (Plank II ∩ Plank III, on $\mathbb{R}\times\Sigma$) is the part where Plank I's exotic 4D content is structurally excluded.** The space/time accounting makes this unavoidable — the working corner is spatial-3-manifold physics with reconstructed time, not 4-manifold physics.

---

# Part B — The completeness step (abelian case), worked out and ledgered

**Goal (Phase 12 §7.1).** Assemble magnetic + electric + dyonic protected data into one symmetric tensor category and match it to the DR superselection category of the theory, using duality to relate the charts. Done here for the **abelian** (Maxwell / SW-abelian) theory on $M=\mathbb{R}\times\Sigma$, $\Sigma$ closed oriented 3-manifold — the case where "the dyonic $SL(2,\mathbb{Z})$" reduces to clean **Pontryagin duality**.

### B.1 The statement

> **Proposition (abelian magnetic superselection category).** For abelian gauge theory on $\mathbb{R}\times\Sigma$, the symmetric tensor category $\mathcal{T}_{\mathrm{mag}}$ of magnetic superselection sectors is
> $$\mathcal{T}_{\mathrm{mag}} \;\simeq\; \mathrm{Rep}\big(\widehat{G}\big), \qquad \widehat{G} \;=\; \mathrm{Hom}\!\big(H^2(\Sigma;\mathbb{Z}),\,U(1)\big)\ \ (\text{Pontryagin dual}),$$
> a compact abelian group; for $H^2(\Sigma;\mathbb{Z})=\mathbb{Z}^{b_2}\oplus T$ this is $\widehat G = U(1)^{b_2}\times T$. The **electric** sectors are the irreps of $\widehat G$, i.e. the Pontryagin double-dual $=H^2(\Sigma;\mathbb{Z})$ again — electric–magnetic duality is the **Pontryagin self-duality** of the picture. The objects, fusion, and grading of $\mathcal T_{\mathrm{mag}}$ are exactly those carried by the monopole Floer homology $HM(\Sigma)$ (the $\mathrm{Spin}^c=H^2$ grading, the $\mathbb{Z}/2$ statistics grading, and the $\Lambda^*(H_1(\Sigma)/\text{Tors})$ module factor — Poincaré-dual to $H^2$, encoding the dual flux data).

For example $\Sigma=S^2\times S^1$ ($b_2=1$): $\widehat G=U(1)$ — the electromagnetic gauge group, recovered from the spatial topology.

### B.2 Proof, as a ledger (what is rigorous, what rests on the open item)

| step | content | status |
|---|---|---|
| 1 | magnetic sectors $\cong H^2(\Sigma;\mathbb{Z})$ as a set; fusion = addition; conjugate = $c\mapsto -c$ | **rigorous** — known (Phase 5/8; Yang–Mills–Higgs quantization literature) |
| 2 | the category is **symmetric** ($\pm1$ statistics) because $\dim\Sigma=3$ ($3{+}1$D spacetime) | **rigorous** — general DHR (Result C) |
| 3 | a symmetric tensor $C^*$-category with these (abelian, discrete-graded) data $=\mathrm{Rep}(\widehat G)$, $\widehat G$ = Pontryagin dual | **rigorous** — Doplicher–Roberts / Tannaka–Krein; for abelian = Pontryagin duality |
| 4 | electric sectors = irreps of $\widehat G$ = double-dual = $H^2(\Sigma;\mathbb{Z})$; EM duality = Pontryagin self-duality | **rigorous** — standard (abelian EM duality is gauging $\to$ dual symmetry) |
| 5 | **this category is precisely the protected content computed by $HM(\Sigma)$ for the SW QFT** | **NOT rigorous** — rests on the Phase-11 OS/BPS bridge (controlled on the protected sector; full OS reflection positivity for the *interacting* SW QFT on $\mathbb{R}\times\Sigma$ is open) |

So steps 1–4 **prove** the Proposition *as a statement about the abelian superselection category itself* — but that statement is essentially a **corollary of Doplicher–Roberts + Pontryagin duality + the known sector classification.** It is not new; it is the expected packaging. The only place where anything could be *original* — the claim that $HM(\Sigma)$ is the carrier, i.e. that this category is the SW QFT's protected sector — is **step 5**, and step 5 is exactly the one open analytic item from Phase 11.

### B.3 What "proceeding with the theorem" actually revealed

Working the completeness step **collapses the program's two residual gaps into one.** Phase 11 left two: (a) BPS sector vs. full sector, (b) OS rigor for the interacting theory. Phase 12 added: (c) completeness across the charge lattice. Part B shows:
- **(c) is solved** in the abelian case (Proposition B.1, steps 1–4) — it is Pontryagin duality, full stop;
- **(a) and (b) merge** — once the category is fixed by DR, "is the BPS/protected content the whole superselection structure?" *is* the question "does the OS bridge identify $HM$ with the protected sector for the interacting theory?" — i.e. step 5.

So after fourteen phases the **entire** edifice — every clause, both planks of the surviving corner, all three earlier gaps — reduces to **one** statement:

> **The single remaining item.** Osterwalder–Schrader reflection positivity (Euclidean → Lorentzian reconstruction) for the interacting abelian Seiberg–Witten QFT on $\mathbb{R}\times\Sigma$, identifying $HM(\Sigma)$ with the protected superselection content.

### B.4 The honest verdict on this being "the theorem"

- **What we have:** a clean, *proved* statement (B.1, steps 1–4) — which is a corollary of standard results, hence (per Phase 13) **not novel**.
- **What we don't have:** step 5, the one thing that would make $HM\leftrightarrow$ superselection an *original* result — and it is a **recognized-hard constructive-QFT problem** (rigorous OS reconstruction of an interacting 4D gauge theory), not something reachable by further synthesis.
- **Therefore:** "proceeding with the theorem" terminates honestly *here*. The next step is not another phase of assembling known results; it is attacking a hard analysis problem that the constructive-QFT community has not solved in general. We have reduced the whole program to that single problem and shown everything else is standard. **That reduction is the result of Phase 14 — and it is the right place for synthesis to stop and real analysis (or a real expert) to begin.**

---

## Combined status after Phase 14

The surviving corner (Plank II ∩ Plank III, on $\mathbb{R}\times\Sigma$) is now: a proved label/category statement (standard), with the lone original-if-true claim ($HM$ = protected superselection content) reduced to a single, named, recognized-hard OS-reconstruction problem. Part A shows this corner is **spatial-3-manifold physics with reconstructed time** — structurally **disjoint from Plank I's exotic 4D content** (which needs the non-product, non-globally-hyperbolic regime). The grand bet's probability is unchanged. What has changed over fourteen phases is that the bet is now **completely mapped**: its working corner is standard mathematics up to one hard analysis problem, and its distinctive corner (exotic 4D) is provably *elsewhere*, in the regime where the tools don't yet exist.

---

## Sources
- Electromagnetic duality of abelian gauge theory = Pontryagin duality; gauging $G\to$ dual symmetry $\widehat G$; Tannaka–Krein reconstructs $G$ from $\mathrm{Rep}(G)$: [Abelian duality in topological field theory (arXiv:2112.02199)](https://arxiv.org/pdf/2112.02199); [Pontryagin/Tannaka–Krein duality overview](https://surya-teja.com/2011/03/13/tannaka-krein-duality-pontryagin-duality/).
- Electric charge non-localizable by Gauss law; superselection structure of electric charge / infrared subtleties; on closed $\Sigma$ net charge is constrained so sectors are flux/Wilson-line (cohomological): [Ruzzi et al., "Where charged sectors are localizable: a viewpoint from covariant cohomology" (arXiv:2306.08449)](https://arxiv.org/pdf/2306.08449).
- Doplicher–Roberts / Tannaka–Krein reconstruction of a compact group from a symmetric tensor category: [Doplicher–Roberts, CMP 131 (1990) 51](https://link.springer.com/article/10.1007/BF02097680); Phase-4 document.
- $HM(\Sigma)$ module structure over $\mathbb{Z}[U]\otimes\Lambda^*(H_1(\Sigma;\mathbb{Z})/\text{Tors})$; $\mathrm{Spin}^c$ grading; Floer flow = instantons in Euclidean time: Kronheimer–Mrowka, *Monopoles and Three-Manifolds*; [Manolescu (arXiv:1508.00495)](https://arxiv.org/pdf/1508.00495).
- Bernal–Sánchez: globally hyperbolic $\Rightarrow$ smoothly $\mathbb{R}\times\Sigma$ (Part A asymmetry): [arXiv:gr-qc/0306108](https://arxiv.org/abs/gr-qc/0306108).
