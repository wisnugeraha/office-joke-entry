#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes one one-line office joke (under 200 characters) to /output/entry.txt.
"""
import os


MAX_CHARS = 199

LINE = "My manager said my code was self-documenting. Turns out self was doing all the work."


def line() -> str:
    """Return the one-line office joke."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line()
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"joke is {len(text)} chars (max {MAX_CHARS})")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # World-readable: the grader collects the file as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
