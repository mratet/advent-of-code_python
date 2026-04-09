import re

from aocd import get_data

input = get_data(day=25, year=2017)

# WRITE YOUR SOLUTION HERE


def parse_turing_machine(text):
    lines = text.strip().splitlines()
    turing_machine = {
        "initial_state": re.findall(r"\w+", lines[0])[-1],
        "checksum_after": int(re.findall(r"\d+", lines[1])[0]),
        "states": {},
    }
    rule = r"value is (\d):\s+- Write the value (\d).\s+- Move one slot to the (\w+).\s+- Continue with state (\w+)."
    for block in text.split("In state ")[1:]:
        turing_machine["states"][block[0]] = {
            int(val): {"write": int(write), "move": 1 if direction == "right" else -1, "next_state": next_state}
            for val, write, direction, next_state in re.findall(rule, block)
        }
    return turing_machine


def part_1(lines):
    turing_machine = parse_turing_machine(lines)
    tape = [0] * 10000
    cursor = len(tape) // 2
    state = turing_machine["initial_state"]
    for _ in range(turing_machine["checksum_after"]):
        action = turing_machine["states"][state][tape[cursor]]
        tape[cursor] = action["write"]
        cursor += action["move"]
        state = action["next_state"]

    return sum(tape)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
