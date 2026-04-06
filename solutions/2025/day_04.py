from itertools import product

from aocd import get_data

input = get_data(day=4, year=2025).splitlines()

# WRITE YOUR SOLUTION HERE
NEIGHBORS = [(dx, dy) for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0)]


def parse_grid(lines):
    return {(x, y) for x, line in enumerate(lines) for y, symb in enumerate(line) if symb == "@"}


def neighbors_in_grid(x, y, grid):
    return sum((x + dx, y + dy) in grid for dx, dy in NEIGHBORS)


def part_1(lines):
    grid = parse_grid(lines)
    return sum(neighbors_in_grid(x, y, grid) < 4 for x, y in grid)


def part_2(lines):
    grid = parse_grid(lines)
    initial_count = len(grid)
    while True:
        new_grid = {(x, y) for x, y in grid if neighbors_in_grid(x, y, grid) >= 4}
        if new_grid == grid:
            break
        grid = new_grid

    return initial_count - len(grid)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
