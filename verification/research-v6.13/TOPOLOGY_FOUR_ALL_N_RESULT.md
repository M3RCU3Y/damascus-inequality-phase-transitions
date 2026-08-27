# Uniform four-variable ordered-pocket theorem for every integer exponent

## Theorem

For every integer `n>=4`, each nonempty ordered strict `2+2` chamber of the
four-variable violation set is homeomorphic to

\[
\mathcal B_n\times(0,1),
\]

where `B_n` is the corresponding labelled three-variable trace sector. If one
adjoins the coordinate-`1` trace to an ordered pocket, the augmented set
strongly deformation-retracts onto that trace.

Together with the uniform three-variable topology theorem, this implies

\[
\boxed{\text{for every integer }n\ge4,\text{ the strict }2+2\text{ locus has exactly }12\text{ contractible components}.}
\]

This removes the former exponent-`10` cutoff.

## 1. Ordered pair chart

Write one ordered `2+2` chamber as

\[
(x_1,x_2,x_3,x_4)
=\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
\qquad c>0,\quad |d|<e<c.
\]

Put `t=e^c`. In the pair-product chart used in the earlier certificate,

\[
xy=ab=t^2,
\]

\[
x+y=2t+u(t-1)^2,
\qquad
a+b=2t+v(t-1)^2,
\]

and the ordered chamber is

\[
t>1,\qquad 0\le u<v<1.
\]

At `v=u` the lower reciprocal pair matches the upper pair and the reciprocal
identity gives `S_n^4<0`. At `v=1`, one lower coordinate reaches `1` and

\[
S_n^4(t,u,1)=S_n^3(x,y,t^{-2}).
\]

Thus it suffices to prove two uniform facts:

1. no violation occurs for `1<t<=T_n`, where
   \[
   T_n=1+\frac4{n^2};
   \]
2. for `t>=T_n`, spreading the lower pair strictly increases `S_n^4`.

## 2. Uniform lower-pair spreading for `t>=T_n`

Define

\[
\phi_n(z)=\frac{z^n-1}{z^{n+1}+1},
\qquad
h_n(z)=z\phi_n'(z)
=\frac{z^n\{n+(n+1)z-z^{n+1}\}}{(1+z^{n+1})^2}.
\]

On `(0,1)`, `h_n` is positive. Its derivative is

\[
h_n'(z)=\frac{z^{n-1}P_n(z)}{(1+z^{n+1})^3},
\]

where

\[
P_n(z)=z^{2n+2}-(n+1)^2z^{n+2}
-(n^2+4n+1)z^{n+1}+(n+1)^2z+n^2.
\]

The coefficient signs of `P_n` give at most two positive roots. Since
`P_n(0)>0`, `P_n(1)<0`, and `P_n(z)->+infinity`, there is exactly one root in
`(0,1)` and one above `1`. Hence `h_n` increases once and then decreases on
`(0,1)`.

Because `h_n(0)=0`, `h_n(1)=n/2`, and `h_n'(1)<0`, there is a unique
`q_n in (0,1)` different from `1` such that

\[
h_n(q_n)=\frac n2.
\]

The point `q_n` lies on the increasing branch.

### Uniform location of `q_n`

Set

\[
z_n=\frac1{T_n}=\frac{n^2}{n^2+4}.
\]

The equation `h_n(z)=n/2` can be rewritten by setting `A=z^{n+1}` as

\[
(2+nz)A^2-2(n+z)A+nz=0.
\]

Its smaller root gives the nontrivial crossing and, after rationalization,

\[
z^n=\frac{n}{n+z+D(z)},
\qquad
D(z)=\sqrt{n^2(1-z^2)+z^2}.
\]

At `z=z_n`, Bernoulli's inequality gives

\[
z_n^n=(1+4/n^2)^{-n}<\frac n{n+4}.
\]

Also

\[
9-D(z_n)^2
=\frac{8(7n^2+18)}{(n^2+4)^2}>0,
\]

so `D(z_n)<3`, and therefore

\[
n+z_n+D(z_n)<n+4.
\]

Consequently

\[
z_n^n<\frac n{n+4}
<\frac n{n+z_n+D(z_n)},
\]

which means `h_n(z_n)<n/2`. Hence

\[
\boxed{q_n>z_n=1/T_n.}
\]

Now fix `t>=T_n` and a strict lower pair

\[
0<z_-<z_+<1,
\qquad z_-z_+=t^{-2}.
\]

Its geometric mean is `1/t<=1/T_n<q_n`.

If `z_+<=q_n`, both points lie on the increasing branch of `h_n`, so
`h_n(z_+)>h_n(z_-)`. If `z_+>q_n`, then

\[
h_n(z_+)>n/2>h_n(z_-).
\]

Thus in every case

\[
\boxed{h_n(z_+)>h_n(z_-).}
\]

Since

\[
\frac{\partial}{\partial e}
\{\phi_n(e^{-c+e})+\phi_n(e^{-c-e})\}
=h_n(e^{-c+e})-h_n(e^{-c-e}),
\]

we obtain strict lower-pair spreading:

\[
\boxed{\partial_e S_n^4>0\quad\text{for }t\ge T_n,\ 0<e<c.}
\]

Equivalently, `partial_v S_n^4>0` throughout the ordered tail.

## 3. Exact low-box exclusion for `4<=n<=11`

For the finitely many exponents `4,...,11`, use the cleared numerator of
`S_n^4` in the pair chart. Make the triangular substitution

\[
v=u+(1-u)w
\]

and the affine substitution

\[
t=1+(T_n-1)s,
\qquad 0\le s,u,w\le1.
\]

Every tensor-product Bernstein coefficient of the negative cleared numerator
is nonnegative. The exact nonzero/zero counts are

| `n` | degree `(s,u,w)` | positive coefficients | zero coefficients |
|---:|---:|---:|---:|
| 4 | `(20,10,5)` | 1254 | 132 |
| 5 | `(24,12,6)` | 2093 | 182 |
| 6 | `(28,14,7)` | 3240 | 240 |
| 7 | `(32,16,8)` | 4743 | 306 |
| 8 | `(36,18,9)` | 6650 | 380 |
| 9 | `(40,20,10)` | 9009 | 462 |
| 10 | `(44,22,11)` | 11868 | 552 |
| 11 | `(48,24,12)` | 15275 | 650 |

No coefficient is negative. Therefore

\[
S_n^4\le0
\]

on the entire low box for `4<=n<=11`.

## 4. Uniform low-box exclusion for `n>=12`

Use logarithmic coordinates `u_j` for the four coordinates. In a strict
`2+2` chamber, two `u_j` are positive, two are negative, and

\[
\sum_{j=1}^4u_j=0.
\]

If `t=e^c<=1+4/n^2`, then `|u_j|<2c<8/n^2`. Put

\[
a_j=nu_j,
\qquad
\varepsilon=1/n,
\qquad
A=\max_j|a_j|.
\]

For `n>=12`,

\[
A\le8\varepsilon\le\frac23.
\]

Define

\[
F_\varepsilon(a)
=\phi_n(e^{a/n})
=\frac{e^a-1}{1+e^{(1+\varepsilon)a}}.
\]

Taylor expansion at zero gives

\[
F_\varepsilon(a)
=\frac a2-\frac{\varepsilon a^2}{4}
-\frac{(1+3\varepsilon)a^3}{24}
+\frac{\varepsilon(1+3\varepsilon+\varepsilon^2)a^4}{48}
+R_5(a),
\]

and the exact interval certificate described below proves

\[
\boxed{|F_\varepsilon^{(5)}(a)|<1}
\]

for

\[
|a|\le2/3,
\qquad 0\le\varepsilon\le1/12.
\]

Hence

\[
|R_5(a)|\le\frac{|a|^5}{120}.
\]

### Cubic moment inequality

For four real numbers with two positive and two negative entries, zero sum,
and `A=max |a_j|`,

\[
-\sum_j a_j^3
\le\frac A2\sum_j a_j^2.
\]

Write the positive pair as `L/2+-p` and the magnitudes of the negative pair as
`L/2+-r`, with `0<=p<=r<=L/2` in the only nontrivial case. After scaling
`x=2r/L`, `y=2p/L`, the desired inequality reduces to

\[
3(x^2-y^2)
\le(1+x)\left(1+\frac{x^2+y^2}{2}\right).
\]

The left side decreases and the right side increases with `y^2`, so it is
enough to set `y=0`. The remaining inequality is

\[
2+2x-5x^2+x^3
=(x-1)(x^2-4x-2)\ge0
\]

for `0<=x<=1`.

Also

\[
\sum_j a_j^4\le A^2\sum_j a_j^2,
\qquad
\sum_j|a_j|^5\le A^3\sum_j a_j^2.
\]

Using `sum a_j=0`, summing the Taylor formula yields

\[
S_n^4\le
\left(\sum_j a_j^2\right)
\left[
-\frac\varepsilon4
+\frac{(1+3\varepsilon)A}{48}
+\frac{\varepsilon(1+3\varepsilon+\varepsilon^2)A^2}{48}
+\frac{A^3}{120}
\right].
\]

Since `A<=8\varepsilon`, the bracket is at most

\[
B(\varepsilon)
=-\frac\varepsilon4
+\frac{\varepsilon(1+3\varepsilon)}6
+\frac43\varepsilon^3(1+3\varepsilon+\varepsilon^2)
+\frac{64}{15}\varepsilon^3.
\]

Exactly,

\[
B(\varepsilon)
=\frac\varepsilon{60}
\left(80\varepsilon^4+240\varepsilon^3+336\varepsilon^2+30\varepsilon-5\right).
\]

The polynomial in parentheses is strictly increasing for positive
`varepsilon`, and at `varepsilon=1/12` it equals `-31/1296`. Thus

\[
\boxed{B(\varepsilon)<0\quad(0<\varepsilon\le1/12).}
\]

Therefore the strict `2+2` low box contains no violations for every `n>=12`.

### Exact fifth-derivative certificate

The verifier writes `X=e^a`, `Y=e^{(1+varepsilon)a}`, `p=1+varepsilon` and
expresses `F^(5)` as an explicit integer polynomial in `(X,Y,p)` divided by
`(1+Y)^6`. The rectangle

\[
-2/3\le a\le2/3,
\qquad 1\le p\le13/12
\]

is recursively subdivided. Exponential enclosures are rational Taylor bounds
with a rational geometric-tail majorant. All subsequent interval operations
use `Fraction` arithmetic. The complete certificate closes with 385 nodes,
193 terminal boxes, and maximum depth 9; every terminal comparison proves
`|F^(5)|<1` exactly.

## 5. Interval-bundle conclusion

Sections 2--4 prove, for every integer `n>=4`,

\[
S_n^4\le0\quad(1<t\le T_n)
\]

and

\[
\partial_vS_n^4>0\quad(t\ge T_n,\ 0<v<1).
\]

At `v=u`, `S_n^4<0`, while at `v=1` the value equals the three-variable trace
function. Hence a strict ordered fiber is nonempty exactly over
`(t,u) in B_n`, and over each such base point there is a unique threshold
`V_n(t,u) in (u,1)` with

\[
S_n^4>0\iff V_n(t,u)<v<1.
\]

The implicit-function theorem makes `V_n` continuous. Consequently each
ordered pocket is homeomorphic to `B_n x (0,1)`.

Increasing the lower-pair spread from a violating point to the coordinate-`1`
trace strictly increases `S_n^4`; therefore the pocket together with its trace
strongly deformation-retracts onto that trace.

The uniform three-variable theorem gives that every `B_n` is contractible.
There are six choices of the two above-one coordinates and two orderings of the
below-one pair. Thus the strict `2+2` locus has exactly twelve contractible
components for every integer `n>=4`.

## Replay

Run

```bash
python topology_four_all_n_audit.py
```

The replay performs the exact finite Bernstein checks for `n=4,...,11`, checks
the algebra used in the uniform tail and Taylor arguments, and independently
replays the rational interval certificate for the fifth derivative bound.
