import collections
import itertools

from aocd import get_data

input = get_data(day=24, year=2016).splitlines()

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def _parse_input(input):
    open_tiles, targets = set(), {}
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c != "#":
                open_tiles.add((j, i))
                if c.isdigit():
                    targets[(j, i)] = c
    return open_tiles, targets


def bfs_distances(start, targets, open_tiles):
    distances = {}
    visited = {start}
    queue = collections.deque([(start, 0)])
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) in targets:
            distances[targets[(x, y)]] = dist
        for dx, dy in dirs:
            neighbor = (x + dx, y + dy)
            if neighbor in open_tiles and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return distances


def build_graph(open_tiles, targets):
    return {label: bfs_distances(pos, targets, open_tiles) for pos, label in targets.items()}


def solve(input, part="part_1"):
    open_tiles, targets = _parse_input(input)
    graph = build_graph(open_tiles, targets)
    nodes = [label for label in graph if label != "0"]
    return min(
        sum(graph[i][j] for i, j in itertools.pairwise(("0", *perm, *(("0",) if part == "part_2" else ()))))
        for perm in itertools.permutations(nodes)
    )


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
