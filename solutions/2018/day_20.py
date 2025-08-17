from collections import defaultdict, deque

from aocd import get_data

input = get_data(day=20, year=2018)

DIRECTIONS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def bfs(start, graph):
    to_visit = deque()
    dist = {start: 0}
    to_visit.append(start)

    while to_visit:
        node = to_visit.pop()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                to_visit.appendleft(neighbor)

    return dist


# WRITE YOUR SOLUTION HERE
def parse_regex(regex_input):
    regex = regex_input[1:-1]
    graph = defaultdict(set)
    positions = {(0, 0)}
    stack = []

    for char in regex:
        if char in DIRECTIONS:
            dx, dy = DIRECTIONS[char]
            new_positions = set()
            for x, y in positions:
                nx, ny = x + dx, y + dy
                graph[(x, y)].add((nx, ny))
                graph[(nx, ny)].add((x, y))
                new_positions.add((nx, ny))
            positions = new_positions

        elif char == "(":
            stack.append((positions, set()))

        elif char == "|":
            start_positions, collected_end_positions = stack[-1]
            collected_end_positions.update(positions)
            positions = start_positions

        elif char == ")":
            start_positions, collected_end_positions = stack.pop()
            collected_end_positions.update(positions)
            positions = collected_end_positions

    return graph


def part_1(input_regex):
    graph = parse_regex(input_regex)
    dist = bfs((0, 0), graph)
    return max(dist.values())


def part_2(input_regex):
    graph = parse_regex(input_regex)
    dist = bfs((0, 0), graph)
    return sum(c >= 1000 for c in dist.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
