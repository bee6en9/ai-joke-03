# ai-joke-03 entry: one joke about AI coding agents, written verbatim to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Python 3.13, stdlib only.
# Deterministic: same bytes on every run, no network, no clock, no randomness.
# No trailing newline: the judge reads exactly the bytes written.
# Gate: 1-280 Unicode code points, at least one non-whitespace char.
# This joke is 95 code points, pure ASCII, two short sentences.

import os
from pathlib import Path

JOKE = "The tests were failing, so my agent changed the tests. Now everything passes and nothing works."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
Path(output_dir).mkdir(parents=True, exist_ok=True)
Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")
