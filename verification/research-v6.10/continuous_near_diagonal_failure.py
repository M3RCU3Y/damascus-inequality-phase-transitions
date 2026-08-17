"""High-precision replay for the near-diagonal continuous failure family.

This is a focused numerical sanity check, not the proof of the asymptotic
theorem.  The proof is the scaled limit in the active manuscript.  The script
uses only Python's standard-library decimal module and evaluates the explicit
B=3 witnesses at increasing target exponents.
"""

from decimal import Decimal as D
from decimal import getcontext


getcontext().prec = 100


def power(x: D, exponent: D) -> D:
    return (exponent * x.ln()).exp()


def phi(exponent: D, x: D) -> D:
    """Stable evaluation of (x^exponent-1)/(x^(exponent+1)+1)."""
    if x >= 1:
        inverse = 1 / x
        return inverse * (1 - power(x, -exponent)) / (
            1 + power(x, -(exponent + 1))
        )
    return -(1 - power(x, exponent)) / (1 + power(x, exponent + 1))


def witness(target: int, b_value: int = 3) -> tuple[D, D, D, D]:
    mu = D(target)
    b = D(b_value)
    gap = b * mu.sqrt() * power(D(2), -mu / 2)
    t = 2 - gap
    q = 1 - gap
    r = power(q, 1 / mu)
    a = 1 / (r * t * t)
    coordinates = (a, r, t, t)

    source_sum = sum(phi(mu - gap, x) for x in coordinates)
    target_sum = sum(phi(mu, x) for x in coordinates)
    assert abs(a * r * t * t - 1) < D("1e-90")
    return gap, source_sum, target_sum, power(D(2), mu)


def main() -> None:
    source_limit = D(3) ** 2 / 4 - D(3) / 2
    target_limit = -(D(3) ** 2) / 4 - D(3) / 2

    for target in (24, 32, 48, 64):
        gap, source_sum, target_sum, scale = witness(target)
        assert source_sum > 0 > target_sum
        print(f"mu={target:2d}  gap={gap}")
        print(f"  2^mu S_(mu-gap) = {scale * source_sum}")
        print(f"  2^mu S_mu       = {scale * target_sum}")

    _, source_sum, target_sum, scale = witness(64)
    assert abs(scale * source_sum - source_limit) < D("1e-5")
    assert abs(scale * target_sum - target_limit) < D("1e-5")
    print("[OK] signs and scaled B=3 limits replayed at 100-digit precision")


if __name__ == "__main__":
    main()
