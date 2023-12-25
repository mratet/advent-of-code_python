import collections
import graphviz
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
def _parse(input):
    graph = collections.defaultdict(list)
    dot = graphviz.Graph(engine='neato')
    for line in input:
        parent, child = line.split(':')
        for node in child.split():
            if (parent, node) in (('lmg', 'krx'), ('vzb', 'tnr'), ('tqn', 'tvf')):
                continue
            graph[parent].append(node)
            graph[node].append(parent)
            dot.edge(node, parent)
            dot.edge(parent, node)
    return graph, dot

def dfs(graph, start):
    q = [start]
    visited = set()
    visited.add(start)

    while q:
        node = q.pop()
        for neighboor in graph[node]:
            if neighboor not in visited:
                q.append(neighboor)
                visited.add(neighboor)

    return len(visited)

def part_1(lines):
    graph, g = _parse(lines)
    n = len(graph)
    m = dfs(graph, 'ddp')
    p = dfs(graph, 'stz')
    assert n == m + p
    return m * p

def part_2(lines):
    return 0
# END OF SOLUTION


# test_input = open('input-test.txt').read().splitlines()
# test_lines = []
# for i, line in enumerate(test_input[3:]):
#     if line[0] == '-':
#         break
#     test_lines.append(line)
# solution = test_input[i + 4]
#
# print(f'My answer on test set for the first problem is {part_1(test_lines)}')
# print(solution)
print(f'My answer is {part_1(lines)}')

# print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')
