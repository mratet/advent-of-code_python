from collections import defaultdict
from aocd import get_data

input = get_data(day=6, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def get_guard_path(obstacles, start, lines):
    path = defaultdict(list)
    path[start].append(0)
    gi, gj = start
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = 0
    n, m = len(lines), len(lines[0])
    while 0 <= gi < n and 0 <= gj < m:
        di, dj = direction[idx]
        ni, nj = gi + di, gj + dj
        if (ni, nj) not in obstacles:
            gi, gj = ni, nj
            if idx in path.get((gi, gj), []):
                return False
            path[(gi, gj)].append(idx)
        else:
            idx = (idx + 1) % 4
    return path


def parse_input(lines):
    obstacles = set()
    start = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                obstacles.add((i, j))
            elif c == "^":
                start = (i, j)
    return obstacles, start


def part_1(lines):
    obstacles, start = parse_input(lines)
    path = get_guard_path(obstacles, start, lines)
    return len(path) - 1


def part_2(lines):
    obstacles, start = parse_input(lines)
    cnt = 0
    path = get_guard_path(obstacles, start, lines)
    for pos in path:
        obstacles.add(pos)
        if not get_guard_path(obstacles, start, lines):
            cnt += 1
        obstacles.remove(pos)
    return cnt


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
