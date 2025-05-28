from collections import defaultdict
from heapq import heappush, heappop

from aocd import get_data

input = get_data(day=15, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    Y, X = len(lines), len(lines[0])
    graph = defaultdict(list)
    weights = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            weights[(x, y)] = int(c)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y:
                    graph[(x, y)].append((nx, ny))
    return graph, weights, X, Y


def extend_grid(lines):
    Y, X = len(lines), len(lines[0])
    final_grid = []
    for tile_y in range(5):
        for y in range(Y):
            row = []
            for tile_x in range(5):
                for x in range(X):
                    base_value = int(lines[y][x])
                    new_value = ((base_value - 1 + tile_x + tile_y) % 9) + 1
                    row.append(str(new_value))
            final_grid.append("".join(row))
    return final_grid


def dijkstra(graph, weights, source, target=None):
    dist = {k: float("inf") for k in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)
        if node == target:
            break
        for neighbor in graph[node]:
            dist_neighbor = dist_node + weights[neighbor]
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                heappush(heap, (dist_neighbor, neighbor))
    return dist


def part_1(lines):
    graph, weights, X, Y = parse_input(lines)
    start, end = (0, 0), (X - 1, Y - 1)
    dist = dijkstra(graph, weights, source=start, target=end)
    return dist[end]


def part_2(lines):
    extended_grid = extend_grid(lines)
    graph, weights, X, Y = parse_input(extended_grid)
    start, end = (0, 0), (X - 1, Y - 1)
    dist = dijkstra(graph, weights, source=start, target=end)
    return dist[end]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
