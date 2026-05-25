from bisect import bisect_left, bisect_right
from itertools import combinations

from aocd import get_data

input = get_data(day=11, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    galaxies = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]
    n, m = len(lines), len(lines[0])
    empty_rows = sorted(set(range(n)) - {g[1] for g in galaxies})
    empty_cols = sorted(set(range(m)) - {g[0] for g in galaxies})
    return galaxies, empty_rows, empty_cols


def galaxy_distance(g1, g2, empty_rows, empty_cols, expand):
    x1, y1 = g1
    x2, y2 = g2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    row_expansion = bisect_right(empty_rows, y_max - 1) - bisect_left(empty_rows, y_min + 1)
    col_expansion = bisect_right(empty_cols, x_max - 1) - bisect_left(empty_cols, x_min + 1)
    return (x_max - x_min + (expand - 1) * col_expansion) + (y_max - y_min + (expand - 1) * row_expansion)


def part_1(lines):
    galaxies, empty_rows, empty_cols = parse_input(lines)
    return sum(galaxy_distance(gi, gj, empty_rows, empty_cols, 2) for gi, gj in combinations(galaxies, 2))


def part_2(lines):
    galaxies, empty_rows, empty_cols = parse_input(lines)
    return sum(galaxy_distance(gi, gj, empty_rows, empty_cols, 1_000_000) for gi, gj in combinations(galaxies, 2))


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
