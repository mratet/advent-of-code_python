from aocd import get_data

input = get_data(day=20, year=2015)

import numpy as np


def part_1(input):
    N = int(input)
    houses = np.zeros(N // 10)
    for i in range(1, N // 10):
        houses[i::i] += i * 10

    index = np.where(houses >= N)[0]
    return index[0]


def part_2(input):
    N = int(input)
    houses = np.zeros(N // 10)
    for i in range(1, N // 10):
        houses[i : (50 * i + 1) : i] += i * 11

    index = np.where(houses >= N)[0]
    return index[0]


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
