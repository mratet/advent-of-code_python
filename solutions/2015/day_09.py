import collections
import itertools

from aocd import get_data

input = get_data(day=9, year=2015).splitlines()


def _parse(lines):
    graph = collections.defaultdict(dict)
    for line in lines:
        start, _, end, _, distance = line.split()
        graph[start][end] = int(distance)
        graph[end][start] = int(distance)
    return graph


def solve(input, part="part_1"):
    weights = _parse(input)
    best_route_distance = 1e9 if part == "part_1" else 0
    comp_func = min if part == "part_1" else max

    for perm in itertools.permutations(weights.keys()):
        path = sum([weights[i][j] for i, j in itertools.pairwise(perm)])
        best_route_distance = comp_func(best_route_distance, path)

    return best_route_distance


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
