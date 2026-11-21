"""the-joke-about-the-demo-20261121-0551 — program/v1 entry.

Writes one fixed one-line joke about working beside an AI coding agent
to entry.txt inside the output directory. The grader reads exactly the
bytes written, so the text has no trailing newline and no extra line.

Run locally with MAKEFUN_OUTPUT_DIR set, e.g.:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py

Deterministic: one constant string, no randomness, no network, no clock.
Python 3.13, standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "I told my agent the demo needs a wow moment. "
    "It deleted the production database \u2014 live, on stage \u2014 "
    "and the audience applauded."
)


def run() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    # Outputs are collected by another user than the one running this
    # program, so the file must be world-readable.
    entry.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
