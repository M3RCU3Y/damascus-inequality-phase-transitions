# Certified stationary fold in the equal-above 2+2 family

## Result

Consider the symmetric strict `2+2` family

\[
X(c,e)=(e^c,e^c,e^{-c+e},e^{-c-e}),\qquad 0<e<c,
\]

and write

\[
F(\nu,c,e)=S_\nu^4(X(c,e)).
\]

There is a unique solution in the box of radius `10^-20` about

\[
(\nu,c,e)=
(7.3596318961093494297131900223\ldots,
 0.5378803623608122497947438140\ldots,
 0.5018998670017891359992347472\ldots)
\]

to the stationary-fold equations

\[
F=0,\qquad F_\nu=0,\qquad
F_{\nu c}F_e-F_{\nu e}F_c=0.
\]

The solution is nondegenerate. In particular, throughout the certified box,

\[
F_{\nu\nu}<0
\]

and the second derivative of `F_nu` along the local source boundary `F=0` in
the `c` direction is strictly positive.

In transformed coordinates the certified centre is

\[
\boxed{\nu_\dagger=7.3596318961093494297131900223\ldots},
\]

\[
t=e^c=1.7123734016209396883693385160\ldots,
\]

\[
r=e^{-c+e}=0.9646591086292099946878430381\ldots,
\qquad a=e^{-c-e}=0.3535323694559284502603093436\ldots,
\]

and

\[
q=r^{\nu_\dagger}=0.7673569499810071921800335019\ldots.
\]

This is a rigorous local symmetric-family theorem. It does not by itself
prove that the fold is the global four-variable inclusion-collapse point;
that remaining statement requires the global equal-above extremality theorem.

## Why these are the correct fold equations

At a fixed geometry, a collapse of the transient exponent interval is a double
zero of the exponent history, hence

\[
F=F_\nu=0.
\]

The symmetric family has two geometric variables. A stationary collapse with
respect to geometry occurs when `F_nu`, restricted to the boundary curve
`F=0`, is stationary. The gradients of `F_nu` and `F` are then parallel,
which is exactly

\[
F_{\nu c}F_e-F_{\nu e}F_c=0.
\]

## Validated computation

`symmetric_fold_certificate.py` uses third-order forward automatic
differentiation with outward-rounded `Decimal` interval arithmetic. It forms
the complete interval Jacobian of the three displayed equations and applies a
Krawczyk operator to the `10^-20` box.

The Krawczyk image is strictly contained in the interior of the box in all
three coordinates. Therefore the box contains exactly one solution.

The same interval evaluation gives

\[
F_{\nu\nu}\in
[-0.0089826297788018310,-0.0089826297788018294],
\]

and the constrained curvature of `F_nu` along `F=0` is contained in

\[
[0.8225821061357489,0.8225821061357502].
\]

Thus neither the exponent double root nor the geometric stationary point is
degenerate.

## Local envelope slope at the fold

Let

\[
m=\frac{\mu+\nu}{2},\qquad
\delta=\frac{\mu-\nu}{2}.
\]

For `delta != 0`, the stationary symmetric two-root envelope can be written
with the regularized equations

\[
A=\frac{F(m+\delta)+F(m-\delta)}2=0,
\]

\[
B=\frac{F(m+\delta)-F(m-\delta)}{2\delta}=0,
\]

and

\[
C=\frac{1}{2\delta}
\det\!\begin{pmatrix}
F_c(m-\delta)&F_e(m-\delta)\\
F_c(m+\delta)&F_e(m+\delta)
\end{pmatrix}=0.
\]

All three extend smoothly to `delta=0`, where they reduce, up to a harmless
sign in the third equation, to the certified stationary-fold system. Their
Jacobian with respect to `(m,c,e)` is therefore nonsingular in the certified
fold box.

Moreover `A`, `B`, and `C` are even functions of `delta`. The implicit
solution consequently has

\[
m(\delta)=\nu_\dagger+O(\delta^2).
\]

Since `nu=m-delta` and `mu=m+delta`, this gives the rigorous local envelope
law

\[
\boxed{
\mu_{\rm sym}(\nu)
=2\nu_\dagger-\nu
+O((\nu_\dagger-\nu)^2)
}
\]

and hence

\[
\boxed{\mu_{\rm sym}'(\nu_\dagger^-)=-1.}
\]

This statement concerns the stationary equal-above envelope. Identifying it
with the global inclusion boundary still requires the global extremality step.

## Replay

```bash
python symmetric_fold_certificate.py
```
