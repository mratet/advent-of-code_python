# advent-of-code_python

This repository contains all my solution for advent of code problems. I'm trying to refactor them so that they are understandable and relatively effective for my input (< 1s).

# Setup

## Python environment

This project requires Python >= 3.12 and uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create the virtual environment and install all dependencies from pyproject.toml
uv sync

source .venv/bin/activate

mkdir ~/.config/aocd/token
aocd-token > ~/.config/aocd/token
```

## Usage

My setup is mostly inspired from [hyper-neutrino](https://github.com/hyper-neutrino/advent-of-code).
I use ```python start.py dd --year yyyy``` to download my input using [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data) and create an empty file. Then, I use 'aos' or 'aot' to run my solution on my input / test file.

# Favorite problems
Here is a recap of my favorite years problems since 2015 :
- 2015 :
- 2016 :
- 2023 :
