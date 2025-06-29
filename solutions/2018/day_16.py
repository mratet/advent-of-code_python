from aocd import get_data
from collections import defaultdict
import re

input = get_data(day=16, year=2018)

INSTRUCTION_NAMES = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
]


def parse_registers(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", line)))


def apply_instruction(name: str, instr: list[int], regs: list[int]) -> list[int]:
    opcode, a, b, c = instr
    result = regs.copy()
    match name:
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


def matching_instructions(before, instr, after):
    instr_values = list(map(int, instr.split()))
    matches = []
    for name in INSTRUCTION_NAMES:
        result = apply_instruction(name, instr_values, before)
        if result == after:
            matches.append(name)
    return matches


def deduce_opcode_mapping(samples) -> dict[int, str]:
    possibilities = defaultdict(set)

    for sample in samples:
        before, instr, after = sample
        opcode = int(instr.split()[0])
        matched = set(matching_instructions(before, instr, after))
        if opcode not in possibilities:
            possibilities[opcode] = matched
        else:
            possibilities[opcode] &= matched

    mapping = {}
    while len(mapping) < len(INSTRUCTION_NAMES):
        for opcode, names in possibilities.items():
            names -= set(mapping.values())
            if len(names) == 1:
                mapping[opcode] = names.pop()

    return mapping


def parse_input_blocks(raw_input: str):
    sections = raw_input.split("\n\n")
    sample_blocks = sections[:-1]
    program = sections[-1].splitlines()

    samples = []
    for block in sample_blocks:
        lines = block.splitlines()
        if len(lines) != 3:
            continue
        before = parse_registers(lines[0])
        instr = lines[1]
        after = parse_registers(lines[2])
        samples.append((before, instr, after))
    return samples, program


def count_ambiguous_samples(samples):
    return sum(1 for b, i, a in samples if len(matching_instructions(b, i, a)) >= 3)


def run_program(program_lines, opcode_mapping):
    regs = [0, 0, 0, 0]
    for line in program_lines:
        instr = list(map(int, line.split()))
        name = opcode_mapping[instr[0]]
        regs = apply_instruction(name, instr, regs)
    return regs


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    samples, program = parse_input_blocks(lines)
    return count_ambiguous_samples(samples)


def part_2(lines):
    samples, program = parse_input_blocks(lines)
    opcode_mapping = deduce_opcode_mapping(samples)
    result = run_program(program, opcode_mapping)
    return result[0]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
