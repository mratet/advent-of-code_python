from aocd import get_data
import re

input = get_data(day=15, year=2022).splitlines()


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
        prev_start, prev_end = merged_intervals[-1]
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


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    y_target = 2_000_000
    sensors = parse_input(lines)
    [[x, y]] = get_coverage_intervals(y_target, sensors)
    return y - x


def part_2(lines):
    MAX_Y = 4_000_000
    sensors = parse_input(lines)

    for y in range(MAX_Y + 1):
        intervals = get_coverage_intervals(y, sensors)

        if len(intervals) > 1:
            x_gap = intervals[0][1] + 1
            return x_gap * MAX_Y + y

    raise Exception("No solution")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
