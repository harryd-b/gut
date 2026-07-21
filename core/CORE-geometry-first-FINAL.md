# Geometry-First Physics and the Protected Stratum
### A constructive synthesis: how four-dimensional geometry fixes physics, and the stiffness that protects it

*Core document. Constructive treatment: the main text presents what the program **builds**. Every claim is tagged by status — **[proved]**, **[established (others')]**, **[conjecture]**, **[interpretation]**. Routes considered and set aside are catalogued in the **Glossary** (§8). Provenance to the 25 working phases is in the Appendix.*

---

## Abstract

We develop a **geometry-first** thesis: that the physical world is, at bottom, the geometry of a single four-dimensional manifold — with forces, quantum structure, matter, and even time *derived from* that geometry. The constructive core is that geometry fixes a great deal on a **protected stratum**: the gauge group is the Tannaka dual of the local-algebra net **[established]**; charge quantization is the integrality of a degree-2 cohomology class — Kaluza–Klein charge quantization *without the extra dimension* **[established]**; superselection sectors and the universal (topological) term of entanglement entropy are read off the *same* geometry-derived sector category **[established]**; and the entire low-energy effective dynamics is the special geometry of the Seiberg–Witten spectral curve, which is at once an integrable system and (by Taubes) the $J$-holomorphic-curve data of the symplectic 4-geometry **[established]**. Exotic smoothness is physical — it sources gravity **[proved]**. Unifying these, we advance the program's central conjecture, **Plank IV**: that the *protecting structure* — what lets geometry fix physics at all — is the **stiffness ("folding rigidity") of spacetime**, its Godbillon–Vey invariant; spacetime can be folded (foliated) only so far before it becomes rigid, and **that rigidity is both the protection and, through its modular flow, the clock that generates time** — yielding the observed 3+1 split and the arrow of time from one structure **[conjecture]**. We give the constructive correspondence (monopole Floer homology = the protected superselection content, proved at the label level and on a controlled family) and the forward program. This is a **synthesis of established results** organized around new framings; the candidate-novel content (Plank IV foremost) awaits the scholarship check of §6. Alternatives reviewed and eliminated are listed in the Glossary (§8).

---

## 1. The thesis — four planks

The geometry-first bet is a set of **planks** (conjectures by nature):

- **Plank I — geometry is fundamental; fundamentally 3-dimensional, with emergent time.** The smooth 3-manifold $\Sigma$ (space) — carrying the AQFT net, the superselection sectors, $HM(\Sigma)$, and its GV foliation/stiffness — is ontologically primitive; **time is not a fourth dimension but the emergent modular flow** (§4–§5). The 4-manifold $\mathbb R\times\Sigma$ (and the exotic $\mathbb R^4$, built from a codim-1 foliation of $S^3$) is reconstructed; 4-manifold richness/exotic smoothness supplies the dynamics, but the apparatus lives on $\Sigma$. This aligns with *gravitizing the quantum* (Berglund–Hübsch–Mattingly–Minic, arXiv:2203.17137): the dynamical arena is the *quantum* geometry with time emergent — see §8B.
- **Plank II — quantum structure is geometry's shadow.** Entanglement and the operator/Hilbert structure are the operator-algebraic shadow of the geometry (the AQFT net).
- **Plank III — forces are geometry.** The gauge structure is read from the geometric data, not added independently.
- **Plank IV — the protecting structure is spacetime's *stiffness* ("folding rigidity").** **[central new conjecture]** What lets geometry fix physics at all is a *protecting structure*; the proposal is that it is the **stiffness of spacetime** — its Godbillon–Vey folding rigidity. Folding (foliating) spacetime is possible only so far before it becomes rigid (like paper); any nonzero fold makes it rigid (a type III von Neumann factor), and **that rigidity is the protection** — and, via its modular flow, the **clock** that generates time.

The thesis, in one line: *a single four-dimensional geometry — whose stiffness both protects its physics and generates its time — is, with no extra dimensions and no fundamental supersymmetry, the substrate of physics.* What follows is what this picture **builds**.

## 2. What geometry fixes (the constructive results)

### 2.1 The gauge group, from the net **[established]**
The compact gauge group is the **Tannaka dual of the category of superselection sectors** of the local-algebra net (Doplicher–Roberts). On $M=\mathbb R\times\Sigma$ the abelian magnetic sector category is $\mathrm{Rep}(\widehat G)$ with $\widehat G$ = Pontryagin dual of $H^2(\Sigma;\mathbb Z)$ **[proved here as a corollary of DR + Pontryagin duality]**. The gauge group is thus a functional of the geometry, exactly as Plank III asks.

### 2.2 Charge quantization, from cohomology **[established]**
Magnetic charge is the first Chern class, $g=c_1\in H^2(\Sigma;\mathbb Z)$ — Dirac quantization as the integrality of a characteristic class; via compactness this quantizes electric charge too. This is **Kaluza–Klein charge quantization without the extra dimension**: the quantizing integer is a Chern number of the 4-geometry, not a momentum on a fifth dimension.

### 2.3 New charges from topology **[established]**
Nontrivial $\pi_1(\Sigma)$ produces Aharonov–Bohm superselection sectors (representations of $\pi_1$); non-abelian $\pi_1$ yields non-abelian sectors. Charge *content* is generated by spacetime topology.

### 2.4 Quantum structure as geometry's shadow **[established]**
The net of local (type III$_1$) algebras fixes the factorization into subsystems and, by Reeh–Schlieder, the vacuum's entanglement. The **universal (topological) term of entanglement entropy**, $\gamma=\log\mathcal D$, is fixed by the superselection-sector category — *the same category §2.1 derives from the geometry* (Casini–Huerta–Magán–Pontello + Kitaev–Preskill). Worked example: $S^2\times S^1\Rightarrow\widehat G=U(1)$, universal coefficient $-1$. So the universal entanglement is geometric, and it is *the same object* as the gauge sector — Planks II and III meet here.

**The bulk (area-law) term is also geometric — carried by stiffness, not by local fields [established mechanism + interpretation].** Entanglement entropy splits as $S = \alpha\,\text{Area} - \gamma + \cdots$. One must separate the *correlations* from the *magnitude*: Bell/Tsirelson forbids local fields carrying the *correlations* (the carrier stays the type III$_1$ net, Reeh–Schlieder), but it does **not** forbid the area-law *coefficient* from being geometric — and it is. By **Susskind–Uglum**, the UV-divergent area term *renormalizes Newton's constant*; the physical area-law that remains is **Bekenstein–Hawking, $S=\text{Area}/4G$** — an area measured in units of the **gravitational stiffness $1/G$**. Since $1/G$ is the gravitational/Planck-scale reading of Plank IV's stiffness (§4, §5.1), **both** terms of the entanglement entropy are carried by stiffness: the universal term by the *topological* (GV/sector) stiffness, the bulk term by the *gravitational* stiffness. The bulk entanglement is carried by **the stiffness of spacetime itself**, not by local geometric fields. *(That the two stiffnesses — GV and $1/G$ — are the **same** is conjecture; that **each** term is geometric via a stiffness is established.)*

**This also supplies a candidate dynamical mechanism (cf. §6.1) — via an established program that must be credited.** The variational principle Plank IV needs is an **entanglement-equilibrium / first-law** condition, and this is a decade-deep, much-cited body of work, *not* original here:
- **Jacobson** (entanglement equilibrium): stationarity of vacuum entanglement entropy at fixed volume holds *iff* the (nonlinear) Einstein equation holds — intrinsic, semiclassical.
- **Faulkner–Guica–Hartman–Myers–Van Raamsdonk** (gravitation from entanglement): the **entanglement first law** $\delta S = \delta\langle H_{\text{mod}}\rangle$ for all ball regions is equivalent to the **linearized Einstein equations** — the precise version (later extended to nonlinear). *Caveat: holographic — it derives the **bulk** equations from a **boundary** CFT, i.e. **emergent** geometry, which is in tension with Plank I (geometry fundamental). The Jacobson/Casini intrinsic versions are the Plank-I-compatible ones to lean on.*
- **Casini** (the QFT-rigorous backbone): relative entropy, the modular Hamiltonian, and the Bekenstein bound from relative-entropy positivity make these statements precise in flat-space QFT.

The fit with the framework is exact: the **modular Hamiltonian $H_{\text{mod}}$** in the first law *is* the generator of the modular flow = thermal time = Plank IV's engine. So the candidate derivation is **GV stiffness $\to$ modular flow $(H_{\text{mod}})$ $\to$ first law $\delta S = \delta\langle H_{\text{mod}}\rangle$ $\to$ (linearized) Einstein equations.** What this program supplies — that equilibrium/first-law *derives* the dynamics — is *theirs* (established); what would be new here is only the identification of $H_{\text{mod}}$'s modular flow with the **Godbillon–Vey stiffness** of the exotic foliation (see §6 novelty).

### 2.5 Low-energy dynamics, from special geometry **[established]**
The entire low-energy effective action is the holomorphic **prepotential** $F$, read off the **Seiberg–Witten spectral curve** ($\tau=\partial^2F$, the moduli metric, BPS masses, couplings). That curve is simultaneously **(i)** the spectral curve of an **integrable system** (Donagi–Witten) and **(ii)**, by **Taubes' $SW=Gr$**, the **$J$-holomorphic-curve data of the symplectic 4-geometry**. One geometric object — the curve — is the gauge group's source, the integrable structure, the exotic-smoothness detector, and the law of the low-energy dynamics.

### 2.6 Exotic smoothness is physical **[proved]**
Exotic smoothness **sources gravity** (Brans conjecture; proved for compact manifolds by Asselmeyer-Maluga and for exotic $\mathbb R^4$ by Sładkowski): it curves spacetime like matter, even in vacuum. The smooth structure — Plank I's primitive datum — does physical work.

## 3. The unifying principle: the protected stratum

Across §2, geometry fixes physics on a **protected stratum**, and where it fixes *dynamics* it does so through a **protecting structure**. The master statement:

> *Geometry fixes physics to exactly the extent that a protecting structure is present — supersymmetry, holomorphy, integrability, or modular/thermal-time. The choice of protecting structure is the program's only freedom; everything geometry achieves, it achieves on the protected stratum.*

This is why the planks cohere: the sector category, the gauge group, the universal entanglement, the spectral curve, and (Plank IV) the stiffness are one structure seen from different sides.

## 4. Plank IV: stiffness as the protecting structure — and the origin of time

### 4.1 Stiffness = folding rigidity = the protection **[conjecture; mapping established]**
The protecting structure is identified physically as the **stiffness of spacetime**, by the paper-folding intuition: a sheet folds only so far before it is rigid. Precisely, in the live channel:
- *"Folding into layers"* = a **codimension-1 foliation** (a stack of leaves) — the structure defining the exotic $\mathbb R^4$ (radial family ↔ foliations of $S^3$).
- *"Amount folded / stiffness"* = the **Godbillon–Vey invariant**, which Thurston interpreted as the **"helical wobble" of a pyramid of stacked discs** (Reinhart–Wood: via leaf curvatures); it varies continuously (uncountably many values).
- *"Becomes rigid; the protection"* = $\mathrm{GV}\neq0 \Rightarrow$ no invariant transverse measure $\Rightarrow$ **type III von Neumann factor** $\Rightarrow$ a canonical **modular (thermal-time) flow** = the protecting structure of §3.

So **folding = foliation, stiffness = Godbillon–Vey, rigidity = type III, protection = thermal-time.** Connes' theorem makes this canonical: the *flow of weights* — the state-independent invariant of the factor — *is determined by the GV class*, so the protection is geometrically pinned, not arbitrary.

### 4.2 Time is what the stiffness generates **[interpretation]**
In this picture the four dimensions are all geometric (the folded Euclidean 4-geometry); **Lorentzian time is emergent** — the modular flow driven by the GV stiffness (Connes' flow of weights; Connes–Rovelli thermal time). The stiffness does not merely protect; it is the **clock**. *(This refines Plank I from "fundamental Lorentzian tetrad" to "fundamental Euclidean 4-geometry + GV stiffness, with time emergent.")*

### 4.3 The 3+1 split and the arrow of time, from one structure **[conjecture]**
- A codim-1 foliation slices the 4-geometry into **3-dimensional leaves** (the perceived spatial world) plus one **transverse direction**. We are embedded *in a leaf* ⟹ we navigate its 3 directions as "space"; the transverse (folding) direction is where the modular flow runs ⟹ we experience it *flowing* as "time."
- **Why 3, not 2+2:** Godbillon–Vey is a **codimension-1** invariant; codim-1 in 4D forces **3 leaf + 1 transverse**. If the stiffness is GV, the world *must* present as 3+1.
- **Arrow of time, free:** the modular (KMS) flow is intrinsically **directional**, so emergent time is *one-way*. The 3+1 split *and* time's one-wayness come from the *same* structure — where standard physics must add the arrow as a separate boundary condition.

### 4.4 Why 4D is the special dimension **[established + interpretation]**
The paper-folding *limit* is a real theorem — **Cheeger finiteness** (bounded curvature + diameter + volume ⟹ finitely many diffeomorphism types). But **dimension 4 is the exception** (the clean finiteness holds for $n\neq 3,4$; 4-manifolds admit *uncountably many* exotic structures). So 4D is the one dimension that **folds without a finite limit** — which is precisely why it is exotic, and why Plank I singles it out. The richness Plank I prizes and the stiffness/folding of Plank IV are the same fact about dimension four.

## 5. The constructive core: monopole Floer = the protected superselection content

The clearest single construction unifying the planks. On globally hyperbolic $\mathbb R\times\Sigma$ for the abelian Seiberg–Witten (monopole) theory:
- **Label theorem [proved]:** magnetic superselection sectors $\cong \mathrm{Spin}^c(\Sigma)\cong H^2(\Sigma;\mathbb Z)$ = the grading set of monopole Floer homology $HM(\Sigma)$.
- **Internal dictionary [conjecture]:** $HM(\Sigma)$ *is* the protected content of each sector — the reducible/$U$-tower is the global-$U(1)$ charge ladder, the Frøyshov invariant is the sector's ground-state grading, irreducibles are charged-matter bound states.
- **The bridge [proved on the protected sector, PSC ∪ all Brieskorn spheres]:** via Witten–Morse ($HM$ = SUSY ground states), the topological twist ($HM$ = the TQFT Hilbert space on $\Sigma$), and Osterwalder–Schrader positivity on the protected sector. Tested on $S^3$ (confirmed, and the dictionary sharpened) and all Brieskorn homology spheres (forced by isolated/nondegenerate critical sets).
- **Stiffness reading [conjecture]:** the relevant $\Sigma$-data is exactly the Godbillon–Vey/foliation stiffness of Plank IV; $HM(\Sigma)$ is its protected, computable face.

This is the program's most developed result: a proved label-level correspondence plus an internal correspondence confirmed clause-by-clause on a controlled family, all carried by the same stiffness/spectral-curve object.

## 6. Status and the forward program

What completes each result (constructive open problems), in order of leverage:

1. **Plank IV → mechanism (the decisive step).** Promote the stiffness identification from interpretation to mechanism. The variational principle is an **entanglement-equilibrium / first-law** condition — and that mechanism already exists (Jacobson; Faulkner–Guica–Hartman–Myers–Van Raamsdonk; Casini's relative-entropy/modular-Hamiltonian work): the first law $\delta S=\delta\langle H_{\text{mod}}\rangle$ yields (linearized, then nonlinear) Einstein equations. The **new** step is to show the modular Hamiltonian's flow *is* the **Godbillon–Vey stiffness** of the exotic foliation (Connes' flow of weights = GV), so that "minimizing geometric tension" = extremizing GV = the equilibrium condition. *(Advance in hand: the flow is geometrically canonical, the favorable setting. Caveat: Faulkner's version is holographic/emergent — in tension with Plank I; lean on the intrinsic Jacobson/Casini versions.)*
2. **Predictivity of the exotic channel.** Fix one exotic (GV) structure and derive $\{\Lambda,\text{inflation},m_H,m_\nu\}$ from it with no further freedom; eliminate the shared modulus pairwise and test the **parameter-free relation** $\Phi(\Lambda,m_H)=0$ against data. One confirmed relation makes the channel predictive.
3. **Complete the constructive correspondence (§5)** beyond the protected sector / beyond Brieskorn (the moduli / higher-$b_1$ case, e.g. $\Sigma_g\times S^1$); and constructive Osterwalder–Schrader for the interacting theory.
4. **Scholarship gate (prerequisite to any novelty claim).** This is a **synthesis of established results** organized around new framings. **What is *not* novel here (and must be credited as others'):** that entanglement equilibrium / the first law *derives* gravitational dynamics (Jacobson; Faulkner–Guica–Hartman–Myers–Van Raamsdonk; Casini); that the universal entanglement term is the sector category (Casini–Huerta–Magán–Pontello); the DR/Tannaka, special-geometry, Taubes, and Connes–GV facts. **The genuinely candidate-novel content is narrow:** (a) identifying the protecting modular structure with the **Godbillon–Vey stiffness** of the exotic foliation (and "rigidity = protection = clock"); (b) the **monopole-Floer ↔ DHR** join. Both are unverified by machine search and **folklore-adjacent** until confirmed. Run MathSciNet/zbMATH and consult experts in the overlap — **the entanglement-equilibrium/modular community (Faulkner, Casini, Jacobson; and Rovelli on thermal time)**, the **Rome AQFT school (Vasselli, Ruzzi)**, **Asselmeyer-Maluga–Król**, and **SW-Floer-as-TQFT (Manolescu)**. *Recommended order:* scholarship → predictivity test (2) → mechanism (1) and the constructive gaps (3).

---

## 7. Summary

Geometry-first, pursued constructively, builds a coherent picture on the **protected stratum**: geometry fixes the gauge group, the charges, the sectors, the universal entanglement, and — through special geometry — the low-energy dynamics; exotic smoothness is physical; and the protecting structure that makes all of this possible is, on the central conjecture, the **stiffness of spacetime** (Godbillon–Vey folding rigidity), which doubles as the origin of time and of the 3+1 split. The four planks are one object — the stiffness/spectral-curve of the 4-geometry — seen from different sides. The forward program is the four items of §6.

---

## 8. Glossary — routes reviewed

### A. Structural routes set aside
Each is a genuine result; together they delimit where the constructive picture lives.

| Route considered | Why set aside |
|---|---|
| **Torsion as the gauge potential** | Wrong representation / gauge group (torsion is field-strength-like; its gauge freedom is local Lorentz, not internal). Weyl's 1918 obstruction. |
| **Merging spacetime + internal symmetry into one group** | Coleman–Mandula forbids it (except via SUSY, Haag–Łopuszański–Sohnius). The program drops the global S-matrix instead. |
| **Emergent (composite) graviton or gauge bosons** | Weinberg–Witten forbids composite massless spin-$>1$ with covariant currents. Graviton stays fundamental; gauge fields co-fundamental. |
| **Geometry → dynamics via the 4-manifold's *period map*** | Hodge-weight obstruction: a prepotential is weight-1 or weight-3; a 4-manifold's own periods are weight-2 (symmetric polarization, no prepotential). |
| **Exotic smoothness changing the *charge spectrum*** | Charge sectors are built from $\pi_1, H^2$ (homotopy invariants), identical for homeomorphic manifolds. Exotic smoothness acts on dynamics/gravity, not the spectrum. |
| **Bulk entanglement carried by local geometric fields** | Bell/Tsirelson excludes a local-field carrier of the *correlations*. (The bulk *magnitude* is still geometric — Area/$4G$; see §2.4.) |
| **A literal "finite fold count" for spacetime** | Cheeger finiteness gives a finite count in dimensions $\neq3,4$; **4D inverts it**. 4D rigidity comes from any nonzero fold (GV $\neq0$), not from running out of folds. |
| **Superselection content = raw BPS spectrum** | The raw BPS spectrum wall-crosses; superselection is robust. Retained statement uses *wall-crossing-invariant* BPS data ($=HM(\Sigma)$). |
| **Fully non-SUSY, *unprotected* "geometry → dynamics"** | tt\*/non-abelian-Hodge exists without SUSY but fixes dynamics only with a protecting $(2,2)$/holomorphic structure. Retained: protection is required, but need not be SUSY. |
| **"Brane thickness" as a sheet in a higher-dimensional bulk** | Contradicts Plank I (no extra dimensions). Retained only as *intrinsic* stiffness — the foliation's GV, or $\sim1/G$. |
| **Globally hyperbolic spacetime carrying exotic smoothness** | Mutually exclusive: globally hyperbolic ⟹ smoothly $\mathbb R\times\Sigma$ (Bernal–Sánchez); exotic $\Sigma\times\mathbb R$ is never globally hyperbolic. |

### B. Predictivity & experimental routes tested (this round)
Adversarial audits of candidate predictions. **SET ASIDE** = no verified/parameter-free prediction; **RETAINED** = a genuine result or a live falsifiable handle. Integrity rule observed: no fitted relation presented as a prediction.

| Route tested | Outcome | Status |
|---|---|---|
| **Lepton masses from hyperbolic knot volumes** | Naive mass $\propto$ volume off by $\times148$; mass $\propto e^{cV}$ with simplest-knot assignment predicts $m_\tau/m_\mu=9.4$ vs measured $16.8$ (off $44\%$). Matching needs an *unforced* knot↔lepton assignment = fitting. | **SET ASIDE** |
| **Inflation $(n_s,r)$** | Formulas are *just* Starobinsky ($n_s=1-2/N$, $r=12/N^2$); numbers ($0.961,\,0.0046$) match Planck, but $N\approx51$ is set by *choosing* the 3-manifold $\Sigma(2,5,7)$. Non-distinctive from vanilla $R^2$ inflation. | **SET ASIDE** (fitted via manifold choice) |
| **Koide relation $Q=2/3$ from Bloch/dilogarithm** | No mechanism: dilogarithm special values give $\pi^2$-multiples / transcendentals, not the rational $2/3$; no $\sqrt m$ structure; AMK never address it. | **SET ASIDE** (aspirational) |
| **Exactly 3 generations from braids** | Not forced: AMK obtain 3 only as a self-described "speculative" lower bound; Bilson-Thompson gives 1 clean generation but *unbounded* count. | **SET ASIDE** (count not forced) |
| **Dark energy $w=-1$, no evolution (Mostow rigidity)** | Falsifiable but *weakly distinctive* (degenerate with $\Lambda$CDM; only forbids evolution); AMK's argument is hedged and epoch-dependent. **Currently DISfavored by DESI DR2 + CMB + SNe (~3.8–4.2$\sigma$ preference for *evolving* DE).** | **RETAINED** — the one **live, near-term, falsifiable** handle (Euclid/DESI-full decide), *currently in mild tension* |
| **Geometric dark matter ⇒ null non-gravitational detection** | A real but weak *null* prediction; degenerate with primordial-black-hole and modified-gravity dark sectors. | **RETAINED** (weak falsifiable; cannot uniquely confirm) |
| **Gravitizing the quantum ⇒ higher-order interference $I_3\neq0$ + clock $\alpha\neq0$** (our modular = state-dependent evolution; topology change as engine — arXiv:2203.17137) | **Distinctive vs standard QM (not vs ΛCDM); currently measured:** $\kappa=0.006\pm0.012$ (photons), $0.007\pm0.003$ (NMR); JUNO/atom interferometry & optical-clock $\alpha\lesssim10^{-5}$ upcoming. Shared with the whole nonlinear-QG class ⇒ not a unique fingerprint. **Next target:** predict $\kappa$ from the GV stiffness. | **RETAINED — the best experimental handle** (distinctive, non-cosmological, currently testable) |
| **Monopole-Floer $HM(\Sigma)$ ↔ DHR superselection (label level)** | Not found in the literature; the $H^2$ (magnetic) analogue of Vasselli–Ruzzi's proven $H^1$ (Aharonov–Bohm) sector theory — **achievable and modestly novel**. (Internal level — Floer $\mathbb Z/2$-grading = DHR statistics — remains conjecture, out of reach as stated.) | **RETAINED — the one positive, achievable new result** (mathematical, not experimental) |

**Net experimental standing (honest):** the framework *does* touch experiment. Its **best handle** (via *gravitizing the quantum*, §8B / phase26) is **distinctive vs standard QM and non-cosmological** — higher-order interference $I_3\neq0$ and atomic-clock $\alpha\neq0$, currently measured — but it is *shared with the whole nonlinear-quantum-gravity class*, so it can support or constrain that class without singling out this framework. Its cosmological handle ($w=-1$) is degenerate with ΛCDM and presently in mild DESI tension. Across every route tested, no *unique-fingerprint* parameter-free prediction has been found; the concrete next target is to **predict the size $\kappa$ of $I_3$ from the GV stiffness** — a distinctive, currently-testable number. Grounding is now real (quantum-foundational), still short of a fingerprint.

---

## Appendix — provenance
The 25 working phases plus this round's five audits map to the document as: gauge group / charges / sectors (§2.1–§2.3); entanglement incl. the bulk-term resolution (§2.4); special geometry / integrability / Taubes (§2.5); exotic smoothness sources gravity (§2.6); the protected-stratum principle (§3); the stiffness/time/3+1 development (§4); the monopole-Floer correspondence and its $S^3$/Brieskorn tests (§5); the forward program and the entanglement-equilibrium mechanism (§6); and the Glossary (§8). Full per-phase records and sources: companion files `phase1`–`phase25` and `research-map-MASTER.md`.

*Status: a constructive synthesis with proved, established, and conjectural layers (tagged throughout). One positive achievable new result (the $H^2$ monopole-Floer↔DHR label correspondence); no distinctive parameter-free experimental prediction; one live falsifiable handle (rigid $w=-1$), currently in mild tension with DESI.*
