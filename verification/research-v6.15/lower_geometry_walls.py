#!/usr/bin/env python3
"""Exact/validated geometry walls for lower-middle source packets.

Uses the proved n=6 three-variable topology theorem plus exact rational
certificates to establish, for any coordinate-1 trace positive at an exponent
nu<=6:

    57/50 < t < 39/20,
    u < 1/4,
    min(x,y) > 28/25.

It also validates the continuous upper-pair curvature sign needed on source
boundaries:

    x h'_nu(x) + y h'_nu(y) < 0

for nu_c <= nu <= 6, 1<=y<=x, xy<=4.

All Bernstein decisions are exact rationals.  The curvature decision uses
outward-rounded Decimal intervals.
"""
from __future__ import annotations

from collections import deque
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction
from math import comb
import sympy as sp

NU_C=Decimal('3.9826231561383400589629765329')
PREC=78; GUARD=24
getcontext().prec=PREC
CUSH=Decimal(10) ** Decimal(-(PREC-8))

# ---------- exact exponent-six geometry ----------
t=sp.symbols('t')
P6=t**10-2*t**9-t**8+3*t**7-t**6-3*t**5+3*t**4+2*t**3-3*t**2+2


def bernstein_1d(poly,var,a,b):
    n=sp.degree(poly,var); s=sp.symbols('s')
    q=sp.Poly(sp.expand(poly.subs(var,a+(b-a)*s)),s,domain=sp.QQ)
    c=[sp.Rational(q.nth(i)) for i in range(n+1)]
    return [sp.simplify(sum(c[i]*sp.Rational(comb(k,i),comb(n,i)) for i in range(k+1))) for k in range(n+1)]

# u=1/4 trace factor.
P20=(2458*t**20-7848*t**19+8858*t**18-5928*t**17+6998*t**16
     -10944*t**15+8710*t**14-864*t**13-2976*t**12+864*t**11
     +2976*t**10-864*t**9-2157*t**8+4788*t**7+1414*t**6
     -3804*t**5+3836*t**4-156*t**3+5954*t**2-7884*t+6553)

# Direct three-variable exponent-six numerator for the y-wall.
x,y,w,s=sp.symbols('x y w s')
def phi6(z):return (z**6-1)/(z**7+1)
S6=sp.together(phi6(x)+phi6(y)-x*y*phi6(x*y))
NUM6,_=sp.fraction(S6)
Y=1+sp.Rational(3,25)*s
X=(Y**2+w*(4-Y**2))/Y
wall_expr=sp.together(NUM6.subs({x:X,y:Y}))
wall_num,_=sp.fraction(wall_expr)
WALL=sp.Poly(-sp.expand(wall_num),s,w,domain=sp.QQ)


def power_to_bernstein_2d(poly):
    ds,dw=poly.degree(s),poly.degree(w)
    c=[[Fraction(0) for _ in range(dw+1)] for __ in range(ds+1)]
    for (i,j),coef in poly.terms():
        c[i][j]=Fraction(int(coef.p),int(coef.q))
    B=[[Fraction(0) for _ in range(dw+1)] for __ in range(ds+1)]
    for k in range(ds+1):
        for ell in range(dw+1):
            total=Fraction(0)
            for i in range(k+1):
                fi=Fraction(comb(k,i),comb(ds,i))
                for j in range(ell+1):
                    if c[i][j]:
                        total += c[i][j]*fi*Fraction(comb(ell,j),comb(dw,j))
            B[k][ell]=total
    return B


def split_1d(vals):
    vals=list(vals); left=[vals[0]]; right=[vals[-1]]; cur=vals
    while len(cur)>1:
        cur=[(cur[i]+cur[i+1])/2 for i in range(len(cur)-1)]
        left.append(cur[0]);right.append(cur[-1])
    return left,right[::-1]


def split_axis(B,axis):
    n=len(B)-1;m=len(B[0])-1
    L=[[Fraction(0) for _ in range(m+1)] for __ in range(n+1)]
    R=[[Fraction(0) for _ in range(m+1)] for __ in range(n+1)]
    if axis==0:
        for j in range(m+1):
            l,r=split_1d([B[i][j] for i in range(n+1)])
            for i in range(n+1):L[i][j]=l[i];R[i][j]=r[i]
    else:
        for i in range(n+1):
            l,r=split_1d(B[i]);L[i]=l;R[i]=r
    return L,R


def certify_wall_bernstein():
    root=power_to_bernstein_2d(WALL)
    q=deque([(root,0)]);nodes=leaves=maxdepth=0
    while q:
        B,d=q.popleft();nodes+=1
        if min(z for row in B for z in row)>=0:
            leaves+=1;maxdepth=max(maxdepth,d);continue
        if d>=20:raise AssertionError('y-wall Bernstein tree failed')
        L,R=split_axis(B,d%2);q.append((L,d+1));q.append((R,d+1))
    return nodes,leaves,maxdepth

# ---------- outward-rounded continuous source curvature ----------
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(str(lo)); self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(str(hi)))
        if self.lo>self.hi:raise ValueError
    def __add__(self,o):
        o=ii(o)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=self.lo+o.lo
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=self.hi+o.hi
        return I(lo,hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-ii(o))
    def __rsub__(self,o):return ii(o)-self
    def __mul__(self,o):
        o=ii(o)
        with localcontext() as c:c.prec=PREC+GUARD;z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+min(z)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+max(z)
        return I(lo,hi)
    __rmul__=__mul__
    def rec(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;a=Decimal(1)/self.hi
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;b=Decimal(1)/self.lo
        return I(min(a,b),max(a,b))
    def __truediv__(self,o):return self*ii(o).rec()
    def __rtruediv__(self,o):return ii(o)*self.rec()
    def exp(self):
        with localcontext() as c:
            c.prec=PREC+GUARD;a=self.lo.exp();b=self.hi.exp();ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
    def ln(self):
        if self.lo<=0:raise ValueError
        with localcontext() as c:
            c.prec=PREC+GUARD;a=self.lo.ln();b=self.hi.ln();ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
def ii(x):return x if isinstance(x,I) else I(x)


def hp(A,Z):
    L=Z.ln(); ap1=A+1; zp1=((A+1)*L).exp()
    P=(((2*A+2)*L).exp()-ap1*ap1*((A+2)*L).exp()
       -(A*A+4*A+1)*zp1+ap1*ap1*Z+A*A)
    return ((A-1)*L).exp()*P/((1+zp1)*(1+zp1)*(1+zp1))

def curvature_box(alo,ahi,ylo,yhi,wlo,whi):
    A=I(alo,ahi);Y=I(ylo,yhi);W=I(wlo,whi);X=Y+W*(I(4)/Y-Y)
    return X*hp(A,X)+Y*hp(A,Y)

def certify_curvature(box,depth=0,maxdepth=22,stats=None):
    alo,ahi,ylo,yhi,wlo,whi=box
    if stats is None:stats={'nodes':0,'leaves':0,'depth':0,'worst':Decimal('-1e100')}
    stats['nodes']+=1;v=curvature_box(*box)
    if v.hi<0:
        stats['leaves']+=1;stats['depth']=max(stats['depth'],depth);stats['worst']=max(stats['worst'],v.hi);return stats
    if depth>=maxdepth:raise AssertionError(('curvature box failed',box,v))
    widths=[(ahi-alo)/(Decimal(6)-NU_C),yhi-ylo,whi-wlo];k=max(range(3),key=lambda i:widths[i])
    if k==0:
        m=(alo+ahi)/2;B1=(alo,m,ylo,yhi,wlo,whi);B2=(m,ahi,ylo,yhi,wlo,whi)
    elif k==1:
        m=(ylo+yhi)/2;B1=(alo,ahi,ylo,m,wlo,whi);B2=(alo,ahi,m,yhi,wlo,whi)
    else:
        m=(wlo+whi)/2;B1=(alo,ahi,ylo,yhi,wlo,m);B2=(alo,ahi,ylo,yhi,m,whi)
    certify_curvature(B1,depth+1,maxdepth,stats);certify_curvature(B2,depth+1,maxdepth,stats);return stats

if __name__=='__main__':
    print('LOWER-MIDDLE GEOMETRY WALL CERTIFICATES')
    # Exact location of the symmetric n=6 positive interval relative to rational walls.
    assert sp.count_roots(P6,sp.Rational(1),sp.Rational(3,2))==1
    assert sp.count_roots(P6,sp.Rational(3,2),sp.Rational(2))==1
    assert P6.subs(t,sp.Rational(57,50))>0
    assert P6.subs(t,sp.Rational(39,20))>0
    print('verified: positive n=6 trace implies 57/50 < t < 39/20')

    b1=bernstein_1d(P20,t,sp.Rational(1),sp.Rational(3,2))
    b2=bernstein_1d(P20,t,sp.Rational(3,2),sp.Rational(2))
    assert min(b1)>0 and min(b2)>0
    print('u=1/4 P20 Bernstein minima:',min(b1),min(b2))
    print('verified: positive n=6 trace implies u<1/4')

    nodes,leaves,dep=certify_wall_bernstein()
    print('y<=28/25 exact Bernstein tree:',nodes,leaves,dep)
    assert nodes==21
    print('verified: positive n=6 trace implies min(x,y)>28/25')

    stats=certify_curvature((NU_C,Decimal(6),Decimal(1),Decimal(2),Decimal(0),Decimal(1)))
    print('continuous source-curvature boxes:',stats)
    assert stats['worst']<0
    print('VERIFIED: x h_nu_prime(x)+y h_nu_prime(y)<0 for nu_c<=nu<=6, xy<=4')
    print('PASSED')
