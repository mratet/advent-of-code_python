from aocd import get_data
from itertools import accumulate, cycle
import re

input = get_data(day=1, year=2018)


def parse_input(lines):
    return list(map(int, re.findall(r"-?\d+", lines)))


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    freq = parse_input(lines)
    return sum(freq)


def part_2(lines):
    freq = parse_input(lines)
    seen = {0}
    for curr_freq in accumulate(cycle(freq)):
        if curr_freq in seen:
            return curr_freq
        seen.add(curr_freq)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
