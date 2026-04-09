import re

import numpy as np
from aocd import get_data

input = get_data(day=20, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def solve(lines, steps, remove_collisions=False):
    particles = np.array([list(map(int, re.findall(r"-?\d+", line))) for line in lines])
    pos, vel, acc = particles[:, 0:3], particles[:, 3:6], particles[:, 6:9]

    for _ in range(steps):
        vel += acc
        pos += vel
        if remove_collisions:
            _, inverse_idx, unique_counts = np.unique(pos, axis=0, return_inverse=True, return_counts=True)
            mask = unique_counts[inverse_idx] == 1
            if mask.any():
                pos, vel, acc = pos[mask], vel[mask], acc[mask]

    return pos


def part_1(lines):
    pos = solve(lines, steps=10_000)
    return np.argmin(np.sum(np.abs(pos), axis=1))


def part_2(lines):
    pos = solve(lines, steps=1_000, remove_collisions=True)
    return len(pos)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
