import re
from itertools import combinations

import sympy as sp
from aocd import get_data

input = get_data(day=24, year=2023).splitlines()

MIN_VAL = 200000000000000
MAX_VAL = 400000000000000

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    return [list(map(int, re.findall(r"-?\d+", line))) for line in lines]


def find_intersection_2d(a1, a2):
    # Cramer's rule
    px1, py1, _, vx1, vy1, _ = a1
    px2, py2, _, vx2, vy2, _ = a2
    det = vx2 * vy1 - vx1 * vy2
    if det == 0:
        return -1, 0, (0, 0)
    dx, dy = px2 - px1, py2 - py1
    t1 = (vx2 * dy - vy2 * dx) / det
    t2 = (vx1 * dy - vy1 * dx) / det
    return t1, t2, (px1 + t1 * vx1, py1 + t1 * vy1)


def solve_rock(hailstones):
    prx, pry, prz, vrx, vry, vrz = sp.symbols("prx pry prz vrx vry vrz")
    t_syms = sp.symbols("t1 t2 t3")
    eqs = []
    for (px, py, pz, vx, vy, vz), t in zip(hailstones[:3], t_syms, strict=False):
        eqs += [
            prx - px - (vx - vrx) * t,
            pry - py - (vy - vry) * t,
            prz - pz - (vz - vrz) * t,
        ]
    sol = sp.solve(eqs, (prx, pry, prz, vrx, vry, vrz, *t_syms), dict=True)[0]
    return sol[prx], sol[pry], sol[prz]


def part_1(lines):
    hailstones = parse_input(lines)
    count = 0
    for a1, a2 in combinations(hailstones, 2):
        t1, t2, (x, y) = find_intersection_2d(a1, a2)
        if t1 >= 0 and t2 >= 0 and MIN_VAL <= x <= MAX_VAL and MIN_VAL <= y <= MAX_VAL:
            count += 1
    return count


def part_2(lines):
    hailstones = parse_input(lines)
    return sum(solve_rock(hailstones))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
