from aocd import get_data

input = get_data(day=12, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def build_graph(lines):
    graph = {}
    for line in lines:
        left, right = line.split(" <-> ")
        node = int(left)
        graph[node] = list(map(int, right.split(", ")))
    return graph


def dfs(node, graph, visited):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, graph, visited)


def compute_connected_components(graph):
    nodes = set(graph)
    connected_components = []
    while nodes:
        visited = set()
        N = nodes.pop()
        dfs(N, graph, visited)
        connected_components.append(visited)
        nodes = nodes - visited
    return connected_components


def part_1(lines):
    graph = build_graph(lines)
    cc = compute_connected_components(graph)
    return next(len(c) for c in cc if 0 in c)


def part_2(lines):
    graph = build_graph(lines)
    cc = compute_connected_components(graph)
    return len(cc)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
