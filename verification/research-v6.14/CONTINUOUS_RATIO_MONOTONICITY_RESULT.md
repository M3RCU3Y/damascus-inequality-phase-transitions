# Monotonic exponent-ratio lemma

## Result

For real exponents `0 < nu < mu`, define

\[
R_{\nu,\mu}(t)=\frac{\phi_\mu(t)}{\phi_\nu(t)},
\qquad
\phi_\alpha(t)=\frac{t^\alpha-1}{t^{\alpha+1}+1},
\]

for `t != 1`, and extend continuously at `t=1`. Then

\[
\boxed{R_{\nu,\mu}(1/t)=R_{\nu,\mu}(t)}
\]

and `R_{nu,mu}` is strictly decreasing on `(1,infinity)`. More precisely,

\[
\boxed{1<R_{\nu,\mu}(t)<\frac\mu\nu\qquad(t>1),}
\]

with

\[
R_{\nu,\mu}(t)\to\frac\mu\nu\quad(t\downarrow1),
\qquad
R_{\nu,\mu}(t)\to1\quad(t\to\infty).
\]

This is the weighted-rearrangement form of the continuous radial multiplier
lemma and is useful for the unresolved four-variable inclusion boundary.

## Proof

For every `alpha>0` and `t != 1`, put

\[
\kappa_\alpha(t)
=\frac{\partial_\alpha\phi_\alpha(t)}{\phi_\alpha(t)}.
\]

The continuous radial multiplier theorem gives

\[
\kappa_\alpha(1/t)=\kappa_\alpha(t)
\]

and strict decrease of `kappa_alpha(t)` for `t>1`.

Because `phi_alpha(t)` has a fixed nonzero sign as `alpha` varies over a
positive compact interval,

\[
\log R_{\nu,\mu}(t)
=\log|\phi_\mu(t)|-\log|\phi_\nu(t)|
=\int_\nu^\mu \kappa_\alpha(t)\,d\alpha.
\]

Reciprocal invariance follows immediately. If `1<t_1<t_2`, then for every
`alpha in [nu,mu]`,

\[
\kappa_\alpha(t_1)>\kappa_\alpha(t_2).
\]

Integrating this strict inequality gives

\[
R_{\nu,\mu}(t_1)>R_{\nu,\mu}(t_2).
\]

Finally, the expansion

\[
\phi_\alpha(t)=\frac\alpha2(t-1)+O((t-1)^2)
\]

gives the limit `mu/nu` at `t=1`, while

\[
\phi_\alpha(t)=t^{-1}(1+o(1))
\]

for every fixed `alpha>0` gives the limit `1` at infinity. Strict monotonicity
therefore yields the displayed two-sided bound.

## Boundary-balance corollary

Write a strict `2+2` point using above-one radii `x,y>1` and reciprocal
below-one radii `a,b>1`, so `xy=ab`. On a source boundary `S_nu=0`,

\[
\phi_\nu(x)+\phi_\nu(y)
=a\phi_\nu(a)+b\phi_\nu(b).
\]

Hence for every target `mu>nu`,

\[
S_\mu
=\phi_\nu(x)R_{\nu,\mu}(x)
 +\phi_\nu(y)R_{\nu,\mu}(y)
 -a\phi_\nu(a)R_{\nu,\mu}(a)
 -b\phi_\nu(b)R_{\nu,\mu}(b).
\]

Thus the finite inclusion problem is exactly a comparison of two equal-mass
weighted averages of a strictly decreasing reciprocal-invariant multiplier.
Any global symmetrization theorem must exploit the additional product/interlacing
structure; pointwise fixed-fiber monotonicity is not required.
