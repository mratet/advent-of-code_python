import itertools, re, collections
from aocd import get_data
input = get_data(day=18, year=2015).splitlines()

import numpy as np
def _parse(input):
    n = len(input)
    state = np.zeros((n, n), dtype=int)
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            state[i, j] = 1 if c == '#' else 0
    return np.pad(state, 1, 'constant', constant_values=0)


def next_state(state, part='part_1'):
    n_state = state.copy()
    n, m = n_state.shape
    neighboors = [(i, j) for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]) if (i, j) != (0, 0)]
    for i, j in itertools.product(range(1, n - 1), range(1, m - 1)):

        if part == 'part_2':
            if (i, j) in [(1, 1), (1, m - 2), (n - 2, 1), (n - 2, m), (n - 2, m - 2)]:
                continue

        neighboors_count = sum([state[i + di, j + dj] for di, dj in neighboors])

        if state[i, j] and 2 <= neighboors_count <= 3:
            n_state[i, j] = 1
        elif not state[i, j] and neighboors_count == 3:
            n_state[i, j] = 1
        else:
            n_state[i, j] = 0

    return n_state


def part_1(input):
    step = 100
    state = _parse(input)
    for _ in range(step):
        state = next_state(state, 'part_1')
    return np.sum(state)


def part_2(input):
    step = 100
    state = _parse(input)
    for _ in range(step):
        state = next_state(state, 'part_2')
    return np.sum(state)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
