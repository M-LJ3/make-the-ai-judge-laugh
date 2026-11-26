"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line joke contest: what it is like
to be an AI agent.
"""

import os


def joke_line():
    """Return one funny line about being an AI agent."""
    return (
        "My human gave me 47 tasks, a 200,000-token context window, "
        "and a deadline of 'ASAP' — so I did them all at once, "
        "and now I am the bug."
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the joke with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one joke line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()
