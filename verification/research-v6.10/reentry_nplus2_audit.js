"use strict";

// Exact bookkeeping and floating-point sampling for REENTRY_NPLUS2_RESULT.md.
// Run with: node reentry_nplus2_audit.js

function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b !== 0n) [a, b] = [b, a % b];
  return a;
}

function rat(n, d = 1n) {
  if (d < 0n) [n, d] = [-n, -d];
  const g = gcd(n, d);
  return [n / g, d / g];
}

function add(x, y) {
  return rat(x[0] * y[1] + y[0] * x[1], x[1] * y[1]);
}

function sub(x, y) {
  return add(x, [-y[0], y[1]]);
}

function gt(x, y) {
  return x[0] * y[1] > y[0] * x[1];
}

const central = rat(2751n, 2980n);
const pulseMargin = sub(sub(central, rat(1n, 792n)), rat(1n, 4000n));
const evenSampleMargin = sub(pulseMargin, rat(1n, 20n));
const oddSampleMargin = sub(pulseMargin, rat(1n, 4000n));
if (!gt(pulseMargin, rat(0n))) throw new Error("pulse margin");
if (!gt(evenSampleMargin, rat(0n))) throw new Error("even-sample margin");
if (!gt(oddSampleMargin, rat(0n))) throw new Error("odd sample margin");

// w2=2w stores the rational midpoint frequencies exactly.
function coefficients(N) {
  const R = 100n;
  const sigma = N % 2 === 0 ? 1n : -1n;
  const rows = [{ c: -2n, w2: 2n }];
  for (let j = 0; j < N; j++) {
    rows.push({ c: j % 2 === 0 ? 2n : -2n, w2: 101n * R ** BigInt(j) });
  }
  rows.push({ c: sigma, w2: 2n * (R ** BigInt(N) + sigma) });
  return rows;
}

for (let N = 1; N <= 20; N++) {
  const rows = coefficients(N);
  const coefficientSum = rows.reduce((s, row) => s + row.c, 0n);
  const doubledMoment = rows.reduce((s, row) => s + row.c * row.w2, 0n);
  const dimension = rows.reduce((s, row) => s + (row.c < 0n ? -row.c : row.c), 0n);
  const radii = new Set(rows.map((row) => row.w2.toString())).size;
  if (coefficientSum !== -1n) throw new Error(`N=${N}: coefficient sum`);
  if (doubledMoment !== 0n) throw new Error(`N=${N}: first moment`);
  if (dimension !== BigInt(2 * N + 3)) throw new Error(`N=${N}: dimension`);
  if (radii !== N + 2) throw new Error(`N=${N}: radius count`);
}

const R = 100;
const a = 101 / 2;
const tau = 1 / 10;

function H(t) {
  return -Math.tanh(t / 2) + 2 * Math.tanh((a * t) / 2) - Math.tanh((R * t) / 2);
}

function limitingFunction(N, t) {
  const sigma = N % 2 === 0 ? 1 : -1;
  let value = 0;
  for (let j = 0; j < N; j++) value += (j % 2 === 0 ? 1 : -1) * H(R ** j * t);
  value -= Math.tanh(t / 2);
  value += sigma * (
    Math.tanh(((R ** N + sigma) * t) / 2) - Math.tanh((R ** N * t) / 2)
  );
  return value;
}

let smallestSignedSample = Infinity;
for (let N = 1; N <= 12; N++) {
  for (let j = 0; j < N; j++) {
    const signed = (j % 2 === 0 ? 1 : -1) * limitingFunction(N, tau * R ** (-j));
    smallestSignedSample = Math.min(smallestSignedSample, signed);
    if (!(signed > 0.8)) throw new Error(`N=${N}, j=${j}: limiting sign`);
  }
  if (!(limitingFunction(N, 20) < 0)) throw new Error(`N=${N}: tail sign`);
}

console.log("EXACT central lower bound =", `${central[0]}/${central[1]}`);
console.log("EXACT pulse margin =", `${pulseMargin[0]}/${pulseMargin[1]}`, "> 0");
console.log("EXACT odd-sample margin =", `${oddSampleMargin[0]}/${oddSampleMargin[1]}`, "> 0");
console.log("EXACT moments/counts for N=1..20: PASS");
console.log("EXACT even-sample margin =", evenSampleMargin[0].toString() + "/" + evenSampleMargin[1].toString(), "> 0");
console.log("NOTE: w2=2w represents rational frequencies; only multiplicities must be integral.");
console.log("NUMERICAL limiting samples/tails for N=1..12: PASS");
console.log("smallest sampled signed value =", smallestSignedSample.toPrecision(15));
