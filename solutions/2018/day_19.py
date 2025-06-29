from aocd import get_data

input = get_data(day=19, year=2018).splitlines()


def apply_instruction(instr, regs):
    opname, *i = instr.split()
    a, b, c = map(int, i)
    result = regs.copy()
    match opname:
        case "addr":
            result[c] = regs[a] + regs[b]
        case "addi":
            result[c] = regs[a] + b
        case "mulr":
            result[c] = regs[a] * regs[b]
        case "muli":
            result[c] = regs[a] * b
        case "banr":
            result[c] = regs[a] & regs[b]
        case "bani":
            result[c] = regs[a] & b
        case "borr":
            result[c] = regs[a] | regs[b]
        case "bori":
            result[c] = regs[a] | b
        case "setr":
            result[c] = regs[a]
        case "seti":
            result[c] = a
        case "gtir":
            result[c] = int(a > regs[b])
        case "gtri":
            result[c] = int(regs[a] > b)
        case "gtrr":
            result[c] = int(regs[a] > regs[b])
        case "eqir":
            result[c] = int(a == regs[b])
        case "eqri":
            result[c] = int(regs[a] == b)
        case "eqrr":
            result[c] = int(regs[a] == regs[b])
    return result


def get_main_value(programm, part="part_1"):
    programm = programm.copy()
    ip_register = int(programm.pop(0)[-1])
    ip = 0
    registers = [0] * 6
    registers[0] = 0 if part == "part_1" else 1

    while ip < len(programm):
        registers[ip_register] = ip
        registers = apply_instruction(programm[ip], registers)
        ip = registers[ip_register]
        ip += 1
        if ip == 1:
            return registers[2]


def real_programm(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    main_value = get_main_value(lines, "part_1")
    return real_programm(main_value)


def part_2(lines):
    main_value = get_main_value(lines, "part_2")
    return real_programm(main_value)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
