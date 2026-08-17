# Exact verification supplement

This archive supports the finite computer-assisted statements in Brandon Deonarine's manuscript *Geometry, Escape, and Phase Transitions in Violation Sets for the Generalized Damascus Inequality*.

## Reproduce all checks

Install the pinned dependencies and run the portable driver from this directory:

```text
python -m pip install -r requirements.txt
python damascus_verify_all.py
```

The driver verifies `MANIFEST.sha256`, performs the exact symbolic, continuous-exponent, and open-problem witness audits, replays the archived four-variable Bernstein trees using two separately implemented checkers, replays the topology certificate, recomputes every early staircase exhaustion using exact rational arithmetic, and verifies the manifest again. The manifest covers the immutable programs, certificates, dependency file, and metadata; it excludes itself and the transcript that records the manifest check.

The staircase program intentionally recomputes its exhaustive subdivision; there are no archived staircase JSON trees. It uses `fractions.Fraction` and exact SymPy rational polynomials for all sign decisions. Parallelism only distributes independent top-level boxes.

## Contents

- `bern_cert_n4.json`, `bern_cert_n5.json`, `bern_cert_n6.json`: archived four-variable terminal split paths and pruning labels.
- `topology_n4_cert.json`: archived topology subdivision certificate.
- `damascus_bernstein_*.py`: exact generator and two replay implementations.
- `damascus_staircase_verify.py`: deterministic exact exhaustive verifier for the finite lower staircase cells.
- `damascus_topology_verify.py`: topology certificate and Sturm-table verifier.
- `damascus_exact_audit.py`, `damascus_continuous_audit.py`: exact symbolic audits, including the continuous three-variable onset factorization and maximum-symmetry derivative identity.
- `damascus_open_problems_audit.py`: exact rational replay of the off-axis `n=7` bifurcation, the half-integer four-variable inclusion failure, and the domination margin plus collected complexity counts in the telescoping-pulse theorem.
- `verification-transcript.txt`: successful frozen run from the release package.
- `requirements.txt`, `MANIFEST.sha256`: pinned dependencies and release hashes.

No floating-point value is used to decide a certified sign. Numerical sweeps printed by the symbolic audit are ancillary sanity checks only.
