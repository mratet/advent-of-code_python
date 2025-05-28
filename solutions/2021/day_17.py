from aocd import get_data
from itertools import product
import re

input = get_data(day=17, year=2021)


def update_vel_x(vel):
    if vel > 0:
        return vel - 1
    elif vel < 0:
        return vel + 1
    return 0


def solve(lines, part="part_1"):
    x1, x2, y1, y2 = map(int, re.findall(r"(-?\d+)", lines))
    check_target_area = lambda x, y: x1 <= x <= x2 and y1 <= y <= y2

    max_height = 0
    s = 0
    for vel_x, vel_y in product(range(1, 400), range(-100, 400)):
        pos_x, pos_y = 0, 0
        height_list = [pos_y]
        for step in range(200):
            pos_x += vel_x
            pos_y += vel_y
            height_list.append(pos_y)
            vel_x = update_vel_x(vel_x)
            vel_y -= 1
            if check_target_area(pos_x, pos_y):
                max_height = max(max(height_list), max_height)
                s += 1
                break
    return max_height if part == "part_1" else s


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
