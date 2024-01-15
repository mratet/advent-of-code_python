import itertools, re, collections
from aocd import get_data
input = get_data(day=12, year=2016).splitlines()

def program_execution(registers, input):

    line_index = 0
    n = len(input)

    while line_index < n:
        instructions, *args = input[line_index].split()
        match instructions:
            case 'inc':
                c = args[0]
                registers[c] = registers[c] + 1
            case 'dec':
                c = args[0]
                registers[c] = registers[c] - 1
            case 'cpy':
                x, y = args[0], args[1]
                registers[y] = registers[x] if x in 'abcd' else int(x)
            case 'jnz':
                x, y = args[0], args[1]
                cond = registers[x] if x in 'abcd' else int(x)
                line_index += int(y) if cond != 0 else 1
                line_index -= 1
        line_index += 1

    return registers

def part_1(input):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    registers = program_execution(registers, input)
    return registers['a']

def part_2(input):
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    registers = program_execution(registers, input)
    return registers['a']

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
