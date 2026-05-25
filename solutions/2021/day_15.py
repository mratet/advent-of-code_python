from heapq import heappop, heappush

from aocd import get_data

input = get_data(day=15, year=2021).splitlines()

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    rows, cols = len(lines), len(lines[0])
    weights = {(x, y): int(c) for y, line in enumerate(lines) for x, c in enumerate(line)}
    return weights, (cols - 1, rows - 1)


def extend_grid(lines):
    rows, cols = len(lines), len(lines[0])
    weights = {
        (x + tile_x * cols, y + tile_y * rows): ((int(lines[y][x]) - 1 + tile_x + tile_y) % 9) + 1
        for tile_y in range(5)
        for y in range(rows)
        for tile_x in range(5)
        for x in range(cols)
    }
    return weights, (cols * 5 - 1, rows * 5 - 1)


def dijkstra(weights, target):
    dist = {}
    heap = [(0, (0, 0))]
    while heap:
        d, node = heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        if node == target:
            return d
        x, y = node
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in weights and (nx, ny) not in dist:
                heappush(heap, (d + weights[(nx, ny)], (nx, ny)))


def part_1(lines):
    return dijkstra(*parse_input(lines))


def part_2(lines):
    return dijkstra(*extend_grid(lines))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
