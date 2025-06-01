from aocd import get_data
import numpy as np
import re

input = get_data(day=22, year=2021).splitlines()

cube = np.zeros((101, 101, 101), dtype=int)
for line in input:
    x1, x2, y1, y2, z1, z2 = map(lambda x: int(x) + 50, re.findall(r"(-?\d+)", line))
    val = 1 if line[:2] == "on" else 0
    cube[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = val

print(cube.sum())


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return


def part_2(lines):
    return


# END OF SOLUTION
# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')
