# Exact fold cutoff for the four-variable right half-plane

## Theorem

Let `(nu_dagger,c_dagger,e_dagger)` be the unique symmetric fold point certified
in `SYMMETRIC_FOLD_RESULT.md`, so

\[
\nu_\dagger
 =7.3596318961093494297131900223\ldots
\]

and, for

\[
F(\alpha,c,e)
 =S_\alpha^4(e^c,e^c,e^{-c+e},e^{-c-e}),
\]

one has

\[
F=F_\alpha=0
\]

at the fold. Then

\[
\boxed{
\nu_\dagger\le \nu<\mu
\quad\Longrightarrow\quad
\mathcal I_\nu^4\not\subseteq\mathcal I_\mu^4.
}
\]

Thus `nu_dagger` itself, not a nearby decimal safety cutoff, is a rigorous
right-half-plane noninclusion threshold.

This theorem does not yet assert that `nu_dagger` is the globally sharp
zero-width threshold from below. That requires excluding an earlier
nonsymmetric first-exit configuration in the remaining middle strip.

## 1. Quantitative bridge immediately to the right of the fold

Put

\[
M_0=7.3596319,
\qquad
\Delta=M_0-\nu_\dagger.
\]

The fold Krawczyk certificate traps the exact fold in the boxes

\[
|\nu-\nu_0|,|c-c_0|,|e-e_0|\le10^{-20}.
\]

On the enlarged local box

\[
\nu_\dagger\le \alpha\le M_0,
\qquad c=c_\dagger,
\qquad e_\dagger\le e\le e_\dagger+3\cdot10^{-20},
\]

the outward-rounded certificate proves the uniform derivative bounds

\[
F_e\ge p,
\qquad
-b\le F_{\alpha\alpha}\le-a<0,
\qquad
|F_{\alpha e}|\le C,
\]

where one may take

\[
\begin{aligned}
p&=3.7156982864250034422\ldots,\\
a&=0.00898262164103805954\ldots,\\
b&=0.00898263789978550751\ldots,\\
C&=0.4890280045581667023\ldots.
\end{aligned}
\]

Fix a target

\[
\mu=\nu_\dagger+\delta,
\qquad0<\delta\le\Delta,
\]

and keep `c=c_dagger` fixed. Since

\[
F(\nu_\dagger,c_\dagger,e_\dagger)=0,
\qquad
F_\alpha(\nu_\dagger,c_\dagger,e_\dagger)=0,
\]

the bound `F_{alpha alpha}<=-a` gives

\[
F_\alpha(\mu,c_\dagger,e_\dagger)\le-a\delta<0
\]

and

\[
-\frac b2\delta^2
\le
F(\mu,c_\dagger,e_\dagger)
\le
-\frac a2\delta^2<0.
\]

At the upper endpoint `e=e_dagger+E`, with `E=3*10^{-20}`,

\[
F(\mu,c_\dagger,e_\dagger+E)
\ge pE-\frac b2\Delta^2.
\]

The certified margin is

\[
\boxed{
pE-\frac b2\Delta^2
>4.3485126682660552\times10^{-20}.}
\]

Hence, because `F_e>0`, there is a unique

\[
e_\mu\in(e_\dagger,e_\dagger+E)
\]

with

\[
F(\mu,c_\dagger,e_\mu)=0.
\]

Moreover the mean-value theorem gives the sharper displacement bound

\[
0<e_\mu-e_\dagger
\le K\delta^2,
\qquad
K=\frac b{2p}
=0.0012087415617951049\ldots.
\]

Therefore

\[
\begin{aligned}
F_\alpha(\mu,c_\dagger,e_\mu)
&\le -a\delta+C(e_\mu-e_\dagger)\\
&\le -\delta\left(a-CK\delta\right).
\end{aligned}
\]

The certificate proves

\[
\boxed{
a-CK\Delta
>0.0089826216387382630.}
\]

Thus the target zero is strictly descending for every
`nu_dagger<mu<=M0`.

Finally, since `e_mu>e_dagger` and `F_e>0`,

\[
F(\nu_\dagger,c_\dagger,e_\mu)>0.
\]

So every target in this microscopic bridge has a strict `2+2` boundary
witness which is already violating at `nu_dagger` and exits at the target.

## 2. Transport from M0 to infinity

For `mu>=M0` use the fixed rational geometric slice

\[
t=1.7123734016,
\qquad
q\in[0.7123734016,0.76735695],
\]

with

\[
r=q^{1/\mu},
\qquad
a=(rt^2)^{-1},
\qquad
X_\mu(q)=(a,r,t,t).
\]

The V6.14 fixed-slice certificate gives a unique target-boundary root
`q_mu`, together with a descending target zero.

The previous right-half-plane transport used the rational source `M0`. Here
the source is replaced by the entire certified interval containing
`nu_dagger`. Define

\[
H(\mu,q)=S_{\nu_\dagger}^4(X_\mu(q)).
\]

At `mu=M0`, a 105-step validated bisection traps `q_M0` in an interval of
width

\[
1.35545\times10^{-33},
\]

and outward-rounded evaluation over the full fold-exponent box gives

\[
\boxed{
H(M_0,q_{M_0})
>5.5559729856810701\times10^{-20}.}
\]

For `M0<=mu<=40`, the same root-tube argument as in the rational-source
transport proves

\[
J=H_\mu F_q-H_qF_\mu>0
\]

along the complete target-boundary branch. The 55-slab certificate has
weakest margin

\[
\boxed{J>8.1486795749113236\times10^{-12}.}
\]

Since `F_q>0`, this implies

\[
\frac d{d\mu}H(\mu,q_\mu)>0,
\]

so every such target-boundary point is already positive at `nu_dagger`.

For `mu>=40`, a direct enclosure over the whole fixed slice yields

\[
\boxed{
H(\mu,q)>0.10221209038823149
}
\]

uniformly, so the tail requires no root tracking.

## 3. Fill every intermediate source exponent

Each witness used above is a strict `2+2` point. By the V6.14
single-transient theorem, its positive real-exponent set is one bounded
interval.

For every target `mu>nu_dagger` we have constructed a point `X_mu` with

\[
S_{\nu_\dagger}^4(X_\mu)>0,
\qquad
S_\mu^4(X_\mu)=0,
\]

and the target zero is descending. Therefore the unique positive interval
contains every

\[
\nu_\dagger\le\nu<\mu.
\]

Hence the same point witnesses

\[
X_\mu\in\mathcal I_\nu^4,
\qquad
X_\mu\notin\mathcal I_\mu^4,
\]

which proves

\[
\boxed{
\mathcal I_\nu^4\not\subseteq\mathcal I_\mu^4
\quad
(\nu_\dagger\le\nu<\mu).
}
\]

## Replay

Run

```bash
python fold_right_halfplane_certificate.py
```

The script replays the local derivative bridge, the fold-source value at the
rational splice point, the 55-slab target-boundary transport, and the analytic
tail enclosure using outward-rounded interval arithmetic.
