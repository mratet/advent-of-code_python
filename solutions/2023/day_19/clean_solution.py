import math
from operator import gt, lt

from aocd import get_data

input = get_data(day=19, year=2023)

# WRITE YOUR SOLUTION HERE

OPERATORS = {"<": lt, ">": gt}


class Conditional:
    def __init__(self, key, op, value, redirect):
        self.key = key
        self.op = OPERATORS[op]
        self.value = value
        self.redirect = redirect

    def apply(self, part):
        return self.op(part[self.key], self.value)

    def split(self, part):
        if self.op is lt:
            true_range = (part[self.key][0], min(part[self.key][1], self.value - 1))
            false_range = (max(self.value, part[self.key][0]), part[self.key][1])
        else:
            false_range = (part[self.key][0], min(part[self.key][1], self.value))
            true_range = (max(self.value + 1, part[self.key][0]), part[self.key][1])
        t_part = dict(part) | {self.key: true_range} if true_range[0] <= true_range[1] else None
        f_part = dict(part) | {self.key: false_range} if false_range[0] <= false_range[1] else None
        return t_part, f_part


class Workflow:
    def __init__(self, description):
        self.name, description = description[:-1].split("{")
        step_data = description.split(",")
        self.steps = []
        for data in step_data[:-1]:
            (key, op, *value), redirect = data.split(":")
            self.steps.append(Conditional(key, op, int("".join(value)), redirect))
        self.redirect = step_data[-1]

    def apply(self, part):
        for step in self.steps:
            if step.apply(part):
                return step.redirect
        return self.redirect

    def count(self, part, workflows):
        total = 0
        for step in self.steps:
            t_part, f_part = step.split(part)
            if t_part is not None:
                total += self.send(t_part, step.redirect, workflows)
            if f_part is not None:
                part = f_part
            else:
                break
        else:
            total += self.send(part, self.redirect, workflows)
        return total

    def send(self, part, redirect, workflows):
        if redirect == "R":
            return 0
        if redirect == "A":
            return math.prod(end - start + 1 for start, end in part.values())
        return workflows[redirect].count(part, workflows)


def is_accepted(part, workflows):
    workflow_id = "in"
    while workflow_id not in {"R", "A"}:
        workflow_id = workflows[workflow_id].apply(part)
    return workflow_id == "A"


def parse_parts(lines):
    return [{k: int(v) for k, v in (seg.split("=") for seg in line[1:-1].split(","))} for line in lines]


def parse_workflows(lines):
    return {wf.name: wf for wf in (Workflow(line) for line in lines)}


def parse_input(data):
    workflows_data, parts_data = data.split("\n\n")
    return parse_workflows(workflows_data.splitlines()), parse_parts(parts_data.splitlines())


def part_1(data):
    workflows, parts = parse_input(data)
    return sum(sum(part.values()) for part in parts if is_accepted(part, workflows))


def part_2(data):
    workflows, _ = parse_input(data)
    start = dict.fromkeys("xmas", (1, 4000))
    return workflows["in"].count(start, workflows)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
