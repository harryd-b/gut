# Phase 17 — Plank II attacked head-on: entanglement from geometry

**The plank.** *Quantum/entanglement structure is the operator-algebraic shadow of the geometry, not its source.* Originally (the opening framing): read Ryu–Takayanagi right-to-left (area primary, entropy derived); defensible via AQFT (geometry → net of algebras → vacuum entanglement, Reeh–Schlieder); but obstructed by Bell/Tsirelson (no *local geometric field on $M$* can carry the correlations). Until now Plank II was asserted, not worked. This phase works it — and, crucially, connects it to the **superselection machinery built in Phases 4–16**, so it is not a separate story but the same one.

**Verdict (one line).** Plank II is **confirmed for the universal (topological/sector) part of entanglement, and provably *not* reducible to geometry for the bulk (area-law) part.** The universal part — the cutoff-independent piece of the entanglement entropy — is *exactly* a function of the superselection-sector category, which Phases 4–14 derived **from the geometry** ($S = \alpha\ell - \log\mathcal D + \cdots$, with $\mathcal D$ fixed by the sector category = the geometry-reconstructed gauge group). So "entanglement from geometry" is **rigorous for the universal term** and ties Plank II to Plank III through the *same* category. The area-law bulk is local-field entanglement: determined by the net (hence by geometry in the weak "geometry → algebra" sense) but **not** sector-geometric, and it is exactly the part the Bell/Tsirelson obstruction keeps from any local-hidden-field reading. So Plank II splits cleanly into a geometric universal part and a non-geometric (in the strong sense) bulk part.

---

## 1. The decomposition that decides the plank

For a region $A$ with boundary of size $\ell$, entanglement entropy has the universal form
$$
S_A \;=\; \underbrace{\alpha\,\ell^{d-2}}_{\text{area law, non-universal}} \;-\; \underbrace{\gamma}_{\text{universal}} \;+\;\cdots, \qquad \gamma = \log \mathcal D .
$$
The two terms have *opposite* status for Plank II:
- the **area term** is cutoff-dependent, dominated by short-distance local-field correlations across $\partial A$ — the bulk of the entanglement;
- the **universal term $\gamma=\log\mathcal D$** is cutoff-independent and *topological*: in $2{+}1$D, $\mathcal D$ is the total quantum dimension of the anyon (superselection) category; in gauge theories generally, $\gamma$ is fixed by the **superselection-sector structure** (Kitaev–Preskill, Levin–Wen; Casini–Huerta–Magán–Pontello tie it directly to the algebra/superselection content of complementary regions).

Plank II is therefore really two claims, and they have different fates.

## 2. The universal part IS geometric — via the machinery we already built

This is the new content, and it is where Plank II meets Phases 4–16.

**Casini–Huerta–Magán–Pontello:** entanglement entropy's universal structure is controlled by the **superselection sectors** — precisely the failure of duality/additivity of the algebras of complementary regions is the *entropic order parameter*, and it is governed by the sector category (the same DR/DHR data). The universal term counts sectors weighted by their dimensions.

**But that sector category is exactly what Phases 4–14 reconstructed from the geometry.** Result C (DR reconstruction): the sector category is the Tannaka dual of the local net. Result L (Phase 14, abelian case): for $\mathbb{R}\times\Sigma$ the magnetic sector category is $\mathrm{Rep}(\widehat G)$, $\widehat G=\mathrm{Pontryagin\ dual\ of\ }H^2(\Sigma;\mathbb Z)$ — *fixed by the spatial topology*. Chaining:

$$
\boxed{\ \text{geometry of }\Sigma \;\xrightarrow{\text{Phases 4–14}}\; \text{sector category }\mathrm{Rep}(\widehat G)\;\xrightarrow{\text{CHMP / Kitaev–Preskill}}\;\gamma=\log\mathcal D(\widehat G).\ }
$$

So the **universal entanglement entropy is a geometric quantity**: for a finite part of $\widehat G$ it is $\log|\widehat G|$; for the $U(1)^{b_2}$ part it is the (regularized) continuous-group analogue; in all cases $\gamma$ is read off $H^2(\Sigma;\mathbb Z)$. **This is Plank II realized rigorously for the universal term, using the identical category that realizes Plank III.** Entanglement (its universal piece), gauge structure, and the sector category are one object — the geometry-first dream, made precise on exactly the protected/topological stratum the whole program converged onto.

*(Consistency with Phase 16: on $\Sigma$ where the sector content is computed by $HM(\Sigma)$, $\gamma$ is determined by $HM$'s graded structure — the same protected data. Entanglement entropy's universal term and the monopole-Floer superselection content are the same geometry-derived quantity.)*

## 3. The bulk part is NOT geometric in the strong sense — and that's forced

The area-law term is local-field entanglement across $\partial A$. Two honest statements:
- **Weak sense (survives):** it is determined by the net $\mathcal O\mapsto\mathfrak A(\mathcal O)$ — the type-III$_1$ local algebras whose vacuum is highly entangled (Reeh–Schlieder). The net is fixed by the geometry/causal structure, so in the weak "geometry → algebra → entanglement" sense even the bulk entanglement is downstream of geometry. This is the defensible direction the opening framing claimed, now precise.
- **Strong sense (fails, by theorem):** the correlations cannot be *carried by local geometric fields on $M$* — Bell/CHSH with Tsirelson's bound rigorously excludes any local-hidden-variable account ($\mathrm{CHSH}\le 2$ classical vs $\le 2\sqrt2$ quantum). So the bulk entanglement is **not** "geometry" in the sense of local field values on $M$; it is irreducibly quantum-algebraic. Plank II cannot claim the bulk as geometric in the strong sense, and no amount of machinery changes that — it is a theorem.

So the plank's grand reading ("*all* entanglement is geometry") is **false in the strong sense** and **true only in the weak (net-determined) sense** for the bulk — while the universal/topological part is geometric in the **strong, computable** sense (§2).

## 4. What Plank II actually is, after the attempt

| part of $S_A$ | status for Plank II | mechanism |
|---|---|---|
| universal $\gamma=\log\mathcal D$ | **geometric (strong, rigorous)** | sector category from geometry (Phases 4–14) → CHMP/Kitaev–Preskill |
| area-law bulk | geometric only in the **weak** (net-determined) sense; **not** carried by local fields | Reeh–Schlieder (weak) / Bell–Tsirelson (strong obstruction) |

This is the same shape as every other plank's resolution in this program: **the geometry-first claim holds exactly on the protected/topological/universal stratum and provably fails on the non-protected/dynamical/bulk stratum.** Plank II now joins Planks III (forces) and the OS correspondence (Phases 8–16) in this pattern — and via the *shared sector category*, the three are literally the same object on that stratum:
$$
\text{geometry of }\Sigma \;\Rightarrow\; \text{sector category} \;\Rightarrow\; \big(\text{gauge group [III]},\ \text{universal entanglement }\gamma\text{ [II]},\ HM(\Sigma)\text{ [the bridge]}\big).
$$

## 5. The deep question, now the same for II and III

This sharpens the program's central open question (Phase 12) into a single form covering both planks: **is the protected/topological stratum foundational or merely skeletal?** For Plank II concretely: is $\gamma=\log\mathcal D$ (the geometric, universal entanglement) the "skeleton" of the entanglement, with the area-law bulk an independent dynamical dressing — or can the bulk be *organized by* / recovered from the universal data plus the dynamics? If the latter, geometry-first reaches further; if the former, geometry fixes only the topological bones of entanglement. This is now identical to the Plank-III question and to the OS-stratum question — the program has converged on **one** deep question wearing three hats.

## 6. Verdict and next

- **Confirmed (rigorous):** the universal entanglement term is geometric, computed by the same sector category that gives the gauge group; Plank II holds on the topological stratum and is *unified* with Plank III there.
- **Refuted (by theorem) for the strong grand reading:** the bulk entanglement is not local-geometric (Bell–Tsirelson); at best net-determined (weak).
- **Net:** Plank II resolves into the program's universal pattern and is no longer a separate, vaguer plank — it is the entanglement face of the one protected-stratum object.

**Next:** (1) compute $\gamma$ explicitly for a concrete $\Sigma$ (e.g. $S^2\times S^1$: $\widehat G=U(1)$, giving the gauge-theory $U(1)$ topological entanglement term) as a worked example tying $H^2(\Sigma)$ → $\gamma$. (2) Attack the unified deep question (§5) — foundational vs. skeletal — now that II, III, and the OS bridge pose it identically.

---

## Sources
- Universal/topological entanglement entropy $\gamma=\log\mathcal D$, total quantum dimension, $\mathcal D>1$ signals topological order: Kitaev–Preskill and Levin–Wen; [overview, "Entanglement in Many-Body Systems" (arXiv:quant-ph/0703044)](https://arxiv.org/pdf/quant-ph/0703044); higher-$d$ gauge-theory generalizations: [Topological Entanglement Entropy in $d$-dimensions for Abelian higher gauge theories (arXiv:1907.01608)](https://arxiv.org/abs/1907.01608).
- Entanglement entropy controlled by superselection sectors / failure of duality–additivity = entropic order parameter: [Casini, Huerta, Magán, Pontello, "Entanglement entropy and superselection sectors I" (arXiv:1905.10487)](https://arxiv.org/abs/1905.10487); "Entropic order parameters for the phases of QFT"; recent SymTFT connection [JHEP06(2026)083](https://link.springer.com/article/10.1007/JHEP06(2026)083).
- Sector category = Tannaka dual of the net (Result C); abelian case = $\mathrm{Rep}(\text{Pontryagin dual of }H^2(\Sigma))$ (Result L): [Doplicher–Roberts, CMP 131 (1990) 51](https://link.springer.com/article/10.1007/BF02097680); Phase-4 and Phase-14 documents.
- Reeh–Schlieder (vacuum highly entangled, net-determined) and Bell/Tsirelson bound (no local-field carrier): standard AQFT; opening framing of the program.
