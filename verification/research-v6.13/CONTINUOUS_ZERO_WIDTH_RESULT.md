# Arbitrarily small forward-inclusion failures at high exponent

## Theorem

There exists `mu_0` such that for every real `mu>=mu_0` there is a number
`delta_mu>0` with

\[
\mathcal I_{\mu-\varepsilon}^4\not\subseteq\mathcal I_\mu^4
\qquad(0<\varepsilon<\delta_\mu).
\]

Thus the forward-inclusion window has zero local width at every sufficiently
large target exponent. In particular, the previously proved scale

\[
B\sqrt\mu\,2^{-\mu/2},\qquad B>\sqrt6,
\]

is an explicit failure construction but is not an optimal gap scale, and
`\sqrt6` is not a sharp phase-boundary constant.

## Proof

Fix any number `t` with `1<t<2`, and put

\[
q_0=t-1\in(0,1).
\]

For a target exponent `mu` and `q` near `q_0`, define

\[
r=q^{1/\mu},\qquad a=(rt^2)^{-1},
\qquad X_\mu(q)=(a,r,t,t).
\]

The product of the four coordinates is one. For `mu` sufficiently large and
`q` in a fixed compact neighbourhood of `q_0`, one has `a,r<1<t`, so these
points lie in a strict `2+2` sign sector.

Define

\[
F_\mu(q)=S_\mu^4(X_\mu(q)).
\]

Because `r^\mu=q`,

\[
\phi_\mu(r)=\frac{q-1}{1+qr}.
\]

Uniformly for `q` in a compact neighbourhood of `q_0`,

\[
r\to1,\qquad a\to t^{-2},
\]

and therefore

\[
F_\mu(q)\longrightarrow
F_\infty(q)
=-1+\frac2t+\frac{q-1}{q+1}.
\]

The limiting function has the unique simple zero

\[
F_\infty(q_0)=0,
\qquad q_0=t-1,
\]

with

\[
F_\infty'(q)=\frac2{(1+q)^2}>0.
\]

Choose a small closed interval around `q_0` contained in `(0,1)`. Uniform
convergence preserves the opposite endpoint signs for all sufficiently large
`mu`, so the intermediate-value theorem gives a root `q_mu` with

\[
F_\mu(q_\mu)=0.
\]

Every such choice satisfies `q_mu->q_0`, since any subsequential limit must be
a zero of `F_infty` in the chosen interval.

Now hold the point `X_mu(q_mu)` fixed and differentiate only with respect to
the exponent. For every fixed `x>0`,

\[
\partial_\alpha\phi_\alpha(x)
=(\log x)\frac{x^\alpha(1+x)}{(1+x^{\alpha+1})^2}.
\]

For the coordinate `r=q_mu^{1/mu}` this gives

\[
\mu\,\partial_\alpha\phi_\alpha(r)\big|_{\alpha=\mu}
=(\log q_\mu)\frac{q_\mu(1+r)}{(1+q_\mu r)^2}
\longrightarrow
\frac{2q_0\log q_0}{(1+q_0)^2}<0.
\]

The two fixed coordinates `t>1` contribute only `O(mu t^{-mu})` after this
scaling. The coordinate `a` stays uniformly below one and contributes an
exponentially small amount as well. Hence

\[
\boxed{
\mu\,\partial_\alpha S_\alpha^4(X_\mu(q_\mu))\big|_{\alpha=\mu}
\longrightarrow
\frac{2q_0\log q_0}{(1+q_0)^2}<0.}
\]

Consequently the target-boundary exponent derivative is strictly negative for
all sufficiently large `mu`. Since

\[
S_\mu^4(X_\mu(q_\mu))=0,
\]

differentiability in the exponent implies that there is `delta_mu>0` such
that

\[
S_{\mu-\varepsilon}^4(X_\mu(q_\mu))>0
\qquad(0<\varepsilon<\delta_\mu).
\]

The same point is therefore a source violation and lies on, hence outside, the
target strict violation set. This proves

\[
\mathcal I_{\mu-\varepsilon}^4\not\subseteq\mathcal I_\mu^4
\]

for every sufficiently small positive `varepsilon` and every sufficiently
large target `mu`.

## Numerical replay

`continuous_zero_width_check.py` uses high-precision decimal arithmetic for the
convenient choice `t=3/2`, for which `q_0=1/2`, and checks convergence of the
boundary roots and scaled exponent derivatives. The replay is a sanity check;
the theorem above is analytic.
