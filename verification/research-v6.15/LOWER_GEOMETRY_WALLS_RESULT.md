# Certified lower-middle geometry walls and the analytic determinant tail

**Status:** `CERTIFIED-GLOBAL` for source exponents `nu_c < nu <= 6`.

This note packages the exact geometry restrictions needed by the remaining finite determinant certificate and proves that the determinant obstruction is automatically positive for every later target exponent `mu>=85`.

## 1. Source packets inherit exponent-six trace geometry

Let a strict `2+2` source-boundary packet at exponent `nu<=6` be written in the pair chart

\[
xy=t^2,
\qquad
x+y=2t+u(t-1)^2,
\qquad
1<x\le y,
\]

with the coordinate-`1` trace obtained by spreading the lower pair to its boundary.

`GLOBAL_LOW_RADIUS_EXCLUSION_RESULT.md` proves that every relevant source packet lies in the lower-spreading regime. Hence spreading the lower pair to the coordinate-`1` trace strictly increases the source sum. The resulting three-variable trace is therefore positive at exponent `nu`.

The continuous one-below persistence theorem transports that positivity to exponent `6`. The exact exponent-six topology theorem from V6.10 then applies.

### Rational t walls

On the symmetric exponent-six slice,

\[
S_6(t,0)
=-\frac{\text{positive factors}\cdot P_6(t)}{\text{positive denominator}},
\]

where

\[
P_6(t)=t^{10}-2t^9-t^8+3t^7-t^6-3t^5+3t^4+2t^3-3t^2+2.
\]

The exact Sturm theorem in V6.10 gives one root in `(1,3/2)` and one in `(3/2,2)`, with positivity only between them. The replay verifies

\[
P_6(57/50)>0,
\qquad
P_6(39/20)>0.
\]

Therefore every positive exponent-six trace, hence every lower-middle source packet, satisfies

\[
\boxed{
\frac{57}{50}<t<\frac{39}{20}.
}
\]

## 2. Exact upper-spread wall u<1/4

At `u=1/4`, the exponent-six trace numerator factors as

\[
-\frac{(t-1)^2(t+1)^2(t^2+1)(5t^2+6t+5)}{16384}\,P_{20}(t),
\]

where

\[
\begin{aligned}
P_{20}(t)={}&2458t^{20}-7848t^{19}+8858t^{18}-5928t^{17}+6998t^{16}
-10944t^{15}+8710t^{14}-864t^{13}\\
&-2976t^{12}+864t^{11}+2976t^{10}-864t^9-2157t^8+4788t^7
+1414t^6-3804t^5\\
&+3836t^4-156t^3+5954t^2-7884t+6553.
\end{aligned}
\]

Exact Bernstein conversion proves `P20>0` separately on `[1,3/2]` and `[3/2,2]`. The minimum Bernstein coefficients are respectively

\[
9984,
\qquad
\frac{38197892297}{524288}.
\]

The exponent-six topology theorem says every nonnegative fixed-product section is strictly decreasing in `u`. Therefore

\[
\boxed{u<\frac14}
\]

for every positive exponent-six trace and hence every lower-middle source packet.

## 3. Exact smaller-radius wall

Let the smaller above-one radius be `y`. Suppose `y<=28/25`. By the rational `t` wall, every positive trace has `xy=t^2<4`, so

\[
y\le x<4/y.
\]

Parameterize the enlarged domain by

\[
y=1+\frac3{25}s,
\qquad
x=y+w\left(\frac4y-y\right),
\qquad 0\le s,w\le1.
\]

After substituting into the exact exponent-six three-variable trace and clearing the positive denominator, the negative numerator is a bivariate polynomial of degree `(35,14)`. Exact rational Bernstein subdivision proves it nonnegative on the full unit square. The frozen deterministic traversal closes in

\[
\boxed{21\text{ nodes},\quad11\text{ leaves},\quad\text{maximum depth }10.}
\]

Hence no exponent-six violation can have `y<=28/25`. Therefore

\[
\boxed{y>\frac{28}{25}}
\]

for every lower-middle source packet.

## 4. Continuous source upper-spread curvature

For

\[
L_\alpha(z)=z h_\alpha'(z),
\]

`lower_geometry_walls.py` applies outward-rounded Decimal interval arithmetic to the enlarged domain

\[
\nu_c\le\alpha\le6,
\qquad
1\le y\le x,
\qquad
xy\le4.
\]

Using

\[
x=y+w(4/y-y),
\qquad0\le w\le1,
\]

it certifies

\[
\boxed{
L_\alpha(x)+L_\alpha(y)<0.
}
\]

For a fixed-product upper pair

\[
x=te^d,
\qquad y=te^{-d},
\]

this is exactly the derivative of

\[
h_\alpha(x)-h_\alpha(y)
\]

with respect to the spread. Since that difference vanishes at `d=0`, one obtains

\[
\boxed{F_{\alpha,d}<0}
\]

for every nonzero upper split. Equivalently, the regularized pair-chart derivative satisfies

\[
\boxed{F_{\alpha,u}<0}
\]

throughout the lower-middle source range.

## 5. Analytic target-curvature tail from mu=85 onward

For `z>1`, the sign of `h'_\mu(z)` is the sign of

\[
P_\mu(z)=z^{2\mu+2}-(\mu+1)^2z^{\mu+2}
-(\mu^2+4\mu+1)z^{\mu+1}
+(\mu+1)^2z+\mu^2.
\]

After division by the positive factor `z^(2mu+2)`, it is enough to prove

\[
(\mu+1)^2 z^{-\mu}
+(\mu^2+4\mu+1)z^{-\mu-1}<1,
\]

because the remaining two terms are positive.

The geometry wall gives `z>=28/25` for both above-one radii. The replay checks exactly at `mu=85` that

\[
86^2\left(\frac{25}{28}\right)^{85}
+7566\left(\frac{25}{28}\right)^{86}<1.
\]

Both terms decrease strictly for all real `mu>=85`. Indeed

\[
\log\frac{28}{25}>\frac3{28},
\]

while

\[
\frac2{\mu+1}<\frac3{28},
\qquad
\frac{2\mu+4}{\mu^2+4\mu+1}<\frac3{28}
\]

for `mu>=85`.

Therefore

\[
\boxed{
h'_\mu(z)>0
\qquad(\mu\ge85,\ z\ge28/25).}
\]

Hence the target upper-pair response satisfies

\[
\boxed{F_{\mu,u}>0}
\qquad(\mu\ge85).
\]

The global low-radius theorem and real lower-spreading theorem give simultaneously

\[
F_{\nu,v}>0,
\qquad F_{\mu,v}>0,
\]

while Section 4 gives `F_{nu,u}<0`. Consequently the pair-chart stationarity determinant

\[
J^{\rm pair}_{\nu,\mu}
=F_{\mu,u}F_{\nu,v}-F_{\mu,v}F_{\nu,u}
\]

satisfies

\[
\boxed{
J^{\rm pair}_{\nu,\mu}>0
\qquad
(\nu_c<\nu\le6,\ \mu\ge85).
}
\]

Thus every possible four-distinct stationary competitor in the lower-middle region is already excluded analytically for target exponent at least `85`.

## 6. Remaining finite lower core

The only lower-middle determinant problem left is now the compact range

\[
\boxed{
\nu_c<\nu\le6,
\qquad
\nu<\mu<85,
}
\]

with the exact geometry restrictions

\[
\boxed{
57/50<t<39/20,
\qquad
u<\mu<85,
\qquad
u_c<\nu\le6,
\qquad
u<\mu,
\qquad
u<\mu,
}
\]

and, more usefully,

\[
\boxed{
u_c<\nu\le6,\quad 57/50<t<39/20,\quad u<1/4,\quad y>28/25.}
\]

The final certificate should operate only on actual source/target double-boundary packets inside this compact tube.

## Replay

Run

```bash
python lower_geometry_walls.py
```

The polynomial/Bernstein decisions are exact rational computations. The continuous curvature statement uses outward-rounded interval arithmetic.
