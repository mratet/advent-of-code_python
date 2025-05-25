from aocd import get_data
import re
import numpy as np
import matplotlib.pyplot as plt

input = get_data(day=13, year=2021)


def parse_input(lines):
    dots, folds = input.split("\n\n")
    coords = [map(int, line.split(",")) for line in dots.splitlines()]

    operations = []
    for line in folds.splitlines():
        match = re.match(r"fold along ([xy])=(\d+)", line)
        axis, value = match.groups()
        operations.append((axis, int(value)))
    return coords, operations


def fold_manual(coords, operations):
    Y = 2 * max(val for (axis, val) in operations if axis == "y") + 1
    X = 2 * max(val for (axis, val) in operations if axis == "x") + 1

    grid = np.zeros((Y, X), dtype=bool)
    x, y = zip(*coords)
    grid[y, x] = True

    manual_fold = []
    for axis, value in operations:
        if axis == "y":
            grid = grid[:value, :] | np.flipud(grid[value + 1 :, :])
        elif axis == "x":
            grid = grid[:, :value] | np.fliplr(grid[:, value + 1 :])
        manual_fold.append(grid)
    return manual_fold


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    coords, operations = parse_input(lines)
    manual_fold = fold_manual(coords, operations)
    return manual_fold[0].sum()


def part_2(lines):
    coords, operations = parse_input(lines)
    manual_fold = fold_manual(coords, operations)
    plt.imshow(manual_fold[-1], cmap="binary")
    plt.show()
    return None


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
