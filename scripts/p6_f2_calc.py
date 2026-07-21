"""
Package 2 of the acting-expert sweep.

PART 1 -- P6 statistics-clause computation (phase 27, P6.2; phase 28 target):
On S^1 x Sigma_g the framework's statistics clause predicts, per flux sector k
(0 < |k| <= g-1), fermionic multiplicity = b_odd(Sym^{g-1-|k|} Sigma_g)
(odd total Betti number of the symmetric product), with protected content
H^*(Sym^{g-1-|k|} Sigma_g) [Munoz-Wang].

Macdonald's formula (Macdonald 1962, 'The Poincare polynomial of a symmetric
product'):  sum_n q^n P_t(Sym^n X) = (1+qt)^{2g} / ((1-q)(1-q t^2))
for X = Sigma_g (b_0=1, b_1=2g, b_2=1).

We compute exact Betti numbers via polynomial arithmetic (sympy-free: use
numpy polynomial with exact ints via python ints and manual series).

PART 2 -- F2 (phase 38 audit item): does the equal-intensity exact null of the
diagonal nonlinear model survive path-mixing H != 0?  Numerics: three-site
model, H = hopping matrix, i dpsi/dt = (H + lam*N(psi)) psi, N = diag local
density (deg-0 homogeneous). Equal-intensity input; measure I3(lam) scaling.
"""
import numpy as np
from itertools import combinations
from scipy.integrate import solve_ivp
from math import comb

# ---------------- PART 1: Macdonald / b_odd table ----------------
def poincare_sym(n, g):
    """Exact Betti numbers b_0..b_{2n} of Sym^n(Sigma_g) via Macdonald.
    Coefficient of q^n in (1+qt)^{2g} * sum_{a,b} q^{a+b} t^{2b}
    ((1-q)^{-1}(1-qt^2)^{-1} expanded)."""
    # (1+qt)^{2g} = sum_j C(2g,j) q^j t^j
    # 1/((1-q)(1-q t^2)) = sum_{a>=0} sum_{b>=0} q^{a+b} t^{2b}
    # coefficient of q^n: sum_j C(2g,j) * [terms a+b = n-j] t^{j+2b}
    maxdeg = 2*n
    betti = [0]*(maxdeg+1)
    for j in range(0, min(2*g, n)+1):
        cj = comb(2*g, j)
        for b in range(0, n-j+1):
            deg = j + 2*b
            if deg <= maxdeg:
                betti[deg] += cj
    return betti

print("PART 1 — statistics clause on S^1 x Sigma_g")
print("sector |k|, n = g-1-|k|, protected content H*(Sym^n Sigma_g):")
print(f"{'g':>3} {'|k|':>4} {'n':>3} {'b_even':>8} {'b_odd':>8} {'chi':>8} {'total':>8}")
results = {}
for g in range(1, 7):
    for k in range(0, g):          # |k| = 0..g-1 ; n = g-1-|k| ; k=0 flagged separately
        n = g - 1 - k
        betti = poincare_sym(n, g)
        b_even = sum(b for i, b in enumerate(betti) if i % 2 == 0)
        b_odd = sum(b for i, b in enumerate(betti) if i % 2 == 1)
        chi = b_even - b_odd
        results[(g, k)] = (b_even, b_odd, chi)
        note = " (k=0: Jacobian dressing/2-torsion caveat, phase 28)" if k == 0 else ""
        print(f"{g:>3} {k:>4} {n:>3} {b_even:>8} {b_odd:>8} {chi:>8} {b_even+b_odd:>8}{note}")

# sanity checks against known topology
print("\nsanity: Sym^0 = pt -> (1,0); Sym^1 Sigma_g = Sigma_g -> (2, 2g);")
print("Sym^2 Sigma_2 known Betti: 1,4,7,4,1 ->", poincare_sym(2, 2))
# Sym^n Sigma_1 = ? Sym^n T^2 fibers over Jac = T^2 with CP^{n-1} fiber:
print("Sym^2 T^2 (should be 1,2,2,2,1? check chi=0):", poincare_sym(2, 1),
      " chi:", sum((-1)**i * b for i, b in enumerate(poincare_sym(2, 1))))

# Euler characteristic cross-check: chi(Sym^n Sigma_g) = C(2-2g+n-1... use
# generating function sum chi q^n = (1-q)^{2g}/(1-q)^2 = (1-q)^{2g-2}
print("\nchi cross-check vs (1-q)^{2g-2} expansion:")
ok = True
for g in range(1, 7):
    for n in range(0, g):
        # coefficient of q^n in (1-q)^{2g-2}
        chi_gf = comb(2*g-2, n)*(-1)**n if n <= 2*g-2 else 0
        chi_direct = sum((-1)**i * b for i, b in enumerate(poincare_sym(n, g)))
        if chi_gf != chi_direct:
            ok = False
            print(f"  MISMATCH g={g} n={n}: {chi_gf} vs {chi_direct}")
print("  all chi match:", ok)

# ---------------- PART 2: F2 mixing check ----------------
print("\nPART 2 — F2: equal-intensity null under path mixing H != 0")
rng = np.random.default_rng(11)
MASK = {s: np.array([1.0 if c in s else 0.0 for c in 'ABC'])
        for s in ['A','B','C','AB','AC','BC','ABC']}

Hmix = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
Hmix = (Hmix + Hmix.conj().T)/2          # hermitian, O(1) hopping

def evolve(alpha, lam):
    def rhs(t, y):
        psi = y[:3] + 1j*y[3:]
        nrm = np.vdot(psi, psi).real
        dpsi = -1j * (Hmix @ psi + lam*(np.abs(psi)**2/nrm)*psi)
        return np.concatenate([dpsi.real, dpsi.imag])
    y0 = np.concatenate([alpha.real, alpha.imag])
    sol = solve_ivp(rhs, (0, 1), y0, rtol=1e-12, atol=1e-14)
    return sol.y[:3, -1] + 1j*sol.y[3:, -1]

def I3(alpha, d, lam):
    P = {s: abs(np.vdot(d, evolve(alpha*MASK[s], lam)))**2 for s in MASK}
    return (P['ABC'] - P['AB'] - P['AC'] - P['BC'] + P['A'] + P['B'] + P['C'])

# equal-intensity input, random phases; random detector
alpha_eq = np.exp(1j*rng.normal(size=3))
d = rng.normal(size=3) + 1j*rng.normal(size=3); d /= np.linalg.norm(d)

print("equal-intensity input, H != 0:")
prev = None
for lam in [1e-2, 1e-3, 1e-4, 1e-5]:
    v = I3(alpha_eq, d, lam)
    scale = "" if prev is None else f"   ratio to prev = {prev/v:.1f}"
    print(f"  lambda={lam:.0e}: I3 = {v: .3e}{scale}")
    prev = v
print("(ratio ~10 per decade => O(lambda); ~100 => O(lambda^2))")

# compare: generic (asymmetric) input with H != 0
alpha_gen = rng.normal(size=3) + 1j*rng.normal(size=3)
print("generic asymmetric input, H != 0:")
prev = None
for lam in [1e-2, 1e-3, 1e-4, 1e-5]:
    v = I3(alpha_gen, d, lam)
    scale = "" if prev is None else f"   ratio to prev = {prev/v:.1f}"
    print(f"  lambda={lam:.0e}: I3 = {v: .3e}{scale}")
    prev = v
