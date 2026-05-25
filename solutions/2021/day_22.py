import re

import numpy as np
from aocd import get_data

input = get_data(day=22, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    cubes = []
    ops = []
    xs, ys, zs = set(), set(), set()
    for line in lines:
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"(-?\d+)", line))
        cubes.append([x1, x2 + 1, y1, y2 + 1, z1, z2 + 1])
        ops.append(line[:3].rstrip())
        xs.update({x1, x2 + 1})
        ys.update({y1, y2 + 1})
        zs.update({z1, z2 + 1})
    return cubes, ops, xs, ys, zs


def solve(lines, part="part_1"):
    cubes, ops, xs, ys, zs = parse_input(lines)
    x_range, y_range, z_range = sorted(xs), sorted(ys), sorted(zs)
    x_idx = {v: i for i, v in enumerate(x_range)}
    y_idx = {v: i for i, v in enumerate(y_range)}
    z_idx = {v: i for i, v in enumerate(z_range)}
    grid = np.zeros((len(x_range), len(y_range), len(z_range)), dtype=bool)
    for op, (x1, x2, y1, y2, z1, z2) in zip(ops, cubes, strict=False):
        if part == "part_1" and (x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50):
            continue
        xi1, xi2 = x_idx[x1], x_idx[x2]
        yi1, yi2 = y_idx[y1], y_idx[y2]
        zi1, zi2 = z_idx[z1], z_idx[z2]
        grid[xi1:xi2, yi1:yi2, zi1:zi2] = op == "on"

    vols_x = np.diff(x_range).astype(np.int64)
    vols_y = np.diff(y_range).astype(np.int64)
    vols_z = np.diff(z_range).astype(np.int64)
    volume_grid = vols_x.reshape(-1, 1, 1) * vols_y.reshape(1, -1, 1) * vols_z.reshape(1, 1, -1)
    return np.sum(volume_grid[grid[:-1, :-1, :-1]])


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
