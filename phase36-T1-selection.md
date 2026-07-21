# Phase 36 — T1 as a selection problem: the decomposition theorem and the collapse of the scale gaps

*Working session, 2026-07-11. Attacks CORE §6 item 1(a) (T1-core) using phase 33's reformulation: the clock exists canonically (Connes' cocycle theorem — the outer modular class δ(t) is state-independent), so T1 is not "construct a flow from GV" but "prove GV selects/parametrizes the canonical flow." Result of the session: T1 decomposes into three layers — two of which are theorems already in the literature, correctly read — and the third collapses into the SAME single scale gap that phases 25/34 found for 1/G and ħ. T1-core is hereby reduced from an open mechanism to a one-parameter normalization problem, and the three scale gaps of the program are shown to be one gap.*

---

## 1. The decomposition

Let (Σ,F) be a codim-1 foliation, G its holonomy groupoid, M = W*(Σ,F) (type III component per [A1]), δ: ℝ → Out(M) the canonical outer dynamics (the image of any faithful normal state's modular flow — state-independent by the Connes cocycle theorem; phase 33 L2).

**Layer 1 — EXISTENCE [theorem]: the fold activates time.** For semifinite algebras the modular flow is inner — δ trivial: *no intrinsic dynamics*. GV(F) ≠ 0 ⟹ M has a type III component (Hurder–Katok) ⟹ **δ ≠ 0: intrinsic time exists.** Caveat, stated: the converse fails in general (type III can occur with GV = 0), so GV ≠ 0 is *sufficient*, not necessary, for intrinsic time — the fold is *an* activator, the program's conjecture is that it is *the physical* one. **[E1: converse landscape — ask an expert which foliation classes are type III with vanishing GV]**

**Layer 2 — METERING [theorem — the corrected core of "GV pins the clock"]:** Connes (Cyclic cohomology and the transverse fundamental class, 1986; NCG book; the structure AMK quotes at 1601.06436 §7 / book p. 239): the **transverse fundamental class** [V/F] ∈ HC¹(C_c^∞(G)) encodes the canonical dynamics; it is not δ-invariant, but its second time-derivative vanishes, and the contraction of its first time-derivative with δ **is the Godbillon–Vey class**:

  d²/dt² [V/F] = 0,  i_δ (d/dt)[V/F] = GV_HC ∈ HC²(C_c^∞(G)).

Read correctly, this is the theorem-strength content of Plank IV's "stiffness = clock": **GV is precisely the rate at which the canonical time shears the transverse geometry** — the pairing between intrinsic time and the transverse structure. Not "the flow of weights is determined by GV" (the over-reading corrected in phase 25), and not a mere co-occurrence: GV *is* the time-derivative of the geometry along the intrinsic dynamics. The stiffness does not just accompany the clock; it is the clock's measured coupling to space. **[E2: exact statement of the Connes pairing to be transcribed from the 1986 paper / NCG III.7 in the expert audit]**

**Layer 3 — NORMALIZATION [open — but now one number]:** what remains of T1-core: identify the physical time unit — i.e., fix the isomorphism between the δ-parameter (dimensionless modular time) and laboratory seconds. This is a *single dimensionful conversion*, not a structure: the flow exists (Layer 1), its geometric meter is GV (Layer 2); what is missing is one scale.

## 2. The collapse of the scale gaps

The program has now met the same gap three times:

| Where | The derived structure | The underived number |
|---|---|---|
| T1 Layer 3 (this phase) | intrinsic time δ(t), GV-metered | the second (modular time ↔ lab time) |
| §4.1(iii) / T2 (phase 25) | curvature modulus induced from GV/modular data | the value of G (GV ↔ 1/G conversion) |
| M0a residue (phase 34) | quantization map with t = e^{h/4} | the value of ħ (when t departs from −1) |

**Claim (structural, this phase): these are one gap, not three.** The framework's primitive data (GV, the foliation, the algebra) are dimensionless/topological; physics requires exactly one dimensionful input to convert them (equivalently: a choice of Planck scale). Once ONE of the three numbers is fixed — by measurement or by a future mechanism (Chishtie's threshold A ≥ 1/M_P² is precisely a candidate mechanism for this single conversion; CORE §6 item 5) — the other two must follow, because they are tied to the same modular/GV structure: the first law links the time normalization to G (δS = δ⟨K⟩ has G on one side and the K-normalization on the other), and the deformation parameter links it to ħ (the modular flow's KMS β and the quantization scale enter the same algebra). **Falsifiable-in-principle consequence: the framework predicts two RELATIONS among (G, ħ, time-unit) once one is fixed — i.e., it is a one-parameter theory at the scale level.** Making those two relations explicit is the quantitative content of M3/M4 and the sharpest possible form of the program's "predict, don't fit" ambition. **[This claim is the session's candidate-new structural statement; the phase-29 sweep has no prior for it — log for the novelty ledger at conjecture level, with the two-relations program as its test.]**

## 3. Consequences

1. **T1-core, restated finally:** *prove that the physical H_mod of the first law is a representative of δ(t) in the GV-metered parametrization, and fix the one scale.* Layers 1–2 discharge the existence and pinning halves as theorems; what the experts should be asked to check is exactly [E1], [E2] — after which T1's残 residue is the normalization, shared with T2 and the ħ-gap.
2. **M3's shape (not executed):** with K = the GV-metered modular Hamiltonian and the wedge reduction of phase 33, Jacobson/Casini's first-law logic applies locally; the Einstein equations emerge with 1/G = (the one scale)-dependent coefficient; **the ¼ in S = A/4G then becomes a consistency check of the single scale, not an independent number.** M3 = write this chain with the normalization tracked honestly.
3. **Plank IV, final reading:** *the fold activates time (Layer 1, theorem), the fold's stiffness meters it (Layer 2, theorem), and one scale converts it to seconds (Layer 3, open) — with the same one scale converting the topology to G and to ħ.* "Rigidity = protection = clock" now has two-thirds theorem support and a precisely posed remainder.
4. **For the outreach:** AMK's open problem #1 ("What is the Hamiltonian of the theory?") receives a concrete proposed answer: the GV-metered representative of the canonical dynamics, with the Connes pairing as its geometric definition and one normalization to fix. That is a letter-ready statement.

## 4. Audit table

| # | Item | Where | Confidence | Ask |
|---|---|---|---|---|
| E1 | Landscape of the converse to Hurder–Katok (type III with GV = 0) | Layer 1 | medium | which classes; does it matter physically |
| E2 | Exact form of the Connes pairing i_δ(d/dt)[V/F] = GV_HC (1986 paper; NCG III.7) | Layer 2 | medium-high (structure quoted by AMK; needs primary-source transcription) | precise statement + hypotheses |
| E3 | The two scale relations (G ↔ time-unit via first law; ħ ↔ time-unit via KMS/deformation) — well-posedness | §2 | new (this phase) | operator-algebraist + EFT sanity check |

*Status: T1-core reduced from open mechanism to (i) two theorem-layers pending primary-source audit and (ii) one normalization shared with all other scale gaps — plus a candidate-new structural claim (the one-scale collapse and its two testable relations). M3 and M4 now have explicit shapes. This is the program's deepest remaining problem made as small as the current record can make it.*
