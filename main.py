#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

The program writes exactly one joke about cats, a single line, to the
output file the grader reads. Standard library only, no network, no
input files: the joke lives in this file and nowhere else.
"""

import os
import sys

JOKE = "I bought my cat a $40 bed. She sleeps in the box it came in, on top of the receipt, out of spite."


def output_path():
    """Where the entry text goes: the kit's output dir, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def check_joke(text):
    """Refuse to write anything the gate would reject.

    The gate wants UTF-8 text of 1 to 200 characters, not only white
    space, in a single line. Anything else means the entry is broken,
    so fail here instead of shipping a dead entry.
    """
    if not text or not text.strip():
        raise ValueError("joke is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if len(text) > 200:
        raise ValueError("joke is over 200 characters")


def main():
    check_joke(JOKE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
