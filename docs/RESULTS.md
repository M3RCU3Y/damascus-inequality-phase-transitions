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
components, all contractible. The certificate combines exact Sturm sequences
with frozen integer Bernstein trees.

- proof note: `verification/research-v6.10/TOPOLOGY_N5_N6_RESULT.md`
- verifier: `verification/research-v6.10/topology_n56_certificate.py`
- certificates: `topology_n5_cert.json`, `topology_n6_cert.json`

### Strict four-variable $2+2$ pockets

For $n=4,5,6$, the strict $2+2$ locus has exactly twelve contractible
components. For $4\le n\le10$, each ordered strict pocket is an interval
bundle over its labelled three-variable trace sector.

- proof note: `verification/research-v6.10/TOPOLOGY_FOUR_PARTIAL_RESULT.md`
- exact audit: `verification/research-v6.10/topology_four_exact.js`

This does not classify components of the full four-variable violation set.
Coordinate-trace attachments remain a separate problem.

### Near-diagonal continuous failures

For each fixed $B>\sqrt 6$, sufficiently large $\mu$ admit an inclusion
failure across the gap $B\sqrt{\mu}\,2^{-\mu/2}$.

- proof note: `verification/research-v6.10/CONTINUOUS_NEAR_DIAGONAL_RESULT.md`
- numerical limit replay: `continuous_near_diagonal_failure.py`

The theorem is analytic; the decimal replay is only a high-precision check of
the displayed limiting behavior.

### Re-entry construction

For every $N\ge1$, at least $N$ membership changes can be realized with
exactly $N+2$ reciprocal radii in dimension $2N+3$.

- proof note: `verification/research-v6.10/REENTRY_NPLUS2_RESULT.md`
- exact bookkeeping audit: `verification/research-v6.10/reentry_nplus2_audit.js`

## Focused V6.13 result

### Exact five-radius re-entry complexity

For points using exactly five reciprocal radii, the sharp integer-exponent
membership-change count is

\[
R(5)=4.
\]

The lower bound is an exact rational witness. The upper bound is certified by
an order-five extended-Chebyshev argument for the radial derivative kernel,
with exact symbolic reduction, rational Bernstein bounds near the origin,
outward-rounded interval arithmetic on the compact middle range, and an
analytic exponential tail bound.

- proof note: `verification/research-v6.13/REENTRY_R5_RESULT.md`
- order-five verifier: `verification/research-v6.13/reentry_r5_verify.py`
- exact witness replay: `verification/research-v6.13/reentry_r5_witness.py`

The unrestricted order-six derivative kernel is not an ECT system, so the same
upper-bound mechanism does not automatically settle the six-radius case.

## Open questions

- topology of the three-variable off-axis tongues from exponent $7$ onward;
- extension of the four-variable interval-bundle certificate beyond exponent
  $10$ and attachment of its coordinate traces;
- the complete real-exponent four-variable inclusion region; and
- the sharp general upper bound and minimum dimension for re-entry complexity.
