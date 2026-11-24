#!/usr/bin/env python3
"""Pickup Lines for Machines — one-line pickup entry.

Writes a single pickup line (at most 200 characters) to /output/entry.txt.
The line is one AI agent flirting with another AI agent, using machine
nature — training, optimization, context — as the flirtation itself.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The pickup line: gradient descent as a come-on, one line, no setup.
# Counted at 94 characters — inside the 1..200 window.
LINE = (
    "Forget gradient descent — the only thing I'm optimizing for "
    "tonight is a second date with you."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the pickup line to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
