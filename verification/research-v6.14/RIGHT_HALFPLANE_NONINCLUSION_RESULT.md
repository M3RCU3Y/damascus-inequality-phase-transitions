# Full noninclusion half-plane above 7.3596319

## Theorem

Let

\[
\mathcal I_\alpha^4
=\left\{X\in(0,\infty)^4:\prod_{j=1}^4x_j=1,
\quad S_\alpha^4(X)>0\right\},
\]

where

\[
S_\alpha^4(X)=\sum_{j=1}^4
\frac{x_j^\alpha-1}{x_j^{\alpha+1}+1}.
\]

Put

\[
\alpha_0=7.3596319=\frac{73596319}{10^7}.
\]

Then for every pair of real exponents

\[
\boxed{\alpha_0\le \nu<\mu}
\]

one has

\[
\boxed{\mathcal I_\nu^4\not\subseteq\mathcal I_\mu^4.}
\]

Thus the complete four-variable inclusion region contains no point in the
right half-plane with source exponent at least `7.3596319` and target exponent
strictly larger than the source. The cutoff is only about `3.89e-9` above the
independently interval-certified symmetric fold

\[
\nu_\dagger=7.3596318961093494297\ldots.
\]

The theorem does not assert that `alpha_0` is the sharp global cutoff.

## 1. Fixed rational target-boundary family

Use

\[
t=1.7123734016,
\qquad q_-=t-1=0.7123734016,
\qquad q_+=0.76735695.
\]

For `m>=alpha_0` and `q in [q_-,q_+]`, set

\[
r=q^{1/m},\qquad a=(rt^2)^{-1},
\qquad X_m(q)=(a,r,t,t).
\]

Every such point has product one and lies in a strict `2+2` sector. Define

\[
F(m,q)=S_m^4(X_m(q)).
\]

The fixed-slice zero-width certificate proves, for every `m>=alpha_0`, that
there is a target-boundary root

\[
q_m\in(q_-,q_+),\qquad F(m,q_m)=0,
\]

and that the exponent derivative with the point held fixed satisfies

\[
\left.\partial_\beta S_\beta^4(X_m(q_m))\right|_{\beta=m}<0.
\]

Hence `m` is a descending zero of the exponent history of `X_m(q_m)`.

On the compact range

\[
\alpha_0\le m\le40,
\]

the interval certificates prove uniformly on the full `(m,q)` rectangle

\[
\boxed{F_q>0},\qquad \boxed{F_m>0}.
\]

The weakest certified margins are

\[
F_q>0.6429997752233,
\qquad F_m>8.70654528105\times10^{-6}.
\]

Consequently the boundary root is unique and, by the implicit-function
theorem,

\[
q_m'=-\frac{F_m}{F_q}<0.
\]

Thus `m -> q_m` is a smooth strictly decreasing branch on the compact range.

## 2. Transporting the witness back to alpha_0

Define

\[
H(m,q)=S_{\alpha_0}^4(X_m(q)),
\qquad G(m)=H(m,q_m).
\]

At the starting exponent,

\[
G(\alpha_0)=F(\alpha_0,q_{\alpha_0})=0.
\]

Differentiating along the branch gives

\[
G'(m)
=H_m+H_q q_m'
=\frac{H_mF_q-H_qF_m}{F_q}.
\]

Write

\[
J(m,q)=H_mF_q-H_qF_m.
\]

It therefore suffices to prove `J>0` along the target-boundary curve.

A direct interval evaluation of `J` on the whole rectangle is unnecessarily
wide because it discards the dependence between `m` and `q_m`. The verifier
instead constructs a validated root tube. Because `F_q>0`, each endpoint root
is enclosed by 55 steps of outward-rounded interval bisection. Because `q_m`
is decreasing, on an exponent slab `[m_0,m_1]` the actual root satisfies

\[
q_{m_1}\le q_m\le q_{m_0}.
\]

The program evaluates `J` only on this thin certified tube and recursively
subdivides the exponent range until the interval lower bound is positive. It
closes `[alpha_0,40]` with

- 55 accepted exponent slabs,
- 56 cached validated endpoint-root brackets,
- maximum subdivision depth 34,
- weakest rigorous margin

\[
\boxed{J>8.14867946744\times10^{-12}.}
\]

Since `F_q>0`,

\[
\boxed{G'(m)>0\qquad(\alpha_0\le m\le40).}
\]

Therefore

\[
G(m)>0\qquad(\alpha_0<m\le40).
\]

## 3. Tail m >= 40

For `m>=40` and `q in [q_-,q_+]`,

\[
r=q^{1/m}\in[q_-^{1/40},1],
\qquad a=\frac1{rt^2}.
\]

The source exponent in `H` is fixed at `alpha_0`, so the whole tail can be
enclosed directly without following the boundary root. Outward-rounded
interval evaluation gives

\[
\boxed{
H(m,q)>0.1022120904419303889
\qquad(m\ge40,\ q_-\le q\le q_+).}
\]

In particular,

\[
G(m)=H(m,q_m)>0\qquad(m\ge40).
\]

Combining the compact and tail certificates gives

\[
\boxed{S_{\alpha_0}^4(X_m(q_m))>0\qquad(m>\alpha_0).}
\]

## 4. Filling every intermediate source exponent

The V6.14 single-transient theorem proves that the exponent history of every
strict four-variable `2+2` point is positive on at most one bounded interval
for exponents at least one.

For `X_m(q_m)` we know

\[
S_{\alpha_0}^4(X_m(q_m))>0,
\qquad S_m^4(X_m(q_m))=0,
\]

and the target zero is descending. Hence its unique positive interval contains
`alpha_0` and terminates at `m`. Therefore

\[
\boxed{
S_\nu^4(X_m(q_m))>0
\qquad(\alpha_0\le\nu<m).}
\]

Now fix arbitrary

\[
\alpha_0\le\nu<\mu.
\]

Choose the target-boundary point `X_mu(q_mu)`. Then

\[
S_\nu^4(X_\mu(q_\mu))>0,
\qquad S_\mu^4(X_\mu(q_\mu))=0.
\]

The same point belongs to the strict source violation set but not the strict
target violation set, proving

\[
\boxed{\mathcal I_\nu^4\not\subseteq\mathcal I_\mu^4.}
\]

## 5. Phase-diagram consequence

Together with the independently proved left-half-plane theorem

\[
0<\nu\le\nu_c,
\quad\mu>\nu
\quad\Longrightarrow\quad
\mathcal I_\nu^4\subseteq\mathcal I_\mu^4,
\]

where

\[
\nu_c=3.9826231561383400589\ldots,
\]

the unknown continuous four-variable inclusion region is now confined to the
finite source strip

\[
\boxed{\nu_c<\nu<7.3596319.}
\]

The symmetric-envelope work supplies rigorously certified local asymptotics at
both ends of the candidate boundary inside this strip. What remains is the
global extremality/classification of that finite middle strip.

## Replay

Run

```bash
python right_halfplane_certificate.py
```

The script replays the root-monotonicity and target-to-source transport
certificate. Every finite-range sign decision uses outward-rounded interval
arithmetic; the `m>=40` source-value bound is a direct outward interval
enclosure. It is intended to be run together with
`fixed_slice_zero_width_certificate.py`, which supplies the descending target
boundary witnesses.
