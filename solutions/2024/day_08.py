from aocd import get_data

input = get_data(day=8, year=2024).splitlines()
from collections import defaultdict
from itertools import product


# WRITE YOUR SOLUTION HERE
def get_antenas(lines):
    antenas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                antenas[c].append((i, j))
    return antenas


def part_1(lines):
    antenas = get_antenas(lines)
    n, m = len(lines), len(lines[0])
    antinodes = set()
    for L in antenas.values():
        for l1, l2 in product(L, repeat=2):
            if l1 == l2:
                continue
            (x1, y1), (x2, y2) = l1, l2
            dx, dy = x2 - x1, y2 - y1
            c1, c2 = (x1 - dx, y1 - dy), (x2 + dx, y2 + dy)
            for c in (c1, c2):
                if 0 <= c[0] < n and 0 <= c[1] < m:
                    antinodes.add(c)
    return len(antinodes)


def part_2(lines):
    antenas = get_antenas(lines)
    n, m = len(lines), len(lines[0])
    antinodes = set()
    for L in antenas.values():
        for l1, l2 in product(L, repeat=2):
            (x1, y1), (x2, y2) = l1, l2
            # I test the whole line
            for idx in range(-50, 50):
                c = (x1 + idx * (x2 - x1), y1 + idx * (y2 - y1))
                if 0 <= c[0] < n and 0 <= c[1] < m:
                    antinodes.add(c)
    return len(antinodes)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
