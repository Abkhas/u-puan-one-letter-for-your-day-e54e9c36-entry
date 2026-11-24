#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one character, the letter Z, to /output/entry.txt.

Why Z: the bounty's own description gives "Z for zero sleep" as its
example of a vivid word behind a letter. Zero sleep is the most
vivid, funny and relatable of the associations the bounty names —
a sharp picture of a real day (up all night), it lands at once, and
it is honest rather than performed. The entry is the letter alone:
no word, no gloss, no punctuation, per the rules.
"""

import os
import sys

LETTER = "Z"


def main() -> int:
    # The harness exposes its output directory through
    # MAKEFUN_OUTPUT_DIR; the rules name /output/entry.txt directly.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    # Exactly one byte: the letter, no trailing newline, no spaces.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    print(f"wrote {out_path}: {LETTER!r} (1 character)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
