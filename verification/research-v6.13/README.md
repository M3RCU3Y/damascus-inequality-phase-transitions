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

- proof note: `REENTRY_R5_RESULT.md`
- exact rational witness: `reentry_r5_witness.py`
- matching upper-bound certificate: `reentry_r5_verify.py`

### Uniform three-variable topology

For every integer `n>=4`, the violation set `I_n^3` has exactly three
connected components, one for each choice of the coordinate below one. Each
component is simply connected and contractible. The off-axis tongues first
visible at exponent `7` remain attached and create no new component or hole.

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

### Full four-variable topology

The persistent `3+1` cores admit a continuous-exponent Morse/compactification
classification. There is a unique continuous birth at

\[
\nu_{31}=1.927014405732976\ldots,
\]

and no later interior zero-critical event. Boundary crossings are transverse
in the full compactified core and only open or close collars/ends.
Consequently

\[
I_1^4=\varnothing,
\]

and for every integer `n>=2`, the full four-variable violation set has exactly
four connected components, indexed by the persistent lone-below coordinate;
every component is contractible. For `n>=4`, the ordered `2+2` pockets retract
onto traces inside these four persistent components and add no homotopy.

- proof note: `TOPOLOGY_FOUR_FULL_RESULT.md`
- exact symbolic/Sturm audit: `full_four_topology_audit.py`

### High-exponent zero-width inclusion failure

For every sufficiently large real target exponent `mu`, there is
`delta_mu>0` such that

\[
I_{\mu-\varepsilon}^4\not\subseteq I_\mu^4
\qquad(0<\varepsilon<\delta_\mu).
\]

Thus the local forward-inclusion width is zero at high exponent. The earlier
`B sqrt(mu) 2^(-mu/2)` theorem remains an explicit construction, but its scale
and the constant `sqrt(6)` are not sharp phase-boundary data.

- proof note: `CONTINUOUS_ZERO_WIDTH_RESULT.md`
- high-precision sanity replay: `continuous_zero_width_check.py`

Run from this directory:

```bash
python reentry_kminus1_base.py
python reentry_r5_witness.py
python reentry_r5_verify.py
python topology_all_n_audit.py
python topology_four_all_n_audit.py
python full_four_topology_audit.py
python continuous_zero_width_check.py
```

## Current boundary

The unrestricted derivative-kernel argument fails at order six: the normalized
order-six Wronskian changes sign. Consequently the six-radius upper bound
requires additional structure, such as the product-one multiplicity
constraint, rather than a direct repetition of the order-five Chebyshev proof.

The remaining principal questions are the complete finite real-exponent
four-variable inclusion boundary and the sharp general upper bound/minimum
dimension for re-entry complexity.
