import re
from math import lcm

import numpy as np
from aocd import get_data

aoc_input = get_data(day=12, year=2019).splitlines()


def extract_numb(l):
    return map(int, re.findall(r"-?\d+", l))


PART_1_STEPS = 1000


def apply_gravity(pos, vel):
    for i in range(len(pos)):
        vel[i] += np.sum(np.sign(pos - pos[i]), axis=0)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pos = np.array([list(extract_numb(l)) for l in lines])
    vel = np.zeros_like(pos)
    for _ in range(PART_1_STEPS):
        apply_gravity(pos, vel)
        pos += vel
    return (np.sum(np.abs(pos), axis=1) * np.sum(np.abs(vel), axis=1)).sum()


def part_2(lines):
    pos = np.array([list(extract_numb(l)) for l in lines])
    vel = np.zeros_like(pos)
    start_stats = np.vstack((pos, vel))
    periods = [0, 0, 0]
    t = 1
    while not all(periods):
        apply_gravity(pos, vel)
        pos += vel

        axes_at_start = np.all(np.vstack((pos, vel)) == start_stats, axis=0)
        for axis in range(3):
            if axes_at_start[axis] and not periods[axis]:
                periods[axis] = t
        t += 1
    return lcm(*periods)


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
