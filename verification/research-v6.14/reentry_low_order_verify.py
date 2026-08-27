#!/usr/bin/env python3
"""Rigorous low-order radial Chebyshev certificate for Damascus re-entry.

For K_x(s)=x sech^2(sx), this verifies the initial scalar Wronskians
through order four. Together with the existing order-five certificate, it
makes the ECT argument self-contained through five reciprocal radii.

Each nontrivial order is certified in three pieces:
  * 0 < u <= 0.1: exact rational Taylor/Bernstein lower bound;
  * 0.1 <= u <= 8: deterministic outward-rounded Decimal interval bound;
  * u >= 8: analytic exponential-tail bound.
"""
from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from math import comb, factorial
import sympy as sp

PREC = 80
u, y, q = sp.symbols("u y q", real=True)


def D(expr):
    return sp.diff(expr, u) + (1-y*y)*sp.diff(expr, y)


def base_derivative_polynomials(max_order=4):
    out = [1-y*y]
    for _ in range(1, max_order):
        out.append(sp.expand((1-y*y)*sp.diff(out[-1], y)))
    return out


def normalized_polynomial(order: int):
    """Return an integer P(u,q)>0 equivalent to nonvanishing of W_order."""
    derivs = base_derivative_polynomials(order)
    cols = []
    for j in range(order):
        cur = sp.expand(u**j * derivs[j])
        col = [cur]
        for _ in range(1, order):
            cur = sp.expand(D(cur))
            col.append(cur)
        cols.append(col)

    M = sp.Matrix([[cols[c][r] for c in range(order)] for r in range(order)])
    det = sp.factor(M.det(method="domain-ge"))

    inner = sp.cancel(det/(1-y*y)**order)
    assert sp.denom(inner) == 1

    expr = sp.together(inner.subs(y, (1-q)/(1+q)))
    num, den = expr.as_numer_denom()
    num = sp.expand(num)
    den = sp.factor(den)
    assert den == (1+q)**(order*(order-1))

    poly = sp.Poly(num, u, q, domain=sp.ZZ)
    sample = sp.N(poly.as_expr().subs({u: 1, q: sp.exp(-2)}), 60)
    orient = 1 if sample > 0 else -1
    poly = sp.Poly(orient*poly.as_expr(), u, q, domain=sp.ZZ)

    q0 = sp.Poly(poly.as_expr(), q).coeff_monomial(1)
    assert not q0.free_symbols and q0 > 0
    return poly, orient, det


def terms_dict(poly):
    return {(i, j): int(c) for (i, j), c in poly.terms()}


def composite_taylor_and_remainder(terms, M):
    coeff = [Fraction(0) for _ in range(M+1)]
    C = Fraction(0)
    for (i, j), cc in terms.items():
        c = Fraction(cc)
        if j == 0:
            if i <= M:
                coeff[i] += c
            continue
        K = M-i
        if K < 0:
            raise AssertionError("Taylor order too small")
        for k in range(K+1):
            coeff[i+k] += c*Fraction((-2*j)**k, factorial(k))
        C += abs(c)*Fraction((2*j)**(K+1), factorial(K+1))
    return coeff, C


def bernstein_0a(power_coeff, a):
    n = len(power_coeff)-1
    scaled = [power_coeff[k]*a**k for k in range(n+1)]
    out = []
    for i in range(n+1):
        total = Fraction(0)
        for k in range(i+1):
            total += scaled[k]*Fraction(comb(i, k), comb(n, k))
        out.append(total)
    return out


def small_interval_exact(poly, order):
    M = 40
    terms = terms_dict(poly)
    coeff, C = composite_taylor_and_remainder(terms, M)
    vanishing_order = order*(order-1)//2
    assert all(coeff[k] == 0 for k in range(vanishing_order))
    assert coeff[vanishing_order] > 0

    lower = [coeff[k+vanishing_order] for k in range(M-vanishing_order+1)]
    lower.append(-C)
    B = bernstein_0a(lower, Fraction(1, 10))
    mn = min(B)
    assert mn > 0
    return mn, len(B), vanishing_order


def d_exp_bounds(x: Decimal):
    with localcontext() as ctx:
        ctx.prec = PREC+20
        v = x.exp()
        eps = (abs(v)+1)*(Decimal(10)**Decimal(-(PREC+5)))
        return v-eps, v+eps


def iadd(A, B):
    with localcontext() as ctx:
        ctx.prec = PREC; ctx.rounding = ROUND_FLOOR
        lo = A[0]+B[0]
    with localcontext() as ctx:
        ctx.prec = PREC; ctx.rounding = ROUND_CEILING
        hi = A[1]+B[1]
    return lo, hi


def imul(A, B):
    with localcontext() as ctx:
        ctx.prec = PREC+10
        vals = [A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1]]
    with localcontext() as ctx:
        ctx.prec = PREC; ctx.rounding = ROUND_FLOOR
        lo = +min(vals)
    with localcontext() as ctx:
        ctx.prec = PREC; ctx.rounding = ROUND_CEILING
        hi = +max(vals)
    return lo, hi


def coeff_array(poly):
    du, dq = poly.degree(u), poly.degree(q)
    A = [[0]*(dq+1) for _ in range(du+1)]
    for (i, j), c in poly.terms():
        A[i][j] = int(c)
    return A


def interval_horner(A, U, Q):
    du, dq = len(A)-1, len(A[0])-1
    curU = (Decimal(0), Decimal(0))
    for i in range(du, -1, -1):
        curQ = (Decimal(0), Decimal(0))
        for j in range(dq, -1, -1):
            c = Decimal(A[i][j])
            curQ = iadd(imul(curQ, Q), (c, c))
        curU = iadd(imul(curU, U), curQ)
    return curU


def q_interval(a: Decimal, b: Decimal | None = None):
    if b is None:
        b = a
    lo, _ = d_exp_bounds(-Decimal(2)*b)
    _, hi = d_exp_bounds(-Decimal(2)*a)
    return lo, hi


def middle_certificate(poly):
    deriv = sp.Poly(
        sp.diff(poly.as_expr(), u)-2*q*sp.diff(poly.as_expr(), q),
        u, q, domain=sp.ZZ,
    )
    A = coeff_array(poly)
    AD = coeff_array(deriv)
    segments = [
        (Decimal("0.1"), Decimal("0.15"), Decimal("0.0002")),
        (Decimal("0.15"), Decimal("0.2"), Decimal("0.001")),
        (Decimal("0.2"), Decimal("0.5"), Decimal("0.003")),
        (Decimal("0.5"), Decimal("2"), Decimal("0.01")),
        (Decimal("2"), Decimal("8"), Decimal("0.05")),
    ]
    count = 0
    best = None
    best_box = None
    for start, end, step in segments:
        a = start
        while a < end:
            b = min(end, a+step)
            m = (a+b)/2
            h = (b-a)/2
            DI = interval_horner(AD, (a, b), q_interval(a, b))
            slope = max(abs(DI[0]), abs(DI[1]))
            FI = interval_horner(A, (m, m), q_interval(m))
            with localcontext() as ctx:
                ctx.prec = PREC; ctx.rounding = ROUND_FLOOR
                lower = FI[0]-slope*h
            if lower <= 0:
                raise AssertionError(f"middle certificate failed on [{a},{b}]: {lower}")
            if best is None or lower < best:
                best, best_box = lower, (a, b)
            count += 1
            a = b
    return count, best, best_box


def tail_certificate(poly):
    terms = terms_dict(poly)
    ratios = [Fraction(i, 2*j) for (i, j), c in terms.items() if j]
    assert max(ratios, default=Fraction(0)) <= 8

    q0 = sp.Poly(poly.as_expr(), q).coeff_monomial(1)
    base = Decimal(int(q0))
    _, q8_hi = d_exp_bounds(Decimal(-16))
    with localcontext() as ctx:
        ctx.prec = PREC+10
        correction = Decimal(0)
        for (i, j), c in terms.items():
            if j == 0:
                continue
            correction += Decimal(abs(c))*(Decimal(8)**i)*(q8_hi**j)
        margin = base-correction
    assert margin > 0
    return correction, margin, max(ratios, default=Fraction(0))


def main():
    print("LOW-ORDER WRONSKIAN CERTIFICATE")
    print("order 1: W_1=sech^2(u)>0")

    for order in (2, 3, 4):
        poly, orient, _ = normalized_polynomial(order)
        small, nbern, d = small_interval_exact(poly, order)
        boxes, midmargin, box = middle_certificate(poly)
        corr, tailmargin, maxratio = tail_certificate(poly)
        original_sign = "+" if orient > 0 else "-"
        print(f"order {order}: oriented numerator positive; original orientation={original_sign}")
        print(f"  small: vanishing order {d}; Bernstein coeffs={nbern}; min={float(small):.8g}")
        print(f"  middle: boxes={boxes}; weakest lower={midmargin} on {box}")
        print(f"  tail: max i/(2j)={float(maxratio):.6g}; correction={corr}; margin={tailmargin}")

    print("CONCLUSION: all initial scalar Wronskians through order four are nonzero for u>0")
    print("Combined with the archived order-five certificate, K_x(s)=x sech^2(sx) is ECT through order five.")


if __name__ == "__main__":
    main()
