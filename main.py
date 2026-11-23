"""Write one love line to /output/entry.txt.

The line: a small, specific act of care — she warms his side of the bed
before she falls asleep — with a turn at the end that makes the old feeling
new. Stdlib only, no network, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "She still warms the left side of the bed before she falls asleep, "
    "so that when I climb in, the cold never gets to say goodnight first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE + "\n"
    assert 1 <= len(LINE) <= 240, f"line must be 1-240 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only white space"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
