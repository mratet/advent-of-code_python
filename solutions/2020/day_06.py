from aocd import get_data

input = get_data(day=6, year=2020).split("\n\n")


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(len(set(line.replace("\n", ""))) for line in lines)


def part_2(lines):
    return sum(len(set.intersection(*map(set, line.split()))) for line in lines)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
