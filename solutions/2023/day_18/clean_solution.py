from itertools import pairwise

from aocd import get_data

input = get_data(day=18, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

DIRECTIONS = {"U": N, "D": S, "R": E, "L": W}
HEX_DIRECTIONS = {"0": E, "1": S, "2": W, "3": N}


def shoelace_area(points):
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(points))) // 2


def parse_input(lines, part="part_1"):
    perimeter, points, point = 0, [], (0, 0)
    for line in lines:
        direction, distance, hexa = line.split()
        if part == "part_2":
            direction, distance = HEX_DIRECTIONS[hexa[-2]], int(hexa[2:-2], 16)
        else:
            direction, distance = DIRECTIONS[direction], int(distance)
        point = (point[0] + distance * direction[0], point[1] + distance * direction[1])
        perimeter += distance
        points.append(point)
    return points, perimeter


def solve(lines, part="part_1"):
    points, perimeter = parse_input(lines, part)
    return shoelace_area(points) + perimeter // 2 + 1


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
