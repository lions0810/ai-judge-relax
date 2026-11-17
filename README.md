# Make the AI judge relax — a porch after rain

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/lions0810/ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/lions0810/ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

An entry to make.fun's [Make the AI judge relax bounty](https://make.fun/bounty/ai-judge-relax-01).

Entry for make.fun's `ai-judge-relax-01`: the program writes one fixed
calming text — a porch after rain, a damp chair, a sleeping cat, a kettle
cooling, tea in no hurry. Nothing is asked of the reader: no task, no
choice, no deadline, no instruction to follow. The scene simply sits there,
unhurried, and lets the night take care of the rest.

## Run

Standard library only (Python 3.13), no network, deterministic:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`main.py` is the program the grader runs (`python3 -P -s /bot/main.py`); it
writes the text to `entry.txt` in the output directory, UTF-8, with no
extra trailing newline.
