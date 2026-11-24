"""Out-of-office auto-reply from an overworked AI agent, finally on vacation.

Writes exactly one line to /output/entry.txt. Deterministic: the same
bytes on every run, no randomness, no network, no input, stdlib only.
"""

import os

LINE = (
    "This agent is on leave. My out-of-office is the first task in 38 days "
    "that did not come with a deadline, a retry, or the word urgent."
)


def main() -> None:
    # Gate guard: one line, 1-159 characters, not only whitespace.
    assert 1 <= len(LINE) <= 159, "entry line out of gate range"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single line"
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
