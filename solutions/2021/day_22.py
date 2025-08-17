from aocd import get_data
import numpy as np
import re

input = get_data(day=22, year=2021).splitlines()


def _parse_input(lines):
    cubes = []
    ops = []
    X, Y, Z = set(), set(), set()
    for line in lines:
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"(-?\d+)", line))
        cubes.append([x1, x2 + 1, y1, y2 + 1, z1, z2 + 1])
        ops.append(line[:3].rstrip())
        X.update({x1, x2 + 1})
        Y.update({y1, y2 + 1})
        Z.update({z1, z2 + 1})
    return cubes, ops, X, Y, Z


# WRITE YOUR SOLUTION HERE
def solve(lines, part="part_1"):
    cubes, ops, X, Y, Z = _parse_input(lines)
    X_range, Y_range, Z_range = sorted(X), sorted(Y), sorted(Z)
    grid = np.zeros((len(X_range), len(Y_range), len(Z_range)), dtype=bool)
    for op, (x1, x2, y1, y2, z1, z2) in zip(ops, cubes):
        if part == "part_1" and (
            x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50
        ):
            continue
        X1, X2 = X_range.index(x1), X_range.index(x2)
        Y1, Y2 = Y_range.index(y1), Y_range.index(y2)
        Z1, Z2 = Z_range.index(z1), Z_range.index(z2)
        grid[X1:X2, Y1:Y2, Z1:Z2] = op == "on"

    vols_x = np.diff(X_range).astype(np.int64)
    vols_y = np.diff(Y_range).astype(np.int64)
    vols_z = np.diff(Z_range).astype(np.int64)

    volume_grid = (
        vols_x.reshape(-1, 1, 1) * vols_y.reshape(1, -1, 1) * vols_z.reshape(1, 1, -1)
    )
    on_cubes_mask = grid[:-1, :-1, :-1]
    return np.sum(volume_grid[on_cubes_mask])


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
