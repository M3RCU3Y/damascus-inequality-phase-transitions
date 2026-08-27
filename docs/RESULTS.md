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
across the gap $B\sqrt\mu\,2^{-\mu/2}$. The later zero-width theorem shows that
this scale and constant are not sharp phase-boundary data.

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

and no later interior zero-critical event. Compactified boundary crossings are
transverse in the full core and do not change its homotopy type. Combining
this with the ordered-pocket retractions gives

\[
\mathcal I_1^4=\varnothing,
\]

and, for every integer $n\ge2$, the full set $\mathcal I_n^4$ has exactly four
connected components, each contractible.

- proof note: `verification/research-v6.13/TOPOLOGY_FOUR_FULL_RESULT.md`
- symbolic/Sturm audit: `verification/research-v6.13/full_four_topology_audit.py`

### Exact five-radius re-entry complexity

For exactly five reciprocal radii,

\[
R(5)=4.
\]

- proof note: `verification/research-v6.13/REENTRY_R5_RESULT.md`
- upper-bound verifier: `verification/research-v6.13/reentry_r5_verify.py`
- exact witness: `verification/research-v6.13/reentry_r5_witness.py`

The unrestricted order-six derivative kernel is not an ECT system, so this
upper-bound mechanism does not automatically settle the six-radius case.

### High-exponent zero-width inclusion failure

For every sufficiently large real $\mu$, there is $\delta_\mu>0$ such that

\[
\mathcal I_{\mu-\varepsilon}^4\not\subseteq\mathcal I_\mu^4
\qquad(0<\varepsilon<\delta_\mu).
\]

Thus the local forward-inclusion width is zero at high exponent.

- proof note: `verification/research-v6.13/CONTINUOUS_ZERO_WIDTH_RESULT.md`
- sanity replay: `verification/research-v6.13/continuous_zero_width_check.py`

## Open questions

- the complete finite real-exponent four-variable inclusion region;
- the sharp general upper bound for re-entry complexity; and
- the sharp minimum-dimension/radius tradeoff for prescribed re-entry counts.
