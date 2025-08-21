from aocd import get_data
from itertools import product

aoc_input = get_data(day=24, year=2019).splitlines()

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

RECURSION_LIMIT = 100
OUT_RECURSION = {(0, 1): (2, 3), (0, -1): (2, 1), (1, 0): (3, 2), (-1, 0): (1, 2)}


# WRITE YOUR SOLUTION HERE
def _parse_input(lines, part="part_1"):
    bugs = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            bugs[(0, y, x)] = lines[y][x]
    if part == "part_2":
        for d in range(-RECURSION_LIMIT, RECURSION_LIMIT):
            if d == 0:
                continue
            for x, y in product(range(5), repeat=2):
                bugs[(d, x, y)] = "."
    return bugs


def get_neighbors(node, part="part_1"):
    d, x, y = node
    if part == "part_1":
        return [(0, x + dx, y + dy) for (dx, dy) in DIRS]

    if (x, y) == (2, 2):
        return []
    neighbors = []
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if (nx, ny) == (2, 2):
            if (x, y) == (2, 1):
                neighbors += [(d - 1, x, 0) for x in range(5)]
            elif (x, y) == (2, 3):
                neighbors += [(d - 1, x, 4) for x in range(5)]
            elif (x, y) == (3, 2):
                neighbors += [(d - 1, 4, y) for y in range(5)]
            elif (x, y) == (1, 2):
                neighbors += [(d - 1, 0, y) for y in range(5)]
            continue

        if not (0 <= nx < 5 and 0 <= ny < 5):
            nx, ny = OUT_RECURSION[(dx, dy)]
            neighbors.append((d + 1, nx, ny))
            continue

        neighbors.append((d, nx, ny))
    return neighbors


def get_next_state(bugs, part="part_1"):
    new_grid = {}
    for node, symb in bugs.items():
        neighbors = get_neighbors(node, part=part)
        count = sum(bugs.get(neighbor, ".") == "#" for neighbor in neighbors)
        if symb == "#":
            new_grid[node] = "#" if count == 1 else "."
        elif symb == ".":
            new_grid[node] = "#" if count in (1, 2) else "."
    return new_grid


def compute_diversity(bugs):
    bug_order = sorted(bugs.keys())
    return sum(2**i for i, node in enumerate(bug_order) if bugs[node] == "#")


def part_1(lines):
    bugs = _parse_input(lines)
    seen = set()
    while True:
        if tuple(bugs.items()) in seen:
            return compute_diversity(bugs)
        seen.add(tuple(bugs.items()))
        next_bugs = get_next_state(bugs, "part_1")
        bugs = next_bugs


def part_2(lines):
    bugs = _parse_input(lines, "part_2")
    for _ in range(200):
        bugs = get_next_state(bugs, "part_2")
    return sum(c == "#" for c in bugs.values())


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
