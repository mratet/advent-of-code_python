from aocd import get_data

input = get_data(day=14, year=2022).splitlines()


def parse_input(lines):
    rocks = set()
    for line in lines:
        points = [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 == x2:  # Vertical segment
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x1, y))
            elif y1 == y2:  # Horizontal segment
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.add((x, y1))
    return rocks


def get_next_step(sand, rocks, sands):
    x, y = sand
    for dx in (0, -1, 1):  # Down, down-left, down-right
        nx, ny = x + dx, y + 1
        if (nx, ny) not in rocks and (nx, ny) not in sands:
            return (nx, ny)
    return sand  # No movement possible


def simulate_sand(rocks, abyss_limit=None):
    sands = set()
    source = (500, 0)

    while True:
        sand = source
        while True:
            next_sand = get_next_step(sand, rocks, sands)
            if abyss_limit and next_sand[1] > abyss_limit:
                return len(sands)
            if next_sand == sand:
                break
            sand = next_sand

        if sand == source:
            return len(sands) + 1  # Include the last settled grain
        sands.add(sand)


def part_1(lines):
    rocks = parse_input(lines)
    abyss_y = max(y for _, y in rocks)
    return simulate_sand(rocks, abyss_limit=abyss_y)


def part_2(lines):
    rocks = parse_input(lines)
    floor_y = max(y for _, y in rocks) + 2
    # Add the infinite floor
    for x in range(500 - floor_y - 1, 500 + floor_y + 1):
        rocks.add((x, floor_y))
    return simulate_sand(rocks)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
