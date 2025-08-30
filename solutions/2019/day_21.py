from aocd import get_data
from intcode import IntcodeComputer, MAP_TO_ASCII

aoc_input = get_data(day=21, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    walk_program = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n"
    *_, amount_damage = pc.run(MAP_TO_ASCII(walk_program))
    return amount_damage


def part_2(lines):
    pc = IntcodeComputer(lines)
    run_program = "NOT C T\nNOT B J\nOR T J\nNOT A T\nOR T J\nOR E T\nOR H T\nAND D T\nAND T J\nRUN\n"
    *_, amount_damage = pc.run(MAP_TO_ASCII(run_program))
    return amount_damage


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
