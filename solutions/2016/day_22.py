import itertools
import re
from collections import defaultdict

from aocd import get_data

input = get_data(day=22, year=2016).splitlines()


def _parse_input(input):
    storage = {}
    for line in input[2:]:
        pattern = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T*"
        X, Y, size, used = map(int, re.findall(pattern, line)[0])
        storage[(X, Y)] = (size, used)
    return storage


def part_1(input):
    storage = _parse_input(input)
    t = 0
    for n1, n2 in itertools.product(storage, storage):
        s1, u1 = storage[n1]
        s2, u2 = storage[n2]
        if u1 > 0 and n1 != n2 and u1 < s2 - u2:
            t += 1
    return t


def part_2(input):
    storage = _parse_input(input)
    max_x, max_y = max(storage)
    [start] = [node for node, (size, used) in storage.items() if used == 0]
    walls = [node for node, (size, used) in storage.items() if size > 200]

    end = (max_x - 1, 0)
    queue = [(start, 0)]
    visited = {start}
    while queue:
        node, steps_to_move_empty_node = queue.pop(0)
        if node == end:
            return steps_to_move_empty_node + 1 + 5 * (max_x - 1)
        x, y = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx <= max_x and 0 <= ny <= max_y): continue
            if (nx, ny) in walls or (nx, ny) in visited: continue
            visited.add((nx, ny))
            queue.append(((nx, ny), steps_to_move_empty_node + 1))
    return -1

print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
