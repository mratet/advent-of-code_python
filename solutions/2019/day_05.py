from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=5, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    *_, diagnostic_code = pc.run([1])
    return diagnostic_code


def part_2(lines):
    pc = IntcodeComputer(lines)
    *_, diagnostic_code = pc.run([5])
    return diagnostic_code


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
