#!/usr/bin/env python3
"""Exact audit for topology, continuous-exponent, and pulse bounds."""

from fractions import Fraction as Q


def phi_integer(n, x):
    return (x**n - 1) / (x ** (n + 1) + 1)


def power_sum(k, pair_sum, pair_product):
    if k == 0:
        return Q(2)
    if k == 1:
        return pair_sum
    previous, current = Q(2), pair_sum
    for _ in range(2, k + 1):
        previous, current = current, pair_sum * current - pair_product * previous
    return current


def positive_pair_sum(n, pair_product, pair_sum):
    p, q = pair_product, pair_sum
    numerator = p**n * q + power_sum(n, q, p) - power_sum(n + 1, q, p) - 2
    denominator = p ** (n + 1) + 1 + power_sum(n + 1, q, p)
    return numerator / denominator


def off_axis_check():
    n, t, q = 7, Q(79, 40), Q(397, 100)
    p = t * t
    assert q * q > 4 * p and q < p + 1
    symmetric = 2 * phi_integer(n, t) + phi_integer(n, 1 / p)
    unequal = positive_pair_sum(n, p, q) + phi_integer(n, 1 / p)
    assert symmetric < Q(-1, 5000) < 0 < Q(1, 10000) < unequal
    print("OPEN-PROBLEM AUDIT: exact n=7 off-axis bifurcation VERIFIED")


def continuous_check():
    bases = (Q(127, 100), Q(32, 25), Q(63, 100))
    bases += (1 / (bases[0] * bases[1] * bases[2]),)
    coordinates = tuple(r * r for r in bases)
    assert coordinates[0] * coordinates[1] * coordinates[2] * coordinates[3] == 1
    s_half = sum((r**15 - 1) / (r**17 + 1) for r in bases)
    s_eight = sum(phi_integer(8, x) for x in coordinates)
    assert s_half > Q(1, 20000) > 0 > Q(-1, 1000) > s_eight
    print("OPEN-PROBLEM AUDIT: I_(15/2)^4 not subset I_8^4 VERIFIED")


def overlapping_pulse_check():
    # Rational inequalities used in the analytic tail domination proof.
    # The only transcendental input is the elementary bound log(3) < 11/10.
    central = Q(6, 35)
    small_tail = Q(1331, 52000)
    large_tail = Q(1, 12)
    margin = central - small_tail - large_tail
    assert margin == Q(68249, 1092000) > 0
    # Collected coefficients after cancellation of adjacent pulse endpoints.
    for changes in range(1, 25):
        coefficients = {1: -1, 3 ** (changes + 1): (-1) ** (changes + 1)}
        for j in range(changes + 1):
            coefficients[2 * 3**j] = 2 * (-1) ** j
        assert len(coefficients) == changes + 3
        assert sum(abs(c) for c in coefficients.values()) == 2 * changes + 4
        assert sum(w * c for w, c in coefficients.items()) == 0
    print("OPEN-PROBLEM AUDIT: telescoping-pulse rational margin VERIFIED")
    print("OPEN-PROBLEM AUDIT: telescoped radius/dimension counts VERIFIED")


if __name__ == "__main__":
    off_axis_check()
    continuous_check()
    overlapping_pulse_check()
    print("OPEN-PROBLEM EXACT AUDIT PASSED")
