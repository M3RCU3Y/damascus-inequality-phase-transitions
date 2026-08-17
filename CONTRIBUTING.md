# Contributing

Contributions that improve reproducibility, portability, or the clarity of an
exact certificate are welcome.

## Standards

1. Keep theorem statements, computer-assisted proofs, conjectures, and
   numerical evidence clearly separated.
2. Do not use floating-point values to certify a sign.
3. Prefer small replayable certificates to opaque search output.
4. Add an independent implementation when a finite certificate carries a
   substantial part of a proof.
5. Preserve the immutable V6.9 directory. New work belongs in a new release or
   research directory.

Run `python verify.py --quick` before opening a pull request. Changes to a
certificate, verifier, or pinned dependency should also pass
`python verify.py --full`.

Please include the mathematical claim affected, the exact arithmetic used, and
the expected replay output in the pull-request description.
