from collections import deque, defaultdict
from string import ascii_lowercase, ascii_uppercase
from heapq import heappush, heappop
import math

from aocd import get_data

DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
START_KEYS = "0123@"
DIALS_ENTRANCE = {"0": (-1, -1), "1": (1, -1), "2": (-1, 1), "3": (1, 1)}

aoc_input = get_data(day=18, year=2019).splitlines()


def parse_input(lines, part="part_1"):
    entrance, dots, doors, keys = None, [], {}, {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            symb = lines[y][x]
            if symb in "#":
                continue
            elif symb == ".":
                dots.append((x, y))
            elif symb.isupper():
                doors[symb] = (x, y)
            else:
                keys[symb] = (x, y)

    if part == "part_2":
        x, y = keys.pop("@")
        for dx, dy in DIRS:
            dots.remove((x + dx, y + dy))
        for entrance_key, (dx, dy) in DIALS_ENTRANCE.items():
            keys[entrance_key] = (x + dx, y + dy)

    return entrance, dots, doors, keys


def build_graph(start, dots, keys, doors):
    reverse_keys = {v: k for k, v in keys.items()}
    reverse_doors = {v: k for k, v in doors.items()}

    queue = deque([(start, 0, 0)])
    visited = {start}

    keys_dist = (
        {} if reverse_keys[start] in START_KEYS else {reverse_keys[start]: (0, 0)}
    )
    while queue:
        (x, y), doors_seen, cnt = queue.popleft()
        for dx, dy in DIRS:
            neighbor = x + dx, y + dy
            if neighbor in visited:
                continue
            visited.add(neighbor)

            if neighbor in reverse_keys:
                if (key := reverse_keys[neighbor]) not in START_KEYS:
                    keys_dist[key] = (doors_seen, cnt + 1)
                queue.append((neighbor, doors_seen, cnt + 1))
            elif neighbor in reverse_doors:
                queue.append(
                    (
                        neighbor,
                        (
                            doors_seen
                            + (1 << ascii_uppercase.index(reverse_doors[neighbor]))
                        ),
                        cnt + 1,
                    )
                )
            elif neighbor in dots:
                queue.append((neighbor, doors_seen, cnt + 1))
    return keys_dist


def dijkstra(graph, start_keys):
    dist = defaultdict(lambda: math.inf)
    heap = [(0, (start_keys, 0))]

    while heap:
        dist_node, (current_keys, owned_key) = heappop(heap)
        if owned_key == (1 << (len(graph) - len(current_keys))) - 1:
            return dist_node

        reachable_keys = [
            (dial_idx, next_key, key_dist)
            for dial_idx, current_key in enumerate(current_keys)
            for next_key, (doors_needed, key_dist) in graph[current_key].items()
            if (
                (doors_needed & owned_key) == doors_needed
                and ((owned_key & (1 << ascii_lowercase.index(next_key))) == 0)
            )
        ]
        for dial_idx, next_key, key_dist in reachable_keys:
            neighbor = (
                current_keys[:dial_idx] + next_key + current_keys[dial_idx + 1 :],
                owned_key + (1 << (ascii_lowercase.index(next_key))),
            )
            dist_neighbor = dist_node + key_dist
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                heappush(heap, (dist_neighbor, neighbor))
    return dist


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    _, dots, doors, keys = parse_input(lines)
    graph = {letter: build_graph(keys[letter], dots, keys, doors) for letter in keys}
    return dijkstra(graph, "@")


def part_2(lines):
    entrance, dots, doors, keys = parse_input(lines, "part_2")
    graph = {letter: build_graph(keys[letter], dots, keys, doors) for letter in keys}
    return dijkstra(graph, "0123")


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
