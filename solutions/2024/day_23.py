from collections import defaultdict
from itertools import combinations

from aocd import get_data

input = get_data(day=23, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    graph = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)
    return graph


def part_1(lines):
    graph = parse_input(lines)
    triplets = set()
    for owner in (c for c in graph if c[0] == "t"):
        for c1, c2 in combinations(graph[owner], 2):
            if c1 in graph[c2]:
                triplets.add(frozenset({owner, c1, c2}))
    return len(triplets)


def part_2(lines):
    graph = parse_input(lines)
    max_clique = set()

    def bron_kerbosch(R, P, X):
        nonlocal max_clique
        if not P and not X:
            if len(R) > len(max_clique):
                max_clique = R
            return
        for v in set(P):
            bron_kerbosch(R | {v}, P & graph[v], X & graph[v])
            P.remove(v)
            X.add(v)

    bron_kerbosch(set(), set(graph), set())
    return ",".join(sorted(max_clique))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
