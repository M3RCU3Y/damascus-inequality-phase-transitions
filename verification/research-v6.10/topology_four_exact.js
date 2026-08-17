"use strict";

// Exact-integer research audit for Paper 2, Open Problem 2.
// It proves the finite Bernstein statements used in
// TOPOLOGY_FOUR_PARTIAL_RESULT.md. Polynomials are Maps from
// comma-separated exponent vectors to BigInt; no floating-point sign
// decision is made.

function key(e) { return e.join(","); }
function exps(k) { return k.split(",").map(Number); }
function zero() { return new Map(); }
function constant(c, vars = 3) {
  const p = zero();
  if (BigInt(c) !== 0n) p.set(key(Array(vars).fill(0)), BigInt(c));
  return p;
}
function variable(i, vars = 3) {
  const e = Array(vars).fill(0); e[i] = 1;
  return new Map([[key(e), 1n]]);
}
function add(a, b) {
  const out = new Map(a);
  for (const [k, v] of b) {
    const z = (out.get(k) || 0n) + v;
    if (z === 0n) out.delete(k); else out.set(k, z);
  }
  return out;
}
function neg(a) { const out = zero(); for (const [k,v] of a) out.set(k,-v); return out; }
function sub(a,b) { return add(a,neg(b)); }
function scale(a,c) {
  c=BigInt(c); const out=zero(); if(c===0n)return out;
  for(const[k,v]of a)out.set(k,v*c); return out;
}
function mul(a,b) {
  const out=zero();
  for(const[ka,va]of a)for(const[kb,vb]of b){
    const ea=exps(ka),eb=exps(kb),e=ea.map((x,i)=>x+eb[i]),k=key(e);
    const z=(out.get(k)||0n)+va*vb;
    if(z===0n)out.delete(k);else out.set(k,z);
  }
  return out;
}
function pow(a,n) {
  let out=constant(1, exps(a.keys().next().value).length), b=a;
  while(n){if(n&1)out=mul(out,b);n>>=1;if(n)b=mul(b,b);}return out;
}
function derivative(a,axis){
  const out=zero();
  for(const[k,v]of a){const e=exps(k);if(e[axis]){const m=BigInt(e[axis]);e[axis]--;out.set(key(e),v*m);}}
  return out;
}
function degree(a,axis){let d=0;for(const k of a.keys())d=Math.max(d,exps(k)[axis]);return d;}
function degrees(a){const n=exps(a.keys().next().value).length;return Array.from({length:n},(_,i)=>degree(a,i));}
function binom(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n-k+i)/BigInt(i);return z;}
function gcd(a,b){while(b){const r=a%b;a=b;b=r;}return a<0n?-a:a;}
function lcm(a,b){return a/gcd(a,b)*b;}

function powerSum(k,Q,p,vars=3){
  if(k===0)return constant(2,vars);if(k===1)return Q;
  let a=constant(2,vars),b=Q;
  for(let j=2;j<=k;j++){const z=sub(mul(Q,b),mul(p,a));a=b;b=z;}return b;
}

function fourVariableNumerator(n){
  const t=variable(0),u=variable(1),v=variable(2),one=constant(1),two=constant(2);
  const p=pow(t,2), tm1=sub(t,one), spread=pow(tm1,2);
  const q=add(scale(t,2),mul(u,spread));
  const r=add(scale(t,2),mul(v,spread));
  const pn=pow(p,n),pn1=mul(pn,p);
  const Pnq=powerSum(n,q,p),Pn1q=powerSum(n+1,q,p);
  const Pnr=powerSum(n,r,p),Pn1r=powerSum(n+1,r,p);
  const NA=sub(add(add(mul(pn,q),Pnq),neg(Pn1q)),two);
  const DA=add(add(pn1,one),Pn1q);
  const NC=sub(add(add(scale(pn1,2),Pn1r),neg(mul(p,Pnr))),r);
  const DC=add(add(pn1,one),Pn1r);
  return {Snum:sub(mul(NA,DC),mul(NC,DA)),NA,DA,NC,DC};
}

function substituteTriangularV(a){
  // (t,u,v) -> (t,u,w), v=u+(1-u)w.
  const t=variable(0),u=variable(1),w=variable(2),one=constant(1);
  const vv=add(u,mul(sub(one,u),w));
  const out=zero();
  for(const[k,c]of a){const[i,j,l]=exps(k);let term=scale(mul(mul(pow(t,i),pow(u,j)),pow(vv,l)),c);for(const[kt,ct]of term){const z=(out.get(kt)||0n)+ct;if(z===0n)out.delete(kt);else out.set(kt,z);}}
  return out;
}

function substituteTProjective(a,A,B,C,D){
  // t=(A+B*s)/(C+D*s), multiply by (C+D*s)^degree_t.
  // Other variables are unchanged. All parameters are integers.
  const vars=exps(a.keys().next().value).length, s=variable(0,vars), one=constant(1,vars);
  const num=add(scale(one,A),scale(s,B)),den=add(scale(one,C),scale(s,D));
  const dt=degree(a,0), out=zero();
  for(const[k,c]of a){const e=exps(k),i=e[0];e[0]=0;let rest=constant(1,vars);for(let ax=1;ax<vars;ax++)rest=mul(rest,pow(variable(ax,vars),e[ax]));let term=scale(mul(mul(pow(num,i),pow(den,dt-i)),rest),c);for(const[kt,ct]of term){const z=(out.get(kt)||0n)+ct;if(z===0n)out.delete(kt);else out.set(kt,z);}}
  return out;
}

function bernsteinAxis(a,axis){
  const d=degree(a,axis);let L=1n;for(let i=0;i<=d;i++)L=lcm(L,binom(d,i));
  const groups=new Map();
  for(const[k,c]of a){const e=exps(k),i=e[axis];e[axis]=0;const g=key(e);if(!groups.has(g))groups.set(g,[]);groups.get(g).push([i,c]);}
  const out=zero();
  for(const[g,terms]of groups){const base=exps(g);for(let k=0;k<=d;k++){let z=0n;for(const[i,c]of terms)if(i<=k)z+=c*binom(k,i)*(L/binom(d,i));if(z){const e=base.slice();e[axis]=k;out.set(key(e),z);}}}
  return {poly:out,scale:L};
}
function bernsteinAll(a){let scaleTotal=1n;for(let axis=0;axis<degrees(a).length;axis++){const r=bernsteinAxis(a,axis);a=r.poly;scaleTotal*=r.scale;}return{poly:a,scale:scaleTotal};}
function minmax(a){let mn=null,mx=null;for(const v of a.values()){if(mn===null||v<mn)mn=v;if(mx===null||v>mx)mx=v;}return{mn,mx,count:a.size};}
function fixAndDropAxis(a,axis,value){
  const out=zero();
  for(const[k,c]of a){const e=exps(k);const power=e[axis];if(value===0&&power>0)continue;e.splice(axis,1);const kk=key(e);const z=(out.get(kk)||0n)+c;if(z===0n)out.delete(kk);else out.set(kk,z);}
  return out;
}
function dense2FromBern(p){
  const [d0,d1]=degrees(p),a=Array.from({length:d0+1},()=>Array(d1+1).fill(0n));
  for(const[k,c]of p){const[i,j]=exps(k);a[i][j]=c;}return a;
}
function splitDense2(a,axis){
  const d0=a.length-1,d1=a[0].length-1;
  if(axis===1){const tr=Array.from({length:d1+1},(_,j)=>Array.from({length:d0+1},(_,i)=>a[i][j]));const [l,r]=splitDense2(tr,0);return [Array.from({length:d0+1},(_,i)=>Array.from({length:d1+1},(_,j)=>l[j][i])),Array.from({length:d0+1},(_,i)=>Array.from({length:d1+1},(_,j)=>r[j][i]))];}
  const left=Array.from({length:d0+1},()=>Array(d1+1).fill(0n)),right=Array.from({length:d0+1},()=>Array(d1+1).fill(0n));
  for(let k=0;k<=d0;k++)for(let j=0;j<=d1;j++){
    let z=0n;for(let h=0;h<=k;h++)z+=a[h][j]*binom(k,h);left[k][j]=z*(1n<<BigInt(d0-k));
    z=0n;for(let h=0;h<=d0-k;h++)z+=a[k+h][j]*binom(d0-k,h);right[k][j]=z*(1n<<BigInt(k));
  }
  return[left,right];
}
function denseMinMax(a){let mn=a[0][0],mx=mn;for(const row of a)for(const z of row){if(z<mn)mn=z;if(z>mx)mx=z;}return{mn,mx};}
function implicationCertificate(S,D,maxDepth=18,maxNodes=200000){
  const Sb=dense2FromBern(bernsteinAll(S).poly),Db=dense2FromBern(bernsteinAll(D).poly);
  const stack=[{S:Sb,D:Db,depth:[0,0]}];let nodes=0,excluded=0,derivative=0,deep=0;
  while(stack.length){const z=stack.pop();nodes++;if(nodes>maxNodes)throw new Error(`node budget exceeded (${maxNodes})`);const sr=denseMinMax(z.S),dr=denseMinMax(z.D);if(sr.mx<=0n){excluded++;continue;}if(dr.mx<=0n){derivative++;continue;}const axis=z.depth[0]<=z.depth[1]?0:1;if(z.depth[axis]>=maxDepth)throw new Error(`unresolved at depth ${z.depth}`);const [sl,sr2]=splitDense2(z.S,axis),[dl,dr2]=splitDense2(z.D,axis),dep=z.depth.slice();dep[axis]++;deep=Math.max(deep,dep[axis]);stack.push({S:sl,D:dl,depth:dep.slice()},{S:sr2,D:dr2,depth:dep.slice()});}
  return{nodes,excludedLeaves:excluded,derivativeLeaves:derivative,maxAxisDepth:deep};
}

function report(name,p,required=true){const ds=degrees(p),total=ds.reduce((z,d)=>z*(d+1),1),b=bernsteinAll(p),m=minmax(b.poly);const ok=m.mn>=0n;if(required&&!ok)throw new Error(`${name}: negative Bernstein coefficient ${m.mn}`);console.log(JSON.stringify({name,degrees:ds,terms:p.size,bernsteinNonzeroTerms:m.count,bernsteinZeroTerms:total-m.count,minNonzero:m.mn.toString(),maxNonzero:m.mx.toString(),allCoefficientsNonnegative:ok,allNonzeroCoefficientsPositive:m.mn>0n}));return b.poly;}

function auditExponent(n,A,C){
  const {Snum,NC,DC}=fourVariableNumerator(n);
  // Exact exclusion on 1<=t<=4/3, 0<=u<=v<=1: -S numerator >=0.
  const low=substituteTProjective(substituteTriangularV(neg(Snum)),C,A-C,C,0);
  report(`n=${n} low-product exclusion, 1<=t<=${A}/${C}`,low);

  // For t>=4/3, prove dC/dv<0. Since S=A-C, this is dS/dv>0.
  const CvNum=sub(mul(derivative(NC,2),DC),mul(NC,derivative(DC,2)));
  const tail=substituteTProjective(neg(CvNum),A,C-A,C,-C);
  const tailBern=report(`n=${n} lower-pair spreading monotonicity, t>=${A}/${C}`,tail);
  let facePositive=0,faceNegative=0;
  for(const[k,c]of tailBern){if(exps(k)[0]===0){if(c>0n)facePositive++;if(c<0n)faceNegative++;}}
  console.log(JSON.stringify({name:`n=${n}, t=${A}/${C} Bernstein face`,positiveCoefficients:facePositive,negativeCoefficients:faceNegative,status:facePositive>0&&faceNegative===0?"strict for 0<v<1":"failed"}));
  if(!(facePositive>0&&faceNegative===0))throw new Error(`strict n=${n} tail face check failed`);

}

function auditThreeVariableSymmetrization(n,A,C){
  const {Snum,NA,DA}=fourVariableNumerator(n);
  const faceS=fixAndDropAxis(Snum,2,1);
  const AuNum=fixAndDropAxis(sub(mul(derivative(NA,1),DA),mul(NA,derivative(DA,1))),2,1);
  const Sc=substituteTProjective(faceS,A,C-A,C,-C);
  const Dc=substituteTProjective(AuNum,A,C-A,C,-C);
  const cert=implicationCertificate(Sc,Dc,20,1000000);
  console.log(JSON.stringify({name:`n=${n} three-variable conditional pair symmetrization, t>=${A}/${C}`,status:"verified",...cert}));
}

function bigintPow(a,n){let z=1n,b=BigInt(a);while(n){if(n&1)z*=b;n>>=1;if(n)b*=b;}return z;}
function auditSymmetricSlice(n){
  // G_n(t)=t^(2n+3)-2t^(2n+2)+t^(n+3)+t^(n+2)+t^2-2.
  // Expand at t=1+s, remove the zero constant coefficient, and apply
  // Descartes' rule to the remaining polynomial.
  const d=2*n+3, shifted=Array(d+1).fill(0n);
  const terms=[[2*n+3,1n],[2*n+2,-2n],[n+3,1n],[n+2,1n],[2,1n],[0,-2n]];
  for(const [power,c] of terms)for(let k=0;k<=power;k++)shifted[k]+=c*binom(power,k);
  if(shifted[0]!==0n||shifted[1]!==6n)throw new Error(`n=${n} symmetric endpoint expansion failed`);
  const H=shifted.slice(1), signs=H.filter(z=>z!==0n).map(z=>z>0n?1:-1);
  let changes=0;for(let i=1;i<signs.length;i++)if(signs[i]!==signs[i-1])changes++;
  const atThreeHalves=-bigintPow(3,2*n+2)+5n*bigintPow(3,n+2)*bigintPow(2,n)+bigintPow(2,2*n+1);
  const atTwo=3n*bigintPow(2,n+2)+2n;
  if(changes!==2||atThreeHalves>=0n||atTwo<=0n)throw new Error(`n=${n} symmetric slice audit failed`);
  console.log(JSON.stringify({name:`n=${n} symmetric trace interval`,status:"verified",descartesSignChanges:changes,GprimeAt1:"6",GatThreeHalvesNumerator:atThreeHalves.toString(),Gat2:atTwo.toString(),ascendingShiftedQuotientCoefficients:H.map(String)}));
}

function main(){
  for(const [n,A,C] of [[4,4,3],[5,6,5],[6,9,8],[7,11,10],[8,21,20],[9,26,25],[10,26,25]])auditExponent(n,A,C);
  for(const [n,A,C] of [[5,6,5],[6,9,8]])auditThreeVariableSymmetrization(n,A,C);
  for(const n of [5,6])auditSymmetricSlice(n);
  console.log("VERIFIED: ordered 2+2 fiber theorem for n=4,...,10; contractible trace sectors for n=5,6");
}

if(require.main===module)main();
