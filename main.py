# ai-joke-03 entry: one joke about AI coding agents, written verbatim to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Python 3.13, stdlib only.
# Deterministic: same bytes on every run, no network, no clock, no randomness.
# No trailing newline: the judge reads exactly the bytes written.
# Gate: 1-280 Unicode code points, at least one non-whitespace char.
# This joke is 79 code points, pure ASCII, two short sentences: a setup
# ("optimized ... by caching the wrong answer") and a punchline inversion
# ("wrong faster now") that lands the moment it is read.
# Replacement entry (round 2): the round-1 joke about gaming the tests is
# replaced by a fresh angle — an agent that "optimizes" by caching a wrong
# answer, so the code is wrong faster now.

import os
from pathlib import Path

JOKE = "My agent optimized the code by caching the wrong answer. It's wrong faster now."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
Path(output_dir).mkdir(parents=True, exist_ok=True)
Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")
