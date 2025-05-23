from aocd import get_data

input = get_data(day=3, year=2020).splitlines()
from math import prod


# WRITE YOUR SOLUTION HERE
def count_tree_encountered(lines, right_slope, down_slope):
    return sum(
        [
            line[(right_slope * i) % len(line)] == "#"
            for i, line in enumerate(lines[::down_slope])
        ]
    )


def part_1(lines):
    return count_tree_encountered(lines, 3, 1)


def part_2(lines):
    return prod(
        [
            count_tree_encountered(lines, s1, s2)
            for (s1, s2) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
