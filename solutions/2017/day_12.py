from collections import defaultdict

from aocd import get_data

input = get_data(day=12, year=2017).splitlines()
import re


# WRITE YOUR SOLUTION HERE
def build_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        n1, *numb = list(map(int, re.findall(r"(\d+)", line)))
        for n2 in numb:
            graph[n1].append(n2)
            # graph[n2].append(n1)
    return graph


def compute_connected_components(graph):
    nodes = set(graph)
    connected_components = []
    while nodes:
        visited = set()

        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n in visited:
                    continue
                dfs(n)

        N = nodes.pop()
        dfs(N)
        connected_components.append(visited)
        nodes = nodes - visited
    return connected_components


def part_1(lines):
    graph = build_graph(lines)
    cc = compute_connected_components(graph)
    for c in cc:
        if 0 in c:
            return len(c)


def part_2(lines):
    graph = build_graph(lines)
    cc = compute_connected_components(graph)
    return len(cc)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
