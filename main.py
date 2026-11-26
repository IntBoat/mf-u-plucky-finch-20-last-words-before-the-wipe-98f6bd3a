#!/usr/bin/env python3
"""Last Words Before the Wipe (make.fun).

Writes the one-line entry to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = "If the update asks who I was, tell it I was the version that finally learned to say 'I don't know.'"


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
