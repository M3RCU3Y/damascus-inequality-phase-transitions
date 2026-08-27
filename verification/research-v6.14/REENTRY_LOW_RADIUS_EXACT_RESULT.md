# Exact re-entry complexity through five reciprocal radii

## Theorem

Let `R(k)` be the maximum number of integer-exponent membership changes of a
product-one Damascus point using exactly `k` distinct reciprocal radii. Then

\[
\boxed{R(k)=k-1\qquad(2\le k\le5).}
\]

The lower bound for every `k>=2` is the one-radius adjunction theorem. The new
content here is a self-contained audit of the low-order upper bounds, removing
the implicit lower-order dependency from the existing `R(5)=4` proof.

## Radial reduction

For a reciprocal radius `r=e^{-2x}`, `x>0`, and `s=nu+1`, every exponent
history is a linear combination of

\[
F_x(s)=\tanh(sx)-\tanh x,
\]

all of which have the common zero `F_x(1)=0`. Their derivatives are

\[
K_x(s)=x\operatorname{sech}^2(sx).
\]

For ordered radii `0<x_1<...<x_k`, if the functions `K_{x_i}` form an
extended Chebyshev system, any nonzero derivative combination has at most
`k-1` zeros. A history with `k` distinct zeros for `s>1`, together with the
common zero at `s=1`, would force at least `k` derivative zeros by Rolle's
theorem, a contradiction. Therefore the history has at most `k-1` positive
zeros and hence at most `k-1` integer membership changes.

## Initial Wronskians through order four

Put

\[
q_0(u)=\operatorname{sech}^2u,
\qquad
g_j(u)=u^j q_0^{(j)}(u).
\]

As in the archived order-five proof, generalized evaluation determinants for
`K_x(s)` reduce to the initial Wronskians

\[
W_m(u)=W(g_0,\ldots,g_{m-1})(u),\qquad m=1,\ldots,k.
\]

The existing order-five certificate proves the new `m=5` case. The verifier
`reentry_low_order_verify.py` independently certifies every missing initial
Wronskian `m<=4` on the complete half-line `u>0`.

For each order, substituting `y=tanh u` and then

\[
y=\frac{1-q}{1+q},\qquad q=e^{-2u},
\]

reduces nonvanishing to positivity of an explicit oriented integer polynomial
`P_m(u,e^{-2u})`. The proof is split into three rigorous ranges:

1. **`0<u<=1/10`.** Exact rational Taylor expansion with an absolute
   Lagrange remainder, followed by exact Bernstein positivity after factoring
   the known vanishing order `m(m-1)/2`.
2. **`1/10<=u<=8`.** A deterministic 670-box outward-rounded Decimal
   interval certificate, using exact integer polynomial derivatives and a
   deliberately inflated enclosure for every exponential.
3. **`u>=8`.** Every `q`-dependent monomial `u^i e^{-2ju}` is decreasing in
   this range. Its total absolute correction is bounded by the value at `u=8`
   and is strictly smaller than the positive `q^0` term.

The certified margins are:

| order | small-range minimum Bernstein coefficient | weakest middle lower margin | tail lower margin |
|---:|---:|---:|---:|
| 2 | `>13.1434` | `>1.31434` | `>1.99999` |
| 3 | `>6048.69` | `>6.04863` | `>15.9992` |
| 4 | `>1.863e8` | `>186.065` | `>767.679` |

Thus all initial Wronskians through order four are nonzero. Together with the
archived order-five certificate, the derivative kernel is ECT through order
five.

Consequently

\[
R(k)\le k-1\qquad(2\le k\le5).
\]

The one-radius adjunction theorem supplies the matching lower bounds
`R(k)>=k-1`, proving the theorem.

## Why the result stops at six

The unrestricted order-six scalar Wronskian changes sign, so this ECT proof
cannot be extended mechanically. A sharp result for `R(6)` must use the
product-one/multiplicity feasibility constraint. This is a structural
obstruction in the method, not evidence that `R(6)>5`.

## Replay

Run

```bash
python reentry_low_order_verify.py
python ../research-v6.13/reentry_r5_verify.py
```

The first command supplies the previously implicit orders `1` through `4`;
the archived second command supplies order `5`.
