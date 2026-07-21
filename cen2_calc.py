# CEN-2 (phase 77), 2026-07-18. The carrier census from OS08 Theorem 5.6.
# Source: Ozsvath-Szabo, "Knot Floer homology and integer surgeries",
# arXiv:math/0410300v2 (AGT 8 (2008) 101-154), Section 5.2 — text extracted
# from the downloaded PDF this session (OBTAIN-5.6 closed).
#
# Thm 5.6 (verbatim structure): Y(g,n) = Euler-number-n>0 circle bundle over
# genus-g surface; for [i] in Z/n, j = min-|.| integer ≡ i (mod n):
#   HF+_red(Y(g,n), i; Z/2) = ⊕_{s ≡ i (n), s ≠ j} X_{c(i,s)}(g, g-1-|s|)
# X(g,d) = ⊕_{k=0}^{d} Λ^{2g-k}H¹(Σ_g) ⊗ Z[U]/U^{d-k+1};  H_*(Sym^d Σ) = X_{*-2d}(g,d)
# c(i,s) = d(n,i) - 1 - s + Σ_{0≤t≤s, t≡i (n)} 2t   (s ≥ 0)
#        = d(n,i) - 1 + s - Σ_{s≤t≤0, t≡i (n)} 2t   (s ≤ 0)
# d(n,i) = -max_{s ≡ i (n)} (1/4)(1 - (n+2s)²/n)    [OS08 eq. (2)]
# T¹Σ_g = Y(g, 2g-2) up to orientation.

from math import comb
from fractions import Fraction

def rankX(g, d):
    if d < 0: return 0
    return sum(comb(2*g, k) * (d - k + 1) for k in range(d + 1))

def dinv(n, i):
    best = None
    for k in range(-200, 201):
        s = i + k * n
        v = Fraction(1, 4) * (1 - Fraction((n + 2*s)**2, n))
        best = v if best is None or v > best else best
    return -best

def c_grading(n, i, s):
    d = dinv(n, i)
    if s >= 0:
        return d - 1 - s + 2 * sum(t for t in range(0, s + 1) if (t - i) % n == 0)
    return d - 1 + s - 2 * sum(t for t in range(s, 1) if (t - i) % n == 0)

def census(g, n):
    out = {}
    for i in range(n):
        cands = [s for s in range(-n, n + 1) if (s - i) % n == 0]
        mn = min(abs(s) for s in cands)
        js = [s for s in cands if abs(s) == mn]
        j = js[0]
        svals = [s for s in range(-(g - 1), g) if (s - i) % n == 0 and s != j]
        out[i] = dict(rank=sum(rankX(g, g - 1 - abs(s)) for s in svals),
                      terms=[(s, rankX(g, g - 1 - abs(s)), c_grading(n, i, s)) for s in svals],
                      tie=len(js) > 1)
    return out

print("Sanity: Thm 5.6 at n=1 reproduces Thm 5.5:")
for g in range(2, 6):
    direct = 2 * sum(rankX(g, g - 1 - s) for s in range(1, g))
    via = sum(v['rank'] for v in census(g, 1).values())
    print(f"  g={g}: {direct} vs {via}  match={direct == via}")

print("\nCEN-2: HF+_red(T^1 Sigma_g) = Y(g, 2g-2):")
for g in range(2, 7):
    n = 2 * g - 2
    c = census(g, n)
    tot = sum(v['rank'] for v in c.values())
    nz = {i: v for i, v in c.items() if v['rank']}
    print(f"  g={g}: total rank = {tot}; nonzero sectors: "
          + "; ".join(f"[{i}] rank {v['rank']} (terms {[(s, r, str(cc)) for s, r, cc in v['terms']]},"
                      f" j-tie={v['tie']})" for i, v in nz.items()))

print("\nExtremality: totals for n = 2g-3 .. 2g+1:")
for g in range(2, 6):
    row = {n: sum(v['rank'] for v in census(g, n).values()) for n in range(max(1, 2*g-4), 2*g+2)}
    print(f"  g={g}: {row}   (2g-2 = {2*g-2})")

# Elementary corollaries of Thm 5.6 (proofs in phase 77):
#  - n >= 2g-1  =>  HF_red = 0 (each class has at most one rep in |s|<=g-1, and it is j)
#  - n = 2g-2   =>  total rank exactly 1, in class [g-1] (the spin-type middle sector):
#                   the window endpoints ±(g-1) share that class; one is j, the other
#                   contributes X(g,0) = Λ^{2g}H¹ = rank 1.
