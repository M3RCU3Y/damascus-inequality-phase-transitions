# Near-diagonal continuous four-variable failures

## Status

**Proved analytically, independently audited, and merged into the V6.10
research draft.**  This is a partial resolution of the continuous four-variable
inclusion problem.  It does not classify the full finite `(nu,mu)` inclusion
region.

## Theorem

For every fixed `B > sqrt(6)`, let

```
d_mu = B sqrt(mu) 2^(-mu/2).
```

Then, for all sufficiently large real `mu`,

```
I_(mu-d_mu)^4 is not contained in I_mu^4.
```

An explicit witness is

```
t_mu = 2-d_mu,
q_mu = 1-d_mu,
r_mu = q_mu^(1/mu),
a_mu = 1/(r_mu t_mu^2),
X_mu = (a_mu,r_mu,t_mu,t_mu).
```

It lies in a strict `2+2` sector for large `mu` and has product one.  The proof
establishes, for `theta` equal to `0` or `1`,

```
2^mu S_(mu-theta*d_mu)^4(X_mu)
  -> (2 theta-1) B^2/4 - 3/2.
```

Thus the source exponent (`theta=1`) is positive when `B>sqrt(6)`, whereas
the target exponent (`theta=0`) is always negative.

## Independent proof audit

Put `e=1/mu`, `q=1-d`, `t=2-d=q+1`, and `L=-log(q)`.  After cancelling the
limiting radial baseline, the middle contribution is exactly

```
F(e)=d/t+(q exp(theta*d*L*e)-1)
          /(1+q exp(-(1-theta*d)*L*e)).
```

Hence `F(0)=0` and

```
F'(0)=(2 theta-1) q L d/t^2.
```

For small `d`, the denominator stays uniformly away from zero and
`F''(e)=O(L^2)` uniformly for `theta in {0,1}`.  Therefore

```
F(1/mu)=(2 theta-1)qLd/(t^2 mu)+O(L^2/mu^2).
```

Because `d^2/mu=B^2 2^(-mu)`, `L~d`, and `qL/(t^2d)->1/4`, this supplies the
signed `B^2/4` term.  The doubled `t` coordinates contribute `-3/2` after
scaling by `2^mu`, and the `a` coordinate is `o(2^(-mu))` since `a->1/4`.
This independently confirms the displayed limit, its sign orientation, and
the threshold `B>sqrt(6)`.

The argument does **not** prove that `sqrt(6)` or this gap scale is optimal;
those questions remain open.

## Focused replay

Run:

```powershell
python continuous_near_diagonal_failure.py
```

The standard-library `decimal` script checks the explicit `B=3` witnesses at
100-digit precision and confirms convergence toward the scaled limits `3/4`
and `-15/4`.  This is a numerical sanity check, not the proof.
