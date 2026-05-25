import re
from collections import defaultdict

from aocd import get_data

input = get_data(day=5, year=2022).split("\n\n")


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    raw_stack, instructions = lines
    cargo_stacks = defaultdict(list)
    for line in zip(*raw_stack.splitlines(), strict=False):
        reversed_line = "".join(reversed(line))
        stack_id, crates = reversed_line[0], reversed_line[1:].rstrip()
        if stack_id.isdigit():
            for crate in crates:
                cargo_stacks[stack_id].append(crate)
    return cargo_stacks, instructions


def solve(lines, part="part_1"):
    cargo_stacks, instructions = parse_input(lines)
    for line in instructions.splitlines():
        q, id1, id2 = re.findall(r"(\d+)", line)
        selected_crates = [cargo_stacks[id1].pop() for _ in range(int(q))]
        cargo_stacks[id2].extend(selected_crates if part == "part_1" else reversed(selected_crates))
    return "".join(s[-1] for s in cargo_stacks.values())


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
