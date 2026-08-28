#!/usr/bin/env python3
"""Validated transverse second variation at the certified four-variable fold."""
from __future__ import annotations

import symmetric_fold_certificate as S


def main() -> None:
    box = S.BOX
    f, _, _ = S.system_and_jac(box)

    # The upper pair is phi(alpha,c+d)+phi(alpha,c-d).  At d=0,
    # F_dd=2 phi_cc and F_add=2 phi_acc.  Reuse the certified third-order jet.
    n = S.J3.var(box[0], 0)
    c = S.J3.var(box[1], 1)
    upper = S.phi(n, c)

    Faa = f.h[0][0]
    Fc = f.d[1]
    Fac = f.h[0][1]
    Fdd = S.I(2) * upper.h[1][1]
    Fadd = S.I(2) * upper.t[0][1][1]

    lam2 = -(S.I(1) / Faa)
    lam1 = -(lam2 * Fac / Fc)
    Ldd = lam1 * Fdd + lam2 * Fadd

    # The symmetric constrained curvature is recomputed exactly as in the
    # parent fold certificate.
    ep = -f.d[1] / f.d[2]
    e2 = -(f.h[1][1] + S.I(2) * f.h[1][2] * ep + f.h[2][2] * ep * ep) / f.d[2]
    curv = (
        f.t[0][1][1]
        + S.I(2) * f.t[0][1][2] * ep
        + f.t[0][2][2] * ep * ep
        + f.h[0][2] * e2
    )
    sym_second = lam2 * curv

    print("FULL FOLD TRANSVERSE CERTIFICATE")
    print("F_aa       =", Faa)
    print("F_dd       =", Fdd)
    print("F_add      =", Fadd)
    print("lambda_1   =", lam1)
    print("lambda_2   =", lam2)
    print("L_dd       =", Ldd)
    print("C_sym      =", curv)
    print("sym second =", sym_second)

    assert Faa.hi < 0
    assert lam2.lo > 0
    assert Ldd.lo > 0
    assert curv.lo > 0
    assert sym_second.lo > 0
    print("VERIFIED: full restricted Hessian is positive definite at the fold")


if __name__ == "__main__":
    main()
