# KKT orientation reduction for the continuous middle strip

**Status:** exact reduction identities and proof architecture only.  This file does **not** claim the global sign `Q_123<0`, `Delta<0`, global equal-above extremality, or completion of the middle strip.

The purpose of this note is to compress the remaining continuous four-variable problem into a small collection of reusable invariants that are simultaneously legible to a human proof and to an interval-certification agent.

## 1. Log-coordinate kernel

Write

\[
\Phi_\alpha(x)=\phi_\alpha(e^x),\qquad
H_\alpha(x)=\Phi_\alpha'(x)=h_\alpha(e^x).
\]

Fix `0<nu<mu` and KKT multipliers `lambda,gamma`.  Put

\[
H(x)=H_\nu(x),\qquad M(x)=H_\mu(x),
\]

and

\[
\boxed{f(x)=M(x)-\lambda H(x)-\gamma.}
\]

At a four-distinct stationary point the four coordinate logs are simple roots

\[
x_1<x_2<x_3<x_4,
\]

so

\[
M_i=\lambda H_i+\gamma,
\qquad H_i=H(x_i),
\]

with the alternating root slopes

\[
f'_1<0,\qquad f'_2>0,\qquad f'_3<0,\qquad f'_4>0.
\]

Everything below treats the ordered roots together with `(nu,mu,lambda,gamma)` as one **root packet**.

## 2. Three-point orientation determinant

For the first three roots define

\[
D_{123}
=\det\begin{pmatrix}
1&H_1&M_1\\
1&H_2&M_2\\
1&H_3&M_3
\end{pmatrix}.
\]

Because the three root images lie on the KKT line `M=lambda H+gamma`,

\[
D_{123}=0.
\]

The canonical first-order feasible vector supported on the first three coordinates is

\[
\boxed{
v=(H_2-H_3,\ H_3-H_1,\ H_1-H_2,\ 0).
}
\]

It satisfies

\[
\sum_i v_i=0,
\qquad
\sum_iH_iv_i=0.
\]

Differentiating `D_123` with respect to its three root positions and then using `M_i=lambda H_i+gamma` gives the exact identities

\[
\frac{\partial D_{123}}{\partial x_i}=-v_i f'_i,
\qquad i=1,2,3.
\]

Therefore the directional derivative along the feasible motion is

\[
\boxed{
\mathrm dD_{123}[v]
=-\sum_{i=1}^3 f'_iv_i^2
=-Q_{123}.
}
\]

Equivalently,

\[
\boxed{
Q_{123}<0
\iff
\mathrm dD_{123}[v]>0.
}
\]

This is the clean geometric meaning of the numerical saddle invariant: it is the signed infinitesimal turning of the three-point collinearity determinant on the planar KKT curve

\[
x\longmapsto(H_\nu(x),H_\mu(x)).
\]

A future analytic proof should target this orientation statement rather than the expanded quadratic form whenever possible.

## 3. Root-map Jacobian invariant

For fixed `(nu,mu)`, treat the four simple roots as implicit functions of `(gamma,lambda)`.  From `f(x_i)=0`,

\[
\frac{\partial x_i}{\partial\gamma}=\frac1{f'_i},
\qquad
\frac{\partial x_i}{\partial\lambda}=\frac{H_i}{f'_i}.
\]

Define the two aggregate constraints

\[
P=\sum_i x_i,
\qquad
A=\sum_i\Phi_\nu(x_i).
\]

Since `Phi_nu'=H`,

\[
P_\gamma=\sum_i\frac1{f'_i},
\qquad
P_\lambda=\sum_i\frac{H_i}{f'_i},
\]

\[
A_\gamma=\sum_i\frac{H_i}{f'_i},
\qquad
A_\lambda=\sum_i\frac{H_i^2}{f'_i}.
\]

Hence

\[
\boxed{
\Delta
=\det\frac{\partial(P,A)}{\partial(\gamma,\lambda)}
=\left(\sum_i\frac1{f'_i}\right)
 \left(\sum_i\frac{H_i^2}{f'_i}\right)
-\left(\sum_i\frac{H_i}{f'_i}\right)^2.
}
\]

Expanding gives the pairwise form

\[
\boxed{
\Delta
=\sum_{i<j}\frac{(H_i-H_j)^2}{f'_if'_j}.
}
\]

Thus `Delta` is not an arbitrary algebraic diagnostic.  It is the orientation Jacobian of the KKT line-parameter map into the product/source constraints.

## 4. Exact relation to the restricted Hessian

Let

\[
D=\operatorname{diag}(f'_1,f'_2,f'_3,f'_4),
\qquad
C=\begin{pmatrix}
1&1&1&1\\
H_1&H_2&H_3&H_4
\end{pmatrix}.
\]

The constrained Hessian is the restriction of `D` to `ker C`.  If `Z` has orthonormal columns spanning `ker C`, then the standard determinant identity gives

\[
\boxed{
\det(Z^TDZ)
=\frac{\det D\;\det(CD^{-1}C^T)}{\det(CC^T)}
=\frac{\det D}{\det(CC^T)}\,\Delta.
}
\]

For the alternating simple-root slope pattern,

\[
\det D=f'_1f'_2f'_3f'_4>0,
\]

and `det(CC^T)>0`.  Therefore

\[
\boxed{
\operatorname{sign}\det(Z^TDZ)=\operatorname{sign}\Delta.
}
\]

In particular,

\[
\boxed{\Delta<0\Longrightarrow\text{the restricted Hessian is indefinite}.}
\]

So there are two equivalent proof interfaces:

1. exhibit the explicit negative direction `Q_123<0`; or
2. prove the orientation Jacobian `Delta<0`.

The second interface is often preferable for continuation/certification because it uses the same derivatives already needed to track the root packet.

## 5. The actual KKT manifold is one-dimensional

In line-parameter coordinates a four-distinct stationary boundary packet is not a raw five-dimensional geometry box.  In addition to the four root equations, the packet must satisfy

\[
\boxed{
P=\sum_i x_i=0,
\qquad
A=\sum_i\Phi_\nu(x_i)=0,
\qquad
B=\sum_i\Phi_\mu(x_i)=0.
}
\]

Thus, after the roots are treated implicitly, the stationary set is generically the one-dimensional zero set

\[
\boxed{
\mathcal K=\{P=A=B=0\}
\subset(\nu,\mu,\lambda,\gamma).
}
\]

This is the correct domain for any future interval sign certificate.  Do **not** return to a raw `(c,d,e,nu,mu)` sign box unless an elimination argument proves that it is cheaper.

A resource-efficient certificate should:

1. bracket the four roots with certified slope signs;
2. solve/continue `P=A=B=0` by interval Newton or Krawczyk boxes;
3. evaluate `Delta` (or `Q_123`) only on that root manifold;
4. separately certify manifold endpoints / root collisions.

## 6. Product-one simplex chart and the symmetry boundary

For direct geometry work use

\[
(x_1,x_2,x_3,x_4)
=
\bigl(-c(2-p),-cp,c(1-q),c(1+q)\bigr),
\]

with

\[
c>0,\qquad p>0,\qquad q>0,\qquad p+q<1.
\]

This builds in `sum x_i=0`.  The boundary `q=0` is the equal-above locus.

Suppose a four-distinct KKT branch with `q>0` approaches `q=0`.  Since

\[
f(x_3)=f(x_4)=0,
\qquad x_4-x_3=2cq,
\]

we have

\[
\frac{f(x_4)-f(x_3)}{x_4-x_3}=0.
\]

Taking the collision limit yields the necessary bifurcation condition

\[
\boxed{f(c)=0,\qquad f'(c)=0.}
\]

Thus any symmetry-breaking interior branch can meet the equal-above boundary only through a KKT-line tangency at the repeated upper root.  This is the correct interface with the existing full-fold nondegeneracy theorem.

## 7. Tilted oddness: a second possible shortcut

The reciprocity identity has a particularly clean log-coordinate normalization.  Define

\[
\Psi_\alpha(x)=e^{x/2}\Phi_\alpha(x).
\]

Then

\[
\boxed{
\Psi_\alpha(x)
=\frac{\sinh(\alpha x/2)}{\cosh((\alpha+1)x/2)},
}
\]

so `Psi_alpha` is odd.  Consequently, for

\[
U(x)=\Phi_\mu(x)-\lambda\Phi_\nu(x),
\]

\[
\boxed{e^{x/2}U(x)\text{ is odd},}
\qquad
U(-x)=-e^xU(x),
\]

and

\[
f(x)=U'(x)-\gamma.
\]

This packages the root-reflection structure into one object.  A stronger shortcut would be to prove the **four-root centroid inequality**

\[
\boxed{x_1+x_2+x_3+x_4<0}
\]

for every admissible four-root packet in the multiplier range

\[
1<\lambda<\mu/\nu,\qquad\gamma<0.
\]

Such a theorem would exclude four-distinct product-one stationary points outright.  The existing reciprocal single-crossing lemma is the first step, but pairwise reciprocal-root inequalities are known to be too strong.  Any successful proof here must be collective.

This is a shortcut target, not a theorem claim.

## 8. Decision rule for the next proof pass

Use the following order.

1. **Analytic orientation attempt:** seek a sign theorem for `Delta` or `dD_123[v]` using the planar KKT curve and the already-proved radial multiplier structure.
2. **Analytic centroid shortcut:** only if the collective root-reflection structure yields a clean proof of `sum x_i<0`; do not revive false pairwise inequalities.
3. **Certified one-dimensional route:** if the analytic sign does not collapse quickly, certify `Delta<0` directly on `K` using implicit root packets and interval continuation.
4. **Boundary closure:** use the collision condition `f=f'=0` together with the existing full-fold nondegeneracy theorem and the already-excluded lower-repeat/trace alternatives.

The goal is to spend exact arithmetic only after the geometry has reduced the dimension as far as possible.
