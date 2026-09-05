# Global low-radius exclusion in the continuous middle strip

**Status:** `CERTIFIED-GLOBAL` on the full source strip `nu_c <= alpha <= nu_dagger`.

Let

\[
\phi_\alpha(t)=\frac{t^\alpha-1}{t^{\alpha+1}+1},
\qquad
h_\alpha(t)=t\phi_\alpha'(t),
\]

and write an ordered strict `2+2` point as

\[
X(c,d,e)=\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
\qquad 0\le d<e<c.
\]

Put

\[
t=e^c,
\qquad
T_\alpha=1+\frac4{\alpha^2}.
\]

Then throughout the full continuous middle strip

\[
\boxed{\nu_c\le\alpha\le\nu_\dagger}
\]

one has

\[
\boxed{
1<t\le T_\alpha
\quad\Longrightarrow\quad
S_\alpha^4(X)\le0.
}
\]

Thus every nontrivial source-boundary packet in the unresolved strip satisfies

\[
\boxed{t>T_\alpha.}
\]

Combined with `REAL_LOWER_SPREADING_RESULT.md`, every relevant double-boundary packet therefore has

\[
\boxed{F_{\alpha,e}>0}
\]

at both source and later target exponents.

## 1. A universal above-one monotonicity box

The derivative numerator from V6.14 is

\[
h_\alpha'(z)
=\frac{z^{\alpha-1}P_\alpha(z)}{(1+z^{\alpha+1})^3},
\]

where

\[
P_\alpha(z)=z^{2\alpha+2}-(\alpha+1)^2z^{\alpha+2}
-(\alpha^2+4\alpha+1)z^{\alpha+1}
+(\alpha+1)^2z+\alpha^2.
\]

Since `T_alpha` decreases with `alpha`, every low-radius trace has both above-one radii in

\[
1\le z\le Z_*,
\qquad
Z_*:=T_{\nu_c}^2
=1.5679706351955372905\ldots.
\]

`low_radius_global_certificate.py` proves with outward-rounded Decimal intervals that

\[
\boxed{
P_\alpha(z)<0
\quad
(\nu_c\le\alpha\le\nu_\dagger,\ 1\le z\le Z_*).
}
\]

The adaptive proof closes in 49 nodes, 25 terminal boxes, maximum depth 6.  Its weakest certified upper bound is still negative.

Hence

\[
\boxed{h_\alpha'(z)<0}
\]

throughout this whole universal radius box.

Therefore, on a coordinate-`1` three-variable trace with fixed above-pair product `xy=t^2`, the above-pair contribution is strictly decreased by splitting the pair.  Indeed for

\[
x=te^d,\qquad y=te^{-d},
\]

\[
\frac{d}{dd}\{\phi_\alpha(x)+\phi_\alpha(y)\}
=h_\alpha(x)-h_\alpha(y)<0
\quad(d>0).
\]

Thus every low-radius coordinate-`1` trace is maximized by equal-above geometry.

## 2. A universal lower bound for the three-variable onset curve

For the equal-above trace

\[
G_\alpha(t)=2\phi_\alpha(t)-t^2\phi_\alpha(t^2),
\qquad 1<t<2,
\]

put

\[
p=t^\alpha.
\]

Clearing the positive denominator gives the exact factorization

\[
\operatorname{num}G_\alpha(t)
=-(p-1)Q(t,p),
\]

where

\[
\boxed{
Q(t,p)=t^2\{(t-2)p^2+(t+1)p+1\}-2.
}
\]

For fixed `t in (1,2)`, `Q(t,p)` is strictly concave in `p`, and

\[
Q(t,1)=2(t^3-1)>0.
\]

Write

\[
t=1+y^2,
\qquad0<y<1.
\]

The certificate proves

\[
\boxed{
\frac{d^2}{dy^2}Q(1+y^2,e^{2y})>0
\quad(0\le y\le1).
}
\]

It closes in 139 nodes, 70 terminal boxes, maximum depth 8.  Direct differentiation gives

\[
Q(1,1)=0,
\qquad
\frac d{dy}Q(1+y^2,e^{2y})\bigg|_{y=0}=0,
\]

so strict positivity of the second derivative implies

\[
\boxed{Q(1+y^2,e^{2y})>0\quad(0<y<1).}
\]

Now if

\[
\alpha\le\frac2y=\frac2{\sqrt{t-1}},
\]

then

\[
p=t^\alpha
\le t^{2/y}
=\exp\!\left(\frac2y\log(1+y^2)\right)
<e^{2y},
\]

because `log(1+y^2)<y^2`.

Since `1<p<e^(2y)` and `Q(t,p)` is concave while positive at both endpoints `p=1` and `p=e^(2y)`, one gets

\[
Q(t,t^\alpha)>0.
\]

Therefore

\[
\boxed{
\alpha\le\frac2{\sqrt{t-1}}
\quad\Longrightarrow\quad
G_\alpha(t)<0.
}
\]

Equivalently, the exact three-variable onset curve obeys the global bound

\[
\boxed{
\eta(t)>\frac2{\sqrt{t-1}}
\qquad(1<t<2).
}
\]

In particular,

\[
t\le1+\frac4{\alpha^2}
\quad\Longrightarrow\quad
G_\alpha(t)<0.
\]

By Section 1, *every* coordinate-`1` trace in this low-radius region is therefore strictly negative, not only the equal-above trace.

## 3. Exclusion of the full strict 2+2 low box

Fix `alpha` in the middle strip and consider the closed ordered low-radius region

\[
1\le t\le T_\alpha,
\qquad0\le d\le e\le c.
\]

Its relevant boundary pieces are:

- `t=1`: the identity, with value zero;
- `e=d`: the reciprocal-pair wall, strictly negative by reciprocity;
- `e=c`: the coordinate-`1` trace, strictly negative by Sections 1--2;
- `t=T_alpha`: `REAL_LOWER_SPREADING_RESULT.md` gives `partial_e S_alpha^4>0`, so this entire face is bounded above by its `e=c` trace and is strictly negative.

If a positive low-radius point existed, continuity and the standard escape/compactness reduction would give a positive maximum.  The listed boundary pieces cannot carry it, so the maximum would occur in the interior of the strict `2+2` sign sector.  V6.14 proves that such a sector has no interior constrained critical point for any real exponent.  Contradiction.

Hence

\[
\boxed{
S_\alpha^4\le0
\quad
(\nu_c\le\alpha\le\nu_\dagger,\ 1<t\le1+4/\alpha^2).
}
\]

## 4. Consequence for V6.15

Every source-boundary packet in the unresolved continuous strip lies in

\[
t>T_\nu.
\]

Since `T_alpha` strictly decreases with the exponent, every later target `mu>nu` obeys

\[
t>T_\nu>T_\mu.
\]

Therefore the real lower-spreading theorem applies simultaneously at source and target:

\[
\boxed{
F_{\nu,e}>0,
\qquad
F_{\mu,e}>0.
}
\]

This removes the last low-radius denominator-sign caveat from the compact determinant problem.

## Replay

Run

```bash
python low_radius_global_certificate.py
```

The interval decisions are rigorous; the reduction from the two validated signs to the low-radius exclusion is analytic.
