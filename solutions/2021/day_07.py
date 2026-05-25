from aocd import get_data

input = get_data(day=7, year=2021)


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    return list(map(int, data.split(",")))


def compute_dist(x, y, part="part_1"):
    n = abs(x - y)
    return n if part == "part_1" else n * (n + 1) // 2


def solve(crabs_pos, part="part_1"):
    n = max(crabs_pos)
    return min(sum(compute_dist(x, i, part) for x in crabs_pos) for i in range(n))


def part_1(data):
    return solve(parse_input(data))


def part_2(data):
    return solve(parse_input(data), "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
