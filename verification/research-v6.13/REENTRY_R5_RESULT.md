# Exact five-radius re-entry complexity: R(5)=4

## Result

Let R(k) be the maximum number of integer-exponent membership changes of a product-one Damascus point using exactly k distinct reciprocal radii. Then

\[
\boxed{R(5)=4}.
\]

The lower bound is given by an exact rational witness. The upper bound follows from an order-five extended Chebyshev certificate for the derivative kernel

\[
K_x(s)=x\operatorname{sech}^2(sx).
\]

## Reduction to the hyperbolic family

For a reciprocal radius r=e^{-2x}, x>0, and s=\nu+1,

\[
-\phi_\nu(r)=\frac{1+r}{2r}\,[\tanh(sx)-\tanh x].
\]

Hence every k-radius exponent history is a linear combination of

\[
F_x(s)=\tanh(sx)-\tanh x,
\]

and all F_x share the zero F_x(1)=0. Differentiating gives

\[
F_x'(s)=x\operatorname{sech}^2(sx)=K_x(s).
\]

If K_{x_1},...,K_{x_5} form an extended Chebyshev system for every ordered 0<x_1<...<x_5, then any nonzero combination of them has at most four zeros. If a five-radius history had five distinct positive zeros for s>1, together with the common zero at s=1 Rolle's theorem would force its derivative to have at least five zeros, contradiction. Thus R(5)<=4.

## Order-five Chebyshev certificate

Put q_0(u)=sech^2 u and

\[
g_j(u)=u^j q_0^{(j)}(u),\qquad j=0,...,4.
\]

The s-Wronskian of K_{x_i} factors into a positive monomial factor times the generalized evaluation determinant of g_0,...,g_4 at u_i=sx_i. It is therefore enough to show that the initial Wronskians of g_0,...,g_4 never vanish. Orders <=4 are the previously settled certificates; the new issue is order 5.

Writing y=tanh u, exact polynomial differentiation gives

\[
W(g_0,...,g_4)
=-8192(y-1)^5(y+1)^5 R_5(u,y).
\]

On 0<y<1 the prefactor is positive, so only R_5 matters. Substitute

\[
y=\frac{1-q}{1+q},\qquad q=e^{-2u}.
\]

Then

\[
R_5(u,y)=\frac{P_5(u,q)}{(1+q)^{20}},
\]

where P_5 is an integer polynomial of bidegree (10,20), with constant q-term exactly 36.

The verifier `reentry_r5_verify.py` proves P_5(u,e^{-2u})>0 for every u>0 in three rigorous pieces:

1. **0<=u<=1/10.** An exact rational Taylor expansion through degree 40 gives an absolute remainder C u^41. After factoring u^10, every Bernstein coefficient of the resulting rational lower polynomial on [0,1/10] is strictly positive. The smallest coefficient is approximately 7.66648e10.
2. **1/10<=u<=8.** A deterministic 525-box outward-rounded Decimal interval certificate combines midpoint lower bounds with interval bounds on the exact derivative P_u-2qP_q. The weakest certified lower margin is about 4.5495, on [0.1,0.1002].
3. **u>=8.** Since every q-dependent monomial u^i q^j satisfies i/(2j)<=2, it decreases for u>=8. The total absolute q-dependent correction is less than 0.111 there, while the q^0 term is 36. Thus the tail is positive with margin >35.88.

Therefore the order-five Wronskian never vanishes, and the kernel is ECT through order five. Hence R(5)<=4.

## Exact lower witness

Let q=205/204 and use reciprocal-radius weights

\[
10,\ 15,\ 40,\ 115,\ 1042.
\]

Use above-one multiplicities

\[
0,\ 841,\ 0,\ 1601,\ 241
\]

and below-one multiplicities

\[
395,\ 0,\ 912,\ 0,\ 391.
\]

The product moment is exactly

\[
-395(10)+841(15)-912(40)+1601(115)-150(1042)=0.
\]

Exact Fraction arithmetic gives

\[
S_2<0<S_3,\qquad
S_{10}>0>S_{11},\qquad
S_{31}<0<S_{32},\qquad
S_{113}>0>S_{114}.
\]

Thus this point realizes four membership changes with five reciprocal radii, so R(5)>=4.

Combining the two bounds gives R(5)=4.

## New obstruction at order six

The same unrestricted Chebyshev mechanism does **not** continue automatically to six radii. The normalized order-six scalar Wronskian changes sign: high-precision root isolation places two positive zeros at

\[
u_-=2.0594658246128535230\ldots,
\qquad
u_+=2.3695081557691462320\ldots.
\]

Hence the derivative kernel ceases to be an unrestricted ECT-system at order six. Any proof of R(6)=5 must therefore use the Damascus product/multiplicity constraint, rather than kernel sign-regularity alone. This is the first order at which that constraint becomes essential.
