from math import sqrt

from aocd import get_data, submit

input = get_data(day=3, year=2017)
import numpy as np


# WRITE YOUR SOLUTION HERE
def generate_spiral_matrix(N):
    matrix = np.zeros((N, N), dtype=int)
    matrix[N // 2, N // 2] = 1
    val = N**2
    x, y = N - 1, N - 1
    dx, dy = 0, -1

    for _ in range(N * N):
        matrix[x, y] = val
        val -= 1
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx, ny] != 0:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy

    return matrix


def part_1(lines):
    matrix = generate_spiral_matrix(700)
    onex, oney = np.argwhere(matrix == 1)[0]
    targetx, targety = np.argwhere(matrix == int(lines))[0]
    return abs(onex - targetx) + abs(oney - targety)


def part_2(lines):
    # Find your sol at https://oeis.org/A141481
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# submit(part_1(input), part="a", day=1, year=2017)
print(f"My answer is {part_2(input)}")
# submit(part_2(input), part="b", day=1, year=2017)
