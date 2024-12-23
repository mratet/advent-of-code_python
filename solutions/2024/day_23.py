# from aocd import get_data, submit
# input = get_data(day=23, year=2024).splitlines()
from collections import defaultdict
from itertools import combinations
input = open('input.txt').read().splitlines()
computers = set()
graph = defaultdict(list)

for line in input:
    l, r = line.split('-')
    computers.update({l, r})
    graph[l].append(r)
    graph[r].append(l)

owners = {c for c in graph if c[0] == 't'}
triplets = set()
for owner in owners:
    for c1, c2 in combinations(graph[owner], 2):
        if c1 in graph[c2]:
            triplets.add(frozenset([owner, c1, c2]))

print(len(triplets))

C = defaultdict(set)
# Voir find_cliques de NetworkX
def bron_kerbosch(R, P, X):
    if not P and not X :
        C[len(R)].add(frozenset(R))
    for v in P.union(set([])):
        bron_kerbosch(R.union({v}), P.intersection(set(graph[v])), X.intersection(set(graph[v])))
        P.remove(v)
        X.add(v)

bron_kerbosch(set(), computers, set())
print(','.join(sorted(list(C[max(C)].pop()))))




# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return

def part_2(lines):
    return
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
