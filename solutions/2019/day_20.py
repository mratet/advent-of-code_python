from collections import defaultdict

from aocd import get_data

aoc_input = get_data(day=20, year=2019).splitlines()
from heapq import heappop, heappush

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


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


def _parse_input(lines):
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
    return door, dots, (min_x, max_x, min_y, max_y)


def compute_shortcuts(door, dots, extreme_coords):
    shortcuts = defaultdict(dict)
    min_x, max_x, min_y, max_y = extreme_coords
    for (x, y), symb in door.items():
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
    return start, end, shortcuts


def build_graph(door, dots, extreme_coords, part="part_1"):
    start, end, shortcuts = compute_shortcuts(door, dots, extreme_coords)

    start = (0, *start)
    end = (0, *end)
    DEPTH = 1 if part == "part_1" else 30
    teleportation_on = part == "part_2"

    graph = defaultdict(list)
    for depth in range(DEPTH):
        for x, y in dots:
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (nx, ny) in dots:
                    graph[(depth, x, y)].append((depth, nx, ny))
        for d in shortcuts.values():
            graph[(depth, *d["inner"])].append((depth + teleportation_on, *d["outer"]))
            graph[(depth + teleportation_on, *d["outer"])].append((depth, *d["inner"]))
    return start, end, graph


def part_1(lines):
    door, dots, extreme_coords = _parse_input(lines)
    start, end, graph = build_graph(door, dots, extreme_coords, "part_1")
    dist, prec = dijkstra(graph, start, end)
    return dist[end]


def part_2(lines):
    # To get faster results, you might need to modify dijkstra instead of precomputing a huge graph
    door, dots, extreme_coords = _parse_input(lines)
    start, end, graph = build_graph(door, dots, extreme_coords, "part_2")
    dist, prec = dijkstra(graph, start, end)
    return dist[end]


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
