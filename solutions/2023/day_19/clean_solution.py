from aocd import get_data
input = get_data(day=19, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
from operator import lt, gt
OPERATORS = {
    '<': lt,
    '>': gt,
}

class Conditional:
    def __init__(self, key, op, value, redirect):
        self.key = key
        self.op = op
        self.value = value
        self.redirect = redirect

    def apply(self, part):
        return OPERATORS[self.op](part[self.key], self.value)

    def split(self, part):
        if self.op == '<':
            T = (part[self.key][0], min(part[self.key][1], self.value - 1))
            F = (max(self.value, part[self.key][0]), part[self.key][1])
        elif self.op == '>':
            F = (part[self.key][0], min(part[self.key][1], self.value))
            T = (max(self.value + 1, part[self.key][0]), part[self.key][1])
        else:
            assert False

        if T[0] <= T[1]:
            t_part = dict(part)
            t_part[self.key] = T
        else:
            t_part = None

        if F[0] <= F[1]:
            f_part = dict(part)
            f_part[self.key] = F
        else:
            f_part = None

        return (t_part, f_part)

class Workflow:
    def __init__(self, description):
        self.name, description = description[:-1].split('{')
        step_data = description.split(',')
        self.steps = []
        for data in step_data[:-1]:
            (key, op, *value), redirect = data.split(':')
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
        if redirect == 'R':
            return 0
        if redirect == 'A':
            total = 1
            for rs, re in part.values():
                total *= re - rs + 1
            return total
        return workflows[redirect].count(part, workflows)



def isAccepted(part, workflows):
    ID = 'in'

    while ID not in ['R', 'A']:
        wf = workflows[ID]
        ID = wf.apply(part)
    return ID == 'A'

def parseParts(lines):
    parts = []
    for line in lines:
        segments = line[1:-1].split(',')
        parts.append(
            {
                'x': int(segments[0].split('=')[-1]),
                'm': int(segments[1].split('=')[-1]),
                'a': int(segments[2].split('=')[-1]),
                's': int(segments[3].split('=')[-1]),
            }
        )

    return parts

def parseWorkflows(lines):
    workflows = dict()

    for line in lines:
        wf = Workflow(line)
        workflows[wf.name] = wf

    return workflows

def _parse(lines):
    empty_line = lines.index('')

    workflows = parseWorkflows(lines[:empty_line])
    parts = parseParts(lines[empty_line + 1:])

    return workflows, parts
def part_1(input):
    workflows, parts = _parse(input)

    total = 0
    for part in parts:
        if isAccepted(part, workflows):
            total += sum(part.values())

    return total

def part_2(input):
    workflows, _ = _parse(input)
    start = {k: (1, 4000) for k in 'xmas'}
    return workflows['in'].count(start, workflows)
# END OF SOLUTION

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
