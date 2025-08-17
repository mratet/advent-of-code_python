import itertools
from collections import defaultdict

from aocd import get_data

input = get_data(day=25, year=2018).splitlines()


def manhattan_distance(p1, p2):
    return sum(abs(p1c - p2c) for p1c, p2c in zip(p1, p2))


def parse_input(lines):
    points = []
    for line in lines:
        x, y, z, t = map(int, line.split(","))
        points.append((x, y, z, t))
    return points


def dfs(start_node, graph, visited):
    stack = [start_node]
    visited.add(start_node)

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


def get_graph(points):
    graph = defaultdict(list)
    for p1, p2 in itertools.combinations(points, 2):
        if manhattan_distance(p1, p2) <= 3:
            graph[p1].append(p2)
            graph[p2].append(p1)
    return graph


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    points = parse_input(lines)
    graph = get_graph(points)
    constellation_count = 0
    seen = set()
    for point in points:
        if point not in seen:
            constellation_count += 1
            dfs(point, graph, seen)

    return constellation_count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f"My answer is {part_2(input)}")
