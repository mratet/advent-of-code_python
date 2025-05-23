from collections import defaultdict

from aocd import get_data

input = get_data(day=8, year=2017).splitlines()
# WRITE YOUR SOLUTION HERE


def cpu_simulation(lines):
    D = defaultdict(int)
    highest_val = 0
    for line in lines:
        var, op, val, _, cond_var, cond_op, cond_val = line.split()
        if eval(str(D[cond_var]) + cond_op + cond_val):
            if op == "inc":
                D[var] += int(val)
            elif op == "dec":
                D[var] -= int(val)
        if D[var] > highest_val:
            highest_val = D[var]
    return max(D.values()), highest_val


def part_1(lines):
    last_temp, _ = cpu_simulation(lines)
    return last_temp


def part_2(lines):
    _, max_temp = cpu_simulation(lines)
    return max_temp


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
