import re
from collections import defaultdict
from math import prod

from aocd import get_data

input = get_data(day=11, year=2022)


# WRITE YOUR SOLUTION HERE
def parse_monkey_data(text):
    monkeys = {}
    for monkey_id, block in enumerate(text.strip().split("\n\n")):
        lines = block.strip().splitlines()
        items = list(map(int, re.findall(r"\d+", lines[1])))
        op_symbol, op_value = re.findall(r"([*+]) (\w+)", lines[2])[0]
        if op_value == "old":
            operation = lambda old, op=op_symbol: old * old if op == "*" else old + old
        else:
            op_value = int(op_value)
            operation = lambda old, op=op_symbol, val=op_value: old * val if op == "*" else old + val
        divisible_by = int(re.findall(r"\d+", lines[3])[0])
        true_target = int(re.findall(r"\d+", lines[4])[0])
        false_target = int(re.findall(r"\d+", lines[5])[0])
        monkeys[monkey_id] = {
            "items": items,
            "operation": operation,
            "divisible_by": divisible_by,
            "true_target": true_target,
            "false_target": false_target,
        }
    return monkeys


def solve(text, part="part_1"):
    monkeys = parse_monkey_data(text)
    counts = defaultdict(int)
    mod = prod(m["divisible_by"] for m in monkeys.values())
    rounds = 20 if part == "part_1" else 10000
    for _ in range(rounds):
        for monkey_id, monkey in monkeys.items():
            while monkey["items"]:
                item = monkey["items"].pop(0)
                worry = monkey["operation"](item)
                if part == "part_1":
                    worry //= 3
                target = monkey["true_target"] if worry % monkey["divisible_by"] == 0 else monkey["false_target"]
                monkeys[target]["items"].append(worry % mod)
                counts[monkey_id] += 1
    return prod(sorted(counts.values())[-2:])


def part_1(text):
    return solve(text)


def part_2(text):
    return solve(text, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
