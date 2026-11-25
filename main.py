#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes a single line to the grader's output directory: a roast about a
midnight fridge raid, told from the raider's side at 3 a.m.
Pure standard library.

Angle: the fridge light comes on like a witness, and the judgement does
not come from a diet plan or a lecture — it comes from the leftovers
themselves, looking disappointed. The food you came to rescue is the
thing shaming you, and the shame is mutual: you are up at 3 a.m. eating
food that has already given up on you. One line, no setup, no
explanation, no moral — the stinger lands in the last three words.
"""

import os
import sys

LINE = "The fridge light came on at 3 a.m. and even the leftovers looked disappointed in me."

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "roast must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # Write exactly one line with no trailing newline: the file is the
    # entry, and the entry is the line — nothing else goes in. A trailing
    # newline would make the file two lines to a strict reader.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the artifact the judge will read is exactly the roast.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written bytes do not match the roast")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
