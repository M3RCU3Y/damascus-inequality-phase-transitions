# Focused V6.13 research certificates

This directory contains later exact checks that are intentionally separated
from the immutable V6.9 supplement and the V6.10 research bundle.

## Verified result

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

Run from this directory:

```bash
python reentry_r5_witness.py
python reentry_r5_verify.py
```

The witness uses exact `Fraction` arithmetic. The upper verifier derives the
Wronskian polynomial symbolically, uses exact rational Bernstein arithmetic
near the origin, outward-rounded high-precision interval bounds on the compact
middle interval, and an analytic tail estimate.

## Current boundary

The analogous unrestricted derivative-kernel argument fails at order six:
the normalized order-six Wronskian changes sign. Consequently the six-radius
upper bound requires additional structure, such as the product-one
multiplicity constraint, rather than a direct repetition of the order-five
Chebyshev proof.
