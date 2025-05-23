from aocd import get_data, submit

input = get_data(day=1, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(int(line) // 3 - 2 for line in lines)


def compute_fuel(mass):
    fuel_needed = mass // 3 - 2
    return fuel_needed + compute_fuel(fuel_needed) if fuel_needed > 0 else 0


def part_2(lines):
    return sum(compute_fuel(int(line)) for line in lines)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
