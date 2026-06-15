#!/usr/bin/env python3
"""Keep rules/RULES.md byte-identical to the canonical RULES.md.

The repo root RULES.md is the single source of truth. rules/RULES.md is the
drop-in copy people ingest into their own projects; it must never drift from
canon. This script is the gate (run by pre-commit): it regenerates the copy and
exits non-zero if it was stale, so a drifted copy can't be committed.

Run manually any time: python3 rules/sync.py
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "RULES.md"
COPY = ROOT / "rules" / "RULES.md"


def main() -> int:
    canon = CANON.read_text(encoding="utf-8")
    current = COPY.read_text(encoding="utf-8") if COPY.exists() else None
    if current == canon:
        return 0
    COPY.write_text(canon, encoding="utf-8")
    print(
        "rules/RULES.md was out of sync with RULES.md — regenerated it. "
        "Stage rules/RULES.md and commit again.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
