from aocd import get_data
input = get_data(day=9, year=2015).splitlines()
import itertools
import collections
def _parse(lines):
    graph = collections.defaultdict(dict)
    for line in lines:
        start, _, end, _, distance = line.split()
        graph[start][end] = int(distance)
        graph[end][start] = int(distance)
    return graph

def part_1(input):
    weights = _parse(input)
    shortest_route = 1e9

    for perm in itertools.permutations(weights.keys()):
        path = sum([weights[i][j] for i, j in itertools.pairwise(perm)])
        shortest_route = min(shortest_route, path)

    return shortest_route


def part_2(input):
    weights = _parse(input)
    longest_route = 0

    for perm in itertools.permutations(weights.keys()):
        path = sum([weights[i][j] for i, j in itertools.pairwise(perm)])
        longest_route = max(longest_route, path)

    return longest_route

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
