from collections import defaultdict, deque
from math import atan2, pi

from aocd import get_data

aoc_input = get_data(day=10, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def get_asteroids(lines):
    return [(x, y) for y, line in enumerate(lines) for x, symb in enumerate(line) if symb == "#"]


def build_best_asteroid_detection(asteroids):
    max_detection = 0
    astro_visu = None
    base_astro = None

    for xa, ya in asteroids:
        detection_dict = defaultdict(list)
        for x, y in asteroids:
            if (x, y) == (xa, ya):
                continue
            angle = atan2(x - xa, -(y - ya)) % (2 * pi)
            detection_dict[angle].append((x, y))

        if len(detection_dict) > max_detection:
            max_detection = len(detection_dict)
            astro_visu = detection_dict
            base_astro = (xa, ya)

    assert astro_visu is not None and base_astro is not None
    for k in astro_visu:
        astro_visu[k] = deque(
            sorted(astro_visu[k], key=lambda a: abs(a[0] - base_astro[0]) + abs(a[1] - base_astro[1]))
        )

    return astro_visu


def part_1(lines):
    asteroids = get_asteroids(lines)
    astro_visu = build_best_asteroid_detection(asteroids)
    return len(astro_visu)


def part_2(lines):
    asteroids = get_asteroids(lines)
    astro_visu = build_best_asteroid_detection(asteroids)

    destruction_order = sorted(astro_visu)
    i = 0
    while True:
        destruction_order = [k for k in destruction_order if astro_visu[k]]
        for k in destruction_order:
            last_astro = astro_visu[k].popleft()
            i += 1
            if i == 200:
                return last_astro[0] * 100 + last_astro[1]


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
