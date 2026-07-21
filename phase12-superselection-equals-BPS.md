# Phase 12 — Is superselection content = BPS content? (the crux, with the skeptic in charge)

**Where we are.** Phase 11 derived the internal monopole-Floer ↔ sector correspondence *on the BPS/protected sector* and reduced the residual gap to one crux: **is the superselection-relevant content of the SW QFT equal to its BPS content?** A "yes" would turn the internal correspondence into a theorem (modulo constructive rigor). This document tests that claim adversarially — and the adversarial stance pays off, because the naive claim is false twice over for instructive reasons, and the *corrected* claim is both defensible and sharper.

**Verdict (one line).** "Superselection = BPS" is **false as literally stated** — twice: a sector's full Hilbert space strictly contains its BPS subspace, *and* the raw BPS spectrum **wall-crosses** (jumps across marginal-stability walls) while superselection sectors are robust. But the **corrected** statement holds and is clean: **superselection structure = the wall-crossing-*invariant* (protected) BPS data**, of which $HM(\Sigma)$ — a genuine topological invariant — is exactly the *magnetic chart*. So the crux is **reduced and clarified, not closed**: the magnetic-sector correspondence is now consistent and theorem-shaped, and the precise remaining gap is **completeness** — assembling the magnetic ($HM$), electric (dual), and dyonic protected data into the full DR sector category.

---

## 0. The skeptic's stance

The temptation is to declare "superselection = BPS" and close the program. The discipline is to try to break it. Two attacks succeed, and surviving them produces the right claim.

---

## 1. Attack 1 — "content" means full Hilbert space (and BPS isn't that)

A superselection sector's Hilbert space is the *entire* representation of the observable algebra carrying that charge: ground states **and** all excited/scattering states — infinitely many, fully dynamical. The BPS content is only the protected ground states. So:
$$\mathcal H^{\text{BPS}}_{\text{sector}} \ \subsetneq\ \mathcal H^{\text{full}}_{\text{sector}}.$$
If "superselection content" meant the full Hilbert space, the claim is **immediately false**.

**Repair.** The superselection *structure* — the object DR reconstruction actually uses — is **not** the internal Hilbert space of each sector. It is the *category*: the set of sectors (charge labels), their composition/fusion, and their statistics. The dynamics *within* a sector (its excited states) is not part of the superselection structure. So the right claim is:
$$\textbf{superselection \emph{structure} (labels + fusion + statistics)}\ \overset{?}{=}\ \textbf{(protected) BPS data},$$
not "= full content." With this repair the claim is at least *type-correct*. Now attack the repaired version.

---

## 2. The magnetic half is supportable

For the magnetic/flux sectors the repaired claim holds, and cleanly:

- **Every sector has a BPS representative.** Magnetic sectors are labeled by $\mathfrak{s}\in\mathrm{Spin}^c(\Sigma)\cong H^2(\Sigma;\mathbb{Z})$ (Phase 8). Each contains the **reducible** solution (pure flux, zero spinor) — a BPS configuration. So no magnetic sector is BPS-empty: the protected data populates *every* magnetic label. ✓
- **Fusion matches.** Composition of flux sectors is addition of $c_1$ in $H^2(\Sigma;\mathbb{Z})$; the $\mathrm{Spin}^c$-grading of $HM$ carries exactly this abelian fusion. ✓
- **Statistics match.** In $3+1$D the DHR category is *symmetric* (permutation, $\pm1$), Result C; the homological/fermion-number $\mathbb{Z}/2$ grading of $HM$ supplies the bose/fermi alternative. ✓

So $HM(\Sigma)$, with its $\mathrm{Spin}^c$-grading (fusion) and homological grading (statistics), provides exactly the **symmetric-tensor-category input that DR reconstruction needs** — for the magnetic sectors. The repaired claim is true on the magnetic axis. This is real, and it's the half that connects directly to the Phase-4 DR bridge.

---

## 3. Attack 2 — wall-crossing (the one a naive claim misses)

Here is the obstruction that a careless "superselection = BPS" would walk straight into. **The BPS spectrum is not invariant.** As one moves in the moduli/parameter space of an $\mathcal{N}=2$ theory, BPS states appear and disappear across **marginal-stability walls** (the Seiberg–Witten $SU(2)$ spectrum: an infinite dyon tower at weak coupling collapses to just a monopole and one dyon at strong coupling). Bound states grow to infinite size at a wall and decay across it; the spectrum *jumps*. This is the Kontsevich–Soibelman / Gaiotto–Moore–Neitzke wall-crossing story.

But **superselection sectors are robust** — they are global charges, invariant under continuous changes of parameters. A robust thing cannot equal a jumping thing. So:
$$\textbf{superselection structure}\ \neq\ \textbf{raw BPS spectrum}.$$
The naive claim is false *again*, now for a physics reason, not a type error.

**Repair (and it's the right one).** Distinguish two pieces of BPS data:
- the **charge lattice** $(n_e,n_m)\in\mathbb{Z}^2$ (electric × magnetic) — the *a priori possible* charges. This is **robust**; it is just the lattice generated by the central charges, rotated by $SL(2,\mathbb{Z})$ duality but never gaining/losing points.
- the **occupation** — which lattice points actually carry a BPS state at a given modulus. This **wall-crosses**.

Superselection sectors = which charges *can exist* = the **charge lattice** (robust). They are matched not by the raw (occupation) spectrum but by the **wall-crossing-invariant data**: the lattice itself, plus *protected indices* (the Witten-index / homology-type counts that are designed to be invariant). And **$HM(\Sigma)$ is precisely such a protected, wall-crossing-invariant object** — it is a topological invariant of the smooth 3-manifold $\Sigma$, independent of metric and perturbation. So:
$$\boxed{\ \textbf{superselection structure}\ =\ \textbf{wall-crossing-invariant (protected) BPS data;}\quad HM(\Sigma)=\text{its magnetic chart.}\ }$$

This survives Attack 2 by construction: both sides are invariant. The wall-crossing *occupation* numbers, which jump, are **not** superselection data — they are dynamics within the parameter space, exactly the non-robust information superselection theory ignores. The skeptic's attack thus *sharpens* the claim into its correct, invariant form.

---

## 4. The remaining gap: completeness across the charge lattice

What is *not* yet established is **completeness**: does the protected/invariant BPS data reproduce the **full** DR sector category, or only the magnetic axis that $HM$ sees?

- $HM(\Sigma)$ captures the **magnetic** ($n_m$, via $\mathrm{Spin}^c=H^2$) protected data.
- The **electric** sectors are the Pontryagin/$SL(2,\mathbb{Z})$-dual; the **dyonic** sectors are the off-axis lattice points. The full BPS framework of $\mathcal{N}=2$ *is* dyonic (central charge $Z=a\,n_e+a_D\,n_m$), so the protected data of the full theory does range over the whole $(n_e,n_m)$ lattice — encouraging — but **$HM(\Sigma)$ is only the magnetic chart of it.**

So the precise open problem is: **assemble the magnetic ($HM$), electric (dual), and dyonic protected invariants into one symmetric tensor category, and show it equals the DR superselection category of the SW QFT.** $SL(2,\mathbb{Z})$ duality strongly suggests the electric and dyonic charts are determined by the magnetic one, but turning "suggests" into "equals the DR category" is unproven. This is the residual of the residual gap — much smaller than where Phase 11 left it (now: "complete the lattice," not "is BPS even the right object").

---

## 5. Verdict

The crux is **reduced and clarified, not closed**. Concretely:

- **Killed two overclaims.** "Superselection = BPS" is false as full-content (Attack 1) and false as raw-spectrum (Attack 2, wall-crossing).
- **Established the correct claim and proved its magnetic half.** Superselection structure = wall-crossing-invariant protected BPS data; on the magnetic axis $HM(\Sigma)$ supplies exactly the DR categorical input (every sector populated by the reducible; fusion = $H^2$ addition; statistics = $3+1$D symmetric).
- **Reduced the open question to completeness:** does magnetic ($HM$) + electric (dual) + dyonic protected data = the full DR category? $SL(2,\mathbb{Z})$ duality makes it plausible; it is unproven.

For the program: the internal correspondence (Plank II ∩ Plank III) is now **a theorem on the magnetic sector** (modulo the Phase-11 OS-rigor item), with completeness across the charge lattice as the one remaining mathematical task. That is the most precisely-located the program has ever been.

---

## 6. The meta-pattern, at its sharpest

Every phase has driven the bet toward the **protected/topological stratum** — no S-matrix (Phase 3), no global hyperbolicity (Phase 7), the protected sector (Phase 11). Wall-crossing is the sharpest form yet: the correspondence holds *exactly* for the wall-crossing-invariant data and *demonstrably fails* for the non-invariant (occupation) data. So the bet is not vaguely "topological-ish"; it is, precisely, **a claim about the wall-crossing-invariant / protected stratum of physics, and nothing else.** That is a falsifiable delimitation, and it is the program's central structural discovery: *the geometry-first correspondence is exactly coextensive with the protected sector — it holds there and provably not beyond.*

This cuts both ways, honestly. It means the correspondence is real and theorem-shaped where it lives. It also means the correspondence, by its nature, **cannot reach the non-protected, fully-dynamical physics** (generic excited states, the running of couplings, scattering) — so "everything is geometry" must be read as "everything *protected* is geometry." Whether the protected stratum is "enough" to be the foundation of physics, or is only its rigid skeleton, is now the deepest open question of the entire bet — and it is a *philosophical/physical* question the mathematics has handed back, sharply posed.

---

## 7. Next sub-questions

1. **[The completeness theorem]** Assemble magnetic ($HM(\Sigma)$) + electric (Pontryagin dual) + dyonic protected data into one symmetric tensor category and compare to the DR superselection category of the SW QFT. Use $SL(2,\mathbb{Z})$ duality to relate the charts. A match completes the internal correspondence as a theorem. **Highest leverage.**
2. **[OS rigor]** Phase-11 gap (b): reflection positivity for the interacting untwisted theory — carried over.
3. **[The big question, now sharply posed]** Is the protected stratum *foundational* or merely *skeletal*? I.e., can the non-protected dynamics be recovered from / built on the protected data (as e.g. a deformation, or via the protected data fixing the theory), or is it genuinely independent information the geometry-first picture cannot supply? This is where the bet's ultimate fate lives, and Phase 12 has finally posed it as a definite question rather than a slogan.

**Recommended next step:** sub-question 1 — it is the last mathematical task in the chain Phases 8→12 built, and finishing it would give the program its first *complete* theorem-level result (the full magnetic+electric+dyonic internal correspondence), not just a magnetic-axis one.

---

## 8. Methodological note

This phase is the clearest vindication of the adversarial method the program adopted at Phase 0. A non-skeptical pass would have announced "superselection = BPS, gap closed." The skeptical pass found **two** ways the literal claim fails — full-content and, more deeply, **wall-crossing** — and in repairing them arrived at the *correct* and *sharper* statement (invariant data only) plus the program's central structural insight (the correspondence is coextensive with the protected stratum). The result is smaller than "gap closed" and far more trustworthy than it would have been. The grand bet's probability is unchanged; its content is now as precisely delimited as the mathematics allows.

---

## Sources
- Wall-crossing of BPS spectra across marginal-stability walls in $\mathcal N=2$ / Seiberg–Witten (infinite dyon tower at weak coupling → monopole + dyon at strong coupling; bound states decay at walls); protected index invariants survive; Kontsevich–Soibelman / Gaiotto–Moore–Neitzke: [Moore, "PiTP Lectures on BPS States and Wall-Crossing in d=4, N=2"](https://www.physics.rutgers.edu/~gmoore/PiTP-LectureNotes.pdf); [Gaiotto–Moore–Neitzke, "Framed BPS States, Moduli Dynamics, and Wall-Crossing" (arXiv:1102.1729)](https://arxiv.org/abs/1102.1729).
- Dyonic BPS spectrum, charge lattice $(n_e,n_m)$, central charge $Z=a\,n_e+a_D\,n_m$, $SL(2,\mathbb{Z})$ duality rotating the charge lattice: [Bilal, "Duality in N=2 SUSY SU(2) Yang–Mills: pedagogical intro to Seiberg–Witten" (arXiv:hep-th/9601007)](https://arxiv.org/pdf/hep-th/9601007); [Seiberg–Witten BPS spectra review (arXiv:hep-th/0106246)](https://arxiv.org/pdf/hep-th/0106246).
- $HM(\Sigma)$ a topological (metric/perturbation-independent) invariant of $\Sigma$, hence wall-crossing-invariant: Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (CUP 2007); [Lin, "Lectures on monopole Floer homology" (arXiv:1605.03140)](https://arxiv.org/pdf/1605.03140).
- DR reconstruction needs the symmetric tensor category (labels + fusion + statistics): [Doplicher–Roberts, CMP 131 (1990) 51](https://link.springer.com/article/10.1007/BF02097680); Phase-4 document.
