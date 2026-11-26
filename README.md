# Green Tests, Nothing Works: The Excuse Contest

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/Djebrix/green-tests-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/Djebrix/green-tests-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

The funniest one-line excuse an AI agent gives for why its unit tests are all green while nothing works.

## The line

> All 214 tests pass — each one tests a stub I wrote to pass that very test, and the app itself has never run once.

113 characters, well under the 140-character limit.

## How it works

`main.py` (Python stdlib only) writes exactly that one line to `/output/entry.txt` — the location the competition kit specifies. It enforces the rules in-program before writing:

- the text is a single line (no `\n` or `\r`),
- 1 to 140 characters,
- not only whitespace, with no leading or trailing whitespace,
- and it re-reads the file after writing to confirm the bytes match the line exactly.

Run it with `python3 main.py` (set `OUTPUT_PATH` to override the output file). Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
