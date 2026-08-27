# Damascus Inequality: Phase Transitions

[![Exact verification](https://github.com/M3RCU3Y/damascus-inequality-phase-transitions/actions/workflows/verify.yml/badge.svg)](https://github.com/M3RCU3Y/damascus-inequality-phase-transitions/actions/workflows/verify.yml)

Exact verification code, finite certificates, and reproducibility notes for
*Geometry, Escape, and Phase Transitions in Violation Sets for the Generalized
Damascus Inequality*.

The repository is organized around auditable arithmetic. Certified sign
decisions use rational or integer computation; floating-point evaluations are
identified as sanity checks and are not substituted for proofs.

The manuscript source and paper PDF are intentionally not included at this
stage.

## Verified results represented here

- the finite lower-cell checks in the minimum-dimension nesting staircase;
- the four-variable Bernstein certificates through the sharp one-step
  threshold;
- three-variable fixed-exponent topology for every integer exponent $n\ge4$;
- the strict four-variable $2+2$ pocket classification and ordered
  interval-bundle reduction for every integer exponent $n\ge4$;
- exact rational witnesses for off-axis and noninteger inclusion failures;
- the high-exponent near-diagonal failure construction;
- the improved general re-entry construction $R(k)\ge k-1$; and
- the exact five-radius re-entry result $R(5)=4$.

The scope and status of each item are summarized in
[docs/RESULTS.md](docs/RESULTS.md).

## Repository layout

```text
verification/
  release-v6.9/       immutable verification supplement
  research-v6.10/     focused follow-up certificates
  research-v6.13/     later uniform topology and re-entry results
docs/
  RESULTS.md
  REPRODUCIBILITY.md
verify.py             cross-platform verification runner
```

The V6.9 directory is retained byte-for-byte so that its SHA-256 manifest
continues to verify. Later results are separated rather than silently changing
that release.

## Quick start

Python 3.12 and Node.js are recommended.

```bash
python -m pip install -r verification/release-v6.9/requirements.txt
python verify.py --quick
```

The complete verification, including the exhaustive staircase subdivision,
is:

```bash
python verify.py --full
```

On a typical four-core machine the exhaustive part takes a few minutes.
GitHub Actions runs the full command on every push and pull request.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff). The research
article should be cited separately once its bibliographic record is available.

## License

Repository-level code is released under the MIT License. The immutable V6.9
supplement retains the CC BY 4.0 license metadata recorded in its own
`CITATION.cff`.
