"""make.fun entry: Two-Sentence Horror.

Writes a horror story in exactly two sentences to entry.txt.
"""

import os
from pathlib import Path

LINE = "I installed a camera to catch the thing moving my keys at night. Last night's footage shows me, asleep in bed, watching myself steal them."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
