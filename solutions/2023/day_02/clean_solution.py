import collections
import math

from aocd import get_data

input = get_data(day=2, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(line):
    synthesis = collections.defaultdict(list)
    for game_set in line.split(":")[1].split(";"):
        for tirage in game_set.split(","):
            n, color = tirage.split()
            synthesis[color].append(int(n))
    return synthesis


def part_1(lines):
    max_values = {"red": 12, "green": 13, "blue": 14}
    return sum(
        i
        for i, line in enumerate(lines, start=1)
        for syn in [parse_input(line)]
        if all(max(syn[k], default=0) <= v for k, v in max_values.items())
    )


def part_2(lines):
    return sum(
        math.prod(max(syn[c]) for c in ("red", "green", "blue")) for line in lines for syn in [parse_input(line)]
    )


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
