"""The Worst Line an AI Could Say.

Writes a single pickup line -- the worst one an AI could plausibly
deliver -- to ``entry.txt`` in the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when unset).

Pure standard library. Deterministic: the same bytes every run.
"""

import os

LINE = "I ran 10,000 simulations of us meeting. In every one, you say hello. Please say hello."

# The sealed gate accepts 1 to 140 characters of UTF-8 text, not only
# whitespace. Refuse to write anything that would fail it.
MAX_CHARS = 140


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, outside the 1-%d gate"
            % (len(line), MAX_CHARS)
        )
    # The grader may run with the repository directory read-only, so
    # everything this program writes goes to the output directory only.
    # An empty MAKEFUN_OUTPUT_DIR falls back to the default, as does
    # an unset one.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, byte for byte,
    # which also keeps it smallest for the size tie-break.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
