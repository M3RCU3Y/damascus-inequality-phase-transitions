# Full four-variable fixed-exponent topology

## Theorem

Let

\[
\phi_n(t)=\frac{t^n-1}{t^{n+1}+1},\qquad
S_n^4(x)=\sum_{j=1}^4\phi_n(x_j),\qquad \prod_{j=1}^4x_j=1.
\]

Then

\[
\mathcal I_1^4=\varnothing,
\]

and for every integer `n>=2`, the full four-variable violation set
`I_n^4={S_n^4>0}` has exactly four connected components. They are indexed by
which coordinate is the persistent lone coordinate below `1`, and every
component is contractible.

For `n>=4`, the strict `2+2` pockets do not create additional components or
homotopy: each ordered pocket, together with its coordinate-`1` trace, strongly
deformation-retracts onto that trace inside the corresponding persistent
`3+1` component.

The proof uses the uniform ordered-pocket theorem already recorded in
`TOPOLOGY_FOUR_ALL_N_RESULT.md`. The new point here is the topology of the
persistent strict `3+1` cores.

## 1. Sign sectors

A violation cannot have exactly one coordinate above `1`. If `a,b,c>1` and
the point is `(abc,a^{-1},b^{-1},c^{-1})`, put

\[
\tau_n(t)=\frac{t^n-1}{t^n+1}.
\]

For `t>1`, the elementary inequalities used in the three-variable sign
reduction give

\[
\phi_n(t)<\tau_n(t)<t\phi_n(t).
\]

Also `tau_n(a)+tau_n(b)>tau_n(ab)`, and iteration gives

\[
\tau_n(a)+\tau_n(b)+\tau_n(c)>\tau_n(abc).
\]

Using `phi_n(t^{-1})=-t phi_n(t)`, one obtains

\[
S_n^4(abc,a^{-1},b^{-1},c^{-1})
<\tau_n(abc)-\tau_n(a)-\tau_n(b)-\tau_n(c)<0.
\]

Thus a strict four-variable violation is either of type `3+1` or `2+2`.
The settled low-exponent result makes the strict `2+2` locus empty for
`n<=3`; for `n>=4` its complete ordered-pocket topology is supplied by the
uniform V6.13 theorem.

## 2. A labelled persistent `3+1` core

Fix

\[
x_1,x_2,x_3>1>x_4,\qquad x_1x_2x_3x_4=1.
\]

Put `u_i=log x_i>0`, so `x_4=exp(-(u_1+u_2+u_3))`. For a real exponent
`nu>1`, write

\[
F_\nu(u_1,u_2,u_3)=\sum_{i=1}^3\phi_\nu(e^{u_i})
+\phi_\nu(e^{-u_1-u_2-u_3}).
\]

Let `h_nu(t)=t phi_nu'(t)`. At an interior constrained critical point,

\[
h_\nu(x_1)=h_\nu(x_2)=h_\nu(x_3)=h_\nu(x_4).
\]

Since `0<x_4<1`, the common value is positive. On the region `t>1` where
`h_nu(t)>0`, `h_nu` is strictly decreasing. Put `X=t^(nu+1)` and
`C=nu+(nu+1)t`. Exact differentiation gives

\[
-\frac{t^2(X+1)^3}{X}h_\nu'(t)=B_\nu(t,X),
\]

where `B` is a concave quadratic in `X`, with

\[
B_\nu(t,1)=4\nu>0,\qquad
B_\nu(t,C)=\nu(\nu+1)^2(t+1)^2>0.
\]

The condition `h_nu(t)>0` is exactly `1<X<C`, hence `B>0` there. Therefore
all three above-one coordinates of every interior critical point coincide:

\[
\boxed{x_1=x_2=x_3=t.}
\]

## 3. The unique continuous birth of the core

On `(t,t,t,t^{-3})`, set `P=t^(nu+1)`. Exact simplification gives

\[
S_\nu^4(t,t,t,t^{-3})
=\frac{(t-P)Q(t,P)}{t(P+1)(P^2-P+1)},
\]

where

\[
Q(t,P)=(t-3)P^2+(t^2+3)P+t^3-3.
\]

For `1<t<3`, let `P_+(t)>1` be the upper root and define

\[
\eta_4(t)=\frac{\log P_+(t)}{\log t}-1.
\]

Then

\[
S_\nu^4(t,t,t,t^{-3})>0\iff \nu>\eta_4(t).
\]

The function `eta_4` has exactly one critical point, a strict global minimum.
Along `Q(t,P)=0`, put

\[
g(t)=\frac{d\log P}{d\log t}=-\frac{tQ_t}{P Q_P}.
\]

Eliminating `P` from `Q=0` and `g'(t)=0` gives, apart from `t=3`,

\[
\begin{aligned}
H(t)={}&t^{16}-12t^{14}-244t^{12}-96t^{11}+5436t^{10}-15456t^9\\
&+28990t^8-20160t^7+34092t^6-88512t^5+29916t^4\\
&+23328t^3+3492t^2+2592t+729.
\end{aligned}
\]

An exact Sturm count gives exactly two roots in `(1,3)`, isolated in
`(1.0984,1.0985)` and `(1.3623,1.3624)`. The penultimate subresultant is
linear in `P`; exact sign checks show that the first root corresponds to
`P<1`, while the second corresponds to `P>1`. Consequently `g` has exactly
one stationary point on the physical upper branch. Since `g` tends to
`+infinity` at both endpoints, this point is its strict global minimum.

Writing `s=log t` and `G(s)=log P_+(e^s)`, the numerator of `eta_4'` is

\[
A(s)=sG'(s)-G(s),\qquad A'(s)=sG''(s).
\]

Thus `A` first decreases and then increases. Quadratic-root asymptotics give
`A<0` near `t=1`, while `A->+infinity` as `t->3-`; hence `A` has exactly one
zero. Therefore `eta_4` has one strict global minimum

\[
\nu_{31}=1.9270144057329760866\ldots,
\]

at

\[
t_{31}=1.8999751364292390396\ldots.
\]

The decimal values are only a replay. Also `nu_31<2`: at `t=2`,
`Q(2,P)=-P^2+7P+5` and `Q(2,8)=-3`, so the upper root is below `8=2^3`.

At the onset the zero critical point is a nondegenerate maximum. The two shape
directions have second derivative proportional to `t h_nu'(t)<0`; the radial
direction is negative because `eta_4` has a strict nondegenerate minimum and
the upper quadratic root is simple.

## 4. Compactification and continuation

Compactify the core by

\[
y_i=x_i^{-1}\in(0,1),\qquad z=y_1y_2y_3.
\]

Then

\[
\overline F_\nu(y_1,y_2,y_3)
=-\sum_{i=1}^3y_i\phi_\nu(y_i)+\phi_\nu(z)
\]

extends continuously to `[0,1]^3` and is `C^1` at the escape faces for
`nu>1`.

For `nu<nu_31`, no positive point exists. Since `nu_31<2`, the coordinate-1
faces are still below the three-variable onset, while on an escape face

\[
\overline F_\nu(0,y_2,y_3)=\phi_\nu(y_2^{-1})+\phi_\nu(y_3^{-1})-1<0
\]

for `nu<=2`: `phi_nu(t)` is increasing in `nu` for `t>1` and
`max phi_2=1/3`. Thus a hypothetical positive point below `nu_31` would have
an interior positive maximum, forced by Step 2 onto the symmetric spine,
contradicting the definition of `nu_31`.

Immediately above `nu_31`, the Morse lemma gives one open 3-ball. There is no
later interior zero-critical event because every interior critical point is
symmetric and `eta_4` has only one critical value.

Boundary crossings are harmless. On an escape face `y_1=0`, the one-sided
inward derivative is `+1`. On a coordinate-1 face `y_1=1`, a zero critical for
the face is a three-variable critical point. Its remaining above-one
coordinates equal some `t>1`, and the inward normal derivative is

\[
\frac\nu2-h_\nu(z)=\frac\nu2-h_\nu(t)>0,
\]

because `h_nu(1)=nu/2` and `h_nu` is strictly decreasing on its positive
above-one branch. Hence a boundary tangency is transverse in the full core and
has a half-space normal form: it can open or close a collar/end but cannot
create a component or attach a handle.

Lower-dimensional boundary strata are strictly nonpositive except for the
all-one corner. At that corner

\[
\phi_\nu(e^u)=\frac\nu2u-\frac\nu4u^2+O(u^3),
\]

and the product constraint cancels the linear terms, so the punctured sector
is negative near the corner.

The standard continuation/isotopy argument for superlevel sets on a
manifold with corners therefore keeps the homotopy type fixed after the unique
interior birth. Every labelled strict `3+1` core is connected and contractible
for every real `nu>nu_31`, in particular for every integer `n>=2`.

## 5. Gluing the transient pockets

There are four labelled persistent cores, one per choice of the lone below-one
coordinate. For `n=2,3`, the strict `2+2` locus is empty. For `n>=4`, the
uniform ordered-pocket theorem gives twelve strict ordered pockets. Each
pocket augmented by its coordinate-1 trace strongly deformation-retracts onto
that trace, and the trace lies in exactly one persistent core. The opposite
ordering is separated by the equal-below-pair locus, which is nonviolating, so
no pocket bridges two persistent cores.

Retract all pockets simultaneously while leaving the four cores fixed. Each
full component deformation-retracts onto its persistent core. Hence the full
violation set has exactly four connected components and every component is
contractible.

## Replay

Run

```bash
python full_four_topology_audit.py
```

The audit checks the symmetric factorization, positive-branch monotonicity,
the degree-16 elimination polynomial, exact Sturm counts and branch
assignment, boundary derivative identities, and the all-one quadratic
expansion. The displayed onset decimals are a high-precision replay only.
