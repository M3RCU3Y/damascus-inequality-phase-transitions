# Four-variable transient-pocket topology: exact partial resolution

Status: **proved for the statements below and merged into the V6.10 research
draft; not yet folded into an immutable verification-supplement release**.

This note addresses Open Problem 2 in the V6.9 handoff.  It does not re-audit
the manuscript's settled results.  Its only computer-assisted inputs are the
new exact-integer Bernstein certificates replayed by
`topology_four_exact.js`.

## 1. Statement of the result

Fix an exponent `n >= 4`.  In one labelled `2+2` sign sector write

\[
 (x_1,x_2,x_3,x_4)
 =\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
 \qquad c>0,\quad |d|<c,\quad |e|<c.
\]

The product is one.  The two choices `e>0` and `e<0` specify which of the
two below-one coordinates is closer to one.  Call either choice an
**ordered `2+2` chamber**.  Let

\[
 \mathcal B_n=
 \left\{(c,d):c>0,\ |d|<c,\quad
 S_n^3(e^{c+d},e^{c-d},e^{-2c})>0\right\}.
\]

Thus `B_n` is one labelled three-variable sign sector.

### Theorem A (exact interval-bundle reduction, `4 <= n <= 10`)

For every `n=4,...,10`, each nonempty ordered strict `2+2` chamber of
`I_n^4` is homeomorphic to

\[
 \mathcal B_n\times(0,1).
\]

In particular, its connected components and homotopy type are exactly those
of `B_n`.

If the chamber with `e>0` is augmented by its attaching coordinate trace
`e=c`, then the augmented set strongly deformation-retracts onto

\[
 \bigl\{(e^{c+d},e^{c-d},1,e^{-2c}):(c,d)\in\mathcal B_n\bigr\}
 \subset I_n^4.
\]

The analogous statement for `e<0` attaches to the other below-one
coordinate face.  The endpoint is an actual point of `I_n^4`, not merely a
limit outside the violation set, because a unit coordinate contributes
zero and the remaining three coordinates form a point of `I_n^3`.

### Theorem B (complete strict-pocket topology through exponent 6)

For each `n=4,5,6`, the strict `2+2` portion of `I_n^4` has exactly

\[
 \boxed{12}
\]

connected components, and every component is contractible.

There are six choices of the two coordinates above one and, in each such
sign sector, two possible orderings of the coordinates below one.  No
further splitting occurs.  For `n<=3` the strict `2+2` portion is empty by
the already-established low-exponent results in V6.9.

Theorem B is a complete classification of the first three nonempty
integer-exponent transient pockets.  For `n=7,...,10`, Theorem A is a
rigorous reduction, not a complete classification: the remaining topology
is precisely the still-open topology of the corresponding three-variable
sector, including its off-axis tongues.

## 2. Pair-product chart

Use the V6.9 symmetric chart

\[
 x,y>1,\qquad a^{-1},b^{-1}<1,\qquad xy=ab=p=t^2,
\]

and put

\[
 q=x+y=2t+u(t-1)^2,
 \qquad
 r=a+b=2t+v(t-1)^2.
\]

The ordered chamber is

\[
 t>1,\qquad 0\le u<v<1.
\]

Indeed, if `t=e^c`, then

\[
 u=\frac{2t(\cosh d-1)}{(t-1)^2},
 \qquad
 v=\frac{2t(\cosh e-1)}{(t-1)^2}.
\]

The strict inequality `u<v` is exactly the spread-inversion obstruction
already proved in V6.9.

Let `P_0(Q)=2`, `P_1(Q)=Q`, and

\[
 P_k(Q)=QP_{k-1}(Q)-pP_{k-2}(Q).
\]

Then, exactly as in the manuscript,

\[
 A_n(t,u)=
 \frac{p^nq+P_n(q)-P_{n+1}(q)-2}
 {p^{n+1}+1+P_{n+1}(q)},
\]

\[
 C_n(t,v)=
 \frac{2p^{n+1}+P_{n+1}(r)-pP_n(r)-r}
 {p^{n+1}+1+P_{n+1}(r)},
\]

and

\[
 S_n^4=A_n(t,u)-C_n(t,v).
\]

Both displayed denominators are strictly positive.

## 3. New exact monotonicity lemma

Define the rational thresholds

\[
\begin{array}{c|rrrrrrr}
n&4&5&6&7&8&9&10\\ \hline
T_n&4/3&6/5&9/8&11/10&21/20&26/25&26/25.
\end{array}
\]

### Lemma C (certified exclusion and lower-pair spreading)

For each `n=4,...,10`:

1. `S_n^4(t,u,v) <= 0` on `1 <= t <= T_n` and
   `0 <= u <= v <= 1`.
2. `partial_v S_n^4(t,u,v) > 0` on `t >= T_n` and
   `0 < v < 1`.

#### Exact certificate

Let `N_n(t,u,v)` be the cleared numerator of `S_n^4`.  For the first
claim make the triangular substitution

\[
 v=u+(1-u)w
\]

and the affine substitution `t=1+(T_n-1)s`.  Every tensor-product
Bernstein coefficient of `-N_n` on the unit cube is nonnegative.

For the second claim, let `D_n` be the cleared numerator of
`partial_v C_n`.  Compactify the tail by

\[
 t=\frac{T_n+(1-T_n)s}{1-s},\qquad 0\le s<1.
\]

After multiplication by the positive clearing power of `1-s`, every
Bernstein coefficient of `-D_n` is nonnegative.  At least one coefficient
is positive in the interior, and the `s=0` face has a positive coefficient,
so `D_n<0` for `t>=T_n` and `0<v<1`.  Since
`partial_v S_n^4=-partial_v C_n`, the asserted strict inequality follows.

The exact coefficient counts are:

| `n` | low-box degree `(s,u,w)` | positive / total coefficients | tail degree `(s,v)` | positive / total coefficients |
|---:|---:|---:|---:|---:|
| 4 | `(20,10,5)` | `1254 / 1386` | `(20,8)` | `183 / 189` |
| 5 | `(24,12,6)` | `2093 / 2275` | `(24,10)` | `265 / 275` |
| 6 | `(28,14,7)` | `3240 / 3480` | `(28,12)` | `362 / 377` |
| 7 | `(32,16,8)` | `4743 / 5049` | `(32,14)` | `474 / 495` |
| 8 | `(36,18,9)` | `6650 / 7030` | `(36,16)` | `601 / 629` |
| 9 | `(40,20,10)` | `9009 / 9471` | `(40,18)` | `743 / 779` |
| 10 | `(44,22,11)` | `11868 / 12420` | `(44,20)` | `900 / 945` |

All unlisted coefficients are zero; none is negative.  The replay derives
the symmetric rational functions from the recurrence, differentiates them,
performs both substitutions, and converts power coefficients to Bernstein
coefficients using `BigInt` arithmetic only.

## 4. Proof of Theorem A

At `v=u`, the pairs `{x,y}` and `{a,b}` coincide.  The reciprocal identity
therefore gives

\[
 S_n^4(t,u,u)
 =\sum_{z\in\{x,y\}}\bigl(\phi_n(z)+\phi_n(1/z)\bigr)<0.
\]

At `v=1`, the roots of the lower-pair quadratic are `t^2` and `1`, so

\[
 S_n^4(t,u,1)
 =S_n^3(x,y,t^{-2}).
\]

By Lemma C, any violating point has `t>T_n`, and for fixed `(t,u)` the
function `v -> S_n^4(t,u,v)` is strictly increasing.  Consequently

\[
 S_n^4(t,u,v)>0\text{ for some }u<v<1
 \quad\Longleftrightarrow\quad
 S_n^4(t,u,1)>0.
\]

For every `(t,u)` in the trace sector there is a unique

\[
 V_n(t,u)\in(u,1)
\]

such that `S_n^4(t,u,V_n)=0`, and positivity holds exactly when
`V_n(t,u)<v<1`.  The strict derivative and the implicit-function theorem
make `V_n` continuous (indeed real analytic in the open chart).

Return to signed logarithmic spread `d` and the ordered choice `e>0`.
Because `e -> v(t,e)` is a diffeomorphism from `(0,c)` to `(0,1)`, there is
a continuous threshold `E_n(c,d)` with

\[
 \mathcal P_n^+
 =\{(c,d,e):(c,d)\in\mathcal B_n,
             \ E_n(c,d)<e<c\}.
\]

The map

\[
 ((c,d),\lambda)\longmapsto
 \bigl(c,d,E_n(c,d)+\lambda(c-E_n(c,d))\bigr),
 \qquad 0<\lambda<1,
\]

is the claimed homeomorphism `B_n x (0,1) -> P_n^+`.  The chamber itself
strongly deformation-retracts onto the middle section
`e=(E_n+c)/2` by linear interpolation in `e`.

For the attachment statement use

\[
 e_s=(1-s)e+sc,\qquad 0\le s\le1.
\]

For `s<1` this remains in the strict chamber, while at `s=1` it reaches
the coordinate trace.  Since `v(t,e_s)` increases with `s` and
`partial_v S_n^4>0`, the value of `S_n^4` is strictly larger for every
`s>0`; in particular it is positive all along the path.  At `s=1` the
coordinates and `S_n^4` extend continuously, and

\[
 S_n^4(e^{c+d},e^{c-d},1,e^{-2c})
 =S_n^3(e^{c+d},e^{c-d},e^{-2c})>0.
\]

Thus the endpoint lies inside `I_n^4`.  The formula fixes the trace
pointwise and gives the stated strong deformation retraction of the
augmented chamber.

## 5. The trace sectors at exponents 5 and 6

The V6.9 manuscript already proves that `B_4` is contractible.  Two small
new exact certificates give the same conclusion for `B_5` and `B_6`.

Let

\[
 F_n(t,u)=S_n^3(x,y,t^{-2}),
 \qquad xy=t^2,quad x+y=2t+u(t-1)^2.
\]

On `t>=T_n`, exact dyadic Bernstein subdivision proves

\[
 F_n(t,u)>0\quad\Longrightarrow\quad
 \partial_uF_n(t,u)\le0
\]

for `n=5,6`.  The `n=5` tree has 3 nodes (one exclusion leaf and one
derivative leaf).  The `n=6` tree has 19 nodes (four exclusion leaves and
six derivative leaves), with maximum axis depth 5.  Together with the
low-box exclusion in Lemma C, decreasing `u` from any violating point to
zero stays in the violation set.  Thus each trace sector strongly
deformation-retracts onto its symmetric slice.

On that slice, the continuous-exponent factorization already present in
V6.9 gives

\[
 F_n(t,0)=
 -\frac{(t^n-1)G_n(t)}
 {(t^{n+1}+1)(t^{2n+2}+1)},
\]

where

\[
 G_n(t)=t^{2n+2}(t-2)+t^{n+2}(t+1)+t^2-2.
\]

For `n=5`, the ascending coefficients of `G_5(1+s)/s` are

\[
 6,-4,-63,-170,-220,-97,141,298,275,154,54,11,1,
\]

and for `n=6` they are

\[
 6,-12,-133,-441,-819,-889,-385,439,1002,1001,
 637,273,77,13,1.
\]

Each list has exactly two sign changes.  Descartes' rule therefore gives
at most two roots with `s>0`.  Also `G_n'(1)=6>0`, `G_n(3/2)<0`, and
`G_n(2)>0`.  The middle inequality holds for every `n>=4`: if
`a=(3/2)^{n+2}`, then

\[
 G_n(3/2)=-\frac{2a^2}{9}+\frac{5a}{2}+\frac14<0,
\]

starting at `n=4` and increasingly strongly thereafter.  Hence `G_n` has
exactly two roots `1<a_n<b_n<2`, and the symmetric violation slice is the
single interval `(a_n,b_n)`.  It follows that `B_5` and `B_6` are
contractible.

Finally, in the strict `2+2` locus the choice of the two above-one
coordinates is constant along paths.  Within a fixed sign sector the two
below-one coordinates can never become equal: equality contradicts the
V6.9 spread-inversion theorem.  Their ordering is therefore also constant.
There are `binom(4,2)*2=12` ordered chambers.  The interval-bundle theorem
and contractibility of `B_4,B_5,B_6` show that these are exactly the 12
contractible components asserted in Theorem B.

## 6. Exact replay

From this directory run:

```powershell
node topology_four_exact.js
```

The script exits nonzero if any required Bernstein coefficient is negative,
if a strict threshold face fails, if an implication subdivision remains
unresolved, or if a node/depth budget is exhausted.  A successful run ends
with

```text
VERIFIED: ordered 2+2 fiber theorem for n=4,...,10; contractible trace sectors for n=5,6
```

Tested in the handoff workspace with Node.js 24.6.0.  The replay uses no
third-party package and makes no floating-point sign decision.

## 7. What remains open

This result does **not** classify the trace-sector topology for `n>=7`.
The exact off-axis bifurcation at exponent 7 shows why a naive
positive-pair symmetrization argument cannot be used there.  Theorem A does,
however, remove the extra four-variable fiber as a source of topology for
`7<=n<=10`: every component, loop, or attachment in an ordered transient
pocket comes directly from the corresponding three-variable sector.

No claim beyond exponent 10 is made here.  The finite exact thresholds were
chosen to obtain a short reproducible certificate, not as conjecturally
sharp constants.
