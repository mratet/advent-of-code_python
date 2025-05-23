from aocd import get_data

input = get_data(day=23, year=2015).splitlines()


def program_execution(registers, input):
    line_index = 0
    n = len(input)

    while line_index < n:
        instructions, *args = input[line_index].split()
        match instructions:
            case "hlf":
                c = args[0]
                registers[c] = registers[c] // 2
                line_index += 1
            case "tpl":
                c = args[0]
                registers[c] = registers[c] * 3
                line_index += 1
            case "inc":
                c = args[0]
                registers[c] = registers[c] + 1
                line_index += 1
            case "jmp":
                jump = int(args[0])
                line_index += jump
            case "jie":
                c, v = args[0][0], args[1]
                jump = int(v[1:]) * 1 if v[0] == "+" else -1
                line_index += jump if registers[c] % 2 == 0 else 1
            case "jio":
                c, v = args[0][0], args[1]
                jump = int(v[1:]) * 1 if v[0] == "+" else -1
                line_index += jump if registers[c] == 1 else 1
    return registers


def part_1(input):
    registers = {"a": 0, "b": 0}
    return program_execution(registers, input)["b"]


def part_2(input):
    registers = {"a": 1, "b": 0}
    return program_execution(registers, input)["b"]


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
