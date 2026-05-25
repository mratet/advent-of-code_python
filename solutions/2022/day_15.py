import re

from aocd import get_data

input = get_data(day=15, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_input(lines):
    sensors = []
    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        s = (sx, sy)
        b = (bx, by)
        sensors.append((s, manhattan_distance(s, b)))
    return sensors


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged_intervals = [intervals[0]]
    for start, end in intervals[1:]:
        _prev_start, prev_end = merged_intervals[-1]
        if start <= prev_end + 1:
            merged_intervals[-1][1] = max(prev_end, end)
        else:
            merged_intervals.append([start, end])
    return merged_intervals


def get_coverage_intervals(y, sensors):
    intervals = []
    for (sx, sy), dist in sensors:
        vertical_dist = abs(sy - y)
        if vertical_dist > dist:
            continue
        horizontal_range = dist - vertical_dist
        intervals.append([sx - horizontal_range, sx + horizontal_range])
    return merge_intervals(intervals)


def solve(lines, part="part_1"):
    sensors = parse_input(lines)
    if part == "part_1":
        [[x, y]] = get_coverage_intervals(2_000_000, sensors)
        return y - x
    max_y = 4_000_000
    # The uncovered point lies at the intersection of neighboring sensor boundaries.
    # In rotated coordinates u=x+y, v=x-y, each boundary is a line u=c or v=c.
    # Generate O(n) candidate u and v values, then check their O(n²) intersections.
    u_candidates = {sx + sy + sign * (d + 1) for (sx, sy), d in sensors for sign in (1, -1)}
    v_candidates = {sx - sy + sign * (d + 1) for (sx, sy), d in sensors for sign in (1, -1)}
    for u in u_candidates:
        for v in v_candidates:
            if (u + v) % 2 != 0:
                continue
            x, y = (u + v) // 2, (u - v) // 2
            if 0 <= x <= max_y and 0 <= y <= max_y and all(manhattan_distance((x, y), s) > d for s, d in sensors):
                return x * max_y + y


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
