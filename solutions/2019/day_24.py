from aocd import get_data

aoc_input = get_data(day=24, year=2019).splitlines()

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
OUT_RECURSION = {(0, 1): (2, 3), (0, -1): (2, 1), (1, 0): (3, 2), (-1, 0): (1, 2)}


# WRITE YOUR SOLUTION HERE
def _parse_input(lines):
    return {(0, row, col) for row in range(len(lines)) for col in range(len(lines[0])) if lines[row][col] == "#"}


def get_neighbors(node, part="part_1"):
    d, row, col = node
    if part == "part_1":
        return [(0, row + drow, col + dcol) for drow, dcol in DIRS]

    if (row, col) == (2, 2):
        return []
    neighbors = []
    for drow, dcol in DIRS:
        nrow, ncol = row + drow, col + dcol
        if (nrow, ncol) == (2, 2):
            if (row, col) == (2, 1):
                neighbors += [(d - 1, i, 0) for i in range(5)]
            elif (row, col) == (2, 3):
                neighbors += [(d - 1, i, 4) for i in range(5)]
            elif (row, col) == (3, 2):
                neighbors += [(d - 1, 4, i) for i in range(5)]
            elif (row, col) == (1, 2):
                neighbors += [(d - 1, 0, i) for i in range(5)]
            continue

        if not (0 <= nrow < 5 and 0 <= ncol < 5):
            nrow, ncol = OUT_RECURSION[(drow, dcol)]
            neighbors.append((d + 1, nrow, ncol))
            continue

        neighbors.append((d, nrow, ncol))
    return neighbors


def get_next_state(bugs, part="part_1"):
    if part == "part_1":
        candidates = {(0, row, col) for row in range(5) for col in range(5)}
    else:
        candidates = bugs | {n for node in bugs for n in get_neighbors(node, part=part)}

    new_bugs = set()
    for node in candidates:
        neighbors = get_neighbors(node, part=part)
        count = sum(1 for n in neighbors if n in bugs)
        is_bug = node in bugs
        if (is_bug and count == 1) or (not is_bug and count in (1, 2)):
            new_bugs.add(node)
    return new_bugs


def compute_diversity(bugs):
    return sum(2 ** (row * 5 + col) for _, row, col in bugs)


def part_1(lines):
    bugs = _parse_input(lines)
    seen = set()
    while True:
        state = frozenset(bugs)
        if state in seen:
            return compute_diversity(bugs)
        seen.add(state)
        bugs = get_next_state(bugs, "part_1")


def part_2(lines):
    bugs = _parse_input(lines)
    for _ in range(200):
        bugs = get_next_state(bugs, "part_2")
    return len(bugs)


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
