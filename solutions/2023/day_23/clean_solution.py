from functools import cache

from aocd import get_data

input = get_data(day=23, year=2023).splitlines()

dirs = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

# WRITE YOUR SOLUTION HERE


def parse_input(grid):
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))
    points = [start, end]
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = sum(
                1
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#"
            )
            if neighbors >= 3:
                points.append((r, c))
    return start, end, points


def graph_construction(points, grid, part):
    graph = {pt: {} for pt in points}
    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}
        while stack:
            n, r, c = stack.pop()
            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue
            direction = dirs[grid[r][c]] if part == "part_1" else [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))
    return graph


def solve(lines, part="part_1"):
    start, end, points = parse_input(lines)
    graph = graph_construction(points, lines, part)
    node_id = {pt: i for i, pt in enumerate(points)}
    adj = [[(node_id[nx], d) for nx, d in graph[pt].items()] for pt in points]
    start_id, end_id = node_id[start], node_id[end]

    @cache
    def dfs(node, seen):
        if node == end_id:
            return 0
        m = -float("inf")
        for nx, dist in adj[node]:
            if not seen & (1 << nx):
                m = max(m, dfs(nx, seen | (1 << nx)) + dist)
        return m

    return dfs(start_id, 1 << start_id)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
