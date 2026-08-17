#!/usr/bin/env python3
"""Standard-library exact replay for the n=5,6 topology theorem.

The certificate proves, on t>1 and 0<=u<=1,

    S_n(t,u) >= 0  ==>  partial_u S_n(t,u) < 0.

Here xy=t^2 and x+y=2t+u(t-1)^2.  The compactification
t=(1+s)/(1-s) sends the parameter rectangle to [0,1]^2.  Every leaf
is certified either by F>0 (so S_n<0 there) or H>0 (so dS_n/du<0).

The script reconstructs F and H by sparse exact polynomial arithmetic,
replays exact Sturm sequences on the symmetric slice, and replays frozen
Bernstein subdivision trees.  It uses only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent

# Sparse bivariate polynomial in (t,u): (degree_t,degree_u) -> Fraction.
Poly = dict[tuple[int, int], Fraction]


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def constant(value: int | Fraction) -> Poly:
    value = Fraction(value)
    return {} if value == 0 else {(0, 0): value}


T: Poly = {(1, 0): Fraction(1)}
U: Poly = {(0, 1): Fraction(1)}
ONE = constant(1)


def add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def scale(poly: Poly, scalar: int | Fraction) -> Poly:
    scalar = Fraction(scalar)
    return clean({monomial: coefficient * scalar for monomial, coefficient in poly.items()})


def subtract(left: Poly, right: Poly) -> Poly:
    return add(left, scale(right, -1))


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (i, j), coefficient_left in left.items():
        for (k, ell), coefficient_right in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = (
                result.get(monomial, Fraction(0))
                + coefficient_left * coefficient_right
            )
    return clean(result)


def power(poly: Poly, exponent: int) -> Poly:
    result = ONE
    base = poly
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        remaining >>= 1
        if remaining:
            base = multiply(base, base)
    return result


def derivative_u(poly: Poly) -> Poly:
    return clean(
        {
            (i, j - 1): coefficient * j
            for (i, j), coefficient in poly.items()
            if j
        }
    )


def divide_exact(dividend: Poly, divisor: Poly) -> Poly:
    """Exact multivariate long division in lexicographic (t,u) order."""
    assert divisor
    remainder = dict(dividend)
    quotient: Poly = {}
    divisor_monomial = max(divisor)
    divisor_coefficient = divisor[divisor_monomial]
    while remainder:
        remainder_monomial = max(remainder)
        remainder_coefficient = remainder[remainder_monomial]
        exponent = (
            remainder_monomial[0] - divisor_monomial[0],
            remainder_monomial[1] - divisor_monomial[1],
        )
        if exponent[0] < 0 or exponent[1] < 0:
            raise ArithmeticError(
                f"nonzero remainder at monomial {remainder_monomial}"
            )
        coefficient = remainder_coefficient / divisor_coefficient
        quotient[exponent] = quotient.get(exponent, Fraction(0)) + coefficient
        term = {exponent: coefficient}
        remainder = subtract(remainder, multiply(term, divisor))
    return clean(quotient)


def degree_list(poly: Poly) -> tuple[int, int]:
    return max(i for i, _ in poly), max(j for _, j in poly)


P = power(T, 2)
T_MINUS_ONE = subtract(T, ONE)
Q = add(scale(T, 2), multiply(U, power(T_MINUS_ONE, 2)))


def power_sum(k: int) -> Poly:
    """The polynomial x^k+y^k for xy=t^2 and x+y=Q."""
    if k == 0:
        return constant(2)
    if k == 1:
        return Q
    previous, current = constant(2), Q
    for _ in range(2, k + 1):
        previous, current = current, subtract(multiply(Q, current), multiply(P, previous))
    return current


def positive_square(n: int) -> Poly:
    if n == 5:
        first = add(power(T, 4), ONE)
        second = add(subtract(power(T, 8), power(T, 4)), ONE)
        return multiply(power(first, 2), power(second, 2))
    if n == 6:
        factor = add(
            subtract(
                add(
                    subtract(
                        add(subtract(power(T, 12), power(T, 10)), power(T, 8)),
                        power(T, 6),
                    ),
                    power(T, 4),
                ),
                power(T, 2),
            ),
            ONE,
        )
        return power(factor, 2)
    raise ValueError(n)


def cancellation_factor(n: int) -> Poly:
    if n == 5:
        return ONE
    if n == 6:
        # (t^2+1)((t+1)^2+u(t-1)^2), manifestly positive on the domain.
        return multiply(add(power(T, 2), ONE), add(power(add(T, ONE), 2), multiply(U, power(T_MINUS_ONE, 2))))
    raise ValueError(n)


def polynomials(n: int) -> tuple[Poly, Poly]:
    """Reconstruct the cleared sign polynomials F_n and H_n."""
    p_n = power(P, n)
    p_n_plus_one = multiply(p_n, P)
    ps_n = power_sum(n)
    ps_n_plus_one = power_sum(n + 1)

    # pair_sum=A/B and p*phi_n(p)=C/E.
    a_poly = add(
        subtract(add(multiply(p_n, Q), ps_n), ps_n_plus_one),
        constant(-2),
    )
    b_poly = add(add(p_n_plus_one, ONE), ps_n_plus_one)
    c_poly = multiply(P, subtract(p_n, ONE))
    e_poly = add(p_n_plus_one, ONE)

    numerator_raw = subtract(multiply(a_poly, e_poly), multiply(c_poly, b_poly))
    denominator_raw = multiply(b_poly, e_poly)
    cancellation = cancellation_factor(n)
    numerator = divide_exact(numerator_raw, cancellation)
    denominator = divide_exact(denominator_raw, cancellation)

    square = power(T_MINUS_ONE, 2)
    f_poly = divide_exact(scale(numerator, -1), square)
    derivative_numerator = subtract(
        multiply(derivative_u(numerator), denominator),
        multiply(numerator, derivative_u(denominator)),
    )
    h_divisor = multiply(square, positive_square(n))
    h_poly = divide_exact(scale(derivative_numerator, -1), h_divisor)

    for poly in (f_poly, h_poly):
        assert all(coefficient.denominator == 1 for coefficient in poly.values())
    assert degree_list(f_poly) == (22, 6)
    assert degree_list(h_poly) == (22, 10)
    return f_poly, h_poly


def t_map(i: int, degree: int) -> list[int]:
    """Coefficients of (1+s)^i(1-s)^(degree-i)."""
    out = [0] * (degree + 1)
    for a in range(degree + 1):
        out[a] = sum(
            comb(i, r) * comb(degree - i, a - r) * (-1) ** (a - r)
            for r in range(max(0, a - (degree - i)), min(i, a) + 1)
        )
    return out


def compact(poly: Poly) -> list[list[int]]:
    """Power coefficients after t=(1+s)/(1-s), with denominator cleared."""
    degree_t, degree_u = degree_list(poly)
    array = [[0 for _ in range(degree_u + 1)] for _ in range(degree_t + 1)]
    maps = [t_map(i, degree_t) for i in range(degree_t + 1)]
    for (i, j), coefficient in poly.items():
        assert coefficient.denominator == 1
        integer = coefficient.numerator
        for a, value in enumerate(maps[i]):
            array[a][j] += integer * value
    return array


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def bernstein_axis(array: list[list[int]], axis: int) -> list[list[int]]:
    rows, columns = len(array), len(array[0])
    degree = (rows if axis == 0 else columns) - 1
    common_scale = 1
    for i in range(degree + 1):
        common_scale = lcm(common_scale, comb(degree, i))

    target = [[0 for _ in range(columns)] for _ in range(rows)]
    if axis == 0:
        for k in range(degree + 1):
            for j in range(columns):
                target[k][j] = sum(
                    array[i][j] * comb(k, i) * (common_scale // comb(degree, i))
                    for i in range(k + 1)
                )
    else:
        for i in range(rows):
            for k in range(degree + 1):
                target[i][k] = sum(
                    array[i][j] * comb(k, j) * (common_scale // comb(degree, j))
                    for j in range(k + 1)
                )
    return target


def bernstein(array: list[list[int]]) -> list[list[int]]:
    return bernstein_axis(bernstein_axis(array, 0), 1)


def split(array: list[list[int]], axis: int) -> tuple[list[list[int]], list[list[int]]]:
    rows, columns = len(array), len(array[0])
    degree = (rows if axis == 0 else columns) - 1
    left = [[0 for _ in range(columns)] for _ in range(rows)]
    right = [[0 for _ in range(columns)] for _ in range(rows)]

    if axis == 0:
        for k in range(degree + 1):
            left_scale = 1 << (degree - k)
            right_scale = 1 << k
            for j in range(columns):
                left[k][j] = left_scale * sum(
                    array[i][j] * comb(k, i) for i in range(k + 1)
                )
                remaining = degree - k
                right[k][j] = right_scale * sum(
                    array[k + i][j] * comb(remaining, i)
                    for i in range(remaining + 1)
                )
    else:
        for k in range(degree + 1):
            left_scale = 1 << (degree - k)
            right_scale = 1 << k
            for i in range(rows):
                left[i][k] = left_scale * sum(
                    array[i][j] * comb(k, j) for j in range(k + 1)
                )
                remaining = degree - k
                right[i][k] = right_scale * sum(
                    array[i][k + j] * comb(remaining, j)
                    for j in range(remaining + 1)
                )
    return left, right


def minimum(array: list[list[int]]) -> int:
    return min(value for row in array for value in row)


# Univariate polynomials for Sturm replay, with ascending Fraction coefficients.
UniPoly = list[Fraction]


def uni_trim(poly: UniPoly) -> UniPoly:
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return result


def uni_derivative(poly: UniPoly) -> UniPoly:
    return uni_trim([poly[index] * index for index in range(1, len(poly))])


def uni_divmod(dividend: UniPoly, divisor: UniPoly) -> tuple[UniPoly, UniPoly]:
    divisor = uni_trim(divisor)
    remainder = uni_trim(dividend)
    quotient = [Fraction(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] += coefficient
        for index, divisor_coefficient in enumerate(divisor):
            remainder[index + degree] -= coefficient * divisor_coefficient
        remainder = uni_trim(remainder)
    return uni_trim(quotient), remainder


def sturm_sequence(poly: UniPoly) -> list[UniPoly]:
    sequence = [uni_trim(poly), uni_derivative(poly)]
    while sequence[-1]:
        _, remainder = uni_divmod(sequence[-2], sequence[-1])
        if not remainder:
            break
        sequence.append([-coefficient for coefficient in remainder])
    return sequence


def uni_evaluate(poly: UniPoly, point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def variations(values: list[Fraction]) -> int:
    signs = [sign(value) for value in values if value]
    return sum(signs[index] != signs[index + 1] for index in range(len(signs) - 1))


DIAGONAL_POLYNOMIALS: dict[int, UniPoly] = {
    # P_5=t^12-t^11-t^10-t^9-t^8+t^6+t^5+t^4+t^3+t^2+2t+2.
    5: [Fraction(value) for value in [2, 2, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, 1]],
    # P_6=t^10-2t^9-t^8+3t^7-t^6-3t^5+3t^4+2t^3-3t^2+2.
    6: [Fraction(value) for value in [2, 0, -3, 2, 3, -3, -1, 3, -1, -2, 1]],
}


EXPECTED_STURM = {
    5: ([7, 6, 5, 5], [Fraction(6), Fraction(-179473, 4096), Fraction(386)]),
    6: ([6, 5, 4, 4], [Fraction(1), Fraction(-10831, 1024), Fraction(22)]),
}


def bi_from_uni(poly: UniPoly) -> Poly:
    return clean(
        {(degree, 0): coefficient for degree, coefficient in enumerate(poly)}
    )


def verify_diagonal_factorization(n: int) -> None:
    """Check the two displayed symmetric-slice factorizations exactly."""
    if n == 5:
        actual = subtract(
            scale(multiply(subtract(power(T, 5), ONE), add(power(T, 12), ONE)), 2),
            multiply(power(T, 2), multiply(subtract(power(T, 10), ONE), add(power(T, 6), ONE))),
        )
        cyclotomic = add(add(add(add(power(T, 4), power(T, 3)), power(T, 2)), T), ONE)
        expected = scale(
            multiply(
                multiply(power(T_MINUS_ONE, 2), cyclotomic),
                bi_from_uni(DIAGONAL_POLYNOMIALS[n]),
            ),
            -1,
        )
    elif n == 6:
        actual = subtract(
            scale(multiply(subtract(power(T, 6), ONE), add(power(T, 14), ONE)), 2),
            multiply(power(T, 2), multiply(subtract(power(T, 12), ONE), add(power(T, 7), ONE))),
        )
        factor = multiply(
            multiply(add(T, ONE), add(power(T, 2), ONE)),
            multiply(
                add(subtract(power(T, 2), T), ONE),
                power(add(add(power(T, 2), T), ONE), 2),
            ),
        )
        expected = scale(
            multiply(
                multiply(power(T_MINUS_ONE, 2), factor),
                bi_from_uni(DIAGONAL_POLYNOMIALS[n]),
            ),
            -1,
        )
    else:
        raise ValueError(n)
    assert actual == expected


def verify_sturm(n: int) -> None:
    verify_diagonal_factorization(n)
    polynomial = DIAGONAL_POLYNOMIALS[n]
    sequence = sturm_sequence(polynomial)
    points = [Fraction(1), Fraction(3, 2), Fraction(2)]
    table = [
        variations([uni_evaluate(item, point) for item in sequence])
        for point in points
    ]
    table.append(variations([item[-1] for item in sequence]))
    values = [uni_evaluate(polynomial, point) for point in points]
    assert (table, values) == EXPECTED_STURM[n]
    samples = "[" + ", ".join(format_fraction(value) for value in values) + "]"
    print(f"n={n} STURM VERIFIED: variations {table}; samples {samples}")


@dataclass
class SearchStats:
    nodes: int = 0
    leaves_f: int = 0
    leaves_h: int = 0
    max_depth: int = 0


def generate(n: int, max_depth: int = 32) -> None:
    f_poly, h_poly = polynomials(n)
    print("degrees", n, degree_list(f_poly), degree_list(h_poly), flush=True)
    root_f = bernstein(compact(f_poly))
    root_h = bernstein(compact(h_poly))
    leaves = []
    stats = SearchStats()

    def walk(path, array_f, array_h, depths):
        stats.nodes += 1
        stats.max_depth = max(stats.max_depth, sum(depths))
        if minimum(array_f) > 0:
            stats.leaves_f += 1
            leaves.append([path, "F", list(depths)])
            return
        if minimum(array_h) > 0:
            stats.leaves_h += 1
            leaves.append([path, "H", list(depths)])
            return
        if sum(depths) >= max_depth:
            raise RuntimeError(
                f"unresolved n={n} path={path!r} depths={depths}; "
                f"minF={minimum(array_f)}, minH={minimum(array_h)}"
            )
        axis = 0 if depths[0] <= depths[1] else 1
        f_left, f_right = split(array_f, axis)
        h_left, h_right = split(array_h, axis)
        next_depths = list(depths)
        next_depths[axis] += 1
        next_depths = tuple(next_depths)
        walk(path + f"{axis}L,", f_left, h_left, next_depths)
        walk(path + f"{axis}R,", f_right, h_right, next_depths)

    walk("", root_f, root_h, (0, 0))
    certificate = {
        "exponent": n,
        "nodes": stats.nodes,
        "leaves": leaves,
        "stats": {
            "F": stats.leaves_f,
            "H": stats.leaves_h,
            "max_depth": stats.max_depth,
        },
    }
    destination = HERE / f"topology_n{n}_cert.json"
    destination.write_text(json.dumps(certificate, separators=(",", ":")))
    print("wrote", destination.name, certificate["stats"], "nodes", stats.nodes, flush=True)


def verify_tree(n: int) -> None:
    certificate = json.loads((HERE / f"topology_n{n}_cert.json").read_text())
    assert certificate["exponent"] == n
    trie = {}
    for path, criterion, recorded_depths in certificate["leaves"]:
        tokens = [] if not path else [
            (int(token[0]), token[1]) for token in path.strip(",").split(",")
        ]
        node = trie
        for token in tokens:
            node = node.setdefault(token, {})
        assert "leaf" not in node
        node["leaf"] = (criterion, tuple(recorded_depths), path)

    f_poly, h_poly = polynomials(n)
    root_f = bernstein(compact(f_poly))
    root_h = bernstein(compact(h_poly))
    stats = {"nodes": 0, "leaves": 0, "F": 0, "H": 0, "max_depth": 0}

    def walk(node, array_f, array_h, depths):
        stats["nodes"] += 1
        stats["max_depth"] = max(stats["max_depth"], sum(depths))
        if "leaf" in node:
            criterion, recorded_depths, path = node["leaf"]
            assert depths == recorded_depths, (path, depths, recorded_depths)
            if criterion == "F":
                assert minimum(array_f) > 0, path
            else:
                assert criterion == "H" and minimum(array_h) > 0, path
            stats[criterion] += 1
            stats["leaves"] += 1
            return

        children = list(node)
        assert len(children) == 2
        assert len({child[0] for child in children}) == 1
        assert {child[1] for child in children} == {"L", "R"}
        axis = children[0][0]
        f_left, f_right = split(array_f, axis)
        h_left, h_right = split(array_h, axis)
        next_depths = list(depths)
        next_depths[axis] += 1
        next_depths = tuple(next_depths)
        walk(node[(axis, "L")], f_left, h_left, next_depths)
        walk(node[(axis, "R")], f_right, h_right, next_depths)

    walk(trie, root_f, root_h, (0, 0))
    expected = certificate["stats"]
    assert stats["nodes"] == certificate["nodes"]
    assert stats["leaves"] == len(certificate["leaves"])
    assert stats["F"] == expected["F"]
    assert stats["H"] == expected["H"]
    assert stats["max_depth"] == expected["max_depth"]
    print(f"n={n} BERNSTEIN TREE VERIFIED: {stats}")


def verify(n: int) -> None:
    verify_sturm(n)
    verify_tree(n)


if __name__ == "__main__":
    generate_mode = "--generate" in sys.argv
    requested = [int(value) for value in sys.argv[1:] if value != "--generate"] or [5, 6]
    for exponent in requested:
        if generate_mode:
            generate(exponent)
        else:
            verify(exponent)
    print("N=5,6 FIXED-EXPONENT TOPOLOGY CERTIFICATES PASSED")
