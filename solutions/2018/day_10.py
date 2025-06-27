from aocd import get_data
import re

input = get_data(day=10, year=2018).splitlines()


def parse_input(lines):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


def compute_area(points):
    xs, ys = zip(*points)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    area = (max_x - min_x) * (max_y - min_y)
    return area


def render_ascii(points):
    xs, ys = zip(*points)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [["." for _ in range(width)] for _ in range(height)]

    for x, y in points:
        gx = x - min_x
        gy = y - min_y
        grid[gy][gx] = "#"

    for row in grid:
        print("".join(row))


def compute_positions(points, time):
    return [(px + time * vx, py + time * vy) for px, py, vx, vy in points]


def find_message_time(points, max_seconds=15000):
    best_time = 0
    smallest_area = float("inf")
    best_positions = []

    for t in range(max_seconds):
        positions = compute_positions(points, t)
        area = compute_area(positions)
        if area < smallest_area:
            smallest_area = area
            best_positions = positions
            best_time = t

    return best_positions, best_time


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    points = parse_input(lines)
    sky, _ = find_message_time(points)
    render_ascii(sky)
    return None


def part_2(lines):
    points = parse_input(lines)
    _, seconds = find_message_time(points)
    return seconds


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
