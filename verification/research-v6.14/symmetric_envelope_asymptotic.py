#!/usr/bin/env python3
"""Validated onset nondegeneracy and the symmetric-envelope 1/mu constant."""
from decimal import Decimal
import mpmath as mp
from symmetric_fold_certificate import I,J3,phi,PREC

CENTER_N=Decimal('3.9826231561383400589629765329692411799980087017884810633028761081411343877625327')
CENTER_C=Decimal('0.42889977585091112885849194819279415225079795809559701667185208934549625774661596')
RAD=Decimal('1e-20')

def build(box):
    n=J3.var(box[0],0); c=J3.var(box[1],1)
    return 2*phi(n,c)+phi(n,-2*c)

def inv2(J):
    a,b=J[0];c,d=J[1];det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]
def dot(row,v):
    return sum((row[i]*v[i] for i in range(2)),I(0))

def lnI(x):
    from decimal import localcontext,ROUND_FLOOR,ROUND_CEILING
    if x.lo<=0: raise ValueError
    cushion=Decimal(10) ** Decimal(-(PREC-8))
    with localcontext() as c:
        c.prec=PREC+20;a=x.lo.ln();b=x.hi.ln();ea=(abs(a)+1)*cushion;eb=(abs(b)+1)*cushion
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
    return I(lo,hi)

def hI(n,u):
    n=n if isinstance(n,I) else n.v; u=u if isinstance(u,I) else u.v
    eu=u.exp(); en=(n*u).exp(); en1=((n+1)*u).exp()
    return en*(n+(n+1)*eu-en1)/(1+en1).powi(2)

def main():
    B=[I(CENTER_N-RAD,CENTER_N+RAD),I(CENTER_C-RAD,CENTER_C+RAD)]
    P=[I(CENTER_N),I(CENTER_C)]
    fp=build(P); fx=build(B)
    gp=[fp.v,fp.d[1]]
    Jp=[[fp.d[0],fp.d[1]],[fp.h[1][0],fp.h[1][1]]]
    # point inverse represented by midpoint decimals (interval points)
    a,b=Jp[0][0].lo,Jp[0][1].lo;c,d=Jp[1][0].lo,Jp[1][1].lo;det=a*d-b*c
    C=[[I(d/det),I(-b/det)],[I(-c/det),I(a/det)]]
    Jx=[[fx.d[0],fx.d[1]],[fx.h[1][0],fx.h[1][1]]]
    CJ=[[sum((C[i][k]*Jx[k][j] for k in range(2)),I(0)) for j in range(2)] for i in range(2)]
    R=[[I(1 if i==j else 0)-CJ[i][j] for j in range(2)] for i in range(2)]
    delta=[I(-RAD,RAD),I(-RAD,RAD)]
    K=[]
    centers=[CENTER_N,CENTER_C]
    for i in range(2):
        K.append(I(centers[i])-dot(C[i],gp)+sum((R[i][j]*delta[j] for j in range(2)),I(0)))
    print('THREE-VARIABLE ONSET KRAWCZYK CERTIFICATE')
    for nm,bx,k in zip(('nu_c','c_c'),B,K): print(nm,'box',bx);print(nm,'K  ',k);assert k.inside(bx)
    print('F_nu',fx.d[0]);print('F_cc',fx.h[1][1]);assert fx.d[0].lo>0 and fx.h[1][1].hi<0
    n=J3.var(B[0],0); c=J3.var(B[1],1)
    t=c.exp(); q=t-1; z=(-2*c).exp()
    Bcoef=lnI(q.v)*(n.v/I(2)-hI(n.v,(-2*c).v))
    Ccoef=-Bcoef/fx.d[0]
    print('q0=t_c-1',q.v)
    print('source epsilon coefficient B',Bcoef)
    print('C=-B/F_nu',Ccoef)
    target=Decimal('11.8487685043754056738569263898805')
    assert Ccoef.lo < target < Ccoef.hi
    mp.mp.dps=50
    print('descriptive t_c=',mp.nstr(mp.e**mp.mpf(str(CENTER_C)),40))
    print('PASSED')
if __name__=='__main__':main()
