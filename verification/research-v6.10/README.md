# Open-problem research ledger

This directory isolates new research from the verified manuscript and
its archived supplement.  A statement is not merged into the manuscript until its
status below is `proved` and its exact checks replay successfully.

## Status

| Target | Status | Result |
|---|---|---|
| Exact continuous onset of `I_nu^3` | proved | Every positive global maximum is symmetric.  Hence `I_nu^3` is nonempty exactly for `nu > nu_c`, where `nu_c=min_(1<t<2) log(p_+(t))/log(t)=3.98262315613834...` and `p_+` is explicit. |
| General fixed-exponent topology of `I_n^3` | open (proved through `n=6`) | Exact Sturm/Bernstein certificates extend the three-contractible-component theorem from `n=4` to `n=5,6`.  At `n=7` there are exact off-axis violation tongues: a symmetric fixed-product point is outside while an unequal point on the same slice is inside, so the remaining problem starts there. |
| Topology of four-variable transient `2+2` pockets | open in general (complete for `n=4,5,6`; reduced through `n=10`) | For `n=4,5,6`, the strict `2+2` locus has exactly 12 contractible components.  For every `4<=n<=10`, each ordered pocket is an interval bundle over its labelled three-variable trace sector and, after adjoining the coordinate-1 trace, strongly deformation-retracts onto it.  The `n>=7` trace-sector tongue topology and extension beyond `n=10` remain open. |
| Exact continuous four-variable inclusion region | open (new asymptotic theorem proved) | Exact failure established for `I_(15/2)^4 subset I_8^4`.  For every `nu > nu_c`, inclusion fails for all sufficiently large `mu`.  More sharply, for every `B > sqrt(6)`, `I_(mu-B sqrt(mu) 2^(-mu/2))^4` is not contained in `I_mu^4` for all sufficiently large `mu`.  The full finite boundary, the optimal near-diagonal scale, and the sharp constant remain open. |
| Optimal re-entry bound | open (construction improved) | An independently audited construction gives `N` changes with exactly `N+2` reciprocal radii in dimension `2N+3`; see `REENTRY_NPLUS2_RESULT.md`.  This improves both V6.9 construction counts by one.  Optimality and the universal upper bound remain open. |
| Arbitrarily many exponent-set membership changes | proved | A positive three-frequency `tanh` pulse, separated-scale alternating superposition, and discrete lifting argument give at least `N` changes for every `N >= 1`. |

## Exact replay

Run:

```powershell
python exact_new_results.py
```

The script uses Python's standard-library `fractions.Fraction` only.  It verifies:

1. the fixed-product `n=7` off-axis bifurcation by the exact symmetric two-root
   reduction; and
2. a four-variable half-integer exponent witness with
   `S_(15/2)>0>S_8`.

The arbitrary-change and telescoping-pulse theorems are analytic rather than
finite certificates; their complete proofs are given in the manuscript.  The
exact audit in the verification supplement checks the two rational witnesses,
the pulse domination margin, and the collected radius/dimension counts.

Exploratory floating-point scans are deliberately not part of the proof package.

## Focused continuous asymptotic replay

Run:

```powershell
python continuous_near_diagonal_failure.py
```

This standard-library `decimal` script evaluates the explicit `B=3`
near-diagonal witnesses at 100-digit precision and checks the two scaled limits
used in the new asymptotic theorem.  It is a numerical sanity check, not a
substitute for the written limit proof in the manuscript.  See
`CONTINUOUS_NEAR_DIAGONAL_RESULT.md` for the theorem and independent proof
audit.

## Exact topology replay at exponents 5 and 6

Run:

```powershell
python topology_n56_certificate.py
```

This standard-library-only script checks the displayed diagonal
factorizations, reconstructs the exact diagonal Sturm computations and the
cleared bivariate polynomials, and replays the two frozen integer Bernstein
proof trees.  See `TOPOLOGY_N5_N6_RESULT.md` for the complete statement, proof
summary, and certificate sizes.

## Exact four-variable pocket replay

Run:

```powershell
node topology_four_exact.js
```

This dependency-free `BigInt` audit reconstructs the symmetric pair formulas
for `n=4,...,10`, checks the exact low-box exclusion and tail-monotonicity
Bernstein coefficients, and replays the two conditional trace-sector trees at
`n=5,6`.  See `TOPOLOGY_FOUR_PARTIAL_RESULT.md` for the theorem, proof, exact
coefficient counts, and the limitation at exponent `7` and beyond.

## Exact improved re-entry bookkeeping

Run:

```powershell
node reentry_nplus2_audit.js
```

This dependency-free audit checks the exact rational pulse margins and, for
representative values `N=1,...,20`, the symbolic coefficient sum, zero first
moment, radius count `N+2`, and dimension `2N+3`.  Its additional
floating-point samples are sanity checks only; the sign and tail proof in
`REENTRY_NPLUS2_RESULT.md` is analytic.
