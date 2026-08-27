# Uniform three-variable topology for every integer exponent

## Theorem

For every integer `n>=4`, the three-variable violation set

\[
\mathcal I_n^3
=\{(x,y,z)>0: xyz=1,\ S_n^3(x,y,z)>0\}
\]

has exactly three connected components. Each component is simply connected,
hence contractible; equivalently, each labelled sign sector is homeomorphic
to an open disk.

The three components are indexed by the unique coordinate below one.

This resolves the fixed-exponent topology problem from exponent `7` onward.
The off-axis tongues which first appear at `n=7` do not create extra
components or holes.

## 1. Critical points in a labelled sector are symmetric

Work in the sector

\[
x,y>1>z,\qquad xyz=1.
\]

Define

\[
\phi_n(t)=\frac{t^n-1}{t^{n+1}+1},
\qquad
h_n(t)=t\phi_n'(t).
\]

A direct differentiation gives

\[
h_n(t)=
\frac{t^n\bigl(n+(n+1)t-t^{n+1}\bigr)}{(1+t^{n+1})^2}.
\]

For `0<t<1`, the bracket is positive, hence `h_n(t)>0`.

A second differentiation gives

\[
h_n'(t)=
\frac{t^{n-1}P_n(t)}{(1+t^{n+1})^3},
\]

where

\[
P_n(t)=t^{2n+2}-(n+1)^2t^{n+2}
-(n^2+4n+1)t^{n+1}+(n+1)^2t+n^2.
\]

The nonzero coefficient signs of `P_n` are

\[
+,-,-,+,+,
\]

so Descartes' rule gives at most two positive roots. Since

\[
P_n(0)=n^2>0,
\qquad
P_n(1)=-4n<0,
\qquad
P_n(t)\to+\infty,
\]

there is exactly one root in `(0,1)` and exactly one root in `(1,infinity)`.

Let `beta_n>1` be the unique zero of

\[
n+(n+1)t-t^{n+1}.
\]

At that point exact substitution gives

\[
P_n(\beta_n)
=-n(n+1)^2(\beta_n+1)^2<0.
\]

Therefore the root of `P_n` above one lies strictly after `beta_n`. It follows
that

\[
\boxed{h_n'(t)<0\quad\text{whenever }t>1\text{ and }h_n(t)>0.}
\]

Now use logarithmic coordinates

\[
x=e^u,\qquad y=e^v,\qquad z=e^{-u-v}.
\]

At an interior critical point of `S_n^3`,

\[
h_n(x)=h_n(y)=h_n(z).
\]

Since `z<1`, the common value is positive. Hence both `x` and `y` lie on the
strictly decreasing positive branch of `h_n`, so

\[
\boxed{x=y.}
\]

Thus every interior critical point in a labelled sector lies on the symmetric
slice.

## 2. No interior critical point is a local minimum

Write

\[
x=e^{c+d},\qquad y=e^{c-d},\qquad z=e^{-2c}.
\]

At a symmetric critical point `d=0`, with `t=e^c`,

\[
\frac{\partial^2}{\partial d^2}S_n^3
\bigl(e^{c+d},e^{c-d},e^{-2c}\bigr)\Big|_{d=0}
=2t h_n'(t)<0.
\]

Hence every interior critical point has a strictly negative transverse
direction. In particular:

\[
\boxed{\text{there are no interior local minima in a labelled sector.}}
\]

## 3. The symmetric violation slice is one interval for every `n>=4`

On the symmetric slice `(t,t,t^{-2})`, exact simplification gives

\[
S_n^3(t,t,t^{-2})
=-\frac{(t^n-1)G_n(t)}
{(t^{n+1}+1)(t^{2n+2}+1)},
\]

where

\[
G_n(t)=t^{2n+2}(t-2)+t^{n+2}(t+1)+t^2-2.
\]

Since `G_n(1)=0`, put `t=1+s` and consider `G_n(1+s)/s`.
The coefficient of `s^{r-1}` is

\[
C_r=
\binom{2n+3}{r}-2\binom{2n+2}{r}
+\binom{n+3}{r}+\binom{n+2}{r}+\binom2r.
\]

For `n=4` the signs are

\[
+,+,-,-,-,+,+,+,+,+,+,
\]

and for `n=5` they are

\[
+,-,-,-,-,-,+,+,+,+,+,+,+.
\]

Thus both have exactly two sign changes.

Now suppose `n>=6`. We have

\[
C_1=6>0,
\qquad
C_2=-n^2+3n+6<0.
\]

For `3<=r<=n+1`, the negative contribution from the first two binomial
terms has magnitude

\[
D_r=
\frac{2n+3-2r}{r}\binom{2n+2}{r-1},
\]

while the positive contribution is

\[
E_r=
\frac{2n+6-r}{r}\binom{n+2}{r-1}.
\]

Their ratio is

\[
Q_r=\frac{E_r}{D_r}
=\frac{\binom{n+2}{r-1}}{\binom{2n+2}{r-1}}
\frac{2n+6-r}{2n+3-2r}.
\]

At `r=3`,

\[
Q_3=
\frac{(n+2)(2n+3)}{2(2n+1)(2n-3)}<1,
\]

because the difference between denominator and numerator is

\[
3(2n^2-5n-4)>0.
\]

For `3<=r<=n`, the sign of `Q_{r+1}/Q_r-1` is the sign of

\[
M_n(r)=
-4n^3+6n^2r-12n^2-2nr^2+11nr+9n-9r+27.
\]

As a function of `r`, `M_n(r)` is strictly increasing on `[3,n]`, while

\[
M_n(n)=27-n^2<0.
\]

Hence `Q_{r+1}<Q_r<1`, and therefore

\[
C_r<0\qquad(2<=r<=n+1).
\]

For `r>=n+2`, the large-binomial difference itself is positive, and all
remaining terms are nonnegative, so

\[
C_r>0.
\]

Thus the coefficient list of `G_n(1+s)/s` has exactly two sign changes for
every integer `n>=4`. Descartes' rule gives at most two positive roots.

There are at least two. Indeed,

\[
G_n'(1)=6>0,
\]

and

\[
G_n(3/2)=
-\frac{2a^2}{9}+\frac{5a}{2}+\frac14<0,
\qquad
a=(3/2)^{n+2},
\]

for every `n>=4` (at `n=4` the value is `-217/2048`, and the quadratic is
strictly decreasing for all subsequent values of `a`). Also

\[
G_n(2)=3\,2^{n+2}+2>0.
\]

Consequently there are exactly two roots

\[
1<a_n<\frac32<b_n<2,
\]

and

\[
\boxed{S_n^3(t,t,t^{-2})>0\iff a_n<t<b_n.}
\]

## 4. Connectedness

The established boundedness and coordinate-separation theorem for fixed
integer exponent implies that the closure of the violation set inside each
labelled sector is compact and stays away from the sector boundary.

Let `C` be any connected component of the positive set in the sector. Since
`C` contains a positive point and its boundary has value zero, `S_n^3`
attains a positive maximum at an interior point of `C`. Every such critical
point is symmetric by Section 1.

Therefore every component intersects the symmetric positive interval

\[
a_n<t<b_n.
\]

That interval is itself connected and lies entirely in the violation set, so
two distinct components cannot both meet it. Hence the labelled sector has
exactly one connected component.

The sign-pattern theorem says every violation has exactly one coordinate
below one. There are three choices, and the symmetric interval shows each is
nonempty. Therefore `\mathcal I_n^3` has exactly three connected components.

## 5. No holes and contractibility

Let `V` denote the positive component in one labelled logarithmic sector. It
is a bounded open connected subset of the plane.

Suppose a Jordan curve contained in `V` enclosed a point outside `V`. Because
the sector is convex, the bounded Jordan interior remains inside the same
sector. On the compact closed interior, `S_n^3` has positive boundary values
and a nonpositive interior value, so it attains a local minimum at an interior
point. This contradicts Section 2.

Thus no Jordan curve in `V` encloses a point of the complement. Hence `V` is
simply connected. By the Riemann mapping theorem it is homeomorphic to an open
disk, and in particular is contractible.

This proves the theorem.

## Consequence for the exponent-7 tongues

The exact exponent-7 off-axis witness remains a genuine geometric
bifurcation: fixed-product symmetrization fails. The theorem above shows that
this bifurcation does not alter the component count or create a hole. The
off-axis tongues remain attached to the unique component in their labelled
sign sector.

## Replay

Run

```bash
python topology_all_n_audit.py
```

for exact symbolic checks of the derivative identities and the finite edge
cases, plus an exact combinatorial replay of the coefficient-sign theorem over
a large exponent range. The proof of the uniform inequalities above is
analytic and does not depend on finite sampling.
