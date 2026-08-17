# Reproducibility

## Trust model

The finite certificates use exact integer or rational arithmetic for every
certified sign decision.

- Bernstein range bounds are consequences of the convex-hull property.
- Dyadic subdivisions use exact de Casteljau arithmetic.
- Archived proof trees are replayed rather than rediscovered.
- A second Bernstein implementation independently reconstructs the relevant
  polynomials and subdivisions.
- Sturm calculations and polynomial identities are checked symbolically.

Numerical output is used only where a file explicitly describes it as a sanity
check.

## Environments

The immutable V6.9 release pins:

```text
sympy==1.14.0
numpy==2.3.5
mpmath==1.3.0
```

The focused V6.10 Python verifiers use the standard library. The two JavaScript
audits require Node.js and use `BigInt` for certified arithmetic.

## Commands

From the repository root:

```bash
python -m pip install -r verification/release-v6.9/requirements.txt
python verify.py --quick
python verify.py --full
```

The quick run omits only the exhaustive lower-cell staircase. The full run
recomputes that subdivision and then executes every focused V6.10 audit.

## Release integrity

`verification/release-v6.9` is an immutable copy of the packaged verification
supplement. Its internal `MANIFEST.sha256` deliberately excludes itself and
the frozen transcript. Do not edit files in this directory without creating a
new release and a new manifest.
