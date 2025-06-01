from aocd import get_data
from itertools import product

input = get_data(day=20, year=2021).split("\n\n")


def parse_grid(lines):
    enhancement_algorithm, raw_grid = lines
    grid = {}
    for y, line in enumerate(raw_grid.splitlines()):
        for x, c in enumerate(line):
            grid[(y, x)] = c
    return enhancement_algorithm, grid


def get_next_grid(grid, enhancement_algorithm, global_symbol, step):
    next_grid = {}
    # Initial grid shape is 100 x 100
    x_range = range(-step - 1, 99 + step + 2)
    y_range = range(-step - 1, 99 + step + 2)
    for x, y in product(x_range, y_range):
        bin_word = (
            "".join(
                [
                    grid.get((x + dx, y + dy), global_symbol)
                    for dx, dy in product((-1, 0, 1), repeat=2)
                ]
            )
            .replace("#", "1")
            .replace(".", "0")
        )
        next_grid[(x, y)] = enhancement_algorithm[int(bin_word, 2)]
    return next_grid


def simulate_grid_n_times(enhancement_algorithm, grid, N):
    full_dark, full_light = enhancement_algorithm[0], enhancement_algorithm[-1]
    global_symb = "."
    for step in range(N):
        grid = get_next_grid(grid, enhancement_algorithm, global_symb, step)
        global_symb = full_dark if global_symb == "." else full_light
    return grid


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    enhancement_algorithm, grid = parse_grid(lines)
    grid = simulate_grid_n_times(enhancement_algorithm, grid, 2)
    return sum(g == "#" for g in grid.values())


def part_2(lines):
    enhancement_algorithm, grid = parse_grid(lines)
    grid = simulate_grid_n_times(enhancement_algorithm, grid, 50)
    return sum(g == "#" for g in grid.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
