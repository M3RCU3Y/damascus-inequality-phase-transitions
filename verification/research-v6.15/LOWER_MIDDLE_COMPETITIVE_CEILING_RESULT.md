# Uniform competitive target ceiling on 4.05 <= nu <= 6

**Status:** `CERTIFIED-GLOBAL` on the stated source interval, conditional only on the already-proved V6.14 single-transient theorem.

Consider the rational equal-above point

\[
X_*=
\left(
 e^{0.43545},e^{0.43545},
 e^{-0.43545+0.43231},e^{-0.43545-0.43231}
\right).
\]

The outward-rounded interval certificate

```text
lower_middle_competitive_ceiling.py
```

proves

\[
S^4_{4.05}(X_*)>0,
\qquad
S^4_6(X_*)>0,
\qquad
S^4_{200}(X_*)<0.
\]

V6.14 proves that every strict `2+2` exponent history has at most one bounded positive interval on exponents at least one.  Since the same history is positive at both endpoints `4.05` and `6`, it is positive throughout

\[
[4.05,6].
\]

Therefore for every source exponent

\[
4.05\le\nu\le6
\]

the same point belongs to `I^4_nu` but not to `I^4_200`.  Consequently inclusion has already failed by target `200`, and the globally earliest later exit satisfies

\[
\boxed{\mu_*(\nu)<200.}
\]

This complements the stronger V6.14 ceiling

\[
\mu_*(\nu)<9.62
\qquad(6\le\nu\le\nu_\dagger).
\]

Hence every competitive middle-strip minimizer with source at least `4.05` lies in a finite target range:

\[
\boxed{
4.05\le\nu\le6\Rightarrow\mu<200,
\qquad
6\le\nu\le\nu_\dagger\Rightarrow\mu<9.62.
}
\]
