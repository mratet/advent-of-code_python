import math

from aocd import get_data

input = get_data(day=23, year=2016).splitlines()


TOGGLE = {"inc": "dec", "dec": "inc", "tgl": "inc", "jnz": "cpy", "cpy": "jnz"}


def _parse_program(input):
    program = []
    for line in input:
        op, *args = line.split()
        args = [a if a in "abcd" else int(a) for a in args]
        program.append([op, args])
    return program


def _resolve(registers, x):
    return registers[x] if isinstance(x, str) else x


def program_execution(registers, program):
    line_index = 0

    while line_index < len(program):
        op, args = program[line_index]
        match op:
            case "inc":
                c = args[0]
                registers[c] = registers[c] + 1
            case "dec":
                c = args[0]
                registers[c] = registers[c] - 1
            case "cpy":
                x, y = args
                if isinstance(y, str):
                    registers[y] = _resolve(registers, x)
            case "jnz":
                x, y = args
                if _resolve(registers, x):
                    line_index += _resolve(registers, y)
                    continue
            case "tgl":
                target = line_index + _resolve(registers, args[0])
                if 0 <= target < len(program):
                    program[target][0] = TOGGLE[program[target][0]]
        line_index += 1

    return registers


def part_1(input):
    program = _parse_program(input)
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    registers = program_execution(registers, program)
    return registers["a"]


def part_2(input):
    # You can't run the program because it'll be too long
    # By looking at the evolution of a, you can understand what the code is doing
    N = 12
    return math.factorial(N) + 73 * 81


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
