# Real-exponent lower-pair spreading theorem

**Status:** `CERTIFIED-GLOBAL` analytic theorem for the stated tail domain.

Let

\[
\phi_\alpha(z)=\frac{z^\alpha-1}{z^{\alpha+1}+1},
\qquad
h_\alpha(z)=z\phi_\alpha'(z),
\qquad \alpha>1.
\]

Write an ordered strict `2+2` point as

\[
X(c,d,e)=\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
\qquad 0\le d<e<c,
\]

and set

\[
t=e^c,
\qquad
T_\alpha=1+\frac4{\alpha^2}.
\]

Then throughout

\[
\boxed{t\ge T_\alpha,\quad 0<e<c}
\]

one has

\[
\boxed{
\partial_e S_\alpha^4(X(c,d,e))>0.
}
\]

The proof is the real-exponent version of the lower-spreading argument used in the integer topology theorem.  No integrality is needed.

## 1. Shape of h_alpha below one

The V6.14 continuous-onset proof gives

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

Generalized Descartes sign counting gives exactly one critical point of `h_alpha` in `(0,1)`.  Thus `h_alpha` increases once and then decreases there.  Moreover

\[
h_\alpha(0+)=0,
\qquad
h_\alpha(1)=\frac\alpha2,
\qquad
h_\alpha'(1)<0,
\]

so the unique maximum is strictly above `alpha/2`.

Hence there is a unique point

\[
q_\alpha\in(0,1)
\]

on the increasing branch such that

\[
h_\alpha(q_\alpha)=\frac\alpha2.
\]

## 2. Uniform real-exponent location of q_alpha

Put

\[
z_\alpha=\frac1{T_\alpha}
=\frac{\alpha^2}{\alpha^2+4}.
\]

The equation `h_alpha(z)=alpha/2` can be rewritten, after setting `A=z^(alpha+1)`, as

\[
(2+\alpha z)A^2-2(\alpha+z)A+\alpha z=0.
\]

The smaller root is equivalently

\[
z^\alpha
=\frac{\alpha}{\alpha+z+D(z)},
\qquad
D(z)=\sqrt{\alpha^2(1-z^2)+z^2}.
\]

At `z=z_alpha`, the real Bernoulli inequality for `alpha>1` gives

\[
(1+4/\alpha^2)^\alpha
>1+\frac4\alpha,
\]

hence

\[
z_\alpha^\alpha
<\frac\alpha{\alpha+4}.
\]

Also a direct simplification gives

\[
9-D(z_\alpha)^2
=\frac{8(7\alpha^2+18)}{(\alpha^2+4)^2}>0,
\]

so `D(z_alpha)<3`.  Since `z_alpha<1`,

\[
\alpha+z_\alpha+D(z_\alpha)<\alpha+4,
\]

and therefore

\[
z_\alpha^\alpha
<\frac\alpha{\alpha+4}
<\frac\alpha{\alpha+z_\alpha+D(z_\alpha)}.
\]

This is exactly the strict inequality placing `z_alpha` before the nontrivial `alpha/2` crossing.  Thus

\[
\boxed{
q_\alpha>z_\alpha=\frac{\alpha^2}{\alpha^2+4}.
}
\]

## 3. Lower-pair spreading

For the two lower coordinates put

\[
z_-=e^{-c-e},
\qquad
z_+=e^{-c+e}.
\]

Then

\[
0<z_-<z_+<1,
\qquad
z_-z_+=t^{-2},
\]

so their geometric mean is

\[
\sqrt{z_-z_+}=\frac1t.
\]

If `t>=T_alpha`, then

\[
\frac1t\le z_\alpha<q_\alpha.
\]

In particular `z_-<q_alpha`.

If `z_+<=q_alpha`, both points lie on the increasing branch of `h_alpha`, hence

\[
h_\alpha(z_+)>h_\alpha(z_-).
\]

If `z_+>q_alpha`, then by the definition of the nontrivial crossing,

\[
h_\alpha(z_+) > \frac\alpha2 > h_\alpha(z_-).
\]

Thus in every case

\[
\boxed{
h_\alpha(z_+)>h_\alpha(z_-).}
\]

Finally,

\[
\partial_e S_\alpha^4
=h_\alpha(e^{-c+e})-h_\alpha(e^{-c-e}),
\]

so

\[
\boxed{
\partial_e S_\alpha^4>0
\quad(t\ge1+4/\alpha^2).
}
\]

## 4. Two-exponent corollary

Because `T_alpha` is strictly decreasing in `alpha`, if

\[
1<\nu<\mu,
\qquad
t\ge T_\nu,
\]

then automatically `t>=T_mu`, and therefore

\[
\boxed{
F_{\nu,e}>0,
\qquad
F_{\mu,e}>0.
}
\]

This is the denominator-sign input needed by the V6.15 source-fiber determinant reduction once a relevant source packet is known to lie outside the low-radius box `t<T_nu`.
