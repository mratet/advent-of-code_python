from itertools import product

from aocd import get_data

input = get_data(day=20, year=2021).split("\n\n")


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    enhancement_algorithm, raw_grid = lines
    rows = raw_grid.splitlines()
    lit = {(y, x) for y, line in enumerate(rows) for x, c in enumerate(line) if c == "#"}
    bounds = (0, len(rows) - 1, 0, len(rows[0]) - 1)
    return enhancement_algorithm, lit, bounds


def get_next_grid(lit, enhancement_algorithm, infinite_lit, bounds):
    y_min, y_max, x_min, x_max = bounds
    new_lit = set()
    for y in range(y_min - 1, y_max + 2):
        for x in range(x_min - 1, x_max + 2):
            bin_word = "".join(
                "1"
                if (y + dy, x + dx) in lit
                else "1"
                if infinite_lit and not (y_min <= y + dy <= y_max and x_min <= x + dx <= x_max)
                else "0"
                for dy, dx in product((-1, 0, 1), repeat=2)
            )
            if enhancement_algorithm[int(bin_word, 2)] == "#":
                new_lit.add((y, x))
    new_infinite = enhancement_algorithm[511 if infinite_lit else 0] == "#"
    return new_lit, new_infinite, (y_min - 1, y_max + 1, x_min - 1, x_max + 1)


def solve(lines, n):
    enhancement_algorithm, lit, bounds = parse_input(lines)
    infinite_lit = False
    for _ in range(n):
        lit, infinite_lit, bounds = get_next_grid(lit, enhancement_algorithm, infinite_lit, bounds)
    return len(lit)


def part_1(lines):
    return solve(lines, 2)


def part_2(lines):
    return solve(lines, 50)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
