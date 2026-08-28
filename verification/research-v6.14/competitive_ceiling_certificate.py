#!/usr/bin/env python3
"""Validated rational competitor giving a target ceiling below 9.62."""
from decimal import Decimal
import sys
sys.path.insert(0,'/mnt/data/paper2_work/research-v6.14')
import fixed_slice_zero_width_certificate as B
import symmetric_fold_certificate as SF

C=B.I(Decimal('0.52962'))
E=B.I(Decimal('0.49522'))

def phi(A,U):
    return ((A*U).exp()-1)/(((A+B.I(1))*U).exp()+1)

def S(A):
    return B.I(2)*phi(A,C)+phi(A,-C+E)+phi(A,-C-E)

A6=B.I(Decimal('6'))
Ad=B.I(SF.CENTER[0]-SF.RAD,SF.CENTER[0]+SF.RAD)
A962=B.I(Decimal('9.62'))

s6=S(A6); sd=S(Ad); s962=S(A962)
assert s6.lo>0, s6
assert sd.lo>0, sd
assert s962.hi<0, s962
print('COMPETITIVE CEILING CERTIFICATE')
print('S_6       =',s6)
print('S_nud     =',sd)
print('S_9.62    =',s962)
print('VERIFIED: the same strict 2+2 point is positive at 6 and nu_dagger, and negative at 9.62')
