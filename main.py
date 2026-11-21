#!/usr/bin/env python3
"""Tide After Dark - make.fun entry for "Make the AI judge feel awe".

Writes one short calming text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

TEXT = (
    "The tide comes in after dark and smooths the sand the way it has "
    "for a thousand years. A lamp burns in one window, and the air smells "
    "of salt and rain. The water keeps its slow promise. The night is wide, "
    "and there is room in it for one more."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text is {len(text)} code points"
    assert text.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
