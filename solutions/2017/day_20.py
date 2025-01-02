from aocd import get_data, submit
input = get_data(day=20, year=2017).splitlines()
import re
import numpy as np

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    particles = np.array([list(map(int, re.findall(r'-?\d+', line))) for line in lines])
    pos, vel, acc = particles[:, 0:3], particles[:, 3:6], particles[:, 6:9]

    for _ in range(10000):
        vel += acc
        pos += vel

    return np.argmin(np.sum(np.abs(pos), axis=1))

def part_2(lines):
    particles = np.array([list(map(int, re.findall(r'-?\d+', line))) for line in lines])
    pos, vel, acc = particles[:, 0:3], particles[:, 3:6], particles[:, 6:9]

    for _ in range(1000):
        vel += acc
        pos += vel
        _, inverse_idx, cnts = np.unique(pos, axis=0, return_inverse=True, return_counts=True)
        mask = cnts[inverse_idx] == 1
        if mask.any():
            pos = pos[mask]
            vel = vel[mask]
            acc = acc[mask]

    return len(pos)

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
