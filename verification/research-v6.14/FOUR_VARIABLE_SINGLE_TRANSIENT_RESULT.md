# A single-transient theorem for strict four-variable 2+2 points

## Theorem

Fix a product-one point in a strict four-variable `2+2` sign sector. As a
function of the real exponent `nu>0`, its Damascus history has at most two
positive real zeros, counted without multiplicity. In particular, on
`nu>=1` its violation set is either empty or one bounded open interval.

Thus a strict four-variable `2+2` point cannot undergo multiple separated
re-entry episodes. The unresolved continuous inclusion diagram is an envelope
of single transient intervals.

## Ordered radial signs

Write one ordered chamber as

\[
(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}),
\qquad 0\le d<e<c.
\]

For a reciprocal radius `r=e^{-2x}` and `s=nu+1`, put

\[
F_x(s)=\tanh(sx)-\tanh x,
\qquad
K_x(s)=F_x'(s)=x\operatorname{sech}^2(sx).
\]

The exact identities

\[
\phi_\nu(e^{2x})=\frac{1+e^{-2x}}2F_x(s),
\qquad
\phi_\nu(e^{-2x})=-\frac{1+e^{-2x}}{2e^{-2x}}F_x(s)
\]

show that an above-one coordinate contributes a positive multiple of `F_x`,
while a below-one coordinate contributes a negative multiple.

The four ordered radial frequencies are

\[
0<\frac{c-e}{2}<\frac{c-d}{2}\le\frac{c+d}{2}<\frac{c+e}{2}.
\]

When `d>0` they are distinct and their coefficient signs are exactly

\[
\boxed{-,+,+,-,}
\]

which has two sign changes. When `d=0`, the middle two frequencies coalesce,
leaving the three-radius sign pattern `-,+,-`, again with two sign changes.

## Variation bound

The V6.14 low-order Wronskian certificate, together with the same generalized
evaluation-determinant argument used in the archived order-five proof, shows
that the kernel

\[
K(s,x)=x\operatorname{sech}^2(sx)
\]

is strictly sign-regular, equivalently strictly totally positive up to order
four, on `s>1`, `x>0`. Hence the generalized Descartes rule applies: a linear
combination of the ordered functions `K_{x_i}` has no more zeros than the
number of sign changes of its ordered coefficients.

If

\[
H(s)=S_{s-1}^4(X),
\]

then

\[
H'(s)=\sum_i c_iK_{x_i}(s)
\]

has at most two zeros on `s>1` because the coefficient pattern has two sign
changes.

All radial functions satisfy `F_x(1)=0`, so every history has the common zero
`H(1)=0`, corresponding to exponent `nu=0`. If `H` had three distinct zeros
strictly above `s=1`, Rolle's theorem on the three intervals between the four
ordered zeros would force at least three zeros of `H'`, contradiction.
Therefore

\[
\boxed{H\text{ has at most two zeros on }s>1.}
\]

Equivalently, the real-exponent Damascus history has at most two positive
zeros.

## Consequence on nu>=1

The fixed-exponent theorem gives `I_1^4=emptyset`, so every product-one point
has `S_1^4<=0`. For a strict `2+2` point the eventual radial constant is

\[
L=\frac1{x_1}+\frac1{x_2}-2<0,
\]

where `x_1,x_2>1` are its two above-one coordinates. Hence the history is also
negative for all sufficiently large exponents.

With at most two positive zeros available, positivity on `nu>=1` can therefore
occur only on one bounded interval. Tangential zero cases simply collapse one
or both endpoints and do not create another component of the positivity set.

## Significance for the phase diagram

Every strict `2+2` point contributes at most one ordered root pair

\[
\nu_-(X)<\nu_+(X).
\]

Consequently the complete four-variable real-exponent inclusion problem can
be formulated as the lower envelope of the exit roots `nu_+(X)` among points
whose entry root is at or below a prescribed source exponent. The numerical
symmetric branch near `nu_dagger` is therefore a candidate envelope of
single pulses, rather than one branch among histories with uncontrolled
oscillation.
