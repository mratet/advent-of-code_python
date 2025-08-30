from aocd import get_data
from intcode import IntcodeComputer

input = get_data(day=2, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    pc.memory[1], pc.memory[2] = 12, 2
    pc.run()
    return pc.memory[0]


def part_2(lines):
    for noun in range(100):
        for verb in range(100):
            pc = IntcodeComputer(lines)
            pc.memory[1], pc.memory[2] = noun, verb
            pc.run()
            if pc.memory[0] == 19690720:
                return 100 * noun + verb


# END OF SOLUTION

print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
