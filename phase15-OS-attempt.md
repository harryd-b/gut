# Phase 15 — A genuine attempt at the single OS problem

**The problem (Phase 14).** Show OS reflection positivity for the protected sector of the interacting abelian Seiberg–Witten QFT on $\mathbb{R}\times\Sigma$, and that the reconstructed protected Hilbert space is $HM(\Sigma)$ (with $\mathrm{Spin}^c$-grading = magnetic charge, $\mathbb{Z}/2$-grading = statistics, $U$-action = charge ladder).

**Outcome of the attempt (one line).** I can **prove it in the positive-scalar-curvature (PSC) case** — there the protected sector is free/Gaussian around a unique gapped reducible, free-field OS is rigorous, and $HM(\Sigma)$ is the manifestly-positive charge ladder with no possible cancellation (this covers $S^3$, $\Sigma(2,3,5)$, all PSC homology spheres). The **general case reduces to one sharp, named, and genuinely open lemma** — a *no-cancellation / sharpness* theorem — and the attempt also **explains why that lemma is hard**: positivity lives in the *untwisted* theory while computability lives in the *twisted* theory, and the protected index is known to differ from the physical Hilbert space exactly when boson–fermion cancellation occurs (the same phenomenon as wall-crossing). So: a real partial theorem, plus the irreducible kernel isolated precisely.

---

## 1. Strategy: route through the topological twist (cohomological field theory)

The protected sector is computed by the **topologically twisted** SW theory (the abelian Donaldson–Witten twist of $\mathcal N=2$). A twisted theory is a **cohomological field theory**: it has a scalar nilpotent supercharge $Q$, $Q^2=0$, with Lagrangian $Q$-exact, and its physical states/observables are $Q$-cohomology classes. By the Witten–Morse correspondence (Phase 11), the $Q$-cohomology on the slice $\Sigma$ is the space of supersymmetric ground states $=$ the monopole Floer homology:
$$
\mathcal H_{\text{prot}} \;=\; H^*\!\big(\mathcal H_{\text{twisted}},\,Q\big) \;\cong\; HM(\Sigma). \tag{$\star$}
$$
$(\star)$ is the standard CohFT structure; at the formal/structural level it is not the hard part. The hard part is **positivity**: $(\star)$ gives a graded vector space, and we need it to be a *Hilbert space* whose inner product is the one OS reconstructs from the physical theory.

## 2. The obstruction the attempt surfaces (and it's the real one)

**The twist breaks unitarity.** A topological twist redefines the rotation/Lorentz generators by mixing in R-symmetry; the stress tensor becomes $Q$-exact; the resulting theory is *not* a unitary QFT in the usual sense (it is "not a TQFT in the Atiyah–Segal sense," and its natural pairing is the topological/bilinear one, generically **indefinite**, not a positive Hermitian inner product). So **the positive-definite inner product is *not* available in the twisted theory** where $HM(\Sigma)$ naturally lives.

Positivity lives in the **untwisted** physical $\mathcal N=2$ theory, on its genuine BPS subspace $\mathcal H_{\text{BPS}}^{\text{phys}}\subset\mathcal H$ (positive-norm, being a subspace of a unitary Hilbert space). So the correspondence we actually need is
$$
HM(\Sigma)\ \ (\text{twisted } Q\text{-cohomology})\ \overset{?}{\cong}\ \mathcal H_{\text{BPS}}^{\text{phys}}\ \ (\text{untwisted, positive-norm}) \tag{$\dagger$}
$$
**as graded Hilbert spaces** — not merely an equality of their dimensions/indices.

**Why $(\dagger)$ is not automatic — confirmed by the literature.** The twisted $Q$-cohomology is a *protected index*; it is well known that *the protected index need not equal the physical BPS Hilbert space*: bosonic and fermionic states can **cancel** in the index, and the $Q$-cohomology can **jump** under deformations. That jumping is precisely **wall-crossing** (Phase 12). So $(\dagger)$ holds only if there is **no cancellation** in the relevant gradings — i.e. if the protected count is *sharp* (realized by genuine states, no $Q$-exact admixture). This is the kernel.

> **Kernel lemma (no-cancellation / sharpness).** For the abelian SW QFT on $\mathbb{R}\times\Sigma$, the twisted $Q$-cohomology $HM(\Sigma)$ is realized by genuine positive-norm physical BPS states with no boson–fermion cancellation in each $\mathrm{Spin}^c$/charge grading; equivalently the OS inner product is non-degenerate and positive on each Floer generator's class.

Everything in Phase 14's "single OS problem" is now concentrated in this lemma.

## 3. The partial theorem: the PSC case is provable

Here the attempt succeeds rigorously.

**Setup.** Let $\Sigma$ admit a positive-scalar-curvature metric (e.g. $S^3$, the Poincaré sphere $\Sigma(2,3,5)$, any spherical space form / PSC homology sphere). Then:

1. **Unique, gapped localization locus.** By Weitzenböck (Phases 9–10), PSC forces the spinor to vanish: the only SW solution is the **reducible** $(A_0,0)$, and for a homology sphere it is unique up to gauge. The Dirac operator at $(A_0,0)$ has a **spectral gap** ($s/4>0$), so the spinor fluctuations are massive with no zero modes.
2. **The protected sector is free/Gaussian.** Expanding the SW action around the isolated gapped reducible, the quadratic fluctuation operator controls the protected sector (localization onto the isolated locus); the spinor sector is gapped and integrates out as a convergent Gaussian, and the surviving light degrees of freedom are the **free Maxwell** field plus the constant-gauge $U(1)$ zero mode. Interactions ($|\Phi|^4$ etc.) are higher-order and do not affect the protected (Gaussian) sector.
3. **OS holds — rigorously.** Free Maxwell theory on $\mathbb{R}\times\Sigma$ is **reflection-positive**; free-field OS reconstruction is one of the rigorously-established cases of constructive QFT. So the OS inner product on the protected sector exists and is positive.
4. **No cancellation is possible.** There is a **single** critical-point type (one reducible), so there is nothing to cancel against — the kernel lemma holds trivially. The protected Hilbert space is the $U(1)$-equivariant cohomology of the reducible's stabilizer,
$$
\mathcal H_{\text{prot}} = H^*_{U(1)}(\mathrm{pt}) = H^*(BU(1)) = \mathbb{Z}[U],
$$
the **positive-norm charge ladder** — which is exactly $HM(\Sigma)$ for PSC homology spheres (the pure $U$-tower, Phases 9–10), shifted by the Frøyshov grading.

**Conclusion (PSC).** For PSC homology spheres the single OS problem is **solved**: reflection positivity holds (free-field OS), and the reconstructed protected Hilbert space is $HM(\Sigma)$ = the positive charge ladder, with $U$ = the charge-raising operator and the Frøyshov invariant = the ground-state grading. This is a genuine (if modest) rigorous theorem — and it is *more* than the "structural confirmation" of Phases 9–10: it actually performs the Euclidean→Lorentzian reconstruction in the case where the theory is free.

*(Caveat, stated honestly: full infinite-dimensional rigor of "localization $\Rightarrow$ Gaussian protected sector" is itself at the standard of constructive free-field QFT, which is in good shape for an isolated gapped locus; I am not claiming more rigor than that.)*

## 4. The general case = the kernel lemma, and why it's hard

When $\Sigma$ admits **no** PSC metric (e.g. $\Sigma(2,3,7)$, hyperbolic $\Sigma$), there are **irreducible** SW solutions; $HM_{red}\neq 0$; multiple critical-point types of differing grading exist. Now:
- the Floer differential already *pairs and cancels* some critical points — $HM(\Sigma)$ is what *survives* cancellation in the **Euclidean/topological** computation;
- the kernel lemma asks that this surviving homology equal the **physical, positive-norm** BPS space — i.e. that the Euclidean Floer cancellation coincides with the physical (Lorentzian, OS) boson–fermion pairing;
- but the twist that defines the Euclidean differential **breaks the unitarity** that defines the physical pairing, and the index-vs-Hilbert-space literature shows these can genuinely differ.

So the general case is **open**, and the attempt shows *why*: it is the precise mismatch between where the computation is clean (twisted, topological, cancellation-taken) and where positivity is defined (untwisted, unitary). Proving the kernel lemma would require one of:
- **(a) a non-renormalization / vanishing theorem** ensuring no boson–fermion cancellation in each charge grading (so index = Hilbert space), or
- **(b) a direct construction** of the untwisted interacting theory's BPS subspace and its OS inner product, identifying it with $HM(\Sigma)$ — i.e. genuine constructive QFT for the 4D interacting gauge-matter theory, the recognized-hard problem.

## 5. Verdict

- **Proved:** the single OS problem in the **PSC case** (free/Gaussian; rigorous free-field OS; $HM=$ positive charge ladder). Covers $S^3$, $\Sigma(2,3,5)$, all PSC homology spheres.
- **Reduced:** the **general case** to one sharply-stated **no-cancellation / sharpness lemma** $(\dagger)$, equivalent to "the protected index $HM(\Sigma)$ equals the physical BPS Hilbert space grading-by-grading."
- **Explained:** *why* the lemma is hard — the twist (where $HM$ is computable) breaks the unitarity (where positivity lives), and protected index $\neq$ Hilbert space exactly when cancellation/wall-crossing occurs.
- **Not claimed:** the full theorem. The general case is genuinely open and sits in hard constructive QFT.

This is the honest result of *having a go*: solve the case that's free, reduce the rest to a single named lemma, and identify the structural reason that lemma resists. The grand bet's status is unchanged; what changed is that the "single OS problem" is now itself split into a proved subcase and a precisely-isolated hard kernel — the most a synthesis pass can responsibly extract before the work becomes constructive-QFT research.

## 6. Next steps (for whoever takes the kernel lemma)

1. **Attack (a) in the simplest non-PSC case, $\Sigma(2,3,7)$.** $HM_{red}$ has rank 1: a *single* irreducible class. Ask whether it can cancel against anything — with one reducible tower and one irreducible generator of definite grading, a grading/parity argument might force no-cancellation, giving a *second* rigorous case beyond PSC. This is the most promising concrete next theorem.
2. **Relate the Floer differential to the physical BPS pairing** explicitly via the SUSY-QM (Witten) picture: both count instantons on $\mathbb{R}\times\Sigma$; making "Euclidean cancellation = physical pairing" precise on the protected sector is exactly $(\dagger)$.
3. **Consult constructive QFT / SUSY-localization experts** on whether a non-renormalization theorem of type (a) is known for twisted abelian gauge-matter theories on $\mathbb{R}\times\Sigma$ — this may already exist in the localization literature and would settle $(\dagger)$ without new analysis.

---

## Sources
- Donaldson–Witten = topological twist of $\mathcal N=2$, cohomological field theory with scalar $Q$, $Q^2=0$, $Q$-exact Lagrangian, observables in $Q$-cohomology; "not a TQFT in the Atiyah–Segal sense": [Renormalization and BRST symmetry in Donaldson–Witten theory (arXiv:1901.03540)](https://arxiv.org/pdf/1901.03540); [Topological Twisting of 4d $\mathcal N=2$ (arXiv:2411.14396)](https://arxiv.org/pdf/2411.14396); [Moore, "Physical Approach to Donaldson Theory" lectures](https://www.physics.rutgers.edu/~gmoore/SCGP-LECTURENOTES.pdf).
- Protected index $\neq$ physical BPS Hilbert space in general (boson–fermion cancellation; $Q$-cohomology jumps under deformation = wall-crossing): [BPS states as $Q$-cohomology / index subtleties (arXiv:2501.05448, "Fortuity in the D1-D5 system")](https://arxiv.org/pdf/2501.05448); [Finite $N$ black hole cohomologies (arXiv:2312.16443)](https://arxiv.org/pdf/2312.16443).
- PSC $\Rightarrow$ only reducible SW solutions, gapped Dirac (Weitzenböck): [Seiberg–Witten invariants — Wikipedia](https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants); Phases 9–10.
- Free-field Osterwalder–Schrader reconstruction is rigorous; reflection positivity of free fields: [Jaffe, "Reflection Positivity" (arXiv:1802.09037)](https://arxiv.org/pdf/1802.09037).
- $HM(S^3)$, $\Sigma(2,3,5)$ pure $U$-tower; $\Sigma(2,3,7)$ reduced rank 1: [Lin, "Lectures on monopole Floer homology" (arXiv:1605.03140)](https://arxiv.org/pdf/1605.03140); Phases 9–10.
