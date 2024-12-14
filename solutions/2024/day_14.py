from aocd import get_data, submit
input = get_data(day=14, year=2024).splitlines()
import re

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    X = 103
    Y = 101
    robots = {}
    for i, line in enumerate(lines):
        # x, y, vx, vy = map(int, re.findall(r'(?:[+\d].*\d|\d))', line))
        pos, v = line.split()
        x, y = pos[2:].split(',')
        x = int(x)
        y = int(y)
        vx, vy = v[2:].split(',')
        vx = int(vx)
        vy = int(vy)
        robots[i] = (y, x, vy, vx)

    for _ in range(100):
        for i, (x, y, vx, vy) in robots.items():
            robots[i] = ((x + vx) % X, (y + vy) % Y, vx, vy)

    quad_count = [0, 0, 0, 0]
    for (x, y, vx, vy) in robots.values():
        if x in range(X//2) and y in range(Y//2):
            quad_count[0] += 1
        elif x in range(X // 2 + 1, X) and y in range(Y // 2):
            quad_count[1] += 1
        elif x in range(X // 2) and y in range(Y // 2 + 1, Y):
            quad_count[2] += 1
        elif x in range(X // 2 + 1, X) and y in range(Y // 2 + 1, Y):
            quad_count[3] += 1

    score = 1
    for c in quad_count:
        score *= c
    return score

def print_grid(X, Y, robots):
    line = ''
    for x in range(X):
        for y in range(Y):
            c = 0
            for (xr, yr, vx, vy) in robots.values():
                if xr == x and yr == y:
                    c += 1
            if c:
                line += str(c)
            else:
                line += '.'
        print(line)
        line = ''
    return

def probable_xmas_tree(curr_pos):
    c = 0
    for (x, y) in curr_pos:
        if  (x - 1, y + 1) in curr_pos and (x +1, y - 1) in curr_pos:
            c += 1
    return c > 30

def part_2(lines):
    X = 103
    Y = 101
    robots = {}
    for i, line in enumerate(lines):
        # x, y, vx, vy = map(int, re.findall(r'(?:[+\d].*\d|\d))', line))
        pos, v = line.split()
        x, y = pos[2:].split(',')
        x = int(x)
        y = int(y)
        vx, vy = v[2:].split(',')
        vx = int(vx)
        vy = int(vy)
        robots[i] = (y, x, vy, vx)

    for j in range(100000):
        curr_pos = set()
        for i, (x, y, vx, vy) in robots.items():
            robots[i] = ((x + vx) % X, (y + vy) % Y, vx, vy)
            (cx, cy, _, _) = robots[i]
            curr_pos.add((cx, cy))
        if probable_xmas_tree(curr_pos):
            print_grid(X, Y, robots)
            return j + 1

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
