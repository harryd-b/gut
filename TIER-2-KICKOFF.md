# Tier 2 kickoff — the critical path (mechanism → prediction)

*Self-contained brief for a fresh session. Paste this in first; keep the reference files (below) in the folder. The goal of Tier 2 is the one thing that decides the framework's fate: **can it produce a distinctive, measurable prediction?** We attack it in-room (no collaborators yet): set the mathematics up rigorously, push the calculation as far as it goes, reach the **go/no-go**, and pinpoint the exact kernel that needs an expert.*

---

## 0. How to use this

1. Start a fresh session in this folder. Load this brief.
2. Skim the **reference files** (§6) — especially `phase26` (gravitize-the-quantum) and `phase25` (the two hard targets T1/T2). You do **not** need all 26 phases; this brief carries the needed context.
3. Adopt the **honesty rules** (§1) verbatim — they are the whole point of this program.
4. Start with **§4 (Problem 2B, the fast go/no-go)** — recommended first move.

---

## 0.5 IMPORTANT — check existing work first

This folder already contains later work from prior sessions — **`phase27`–`phase37`** and **`REVIEW-phys-docs-*.md`**. Several look directly relevant to Tier 2 (e.g. `phase27-predictions`, `phase31-benchmark-scorecard`, `phase32-born-rule-assembly`, `phase33-unruh-check`, `phase36-T1-selection`, `phase35-donoghue-check`). **Before starting fresh, read these** — the $I_3$/Born-rule and T1 work below may already be partly done. Build on them; do not duplicate. If they already answer the go/no-go, jump straight to the decision point.

## 1. Honesty rules (non-negotiable — carry these over)

- **Tag every claim** [proved] / [established (others')] / [conjecture] / [interpretation] / [fitted].
- **Never present a fitted relation or an assumed ansatz as a prediction.** If a result rests on an ansatz (e.g. "the coupling = the stiffness"), say so, in bold, every time.
- **Report negatives.** A null result / Planck-suppressed answer is a *result* and must be stated plainly, not buried.
- **Honor the kill tests (§5).** The plan is designed so we learn cheaply when to stop.
- **Don't fabricate numbers, assignments, or derivations.** Compute or cite; otherwise say "unknown / needs expert."

## 2. Minimal context (the framework in one screen)

The thesis ("geometry-first"): physics is the geometry of a fundamentally **3-dimensional** space $\Sigma$ (a 3-manifold), with **time emergent** as the modular (Tomita–Takesaki / thermal-time) flow. The central conjecture (**Plank IV**): the *protecting structure* that lets geometry fix physics is the **"stiffness" of spacetime** — the **Godbillon–Vey (GV) invariant** of a codim-1 foliation (the exotic-$\mathbb R^4$ ↔ foliation-of-$S^3$ correspondence). GV$\neq0$ ⟹ a **type III$_1$ von Neumann factor** ⟹ a canonical modular flow (Connes: the *flow of weights* is fixed by GV) = the **clock**.

The critical path: **(2A) mechanism** — force the modular/GV flow to be the physical dynamics; **(2B) prediction** — derive the size of the resulting observable deviation. If 2B yields a measurable number, the framework becomes physics.

## 3. Problem 2A — force thermal time from the stiffness (the mechanism)

**Precise target.** Prove that the canonical GV/modular (Tomita–Takesaki) flow of the foliation III$_1$ factor **is** the physical time evolution — not by stipulation (the Connes–Rovelli *thermal-time hypothesis*, currently unproven) but forced by a **stiffness-equilibrium (KMS) variational principle**.

**Ingredients in hand:**
- Connes: the flow of weights $\mathrm{mod}(M)$ of the foliation factor is **determined by GV** — so the modular flow is *geometrically canonical*, not state-arbitrary (this removes the usual "which flow?" objection).
- Entanglement-equilibrium / first law (Jacobson; Faulkner–Guica–Hartman–Myers–Van Raamsdonk; Casini): $\delta S = \delta\langle H_{\text{mod}}\rangle$ **yields the (linearized, then nonlinear) Einstein equations.** *[established — theirs, not ours]*.

**In-room sub-target (the doable part):** formulate the variational principle "**extremize GV (geometric tension) subject to a KMS/equilibrium condition**," and show its stationarity is the entanglement-first-law with $H_{\text{mod}}$ = the **GV-modular generator** — i.e. "minimizing geometric tension = the equilibrium condition ⟹ Einstein dynamics." Write it down explicitly; identify precisely which step needs constructive-QFT rigor (that step = the expert kernel).
**Kill test:** if no such variational principle can be written that forces modular = physical, Plank IV stays interpretation.

## 4. Problem 2B — derive $\kappa$ from the stiffness (the prediction) — **START HERE**

This is the fastest route to a **go/no-go**, and its leading-order structure is computable in-room.

**The physics (from `phase26` / "Gravitizing the Quantum," Berglund–Hübsch–Mattingly–Minic, arXiv:2203.17137).** Topology change makes the Hamiltonian *state-dependent*, $H_\psi = H + g\,\psi$ (nonlinear evolution). Nonlinearity relaxes the Born rule and produces **Sorkin's higher-order (triple-path) interference** $I_3\neq0$ (standard QM forces $I_3=0$). The observable is
$$\kappa=\frac{I_3(A,B,C)}{|I_2(A,B)|+|I_2(B,C)|+|I_2(C,A)|},\qquad I_3 = P_3-P_2^{AB}-P_2^{BC}-P_2^{CA}+P_1^A+P_1^B+P_1^C.$$
Current bounds: $\kappa=0.006\pm0.012$ (photons), $0.007\pm0.003$ (NMR); $|\kappa|\lesssim0.01$–$0.02$. Upcoming: JUNO neutrinos, atom interferometry.

**The framework's claim:** the topology-change coupling $g$ is set by the **GV stiffness** — $g=g(\mathrm{GV})$. *(This link is the ansatz to be justified by 2A; **flag it as an ansatz** until then.)*

**In-room steps (do these):**
1. **Perturbative $I_3$.** With $U_\psi=\exp(iH_\psi t)$, $H_\psi=H+g\psi$, compute $I_3$ for a three-path interferometer to leading order in $g$. Expect $I_3=O(g)$ (standard QM's $I_3=0$ is the $g\to0$ limit), so $\kappa \sim g\times(\text{O(1) matrix-element ratio})$. Get the explicit coefficient.
2. **The scale of $g$ — the decisive sub-question.** In gravitize-the-quantum, the state-dependent coupling $G_{QG}$ is "presumably related to $G_N$" (Newton's constant) ⟹ **naively Planck-suppressed**. Estimate: for atomic/optical energies $E$, a Planck-suppressed $g$ gives $\kappa\sim (E/E_{\text{Planck}})^{p}\sim 10^{-22}$ or smaller — **far below** the $0.01$ bound. **So the make-or-break question is: does the GV/exotic-smoothness stiffness *evade* Planck suppression?** (e.g. a large GV, an IR-not-UV scale, a non-perturbative enhancement.)
3. **Assess the enhancement.** Determine whether $g(\mathrm{GV})$ can be $O(10^{-2})$ (measurable) rather than $O(10^{-22})$ (dead). This is the fastest go/no-go and is assessable early — before the full 2A mechanism.

**Kill test (the big one):** if $\kappa$ is Planck-suppressed with no GV enhancement, the framework has **no measurable distinctive prediction** — it is an interpretation, not physics. If GV can lift $\kappa$ into the $10^{-2}$–$10^{-3}$ window, it is testable physics; then compute the specific number and confront the bounds.

## 5. Kill tests (decide to stop here if…)

| If… | then |
|---|---|
| 2B: $\kappa$ is Planck-suppressed, no GV enhancement | **no measurable prediction — framework is an interpretation; stop the physics claim** |
| 2A: no variational principle forces modular = physical | mechanism fails; Plank IV stays interpretation |
| 2B: $\kappa$ enhanced into $10^{-2}$–$10^{-3}$ | **testable physics** — compute the number, confront JUNO/atom-interferometry/atomic-clock bounds, and *then* it's worth collaborators |

## 6. Reference files (keep in the folder)

- `CORE-geometry-first-FINAL.md` / `.pdf` — the full framework (Planks I–IV; §4–5 emergent time/stiffness; §8B experimental audits). **Authoritative version** (older `CORE-...-stratum` files were unstable).
- `RESEARCH-PLAN.md` — the full plan; Tier 2 is §"Tier 2".
- `phase26-3D-emergent-time-gravitizing-quantum.md` — the gravitize-the-quantum synthesis (the basis of 2B).
- `phase25-tackling-the-hard-targets.md` — T1 (thermal time; the canonical-GV advance) and T2 (the $\kappa$ test framing).
- `phase24-AMK-audit.md` — the exotic/AMK chain, modular-flow = thermal-time engine.
- Papers: `2203.17137v1.pdf` (Gravitizing the Quantum — for 2B), `2602.08341v1.pdf` (combinatorial spacetime / LQG context).
- `research-map-MASTER.md` — the phase-by-phase index if deeper context is needed.

## 7. Recommended first action (new session)

**Do §4 step 1–3 (Problem 2B).** Compute the leading-order $I_3(g)$, then *immediately* assess the Planck-suppression question (step 2–3) — that is the single fastest way to learn whether the framework can make a measurable prediction at all. Treat $g=g(\mathrm{GV})$ as a flagged ansatz. Report the go/no-go plainly. Only if it survives do 2A (justify the ansatz / the mechanism) and then the precise number.

*One honest note to carry in: the most likely outcome of 2B is Planck suppression (a null). That is a real, valuable result — it would tell us the framework's distinctive prediction is undetectable, which is decisive. Do not tune to avoid it.*
