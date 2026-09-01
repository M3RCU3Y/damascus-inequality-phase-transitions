# Full large-target rigidity at the continuous onset

**Status:** `CERTIFIED-LOCAL` at the regularized endpoint, with an analytic compactness/localization corollary for globally competitive stationary minimizers.  The size of the resulting source neighborhood is not yet made explicit.

## 1. Full regularized chart

Let

\[
\varepsilon=\mu^{-1},\qquad r=q^\varepsilon,
\qquad a=(rt^2)^{-1},
\]

and introduce the upper-pair splitting variable `d`:

\[
X(t,d,q,\varepsilon)
=(te^d,te^{-d},r,a).
\]

Define

\[
G(\nu,t,d,q,\varepsilon)
=S_\nu^4(X(t,d,q,\varepsilon)),
\]

\[
H(t,d,q,\varepsilon)
=S_{1/\varepsilon}^4(X(t,d,q,\varepsilon)).
\]

The V6.14 regularization extends both functions smoothly one-sided to `epsilon=0`.  There

\[
G(\nu,t,d,q,0)
=S_\nu^3(te^d,te^{-d},t^{-2}),
\]

and

\[
\boxed{
H(t,d,q,0)
=\frac{2\cosh d}{t}-1+\frac{q-1}{q+1}.
}
\]

The limiting symmetric onset point is

\[
(\nu,t,d,q)
=(\nu_c,t_c,0,t_c-1),
\]

where V6.14 certifies

\[
G_\nu>0,\qquad G_{tt}<0.
\]

## 2. Full stationary equations

For fixed `epsilon`, a stationary double-boundary point in the full three-dimensional geometry `(t,d,q)` satisfies

\[
G=0,\qquad H=0,
\]

and rank one of the two geometry gradients.  Since `H_q\ne0` at the endpoint, use the two minors

\[
D_t=G_tH_q-G_qH_t,
\]

\[
D_d=G_dH_q-G_qH_d.
\]

Thus the full stationary system is

\[
\boxed{G=H=D_t=D_d=0.}
\]

At `epsilon=0`, the source function is independent of `q`, while both `G` and `H` are even in `d`.

## 3. Transverse source curvature is strictly negative

At `d=0`,

\[
G_{dd}
=2\frac{d^2}{dx^2}\phi_\nu(e^x)\bigg|_{x=\log t}
=2t\,h_\nu'(t).
\]

At the three-variable onset, stationarity gives

\[
h_{\nu_c}(t_c)=h_{\nu_c}(t_c^{-2})>0.
\]

The V6.14 positive-branch monotonicity theorem states

\[
h_\nu'(t)<0
\qquad(t>1,\ h_\nu(t)>0).
\]

Therefore

\[
\boxed{G_{dd}(\nu_c,t_c,0,t_c-1,0)<0.}
\]

## 4. Exact Jacobian factorization

At the endpoint,

\[
G_t=G_d=G_q=H_d=0,
\qquad H_q=\frac{2}{(1+q)^2}>0.
\]

Evenness kills every derivative containing exactly one `d`, and `G(\cdot,0)` is independent of `q`.  Consequently the Jacobian of

\[
(G,H,D_t,D_d)
\]

with respect to

\[
(\nu,t,d,q)
\]

has determinant

\[
\boxed{
\det J_0
=G_\nu\,G_{tt}\,G_{dd}\,H_q^3.
}
\]

Every factor is nonzero:

\[
G_\nu>0,
\qquad G_{tt}<0,
\qquad G_{dd}<0,
\qquad H_q>0.
\]

Hence

\[
\boxed{\det J_0\ne0.}
\]

The implicit-function theorem gives a unique stationary solution

\[
(\nu(\varepsilon),t(\varepsilon),d(\varepsilon),q(\varepsilon))
\]

for all sufficiently small positive `epsilon`.

The full stationary equations are invariant under

\[
d\mapsto-d.
\]

By uniqueness, the reflected solution is the same solution.  Therefore

\[
\boxed{d(\varepsilon)\equiv0.}
\]

Thus the V6.14 large-target symmetric envelope is in fact the **unique full nonsymmetric stationary branch** entering the onset endpoint.  Symmetry is forced by the full equations; it is not an ansatz.

## 5. Localization of competitive source-boundary sequences

Let `nu_k downarrow nu_c` and let `X_k` be a sequence of globally competitive strict `2+2` source-boundary/exit packets.  For large `k`, `nu_k<4`.  The escape estimate used in the exact-onset theorem is uniform there: a sequence leaving every compact logarithmic subset of the chamber has source limsup bounded strictly below zero.  Since

\[
S_{\nu_k}^4(X_k)=0,
\]

the geometry cannot escape.  After passing to a subsequence,

\[
X_k\to X_\infty
\]

in the closed ordered chamber, with

\[
S_{\nu_c}^4(X_\infty)=0.
\]

At `nu_c` the strict `2+2` locus has no positive point.  A nontrivial zero in the interior would therefore be a global interior maximum and hence a constrained critical point, contradicting the V6.14 no-interior-critical-point theorem.  The reciprocal-pair boundary `e=d` is strictly negative.  The identity is isolated from nontrivial zeros by the local nucleation law since `nu_c` lies far below the local four-variable threshold.  Hence the only possible nontrivial limiting zero lies on the coordinate-1 trace `e=c`.

On that trace the problem is three-variable.  The exact three-variable onset theorem has a unique nontrivial onset configuration, so

\[
\boxed{
X_\infty=(t_c,t_c,t_c^{-2},1)
}
\]

up to permutation.

## 6. The competitive target must diverge

Suppose the corresponding target exponents had a bounded subsequence

\[
\mu_k\to\mu_*>\nu_c.
\]

Passing to the limit in the target boundary would give

\[
S_{\mu_*}^3(t_c,t_c,t_c^{-2})=0.
\]

But the trace point is a nontrivial source-boundary point at `nu_c`.  The strict trace-transport lemma follows immediately from the V6.14 exponent-ratio theorem: writing the two above radii as `x,y>1`, their reciprocal lower radius is `xy>x,y`, so for every `mu>nu_c`,

\[
S_\mu^3
=\phi_{\nu_c}(x)[R(x)-R(xy)]
 +\phi_{\nu_c}(y)[R(y)-R(xy)]>0.
\]

Contradiction.  Therefore

\[
\boxed{\mu_k\to\infty.}
\]

Let `r_k` be the coordinate tending to `1` and set

\[
q_k=r_k^{\mu_k}.
\]

Every convergent subsequence of `q_k in [0,1]` satisfies, after passing to the target limit,

\[
\frac2{t_c}-1+\frac{q-1}{q+1}=0.
\]

The unique solution is

\[
\boxed{q=t_c-1.}
\]

Hence every competitive sequence enters the same regularized endpoint chart.

## 7. Near-onset global rigidity corollary

Combine Sections 4--6 with the active-source and boundary reductions in `GLOBAL_EXTREMIZER_REDUCTION.md`.

If nonsymmetric globally earliest-exit minimizers existed for a sequence of source exponents `nu_k downarrow nu_c`, then their active source roots and target exits would localize to the regularized endpoint and, being strict-interior nonsymmetric minimizers, satisfy the full stationary system.  Section 4 says the unique stationary branch there has `d=0`, contradiction.

Therefore there exists

\[
\boxed{\delta>0}
\]

such that throughout

\[
\boxed{\nu_c<\nu<\nu_c+\delta}
\]

no nonsymmetric strict-interior globally earliest-exit minimizer exists.  The globally competitive stationary envelope in this neighborhood is forced onto the equal-above family.

The present theorem is qualitative in `delta`.  The next certification task is to make the overlap explicit, ideally through `nu=4.05`, so that the compact determinant certificates can take over.
