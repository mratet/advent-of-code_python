from collections import Counter
from math import log

from aocd import get_data

input = get_data(day=11, year=2024)


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    return [int(s) for s in lines.split()]


def solve(lines, part="part_1"):
    stones = Counter(parse_input(lines))
    n = 25 if part == "part_1" else 75
    for _ in range(n):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
                continue
            cnt_bits = int(log(stone, 10)) + 1
            if cnt_bits % 2 == 0:
                middle = 10 ** (cnt_bits // 2)
                new_stones[stone // middle] += count
                new_stones[stone % middle] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones
    return sum(stones.values())


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
