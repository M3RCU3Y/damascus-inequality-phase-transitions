#!/usr/bin/env python3
"""High-precision sanity check for the high-exponent zero-width theorem."""
from decimal import Decimal, localcontext

P=90

def power(x,a):
    with localcontext() as c:
        c.prec=P
        return (a*x.ln()).exp()

def phi(a,x):
    xa=power(x,a)
    return (xa-1)/(xa*x+1)

def dphi_da(a,x):
    xa=power(x,a)
    return x.ln()*xa*(1+x)/(1+xa*x)**2

def point(mu,q,t):
    r=power(q,Decimal(1)/mu)
    a=Decimal(1)/(r*t*t)
    return a,r,t,t

def S(alpha,X):
    return sum(phi(alpha,x) for x in X)

def Ftarget(mu,q,t):
    return S(mu,point(mu,q,t))

def bisect(mu,t):
    lo=Decimal('0.35');hi=Decimal('0.65')
    flo=Ftarget(mu,lo,t);fhi=Ftarget(mu,hi,t)
    assert flo<0<fhi,(mu,flo,fhi)
    for _ in range(260):
        mid=(lo+hi)/2;fm=Ftarget(mu,mid,t)
        if fm>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def main():
    with localcontext() as c:
        c.prec=P
        t=Decimal(3)/2;q0=Decimal(1)/2
        limit=2*q0*q0.ln()/(1+q0)**2
        print('limit mu*dS/dalpha =',limit)
        for m in [40,80,160,320]:
            mu=Decimal(m);q=bisect(mu,t);X=point(mu,q,t)
            deriv=sum(dphi_da(mu,x) for x in X)
            eps=Decimal('1e-8')
            src=S(mu-eps,X);tar=S(mu,X)
            assert abs(tar)<Decimal('1e-70')
            assert deriv<0 and src>0
            print(m,'q=',q,'mu*d=',mu*deriv,'source@mu-1e-8=',src)
        print('CONTINUOUS ZERO-WIDTH SANITY CHECK PASSED')

if __name__=='__main__':main()
