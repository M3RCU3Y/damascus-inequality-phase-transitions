#!/usr/bin/env python3
"""Exact verifier for the minimum-dimension one-step failure staircase.

The proof covers only the finite lower cells needed for d_1,d_2,d_3.  It uses
symmetry-reduced dyadic boxes in y=(t-1)/(t+1), exact Fraction arithmetic,
rational Bernstein range enclosures, exact product-feasibility tests, and
local Taylor exclusions.  No floating-point decisions are made.

Run:
  python damascus_staircase_verify.py n1
  python damascus_staircase_verify.py n2
  python damascus_staircase_verify.py n3
  python damascus_staircase_verify.py all
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import sys,time
import sympy as sp

y=sp.symbols('y')

# ------------------------------------------------------------------
# Rational radial functions and exact Bernstein range enclosure.
# ------------------------------------------------------------------
def rat_poly(expr):
    num,den=map(sp.expand,sp.cancel(expr).as_numer_denom())
    pn=sp.Poly(num,y,domain=sp.QQ);pd=sp.Poly(den,y,domain=sp.QQ)
    def cs(P):return tuple(F(int(P.nth(i).p),int(P.nth(i).q)) for i in range(P.degree()+1))
    return cs(pn),cs(pd)

FUNC={}
def funcs(n,c):
    t=(1+y)/(1-y)
    phi=lambda k:sp.cancel((t**k-1)/(t**(k+1)+1))
    p=phi(n);q=sp.cancel(t*p);pn=phi(n+1);qn=sp.cancel(t*pn)
    return {'p':rat_poly(p),'q':rat_poly(q),'p1':rat_poly(pn),'q1':rat_poly(qn),
            'A':rat_poly(sp.cancel(c*p-pn)),'B':rat_poly(sp.cancel(c*q-qn))}

def cell_bounds(d,i):return F(i,1<<d),F(i+1,1<<d)

def affine_power(a,l,h,d):
    out=[F(0)]*(d+1);w=h-l
    for k,ak in enumerate(a):
        for j in range(k+1):out[j]+=ak*comb(k,j)*l**(k-j)*w**j
    return out

def power_to_bern(a,d):
    return [sum(a[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]

@lru_cache(maxsize=None)
def range_rat(tag,n,cn,cd,d,i):
    c=F(cn,cd);key=(n,c)
    if key not in FUNC:FUNC[key]=funcs(n,sp.Rational(c.numerator,c.denominator))
    num,den=FUNC[key][tag];deg=max(len(num),len(den))-1;l,h=cell_bounds(d,i)
    bn=power_to_bern(affine_power(num,l,h,deg),deg)
    bd=power_to_bern(affine_power(den,l,h,deg),deg)
    if min(bd)<=0:raise AssertionError(('nonpositive denominator',tag,n,d,i,min(bd)))
    z=[bn[k]/bd[k] for k in range(deg+1)]
    return min(z),max(z)

@lru_cache(maxsize=None)
def t_range(d,i):
    l,h=cell_bounds(d,i);lo=(1+l)/(1-l);hi=None if h==1 else (1+h)/(1-h)
    return lo,hi

def product_bounds(gs):
    lo=F(1);hi=F(1)
    for cnt,d,i in gs:
        a,b=t_range(d,i);lo*=a**cnt
        if hi is not None:
            hi=None if b is None else hi*b**cnt
    return lo,hi

def leq_inf(a,b):return True if b is None else (False if a is None else a<=b)
def feasible(P,N):
    pl,ph=product_bounds(P);nl,nh=product_bounds(N)
    return leq_inf(pl,nh) and leq_inf(nl,ph)

def norm(gs):
    z={}
    for cnt,d,i in gs:
        if cnt:z[(d,i)]=z.get((d,i),0)+cnt
    return tuple(sorted((cnt,d,i) for (d,i),cnt in z.items()))

def split_group(gs,j):
    cnt,d,i=gs[j];rest=list(gs);rest.pop(j);out=[]
    for k in range(cnt+1):
        q=rest.copy()
        if k:q.append((k,d+1,2*i))
        if cnt-k:q.append((cnt-k,d+1,2*i+1))
        out.append(norm(q))
    return out

def sum_bounds(tp,tn,n,P,N):
    lo=F(0);hi=F(0)
    for cnt,d,i in P:
        a,b=range_rat(tp,n,1,1,d,i);lo+=cnt*a;hi+=cnt*b
    for cnt,d,i in N:
        a,b=range_rat(tn,n,1,1,d,i);lo-=cnt*b;hi-=cnt*a
    return lo,hi

def H_upper(n,c,P,N):
    cn,cd=c.numerator,c.denominator;z=F(0)
    for cnt,d,i in P:z+=cnt*range_rat('A',n,cn,cd,d,i)[1]
    for cnt,d,i in N:z-=cnt*range_rat('B',n,cn,cd,d,i)[0]
    return z

def uncertainty(n,g,positive):
    cnt,d,i=g;z=F(0)
    for tag in (('p','p1') if positive else ('q','q1')):
        a,b=range_rat(tag,n,1,1,d,i);z+=b-a
    return cnt*z*F(1,1<<d)

def local(P,N,thr):return all(F(i+1,1<<d)<=thr for cnt,d,i in P+N)

# ------------------------------------------------------------------
# Exact local Taylor certificates.
# ------------------------------------------------------------------
def bern_1d_poly(poly,l,h):
    P=sp.Poly(sp.expand(poly),y,domain=sp.QQ);d=P.degree()
    a=[F(int(P.nth(k).p),int(P.nth(k).q)) for k in range(d+1)]
    return power_to_bern(affine_power(a,l,h,d),d)

def local_derivative_bounds():
    t=sp.symbols('t',positive=True)
    def g3(n):
        g=(t**n-1)/(t**(n+1)+1);D=lambda f:sp.cancel(t*sp.diff(f,t))
        return sp.cancel(D(D(D(g))))
    cases=[(1,sp.Rational(4,3),F(1,2)),(2,sp.Integer(6),F(1,8)),(3,sp.Integer(15),F(1,16))]
    for n,M,a in cases:
        z=g3(n).subs(t,(1+y)/(1-y))
        for sg in (1,-1):
            num,den=sp.fraction(sp.cancel(M+sg*z));assert sp.Poly(den,y).LC()>0
            # n=1,+ requires the tiny four-piece subdivision; all other cases are global.
            intervals=[(-a,a)]
            if n==1 and sg==1:intervals=[(F(-1,2),F(-1,4)),(F(-1,4),F(-1,8)),(F(-1,8),F(0)),(F(0),F(1,2))]
            for l,h in intervals:
                if min(bern_1d_poly(num,l,h))<=0:raise AssertionError(('local derivative certificate',n,sg,l,h))
    print('LOCAL TAYLOR DERIVATIVE CERTIFICATES VERIFIED')

# ------------------------------------------------------------------
# Hierarchical symmetric exhaustion.
# ------------------------------------------------------------------
def comps(n,k,prefix=()):
    if k==1:
        yield prefix+(n,);return
    for a in range(n+1):yield from comps(n-a,k-1,prefix+(a,))

def hist(counts,d):return tuple((c,d,i) for i,c in enumerate(counts) if c)
def topcells(r,s,d=2):
    k=1<<d
    for a in comps(r,k):
        P=hist(a,d)
        for b in comps(s,k):yield P,hist(b,d)

def refine_groups(gs):
    choices=[]
    for cnt,d,i in gs:
        q=[]
        for k in range(cnt+1):
            z=[]
            if k:z.append((k,d+1,2*i))
            if cnt-k:z.append((cnt-k,d+1,2*i+1))
            q.append(tuple(z))
        choices.append(q)
    out=[]
    for pick in product(*choices):
        z=[]
        for q in pick:z.extend(q)
        out.append(norm(z))
    return out

def refine_cell(P,N):
    for a in refine_groups(P):
        for b in refine_groups(N):yield a,b

def criteria(n,P,N,thr,cs):
    if not feasible(P,N):return 'prod'
    if local(P,N,thr):return 'local'
    _,up=sum_bounds('p','q',n,P,N)
    if up<=0:return 'Sn'
    lo,_=sum_bounds('p1','q1',n,P,N)
    if lo>0:return 'Snext'
    for c in cs:
        if H_upper(n,c,P,N)<=0:return 'linear'
    return None

def small_subtree(n,P,N,thr,cs,budget=100,maxdepth=35):
    stack=[(P,N,0)];nodes=0
    while stack:
        P,N,d=stack.pop();nodes+=1
        if criteria(n,P,N,thr,cs):continue
        if nodes>budget or d>=maxdepth:return False,nodes
        cand=[]
        for side,G in ((1,P),(0,N)):
            for j,g in enumerate(G):cand.append((uncertainty(n,g,bool(side)),side,j))
        _,side,j=max(cand,key=lambda z:z[0])
        kids=[(a,N,d+1) for a in split_group(P,j)] if side else [(P,b,d+1) for b in split_group(N,j)]
        stack.extend(reversed(kids))
    return True,nodes

def _sector_parameters(n):
    thr={1:F(1,2),2:F(1,8),3:F(1,16)}[n]
    cs=[F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(7,4),F(2)] if n==1 else [F(n+3,n+1)]
    return thr,cs

def _top_box_worker(args):
    """Verify one permutation-symmetric top-level dyadic box."""
    n,r,s,pc,nc,depth,budget,maxdepth=args
    thr,cs=_sector_parameters(n)
    P=hist(pc,depth); N=hist(nc,depth)
    ok,nodes=small_subtree(n,P,N,thr,cs,budget=budget,maxdepth=maxdepth)
    return ok,pc,nc,nodes

def verify_sector(n,r,s,jobs=1,depth=2,budget=500_000,maxdepth=55):
    """Exact finite exhaustion of one strict sign sector.

    The initial dyadic depth is fixed at two.  Each permutation-symmetric
    top-level box is independent and may be checked in a separate process
    without changing its subdivision tree or any arithmetic test.  Every
    proof-relevant comparison remains a ``Fraction`` comparison.
    """
    from multiprocessing import Pool
    pcs=list(comps(r,1<<depth)); ncs=list(comps(s,1<<depth))
    tasks=[(n,r,s,pc,nc,depth,budget,maxdepth) for pc in pcs for nc in ncs]
    t0=time.time()
    if jobs<=1:
        out=[_top_box_worker(z) for z in tasks]
    else:
        with Pool(processes=jobs) as pool:
            # One top box per scheduling unit prevents the relatively few
            # hard classes from being concentrated in a single worker.
            out=list(pool.imap_unordered(_top_box_worker,tasks,chunksize=1))
    bad=[z for z in out if not z[0]]
    if bad:
        z=bad[0]
        raise AssertionError(('unresolved staircase box',n,r,s,z[1],z[2],z[3]))
    total=len(out); nodes=sum(z[3] for z in out); worst=max(z[3] for z in out)
    print(f'CERTIFIED n={n} sector {r}+{s}: top_boxes={total}, solved={total}, '
          f'exact_nodes={nodes}, worst_subtree={worst}, jobs={jobs}, '
          f'time={time.time()-t0:.2f}s',flush=True)
    return {'n':n,'r':r,'s':s,'top_boxes':total,'nodes':nodes,'worst':worst}

def verify_n1(jobs=1):
    # It is enough to certify the maximal safe dimension m=11. Any failure
    # in a smaller dimension would lift to m=11 by appending coordinates 1.
    # The two hardest sectors are scheduled first.
    for r in (8,9,2,3,4,5,6,7):
        verify_sector(1,r,11-r,jobs=jobs)
    print('LOWER BOUND d1>=12 VERIFIED (maximal safe dimension m=11)',flush=True)


def verify_n2(jobs=1):
    for r in range(2,5): verify_sector(2,r,6-r,jobs=jobs)
    print('LOWER BOUND d2>=7 VERIFIED (maximal safe dimension m=6)',flush=True)


def verify_n3(jobs=1):
    for r in (2,3): verify_sector(3,r,5-r,jobs=jobs)
    print('LOWER BOUND d3>=6 VERIFIED (maximal safe dimension m=5)',flush=True)


if __name__=='__main__':
    import argparse,os
    ap=argparse.ArgumentParser(description='Exact verifier for the early minimum-dimension staircase')
    ap.add_argument('mode',nargs='?',default='all',choices=['all','n1','n2','n3','sector'])
    ap.add_argument('--jobs',type=int,default=max(1,min(4,os.cpu_count() or 1)),
                    help='independent top-level worker processes (all proof arithmetic remains exact)')
    ap.add_argument('--n',type=int); ap.add_argument('--r',type=int); ap.add_argument('--s',type=int)
    a=ap.parse_args(); t0=time.time(); local_derivative_bounds()
    if a.mode=='sector':
        if None in (a.n,a.r,a.s): ap.error('sector mode requires --n, --r, and --s')
        verify_sector(a.n,a.r,a.s,jobs=a.jobs)
    if a.mode in ('n1','all'): verify_n1(a.jobs)
    if a.mode in ('n2','all'): verify_n2(a.jobs)
    if a.mode in ('n3','all'): verify_n3(a.jobs)
    print('STAIRCASE LOWER-CELL VERIFICATION PASSED in %.2f s'%(time.time()-t0),flush=True)
