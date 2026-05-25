from collections import deque

from aocd import get_data

input = get_data(day=18, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
N = 71


def parse_blocked(lines, count):
    blocked = set()
    for line in lines[:count]:
        col, row = map(int, line.split(","))
        blocked.add((row, col))
    return blocked


def bfs(blocked, source, target):
    visited = {source}
    queue = deque([(source, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        row, col = node
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_row, n_col = row + d_row, col + d_col
            neighbor = (n_row, n_col)
            if 0 <= n_row < N and 0 <= n_col < N and neighbor not in blocked and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return float("inf")


def part_1(lines):
    blocked = parse_blocked(lines, 1024)
    return bfs(blocked, (0, 0), (N - 1, N - 1))


def part_2(lines):
    l, r = 0, len(lines) - 1
    while l <= r:
        m = (l + r) // 2
        blocked = parse_blocked(lines, m)
        if bfs(blocked, (0, 0), (N - 1, N - 1)) != float("inf"):
            l = m + 1
        else:
            r = m - 1
    return lines[l - 1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
