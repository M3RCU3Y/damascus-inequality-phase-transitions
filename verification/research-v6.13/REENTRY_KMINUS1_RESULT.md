# A one-radius adjunction theorem for re-entry complexity

## Result

Let `R(k)` denote the maximum number of integer-exponent membership changes
realized by a product-one Damascus point using exactly `k` distinct reciprocal
radii. Then

\[
\boxed{R(k)\ge k-1\qquad(k\ge2).}
\]

Equivalently, for every integer `N>=1`, at least `N` membership changes can be
realized with exactly `N+1` reciprocal radii.

This improves the earlier general `N+2`-radius construction by one radius.
The proof is an induction based on a product-neutral block which introduces
one new radius while leaving any prescribed finite set of exponent signs
arbitrarily easy to protect by replication.

## Extension lemma

Suppose a product-one point `X` uses exactly `k` reciprocal radii and has
alternating nonzero values at integer exponents

\[
n_0<n_1<\cdots<n_r,
\]

so it realizes at least `r` membership changes. Assume also that

\[
L(X)=\lim_{n\to\infty}S_n(X)\ne0.
\]

Choose one existing reciprocal radius `Q>1`. For an integer `A>=1`, put

\[
R_A=Q^{1/A}>1.
\]

There are two product-neutral blocks.

### Positive-tail block

Take `A` copies of `R_A` and one copy of `Q^{-1}`. Their product is one,
because

\[
R_A^A Q^{-1}=1.
\]

Their contribution is

\[
T_{n,A}^{+}=A\phi_n(R_A)+\phi_n(Q^{-1}).
\]

For each fixed integer `n`, the derivative

\[
\phi_n'(1)=\frac n2
\]

and `R_A=\exp((\log Q)/A)` give

\[
A\phi_n(R_A)\longrightarrow \frac{n\log Q}{2}.
\]

Hence `T_{n,A}^{+}` stays bounded as `A->infinity` for every fixed `n`.
On the other hand,

\[
\lim_{n\to\infty}T_{n,A}^{+}
=\frac{A}{R_A}-1\longrightarrow +\infty
\qquad(A\to\infty).
\]

### Negative-tail block

Take `A` copies of `R_A^{-1}` and one copy of `Q`. Again the product is one:

\[
R_A^{-A}Q=1.
\]

The contribution

\[
T_{n,A}^{-}=A\phi_n(R_A^{-1})+\phi_n(Q)
\]

is bounded at each fixed exponent as `A->infinity`, while

\[
\lim_{n\to\infty}T_{n,A}^{-}
=-A+\frac1Q\longrightarrow-\infty.
\]

Thus either eventual sign can be forced with one new reciprocal radius.

## Preserving the old changes

Let

\[
\delta=\min_{0\le j\le r}|S_{n_j}(X)|>0.
\]

Choose the block orientation whose eventual sign is opposite to the sign at
the final witness exponent `n_r`. Since the chosen block is bounded at the
finite set `n_0,...,n_r` for all sufficiently large `A`, there are constants
`C` and `A_0` such that

\[
|T_{n_j,A}^{\pm}|\le C
\]

for every `j` and `A>=A_0`.

Now replace `X` by `M` disjoint copies of itself, where

\[
M\delta>C.
\]

Replication preserves the product-one condition, the reciprocal radii, and
the signs at all the witness exponents. Add the product-neutral block. For
every `A>=A_0`, the combined point still has the same alternating signs at
`n_0,...,n_r`.

Finally choose `A` so large that the block's eventual limit dominates
`M L(X)` and has the sign opposite to `S_{n_r}(X)`. The combined history
therefore has some later integer exponent with the opposite sign, adding at
least one further membership change.

For sufficiently large `A`, `R_A` lies strictly between `1` and the smallest
old reciprocal radius, so it is genuinely new. Hence the number of distinct
reciprocal radii increases from `k` to exactly `k+1`.

The new eventual limit is nonzero, so the lemma can be iterated.

## Exact two-radius base point

Let

\[
q=\frac{23}{20}
\]

and take the point with

- six copies of `q`,
- three copies of `q^{-1}`,
- three copies of `q^3`, and
- four copies of `q^{-3}`.

Its product is exactly one because

\[
6-3+9-12=0.
\]

It uses exactly two reciprocal radii, `q` and `q^3`. Exact rational arithmetic
gives

\[
S_{21}<0<S_{22},
\]

so it has at least one membership change. Its limiting value is

\[
L=\frac6q+\frac3{q^3}-7
 =\frac{2311}{12167}>0.
\]

Thus the extension lemma starts at `k=2` and iterates indefinitely. Therefore

\[
\boxed{R(k)\ge k-1\quad(k\ge2).}
\]

## Replay

Run

```bash
python reentry_kminus1_base.py
```

for the exact base-point product, sign, and limiting-value audit. The induction
step is analytic; the script is not used as a substitute for it.
