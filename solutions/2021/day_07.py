from aocd import get_data

input = get_data(day=7, year=2021)


# WRITE YOUR SOLUTION HERE
def compute_dist(x, y, part="part_1"):
    n = abs(x - y)
    return n if part == "part_1" else n * (n + 1) // 2


def solve(crabs_pos, part="part_1"):
    N = max(crabs_pos)
    dist = [sum(compute_dist(x, i, part) for x in crabs_pos) for i in range(N)]
    return min(dist)


def part_1(lines):
    crabs_pos = list(map(int, lines.split(",")))
    return solve(crabs_pos, "part_1")


def part_2(lines):
    crabs_pos = list(map(int, lines.split(",")))
    return solve(crabs_pos, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
