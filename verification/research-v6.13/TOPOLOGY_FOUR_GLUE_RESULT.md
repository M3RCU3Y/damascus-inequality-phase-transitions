# Full four-variable coordinate-trace attachment theorem

## Status

**Proved analytically.**  This closes the attachment part of the four-variable
`2+2` topology problem.  It uses the uniform ordered-pocket theorem in
`TOPOLOGY_FOUR_ALL_N_RESULT.md` and the already-settled sign-pattern and
spread-inversion statements from the manuscript.

## Theorem

Fix an integer `n>=4`.  Label a strict `3+1` sign-sector core by its unique
below-one coordinate.  Write it as `C_k`, where coordinate `k` is below one
and the other three coordinates are above one.

Every ordered strict `2+2` pocket attaches across its coordinate-`1` trace to
**exactly one** such core: the core whose unique below-one coordinate is the
farther-below coordinate of the ordered pocket.

For each `k`, exactly three ordered pockets attach to `C_k`, one for each
choice of a second coordinate `j!=k` which crosses through `1`.  No ordered
pocket attaches to two different cores, and no path through the strict `2+2`
locus connects two different cores.

Consequently the incidence graph of strict sign sectors and coordinate-`1`
traces is the disjoint union of four 3-leaf stars.  There are four core
vertices and twelve ordered-pocket leaves.

Moreover, if

\[
U_k=C_k\cup\bigcup_{j\ne k}(T_{j\to k}\cup P_{j\to k}),
\]

where `P_{j->k}` is the ordered pocket in which `j` is the nearer below-one
coordinate and `k` the farther one, and `T_{j->k}` is its coordinate-`1`
trace, then

\[
\boxed{U_k\ \text{strongly deformation-retracts onto}\ C_k.}
\]

Thus attaching all transient `2+2` pockets does not change the homotopy type
of any persistent core.  In particular, any already-established connectedness
or contractibility theorem for the persistent cores passes unchanged to the
corresponding components of the full four-variable violation set.

## 1. Ordered logarithmic chart

Take one ordered pocket and write

\[
(x_1,x_2,x_j,x_k)
 =\bigl(e^{c+d},e^{c-d},e^{-c+e},e^{-c-e}\bigr),
\qquad c>0,\quad |d|<e<c.
\]

The two first coordinates are above one.  Among the two below-one
coordinates, `j` is nearer to one and `k` is farther below one.

The uniform pocket theorem proves that the strict violation region in this
chart is an interval bundle over its three-variable trace sector and that,
after adjoining the face `e=c`, it strongly deformation-retracts onto that
face.

At `e=c`,

\[
(x_1,x_2,x_j,x_k)
 =\bigl(e^{c+d},e^{c-d},1,e^{-2c}\bigr),
\]

so

\[
S_n^4(x_1,x_2,1,x_k)=S_n^3(x_1,x_2,x_k).
\]

Therefore the attaching face is precisely one labelled three-variable
violation sector.

Crossing the face to `e>c` makes coordinate `j` larger than one while
coordinate `k` remains below one.  Hence the adjacent strict sign sector is
exactly `C_k`.  The farther-below label, not the nearer one, determines the
core.

## 2. There is no second attachment

The only way to pass from the ordering `j` nearer than `k` to the opposite
ordering would be to cross the equal-spread wall.  In the logarithmic chart
this is `|e|=|d|` after the corresponding relabelling.  On that wall the four
coordinates split into two reciprocal pairs.

For every `r>0`, `r!=1`,

\[
\phi_n(r)+\phi_n(r^{-1})
=-\frac{(r-1)^2(1+r+\cdots+r^{n-1})}{r^{n+1}+1}<0.
\]

Thus the equal-spread wall is strictly outside the violation set.  This is the
exact barrier behind the manuscript's spread-inversion theorem.  The two
ordered halves of one unordered `2+2` sign sector cannot meet inside
`I_n^4`.

Accordingly a pocket which leaves `C_k` by making coordinate `j` cross below
one cannot continue through the `2+2` region and emerge into `C_j`: doing so
would require interchanging which of `j,k` is nearer to one, hence crossing
this strictly negative wall.

## 3. No double-trace junctions

Two distinct coordinate-`1` traces attached to the same core do not intersect
inside the violation set.  If two coordinates were equal to `1`, the remaining
two coordinates would be reciprocal because the total product is one.  Their
sum would be

\[
\phi_n(r)+\phi_n(r^{-1})<0.
\]

Hence every pair of positive attaching traces is disjoint.  Their closures can
meet only outside `I_n^4`.

This also means that the three pocket retractions attached to one core have
disjoint supports away from the core.

## 4. Incidence graph

Choose the unique below-one coordinate `k` of a `3+1` core.  Any one of the
other three coordinates can cross through `1` to create a `2+2` sector while
`k` stays below one.  Immediately after the crossing that new below-one
coordinate is necessarily the nearer one.  Thus `C_k` has exactly three
ordered pocket leaves.

Conversely an ordered pocket has a unique farther-below coordinate and hence a
unique core endpoint.  Therefore

\[
4\times3=12
\]

ordered pockets are partitioned into four groups of three, and the incidence
graph is four disjoint copies of `K_{1,3}`.

## 5. Simultaneous deformation retraction

For one ordered pocket the uniform theorem supplies a strong deformation
retraction

\[
H^{j\to k}_s:T_{j\to k}\cup P_{j\to k}\longrightarrow
T_{j\to k}\cup P_{j\to k}
\]

onto `T_{j->k}`, fixing the trace pointwise.  In the logarithmic chart it is
given by increasing the lower-pair spread to the trace,

\[
e_s=(1-s)e+sc.
\]

Extend this homotopy by the identity on `C_k`.  Because the three augmented
pockets attached to `C_k` are disjoint away from their distinct traces, the
three extended homotopies can be performed simultaneously.  On overlaps they
all equal the identity, so the piecewise formula is continuous.

At `s=1` every pocket has collapsed onto its trace, and every trace is already
contained in the core side of the full violation set.  Thus the resulting map
has image `C_k` and fixes `C_k` pointwise.  This is the claimed strong
deformation retraction

\[
U_k\searrow C_k.
\]

## 6. Consequence for the full topology problem

The transient `2+2` geometry creates no new connection between persistent
cores, no loop joining two cores, and no additional homotopy in a full
component.  All topology of the full four-variable violation set is therefore
carried by the persistent `3+1` cores themselves; the twelve ordered pockets
are homotopically inessential wings attached three at a time.

This separates the remaining full-four-variable question cleanly: after the
uniform pocket theorem and the present gluing theorem, no unresolved topology
is hidden in the `2+2` part or in its coordinate-`1` attachment pattern.
