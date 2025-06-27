from aocd import get_data
from collections import Counter

input_data = get_data(day=6, year=2018).splitlines()


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_coordinates(lines):
    return [tuple(map(int, line.split(", "))) for line in lines]


def closest_coordinate_index(point, coordinates):
    distances = [manhattan(point, c) for c in coordinates]
    min_dist = min(distances)
    indices = [i for i, d in enumerate(distances) if d == min_dist]
    return indices[0] if len(indices) == 1 else -1


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    coordinates = parse_coordinates(lines)
    grid_size = 1000
    edge_ids = {-1}
    all_tiles = []

    for x in range(grid_size):
        for y in range(grid_size):
            closest_id = closest_coordinate_index((x, y), coordinates)
            if x in {0, grid_size - 1} or y in {0, grid_size - 1}:
                edge_ids.add(closest_id)
            all_tiles.append(closest_id)

    area_counts = Counter(all_tiles)
    return max(
        count for coord_id, count in area_counts.items() if coord_id not in edge_ids
    )


def part_2(lines):
    coordinates = parse_coordinates(lines)
    grid_size = 1000
    max_total_distance = 10000

    return sum(
        sum(manhattan((x, y), c) for c in coordinates) < max_total_distance
        for x in range(grid_size)
        for y in range(grid_size)
    )


print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
