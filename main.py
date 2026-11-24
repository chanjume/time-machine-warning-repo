#!/usr/bin/env python3
"""Write one warning label for a time machine to /output/entry.txt.

The label imitates a real printed safety notice: a dated exit ban plus a
handling instruction as the punchline. One concrete detail (the year 1962)
names the real hazard -- the grandfather paradox, the classic
kill-your-own-ancestor loop -- and the last words reverse it: the danger
is not the handshake itself, it is that grandpa has not met grandma yet. The line is 119 characters, inside the 1-120 gate.
"""
import os

LINE = "WARNING: Do not exit in 1962. If you meet your grandfather, do not shake his hand \u2014 he hasn't met your grandmother yet."


def main():
    assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
