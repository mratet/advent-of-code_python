from enum import Enum

from aocd import get_data
from heapq import heappop, heappush

input = get_data(day=22, year=2018).splitlines()

TOOLS = ["TORCH", "CLIMBING_GEAR", "NEITHER"]


class Region(Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2


FORBIDDEN_TOOLS = {
    Region.ROCKY.value: "NEITHER",
    Region.WET.value: "TORCH",
    Region.NARROW.value: "CLIMBING_GEAR",
}


def parse_input(lines):
    depth = int(lines[0].split(": ")[1])
    X, Y = map(int, lines[1].split(": ")[1].split(","))
    return depth, X, Y


def get_erosion_grid(X, Y, depth, target):
    erosion_grid = {}
    for x in range(X + 1):
        for y in range(Y + 1):
            if (x, y) == (0, 0):
                index_geologique = 0
            elif (x, y) == target:
                index_geologique = 0
            elif y == 0:
                index_geologique = x * 16807
            elif x == 0:
                index_geologique = y * 48271
            else:
                index_geologique = erosion_grid[(x - 1, y)] * erosion_grid[(x, y - 1)]
            erosion_grid[(x, y)] = (index_geologique + depth) % 20183
    return erosion_grid


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    depth, X, Y = parse_input(lines)
    region_map = get_erosion_grid(X, Y, depth, (X, Y))
    return sum(region_map[(x, y)] % 3 for x in range(X + 1) for y in range(Y + 1))


def part_2(lines):
    depth, X, Y = parse_input(lines)
    erosion_grid = get_erosion_grid(1000, 1000, depth, (X, Y))

    source = (0, 0, "TORCH")
    target = (X, Y, "TORCH")

    heap = [(0, source)]
    dist = {source: 0}

    while heap:
        dist_node, node = heappop(heap)
        if dist_node > dist[node]:
            continue

        if node == target:
            return dist_node

        x, y, t = node
        neighbors = [(x, y, tool) for tool in TOOLS if tool is not t] + [
            (x + dx, y + dy, t) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
        ]
        for neighbor in neighbors:
            (nx, ny, nt) = neighbor
            if nx < 0 or ny < 0:
                continue

            if nt == FORBIDDEN_TOOLS[erosion_grid[(nx, ny)] % 3]:
                continue

            dist_neighbor = dist_node + (1 if nt == t else 7)
            if dist_neighbor < dist.get(neighbor, float("inf")):
                dist[neighbor] = dist_neighbor
                heappush(heap, (dist_neighbor, neighbor))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
