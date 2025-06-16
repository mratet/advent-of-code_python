import itertools
from functools import lru_cache
from aocd import get_data
from collections import deque
import re

input = get_data(day=16, year=2022)


def parse_input(lines):
    graph = {}

    for line in lines.splitlines():
        match = re.match(
            r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line
        )
        name, flow, neighbors = match.groups()
        graph[name] = {"flow": int(flow), "tunnels": [n for n in neighbors.split(", ")]}

    useful_valves = {name for name, props in graph.items() if props["flow"] > 0}
    return graph, useful_valves


def compute_distances(graph):
    """BFS to compute shortest path lengths between all pairs of valves."""
    dists = {}
    for start in graph:
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            node, dist = queue.popleft()
            dists[(start, node)] = dist
            for neighbor in graph[node]["tunnels"]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, dist + 1))
    return dists


def solve(graph, useful_valves, max_minutes=30):
    dists = compute_distances(graph)

    @lru_cache(maxsize=None)
    def dfs(current, time_left, unopened):
        best = 0
        for valve in unopened:
            travel_time = dists[(current, valve)] + 1  # 1 minute to open
            if time_left >= travel_time:
                remaining_time = time_left - travel_time
                gain = graph[valve]["flow"] * remaining_time
                best = max(
                    best,
                    gain + dfs(valve, remaining_time, frozenset(unopened - {valve})),
                )
        return best

    return dfs("AA", max_minutes, frozenset(useful_valves))


def generate_disjoint_partitions_7_8(elements):
    # We share the valves equally with the elephant
    all_partitions = []
    for subset_a in itertools.combinations(elements, 7):
        subset_b = tuple(sorted(set(elements) - set(subset_a)))
        all_partitions.append((tuple(sorted(subset_a)), subset_b))
    return all_partitions


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    graph, useful_valves = parse_input(lines)
    return solve(graph, useful_valves, max_minutes=30)


def part_2(lines):
    graph, useful_valves = parse_input(lines)
    max_minutes = 26
    return max(
        solve(graph, useful_valves=valves_1, max_minutes=max_minutes)
        + solve(graph, useful_valves=valves_2, max_minutes=max_minutes)
        for valves_1, valves_2 in generate_disjoint_partitions_7_8(useful_valves)
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
