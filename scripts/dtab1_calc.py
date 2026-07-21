# DTAB-1 stage 1 (phase 88), 2026-07-18.
# Tower bottoms (generalized d-invariants) for circle bundles Y(g,n), n>0, from the
# OS08 Borromean mapping cone. Method disciplined per phase 86: the absolute shift is
# CALIBRATED at g=0 (lens spaces, where HF+(L(n,1),i) = T+_{d(n,i)} is ground truth)
# and the calibration is knot-independent (the shift comes from the surgery cobordism).
#
# CLOSED FORM [derived, calibrated, conjugation-verified on its domain]:
#   d_m(Y(g,n), [i]) = d(n,i) + (m - g) + 2*min(0, g+j-m) - 2*min(0, j)
# where j = the unique minimal-|.| representative of [i] mod n, and m = 0..2g indexes
# the Lambda^m H^1 tower family (multiplicity C(2g,m)).
# DOMAIN: all classes [i] with a UNIQUE minimal representative. For tied classes
# (i = n/2, n even — including the carrier's protected class [g-1] at n = 2g-2) the
# correct computation is the cone over BOTH A_{±j}: stage 2, NOT provided here; the
# conjugation test below FAILS exactly on those classes, as it must.
#
# For n >= 2g-1 with n odd: HF_red = 0 and this table is the COMPLETE Floer package.

from fractions import Fraction
from math import comb

def dinv(n, i):
    best = None
    for k in range(-300, 301):
        s = i + k * n
        v = Fraction(1, 4) * (1 - Fraction((n + 2 * s) ** 2, n))
        best = v if best is None or v > best else best
    return -best

def minabs_rep(n, i):
    cands = [i + k * n for k in range(-2, 3)]
    mn = min(abs(s) for s in cands)
    js = sorted(s for s in cands if abs(s) == mn)
    return js[0], len(js) > 1

def d_m(g, n, i, m):
    j, tie = minabs_rep(n, i)
    val = dinv(n, i) + (m - g) + 2 * min(0, g + j - m) - 2 * min(0, j)
    return val, tie

if __name__ == "__main__":
    print("Calibration (g=0 -> d(n,i) exactly):")
    for n in (3, 4, 5):
        print(f"  L({n},1):", {i: str(d_m(0, n, i, 0)[0]) for i in range(n)})

    print("\nConjugation test d_m(i) = d_(2g-m)(-i): holds off ties, fails on ties (diagnostic):")
    for g in (2, 3):
        for n in range(2 * g - 2, 2 * g + 3):
            bad = []
            for i in range(n):
                tie = minabs_rep(n, i)[1]
                ok = all(d_m(g, n, i, m)[0] == d_m(g, n, (n - i) % n, 2 * g - m)[0]
                         for m in range(2 * g + 1))
                if not ok:
                    bad.append((i, tie))
            print(f"  g={g}, n={n}: failures {bad} (all tied: {all(t for _, t in bad)})")

    print("\nSample rows (g=2): see phase 88 for the table.")
