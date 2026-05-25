from collections import defaultdict
from heapq import heappop, heappush

from aocd import get_data

input = get_data(day=16, year=2024).splitlines()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# WRITE YOUR SOLUTION HERE
def dijkstra(graph, source, target=None):
    prec = dict.fromkeys(graph)
    black = dict.fromkeys(graph, False)
    dist = dict.fromkeys(graph, float("inf"))
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                weight = 1 if neighbor[-1] == node[-1] else 1000
                dist_neighbor = dist_node + weight
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec


def construct_graph(lines):
    graph = defaultdict(list)
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            c = lines[x][y]
            if c != "#":
                for i in range(len(DIRS)):
                    graph[(x, y, i)].append((x, y, (i + 1) % 4))
                    graph[(x, y, i)].append((x, y, (i - 1) % 4))
                    nx, ny = x + DIRS[i][0], y + DIRS[i][1]
                    if lines[nx][ny] != "#":
                        graph[(x, y, i)].append((nx, ny, i))
                if c == "E":
                    target = x, y
                if c == "S":
                    source = x, y
    return graph, source, target


def part_1(lines):
    graph, (sx, sy), (tx, ty) = construct_graph(lines)
    dist, prec = dijkstra(graph, source=(sx, sy, 0))
    return min(dist[tx, ty, i] for i in range(4))


def get_path(dist, prec, node, seen):
    while True:
        if node in seen:
            return seen
        seen.add((node[0], node[1], dist[node]))
        node = prec[node]


def part_2(lines):
    graph, (sx, sy), (tx, ty) = construct_graph(lines)
    dist, prec = dijkstra(graph, source=(sx, sy, 0))
    _, final_dir = min((dist[tx, ty, i], i) for i in range(4))
    seen = get_path(dist, prec, (tx, ty, final_dir), {(sx, sy, 0)})
    for (x, y, d), _ in dist.items():
        dx, dy = DIRS[d]
        if (x + dx, y + dy, dist[(x, y, d)] + 1) in seen:
            cand = get_path(dist, prec, (x, y, d), seen)
            seen.update(cand)
    return len({(x, y) for (x, y, _) in seen})


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
