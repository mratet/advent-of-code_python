from aocd import get_data

input = get_data(day=23, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
dirs = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def _parse(grid):
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] != "#"
                ):
                    neighbors += 1
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

            direction = (
                dirs[grid[r][c]]
                if part == "part_1"
                else [(-1, 0), (0, 1), (1, 0), (0, -1)]
            )

            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] != "#"
                    and (nr, nc) not in seen
                ):
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))
    return graph


def part_1(input):
    # taken from hyper-neutrino
    start, end, points = _parse(input)
    graph = graph_construction(points, input, "part_1")

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    return dfs(start)


def part_2(input):
    start, end, points = _parse(input)
    graph = graph_construction(points, input, "part_2")

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    return dfs(start)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
