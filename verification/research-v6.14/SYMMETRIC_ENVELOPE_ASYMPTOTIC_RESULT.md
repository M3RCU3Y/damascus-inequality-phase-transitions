# The large-target end of the stationary symmetric inclusion envelope

## Result

Let `(nu_c,t_c)` be the nondegenerate three-variable symmetric onset point,
so

\[
S_{\nu_c}^3(t_c,t_c,t_c^{-2})=0,
\qquad
\partial_tS_{\nu_c}^3(t_c,t_c,t_c^{-2})=0.
\]

The V6.14 interval replay certifies the local solution

\[
\nu_c=3.9826231561383400589629765329\ldots,
\qquad
t_c=1.5355671257762481178820968818\ldots,
\]

with positive exponent derivative and strictly negative radial second
derivative.

There is a unique local stationary equal-above `2+2` envelope branch for
sufficiently large target exponent `mu`.  Along this branch,

\[
\boxed{
\mu(\nu-\nu_c)\longrightarrow C_c
}
\qquad(\mu\to\infty),
\]

where

\[
\boxed{
C_c=
-\frac{
\log(t_c-1)
\left[\nu_c/2-h_{\nu_c}(t_c^{-2})\right]
}{
\partial_\nu S_\nu^3(t_c,t_c,t_c^{-2})\vert_{\nu=\nu_c}
}}
\]

and

\[
C_c=11.8487685043754056738569263899\ldots.
\]

Thus the stationary symmetric phase boundary approaches the exact
three-variable onset hyperbolically:

\[
\nu=\nu_c+\frac{C_c}{\mu}+O(\mu^{-2}).
\]

## Regularized large-target chart

Put

\[
\varepsilon=\mu^{-1},\qquad
r=q^\varepsilon,\qquad
a=(rt^2)^{-1}.
\]

Define the source and target boundary functions

\[
G(\nu,t,q,\varepsilon)
=S_\nu^4(t,t,r,a),
\]

\[
H(t,q,\varepsilon)
=S_{1/\varepsilon}^4(t,t,r,a).
\]

The target function has a smooth one-sided extension to `epsilon=0`.  The two
fixed above-one coordinates tend to `1/t`, the fixed below-one coordinate
tends to `-1`, and the moving coordinate satisfies `r^(1/epsilon)=q` exactly.
Consequently

\[
H(t,q,0)
=\frac2t-1+\frac{q-1}{q+1}.
\]

The source function extends as

\[
G(\nu,t,q,0)=S_\nu^3(t,t,t^{-2}).
\]

A stationary envelope point is characterized by the two boundary equations
together with tangency of their level curves in `(t,q)`:

\[
D:=G_tH_q-G_qH_t=0.
\]

At `epsilon=0`, the equations `G=H=D=0` give

\[
(\nu,t,q)=(\nu_c,t_c,t_c-1).
\]

Indeed `G=G_t=0` is the three-variable onset condition and `H=0` gives
`q=t-1`.

## Implicit-function argument

At the limiting point, `G_q=G_t=0`, whereas

\[
G_\nu>0,\qquad G_{tt}<0,
\qquad H_q=\frac{2}{(1+q)^2}>0.
\]

The Jacobian of `(G,H,D)` with respect to `(nu,t,q)` therefore has determinant

\[
-\,G_\nu G_{tt}H_q^2\ne0.
\]

The implicit-function theorem supplies a unique local stationary branch
`(nu(epsilon),t(epsilon),q(epsilon))` for small positive `epsilon`.

Differentiate the source equation at `epsilon=0`.  Because `G_t=G_q=0`,

\[
G_\nu\nu'(0)+G_\varepsilon=0.
\]

Now

\[
\frac{d}{d\varepsilon}\log r\bigg|_0=\log q,
\qquad
\frac{d}{d\varepsilon}\log a\bigg|_0=-\log q,
\]

so

\[
G_\varepsilon
=\log q\left(\frac\nu2-h_\nu(t^{-2})\right).
\]

Using `q=t_c-1` gives the displayed constant `C_c=nu'(0)`.  Since
`epsilon=1/mu`, the asymptotic statement follows.

## Validated onset replay

`symmetric_envelope_asymptotic.py` applies a two-dimensional Krawczyk test to
`S_nu^3=0` and its radial derivative.  In the certified box it proves

\[
\partial_\nu S^3\in
[0.09470539026516279668,0.09470539026516279698]
\]

and

\[
\partial_c^2S^3\in
[-2.917600376882724557,-2.917600376882724507].
\]

It then evaluates the exact formula for `C_c` with outward-rounded intervals,
obtaining

\[
C_c\in
[11.8487685043754056557,11.8487685043754056937].
\]

## Replay

```bash
python symmetric_envelope_asymptotic.py
```
