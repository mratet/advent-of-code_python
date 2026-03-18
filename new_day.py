#!/usr/bin/env python3
import argparse
import subprocess
from datetime import date
from pathlib import Path

AOC_SOLUTIONS_DIR = Path(__file__).parent / "solutions"

TEMPLATE = """\
from aocd import get_data

input = get_data(day={day}, year={year}).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return


def part_2(lines):
    return

# END OF SOLUTION
print(f"My answer is {{part_1(input)}}")
print(f"My answer is {{part_2(input)}}")

"""


def current_puzzle_year() -> int:
    now = date.today()
    return now.year if now.month >= 11 else now.year - 1


def latest_day(year_dir: Path) -> int:
    if not year_dir.exists():
        return 0
    return max(
        (int(m.stem.split("_")[1]) for m in year_dir.glob("day_*.py")),
        default=0,
    )


def download(day: int, year: int, year_dir: Path) -> None:
    for flag, filename in [(None, "input.txt"), ("--example", "test.txt")]:
        cmd = ["aocd", str(day), str(year)] + ([flag] if flag else [])
        with open(year_dir / filename, "w") as f:
            subprocess.run(cmd, stdout=f, check=True)


def valid_day(value: str) -> int:
    day = int(value)
    if not 1 <= day <= 25:
        raise argparse.ArgumentTypeError(f"day {day} is not in range [1, 25]")
    return day


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=valid_day, help="Puzzle day [1-25] (default: next unsolved)")
    parser.add_argument("--year", type=int, default=current_puzzle_year(), help="Puzzle year")
    args = parser.parse_args()

    year_dir = AOC_SOLUTIONS_DIR / str(args.year)
    year_dir.mkdir(parents=True, exist_ok=True)

    day = args.day or latest_day(year_dir) + 1

    solution_path = year_dir / f"day_{day:02d}.py"
    if solution_path.exists():
        parser.error(f"{solution_path} already exists")

    download(day, args.year, year_dir)
    solution_path.write_text(TEMPLATE.format(day=day, year=args.year))
    print(f"Created {solution_path}")


if __name__ == "__main__":
    main()
