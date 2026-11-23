#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Entry for make.fun competition
u-daring-gecko-25-one-line-zero-use-the-useless-01ca1c68.

Writes a single original line (max 200 characters) describing a
hilariously useless superpower to /output/entry.txt.
"""

import os
import sys

# The line: a superpower with a catch that cancels it entirely.
# Teleportation sounds godlike until the fine print kicks in.
LINE = (
    "I can teleport anywhere in the world \u2014 as long as it\u2019s "
    "the exact spot I\u2019m already standing on."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The gate wants 1-200 UTF-8 chars, a single non-blank line."""
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    if not text.strip():
        sys.exit("entry must not be only whitespace")


def main() -> None:
    text = LINE.strip()
    validate(text)
    # The gate reads /output/entry.txt; honour OUTPUT_DIR if set.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(f"Wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
