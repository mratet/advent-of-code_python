from aocd import get_data
import re
from heapq import heappush, heappop

input = get_data(day=23, year=2018).splitlines()


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def parse_input(lines):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


def divide_box(box):
    if box[0] == box[1]: return [box]

    (mx, my, mz), (Mx, My, Mz) = box
    cx = (mx + Mx) // 2
    cy = (my + My) // 2
    cz = (mz + Mz) // 2
    return [
        ((mx, my, mz), (cx, cy, cz)),
        ((cx + 1, my, mz), (Mx, cy, cz)),
        ((mx, cy + 1, mz), (cx, My, cz)),
        ((mx, my, cz + 1), (cx, cy, Mz)),
        ((mx, cy + 1, cz + 1), (cx, My, Mz)),
        ((cx + 1, my, cz + 1), (Mx, cy, Mz)),
        ((cx + 1, cy + 1, mz), (Mx, My, cz)),
        ((cx + 1, cy + 1, cz + 1), (Mx, My, Mz)),
    ]


def get_closest_point(nanobot, box):
    nx, ny, nz = nanobot
    (mx, my, mz), (Mx, My, Mz) = box
    px = max(mx, min(nx, Mx))
    py = max(my, min(ny, My))
    pz = max(mz, min(nz, Mz))
    return (px, py, pz)


def count_intersection(box, nanobots):
    box_score = 0
    for nanobot in nanobots:
        nx, ny, nz, nr = nanobot
        closest_point = get_closest_point((nx, ny, nz), box)
        dist = manhattan_distance(closest_point, nanobot)
        if dist <= nr:
            box_score += 1
    return box_score


def distance_to_origin(box):
    origin = (0, 0, 0)
    ox, oy, oz = get_closest_point(origin, box)
    return abs(ox) + abs(oy) + abs(oz)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    nanobots = parse_input(lines)
    max_nanobot = max(nanobots, key=lambda x: x[3])
    return sum(
        manhattan_distance(max_nanobot, nanobot) <= max_nanobot[3]
        for nanobot in nanobots
    )


def part_2(lines):
    nanobots = parse_input(lines)
    min_coord = min(c for bot in nanobots for c in bot[:3])
    max_coord = max(c for bot in nanobots for c in bot[:3])
    max_abs_coord = max(abs(min_coord), abs(max_coord))

    size = 1
    while size < max_abs_coord:
        size *= 2

    initial_box = ((-size, -size, -size), (size - 1, size - 1, size - 1))
    heap = [(-len(nanobots), 0, initial_box)]

    while True:
        neg_score, dist, box = heappop(heap)
        sub_boxes = divide_box(box)
        if len(sub_boxes) == 1:
            return dist

        for sub_box in sub_boxes:
            box_score = count_intersection(sub_box, nanobots)
            heappush(heap, (-box_score, distance_to_origin(sub_box), sub_box))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
