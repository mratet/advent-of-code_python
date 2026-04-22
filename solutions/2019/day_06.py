from collections import defaultdict

from aocd import get_data

input = get_data(day=6, year=2019).splitlines()


def compute_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        l, r = line.split(")")
        graph[l].append(r)
        graph[r].append(l)
    return graph


def compute_distances(graph, start):
    dist = {}

    def dfs(s, d):
        if s in dist:
            return
        dist[s] = d
        for n in graph[s]:
            dfs(n, d + 1)

    dfs(start, 0)
    return dist


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    graph = compute_graph(lines)
    return sum(compute_distances(graph, "COM").values())


def part_2(lines):
    graph = compute_graph(lines)
    return compute_distances(graph, "YOU")["SAN"] - 2


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
