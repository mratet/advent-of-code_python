from aocd import get_data, submit

aoc_input = get_data(day=5, year=2019)
from intcode import run_program, read_program, deque
# WRITE YOUR SOLUTION HERE


def part_1(lines):
    program = read_program(lines)
    _, out = run_program(program, deque([1]))
    return out[-1]


def part_2(lines):
    program = read_program(lines)
    _, out = run_program(program, deque([5]))
    return out[-1]


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")  # 5074395
print(f"My answer is {part_2(aoc_input)}")  # 8346937
