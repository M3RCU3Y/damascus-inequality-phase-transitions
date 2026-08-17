"""Exact / symbolic audit for the generalized Damascus phase-transition draft.

Every assertion labelled exact uses Fraction or SymPy exact arithmetic.
The final uniform-family sweep is a high-precision numerical independent audit,
not part of the analytic proof.
"""
from fractions import Fraction as F
from functools import reduce
import mpmath as mp
import sympy as sp


def phi(n, x):
    return (x**n - F(1)) / (x**(n + 1) + F(1))


def S(n, xs):
    return sum((phi(n, x) for x in xs), F(0))


def prod(xs):
    return reduce(lambda a, b: a * b, xs, F(1))


def check_flip(n, xs):
    assert prod(xs) == 1
    a, b = S(n, xs), S(n + 1, xs)
    assert a > 0 and b < 0, (n, a, b)
    return a, b


# ---------------------------------------------------------------------------
# 1. Exact rational one-step counterexamples.
# ---------------------------------------------------------------------------
witnesses = {
    1: [F(5)] * 9 + [F(5, 7), F(5, 7), F(49, 5**11)],
    2: [F(3)] * 5 + [F(2, 3), F(1, 162)],
    3: [F(3)] * 4 + [F(23, 27), F(1, 69)],
    4: [F(2)] * 3 + [F(7, 47), F(47, 56)],
    5: [F(2)] * 3 + [F(4, 27), F(27, 32)],
    6: [F(2)] * 3 + [F(6, 7), F(7, 48)],
    7: [F(70, 41), F(30, 17), F(12, 35), F(697, 720)],
    8: [F(5, 3), F(5, 3), F(3, 8), F(24, 25)],
}
for k, xs in witnesses.items():
    a, b = check_flip(k, xs)
    print(f"exact flip {k}->{k+1}: {float(a): .12g}, {float(b): .12g}")


# ---------------------------------------------------------------------------
# 2. Exact re-entrant point.
# ---------------------------------------------------------------------------
Y = [F(4, 7), F(9, 10), F(5, 4), F(3, 2), F(28, 27)]
assert prod(Y) == 1
checks = [(11, -1), (12, 1), (18, 1), (19, -1), (23, -1), (24, 1)]
for k, sgn in checks:
    sk = S(k, Y)
    assert (sk > 0) == (sgn > 0)
L_exact = sum((F(1, x) for x in Y if x > 1), F(0)) - sum(1 for x in Y if x < 1)
assert L_exact == F(181, 420)
print("re-entry exact signs and L=181/420 checked")


# ---------------------------------------------------------------------------
# 3. Critical (m,n)=(5,2) factorization.
# ---------------------------------------------------------------------------
e = sp.symbols("e", positive=True)
ph = lambda k, t: (t**k - 1) / (t ** (k + 1) + 1)
expr = sp.factor(ph(2, e) + ph(2, 1 / (8 * e)) + 3 * ph(2, sp.Integer(2)))
target = e * (64 * e**2 - 71 * e + 8) / ((e**2 - e + 1) * (64 * e**2 - 8 * e + 1))
assert sp.simplify(expr - target) == 0
print("critical escape factorization checked")


# ---------------------------------------------------------------------------
# 4. Taylor jet of g_n(u)=phi_n(exp u).
# ---------------------------------------------------------------------------
u, Nsym = sp.symbols("u N", real=True, positive=True)
g = (sp.exp(Nsym * u) - 1) / (sp.exp((Nsym + 1) * u) + 1)
coeff = [sp.factor(sp.diff(g, u, k).subs(u, 0) / sp.factorial(k)) for k in range(1, 6)]
assert coeff[0] == Nsym / 2
assert coeff[1] == -Nsym / 4
assert coeff[2] == -Nsym**2 * (Nsym + 3) / 24
assert coeff[3] == Nsym * (Nsym**2 + 3 * Nsym + 1) / 48
assert coeff[4] == Nsym**2 * (2 * Nsym**3 + 10 * Nsym**2 + 15 * Nsym + 5) / 480
print("Taylor coefficients through order five checked")


# ---------------------------------------------------------------------------
# 5. Inversion-dissipation identity for n=1,...,12.
# ---------------------------------------------------------------------------
t = sp.symbols("t", positive=True)
for k in range(1, 13):
    lhs = sp.cancel(ph(k, t) + ph(k, 1 / t))
    geom = sum(t**j for j in range(k))
    rhs = -(t - 1) ** 2 * geom / (t ** (k + 1) + 1)
    assert sp.factor(lhs - rhs) == 0
print("inversion identity checked for n=1..12")


# ---------------------------------------------------------------------------
# 6. Global and sign-sector sharp moment equality vectors.
# ---------------------------------------------------------------------------
for M in range(3, 30):
    v = [sp.Rational(-1)] + [sp.Rational(1, M - 1)] * (M - 1)
    mu2 = sum(z * z for z in v)
    mu3 = sum(z**3 for z in v)
    assert sp.simplify(-mu3 - sp.Rational(M - 2, M - 1) * mu2) == 0
for r in range(1, 20):
    v = [sp.Rational(-1)] + [sp.Rational(1, r)] * r
    mu2 = sum(z * z for z in v)
    mu3 = sum(z**3 for z in v)
    assert sp.simplify(-mu3 - sp.Rational(r - 1, r) * mu2) == 0
print("global and sign-count moment sharpness vectors checked")


# ---------------------------------------------------------------------------
# 7. Exact base inequalities in the uniform n>=9 four-variable proof.
# ---------------------------------------------------------------------------
base_pos = F(3, 35) - 22 * F(4, 7) ** 10
assert base_pos == F(5717461, 1412376245) and base_pos > 0
base_neg = F(211, 147) * F(64, 147) ** 10
assert base_neg < F(1, 588)
# Ratio tests proving monotone decay of the two exponential tails.
# a_N=N(4/7)^N: a_{N+1}/a_N=((N+1)/N)*(4/7)<1 for N>=2.
assert F(3, 2) * F(4, 7) < 1
# b_N=(7N+2)(64/147)^N; worst ratio at N=1.
assert F(16, 9) * F(64, 147) < 1
print("uniform-family exact base and ratio inequalities checked")


# ---------------------------------------------------------------------------
# 8. Exact threshold inequalities used in the phase tables.
# ---------------------------------------------------------------------------
assert F(8, 5) ** 5 - 5 * F(8, 5) - 4 < 0  # alpha_4 > 8/5 -> M_4<1/2
assert F(5, 3) ** 6 - 6 * F(5, 3) - 5 > 0  # alpha_5 < 5/3 -> M_5>1/2
print("M_4<1/2<M_5 root certificates checked")


# ---------------------------------------------------------------------------
# 9. Radial decomposition on exact rational test points.
# ---------------------------------------------------------------------------
def radial_decomp_fraction(n, xs):
    # Group reciprocal pairs only when exact values match. Units vanish.
    from collections import Counter
    above = Counter(x for x in xs if x > 1)
    below = Counter(x for x in xs if x < 1)
    radii = set(below) | {F(1, a) for a in above}
    L = sum((F(1, x) for x in xs if x > 1), F(0)) - sum(1 for x in xs if x < 1)
    corr = F(0)
    for r in radii:
        a = above.get(F(1, r), 0)
        b = below.get(r, 0)
        corr += (F(1) + r) * r**n / (F(1) + r ** (n + 1)) * (b - a * r)
    return L + corr
for xs in [Y, witnesses[7], witnesses[8]]:
    for k in [1, 3, 7, 12]:
        assert radial_decomp_fraction(k, xs) == S(k, xs)
print("radial decomposition exact tests checked")


# ---------------------------------------------------------------------------
# 10. Independent high-precision sweep of the analytic uniform family.
# ---------------------------------------------------------------------------
mp.mp.dps = 80

def mph(k, x):
    return (x**k - 1) / (x ** (k + 1) + 1)

for n0 in range(9, 61):
    NN = n0 + 1
    rr = mp.power(mp.mpf(3) / 4, mp.mpf(1) / NN)
    xs = [mp.mpf(16) / (49 * rr), rr, mp.mpf(7) / 4, mp.mpf(7) / 4]
    a = sum(mph(n0, x) for x in xs)
    b = sum(mph(n0 + 1, x) for x in xs)
    assert a > 0 and b < 0, (n0, a, b)
print("80-digit uniform-family sweep n=9..60 passed (independent numerical audit)")

print("ALL EXACT SYMBOLIC ASSERTIONS PASSED")
