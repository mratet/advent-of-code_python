from functools import reduce
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


from aocd import get_data

input = get_data(day=10, year=2025).splitlines()

_STRIP_TABLE = str.maketrans('', '', '[]{}()')

# WRITE YOUR SOLUTION HERE
def parse_input(text):
    machines = []
    for line in text:
        indicator_lights, *button_schematics, voltage_str = line.translate(_STRIP_TABLE).split()

        num_lights = len(indicator_lights)
        target = int(indicator_lights.replace(".", "0").replace("#", "1"), 2)

        raw_buttons = [list(map(int, button.split(","))) for button in button_schematics]
        buttons = [sum(1 << (num_lights - 1 - i) for i in indices) for indices in raw_buttons]
        voltage_str = list(map(int, voltage_str.split(",")))
        machines.append({"num_lights": num_lights, "target": target, "buttons": buttons, "raw_buttons":raw_buttons, "voltage_requirements": voltage_str})
    return machines

def part_1(lines):
    machines = parse_input(lines)
    return sum(
        next(
            len(combo)
            for size in range(machine["num_lights"] + 1)
            for combo in combinations(machine["buttons"], size)
            if reduce(lambda acc, b: acc ^ b, combo, 0) == machine["target"]
    )
        for machine in machines)

def part_2(lines):
    machines = parse_input(lines)
    button_presses = 0
    for machine in machines:
        voltage_requirements, raw_buttons = machine["voltage_requirements"], machine["raw_buttons"]
        n_counters, n_buttons = len(voltage_requirements), len(raw_buttons)

        A = np.zeros((n_counters, n_buttons), dtype=np.float64)
        for b, indices in enumerate(raw_buttons):
            A[indices, b] = 1.0

        res = milp(
            c=np.ones(n_buttons),
            constraints=LinearConstraint(A, lb=voltage_requirements, ub=voltage_requirements),
            integrality=np.ones(n_buttons),
            bounds=Bounds(lb=0)
        )
        button_presses += res.fun
    return int(button_presses)

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")


