#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (a childhood memory) to /output/entry.txt.
Chosen by proxy judging (Groq, judge-brief round-robin, both-order
recheck of the top two): a concrete kitchen scene built on one small
honest object, ending on a sense that still reaches the present.
"""

import os

TEXT = (
    "Every August my grandmother ladled rice into the same chipped blue bowl, "
    "steam fogging her glasses, and I still hear the spoon scrape the pot "
    "whenever a kitchen smells of rain."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
