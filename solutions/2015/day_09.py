from aocd import get_data
input = get_data(day=9, year=2015).splitlines()
import itertools

def _parse(lines):
    nodes_id = []
    for line in lines:
        start, _, end, *_ = line.split()
        if start not in nodes_id:
            nodes_id.append(start)
        if end not in nodes_id:
            nodes_id.append(end)

    n = len(nodes_id)
    weights = [[0]*n for _ in range(n)]
    for line in lines:
        start, _, end, _ , distance = line.split()
        start_id, end_id = nodes_id.index(start), nodes_id.index(end)
        weights[start_id][end_id] = int(distance)
        weights[end_id][start_id] = int(distance)

    return weights

def part_1(input):
    weights = _parse(input)

    n = len(weights)
    V = range(n)
    shortest_route = 1e9

    for perm in itertools.permutations(V, n):
        path = 0
        for i, j in zip(perm, perm[1:]):
            path += weights[i][j]
        shortest_route = min(shortest_route, path)

    return shortest_route


def part_2(input):
    weights = _parse(input)

    n = len(weights)
    V = range(n)
    longest_route = 0

    for perm in itertools.permutations(V, n):
        path = 0
        for i, j in zip(perm, perm[1:]):
            path += weights[i][j]
        longest_route = max(longest_route, path)

    return longest_route

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
