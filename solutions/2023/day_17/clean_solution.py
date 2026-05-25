from heapq import heappop, heappush

from aocd import get_data

input = get_data(day=17, year=2023).splitlines()

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    return {(x, y): int(c) for y, line in enumerate(lines) for x, c in enumerate(line)}


def dijkstra(graph, source, target, part="part_1"):
    heap = [(0, source, E, -1)]
    visited = {}
    while heap:
        dist, node, direction, streak = heappop(heap)
        if node == target and (part == "part_1" or streak >= 4):
            return dist
        if (node, direction, streak) in visited:
            continue
        visited[(node, direction, streak)] = dist
        for new_dir in [N, S, W, E]:
            next_node = (node[0] + new_dir[0], node[1] + new_dir[1])
            new_streak = 1 if new_dir != direction else streak + 1
            not_reverse = direction[0] * new_dir[0] + direction[1] * new_dir[1] != -1
            if part == "part_2":
                is_valid = new_streak <= 10 and (new_dir == direction or streak >= 4 or streak == -1)
            else:
                is_valid = new_streak <= 3
            if next_node in graph and not_reverse and is_valid:
                heappush(heap, (dist + graph[next_node], next_node, new_dir, new_streak))


def solve(lines, part="part_1"):
    graph = parse_input(lines)
    n, m = len(lines), len(lines[0])
    return dijkstra(graph, (0, 0), (m - 1, n - 1), part)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
