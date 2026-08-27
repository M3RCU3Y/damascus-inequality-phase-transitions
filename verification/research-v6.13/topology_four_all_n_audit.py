#!/usr/bin/env python3
"""Exact audit for the uniform four-variable ordered-pocket theorem."""
from math import comb,gcd
import time

def add(a,b):
    out=a.copy()
    for k,v in b.items():
        z=out.get(k,0)+v
        if z:out[k]=z
        elif k in out:del out[k]
    return out

def neg(a):return {k:-v for k,v in a.items()}
def sub(a,b):return add(a,neg(b))
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
    out={}
    for ea,va in a.items():
      for eb,vb in b.items():
        e=tuple(x+y for x,y in zip(ea,eb));z=out.get(e,0)+va*vb
        if z:out[e]=z
        elif e in out:del out[e]
    return out

def const(c,vars=3):return {(0,)*vars:int(c)} if c else {}
def var(i,vars=3):
    e=[0]*vars;e[i]=1;return {tuple(e):1}
def powp(a,n):
    vars=len(next(iter(a))) if a else 3
    out=const(1,vars);b=a
    while n:
        if n&1:out=mul(out,b)
        n//=2
        if n:b=mul(b,b)
    return out

def degree(a,axis):return max((e[axis] for e in a),default=0)
def degrees(a):
    vars=len(next(iter(a)))
    return [degree(a,i) for i in range(vars)]

def power_sum(k,Q,p,vars=3):
    if k==0:return const(2,vars)
    if k==1:return Q
    a=const(2,vars);b=Q
    for _ in range(2,k+1):a,b=b,sub(mul(Q,b),mul(p,a))
    return b

def four_num(n):
    t,u,v=var(0),var(1),var(2);one=const(1);two=const(2)
    p=powp(t,2);tm1=sub(t,one);spread=powp(tm1,2)
    q=add(scale(t,2),mul(u,spread));r=add(scale(t,2),mul(v,spread))
    pn=powp(p,n);pn1=mul(pn,p)
    Pnq=power_sum(n,q,p);Pn1q=power_sum(n+1,q,p)
    Pnr=power_sum(n,r,p);Pn1r=power_sum(n+1,r,p)
    NA=sub(add(add(mul(pn,q),Pnq),neg(Pn1q)),two)
    DA=add(add(pn1,one),Pn1q)
    NC=sub(add(add(scale(pn1,2),Pn1r),neg(mul(p,Pnr))),r)
    DC=add(add(pn1,one),Pn1r)
    return sub(mul(NA,DC),mul(NC,DA))

def sub_tri_v(a):
    t,u,w=var(0),var(1),var(2);one=const(1)
    vv=add(u,mul(sub(one,u),w));out={}
    dt=degree(a,0);du=degree(a,1);dv=degree(a,2)
    tp=[const(1)];up=[const(1)];vp=[const(1)]
    for _ in range(dt):tp.append(mul(tp[-1],t))
    for _ in range(du):up.append(mul(up[-1],u))
    for _ in range(dv):vp.append(mul(vp[-1],vv))
    for (i,j,l),c in a.items():
        out=add(out,scale(mul(mul(tp[i],up[j]),vp[l]),c))
    return out

def sub_t_projective(a,A,B,C,D):
    vars=len(next(iter(a)));s=var(0,vars);one=const(1,vars)
    num=add(scale(one,A),scale(s,B));den=add(scale(one,C),scale(s,D));dt=degree(a,0)
    nump=[const(1,vars)];denp=[const(1,vars)]
    for _ in range(dt):nump.append(mul(nump[-1],num));denp.append(mul(denp[-1],den))
    vars_pows={ax:[const(1,vars)] for ax in range(1,vars)}
    for ax in range(1,vars):
        vv=var(ax,vars);d=degree(a,ax)
        for _ in range(d):vars_pows[ax].append(mul(vars_pows[ax][-1],vv))
    out={}
    for e,c in a.items():
        i=e[0];term=mul(nump[i],denp[dt-i])
        for ax in range(1,vars):term=mul(term,vars_pows[ax][e[ax]])
        out=add(out,scale(term,c))
    return out

def lcm(a,b):return a//gcd(a,b)*b

def bern_axis(a,axis):
    d=degree(a,axis);L=1
    for i in range(d+1):L=lcm(L,comb(d,i))
    groups={}
    for e,c in a.items():
        ee=list(e);i=ee[axis];ee[axis]=0;g=tuple(ee)
        groups.setdefault(g,[]).append((i,c))
    out={}
    for g,terms in groups.items():
        for k in range(d+1):
            z=0
            for i,c in terms:
                if i<=k:z+=c*comb(k,i)*(L//comb(d,i))
            if z:
                e=list(g);e[axis]=k;out[tuple(e)]=z
    return out,L

def bern_all(a):
    L=1
    for ax in range(len(next(iter(a)))):
        a,l=bern_axis(a,ax);L*=l
    return a,L

def audit(n):
    N=four_num(n)
    A=n*n+4;C=n*n
    low=sub_t_projective(sub_tri_v(neg(N)),C,A-C,C,0)
    b,_=bern_all(low);ds=degrees(low);tot=1
    for d in ds:tot*=d+1
    vals=list(b.values());mn=min(vals);negc=sum(x<0 for x in vals)
    return negc,mn,ds,len(vals),tot-len(vals)

from fractions import Fraction as Q

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi)
        if self.lo>self.hi:self.lo,self.hi=self.hi,self.lo
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-asI(o))
    def __rsub__(self,o):return asI(o)-self
    def __mul__(self,o):
        o=asI(o); vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def recip(self):
        assert not (self.lo<=0<=self.hi)
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o):return self*asI(o).recip()
    def __pow__(self,n):
        if n==0:return I(1)
        if n%2==0 and self.lo<0<self.hi:
            return I(0,max(abs(self.lo),abs(self.hi))**n)
        vals=[self.lo**n,self.hi**n];return I(min(vals),max(vals))
    def absmax(self):return max(abs(self.lo),abs(self.hi))
def asI(x):return x if isinstance(x,I) else I(x)

def exp_pos_bounds(x,N=18):
    assert 0<=x<=1
    term=Q(1);s=Q(1)
    for k in range(1,N+1):
        term*=x/Q(k);s+=term
    nextt=term*x/Q(N+1)
    tail=nextt/(1-x/Q(N+2))
    return s,s+tail

def exp_point_bounds(x,N=18):
    x=Q(x)
    if x>=0:return exp_pos_bounds(x,N)
    lo,hi=exp_pos_bounds(-x,N)
    return 1/hi,1/lo

def expI(z,N=18):
    llo,_=exp_point_bounds(z.lo,N)
    _,uhi=exp_point_bounds(z.hi,N)
    return I(llo,uhi)

def poly_num(X,Y,p):
    p2=p*p;p3=p2*p;p4=p3*p;p5=p4*p
    A5=-p5+5*p4-10*p3+10*p2-5*p+1
    A4=26*p5-50*p4+20*p3+20*p2-20*p+5
    A3=-66*p5+60*p3-30*p+10
    A2=26*p5+50*p4+20*p3-20*p2-20*p+10
    A1=-p5-5*p4-10*p3-10*p2-5*p+5
    Aval=(((((A5*Y+A4)*Y+A3)*Y+A2)*Y+A1)*Y+1)
    Bbase=(((((Y-26)*Y+66)*Y-26)*Y+1)*Y)
    return X*Aval+p5*Bbase

def certify_box(alo,ahi,plo,phi,Nexp=18):
    a=I(alo,ahi);p=I(plo,phi)
    X=expI(a,Nexp);Y=expI(p*a,Nexp)
    num=poly_num(X,Y,p);den=(I(1)+Y)**6
    ratio=num.absmax()/den.lo
    return num.absmax()<den.lo,ratio

def recurse(alo,ahi,plo,phi,depth=0,maxdepth=20,stats=None):
    if stats is None:stats={'nodes':0,'leaves':0,'maxdepth':0,'leafworst':Q(0)}
    stats['nodes']+=1;stats['maxdepth']=max(stats['maxdepth'],depth)
    ok,ratio=certify_box(alo,ahi,plo,phi)
    if ok:
        stats['leaves']+=1;stats['leafworst']=max(stats['leafworst'],ratio);return stats
    if depth>=maxdepth:raise RuntimeError('unresolved interval box')
    aw=ahi-alo;pw=phi-plo
    if aw/Q(4,3)>=pw/Q(1,12):
        m=(alo+ahi)/2
        recurse(alo,m,plo,phi,depth+1,maxdepth,stats);recurse(m,ahi,plo,phi,depth+1,maxdepth,stats)
    else:
        m=(plo+phi)/2
        recurse(alo,ahi,plo,m,depth+1,maxdepth,stats);recurse(alo,ahi,m,phi,depth+1,maxdepth,stats)
    return stats

import sympy as sp
Nsym,zsym,esym=sp.symbols('N z eps',positive=True)
Tinv=Nsym**2/(Nsym**2+4)
D2=Nsym**2*(1-Tinv**2)+Tinv**2
assert sp.simplify((9-D2)-8*(7*Nsym**2+18)/(Nsym**2+4)**2)==0
Aq=sp.symbols('Aq')
quad=(2+Nsym*zsym)*Aq**2-2*(Nsym+zsym)*Aq+Nsym*zsym
raw=zsym*(2*(Aq/zsym)*(Nsym+(Nsym+1)*zsym-Aq)-Nsym*(1+Aq)**2)
assert sp.expand(raw+quad)==0

a_sym=sp.symbols('a')
Fsym=(sp.exp(a_sym)-1)/(1+sp.exp((1+esym)*a_sym))
series=sp.series(Fsym,a_sym,0,5).removeO().expand()
expected=(a_sym/sp.Integer(2)-esym*a_sym**2/sp.Integer(4)
          -(1+3*esym)*a_sym**3/sp.Integer(24)
          +esym*(1+3*esym+esym**2)*a_sym**4/sp.Integer(48))
assert sp.simplify(series-expected)==0
Bexpr=(-esym/sp.Integer(4)+esym*(1+3*esym)/6
       +sp.Rational(4,3)*esym**3*(1+3*esym+esym**2)
       +sp.Rational(64,15)*esym**3)
assert sp.factor(Bexpr)==esym*(80*esym**4+240*esym**3+336*esym**2+30*esym-5)/60
assert sp.factor((80*esym**4+240*esym**3+336*esym**2+30*esym-5).subs(esym,sp.Rational(1,12)))==-sp.Rational(31,1296)

Xsym,Ysym,psym=sp.symbols('X Y p',positive=True)
base=(Xsym-1)/(1+Ysym)
def Dop(f):return sp.factor(Xsym*sp.diff(f,Xsym)+psym*Ysym*sp.diff(f,Ysym))
expr=base
for _ in range(5):expr=Dop(expr)
num,den=sp.together(expr).as_numer_denom()
assert sp.factor(den-(1+Ysym)**6)==0
p2=psym**2;p3=p2*psym;p4=p3*psym;p5=p4*psym
A5=-p5+5*p4-10*p3+10*p2-5*psym+1
A4=26*p5-50*p4+20*p3+20*p2-20*psym+5
A3=-66*p5+60*p3-30*psym+10
A2=26*p5+50*p4+20*p3-20*p2-20*psym+10
A1=-p5-5*p4-10*p3-10*p2-5*psym+5
Aval=(((((A5*Ysym+A4)*Ysym+A3)*Ysym+A2)*Ysym+A1)*Ysym+1)
Bbase=(((((Ysym-26)*Ysym+66)*Ysym-26)*Ysym+1)*Ysym)
assert sp.expand(num-(Xsym*Aval+p5*Bbase))==0

def main():
    rows=[]
    for n in range(4,12):
        negc,mn,ds,nonzero,zero=audit(n)
        assert negc==0 and mn>0
        rows.append((n,ds,nonzero,zero))
    st=recurse(Q(-2,3),Q(2,3),Q(1),Q(13,12),maxdepth=24)
    assert st['nodes']==385 and st['leaves']==193 and st['maxdepth']==9 and st['leafworst']<1
    print('finite low-box certificates:',rows)
    print('fifth-derivative interval certificate:',{'nodes':st['nodes'],'leaves':st['leaves'],'maxdepth':st['maxdepth'],'all_terminal_ratios_lt_one':True})
    print('UNIFORM FOUR-VARIABLE POCKET AUDIT PASSED')

if __name__=='__main__':main()
