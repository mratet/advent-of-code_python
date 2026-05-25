import re

from aocd import get_data

input = get_data(day=14, year=2024).splitlines()

X = 103
Y = 101


# WRITE YOUR SOLUTION HERE
def probable_xmas_tree(curr_pos):
    c = 0
    for x, y in curr_pos:
        if (x - 1, y + 1) in curr_pos and (x + 1, y - 1) in curr_pos:
            c += 1
    return c > 30


def part_1(lines):
    tl = tr = bl = br = 0
    for line in lines:
        y, x, vy, vx = map(int, re.findall(r"-?\d+", line))
        px, py = (x + 100 * vx) % X, (y + 100 * vy) % Y
        if px < X // 2 and py < Y // 2:
            tl += 1
        elif px > X // 2 and py < Y // 2:
            bl += 1
        elif px < X // 2 and py > Y // 2:
            tr += 1
        elif px > X // 2 and py > Y // 2:
            br += 1
    return tl * bl * tr * br


def part_2(lines):
    robots = {}
    for i, line in enumerate(lines):
        y, x, vy, vx = map(int, re.findall(r"-?\d+", line))
        robots[i] = (x, y, vx, vy)
    for j in range(X * Y):
        curr_pos = set()
        for i, (x, y, vx, vy) in robots.items():
            nx, ny = (x + vx) % X, (y + vy) % Y
            robots[i] = (nx, ny, vx, vy)
            curr_pos.add((nx, ny))
        if probable_xmas_tree(curr_pos):
            return j + 1


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
