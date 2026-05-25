from itertools import combinations, pairwise

from aocd import get_data

input = get_data(day=2, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    return [[int(n) for n in line.split()] for line in lines]


def is_safe_level(level):
    diffs = [b - a for a, b in pairwise(level)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def part_1(lines):
    return sum(is_safe_level(level) for level in parse_input(lines))


def part_2(lines):
    return sum(any(map(is_safe_level, combinations(level, len(level) - 1))) for level in parse_input(lines))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
