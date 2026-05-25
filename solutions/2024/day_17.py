from aocd import get_data

input = get_data(day=17, year=2024)


# WRITE YOUR SOLUTION HERE
def parse_input(input):
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
    while inst_pointer < len(instructions) - 1:
        opcode = instructions[inst_pointer]
        operand = instructions[inst_pointer + 1]
        if 0 <= operand <= 3:
            combo_operand = operand
        elif operand == 4:
            combo_operand = registers["A"]
        elif operand == 5:
            combo_operand = registers["B"]
        elif operand == 6:
            combo_operand = registers["C"]
        elif operand == 7:
            combo_operand = 7
        if opcode == 0:
            registers["A"] = registers["A"] // (1 << combo_operand)
        elif opcode == 1:
            registers["B"] = registers["B"] ^ operand
        elif opcode == 2:
            registers["B"] = combo_operand % 8
        elif opcode == 3:
            if registers["A"]:
                inst_pointer = operand
                continue
        elif opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
        elif opcode == 5:
            res.append(combo_operand % 8)
        elif opcode == 6:
            registers["B"] = registers["A"] // (1 << combo_operand)
        elif opcode == 7:
            registers["C"] = registers["A"] // (1 << combo_operand)
        inst_pointer += 2
    return ",".join(str(r) for r in res)


def part_1(lines):
    registers, instructions = parse_input(lines)
    return run_program(registers, instructions)


def part_2(lines):
    registers, instructions = parse_input(lines)

    def backtrack(a, depth):
        if depth == len(instructions):
            return a
        for k in range(8):
            candidate = a * 8 + k
            regs = {**registers, "A": candidate}
            expected = ",".join(str(n) for n in instructions[len(instructions) - depth - 1 :])
            if run_program(regs, instructions) == expected:
                result = backtrack(candidate, depth + 1)
                if result is not None:
                    return result
        return None

    return backtrack(0, 0)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
