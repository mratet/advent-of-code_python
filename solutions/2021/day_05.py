import re

import numpy as np
from aocd import get_data

input = get_data(day=5, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def interpolate(x, y):
    step = -1 if x > y else 1
    return np.arange(x, y + step, step)


def solve(input_data, part="part_2"):
    field = np.zeros((1000, 1000), dtype=int)
    for line in input_data:
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        if x1 == x2:
            field[interpolate(y1, y2), x1] += 1
        elif y1 == y2:
            field[y1, interpolate(x1, x2)] += 1
        elif part == "part_2":
            field[interpolate(y1, y2), interpolate(x1, x2)] += 1
    return (field > 1).sum()


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
