from aocd import get_data

input = get_data(day=25, year=2016).splitlines()


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
    sig = []

    while line_index < len(program) and len(sig) < 15:
        op, args = program[line_index]
        match op:
            case "inc":
                c = args[0]
                registers[c] = registers[c] + 1
            case "dec":
                c = args[0]
                registers[c] = registers[c] - 1
            case "out":
                sig.append(_resolve(registers, args[0]))
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

    return registers, sig


def part_1(input):
    # The program will print the inverse binary representation of N - b * c
    binary = "010101010101"
    return int(binary[::-1], 2) - 4 * 643


print(f"My answer is {part_1(input)}")
