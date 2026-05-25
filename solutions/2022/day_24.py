from collections import deque
from math import lcm

from aocd import get_data

DIRECTIONS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
MOVES = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

input = get_data(day=24, year=2022).splitlines()
H, W = len(input), len(input[0])


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    blizzards = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in DIRECTIONS:
                blizzards.append((x, y, c))
    return blizzards


def build_blizzard_states(blizzards, cycle_length):
    states = []
    for t in range(cycle_length):
        forbidden = set()
        for x, y, c in blizzards:
            dx, dy = DIRECTIONS[c]
            nx = 1 + (x - 1 + dx * t) % (W - 2)
            ny = 1 + (y - 1 + dy * t) % (H - 2)
            forbidden.add((nx, ny))
        states.append(forbidden)
    return states


def bfs(blizzard_states, cycle_length, start, end, start_time):
    t_mod = start_time % cycle_length
    queue = deque([(start[0], start[1], t_mod, start_time)])
    seen = {(start[0], start[1], t_mod)}
    while queue:
        x, y, t_mod, t_abs = queue.popleft()
        if (x, y) == end:
            return t_abs
        next_t = (t_mod + 1) % cycle_length
        forbidden = blizzard_states[next_t]
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if ((nx, ny) == start or (nx, ny) == end or (1 <= nx < W - 1 and 1 <= ny < H - 1)) and (
                nx,
                ny,
            ) not in forbidden:
                state = (nx, ny, next_t)
                if state not in seen:
                    seen.add(state)
                    queue.append((nx, ny, next_t, t_abs + 1))
    return -1


def solve(lines, part="part_1"):
    blizzards = parse_input(lines)
    start, end = (1, 0), (W - 2, H - 1)
    cycle_length = lcm(W - 2, H - 2)
    states = build_blizzard_states(blizzards, cycle_length)
    t1 = bfs(states, cycle_length, start, end, 0)
    if part == "part_1":
        return t1
    t2 = bfs(states, cycle_length, end, start, t1)
    return bfs(states, cycle_length, start, end, t2)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
