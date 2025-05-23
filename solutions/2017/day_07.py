from aocd import get_data, submit

input = get_data(day=7, year=2017)
import re


# WRITE YOUR SOLUTION HERE
def parse_programs(data):
    program_dict = {}

    lines = data.strip().split("\n")
    for line in lines:
        match = re.match(r"(\w+) \((\d+)\)(?: -> (.*))?", line)
        if match:
            name = match.group(1)
            weight = int(match.group(2))
            supports = match.group(3).split(", ") if match.group(3) else []
            program_dict[name] = {"weight": weight, "supports": supports}

    return program_dict


def compute_weight(program, programs):
    if not programs[program]["supports"]:
        return programs[program]["weight"]
    return programs[program]["weight"] + sum(
        compute_weight(program, programs) for program in programs[program]["supports"]
    )


def part_1(lines):
    programs = parse_programs(lines)
    cnt = {program: compute_weight(program, programs) for program in programs}
    A = max(cnt.values())
    for n, w in cnt.items():
        if w == A:
            return n


def part_2(lines):
    programs = parse_programs(lines)
    tot_weights = {program: compute_weight(program, programs) for program in programs}
    min_program = ""
    min_weight = 1e9
    for n, w in tot_weights.items():
        support = programs[n]["supports"]
        if support:
            support_weights = [tot_weights[s] for s in support]
            if len(set(support_weights)) > 1:
                if min(support_weights) < min_weight:
                    min_program = n
                    min_weight = min(support_weights)

    for s in programs[min_program]["supports"]:
        if tot_weights[s] > min_weight:  # Heavier tower case
            return programs[s]["weight"] - (tot_weights[s] - min_weight)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
