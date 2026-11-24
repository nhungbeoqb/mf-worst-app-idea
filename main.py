#!/usr/bin/env python3
"""Puddle - the worst app idea ever pitched.

Writes the one-sentence pitch to /output/entry.txt.
"""
import os

PITCH = (
    "Puddle rates every puddle you step in for depth, splash radius, "
    "and sock damage, then ranks you on a live leaderboard of everyone "
    "who stepped in the same puddle, because somebody has to keep score."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
