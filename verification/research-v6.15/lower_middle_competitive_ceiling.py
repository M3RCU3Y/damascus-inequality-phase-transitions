#!/usr/bin/env python3
"""Validated rational competitor giving a uniform target ceiling below 200.

Scope: 4.05 <= source exponent <= 6.
"""
from decimal import Decimal
import fixed_slice_zero_width_certificate as B

C = B.I(Decimal('0.43545'))
E = B.I(Decimal('0.43231'))


def phi(A, U):
    return ((A * U).exp() - 1) / (((A + B.I(1)) * U).exp() + 1)


def S(A):
    return B.I(2) * phi(A, C) + phi(A, -C + E) + phi(A, -C - E)


A405 = B.I(Decimal('4.05'))
A6 = B.I(Decimal('6'))
A200 = B.I(Decimal('200'))

s405 = S(A405)
s6 = S(A6)
s200 = S(A200)

assert s405.lo > 0, s405
assert s6.lo > 0, s6
assert s200.hi < 0, s200

print('LOWER-MIDDLE COMPETITIVE CEILING CERTIFICATE')
print('geometry: c=0.43545, d=0, e=0.43231')
print('S_4.05 =', s405)
print('S_6    =', s6)
print('S_200  =', s200)
print('VERIFIED: the point is positive at 4.05 and 6, and negative at 200')
print('ANALYTIC INPUT: the V6.14 single-transient theorem makes its positivity set one interval')
print('CONSEQUENCE: every source 4.05 <= nu <= 6 has a failure by target 200, hence its earliest exit is < 200')
