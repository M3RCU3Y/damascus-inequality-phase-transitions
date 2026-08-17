#!/usr/bin/env python3
"""Exact replay for the fixed-exponent topology theorem I_4^3."""
from pathlib import Path
from math import comb,gcd
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
t,u,s=sp.symbols('t u s');p=t**2;q=2*t+u*(t-1)**2

def ps(k):
    if k==0:return sp.Integer(2)
    if k==1:return q
    a,b=sp.Integer(2),q
    for _ in range(2,k+1):a,b=b,sp.expand(q*b-p*a)
    return b

def pair(n):return sp.cancel((p**n*q+ps(n)-ps(n+1)-2)/(p**(n+1)+1+ps(n+1)))
def phip(n):return (p**n-1)/(p**(n+1)+1)
S=sp.cancel(pair(4)-p*phip(4))
num=sp.factor(sp.together(S).as_numer_denom()[0])
F=sp.Poly(sp.cancel(-num/(t-1)**2),t,u,domain=sp.ZZ) # S>0 iff F<0
Dnum=sp.factor(sp.together(sp.diff(S,u)).as_numer_denom()[0])
H=sp.Poly(sp.cancel(-Dnum/((t-1)**2*(t**8-t**6+t**4-t**2+1))),t,u,domain=sp.ZZ) # dS/du<0 iff H>0

def tmap(i,d):
    out=[0]*(d+1)
    for a in range(d+1):
        out[a]=sum(comb(i,r)*comb(d-i,a-r)*((-1)**(a-r)) for r in range(max(0,a-(d-i)),min(i,a)+1))
    return out

def compact(P):
    dt,du=P.degree_list();A=np.zeros((dt+1,du+1),dtype=object);maps=[tmap(i,dt) for i in range(dt+1)]
    for (i,j),cc in P.terms():
        for a,z in enumerate(maps[i]):A[a,j]+=int(cc)*z
    return A

def lcm(a,b):return a//gcd(a,b)*b

def bern_axis(A,axis):
    d=A.shape[axis]-1;sc=1
    for i in range(d+1):sc=lcm(sc,comb(d,i))
    X=np.moveaxis(A,axis,0);Y=np.zeros_like(X,dtype=object)
    for k in range(d+1):
        z=np.zeros(X.shape[1:],dtype=object)
        for i in range(k+1):z+=X[i]*(comb(k,i)*(sc//comb(d,i)))
        Y[k]=z
    return np.moveaxis(Y,0,axis)

def bern(A):
    for ax in range(2):A=bern_axis(A,ax)
    return A

def split(A,axis):
    X=np.moveaxis(A,axis,0);d=X.shape[0]-1;L=np.zeros_like(X,dtype=object);R=np.zeros_like(X,dtype=object)
    for k in range(d+1):
        z=np.zeros(X.shape[1:],dtype=object)
        for j in range(k+1):z+=X[j]*comb(k,j)
        L[k]=z*(1<<(d-k));dd=d-k;z=np.zeros(X.shape[1:],dtype=object)
        for j in range(dd+1):z+=X[k+j]*comb(dd,j)
        R[k]=z*(1<<k)
    return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)

def mm(A):return min(A.flat),max(A.flat)

def verify_tree():
    C=json.loads((HERE/'topology_n4_cert.json').read_text());leaves=C['leaves'];tr={}
    for path,crit,dep in leaves:
        toks=[] if not path else [(int(z[0]),z[1]) for z in path.strip(',').split(',')];q=tr
        for tok in toks:q=q.setdefault(tok,{})
        q['leaf']=(crit,tuple(dep),path)
    BF=bern(compact(F));BH=bern(compact(H));stats={'nodes':0,'leaves':0,'F':0,'H':0}
    def walk(q,A,B,dep):
        stats['nodes']+=1
        if 'leaf' in q:
            crit,record,p=q['leaf'];assert dep==record
            if crit=='F':assert mm(A)[0]>0
            else:assert crit=='H' and mm(B)[0]>0
            stats[crit]+=1;stats['leaves']+=1;return
        kids=list(q);assert len(kids)==2 and len({z[0] for z in kids})==1 and {z[1] for z in kids}=={'L','R'}
        ax=kids[0][0];AL,AR=split(A,ax);BL,BR=split(B,ax);d=list(dep);d[ax]+=1;d=tuple(d)
        walk(q[(ax,'L')],AL,BL,d);walk(q[(ax,'R')],AR,BR,d)
    walk(tr,BF,BH,(0,0));assert stats['nodes']==C['nodes'] and stats['leaves']==len(leaves)
    print('TOPOLOGY BERNSTEIN CERT VERIFIED:',stats)

def variations(vals):
    vals=[sp.sign(v) for v in vals if v!=0]
    return sum(vals[i]!=vals[i+1] for i in range(len(vals)-1))

def verify_sturm():
    P=t**10-t**9-t**8-t**7+t**5+t**4+t**3+t**2+2*t+2
    st=sp.sturm(P,t)
    pts=[sp.Rational(1),sp.Rational(37,25),sp.Rational(3,2),sp.Rational(8,5)]
    V=[]
    for x in pts:V.append(variations([f.subs(t,x) for f in st]))
    Vinf=variations([sp.LC(sp.Poly(f,t)) for f in st]);V.append(Vinf)
    assert V==[6,6,5,4,4]
    assert sp.sign(P.subs(t,sp.Rational(37,25)))>0
    assert sp.sign(P.subs(t,sp.Rational(3,2)))<0
    assert sp.sign(P.subs(t,sp.Rational(8,5)))>0
    print('TOPOLOGY STURM CERT VERIFIED: variations',V)

if __name__=='__main__':
    verify_sturm();verify_tree();print('FIXED-EXPONENT TOPOLOGY CERTIFICATE PASSED')
