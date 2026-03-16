from itertools import combinations
from disjoint_set import DisjointSet

from aocd import get_data
from math import dist

STEPS = 1000

input = get_data(day=8, year=2025).splitlines()

# WRITE YOUR SOLUTION HERE
def parse_coords(lines):
    return [tuple(map(int, line.split(','))) for line in lines]

def compute_sorted_distances(coords):
    return sorted([
        (dist(coords[i], coords[j]), i, j)
        for i, j in combinations(range(len(coords)), 2)
    ], key=lambda x: x[0])

def part_1(lines):
    coords = parse_coords(lines)
    dists = compute_sorted_distances(coords)

    ds = DisjointSet()

    for _, i, j in dists[:STEPS]:
        ds.union(i, j)

    sizes = sorted([len(component) for component in ds.itersets()])
    return sizes[-1] * sizes[-2] * sizes[-3]

def part_2(lines):
    coords = parse_coords(lines)
    dists = compute_sorted_distances(coords)

    ds = DisjointSet()
    for _, i, j in dists:
        ds.union(i, j)

        if len(list(ds)) == len(coords):
            x1, _, _ = coords[i]
            x2, _, _ = coords[j]
            return x1 * x2

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
