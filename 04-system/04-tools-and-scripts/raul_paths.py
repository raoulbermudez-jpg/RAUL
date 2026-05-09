"""
raul_paths.py — Canonical paths helper for /RAUL/ system

Provides resolved Path objects for the canonical /RAUL/ filesystem tree,
configurable via RAUL_ROOT env var with fallback to C:\\RAUL.

Used by Tier 1 scripts (fase4_kb_formatter, pendrive_pipeline) per
04-system/01-config/SCRIPTS-DEPENDENCIES.md.

Usage:
    from raul_paths import paths
    inbox = paths.INBOX
    indexes = paths.REPORTS_DIR  # actual 05-indexes/ (pre-separación)

    # Or explicit (testing):
    from raul_paths import get_paths
    p = get_paths(root="D:/alt/raul")

Configuration (priority order):
    1. Argument root=... to get_paths()
    2. Environment variable RAUL_ROOT
    3. Default hardcoded C:\\RAUL
"""
from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path

DEFAULT_ROOT = r"C:\RAUL"


@dataclass(frozen=True)
class RaulPaths:
    """Canonical filesystem paths for the /RAUL/ system."""
    ROOT: Path
    INBOX: Path
    KB: Path
    PROJECTS: Path
    SYSTEM: Path
    INDEXES_CANONICAL_DIR: Path  # post-separación: 05-indexes/canonical/
    LOGS_DIR: Path               # post-separación: 06-logs/
    REPORTS_DIR: Path            # actual (pre-separación): 05-indexes/
    PENDRIVE: Path               # D:/ (runtime device, no env override)
    ENV_FILE: Path               # .env at repo root


def get_paths(root: str | Path | None = None) -> RaulPaths:
    """Resolve /RAUL/ paths from explicit root, RAUL_ROOT env, or default."""
    if root is None:
        root = os.environ.get("RAUL_ROOT", DEFAULT_ROOT)
    root = Path(root)
    system = root / "04-system"
    return RaulPaths(
        ROOT=root,
        INBOX=root / "01-inbox",
        KB=root / "02-knowledge-base",
        PROJECTS=root / "03-projects",
        SYSTEM=system,
        INDEXES_CANONICAL_DIR=system / "05-indexes" / "canonical",
        LOGS_DIR=system / "06-logs",
        REPORTS_DIR=system / "05-indexes",
        PENDRIVE=Path("D:/"),
        ENV_FILE=root / ".env",
    )


paths = get_paths()


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print("=== RaulPaths (resolved from RAUL_ROOT or default) ===")
    p = get_paths()
    for field_name in p.__dataclass_fields__:
        value = getattr(p, field_name)
        exists = "[OK]" if value.exists() else "[MISSING]"
        print(f"  {field_name:25s} = {value}  {exists}")
