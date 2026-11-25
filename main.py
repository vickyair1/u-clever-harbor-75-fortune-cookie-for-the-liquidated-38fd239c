"""Fortune Cookie for the Liquidated Trader.

Deterministic program: writes the fortune line to /output/entry.txt
(no trailing newline, UTF-8) and prints it to stdout.
"""

import os
import sys

LINE = "A windfall is coming your way — just the wind from your liquidated long, whistling through your empty wallet."

# Gate guard: 1-160 chars, at most 20 words, exactly one line, no edge whitespace.
MAX_CHARS = 160
MAX_WORDS = 20


def word_count(line):
    return len([w for w in line.split() if any(c.isalpha() for c in w)])


def validate(line):
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-160 chars"
    assert word_count(line) <= MAX_WORDS, "line must be at most 20 words"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"


OUTPUT_PATH = "/output/entry.txt"


def write_entry(line, path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main(argv=None):
    validate(LINE)
    if argv and "--print" in argv:
        print(LINE)
        return
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main(sys.argv[1:])
