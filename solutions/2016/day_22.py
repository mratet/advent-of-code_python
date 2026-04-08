import itertools
import re
from collections import deque

from aocd import get_data

input = get_data(day=22, year=2016).splitlines()


def _parse_input(input):
    storage = {}
    for line in input[2:]:
        X, Y, size, used, _, _ = map(int, re.findall(r"\d+", line))
        storage[(X, Y)] = (size, used)
    return storage


def part_1(input):
    storage = _parse_input(input)
    return sum(u1 > 0 and u1 < s2 - u2 for (s1, u1), (s2, u2) in itertools.permutations(storage.values(), 2))


def part_2(input):
    storage = _parse_input(input)
    max_x, max_y = max(storage)
    [start] = [node for node, (size, used) in storage.items() if used == 0]
    # Nodes with size > 200T are immovable walls that block the empty node
    walls = {node for node, (size, used) in storage.items() if size > 200}

    # BFS to move the empty node next to (max_x, 0)
    end = (max_x - 1, 0)
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            # 1 step to swap empty with goal, then 5 steps per shift to move goal left
            return dist + 1 + 5 * (max_x - 1)
        x, y = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx <= max_x and 0 <= ny <= max_y):
                continue
            if (nx, ny) in walls or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            queue.append(((nx, ny), dist + 1))
    return -1


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
