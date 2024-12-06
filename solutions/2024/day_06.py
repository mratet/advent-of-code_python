from aocd import get_data
input = get_data(day=6, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
def get_guard_path(obstacles, start, lines):
    path = {start}
    gi, gj = start
    par_path = {(gi, gj, 0)}
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = 0
    n, m = len(lines), len(lines[0])
    while  0 <= gi < n and 0 <= gj < m :
        di, dj = direction[idx]
        ni, nj = gi + di, gj + dj
        if (ni, nj) not in obstacles:
            gi, gj = ni, nj
            path.add((gi, gj))
            if (gi, gj, idx) in par_path:
                return False
            else:
                par_path.add((gi, gj, idx))
        else:
            idx = (idx + 1) % 4
    return path

def part_1(lines):
    obstacles = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                obstacles.add((i, j))
            elif c == '^':
                gi, gj = i, j
    path = get_guard_path(obstacles, (gi, gj), lines)
    return len(path) - 1

def part_2(lines):
    obstacles = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                obstacles.add((i, j))
            elif c == '^':
                gi, gj = i, j

    cnt = 0
    path = get_guard_path(obstacles, (gi, gj), lines)
    for pos in path:
        obstacles.add(pos)
        if not get_guard_path(obstacles, (gi, gj), lines):
            cnt += 1
        obstacles.remove(pos)

    return cnt
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
