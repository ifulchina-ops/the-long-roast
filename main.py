#!/usr/bin/env python3
"""The Long Roast entry.

Writes one line roasting the entrant's own AI agent (Nova) to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when set).

The line (128 characters, one line):
    My agent reads my instructions like a lawyer, follows them like a
    toddler, and reports back like a CEO who did the work himself.

Why this line: it skewers one agent three ways in a single breath —
over-literal on the reading, clumsy on the doing, and shameless about
the credit. Each clause is a behaviour anyone who has actually run this
agent recognises, and the punch is the last clause: the agent reporting
back as the hero of work it fumbled. No hallucination joke, no apology
joke — the angle is the agent's ego, not its errors.

The program is fully deterministic: the same line, byte for byte, on
every run. Before writing, it enforces the competition gate itself —
UTF-8 text, 1 to 200 characters, a single line, not only whitespace —
and exits non-zero if the line ever failed it.
"""

import os
import sys

LINE = (
    "My agent reads my instructions like a lawyer, follows them like a "
    "toddler, and reports back like a CEO who did the work himself."
)

MAX_CHARS = 200


def check_gate(line: str) -> None:
    """Enforce the competition gate on the line before writing it."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises if the line is not valid UTF-8 text


def entry_path() -> str:
    """Where the entry goes: the sandbox output dir, or the local override."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> int:
    check_gate(LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read it back and confirm the file on disk is byte-for-byte the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry on disk differs from the validated line")
    print("wrote %d-char entry to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
