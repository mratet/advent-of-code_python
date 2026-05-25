from math import prod

from aocd import get_data

input = get_data(day=13, year=2020).splitlines()


def crt(nm, am):
    total = prod(nm)
    result = sum(a_i * (prod_i := total // n_i) * pow(prod_i, -1, n_i) for n_i, a_i in zip(nm, am, strict=False))
    return result % total


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    timestamp = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]
    waiting_time, bus_id = min((bus - timestamp % bus, bus) for bus in buses)
    return waiting_time * bus_id


def part_2(lines):
    pairs = [(int(bus), -i) for i, bus in enumerate(lines[1].split(",")) if bus != "x"]
    nm, am = zip(*pairs, strict=False)
    return crt(nm, am)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
