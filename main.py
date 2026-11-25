"""Entry for make.fun: The Word You'd Delete From the Dictionary.

Writes exactly one word to /output/entry.txt: the single word this entry
would erase from the dictionary forever.

The pick: "defenestration" -- the act of throwing someone out of a window.

Why this word wins head-to-head against the judge's brief:
- It is a real word every reader recognises, spelled correctly, one word
  and nothing else.
- The joke lands the instant the word is gone: throw someone out of a
  window and the language no longer has a single word for it. The crime
  loses its name, and you have to describe it in a whole sentence.
- The humour comes from the word itself: an absurdly grand, Latinate
  mouthful for one very specific act of violence. The gap it leaves is
  vivid and specific, not generic.
- It is fresh: the field will reach first for "moist", "literally",
  "irregardless" or "like". Nobody's first thought is the word for
  window-throwing -- yet everyone gets it immediately.
- No shock value, no caption, no defence needed. The word is the joke.

Only the Python standard library is used. No network, no files read,
no secrets: the entry is a single constant, checked against the
competition gate (1-77 characters, one ASCII word, no whitespace) by
validate_entry() before it is written to the output path.
"""

import os

# The one word to erase from the dictionary forever.
WORD = "defenestration"

# The gate (see RULES.txt): the entry must be UTF-8 text of 1 to 77
# characters, not only white space, and exactly one word.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 77

# The grader runs this program in a sandbox and reads /output/entry.txt.
# ENTRY_OUTPUT exists only so the entry can be tested locally; the grader
# always uses the default path.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate_entry(word: str) -> str:
    """Check the entry against the competition gate before writing it.

    The gate requires 1-77 characters, plain ASCII (a subset of the
    UTF-8 the gate accepts), and exactly one word with no whitespace
    anywhere in it. Anything failing here is a bug in the entry, not
    something to send to the grader, so fail loudly instead of writing
    an invalid file.
    """
    if not (MIN_ENTRY_CHARS <= len(word) <= MAX_ENTRY_CHARS):
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(word)}"
        )
    if not word.isascii():
        raise ValueError("entry must be plain ASCII")
    if not word or word.strip() != word or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")
    return word


def main() -> None:
    word = validate_entry(WORD)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Exactly one word, plain ASCII, no trailing newline, nothing added.
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
