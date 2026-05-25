from math import ceil, floor, prod

from aocd import get_data

input = get_data(day=6, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def nb_records(time, distance):
    """
    The total distance is : D = v * (time - t_charge)
    By definition, v = t_charge (= x)
    We're looking for points s.t x * (time - x) - distance >= 0
    In particular, we're computing the distance between both squares-roots
    With a bit of basic algebra, we can show that :
    """
    sqrt_disc = (time**2 - 4 * distance) ** 0.5
    root_low = (time - sqrt_disc) / 2
    root_high = (time + sqrt_disc) / 2
    int_low = ceil(root_low)
    int_high = floor(root_high)
    return int_high - int_low + 1 - int(root_low == int_low) - int(root_high == int_high)


def parse_input(lines, part="part_1"):
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))
    if part == "part_2":
        times = int("".join(map(str, times)))
        distances = int("".join(map(str, distances)))
    return times, distances


def part_1(lines):
    times, distances = parse_input(lines)
    return prod(nb_records(time, distance) for time, distance in zip(times, distances, strict=False))


def part_2(lines):
    time, distance = parse_input(lines, part="part_2")
    return nb_records(time, distance)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
