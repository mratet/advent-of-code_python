from aocd import get_data, submit
input = get_data(day=8, year=2024).splitlines()
from collections import defaultdict
from itertools import product

# WRITE YOUR SOLUTION HERE
def get_antenas(lines):
    antenas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '.':
                antenas[c].append((i, j))
    return antenas

def part_1(lines):
    antenas = get_antenas(lines)

    n, m = len(lines), len(lines[0])
    antinodes = set()
    for L in antenas.values():
        for l1, l2 in product(L, repeat=2):
            if l1 == l2: continue
            (x1, y1), (x2, y2) = l1, l2
            c1, c2 = x1 - (x2 - x1), y1 - (y2 - y1)
            if 0 <= c1 < n and 0 <= c2 < m:
                antinodes.add((c1, c2))
            c1, c2 = x2 + (x2 - x1), y2 + (y2 - y1)
            if 0 <= c1 < n and 0 <= c2 < m:
                antinodes.add((c1, c2))
    return len(antinodes)

def part_2(lines):
    antenas = get_antenas(lines)

    n, m = len(lines), len(lines[0])
    antinodes = set()
    for L in antenas.values():
        for l1, l2 in product(L, repeat=2):
            if l1 == l2: continue
            (x1, y1), (x2, y2) = l1, l2
            idx = 1
            while 0 <= x1 - idx * (x2 - x1) < n and 0 <= y1 - idx * (y2 - y1) < m:
                antinodes.add((x1 - idx * (x2 - x1), y1 - idx * (y2 - y1)))
                idx += 1
            idx = 1
            while 0 <= x2 + idx * (x2 - x1) < n and 0 <= y2 + idx * (y2 - y1) < m:
                antinodes.add((x2 + idx * (x2 - x1), y2 + idx * (y2 - y1)))
                idx += 1
        if len(L) > 1:
            antinodes.update(set(L))
    return len(antinodes)

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

