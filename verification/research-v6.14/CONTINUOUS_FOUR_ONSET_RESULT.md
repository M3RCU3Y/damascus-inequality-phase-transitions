# Exact continuous onset of the strict four-variable 2+2 locus

## Result

Let

\[
\nu_c=3.9826231561383400589\ldots
\]

be the exact three-variable onset defined in the manuscript by

\[
\nu_c=\min_{1<t<2}\eta(t).
\]

Then the strict four-variable `2+2` locus satisfies

\[
\boxed{
\mathcal I_{\nu,2+2}^4\ne\varnothing
\quad\Longleftrightarrow\quad
\nu>\nu_c.}
\]

Consequently the complete four-variable real-exponent inclusion region has an
exact left half-plane:

\[
\boxed{
0<\nu\le\nu_c,\ \mu>\nu
\quad\Longrightarrow\quad
\mathcal I_\nu^4\subseteq\mathcal I_\mu^4.}
\]

Thus the source exponent `nu_c` is the exact point at which transient
four-variable behavior first becomes possible.

## 1. The logarithmic derivative h_nu

Put

\[
\phi_\nu(t)=\frac{t^\nu-1}{t^{\nu+1}+1},
\qquad
h_\nu(t)=t\phi_\nu'(t)
=\frac{t^\nu\{\nu+(\nu+1)t-t^{\nu+1}\}}
       {(1+t^{\nu+1})^2}.
\]

For `0<t<1`, the bracket is positive, so `h_nu(t)>0`.  Direct
differentiation gives

\[
h_\nu'(t)=\frac{t^{\nu-1}P_\nu(t)}{(1+t^{\nu+1})^3},
\]

where

\[
P_\nu(t)=t^{2\nu+2}-(\nu+1)^2t^{\nu+2}
-(\nu^2+4\nu+1)t^{\nu+1}+(\nu+1)^2t+\nu^2.
\]

The ascending real exponents are

\[
0,\ 1,\ \nu+1,\ \nu+2,\ 2\nu+2,
\]

and the corresponding coefficient signs are

\[
+,+,-,-,+.
\]

The generalized Descartes rule for real powers therefore gives at most two
positive zeros of `P_nu`.  Since

\[
P_\nu(0+)=\nu^2>0,\qquad
P_\nu(1)=-4\nu<0,\qquad
P_\nu(t)\to+\infty,
\]

there is exactly one zero in `(0,1)` and exactly one above `1`.
Consequently `h_nu` increases once and then decreases on `(0,1)`.  Moreover

\[
h_\nu(0+)=0,\qquad h_\nu(1)=\nu/2,
\]

and `h_nu'(1)<0`, so the unique lower-side maximum is strictly larger than
`nu/2`.

On the above-one interval where `h_nu>0`, the continuous critical-point lemma
already used for the three- and four-variable persistent cores proves

\[
\boxed{h_\nu'(t)<0\qquad(t>1,\ h_\nu(t)>0).}
\]

Thus every positive above-one level of `h_nu` is attained at most once.

## 2. No interior critical points in a strict 2+2 sector

Fix a strict sign sector

\[
x_1,x_2>1>x_3,x_4,
\qquad x_1x_2x_3x_4=1.
\]

At an interior constrained critical point of `S_nu^4`, logarithmic
Lagrange multipliers give

\[
h_\nu(x_1)=h_\nu(x_2)=h_\nu(x_3)=h_\nu(x_4)=k.
\]

The lower coordinates make `k>0`.  Strict decrease of `h_nu` on its positive
above-one branch therefore forces

\[
x_1=x_2=t>1.
\]

Also `h_nu(t)<h_nu(1)=nu/2`.

If `x_3` and `x_4` are distinct, they would be two distinct points of
`(0,1)` satisfying

\[
h_\nu(x)=k<\nu/2.
\]

But the lower-side shape established above gives exactly one such point:
`h_nu` rises from zero through `k`, reaches a maximum above `nu/2`, and then
stays above `k` all the way to its endpoint value `nu/2`.  This is a
contradiction.

If instead `x_3=x_4`, the product constraint gives `x_3=x_4=t^{-1}`.
Differentiate the reciprocal identity

\[
\phi_\nu(t^{-1})=-t\phi_\nu(t)
\]

with respect to `log t`.  One obtains

\[
\boxed{
h_\nu(t^{-1})=t\bigl(h_\nu(t)+\phi_\nu(t)\bigr)>h_\nu(t),}
\]

again contradicting the critical-point equations.

Hence

\[
\boxed{\text{a strict four-variable 2+2 sector has no interior critical
points for any real }\nu>0.}
\]

## 3. No strict 2+2 violation at or below nu_c

Assume `0<nu<=nu_c`.  First note that `nu_c<4`, because the exact
three-variable theorem has a positive point at exponent `4`.
For `t>1`, `phi_nu(t)` is strictly increasing in the exponent, hence

\[
\phi_\nu(t)<\phi_4(t)<\frac12.
\]

The last inequality is elementary:

\[
\phi_4(t)<\frac12
\iff t^5-2t^4+3>0.
\]

The polynomial on the right has its unique minimum on `(1,infinity)` at
`t=8/5`, where its value is exactly `1183/3125>0`.

Now suppose a strict `2+2` violation existed.  Work in its fixed sign sector.
On a coordinate-`1` boundary face there are two possibilities.

* If a below-one coordinate reaches `1`, the remaining three coordinates
  give a three-variable point.  Its sum is nonpositive because
  `nu<=nu_c` and `nu_c` is the exact three-variable onset.
* If an above-one coordinate reaches `1`, the remaining point has exactly one
  coordinate above `1`; the real-exponent one-above obstruction makes its
  sum strictly negative.

Escape cannot carry a positive maximum.  Along any sequence leaving every
compact subset of the logarithmic `2+2` sector, at least one above-one
coordinate tends to infinity and at least one below-one coordinate tends to
zero.  The former contribution tends to zero, the latter tends to `-1`, the
second below-one contribution is nonpositive, and the remaining above-one
contribution is always strictly less than `1/2`.  Hence the limiting superior
of `S_nu^4` is at most `-1/2`.

Therefore a positive value would force a positive global maximum in the
interior of the sector.  Section 2 proves that no interior critical point
exists.  Contradiction.  Thus

\[
\mathcal I_{\nu,2+2}^4=\varnothing
\qquad(0<\nu\le\nu_c).
\]

## 4. Sharpness of the onset

If `nu>nu_c`, choose a three-variable violation

\[
(x,y,z)\in\mathcal I_\nu^3,
\qquad x,y>1>z.
\]

For `r<1` sufficiently close to `1`, set

\[
X_r=(x/r,y,z,r).
\]

Then `X_r` has product one and lies in a strict `2+2` sector, while

\[
S_\nu^4(X_r)\to S_\nu^3(x,y,z)>0
\qquad(r\uparrow1).
\]

Hence the strict `2+2` locus is nonempty for every `nu>nu_c`.  This proves
the exact onset theorem.

## 5. Exact left half-plane of the inclusion region

Let `0<nu<=nu_c` and `mu>nu`.  A four-variable violation at exponent `nu`
cannot be one-above, by the real-exponent one-above obstruction, and cannot
be `2+2`, by the theorem above.  A coordinate-`1` violation would reduce to a
three-variable violation and is also impossible at or below `nu_c`.
Therefore every source violation lies in a strict one-below `3+1` sector.

The manuscript's continuous one-below persistence theorem then gives

\[
S_\mu^4(X)>S_\nu^4(X)>0.
\]

Thus

\[
\boxed{
\mathcal I_\nu^4\subseteq\mathcal I_\mu^4
\quad\text{for every }0<\nu\le\nu_c\text{ and every }\mu>\nu.
}
\]

Combined with the existing theorem that every source `nu>nu_c` eventually
fails inclusion at sufficiently large target exponent, this identifies
`nu_c` as the exact transition between source exponents with an infinite
forward-inclusion ray and source exponents without one.

## Replay

`continuous_four_onset_audit.py` checks the derivative numerator, reciprocal
`h` identity, endpoint signs, and the exact `phi_4<1/2` escape bound.  The
critical-point and compactness argument is analytic.
