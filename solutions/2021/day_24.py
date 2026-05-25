from aocd import get_data

input = get_data(day=24, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
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
    C = [int(line.split()[-1]) for line in lines[5::18]]
    C2 = [int(line.split()[-1]) for line in lines[15::18]]
    stack = []
    for idx, (c1, c2) in enumerate(zip(C, C2, strict=False)):
        if c1 > 0:
            stack.append((idx, c2))
        else:
            i1, prev_c2 = stack.pop()
            constraints.append((idx, i1, c1 + prev_c2))
    return constraints


def solve(lines):
    constraints = generate_constraints(lines)
    targets = {target for target, _, _ in constraints}
    max_digits, min_digits = [0] * 14, [0] * 14
    for pos in set(range(14)) - targets:
        max_digits[pos] = 9
        min_digits[pos] = 1
    for target, source, delta in constraints:
        max_digits[source] = min(9, 9 - delta)
        max_digits[target] = max_digits[source] + delta
        min_digits[source] = max(1, 1 - delta)
        min_digits[target] = min_digits[source] + delta
    return "".join(map(str, max_digits)), "".join(map(str, min_digits))


def part_1(lines):
    return solve(lines)[0]


def part_2(lines):
    return solve(lines)[1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
