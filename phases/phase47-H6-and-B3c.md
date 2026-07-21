# Phase 47 — H6 executed (EQ in operator-algebra language) and B3c sharpened (the level is the stiffness)

*Working session, 2026-07-17. Two items from the CORE v3 forward program. §1 transcribes the equilibrium principle EQ (phase 46) into the von Neumann weight/modular language — the form an operator algebraist can check — and finds that EQ closes the R1 temperature loop exactly. §2 attacks the B3c pivot (finite census = finite level) and finds an exact arithmetic identity: **the quantization level that matches the framework's sector census is precisely the quantized stiffness, ℓ = GV/4π² = 2g−2** — with the honest boundary between the proven count-level match and the open content-level identification drawn sharply.*

---

## 1. H6 — the equilibrium principle in weight/modular language

**Setup.** M = W*(Σ,F) on the carrier; two distinguished transverse measure classes: the geometric (Liouville) class, weight φ_geo, whose Radon–Nikodym cocycle is the unstable-Jacobian (geometric-potential) cocycle δ(γ); and the maximal-entropy (Bowen–Margulis) class, weight φ_BM, whose cocycle is h_top·s(γ) with s the geodesic-time cocycle. By the Connes cocycle theorem the two modular flows always agree in Out(M); EQ demands more — that they agree *as geometric data*.

**H6 statement (measure level — theorem-backed via the verified H4/H5 dictionary):**

> **EQ ⟺ δ and h_top·s are cohomologous (Livšic transfer function u) ⟺ the geometric folium contains a KMS state at inverse temperature β = h_top for the canonical geodesic-time dynamics.**

Via Renault–Neshveyev [verified-source, phase 46 H5]: KMS_β states for the s-dynamics are exactly the quasi-invariant measures with RN cocycle e^{−βs}; the Liouville class has RN cocycle e^{−δ}; cohomology δ = h_top·s + (u∘r − u∘s) means the density-adjusted measure e^u·(Liouville) has RN cocycle exactly e^{−h_top·s} — a KMS_{h_top} state. Every step is a cited theorem; only the *designation* of this as the physical equilibrium is EQ itself.

**H6 statement (operator level — derived-structural; audit item H6b):** the Connes cocycle derivative between the two weights is a **coboundary implemented in the abelian subalgebra**: (Dφ_geo : Dφ_BM)_t = e^{itU} with U = multiplication by the Livšic transfer function u ∈ L∞(Σ) ⊂ M. In words: **EQ holds iff the geometric and equilibrium weights differ by a *potential* — a function on space — rather than by a genuinely noncommutative perturbation.** [The Livšic-to-cocycle-derivative step is structurally forced but must be written with care — Hölder regularity of u, unboundedness, weight domains; this is exactly what H6b asks a specialist to check. The G1 lesson applies: the measure-level form above is the load-bearing one.]

**The temperature loop closes.** On the carrier at constant curvature, h_top = 1 in curvature-radius units. So EQ says: *the geometric state is KMS at β = 1 in the fold's natural units* — the fold sits at its own natural temperature. Converting with 𝒯 = 2πR/c (phase 45) and R1: **k_B T_fold = ħc/2πR** — the Gibbons–Hawking form. **[RE-TAG, 2026-07-18, FR-5: "emerging from the equilibrium principle rather than being imposed" is withdrawn as circular — the 2π enters through the borrowed vacuum-net normalization (see phase 45's re-tag), so the GH *form* is a consistency of conventions, not an emergence. What EQ genuinely supplies is β = 1 in natural units — the coefficient awaits the T-2π transport.]** The phase 44 §1d "Planck-hot" worry resolves into this statement: the fold's intrinsic temperature is the GH temperature of its own curvature scale, a *global* statement about the fundamental state (and by L1 invisible locally) — not a lab thermometer reading. [derived; interpretation layer flagged]

## 2. B3c sharpened — the level is the stiffness

**The pivot (phase 43/45):** the discreteness cascade needs "finite census = finite level" — that the Bradlow-truncated sector count is implemented by a root-of-unity (finite-level) quantization.

**The arithmetic identity (exact, verified for all g ≥ 2).** The framework's sector census on S¹×Σ_g is 2g−1 (sectors |k| ≤ g−1, phase 28/40). The stiffness is quantized: GV/4π² = 2g−2 (phase 44). An SU(2) TQFT at level ℓ has ℓ+1 primaries. Then:

> **ℓ = GV/4π² = 2g−2 ⟹ number of primaries = 2g−1 = the Bradlow census. Exactly, for every genus.**

*The level that reproduces the framework's own sector count is the quantized stiffness itself.* If this identification is right, the chain closes into a single self-referential structure: **the stiffness sets the level; the level sets the deformation parameter (t at the corresponding root of unity — the "value of ħ" residue of phase 34); the level's superselection structure is classical shadow data (phase 45 B3b); and the sector count it produces is the one the Floer side independently computed.** Every number in the framework's structural core would then be one integer — the genus — read four ways.

**The honest boundary, drawn sharply.** What is proven: the count-level match (trivial arithmetic once both counts are known — but both counts come from *independent* computations: Muñoz–Wang/Bradlow on the Floer side, phase 44's frame computation on the GV side; their agreement through the SU(2) level formula was not built in). What is **open**: the content-level identification — the framework's flux sectors are U(1)/Spin^c labels, SU(2)_ℓ primaries are a different label set, and the per-sector protected ranks (phase 40 table: 1, 2g+2, …) are not the primaries' quantum dimensions. So the match could still be numerology. **The decidable test (logged as B3c-test):** find the dictionary — the natural candidate is that the framework's sector *k* corresponds to the level-ℓ primary of spin |k| (both run over 2g−1 values with matching symmetry k ↔ −k), and the thing to compare is not quantum dimensions but the *fusion structure*: does the truncated fusion of level 2g−2 reproduce the sector-composition rules the Floer side imposes (Bradlow truncation as fusion truncation)? This is a finite, checkable computation per genus — exactly the kind of desk test the program's method demands. Until it is run, B3c stays [conjecture — count-level exact, content-level open], and the phrase "the level is the stiffness" carries that tag.

## 3. Ledger

- **H6: executed** at measure level (theorem-backed transcription); operator level logged as H6b for the specialist. The EQ→GH-temperature loop is closed; phase 44 §1d's flagged tension is resolved.
- **B3c: sharpened** from a vague pivot to an exact count identity plus one named decidable test (fusion vs Bradlow). The expert kernel gains its most concrete question yet: *is Bradlow truncation a fusion truncation at level GV/4π²?*
- Updated critical path: (i) the B3c fusion test (desk, per-genus, decidable); (ii) the Γ-twisted net (join rows 2–4); (iii) the species sum; (iv) H5b/H6b for the specialist packet.

*Status line [amended 2026-07-18, FR2-7 — the original "closing exactly onto the Gibbons–Hawking form" survived its own §1 re-tag and is corrected here]: EQ now exists in the language a referee would demand, supplying β = 1 in the fold's natural units — the Gibbons–Hawking coefficient awaits the T-2π transport; and the discreteness cascade has acquired an exact arithmetic spine — level = stiffness — with its remaining gap isolated as one finite fusion computation (later refuted; see phase 48). The framework's structural story: one integer (genus), four readings, one decidable test standing between them.*
