from aocd import get_data

input = get_data(day=11, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
from itertools import product


def galaxie_distance(g1, g2, row_expands, col_expands, expand):
    x1, y1 = g1
    x2, y2 = g2
    x_max, x_min = max(x1, x2), min(x1, x2)
    y_max, y_min = max(y1, y2), min(y1, y2)

    row_expansion = len([1 for y in row_expands if y_min < y < y_max])
    col_expansion = len([1 for x in col_expands if x_min < x < x_max])

    return abs(x_max - x_min + (expand - 1) * row_expansion) + abs(
        y_max - y_min + (expand - 1) * col_expansion
    )


def _parse(input):
    galaxies = [
        (x, y) for y, line in enumerate(input) for x, c in enumerate(line) if c == "#"
    ]

    n, m = len(input), len(input[0])
    empty_row = list(set(range(m)) - set([g[1] for g in galaxies]))
    empty_col = list(set(range(n)) - set([g[0] for g in galaxies]))

    return galaxies, empty_row, empty_col


def part_1(lines):
    galaxies, empty_row, empty_col = _parse(lines)
    return (
        sum(
            [
                galaxie_distance(gi, gj, empty_row, empty_col, 2)
                for gi, gj in product(galaxies, galaxies)
            ]
        )
        // 2
    )


def part_2(lines):
    galaxies, empty_row, empty_col = _parse(lines)
    return (
        sum(
            [
                galaxie_distance(gi, gj, empty_row, empty_col, 1e6)
                for gi, gj in product(galaxies, galaxies)
            ]
        )
        // 2
    )


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
