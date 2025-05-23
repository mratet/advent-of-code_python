import re

from aocd import get_data

aoc_input = get_data(day=12, year=2019).splitlines()
import numpy as np
from math import lcm


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    extract_numb = lambda l: map(int, re.findall(r"-?\d+", l))
    pos = np.array([list(extract_numb(l)) for l in lines])
    vel = np.zeros_like(pos)
    T = 1000
    for _ in range(T):
        for i in range(len(pos)):
            vel[i] += np.sum(np.sign(pos - pos[i]), axis=0)
        pos += vel
    return (np.sum(abs(pos), axis=1) * np.sum(abs(vel), axis=1)).sum()


def part_2(lines):
    extract_numb = lambda l: map(int, re.findall(r"-?\d+", l))
    pos = np.array([list(extract_numb(l)) for l in lines])
    vel = np.zeros_like(pos)
    start_stats = np.vstack((pos, vel))
    repetition_time = [0, 0, 0]
    T = 1
    while not all(repetition_time):
        for x in range(len(pos)):
            vel[x] += np.sum(np.sign(pos - pos[x]), axis=0)
        pos += vel

        cur_stats = np.vstack((pos, vel))
        flag = np.all(cur_stats == start_stats, axis=0)
        for x in range(3):
            if flag[x] and not repetition_time[x]:
                repetition_time[x] = T
        T += 1
    return lcm(*repetition_time)


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
