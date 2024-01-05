import itertools, re, collections
# from aocd import get_data
# input = get_data(day=1, year=2015)

input = open(0).read().splitlines()

import numpy as np
def _parse(input):
    n = len(input)
    cod = {'.': 0, '#': 1}
    state = np.zeros((n, n), dtype=int)
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            state[i, j] = cod[c]
    return np.pad(state, 1, 'constant', constant_values=0)


def next_state(state):
    n_state = state.copy()
    n, m = n_state.shape
    neighboors = [(i, j) for i, j in itertools.product([-1, 0, 1], [-1, 0, 1])]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (i, j) in [(1, 1), (1, m - 2), (n - 2, 1), (n - 2, m), (n - 2, m - 2)]:
                continue
            neighboors_count = sum([state[i + di, j + dj] for di, dj in neighboors]) - state[i, j]
            if state[i, j] and 2 <= neighboors_count <= 3:
                n_state[i, j] = 1
            elif not state[i, j] and neighboors_count == 3:
                n_state[i, j] = 1
            else:
                n_state[i, j] = 0
    return n_state

step = 100
state = _parse(input)
for _ in range(step):
    state = next_state(state)
print(np.sum(state))

# def part_1(input):
#
# def part_2(input):
#
# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')
