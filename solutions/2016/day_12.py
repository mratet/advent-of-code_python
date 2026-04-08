from aocd import get_data

input = get_data(day=12, year=2016).splitlines()


def _parse_program(input):
    program = []
    for line in input:
        op, *args = line.split()
        args = [a if a in "abcd" else int(a) for a in args]
        program.append((op, args))
    return program


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
                registers[y] = registers[x] if isinstance(x, str) else x
            case "jnz":
                x, y = args
                cond = registers[x] if isinstance(x, str) else x
                if cond:
                    line_index += y
                    continue
        line_index += 1

    return registers


def part_1(input):
    program = _parse_program(input)
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers = program_execution(registers, program)
    return registers["a"]


def part_2(input):
    program = _parse_program(input)
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    registers = program_execution(registers, program)
    return registers["a"]


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
