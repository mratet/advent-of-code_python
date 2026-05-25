import heapq

from aocd import get_data

input = get_data(day=1, year=2022).split("\n\n")


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    return [sum(int(cal) for cal in elf.splitlines()) for elf in lines]


def part_1(lines):
    return max(parse_input(lines))


def part_2(lines):
    return sum(heapq.nlargest(3, parse_input(lines)))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
