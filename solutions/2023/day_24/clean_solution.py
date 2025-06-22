from aocd import get_data
import re
from itertools import combinations
import sympy as sp

input = get_data(day=24, year=2023).splitlines()


def _parse(lines):
    return [list(map(int, re.findall(r"-?\d+", line))) for line in lines]


def find_intersection_2d(a1, a2):
    """
    Solve this linear system using Cramer's rule (cf https://en.wikipedia.org/wiki/Cramer%27s_rule):
    - t1 * vx1 + t2 * (-vx2) = px2 - px1
    - t1 * vy1 + t2 * (-vy2) = py2 - py1
    """
    px1, py1, _, vx1, vy1, _ = a1
    px2, py2, _, vx2, vy2, _ = a2

    determinant = lambda a, b, c, d: a * d - b * c
    det = determinant(vx1, -vx2, vy1, -vy2)

    if det == 0:
        return -1, 0, 0
    t1 = determinant(px2 - px1, -vx2, py2 - py1, -vy2) / det
    t2 = determinant(vx1, px2 - px1, vy1, py2 - py1) / det
    return t1, t2, (px1 + t1 * vx1, py1 + t1 * vy1)


def solve_rock(hailstones):
    prx, pry, prz = sp.symbols("prx pry prz")
    vrx, vry, vrz = sp.symbols("vrx vry vrz")
    t1, t2, t3 = sp.symbols("t1 t2 t3")

    eqs = []

    for i, (px, py, pz, vx, vy, vz) in enumerate(hailstones[:3]):
        t = [t1, t2, t3][i]
        eqs.append(prx - px - (vx - vrx) * t)
        eqs.append(pry - py - (vy - vry) * t)
        eqs.append(prz - pz - (vz - vrz) * t)

    sol = sp.solve(eqs, (prx, pry, prz, vrx, vry, vrz, t1, t2, t3), dict=True)[0]
    return sol[prx], sol[pry], sol[prz]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    asteroids = _parse(lines)

    ans = 0
    min_val = 200000000000000
    max_val = 400000000000000

    for a1, a2 in combinations(asteroids, 2):
        t1, t2, intersection = find_intersection_2d(a1, a2)
        if (
            t1 >= 0
            and t2 >= 0
            and min_val <= intersection[0] <= max_val
            and min_val <= intersection[1] <= max_val
        ):
            ans += 1
    return ans


def part_2(lines):
    asteroids = _parse(lines)
    pos = solve_rock(asteroids)
    return sum(pos)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
