#!/usr/bin/env python3
"""Generate deterministic exact Bernstein subdivision certificates."""
import json
from collections import deque
from pathlib import Path
from damascus_bernstein_core import (
    int_minmax, root_bernstein, split_axis_int,
)

ROOT = Path(__file__).resolve().parent


def generate(n, max_nodes=100000):
    A = root_bernstein(n)
    B = root_bernstein(n+1)
    queue = deque([(A, B, (0, 0, 0), "")])
    leaves = []
    nodes = prA = prB = maxdepth = 0
    while queue:
        AA, BB, depth, path = queue.pop()
        nodes += 1
        if nodes > max_nodes:
            raise RuntimeError("certificate tree exceeded node budget")
        minA, maxA = int_minmax(AA)
        minB, maxB = int_minmax(BB)
        if minA >= 0:
            prA += 1
            leaves.append((path, "A", depth))
            continue
        if maxB < 0:
            prB += 1
            leaves.append((path, "B", depth))
            continue
        degA = [AA.shape[i]-1 for i in range(3)]
        degB = [BB.shape[i]-1 for i in range(3)]
        dmax = max(depth)
        scores = [max(degA[i], degB[i]) << (dmax-depth[i]) for i in range(3)]
        axis = max(range(3), key=lambda i: (scores[i], -i))
        AL, AR = split_axis_int(AA, axis)
        BL, BR = split_axis_int(BB, axis)
        dep = list(depth); dep[axis] += 1; dep = tuple(dep)
        maxdepth = max(maxdepth, max(dep))
        queue.append((AR, BR, dep, path + f"{axis}R,"))
        queue.append((AL, BL, dep, path + f"{axis}L,"))
    cert = {
        "format": "damascus-bernstein-v1",
        "n": n,
        "nodes": nodes,
        "leaves": len(leaves),
        "pruned_Fn_nonnegative": prA,
        "pruned_Fnext_negative": prB,
        "maxdepth": maxdepth,
        "leaf_paths": leaves,
    }
    out = ROOT / f"bern_cert_n{n}.json"
    out.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print(f"generated {out.name}: nodes={nodes}, leaves={len(leaves)}, maxdepth={maxdepth}")


if __name__ == "__main__":
    for n in (4, 5, 6):
        generate(n)
