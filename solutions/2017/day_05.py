from aocd import get_data

input = get_data(day=5, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def solve(lines, part):
    i, count = 0, 0
    inst = [int(n) for n in lines]
    while i < len(inst):
        offset = inst[i]
        inst[i] += 1 if (part == "part_1" or offset < 3) else -1
        i += offset
        count += 1
    return count


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
