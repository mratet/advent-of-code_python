import re

from aocd import get_data

input = get_data(day=4, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    return [
        (range(x1, x2 + 1), range(y1, y2 + 1))
        for line in lines
        for x1, x2, y1, y2 in [tuple(map(int, re.findall(r"\d+", line)))]
    ]


def solve(lines, part="part_1"):
    pairs = parse_input(lines)
    if part == "part_1":
        return sum(set(p1).issubset(p2) or set(p2).issubset(p1) for p1, p2 in pairs)
    return sum(bool(set(p1) & set(p2)) for p1, p2 in pairs)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
