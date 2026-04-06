import numpy as np
from aocd import get_data

input = get_data(day=20, year=2015)

MAX_VISIT = 50


def solve(input, multiplier, max_visits=None):
    N = int(input)
    houses = np.zeros(N // 10)
    for i in range(1, N // 10):
        houses[i : (max_visits * i + 1 if max_visits else None) : i] += i * multiplier
    return np.where(houses >= N)[0][0]


def part_1(input):
    return solve(input, 10)


def part_2(input):
    return solve(input, 11, MAX_VISIT)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
