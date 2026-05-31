"""Run all solutions from the last 10 years and produce a results report with execution times."""

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

from aocd import get_data

TIMEOUT = 120.0

SOLUTIONS_DIR = Path(__file__).parent / "solutions"
OUTPUT_FILE = Path(__file__).parent / "results.txt"
YEARS = range(2015, 2026)


def warm_cache():
    print("Pre-downloading inputs...", flush=True)
    for year in YEARS:
        for day in range(1, 26):
            if find_solution(year, day) is None:
                continue
            try:
                get_data(day=day, year=year)
            except Exception as e:
                print(f"  {year} day {day:02d}: {e}")
                continue
            time.sleep(0.2)
    print("Done.", flush=True)


def find_solution(year: int, day: int) -> Path | None:
    year_dir = SOLUTIONS_DIR / str(year)
    standard = year_dir / f"day_{day:02d}.py"
    if standard.exists():
        return standard
    clean = year_dir / f"day_{day:02d}" / "clean_solution.py"
    if clean.exists():
        return clean
    return None


def parse_answers(raw: str) -> tuple[str, str]:
    answers = re.findall(r"My answer is (.+)", raw)
    if len(answers) >= 2:
        return answers[0].strip(), answers[1].strip()
    if len(answers) == 1:
        return answers[0].strip(), ""
    return raw.replace("\n", " | "), ""


def run_solution(path: Path) -> tuple[str, str, float]:
    start = time.perf_counter()
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )
    elapsed = time.perf_counter() - start
    if result.returncode != 0:
        return f"ERROR: {result.stderr.strip()[:80]}", "", elapsed
    part_1, part_2 = parse_answers(result.stdout.strip())
    return part_1, part_2, elapsed


def main(year_filter: int | None):
    years = [year_filter] if year_filter else YEARS
    tasks = []
    for year in years:
        for day in range(1, 26):
            path = find_solution(year, day)
            if path is not None:
                tasks.append((year, day, path))

    raw: dict[tuple[int, int], tuple[str, str, float]] = {}

    for year, day, path in tasks:
        try:
            part_1, part_2, elapsed = run_solution(path)
        except subprocess.TimeoutExpired:
            part_1, part_2, elapsed = f"TIMEOUT (>{TIMEOUT:.0f}s)", "", TIMEOUT
        raw[(year, day)] = (part_1, part_2, elapsed)

    results = [(year, day, *raw[(year, day)]) for year, day, _ in sorted(tasks)]

    year_totals: dict[int, float] = {}
    for year, _day, _part_1, _part_2, elapsed in results:
        year_totals[year] = year_totals.get(year, 0.0) + elapsed

    p1_width = max((len(r[2]) for r in results), default=0)

    lines = []
    header = f"{'Year':>4}  {'Day':>3}  {'Time':>10}  {'Part 1':<{p1_width}}  Part 2"
    lines.append(header)
    lines.append("-" * len(header))

    prev_year = None
    for year, day, part_1, part_2, elapsed in results:
        if prev_year is not None and year != prev_year:
            total = year_totals[prev_year]
            lines.append(f"{prev_year:>4}  {'':>3}  {total:>9.3f}s  {'** YEAR TOTAL **'}")
            lines.append("-" * len(header))
        prev_year = year
        lines.append(f"{year:>4}  {day:>3}  {elapsed:>9.3f}s  {part_1:<{p1_width}}  {part_2}")

    if prev_year is not None and year_totals[prev_year] > 0:
        total = year_totals[prev_year]
        lines.append(f"{prev_year:>4}  {'':>3}  {total:>9.3f}s  {'** YEAR TOTAL **'}")
        lines.append("-" * len(header))

    report = "\n".join(lines) + "\n"
    OUTPUT_FILE.write_text(report)
    print(report)
    print(f"Report saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--warm-cache", action="store_true", help="Pre-download all inputs before running solutions")
    parser.add_argument("--year", type=int, help="Run only solutions for a specific year")
    args = parser.parse_args()
    if args.warm_cache:
        warm_cache()
    main(args.year)
