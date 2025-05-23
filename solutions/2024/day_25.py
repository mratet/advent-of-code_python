from aocd import get_data, submit

input = get_data(day=25, year=2024).split("\n\n")
from itertools import product


def part_1(input):
    keys = set()
    pins = set()

    for schema in input:
        grid = list(zip(*schema.splitlines()))
        if grid[0][0] == "#":  # pins
            pins.add(tuple([t.count("#") - 1 for t in grid]))
        else:  # keys
            keys.add(tuple([t.count("#") - 1 for t in grid]))

    ans = 0
    for key, pin in product(keys, pins):
        ans += all([t1 + t2 < 6 for t1, t2 in zip(key, pin)])
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')
