from collections import defaultdict
from math import prod

from aocd import get_data
import re

input = get_data(day=11, year=2022)


def parse_monkey_data(input_text):
    monkey_blocks = input_text.strip().split("\n\n")
    monkeys = {}

    for monkey_id, block in enumerate(monkey_blocks):
        lines = block.strip().splitlines()

        items = list(map(int, re.findall(r"\d+", lines[1])))

        operation_match = re.search(r"Operation: new = old ([*+]) (\w+)", lines[2])
        op_symbol, op_value = operation_match.groups()
        if op_value == "old":
            operation = lambda old, op=op_symbol: old * old if op == "*" else old + old
        else:
            op_value = int(op_value)
            operation = (
                lambda old, op=op_symbol, val=op_value: old * val
                if op == "*"
                else old + val
            )

        divisible_by = int(re.search(r"divisible by (\d+)", lines[3]).group(1))
        true_target = int(
            re.search(r"If true: throw to monkey (\d+)", lines[4]).group(1)
        )
        false_target = int(
            re.search(r"If false: throw to monkey (\d+)", lines[5]).group(1)
        )

        monkeys[monkey_id] = {
            "items": items,
            "operation": operation,
            "divisible_by": divisible_by,
            "true_target": true_target,
            "false_target": false_target,
        }

    return monkeys


def solve(monkeys, part):
    counts = defaultdict(int)
    mod = prod([m["divisible_by"] for m in monkeys.values()])
    rounds = 20 if part == "part_1" else 10000
    for _ in range(rounds):
        for monkey_id, monkey_data in monkeys.items():
            while monkey_data["items"]:
                item = monkey_data["items"].pop(0)
                worry_level = monkey_data["operation"](item)
                if part == "part_1":
                    worry_level //= 3
                next_monkey = (
                    monkey_data["true_target"]
                    if worry_level % monkey_data["divisible_by"] == 0
                    else monkey_data["false_target"]
                )
                monkeys[next_monkey]["items"].append(worry_level % mod)
                counts[monkey_id] += 1
    return counts


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    monkeys = parse_monkey_data(lines)
    counts = solve(monkeys, "part_1")
    return prod(sorted(counts.values())[-2:])


def part_2(lines):
    monkeys = parse_monkey_data(lines)
    counts = solve(monkeys, "part_2")
    return prod(sorted(counts.values())[-2:])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
