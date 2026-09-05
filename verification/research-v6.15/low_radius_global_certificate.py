#!/usr/bin/env python3
"""Validated global low-radius exclusion ingredients for V6.15.

This certificate proves two sign inputs on the full continuous middle strip:

1. h'_alpha(z)<0 for nu_c <= alpha <= nu_dagger and
   1 <= z <= (1+4/nu_c^2)^2.
2. For 0<y<1, with t=1+y^2,
      Q(t,exp(2y))>0,
   where Q(t,p)=t^2((t-2)p^2+(t+1)p+1)-2.
   This is proved from Q(0)=Q'(0)=0 and validated Q''>0.

All proof decisions use outward-rounded Decimal interval arithmetic.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext

PREC=80
GUARD=25
getcontext().prec=PREC
CUSH=Decimal(10) ** Decimal(-(PREC-8))

NU_C=Decimal('3.9826231561383400589629765329')
NU_D=Decimal('7.3596318961093494297131900224')

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(str(lo))
        self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(str(hi)))
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
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
        with localcontext() as c:
            c.prec=PREC+GUARD
            z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+min(z)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+max(z)
        return I(lo,hi)
    __rmul__=__mul__
    def rec(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError(self)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;a=Decimal(1)/self.hi
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;b=Decimal(1)/self.lo
        return I(min(a,b),max(a,b))
    def __truediv__(self,o):return self*ii(o).rec()
    def __rtruediv__(self,o):return ii(o)*self.rec()
    def exp(self):
        with localcontext() as c:
            c.prec=PREC+GUARD
            a=self.lo.exp();b=self.hi.exp()
            ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
    def ln(self):
        if self.lo<=0:raise ValueError(self)
        with localcontext() as c:
            c.prec=PREC+GUARD
            a=self.lo.ln();b=self.hi.ln()
            ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
    def __repr__(self):return f'[{self.lo},{self.hi}]'

def ii(x):return x if isinstance(x,I) else I(x)

def ipow(x,n):
    out=I(1)
    for _ in range(n):out=out*x
    return out

def P_box(alo,ahi,zlo,zhi):
    A=I(alo,ahi); Z=I(zlo,zhi); L=Z.ln()
    ap1=A+1
    return (((2*A+2)*L).exp()
            -ap1*ap1*((A+2)*L).exp()
            -(A*A+4*A+1)*((A+1)*L).exp()
            +ap1*ap1*Z+A*A)

def certify_P(alo,ahi,zlo,zhi,depth=0,maxdepth=24,stats=None):
    if stats is None:stats={'nodes':0,'leaves':0,'depth':0,'worst':Decimal('-1e100')}
    stats['nodes']+=1
    v=P_box(alo,ahi,zlo,zhi)
    if v.hi<0:
        stats['leaves']+=1;stats['depth']=max(stats['depth'],depth);stats['worst']=max(stats['worst'],v.hi)
        return
    if depth>=maxdepth:raise AssertionError(('P box failed',alo,ahi,zlo,zhi,v))
    aw=(ahi-alo)/(NU_D-NU_C)
    zw=(zhi-zlo)/(ZMAX-Decimal(1))
    if aw>=zw:
        m=(alo+ahi)/2
        certify_P(alo,m,zlo,zhi,depth+1,maxdepth,stats)
        certify_P(m,ahi,zlo,zhi,depth+1,maxdepth,stats)
    else:
        m=(zlo+zhi)/2
        certify_P(alo,ahi,zlo,m,depth+1,maxdepth,stats)
        certify_P(alo,ahi,m,zhi,depth+1,maxdepth,stats)
    return stats

def qsecond_box(lo,hi):
    Y=I(lo,hi); E2=(2*Y).exp(); E4=(4*Y).exp()
    y2=Y*Y;y3=y2*Y;y4=y3*Y;y5=y4*Y;y6=y5*Y
    inner=(8*y6*E4+2*y6*E2+24*y5*E4+12*y5*E2
           +23*y4*E4+23*y4*E2+16*y3*E4+32*y3*E2
           -2*y2*E4+34*y2*E2+6*y2-8*Y*E4+20*Y*E2
           -9*E4+9*E2+2)
    return 2*inner

def certify_qsecond(lo,hi,depth=0,maxdepth=20,stats=None):
    if stats is None:stats={'nodes':0,'leaves':0,'depth':0,'worst':Decimal('1e100')}
    stats['nodes']+=1
    v=qsecond_box(lo,hi)
    if v.lo>0:
        stats['leaves']+=1;stats['depth']=max(stats['depth'],depth);stats['worst']=min(stats['worst'],v.lo)
        return
    if depth>=maxdepth:raise AssertionError(('Qsecond box failed',lo,hi,v))
    m=(lo+hi)/2
    certify_qsecond(lo,m,depth+1,maxdepth,stats)
    certify_qsecond(m,hi,depth+1,maxdepth,stats)
    return stats

TMAX=I(1)+I(4)/(I(NU_C)*I(NU_C))
ZMAX=(TMAX*TMAX).hi

if __name__=='__main__':
    print('V6.15 GLOBAL LOW-RADIUS CERTIFICATE')
    s1={'nodes':0,'leaves':0,'depth':0,'worst':Decimal('-1e100')}
    certify_P(NU_C,NU_D,Decimal(1),ZMAX,stats=s1)
    print('h-prime numerator boxes:',s1)
    assert s1['worst']<0

    s2={'nodes':0,'leaves':0,'depth':0,'worst':Decimal('1e100')}
    certify_qsecond(Decimal(0),Decimal(1),stats=s2)
    print('Q-second boxes:',s2)
    assert s2['worst']>0

    print('ZMAX =',ZMAX)
    print('VERIFIED: P_alpha(z)<0 on the universal low-radius box')
    print('VERIFIED: d^2/dy^2 Q(1+y^2, exp(2y))>0 on [0,1]')
    print('PASSED')
