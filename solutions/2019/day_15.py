from collections import defaultdict
from collections import deque

from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=15, year=2019)

N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
DIRS = [N, S, W, E]

REVERSE_DIRS = [0, 1, 0, 3, 2]


def bfs(empty, start=(0, 0)):
    to_visit = deque()
    dist = defaultdict(lambda: float("-inf"))
    dist[start] = 0
    to_visit.append(start)

    while to_visit:
        node = to_visit.pop()
        x, y = node
        for dx, dy in DIRS:
            neighbor = (x + dx, y + dy)
            if neighbor in empty and dist[neighbor] == float("-inf"):
                dist[neighbor] = dist[node] + 1
                to_visit.appendleft(neighbor)
    return dist


def explore_space(pc):
    walls, empty_spaces, oxygen_system = [], [], None
    px, py = 0, 0
    current_path = []

    while True:
        successful_move = False

        for dir_id, (dx, dy) in enumerate(DIRS, start=1):
            neighbor = px + dx, py + dy
            if neighbor in walls + empty_spaces:
                continue
            [status_code] = pc.run([dir_id])
            if status_code == 0:
                walls.append(neighbor)
            else:
                if status_code == 2:
                    oxygen_system = neighbor
                empty_spaces.append(neighbor)
                px, py = neighbor
                current_path.append(dir_id)
                successful_move = True

        if not successful_move:
            if len(current_path) == 0:
                break
            last_successful_move = REVERSE_DIRS[current_path.pop()]
            dx, dy = DIRS[last_successful_move]
            px, py = px + dx, py + dy
            pc.run([last_successful_move + 1])

    return empty_spaces, oxygen_system


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    empty_spaces, oxygen_system = explore_space(pc)
    dist = bfs(empty_spaces, start=(0, 0))
    return dist[oxygen_system]


def part_2(lines):
    pc = IntcodeComputer(lines)
    empty_spaces, oxygen_system = explore_space(pc)
    dist_oxygen = bfs(empty_spaces, start=oxygen_system)
    return max(dist_oxygen.values())


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
