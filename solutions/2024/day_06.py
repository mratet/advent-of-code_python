from aocd import get_data

input = get_data(day=6, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
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


def get_guard_path(obstacles, start, lines):
    visited = {(*start, 0)}
    gi, gj = start
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = 0
    n, m = len(lines), len(lines[0])
    while 0 <= gi < n and 0 <= gj < m:
        di, dj = directions[idx]
        ni, nj = gi + di, gj + dj
        if (ni, nj) not in obstacles:
            gi, gj = ni, nj
            if 0 <= gi < n and 0 <= gj < m:
                state = (gi, gj, idx)
                if state in visited:
                    return False
                visited.add(state)
        else:
            idx = (idx + 1) % 4
    return {(gi, gj) for gi, gj, _ in visited}


def part_1(lines):
    obstacles, start = parse_input(lines)
    return len(get_guard_path(obstacles, start, lines))


def part_2(lines):
    obstacles, start = parse_input(lines)
    path = get_guard_path(obstacles, start, lines)
    count = 0
    for pos in path:
        obstacles.add(pos)
        if not get_guard_path(obstacles, start, lines):
            count += 1
        obstacles.remove(pos)
    return count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
