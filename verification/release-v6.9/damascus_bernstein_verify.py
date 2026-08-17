#!/usr/bin/env python3
"""Small replay verifier for the packaged exact Bernstein certificates.

The verifier does not search for a subdivision tree.  It reads the supplied
JSON tree leaves, checks that they form a complete dyadic partition, rebuilds
the exact root Bernstein tensors, follows only the recorded splits, and checks
the advertised leaf sign conditions using integer arithmetic.
"""
import json
from pathlib import Path
from damascus_bernstein_core import int_minmax, root_bernstein, split_axis_int

ROOT = Path(__file__).resolve().parent
LEAF = "__leaf__"


def build_trie(leaves):
    trie = {}
    for path, criterion, depth in leaves:
        tokens = [] if not path else [(int(t[0]), t[1]) for t in path.strip(',').split(',')]
        node = trie
        for tok in tokens:
            if LEAF in node:
                raise AssertionError("certificate leaf is a prefix of another leaf")
            node = node.setdefault(tok, {})
        if node:
            raise AssertionError("certificate contains a duplicate/prefix leaf")
        node[LEAF] = (criterion, tuple(depth), path)
    return trie


def verify_file(path):
    cert = json.loads(path.read_text(encoding="utf-8"))
    if cert.get("format") not in (None, "damascus-bernstein-v1"):
        raise AssertionError("unknown certificate format")
    n = int(cert["n"])
    leaves = cert["leaf_paths"]
    trie = build_trie(leaves)
    A0 = root_bernstein(n)
    B0 = root_bernstein(n+1)
    stats = {"leaves": 0, "A": 0, "B": 0, "maxdepth": 0, "nodes": 0}

    def walk(node, AA, BB, depth):
        stats["nodes"] += 1
        if LEAF in node:
            if len(node) != 1:
                raise AssertionError("leaf has children")
            criterion, recorded_depth, path_str = node[LEAF]
            if depth != recorded_depth:
                raise AssertionError(f"depth mismatch at {path_str}: {depth} != {recorded_depth}")
            minA, maxA = int_minmax(AA)
            minB, maxB = int_minmax(BB)
            if criterion == "A":
                if minA < 0:
                    raise AssertionError(f"A leaf fails at {path_str}: minA={minA}")
                stats["A"] += 1
            elif criterion == "B":
                if maxB >= 0:
                    raise AssertionError(f"B leaf fails at {path_str}: maxB={maxB}")
                stats["B"] += 1
            else:
                raise AssertionError(f"unknown pruning criterion {criterion!r}")
            stats["leaves"] += 1
            stats["maxdepth"] = max(stats["maxdepth"], max(depth))
            return

        kids = list(node.keys())
        if len(kids) != 2:
            raise AssertionError(f"incomplete subdivision node: {kids}")
        axes = {k[0] for k in kids}; sides = {k[1] for k in kids}
        if len(axes) != 1 or sides != {'L','R'}:
            raise AssertionError(f"children do not form one dyadic split: {kids}")
        axis = next(iter(axes))
        AL, AR = split_axis_int(AA, axis)
        BL, BR = split_axis_int(BB, axis)
        dep = list(depth); dep[axis] += 1; dep = tuple(dep)
        walk(node[(axis,'L')], AL, BL, dep)
        walk(node[(axis,'R')], AR, BR, dep)

    walk(trie, A0, B0, (0,0,0))
    expected = {
        "nodes": stats["nodes"],
        "leaves": stats["leaves"],
        "pruned_Fn_nonnegative": stats["A"],
        "pruned_Fnext_negative": stats["B"],
        "maxdepth": stats["maxdepth"],
    }
    for key, value in expected.items():
        if int(cert[key]) != value:
            raise AssertionError(f"metadata mismatch for {key}: JSON={cert[key]}, replay={value}")
    print(f"VERIFIED {n}->{n+1}: nodes={stats['nodes']}, leaves={stats['leaves']}, maxdepth={stats['maxdepth']}")


def verify_base_positive():
    """Verify the global all-positive Bernstein tables for n=2,3."""
    for n, expected in ((2, 105), (3, 675)):
        coeff = root_bernstein(n)
        mn, _ = int_minmax(coeff)
        if mn <= 0:
            raise AssertionError(f"n={n} base table is not strictly positive: min={mn}")
        if coeff.size != expected:
            raise AssertionError(f"n={n} coefficient count mismatch: {coeff.size} != {expected}")
        print(f"VERIFIED n={n} 2+2 exclusion: {coeff.size}/{coeff.size} Bernstein coefficients positive")


if __name__ == "__main__":
    verify_base_positive()
    for n in (4, 5, 6):
        verify_file(ROOT / f"bern_cert_n{n}.json")
    print("ALL PACKAGED BERNSTEIN CERTIFICATES VERIFIED")
