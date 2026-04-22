from collections import Counter

from aocd import get_data

MAX_TOTAL_DISTANCE = 10000

input_data = get_data(day=6, year=2018).splitlines()


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_coordinates(lines):
    return [tuple(map(int, line.split(", "))) for line in lines]


def closest_coordinate_index(point, coordinates):
    distances = [manhattan_distance(point, c) for c in coordinates]
    min_dist = min(distances)
    return distances.index(min_dist) if distances.count(min_dist) == 1 else -1


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    coordinates = parse_coordinates(lines)
    max_x = max(x for x, _ in coordinates)
    max_y = max(y for _, y in coordinates)
    edge_ids = {-1}
    all_tiles = []

    for x in range(max_x):
        for y in range(max_y):
            closest_id = closest_coordinate_index((x, y), coordinates)
            if x in {0, max_x - 1} or y in {0, max_y - 1}:
                edge_ids.add(closest_id)
            all_tiles.append(closest_id)

    area_counts = Counter(all_tiles)
    return max(count for coord_id, count in area_counts.items() if coord_id not in edge_ids)


def part_2(lines):
    coordinates = parse_coordinates(lines)
    max_x = max(x for x, _ in coordinates)
    max_y = max(y for _, y in coordinates)
    return sum(
        sum(manhattan_distance((x, y), c) for c in coordinates) < MAX_TOTAL_DISTANCE
        for x in range(max_x)
        for y in range(max_y)
    )


print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
