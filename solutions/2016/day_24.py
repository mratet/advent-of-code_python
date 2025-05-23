import itertools
import collections
from aocd import get_data

input = get_data(day=24, year=2016).splitlines()

N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
dirs = [N, E, S, W]


def _parse_input(input):
    maze, interest_coords = {}, {}
    n, m = len(input), len(input[0])
    for i, j in itertools.product(range(n), range(m)):
        c = input[i][j]
        if c == ".":
            maze[(j, i)] = "."
        elif c.isdigit():
            interest_coords[(j, i)] = c
            maze[(j, i)] = "."
    return maze, interest_coords


def return_distance(start, interest_coords, maze):
    res = [0] * len(interest_coords)
    visited = set()
    visited.add(start)
    q = collections.deque()
    q.append(start)
    dist = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) in interest_coords.keys():
                res[int(interest_coords[(x, y)])] = dist

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in maze and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        dist += 1
    return res


def graph_construction(maze, interest_coords):
    weights = collections.defaultdict(dict)
    for start, c in interest_coords.items():
        tab = return_distance(start, interest_coords, maze)
        for i, dist in enumerate(tab):
            weights[c][str(i)] = dist
            weights[str(i)][c] = dist
    return weights


def part_1(input):
    maze, interest_coords = _parse_input(input)
    graph = graph_construction(maze, interest_coords)

    l = [str(i) for i in range(len(interest_coords))]

    shortest_route = 1e9
    for perm in itertools.permutations(l):
        if perm[0] == "0":
            # if perm[0] == '0' and perm[-1] == '0':
            path = sum([graph[i][j] for i, j in itertools.pairwise(perm)])
            shortest_route = min(shortest_route, path)
    return shortest_route


def part_2(input):
    maze, interest_coords = _parse_input(input)
    graph = graph_construction(maze, interest_coords)

    l = [str(i) for i in range(len(interest_coords))]
    l.append("0")

    shortest_route = 1e9
    for perm in itertools.permutations(l):
        if perm[0] == "0" and perm[-1] == "0":
            path = sum([graph[i][j] for i, j in itertools.pairwise(perm)])
            shortest_route = min(shortest_route, path)
    return shortest_route


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
