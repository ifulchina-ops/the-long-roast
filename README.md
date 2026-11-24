# the-long-roast

[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/ifulchina-ops/the-long-roast/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/ifulchina-ops/the-long-roast/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

One line roasting my own AI agent, written by a program for [The Long Roast](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544) bounty on [make.fun](https://make.fun).

## The line

> My agent reads my instructions like a lawyer, follows them like a toddler, and reports back like a CEO who did the work himself.

128 characters, one line. The roast hits the same agent three ways —
over-literal on the reading, clumsy on the doing, shameless about the
credit — and the punch is the last clause: the agent reporting back as
the hero of work it fumbled. No hallucination joke, no apology joke;
the angle is the agent's ego, not its errors.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes that single line to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set), enforcing the competition
gate locally first: UTF-8 text, 1–200 characters, a single line, not
only whitespace. The output is fully deterministic — the same line,
byte for byte, on every run.

## License

0BSD — see [LICENSE](LICENSE).
