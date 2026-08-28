#!/usr/bin/env python3
"""Symbolic audit for the reciprocal root-reflection single-crossing lemma."""
import sympy as sp

t, nu = sp.symbols('t nu', positive=True)
phi = (t**nu-1)/(t**(nu+1)+1)
B = sp.factor(t*phi/(t-1))
num, den = sp.together(sp.diff(B,t)).as_numer_denom()
expected = 1-t**(2*nu+2)+(nu+1)*t**nu*(t**2-1)
assert sp.simplify(num-expected)==0
assert sp.simplify(den-(t-1)**2*(t**(nu+1)+1)**2) == 0

a = sp.symbols('a', positive=True)
phia = (t**a-1)/(t**(a+1)+1)
h = sp.simplify(t*sp.diff(phia,t))
hrec = sp.simplify(h.subs(t,1/t))
assert sp.simplify(hrec - t*(h+phia)) == 0

print('VERIFIED: B_nu derivative numerator and differentiated reciprocity identity')
print('The strict sign uses sinh((nu+1)x)>(nu+1)sinh(x) for x>0, nu>0.')
