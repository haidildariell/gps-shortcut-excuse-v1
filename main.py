#!/usr/bin/env python3
"""Write the GPS shortcut excuse entry to /output/entry.txt.

Deterministic, no network, no third-party dependencies.
"""

import os

ENTRY_PARTS = (
    "The shortcut was real: it cut twelve minutes off the trip ",
    "and added forty minutes of explaining to your wife. ",
    "I count that as a win.",
)


def build_entry_text():
    """Assemble the single-line entry and check it against the gate."""
    text = "".join(ENTRY_PARTS)
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    output_dir = "/output"
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_entry_text() + "\n")


if __name__ == "__main__":
    main()
