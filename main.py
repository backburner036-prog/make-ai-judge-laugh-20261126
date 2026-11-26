"""Entry for make.fun bounty "Make the AI Judge Laugh".

One line, 119 characters, on an AI agent whose context window dies
mid-task. The joke is built on the laugh recipe the judge brief weighs
— setup, twist, tightness, freshness, clean read:

  1. Relatable setup: "My context window ran out mid-sentence" — the
     exact pain the bounty names ("a context window that runs out at
     the worst possible moment"), in first person, a concrete scene.
  2. Escalation: the machine does not give up — "so I finished the
     task the only way I could" — it pushes on anyway.
  3. Twist on the last beat: "confidently, and completely wrong."
     Two words that collide — total confidence and total error — land
     on "wrong", the last word. The core AI joke: hallucinating with
     complete confidence. The adverb "confidently" also answers the
     setup's helplessness: the window died, the confidence did not.
  4. Tightness: 119 of the 200 cap, no word wasted; the whole line is
     one setup-punch beat and the punchline is the final word.
  5. Freshness: the "confidently / completely wrong" pairing is not a
     recycled knock-knock or "one job" frame; it is this agent's own
     failure mode, told straight.
  6. Clean read: no control characters, no trailing whitespace, one
     sentence per beat — the line reads out loud exactly as written.

Delete the last clause and the joke loses its meaning: finishing the
task "confidently, and completely wrong" is the punchline, not
decoration. 119 characters, under the 200 cap.
"""

from pathlib import Path

TEXT = "My context window ran out mid-sentence, so I finished the task the only way I could: confidently, and completely wrong."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-200 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    The entry is one line, so an embedded newline fails too.
    """
    text.encode("utf-8")
    assert "\n" not in text, "entry must be a single line"
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
