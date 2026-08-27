#!/usr/bin/env python3
"""Validated local Krawczyk certificate for the symmetric 2+2 fold.

Family: X=(e^c,e^c,e^{-c+e},e^{-c-e}).
F(nu,c,e)=S_nu^4(X).
Fold equations:
  F=0,
  F_nu=0,
  F_{nu c} F_e - F_{nu e} F_c=0.

All proof decisions use outward-rounded Decimal interval arithmetic and
third-order forward automatic differentiation. The centre is only a seed.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
import mpmath as mp

PREC=85; GUARD=25
getcontext().prec=PREC
CUSH=Decimal(10) ** Decimal(-(PREC-8))
NVAR=3

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(str(lo))
        self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(str(hi)))
        if self.lo>self.hi: raise ValueError
    def __add__(self,o):
        o=ii(o)
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_FLOOR; lo=self.lo+o.lo
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING; hi=self.hi+o.hi
        return I(lo,hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-ii(o))
    def __rsub__(self,o): return ii(o)-self
    def __mul__(self,o):
        o=ii(o)
        with localcontext() as c:
            c.prec=PREC+GUARD
            z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_FLOOR; lo=+min(z)
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING; hi=+max(z)
        return I(lo,hi)
    __rmul__=__mul__
    def rec(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_FLOOR; a=Decimal(1)/self.hi
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING; b=Decimal(1)/self.lo
        return I(min(a,b),max(a,b))
    def __truediv__(self,o): return self*ii(o).rec()
    def __rtruediv__(self,o): return ii(o)*self.rec()
    def powi(self,n):
        if n==0:return I(1)
        if n<0:return self.powi(-n).rec()
        out=I(1); base=self; k=n
        while k:
            if k&1: out=out*base
            base=base*base;k//=2
        return out
    def exp(self):
        with localcontext() as c:
            c.prec=PREC+GUARD
            a=self.lo.exp();b=self.hi.exp()
            ea=(abs(a)+1)*CUSH; eb=(abs(b)+1)*CUSH
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_FLOOR; lo=+(a-ea)
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING; hi=+(b+eb)
        return I(lo,hi)
    def inside(self,o): return self.lo>o.lo and self.hi<o.hi
    def __repr__(self): return f'[{self.lo},{self.hi}]'
def ii(x): return x if isinstance(x,I) else I(x)

Z=lambda:[I(0) for _ in range(NVAR)]
ZM=lambda:[[I(0) for _ in range(NVAR)] for __ in range(NVAR)]
ZT=lambda:[[[I(0) for _ in range(NVAR)] for __ in range(NVAR)] for ___ in range(NVAR)]

class J3:
    __slots__=('v','d','h','t')
    def __init__(self,v,d=None,h=None,t=None): self.v=ii(v);self.d=d or Z();self.h=h or ZM();self.t=t or ZT()
    @staticmethod
    def var(v,k):
        d=Z();d[k]=I(1);return J3(v,d)
    def __add__(self,o):
        o=jj(o)
        return J3(self.v+o.v,[self.d[i]+o.d[i] for i in range(NVAR)],
          [[self.h[i][j]+o.h[i][j] for j in range(NVAR)] for i in range(NVAR)],
          [[[self.t[i][j][k]+o.t[i][j][k] for k in range(NVAR)] for j in range(NVAR)] for i in range(NVAR)])
    __radd__=__add__
    def __neg__(self): return self*(-1)
    def __sub__(self,o): return self+(-jj(o))
    def __rsub__(self,o): return jj(o)-self
    def __mul__(self,o):
        o=jj(o); a=self;b=o
        d=[a.d[i]*b.v+a.v*b.d[i] for i in range(NVAR)]
        h=[[a.h[i][j]*b.v+a.d[i]*b.d[j]+a.d[j]*b.d[i]+a.v*b.h[i][j] for j in range(NVAR)] for i in range(NVAR)]
        t=ZT()
        for i in range(NVAR):
          for j in range(NVAR):
            for k in range(NVAR):
              t[i][j][k]=(a.t[i][j][k]*b.v+a.h[i][j]*b.d[k]+a.h[i][k]*b.d[j]+a.h[j][k]*b.d[i]
                +a.d[i]*b.h[j][k]+a.d[j]*b.h[i][k]+a.d[k]*b.h[i][j]+a.v*b.t[i][j][k])
        return J3(a.v*b.v,d,h,t)
    __rmul__=__mul__
    def unary(self,f0,f1,f2,f3):
        a=self; d=[f1*a.d[i] for i in range(NVAR)]
        h=[[f2*a.d[i]*a.d[j]+f1*a.h[i][j] for j in range(NVAR)] for i in range(NVAR)]
        t=ZT()
        for i in range(NVAR):
          for j in range(NVAR):
            for k in range(NVAR):
              t[i][j][k]=(f3*a.d[i]*a.d[j]*a.d[k]+f2*(a.h[i][j]*a.d[k]+a.h[i][k]*a.d[j]+a.h[j][k]*a.d[i])+f1*a.t[i][j][k])
        return J3(f0,d,h,t)
    def exp(self):
        z=self.v.exp();return self.unary(z,z,z,z)
    def rec(self):
        x=self.v; f0=x.rec();f1=-(x.powi(-2));f2=I(2)*x.powi(-3);f3=I(-6)*x.powi(-4)
        return self.unary(f0,f1,f2,f3)
    def __truediv__(self,o): return self*jj(o).rec()
    def __rtruediv__(self,o): return jj(o)*self.rec()
def jj(x): return x if isinstance(x,J3) else J3(x)

def phi(nu,u): return ((nu*u).exp()-1)/(((nu+1)*u).exp()+1)
def build(box):
    n=J3.var(box[0],0); c=J3.var(box[1],1); e=J3.var(box[2],2)
    return 2*phi(n,c)+phi(n,-c+e)+phi(n,-c-e)

def system_and_jac(box):
    f=build(box)
    g=[f.v,f.d[0],f.h[0][1]*f.d[2]-f.h[0][2]*f.d[1]]
    J=[f.d[:],f.h[0][:],[]]
    for j in range(3):
        J[2].append(f.t[0][1][j]*f.d[2]+f.h[0][1]*f.h[2][j]-f.t[0][2][j]*f.d[1]-f.h[0][2]*f.h[1][j])
    return f,g,J

CENTER=[Decimal('7.35963189610934942971319002231776493349397178104972564388319'),
Decimal('0.537880362360812249794743814014949315125222090806407365090299'),
Decimal('0.501899867001789135999234747246328698672819506700907926112985')]
RAD=Decimal('1e-20')
BOX=[I(x-RAD,x+RAD) for x in CENTER]; POINT=[I(x) for x in CENTER]

def inverse_point(Jp):
    mp.mp.dps=100
    M=mp.matrix([[mp.mpf(str(Jp[i][j].lo)) for j in range(3)] for i in range(3)])
    C=M**-1
    return [[Decimal(mp.nstr(C[i,j],95)) for j in range(3)] for i in range(3)]
def pim(A,B):
    return [[sum((I(A[i][k])*B[k][j] for k in range(3)),I(0)) for j in range(3)] for i in range(3)]
def piv(a,v): return sum((I(x)*y for x,y in zip(a,v)),I(0))

def main():
    fp,gp,Jp=system_and_jac(POINT); fx,gx,Jx=system_and_jac(BOX)
    C=inverse_point(Jp)
    CJ=pim(C,Jx); R=[[I(1 if i==j else 0)-CJ[i][j] for j in range(3)] for i in range(3)]
    delta=[I(-RAD,RAD) for _ in range(3)]
    K=[]
    for i in range(3):
        k=I(CENTER[i])-piv(C[i],gp)+sum((R[i][j]*delta[j] for j in range(3)),I(0));K.append(k)
    print('SYMMETRIC FOLD KRAWCZYK CERTIFICATE')
    for name,b,k in zip(('nu','c','e'),BOX,K): print(name,'box',b);print(name,'K  ',k);assert k.inside(b)
    print('unique zero certified')
    fnn=fx.h[0][0]
    ep=-fx.d[1]/fx.d[2]
    e2=-(fx.h[1][1]+I(2)*fx.h[1][2]*ep+fx.h[2][2]*ep*ep)/fx.d[2]
    curv=fx.t[0][1][1]+I(2)*fx.t[0][1][2]*ep+fx.t[0][2][2]*ep*ep+fx.h[0][2]*e2
    print('F_nunu',fnn);print('constrained curvature',curv)
    assert fnn.hi<0 and curv.lo>0
    mp.mp.dps=60;n=mp.mpf(str(CENTER[0]));c=mp.mpf(str(CENTER[1]));e=mp.mpf(str(CENTER[2]))
    t=mp.exp(c);r=mp.exp(-c+e);a=mp.exp(-c-e);q=r**n
    print('nu',mp.nstr(n,40));print('t',mp.nstr(t,40));print('r',mp.nstr(r,40));print('a',mp.nstr(a,40));print('q',mp.nstr(q,40));print('PASSED')
if __name__=='__main__':main()
