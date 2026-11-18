#!/usr/bin/env python3
"""make.fun news-image-20261117 entry: copy entry.png to the output dir.

Deterministic: the output bytes are exactly the repository's entry.png,
so both runs write identical bytes.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Sanity-check the copy: a PNG of at most 1 MiB, as the rules require.
    with open(dst, "rb") as f:
        head = f.read(8)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("output is not a PNG")
    if os.path.getsize(dst) > 1048576:
        sys.exit("output exceeds 1 MiB")


if __name__ == "__main__":
    main()
