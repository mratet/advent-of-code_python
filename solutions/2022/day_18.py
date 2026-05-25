from collections import defaultdict

from aocd import get_data

input = get_data(day=18, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


def get_neighbors(cube):
    x, y, z = cube
    return [
        (x + dx, y + dy, z + dz) for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    ]


def get_surface_cubes(cubes):
    grid = defaultdict(int)
    cube_set = set(cubes)
    for cube in cubes:
        for ncube in get_neighbors(cube):
            if ncube not in cube_set:
                grid[ncube] += 1
    return grid


def get_bounds(cubes):
    xs, ys, zs = zip(*cubes, strict=False)
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def is_interior_cube(cube_set, starting_cube, bounds):
    min_x, max_x, min_y, max_y, min_z, max_z = bounds
    visited = set()
    to_visit = [starting_cube]
    while to_visit:
        cube = to_visit.pop()
        x, y, z = cube
        if not (min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z):
            return set()
        if cube in visited:
            continue
        visited.add(cube)
        for ncube in get_neighbors(cube):
            if ncube not in cube_set:
                to_visit.append(ncube)
    return visited


def solve(lines, part="part_1"):
    cubes = parse_input(lines)
    surface_cubes = get_surface_cubes(cubes)
    if part == "part_1":
        return sum(surface_cubes.values())
    cube_set = set(cubes)
    bounds = get_bounds(cubes)
    forbidden = set()
    for cube in surface_cubes:
        if cube in forbidden:
            continue
        if interior := is_interior_cube(cube_set, cube, bounds):
            forbidden |= interior
    for fcube in forbidden:
        surface_cubes[fcube] = 0
    return sum(surface_cubes.values())


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
