from itertools import count

from aocd import get_data

input = get_data(day=13, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def get_security_scanner(lines):
    return [tuple(map(int, line.split(": "))) for line in lines]


def part_1(lines):
    firewall = get_security_scanner(lines)
    return sum(depth * range for depth, range in firewall if depth % (2 * (range - 1)) == 0)


def part_2(lines):
    firewall = get_security_scanner(lines)
    return next(
        delay for delay in count(0) if all((delay + depth) % (2 * (range - 1)) != 0 for depth, range in firewall)
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
