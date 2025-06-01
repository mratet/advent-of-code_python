from aocd import get_data
from itertools import product

input = get_data(day=24, year=2021).splitlines()


def run_program(model_number):
    variables = {"w": 0, "x": 0, "y": 0, "z": 0}
    j = 0
    i = 0
    while i < len(input):
        instr, *v = input[i].split()
        if instr == "inp":
            variables[v[0]] = int(model_number[j])
            j += 1
        elif instr == "add":
            a, b = v
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] + b
        elif instr == "mul":
            a, b = v
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] * b
        elif instr == "div":
            a, b = v
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] // b
        elif instr == "mod":
            a, b = v
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] % b
        elif instr == "eql":
            a, b = v
            b = variables[b] if b in variables else int(b)
            variables[a] = 1 if variables[a] == b else 0
        i += 1
    return variables


def generate_constraints(lines):
    """
    input w
    if C > 0, z = z * 26 + w + C2
    if C < 0, z = z // 26 iff w == (z % 26 - C)
    """
    constraints = []
    C = [int(line[-3:]) for line in lines[5::18]]
    C2 = [int(line[-2:]) for line in lines[15::18]]
    stack = []
    for idx, (c1, c2) in enumerate(zip(C, C2)):
        if c1 > 0:
            stack.append((idx, c2))
        else:
            i1, prev_c2 = stack.pop()
            constraints.append((idx, i1, c1 + prev_c2))
    return constraints


def is_valid(combo, constraints):
    digits = [0] * 14
    targets = {target for target, _, _ in constraints}
    idx_free = sorted(set(range(14)) - targets)
    for i, val in zip(idx_free, combo):
        digits[i] = val

    for target, source, delta in constraints:
        val = digits[source] + delta
        if not (1 <= val <= 9):
            return False
        digits[target] = val

    return "".join(map(str, digits))


def generate_all_valid_numbers(constraints):
    domain = range(1, 10)
    return [
        number
        for combo in product(domain, repeat=7)
        if (number := is_valid(combo, constraints))
    ]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    constraints = generate_constraints(lines)
    valid_numbers = generate_all_valid_numbers(constraints)
    return max(valid_numbers)


def part_2(lines):
    constraints = generate_constraints(lines)
    valid_numbers = generate_all_valid_numbers(constraints)
    return min(valid_numbers)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
