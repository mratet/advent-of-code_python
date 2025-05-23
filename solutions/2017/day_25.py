from aocd import get_data, submit

input = get_data(day=25, year=2017)
import re
# WRITE YOUR SOLUTION HERE


def parse_turing_machine(input_text):
    ### LLM parsing

    turing_machine = {"states": {}}
    lines = input_text.strip().splitlines()
    turing_machine["initial_state"] = re.search(r"state (\w+)", lines[0]).group(1)
    turing_machine["checksum_after"] = int(re.search(r"(\d+)", lines[1]).group(1))

    state = None
    for line in lines[2:]:
        line = line.strip()

        if line.startswith("In state"):
            state = re.search(r"In state (\w+):", line).group(1)
            turing_machine["states"][state] = {}

        elif line.startswith("If the current value is"):
            current_value = int(
                re.search(r"If the current value is (\d):", line).group(1)
            )
            turing_machine["states"][state][current_value] = {}

        elif line.startswith("- Write the value"):
            write_value = int(re.search(r"- Write the value (\d).", line).group(1))
            turing_machine["states"][state][current_value]["write"] = write_value

        elif line.startswith("- Move one slot to the"):
            move_direction = re.search(r"- Move one slot to the (\w+).", line).group(1)
            move = 1 if move_direction == "right" else -1
            turing_machine["states"][state][current_value]["move"] = move

        elif line.startswith("- Continue with state"):
            next_state = re.search(r"- Continue with state (\w+).", line).group(1)
            turing_machine["states"][state][current_value]["next_state"] = next_state

    return turing_machine


def part_1(lines):
    turing_machine = parse_turing_machine(lines)
    tape = [0] * 100000
    cursor = len(tape) // 2
    state = turing_machine["initial_state"]
    for _ in range(turing_machine["checksum_after"]):
        action = turing_machine["states"][state][tape[cursor]]
        tape[cursor] = action["write"]
        cursor += action["move"]
        state = action["next_state"]

    return sum(tape)


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
