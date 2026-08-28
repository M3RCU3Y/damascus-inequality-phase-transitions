#!/usr/bin/env python3
"""Validated transport certificate for the full right-half-plane theorem."""
from __future__ import annotations

from decimal import Decimal

import fixed_slice_zero_width_certificate as B

ALPHA0 = B.M0
ROOT_STEPS = 55
ROOT_CACHE = {}


def adaptive_fm(mlo, mhi, qlo, qhi, depth=0, maxdepth=28):
    M = B.I(mlo, mhi)
    Q = B.I(qlo, qhi)
    Fm, _ = B.FD(M, Q, 'm')
    if Fm.d.lo > 0:
        return 1, Fm.d.lo, depth
    if depth >= maxdepth:
        raise AssertionError(('F_m certificate failed', mlo, mhi, qlo, qhi, Fm.d))
    mw = (mlo + mhi) / 2
    qw = (qlo + qhi) / 2
    if (mhi-mlo)/mlo > (qhi-qlo)/qlo:
        a = adaptive_fm(mlo, mw, qlo, qhi, depth+1, maxdepth)
        b = adaptive_fm(mw, mhi, qlo, qhi, depth+1, maxdepth)
    else:
        a = adaptive_fm(mlo, mhi, qlo, qw, depth+1, maxdepth)
        b = adaptive_fm(mlo, mhi, qw, qhi, depth+1, maxdepth)
    return a[0]+b[0], min(a[1], b[1]), max(a[2], b[2])


def phi_log(alpha, u):
    return ((B.D1(alpha) * u).exp() - 1) / ((B.D1(alpha+1) * u).exp() + 1)


def source_value(m, q, dervar=None):
    M = B.D1(m, 1 if dervar == 'm' else 0)
    Q = B.D1(q, 1 if dervar == 'q' else 0)
    c = B.D1(B.C)
    lq = Q.ln()
    ur = lq / M
    ua = -ur - 2*c
    return 2*phi_log(ALPHA0, c) + phi_log(ALPHA0, ur) + phi_log(ALPHA0, ua)


def jacobian_numerator(box_m, box_q):
    Fm, _ = B.FD(box_m, box_q, 'm')
    Fq, _ = B.FD(box_m, box_q, 'q')
    Hm = source_value(box_m, box_q, 'm')
    Hq = source_value(box_m, box_q, 'q')
    return Hm.d * Fq.d - Hq.d * Fm.d


def root_bracket(m, steps=ROOT_STEPS):
    m = m if isinstance(m, Decimal) else Decimal(str(m))
    key = (m, steps)
    if key in ROOT_CACHE:
        return ROOT_CACHE[key]
    lo = B.QL.lo
    hi = B.QU.lo
    M = B.I(m)
    Flo, _ = B.FD(M, B.I(lo), None)
    Fhi, _ = B.FD(M, B.I(hi), None)
    assert Flo.v.hi < 0 and Fhi.v.lo > 0, (m, Flo.v, Fhi.v)
    for _ in range(steps):
        mid = (lo + hi) / 2
        Fmid, _ = B.FD(M, B.I(mid), None)
        if Fmid.v.hi < 0:
            lo = mid
        elif Fmid.v.lo > 0:
            hi = mid
        else:
            raise AssertionError(('ambiguous midpoint sign', m, mid, Fmid.v))
    ROOT_CACHE[key] = (lo, hi)
    return lo, hi


def adaptive_j_tube(mlo, mhi, depth=0, maxdepth=38):
    # F_m>0 and F_q>0 imply q_m decreases with m.
    b_lo, _ = root_bracket(mhi)
    _, a_hi = root_bracket(mlo)
    J = jacobian_numerator(B.I(mlo, mhi), B.I(b_lo, a_hi))
    if J.lo > 0:
        return 1, J.lo, depth
    if depth >= maxdepth:
        raise AssertionError(('J tube certificate failed', mlo, mhi, b_lo, a_hi, J))
    mid = (mlo + mhi) / 2
    a = adaptive_j_tube(mlo, mid, depth+1, maxdepth)
    b = adaptive_j_tube(mid, mhi, depth+1, maxdepth)
    return a[0]+b[0], min(a[1], b[1]), max(a[2], b[2])


def tail_source_value():
    M40 = B.I(Decimal('40'))
    rmin = (B.QL.ln() / M40).exp()
    r = B.I(rmin.lo, Decimal(1))
    a = 1 / (r * B.T * B.T)

    def phi_x(alpha, x):
        lx = x.ln()
        return ((B.I(alpha)*lx).exp()-1) / ((B.I(alpha+1)*lx).exp()+1)

    H = 2*phi_x(ALPHA0, B.T) + phi_x(ALPHA0, r) + phi_x(ALPHA0, a)
    assert H.lo > 0, H
    return H


def main():
    m1 = Decimal('40')
    print('RIGHT-HALF-PLANE TRANSPORT CERTIFICATE')

    n, mins, dep = B.adaptive_rect(ALPHA0, m1, B.QL.lo, B.QU.lo)
    print('base rectangle boxes', n, 'min F_q,D_q', mins, 'depth', dep)

    nfm, mfm, dfm = adaptive_fm(ALPHA0, m1, B.QL.lo, B.QU.lo)
    print('F_m boxes', nfm, 'margin', mfm, 'depth', dfm)

    nj, mj, dj = adaptive_j_tube(ALPHA0, m1)
    print('J-tube slabs', nj, 'margin', mj, 'depth', dj,
          'root brackets', len(ROOT_CACHE))

    htail = tail_source_value()
    print('tail source-value interval', htail)
    print('CONCLUSION: S_alpha0(X_m(q_m))>0 for every m>alpha0')
    print('Combined with the single-transient theorem, all alpha0<=nu<m are positive.')
    print('RIGHT-HALF-PLANE CERTIFICATE PASSED')


if __name__ == '__main__':
    main()
