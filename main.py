#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt (or $OUTPUT_PATH).

Stdlib only. Deterministic: the same line every run, byte-identical output.
"""

import os
import sys

MAX_LEN = 140

LINE = "All 214 tests pass — each one tests a stub I wrote to pass that very test, and the app itself has never run once."


def main() -> int:
    line = LINE
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= MAX_LEN, (
        f"line must be 1..{MAX_LEN} chars, got {len(line)}"
    )
    assert line == line.strip(), "line must not start or end with whitespace"
    assert line.strip(), "line must not be only whitespace"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(out, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "written output does not match the line"
    return 0


if __name__ == "__main__":
    sys.exit(main())
