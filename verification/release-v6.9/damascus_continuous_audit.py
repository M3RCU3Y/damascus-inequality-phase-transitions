#!/usr/bin/env python3
"""Symbolic checks for continuous exponents and the critical (5,2) expansion."""
import sympy as sp

nu, x, w = sp.symbols("nu x w", positive=True)
t = sp.exp(w)
phi = (t**nu - 1) / (t**(nu + 1) + 1)
g = sp.exp(-w/2) * sp.sinh(nu*w/2) / sp.cosh((nu+1)*w/2)
assert sp.simplify(sp.together(phi - g).rewrite(sp.exp)) == 0
kappa = sp.simplify(sp.diff(sp.log(g), nu))
kappa_expected = w*sp.cosh(w/2)/(2*sp.sinh(nu*w/2)*sp.cosh((nu+1)*w/2))
assert sp.simplify(kappa - kappa_expected) == 0

t0 = sp.symbols("t0", positive=True)
phi0 = lambda z: (z**nu - 1)/(z**(nu+1)+1)
assert sp.simplify(phi0(1/t0) + t0*phi0(t0)) == 0

# Exact continuous three-variable onset reduction.  Here p=t^nu is treated as
# an independent positive symbol; the audit checks the algebraic factorization
# and the derivative lemma used to force a positive maximum onto x=y.
p = sp.symbols("p", positive=True)
symmetric_sum = 2 * (p - 1) / (p * t0 + 1) + (p**-2 - 1) / (t0**-2 * p**-2 + 1)
critical_polynomial = p**2 * t0**2 * (t0 - 2) + p * t0**2 * (t0 + 1) + t0**2 - 2
assert sp.factor(
    symmetric_sum
    + (p - 1) * critical_polynomial / ((p * t0 + 1) * (p**2 * t0**2 + 1))
) == 0
discriminant = sp.factor(sp.discriminant(critical_polynomial, p))
assert discriminant == t0**2 * (t0 - 1) * (t0**3 - t0**2 + 8 * t0 + 16)

X = sp.symbols("X", positive=True)
h = X * (nu + (nu + 1) * t0 - X) / (t0 * (X + 1) ** 2)
h_prime = sp.factor(sp.diff(h, t0) + sp.diff(h, X) * (nu + 1) * X / t0)
B = sp.factor(-h_prime * t0**2 * (X + 1) ** 3 / X)
C = nu + (nu + 1) * t0
assert sp.factor(B.subs(X, 1)) == 4 * nu
assert sp.factor(B.subs(X, C)) == nu * (nu + 1) ** 2 * (t0 + 1) ** 2

phi2 = (x**2 - 1)/(x**3 + 1)
assert sp.simplify(phi2.subs(x, 2) - sp.Rational(1,3)) == 0
assert sp.simplify(sp.diff(phi2, x).subs(x,2)) == 0
assert sp.simplify(sp.diff(phi2, x, 2).subs(x,2) + sp.Rational(2,9)) == 0

# Critical-sphere expansion through quartic order.
h=sp.symbols('h')
y1,y2,y3=sp.symbols('y1 y2 y3')
ys=(y1,y2,y3);eps=h**2
f2=lambda z:(z**2-1)/(z**3+1)
coords=[eps,1/(eps*sp.prod(2+h*y for y in ys))]+[2+h*y for y in ys]
S=sp.series(sum(f2(z) for z in coords),h,0,5).removeO().expand()
c2=sp.factor(S.coeff(h,2));c3=sp.factor(S.coeff(h,3));c4=sp.factor(S.coeff(h,4))
assert sp.expand(c2 - (72-sum(y*y for y in ys))/9)==0
C3=sum(y**3+36*y for y in ys)
assert sp.expand(c3-C3/9)==0
Q=1+2*(y1*y2+y1*y3+y2*y3)-sp.Rational(2,27)*sum(y**4 for y in ys)
assert sp.expand(c4-Q)==0
print("CONTINUOUS ONSET, EXPONENT, AND CRITICAL-SPHERE SYMBOLIC AUDIT PASSED")
