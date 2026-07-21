"""
Tier 2, Problem 2B, step 1: leading-order Sorkin I_3 for a state-dependent
(nonlinear) Hamiltonian H_psi = H + g N(psi), three-path interferometer.

Model (minimal concrete realization of BHMM's schematic H_psi = H + g psi):
  path space C^3; slit set S: psi_S = sum_{i in S} alpha_i |i>;
  local-density nonlinearity N(psi) = sum_i (|<i|psi>|^2/<psi|psi>) |i><i|;
  lambda := g tau / hbar. Exact solution: n_i(S) = |alpha_i|^2 / sum_{j in S} |alpha_j|^2
  conserved -> psi_S(tau) = sum_{i in S} alpha_i e^{-i lambda n_i(S)} |i>.
  A_S = sum_{i in S} beta_i e^{-i lambda n_i(S)}, beta_i = conj(d_i) alpha_i = r_i e^{i phi_i}.

Hand-derived leading order:
  I_3 = lambda * SUM_{i<j} 2 r_i r_j sin(phi_i-phi_j) (Dn3_ij - Dn2_ij) + O(lambda^2),
  Dn3_ij = (a_i-a_j)/(a_A+a_B+a_C), Dn2_ij = (a_i-a_j)/(a_i+a_j), a_i = |alpha_i|^2.

Checks: (1) I_3 = 0 at lambda=0 exactly; (2) O(lambda) coefficient matches exact
nonlinear integration; (3) projector nonlinearity -> I_3 = 0 exactly; (4) equal
intensities or all-real amplitudes -> coefficient vanishes (I_3 = O(lambda^2));
(5) distribution of C = I_3/(lambda * sum|I_2|); (6) scale table.
"""
import numpy as np
from itertools import combinations
from scipy.integrate import solve_ivp

rng = np.random.default_rng(7)
MASK = {s: np.array([1.0 if k in s else 0.0 for k in 'ABC'])
        for s in ['A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']}

def evolve_exact(alpha, lam, kind='local'):
    if np.allclose(alpha, 0):
        return alpha.astype(complex)
    def rhs(t, y):
        psi = y[:3] + 1j*y[3:]
        nrm = np.vdot(psi, psi).real
        if kind == 'local':
            dpsi = -1j * lam * (np.abs(psi)**2 / nrm) * psi
        else:  # projector: N = |psi><psi|/<psi|psi>  ->  N psi = psi
            dpsi = -1j * lam * psi
        return np.concatenate([dpsi.real, dpsi.imag])
    y0 = np.concatenate([alpha.real, alpha.imag])
    sol = solve_ivp(rhs, (0, 1), y0, rtol=1e-12, atol=1e-14)
    yf = sol.y[:, -1]
    return yf[:3] + 1j*yf[3:]

def probs(alpha, d, lam, kind='local'):
    return {s: abs(np.vdot(d, evolve_exact(alpha*MASK[s], lam, kind)))**2
            for s in MASK}

def I3_of(P):
    return P['ABC'] - P['AB'] - P['AC'] - P['BC'] + P['A'] + P['B'] + P['C']

def I2sum_of(P):
    return (abs(P['AB']-P['A']-P['B']) + abs(P['AC']-P['A']-P['C'])
            + abs(P['BC']-P['B']-P['C']))

def coef_formula(alpha, d):
    beta = np.conj(d) * alpha
    rr, pp, aa = np.abs(beta), np.angle(beta), np.abs(alpha)**2
    tot = 0.0
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        Dn3 = (aa[i]-aa[j]) / aa.sum()
        Dn2 = (aa[i]-aa[j]) / (aa[i]+aa[j])
        tot += 2*rr[i]*rr[j]*np.sin(pp[i]-pp[j])*(Dn3-Dn2)
    return tot

alpha = rng.normal(size=3) + 1j*rng.normal(size=3)
d = rng.normal(size=3) + 1j*rng.normal(size=3); d /= np.linalg.norm(d)

print("(1) linear QM (lambda=0): I_3 =", f"{I3_of(probs(alpha,d,0.0)):.3e}")

print("\n(2) exact nonlinear I_3 vs lambda * (hand coefficient):")
c = coef_formula(alpha, d)
for lv in [1e-2, 1e-3, 1e-4]:
    i3 = I3_of(probs(alpha, d, lv))
    print(f"  lambda={lv:.0e}:  I3={i3: .6e}   lambda*coef={lv*c: .6e}   "
          f"ratio={i3/(lv*c):.6f}")

print("\n(3) projector nonlinearity (global phase), lambda=0.1: I_3 =",
      f"{I3_of(probs(alpha,d,0.1,'projector')):.3e}")

al_sym = np.exp(1j*rng.normal(size=3))            # equal intensities
al_real = np.abs(rng.normal(size=3))              # real amplitudes
d_real = np.abs(rng.normal(size=3)); d_real /= np.linalg.norm(d_real)
print("\n(4) degeneracies (coefficient must vanish; I_3 = O(lambda^2)):")
print("  equal |alpha_i|: coef =", f"{coef_formula(al_sym, d):.3e}",
      "  I3(1e-3) =", f"{I3_of(probs(al_sym,d,1e-3)):.3e}")
print("  all real:        coef =", f"{coef_formula(al_real, d_real):.3e}",
      "  I3(1e-3) =", f"{I3_of(probs(al_real,d_real,1e-3)):.3e}")

print("\n(5) kappa = C*lambda: |C| over 5000 random configs")
Cs = []
for _ in range(5000):
    al = rng.normal(size=3) + 1j*rng.normal(size=3)
    dd = rng.normal(size=3) + 1j*rng.normal(size=3)
    b = np.conj(dd)*al
    rr, pp, aa = np.abs(b), np.angle(b), np.abs(al)**2
    num = sum(2*rr[i]*rr[j]*np.sin(pp[i]-pp[j])
              * ((aa[i]-aa[j])/aa.sum() - (aa[i]-aa[j])/(aa[i]+aa[j]))
              for i, j in [(0, 1), (0, 2), (1, 2)])
    den = sum(abs(2*rr[i]*rr[j]*np.cos(pp[i]-pp[j]))
              for i, j in [(0, 1), (0, 2), (1, 2)])
    Cs.append(abs(num)/den)
Cs = np.array(Cs)
print(f"  |C|: median={np.median(Cs):.3f}  90th={np.percentile(Cs,90):.3f}  "
      f"99th={np.percentile(Cs,99):.3f}  max={Cs.max():.3f}")

print("\n(6) scales")
hbar_eVs = 6.582119569e-16; EP = 1.2209e28
for tau, lab in [(1e-9, "photon bench, tau~1 ns"), (1.0, "atom interf., tau~1 s")]:
    print(f"  kappa=1e-2 with |C|=0.1 needs g ~ {1e-1*hbar_eVs/tau:.2e} eV  ({lab})")
G, c_, hb, eV = 6.674e-11, 2.998e8, 1.0546e-34, 1.602e-19
m_Cs, L = 2.207e-25, 1e-3
gSN = G*m_Cs**2/L/eV
print(f"  Schroedinger-Newton g ~ G m^2/L (Cs atom, L=1 mm): {gSN:.1e} eV"
      f"  -> lambda(tau=1s) = {gSN*eV/hb:.1e}")
for E, plat in [(1.5, "optical photon"), (4e6, "JUNO reactor nu"), (1e10, "10 GeV probe")]:
    print(f"  E/E_P ({plat}): {E/EP:.1e}")
eps = 4.135667696e-15 * 4e-6   # h * 4 uHz  (Bollinger et al. 1989, 9Be+)
print(f"  Weinberg-nonlinearity spectroscopy bound (~4 uHz): {eps:.1e} eV")
print(f"  g(kappa=1e-2, tau=1 s) exceeds that bound by "
      f"{(1e-1*hbar_eVs/1.0)/eps:.0f}x")
