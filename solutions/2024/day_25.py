from itertools import product

from aocd import get_data

input = get_data(day=25, year=2024).split("\n\n")


# WRITE YOUR SOLUTION HERE
def part_1(schemas):
    keys, pins = set(), set()
    for schema in schemas:
        grid = list(zip(*schema.splitlines(), strict=False))
        heights = tuple(t.count("#") - 1 for t in grid)
        if grid[0][0] == "#":
            pins.add(heights)
        else:
            keys.add(heights)
    return sum(all(t1 + t2 < 6 for t1, t2 in zip(key, pin, strict=False)) for key, pin in product(keys, pins))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
