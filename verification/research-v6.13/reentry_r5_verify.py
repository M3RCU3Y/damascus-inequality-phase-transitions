#!/usr/bin/env python3
"""Rigorous verification of the order-five radial Chebyshev certificate.

This proves that the scalar Wronskian associated with
    K_x(s) = x sech^2(s x)
keeps a fixed nonzero sign through order five. Combined with the common zero
of F_x(s)=tanh(sx)-tanh(x) at s=1, this yields the four-zero upper bound for
five reciprocal radii.

Proof strategy
--------------
1. Derive the exact polynomial form of the fifth scalar Wronskian using SymPy.
2. Substitute y=tanh(u)=(1-q)/(1+q), q=e^{-2u}; the sign reduces to an
   integer polynomial P(u,q) divided by (1+q)^20.
3. On 0 <= u <= 0.1, use an exact rational Taylor remainder and exact
   Bernstein coefficients.
4. On 0.1 <= u <= 8, use outward-rounded Decimal interval arithmetic on a
   finite deterministic partition. Decimal.exp is correctly rounded by the
   Python decimal implementation; we additionally inflate every exponential
   by a much larger safety cushion.
5. On u >= 8, the q^0 term is 36 and all q-dependent terms are bounded in
   absolute value by their values at u=8, since u^i e^{-2ju} is decreasing
   there for every term occurring in P.
"""
from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from math import comb, factorial
import sympy as sp

PREC = 70
u, y, q = sp.symbols("u y q", real=True)


def D(expr):
    return sp.diff(expr, u) + (1-y*y)*sp.diff(expr, y)


def build_polynomial():
    # q0(u)=sech^2 u = 1-y^2, with y=tanh u and d/du=(1-y^2)d/dy.
    P = [1-y*y]
    for _ in range(1, 5):
        P.append(sp.expand((1-y*y)*sp.diff(P[-1], y)))

    cols = []
    for j in range(5):
        cur = sp.expand(u**j * P[j])
        col = [cur]
        for _ in range(1, 5):
            cur = sp.expand(D(cur))
            col.append(cur)
        cols.append(col)
    M = sp.Matrix([[cols[c][r] for c in range(5)] for r in range(5)])
    det = sp.factor(M.det(method="domain-ge"))

    obvious = -8192*(y-1)**5*(y+1)**5
    R = sp.cancel(det/obvious)
    assert sp.denom(R) == 1
    R = sp.expand(R)

    expr = sp.together(R.subs(y, (1-q)/(1+q)))
    num, den = expr.as_numer_denom()
    num = sp.expand(num)
    den = sp.factor(den)
    assert den == (q+1)**20
    poly = sp.Poly(num, u, q, domain=sp.ZZ)
    assert poly.degree(u) == 10 and poly.degree(q) == 20
    assert sp.Poly(num, q).coeff_monomial(1) == 36
    return poly


def terms_dict(poly):
    return {(i,j): int(c) for (i,j), c in poly.terms()}


def composite_taylor_and_remainder(terms, M):
    """Taylor of P(u,e^-2u) through degree M and absolute remainder C*u^(M+1)."""
    coeff = [Fraction(0) for _ in range(M+1)]
    C = Fraction(0)
    for (i,j), cc in terms.items():
        c = Fraction(cc)
        if j == 0:
            if i <= M:
                coeff[i] += c
            continue
        K = M-i
        if K < 0:
            raise AssertionError("M too small for polynomial degree")
        for k in range(K+1):
            coeff[i+k] += c*Fraction((-2*j)**k, factorial(k))
        # Lagrange remainder for e^{-2ju}: derivative magnitude <=1 on u>=0.
        C += abs(c)*Fraction((2*j)**(K+1), factorial(K+1))
    return coeff, C


def bernstein_0a(power_coeff, a):
    n = len(power_coeff)-1
    scaled = [power_coeff[k]*a**k for k in range(n+1)]
    out = []
    for i in range(n+1):
        s = Fraction(0)
        for k in range(i+1):
            s += scaled[k]*Fraction(comb(i,k), comb(n,k))
        out.append(s)
    return out


def small_interval_exact(terms):
    M = 40
    coeff, C = composite_taylor_and_remainder(terms, M)
    # Exact expansion starts at degree 10.
    assert all(coeff[k] == 0 for k in range(10))
    assert coeff[10] > 0
    # P(u,e^-2u)/u^10 >= T_M/u^10 - C u^(M-9).
    lower = [coeff[k+10] for k in range(M-9)]
    lower.append(-C)
    B = bernstein_0a(lower, Fraction(1,10))
    mn = min(B)
    assert mn > 0
    return mn, len(B)


def coeff_array(poly):
    du, dq = poly.degree(u), poly.degree(q)
    A = [[0]*(dq+1) for _ in range(du+1)]
    for (i,j), c in poly.terms():
        A[i][j] = int(c)
    return A


def d_exp_bounds(x: Decimal):
    # Decimal.exp is correctly rounded. Compute at PREC+20 and inflate by a
    # safety interval ~1e-75 relative/absolute, vastly larger than its ulp.
    with localcontext() as ctx:
        ctx.prec = PREC+20
        v = x.exp()
        eps = (abs(v)+1) * (Decimal(10) ** Decimal(-(PREC+5)))
        return v-eps, v+eps


def iadd(A, B):
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_FLOOR
        lo = A[0]+B[0]
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_CEILING
        hi = A[1]+B[1]
    return lo, hi


def imul(A, B):
    with localcontext() as ctx:
        ctx.prec=PREC+10
        vals = [A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1]]
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_FLOOR
        lo = (+min(vals))
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_CEILING
        hi = (+max(vals))
    return lo, hi


def interval_horner(A, U, Q):
    du, dq = len(A)-1, len(A[0])-1
    curU = (Decimal(0), Decimal(0))
    for i in range(du, -1, -1):
        curQ = (Decimal(0), Decimal(0))
        for j in range(dq, -1, -1):
            c = Decimal(A[i][j])
            curQ = iadd(imul(curQ, Q), (c,c))
        curU = iadd(imul(curU, U), curQ)
    return curU


def q_interval(a: Decimal, b: Decimal | None = None):
    if b is None:
        b = a
    lo, _ = d_exp_bounds(-Decimal(2)*b)
    _, hi = d_exp_bounds(-Decimal(2)*a)
    return lo, hi


def middle_certificate(poly):
    # d/du P(u,e^-2u) = P_u - 2q P_q.
    deriv = sp.Poly(sp.diff(poly.as_expr(),u)-2*q*sp.diff(poly.as_expr(),q), u,q,domain=sp.ZZ)
    A = coeff_array(poly)
    AD = coeff_array(deriv)

    segments = [
        (Decimal("0.1"), Decimal("0.15"), Decimal("0.0002")),
        (Decimal("0.15"), Decimal("0.2"), Decimal("0.001")),
        (Decimal("0.2"), Decimal("0.25"), Decimal("0.002")),
        (Decimal("0.25"), Decimal("0.5"), Decimal("0.005")),
        (Decimal("0.5"), Decimal("8"), Decimal("0.05")),
    ]
    count=0
    best=None
    best_box=None
    for start,end,step in segments:
        a=start
        while a<end:
            b=min(end,a+step)
            m=(a+b)/2
            h=(b-a)/2
            DI=interval_horner(AD,(a,b),q_interval(a,b))
            M=max(abs(DI[0]),abs(DI[1]))
            FI=interval_horner(A,(m,m),q_interval(m))
            with localcontext() as ctx:
                ctx.prec=PREC;ctx.rounding=ROUND_FLOOR
                lower=FI[0]-M*h
            if lower <= 0:
                raise AssertionError(f"middle interval failed: [{a},{b}], lower={lower}")
            if best is None or lower<best:
                best=lower; best_box=(a,b)
            count += 1
            a=b
    return count,best,best_box


def tail_certificate(poly):
    terms = terms_dict(poly)
    # constant in q is exactly 36. For every q-dependent monomial u^i q^j,
    # i/(2j) <= 2 < 8, so u^i e^{-2ju} decreases for u>=8.
    ratios=[Fraction(i,2*j) for (i,j),c in terms.items() if j]
    assert max(ratios) <= 2
    _, q8_hi = d_exp_bounds(Decimal(-16))
    with localcontext() as ctx:
        ctx.prec=PREC+10
        tail=Decimal(0)
        for (i,j),c in terms.items():
            if j==0: continue
            tail += Decimal(abs(c))*(Decimal(8)**i)*(q8_hi**j)
        margin=Decimal(36)-tail
    assert margin>0
    return tail,margin


def main():
    poly=build_polynomial()
    terms=terms_dict(poly)
    sm,nB=small_interval_exact(terms)
    count,midmargin,box=middle_certificate(poly)
    tail,tailmargin=tail_certificate(poly)
    print("ORDER-5 WRONSKIAN CERTIFICATE PASSED")
    print(f"small exact Bernstein coefficients: {nB}; min={float(sm):.6g}")
    print(f"middle interval boxes: {count}; weakest lower margin={midmargin} on {box}")
    print(f"tail absolute correction bound={tail}; tail margin={tailmargin}")
    print("CONCLUSION: scalar order-5 Wronskian has fixed nonzero sign for all u>0")


if __name__ == "__main__":
    main()
