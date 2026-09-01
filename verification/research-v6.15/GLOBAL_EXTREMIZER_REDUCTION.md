# Global middle-strip extremizer reduction

**Status:** `IDENTITY` + analytic reduction lemmas.  This note does not claim the remaining determinant sign certificate.

## Target

Fix a source exponent `nu` in the unresolved continuous strip and consider the earliest later target exponent at which four-variable inclusion can fail.  This note reduces any genuine nonsymmetric interior minimizer to one scalar determinant equation and eliminates the non-equal-above chamber boundaries analytically.

Write the ordered strict `2+2` geometry as

\[
X(c,d,e)=\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
\qquad 0<d<e<c,
\]

and

\[
F_\alpha(c,d,e)=S_\alpha^4(X(c,d,e)).
\]

Let

\[
H_\alpha(x)=h_\alpha(e^x)=\frac{d}{dx}\phi_\alpha(e^x).
\]

Then

\[
F_{\alpha,d}=H_\alpha(c+d)-H_\alpha(c-d),
\]

\[
F_{\alpha,e}=H_\alpha(-c+e)-H_\alpha(-c-e).
\]

## 1. The source constraint is active at a simple earliest exit

Suppose `X_*` is a strict interior `2+2` local minimizer of its later exit exponent `mu_+(X)` among points whose transient positive interval contains a fixed source exponent `nu`.  Assume the later zero is simple (hence descending, as it is the exit from the unique positive interval).

Then

\[
\boxed{F_\nu(X_*)=0.}
\]

Indeed, if `F_nu(X_*)>0`, source feasibility has slack and persists under every sufficiently small geometric perturbation.  Thus `X_*` would be an unconstrained local minimizer of the smooth exit-root function `mu_+`.

From

\[
F_{\mu_+(X)}(X)=0
\]

implicit differentiation gives

\[
\nabla_X\mu_+(X)
=-\frac{\nabla_XF_{\mu_+(X)}(X)}{\partial_\alpha F_\alpha(X)|_{\alpha=\mu_+(X)}}.
\]

The denominator is nonzero at a simple descending exit.  Therefore an unconstrained local minimum would force

\[
\nabla_XF_{\mu_+}(X_*)=0,
\]

which is an interior constrained critical point of `S^4_{mu_+}` in a strict `2+2` sector.  V6.14 proves that no such interior critical point exists for any real exponent.  Contradiction.

Thus every simple strict-interior earliest-exit minimizer lies on the **double boundary**

\[
F_\nu=F_\mu=0.
\]

Non-simple target zeros are a separate double-root problem; the certified full fold theorem already controls the known fold locally.

## 2. The fiber determinant is the exact nonsymmetric stationarity obstruction

At an interior stationary point of the target exponent on the source boundary, logarithmic Lagrange multipliers give constants `lambda,gamma` such that every coordinate log `x_i` satisfies

\[
H_\mu(x_i)-\lambda H_\nu(x_i)-\gamma=0.
\]

Subtract the equations at the two positive logs `c+d` and `c-d`:

\[
F_{\mu,d}=\lambda F_{\nu,d}.
\]

Subtract the equations at the two negative logs `-c+e` and `-c-e`:

\[
F_{\mu,e}=\lambda F_{\nu,e}.
\]

Hence every four-distinct interior stationary packet satisfies

\[
\boxed{
J_{\nu,\mu}(c,d,e)=0,
}
\]

where

\[
\boxed{
J_{\nu,\mu}
=F_{\mu,d}F_{\nu,e}-F_{\mu,e}F_{\nu,d}.
}
\]

Conversely, whenever `F_{nu,e}` and `F_{mu,e}` are nonzero, `J=0` is exactly equality of the two pairwise KKT slopes.

Therefore any theorem

\[
J_{\nu,\mu}>0
\]

on the globally competitive double-boundary region excludes every four-distinct interior minimizer at once.  This determinant is the preferred compact certificate target.

## 3. Equivalent source-fiber derivative

Along a fixed-`c` source-boundary fiber `F_nu(c,d,e(d))=0`,

\[
e'(d)=-\frac{F_{\nu,d}}{F_{\nu,e}}.
\]

If `mu(d)` is a simple later zero on the same point, then

\[
\boxed{
\mu'(d)
=-\frac{J_{\nu,\mu}}
{(\partial_\alpha F_\mu)F_{\nu,e}}.
}
\]

At a descending target zero, `partial_alpha F_mu<0`.  Thus whenever `F_{nu,e}>0`, the sign `J>0` says exactly that splitting the equal upper pair pushes the exit exponent later.

## 4. The boundary e=d is impossible

At `e=d`, the point is

\[
(e^{c+d},e^{c-d},e^{-c+d},e^{-c-d})
=(A,B,B^{-1},A^{-1}),
\]

with `A,B>1`.  The reciprocal identity gives, for every `t>1`,

\[
\phi_\alpha(t)+\phi_\alpha(t^{-1})
=(1-t)\phi_\alpha(t)<0.
\]

Therefore

\[
\boxed{F_\alpha(c,d,d)<0}
\]

for every nontrivial point and every `alpha>0`.  The boundary `e=d` cannot carry a source violation or source zero relevant to inclusion failure.

## 5. The coordinate-1 trace e=c cannot be a later exit

At `e=c`, one lower coordinate equals `1` and the remaining three coordinates have the form

\[
(x,y,(xy)^{-1}),
\qquad x,y>1.
\]

Suppose this trace point is on a nontrivial source boundary at exponent `nu`:

\[
\phi_\nu(x)+\phi_\nu(y)=xy\,\phi_\nu(xy).
\]

For every `mu>nu`, write

\[
R(t)=\frac{\phi_\mu(t)}{\phi_\nu(t)}.
\]

V6.14 proves that `R` is strictly decreasing for `t>1`.  Since `xy>x,y`,

\[
R(x)>R(xy),\qquad R(y)>R(xy).
\]

Using the source balance,

\[
\begin{aligned}
S_\mu^3
&=\phi_\nu(x)R(x)+\phi_\nu(y)R(y)
-xy\phi_\nu(xy)R(xy)\\
&=\phi_\nu(x)[R(x)-R(xy)]
 +\phi_\nu(y)[R(y)-R(xy)]>0.
\end{aligned}
\]

Hence

\[
\boxed{
F_\nu(c,d,c)=0\ \Longrightarrow\ F_\mu(c,d,c)>0
\quad(\mu>\nu)
}
\]

for every nontrivial trace point.  A coordinate-1 trace source boundary can never be the later target-zero witness of an inclusion failure.

## 6. Global consequence once J>0 is certified

For a compact competitive region in which:

1. an earliest exit is attained or every minimizing sequence has controlled boundary limits;
2. simple interior exits have active source constraint by Section 1;
3. `J_{nu,mu}>0` on every four-distinct competitive double-boundary packet;
4. non-simple target zeros are separately controlled;

there is no four-distinct interior minimizer.  The boundaries `e=d` and `e=c` are impossible by Sections 4--5.  The surviving symmetry boundary is

\[
\boxed{d=0,}
\]

the equal-above family.

Thus the global middle-strip theorem has been reduced to a compact determinant sign problem plus endpoint/non-simple-zero control.
