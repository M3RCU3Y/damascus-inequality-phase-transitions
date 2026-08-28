#!/usr/bin/env python3
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
getcontext().prec=80
PREC=70; GUARD=20; CUSH=Decimal(10)**Decimal(-(PREC-8))

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(str(lo)); self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(str(hi)))
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    def __add__(self,o):
        o=ii(o)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=self.lo+o.lo
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=self.hi+o.hi
        return I(lo,hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-ii(o))
    def __rsub__(self,o):return ii(o)-self
    def __mul__(self,o):
        o=ii(o)
        with localcontext() as c:
            c.prec=PREC+GUARD;z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+min(z)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+max(z)
        return I(lo,hi)
    __rmul__=__mul__
    def rec(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError(self)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;a=Decimal(1)/self.hi
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;b=Decimal(1)/self.lo
        return I(min(a,b),max(a,b))
    def __truediv__(self,o):return self*ii(o).rec()
    def __rtruediv__(self,o):return ii(o)*self.rec()
    def exp(self):
        with localcontext() as c:
            c.prec=PREC+GUARD;a=self.lo.exp();b=self.hi.exp();ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
    def ln(self):
        if self.lo<=0:raise ValueError(self)
        with localcontext() as c:
            c.prec=PREC+GUARD;a=self.lo.ln();b=self.hi.ln();ea=(abs(a)+1)*CUSH;eb=(abs(b)+1)*CUSH
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=+(a-ea)
        with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=+(b+eb)
        return I(lo,hi)
    def sq(self):return self*self
    def __repr__(self):return f'[{self.lo},{self.hi}]'
def ii(x):return x if isinstance(x,I) else I(x)

class D1:
    __slots__=('v','d')
    def __init__(self,v,d=0):self.v=ii(v);self.d=ii(d)
    def __add__(self,o):o=dd(o);return D1(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return D1(-self.v,-self.d)
    def __sub__(self,o):return self+(-dd(o))
    def __rsub__(self,o):return dd(o)-self
    def __mul__(self,o):o=dd(o);return D1(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def rec(self):return D1(1/self.v,-self.d/(self.v*self.v))
    def __truediv__(self,o):return self*dd(o).rec()
    def __rtruediv__(self,o):return dd(o)*self.rec()
    def exp(self):z=self.v.exp();return D1(z,z*self.d)
    def ln(self):return D1(self.v.ln(),self.d/self.v)
def dd(x):return x if isinstance(x,D1) else D1(x)

T=I(Decimal('1.71237')); C=T.ln(); QL=I(Decimal('0.71237')); QU=I(Decimal('0.76738')); M0=Decimal('7.36')

def FD(m,q,dervar=None):
    M=D1(m,1 if dervar=='m' else 0); Q=D1(q,1 if dervar=='q' else 0)
    c=D1(C); tt=D1(T)
    y=(-c*M).exp(); TT=y*y
    lq=Q.ln(); r=(lq/M).exp(); a=1/(r*tt*tt)
    Fr=2*(1-y)/(tt+y)+(TT/Q-1)/(1+TT*a/Q)+(Q-1)/(1+Q*r)
    Dt=2*c*y*(1+tt)/((tt+y)*(tt+y))
    Dr=(lq/M)*Q*(1+r)/((1+Q*r)*(1+Q*r))
    loga=-lq/M-2*c; V=TT*a/Q
    Da=loga*(TT/Q)*(1+a)/((1+V)*(1+V))
    return Fr,Dt+Dr+Da

def cert_box(mlo,mhi,qlo,qhi):
    M=I(mlo,mhi);Q=I(qlo,qhi)
    Fq,Dq=FD(M,Q,'q')
    return Fq.d,Dq.d

def adaptive_rect(mlo,mhi,qlo,qhi,depth=0,maxdepth=18):
    fq,dq=cert_box(mlo,mhi,qlo,qhi)
    if fq.lo>0 and dq.lo>0:return 1,(fq.lo,dq.lo),depth
    if depth>=maxdepth:
        raise AssertionError(('rect fail',mlo,mhi,qlo,qhi,fq,dq))
    mw=(mlo+mhi)/2; qw=(qlo+qhi)/2
    if (mhi-mlo)/(mlo) > (qhi-qlo)/(qlo):
        a=adaptive_rect(mlo,mw,qlo,qhi,depth+1,maxdepth);b=adaptive_rect(mw,mhi,qlo,qhi,depth+1,maxdepth)
    else:
        a=adaptive_rect(mlo,mhi,qlo,qw,depth+1,maxdepth);b=adaptive_rect(mlo,mhi,qw,qhi,depth+1,maxdepth)
    return a[0]+b[0],(min(a[1][0],b[1][0]),min(a[1][1],b[1][1])),max(a[2],b[2])

def adaptive_1d(kind,mlo,mhi,q,depth=0,maxdepth=22):
    M=I(mlo,mhi);Q=I(q)
    F,D=FD(M,Q,None)
    if kind=='flo': good=F.v.hi<0; margin=-F.v.hi
    elif kind=='fhi':good=F.v.lo>0;margin=F.v.lo
    elif kind=='dhi':good=D.v.hi<0;margin=-D.v.hi
    else:raise ValueError
    if good:return 1,margin,depth
    if depth>=maxdepth:raise AssertionError((kind,mlo,mhi,F.v,D.v))
    mid=(mlo+mhi)/2
    a=adaptive_1d(kind,mlo,mid,q,depth+1,maxdepth);b=adaptive_1d(kind,mid,mhi,q,depth+1,maxdepth)
    return a[0]+b[0],min(a[1],b[1]),max(a[2],b[2])

def tail_certificate():
    M=I(Decimal('40'))
    ql=QL; qu=QU; tt=T; c=C
    y40=(-c*M).exp()
    rmin=(ql.ln()/M).exp()
    Llow=-ql.ln()
    Er_coeff=(1-ql)*ql*Llow*rmin/((1+ql)*(1+ql))
    amax=1/(rmin*tt*tt)
    Ea_coeff=(1+amax)/ql
    left=Er_coeff
    right=I(40)*Ea_coeff*y40*y40
    assert left.lo>right.hi, (left,right)
    ru40=(qu.ln()/M).exp()
    lower_fhi=2*(1-y40)/(tt+y40)+(qu-1)/(1+qu*ru40)-1
    assert lower_fhi.lo>0, lower_fhi
    A=2*c*(1+tt)/(tt*tt)
    Lmin=-qu.ln()
    Gmin=ql*(1+rmin)/((1+qu)*(1+qu))
    derivative_margin=Lmin*Gmin-A*I(40)*y40
    assert derivative_margin.lo>0, derivative_margin
    return left-right, lower_fhi, derivative_margin

def main():
    M1=Decimal('40')
    print('FIXED-SLICE FINITE CERTIFICATE')
    n,mins,dep=adaptive_rect(M0,M1,QL.lo,QU.lo)
    print('rectangle boxes',n,'min F_q,D_q',mins,'depth',dep)
    for kind,q in [('flo',QL.lo),('fhi',QU.lo),('dhi',QU.lo)]:
        n,mar,dep=adaptive_1d(kind,M0,M1,q)
        print(kind,'boxes',n,'margin',mar,'depth',dep)
    print('FINITE PASSED')
    a,b,d=tail_certificate()
    print('tail q_l margin',a)
    print('tail q_u lower',b)
    print('tail derivative margin',d)
    print('TAIL PASSED')
if __name__=='__main__':main()
