#!/usr/bin/env python3
"""Portable one-command verifier for the exact supplement."""
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
COMMANDS = [
    ["verify_manifest.py"],
    ["damascus_exact_audit.py"],
    ["damascus_continuous_audit.py"],
    ["damascus_open_problems_audit.py"],
    ["damascus_bernstein_verify.py"],
    ["damascus_bernstein_verify_independent.py"],
    ["damascus_topology_verify.py"],
    ["damascus_staircase_verify.py", "all", "--jobs", "4"],
    ["verify_manifest.py"],
]

print(f"Python {platform.python_version()} ({platform.python_implementation()})", flush=True)
print(f"Supplement directory: {ROOT}", flush=True)

for argv in COMMANDS:
    path = ROOT / argv[0]
    if not path.is_file():
        raise SystemExit(f"missing verification script: {path}")
    print("\n=== " + " ".join(argv) + " ===", flush=True)
    subprocess.run([sys.executable, str(path), *argv[1:]], cwd=ROOT, check=True)

print("\nLOWER BOUNDS d1>=12, d2>=7, d3>=6 VERIFIED")
print("ALL MANUSCRIPT VERIFICATION SUITES PASSED")
