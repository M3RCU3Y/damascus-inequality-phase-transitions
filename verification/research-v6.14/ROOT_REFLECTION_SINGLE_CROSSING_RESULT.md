# Reciprocal root-reflection single-crossing lemma

Let

\[
\phi_\alpha(t)=\frac{t^\alpha-1}{t^{\alpha+1}+1},\qquad
h_\alpha(t)=t\phi_\alpha'(t),\qquad t>0.
\]

Fix `0<nu<mu`, `lambda>1`, and `gamma<0`, and put

\[
f(t)=h_\mu(t)-\lambda h_\nu(t)-\gamma.
\]

For `t>1` define

\[
R(t)=\frac{\phi_\mu(t)}{\phi_\nu(t)},\qquad
B_\nu(t)=\frac{t\phi_\nu(t)}{t-1}.
\]

The V6.14 ratio theorem gives that `R` is strictly decreasing on `(1,infinity)`,
from `mu/nu` to `1`.

## Lemma 1: B_nu is strictly decreasing

A direct differentiation gives

\[
B_\nu'(t)=\frac{N_\nu(t)}{(t-1)^2(t^{\nu+1}+1)^2},
\]

where

\[
N_\nu(t)=1-t^{2\nu+2}+(\nu+1)t^\nu(t^2-1).
\]

Write `t=e^x`, `x>0`.  After division by the positive factor `t^(nu+1)`,

\[
t^{-\nu-1}N_\nu(t)
=-2\sinh((\nu+1)x)+2(\nu+1)\sinh x<0,
\]

because `sinh(kx)>k sinh(x)` for `k>1` and `x>0`.  Hence

\[
\boxed{B_\nu'(t)<0\quad(t>1).}
\]

## Lemma 2: reciprocal defect at a positive root

Differentiating the reciprocity identity

\[
\phi_\alpha(t^{-1})=-t\phi_\alpha(t)
\]

with respect to `log t` yields

\[
h_\alpha(t^{-1})=t\{h_\alpha(t)+\phi_\alpha(t)\}.
\]

Therefore

\[
f(t^{-1})-t f(t)
=(t-1)\gamma+t\phi_\nu(t)(R(t)-\lambda).
\]

In particular, whenever `f(t)=0`,

\[
\boxed{
\frac{f(t^{-1})}{{t-1}}
=\gamma+B_\nu(t)(R(t)-\lambda).
}
\]

## Lemma 3: single crossing

Assume additionally `1<lambda<mu/nu`.  Let `t_lambda>1` be the unique point
with `R(t_lambda)=lambda`.  On `(1,t_lambda)`, both positive factors
`B_nu(t)` and `R(t)-lambda` are strictly decreasing, so their product is
strictly decreasing.  On `[t_lambda,infinity)` that product is nonpositive,
and adding `gamma<0` makes the whole expression strictly negative.
Consequently

\[
E(t)=\gamma+B_\nu(t)(R(t)-\lambda)
\]

has at most one zero on `(1,infinity)`, and any crossing is from positive to
negative.

Thus, along the positive roots of `f`, the sign of the reflected value
`f(1/t)` can change at most once as the positive root moves outward.

This is the analytic single-crossing backbone behind the observed four-root
product inequality.  It does not by itself prove the full product inequality;
that remaining step must compare the cumulative outward displacement of the
two reciprocal lower roots with the two positive roots.
