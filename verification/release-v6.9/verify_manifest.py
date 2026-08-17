#!/usr/bin/env python3
"""Verify SHA-256 hashes in MANIFEST.sha256 relative to this script."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.sha256"
if not MANIFEST.is_file():
    raise SystemExit("MANIFEST.sha256 not found")

checked = 0
for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    digest, rel = line.split("  ", 1)
    path = ROOT / rel
    if not path.is_file():
        raise AssertionError(f"manifest file missing: {rel}")
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    actual = h.hexdigest()
    if actual != digest:
        raise AssertionError(f"SHA-256 mismatch for {rel}: {actual} != {digest}")
    checked += 1
print(f"MANIFEST VERIFIED: {checked} files")
