from collections import defaultdict

from aocd import get_data

aoc_input = get_data(day=10, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def get_asteroids(lines):
    asteroids = []
    for y, line in enumerate(lines):
        for x, symb in enumerate(line):
            if symb == "#":
                asteroids.append((x, y))
    return asteroids


def build_best_asteroid_detection(asteroids):
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    max_detection = 0
    for xa, ya in asteroids:
        detection_dict = defaultdict(list)
        for x, y in asteroids:
            if (x, y) == (xa, ya):
                continue
            if x == xa:
                detection_dict[(UP if ya > y else DOWN, 0)].append((x, y))
            else:
                slope = (y - ya) / (x - xa)
                detection_dict[((LEFT if xa > x else RIGHT), slope)].append((x, y))

        if len(detection_dict) > max_detection:
            max_detection = len(detection_dict)
            astro_visu = detection_dict
            base_astro = (x, y)

    for k in astro_visu:
        astro_visu[k].sort(
            key=lambda a: abs(a[0] - base_astro[0]) + abs(a[1] - base_astro[1])
        )

    return astro_visu


def part_1(lines):
    asteroids = get_asteroids(lines)
    astro_visu = build_best_asteroid_detection(asteroids)
    return len(astro_visu)


def part_2(lines):
    asteroids = get_asteroids(lines)
    astro_visu = build_best_asteroid_detection(asteroids)

    i = 0
    destruction_order = sorted(astro_visu)
    while True:
        for k in destruction_order:
            if astro_visu[k]:
                last_astro = astro_visu[k].pop(0)
                i += 1
                if i == 200:
                    return last_astro[0] * 100 + last_astro[1]
            else:
                destruction_order.remove(k)


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
