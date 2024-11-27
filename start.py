#!/usr/bin/env python3
import shutil
import argparse
import re
import os
from datetime import date
from pathlib import Path


def current_puzzle_year() -> str:
    """
    if it's on or after nov 30, use this year. Otherwise, use last year.

    Returns a string because math is never done on the result
    """

    now = date.today()
    if now.month == 12 or (now.month == 11 and now.day == 30):
        return str(now.year)
    return str(now.year - 1)


def next_day(year_dir: Path) -> int:
    """
    Finds the day of the last completed puzzle in a given folder.

    Returns 0 by default. Uses int because we add 1 later.
    """
    return max(
        [
            0,  # included so that new years don't break without anything in them
            *[
                int(m.group(0))
                for x in year_dir.iterdir()
                for m in [re.search(r"\d+", x.parts[-1])] if m
            ],
        ]
    )

PARSER = argparse.ArgumentParser(
    prog="./start", description="Scaffold a new Advent of Code solution"
)
PARSER.add_argument(
    "day",
    type=int,
    help=(
        "Which puzzle day to start, between [1,25]."
        " Defaults to the next day without a folder (matching `day_N`) in that year."
    ),
    nargs="?",
)
PARSER.add_argument("--year", default="2020", help="Puzzle year")


if __name__ == "__main__":
    ARGS = PARSER.parse_args()

    year_dir = Path("solutions", ARGS.year)
    year_dir.mkdir(parents=True, exist_ok=True)
    year = ARGS.year

    if ARGS.day is None:
        day = next_day(year_dir) + 1
    else:
        day = ARGS.day

    if not 1 <= day <= 25:
        PARSER.error(f"day {day} is not in range [1,25]")

    command = f'aocd {day} {year} > {year_dir}/input.txt'
    os.system(command)
    command = f'aocd {day} {year} --example  > {year_dir}/test.txt'
    os.system(command)

    submission_path = Path(year_dir, f"solution.py")
    shutil.copyfile('template_submissions.py', submission_path)


