from collections import defaultdict

from aocd import get_data

input = get_data(day=18, year=2022).splitlines()


def parse_input(input):
    grid_cubes = []
    for line in input:
        x, y, z = map(int, line.split(","))
        grid_cubes.append((x, y, z))
    return grid_cubes


def get_neighbors_cube(cube):
    x, y, z = cube
    return [
        (x + dx, y + dy, z + dz)
        for dx, dy, dz in (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
        )
    ]


def get_surface_cubes(grid_cubes):
    cubes = defaultdict(int)
    for cube in grid_cubes:
        ncubes = get_neighbors_cube(cube)
        for ncube in ncubes:
            if ncube not in grid_cubes:
                cubes[ncube] += 1
    return cubes


def lambda_is_inside_main_cube(grid_cubes):
    min_x = min(x for x, _, _ in grid_cubes)
    max_x = max(x for x, _, _ in grid_cubes)
    min_y = min(y for _, y, _ in grid_cubes)
    max_y = max(y for _, y, _ in grid_cubes)
    min_z = min(z for _, _, z in grid_cubes)
    max_z = max(z for _, _, z in grid_cubes)
    return (
        lambda x, y, z: min_x <= x <= max_x
        and min_y <= y <= max_y
        and min_z <= z <= max_z
    )


def is_interior_cube(grid_cubes, starting_cube):
    visited = set()
    to_visit = [starting_cube]
    is_inside_main_cube = lambda_is_inside_main_cube(grid_cubes)
    while to_visit:
        cube = to_visit.pop()
        if not is_inside_main_cube(*cube):
            return set()
        if cube in visited:
            continue
        visited.add(cube)
        for ncube in get_neighbors_cube(cube):
            if ncube not in grid_cubes:
                to_visit.append(ncube)
    return visited


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    grid_cubes = parse_input(lines)
    surface_cubes = get_surface_cubes(grid_cubes)
    return sum(surface_cubes.values())


def part_2(lines):
    grid_cubes = parse_input(lines)
    surface_cubes = get_surface_cubes(grid_cubes)
    forbidden_cubes = []
    for cube in surface_cubes:
        if cube in forbidden_cubes:
            continue
        if interior_cubes := is_interior_cube(grid_cubes, cube):
            forbidden_cubes += interior_cubes

    for fcube in forbidden_cubes:
        surface_cubes[fcube] = 0

    return sum(surface_cubes.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
