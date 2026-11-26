"""Rename the Planet — one funny new name for a planet, plus the why.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run, no network, stdlib only.
"""

import os

LINE = (
    "Rename Uranus 'The Side Sleeper': knocked 98 degrees onto its side, "
    "it has napped sideways for four billion years and sees no reason "
    "to get up."
)


def main() -> None:
    # Gate (competition.yaml): entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write a line that
    # would fail the gate instead of shipping an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} chars; gate needs 1-200")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
