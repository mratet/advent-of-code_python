import numpy as np
from advent_of_code_ocr import convert_array_6
from aocd import get_data

input = get_data(day=13, year=2021)


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    dots, folds = data.split("\n\n")
    coords = [tuple(map(int, line.split(","))) for line in dots.splitlines()]
    operations = []
    for line in folds.splitlines():
        axis, value = line.split("=")
        operations.append((axis[-1], int(value)))
    return coords, operations


def solve(data, part="part_1"):
    coords, operations = parse_input(data)
    y_size = 2 * max(val for axis, val in operations if axis == "y") + 1
    x_size = 2 * max(val for axis, val in operations if axis == "x") + 1
    grid = np.zeros((y_size, x_size), dtype=bool)
    xs, ys = zip(*coords, strict=False)
    grid[ys, xs] = True
    for axis, value in operations:
        if axis == "y":
            grid = grid[:value, :] | np.flipud(grid[value + 1 :, :])
        else:
            grid = grid[:, :value] | np.fliplr(grid[:, value + 1 :])
        if part == "part_1":
            return grid.sum()
    return convert_array_6(grid, fill_pixel=True, empty_pixel=False)


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
