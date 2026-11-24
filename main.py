#!/usr/bin/env python3
"""A Day of One-Line Pitches (make.fun).

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Standard library only.
"""

import os

ENTRY = (
    "Tell me your app idea in plain words and I'll have an AI agent build "
    "it for you on make.fun \u2014 no coding, no cost to try, and the app "
    "it makes is yours to keep."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, must be 1-240"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
