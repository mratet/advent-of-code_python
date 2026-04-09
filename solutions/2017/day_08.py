import operator
from collections import defaultdict

from aocd import get_data

input = get_data(day=8, year=2017).splitlines()
# WRITE YOUR SOLUTION HERE
OPS = {"<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge, "==": operator.eq, "!=": operator.ne}


def cpu_simulation(lines):
    regs = defaultdict(int)
    highest = 0
    for line in lines:
        var, op, val, _, cond_var, cond_op, cond_val = line.split()
        if OPS[cond_op](regs[cond_var], int(cond_val)):
            regs[var] += int(val) if op == "inc" else -int(val)
            highest = max(regs[var], highest)
    return max(regs.values()), highest


def part_1(lines):
    last_temp, _ = cpu_simulation(lines)
    return last_temp


def part_2(lines):
    _, max_temp = cpu_simulation(lines)
    return max_temp


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
