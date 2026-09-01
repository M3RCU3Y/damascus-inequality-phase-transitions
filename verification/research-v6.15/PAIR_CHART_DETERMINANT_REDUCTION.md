# Pair-chart regularization of the middle-strip determinant

**Status:** `IDENTITY` / exact coordinate reduction.  This note does not assert the remaining determinant sign.

The raw `(c,d,e)` determinant has forced zeros at the equal-above face `d=0`.  The pair-product chart removes that degeneracy and is the preferred coordinate system for the compact V6.15 certificate.

## 1. Pair-product chart

Put

\[
t=e^c>1.
\]

For the two above-one radii `x>=y>1` and the reflected lower radii `b>=a>1`, write

\[
xy=ab=t^2,
\]

\[
x+y=2t+u(t-1)^2,
\qquad
a+b=2t+v(t-1)^2.
\]

The ordered strict `2+2` chamber is

\[
\boxed{0<u<v<1.}
\]

The boundary meanings are exact:

- `u=0`: `x=y=t`, the equal-above family;
- `v=u`: the two reflected pairs coincide, the reciprocal-pair wall;
- `v=1`: one lower coordinate is `1`, the three-variable trace.

In terms of the log-spreads,

\[
2t\cosh d=2t+u(t-1)^2,
\]

\[
2t\cosh e=2t+v(t-1)^2.
\]

Hence

\[
\frac{du}{dd}=\frac{2t\sinh d}{(t-1)^2}>0,
\qquad
\frac{dv}{de}=\frac{2t\sinh e}{(t-1)^2}>0
\]

in the strict chamber.

## 2. Source/target function in pair variables

Let

\[
F_\alpha(t,u,v)
=\phi_\alpha(x)+\phi_\alpha(y)
-a\phi_\alpha(a)-b\phi_\alpha(b).
\]

This is exactly the original four-variable sum because

\[
\phi_\alpha(1/z)=-z\phi_\alpha(z).
\]

Define

\[
h_\alpha(z)=z\phi_\alpha'(z),
\]

and

\[
g_\alpha(z)=z\{\phi_\alpha(z)+h_\alpha(z)\}.
\]

The reciprocal derivative identity gives the useful interpretation

\[
\boxed{g_\alpha(z)=h_\alpha(1/z).}
\]

## 3. Exact regular divided differences

At fixed product `xy=t^2`, differentiation of the quadratic root equations gives

\[
\frac{dx}{d(x+y)}=\frac{x}{x-y},
\qquad
\frac{dy}{d(x+y)}=-\frac{y}{x-y}.
\]

Therefore

\[
\boxed{
F_{\alpha,u}
=(t-1)^2\frac{h_\alpha(x)-h_\alpha(y)}{x-y}.
}
\]

The quotient has the regular equal-pair limit

\[
\boxed{
F_{\alpha,u}(t,0,v)
=(t-1)^2 h_\alpha'(t).
}
\]

Likewise, differentiating

\[
a\phi_\alpha(a)+b\phi_\alpha(b)
\]

at fixed `ab=t^2` gives

\[
\boxed{
F_{\alpha,v}
=-(t-1)^2\frac{g_\alpha(b)-g_\alpha(a)}{b-a}.
}
\]

At `v=0` this extends regularly as

\[
\boxed{
F_{\alpha,v}(t,u,0)
=-(t-1)^2 g_\alpha'(t).
}
\]

Thus the pair chart converts the apparent `d` and `e` singular factors into ordinary first divided differences.

## 4. Determinant equivalence

Define the pair-chart orientation determinant

\[
\boxed{
J^{\rm pair}_{\nu,\mu}
=F_{\mu,u}F_{\nu,v}-F_{\mu,v}F_{\nu,u}.
}
\]

By the chain rule,

\[
F_{\alpha,u}=F_{\alpha,d}\frac{dd}{du},
\qquad
F_{\alpha,v}=F_{\alpha,e}\frac{de}{dv}.
\]

Hence

\[
\boxed{
J^{\rm pair}_{\nu,\mu}
=\frac{dd}{du}\frac{de}{dv}
J_{\nu,\mu},
}
\]

where

\[
J_{\nu,\mu}
=F_{\mu,d}F_{\nu,e}-F_{\mu,e}F_{\nu,d}.
\]

The multiplier is strictly positive in the strict chamber, so

\[
\boxed{
\operatorname{sign}J^{\rm pair}_{\nu,\mu}
=\operatorname{sign}J_{\nu,\mu}.
}
\]

The pair determinant is therefore an exactly equivalent stationarity obstruction with much better conditioning at `u=0`.

## 5. Fully normalized certificate target

Each pair derivative contains the factor `(t-1)^2`, and the determinant is antisymmetric in the two exponents.  The natural normalized object is

\[
\boxed{
\mathcal D_{\nu,\mu}(t,u,v)
=\frac{J^{\rm pair}_{\nu,\mu}}
{(\mu-\nu)(t-1)^4}.
}
\]

For `mu>nu` and `t>1`, positivity of `mathcal D` is exactly positivity of the original determinant.

The divided-difference formulas show that the geometry part extends continuously to `u=0` and `v=0`.  Antisymmetry gives a continuous exponent-diagonal extension by replacing the quotient in `(mu-nu)` with the corresponding exponent derivative.

This is the preferred object for interval subdivision.  It removes the three artificial small factors that made the raw determinant poorly conditioned:

- the equal-above spread;
- the lower-pair spread;
- the exponent gap.

## 6. Relation to threshold graphs

Whenever `F_{alpha,v}>0`, the source/target zero surface can locally be written

\[
v=V_\alpha(t,u).
\]

Then

\[
V_{\alpha,u}=-\frac{F_{\alpha,u}}{F_{\alpha,v}},
\]

and at a double-boundary point

\[
\boxed{
J^{\rm pair}_{\nu,\mu}
=F_{\mu,v}F_{\nu,v}
\{V_{\nu,u}-V_{\mu,u}\}.
}
\]

Thus, once the real lower-spreading theorem supplies positive `v`-derivatives, the determinant theorem has a transparent geometric meaning:

> increasing the exponent strictly decreases the sensitivity of the lower-spread threshold to upper-pair splitting.

A global proof of that threshold-slope ordering, or a certified positive lower bound for `mathcal D` on the competitive compact slabs, closes the four-distinct interior case.
