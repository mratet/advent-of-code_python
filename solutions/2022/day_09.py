from itertools import product

from aocd import get_data

input = get_data(day=9, year=2022).splitlines()


def next_step(v1, v2):
    if v1 == v2:
        return 0
    elif v1 > v2:
        return 1
    else:
        return -1


def update_tail_position(head, tail):
    hx, hy = head
    tx, ty = tail
    if max(abs(hx - tx), abs(hy - ty)) <= 1:
        return tail
    stepx = next_step(hx, tx)
    stepy = next_step(hy, ty)
    return tx + stepx, ty + stepy


def move(lines, knots_len):
    knots = [(0, 0)] * knots_len
    visited = {(0, 0)}
    DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for line in lines:
        direction, steps = line.split()
        dx, dy = DIRS[direction]
        for _ in range(int(steps)):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(1, len(knots)):
                knots[i] = update_tail_position(knots[i - 1], knots[i])
            visited.add(knots[-1])
    return len(visited)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return move(lines, 2)


def part_2(lines):
    return move(lines, 10)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
