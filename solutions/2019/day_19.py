from aocd import get_data
from intcode import IntcodeComputer
from itertools import product

aoc_input = get_data(day=19, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    screen_state = {}
    N = 50
    for x, y in product(range(N), range(N)):
        pc = IntcodeComputer(lines)
        [state] = pc.run([x, y])
        screen_state[(x, y)] = state
    return sum(screen_state.values())


def part_2(lines):
    square_size = 100
    x, y = square_size, square_size

    while True:
        x -= 5
        # Find left beam border
        while True:
            pc = IntcodeComputer(lines)
            [state] = pc.run([x, y])
            if state:
                break
            x += 1

        pc = IntcodeComputer(lines)
        [state] = pc.run([x + square_size - 1, y - (square_size - 1)])  # TOP_RIGHT_CORNER
        if state:
            return x * 10000 + y - (square_size - 1)  # TOP_LEFT_CORNER
        y += 1


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
