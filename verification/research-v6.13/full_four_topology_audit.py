#!/usr/bin/env python3
"""Exact symbolic/Sturm audit for the full four-variable 3+1 core topology theorem."""
import sympy as sp

nu, t, p, X = sp.symbols('nu t p X', positive=True)

# Symmetric spine: (t,t,t,t^-3), with p=t^(nu+1).
phi_t = (p/t - 1)/(p + 1)
phi_z = ((t/p)**3 - 1)/(p**-3 + 1)
Ssym = sp.factor(3*phi_t + phi_z)
Q = (t-3)*p**2 + (t**2+3)*p + t**3 - 3
expected = sp.factor((t-p)*Q/(t*(p+1)*(p**2-p+1)))
assert sp.factor(Ssym-expected) == 0

# h_nu(t)=t phi_nu'(t), expressed with X=t^(nu+1).
C = nu + (nu+1)*t
h = X*(C-X)/(t*(X+1)**2)
hp = sp.factor(sp.diff(h,t) + sp.diff(h,X)*(nu+1)*X/t)
B = sp.factor(-hp*t**2*(X+1)**3/X)
assert sp.Poly(B,X).degree() == 2
assert sp.Poly(B,X).LC() == -1
assert sp.factor(B.subs(X,1)) == 4*nu
assert sp.factor(B.subs(X,C)) == nu*(nu+1)**2*(t+1)**2

# Uniqueness of the continuous 3+1 onset.
Qt, Qp = sp.diff(Q,t), sp.diff(Q,p)
g = sp.factor(-t*Qt/(p*Qp))
gp = sp.factor(sp.diff(g,t) + sp.diff(g,p)*(-Qt/Qp))
N = sp.factor(sp.together(gp)).as_numer_denom()[0]
R = sp.factor(sp.resultant(Q,N,p))
H = sp.factor(R/(81*(t-3)))
H_expected = (
    t**16 - 12*t**14 - 244*t**12 - 96*t**11 + 5436*t**10
    - 15456*t**9 + 28990*t**8 - 20160*t**7 + 34092*t**6
    - 88512*t**5 + 29916*t**4 + 23328*t**3 + 3492*t**2
    + 2592*t + 729
)
assert sp.expand(H-H_expected) == 0
Hpoly = sp.Poly(H,t,domain=sp.QQ)
assert sp.count_roots(Hpoly, sp.Rational(1), sp.Rational(3)) == 2

I1 = (sp.Rational(10984,10000), sp.Rational(10985,10000))
I2 = (sp.Rational(13623,10000), sp.Rational(13624,10000))
assert sp.count_roots(Hpoly,*I1) == 1
assert sp.count_roots(Hpoly,*I2) == 1

subs = sp.subresultants(Q,N,p)
L = sp.factor(subs[-2]/(-9*(t-3)))
Lp = sp.Poly(L,p)
assert Lp.degree() == 1
A = sp.factor(Lp.coeff_monomial(p))
D = sp.factor(Lp.coeff_monomial(1))
pcrit = sp.factor(-D/A)
num_pm1, den_pm1 = map(sp.factor, sp.together(pcrit-1).as_numer_denom())
for interval, wanted in ((I1,-1),(I2,1)):
    a,b = interval
    for poly in (sp.Poly(num_pm1,t), sp.Poly(den_pm1,t), sp.Poly(A,t)):
        assert sp.count_roots(poly,a,b) == 0
    sgn = sp.sign(num_pm1.subs(t,a))*sp.sign(den_pm1.subs(t,a))
    assert int(sgn) == wanted

# Exact upper bound nu_31<2.
assert sp.expand(Q.subs({t:2,p:8})) == -3

# Boundary transversality identities.
y = sp.symbols('y', positive=True)
phiy = (y**nu-1)/(y**(nu+1)+1)
hy = sp.factor(y*sp.diff(phiy,y))
assert sp.simplify(hy.subs(y,1) - nu/2) == 0
z0 = sp.symbols('z0', positive=True)
phi_z0 = (z0**nu-1)/(z0**(nu+1)+1)
dface0 = sp.factor(-nu/2 + z0*sp.diff(phi_z0,z0))
assert sp.simplify(dface0 - (-nu/2 + hy.subs(y,z0))) == 0
expr = sp.factor(-y*phiy)
assert sp.limit(expr/y, y, 0, dir='+') == 1

# All-one quadratic expansion.
u = sp.symbols('u')
gphi=(sp.exp(nu*u)-1)/(sp.exp((nu+1)*u)+1)
ser=sp.series(gphi,u,0,3).removeO().expand()
assert sp.simplify(ser.coeff(u,1)-nu/2)==0
assert sp.simplify(ser.coeff(u,2)+nu/4)==0

# Numerical replay only.
import mpmath as mp
mp.mp.dps = 40
def pplus(tv):
    a=tv-3; b=tv*tv+3; c=tv**3-3
    disc=b*b-4*a*c
    return (-b-mp.sqrt(disc))/(2*a)
def eta(tv):
    return mp.log(pplus(tv))/mp.log(tv)-1
root = mp.findroot(lambda q: mp.diff(eta,q), (mp.mpf('1.8'),mp.mpf('2.0')))
val = eta(root)
assert mp.mpf('1.89') < root < mp.mpf('1.91')
assert mp.mpf('1.92') < val < mp.mpf('1.94')

print('FULL FOUR-VARIABLE 3+1 TOPOLOGY ALGEBRA AUDIT PASSED')
print('unique onset t =', mp.nstr(root,30))
print('unique onset nu =', mp.nstr(val,30))
print('Sturm roots of g-prime resultant in (1,3): 2; exactly one lies on P_+>1')
