from collections import defaultdict
from itertools import combinations

from aocd import get_data

input = get_data(day=8, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    antennas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                antennas[c].append((i, j))
    return antennas


def solve(lines, part="part_1"):
    antennas = parse_input(lines)
    n, m = len(lines), len(lines[0])
    antinodes = set()
    for positions in antennas.values():
        for p1, p2 in combinations(positions, 2):
            (x1, y1), (x2, y2) = p1, p2
            dx, dy = x2 - x1, y2 - y1
            ks = (-1, 2) if part == "part_1" else range(-(n + m), n + m)
            for k in ks:
                c = (x1 + k * dx, y1 + k * dy)
                if 0 <= c[0] < n and 0 <= c[1] < m:
                    antinodes.add(c)
    return len(antinodes)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
