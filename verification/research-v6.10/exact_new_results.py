"""Exact checks for new, manuscript-level Damascus results.

This file intentionally depends only on fractions.Fraction.
"""

from fractions import Fraction as Q


def phi_integer(n: int, x: Q) -> Q:
    return (x**n - 1) / (x ** (n + 1) + 1)


def power_sum(k: int, pair_sum: Q, pair_product: Q) -> Q:
    """x^k+y^k from x+y and xy, without adjoining the roots."""
    if k == 0:
        return Q(2)
    if k == 1:
        return pair_sum
    previous, current = Q(2), pair_sum
    for _ in range(2, k + 1):
        previous, current = current, pair_sum * current - pair_product * previous
    return current


def positive_pair_sum(n: int, pair_product: Q, pair_sum: Q) -> Q:
    """phi_n(x)+phi_n(y), given p=xy and q=x+y."""
    p, q = pair_product, pair_sum
    numerator = p**n * q + power_sum(n, q, p) - power_sum(n + 1, q, p) - 2
    denominator = p ** (n + 1) + 1 + power_sum(n + 1, q, p)
    return numerator / denominator


def check_off_axis_bifurcation() -> None:
    n = 7
    t = Q(79, 40)
    p = t * t
    q = Q(397, 100)

    # The unequal x,y are the two roots of X^2-qX+p.  The inequalities
    # 2*sqrt(p)<q<p+1 ensure x,y>1 and x != y.  The first is checked by
    # squaring, since all quantities are positive.
    assert q * q > 4 * p
    assert q < p + 1

    symmetric = 2 * phi_integer(n, t) + phi_integer(n, 1 / p)
    unequal = positive_pair_sum(n, p, q) + phi_integer(n, 1 / p)

    assert symmetric < Q(-1, 5000) < 0 < Q(1, 10000) < unequal
    print("[OK] n=7 off-axis fixed-product bifurcation")
    print("     S_7(t,t,t^-2) =", symmetric)
    print("     S_7(x,y,t^-2) =", unequal)


def phi_on_square_half_integer(base: Q) -> Q:
    """phi_(15/2)(base^2) = (base^15-1)/(base^17+1)."""
    return (base**15 - 1) / (base**17 + 1)


def check_continuous_counterexample() -> None:
    bases = (Q(127, 100), Q(32, 25), Q(63, 100))
    bases = bases + (1 / (bases[0] * bases[1] * bases[2]),)
    coordinates = tuple(base * base for base in bases)
    product = coordinates[0] * coordinates[1] * coordinates[2] * coordinates[3]
    assert product == 1

    s_half = sum(phi_on_square_half_integer(base) for base in bases)
    s_eight = sum(phi_integer(8, coordinate) for coordinate in coordinates)

    assert s_half > Q(1, 20000) > 0 > Q(-1, 1000) > s_eight
    print("[OK] continuous four-variable inclusion failure")
    print("     X =", coordinates)
    print("     S_(15/2)^4(X) =", s_half)
    print("     S_8^4(X) =", s_eight)


if __name__ == "__main__":
    check_off_axis_bifurcation()
    check_continuous_counterexample()
    print("All new exact checks passed.")
