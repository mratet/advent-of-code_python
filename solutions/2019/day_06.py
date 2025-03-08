
from collections import defaultdict
from aocd import get_data, submit
input = get_data(day=6, year=2019).splitlines()
# WRITE YOUR SOLUTION HERE
def part_1(lines):
    graph = {r: l for l, r in (line.split(')') for line in lines)}
    dfs = lambda s : 0 if s == 'COM' else 1 + dfs(graph[s])
    return sum(dfs(n) for n in graph)

def compute_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        l, r = line.split(')')
        graph[l].append(r)
        graph[r].append(l)
    return graph

def part_2(lines):
    graph = compute_graph(lines)
    dist = {}
    def dfs(s, d):
        if s in dist: return
        dist[s] = d
        for n in graph[s]:
            dfs(n, d + 1)

    dfs('YOU', 0)
    return dist["SAN"] - 2

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

