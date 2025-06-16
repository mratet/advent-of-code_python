import itertools
from collections import defaultdict

from aocd import get_data
from itertools import cycle, count

WIDE = 7
MAX_HEIGHT_TO_KEEP = 50
SHAPES_RAW = ["####", ".#.\n###\n.#.", "..#\n..#\n###", "#\n#\n#\n#", "##\n##"]

input = get_data(day=17, year=2022)


def parse_shape(shape_str):
    return [
        (x, y)
        for y, row in enumerate(reversed(shape_str.splitlines()))
        for x, char in enumerate(row)
        if char == "#"
    ]


def can_move(shape_coords, occupied, offset):
    for x, y in shape_coords:
        nx, ny = x + offset[0], y + offset[1]
        if nx < 0 or nx >= WIDE or ny < 0 or (nx, ny) in occupied:
            return False
    return True


def place_shape(occupied, shape_coords, offset):
    for x, y in shape_coords:
        occupied.add((x + offset[0], y + offset[1]))


def simulate_with_cycle_detections(jets):
    jet_stream = cycle(enumerate(jets))
    shapes = [parse_shape(s) for s in SHAPES_RAW]
    shape_stream = cycle(enumerate(shapes))

    occupied = set()
    seen = dict()
    height_reached = []
    highest_y = -1

    for rock_num in count():
        shape_idx, shape = next(shape_stream)
        x = 2
        y = highest_y + 4

        while True:
            jet_idx, jet = next(jet_stream)
            dx = 1 if jet == ">" else -1
            if can_move(shape, occupied, (x + dx, y)):
                x += dx

            if can_move(shape, occupied, (x, y - 1)):
                y -= 1
            else:
                place_shape(occupied, shape, (x, y))
                highest_y = max(highest_y, *(y + dy for _, dy in shape))
                height_reached.append(highest_y + 1)

                min_y = highest_y - MAX_HEIGHT_TO_KEEP
                occupied = {(ox, oy) for (ox, oy) in occupied if oy >= min_y}
                break

        normalized_occupied = {(ox, oy - min_y) for (ox, oy) in occupied}
        state_key = (tuple(normalized_occupied), shape_idx, jet_idx)

        if state_key in seen:
            prev_rock_num, prev_height = seen[state_key]
            return {
                "cycle_start": prev_rock_num,
                "cycle_length": rock_num - prev_rock_num,
                "cycle_height_gain": highest_y - prev_height,
                "height_before_cycle": prev_height,
                "height_reached": height_reached,
            }
        seen[state_key] = (rock_num, highest_y)
    return


def extrapolate_height(
    n, cycle_start, cycle_length, cycle_height_gain, height_before_cycle, height_reached
):
    remaining = n - cycle_start
    full_cycles, leftover = divmod(remaining, cycle_length)
    leftover_height = height_reached[cycle_start + leftover - 1] - height_before_cycle
    return height_before_cycle + full_cycles * cycle_height_gain + leftover_height


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    cycle_detected = simulate_with_cycle_detections(lines)
    return extrapolate_height(2022, **cycle_detected)


def part_2(lines):
    cycle_detected = simulate_with_cycle_detections(lines)
    return extrapolate_height(1000000000000, **cycle_detected)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
