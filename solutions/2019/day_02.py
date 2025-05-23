from collections import deque

from aocd import get_data, submit
from intcode import run_program, read_program

input = get_data(day=2, year=2019)
# WRITE YOUR SOLUTION HERE


def part_1(lines):
    intcode_program = read_program(lines)
    intcode_program[1] = 12
    intcode_program[2] = 2
    program, _ = run_program(intcode_program)
    return program[0]


def part_2(lines):
    computer = read_program(lines)
    for noun in range(100):
        for verb in range(100):
            program = computer[:]
            program[1], program[2] = noun, verb
            program, _ = run_program(program)
            if program[0] == 19690720:
                return 100 * noun + verb


# END OF SOLUTION
print(f"My answer is {part_1(input)}")  # 9706670
print(f"My answer is {part_2(input)}")  # 2552
