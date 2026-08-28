# Zero local forward width for every target exponent at least 7.3596319

## Theorem

Let

\[
\phi_\alpha(x)=\frac{x^\alpha-1}{x^{\alpha+1}+1},\qquad
S_\alpha^4(X)=\sum_{j=1}^4\phi_\alpha(x_j).
\]

Then for every real target exponent

\[
\boxed{\mu\ge \frac{73596319}{10000000}=7.3596319}
\]

there exists `delta_mu>0` such that

\[
\boxed{
\mathcal I_{\mu-\varepsilon}^4\not\subseteq\mathcal I_\mu^4
\qquad(0<\varepsilon<\delta_\mu).}
\]

Thus every target exponent at least `7.3596319` has zero local forward-inclusion
width. This replaces the V6.13 statement "for every sufficiently large
target exponent" by the explicit finite rational threshold `7.3596319`.

The theorem does **not** assert that `7.3596319` is sharp. The interval-certified
symmetric fold lies slightly below it at

\[
\nu_\dagger=7.3596318961093494297\ldots,
\]

Thus the explicit rational cutoff lies only about `3.89e-9` above the certified fold.
The remaining global-envelope problem is to determine whether the exact
sharp threshold is `nu_dagger` or possibly smaller.

## 1. A fixed rational geometric slice

Use the exact decimal/rational constants

\[
t=1.7123734016=\frac{1070233376}{625000000},
\qquad q_-=0.7123734016=t-1,
\qquad q_+=0.76735695.
\]

For a target exponent `mu>=7.3596319` and `q in [q_-,q_+]`, define

\[
r=q^{1/\mu},\qquad a=\frac1{rt^2},
\qquad X_\mu(q)=(a,r,t,t).
\]

The product is exactly one. Since `0<q<1` one has `q<r<1`; moreover
`r>q_->t^{-2}`, so `a<1`. Hence every point in the slice lies in a strict
`2+2` sector.

Put

\[
F(\mu,q)=S_\mu^4(X_\mu(q))
\]

and let

\[
D(\mu,q)=
\left.\partial_\alpha S_\alpha^4(X_\mu(q))\right|_{\alpha=\mu},
\]

where the point is held fixed while differentiating the exponent.

For a fixed coordinate `x>0`,

\[
\partial_\alpha\phi_\alpha(x)
=(\log x)\frac{x^\alpha(1+x)}{(1+x^{\alpha+1})^2}.
\]

Therefore `D<0` at a target-boundary point immediately gives a source
violation just below the target exponent.

## 2. Stable exact formulas

Write

\[
c=\log t,\qquad y=t^{-\mu},\qquad T=y^2.
\]

Then

\[
r=q^{1/\mu},\qquad a=\frac1{rt^2}
\]

and direct cancellation of the large powers gives

\[
F(\mu,q)
=2\frac{1-y}{t+y}
+\frac{T/q-1}{1+Ta/q}
+\frac{q-1}{1+qr}.
\]

The corresponding exponent derivative is

\[
\begin{aligned}
D(\mu,q)
={}&2c\,\frac{y(1+t)}{(t+y)^2}\\
&+\frac{\log q}{\mu}
  \frac{q(1+r)}{(1+qr)^2}\\
&+\left(-\frac{\log q}{\mu}-2c\right)
  \frac{(T/q)(1+a)}{(1+Ta/q)^2}.
\end{aligned}
\]

These formulas are used by the verifier and avoid unstable powers such as
`t^mu`.

## 3. Validated compact-range certificate, 7.3596319 <= mu <= 40

`fixed_slice_zero_width_certificate.py` uses outward-rounded `Decimal`
interval arithmetic, including inflated correctly-rounded logarithms and
exponentials. On the full rectangle

\[
7.3596319\le\mu\le40,
\qquad q_-\le q\le q_+,
\]

it proves

\[
\boxed{F_q>0},\qquad
\boxed{D_q>0}.
\]

The adaptive proof closes with only three two-dimensional boxes. The weakest
certified lower margins are

\[
F_q>0.6429997752,
\qquad
D_q>0.0088076158.
\]

It separately certifies, for every `mu` in the same interval,

\[
F(\mu,q_-)<0,
\qquad
F(\mu,q_+)>0,
\qquad
D(\mu,q_+)<0.
\]

The weakest outward-rounded margins are respectively

\[
3.1092\times10^{-4},
\qquad
9.7322\times10^{-12},
\qquad
9.4890\times10^{-12}.
\]

Hence the intermediate-value theorem gives a unique

\[
q_\mu\in(q_-,q_+)
\]

with `F(mu,q_mu)=0`. Because `D_q>0` and `q_mu<q_+`,

\[
D(\mu,q_\mu)<D(\mu,q_+)<0.
\]

Thus the theorem holds throughout the compact range.

## 4. Analytic tail, mu >= 40

The tail needs no subdivision.

### Lower endpoint

At `q=q_-=t-1`, the limiting three main terms cancel exactly:

\[
\frac2t+\frac{q_--1}{1+q_-}-1=0.
\]

Write the finite-exponent corrections as

\[
F(\mu,q_-)=-E_t-E_r+E_a,
\]

where all three quantities are positive. Dropping `E_t`, one has

\[
E_r\ge
\frac{(1-q_-)q_-(-\log q_-)r_{40}}
     {\mu(1+q_-)^2},
\]

with

\[
r_{40}=q_-^{1/40},
\]

because `1-e^{-x}>=xe^{-x}`. Also

\[
E_a\le
\frac{1+a_{\max}}{q_-}\,t^{-2\mu},
\qquad
 a_{\max}=\frac1{r_{40}t^2}.
\]

Since `mu*t^{-2mu}` decreases for `mu>=40`, it is enough to compare the two
bounds at `mu=40`. The outward-rounded certificate gives the positive margin

\[
E_r-E_a>0.02349920836/\mu.
\]

Therefore

\[
\boxed{F(\mu,q_-)<0\qquad(\mu\ge40).}
\]

### Upper endpoint

For `q=q_+`, the below-one `a` contribution is strictly greater than `-1`.
Both the fixed-`t` term and the `r` term are bounded below by their values at
`mu=40`. Thus

\[
F(\mu,q_+)
>
2\frac{1-t^{-40}}{t+t^{-40}}
+\frac{q_+-1}{1+q_+q_+^{1/40}}-1.
\]

The validated lower bound is

\[
\boxed{F(\mu,q_+)>0.03595805035\qquad(\mu\ge40).}
\]

Hence a boundary root exists for every target in the tail.

### Uniform negativity of the target exponent derivative

The `a` contribution to `D` is negative, so it may be discarded in an upper
bound. Uniformly for `q in [q_-,q_+]` and `mu>=40`,

\[
D(\mu,q)
\le
A t^{-\mu}-\frac{B}{\mu},
\]

where

\[
A=\frac{2\log t(1+t)}{t^2},
\]

and

\[
B=(-\log q_+)
\frac{q_-(1+q_-^{1/40})}{(1+q_+)^2}>0.
\]

Since `mu*t^{-mu}` decreases for `mu>=40`, multiplication by `mu` reduces the
claim to the endpoint `mu=40`. The outward-rounded margin is

\[
B-40A t^{-40}>0.1202749159.
\]

Consequently

\[
\boxed{D(\mu,q)<0}
\]

on the entire tail rectangle, including every boundary root supplied by the
intermediate-value theorem.

## 5. Conclusion

For every real `mu>=7.3596319` we have constructed a strict product-one `2+2`
point `X_mu` satisfying

\[
S_\mu^4(X_\mu)=0,
\qquad
\left.\partial_\alpha S_\alpha^4(X_\mu)\right|_{\alpha=\mu}<0.
\]

By differentiability there is `delta_mu>0` such that

\[
S_{\mu-\varepsilon}^4(X_\mu)>0
\qquad(0<\varepsilon<\delta_\mu).
\]

The same point lies outside the strict target violation set because its target
value is zero. Hence

\[
\mathcal I_{\mu-\varepsilon}^4
\not\subseteq
\mathcal I_\mu^4.
\]

This proves zero local forward-inclusion width for every target exponent at
least `7.3596319`.

## Replay

Run

```bash
python fixed_slice_zero_width_certificate.py
```

The finite-range sign decisions are validated interval computations; the tail
inequalities are analytic and their endpoint constants are evaluated with the
same outward-rounded arithmetic.
