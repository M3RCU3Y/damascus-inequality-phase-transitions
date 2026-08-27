#!/usr/bin/env python3
from fractions import Fraction

q=Fraction(205,204)
weights=[10,15,40,115,1042]
above=[0,841,0,1601,241]
below=[395,0,912,0,391]


def phi(n,t):
    return (t**n-1)/(t**(n+1)+1)

def S(n):
    ans=Fraction(0)
    for w,a,b in zip(weights,above,below):
        t=q**w
        ans += a*phi(n,t)+b*phi(n,1/t)
    return ans

moment=sum((a-b)*w for w,a,b in zip(weights,above,below))
assert moment==0
checks=[(2,-1),(3,1),(10,1),(11,-1),(31,-1),(32,1),(113,1),(114,-1)]
for n,sgn in checks:
    v=S(n)
    assert (v>0)-(v<0)==sgn,(n,v)
    print(n, '+' if v>0 else '-', float(v))
print('PRODUCT MOMENT VERIFIED:',moment)
print('FIVE-RADIUS FOUR-CHANGE WITNESS VERIFIED')
