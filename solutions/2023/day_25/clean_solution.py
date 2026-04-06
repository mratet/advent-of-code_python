import collections

import graphviz
from aocd import get_data

input = get_data(day=25, year=2023).splitlines()

CUTS = [("lmg", "krx"), ("vzb", "tnr"), ("tqn", "tvf")]


# WRITE YOUR SOLUTION HERE
def _parse(lines):
    graph = collections.defaultdict(list)
    for line in lines:
        parent, child = line.split(":")
        for node in child.split():
            graph[parent].append(node)
            graph[node].append(parent)
    return graph


def save_graph(graph, filename="graph_day25"):
    dot = graphviz.Graph(engine="neato")
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if node < neighbor:
                dot.edge(node, neighbor)
    dot.render(filename, format="png", cleanup=True)


def cut_edges(graph, cuts):
    for a, b in cuts:
        graph[a].remove(b)
        graph[b].remove(a)


def dfs(graph, start):
    q = [start]
    visited = {start}

    while q:
        node = q.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return len(visited)


def part_1(lines):
    graph = _parse(lines)
    # save_graph(graph)
    cut_edges(graph, CUTS)
    n = len(graph)
    m = dfs(graph, "ddp")
    p = dfs(graph, "stz")
    assert n == m + p
    return m * p


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
