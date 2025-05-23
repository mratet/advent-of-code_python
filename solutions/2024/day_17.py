from aocd import get_data

input = get_data(day=17, year=2024)


# WRITE YOUR SOLUTION HERE
def _parse(input):
    regs, insts = input.split("\n\n")
    registers = {}
    for i, line in enumerate(regs.splitlines()):
        _, b = line.split(": ")
        registers[chr(ord("A") + i)] = int(b)
    _, inst = insts.split(": ")
    instructions = [int(n) for n in inst.split(",")]
    return registers, instructions


def run_program(registers, instructions):
    inst_pointer = 0
    res = []
    while True:
        if inst_pointer >= len(instructions) - 1:
            break
        opcode = instructions[inst_pointer]
        operand = instructions[inst_pointer + 1]
        literal_operand = operand
        if 0 <= literal_operand <= 3:
            combo_operand = literal_operand
        elif literal_operand == 4:
            combo_operand = registers["A"]
        elif literal_operand == 5:
            combo_operand = registers["B"]
        elif literal_operand == 6:
            combo_operand = registers["C"]
        elif literal_operand == 7:
            combo_operand = 7  # Will not be used this iteration

        if opcode == 0:
            registers["A"] = registers["A"] // (1 << combo_operand)
        elif opcode == 1:
            registers["B"] = registers["B"] ^ literal_operand
        elif opcode == 2:
            registers["B"] = combo_operand % 8
        elif opcode == 3:
            if registers["A"]:
                inst_pointer = literal_operand
                continue
        elif opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
        elif opcode == 5:
            val = combo_operand % 8
            res.append(val)
        elif opcode == 6:
            registers["B"] = registers["A"] // (1 << combo_operand)
        elif opcode == 7:
            registers["C"] = registers["A"] // (1 << combo_operand)
        inst_pointer += 2
    return ",".join([str(r) for r in res])


def part_1(lines):
    registers, instructions = _parse(lines)
    return run_program(registers, instructions)


def part_2(lines):
    registers, instructions = _parse(lines)
    registers["A"] = 190384615275535
    assert run_program(registers, instructions) == ",".join(
        [str(n) for n in instructions]
    )
    return 190384615275535
    # instructions_test = [0, 3, 5, 4, 3, 0]
    # 117440 = int('0o034530, 8) * 8
    # '0o34530 = oct(117440 // 8)
    ##### To clean in the future
    n = 4
    # for i in range(8 ** n, 8 ** (n + 1), 8):
    for i in range(int("0o5322353727230000", 8), int("0o5322353777700000", 8)):
        registers["A"] = i
        res = run_program(registers, instructions)
        if res.startswith("2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0"):
            print(res, oct(i), i)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
