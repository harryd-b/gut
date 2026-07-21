# FR-2 arithmetic (phase 75), 2026-07-18.
# Corrected sector counts on the carrier T^1 Sigma_g and the (flagged, zero-weight)
# count-level menus; plus the block correspondence old-census <-> MOY components.
# Sources: MOY math/9612221 Cor 1.0.5 & Thm 5.9.1 (moduli; torsion-only sectors);
# OS math/0105202 Thm 1.6 (adjunction vanishing on vertical tori);
# Nelson-Weiler 2007.13883 Thm 1.1 (ECH per torsion class, all 2g-2 nonzero);
# OS08 AGT 8 (2008) 101-154 Thm 5.6 (HF_red of nontrivial circle bundles) - verbatim
# statement pending retrieval (OBTAIN-5.6).

from math import gcd

def menu(X):
    return [(p, pp, pp == p + 1) for p in range(2, 20) for pp in range(p + 1, 40)
            if gcd(p, pp) == 1 and (p - 1) * (pp - 1) == X]

f = lambda L: ", ".join(f"({a},{b})" + ("*U*" if u else "") for a, b, u in L) or "NONE"

print("Count-level menus on the carrier (FLAGGED: numerology; zero evidential weight):")
for g in range(2, 7):
    print(f" g={g}: all-torsion N=2g-2={2*g-2}: X={4*g-4}: {f(menu(4*g-4))}"
          f"   |   irreducible-carrying N=2g-3={2*g-3}: X={4*g-6}: {f(menu(4*g-6))}")

print("\nUnitary series m(m-1)=X hits:")
for m in range(3, 14):
    X = m * (m - 1)
    a = (X + 4) / 4 if (X + 4) % 4 == 0 else None
    b = (X + 6) / 4 if (X + 6) % 4 == 0 else None
    print(f" m={m} ({m},{m+1}): 2g-2 count -> g={a} ; 2g-3 count -> g={b}")

print("\nBlock correspondence: old r-sector (Sym^{g-1-|r|}) <-> MOY C+-(e), e=g-1-|r|:")
for g in (2, 3, 4):
    pairs = []
    for r in list(range(-(g - 1), 0)) + list(range(1, g)):
        e = g - 1 - abs(r)
        fam = 'C+' if r > 0 else 'C-'
        cls = e if r > 0 else (2 * g - 2 - e) % (2 * g - 2)
        pairs.append(f"r={r:+d}->{fam}({e})@[{cls}]")
    print(f"  g={g} (classes mod {2*g-2}): " + ", ".join(pairs))
    # middle class g-1 is reducible-only (MOY-degenerate spin sector)
    print(f"        middle class [{g-1}]: reducibles only (spin-type, MOY Cor 5.8.5 degenerate)")
