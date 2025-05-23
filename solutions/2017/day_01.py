from aocd import get_data

input = get_data(day=1, year=2017)


# WRITE YOUR SOLUTION HERE
def find_matches(input, next):
    return sum(
        [int(n) for i, n in enumerate(input) if n == input[(i + next) % len(input)]]
    )


def part_1(lines):
    return find_matches(lines, 1)


def part_2(lines):
    return find_matches(lines, len(lines) // 2)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
