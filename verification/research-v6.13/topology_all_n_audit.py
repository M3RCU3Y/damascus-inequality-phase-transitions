#!/usr/bin/env python3
"""Exact audit for the uniform three-variable topology theorem."""
from math import comb
from fractions import Fraction
import sympy as sp

n, t, r = sp.symbols("n t r", positive=True, integer=True)

# h_n derivative identity.
h = t**n * (n + (n + 1) * t - t ** (n + 1)) / (1 + t ** (n + 1)) ** 2
P = (
    t ** (2 * n + 2)
    - (n + 1) ** 2 * t ** (n + 2)
    - (n**2 + 4 * n + 1) * t ** (n + 1)
    + (n + 1) ** 2 * t
    + n**2
)
assert sp.factor(sp.diff(h, t) - t ** (n - 1) * P / (1 + t ** (n + 1)) ** 3) == 0
A = sp.symbols("A")
P_A = A**2 - (n + 1)**2 * t * A - (n**2 + 4*n + 1) * A + (n + 1)**2 * t + n**2
assert sp.factor(P_A.subs(A, n + (n + 1) * t)) == -n * (n + 1) ** 2 * (t + 1) ** 2
assert sp.expand(P.subs(t, 1)) == -4 * n

# Uniform ratio-monotonicity algebra used in the coefficient proof.
M = -4*n**3 + 6*n**2*r - 12*n**2 - 2*n*r**2 + 11*n*r + 9*n - 9*r + 27
assert sp.factor(M.subs(r, n)) == 27 - n**2
assert sp.factor(sp.diff(M, r)) == -4*n*r + 6*n**2 + 11*n - 9
assert sp.expand(2*(2*n+1)*(2*n-3) - (n+2)*(2*n+3) - 3*(2*n**2 - 5*n - 4)) == 0

# Verify the rational step-ratio identity used to show Q_r decreases.
qratio = (
    (n + 3 - r) / (2*n + 3 - r)
    * (2*n + 5 - r) / (2*n + 1 - 2*r)
    * (2*n + 3 - 2*r) / (2*n + 6 - r)
)
den = (-2*n + r - 6) * (-2*n + r - 3) * (-2*n + 2*r - 1)
assert sp.factor((qratio - 1) * den + M) == 0


def coeffs(N: int) -> list[int]:
    out = []
    for R in range(1, 2 * N + 4):
        value = comb(2 * N + 3, R) - 2 * comb(2 * N + 2, R)
        if R <= N + 3:
            value += comb(N + 3, R)
        if R <= N + 2:
            value += comb(N + 2, R)
        if R <= 2:
            value += comb(2, R)
        out.append(value)
    return out


def phi(N: int, x):
    return (x**N - 1) / (x**(N + 1) + 1)


# Direct symbolic replay of the symmetric-slice factorization for representative
# exponents. The proof in the note is uniform; this guards transcription.
T = sp.symbols("T", positive=True)
for N in range(4, 13):
    G = T**(2*N + 2) * (T - 2) + T**(N + 2) * (T + 1) + T**2 - 2
    lhs = 2 * phi(N, T) + phi(N, T**-2)
    rhs = -(T**N - 1) * G / ((T**(N + 1) + 1) * (T**(2*N + 2) + 1))
    assert sp.factor(lhs - rhs) == 0


def sign_changes(values: list[int]) -> int:
    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in values]
    signs = [x for x in signs if x]
    return sum(a != b for a, b in zip(signs, signs[1:]))


assert coeffs(4) == [6, 2, -20, -40, -15, 50, 91, 75, 35, 9, 1]
assert coeffs(5) == [6, -4, -63, -170, -220, -97, 141, 298, 275, 154, 54, 11, 1]

for N in range(4, 501):
    cs = coeffs(N)
    assert sign_changes(cs) == 2
    if N >= 6:
        assert cs[0] > 0
        assert all(v < 0 for v in cs[1:N+1])
        assert all(v > 0 for v in cs[N+1:])

# Exact n=4 midpoint sign used to seed the uniform G_n(3/2)<0 argument.
a = Fraction(3, 2) ** 6
mid = -Fraction(2, 9) * a * a + Fraction(5, 2) * a + Fraction(1, 4)
assert mid == Fraction(-217, 2048)

print("UNIFORM TOPOLOGY ALGEBRA AUDIT PASSED")
print("coefficient sign pattern replayed exactly for n=4,...,500")
print("n=4 midpoint value:", mid)
