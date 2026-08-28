# Result and certificate map

This file records what the repository verifies and what remains open. It is a
guide to the code, not a substitute for the written proofs.

## Immutable V6.9 verification release

| Topic | Verification entry point |
|---|---|
| Exact rational witnesses and symbolic identities | `verification/release-v6.9/damascus_exact_audit.py` |
| Continuous-exponent identities and onset algebra | `verification/release-v6.9/damascus_continuous_audit.py` |
| Off-axis and half-integer witnesses | `verification/release-v6.9/damascus_open_problems_audit.py` |
| Four-variable finite Bernstein certificates | `verification/release-v6.9/damascus_bernstein_verify.py` |
| Independent Bernstein implementation | `verification/release-v6.9/damascus_bernstein_verify_independent.py` |
| Exponent-$4$ topology certificate | `verification/release-v6.9/damascus_topology_verify.py` |
| Exhaustive lower staircase cells | `verification/release-v6.9/damascus_staircase_verify.py` |

The SHA-256 manifest in that directory covers the release files and is checked
before and after the full legacy run.

## Focused V6.10 results

### Fixed-exponent topology at $n=5,6$

Each of $\mathcal I_5^3$ and $\mathcal I_6^3$ has exactly three connected
components, all contractible. The later V6.13 theorem makes this uniform for
all integer $n\ge4$.

### Strict four-variable $2+2$ pockets

The V6.10 certificate proves twelve contractible strict pockets through the
first exponents and an interval-bundle reduction through $n=10$. The later
V6.13 theorem removes both finite cutoffs.

### Near-diagonal continuous failures

For each fixed $B>\sqrt6$, sufficiently large $\mu$ admit an inclusion failure
across the gap $B\sqrt\mu\,2^{-\mu/2}$. The later V6.14 finite-threshold and
right-half-plane theorems supersede the qualitative high-exponent cutoff.

### Re-entry construction

The V6.10 construction realizes $N$ changes with $N+2$ reciprocal radii. The
later V6.13 adjunction improves this to $N+1$ radii.

## Focused V6.13 results

### General one-radius re-entry adjunction

For every $k\ge2$,

\[
R(k)\ge k-1.
\]

Equivalently, $N$ integer-exponent membership changes can be realized with
exactly $N+1$ reciprocal radii.

- proof note: `verification/research-v6.13/REENTRY_KMINUS1_RESULT.md`
- exact base audit: `verification/research-v6.13/reentry_kminus1_base.py`

### Uniform three-variable topology

For every integer $n\ge4$, $\mathcal I_n^3$ has exactly three connected,
contractible components. The exponent-$7$ off-axis tongues remain attached and
create neither new components nor holes.

- proof note: `verification/research-v6.13/TOPOLOGY_ALL_N_RESULT.md`
- audit: `verification/research-v6.13/topology_all_n_audit.py`

### Uniform four-variable ordered pockets

For every integer $n\ge4$, each ordered strict $2+2$ pocket is homeomorphic to
its labelled three-variable trace sector times an open interval. Adding the
coordinate-$1$ trace gives a strong deformation retraction onto that trace.
Thus the strict $2+2$ locus has exactly twelve contractible components for
every $n\ge4$.

- proof note: `verification/research-v6.13/TOPOLOGY_FOUR_ALL_N_RESULT.md`
- audit: `verification/research-v6.13/topology_four_all_n_audit.py`

### Full four-variable topology

The persistent strict $3+1$ core has a unique continuous birth at

\[
\nu_{31}=1.927014405732976\ldots
\]

and no later interior zero-critical event. Combining the persistent-core
continuation with the ordered-pocket retractions gives

\[
\mathcal I_1^4=\varnothing,
\]

and, for every integer $n\ge2$, the full set $\mathcal I_n^4$ has exactly four
connected components, each contractible.

- proof note: `verification/research-v6.13/TOPOLOGY_FOUR_FULL_RESULT.md`
- symbolic/Sturm audit: `verification/research-v6.13/full_four_topology_audit.py`
- explicit boundary-positive continuation lemma:
  `verification/research-v6.14/TOPOLOGY_CONTINUATION_LEMMA.md`

### High-exponent zero-width inclusion failure

V6.13 proved zero local forward-inclusion width for every sufficiently large
real target exponent. The V6.14 fixed-slice theorem replaces this with an
explicit finite threshold and is therefore the current stronger statement.

- proof note: `verification/research-v6.13/CONTINUOUS_ZERO_WIDTH_RESULT.md`
- sanity replay: `verification/research-v6.13/continuous_zero_width_check.py`

## Focused V6.14 results

### Exact low-radius re-entry law

The missing lower-order Wronskian dependencies in the five-radius argument
have been independently certified. Together with the V6.13 lower construction,

\[
\boxed{R(k)=k-1\qquad(2\le k\le5).}
\]

- proof note: `verification/research-v6.14/REENTRY_LOW_RADIUS_EXACT_RESULT.md`
- verifier: `verification/research-v6.14/reentry_low_order_verify.py`
- order-five proof/witness remain in `verification/research-v6.13/`

The unrestricted order-six normalized Wronskian changes sign, so the same ECT
mechanism does not by itself settle $R(6)$.

### Exponent-ratio monotonicity

For $0<\nu<\mu$,

\[
R_{\nu,\mu}(t)=\frac{\phi_\mu(t)}{\phi_\nu(t)}
\]

is reciprocal-invariant and strictly decreasing for $t>1$, with limits
$\mu/\nu$ at $1+$ and $1$ at infinity. This converts a $2+2$ source-boundary
comparison into an equal-mass weighted-average problem with one decreasing
radial multiplier.

- proof note: `verification/research-v6.14/CONTINUOUS_RATIO_MONOTONICITY_RESULT.md`

### Single-transient theorem for strict $2+2$ histories

Every strict four-variable $2+2$ point has at most two positive real-exponent
zeros. Hence on exponents at least one its violation set is empty or one
bounded open interval. The continuous inclusion problem is therefore an
envelope of single transient intervals rather than a multiple-re-entry
problem.

- proof note: `verification/research-v6.14/FOUR_VARIABLE_SINGLE_TRANSIENT_RESULT.md`

### Exact continuous onset of the strict $2+2$ locus

Let

\[
\nu_c=3.9826231561383400589\ldots
\]

be the exact three-variable onset. Then

\[
\mathcal I_{\nu,2+2}^4\ne\varnothing
\quad\Longleftrightarrow\quad
\nu>\nu_c.
\]

Consequently the complete four-variable inclusion region contains the exact
left half-plane

\[
\boxed{
0<\nu\le\nu_c,\quad\mu>\nu
\Longrightarrow
\mathcal I_\nu^4\subseteq\mathcal I_\mu^4.}
\]

- proof note: `verification/research-v6.14/CONTINUOUS_FOUR_ONSET_RESULT.md`
- algebra audit: `verification/research-v6.14/continuous_four_onset_audit.py`

### Certified symmetric fold

Inside the equal-above strict $2+2$ family there is a unique stationary fold in
a radius-$10^{-20}$ box around

\[
\nu_\dagger=7.3596318961093494297131900223\ldots.
\]

The interval Krawczyk certificate proves that the exponent double root and the
geometric stationary point are nondegenerate. The local stationary-envelope
slope is

\[
\mu_{\rm sym}'(\nu_\dagger^-)=-1.
\]

- proof note: `verification/research-v6.14/SYMMETRIC_FOLD_RESULT.md`
- verifier: `verification/research-v6.14/symmetric_fold_certificate.py`

This is a local symmetric-family theorem; global equal-above extremality is
still the remaining step needed to identify the fold itself as the exact
sharp inclusion-collapse point.

### Large-target end of the stationary symmetric envelope

The stationary symmetric branch approaches the exact three-variable onset and
satisfies

\[
\mu(\nu-\nu_c)\longrightarrow
11.84876850437540567\ldots.
\]

The onset point and the asymptotic constant are interval-certified.

- proof note: `verification/research-v6.14/SYMMETRIC_ENVELOPE_ASYMPTOTIC_RESULT.md`
- verifier: `verification/research-v6.14/symmetric_envelope_asymptotic.py`

### Explicit finite zero-width threshold

Using one fixed rational geometric slice, every target

\[
\mu\ge7.3596319
\]

has zero local forward-inclusion width. The compact range is validated by
outward-rounded interval arithmetic and the infinite tail by explicit analytic
bounds.

- proof note: `verification/research-v6.14/FIXED_SLICE_ZERO_WIDTH_RESULT.md`
- verifier: `verification/research-v6.14/fixed_slice_zero_width_certificate.py`

The rational threshold lies only about $3.89\times10^{-9}$ above the
independently certified symmetric fold.

### Full right-half-plane noninclusion

The same fixed-slice target-boundary witnesses can be transported back to the
fixed source exponent $7.3596319$. A validated monotone root tube proves that
for every

\[
\boxed{7.3596319\le\nu<\mu}
\]

one has

\[
\boxed{\mathcal I_\nu^4\not\subseteq\mathcal I_\mu^4.}
\]

Thus the complete continuous inclusion problem is rigorously confined to the
finite source strip

\[
\boxed{
3.9826231561383400589\ldots<\nu<7.3596319.}
\]

- proof note: `verification/research-v6.14/RIGHT_HALFPLANE_NONINCLUSION_RESULT.md`
- verifier: `verification/research-v6.14/right_halfplane_certificate.py`

## Current open questions

1. Prove the global equal-above extremality theorem in the finite strip
   $\nu_c<\nu<7.3596319$, thereby identifying the complete finite
   real-exponent four-variable inclusion boundary and deciding whether the
   certified symmetric fold is the exact sharp collapse threshold.
2. Determine $R(k)$ for $k\ge6$. In particular, decide whether the exact law
   $R(k)=k-1$ continues after the unrestricted order-six ECT failure.
3. Determine the sharp minimum-dimension/radius tradeoff for prescribed
   re-entry counts.
