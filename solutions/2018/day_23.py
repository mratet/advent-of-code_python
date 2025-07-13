from aocd import get_data
import re

input = get_data(day=23, year=2018).splitlines()


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def parse_input(lines):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    nanobots = parse_input(lines)
    max_nanobot = max(nanobots, key=lambda x: x[3])
    return sum(
        manhattan_distance(max_nanobot, nanobot) <= max_nanobot[3] for nanobot in nanobots
    )


def part_2(lines):
    # Have a look at Sweep Line
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
