import itertools

from aocd import get_data

input = get_data(day=11, year=2018)


def compute_power_level(X, Y, grid_serial_number):
    rack_id = X + 10
    power_level = ((rack_id * Y) + grid_serial_number) * rack_id
    return (power_level % 1000) // 100 - 5


def compute_prefix_power_grid(serial_number, grid_size=300):
    grid = {}
    for x, y in itertools.product(range(1, grid_size + 1), repeat=2):
        grid[(x, y)] = compute_power_level(x, y, serial_number)

    # Summed-area table : https://en.wikipedia.org/wiki/Summed-area_table
    for x, y in itertools.product(range(2, grid_size + 1), repeat=2):
        grid[(x, y)] = (
            grid[(x, y)] + grid[(x - 1, y)] + grid[(x, y - 1)] - grid[(x - 1, y - 1)]
        )

    return grid


def find_max_power_square(serial_number, size_range):
    power_grid = compute_prefix_power_grid(serial_number)
    grid_size = 300

    best = (float("-inf"), (0, 0, 0))
    for blk in size_range:
        for x in range(2, grid_size - blk + 1):
            for y in range(2, grid_size - blk + 1):
                total = (
                    power_grid[(x + blk, y + blk)]
                    - power_grid[(x, y + blk)]
                    - power_grid[(x + blk, y)]
                    + power_grid[(x, y)]
                )
                best = max(best, (total, (x + 1, y + 1, blk)))

    return best[1]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    serial_number = int(lines)
    x, y, _ = find_max_power_square(serial_number, size_range=[3])
    return f"{x},{y}"


def part_2(lines):
    serial_number = int(lines)
    x, y, size = find_max_power_square(serial_number, size_range=range(1, 300))
    return f"{x},{y},{size}"


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
