# Full local nondegeneracy of the continuous four-variable fold

Let

\[
F(\alpha,c,d,e)=S_\alpha^4\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr).
\]

At the certified symmetric fold

\[
(\alpha,c,d,e)=(\nu_\dagger,c_\dagger,0,e_\dagger)
\]

with

\[
\nu_\dagger=7.35963189610934942971319002231776493349\ldots,
\]

the double-root equations are

\[
F=0,\qquad F_\alpha=0.
\]

The gradients of these two constraints have rank two because
\(F_{\alpha\alpha}<0\) and \((F_c,F_e)\ne(0,0)\). Hence their common zero set
is a smooth two-dimensional manifold near the fold.

## Constrained stationary point

Minimize the exponent coordinate \(\alpha\) on this double-root manifold.
For

\[
\mathscr L=\alpha+\lambda_1F+\lambda_2F_\alpha,
\]

the multiplier equations at the fold give

\[
\lambda_2=-\frac1{F_{\alpha\alpha}},
\qquad
\lambda_1=-\lambda_2\frac{F_{\alpha c}}{F_c}.
\]

The fold tangency equation

\[
F_{\alpha c}F_e-F_{\alpha e}F_c=0
\]

is exactly the remaining first-order multiplier equation. Thus the certified
symmetric fold is stationary for the *full* constrained problem, including
the off-axis direction.

## Transverse second variation

Because \(F\) is even in \(d\), the pure \(d\)-direction belongs to the
tangent space and all mixed Hessian entries containing exactly one \(d\)
vanish at \(d=0\). Its constrained second variation is therefore

\[
\mathscr L_{dd}=\lambda_1F_{dd}+\lambda_2F_{\alpha dd}.
\]

Using the same outward-rounded interval arithmetic as the fold certificate,
one obtains

\[
F_{dd}\in[-1.418552608575671406,-1.418552608575671095],
\]

\[
F_{\alpha dd}\in[0.7420619761682942209,0.7420619761682952559],
\]

\[
\lambda_1\in[-14.65175969596239140,-14.65175969596238834],
\]

\[
\lambda_2\in[111.3259729750753833,111.3259729750754020],
\]

and hence

\[
\boxed{
\mathscr L_{dd}\in
[103.3950634416738832,103.3950634416740212]>0.}
\]

## Symmetric tangent second variation

Inside the plane \(d=0\), a tangent vector to the double-root manifold at the
fold has \(\delta\alpha=0\) and

\[
\delta e=-\frac{F_c}{F_e}\,\delta c.
\]

The original fold certificate proves that the constrained second derivative
of \(F_\alpha\) along the fixed-\(\alpha\) curve \(F=0\) is

\[
\mathcal C_{\rm sym}
\in[0.8225821061357489653,0.8225821061357501764]>0.
\]

The second variation of \(\mathscr L\) in this tangent direction simplifies,
using the multiplier equations and the second derivative of the constraint
\(F=0\), to

\[
\lambda_2\mathcal C_{\rm sym}>0.
\]

Finally, evenness in \(d\) makes the cross term between the symmetric tangent
and the transverse \(d\)-tangent vanish. Therefore the Hessian of the exponent
coordinate restricted to the two-dimensional double-root manifold is positive
definite.

## Theorem

The certified fold is a strict nondegenerate local minimum of the double-root
exponent in the *full* strict-\(2+2\) geometry:

\[
\boxed{
\alpha\ge\nu_\dagger
}
\]

for every double-root point sufficiently close to the fold, with equality only
at \((\nu_\dagger,c_\dagger,0,e_\dagger)\).

Thus the fold is not an artifact of restricting to the equal-above family.
Any off-axis double-root branch entering a sufficiently small neighborhood is
forced to bend toward larger exponent.

This is a local theorem. It does not by itself exclude a disconnected
off-axis double-root branch elsewhere in the middle strip.

## Replay

Run

```bash
python full_fold_transverse_certificate.py
```

which imports the validated fold box and third-order interval jet from
`symmetric_fold_certificate.py` and checks the transverse Lagrangian curvature.
