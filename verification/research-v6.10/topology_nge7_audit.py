#!/usr/bin/env python3
"""Exact arithmetic audit for the all-n>=7 three-variable topology theorem.

The accompanying proof is analytic. This script checks every displayed finite
identity/base inequality and stress-tests the coefficient/shape lemmas for a
large integer range using integers/Fraction only. No floating-point sign
decision is made.
"""
from fractions import Fraction as Q
from math import comb

R0 = Q(39, 20)


def G(n: int, t: Q) -> Q:
    return t ** (2*n + 2) * (t - 2) + t ** (n + 2) * (t + 1) + t*t - 2


def K(n: int, r: Q) -> Q:
    return (r ** (2*n + 2)
            - (n+1)**2 * r ** (n+2)
            - (n*n + 4*n + 1) * r ** (n+1)
            + (n+1)**2 * r + n*n)


def shifted_G_coeff(n: int, k: int) -> int:
    def C(a, b):
        return comb(a, b) if 0 <= b <= a else 0
    return (C(2*n+3, k) - 2*C(2*n+2, k)
            + C(n+3, k) + C(n+2, k) + C(2, k)
            - (2 if k == 0 else 0))


def audit_coefficient_lemma(limit: int = 250) -> None:
    for n in range(7, limit + 1):
        coeff = [shifted_G_coeff(n, k) for k in range(2*n+4)]
        assert coeff[0] == 0
        assert coeff[1] == 6
        assert coeff[2] == -n*n + 3*n + 6 < 0
        assert all(coeff[k] < 0 for k in range(2, n+2))
        assert all(coeff[k] > 0 for k in range(n+2, 2*n+4))

        # Ratio comparison used in the written proof. j=n-k.
        for k in range(2, n+1):
            j = n-k
            num = 2*j*j*n + 2*j*n*n + 11*j*n - 9*j + n*n - 27
            assert num > 0
    print(f"[OK] shifted G coefficient lemma for n=7..{limit}")


def audit_shape_bases(limit: int = 250) -> None:
    n = 7
    q7 = (n+1)**2 * R0 + n*n + 4*n + 1
    assert R0**8 - q7 == Q(160329260481, 25600000000) > 0
    assert G(7, R0) == Q(-12857211561564900828351361,
                           13107200000000000000000) < 0
    assert Q(3,2)**8 - 8*Q(3,2) - 7 == Q(1697,256) > 0

    for n in range(7, limit + 1):
        qn = (n+1)**2 * R0 + n*n + 4*n + 1
        assert R0 ** (n+1) > qn
        assert K(n, R0) > 0
        assert G(n, R0) < 0
        assert Q(3,2) ** (n+1) > (n+1)*Q(3,2) + n
        assert -2*n*n + Q(45,8)*n + Q(19,4) < 0

        # Exact induction margin appearing in the proof.
        assert (1121*n*n + 642*n - 3219) > 0
    print(f"[OK] alpha/rho/root sandwich inequalities for n=7..{limit}")


def audit_descartes_samples(limit: int = 250) -> None:
    for n in range(7, limit+1):
        assert G(n, Q(3,2)) < 0
        assert G(n, Q(2)) > 0
    print(f"[OK] symmetric-root sign samples for n=7..{limit}")


if __name__ == "__main__":
    audit_coefficient_lemma()
    audit_shape_bases()
    audit_descartes_samples()
    print("N>=7 THREE-VARIABLE TOPOLOGY EXACT AUDIT PASSED")
