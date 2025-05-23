from aocd import get_data

input = get_data(day=6, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
from math import ceil, floor, prod


def nb_records(time, distance):
    """
    The total distance is : D = v * (time - t_charge)
    By definition, v = t_charge (= x)
    We're looking for points s.t x * (time - x) - distance >= 0
    In particular, we're computing the distance between both squares-roots
    With a bit of basic algebra, we can show that :
    """
    y = (time**2 - 4 * distance) ** 0.5
    x_1 = (time - y) / 2
    x_2 = (time + y) / 2
    X_1 = ceil(x_1)
    X_2 = floor(x_2)

    return X_2 - X_1 + 1 - int(x_1 == X_1) - int(x_2 == X_2)


def _parse(input, part):
    times, distances = None, None
    match part:
        case "part_1":
            times = list(map(int, input[0].split(":")[1].split()))
            distances = list(map(int, input[1].split(":")[1].split()))
        case "part_2":
            times = int(input[0].split(":")[1].replace(" ", ""))
            distances = int(input[1].split(":")[1].replace(" ", ""))
    return times, distances


def part_1(input):
    times, distances = _parse(input, "part_1")
    return prod(
        [nb_records(time, distance) for time, distance in zip(times, distances)]
    )


def part_2(lines):
    time, distance = _parse(input, "part_2")
    return nb_records(time, distance)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
