import numpy as np
from aocd import get_data

input = get_data(day=18, year=2015).splitlines()

STEP = 100
CORNERS = ([0, 0, -1, -1], [0, -1, 0, -1])


def _parse(input):
    return np.array([[c == "#" for c in line] for line in input], dtype=int)


def count_neighbors(state):
    padded = np.pad(state, 1)
    R, C = state.shape
    return sum(padded[r : r + R, c : c + C] for r in range(3) for c in range(3) if (r, c) != (1, 1))


def next_step(state):
    neighbors = count_neighbors(state)
    state = state & (neighbors >= 2) & (neighbors <= 3) | ~state & (neighbors == 3)
    return state


def solve(input, part="part_1"):
    state = _parse(input)
    if part == "part_2":
        state[CORNERS] = 1

    for _ in range(STEP):
        state = next_step(state)
        if part == "part_2":
            state[CORNERS] = 1
    return state.sum()


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
