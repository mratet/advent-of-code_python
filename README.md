# advent-of-code_python

This repository contains all my solution for advent of code problems. I'm trying to refactor them so that they are understandable and relatively effective for my input (< 1s).

# Setup

## Python environment

This project requires Python >= 3.13 and uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create the virtual environment and install all dependencies from pyproject.toml
uv sync
```

## AoC session token

Solutions use [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data) to download puzzle inputs automatically. A valid AoC session token is required.

```bash
# Scrape the token automatically from your browser's cookies (Chrome/Firefox must be open and logged in to adventofcode.com)
uv run aocd-token

# Alternatively, set it manually: copy the session cookie from your browser's DevTools (Application > Cookies > adventofcode.com)
mkdir -p ~/.config/aocd
echo "YOUR_SESSION_COOKIE" > ~/.config/aocd/token
```

## pre-commit

This project uses [pre-commit](https://pre-commit.com/) to run `ruff` (linter + formatter) and `ty` (type checker) before each commit.

```bash
# Install the git hooks (one-time setup)
uv run pre-commit install

# Run manually on all files
uv run pre-commit run --all-files
```

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
# Default: parallel execution (cpu_count / 2 workers) — fast but times are approximate
uv run python run_all.py

# Sequential: accurate per-solution benchmarking
uv run python run_all.py --sequential

# Pre-download all inputs before running (avoids counting download time on first run)
uv run python run_all.py --warm-cache --sequential

# Run only one year
uv run python run_all.py --year 2024 --sequential
```

> **Note:** Times reported in parallel mode are wall-clock times under CPU contention and will be higher than actual solution runtime. Use `--sequential` for reliable benchmarks.

# Favorite problems

## 2025
- **Nice** : 7, 11
- **Hard** : 10
- **Very cool** : 8

## 2024
- **Nice** : 11, 14, 20
- **Hard** : 12, 15
- **Very cool** : 9, 17, 21 (BOY), 24

## 2023
- **Nice** : 8, 10, 16, 18, 21
- **Hard** : 12, 19
- **Very cool** : 5, 20 (BOY), 24

## 2022
- **Nice** : 10, 14, 17, 18, 23, 25
- **Hard** : 15, 19
- **Very cool** : 7, 16, 22 (BOY)

## 2021
- **Nice** : 6, 12, 13, 18, 21, 22
- **Hard** : 8
- **Very cool** : 14, 16 (imo tres difficile), 19 / 24 (BOY)

## 2020
- **Nice** : 8, 10, 23
- **Hard** : 18, 19
- **Very cool** : 14, 20 (BOY), 22

## 2019
- **Nice** : 8, 10, 14
- **Hard** : 12, 18, 22 (peut-être le meilleur problème d'un pdv recherche)
- **Very cool** : Intcode (2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25), 16 (compliqué sans avoir l'intuition de la FFT), 20

## 2018
- **Nice** : 7, 8, 10, 16 (alternative sympa sur le reverse engenerring), 17 (original)
- **Hard** : 11, 13, 21 (reverse hardcore), 23 (non trivial)
- **Very cool** : 9, 12, 15 / 24 (deux problèmes très cool), 19 (reverse sympa)

## 2017
- **Nice** : 6, 7, 9, 13 (surprisingly only brute-forceable), 17, 19
- **Hard** : 3 , 21 (easy thanks to numpy), 24
- **Very cool** : 18, 20 (particle collision optimization), 23 (reverse engineering)

## 2016
- **Nice** : 8, 15, 21
- **Hard** : 11, 22 (sympa d'un pdv recherche)
- **Very cool** : 9, 19 (j'adore ces problemes), 12 / 23 / 25

## 2015
- **Nice** : 10, 11, 14, 18, 25
- **Hard** : 7, 22
- **Very cool** : 19, 20 (malheureusement brute-force)
