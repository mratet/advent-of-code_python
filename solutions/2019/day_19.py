from itertools import product

from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=19, year=2019)


def probe(lines, x, y):
    [state] = IntcodeComputer(lines).run([x, y])
    return state


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(probe(lines, x, y) for x, y in product(range(50), range(50)))


def part_2(lines):
    square_size = 100
    x, y = 0, square_size

    while True:
        while not probe(lines, x, y):
            x += 1
        if probe(lines, x + square_size - 1, y - (square_size - 1)):  # TOP_RIGHT_CORNER
            return x * 10000 + y - (square_size - 1)  # TOP_LEFT_CORNER
        y += 1


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
