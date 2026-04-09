from aocd import get_data

input = get_data(day=4, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(len(word := line.split()) == len(set(word)) for line in lines)


def part_2(lines):
    return sum(len(word := [tuple(sorted(x)) for x in line.split()]) == len(set(word)) for line in lines)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
