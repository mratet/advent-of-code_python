from aocd import get_data, submit

input = get_data(day=14, year=2024).splitlines()
import re


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    X = 103
    Y = 101
    tl = tr = bl = br = 0
    for i, line in enumerate(lines):
        y, x, vy, vx = map(int, re.findall(r"-?\d+", line))
        px, py = (x + 100 * vx) % X, (y + 100 * vy) % Y

        if px in range(X // 2) and py in range(Y // 2):
            tl += 1
        elif px in range(X // 2 + 1, X) and py in range(Y // 2):
            bl += 1
        elif px in range(X // 2) and py in range(Y // 2 + 1, Y):
            tr += 1
        elif px in range(X // 2 + 1, X) and py in range(Y // 2 + 1, Y):
            br += 1
    return tl * bl * tr * br


def print_grid(X, Y, curr_pos):
    line = ""
    for x in range(X):
        for y in range(Y):
            line += "1" if (x, y) in curr_pos else "."
        print(line)
        line = ""
    return


def probable_xmas_tree(curr_pos):
    c = 0
    for x, y in curr_pos:
        if (x - 1, y + 1) in curr_pos and (x + 1, y - 1) in curr_pos:
            c += 1
    return c > 30


def part_2(lines):
    X = 103
    Y = 101
    robots = {}
    for i, line in enumerate(lines):
        y, x, vy, vx = map(int, re.findall(r"-?\d+", line))
        robots[i] = (x, y, vx, vy)

    for j in range(100000):
        curr_pos = set()
        for i, (x, y, vx, vy) in robots.items():
            robots[i] = ((x + vx) % X, (y + vy) % Y, vx, vy)
            (cx, cy, _, _) = robots[i]
            curr_pos.add((cx, cy))
        if probable_xmas_tree(curr_pos):
            # print_grid(X, Y, curr_pos)
            return j + 1


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
