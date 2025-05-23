from aocd import get_data, submit
from collections import deque

aoc_input = get_data(day=9, year=2019)
from intcode import read_program, run_program


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    memory = read_program(lines)
    print(memory)
    mem, out_buff = run_program(memory, deque([1]))
    return out_buff[0]


def part_2(lines):
    memory = read_program(lines)
    mem, out_buff = run_program(memory, deque([2]))
    return out_buff[0]


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")  # 2351176124
print(f"My answer is {part_2(aoc_input)}")  # 73110
