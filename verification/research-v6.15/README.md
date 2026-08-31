# Research V6.15: continuous middle-strip KKT frontier

V6.15 is the focused research layer for the remaining continuous four-variable inclusion problem.

## The only live continuous target

The V6.14 theorem layer already proves the two outer source regions.  The unresolved strip is

\[
\nu_c<\nu<\nu_\dagger.
\]

The symmetric equal-above envelope is locally certified at both ends, but global equal-above extremality is not yet a theorem.

## Primary proof kernel

For a four-distinct KKT stationary point in log coordinates, use

\[
f(x)=H_\mu(x)-\lambda H_\nu(x)-\gamma,
\qquad H_\alpha(x)=h_\alpha(e^x),
\]

with four ordered simple roots `x1<x2<x3<x4`.

The current target is to prove one of the equivalent saddle interfaces:

- the explicit feasible second variation `Q_123<0`; or
- the root-map / restricted-Hessian orientation invariant `Delta<0`.

The exact reduction identities are documented in:

- `KKT_ORIENTATION_REDUCTION.md`

and audited by:

- `kkt_orientation_identity_check.py`

The audit verifies algebraic identities only. It does **not** certify either conjectural sign.

## Root-packet abstraction

A four-root packet consists of:

1. parameters `(nu,mu,lambda,gamma)`;
2. ordered certified roots `(x1,x2,x3,x4)` of `f`;
3. alternating certified slope signs;
4. aggregate constraints
   \[
   P=\sum x_i,\quad A=\sum\Phi_\nu(x_i),\quad B=\sum\Phi_\mu(x_i);
   \]
5. diagnostics `Q_123` and `Delta`.

The stationary KKT manifold is generically the one-dimensional set

\[
P=A=B=0
\]

in `(nu,mu,lambda,gamma)` after the roots are treated implicitly. Any global sign certificate should operate on this manifold, not on the raw five-dimensional geometry box.

## Research order

1. Seek an analytic orientation theorem for `Delta` or `dD_123[v]`.
2. In parallel, test the collective root-centroid shortcut `sum x_i<0`; do not revive false pairwise reciprocal-root claims.
3. If the analytic sign does not collapse cleanly, build a validated one-dimensional interval continuation of the KKT root manifold and certify `Delta<0` there.
4. Treat root collisions and geometry boundaries separately.
5. Use the existing full-fold nondegeneracy theorem at the equal-above collision boundary.

## Proof-status discipline

Every V6.15 artifact must label itself as one of:

- `IDENTITY`: exact algebraic/logical reduction;
- `CERTIFIED-LOCAL`: rigorous statement on a validated local box/branch;
- `CERTIFIED-GLOBAL`: rigorous statement covering the full stated domain;
- `NUMERICAL`: exploratory evidence only;
- `CONJECTURE`: unproved target.

A numerical scan may guide subdivision or theorem discovery, but may never silently become a theorem statement.

## Known dead ends

Do not restart these without a genuinely new hypothesis:

- strong fixed-fiber pointwise symmetrization;
- raw-box pointwise two-kernel total positivity;
- global one-variable dual-potential positivity;
- arbitrary four-node Chebyshev orientation without product-one geometry;
- pairwise reciprocal-root inequalities strong enough to force the desired product relation.

## Completion criterion

The continuous middle strip is closed only after a rigorous global argument excludes all nonsymmetric stationary competitors and all relevant boundary alternatives, leaving the equal-above stationary envelope as the global extremal boundary.

Until then, do not claim the exact middle-strip inclusion boundary or global equal-above extremality.
