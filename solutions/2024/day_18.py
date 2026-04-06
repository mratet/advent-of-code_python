import re
from collections import defaultdict
from heapq import heappop, heappush

from aocd import get_data

input = get_data(day=18, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
X, Y = 71, 71


def dijkstra(graph, source, target=None):
    prec = dict.fromkeys(graph)
    black = dict.fromkeys(graph, False)
    dist = {k: float("inf") for k in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + 1
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec


def construct_grid(lines, i_max):
    grid = [["." for _ in range(X)] for _ in range(Y)]
    for line in lines[:i_max]:
        y, x = map(int, re.findall(r"-?\d+", line))
        grid[x][y] = "#"
    graph = defaultdict(list)
    for x in range(X):
        for y in range(Y):
            c = grid[x][y]
            if c != ".":
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y and grid[nx][ny] != "#":
                    graph[(x, y)].append((nx, ny))
    return graph


def part_1(lines):
    graph = construct_grid(lines, 1024)
    dist, prec = dijkstra(graph, (0, 0), (X - 1, Y - 1))
    return dist[(X - 1, Y - 1)]


def part_2(lines):
    l, r = 0, len(lines) - 1
    while l <= r:
        m = (l + r) // 2
        graph = construct_grid(lines, m)
        dist, prec = dijkstra(graph, (0, 0), (X - 1, Y - 1))
        if prec[(X - 1, Y - 1)]:
            l = m + 1
        else:
            r = m - 1
    return lines[m - 1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
