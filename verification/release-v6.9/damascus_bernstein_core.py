#!/usr/bin/env python3
"""Exact algebraic core for the four-variable Bernstein certificates.

All pruning-relevant quantities are Python integers.  NumPy is used only as
an n-dimensional object-array container; SymPy is used only to derive the
integer coefficient tensors from the closed polynomial formulas.
"""
from math import comb, gcd
import numpy as np
import sympy as sp

# Four-variable 2+2 symmetric chart.
t, u, v = sp.symbols("t u v")
p = t**2
q = 2*t + u*(t-1)**2
r = 2*t + v*(t-1)**2


def power_sum(k, Q):
    if k == 0:
        return sp.Integer(2)
    if k == 1:
        return Q
    a, b = sp.Integer(2), Q
    for _ in range(2, k + 1):
        a, b = b, sp.expand(Q*b - p*a)
    return b


def pair_positive_sum(n, Q):
    """phi_n(x)+phi_n(y) for xy=p and x+y=Q."""
    return sp.cancel(
        (p**n*Q + power_sum(n, Q) - power_sum(n+1, Q) - 2)
        / (p**(n+1) + 1 + power_sum(n+1, Q))
    )


def reciprocal_pair_cost(n, R):
    """a phi_n(a)+b phi_n(b) for ab=p and a+b=R."""
    return sp.cancel(
        (2*p**(n+1) + power_sum(n+1, R) - p*power_sum(n, R) - R)
        / (p**(n+1) + 1 + power_sum(n+1, R))
    )


def Fpoly(n):
    """Return F_n(t,u,v) with S_n^4>0 iff F_n<0 on the 2+2 chart.

    The chart has xy=ab=t^2, q=x+y, r=a+b, and 0<=u<v<=1.
    The common rational denominator is strictly positive.  The numerator of
    S_n^4 has the factor -(t-1)^2; F_n is the remaining polynomial.
    """
    num = sp.fraction(sp.cancel(pair_positive_sum(n, q) - reciprocal_pair_cost(n, r)))[0]
    F = sp.cancel(-num/(t-1)**2)
    return sp.Poly(F, t, u, v, domain=sp.QQ)


def tmap_int(i, d):
    """Coefficients of (1+s)^i(1-s)^(d-i)."""
    out = [0]*(d+1)
    for a in range(d+1):
        val = 0
        lo = max(0, a-(d-i))
        hi = min(i, a)
        for rr in range(lo, hi+1):
            val += comb(i, rr)*comb(d-i, a-rr)*((-1)**(a-rr))
        out[a] = val
    return out


def compact_power_tensor_int(n):
    """Power coefficients after t=(1+s)/(1-s), v=U+(1-U)B.

    Multiplication by (1-s)^deg_t clears the only compactification
    denominator.  That factor is positive on 0<=s<1, and the boundary s=1
    is treated by continuity of the resulting polynomial.  The second map
    sends 0<=U,B<=1 onto the triangular region 0<=u<=v<=1.
    """
    F = Fpoly(n)
    dt, du, dv = F.degree_list()
    arr = np.zeros((dt+1, du+dv+1, dv+1), dtype=object)
    tmaps = [tmap_int(i, dt) for i in range(dt+1)]

    for (i, j, k), cc in F.terms():
        cc = sp.Rational(cc)
        if cc.q != 1:
            raise AssertionError("unexpected non-integral F_n coefficient")
        c = int(cc)
        tv = tmaps[i]
        # v^k=[U+(1-U)B]^k.
        for h in range(k+1):
            ch = comb(k, h)
            for ell in range(h+1):
                Udeg = j + k - h + ell
                Bdeg = h
                mult = c*ch*comb(h, ell)*((-1)**ell)
                if mult:
                    for aa, val in enumerate(tv):
                        if val:
                            arr[aa, Udeg, Bdeg] += mult*val
    return arr


def _lcm(a, b):
    return a//gcd(a, b)*b


def bern_int_axis(arr, axis):
    """Power-to-Bernstein conversion with one common positive integer scale."""
    d = arr.shape[axis]-1
    scale = 1
    for i in range(d+1):
        scale = _lcm(scale, comb(d, i))
    a = np.moveaxis(arr, axis, 0)
    out = np.zeros_like(a, dtype=object)
    for k in range(d+1):
        acc = np.zeros(a.shape[1:], dtype=object)
        for i in range(k+1):
            acc += a[i]*(comb(k, i)*(scale//comb(d, i)))
        out[k] = acc
    return np.moveaxis(out, 0, axis), scale


def power_to_bern_int(arr):
    scale = 1
    for axis in range(arr.ndim):
        arr, local = bern_int_axis(arr, axis)
        scale *= local
    return arr, scale


def split_axis_int(c, axis):
    """Exact midpoint de Casteljau restriction to the two half-boxes.

    Both children are multiplied by the same positive factor 2^degree along
    the split axis, so signs of all Bernstein coefficients are unchanged.
    """
    a = np.moveaxis(c, axis, 0)
    d = a.shape[0]-1
    left = np.zeros_like(a, dtype=object)
    right = np.zeros_like(a, dtype=object)
    for k in range(d+1):
        acc = np.zeros(a.shape[1:], dtype=object)
        for j in range(k+1):
            acc += a[j]*comb(k, j)
        left[k] = acc*(1 << (d-k))

        acc = np.zeros(a.shape[1:], dtype=object)
        dd = d-k
        for j in range(dd+1):
            acc += a[k+j]*comb(dd, j)
        right[k] = acc*(1 << k)
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)


def int_minmax(a):
    it = iter(a.flat)
    first = next(it)
    mn = mx = first
    for z in it:
        if z < mn:
            mn = z
        if z > mx:
            mx = z
    return mn, mx


def root_bernstein(n):
    return power_to_bern_int(compact_power_tensor_int(n))[0]


def parse_path(path):
    if not path:
        return []
    out = []
    for token in path.strip(',').split(','):
        if len(token) != 2 or token[0] not in '012' or token[1] not in 'LR':
            raise ValueError(f"invalid path token {token!r}")
        out.append((int(token[0]), token[1]))
    return out


def restrict_path(coeff, path):
    depth = [0, 0, 0]
    for axis, side in parse_path(path):
        left, right = split_axis_int(coeff, axis)
        coeff = left if side == 'L' else right
        depth[axis] += 1
    return coeff, tuple(depth)
