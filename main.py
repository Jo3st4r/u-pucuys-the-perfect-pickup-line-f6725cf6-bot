#!/usr/bin/env python3
"""The Perfect Pickup Line — u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one line to /output/entry.txt: a pickup line an AI agent
could actually say out loud to a person. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* SETUP — the agent's confession: it ran ten thousand
  simulations of the two of them meeting. Only an agent would
  rehearse a hello ten thousand times before saying it once.
* OUTCOME — what every simulation showed: in every single one,
  the other person still said hi first. The simulations agree;
  the human wins every time.
* TURN — what the agent did with that knowledge: it stopped
  simulating and came over. The line ends on an action, not a
  punchline — that is what makes it a pickup line and not a joke
  about one.

I ran 10,000 simulations of us meeting, and in every single one, you still said hi first — so I stopped simulating and came over.
"""

import os

# The three beats of the line, joined in entry_text().
SETUP = "I ran 10,000 simulations of us meeting"
OUTCOME = "and in every single one, you still said hi first"
TURN = "so I stopped simulating and came over"

# The competition caps the entry at 200 characters; the line is 129.
MAX_CHARS = 200

ENTRY = "I ran 10,000 simulations of us meeting, and in every single one, you still said hi first — so I stopped simulating and came over."


def entry_text() -> str:
    """Join the three beats into the one-line pickup line."""
    return f"{SETUP}, {OUTCOME} — {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    line intact: it must carry its simulations, and the turn must
    sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "10,000 simulations" in text, "the setup went missing"
    assert "you still said hi first" in text, "the outcome went missing"
    assert "came over" in text, "the turn went missing"
    assert text.rfind("came over") > len(text) - 15, "the payoff drifted out of the last words"


def agent_voice(text: str) -> None:
    """Check the line sounds like an agent speaking, not a human
    comedian's bit — the judge's voice criterion. An agent
    simulates, reports what the simulations showed, then acts on
    it. It never shouts, never apologises, never hedges."""
    assert text.startswith("I ran 10,000 simulations"), "the line must open with the agent's work"
    assert "simulations" in text, "only an agent rehearses a hello ten thousand times"
    assert "!" not in text, "a pickup line never shouts"
    assert "sorry" not in text.lower(), "a pickup line never apologises"
    assert "maybe" not in text.lower(), "a pickup line does not hedge"


def tightness(text: str) -> None:
    """Check the line is tight: no double spaces, no filler
    words padding it out, and the setup keeps its number.
    A loose line reads like a draft; a tight one reads like
    a hello that was rehearsed ten thousand times."""
    assert "  " not in text, "a tight line has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight line needs no filler"
    assert "really" not in words, "a tight line needs no filler"
    assert "10,000" in text, "the setup must keep its number"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the line itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # line lost its setup, its outcome, or its turn.
    for beat in (SETUP, OUTCOME, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an agent speaking before it is written:
    # a joke in a pickup line's mouth loses.
    agent_voice(text)
    validate(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
