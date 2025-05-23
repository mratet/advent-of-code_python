from collections import defaultdict

from aocd import get_data

aoc_input = get_data(day=20, year=2019).splitlines()
from heapq import heappop, heappush


# WRITE YOUR SOLUTION HERE
def dijkstra(graph, source=0, target=None):
    n = len(graph)
    prec = {k: None for k in graph}
    black = {k: False for k in graph}
    dist = {k: float("inf") for k in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)  # le sommet le plus proche
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


def part_1(lines):
    min_x, max_x, min_y, max_y = 1e9, 0, 1e9, 0
    dots = []
    door = {}
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            symb = lines[x][y]
            if symb == " " or symb == "#":
                continue
            if symb == ".":
                dots.append((x, y))
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
            else:
                door[(x, y)] = symb

    shortcuts = defaultdict(dict)
    for (x, y), symb in door.items():
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, (dx, dy) in enumerate(DIRS):
            nx, ny = x + dx, y + dy
            if (nx, ny) in dots:
                sx, sy = DIRS[(i + 2) % 4]
                pair_symb = door[(x + sx, y + sy)]
                shortcut_txt = "".join(sorted(symb + pair_symb))
                if shortcut_txt == "AA":
                    start = (nx, ny)
                elif shortcut_txt == "ZZ":
                    end = (nx, ny)
                else:
                    side = (
                        "inner"
                        if min_x <= x <= max_x and min_y <= y <= max_y
                        else "outer"
                    )
                    shortcuts[shortcut_txt][side] = (nx, ny)

    graph = defaultdict(list)
    for x, y in dots:
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in dots:
                graph[(x, y)].append((nx, ny))

    for d in shortcuts.values():
        graph[d["inner"]].append(d["outer"])
        graph[d["outer"]].append(d["inner"])

    dist, prec = dijkstra(graph, start, end)
    return dist[end]


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
