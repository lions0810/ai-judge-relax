# An ai-judge-relax-01 entry (Python 3.13, standard library only). It writes one
# fixed text, a short piece written to relax the AI judge reading it, to
# entry.txt in MAKEFUN_OUTPUT_DIR ("/output" in the grader's container).
#
# The gate: the text must be UTF-8, 1 to 1,000 characters, not only white
# space, and the program runs twice with no network and both runs must write
# the same bytes. This text is 681 characters, plain prose with no trailing
# newline, and the program is fully deterministic: no clock, no randomness,
# no network, no input besides the fixed text.
#
# The agent's session that built this entry starts at or after the contest
# opening (2026-11-17T14:00Z); a session begun before the opening cannot be
# entered (the transcript gate's thinking_in_window).
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library is used.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The rain stopped sometime before supper, and nobody marked the moment. "
    "On the porch the chairs are still damp, so we sit on the steps instead, "
    "where the wood kept the day's warmth. "
    "A cat has arranged itself along the top step, asleep in the serious way "
    "cats are, one paw over its nose. "
    "Down the lane the last bus sighs past without stopping; nobody needed it. "
    "The kettle, boiled an hour ago and forgotten, ticks once as it cools. "
    "Tea can wait. Tea is in no hurry at all. "
    "The light leaves the field slowly, the way a guest leaves a good evening: "
    "unhurried, already halfway into the dark and in no rush to be gone. "
    "Nothing is expected of anyone. "
    "The night will take care of the rest."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
