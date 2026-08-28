#!/usr/bin/env python3
"""Exact algebra audit for the continuous four-variable 2+2 onset theorem."""
import sympy as sp

x, n = sp.symbols('x n', positive=True)
phi = (x**n - 1)/(x**(n+1)+1)
h = sp.factor(x*sp.diff(phi, x))
expected_h = x**n*(n+(n+1)*x-x**(n+1))/(1+x**(n+1))**2
assert sp.simplify(h-expected_h) == 0

P = (x**(2*n+2)
     -(n+1)**2*x**(n+2)
     -(n**2+4*n+1)*x**(n+1)
     +(n+1)**2*x+n**2)
expected_hp = x**(n-1)*P/(1+x**(n+1))**3
assert sp.simplify(sp.diff(h, x)-expected_hp) == 0
assert sp.expand(P.subs(x,1)) == -4*n

# Reciprocal derivative identity h(1/x)=x(h(x)+phi(x)).
y = sp.symbols('y', positive=True)
phi_y = (y**n-1)/(y**(n+1)+1)
h_y = sp.factor(y*sp.diff(phi_y,y))
recip = sp.simplify(h_y.subs(y,1/x) - x*(h+phi))
assert recip == 0

# Exact escape bound phi_4(t)<1/2 for every t>1.
t = sp.symbols('t', positive=True)
f = t**5-2*t**4+3
assert sp.factor(sp.diff(f,t)) == t**3*(5*t-8)
assert sp.simplify(f.subs(t,sp.Rational(8,5))) == sp.Rational(1183,3125)

print('CONTINUOUS FOUR-VARIABLE ONSET ALGEBRA AUDIT PASSED')
print('h derivative numerator verified')
print('P_nu(1) = -4 nu verified')
print('h_nu(1/t) = t(h_nu(t)+phi_nu(t)) verified')
print('phi_4(t) < 1/2 escape bound: minimum numerator = 1183/3125')
print('NOTE: generalized Descartes for real powers and the maximum argument are analytic.')
