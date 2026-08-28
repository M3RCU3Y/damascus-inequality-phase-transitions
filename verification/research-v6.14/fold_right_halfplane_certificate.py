#!/usr/bin/env python3
"""Validated certificate with the symmetric fold as the exact right-half-plane cutoff.

Combines two pieces:
  1. a quantitative fixed-c implicit-function bridge from the certified fold
     exponent nu_dagger to the rational target M0=7.3596319;
  2. the existing fixed-slice target-boundary transport from M0 to infinity,
     now evaluated at the entire certified nu_dagger interval.

Together with the single-transient theorem, this proves
    I_nu^4 is not contained in I_mu^4
for every nu_dagger <= nu < mu.
"""
from __future__ import annotations

from decimal import Decimal

import fixed_slice_zero_width_certificate as B
import right_halfplane_certificate as R
import symmetric_fold_certificate as SF

NBOX = B.I(SF.CENTER[0] - SF.RAD, SF.CENTER[0] + SF.RAD)
CBOX = B.I(SF.CENTER[1] - SF.RAD, SF.CENTER[1] + SF.RAD)
EBOX = B.I(SF.CENTER[2] - SF.RAD, SF.CENTER[2] + SF.RAD)
M0 = B.M0
BRIDGE_E = Decimal('3e-20')


def bridge_constants():
    """Derivative bounds on the full quantitative local bridge box."""
    box = [
        SF.I(NBOX.lo, M0),
        SF.I(CBOX.lo, CBOX.hi),
        SF.I(EBOX.lo, EBOX.hi + BRIDGE_E),
    ]
    f = SF.build(box)
    fe = f.d[2]
    fnn = f.h[0][0]
    fne = f.h[0][2]
    assert fe.lo > 0
    assert fnn.hi < 0

    a = -fnn.hi
    b = -fnn.lo
    p = fe.lo
    c = max(abs(fne.lo), abs(fne.hi))
    delta = M0 - NBOX.lo
    k = b / (Decimal(2) * p)

    crossing = p * BRIDGE_E - b * delta * delta / Decimal(2)
    dmargin = a - c * k * delta
    assert crossing > 0
    assert dmargin > 0
    return fe, fnn, fne, delta, k, crossing, dmargin


def phi_log(alpha, u):
    """phi_alpha(exp(u)) with interval alpha and dual/interval u."""
    return ((B.D1(alpha) * u).exp() - 1) / (((B.D1(alpha) + 1) * u).exp() + 1)


def source_value(m, q, dervar=None):
    """H(m,q)=S_alpha(X_m(q)), uniformly for alpha in the fold exponent box."""
    M = B.D1(m, 1 if dervar == 'm' else 0)
    Q = B.D1(q, 1 if dervar == 'q' else 0)
    c = B.D1(B.C)
    ur = Q.ln() / M
    ua = -ur - 2*c
    return 2*phi_log(NBOX, c) + phi_log(NBOX, ur) + phi_log(NBOX, ua)


def jacobian_numerator(box_m, box_q):
    """J=H_m F_q-H_q F_m along the target-boundary branch."""
    Fm, _ = B.FD(box_m, box_q, 'm')
    Fq, _ = B.FD(box_m, box_q, 'q')
    Hm = source_value(box_m, box_q, 'm')
    Hq = source_value(box_m, box_q, 'q')
    return Hm.d * Fq.d - Hq.d * Fm.d


def adaptive_j_tube(mlo, mhi, depth=0, maxdepth=38):
    blo, _ = R.root_bracket(mhi, steps=90)
    _, ahi = R.root_bracket(mlo, steps=90)
    J = jacobian_numerator(B.I(mlo, mhi), B.I(blo, ahi))
    if J.lo > 0:
        return 1, J.lo, depth
    if depth >= maxdepth:
        raise AssertionError(('fold-source J tube failed', mlo, mhi, blo, ahi, J))
    mid = (mlo + mhi) / 2
    a = adaptive_j_tube(mlo, mid, depth+1, maxdepth)
    b = adaptive_j_tube(mid, mhi, depth+1, maxdepth)
    return a[0]+b[0], min(a[1], b[1]), max(a[2], b[2])


def start_source_value():
    """H(M0,q_M0)>0 for the entire fold-exponent interval."""
    lo, hi = R.root_bracket(M0, steps=105)
    H = source_value(B.I(M0), B.I(lo, hi), None).v
    assert H.lo > 0
    return H, hi-lo


def tail_source_value():
    """Direct fold-source positivity on the entire fixed slice for m>=40."""
    M40 = B.I(Decimal('40'))
    rmin = (B.QL.ln() / M40).exp()
    r = B.I(rmin.lo, Decimal(1))
    a = 1 / (r * B.T * B.T)

    def phi_x(alpha, x):
        lx = x.ln()
        return ((alpha*lx).exp()-1) / (((alpha+B.I(1))*lx).exp()+1)

    H = 2*phi_x(NBOX, B.T) + phi_x(NBOX, r) + phi_x(NBOX, a)
    assert H.lo > 0
    return H


def main():
    print('FOLD-CUTOFF RIGHT-HALF-PLANE CERTIFICATE')
    print('fold exponent box', NBOX)

    fe, fnn, fne, delta, k, crossing, dmargin = bridge_constants()
    print('local bridge F_e', fe)
    print('local bridge F_nunu', fnn)
    print('local bridge F_nue', fne)
    print('max delta', delta)
    print('root displacement coefficient K', k)
    print('upper-e crossing margin', crossing)
    print('descending derivative coefficient margin', dmargin)

    m1 = Decimal('40')
    n, mins, dep = B.adaptive_rect(M0, m1, B.QL.lo, B.QU.lo)
    print('base fixed-slice boxes', n, 'min F_q,D_q', mins, 'depth', dep)
    nfm, mfm, dfm = R.adaptive_fm(M0, m1, B.QL.lo, B.QU.lo)
    print('F_m boxes', nfm, 'margin', mfm, 'depth', dfm)

    h0, qwidth = start_source_value()
    print('fold-source value at M0 boundary root', h0)
    print('M0 root bracket width', qwidth)

    nj, mj, dj = adaptive_j_tube(M0, m1)
    print('fold-source J-tube slabs', nj, 'margin', mj, 'depth', dj)

    ht = tail_source_value()
    print('fold-source tail interval', ht)
    print('CONCLUSION: every target mu>nu_dagger has a boundary witness')
    print('that is positive at nu_dagger and has a descending target zero.')
    print('Together with the single-transient theorem, every nu_dagger<=nu<mu fails inclusion.')
    print('FOLD-CUTOFF RIGHT-HALF-PLANE CERTIFICATE PASSED')


if __name__ == '__main__':
    main()
