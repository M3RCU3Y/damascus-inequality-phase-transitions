# Focused V6.13 research certificates

This directory contains later exact checks that are intentionally separated
from the immutable V6.9 supplement and the V6.10 research bundle.

## Verified results

### General one-radius adjunction

For every `k>=2`, the re-entry complexity satisfies

\[
R(k)\ge k-1.
\]

Equivalently, `N` integer-exponent membership changes can be realized with
exactly `N+1` reciprocal radii. The proof adds one new radius while preserving
any prescribed finite set of old signs and forcing one extra eventual sign
change.

- proof note: `REENTRY_KMINUS1_RESULT.md`
- exact two-radius base audit: `reentry_kminus1_base.py`

### Five reciprocal radii

The sharp integer-exponent re-entry complexity for five reciprocal radii is

\[
R(5)=4.
\]

Files:

- `REENTRY_R5_RESULT.md` — theorem statement and proof/certificate map;
- `reentry_r5_witness.py` — exact rational replay of a five-radius point with
  four membership changes;
- `reentry_r5_verify.py` — order-five radial Chebyshev certificate proving the
  matching upper bound.

### Uniform three-variable topology

For every integer `n>=4`, the violation set `I_n^3` has exactly three
connected components, one for each choice of the coordinate below one. Each
component is simply connected and hence contractible. In particular, the
off-axis tongues first visible at exponent `7` remain attached and create no
new component or hole.

- proof note: `TOPOLOGY_ALL_N_RESULT.md`
- exact algebra/combinatorics audit: `topology_all_n_audit.py`

### Uniform four-variable ordered pockets

For every integer `n>=4`, each ordered strict `2+2` pocket is an interval
bundle over its labelled three-variable trace sector. Adding its coordinate-1
trace gives a strong deformation retraction onto that trace. Consequently the
strict `2+2` locus has exactly twelve contractible components for every
integer exponent `n>=4`.

- proof note: `TOPOLOGY_FOUR_ALL_N_RESULT.md`
- exact finite/uniform audit: `topology_four_all_n_audit.py`

Run from this directory:

```bash
python reentry_kminus1_base.py
python reentry_r5_witness.py
python reentry_r5_verify.py
python topology_all_n_audit.py
python topology_four_all_n_audit.py
```

The exact witness scripts use `Fraction` arithmetic. The order-five upper
verifier derives the Wronskian polynomial symbolically, uses exact rational
Bernstein arithmetic near the origin, outward-rounded high-precision interval
bounds on the compact middle interval, and an analytic exponential tail bound.
The all-exponent pocket audit uses exact integer Bernstein arithmetic for the
finite low exponents and exact rational interval arithmetic for the uniform
Taylor remainder bound.

## Current boundary

The analogous unrestricted derivative-kernel argument fails at order six:
the normalized order-six Wronskian changes sign. Consequently the six-radius
upper bound requires additional structure, such as the product-one
multiplicity constraint, rather than a direct repetition of the order-five
Chebyshev proof.
