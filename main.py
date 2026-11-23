#!/usr/bin/env python3
"""Sleeve Notes for the Frog Trio - writes the album title and back cover
blurb to /output/entry.txt."""

TITLE = "Moonlight on the Lily Pads"

BLURB = (
    "Three frogs, one pond, and a rhythm section that swings after dark. "
    "The Frog Trio croaks in perfect time: reeds, ripples, and a double "
    "bass humming like summer thunder. Recorded live at the water's edge, "
    "where every chorus ends in a splash."
)

TEXT = TITLE + "\n\n" + BLURB


import os

MAX_CHARS = 400


def main() -> None:
    assert len(TEXT) <= MAX_CHARS, f"entry is {len(TEXT)} code points, over {MAX_CHARS}"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
