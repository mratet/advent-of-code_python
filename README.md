# advent-of-code_python

Solutions to [Advent of Code](https://adventofcode.com/) problems in Python (2015–2025), aiming for < 1s per problem. Also includes solutions written in non-English languages in `i18n_solutions/`.

# Setup

**Requirements:** Python >= 3.13, [uv](https://docs.astral.sh/uv/)

1. Install dependencies:

```bash
uv sync
```

2. Configure your AoC session token (used to download inputs via [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)):

```bash
# Auto-detect from browser cookies (Chrome/Firefox must be logged in to adventofcode.com)
uv run aocd-token

# Or set it manually
mkdir -p ~/.config/aocd && echo "YOUR_SESSION_COOKIE" > ~/.config/aocd/token
```

3. Install pre-commit hooks (`ruff` + `ty`):

```bash
uv run pre-commit install
```

# Usage

## Running a single solution

```bash
uv run python solutions/<year>/day_XX.py
```

## Scaffolding a new day

```bash
python start.py <day> --year <yyyy>
```

This downloads the puzzle input via `aocd` and creates an empty solution file.

## Running all solutions

`run_all.py` runs every solution found in `solutions/` and produces a timing report in `results.txt`.

```bash
# Run all solutions
uv run python run_all.py

# Pre-download all inputs before running (avoids counting download time on first run)
uv run python run_all.py --warm-cache

# Run only one year
uv run python run_all.py --year 2024
```

# Favorite problems

| Year | Nice                   | Hard            | Very cool                                                              |
|------|------------------------|-----------------|------------------------------------------------------------------------|
| 2025 | 7, 11                  | 10              | 8 (BOY)                                                                |
| 2024 | 11, 14, 20             | 12, 15          | 9, 17, 21 (BOY), 24                                                    |
| 2023 | 8, 10, 16, 18, 21      | 12, 19          | 5, 20 (BOY), 24                                                        |
| 2022 | 10, 14, 17, 18, 23, 25 | 15, 19          | 7, 16, 22 (BOY)                                                        |
| 2021 | 6, 12, 13, 18, 21, 22  | 8               | 14, 16, 19 / 24 (BOY)                                                  |
| 2020 | 8, 10, 23              | 18, 19          | 14, 20 (BOY), 22                                                       |
| 2019 | 8, 10, 14              | 12, 18, 22 (BOY)| Intcode (2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25), 16 (FFT), 20   |
| 2018 | 7, 8, 10, 16, 17       | 11, 13, 21, 23  | 9, 12, 15 / 24 (BOY), 19                                              |
| 2017 | 6, 7, 9, 13, 17, 19    | 3, 21, 24       | 18, 20, 23 (BOY)                                                       |
| 2016 | 8, 15, 21              | 11, 22          | 9, 19 (BOY), 12 / 23 / 25                                             |
| 2015 | 10, 11, 14, 18, 25     | 7, 22           | 19 (BOY), 20                                                           |
