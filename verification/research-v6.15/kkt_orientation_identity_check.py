#!/usr/bin/env python3
"""Exact symbolic checks for the V6.15 KKT orientation reductions.

This verifier checks identities only.  It deliberately makes no assertion
about the conjectural global signs Q_123 < 0 or Delta < 0.
"""

from __future__ import annotations

import sympy as sp


def check_three_point_orientation() -> None:
    lam, gam = sp.symbols("lambda gamma")
    H1, H2, H3 = sp.symbols("H1 H2 H3")
    M1, M2, M3 = sp.symbols("M1 M2 M3")
    Hp1, Hp2, Hp3 = sp.symbols("Hp1 Hp2 Hp3")
    Mp1, Mp2, Mp3 = sp.symbols("Mp1 Mp2 Mp3")

    D = sp.Matrix(
        [
            [1, H1, M1],
            [1, H2, M2],
            [1, H3, M3],
        ]
    ).det()

    substitutions = {
        M1: lam * H1 + gam,
        M2: lam * H2 + gam,
        M3: lam * H3 + gam,
    }

    dD = [
        sp.diff(D, H1) * Hp1 + sp.diff(D, M1) * Mp1,
        sp.diff(D, H2) * Hp2 + sp.diff(D, M2) * Mp2,
        sp.diff(D, H3) * Hp3 + sp.diff(D, M3) * Mp3,
    ]

    v = [H2 - H3, H3 - H1, H1 - H2]
    fp = [Mp1 - lam * Hp1, Mp2 - lam * Hp2, Mp3 - lam * Hp3]

    for i in range(3):
        residual = sp.expand(dD[i].subs(substitutions) + v[i] * fp[i])
        assert residual == 0, f"orientation derivative identity failed at root {i + 1}"

    directional = sp.expand(
        sum(v[i] * dD[i].subs(substitutions) for i in range(3))
        + sum(fp[i] * v[i] ** 2 for i in range(3))
    )
    assert directional == 0, "dD[v] = -Q_123 identity failed"


def check_delta_pairwise_expansion() -> None:
    d1, d2, d3, d4 = sp.symbols("d1 d2 d3 d4", nonzero=True)
    H1, H2, H3, H4 = sp.symbols("H1 H2 H3 H4")
    ds = [d1, d2, d3, d4]
    hs = [H1, H2, H3, H4]

    delta = (
        sum(1 / d for d in ds) * sum(h * h / d for h, d in zip(hs, ds))
        - sum(h / d for h, d in zip(hs, ds)) ** 2
    )
    pairwise = sum(
        (hs[i] - hs[j]) ** 2 / (ds[i] * ds[j])
        for i in range(4)
        for j in range(i + 1, 4)
    )
    assert sp.cancel(delta - pairwise) == 0, "pairwise Delta identity failed"


def check_bordered_hessian_identity() -> None:
    d1, d2, d3, d4 = sp.symbols("d1 d2 d3 d4", nonzero=True)
    H1, H2, H3, H4 = sp.symbols("H1 H2 H3 H4")
    ds = [d1, d2, d3, d4]
    hs = [H1, H2, H3, H4]

    D = sp.diag(*ds)
    C = sp.Matrix([[1, 1, 1, 1], hs])
    bordered = D.row_join(C.T).col_join(C.row_join(sp.zeros(2, 2)))

    delta = (
        sum(1 / d for d in ds) * sum(h * h / d for h, d in zip(hs, ds))
        - sum(h / d for h, d in zip(hs, ds)) ** 2
    )
    target = sp.prod(ds) * delta

    assert sp.cancel(bordered.det() - target) == 0, "bordered Hessian identity failed"


def check_root_map_jacobian() -> None:
    d1, d2, d3, d4 = sp.symbols("d1 d2 d3 d4", nonzero=True)
    H1, H2, H3, H4 = sp.symbols("H1 H2 H3 H4")
    ds = [d1, d2, d3, d4]
    hs = [H1, H2, H3, H4]

    # Implicit root sensitivities for f=M-lambda H-gamma=0:
    # x_gamma = 1/f' and x_lambda = H/f'.
    P_gamma = sum(1 / d for d in ds)
    P_lambda = sum(h / d for h, d in zip(hs, ds))
    A_gamma = P_lambda
    A_lambda = sum(h * h / d for h, d in zip(hs, ds))

    jacobian = sp.Matrix([[P_gamma, P_lambda], [A_gamma, A_lambda]]).det()
    delta = P_gamma * A_lambda - P_lambda**2
    assert sp.cancel(jacobian - delta) == 0, "root-map Jacobian identity failed"


def main() -> None:
    check_three_point_orientation()
    print("PASS three-point orientation: dD_123[v] = -Q_123")

    check_delta_pairwise_expansion()
    print("PASS Delta pairwise expansion")

    check_bordered_hessian_identity()
    print("PASS bordered constrained-Hessian determinant identity")

    check_root_map_jacobian()
    print("PASS root-map orientation Jacobian identity")

    print("ALL V6.15 KKT ORIENTATION IDENTITIES PASSED")
    print("NOTE: no global sign claim for Q_123 or Delta is made by this audit")


if __name__ == "__main__":
    main()
