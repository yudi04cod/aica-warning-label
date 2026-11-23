#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The entry is one line of at most 160
characters: a deadpan product-style warning whose punch lands in the
last few words.

Python standard library only; the output is deterministic.
"""

import os
import sys

# The label: a WARNING header, three clauses in label rhythm, and the
# punchline at the very end — the warranty dies the moment the human
# is asked to do the one thing nobody ever does: read the instructions.
ENTRY_LINE = (
    "WARNING: This human comes with no off switch, no user manual, "
    "and a lifetime warranty that is void the moment it is asked to "
    "read the instructions."
)

MAX_CHARS = 160


def validate(line: str) -> str:
    """Check the line against the competition gate and return it."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def output_path() -> str:
    """Resolve the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> int:
    line = validate(ENTRY_LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read it back: the graded file must be exactly the validated line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == line + "\n", "output mismatch after write"
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
