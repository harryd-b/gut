# Phase 33 — M1 executed: the Unruh check (the GV-pinned clock on wedge algebras)

*Working session, 2026-07-11. Executes scorecard milestone M1: show that the framework's clock — the modular flow associated with the GV/foliation structure (Plank IV) — restricts, on wedge subalgebras of the physical net, to the Bisognano–Wichmann boost flow, hence the Unruh temperature T = a/2π. Same discipline as phase 32: theorem assembly, hypotheses audited, in-house content identified precisely, expert-audit table attached. The promised failure mode is resolved in the framework's favor, and the resolution itself is the session's main structural insight.*

---

## 0. The shape of the problem

Plank IV asserts one clock: the modular flow pinned (conjecturally, via T1-core) by the GV class of the foliation. Physics asserts another: for a uniformly accelerated observer, the wedge algebra's modular flow in the vacuum is the boost (Bisognano–Wichmann), giving T = a/2π. If these two flows could disagree on a wedge, Plank IV would be experimentally dead on arrival (Unruh physics is woven into QFT consistency). M1 asks: do they agree, and *why*?

## 1. Lemma L1 (locality of the fold) — the structural insight

**The Godbillon–Vey class is a secondary, global invariant: every codimension-1 foliation is locally a product, and GV has no local density with local physical meaning — it obstructs and classifies only globally.** Consequently the folded geometry's algebra, restricted to any sufficiently small region, is indistinguishable from the unfolded one: local subalgebras, local states (by local normality/local quasi-equivalence of physically admissible states), and hence local modular data are the *standard* ones. **[geometry: standard foliation theory; AQFT input: local normality — audit B1]**

Physics reading, worth stating loudly: **the fold is locally invisible.** Plank IV's stiffness cannot and does not modify any local experiment — no local Unruh anomaly, no local Lorentz violation, no local Born-rule deviation (phase 32) — because the geometric datum carrying the framework's content has no local expression. The framework's physics lives entirely in *global* structure (state selection, sector structure, type classification, cosmology). This is simultaneously: (i) why the framework survives every precision test for free; (ii) why its predictions (phase 27/30) are global/cosmological or statistical-structural; (iii) the precise reason the P2/P3 zero-anomaly commitments are not accidents but theorems-in-waiting.

## 2. Lemma L2 (class invariance of the clock)

For the type III₁ factor (subtype per audit [A1] of phase 32): by the **Connes cocycle (Radon–Nikodym) theorem**, the modular flows of *all* faithful normal states differ only by inner cocycles — they define a **single canonical outer flow** δ(t) ∈ Out(M), state-independent. "The clock," as an outer dynamical class, is therefore unique: whatever pins it globally (GV, on Plank IV's conjecture) and whatever computes it locally (a vacuum on a wedge) must be representatives of the same class. **[theorem — Connes; this is also the corrected reading of AMK's flow-of-weights argument per the phase-25 correction]**

## 3. The assembled theorem (M1)

> **Let A(W) be a wedge subalgebra of the physical net in a locally Minkowskian region of ℝ×Σ, with the state locally in the vacuum folium (L1). Grant the V.7 identification at the level "the net's local algebras are subalgebras of the geometric algebra." Then the restriction of the framework's clock to (A(W), vacuum) is the Bisognano–Wichmann boost flow: Δ^{it}_W = U(Λ_W(−2πt)); equivalently, the vacuum is KMS at β = 2π in boost rapidity, and a uniformly accelerated observer measures T = a/2π exactly. The same assembly, run on a bifurcate Killing horizon with the Hartle–Hawking state (Kay–Wald uniqueness; Sewell), yields the Hawking temperature T_H = κ/2π.**

*Proof structure:* L1 reduces the local situation to standard AQFT; the **Bisognano–Wichmann theorem** (Wightman setting; model-independent AQFT versions via Borchers' theorem and Mund's results for massive theories; modular covariance as the general hypothesis — audit B2) identifies the wedge modular flow with the boost; L2 guarantees the globally-pinned clock cannot be a *different* clock on the wedge — it is a representative of the same outer class, and on (A(W), Ω) the representative is fixed to be BW by the state. ∎ *(conditional on V.7; audits B1–B3)*

**What is in-house here:** not BW (imported theorem), but the two lemmas and their join — the demonstration that Plank IV's global clock is *forced* to look like boost time locally, with the "why" (secondary-invariant locality + cocycle uniqueness) supplied by the framework's own structure. The failure mode promised in phase 31 is resolved: the GV flow *cannot fail* to reduce to BW, precisely because GV has no local density to disagree with.

## 4. Consequences

1. **Scorecard II.3: IMPORTED → DERIVED (assembly; conditional on V.7; audits pending).** The gravity track's first derived benchmark. II.4 gains its temperature half (κ/2π via Kay–Wald); the flux/entropy half remains M3.
2. **Ledger addition (P2-family):** *zero Unruh/Hawking-temperature anomaly* — any confirmed deviation from T = a/2π (analogue-gravity precision tests, circular-Unruh proposals) or from T_H = κ/2π falsifies the framework's clock. Same epistemic class as the GW nulls: shared with standard theory, but a *commitment*, and now theorem-backed inside the framework.
3. **A sharpened self-description:** the framework is *locally exactly standard physics* (theorem, not choice — L1) *plus global geometric structure* (sectors, type III statisticality, cosmological rigidities). All its distinctive physics is global; all its local physics is inherited exactly. Frameworks in this class cannot be killed by local precision tests — only by the global handles (P1, P4a) and the desk tests (P6).
4. **For T1-core:** L2 clarifies what T1 must actually do — not *produce* a flow (the outer class exists canonically) but prove that **GV data selects/parametrizes the class** across the global algebra, i.e., pin the *global* representative the way the vacuum pins the wedge representative. T1 is thus a well-posed selection problem, not a construction problem — a genuine simplification of §6.1(a).

## 5. Scope and caveats

- **V.7 rides along**, as everywhere: the net-in-geometric-algebra identification is assumed at subalgebra level. M1 does not tighten it, but note the direction used here is the *weak* one (net ⊆ geometric algebra locally), plausibly the easier half.
- **BW hypotheses:** Wightman fields or modular covariance / Borchers–Mund conditions; for curved ℝ×Σ the statement is local (locally Minkowskian wedges; for the horizon case, Kay–Wald's uniqueness theorem for the bifurcate-Killing-horizon KMS state). No claim is made for wedges "of the size of the topology."
- **What M1 does *not* derive:** the Hawking *flux* (radiation as a process), back-reaction, or the entropy coefficient — those are M3. The temperature identities are the full content here.

## 6. Expert-audit table (AQFT specialist; short)

| # | Fact used | Where | Confidence | Ask |
|---|---|---|---|---|
| B1 | Local normality/quasi-equivalence of physical states on the local algebras of the foliation-net | L1 | high (standard for reasonable nets) | confirm formulation on ℝ×Σ |
| B2 | Model-independent BW: modular covariance from Borchers/Mund-type hypotheses | §3 | high | best current citation set |
| B3 | Connes cocycle theorem ⇒ state-independent outer class δ(t) on a type III₁ factor | L2 | high | textbook citation (Takesaki II) |
| B4 | Kay–Wald uniqueness + Sewell for T_H = κ/2π on bifurcate Killing horizons | §3 | high | confirm scope statement |

*Status line: M1 executed as a conditional theorem assembly. Two class-II items now carry in-house derivations (II.3 fully; II.4's temperature half); the milestone's promised failure mode is closed in the framework's favor, with the structural byproduct — "the fold is locally invisible" — promoted to a named principle (L1) that explains the framework's entire null-prediction family and re-poses T1 as a selection problem.*
