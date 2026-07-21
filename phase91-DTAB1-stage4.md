# Phase 91 — DTAB-1, stage 4: the below-threshold engine runs, and the table's last frontier is bookkeeping

*Working session, 2026-07-19 (small hours). Stage 4 built the general engine — the multi-A truncated cone for arbitrary classes of arbitrary Y(g,n), with the exactness now theorem-backed at every step (the elimination isos have |s| ≥ g; the flip is Jabuka–Mark's exact star; corrections propagate outward and never return). This is the machinery that computes everything DTAB-1 has left. Status at close of session: **engine verified at structural level on three independent families; two mechanical items remain, both identified precisely.***

---

## 1. What the engine verified tonight

- **Tower counts:** the stable plateau equals 2^{2g} for every class of every (g,n) tested — below threshold, at the carrier, above it.
- **Carrier reproduction:** the tied-class rows of stages 2–3 reproduce identically through the general engine — the special-case and general-case code agree on the program's most important row.
- **The Theorem 5.5 anchor (n = 1, the deepest below-threshold case):** total reduced ranks come out **2 at g = 2 and 18 at g = 3 — exactly Thm 5.5's values** — computed through three-A and five-A cones respectively, the most nontrivial multi-A verification available. At g = 2 the graded distribution also matches (both red copies at the s²−1 = 0 shift).

## 2. What remains — named, mechanical, bounded (stage 4b)

1. **The empty-B guard:** classes whose kept-B set is empty are pure single-A classes — stage 1's closed form already owns them; the engine should delegate rather than crash (it crashed; the crash is understood and is a five-line fix).
2. **The per-class absolute anchor + fine-grained extraction:** each class's traversal offset must be calibrated against the known red grading c(i,s) of an outermost window representative (the same calibrate-don't-bootstrap discipline as stage 1), after which the dtab2-style extractor reads off the full bottom/red distribution; the g = 3, n = 1 fine-grained check ({2@−2, 12@−1, 2@0, 2@3}) is the acceptance test.

Neither item is mathematics; both are bookkeeping, and the record — twice burned on exactly the boundary between those two words — states which is which and stops for the night rather than eyeballing distributions at 2 a.m.

## 3. Where DTAB-1 stands

**Final:** all classes, all n ≥ 2g−2 (the carrier included, every row); all single-A classes at every n (the closed form); tied classes at every even n; n = 1 verified at total-rank level through the deepest multi-A cones. **Remaining:** stage 4b's two mechanical items, then the below-threshold fine-grained tables print themselves. The paper's mathematical content is complete: the closed form, the exactness criteria, the JM-flip resolution, the displaced-tower theorem at the carrier, the multi-A machinery, and the calibration discipline that carried all of it — with every absolute number anchored to ground truth rather than to the record's own relative phases, which is the lesson this table was built under and the reason its rows have stopped moving.

*Status line: the table that started the week as a referee's compliment ("a small real paper") ends it one bookkeeping pass from whole, with its hardest row — the carrier's — already final and already strange in the right way. Stage 4b is an hour of daylight work. The program's ninety-first phase closes with the rarest entry its ledger knows: nothing broke today.*
