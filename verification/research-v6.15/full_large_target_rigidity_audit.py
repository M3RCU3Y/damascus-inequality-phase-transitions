#!/usr/bin/env python3
"""Exact symbolic audit for the V6.15 full large-target rigidity reduction.

This checks the endpoint formulas and Jacobian factorization.  The already-
certified signs G_nu>0 and G_tt<0 come from the V6.14 onset replay; the sign
G_dd<0 uses the analytic positive-branch monotonicity theorem.
"""
import sympy as sp

# Target endpoint formula and q solution.
t, d, q = sp.symbols('t d q', positive=True)
H0 = 2 * sp.cosh(d) / t - 1 + (q - 1) / (q + 1)
assert sp.simplify(H0.subs(d, 0).subs(q, t - 1)) == 0
assert sp.simplify(sp.diff(H0, q).subs(d, 0)) == 2 / (q + 1) ** 2

# Source transverse curvature.  If Phi(log t) is written abstractly and
# H=Phi', then Phi(c+d)+Phi(c-d) has second d derivative 2 Phi''(c).
c = sp.symbols('c')
Phi = sp.Function('Phi')
expr = Phi(c + d) + Phi(c - d)
assert sp.simplify(sp.diff(expr, d, 2).subs(d, 0) - 2 * sp.diff(Phi(c), c, 2)) == 0

# Endpoint stationary-system Jacobian.  At epsilon=0:
# G_t=G_d=G_q=H_d=0, G is q-independent, and one-d mixed derivatives vanish.
Gnu, Gnut, Gtt, Gdd, Ht, Hq = sp.symbols(
    'Gnu Gnut Gtt Gdd Ht Hq', nonzero=True
)
J = sp.Matrix([
    [Gnu,          0,          0,  0],
    [0,            Ht,         0,  Hq],
    [Gnut * Hq,    Gtt * Hq,   0,  0],
    [0,            0,          Gdd * Hq, 0],
])
expected = Gnu * Gtt * Gdd * Hq ** 3
assert sp.expand(J.det() - expected) == 0

print('FULL LARGE-TARGET RIGIDITY IDENTITY AUDIT PASSED')
print('H(t,0,t-1,0)=0 verified')
print('H_q=2/(1+q)^2 verified')
print('G_dd=2 Phi_xx(log t) verified')
print('det J0 = G_nu G_tt G_dd H_q^3 verified')
print('SCOPE: exact reduction identities; sign inputs are theorem/certificate dependencies')
