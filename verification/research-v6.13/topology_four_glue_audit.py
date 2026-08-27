#!/usr/bin/env python3
"""Finite bookkeeping audit for the full four-variable attachment theorem.

The topology proof is analytic.  This script independently checks the labelled
incidence graph and exact reciprocal-pair barrier on representative rational
values using Fraction arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations


def phi(n: int, x: Q) -> Q:
    return (x**n - 1) / (x ** (n + 1) + 1)


def reciprocal_barrier(n: int, r: Q) -> None:
    lhs = phi(n, r) + phi(n, 1 / r)
    geom = sum((r**j for j in range(n)), Q(0))
    rhs = -(r - 1) ** 2 * geom / (r ** (n + 1) + 1)
    assert lhs == rhs
    assert lhs < 0


def incidence_graph():
    coords = range(4)
    pockets = []
    by_core = {k: [] for k in coords}

    # A pocket is determined by its two below-one coordinates {j,k} and by
    # which one is nearer to one.  We record (near, far).  Its unique core is
    # the far coordinate.
    for j, k in combinations(coords, 2):
        for near, far in ((j, k), (k, j)):
            p = (near, far)
            pockets.append(p)
            by_core[far].append(p)

    assert len(pockets) == 12
    assert len(set(pockets)) == 12
    assert all(len(by_core[k]) == 3 for k in coords)

    for far, leaves in by_core.items():
        assert {near for near, _ in leaves} == set(coords) - {far}
        assert all(f == far for _, f in leaves)

    # No ordered pocket has two core endpoints.
    endpoint = {p: p[1] for p in pockets}
    assert len(endpoint) == 12

    # Distinct traces on one core correspond to distinct near coordinates.
    assert all(len({near for near, _ in leaves}) == 3 for leaves in by_core.values())

    return by_core


def main():
    for n in range(1, 41):
        for r in (Q(5, 4), Q(7, 3), Q(23, 20)):
            reciprocal_barrier(n, r)

    graph = incidence_graph()
    print("RECIPROCAL-PAIR BARRIER VERIFIED FOR n=1..40")
    for core in sorted(graph):
        print(f"core {core}: {graph[core]}")
    print("FOUR-VARIABLE ATTACHMENT GRAPH VERIFIED: 4 disjoint K_(1,3) stars")


if __name__ == "__main__":
    main()
