from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=9, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    [boost_keycode] = pc.run([1])
    return boost_keycode


def part_2(lines):
    pc = IntcodeComputer(lines)
    [distress_signal] = pc.run([2])
    return distress_signal


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
