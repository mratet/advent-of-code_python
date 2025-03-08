from aocd import get_data, submit
from collections import deque
aoc_input = get_data(day=7, year=2019)
from intcode import read_program, run_program
from itertools import permutations
# WRITE YOUR SOLUTION HERE

def part_1(lines):
    memory = read_program(lines)
    tab = []
    for perm in permutations(range(5)):
        program = memory[:]
        in_buff = deque([perm[0], 0])
        _, out_buff = run_program(program, in_buff)
        for p in perm[1:]:
            program = memory[:]
            in_buff = deque([p, out_buff[0]])
            _, out_buff = run_program(program, in_buff)
        tab.append(out_buff[0])
    return max(tab)

def part_2(lines):
    return
    # memory = read_program(lines)
    # tab = []
    # for perm in permutations(range(5, 10)):
    #     program = memory[:]
    #     in_buff = deque([perm[0], 0])
    #     _, out_buff = run_program(program, in_buff)
    #     for p in perm[1:]:
    #         program = memory[:]
    #         in_buff = deque([p, out_buff[0]])
    #         _, out_buff = run_program(program, in_buff)
    #     tab.append(out_buff[0])
    # return max(tab)

# END OF SOLUTION
print(f'My answer is {part_1(aoc_input)}') # 13848
print(f'My answer is {part_2(aoc_input)}')

