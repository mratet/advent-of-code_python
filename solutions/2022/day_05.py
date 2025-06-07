from aocd import get_data
import re
from collections import defaultdict

input = get_data(day=5, year=2022).split("\n\n")


def parse_input(lines):
    raw_stack, instructions = lines

    cargo_stacks = defaultdict(list)
    for line in zip(*raw_stack.splitlines()):
        reversed_line = "".join(reversed(line))
        stack_id, crates = reversed_line[0], reversed_line[1:].rstrip()
        if stack_id.isdigit():
            for crate in crates:
                cargo_stacks[stack_id].append(crate)
    return cargo_stacks, instructions


def get_final_state(cargo_stacks, instructions, part="part_1"):
    for line in instructions.splitlines():
        q, id1, id2 = re.findall(r"(\d+)", line)
        selected_crates = [cargo_stacks[id1].pop() for _ in range(int(q))]
        cargo_stacks[id2].extend(
            selected_crates if part == "part_1" else reversed(selected_crates)
        )
    return cargo_stacks


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    cargo_stacks, instructions = parse_input(lines)
    cargo_stacks = get_final_state(cargo_stacks, instructions, "part_1")
    return "".join([s[-1] for s in cargo_stacks.values()])


def part_2(lines):
    cargo_stacks, instructions = parse_input(lines)
    cargo_stacks = get_final_state(cargo_stacks, instructions, "part_2")
    return "".join([s[-1] for s in cargo_stacks.values()])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
