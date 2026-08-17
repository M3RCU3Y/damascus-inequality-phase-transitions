# Exact topology at exponents 5 and 6

## Status

**Proved, computer-assisted, independently audited, and merged into the V6.10
research draft.**  This note records a partial resolution of Open Problem 1;
the certificates have not yet been folded into an immutable supplement release.

## Theorem

For each `n in {5,6}`, the three-variable violation set `I_n^3` has exactly
three connected components, one for each choice of the coordinate below `1`.
Every component is contractible.  More precisely, in the sector `x,y>1>z`,
each fixed-product cross-section is an interval in logarithmic pair-spread,
and the sector strongly deformation-retracts onto the symmetric slice `x=y`.

Together with the manuscript's theorem at `n=4`, this classifies the topology
for every exponent before the first off-axis bifurcation at `n=7`.

## Proof

Fix `n in {5,6}` and the sector `x,y>1>z`.  As in the proof already given for
`n=4`, write

```
xy=t^2,
x+y=2t+u(t-1)^2,
t>1, 0<=u<1.
```

The endpoint `u=0` is the symmetric point `x=y=t`; as `u` tends to `1`, one
of `x,y` tends to `1`.  Put `z=t^(-2)`, and denote the resulting rational
function by `S_n(t,u)`.

### 1. The symmetric slice is one interval

At `u=0`, direct exact simplification gives

```
S_5(t,0) = -(t-1)^2 (t^4+t^3+t^2+t+1) P_5(t)
           / ((t^6+1)(t^12+1)),

P_5(t) = t^12-t^11-t^10-t^9-t^8+t^6+t^5+t^4+t^3+t^2+2t+2,
```

and

```
S_6(t,0) = -(t-1)^2 (t+1)(t^2+1)(t^2-t+1)(t^2+t+1)^2 P_6(t)
           / ((t^7+1)(t^14+1)),

P_6(t) = t^10-2t^9-t^8+3t^7-t^6-3t^5+3t^4+2t^3-3t^2+2.
```

Every displayed factor outside `P_n` is positive for `t>1`.  Exact Sturm
sequences for `P_5` and `P_6` have sign-variation counts

```
             t=1   t=3/2   t=2   t=+infinity
P_5            7      6       5        5
P_6            6      5       4        4.
```

The exact sample values are

```
P_5(1)=6,       P_5(3/2)=-179473/4096,   P_5(2)=386,
P_6(1)=1,       P_6(3/2)=-10831/1024,    P_6(2)=22.
```

Thus each `P_n` has exactly two roots `a_n,b_n` in `(1,2)`, one in
`(1,3/2)` and one in `(3/2,2)`, and no further root above `2`.  Consequently
`S_n(t,0)>0` exactly on the single interval `(a_n,b_n)`.

### 2. Every nonnegative fixed-product section is transversely decreasing

Let `F_n(t,u)` be the integer polynomial obtained from the cleared numerator
so that

```
S_n(t,u)>0  iff  F_n(t,u)<0,
```

and let `H_n(t,u)` be the integer polynomial obtained from the cleared
`u`-derivative so that

```
partial_u S_n(t,u)<0  iff  H_n(t,u)>0.
```

For both exponents, `deg(F_n)=(22,6)` and `deg(H_n)=(22,10)` in `(t,u)`.
Compactify `t=(1+s)/(1-s)`, with `0<=s<=1`.  Exact bivariate Bernstein
subdivision proves

```
F_n(t,u)<=0  ==>  H_n(t,u)>0
```

throughout `t>1, 0<=u<1`.  The frozen proof trees have:

```
n=5: 11 nodes, 6 leaves (4 excluded by F_5>0; 2 certified by H_5>0),
n=6: 23 nodes, 12 leaves (7 excluded by F_6>0; 5 certified by H_6>0).
```

All coefficients, compactification steps, Bernstein transforms, and midpoint
subdivisions are exact integers.  Hence, whenever a section is nonnegative,
increasing `u` strictly decreases `S_n`.

It follows that a positive section can exist only when its symmetric point is
positive, hence only for `a_n<t<b_n`.  At `u=0` it is positive, while at
`u=1` the limiting pair has one coordinate equal to `1`; the other two form a
reciprocal pair and give a strictly negative value.  The certified derivative
condition prevents a second crossing.  Thus there is a unique continuous
threshold `U_n(t) in (0,1)` with

```
S_n(t,u)>0  iff  0<=u<U_n(t).
```

### 3. Deformation retraction and components

Write

```
x=t exp(delta), y=t exp(-delta), z=t^(-2).
```

Then

```
u(t,delta)=2t(cosh(delta)-1)/(t-1)^2.
```

The homotopy

```
H_s(t,delta)=(t exp((1-s)delta), t exp(-(1-s)delta), t^(-2))
```

monotonically decreases `u` and therefore stays within `u<U_n(t)`.  It fixes
the symmetric slice pointwise and is a strong deformation retraction onto
the interval `a_n<t<b_n`.  Hence the sector is contractible.

The settled sign-pattern theorem says every three-variable violation has
exactly one coordinate below `1`, and no coordinate can equal `1`.  Its
identity is constant along a path.  The three nonempty contractible sectors
are therefore exactly the three connected components.  This proves the
theorem.

## Exact replay

From `Paper 2 - Phase Transitions`, run:

```powershell
python research-open-problems/topology_n56_certificate.py
```

The script uses only the Python standard library.  It independently checks
the displayed diagonal factorizations, reconstructs `F_n,H_n` by sparse exact
polynomial arithmetic, checks the exact Sturm tables and sample values, reads
the two frozen JSON trees, and replays every Bernstein leaf.  The successful
transcript is:

```
n=5 STURM VERIFIED: variations [7, 6, 5, 5]; samples [6, -179473/4096, 386]
n=5 BERNSTEIN TREE VERIFIED: {'nodes': 11, 'leaves': 6, 'F': 4, 'H': 2, 'max_depth': 5}
n=6 STURM VERIFIED: variations [6, 5, 4, 4]; samples [1, -10831/1024, 22]
n=6 BERNSTEIN TREE VERIFIED: {'nodes': 23, 'leaves': 12, 'F': 7, 'H': 5, 'max_depth': 9}
N=5,6 FIXED-EXPONENT TOPOLOGY CERTIFICATES PASSED
```

Files:

- `topology_n56_certificate.py`
- `topology_n5_cert.json`
- `topology_n6_cert.json`

The committed JSON certificates are replay-only data.  Passing
`--generate` deliberately regenerates and overwrites them and is not needed
for verification.

## Precise suggested manuscript insertion

In the subsection **A fixed-exponent topology theorem**, replace

> At the first nonempty three-variable exponent one can also determine the
> exact component topology.

with

> At the first three nonempty integer exponents one can determine the exact
> component topology.  The proof at exponent `4` was found first; the same
> deformation mechanism remains valid at exponents `5` and `6`, immediately
> before the off-axis bifurcation at exponent `7`.

After the proof of the existing theorem `Topology of I_4^3` and before the
paragraph beginning *The fixed-product monotonicity in the preceding proof...*,
insert the theorem above, abbreviating Steps 2 and 3 by explicit reference to
the definitions and homotopy in the `n=4` proof.  A concise manuscript version
can state the two displayed diagonal factorizations, the Sturm table, and the
Bernstein-tree sizes; the homotopy need not be rederived.

Then change the opening sentence of the next paragraph to:

> The fixed-product monotonicity in the preceding proofs holds through
> exponent `6`, but is not a formal consequence of three-variable nestedness.
> In fact, a new transverse phenomenon occurs at exponent `7`.

Finally update the Open Problems bullet from *beyond I_4^3* to *from exponent
7 onward*.

## Remaining obstruction

This is a strict partial result, not a full solution for all exponents.  The
exact `n=7` witness already in the manuscript proves that the fixed-product
symmetrization implication fails there, so the present certificate strategy
cannot be extended verbatim.  Dense exploratory grids (not part of the proof)
continue to show a single hole-free region per sign sector for tested
exponents through `n=200`; proving attachment of the off-axis tongues, or
finding a counterexample, requires a different global mechanism.
