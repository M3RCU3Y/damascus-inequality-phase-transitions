# Complete three-variable topology for every integer exponent n >= 7

Status: **proved analytically; exact finite inequalities independently replayed by
`topology_nge7_audit.py`.** This closes the fixed-integer three-variable
topology problem left open in V6.10. Combined with the existing n=4,5,6
certificates, it classifies every nonempty integer-exponent three-variable
violation set.

## Theorem

Let

\[
 \phi_n(r)=\frac{r^n-1}{r^{n+1}+1},\qquad
 S_n(x,y,z)=\phi_n(x)+\phi_n(y)+\phi_n(z),\qquad xyz=1.
\]

For every integer `n >= 7`, the violation set

\[
 \mathcal I_n^3=\{(x,y,z)>0:xyz=1,\ S_n(x,y,z)>0\}
\]

has exactly three connected components, according to which coordinate is below
one. Every component is contractible. More strongly, each labelled sign
sector is a bounded simply connected real-analytic planar domain with one
smooth Jordan boundary, hence is homeomorphic to an open disk.

The boundary has no singular points. In a sector `x,y>1>z`, the two
permutation-related off-axis tongues are not extra components or handles. They
are the two sides of the same disk and attach at the upper symmetric boundary
point by a quadratic fold in the fixed-product projection. In the full
labelled logarithmic chart the boundary itself remains smooth.

Thus, for every integer `n >= 4`, `I_n^3` has exactly three contractible
components. (`n<=3` is empty by the settled low-exponent theorem.)

## 1. Logarithmic chart

Fix the labelled sector `x,y>1>z` and write

\[
 x=e^{c+d},\qquad y=e^{c-d},\qquad z=e^{-2c},
 \qquad c>0,\quad |d|<c.
\]

Put

\[
 F_n(c,d)=S_n(e^{c+d},e^{c-d},e^{-2c}).
\]

The sector is the open wedge `D={(c,d):c>0, |d|<c}`. The function `F_n` is
real analytic and even in `d`.

Define the logarithmic radial derivative

\[
 h_n(r)=r\phi_n'(r)
 =\frac{r^n\bigl(-r^{n+1}+(n+1)r+n\bigr)}{(r^{n+1}+1)^2}.
\]

Then

\[
 \partial_dF_n=h_n(x)-h_n(y),
 \qquad
 \partial_cF_n=h_n(x)+h_n(y)-2h_n(z).
\]

## 2. The one-well lemma for h_n

A direct differentiation gives

\[
 h_n'(r)=\frac{r^{n-1}K_n(r)}{(1+r^{n+1})^3},
\]

where

\[
\begin{aligned}
K_n(r)={}&r^{2n+2}-(n+1)^2r^{n+2}
 -(n^2+4n+1)r^{n+1}\\
&+(n+1)^2r+n^2.
\end{aligned}
\]

Read in descending powers, the nonzero coefficient signs of `K_n` are
`+,-,-,+,+`. Descartes' rule therefore gives at most two positive roots,
counted with multiplicity. But

\[
 K_n(0)=n^2>0,\qquad K_n(1)=-4n<0,
 \qquad K_n(r)\to+\infty,
\]

so there is a root in `(0,1)` and a root in `(1,infinity)`. These are the only
two positive roots and are simple. Write them

\[
 0<\eta_n<1<\rho_n.
\]

Consequently `h_n` is strictly decreasing on `(1,rho_n)` and strictly
increasing on `(rho_n,infinity)`.

Also

\[
 q_n(r)=-r^{n+1}+(n+1)r+n
\]

is positive on `(0,1)`. On `(1,infinity)` it is strictly decreasing, starts
at `q_n(1)=2n`, and tends to `-infinity`. It therefore has one root
`alpha_n>1`. Thus `h_n(r)>0` for `0<r<alpha_n`, `h_n(r)<0` for
`r>alpha_n`, and `alpha_n<rho_n` because `h_n` crosses zero with negative
derivative.

### Corollary: no off-axis critical point

Suppose `d>0` and `partial_d F_n=0`. Then `x>y>1` and
`h_n(x)=h_n(y)`. Strict monotonicity on the two sides of the unique minimum
forces `y<rho_n<x`, and the common value is negative: the right branch of
`h_n` increases from its negative minimum to `0` from below. Since `z<1`,
`h_n(z)>0`. Therefore

\[
 \partial_cF_n=2h_n(x)-2h_n(z)<0.
\]

The case `d<0` is symmetric. Hence

\[
 \boxed{\nabla F_n(c,d)\ne0\text{ at every off-axis point of }D.}
\]

This replaces the fixed-product symmetrization argument which fails beginning
at `n=7`.

## 3. The symmetric slice has exactly one positive interval

On `d=0`, put `t=e^c>1`. Exact simplification gives

\[
 F_n(\log t,0)
 =-\frac{(t^n-1)G_n(t)}
 {(t^{n+1}+1)(t^{2n+2}+1)},
\]

with

\[
 G_n(t)=t^{2n+2}(t-2)+t^{n+2}(t+1)+t^2-2.
\]

Write `G_n(1+s)=sum_k g_(n,k)s^k`. The coefficients satisfy

\[
 g_{n,k}=\binom{2n+2}{k-1}-\binom{2n+2}{k}
 +\binom{n+3}{k}+\binom{n+2}{k}+\binom2k.
\]

(Out-of-range binomial coefficients are zero.) In particular

\[
 g_{n,0}=0,\qquad g_{n,1}=6,
 \qquad g_{n,2}=-n^2+3n+6<0
\]

for `n>=7`.

For `2<=k<=n+1`, set

\[
 A_k=\binom{2n+2}{k}-\binom{2n+2}{k-1},\qquad
 B_k=\binom{n+3}{k}+\binom{n+2}{k}.
\]

Here `A_k,B_k>0`. For `2<=k<=n`, putting `j=n-k>=0`, direct cancellation
shows

\[
\frac{A_{k+1}}{A_k}-\frac{B_{k+1}}{B_k}
=\frac{
 2j^2n+2jn^2+11jn-9j+n^2-27
}{(k+1)(2n+6-k)(2n+3-2k)}.
\]

Every denominator factor is positive in this range, and the numerator is
strictly positive for `n>=7`. Since `A_2>B_2+1` is exactly
`n^2-3n-6>0`, induction gives

\[
 g_{n,k}<0\qquad(2\le k\le n+1).
\]

For `k>=n+2`,

\[
 \binom{2n+2}{k-1}-\binom{2n+2}{k}>0,
\]

and all remaining terms are nonnegative, hence

\[
 g_{n,k}>0\qquad(n+2\le k\le2n+3).
\]

Thus the nonzero coefficients of `G_n(1+s)/s` have exactly two sign changes:
`+,-...-,+...+`. Descartes' rule gives at most two roots of `G_n` above `1`,
counted with multiplicity. Moreover

\[
 G_n'(1)=6>0,\qquad G_n(3/2)<0,\qquad
 G_n(2)=3\,2^{n+2}+2>0.
\]

For the middle sign, if `A=(3/2)^(n+2)` then

\[
 G_n(3/2)=-\frac{2A^2}{9}+\frac{5A}{2}+\frac14<0
\]

for `n>=7`. Hence there are exactly two roots

\[
 1<a_n<\frac32<b_n<2,
\]

one on each side of `3/2`; because Descartes counts multiplicity, both roots
are simple. Therefore

\[
 F_n(c,0)>0
 \quad\Longleftrightarrow\quad
 \log a_n<c<\log b_n.
\]

## 4. Compactness of the positive sector

On either side `|d|=c`, one above-one coordinate equals one and the other is
reciprocal to `z`; hence

\[
 F_n(c,\pm c)
 =\phi_n(e^{2c})+\phi_n(e^{-2c})
 =(1-e^{2c})\phi_n(e^{2c})<0.
\]

Near the wedge vertex, put `f_n(s)=phi_n(e^s)`. Then

\[
 f_n(0)=0,\qquad f_n'(0)=\frac n2,\qquad
 f_n''(0)=-\frac n2.
\]

The three logarithmic coordinates sum to zero, so uniformly for `|d|<=c`,

\[
 F_n(c,d)
 =-\frac n4\bigl((c+d)^2+(c-d)^2+4c^2\bigr)+O(c^3)<0
\]

for sufficiently small `c>0`.

At the other end, for `r>1`, `0<phi_n(r)<1/r`. Let
`m_n=max_(r>=1) phi_n(r)<1`. Since `xy=e^(2c)`, one of `x,y` is at least
`e^c`, and

\[
 \phi_n(x)+\phi_n(y)\le m_n+e^{-c},
 \qquad \phi_n(e^{-2c})\to-1.
\]

Thus `F_n<0` uniformly for large `c`. Together with the strict side-boundary
sign, the positive set

\[
 P_n=\{(c,d)\in D:F_n(c,d)>0\}
\]

is precompact in `D`.

## 5. Connectedness

Let `C` be a connected component of `P_n`. By precompactness, `F_n` attains
a positive maximum on the compact closure of `C`; the maximum is not on the
zero boundary, hence occurs at an interior critical point. Section 2 proves
that no off-axis critical point exists, so the maximum lies on `d=0`.
Therefore every component of `P_n` meets the symmetric axis.

But the positive part of that axis is the single connected interval

\[
 (\log a_n,\log b_n)\times\{0\}.
\]

That entire interval belongs to one component. Since every component meets it,
there can be only one. Thus `P_n` is connected.

## 6. Boundary regularity and absence of holes

At an off-axis zero of `F_n`, if `partial_dF_n` is nonzero then the gradient
is nonzero; if `partial_dF_n=0`, Section 2 gives `partial_cF_n<0`. Hence every
off-axis boundary point is regular.

On the axis the only zeros are `log a_n` and `log b_n`, and both symmetric
roots are simple. Thus `partial_cF_n` is nonzero there as well. Consequently
`partial P_n` has no singular points and is a compact smooth real-analytic
one-manifold.

There is also no hole. If a bounded complementary component existed, the
regular zero boundary would enclose an open region where `F_n<0`. On its
compact closure `F_n` would attain a strictly negative interior minimum. By
Section 2 that critical point would have to lie on the axis. But outside the
single positive axis interval, the two negative axis rays connect directly to
the exterior of the precompact domain, so no point of either ray can lie in a
bounded complementary component. Contradiction.

Thus the complement has no bounded component. Since `P_n` is bounded and
connected with smooth boundary, its boundary consists of one Jordan circle.
By the Jordan-Schoenflies theorem, `P_n` is homeomorphic to the open disk. In
particular it is contractible.

## 7. Exact tongue attachment and the n=7 transition

The preceding proof determines the topology without fixed-product
monotonicity. To identify the observed tongue attachment, note that

\[
 \partial_{dd}F_n(c,0)=2t\,h_n'(t),\qquad t=e^c.
\]

We locate the two symmetric roots relative to the unique above-one minimum
`rho_n` of `h_n`.

### Lower root

Let `alpha_n` be the unique root of `h_n` above one. For `n>=7`,
`alpha_n<3/2`. Indeed

\[
 (3/2)^{n+1}>(n+1)(3/2)+n
\]

holds at `n=7` with exact margin `1697/256` and is preserved by induction.
At `t=alpha_n`, use `alpha_n^(n+1)=(n+1)alpha_n+n` to reduce `G_n` to

\[
 G_n(\alpha_n)
 =n^2(\alpha_n-2)(\alpha_n+1)^2
 +3n\alpha_n(\alpha_n^2-1)+2(\alpha_n^3-1).
\]

Since `1<alpha_n<3/2`,

\[
 G_n(\alpha_n)
 <-2n^2+\frac{45}{8}n+\frac{19}{4}<0
\]

for `n>=7`. Hence `a_n<alpha_n<rho_n`, so `h_n'(a_n)<0`.

### Upper root

Put `r_0=39/20`. For all `n>=7`, `K_n(r_0)>0`. A sufficient inequality is

\[
 r_0^{n+1}>(n+1)^2r_0+n^2+4n+1.
\]

At `n=7` its exact margin is

\[
 \frac{160329260481}{25600000000}>0,
\]

and the induction step follows from

\[
 r_0Q_n-Q_{n+1}
 =\frac{1121n^2+642n-3219}{400}>0.
\]

Thus `rho_n<r_0`. Also `G_n(r_0)<0` for every `n>=7`; the exact `n=7`
value is

\[
 -\frac{12857211561564900828351361}
 {13107200000000000000000},
\]

and for larger `n` the negative term

\[
 -\frac{r_0^{n+2}(r_0^n-59)}{20}
\]

only grows in magnitude. Therefore `r_0` lies inside the symmetric positive
interval and `b_n>r_0>rho_n`, so `h_n'(b_n)>0`.

### Local normal form

Let `c_a=log a_n`, `c_b=log b_n`. Simplicity of the symmetric roots gives

\[
 F_c(c_a,0)>0,\qquad F_c(c_b,0)<0.
\]

The implicit-function theorem writes the boundary near either axis point as an
even analytic graph `c=gamma(d)`. Since `F_d=0` on the axis,

\[
 \gamma''(0)=-\frac{2t h_n'(t)}{F_c}.
\]

At the lower point both `h_n'(a_n)<0` and `F_c(c_a,0)>0`, so
`gamma_a''(0)>0`: the violation set begins to the right of the lower
symmetric root, with no lower off-axis tongue.

At the upper point `h_n'(b_n)>0` while `F_c(c_b,0)<0`, hence again
`gamma_b''(0)>0`. More explicitly,

\[
 c= c_b+\kappa_n d^2+O(d^4),\qquad
 \kappa_n=-\frac{b_nh_n'(b_n)}{F_c(c_b,0)}>0.
\]

Therefore points with `c>c_b` and small nonzero `|d|` remain violating even
though the symmetric point at the same product is not. These are exactly the
local off-axis tongues detected by the n=7 rational witness.

Crucially, this is a fold of the **projection onto fixed product**, not a
singularity of the level set: `F_c(c_b,0)` is nonzero, so the full boundary is
smooth there. Reflection `d -> -d` gives the two permutation-related tongue
sides. Since the complete boundary is one Jordan circle and it meets the axis
only at `c_a,c_b`, these sides belong to the same disk and create neither a new
component nor a handle. This is the complete topological attachment pattern.

## 8. Full three-variable conclusion

The settled sign-pattern theorem in V6.9 says every three-variable violation
has exactly one coordinate below one and no coordinate is equal to one. The
identity of that coordinate is path-invariant. The argument above proves that
each of the three labelled sectors is one contractible disk. Hence

\[
 \boxed{\mathcal I_n^3\text{ has exactly three contractible components for
 every integer }n\ge4.}
\]

The n=7 off-axis bifurcation changes fixed-product geometry but **does not
change global topology**.

## Exact replay

Run

```text
python topology_nge7_audit.py
```

The script uses only `fractions.Fraction` and integer arithmetic. It verifies
the exact shifted-coefficient sign pattern and ratio-comparison numerator, the
`39/20` base inequalities and induction margins locating `rho_n<b_n`, the
`3/2` base inequality locating `a_n<alpha_n`, and the symmetric-root sample
signs for `n=7,...,250`. The finite loop is a regression audit. The theorem for
all `n>=7` is the analytic argument above and does not depend on checking
finitely many exponents.
