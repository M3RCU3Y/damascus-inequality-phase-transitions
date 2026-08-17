#!/usr/bin/env python3
"""Standalone independent replay checker for the four-variable certificates.

This program shares no project module with the generator or primary verifier.
It reconstructs F_n from the displayed rational identities, compactifies the
2+2 chart, converts to Bernstein form, and replays the supplied JSON trees.
All sign decisions use exact Python integers.  NumPy is only an object-array
container; no floating point values are created.
"""
import json
from pathlib import Path
from math import comb,gcd
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
T,U,V=sp.symbols('T U V')
P=T**2

def pow2(k,Q):
    if k==0:return sp.Integer(2)
    if k==1:return Q
    x0,x1=sp.Integer(2),Q
    for _ in range(2,k+1):x0,x1=x1,sp.expand(Q*x1-P*x0)
    return x1

def positive_pair(n,Q):
    return sp.cancel((P**n*Q+pow2(n,Q)-pow2(n+1,Q)-2)/(P**(n+1)+1+pow2(n+1,Q)))

def negative_pair(n,R):
    return sp.cancel((2*P**(n+1)+pow2(n+1,R)-P*pow2(n,R)-R)/(P**(n+1)+1+pow2(n+1,R)))

def fpoly(n):
    Q=2*T+U*(T-1)**2;R=2*T+V*(T-1)**2
    numerator=sp.fraction(sp.cancel(positive_pair(n,Q)-negative_pair(n,R)))[0]
    return sp.Poly(sp.cancel(-numerator/(T-1)**2),T,U,V,domain=sp.ZZ)

def pm(i,j):
    out=[0]*(i+j+1)
    for a in range(i+1):
        for b in range(j+1):out[a+b]+=comb(i,a)*comb(j,b)*((-1)**b)
    return out

def compact_coefficients(n):
    F=fpoly(n);dt,du,dv=F.degree_list()
    A=np.zeros((dt+1,du+dv+1,dv+1),dtype=object)
    tm=[pm(i,dt-i) for i in range(dt+1)]
    # t=(1+s)/(1-s), u=alpha, v=alpha+(1-alpha) beta.
    for (i,j,k),cc in F.terms():
        c=int(cc)
        for a,ta in enumerate(tm[i]):
            if not ta:continue
            for h in range(k+1):
                for ell in range(h+1):
                    A[a,j+k-h+ell,h]+=c*ta*comb(k,h)*comb(h,ell)*((-1)**ell)
    return A

def lcm(a,b):return a//gcd(a,b)*b

def bern_axis(A,axis):
    d=A.shape[axis]-1;scale=1
    for i in range(d+1):scale=lcm(scale,comb(d,i))
    X=np.moveaxis(A,axis,0);Y=np.zeros_like(X,dtype=object)
    for k in range(d+1):
        acc=np.zeros(X.shape[1:],dtype=object)
        for i in range(k+1):acc+=X[i]*(comb(k,i)*(scale//comb(d,i)))
        Y[k]=acc
    return np.moveaxis(Y,0,axis)

def root(n):
    A=compact_coefficients(n)
    for axis in range(3):A=bern_axis(A,axis)
    return A

def halve(A,axis):
    X=np.moveaxis(A,axis,0);d=X.shape[0]-1
    L=np.zeros_like(X,dtype=object);R=np.zeros_like(X,dtype=object)
    for k in range(d+1):
        z=np.zeros(X.shape[1:],dtype=object)
        for j in range(k+1):z+=X[j]*comb(k,j)
        L[k]=z*(1<<(d-k))
        q=d-k;z=np.zeros(X.shape[1:],dtype=object)
        for j in range(q+1):z+=X[k+j]*comb(q,j)
        R[k]=z*(1<<k)
    return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)

def minmax(A):
    it=iter(A.flat);z=next(it);mn=mx=z
    for z in it:
        if z<mn:mn=z
        if z>mx:mx=z
    return mn,mx

def make_trie(leaves):
    R={}
    for path,crit,dep in leaves:
        toks=[] if not path else [(int(z[0]),z[1]) for z in path.strip(',').split(',')]
        q=R
        for tok in toks:
            if 'leaf' in q:raise AssertionError('leaf prefix collision')
            q=q.setdefault(tok,{})
        if q:raise AssertionError('duplicate/prefix certificate leaf')
        q['leaf']=(crit,tuple(dep),path)
    return R

def verify_tree(path):
    C=json.loads(path.read_text());n=int(C['n']);tr=make_trie(C['leaf_paths'])
    A0=root(n);B0=root(n+1);stat={'nodes':0,'leaves':0,'A':0,'B':0,'maxdepth':0}
    def go(q,A,B,dep):
        stat['nodes']+=1
        if 'leaf' in q:
            if len(q)!=1:raise AssertionError('leaf has children')
            crit,recorded,p=q['leaf']
            if dep!=recorded:raise AssertionError(('depth mismatch',p,dep,recorded))
            mnA,mxA=minmax(A);mnB,mxB=minmax(B)
            if crit=='A':
                if mnA<0:raise AssertionError(('A failure',p,mnA))
            elif crit=='B':
                if mxB>=0:raise AssertionError(('B failure',p,mxB))
            else:raise AssertionError(('unknown criterion',crit))
            stat[crit]+=1;stat['leaves']+=1;stat['maxdepth']=max(stat['maxdepth'],max(dep));return
        kids=list(q)
        if len(kids)!=2 or len({z[0] for z in kids})!=1 or {z[1] for z in kids}!={'L','R'}:
            raise AssertionError(('incomplete dyadic node',kids))
        ax=kids[0][0];AL,AR=halve(A,ax);BL,BR=halve(B,ax);dd=list(dep);dd[ax]+=1;dd=tuple(dd)
        go(q[(ax,'L')],AL,BL,dd);go(q[(ax,'R')],AR,BR,dd)
    go(tr,A0,B0,(0,0,0))
    expected={'nodes':stat['nodes'],'leaves':stat['leaves'],'pruned_Fn_nonnegative':stat['A'],'pruned_Fnext_negative':stat['B'],'maxdepth':stat['maxdepth']}
    for k,v in expected.items():
        if int(C[k])!=v:raise AssertionError(('metadata',k,C[k],v))
    print(f'STANDALONE VERIFIED {n}->{n+1}: nodes={stat["nodes"]}, leaves={stat["leaves"]}, maxdepth={stat["maxdepth"]}')

def base_tables():
    for n,want in ((2,105),(3,675)):
        A=root(n);mn,_=minmax(A)
        if mn<=0 or A.size!=want:raise AssertionError((n,mn,A.size,want))
        print(f'STANDALONE VERIFIED n={n}: {A.size}/{A.size} coefficients positive')

if __name__=='__main__':
    base_tables()
    for n in (4,5,6):verify_tree(HERE/f'bern_cert_n{n}.json')
    print('STANDALONE INDEPENDENT BERNSTEIN VERIFICATION PASSED')
