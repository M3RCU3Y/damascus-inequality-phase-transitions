# Agent research operating system

This document is the control plane for continuing the Damascus phase-transition project efficiently and safely across research threads.

It is intentionally different from `RESULTS.md`:

- `RESULTS.md` answers **what is rigorously known?**
- this file answers **how should an agent reason, navigate, certify, and hand off the next step?**

The repository remains the home of proof notes, exact/certified code, witnesses, and reproducibility material. Do not commit manuscript source or compiled paper PDFs here.

## 1. North-star objective

Complete exact structural understanding of the generalized Damascus violation sets while keeping every promoted theorem reproducible and sharply separated from numerical reconnaissance.

For the current continuous four-variable frontier, the concrete objective is:

> prove or disprove global equal-above extremality in the finite middle source strip and thereby determine the exact inclusion boundary.

Do not dilute the active proof effort by reopening already-settled outer ranges unless a new argument directly simplifies the middle-strip proof.

## 2. The abstraction tower

Work from the lowest reusable layer upward. Never make a higher layer depend on hidden algebra that has not been captured below it.

### Layer 0: scalar kernel

Canonical functions and exact identities:

\[
\phi_\alpha(t),\quad \Phi_\alpha(x)=\phi_\alpha(e^x),\quad
H_\alpha(x)=\Phi_\alpha'(x)=h_\alpha(e^x).
\]

This layer owns reciprocity, derivative formulas, monotonicity lemmas, and exact scalar bounds.

### Layer 1: KKT line kernel

For fixed parameters:

\[
f(x)=H_\mu(x)-\lambda H_\nu(x)-\gamma.
\]

This layer owns root equations, root reflection, slope signs, and parameter sensitivities.

### Layer 2: root packet

A root packet is the atomic state object for a four-distinct stationary candidate:

```text
(nu, mu, lambda, gamma)
ordered roots x1 < x2 < x3 < x4
root brackets / uniqueness proof
slope signs f'(xi)
Hi = H_nu(xi)
```

A numerical root list without brackets and branch identity is reconnaissance, not a certified packet.

### Layer 3: aggregate invariants

Every root packet exposes the same small API:

\[
P=\sum_i x_i,
\qquad
A=\sum_i\Phi_\nu(x_i),
\qquad
B=\sum_i\Phi_\mu(x_i),
\]

plus

\[
Q_{123},\qquad\Delta.
\]

This is the level at which the current saddle theorem should be attacked.

### Layer 4: constrained root manifold

The four-distinct stationary boundary manifold is

\[
\mathcal K=\{P=A=B=0\}
\]

inside `(nu,mu,lambda,gamma)` after roots are implicit.

The key engineering principle is:

> certify on the smallest mathematically valid manifold, never on a convenient but vastly larger ambient box.

### Layer 5: global branch geometry

This layer owns continuation, endpoints, collisions, trace limits, the equal-above boundary, and exclusion of competing components.

### Layer 6: phase diagram theorem

Only after all interior and boundary alternatives are closed may a global inclusion/exclusion statement be promoted into the manuscript-level theorem inventory.

## 3. Proof-status lattice

Every research artifact must explicitly belong to one of these statuses:

| Status | Meaning | May support a theorem? |
|---|---|---|
| `IDENTITY` | Exact algebraic/logical reduction | Yes, as a lemma/reduction |
| `CERTIFIED-LOCAL` | Rigorous validated statement on a stated local box/branch | Only within that domain |
| `CERTIFIED-GLOBAL` | Rigorous coverage of the entire stated domain | Yes |
| `NUMERICAL` | Floating-point reconnaissance / stress test | No |
| `CONJECTURE` | Unproved target | No |
| `DISPROVED` | Explicit counterexample or rigorous contradiction | Used to block dead routes |

Never use prose such as “verified”, “proved numerically”, or “essentially established” for a `NUMERICAL` artifact.

## 4. Active continuous frontier

The theorem layer has already reduced the real-exponent four-variable problem to

\[
\nu_c<\nu<\nu_\dagger.
\]

The current proof kernel is the four-root KKT saddle problem. Read in this order:

1. `verification/research-v6.15/README.md`
2. `verification/research-v6.15/KKT_ORIENTATION_REDUCTION.md`
3. `verification/research-v6.14/ROOT_REFLECTION_SINGLE_CROSSING_RESULT.md`
4. `verification/research-v6.14/FULL_FOLD_TRANSVERSE_RESULT.md`
5. relevant V6.14 fold/envelope notes only as needed

The immediate theorem target is one of

\[
Q_{123}<0
\qquad\text{or}\qquad
\Delta<0
\]

on every admissible four-distinct packet in `K`.

## 5. Decision tree for the KKT proof

### Route A: analytic orientation

Try first because it has the highest theorem-to-resource ratio.

Use the exact identity

\[
\mathrm dD_{123}[v]=-Q_{123}
\]

and the planar curve

\[
x\mapsto(H_\nu(x),H_\mu(x)).
\]

Look for a turning/orientation theorem that requires only conditions already forced by a valid root packet.

Success criterion: a short global sign proof with assumptions exactly matching the KKT manifold.

### Route B: collective root reflection / centroid

The log-normalized reciprocity gives a promising collective shortcut. A theorem

\[
\sum_i x_i<0
\]

for every admissible four-root packet would exclude product-one stationary packets before any Hessian analysis.

Do not replace this collective target by already-failed pairwise reciprocal inequalities.

### Route C: certified one-dimensional continuation

If Routes A/B do not collapse cleanly, build the certificate directly on `K`.

Minimum desired packet operations:

```text
bracket_roots(params)
validate_root_packet(params, brackets)
evaluate_aggregates(packet) -> P,A,B
evaluate_orientation(packet) -> Delta,Q123
continue_K(seed_packet)
certify_sign_on_segment(segment, invariant)
classify_endpoint(endpoint)
```

Preferred validation stack:

- interval Newton / Krawczyk for root uniqueness and manifold continuation;
- outward-rounded interval evaluation for invariants;
- adaptive subdivision based on the actual sign margin and conditioning;
- analytic endpoint asymptotics where interval conditioning deteriorates.

### Route D: boundary closure

Treat boundaries as separate mathematical objects instead of forcing one giant certificate to swallow degeneracies.

Important interfaces include:

- upper-root collision / equal-above boundary;
- lower-repeat alternatives;
- coordinate-1 trace;
- source and target endpoint limits;
- any root escaping or multiplier-range boundary.

A four-distinct branch approaching equal-above must satisfy the collision condition `f=f'=0`; combine that with the existing full-fold nondegeneracy theorem rather than recertifying the fold from scratch.

## 6. Resource budget policy

Spend computation in this order:

1. symbolic reduction;
2. exact structural lemmas;
3. low-dimensional floating reconnaissance;
4. interval continuation on the true constrained manifold;
5. compact-domain subdivision;
6. only as a last resort, high-dimensional ambient certification.

A certificate that can be replaced by a monotonicity lemma should be replaced. A five-dimensional sign box that can be reduced to a one-dimensional root manifold should never be the default implementation.

## 7. Numerical reconnaissance contract

Numerics are scouts, not judges.

Good uses:

- locate branches and folds;
- estimate sign margins;
- discover rescalings and monotone quantities;
- identify conditioning failures;
- choose interval charts and subdivision priorities;
- search aggressively for counterexamples.

Required output from any serious reconnaissance script:

```text
parameter ranges
sampling / continuation method
number of valid packets
minimum and maximum invariant values
closest-to-zero packet
worst conditioning packet
any rejected/ambiguous cases
seed values sufficient for reproduction
```

If a scan finds a sign margin, immediately ask whether the same coordinate system makes interval certification cheap.

## 8. Counterexample-first discipline

Before investing in a global inequality:

1. test it on unconstrained raw points;
2. test it on KKT roots without product/source constraints;
3. test it on approximate constrained packets;
4. only then attempt a proof.

If the inequality fails before the true manifold, determine whether the missing KKT/product geometry repairs it. Do not silently strengthen hypotheses after a failed proof attempt.

## 9. Dead-route ledger

Known overstrong or false approaches are part of the project state, not disposable chat history.

Current continuous dead ends include:

- strong fixed-fiber pointwise symmetrization;
- pointwise two-kernel total positivity on the raw box;
- a global one-variable dual potential at the candidate envelope;
- arbitrary four-node Chebyshev orientation for `{1,x,g_nu,g_mu}`;
- pairwise reciprocal-root inequalities strong enough to settle the collective product relation.

A future agent may reopen one only if it adds a materially new hypothesis or identifies a precise flaw in the prior counterexample.

## 10. Research artifact contract

Each new proof note should begin with:

```text
Status:
Target:
Inputs / assumptions:
Claim actually established:
What remains open:
Verifier / certificate:
Dependencies:
```

Each verifier should print a final scope statement, for example:

```text
PASS: exact identity X
SCOPE: algebraic identity only
NOT CLAIMED: global sign Y
```

This prevents a later agent from mistaking a reduction check for a theorem certificate.

## 11. Handoff contract

A research handoff should be reconstructible without chat history. It must include:

1. exact theorem inventory;
2. exact live frontier;
3. best current reduction;
4. failed routes and why they failed;
5. all numerical conjectures clearly labeled;
6. certificate entry points;
7. branch seeds / compact parameter bounds if relevant;
8. next three actions in priority order;
9. what result would count as closure.

The handoff should be written for an agent that knows mathematics but remembers nothing about the previous thread.

## 12. Verification command hierarchy

Use the repository driver rather than invoking theorem-grade scripts ad hoc when checking the integrated state:

```bash
python verify.py --research-only
python verify.py --quick
python verify.py --full
```

`--research-only` is the fastest integrated frontier check. It includes exact/certified research audits across the focused layers. Exploratory numerical scripts should not be silently wired into this path.

## 13. Definition of done for the middle strip

The middle strip is not solved merely because:

- millions of samples have `Q_123<0`;
- the symmetric branch looks lower everywhere plotted;
- no symmetry-breaking branch is found numerically;
- a local fold theorem holds.

It is solved when a rigorous global argument covers every admissible stationary and boundary alternative and proves that the global extremal boundary is exactly the claimed envelope.

That is the bar.
