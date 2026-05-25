import re
from itertools import product

from aocd import get_data

input = get_data(day=17, year=2021)


# WRITE YOUR SOLUTION HERE
def update_vel_x(vel):
    if vel > 0:
        return vel - 1
    elif vel < 0:
        return vel + 1
    return 0


def solve(lines, part="part_1"):
    x1, x2, y1, y2 = map(int, re.findall(r"(-?\d+)", lines))
    peak = 0
    s = 0
    # vel_x in [1, x2]: beyond x2 overshoots in one step; below 1 never reaches target
    # vel_y in [y1, abs(y1)-1]: below y1 misses in one step; above abs(y1)-1 the probe
    # crosses y=0 downward with speed > abs(y1) and jumps over the target
    for vel_x, vel_y in product(range(1, x2 + 1), range(y1, abs(y1))):
        vx, vy, pos_x, pos_y, curr_peak = vel_x, vel_y, 0, 0, 0
        while True:
            pos_x += vx
            pos_y += vy
            vx = update_vel_x(vx)
            vy -= 1
            curr_peak = max(curr_peak, pos_y)
            if x1 <= pos_x <= x2 and y1 <= pos_y <= y2:
                peak = max(peak, curr_peak)
                s += 1
                break
            if pos_y < y1 or pos_x > x2:
                break
    return peak if part == "part_1" else s


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
