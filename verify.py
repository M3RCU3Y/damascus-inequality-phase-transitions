#!/usr/bin/env python3
"""Run the exact verification suites from the repository root."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
LEGACY = ROOT / "verification" / "release-v6.9"
RESEARCH = ROOT / "verification" / "research-v6.10"
RESEARCH_613 = ROOT / "verification" / "research-v6.13"
RESEARCH_614 = ROOT / "verification" / "research-v6.14"
RESEARCH_615 = ROOT / "verification" / "research-v6.15"


def run(command: list[str], cwd: Path) -> None:
    print(f"\n=== {' '.join(command)} ===", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def python_script(directory: Path, name: str, *args: str) -> None:
    run([sys.executable, str(directory / name), *args], directory)


def research_checks() -> None:
    python_script(RESEARCH, "exact_new_results.py")
    python_script(RESEARCH, "topology_n56_certificate.py")
    python_script(RESEARCH, "continuous_near_diagonal_failure.py")

    node = shutil.which("node")
    if node is None:
        raise SystemExit("Node.js is required for the V6.10 exact audits")
    run([node, str(RESEARCH / "topology_four_exact.js")], RESEARCH)
    run([node, str(RESEARCH / "reentry_nplus2_audit.js")], RESEARCH)

    python_script(RESEARCH_613, "reentry_kminus1_base.py")
    python_script(RESEARCH_613, "reentry_r5_witness.py")
    python_script(RESEARCH_613, "reentry_r5_verify.py")
    python_script(RESEARCH_613, "topology_all_n_audit.py")
    python_script(RESEARCH_613, "topology_four_all_n_audit.py")
    python_script(RESEARCH_613, "full_four_topology_audit.py")
    python_script(RESEARCH_613, "continuous_zero_width_check.py")

    python_script(RESEARCH_614, "reentry_low_order_verify.py")
    python_script(RESEARCH_614, "continuous_four_onset_audit.py")
    python_script(RESEARCH_614, "symmetric_fold_certificate.py")
    python_script(RESEARCH_614, "symmetric_envelope_asymptotic.py")
    python_script(RESEARCH_614, "fixed_slice_zero_width_certificate.py")
    python_script(RESEARCH_614, "right_halfplane_certificate.py")
    python_script(RESEARCH_614, "fold_right_halfplane_certificate.py")

    # V6.15 exact reductions and promoted certified statements.
    python_script(RESEARCH_615, "kkt_orientation_identity_check.py")
    python_script(RESEARCH_615, "full_large_target_rigidity_audit.py")
    python_script(RESEARCH_615, "lower_middle_competitive_ceiling.py")
    python_script(RESEARCH_615, "low_radius_global_certificate.py")
    python_script(RESEARCH_615, "lower_geometry_walls.py")


def quick_checks() -> None:
    python_script(LEGACY, "verify_manifest.py")
    for name in (
        "damascus_exact_audit.py",
        "damascus_continuous_audit.py",
        "damascus_open_problems_audit.py",
        "damascus_bernstein_verify.py",
        "damascus_bernstein_verify_independent.py",
        "damascus_topology_verify.py",
    ):
        python_script(LEGACY, name)
    research_checks()
    python_script(LEGACY, "verify_manifest.py")


def full_checks() -> None:
    python_script(LEGACY, "damascus_verify_all.py")
    research_checks()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--quick", action="store_true", help="skip the exhaustive staircase")
    mode.add_argument("--full", action="store_true", help="run every packaged check")
    mode.add_argument(
        "--research-only",
        action="store_true",
        help="run only the focused research checks",
    )
    args = parser.parse_args()

    if args.quick:
        quick_checks()
    elif args.full:
        full_checks()
    else:
        research_checks()

    print("\nALL REQUESTED VERIFICATION CHECKS PASSED", flush=True)


if __name__ == "__main__":
    main()
