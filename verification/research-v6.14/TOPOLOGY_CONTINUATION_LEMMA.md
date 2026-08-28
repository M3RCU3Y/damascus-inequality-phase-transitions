# Boundary-positive continuation lemma for superlevel sets

## Purpose

This note makes explicit the continuation step used in the full four-variable
fixed-exponent topology proof.  The point is orientation-sensitive: a
boundary critical point of the restriction need not be harmless for an
arbitrary sublevel problem, but it is harmless for the **positive superlevel**
when the full function increases strictly in the inward normal direction.

## Lemma

Let `M` be a compact smooth manifold with corners and let

\[
 f:[a,b]\times M\to\mathbb R
\]

be a `C^1` family, smooth on every open stratum.  Put

\[
 U_t=\{x\in M:f_t(x)>0\}.
\]

Assume throughout a closed parameter interval `J subset [a,b]` that:

1. there is no interior point with `f_t=0` and `d f_t=0`;
2. on every open codimension-one face, a zero which is critical for the
   restriction to the face has strictly positive derivative in the inward
   normal direction;
3. no zero-critical event occurs on a lower-dimensional stratum.

Then the homotopy type of `U_t` is constant on `J`.

More precisely, away from the finitely covered neighborhoods of boundary
restriction-critical zeros, the sets are carried by an ordinary ambient
isotopy.  In each boundary neighborhood the superlevel set differs only by a
collar which strongly deformation-retracts onto its inner collar wall.
Consequently crossing such a boundary value cannot create or destroy a
connected component and cannot attach a nontrivial handle to the positive
superlevel.

## Proof

### 1. Regular zero set away from boundary tangencies

Remove small pairwise compatible collar neighborhoods of all points where a
zero is critical for the restriction to a codimension-one face.  On the
remaining compact set, every zero is regular on its active stratum.  The
usual parameterized implicit-function argument gives local vector fields
which solve

\[
 d_x f_t(V_t)=-\partial_t f_t
\]

along the zero set and are tangent to the active boundary strata.  A partition
of unity and compactness give a finite-time flow.  Thus the positive
superlevels outside the removed collars are ambiently isotopic as `t` varies.

No Morse-theoretic event can occur there because such an event would require a
zero critical point on an active stratum.

### 2. Local normal form at a face-critical zero

Let `p` lie on a codimension-one face and suppose

\[
 f_{t_0}(p)=0,
 \qquad d(f_{t_0}|_{\partial M})(p)=0,
\]

while the inward derivative is positive.  Choose a collar coordinate
`r>=0`, with `r=0` the face.  By continuity, after shrinking the parameter and
spatial neighborhoods,

\[
 \partial_r f_t>m>0.
\]

For each tangential coordinate `y`, the map `r -> f_t(r,y)` is therefore
strictly increasing.  Shrink the collar to `0<=r<=epsilon` and the parameter
neighborhood so that every relevant zero occurs with `r<epsilon/2`.

For fixed `(t,y)`, the positive fiber

\[
 \{r\in[0,\epsilon]:f_t(r,y)>0\}
\]

is then either all of `[0,epsilon]` or an interval of the form

\[
 (\rho_t(y),\epsilon].
\]

It is never empty, because `f_t(epsilon,y)>0` after the preceding shrinking.
Hence linear motion in the inward coordinate gives a strong deformation
retraction of the complete collar superlevel onto the inner wall

\[
 \{r=\epsilon\}.
\]

The retraction is uniform in `t` and in `y`.  The tangential Morse type of
`f_t|_{r=0}` is irrelevant: positive inward transversality fills the would-be
boundary handle by a product interval before it can change the homotopy type
of the positive superlevel.

This is exactly where the sign of the normal derivative matters.  With the
opposite orientation the analogous statement for positive superlevels would
not follow.

### 3. Gluing

Choose the collars disjoint after passing to the natural corner-compatible
cover.  On their inner walls the collar retractions agree with the regular
isotopy from Step 1 up to an arbitrarily small isotopy adjustment.  The
homotopy extension property for collars therefore glues the local
retractions to the outside isotopy.  Covering the compact parameter interval
by finitely many such neighborhoods proves that all `U_t`, `t in J`, are
homotopy equivalent.

Connected-component count is preserved as well: every collar fiber is
connected and attached to its inner wall, while the outside part is related
by an ambient isotopy.

## Application to the four-variable persistent core

In the compactified labelled `3+1` core of
`TOPOLOGY_FOUR_FULL_RESULT.md`:

- there is one interior birth, and no later interior zero-critical value;
- on an escape face the inward derivative is exactly `+1`;
- on a coordinate-`1` face, at a face-critical zero the inward derivative is

\[
 \frac\nu2-h_\nu(t)>0;
\]

- lower-dimensional strata are strictly nonpositive away from the all-one
  corner, and the punctured sector is negative near that corner.

Thus, immediately after the unique nondegenerate interior birth the labelled
core is an open ball, and the lemma proves that every later labelled core has
the same homotopy type.  This supplies the explicit continuation argument
behind the four-component contractibility theorem.
