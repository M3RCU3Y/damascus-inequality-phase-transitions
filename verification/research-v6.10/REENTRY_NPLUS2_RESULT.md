# Sharper reciprocal-radius and dimension construction

Status: **proved analytic theorem, independently audited, and merged into the
V6.10 research draft**.  `reentry_nplus2_audit.js` replays all finite rational
inequalities and the coefficient/moment/count bookkeeping.  Its floating-point
sample check is evidence only and is not used in the proof.

## Theorem

For every integer `N>=1`, there is a point in dimension `2N+3` whose
integer-exponent membership sequence changes value at least `N` times and whose
coordinates use exactly `N+2` distinct reciprocal radii.

Thus it improves both V6.9 counts (`N+3` radii and dimension `2N+4`) by one.

## A sharply localized positive pulse

Put

```text
R=100,   a=(R+1)/2=101/2,   tau=1/10,
H(t)=-tanh(t/2)+2tanh(at/2)-tanh(Rt/2).
```

Strict concavity of `tanh` on `(0,infinity)` gives `H(t)>0`, because `at/2`
is the midpoint of `t/2` and `Rt/2`.

At `t=tau`, use `tanh(tau/2)<tau/2=1/20`, `tanh(Rtau/2)<1`, and
`tanh(a tau/2)>147/149`.  The last inequality follows from
`exp(2a tau/2)=exp(101/20)>exp(5)>148` and
`tanh z=(exp(2z)-1)/(exp(2z)+1)`; `exp(5)>148` follows directly by truncating
its positive Taylor series.  Hence

```text
H(tau)>-1/20+2(147/149)-1=2751/2980.              (1)
```

For small scales, the centered second-difference formula and
`|tanh''|<2` give

```text
0<H(t)<(R-1)^2 t^2/8<R^2t^2/8.
```

Therefore

```text
sum_(h>=1)H(tau R^{-h})
 < tau^2/[8(1-R^{-2})]=25/19998<1/792.            (2)
```

For large scales,

```text
0<H(t)<1-tanh(t/2)<2e^{-t}.
```

Since `tau R^h>=10h` and `e^10>10000`,

```text
sum_(h>=1)H(tau R^h)
 <2 sum_(h>=1)e^{-10h}=2/(e^10-1)<1/4000.         (3)
```

Combining (1)--(3), every central pulse dominates all other scales by

```text
Delta=2751/2980-1/792-1/4000
     =54380549/59004000>0.                         (4)
```

For fixed `N`, define

```text
F_N(t)=sum_(j=0)^(N-1)(-1)^j H(R^j t),
t_j=tau R^{-j}  (0<=j<N).
```

Then (4) yields

```text
(-1)^j F_N(t_j)>Delta.                             (5)
```

## Endpoint perturbation and tail sign

Write `sigma=(-1)^N` and put

```text
G_N(t)=F_N(t)-tanh(t/2)
       +sigma{tanh((R^N+sigma)t/2)-tanh(R^N t/2)}. (6)
```

The final correction is positive for either sign of `sigma`.  At even `j` it
helps the desired positive sign, while `tanh(t_j/2)<1/20`; hence

```text
G_N(t_j)>Delta-1/20>0.
```

At odd `j`, the low endpoint helps the desired negative sign.  If `sigma=1`,
then `R^N t_j>=10`; if `sigma=-1`, then `N` and `j` are odd, so `j<=N-2` and
`(R^N-1)t_j>10`.  In either case the adverse correction is less than
`2e^{-10}<1/4000`.  Thus

```text
-G_N(t_j)>Delta-1/4000>0.
```

Consequently `sign G_N(t_j)=(-1)^j` at every sample.  Telescoping (6) gives

```text
c_1=-2,
c_(aR^j)=2(-1)^j       (0<=j<N),
c_(R^N+sigma)=sigma.
```

The moment is exactly

```text
-2+2a sum_(j=0)^(N-1)(-R)^j+sigma(R^N+sigma)
=-2+(1-sigma R^N)+sigma R^N+1=0,
```

because `2a=R+1`.  Its coefficient sum is always `-1`, so `G_N(t)->-1`.

The sample parameters satisfy `t_(N-1)<...<t_1<t_0`.  Read in increasing
parameter order, their signs still alternate and hence supply `N-1` changes;
the final (largest-parameter) sample `t_0` is positive.  A still later negative
tail sample supplies the `N`th change.  There are `N+2` frequencies and the
dimension is `2+2N+1=2N+3`.

## Discrete lifting

Let the collected signed multiplicities be `c_w`.  For `eps>0`, take `c_w`
copies of `exp(w eps)` when `c_w>0` and `-c_w` copies of `exp(-w eps)` when
`c_w<0`.  The exact moment identities above give product one.  Frequencies need
not be integral: `a=101/2` is allowed because the coordinates are simply
`exp(+/-w eps)`; only the multiplicities are required to be integers.

For `n_eps(t)=floor(t/eps)`, the V6.9 lifting limit is

```text
phi_(n_eps(t))(exp(w eps))->tanh(wt/2),
phi_(n_eps(t))(exp(-w eps))->-tanh(wt/2).
```

Choose the finite alternating samples above plus one tail sample strictly
larger than `t_0` at which `G_N<0`.  Then choose `eps` small enough that all
limiting signs are preserved and all integers `n_eps(t)` are distinct.  Reading
those integers in increasing order proves at least `N` changes in the discrete
membership sequence.

## What remains open

This is a simultaneous one-unit improvement in the general construction, not
an optimality theorem.  Whether `N+2` radii or dimension `2N+3` is necessary,
and the best joint tradeoff, remain open.  No improved universal upper bound
over V6.9's `2^k-2` was proved here.
