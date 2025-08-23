from collections import deque, defaultdict
from string import ascii_lowercase, ascii_uppercase
from heapq import heappush, heappop
import math

from aocd import get_data

DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

aoc_input = get_data(day=18, year=2019).splitlines()


def parse_input(lines):
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
    return dots, doors, keys


def build_graph(start, dots, keys, doors):
    reverse_keys = {v: k for k, v in keys.items()}
    reverse_doors = {v: k for k, v in doors.items()}

    queue = deque([(start, 0, 0)])
    visited = {start}

    keys_dist = {} if reverse_keys[start] == "@" else {reverse_keys[start]: (0, 0)}
    while queue:
        (x, y), doors_seen, cnt = queue.popleft()
        for dx, dy in DIRS:
            neighbor = x + dx, y + dy
            if neighbor in visited:
                continue
            visited.add(neighbor)

            if neighbor in reverse_keys:
                if (key := reverse_keys[neighbor]) != "@":
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


def dijkstra(graph):
    dist = defaultdict(lambda: math.inf)
    heap = [(0, ("@", 0))]

    while heap:
        dist_node, (current_key, owned_key) = heappop(heap)
        if owned_key == (1 << (len(graph) - 1)) - 1:
            return dist_node

        reachable_keys = [
            (next_key, key_dist)
            for next_key, (doors_needed, key_dist) in graph[current_key].items()
            if (
                (doors_needed & owned_key) == doors_needed
                and ((owned_key & (1 << ascii_lowercase.index(next_key))) == 0)
            )
        ]
        for next_key, key_dist in reachable_keys:
            neighbor = next_key, owned_key + (1 << (ascii_lowercase.index(next_key)))
            dist_neighbor = dist_node + key_dist
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                heappush(heap, (dist_neighbor, neighbor))
    return dist


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    dots, doors, keys = parse_input(lines)
    graph = {letter: build_graph(keys[letter], dots, keys, doors) for letter in keys}
    return dijkstra(graph)


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
# submit(part_1(aoc_input), part="a", day=18, year=2019)
print(f"My answer is {part_2(aoc_input)}")
# submit(part_2(aoc_input), part="b", day=18, year=2019)
