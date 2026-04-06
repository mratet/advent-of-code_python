from itertools import accumulate, pairwise

from aocd import get_data

input = get_data(day=1, year=2025).replace("L", "-").replace("R", "+").splitlines()

DIAL_SIZE = 100
DIAL_START_POS = 50

# WRITE YOUR SOLUTION HERE


def part_1(lines):
    positions = accumulate(map(int, lines))
    return sum((pos - DIAL_START_POS) % DIAL_SIZE == 0 for pos in positions)


def part_2(lines):
    positions = (DIAL_START_POS + x for x in [0, *accumulate(map(int, lines))])
    return sum(abs(next_pos // DIAL_SIZE - pos // DIAL_SIZE) for pos, next_pos in pairwise(positions))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
