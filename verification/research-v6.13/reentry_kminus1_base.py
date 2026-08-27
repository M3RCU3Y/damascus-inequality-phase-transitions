#!/usr/bin/env python3
"""Exact base audit for the R(k) >= k-1 adjunction theorem."""
from fractions import Fraction

q = Fraction(23, 20)
# (power of q, multiplicity)
coords = [(1, 6), (-1, 3), (3, 3), (-3, 4)]


def phi(n: int, t: Fraction) -> Fraction:
    return (t**n - 1) / (t ** (n + 1) + 1)


def S(n: int) -> Fraction:
    total = Fraction(0)
    for power, multiplicity in coords:
        total += multiplicity * phi(n, q**power)
    return total


moment = sum(power * multiplicity for power, multiplicity in coords)
assert moment == 0

s21 = S(21)
s22 = S(22)
assert s21 < 0 < s22

limit_value = Fraction(6, 1) / q + Fraction(3, 1) / (q**3) - 7
assert limit_value == Fraction(2311, 12167)
assert limit_value > 0

print("PRODUCT MOMENT VERIFIED:", moment)
print("S_21 < 0:", s21 < 0)
print("S_22 > 0:", s22 > 0)
print("LIMIT VALUE:", limit_value)
print("TWO-RADIUS BASE WITNESS VERIFIED")
