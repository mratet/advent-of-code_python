import re
from collections import deque

from aocd import get_data

input = get_data(day=16, year=2022)


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    graph = {}
    for line in lines.splitlines():
        name, flow, neighbors = re.findall(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)[0]
        graph[name] = {"flow": int(flow), "tunnels": neighbors.split(", ")}
    useful_valves = {name for name, props in graph.items() if int(props["flow"]) > 0}
    return graph, useful_valves


def compute_distances(graph):
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


def compute_all_scores(graph, useful_valves, max_minutes):
    dists = compute_distances(graph)
    valve_idx = {v: 1 << i for i, v in enumerate(useful_valves)}
    scores = {}

    def dfs(current, time_left, opened, pressure):
        scores[opened] = max(scores.get(opened, 0), pressure)
        for valve in useful_valves:
            bit = valve_idx[valve]
            if opened & bit:
                continue
            travel_time = dists[(current, valve)] + 1
            if time_left >= travel_time:
                remaining_time = time_left - travel_time
                dfs(valve, remaining_time, opened | bit, pressure + graph[valve]["flow"] * remaining_time)

    dfs("AA", max_minutes, 0, 0)
    return scores


def solve(lines, part="part_1"):
    graph, useful_valves = parse_input(lines)
    if part == "part_1":
        return max(compute_all_scores(graph, useful_valves, 30).values())
    scores = compute_all_scores(graph, useful_valves, 26)
    return max(v1 + v2 for s1, v1 in scores.items() for s2, v2 in scores.items() if not s1 & s2)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
